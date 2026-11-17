# CLS-006 brief: repeat a verified evidence collection with explicit limits

November15,2026. Saved before code and learner prose. Continues the registered design from CLS-005: automate its supported GET-only capture before adding any write workflow. User's standing continue authorizes the next complete local unit and necessary support files; no tenant run or publication.

Learner: CLS-006_Automate_a_Bounded_Read_Only_Evidence_Collection.md.

## Chosen outcome and implementation

Provide a usable Python3.11+ standard-library script, protected private configuration example, offline unit tests and a patient beginner procedure. No SDK/dependency installation or scheduled service. Script plans/validates by default; --live explicitly enables GET requests using a hidden token prompt. It repeats an already manually verified next-generation identity campaign capture, not creating test history or making review decisions.

The registered alternative of writing campaign payloads is unnecessary for this first automation task and would introduce experimental mutation/authority/duplicate-delivery concerns beyond the verified read contract. Full SDK scaffolding is also unnecessary for five public read operations. This concrete design stays within the previously accepted next-file direction; no new product, tenant mutation, deployment or confirmation required.

## Required actual binding and entry facts

Use a real compatible two-A-Export signed case, preferably certlab-cls004-context-run01, whose manual CLS-005-style request capture has already worked. Actual tenant API base, campaign ID/name, full known certification ID set, current reviewer ID, A source/Export entitlement IDs, and both person's/account IDs must be verified privately. Config includes admin versus reviewer view; non-admin gets reviewer-identity=me. Token actual read scopes/object/user authority and experimental permission remain manual preflight facts, not derived from config booleans. No compatible case/token exists in author evidence.

Expected two entitlement holdings: employee01/account01 APPROVED, employee02/account02 REVOKED, source certlab-reports-csv, value certlab-report-export. All3 Read accounts, employee01 Export, B six and historical A4/later restored A5 are separate actual UI/task/source evidence. Script verifies captured relationships/states only, not business approval, identity ownership, actual external removal or restored current permissions.

## Script boundaries

Validate private JSON config shape/IDs and reject incomplete template. HTTPS only, standard single-label tenant.api.identitynow.com origin, no username/password/port/path/query/fragment. Other domains/regional/gov/custom alias need a separately reviewed adapter; never relax TLS or follow arbitrary redirect. Strict route builder permits only the five CLS-005 GET paths using bound campaign and pinned certification IDs. No caller-supplied URL/path/method/body, no browser cookie/internal API, no server-provided pagination link followed, no proxy credential forwarding. No redirect following. Protected token in memory only; no command-line token or token file/environment requirement. Token omitted/redacted from journal.

Fixed lab limits: page size1,10 pages per collection including empty terminator,4 pinned certification IDs maximum,40 HTTP attempts total including retries,15-second request timeout,180-second read budget,2 retries per transient failed GET,30-second maximum single retry wait,2MiB per response. Actual Retry-After seconds or HTTP-date respected; excessive/invalid delay stops incomplete rather than retrying early. Retry only429/selected5xx/network read failures; no auth/validation/path retry or version fallback. All retries remain GET and consume budget.

Output only into a new private subfolder under this course; reject reuse/escape/symlink-outside paths. Preserve partial result and sanitized error status on failure; no overwriting old capture. Responses saved per request with request route/query, observation time, status/selected nonsecret headers and JSON. No raw non-200 body or secrets/header dumps. Report stays INCOMPLETE until all checks pass; successful report is CAPTURE_CHECKS_PASSED/manualComparisonRequired, not a tenant lab/removal pass. Distinguish LIVE_GET from injected OFFLINE_TEST transport in test journals.

## Completeness and reconciliation

Verify campaign ID/name/IDENTITY type and stable available status/modified/count fields. Enumerate campaign-filtered certifications through empty page, check required numeric totals and unique IDs/consistent counts; require retrieved set equals manually pinned IDs before fetching children. Both admin/reviewer view explicit and recorded.

For each pinned certification, read details, verify parent/reviewer/signed phase/dateSigned/completed/progress/counts, enumerate all items with no hidden filter, compare exact source/entitlement/account/subjectTargetId and decision against expected bindings. Count summary per certification and validate totals/approve/revoke/acknowledge; require zero other model units if present. Snapshot before/after certificate detail and re-enumerate parents/get campaign again to detect observed changes. This is bounded consistency checking, not a transactional snapshot guarantee. Missing/duplicate/changed/malformed or unexpected fields/IDs/status remain incomplete, never silent deduplication or inferred success.

## Local test plan before implementation

Write offline tests first and observe import failure before creating the script. Tests inject a fake transport, clock/sleep and synthetic local records labelled offline; no network/real IDs/secrets. Verify nominal grouped/split certification cases, next-page termination, pinned parent scope, expected source/account/decision, child wrong-parent, unsigned/completed distinction, malformed/count/missing page/duplicate IDs/oversize/budgets, protected token/GET-only URLs/redirect refusal/retry429 timing/long wait/auth-stop and exclusive output/partial artifacts. Observe failure on missing implementation, then implement and run meaningful tests, not mirrored line-by-line assertions. Test failures corrected before completion.

## Learner teaching and repeat/recovery

Explain automation as repeating the checked manual process, configuration as exact expected bindings, check-only versus live, timeout/page/retry budgets, private capture and capture checks versus proof. Provide Windows-friendly commands from course root using python -B; actual token pasted into hidden prompt after preflight. Example config blank actual identifiers and clearly non-runnable until private binding; no fake tenant JSON response. Copy into private area; no learner links/source footer. Outline private fields in plain language before the full table/commands.

Run check-only, compare plan to manual case, explicit live run into new run01 directory, read report/raw scope and compare interface/historical fulfillment manually. Repeat capture into new run02, compare stable source/account-right/decision records rather than file bytes/timestamps. Leave state changed by others as observed changes requiring manual reconciliation; do not normalize them away. Capture-only rerun cannot duplicate a sign-off/access request because no writes exist. Safe recovery resolves recorded cause/authority/contract externally then starts fresh folder; no blind automatic restart/resume overwriting partial evidence. Changed-case unexpected reviewer, duplicated page or current Export after documented reset is reasoning, not deliberate live mutation. No tenant reset because GET only; remove temporary token from local session/memory by exit.

## Completion and verification

Finish one full learner file plus script/config example/tests and author source/read-through record. Extend existing validator23 learner files/23 planning IDs/14 CSV unchanged/new JSON total5. Keep original A hashes/native fixtures/previous source semantics. Run offline tests and full-course checks after final changes. Actual requests/authority/live capture/repeat/independent learner pass all0. All23 authored does not mean tenant validated. Next normal work is course-wide final author audit, followed by actual setup/execution readiness, not another arbitrary lesson or publication.
