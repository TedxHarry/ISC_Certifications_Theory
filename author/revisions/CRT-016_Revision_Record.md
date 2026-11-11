# CRT-016 author record

Revision 1.0. November 11, 2026.
Learner: [What does this search actually select for the campaign?](../../lessons/CRT-016_Understanding_What_a_Campaign_Search_Selects.md).
Editable diagram: [separate tests versus one account](../../assets/CRT-016_Separate_Account_Tests_and_a_Same_Account_Test.txt).

## Authorization and distinct purpose

The user requested continuation after local CRT-015. This task authors one complete new learner locally; CRT-014/015 and the thirteen-lesson publication remain preserved. The author brief and relevant primary checks were saved before drafting.

Primary COV-11 is query meaning and validation: returned category, exact field/value, operator/grouping, repeated-record scope, actual saved selection and evidence. CRT-013/014 retain full route/refinement comparisons. CRT-017/018 retain configured campaign-filter criteria and combination. This is neither a complete Search syntax reference nor an API procedure.

## Checked primary claims and boundaries

Verified November 11, 2026. The first five references were reopened for this task. Query construction, fields, campaign steps, FAQ/update/data-model passages and relevant overview guidance were inspected; FAQ/overview text was also extracted read-only from the official pages to inspect passages hidden inside long rendered/raw sections. The final three references reuse preceding same-day checks within their stated scope.

| Primary reference | Scoped verification |
|---|---|
| [Building a query](https://documentation.sailpoint.com/saas/help/search/building-query.html) | Field:value, quoted phrases, case-sensitive exact text support, field restrictions, capitalized AND/OR, default OR, parentheses, nested syntax and combined simple/nested conditions. Literal examples are constructed from verified grammar and field definitions, not executed in a tenant. No general precedence, wildcard/regex/date catalog or API syntax contract. |
| [Searchable fields](https://documentation.sailpoint.com/saas/help/search/searchable-fields.html) | Category-specific models and case-sensitive field names; mapped identity attributes; source.name on identity means authoritative source; nested accounts source.name and disabled Boolean. A missing searchable value is not a proven business exclusion. No claim that department/location mappings exist in every environment. |
| [Search campaign creation](https://documentation.sailpoint.com/saas/help/certs/starting_search_campaign.html) | Identity/access selection, all results versus specific additions, later access scope, generated preview and type-dependent assignment. Page marks phased availability and selection/display limits. No automatic account-only scope from an identity predicate, unlimited result claim or assumed live campaign update. |
| [Search FAQ and data models](https://documentation.sailpoint.com/saas/help/search/search_guide.html) | Search data updates can lag record changes; source/entitlement edits have separate synchronization context; sample identity has multiple account records with individual flags and source relationships. No fixed delay or universal job sequence taught. |
| [Search overview](https://documentation.sailpoint.com/saas/help/search/index.html) | Search categories, fields, nested-record syntax and need to inspect actual query construction. No natural-language assistant capability, license or generated-query accuracy claim is taught. |
| [Account loading](https://documentation.sailpoint.com/saas/help/accounts/loading_data.html) | Collected account information versus actual application observation. No fixed refresh interval, source mutation or guaranteed immediate Search reflection. |
| [Account correlation](https://documentation.sailpoint.com/saas/help/accounts/correlation.html) | Correct source-account/person association matters to identity-based selection. No arbitrary ownership repair or invented tenant match. |
| [Understanding certifications](https://documentation.sailpoint.com/saas/help/certs/understanding_certifications.html) | Access model/origin affects which permission/package can appear; selection is not a decision or delivered access change. No unresolved completion/remediation timing claim. |

Primary Search strings use the UI's query language, not campaign-filter-builder combination rules, JSON/API filter syntax or IdentityIQ. A new CAP-16 entry records this independently maintainable query-contract area.

The same-account conclusion follows the documented nested account model and scoped conditions: separate existential account tests can be satisfied by different accounts; one account group tests its conditions on a matching account. The example's local predicate checks validate supplied reasoning, not actual ISC parsing, availability or runtime results.

All seven product questions remain open. Tenant capability/permissions, exhaustive release currency, exact query execution, graphical rendering and actual learner assessment were not observed.

## Actual saved coverage

| Purpose | Saved explanation and evidence |
|---|---|
| Search success versus correct question | Opening distinguishes valid syntax/results from satisfying the intended Finance/Chennai request. |
| Local object and category meanings | Identity/account/source, attributes, query, category, entitlement/profile/role and campaign precede selection reasoning. |
| Field/model/mapping | Location path, colon/value, exact technical names, data model and mapping; configured department/location fields are supplied conditions. |
| Main AND result | 1201 Finance/Chennai matches; 1202 wrong location, 1203 wrong department, 1204 no location, 1205 longer department value do not. |
| Exact text versus phrase | Plain .exact text values check complete value/case; quotes group multiword phrase; case variants need business/data judgment; Boolean fields do not use .exact. |
| OR and grouping | OR expands to all five supplied identities; grouped Finance/Operations plus Chennai gives 1201/1203. No reliance on implicit operator precedence. |
| Repeated-account mechanism | 1301 has disabled Production and non-disabled Test; separate nested tests succeed but same-account combined query fails. |
| Editable relationship diagram | Same two account facts and three questions; no private backend job order. |
| Field-path ambiguity | Identity source is authoritative source; nested account source is its system. Distinct example labels do not replace real source references. |
| Results versus actual selections | 1201/1203 found, only 1201 added in a specific-choice example; access-object definitions behave similarly. |
| Identity match versus review scope | Matching account predicates return identity records; later refinement/filter/eligibility and actual preview/reviewer need separate checks. |
| Data correctness and time | Missing location, source information/mapping/processing/Search, account observation time and avoiding broad OR to hide missing data. |
| Independent transfer | Department plus one non-disabled Warehouse Production account: only 1401; 1402 split accounts, 1403 department and 1404 absent department are distinguished. |
| Changed input | Search later shows 1402 Production false; same predicate then matches 1401/1402, without proving a generated campaign changed. |

Supporting COV-04/05/06/09/10/12/13/15 supplies source/person/model, completeness, selection, filter boundaries, time and preview context. Full later mechanisms remain planned.

Routine task foundations: 1 clarify requirement, 2 data/association readiness, 4 build/validate selection, 7 inspect actual generated contents, 13 investigate missing/different access, 22 compare useful evidence. No full API retrieval, campaign filter, launch or recovery procedure is marked complete.

## Inputs and logical reconciliation

Identity department/location attributes are mapped and searchable under those exact technical names in the supplied environment. Their values are literal plain strings, not patterns. Source labels are distinct in the examples. The tables' No value label means no searchable value is available, not a literal substitute string.

Main records are 1201 Finance/Chennai, 1202 Finance/Pune, 1203 Operations/Chennai, 1204 Finance/no location and 1205 Finance Support/Chennai. AND yields [1201], OR yields all five, and grouped departments plus Chennai yields [1201,1203]. No present-missing value establishes actual organizational membership by itself.

Separate accounts of 1301 are Production true and Test false. The two independent account-existence conditions are true; one account satisfying both production and false does not exist. disabled:false means the recorded flag is false, not successful login or confirmed current target functionality.

Transfer 1401 has Finance/Production false; 1402 Finance/Production true and Test false; 1403 Operations/Production false; 1404 missing department/Production false. The result is [1401]. Changing 1402's Production flag to false in Search yields [1401,1402]. The exercise does not imply that a source change immediately reaches Search.

A read-only ad hoc logical check evaluated these supplied rows with independent predicates for AND, OR, grouped departments, separate/same-account tests and before/after transfer input. All assertions passed. This is not a test of SailPoint's query parser, an API call or an observed tenant campaign.

## Complete saved-file beginner reading

The full saved learner was read in contiguous opening, middle and final portions, including each literal query, the complete nested-account passage and the final worked transfer.

The review replaced exact-string/wildcard jargon with complete plain text value, defined identity attributes and attribute mapping locally, and used a direct identity-record explanation instead of top-level jargon. No value was clarified for both tables. Campaign filter and reviewer meanings were introduced where the generated-work passage needs them. The tenant phrase was replaced with ISC environment.

Edited passages and the ending were reread. Query terms are explained in prose before the result relies on them. The figures, source paths, true/false flags and grouped conditions match the saved explanation. Inline query examples are not mislabeled as teaching-diagram assets; only the actual editable diagram is fenced as text.

No fictional person/company, prior-lesson dependency, source/course URL, teaching-method announcement, revision footer or fixed content quota is used. Author reading is not an observed beginner pass. Actual learner assessment, tenant query execution and visual rendering remain pending.

## Initial executed local checks

All four navigation tests passed against the unchanged published thirteen-entry manifest. Its local verifier passed for thirteen lessons, 1555 normalized content units, thirteen diagrams, fifteen tables and sixteen local editable assets.

The same verifier was run with local CRT-014/015/016 and the planned fourth module added only to its course data in memory. No manifest or verifier code changed. All sixteen local learners passed: 1961 normalized content units, sixteen diagrams, nineteen tables and sixteen editable assets. This is local content/asset validation, not a rendered-navigation test of an unpublished fourth module or a live deployment.

Tracked whitespace checks passed. Final metadata/structure/hash reconciliation follows after execution. CRT-014/015/016 remain local and unpublished; no push is claimed.

## Final saved-package verification

Final local checks completed November 11, 2026:

- The final language pass replaces an early Boolean-fields label with fields storing true or false, and expands missing-location diagnosis into source record, mapped ISC identity value and Search value. Changed saved passages were reread.
- The final in-memory sixteen-learner verification passed: 1961 normalized content units, sixteen diagrams, nineteen tables and sixteen editable assets. The four published-reader navigation tests and unchanged thirteen-entry local verifier passed as recorded above. No new rendered fourth-module or live-site claim is made.
- The inventory contains 91 authored/site files and 58 Markdown documents. All 335 relative Markdown links resolve. All 105 table groups have consistent columns across 1353 rows; fences are closed. Learner/asset/record whitespace and newlines passed.
- Title matches the planned question. The inline account relationship diagram exactly matches its asset; the learner contains no external URLs, fictional-character names, placeholders, course links or revision footer.
- The supplied AND/OR/grouping/same-account/transfer outcomes passed the independent local predicate check. This checks the stated input/result reasoning only; no ISC query, parser or tenant execution occurred.
- Design and candidate inventory retain the same 50 ordered IDs. Sixteen complete learner files exist, no CRT-017 stub exists, 118 distinct working meanings and seven open questions remain. CAP-16 records query-contract scope without resolving OQ-06's campaign-filter ambiguity.
- Pre-task SHA-256 comparison confirms 79 existing files remain byte-identical, including all previous learner/asset/per-lesson records, local CRT-014/015, historical publication evidence, manifest, reader code, verifier and navigation tests. Nine current metadata/author/task files changed. Only this learner, diagram and author record were added.
- Current records consistently identify sixteen authored topics, 34 unwritten candidates, local CRT-014 through CRT-016 and CRT-017 next. The verified live publication remains the thirteen-lesson November 11 snapshot.
- Tracked whitespace checks passed. HEAD remains 41e744d73eb1b000685c1cc6ff770c1ab3e5880c. No commit, push, deployment, source mutation or live campaign action occurred.

Local consistency and source/author review do not establish graphical rendering, observed learner understanding, practical production competence or exhaustive feature currency.
