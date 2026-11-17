# CLB-005 author and selection record

Revision 1.0. November 14, 2026.
Learner: [Target people and access through Search](../../lessons/CLB-005_Target_People_and_Access_Through_Search.md).
Prepared [brief](../briefs/CLB-005_Targeted_Search_Review_Brief.md).
Inputs reuse [baselineA](../../lab-data/baselineA/README.md) and [baselineB](../../lab-data/baselineB/README.md).

## Distinct authored result

The complete targeted Search procedure separates identity results, explicitly added identities, refined source-specific access and generated review holdings. It selects exactly employee01/02 and Export Reports on the original A source.

No new source or CSV file was necessary. A and B give the same selected people eight fixture holdings, including two indistinguishably named Export definitions on different sources. The intended set has only two A holdings; the wrong-source example also has two holdings, demonstrating why counts/names are insufficient.

The complete run includes one Approve/one Revoke, final confirmation, actual source-owner manual work, simulated A file removal, wider data checks and reset. The existing A expected result is reused; B remains unchanged.

## Primary documentation checks

Official ISC pages were opened on November 14. No tenant UI, Search request, campaign, source upload or actual preview was observed.

| Reference | Bounded support |
|---|---|
| [Search campaign creation](https://documentation.sailpoint.com/saas/help/certs/starting_search_campaign.html) | Explicit identity selection, Refine Access Items, Manager reviewer and preview/template configuration. |
| [Query construction](https://documentation.sailpoint.com/saas/help/search/building-query.html) | Fixture query uses name.exact, quoted identity names and OR. Includes a documented quoted-hyphen name example; no generalized punctuation rule is inferred. |
| [Searchable fields](https://documentation.sailpoint.com/saas/help/search/searchable-fields.html) | Identity name is a search field; source-specific entitlement identity must be inspected. |
| [Search overview](https://documentation.sailpoint.com/saas/help/search/index.html) | Query/field/operator meanings and separate searchable categories. No indexing delay or refresh recipe is claimed. |
| [Reviewer operations](https://documentation.sailpoint.com/saas/user-help/certs/reviewing/index.html) | Active assigned work, Approve/Revoke and final Finish. No post-sign-off correction promise. |
| [Task Manager](https://documentation.sailpoint.com/saas/user-help/task_manager.html) | Inspect actual task, changed file collection, then Mark Complete. |
| [Campaign reports](https://documentation.sailpoint.com/saas/help/certs/campaign_status_reports.html) | Source/account/decision/sign-off/remediation evidence and current report generation. |

The query is source-supported author input, not a tested tenant query. Actual names, identity IDs, entitlement object/source, engine and allowed actions require inspection. No backend storage or universal query-to-review projection is invented.

## Important route decisions

Use Specific Identities that I Select, then Refine Access Items. Do not use a new campaign filter or teach the original identity query as an access filter. CLB-006 retains campaign-filter experiments and package/role variation.

The chosen immediate-preview-and-template option explicitly retains a saved configuration and leaves it unscheduled. The other immediate option mixes preview/start wording in the guide; the author does not guess a combined activation action. A checked preview precedes Start Campaign. Saved template state, active review and recurrence are distinct.

Known manager links route the two subjects to manager01. Actual review grouping and final confirmation are checked per assigned object; two holdings are not assumed to be two certification objects. Source-owner removal work is separately inspected.

All normal reviewer work is finalized. Unsigned administrator completion, owner fallback, legacy/new-engine parity, post-sign-off edits and fixed processing timers are not tested or declared resolved.

## Beginner author reading

Read the whole saved learner through its final reset, including the full changed-case answer. Rechecked the changed supporting passages.

The explanation starts with the actual small request and states included/excluded records. Identity, source, entitlement, subject, reviewer, holding and query meanings precede the choices that depend on them.

The exact-name query is explained as a people search. The added identity list and the added entitlement list are checked separately. The same display/value on B is shown as a different source-specific access item.

The first language pass named A/B directly in the starting table, replaced compressed setting wording with connected sentences and put preview/template and sign-off meanings before those actions. It clarifies complete private template-aligned files instead of relying on an unexplained short phrase. The brief's query quotes were normalized to the same literal input as the learner.

Business evidence justifies one approval and one removal. The unchanged B Export is distinguished from a failed A removal, and all retained rights remain part of the outcome check.

Two tables serve the actual task: exact requested holdings and the larger starting data. A new diagram would repeat a selection already visible in those tables, so no diagram quota or screenshot was imposed.

No fictional company, continuing character, learner source/course links, new source quota or fake tenant result was added.

## Local reconciliation scope

The existing people data supplies exactly the two named identities and manager01 relationship. Their A/B fixture holdings total eight. The intended source-specific Export subset has two; B's same-name Export subset also has two and fails the source requirement.

Removing only employee02's A Export preserves A's three accounts and four holdings. B's four accounts and six holdings remain unchanged. Both catalogues and all seven canonical CSV files are preserved.

This is local data/query-input reconciliation, not an actual Search result, generated preview, final sign-off or remediation observation.

## Actual status

Local validation passed38 files,29 Markdown documents,68 project-local relative links and35 consistent table groups across315 rows. The design/register agree on23 planning IDs and exactly five complete learner files. All seven existing CSVs retain their checked structure. The two selected people have eight A/B fixture holdings; the intended A subset and incorrect B alternative each have two, with distinct source-scoped tuples. Query text agrees between brief and learner, original A hashes are unchanged and the existing A/B output checks pass. Fences, answer wrappers, whitespace and absence of learner source/course links passed. The separate theory repository remains clean at1f1028a89ba8d266c80710dc5424dcafd160760d.

Authored/source/language reviewed:005 revision1.0. New CSV files:0. Actual tenant queries, imports, templates, campaigns, reviewer work, tasks, screenshots, repeated runs and independent learner tests:0. No repository or publication action.
