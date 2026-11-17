"""Collect one manually verified training review. Only fixed GET routes are sent."""
from __future__ import annotations

import argparse
import getpass
import http.client
import json
import math
import os
import re
import ssl
import time
from dataclasses import dataclass
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode, urlsplit
from urllib.request import HTTPRedirectHandler, HTTPSHandler, ProxyHandler, Request, build_opener

ROOT = Path(__file__).resolve().parents[1]
PREFIX = "/certification-campaigns/v1"
MAX_PAGES = 10
MAX_ATTEMPTS = 40
MAX_SECONDS = 180
TIMEOUT = 15
MAX_RETRIES = 2
MAX_WAIT = 30
MAX_BODY = 2 * 1024 * 1024
ID = re.compile(r"[A-Za-z0-9][A-Za-z0-9_-]{0,127}\Z")
TOKEN = re.compile(r"[A-Za-z0-9._~+/-]+=*\Z")
FIELDS = {"api_base_url", "campaign_id", "campaign_name", "caller_view",
          "certification_ids", "reviewer_id", "source_id", "entitlement_id",
          "attribute_name", "entitlement_value", "expected_items"}


class CaptureError(Exception):
    """Only fixed, credential-free reason codes may be raised."""


def need(condition, code):
    if not condition:
        raise CaptureError(code)


def valid_id(value):
    return isinstance(value, str) and ID.fullmatch(value) is not None


def integer(value):
    return type(value) is int and value >= 0


def validate_config(raw):
    need(isinstance(raw, dict) and set(raw) == FIELDS, "CONFIG_FIELDS")
    cfg = json.loads(json.dumps(raw))
    base = cfg["api_base_url"]
    need(isinstance(base, str), "CONFIG_ORIGIN")
    try:
        u = urlsplit(base)
        need(u.scheme == "https" and not u.username and not u.password
             and u.port is None and u.path in ("", "/") and not u.query
             and not u.fragment and re.fullmatch(
                 r"[a-z0-9-]+\.api\.identitynow\.com", u.netloc or "") is not None,
             "CONFIG_ORIGIN")
    except ValueError:
        raise CaptureError("CONFIG_ORIGIN") from None
    cfg["api_base_url"] = base.rstrip("/")
    for field in ["campaign_id", "reviewer_id", "source_id", "entitlement_id"]:
        need(valid_id(cfg[field]), "CONFIG_IDS")
    name = cfg["campaign_name"]
    need(isinstance(name, str) and 0 < len(name) <= 256
         and not any(ord(c) < 32 for c in name), "CONFIG_CAMPAIGN_NAME")
    need(cfg["caller_view"] in ("admin", "reviewer"), "CONFIG_CALLER_VIEW")
    ids = cfg["certification_ids"]
    need(isinstance(ids, list) and 1 <= len(ids) <= 4
         and all(valid_id(x) for x in ids) and len(set(ids)) == len(ids),
         "CONFIG_CERTIFICATION_IDS")
    need(cfg["attribute_name"] == "groups"
         and cfg["entitlement_value"] == "certlab-report-export", "CONFIG_PERMISSION")
    items = cfg["expected_items"]
    need(isinstance(items, list) and len(items) == 2, "CONFIG_EXPECTED_ITEMS")
    for item in items:
        need(isinstance(item, dict) and set(item) == {"identity_id", "account_id", "decision"}
             and valid_id(item["identity_id"]) and valid_id(item["account_id"])
             and item["decision"] in ("APPROVED", "REVOKED"), "CONFIG_EXPECTED_ITEMS")
    need(len({x["identity_id"] for x in items}) == 2
         and len({x["account_id"] for x in items}) == 2
         and {x["decision"] for x in items} == {"APPROVED", "REVOKED"},
         "CONFIG_EXPECTED_ITEMS")
    return cfg


def prepare_output(output, root=ROOT):
    root = Path(root).resolve()
    out = Path(output).resolve()
    private = root / "private"
    need(out != private and out.is_relative_to(private), "OUTPUT_MUST_BE_PRIVATE")
    need(not out.exists(), "OUTPUT_ALREADY_EXISTS")
    try:
        out.mkdir(parents=True, exist_ok=False)
    except OSError:
        raise CaptureError("OUTPUT_CREATION_FAILED") from None
    return out


def utc_now():
    return datetime.now(timezone.utc).isoformat()


class Journal:
    def __init__(self, directory, token):
        self.directory = directory
        self.token = token
        self.number = 0

    def write(self, filename, data, exclusive=False):
        text = json.dumps(data, indent=2, ensure_ascii=False, allow_nan=False)
        text = text.replace(self.token, "[REDACTED]")
        try:
            target = self.directory / filename
            temporary = target if exclusive else self.directory / (filename + ".tmp")
            with temporary.open("x", encoding="utf-8", newline="\n") as f:
                f.write(text + "\n")
            if not exclusive:
                os.replace(temporary, target)
        except OSError:
            raise CaptureError("OUTPUT_WRITE_FAILED") from None

    def response(self, path, query, status, headers, payload):
        self.number += 1
        keep = {k: v for k, v in headers.items()
                if k in {"content-type", "x-total-count", "retry-after", "date"}}
        self.write(f"response-{self.number:03d}.json",
                   {"observed_at": utc_now(), "method": "GET", "path": path,
                    "query": query, "status": status, "headers": keep, "body": payload},
                   exclusive=True)


@dataclass
class Response:
    status: int
    headers: dict
    body: bytes


class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


class HTTPTransport:
    def __init__(self):
        self.opener = build_opener(ProxyHandler({}), NoRedirect(),
                                  HTTPSHandler(context=ssl.create_default_context()))

    def send(self, url, headers, timeout):
        request = Request(url, headers=headers, method="GET")
        started = time.monotonic()
        try:
            with self.opener.open(request, timeout=timeout) as response:
                body = bytearray()
                while len(body) <= MAX_BODY:
                    if time.monotonic() - started >= timeout:
                        return Response(0, {}, b"")
                    chunk = response.read1(min(65536, MAX_BODY + 1 - len(body)))
                    if not chunk:
                        break
                    body.extend(chunk)
                return Response(response.status, dict(response.headers), bytes(body))
        except HTTPError as error:
            status, response_headers = error.code, dict(error.headers or {})
            error.close()
            return Response(status, response_headers, b"")
        except (URLError, OSError, http.client.HTTPException):
            return Response(0, {}, b"")


class Client:
    def __init__(self, cfg, token, transport, journal=None,
                 clock=time.monotonic, sleep=time.sleep):
        need(isinstance(token, str) and TOKEN.fullmatch(token) is not None, "TOKEN_FORMAT")
        self.cfg, self.token, self.transport, self.journal = cfg, token, transport, journal
        self.clock, self.sleep, self.started = clock, sleep, clock()
        self.attempts = 0

    def validate_request(self, path, query):
        campaign = PREFIX + "/campaigns/" + self.cfg["campaign_id"]
        certs = PREFIX + "/certifications"
        if path == campaign:
            need(query == {}, "REQUEST_QUERY_NOT_ALLOWED")
            return
        if path == certs:
            expected = {"filters": 'campaignRef.id eq "' + self.cfg["campaign_id"] + '"',
                        "limit": 1, "offset": query.get("offset"), "count": True,
                        "sorters": "name"}
            if self.cfg["caller_view"] == "reviewer":
                expected["reviewer-identity"] = "me"
            need(query == expected and type(query.get("count")) is bool
                 and type(query.get("limit")) is int and integer(query.get("offset")),
                 "REQUEST_QUERY_NOT_ALLOWED")
            return
        for cid in self.cfg["certification_ids"]:
            detail = certs + "/" + cid
            if path in (detail, detail + "/decision-summary"):
                need(query == {}, "REQUEST_QUERY_NOT_ALLOWED")
                return
            if path == detail + "/review-items":
                expected = {"limit": 1, "offset": query.get("offset"), "count": True,
                            "sorters": "certificationSubjectSummary.subjectName"}
                need(query == expected and type(query.get("count")) is bool
                     and type(query.get("limit")) is int and integer(query.get("offset")),
                     "REQUEST_QUERY_NOT_ALLOWED")
                return
        raise CaptureError("REQUEST_PATH_NOT_ALLOWED")

    def wait_for_retry(self, headers, attempt):
        value = headers.get("retry-after")
        if value is None:
            seconds = 2 ** attempt
        else:
            need(isinstance(value, str), "RETRY_AFTER_INVALID")
            if value.isdecimal():
                seconds = int(value)
            else:
                try:
                    stamp = parsedate_to_datetime(value)
                    need(stamp.tzinfo is not None, "RETRY_AFTER_INVALID")
                    seconds = max(0, stamp.timestamp() - time.time())
                except (ValueError, TypeError, OverflowError):
                    raise CaptureError("RETRY_AFTER_INVALID") from None
        need(math.isfinite(seconds) and 0 <= seconds <= MAX_WAIT, "RETRY_WAIT_EXCEEDS_LIMIT")
        need(self.clock() - self.started + seconds < MAX_SECONDS, "TIME_BUDGET_EXCEEDED")
        self.sleep(seconds)

    def get_json(self, path, query):
        self.validate_request(path, query)
        encoded = urlencode({k: str(v).lower() if type(v) is bool else v
                             for k, v in query.items()})
        url = self.cfg["api_base_url"] + path + ("?" + encoded if encoded else "")
        headers = {"Accept": "application/json", "Authorization": "Bearer " + self.token,
                   "X-SailPoint-Experimental": "true"}
        for attempt in range(MAX_RETRIES + 1):
            remaining = MAX_SECONDS - (self.clock() - self.started)
            need(remaining > 0, "TIME_BUDGET_EXCEEDED")
            need(self.attempts < MAX_ATTEMPTS, "REQUEST_BUDGET_EXCEEDED")
            self.attempts += 1
            result = self.transport.send(url, headers, min(TIMEOUT, remaining))
            h = {str(k).lower(): str(v) for k, v in result.headers.items()}
            payload = None
            code = None
            if result.status == 200:
                if len(result.body) > MAX_BODY:
                    code = "RESPONSE_TOO_LARGE"
                elif not (h.get("content-type", "").split(";")[0].strip() == "application/json"
                          or h.get("content-type", "").split(";")[0].strip().endswith("+json")):
                    code = "RESPONSE_CONTENT_TYPE"
                else:
                    try:
                        payload = json.loads(result.body.decode("utf-8"),
                                             parse_constant=lambda _: (_ for _ in ()).throw(ValueError()))
                    except (ValueError, UnicodeError):
                        code = "RESPONSE_JSON_INVALID"
            if self.journal:
                self.journal.response(path, query, result.status, h, payload)
            need(self.clock() - self.started < MAX_SECONDS, "TIME_BUDGET_EXCEEDED")
            if result.status == 200:
                need(code is None, code)
                return payload, h
            need(not 300 <= result.status < 400, "REDIRECT_REFUSED")
            transient = result.status in (0, 429, 500, 502, 503, 504)
            need(transient, "HTTP_" + str(result.status))
            need(attempt < MAX_RETRIES, "RETRY_LIMIT_REACHED")
            self.wait_for_retry(h, attempt)
        raise CaptureError("RETRY_LIMIT_REACHED")


def pages(client, path, query):
    records, ids, offset, total = [], set(), 0, None
    for _ in range(MAX_PAGES):
        payload, headers = client.get_json(path, {**query, "offset": offset})
        need(isinstance(payload, list) and len(payload) <= 1, "PAGE_SHAPE_CHANGED")
        count = headers.get("x-total-count")
        need(count is not None and count.isdecimal(), "PAGE_TOTAL_MISSING_OR_INVALID")
        count = int(count)
        need(total is None or count == total, "PAGE_TOTAL_CHANGED")
        total = count
        for record in payload:
            need(isinstance(record, dict) and valid_id(record.get("id")), "PAGE_ID_MISSING")
            need(record["id"] not in ids, "PAGE_ID_REPEATED")
            ids.add(record["id"])
            records.append(record)
        if not payload:
            need(len(records) == total, "PAGE_COUNT_MISMATCH")
            return records
        offset += len(payload)
    raise CaptureError("PAGE_LIMIT_REACHED")


def campaign_signature(data, cfg):
    need(isinstance(data, dict) and data.get("id") == cfg["campaign_id"]
         and data.get("name") == cfg["campaign_name"] and data.get("type") == "IDENTITY",
         "CAMPAIGN_BINDING_MISMATCH")
    return {k: data.get(k) for k in ["id", "name", "type", "status", "modified",
                                    "totalCertifications", "completedCertifications"]}


def cert_signature(data, cfg):
    need(isinstance(data, dict) and data.get("id") in cfg["certification_ids"],
         "CERTIFICATION_BINDING_MISMATCH")
    ref, reviewer = data.get("campaignRef"), data.get("reviewer")
    need(isinstance(ref, dict) and ref.get("id") == cfg["campaign_id"]
         and ref.get("type") == "IDENTITY", "CERTIFICATION_PARENT_MISMATCH")
    need(isinstance(reviewer, dict) and reviewer.get("id") == cfg["reviewer_id"]
         and reviewer.get("type") == "IDENTITY", "REVIEWER_MISMATCH")
    need(data.get("phase") == "SIGNED" and data.get("completed") is True
         and data.get("reviewProgress") in (None, "SIGNED"), "SIGN_OFF_NOT_ESTABLISHED")
    try:
        stamp = datetime.fromisoformat(data["dateSigned"].replace("Z", "+00:00"))
        need(stamp.tzinfo is not None, "SIGN_OFF_NOT_ESTABLISHED")
    except (KeyError, AttributeError, ValueError):
        raise CaptureError("SIGN_OFF_NOT_ESTABLISHED") from None
    for key in ["decisionsMade", "decisionsTotal"]:
        need(integer(data.get(key)), "CERTIFICATION_COUNTS_INVALID")
    return {k: data.get(k) for k in ["id", "campaignRef", "reviewer", "phase",
             "reviewProgress", "dateSigned", "completed", "modified",
             "decisionsMade", "decisionsTotal"]}


def validate_item(item, cfg):
    need(isinstance(item, dict) and item.get("type") == "ENTITLEMENT"
         and item.get("completed") is True, "ITEM_TYPE_OR_STATE_MISMATCH")
    subject = item.get("certificationSubjectSummary", {})
    entitlement = item.get("reviewData", {}).get("entitlement", {})
    account = entitlement.get("account", {})
    need(isinstance(subject, dict) and subject.get("subjectType") == "IDENTITY"
         and valid_id(subject.get("id")), "SUBJECT_MAPPING_MISSING")
    need(entitlement.get("sourceId") == cfg["source_id"]
         and entitlement.get("id") == cfg["entitlement_id"]
         and entitlement.get("attributeName") == cfg["attribute_name"]
         and entitlement.get("attributeValue") == cfg["entitlement_value"],
         "ENTITLEMENT_MAPPING_MISMATCH")
    identity, account_id = subject.get("subjectTargetId"), account.get("id")
    expected = [e for e in cfg["expected_items"]
                if e["identity_id"] == identity and e["account_id"] == account_id]
    need(len(expected) == 1 and item.get("decision") == expected[0]["decision"],
         "ITEM_SCOPE_OR_DECISION_MISMATCH")
    if item["decision"] == "REVOKED":
        need(isinstance(item.get("comments"), str) and bool(item["comments"].strip()),
             "REVOKE_REASON_MISSING")
    return identity, account_id


def validate_summary(summary, items):
    counts = {"approved": sum(i["decision"] == "APPROVED" for i in items),
              "revoked": sum(i["decision"] == "REVOKED" for i in items),
              "acknowledged": 0, "decisionsMade": len(items), "decisionsTotal": len(items)}
    need(isinstance(summary, dict), "SUMMARY_SHAPE_CHANGED")
    ent = summary.get("entitlementDecisions")
    need(isinstance(ent, dict) and all(integer(ent.get(k)) and ent[k] == v
                                      for k, v in counts.items()), "SUMMARY_MISMATCH")
    for field in ["accessProfileDecisions", "roleDecisions"]:
        if field in summary:
            other = summary[field]
            need(isinstance(other, dict) and all(integer(other.get(k)) and other[k] == 0
                                                for k in counts), "UNEXPECTED_REVIEW_UNITS")


def collect(raw_config, output_dir, token, *, transport=None, clock=time.monotonic,
            sleep=time.sleep, root=ROOT):
    cfg = validate_config(raw_config)
    need(isinstance(token, str) and TOKEN.fullmatch(token) is not None, "TOKEN_FORMAT")
    out = prepare_output(output_dir, root)
    transport = transport if transport is not None else HTTPTransport()
    journal = Journal(out, token)
    client = Client(cfg, token, transport, journal, clock, sleep)
    report = {"outcome": "INCOMPLETE", "mode": "LIVE_GET" if isinstance(
        transport, HTTPTransport) else "OFFLINE_TEST", "started_at": utc_now(),
        "bound_configuration": cfg, "manual_comparison_required": True,
        "authority_verified_by_script": False, "fulfillment_verified": False,
        "target_permission_verified": False, "tenant_data_mutated": False}
    journal.write("run.json", report)
    try:
        campaign_path = PREFIX + "/campaigns/" + cfg["campaign_id"]
        first, _ = client.get_json(campaign_path, {})
        initial_campaign = campaign_signature(first, cfg)
        cert_query = {"filters": 'campaignRef.id eq "' + cfg["campaign_id"] + '"',
                      "limit": 1, "count": True, "sorters": "name"}
        if cfg["caller_view"] == "reviewer":
            cert_query["reviewer-identity"] = "me"
        listed = pages(client, PREFIX + "/certifications", cert_query)
        need({c["id"] for c in listed} == set(cfg["certification_ids"]),
             "PINNED_CERTIFICATION_SET_MISMATCH")
        for field in ["totalCertifications", "completedCertifications"]:
            if field in first:
                need(integer(first[field]) and first[field] == len(listed),
                     "CAMPAIGN_COUNT_MISMATCH")
        listed_signatures = {c["id"]: cert_signature(c, cfg) for c in listed}
        seen_holdings, item_total, decisions = set(), 0, {"APPROVED": 0, "REVOKED": 0}
        for cid in cfg["certification_ids"]:
            path = PREFIX + "/certifications/" + cid
            before, _ = client.get_json(path, {})
            before_signature = cert_signature(before, cfg)
            need(before_signature == listed_signatures[cid], "CERTIFICATION_CHANGED")
            items = pages(client, path + "/review-items", {"limit": 1, "count": True,
                         "sorters": "certificationSubjectSummary.subjectName"})
            for item in items:
                holding = validate_item(item, cfg)
                need(holding not in seen_holdings, "HOLDING_REPEATED")
                seen_holdings.add(holding)
                decisions[item["decision"]] += 1
            need(before["decisionsMade"] == before["decisionsTotal"] == len(items),
                 "CERTIFICATION_ITEM_COUNT_MISMATCH")
            summary, _ = client.get_json(path + "/decision-summary", {})
            validate_summary(summary, items)
            after, _ = client.get_json(path, {})
            need(cert_signature(after, cfg) == before_signature, "CERTIFICATION_CHANGED")
            item_total += len(items)
        expected = {(e["identity_id"], e["account_id"]) for e in cfg["expected_items"]}
        need(seen_holdings == expected and item_total == 2
             and decisions == {"APPROVED": 1, "REVOKED": 1}, "FINAL_ITEM_SET_MISMATCH")
        final_list = pages(client, PREFIX + "/certifications", cert_query)
        need({c["id"]: cert_signature(c, cfg) for c in final_list} == listed_signatures,
             "CERTIFICATION_COLLECTION_CHANGED")
        last, _ = client.get_json(campaign_path, {})
        need(campaign_signature(last, cfg) == initial_campaign, "CAMPAIGN_CHANGED")
        report.update(outcome="CAPTURE_CHECKS_PASSED", item_count=item_total,
                      decisions=decisions, certification_count=len(listed))
    except CaptureError as error:
        report["reason_code"] = str(error)
    except (KeyError, TypeError, AttributeError, ValueError, IndexError):
        report["reason_code"] = "RESPONSE_SCHEMA_CHANGED"
    except Exception:
        report["reason_code"] = "UNEXPECTED_CAPTURE_ERROR"
    report.update(finished_at=utc_now(), http_attempts=client.attempts,
                  response_files=journal.number)
    journal.write("run.json", report)
    return report


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", required=True)
    parser.add_argument("--live", action="store_true",
                        help="Send the bounded GET requests after the manual preflight.")
    parser.add_argument("--out", help="New directory inside this course's private folder.")
    args = parser.parse_args(argv)
    try:
        try:
            raw = json.loads(Path(args.config).read_text(encoding="utf-8"))
        except (OSError, ValueError):
            raise CaptureError("CONFIG_READ_FAILED") from None
        cfg = validate_config(raw)
        if not args.live:
            print("CONFIG_CHECKED_NO_NETWORK: one pinned campaign, GET only; "
                  "page size 1, 10 pages/collection, 40 attempts, 180 seconds.")
            print("This validates configuration, not token authority or tenant results.")
            return 0
        need(bool(args.out), "OUTPUT_REQUIRED")
        token = getpass.getpass("Paste approved access token (hidden): ")
        result = collect(cfg, args.out, token)
        token = None
        print(result["outcome"])
        if result["outcome"] != "CAPTURE_CHECKS_PASSED":
            print(result.get("reason_code", "INCOMPLETE"))
            return 1
        print("Compare the private capture with the UI and separate fulfillment evidence.")
        return 0
    except CaptureError as error:
        print("NOT_RUN: " + str(error))
        return 2
    except KeyboardInterrupt:
        print("INTERRUPTED: preserve any partial private output and start a new capture.")
        return 130
    except Exception:
        print("NOT_RUN: CLIENT_SETUP_OR_OUTPUT_FAILURE")
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
