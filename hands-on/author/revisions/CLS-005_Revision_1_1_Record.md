# CLS-005 beginner-readability revision

Revision 1.1. November 16, 2026.
Learner: [Investigate a certification through read-only APIs](../../lessons/CLS-005_Investigate_a_Certification_Through_Read_Only_APIs.md).
The original [revision1.0 record](CLS-005_Revision_Record.md), [brief](../briefs/CLS-005_Read_Only_API_Investigation_Brief.md) and [planned request contract](../contracts/CLS-005_Read_Only_Request_Plan.json) retain their original stage. The request plan and all CSV/JSON assets are unchanged.

## Complete author reading

Read the original learner, saved revised learner, brief, original record and complete request plan. Followed the existing-case prerequisite, engine and caller checks, request structure, parent/child reads, paging, item matching, state/totals, fulfillment history, errors, reasoning exercise and local cleanup. This is author review, not an independent beginner attempt or executed API investigation.

## Concrete teaching changes

The API client, campaign engine, caller, user level and scopes have local explanations. Initial ISC observations supply the comparison point before API reads. Source A/B and full manager aliases are stated locally.

JSON object/array punctuation and nested field paths are explained without invented response values. Status is separated from response headers. An unsuccessful read cannot supply a parent ID for the next step.

The campaign filter is read in plain English: eq means equals. Encoding, count and sorter settings have specific purposes. Each certification ID comes from the returned certification object. The parent path stays fixed while its child pages change.

A successful empty array differs from a failed or blank response. The existing ten-page bound now explicitly includes the final empty page. A conditional two-item, offsets0/1/2 illustration explains paging without claiming the tenant groups the work that way.

The item table spells out complete source/value paths and explains nativeIdentity. Sign-off, phase, progress and fulfillment meanings precede interpretation. Summary fields are explained before the expected combined1/1/0/2/2 totals; these are planned case counts, never an observed JSON response.

The existing relationship sketch, four tables and first-page reasoning exercise remain. No new endpoint, credential-generation tutorial, write operation, fixture response, object ID, account change or screenshot was added. Historical removal, later reset and current state remain separate.

## Bounded current primary-source checks

Checked November 16, 2026. Public documentation only.

| Primary source | Relevant current check |
|---|---|
| [Get campaign](https://developer.sailpoint.com/docs/api/get-gov-certification-campaign-v-1/) | Selected service path, experimental header and documented actor access. |
| [List certifications](https://developer.sailpoint.com/docs/api/list-certifications-v-1/) | Exact parent filter, parameters/sorter, count and non-admin reviewer view. |
| [Get certification](https://developer.sailpoint.com/docs/api/get-certification-v-1/) | Actual child ID, selected service and authorized read. |
| [List review items](https://developer.sailpoint.com/docs/api/list-review-items-v-1/) | Identity-review items, supported sorter, nested subject/entitlement/source/value/account fields and decision values. |
| [Decision summary](https://developer.sailpoint.com/docs/api/get-decision-summary-v-1/) | Per-certification entitlement counters and made-versus-total distinction. |
| [Certification model](https://developer.sailpoint.com/docs/tools/sdk/typescript/gov_certification/models/certification/) | completed concerns entered choices; progress, phase and sign-off date remain distinct. |
| [Collection parameters](https://developer.sailpoint.com/docs/api/standard-collection-parameters/) | Array results, record-based offsets and filtered count; exercise uses complete bounded reads without snapshot claims. |
| [Authorization](https://developer.sailpoint.com/docs/api/authorization/) | Caller user level, operation scope and object access; a read scope does not automatically establish complete visibility. |

Current operation pages still mark all five selected reads experimental. Public operation search rendering supplied request/schema detail where static page rendering omitted it. No tenant endpoint, experimental availability, actual response schema/value, authority, grouping or pagination was exercised. Original authentication/rate-limit/fulfillment boundaries are retained; no new task API correspondence is asserted. All inherited product questions remain open.

## Planned case and local verification

The case remains two A Export holdings: employee01 APPROVED, employee02 REVOKED. Complete parent and child enumeration precedes the expected combined entitlement totals: approved1, revoked1, acknowledged0, decisionsMade2, decisionsTotal2. Historical A4/B6, possible later A5/B6 restoration and present observations are compared without changing accounts.

The project validator passed across128 reusable files,106 Markdown files,398 project-local links,129 table groups and993 rows. All23 learner IDs,14 CSV fixtures and five JSON assets/contracts reconcile. Original baselineA hashes are unchanged; no request plan, collector code or fixture was edited.

The five GET operations and two-holding scope remain consistent. Existing offline pagination checks accept a complete capture and independent parent/child offsets, while rejecting truncated, duplicate, changing-count and skipped-offset captures. These are reasoning checks, not tenant response examples. The collector's earlier25 offline test methods were not rerun for these prose changes. No local check establishes actual authority, response completeness, API/UI correspondence or historical fulfillment.

## Actual state and next work

No token, tenant URL, actual compatible history or authenticated API response was supplied or inspected. Actual requests, authority/visibility checks, UI matching, historical fulfillment verification, repeat captures and independent learner tests remain0. Maintenance remains the last user-reported tenant status.

Twenty-two of23 fresh complete learner readings are covered: all17 main units plus CLS-001 through005. Next is CLS-006; one learner reading remains. Later course-wide consistency/packaging and all tenant testing remain separate work. Local only; no repository, push or Pages action.
