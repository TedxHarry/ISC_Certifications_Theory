"""Offline-only checks. All records and tokens here are synthetic test values."""
import copy
import importlib
import contextlib
import io
import json
import tempfile
import unittest
from unittest.mock import patch
from email.utils import formatdate
from pathlib import Path
from urllib.parse import parse_qs, urlsplit
from urllib.request import Request

import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools"))
m = importlib.import_module("collect_certification_evidence")


def config():
    return {
        "api_base_url": "https://offline-test.api.identitynow.com",
        "campaign_id": "offline-campaign",
        "campaign_name": "certlab-cls004-context-run01",
        "caller_view": "admin",
        "certification_ids": ["offline-cert-a"],
        "reviewer_id": "offline-reviewer",
        "source_id": "offline-source",
        "entitlement_id": "offline-entitlement",
        "attribute_name": "groups",
        "entitlement_value": "certlab-report-export",
        "expected_items": [
            {"identity_id": "offline-person-a", "account_id": "offline-account-a",
             "decision": "APPROVED"},
            {"identity_id": "offline-person-b", "account_id": "offline-account-b",
             "decision": "REVOKED"},
        ],
    }


def certificate(cid="offline-cert-a", count=2):
    return {"id": cid, "campaignRef": {"id": "offline-campaign", "type": "IDENTITY"},
            "reviewer": {"id": "offline-reviewer", "type": "IDENTITY"},
            "phase": "SIGNED", "reviewProgress": "SIGNED", "completed": True,
            "dateSigned": "2026-01-01T00:00:00Z", "modified": "2026-01-01T00:00:00Z",
            "decisionsMade": count, "decisionsTotal": count}


def item(suffix, decision):
    return {"id": "offline-item-" + suffix, "type": "ENTITLEMENT", "completed": True,
            "decision": decision, "comments": "Synthetic offline review reason",
            "certificationSubjectSummary": {"id": "offline-summary-" + suffix,
                "subjectType": "IDENTITY", "subjectTargetId": "offline-person-" + suffix},
            "reviewData": {"entitlement": {"id": "offline-entitlement",
                "sourceId": "offline-source", "attributeName": "groups",
                "attributeValue": "certlab-report-export",
                "account": {"id": "offline-account-" + suffix,
                            "nativeIdentity": "offline-account-" + suffix}}}}


def summary(items):
    return {"entitlementDecisions": {"approved": sum(x["decision"] == "APPROVED" for x in items),
            "revoked": sum(x["decision"] == "REVOKED" for x in items), "acknowledged": 0,
            "decisionsMade": len(items), "decisionsTotal": len(items)}}


def response(status=200, payload=None, headers=None):
    h = {"content-type": "application/json", **(headers or {})}
    return m.Response(status, h, json.dumps(payload).encode("utf-8"))


class FakeTransport:
    def __init__(self, split=False):
        self.campaign = {"id": "offline-campaign", "name": "certlab-cls004-context-run01",
                         "type": "IDENTITY", "status": "COMPLETED"}
        self.items = {"offline-cert-a": [item("a", "APPROVED"), item("b", "REVOKED")]}
        if split:
            self.items = {"offline-cert-a": [item("a", "APPROVED")],
                          "offline-cert-b": [item("b", "REVOKED")]}
        self.certificates = {cid: certificate(cid, len(items)) for cid, items in self.items.items()}
        self.calls = []
        self.override = None

    def send(self, url, headers, timeout):
        parsed = urlsplit(url)
        path, q = parsed.path, parse_qs(parsed.query)
        self.calls.append((url, dict(headers), timeout))
        if self.override:
            altered = self.override(path, q, len(self.calls))
            if altered is not None:
                return altered
        prefix = "/certification-campaigns/v1"
        if path == prefix + "/campaigns/offline-campaign":
            return response(payload=copy.deepcopy(self.campaign))
        if path == prefix + "/certifications":
            records = list(self.certificates.values())
            return self.page(records, q)
        for cid, cert in self.certificates.items():
            base = prefix + "/certifications/" + cid
            if path == base:
                return response(payload=copy.deepcopy(cert))
            if path == base + "/review-items":
                return self.page(self.items[cid], q)
            if path == base + "/decision-summary":
                return response(payload=summary(self.items[cid]))
        return response(404)

    @staticmethod
    def page(records, query):
        start, limit = int(query["offset"][0]), int(query["limit"][0])
        return response(payload=copy.deepcopy(records[start:start + limit]),
                        headers={"x-total-count": str(len(records))})


class Clock:
    def __init__(self):
        self.now = 0
        self.waits = []
    def __call__(self):
        return self.now
    def sleep(self, seconds):
        self.waits.append(seconds)
        self.now += seconds


class CollectorChecks(unittest.TestCase):
    def run_capture(self, fake=None, cfg=None, token="OFFLINE_TOKEN", change=None):
        fake = fake or FakeTransport()
        if change:
            change(fake)
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        root = Path(tmp.name)
        out = root / "private" / "capture"
        clock = Clock()
        result = m.collect(cfg or config(), out, token, transport=fake,
                           clock=clock, sleep=clock.sleep, root=root)
        return result, fake, out, clock

    def test_complete_grouped_capture_reads_empty_terminal_pages(self):
        result, fake, out, _ = self.run_capture()
        self.assertEqual(result["outcome"], "CAPTURE_CHECKS_PASSED", result)
        self.assertEqual(result["mode"], "OFFLINE_TEST")
        self.assertTrue(result["manual_comparison_required"])
        self.assertFalse(result["fulfillment_verified"])
        self.assertEqual(result["item_count"], 2)
        pages = [parse_qs(urlsplit(c[0]).query) for c in fake.calls
                 if urlsplit(c[0]).path.endswith("/review-items")]
        self.assertEqual([p["offset"][0] for p in pages], ["0", "1", "2"])
        self.assertTrue((out / "run.json").exists())
        self.assertTrue(all(c[2] <= 15 for c in fake.calls))

    def test_split_certifications_restart_child_offsets(self):
        cfg = config()
        cfg["certification_ids"].append("offline-cert-b")
        result, fake, _, _ = self.run_capture(FakeTransport(split=True), cfg)
        self.assertEqual(result["outcome"], "CAPTURE_CHECKS_PASSED", result)
        for cid in cfg["certification_ids"]:
            offsets = [parse_qs(urlsplit(x[0]).query)["offset"][0] for x in fake.calls
                       if urlsplit(x[0]).path.endswith(cid + "/review-items")]
            self.assertEqual(offsets, ["0", "1"])

    def test_reviewer_query_is_narrow_and_encoded_once(self):
        cfg = config()
        cfg["caller_view"] = "reviewer"
        result, fake, _, _ = self.run_capture(cfg=cfg)
        self.assertEqual(result["outcome"], "CAPTURE_CHECKS_PASSED", result)
        for url, _, _ in fake.calls:
            if urlsplit(url).path.endswith("/certifications"):
                q = parse_qs(urlsplit(url).query)
                self.assertEqual(q["filters"], ['campaignRef.id eq "offline-campaign"'])
                self.assertEqual(q["reviewer-identity"], ["me"])

    def test_unexpected_parent_is_not_followed(self):
        def change(fake):
            fake.certificates["offline-cert-a"]["campaignRef"]["id"] = "offline-other"
        result, fake, _, _ = self.run_capture(change=change)
        self.assertEqual(result["outcome"], "INCOMPLETE")
        self.assertFalse(any("/review-items" in c[0] for c in fake.calls))

    def test_pinned_certification_set_prevents_partial_visibility_pass(self):
        cfg = config()
        cfg["certification_ids"].append("offline-unseen")
        result, _, _, _ = self.run_capture(cfg=cfg)
        self.assertEqual(result["outcome"], "INCOMPLETE")

    def test_unsigned_completed_true_is_not_signed(self):
        def change(fake):
            fake.certificates["offline-cert-a"].update(
                phase="ACTIVE", reviewProgress="DECISIONS_COMPLETE")
            fake.certificates["offline-cert-a"].pop("dateSigned")
        result, _, _, _ = self.run_capture(change=change)
        self.assertEqual(result["outcome"], "INCOMPLETE")

    def test_wrong_source_account_target_or_decision_fails_exact_scope(self):
        mutations = [
            lambda x: x["reviewData"]["entitlement"].update(sourceId="offline-wrong"),
            lambda x: x["reviewData"]["entitlement"]["account"].update(id="offline-wrong"),
            lambda x: x["certificationSubjectSummary"].update(subjectTargetId="offline-wrong"),
            lambda x: x.update(decision="APPROVED"),
        ]
        for mutate in mutations:
            with self.subTest(mutate=mutate):
                def change(fake):
                    mutate(fake.items["offline-cert-a"][1])
                result, _, _, _ = self.run_capture(change=change)
                self.assertEqual(result["outcome"], "INCOMPLETE")

    def test_duplicate_or_early_empty_page_is_incomplete(self):
        for duplicate in [True, False]:
            fake = FakeTransport()
            def override(path, q, _):
                if path.endswith("/review-items") and q["offset"] == ["1"]:
                    return response(payload=[item("a", "APPROVED")] if duplicate else [],
                                    headers={"x-total-count": "2"})
            fake.override = override
            result, _, _, _ = self.run_capture(fake)
            self.assertEqual(result["outcome"], "INCOMPLETE")

    def test_missing_or_changing_total_is_incomplete(self):
        for total in [None, "3", "not-a-count"]:
            fake = FakeTransport()
            def override(path, q, _):
                if path.endswith("/review-items") and q["offset"] == ["1"]:
                    h = {} if total is None else {"x-total-count": total}
                    return response(payload=[item("b", "REVOKED")], headers=h)
            fake.override = override
            result, _, _, _ = self.run_capture(fake)
            self.assertEqual(result["outcome"], "INCOMPLETE")

    def test_summary_mismatch_and_changed_final_record_fail(self):
        for kind in ["summary", "changed"]:
            fake = FakeTransport()
            count = 0
            def override(path, q, _):
                nonlocal count
                if kind == "summary" and path.endswith("/decision-summary"):
                    return response(payload={"entitlementDecisions": {
                        "approved": 2, "revoked": 0, "acknowledged": 0,
                        "decisionsMade": 2, "decisionsTotal": 2}})
                if kind == "changed" and path.endswith("/certifications/offline-cert-a"):
                    count += 1
                    if count > 1:
                        changed = certificate()
                        changed["modified"] = "2026-01-02T00:00:00Z"
                        return response(payload=changed)
            fake.override = override
            result, _, _, _ = self.run_capture(fake)
            self.assertEqual(result["outcome"], "INCOMPLETE")

    def test_parent_count_conflict_is_not_ignored(self):
        fake = FakeTransport()
        fake.campaign["totalCertifications"] = 99
        result, _, _, _ = self.run_capture(fake)
        self.assertEqual(result["outcome"], "INCOMPLETE")

    def test_http_transport_constructs_only_get(self):
        calls = []
        class Raw:
            status = 200
            headers = {"Content-Type": "application/json"}
            def __init__(self):
                self.chunks = [b"{}", b""]
            def __enter__(self):
                return self
            def __exit__(self, *args):
                return False
            def read1(self, size):
                return self.chunks.pop(0)
        class Opener:
            def open(self, request, timeout):
                calls.append((request, timeout))
                return Raw()
        transport = object.__new__(m.HTTPTransport)
        transport.opener = Opener()
        result = transport.send("https://offline-test.api.identitynow.com/only-test", {}, 15)
        self.assertEqual(calls[0][0].get_method(), "GET")
        self.assertIsNone(calls[0][0].data)
        self.assertEqual(result.body, b"{}")

    def test_retry_after_wait_and_attempt_bound(self):
        fake = FakeTransport()
        fake.override = lambda path, q, n: response(429, headers={"retry-after": "2"}) if n == 1 else None
        result, _, _, clock = self.run_capture(fake)
        self.assertEqual(result["outcome"], "CAPTURE_CHECKS_PASSED", result)
        self.assertEqual(clock.waits, [2])
        fake = FakeTransport()
        fake.override = lambda *args: response(503)
        result, fake, _, clock = self.run_capture(fake)
        self.assertEqual(result["outcome"], "INCOMPLETE")
        self.assertEqual(len(fake.calls), 3)
        self.assertEqual(clock.waits, [1, 2])

    def test_http_date_retry_after_is_respected(self):
        fake = FakeTransport()
        fake.override = lambda path, q, n: response(429, headers={
            "retry-after": formatdate(102, usegmt=True)}) if n == 1 else None
        with patch.object(m.time, "time", return_value=100):
            result, _, _, clock = self.run_capture(fake)
        self.assertEqual(result["outcome"], "CAPTURE_CHECKS_PASSED", result)
        self.assertEqual(clock.waits, [2])

    def test_control_or_quoted_token_is_rejected_before_network(self):
        for token in ['bad"token', 'bad\\token', 'bad\ntoken', 'bad token']:
            with self.assertRaises(m.CaptureError):
                self.run_capture(token=token)

    def test_default_command_checks_without_token_prompt_or_network(self):
        with tempfile.TemporaryDirectory() as tmp:
            file = Path(tmp) / "config.json"
            file.write_text(json.dumps(config()), encoding="utf-8")
            output = io.StringIO()
            with patch.object(m, "HTTPTransport") as transport, patch.object(
                    m.getpass, "getpass") as prompt, contextlib.redirect_stdout(output):
                self.assertEqual(m.main(["--config", str(file)]), 0)
            transport.assert_not_called()
            prompt.assert_not_called()
            self.assertIn("CONFIG_CHECKED_NO_NETWORK", output.getvalue())

    def test_long_invalid_retry_or_auth_error_stops_without_sleep(self):
        for status, retry in [(429, "60"), (429, "bad"), (401, None), (403, None),
                              (404, None), (302, None)]:
            fake = FakeTransport()
            fake.override = lambda *args: response(status, headers={"retry-after": retry} if retry else {})
            result, fake, _, clock = self.run_capture(fake)
            self.assertEqual(result["outcome"], "INCOMPLETE")
            self.assertEqual(len(fake.calls), 1)
            self.assertEqual(clock.waits, [])

    def test_bad_json_oversize_and_non_json_fail_without_raw_error_dump(self):
        bad = [
            m.Response(200, {"content-type": "application/json"}, b"{"),
            m.Response(200, {"content-type": "application/json"}, b" " * (2 * 1024 * 1024 + 1)),
            m.Response(200, {"content-type": "text/html"}, b"OFFLINE_TOKEN"),
        ]
        for answer in bad:
            fake = FakeTransport()
            fake.override = lambda *args: answer
            result, _, out, _ = self.run_capture(fake)
            self.assertEqual(result["outcome"], "INCOMPLETE")
            self.assertNotIn("OFFLINE_TOKEN", "".join(p.read_text() for p in out.glob("*.json")))

    def test_attempt_and_elapsed_budgets(self):
        cfg = m.validate_config(config())
        fake, clock = FakeTransport(), Clock()
        client = m.Client(cfg, "OFFLINE_TOKEN", fake, None, clock, clock.sleep)
        client.attempts = 40
        with self.assertRaises(m.CaptureError):
            client.get_json("/certification-campaigns/v1/campaigns/offline-campaign", {})
        self.assertEqual(fake.calls, [])
        clock.now = 181
        client.attempts = 0
        with self.assertRaises(m.CaptureError):
            client.get_json("/certification-campaigns/v1/campaigns/offline-campaign", {})

    def test_page_bound_stops_unending_collection(self):
        fake = FakeTransport()
        fake.override = lambda path, q, n: response(payload=[
            {"id": "offline-row-" + q["offset"][0]}],
            headers={"x-total-count": "100"}) if path.endswith("/certifications") else None
        result, fake, _, _ = self.run_capture(fake)
        self.assertEqual(result["outcome"], "INCOMPLETE")
        self.assertLessEqual(len(fake.calls), 11)

    def test_token_never_saved_and_headers_only_reach_bound_origin(self):
        fake = FakeTransport()
        fake.campaign["extra"] = "OFFLINE_TOKEN"
        result, fake, out, _ = self.run_capture(fake)
        self.assertEqual(result["outcome"], "CAPTURE_CHECKS_PASSED", result)
        self.assertNotIn("OFFLINE_TOKEN", "".join(p.read_text() for p in out.glob("*.json")))
        self.assertTrue(all(urlsplit(c[0]).hostname == "offline-test.api.identitynow.com"
                            for c in fake.calls))
        self.assertTrue(all(c[1]["X-SailPoint-Experimental"] == "true" for c in fake.calls))

    def test_config_origin_ids_and_templates_rejected_before_network(self):
        for field, value in [
            ("api_base_url", "http://offline-test.api.identitynow.com"),
            ("api_base_url", "https://offline-test.api.identitynow.com.evil.test"),
            ("api_base_url", "https://user:pass@offline-test.api.identitynow.com"),
            ("api_base_url", "https://offline-test.api.identitynow.com/path"),
            ("api_base_url", "https://offline-test.api.identitynow.com:444"),
            ("campaign_id", "../wrong"), ("source_id", ""),
        ]:
            cfg = config()
            cfg[field] = value
            with self.subTest(field=field, value=value), self.assertRaises(m.CaptureError):
                m.validate_config(cfg)

    def test_only_bound_get_routes_and_exact_parameters(self):
        cfg = m.validate_config(config())
        fake, clock = FakeTransport(), Clock()
        client = m.Client(cfg, "OFFLINE_TOKEN", fake, None, clock, clock.sleep)
        for path, params in [
            ("/certification-campaigns/v1/campaigns/other", {}),
            ("/certification-campaigns/v1/certifications", {}),
            ("/certification-campaigns/v1/certifications/offline-cert-a/decide", {}),
            ("/certification-campaigns/v1/certifications/offline-cert-a/review-items",
             {"limit": 1, "offset": 0, "count": True, "sorters": "name"}),
        ]:
            with self.assertRaises(m.CaptureError):
                client.get_json(path, params)
        self.assertEqual(fake.calls, [])
        handler = m.NoRedirect()
        self.assertIsNone(handler.redirect_request(Request(
            "https://offline-test.api.identitynow.com"), None, 302, "", {}, "https://elsewhere.test"))

    def test_output_is_new_and_confined(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            outside = root / "outside"
            with self.assertRaises(m.CaptureError):
                m.prepare_output(outside, root)
            out = root / "private" / "run"
            m.prepare_output(out, root)
            with self.assertRaises(m.CaptureError):
                m.prepare_output(out, root)

    def test_repeat_uses_new_folder_and_preserves_first_capture(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for name in ["run01", "run02"]:
                fake, clock = FakeTransport(), Clock()
                result = m.collect(config(), root / "private" / name, "OFFLINE_TOKEN",
                                   transport=fake, clock=clock, sleep=clock.sleep, root=root)
                self.assertEqual(result["outcome"], "CAPTURE_CHECKS_PASSED", result)
            first = (root / "private" / "run01" / "run.json").read_text()
            with self.assertRaises(m.CaptureError):
                m.collect(config(), root / "private" / "run01", "OFFLINE_TOKEN",
                          transport=FakeTransport(), root=root)
            self.assertEqual((root / "private" / "run01" / "run.json").read_text(), first)


if __name__ == "__main__":
    unittest.main()
