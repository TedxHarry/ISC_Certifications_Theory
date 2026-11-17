# CLS-005 revision1.0 author record

November15,2026. Complete authored/source/language-reviewed guide. No authenticated API request, tenant action, repeat, independent learner test or publication.

Learner: [Investigate a certification through read-only APIs](../../lessons/CLS-005_Investigate_a_Certification_Through_Read_Only_APIs.md).
Prepared from the saved [brief](../briefs/CLS-005_Read_Only_API_Investigation_Brief.md) and [planned request contract](../contracts/CLS-005_Read_Only_Request_Plan.json).

## Concrete scope and prior evidence requirement

Read one actually executed next-generation identity campaign, preferably a compatible CLS-004 instance, containing the two A Export holdings. This unit does not manufacture the prerequisite campaign/history or change current permissions. All project tenant runs remain0; no such case is claimed to exist here.

Separate actual campaign ID from template ID; assigned certification ID, item ID, subject-summary ID, target identity ID, entitlement/source/account IDs remain distinct. Enumerate all authorized parent/child collections before claims about complete scope. Record caller-limited view explicitly. Historical review, manual fulfillment, later test reset and current account state require separate evidence.

No CSV creation/upload/change, task closure, report generation, decision/reassignment/sign-off, campaign activation/completion/deletion or credential promotion. GET request plan has no server/token/actual object IDs. It is a planned contract, not an API-client import or observed response. Preparation of a compatible review or access token belongs before this unit.

## Current primary checks

Checked November15,2026. Focused public request/response contracts; no tenant endpoint, actual permissions or experimental availability tested.

| Primary source | Supported use and qualification |
|---|---|
| [Service-version migration](https://developer.sailpoint.com/docs/api/api-versioning-migration/) | Per-service paths distinguish next-generation certification-campaigns/v1 from older service families. No blanket shutdown claim for prior versions and no inferred engine migration. |
| [Get next-generation campaign](https://developer.sailpoint.com/docs/api/get-gov-certification-campaign-v-1/) | GET campaign by actual ID, current experimental header and documented caller roles/reviewer access. Not a saved template. |
| [List certifications](https://developer.sailpoint.com/docs/api/list-certifications-v-1/) | campaignRef.id filtering, limit/offset/count/supported sorter, authorized visibility and required reviewer-identity=me for non-admins. Do not copy the generic unsupported name-filter example. |
| [Get certification](https://developer.sailpoint.com/docs/api/get-certification-v-1/) | Child lookup by its actual ID, caller access and parent relationship. |
| [Review items](https://developer.sailpoint.com/docs/api/list-review-items-v-1/) | Identity-campaign entitlement items, pagination, actual decision and subject/target/source/account fields. Preserve opaque IDs; no fabricated GUIDs or fixture response. |
| [Decision summary](https://developer.sailpoint.com/docs/api/get-decision-summary-v-1/) | Per-certification entitlement counts with no hidden subject filter; complete enumeration precedes aggregation. |
| [Certification model](https://developer.sailpoint.com/docs/tools/sdk/typescript/gov_certification/models/certification/) | completed is all decisions entered; phase/reviewProgress/dateSigned/reviewer are separate evidence. DECISIONS_COMPLETE is not sign-off. |
| [Authentication](https://developer.sailpoint.com/docs/api/authentication/) and [authorization](https://developer.sailpoint.com/docs/api/authorization/) | Prepared bearer access token, actual caller, user-level/object authority and per-operation least read scope. No sp:scopes:all or privilege escalation as automatic error repair. |
| [Collection parameters](https://developer.sailpoint.com/docs/api/standard-collection-parameters/) | Record-based offsets, array results/counts and explicit complete paging. No assumption of atomic snapshot or fixed global dataset. |
| [Rate limiting](https://developer.sailpoint.com/docs/api/rate-limit/) | Respect actual Retry-After for429 and bounded attempts; no rapid blind retry or universal throughput promise. |
| [Certification task model](https://developer.sailpoint.com/docs/tools/sdk/typescript/gov_certification/models/certification-task/) | API task targets/types/status do not establish mapping to a manual entitlement-removal work item. Actual fulfillment uses existing matching UI/task/file/collection evidence. |

All five selected service operations are currently marked experimental and require X-SailPoint-Experimental:true. A v1 path alone is not stable/public status. Verify actual engine/contract/allowed experimental use for the run. Body parameter/response details were checked through primary operation search rendering and current SDK model where the static page omitted hydrated schema. Operation examples for another engine or unrelated endpoints are excluded.

Several guessed model leaves and a guessed single-review-item endpoint were unavailable; they do not support a contract. The public item-list schema supplied the required entitlement/account mapping. The documentation edit link opened an issue-template destination and was not used for authoring evidence or submission. No issue/message was sent. No unsupported direct item/task mapping or report-creation call was added.

## Meaning and completeness checks

The saved lesson starts with the practical investigation and introduces API/GET/URL/path/query/headers/response/JSON/array and nested field notation before the learner relies on them. It scopes one API family rather than teaching several competing engine implementations. The existing authorized actor and token are checked separately from browser access.

Manual requests deliberately use limit1 so a successful first page cannot hide missing work. Each parent/child collection starts at offset0 and advances by returned record count, preserves its query, checks unique IDs/reported total and reads through an empty terminal page. Ten-page bound is local exercise scope, not API maximum. Supported sorting does not freeze underlying data. Duplicate IDs or changing counts leave capture incomplete; no silent deduplication to pass.

The complete set matches two actual person-source-account-Export tuples, not two certifications. Decision summary is crosscheck, not a substitute for items/authority/sign-off. Any missing mapping, unrelated B right, unreviewable unit or changed scope remains a gap. Current reviewer is not automatically every item's actor after reassignment.

Historical A4/B6 result and later A5/B6 reset may both be valid at their own times while the same signed REVOKED item persists. Current account observation cannot establish a missing historical removal. No new rejection/upload is performed to force consistency. CSV outcome is simulated application work; actual external capability needs real target observations.

## Full saved beginner read-through

Read the entire saved learner procedure through prerequisite case, family/authority, request structure, parent lookup, all parent pages, each child/items, fields, sign-off/summary, fulfillment/history/current state, errors, changed-page reasoning and cleanup. Read planned request JSON for consistent paths, parameters and symbolic bindings.

Clarified the API contract meaning and protected authentication-header setup. Replaced compressed limit1/offset0 instructions with explicit parameter=value notation and replaced atomic-snapshot jargon with an explanation of data changing between pages. Kept only the response fields needed for this two-item task rather than reproducing entire schemas or SDK output. Examples are request templates and clearly labelled reasoning, never fabricated tenant responses.

Four focused learner tables serve known scope, query parameters, item mapping and error investigation. The relationship sketch is plain quoted text. No fixed diagram/table quota, fictional company, continuing character, learner source/course links or invented screenshot/ID/status. Optional broad endpoint catalogues and token-generation tutorials are omitted.

## Local verification

The full-course validator passes across104 course files:85 Markdown,260 resolving project-local links,106 consistent table groups/810 rows,23 reconciled design/register IDs and22 complete learner files. All14 canonical CSVs remain checked and unchanged;4 JSON assets/contracts parse. Original A hashes, prior diagram and005–017/D/E/F/context example checks remain passing. Learner links/stubs, fences/details wrappers, whitespace and final newlines pass.

The request plan validates exactly five whitelisted GET paths, experimental/nonsecret headers, protected token prerequisite, narrow parent filter, reviewer-view parameter, correct list sorters and no body/hidden completed or subject filter. Its symbolic IDs and exact A two-holding expected scope reconcile the existing final one-approval/one-rejection result and historical-versus-restored account states. An initial cross-file check found abbreviated account aliases in the brief; full certlab-account01/02 aliases were added and the fresh run passes.

Offline reasoning checks accept a complete two-item capture and separately restarted parent/child offsets. They reject a first-page-only capture, missing terminal page, duplicate ID, changing count and skipped offset. These local keys are not ISC response examples or tenant object IDs. They establish pagination reasoning, not server behavior, authority or complete runtime data. Actual API/visibility/pagination/UI/fulfillment flags remain false. No authentication, API request, real page, actual permission/visibility/response match or fulfillment outcome has occurred.

## Remaining evidence and next unit

Actual API/tenant execution, repeated captures and independent learner tests remain0. Experimental availability, token authority, real historical case, endpoint response shape/IDs/pages and API/UI/task/current-state correspondence need an actual run. Existing product questions remain open. No repository/push/Pages action.

Next CLS-006 should automate a narrowly defined task only after this manual read process works. Prefer automating the verified bounded evidence collection before adding writes. Mutation-specific contracts, authority, scope/duplicate/recovery controls and tenant validation cannot be inferred from this GET-only plan.
