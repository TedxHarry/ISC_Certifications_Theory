# X-05: checking all review items across API pages

November 13, 2026. Prepared before the learner draft. The user also explicitly authorized pushing all completed work and Pages after continuation.

Completion update: [CRT-058](../lessons/CRT-058_Checking_All_Review_Items_Across_API_Pages.md) is saved with an editable flow and [claim/review evidence](revisions/CRT-058_Revision_Record.md). The brief below preserves the pre-draft boundary. Publication results are separate observations, not implied by this completion note.

## Distinct task

042/044 establish page-versus-total and API/report literacy. They do not work through record-based offsets, a complete set of pages, duplicate/missing item reconciliation or a changed query/collection during paging.

Add one focused read-only task reference, not a scripting course or another report catalogue. Preserve the thirty-main sequence and existing learners.

## Fresh primary checks

List Review Items API positively establishes GET /certification-campaigns/v1/certifications/{certificationId}/review-items for an identity-campaign certification, required ORG_ADMIN/CERT_ADMIN or reviewer for that certification, Experimental state/header and request/error meanings.

The official Python SDK's exact list-review-items-v1 method supplies limit/offset/count, X-Total-Count and supported filters/sorters. Standard Collection Parameters confirms offset is records skipped from zero, not a page number. Its later combined example has inconsistent page wording; rely on its explicit definition and verified operation/SDK contract, not that example. No code SDK example is copied.

Use one assigned certification's five supplied review-item records, fixed authorized scope, no filters and no changes during the example. limit2 at offsets0/2/4 returns2/2/1. Three pages and matching five unique IDs reconcile against the known expected item set. A response total is scoped by the query/actor and is not whole-campaign/source-removal evidence.

Count=true is used for the actual comparison, without repeated count requests as a rule. Preserve source/account/access context with review-item IDs. Do not confuse repeated entitlement names on different accounts with duplicate items.

## Learner brief

Question: How do you check all review items across API pages?

Explain campaign/certification/item, API/request/response/GET, endpoint, actual IDs, query/header and the supported read-only authority locally.

Normal task asks whether a specific export item is missing from an assigned review. Define the export/read permissions, collect all pages consistently and compare the expected IDs and account contexts. Use an arithmetic table and a compact editable reconciliation flow only where useful.

Changed cases: treating offset1 as page2, silently retaining a completed=false filter, a403 mistaken for an empty list, and item changes between page requests. Supported sorters are not a guaranteed immutable snapshot or unique tie-breaker. Retain observation times and investigate changed-set evidence; do not invent cursor/snapshot APIs.

End by changing the question to a whole campaign with several certifications. A complete single-certification result does not answer that larger population. Scope future bulk work from the actual gap, not a lesson quota.

## Terms and completion

Add four genuinely distinct author meanings: limit, offset, X-Total-Count and sorter. Existing210 becomes214. Pagination/API/reconciliation already exist and gain actual locations.

Complete learner, asset, record and source/author checks before publication. No secrets, actual tenant calls, decision writes, sign-off, exact private states or invented payloads. Record pending actual learner assessment.

The authorized push includes local051–0581.0 and0051.3, current metadata and full source/evidence set. Stage only the course repository's intended work, run local validation, push main, observe Pages deployment, verify live contents/routes and record the actual publication separately. Preserve historical author checkpoints.
