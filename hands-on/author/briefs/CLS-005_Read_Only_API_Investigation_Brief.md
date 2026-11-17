# CLS-005 brief: reconcile a next-generation identity review through GET requests

November15,2026. Saved before learner prose.
Learner: CLS-005_Investigate_a_Certification_Through_Read_Only_APIs.md.

## Concrete responsibility and entry case

Use supported public read APIs to trace one actual next-generation identity campaign through assigned certifications and individual entitlement review items. Retrieve all scoped pages, identify actual actors/decisions/sign-off, compare UI/history/manual removal/current source observations and explain gaps without changing work. No campaign creation/start/completion, decision/sign-off/reassignment, report generation, task completion, CSV upload, account change or deletion in this lab.

Require one actually executed compatible two-A-Export case, preferably certlab-cls004-context-run01. Its known scope is employee01/account01 and employee02/account02 on certlab-reports-csv, certlab-report-export only. Final intended one Approve employee01/one Revoke employee02; manager01 reviewer, source owner manager02. Match actual recorded ID, scope and stage, not merely its name. No history exists in this project's authoring session; exercise remains not run until real case and authorized API access are available. Creating seed history belongs to the separate review task, not a hidden mutation in this read-only investigation.

Full target account aliases are certlab-account01 for certlab-employee01 and certlab-account02 for certlab-employee02. Bind the actual IDs separately from these readable aliases.

Historical source result A4/B6 before reset versus restored A5/B6 afterward must be dated. Review items remain historical even after source restoration; current data does not retroactively prove an old removal. If original removal/file/collection proof absent, report gap. Use UI/actual Task Manager evidence for manual fulfillment; do not mislabel next-generation certification-tasks service records as external entitlement-remediation tasks without a verified contract.

## Current primary contract

Current API service-version migration distinguishes /certification-campaigns/v1 (next-generation) from /campaigns/v1 and /certifications/v1 legacy resources. A semver v1 path is not a guarantee of public stable status. The selected next-generation operations currently experimental and require X-SailPoint-Experimental:true. Verify actual engine, current public operation specifications, experimental allowance and availability before sending. No silent engine/version fallback, internal browser endpoints or guessed models; no blanket legacy deprecation claim.

Five GET request templates, all on one verified tenant API base:
1 /certification-campaigns/v1/campaigns/{campaignId}
2 /certification-campaigns/v1/certifications with filters campaignRef.id eq "{campaignId}", limit1, offset0, counttrue, sorters name.
3 /certification-campaigns/v1/certifications/{certificationId}
4 /certification-campaigns/v1/certifications/{certificationId}/review-items with limit1, offset0, counttrue, sorters certificationSubjectSummary.subjectName, no decision/completed/item filter.
5 /certification-campaigns/v1/certifications/{certificationId}/decision-summary with no filters.

Paths use actual opaque IDs from the preceding resource. IDs cannot be inferred from display names, prefixes/UUID appearance or entitlement attribute values. subject summary id is not necessarily the identity ID: subjectTargetId is target entity; preserve summary ID separately. ENTITLEMENT item mapping reviewData.entitlement.sourceId/id/attributeName/attributeValue/account plus certificationSubjectSummary.subjectTargetId and top-level reviewItem id; actual shape checked. Missing mapping stays incomplete rather than invented.

Existing authorized Org/Cert Admin for full case visibility, or verified assigned reviewer view explicitly limited. Use an approved prepared bearer access token; token preparation/authentication happens before this unit. Verify least read scope in each operation's Authorization, idn:campaign:read when actually listed, plus user-level/object authority. No sp:scopes:all/admin promotion/credential sharing as automatic repair. Non-admin list requires reviewer-identity=me and returns only authorized work; do not infer campaign-wide absence from limited view. Distinguish token's acting identity from browser session. Keep token/secret out of paths, source files, raw exports and run notes; use protected client auth storage.

## Manual requests and pagination proof

Approved API client, not code/install requirement. Explain URL/path/GET/headers/query/response/JSON/array before relying on them. Accept application/json, Authorization Bearer protected access token and experimental header. No request body or bundled imported write examples. API base is actual permitted tenant endpoint, not the UI URL or documentation example host.

Capture UI first: actual campaign ID/engine/type/scope, assigned review IDs/actors/phase and total2 entitlement holdings, not assumed two certification objects. Stable read window after completion preferred. Capture each response status/header/body/query/time privately; secret header excluded. Parent campaign exact match before list.

Use API client's parameter table so filters/spaces/quotes encoded once; API filter syntax differs from Search query. Preserve parent filter for every certification page; optional reviewer-identity=me restricts view and is recorded. counttrue total means filtered/authorized collection, not role/entitlement count or tenant-wide truth. A successful first page with1 record is not complete.

For each collection independently, start offset0/limit1, save page/IDs/count, increase offset by number of returned records, request until empty page and reconcile unique IDs with total when provided. Full page always needs next check. Bound ten pages per collection for this small case; unexpected size/missing filter/duplicate ID/changing count requires stop/reconciliation, not silently discard duplicates or broaden scope. Offsets are record-based, reset to0 for each child certification. Supported sorters improve ordering, not atomic snapshot guarantees. Repeat read after confirmed state settles if capture changes, preserving both observations.

For every certification verify campaignRef.id; retrieve full certification and all child items. A single known certification or reviewer-only list may be incomplete. Compute exact source-account-right tuples across all children; expect two only if actual case matches. Preserve actual IDs and item count versus subject count. No live JSON response or invented GUID fixture.

## State and evidence interpretation

Certification completed means all decisions made; not proof sign-off or removal. Inspect phase/reviewProgress/dateSigned/reviewer, signed UI and item decision/comments/actor where available. reviewProgress DECISIONS_COMPLETE signals pending sign-off; SIGNED plus dateSigned concerns review, not fulfillment. Do not assume modified is decision/sign-off/collection time, or infer deciding actor solely from current reviewer when reassignment exists.

Expected item decisions APPROVED and REVOKED, direct ENTITLEMENT. Summary entitlementDecisions approved/revoked/acknowledged/decisionsMade/decisionsTotal crosschecks item totals per certification; aggregate only after full parent enumeration. No omitted-subject filter, no double counting historical draft/sign-off observations as new decisions. Unexpected ROLE/profile/Acknowledge requires actual-case diagnosis, not case conversion.

Compare actual UI/task/removal evidence separately: account02 Export removed, Read retained and account01 Export retained in historical A4/B6 proof. Current A5 after documented test reset can coexist with signed REVOKED history. Do not re-upload, re-revoke or recreate work to force current state match. Actual application permission would need real connected target evidence; CSV remains simulated.

## Errors, changed case, finish

200 validates request, not complete scope/result. 400 filter/encoding/contract check;401 missing/expired credentials;403 user/scope/object authority;404 wrong tenant/engine/version/object or missing resource, never proof deletion;429 obey Retry-After and bounded later manual read;5xx bounded retry/read failure record. No blind retries, alternative-tenant probes or credential privilege escalation.

Changed case, reasoning only: page0 shows one approved item with limit1 and investigator claims no rejected work. Explain missing pagination and certificate grouping/authority; retrieve remaining pages before concluding. Second factual check: completedtrue alone does not prove sign-off; no invented runtime response needed. No optional endpoint catalogue or token-generation tutorial.

End with private evidence index/scope/completeness/state/removal-versus-reset conclusions and unresolved gaps. Remove temporary local token/session from approved client when done; preserve response originals without secrets. No tenant data reset because no tenant object changed. Next CLS-006 automation may automate this already-understood read process; mutations require their own verified contract and scope, not a generic write payload.

## Author checks

Save a planned request-contract JSON (GET-only, symbolic IDs, no credentials/tenant values, not executable import or API output) for consistent endpoint/pagination review. Full saved beginner read-through and meaningful local validation22 learners,14 CSV unchanged/4 JSON including plan,23IDs; read paths/headers/query/IDs and page-completeness examples reconcile original A/B. Fake pagination tokens are local reasoning data only, never tenant IDs/observations. Actual request/authorization/pagination/API-UI matching/remediation proof/repeat/learner/publication all0.
