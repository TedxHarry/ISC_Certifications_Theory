# CLB-008 author and source record

Revision1.0. November14,2026.
Learner file: [Investigate missing and unexpected review items](../../lessons/CLB-008_Investigate_Missing_and_Unexpected_Review_Items.md).
Prepared from the saved [brief](../briefs/CLB-008_Review_Content_Investigation_Brief.md), teaching specification, environment record and unchanged A/B fixtures.

## New practical task

Diagnose a same-count wrong preview, trace two symptoms to separate campaign inputs and verify controlled repairs. This develops005's selection concepts into a reproducible investigation. Unlike007, it does not change source data or schedule future work. It does not repeat an end-to-end review/removal exercise.

The correct requirement is A Export for employee01/02 with manager01. The faulty configuration adds only employee01 and both A Read/Export. The missing employee02 Export and extra employee01 Read have different causes.

The administrator creates three separate immediate previews and their unscheduled saved configurations. They remain unstarted. This avoids inventing an Edit, Duplicate or Regenerate operation and preserves evidence from each generation. There are no intended account, manager, model, source, filter or CSV changes. The existing [A package](../../lab-data/baselineA/README.md) and [B package](../../lab-data/baselineB/README.md) are reused.

## Current primary checks

Checked November14,2026. Documentation support is not tenant execution or an exhaustive update audit.

| Primary source | Bounded use |
|---|---|
| [Starting a campaign from Search](https://documentation.sailpoint.com/saas/help/certs/starting_search_campaign.html) | Candidate search versus specific added identities, Refine Access Items, optional filter, Manager choice and immediate preview plus saved configuration. Distinct new configurations use the documented creation flow rather than assuming an unsupported existing-preview edit. |
| [Building search queries](https://documentation.sailpoint.com/saas/help/search/building-query.html) | Reuse of the exact-name two-person query and OR meaning already checked for005/007. No new dynamic query behavior is inferred. |
| [Loading account data](https://documentation.sailpoint.com/saas/help/accounts/loading_data.html) | Collected account facts, aggregation history and separate Search freshness checks. No fixed delay or automatic recorrelation result is claimed. |
| [Using campaign filters](https://documentation.sailpoint.com/saas/help/certs/campaign_filters.html) | A filter is an additional selection condition; the normal experiment leaves it empty. Profile/entitlement distinctions support first-check triage, not a new model experiment. |
| [Understanding certifications](https://documentation.sailpoint.com/saas/help/certs/understanding_certifications.html) | Review-item representation and distinction between individual rights and higher-level access items. Item totals are not equated with assigned certification-object totals. |
| [Completing a certification campaign](https://documentation.sailpoint.com/saas/help/certs/completing_campaigns.html) | Retire only unused saved configurations and never-started previews after preserving evidence. No deletion effect on active delivery or rollback is inferred. |

Actual engine availability, account/identity records, stored selections, generated scope/grouping, reviewer routing and cleanup remain runtime checks. The expected result assumes the stated baseline and no model/filter changes. A different actual result is retained as a mismatch rather than forced by granting access or changing source data.

## Saved beginner read-through

The saved learner file was read in full. Campaign, preview, subject, reviewer, identity, source, entitlement, holding, query and account correlation receive local meanings. Supporting definitions are placed at the action that needs them.

The explanation separates a search candidate from an added person and an existing permission from one selected for review. It follows employee02's missing holding through account data, identity association, Search and the added list, then separately follows the unexpected Read through the access selection.

The language pass clarifies that campaign instances are unstarted while their saved configurations are unscheduled. Added-list evidence is captured before leaving the builder; current Search results are not treated as historical proof of a previous added selection. Source/model/manager data is not changed merely to force a preferred preview count.

Two tables serve different tasks: the precise requirement and the controlled repair sequence. No screenshot, diagram or table quota is imposed. No fictional company, continuing character, learner citation/course links or invented tenant result is used.

The exercise reverses the correction order. It lets a learner explain a partial one-holding result before opening the worked reasoning, without adding another compulsory generated campaign.

## Local expected sets

Initial: employee01's A Read and Export, two holdings. Compared with the two required Exports, one holding matches, employee02 Export is missing and employee01 Read is extra.

People-only correction: employee01/02 A Read/Export, four holdings. Both required Exports are present, but two Read holdings remain outside scope.

Final: employee01/account01/A Export and employee02/account02/A Export, exactly two correct source-specific holdings. The reverse-order exercise gives one employee01 Export holding before employee02 is added.

All seven CSVs remain unchanged. A retains three accounts/five holdings, B four accounts/six holdings. Both employees' manager01 links remain the same. These are local fixture calculations, not generated previews, actual selection repairs or tenant observations.

## Evidence and restoration

Retain the requirement, each symptom/cause, account/identity checks, candidate and added-list evidence, actual selections, source references, settings and three preview/template IDs/times. Change one campaign input at a time and compare its full result.

Confirm no activation, decisions, removal work or schedule. Reconcile any accidental dependency or active work before routine cleanup. Retire only unused008 configurations and unstarted008 instances after preserving evidence. Verify A five/B six and original relationships; no CSV reset is needed when those inputs remained unchanged.

The short branching guide points to first checks for source data, associations, query/Search, selections, access models and reviewer choice. It is not a blanket repair procedure. It does not execute Role/account-filter edge experiments, change correlation or manager mappings, or claim completion of those tasks. Existing responsibility transfer is owned by009. OQ-06/08 and every other inherited question retain their prior status.

## Actual status

Local validation passed47 files,38 Markdown documents,93 project-local relative links and45 consistent table groups across375 rows. The design/register agree on23 planning IDs and eight complete learner files. All seven CSVs retain checked structure, relationships and exact expected-result files; original A hashes remain unchanged. The008 fixture produces two initial holdings with one missing/one extra, four after correcting people, two exact required Exports after narrowing access, and one for the reverse-order partial correction. A five/B six are preserved. Earlier003 diagram-source,005 query/source-scope,006 filter/model and007 next-cycle checks still pass. Fences, answer wrappers, whitespace and absence of learner source/course links pass. These are local document/data checks, not actual generated previews or tenant repairs.

Authored/source/language reviewed:008 revision1.0. New CSV files:0. Actual tenant imports, queries, configurations, previews, selection repairs, activations, decisions, tasks, screenshots, cleanup operations, repeated runs and independent learner tests:0. No repository, push or Pages action. This course remains local.
