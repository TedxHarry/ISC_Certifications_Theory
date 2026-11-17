# CLS-006 revision1.0 author record

November15,2026. Authored with executable support and offline tests; no authenticated API/tenant execution, repeated live capture, independent learner test or publication.

Learner: [Automate a bounded read-only evidence collection](../../lessons/CLS-006_Automate_a_Bounded_Read_Only_Evidence_Collection.md).
Design: [saved brief](../briefs/CLS-006_Bounded_Read_Automation_Brief.md).
Support: [collector](../../tools/collect_certification_evidence.py), [blank configuration example](../contracts/CLS-006_Config_Example.json), [offline tests](../tests/test_collect_certification_evidence.py) and the existing [five-GET contract](../contracts/CLS-005_Read_Only_Request_Plan.json).

## Authorized scope and choice

The registered CLS-006 direction and normal continue authorize local authoring of bounded automation after the manual API unit. This implements a GET-only evidence collector for the same already verified next-generation identity case. It does not broaden scope to creating campaigns, deciding/reassigning/signing reviews, removing permissions, closing tasks, generating reports or onboarding another connector.

Python3.11+ standard library avoids SDK/dependency scaffolding; local tests ran with Python3.13.0. Default command validates configuration without a token prompt/network. Explicit --live uses a protected prompt and new private folder. User's reported full tenant access is not a successful actual token/role/endpoint check. No credential, actual host binding or tenant response was supplied.

## Current source checks

November15,2026 focused recheck, not exhaustive release audit or observed tenant contract.

| Primary source | Use and limitation |
|---|---|
| [Certification list](https://developer.sailpoint.com/docs/api/list-certifications-v-1/) | Current experimental path/header, parent filter, read scope/view, limit/offset/count and name sorter. Non-admin reviewer query kept separate. |
| [Item list](https://developer.sailpoint.com/docs/api/list-review-items-v-1/) | Entitlement/subject/account/source mapping and complete item paging with actual returned schema. No inferred legacy/write contract. |
| [Parent campaign](https://developer.sailpoint.com/docs/api/get-gov-certification-campaign-v-1/) | Actual generated campaign binding and current experimental read. |
| [Campaign representation](https://developer.sailpoint.com/docs/api/create-gov-certification-campaign-v-1/) | Public representation confirms type/identity and available parent counts/state. POST operation was read as documentation only, never implemented or invoked. |
| [Certification detail](https://developer.sailpoint.com/docs/api/get-certification-v-1/) | Current child lookup/access and signed record capture. |
| [Certification model](https://developer.sailpoint.com/docs/tools/sdk/typescript/gov_certification/models/certification/) | completed/phase/reviewProgress/dateSigned/counts/reviewer meanings; completed alone does not establish sign-off. |
| [Decision summary](https://developer.sailpoint.com/docs/api/get-decision-summary-v-1/) | Compare actual entitlement counts and no unexpected model units. |
| [Rate limiting](https://developer.sailpoint.com/docs/api/rate-limit/) | Respect Retry-After with bounded attempts; long waits stop incomplete rather than retry early. No universal throughput promise. |
| [Authorization](https://developer.sailpoint.com/docs/api/authorization/) | Actual caller/user-level/object/read scopes checked manually; no automatic all-scope/admin repair. |
| [Python URL requests](https://docs.python.org/3/library/urllib.request.html) | Explicit GET, HTTPS handler/default TLS, disabling automatic proxies and redirects, network timeout; bounded reads supplement per-operation timeout. |

All selected next-generation operations remain documented as experimental with X-SailPoint-Experimental:true. Service paths/experimental availability must be rechecked in the actual tenant. Header/schema changes stop incomplete. The supported adapter accepts only the standard single-label tenant.api.identitynow.com HTTPS origin without port/path/userinfo; custom/government/other domains or proxy-dependent networks require separate reviewed preparation, not relaxed TLS.

## Implementation checks and behavior

Exact bound host/campaign and one-to-four manually pinned certification IDs. Fixed route/query builder permits only the five read operations; no arbitrary URLs, server pagination links, request bodies, token arguments or write operation. Non-admin view sets reviewer-identity=me. Returned parent set must match all pinned IDs before children are followed; manual authority remains a prerequisite rather than a programmatically asserted permission.

One-record pages terminate with a verified empty page, consistent required X-Total-Count and unique IDs. Bounds:10 pages per collection,40 HTTP attempts including retries,15-second socket/network timeout,180-second budget checked between reads/waits,2 retries,30-second maximum wait and2MiB response cap. HTTP-date/seconds Retry-After respected. Timed chunk reads prevent endless body trickling; socket/OS behavior means the read-budget check is not a transactional wall-clock guarantee.

Exact two entitlement relationships and decisions, signed phase/date, current reviewer, parent/child/summary counts and end-of-capture repeated records are checked. Unexpected source/account/person/decision, missing/changed schema/count, unsigned review, changed record or repeated holding fails. Repeated parent/child reads detect observed changes but cannot provide an atomic tenant snapshot.

Output confined to a new course/private subdirectory; resolved escapes and existing output rejected. Run report writes replace only this new run's own metadata through a temporary file; response files are exclusive. Partial run remains INCOMPLETE; sanitized reason/status retained without raw error bodies. Bearer token syntax excludes control/quoted/backslash forms and its literal value is redacted in successful JSON output. No token is saved in configuration or a credential file. Default TLS retained; redirects/proxy forwarding disabled.

Success name CAPTURE_CHECKS_PASSED deliberately states the actual scope of proof. Report preserves manual_comparison_required=true, authority_verified_by_script=false, fulfillment_verified=false, target_permission_verified=false and tenant_data_mutated=false. Real HTTP adapter capture is LIVE_GET; injected tests OFFLINE_TEST. Signed rejection, historical CSV removal, later reset and current target access remain separate evidence.

## Test-first and correction evidence

Saved offline tests before the collector; initial run failed with missing implementation. After implementation,20 meaningful cases passed. Further failing tests exposed acceptance of malformed quoted token forms and lack of a parent-count conflict check. Token validation and parent count reconciliation were corrected; added date-based Retry-After, default no-network and actual Request-method checks. Current suite contains25 passing test methods, with subcases for several failure variants.

All records/tokens/hosts in tests are explicitly synthetic offline values. Fake transports and clocks avoid network, real waits and actual credentials. Tests cover grouped/split assignments; terminal pages/offsets; narrow encoded filters/view; wrong parent/pinned set; unsigned completed=true; exact source/account/subject/decision; duplicate/early-empty/missing/changing/malformed total; summary/record/parent count changes; transient retries/date delays/auth/redirect stop; JSON/content/size limits; request/time/page budgets; protected token/no-network command; standard host/path restrictions; output confinement/exclusivity; repeated capture preserving first run. No mock result becomes an actual API response or tenant pass.

CLI help was checked and the supplied blank example was intentionally rejected before any token/network. No real --live command was executed. Repeat testing refers to separate offline captures, not a repeated tenant lab. No test generated files or bytecode caches inside the course.

## Full saved beginner read-through

Read the saved complete learner guide, configuration, script boundary/collection flow and tests. The lesson explains automation as repeating the verified manual checks, then exact private bindings, JSON list structure, default versus live, bounds, capture report, manual comparison, failure recovery and repetition. Keeps code mechanics outside the ordinary learning flow while giving usable commands and exact supporting filenames.

Known IDs differ from names/values; pinned set differs from returned authorized subset. No token in command/config. Failed capture remains useful partial evidence, not overwritten. Changed reviewer must be explained through actual history before updating expected bindings. Native capture checks do not supply business approval, real authority or permission-removal proof. Three focused learner tables address scope, configuration and limits; dynamic structure/no fixed quota. No fictional company, continuing character, source/course links or invented screenshots in learner prose.

## Local verification

Fresh checks pass across110 reusable course files:88 Markdown,280 resolving project-local links,110 consistent table groups/851 rows,23 matching design/register IDs and all23 learner files. All14 canonical CSVs remain checked;5 JSON assets/contracts parse. Original A hashes, earlier diagram/source-set and005–017/D/E/F/context/API-plan checks still pass. Learner source/course-link absence, no stubs, fence/details wrappers, whitespace and final newlines pass.

The automation support check confirms the collector/test assets and deliberately blank actual host/IDs, compatible case alias, two expected decisions and credential-free configuration template. Private evidence/raw captures, caches, site/dependency/repository directories are excluded from reusable-course inventory checks; private observations are not published course assets. Python3.13.0 executes25 offline test methods successfully with no network. CLI help and intentional blank-template rejection were also checked. No real request or live output was produced.

These checks establish authored consistency and tested local program behavior, not actual token authority, endpoint availability, live completeness, UI comparison, manual fulfillment, repeated tenant execution or learner performance. All actual execution/repeat/learner/publication states remain unchanged at0.

## Course state and next work

This completes authoring of the initial23-unit inventory:17 main and6 specialist guides. Authored/source/language reviewed and offline support checked are separate from tenant executed/repeated/learner tested; the latter remain0. Existing eleven product verification questions remain open. No repository, push or Pages publication for this hands-on project.

Next work is a final whole-course author audit for consistency, duplicate steps, beginner readability and execution readiness, then actual setup/lab validation. Do not invent another lesson to extend the count or promote local support tests to a course pass.
