# Capability, update and open-question register

Version 4.1. November 11, 2026.
Source leads: [official source map](../AUTHOR_SOURCE_MAP.md).
Purpose: stop unsupported current/legacy/availability claims entering lessons.

A documentation scoping check is not a tenant test or final lesson verification. Exact relevant claims must be checked when the lesson is written and before affected publication. No exhaustive release-by-release audit or tenant-specific availability check has been completed.

## Working baseline

Use next-generation campaign examples where supported. Mark a bounded legacy or conditional case when relevant. The current official overview describes phased availability and migration; the next-generation API is marked Experimental. Do not label a capability generally available merely because it appears in documentation.

The administrative help paths currently use Identity Services/Human Fabric headings. This course retains ISC naming and does not import similarly titled IdentityIQ or File Access Manager behavior.

## Capability inventory

The original CAP-01–14 scoping rows date to October 29, 2026; later dated authored applications give their actual claim checks. CAP-15 was added October 30, 2026 with CRT-005. CAP-16 was added November 11, 2026 with CRT-016. “Scoping checked” is planning evidence, not verification of an unwritten lesson or a tenant run.

| Key | Capability / claim area | Engine and availability handling | Primary source and current check | Affected topics |
|---|---|---|---|---|
| CAP-01 | Purpose, campaign/review objects and administrator responsibility | Stable concepts; actual permission/actions checked for applicable engine. | [Overview](https://documentation.sailpoint.com/saas/help/certs/index.html), scoping checked and refreshed during setup. | CRT-001–004/021/022 |
| CAP-02 | Next-generation migration and APIs | Overview describes phased availability; API marked Experimental and engine-scoped. No universal tenant-availability claim. | [Overview](https://documentation.sailpoint.com/saas/help/certs/index.html), [next-generation APIs](https://developer.sailpoint.com/docs/api/next-generation-certification-campaigns/), refreshed during setup. | All affected flows; X-05 |
| CAP-03 | Role-composition review | Current overview/search guidance keeps it legacy; recheck before deeper authoring. | [Search campaign guidance](https://documentation.sailpoint.com/saas/help/certs/starting_search_campaign.html), refreshed November 11 for CRT-015: legacy composition, eligibility and selected permitted manual remediation owner. | CRT-015; X-01 |
| CAP-04 | Certifiable access and assignment origin | Exact unit/origin controls actions: requested role Approve/Revoke, criteria-role Acknowledge, profile/entitlement containment and lifecycle exclusions. No universal package-removal result. | [Understanding certifications](https://documentation.sailpoint.com/saas/help/certs/understanding_certifications.html), [reviewer guidance](https://documentation.sailpoint.com/saas/user-help/certs/reviewing/index.html), refreshed November 11 for CRT-028. | CRT-006/007/028/035 |
| CAP-05 | Manager/source-owner versus targeted selection | Verify campaign-specific data prerequisites, exclusion and fallback behavior; do not combine different routes into one rule. | [Manager/source-owner campaigns](https://documentation.sailpoint.com/saas/help/certs/starting_campaign.html), [Search](https://documentation.sailpoint.com/saas/help/certs/starting_search_campaign.html), scoping checked. | CRT-011–016/023 |
| CAP-06 | Filters and access refinement | Verify criteria scope and grouping/combination; no assumed SQL semantics or inclusion/exclusion precedence. | [Campaign filters](https://documentation.sailpoint.com/saas/help/certs/campaign_filters.html), refreshed November 11 for CRT-017: criterion/mode, display matching and documented UI alternatives; Role and mixed-account scope remain bounded. | CRT-014/017/018 |
| CAP-07 | Generation, templates, schedules and preview | Verify what is generated, when values are captured, and which step requires activation. No all-field immutable snapshot or automatic refresh assumption. | [Search creation](https://documentation.sailpoint.com/saas/help/certs/starting_search_campaign.html), [dedicated creation](https://documentation.sailpoint.com/saas/help/certs/starting_campaign.html), refreshed November 11 for CRT-019–021: bounded capture/freshness, reusable settings and generation/start separation, actual preview acceptance and verified authorized launch. No universal field-propagation or automatic business-gap validator. | CRT-019–021 |
| CAP-08 | Reviewer routing and self-certification | Verify owner hierarchy, group behavior, fallback and self-review handling for the exact campaign. | [Understanding certifications](https://documentation.sailpoint.com/saas/help/certs/understanding_certifications.html), [Search](https://documentation.sailpoint.com/saas/help/certs/starting_search_campaign.html), scoping checked. | CRT-022–024 |
| CAP-09 | Reassignment and reviewer visibility | Verify exact unit, actor/state/recipient, whole versus identity-campaign subject/item scopes and current result. Configured as-created redirection has separate type/period/recipient/feature and end/replacement boundaries. Experimental API scope is not universal UI/state support. | [Reassignment](https://documentation.sailpoint.com/saas/help/certs/config_reassignment.html), [whole certifications](https://developer.sailpoint.com/docs/api/move-certifications-v-1/), [subjects/items](https://developer.sailpoint.com/docs/api/move-subject-and-items-v-1/), [Work Reassignment](https://documentation.sailpoint.com/saas/help/users/work_reassignment.html), [user-help configuration/history](https://documentation.sailpoint.com/saas/user-help/accounts/work_reassignment.html), refreshed November 11 for CRT-025/026. | CRT-025/026/045 |
| CAP-10 | Decisions, sign-off, unsigned completion | Normal next-generation saved/all-decided versus signed is verified; OQ-01 unsigned administrator completion and OQ-10 broader edit wording remain unresolved. | [Understanding](https://documentation.sailpoint.com/saas/help/certs/understanding_certifications.html), [Completion](https://documentation.sailpoint.com/saas/help/certs/completing_campaigns.html), [Finalize](https://developer.sailpoint.com/docs/api/process-sign-off-certification-v-1/), refreshed November 11 for CRT-030. | CRT-028/030/039/040/041 |
| CAP-11 | Revocation timing and remediation phase | Verify exact trigger/date/state for the engine; see OQ-02. Do not infer a universal private sequence. | [Understanding](https://documentation.sailpoint.com/saas/help/certs/understanding_certifications.html), [API overview](https://developer.sailpoint.com/docs/api/next-generation-certification-campaigns/), scoped, exact timing unresolved. | CRT-003/032–040/046 |
| CAP-12 | Manual/automatic fulfillment, overlap and failures | Verify source write permission, supported operation, actual task assignment and grant paths. | [Reviewer guidance](https://documentation.sailpoint.com/saas/user-help/certs/reviewing/index.html), [Completion](https://documentation.sailpoint.com/saas/help/certs/completing_campaigns.html), scoping checked. | CRT-033–037/046 |
| CAP-13 | Notifications, deadlines, reports and retirement | Verify settings/state/engine and report availability. Decision Comments/status Comments and current reviewer/decision actor differ; report freshness does not prove target change. | [Completion](https://documentation.sailpoint.com/saas/help/certs/completing_campaigns.html), [Reports](https://documentation.sailpoint.com/saas/help/certs/campaign_status_reports.html), report fields refreshed November 11 for CRT-029. | CRT-029/038–044 |
| CAP-14 | Reviewer descriptions/context and specialist capability | Core context is taught; exact licensed/phased/type/display scope remains bounded. Flags, recommendations and source activity answer different questions. | [Reviewer guidance](https://documentation.sailpoint.com/saas/user-help/certs/reviewing/index.html), [recommendations](https://documentation.sailpoint.com/saas/help/ai/access_recs/recommendations.html), [Activity Insights](https://documentation.sailpoint.com/saas/help/ai/activity_insights/index.html), refreshed November 11 for CRT-027; scoped cloud/data/privilege checks in its record. | CRT-008/009/015/027/031; X-01–05 |
| CAP-15 | Source/account data, schema and identity association | Source-supported collection, account versus catalog data, correct correlation and observation time; no universal connector contract or refresh duration. | [Account loading](https://documentation.sailpoint.com/saas/help/accounts/loading_data.html), [schemas](https://documentation.sailpoint.com/saas/help/accounts/schema.html), [correlation](https://documentation.sailpoint.com/saas/help/accounts/correlation.html), refreshed November 2, 2026 for CRT-008's account-specific teaching; earlier CRT-005 check remains historical. | CRT-005/008/009/010/019/045 |
| CAP-16 | Search query fields and matching semantics | Verify category-specific field paths/types, exact text, operators/grouping and nested-record scope; separate query grammar from campaign filters and API contracts. | [Query construction](https://documentation.sailpoint.com/saas/help/search/building-query.html), [fields](https://documentation.sailpoint.com/saas/help/search/searchable-fields.html), [FAQ/models](https://documentation.sailpoint.com/saas/help/search/search_guide.html), checked November 11 for CRT-016's scoped examples; no tenant execution. | CRT-016/044/045 |

## CRT-008 authored application, November 2, 2026

[CRT-008's record](revisions/CRT-008_Revision_Record.md) documents thirteen primary checks. CAP-15 supplies exact account/source/identifier context, multiple accounts on one identity, collection, correlation and observation time. CAP-04/12 support the scoped direct-entitlement decision and actual target result. CAP-14 supplies recognition of conditional uncorrelated and machine-account review routes. CAP-02's Experimental limitation applies to the two inspected next-generation read API references; no request, response payload or universal tenant capability is claimed.

The main example confirms the precise account-specific target before following removal. It does not assert that every UI item maps to one account or permits a separate decision for each account. The service-account section distinguishes responsible human ownership from a personal login and supplies no universal reviewer fallback. Source comparison discovered OQ-07 below. Seven product questions remain open; this bounded learner does not require their resolution.

## Open questions

| Question | Evidence / unresolved point | Writing treatment and next verification |
|---|---|---|
| OQ-01: Unsigned decisions at administrator completion | Understanding guidance treats unsigned reviews as undecided at completion; completion guidance also says saved manager decisions may be preserved. CRT-030 freshly investigated both passages, the direct administrative Complete body and targeted ISC sources without establishing reconciliation. Normal reviewer sign-off is verified, but no authoritative universal unsigned-result or tenant observation exists here. | Establish exact engine/type, recheck current guidance and seek authoritative clarification or explicitly permitted controlled observation. Do not assign either description universally. CRT-030/039/040 need resolution or a clearly verified narrower scope. |
| OQ-02: Exact remediation trigger and campaign phases | Administrative guidance describes initiation at sign-off; developer overview also describes a campaign-level remediation phase after reviewers finish. CRT-028 directly checked the Experimental Finalize operation, which finalizes decisions and initiates needed remediation. These are scoped contracts, not an established universal phase relationship or target-completion result. | Verify the engine-specific event/state path before exact timing diagrams or claims. Stable purpose and the distinction between decision/delivery/evidence can be taught without inventing that timing. |
| OQ-03: Exact tenant capability and permission matrix | No target tenant, entitlement/license inventory or actual user-level test has been supplied or inspected. | Teach verified documented conditions. Identify prerequisites per affected lesson; do not claim screenshots or behavior observed in a tenant. |
| OQ-04: Exhaustive current-update coverage | Ten primary scoping sources have been reviewed; this is not a release-by-release completeness audit. A discoverable announcement FAQ failed direct retrieval in the earlier check. | Recheck authoritative release information during authoring/publication, maintain the change log below and record unavailable evidence. Do not promote roadmap/search snippets to released behavior. |
| OQ-05: Manual-task recipient scope | Certification Understanding guidance names the source owner; the general provisioning overview says manual entitlement tasks go to the entitlement owner with source-owner fallback. Their process/engine scope relationship has not been established here. | Inspect actual task assignment in CRT-003; verify the exact certification path before CRT-034 recipient/routing claims. No universal owner rule is inferred. |
| OQ-06: Role-filter selection unit | The filter guide introduces a Role criterion in terms of roles but its examples describe role-member identity inclusion/exclusion. The exact object/subject effect for the supported engine/type is not established here. | Before CRT-017/018/045 role-filter unit claims, verify scoped documentation or explicitly permitted generated evidence. CRT-007 uses only the supported single-entitlement exclusion and does not infer a universal role-filter model. |
| OQ-07: Overlapping access-profile entitlement removal | On November 2, 2026, the reviewer guide says a common entitlement is retained when revoking one of two profiles, while the access-profile administration guide says overlapping entitlements between profiles are revoked. The process/engine/assignment scope explaining the difference has not been established. | Before CRT-035/046 or specialist overlap outcomes, verify the exact assignment, operation and engine with authoritative evidence. CRT-004 1.1 promises no shared-permission protection; CRT-008 excludes package/automatic requirements from its account-specific example and verifies actual account results. [Reviewer guide](https://documentation.sailpoint.com/saas/user-help/certs/reviewing/index.html), [profile administration](https://documentation.sailpoint.com/saas/help/access/access-profiles.html). |
| OQ-08: Account-attribute filter effects across accounts/sources | Newly recorded November 11 during CRT-017. The guide describes matching certification items and gives a people-worded example; current overview/API metadata do not establish effects on the same person's unrelated accounts or access. This is an unestablished scope, not a proven defect or conflict. | CRT-017 uses one source/one account per identity only. Before mixed-account outcomes in CRT-018/045, establish the exact criterion, route and retained/omitted work through authoritative clarification or explicitly permitted controlled preview evidence. No automatic person-wide or account-only propagation is inferred. |
| OQ-09: Terminal missing ownership in Search certification routes | November 11 CRT-023 checks establish Account Owner source fallback and Access Owner ownership sequence, but not the exact final recipient/status for each type/engine when the expected owner and final source owner are both absent. Targeted official-source searches did not establish a terminal certification contract; access-request escalation is a different process. | Teach verified ordinary fallback, restore supported responsibility and inspect actual generated work/error. Before a terminal outcome claim in CRT-023/045 or specialist account routes, obtain scoped authoritative clarification or explicitly permitted controlled observation. No universal creator, Org Admin, unassigned or error result is invented. |
| OQ-10: Editing after review completion/sign-off | Recorded November 11 for CRT-030. Reviewer guidance permits revisiting until sign-off but also says decisions can change after completing a certification; its final section and next-generation overview say submitted/signed decisions cannot change. The distinction between item-completed, certification-finalized and engine-specific correction paths is not fully reconciled. | Teach verified normal next-generation read-only sign-off and permitted unsigned changes. Before a post-sign-off correction/reopen claim in CRT-030/041/043, obtain exact engine/state/action authority and scoped primary clarification or explicitly authorized observation. Do not invent Undo, signed-work reassignment or an all-engine editing permission. |

These questions affect particular claims. They do not block writing the verified purpose and business reasoning in CRT-001.

## First authored application

CRT-001 revision 1.0 uses CAP-01's stable purpose/objects, a bounded CAP-04 individually reviewable entitlement and CAP-12's distinction between a removal decision and its applicable delivery. Six official pages were freshly checked October 29, 2026 in [the lesson record](revisions/CRT-001_Revision_Record.md).

It explains finishing/confirming a review but makes no exact unsigned-completion or universal remediation-phase timing claim. OQ-01 and OQ-02 remain unresolved, and OQ-03/04 remain pending. This is one bounded learner verification, not a whole-engine, tenant-availability or exhaustive-release validation.

## CRT-002 authored application, October 30, 2026

CRT-002 revision 1.0 uses CAP-01's stable campaign/review/actor concepts. The overview, campaign reports, Search creation guidance, reviewer guidance and Understanding Certifications were freshly checked for its actual claims; see [the lesson record](revisions/CRT-002_Revision_Record.md). CAP-04 supplies the bounded individually reviewable-entitlement condition. CAP-07/08/13 supply limited generation/start, campaign-dependent reviewer choice and current-reviewer versus recorded-actor context, not full mechanisms.

No feature-availability, release-completeness, exact permission, unsigned-completion or removal-timing conclusion was added. OQ-01–04 remain unresolved. The lesson is author-reviewed locally; actual learner validation, tenant execution and CRT-002 publication are unperformed. CRT-001 alone is published.

## CRT-003 authored application, October 30, 2026

CRT-003 revision 1.0 connects the stable CAP-01 objects with bounded CAP-04 access eligibility, CAP-07 generation/start, CAP-10 review confirmation, CAP-12 automated/manual change and CAP-13 evidence. Eleven relevant official pages were freshly checked; see [the lesson record](revisions/CRT-003_Revision_Record.md). Account loading, correlation, source configuration and provisioning references support its necessary introductions.

OQ-01/02 were refreshed and remain unresolved. The trace supplies confirmed review finalization and actual ready removal work without a universal trigger, duration or campaign-completion order. OQ-03/04 remain pending, and OQ-05 records the newly noticed manual-recipient scope question. The manual branch uses actual task assignment. No release, permission, availability or tenant-execution claim is inferred.

The lesson is author-reviewed locally. Actual learner validation and CRT-003 publication have not occurred. CRT-001 remains the only published learner; CRT-002/003 remain local.

## CRT-004 authored application, October 30, 2026

CRT-004 revision 1.0 develops the CAP-01 purpose comparison and bounded CAP-04 assignment-origin/eligibility behavior, with CAP-12's decision-versus-delivery distinction. Eight fresh official references are mapped in [its author record](revisions/CRT-004_Revision_Record.md). Request approval is configured; a supported removal request is not a certification. Requested access profiles and current LCS-granted profiles have different review treatment.

The lifecycle source explicitly distinguishes access-profile enforcement while the state applies from account enable/disable actions that do not form a persistent retry mechanism. The lesson preserves that distinction and does not promise immediate successful restoration or behavior from a state label alone. No tenant permission/configuration or mutation was inspected or performed.

OQ-01–05 remain open. No exhaustive release or universal availability claim is added. CRT-004 is author-reviewed locally, actual learner validation pending and publication unperformed. CRT-001 through CRT-003 are published and live-verified; earlier local-only authored-application entries are historical.

## CRT-005 authored application, October 30, 2026

CRT-005 revision 1.0 develops CAP-15's collection/schema/catalog/association foundation, with bounded CAP-04 certifiability and CAP-07 generation context. Eight official references are mapped in [its author record](revisions/CRT-005_Revision_Record.md). The account's entitlement attribute/type/value linkage and supplied unique ownership establish the example's represented held access; a catalog record alone does not.

Optimized aggregation can skip correlation on unchanged records; supported unoptimized reexamination is explained without promising all associations are repaired or proposing destructive resets. Source-supported capabilities and actual collected values remain necessary evidence. Example clock values are observation order, not duration or propagation guarantees.

OQ-01–05 remain open. No exhaustive release or tenant-availability conclusion is added. CRT-005 is author-reviewed locally, participant validation pending and publication unperformed. CRT-001 through CRT-004 are published and live-verified; earlier authored-application publication states are historical.

## CRT-006 authored application, October 31, 2026

CRT-006 revision 1.0 develops CAP-04's object/origin/eligibility foundation and CAP-03's composition recognition, with scoped CAP-10/12 decision/outcome distinctions. Eight current primary references are mapped in [its author record](revisions/CRT-006_Revision_Record.md). Role management explicitly permits direct entitlements and profiles across sources; no universal role-to-profile-only hierarchy is taught.

Requested role Approve/Revoke, automated criteria role Acknowledge, requested/detected profile eligibility and role/LCS containment are explained with supplied conditions. Acknowledge is not an override/removal action. The overview continues to place composition in the legacy experience. No full role-change propagation, dynamic-dimension, activation, unsigned-completion or manual-recipient procedure is inferred.

OQ-01–05 remain open. No exhaustive release or tenant-availability conclusion is added. CRT-006 is author-reviewed locally, actual learner validation pending and publication unperformed; CRT-001 through CRT-005 are published/live-verified. Earlier authored-application publication states are historical.

## CRT-007 authored application, October 31, 2026

CRT-007 revision 1.0 develops CAP-04 origin/containment/eligibility with bounded CAP-06 selection, CAP-07 generation context, CAP-09 assignment/view context and CAP-15 collected values/association. Nine current primary references are mapped in [its author record](revisions/CRT-007_Revision_Record.md). The active authorized main review produces three supplied units from four rights; no universal count or implicit certification of lifecycle requirements is claimed.

The single-entitlement exclusion is documented. Role-filter unit wording is separately recorded in OQ-06 instead of generalized. OQ-01–05 remain unresolved, and no finality, manual recipient, automatic refresh or full permission matrix is inferred. A current source grant can postdate the data used for generation; actual timing and intended observation scope must be established before correction.

CRT-007 is author-reviewed locally, actual learner validation pending and publication unperformed. CRT-001 through CRT-006 are published/live-verified; earlier authored-application states are historical. No exhaustive release or tenant-result claim is added.

## CRT-009 authored application, November 11, 2026

[CRT-009's record](revisions/CRT-009_Revision_Record.md) develops CAP-14's foundational description/metadata/privilege recognition, with CAP-04 item scope and CAP-15 source/account context. Seven primary references support source versus ISC description editing, responsible ownership, configurable displayed identity/entitlement fields, package meaning and conditional reviewer indicators. The inspected entitlement guide explicitly states display/description edits are not sent to the source; generated descriptions need approval where supported.

No flag or classification is treated as automatic need/safety evidence. New Access is interpreted as not previously certified, not a grant timestamp. Detailed licensed insights, classification setup/inheritance and automatic campaign repair are outside this scope. All seven product questions remain open. CRT-009 is local and author-reviewed; learner assessment, tenant execution and publication remain unperformed. Earlier dated authored-application states remain historical.

## CRT-010 authored application, November 11, 2026

[CRT-010's record](revisions/CRT-010_Revision_Record.md) develops CAP-15 account/association evidence with CAP-04 certifiable unit, CAP-05/06/07 route/selection/generated context and CAP-13 report scope. CAP-02's next-generation-only Experimental API limitation informs the generic retrieval warning; no endpoint contract is taught. Ten primary references support the bounded claims. Independent baselines and full record comparison are engineering methods, not a built-in automatic ISC completeness guarantee.

The dedicated manager-route missing-manager exclusion is kept separate from Search manager-reviewer behavior. Special account types need explicit scope/ownership and supported conditional review routes. All seven product questions remain open; no universal Role-filter model, manager fallback, report matrix or refresh behavior is inferred. CRT-010 is local and author-reviewed; participant assessment, tenant execution and publication remain unperformed. Earlier dated authored-application states remain historical.

## CRT-011 authored application, November 11, 2026

[CRT-011's record](revisions/CRT-011_Revision_Record.md) develops CAP-05 manager purpose/prerequisites with CAP-08/09 routing and assignment support, CAP-15 manager data and CAP-04 review-unit boundaries. Manager correlation and identity-profile mapping were checked directly: configured employee source reference matches the manager identity; Manager Name mapping plus source configuration are required. Documented field matching can retain an old manager when a changed value fails to match, so a nonblank relationship does not prove correctness.

Dedicated Manager Campaign missing-manager exclusion is separate from Search Manager creator handling. Self-review and reassignment limits remain applicable, and actual generated assignment must be inspected after data changes. No universal custom-rule/priority model, owner fallback, exact state matrix or automatic old-review refresh is inferred. All seven product questions remain open. CRT-011 is local and author-reviewed; participant assessment, tenant execution and publication remain unperformed. Earlier dated states remain historical.

## CRT-012 authored application, November 11, 2026

[CRT-012's record](revisions/CRT-012_Revision_Record.md) develops CAP-05's source-owner purpose/readiness with CAP-08/09 assignment, CAP-15 account/source data, CAP-04 review-unit boundaries and limited CAP-12 actual-result recognition. Dedicated source-owner campaign generation requires recorded owners for included sources. Source configuration records system responsibility; Search Source Owner and Access Owner choices are distinct and campaign-type dependent. No missing-owner creator or manager fallback is inferred.

Recorded source owner, actual reviewer, current decision actor and actual change-task recipient remain separate. Updating ownership does not establish that generated work was reassigned or newly selected sources were included. All seven product questions remain open, including OQ-05's manual-recipient conflict. CRT-012 is local and author-reviewed; participant assessment, tenant execution and publication remain unperformed. Earlier dated states remain historical.

## Update log and authoring protocol

For each actual relevant change, record:
- Capability/change and primary source, publication/update date and verification date.
- Available, limited/phased, legacy, planned or unresolved status, with engine and prerequisites.
- Affected learner IDs/sections, examples, diagrams, decisions and evidence.
- What changed in the teaching, and the exact source/tenant checks actually performed.
- Review and publication status.

Do not create fake release entries to fill a register. No release-completeness claim is recorded at setup. This is a manual authoring/maintenance record, not an automated monitoring service.

Before marking a lesson technically checked, link the concrete claims to sources in its own author record. Record unresolved scope rather than using “verified” for a whole document that contains unchecked behavior.

Never perform a live campaign, source permission change, email, API mutation or remediation experiment merely to clear an authoring note. Such actions need authorization in the actual task context.

## CRT-013 authored application, November 11, 2026

[CRT-013 record](revisions/CRT-013_Revision_Record.md) develops CAP-05 targeted identity/access selection, with limited CAP-06 later access refinement, CAP-04 containment/actions, CAP-07 preview, CAP-08/09 reviewer separation and CAP-15 source/account information. Fresh Search guidance confirms that both identity and access-item routes offer all/refined access afterward. Access-object selection respects standalone/container conditions; a saved query is not actual generated work.

The page marks phased availability; no universal engine/options equivalence, exact query/API/limit contract, role-filter meaning or grouping formula is inferred. All seven product questions remain open. CRT-013 is author-reviewed; independent learner assessment and tenant execution are pending. Publication is authorized and its actual results belong in the publication record.

## CRT-014 authored application, November 11, 2026

[CRT-014 record](revisions/CRT-014_Revision_Record.md) develops CAP-06 access refinement with bounded CAP-04 reviewable units/origins, CAP-05 established subject selection, CAP-07 preview, CAP-08/09 actual assignment and CAP-15 collected account evidence. Search guidance verifies saved choices by access type and later all/refined-access selection. Its refinement display limit was inspected; no API or unlimited-list guarantee is taught. Profile/container and requested/criteria/lifecycle action boundaries remain applicable.

Manual refinement is distinct from configured campaign filters; exact combination and Role-criterion semantics remain for their primary topics. A shared object does not establish a supported one-account-only selector. No automatic mutation of existing generated work, private processing sequence, unsigned policy or removal timing is inferred. All seven questions remain open. CRT-014 is local and author-reviewed; actual learner assessment, tenant execution and publication remain unperformed.

## CRT-015 authored application, November 11, 2026

[CRT-015 record](revisions/CRT-015_Revision_Record.md) develops CAP-05 approach selection and CAP-03 core composition recognition, with CAP-04 origins/containers, CAP-07 preview, CAP-08/09 assignment, CAP-14 specialist account recognition and CAP-15 person/account data. The Search composition flow remains legacy with supported role eligibility and selected Org/Role Admin manual remediation responsibility. Rejection is not a universal automatic role rewrite or proof of account outcomes. OQ-05's separate general removal-task recipient issue remains open.

Machine classification and responsible human owner versus application identity were checked in the current account-configuration guide. No naming-prefix classifier, universal license/engine availability, forced person match, exact role propagation or specialist setup is invented. Dedicated Manager exclusion is distinguished from Search Manager creator handling. All seven questions remain open. CRT-015 is local and author-reviewed; participant assessment, tenant execution and publication remain unperformed.

## CRT-016 authored application, November 11, 2026

[CRT-016 record](revisions/CRT-016_Revision_Record.md) develops new CAP-16 query semantics with CAP-05 selection, CAP-06 refinement/filter boundaries, CAP-07 preview and CAP-15 account/source data. Exact text on supported free-text fields, Boolean disabled without .exact, case-sensitive technical field names, capitalized operators/default OR, grouping and nested account/source paths were inspected. Identity source means authoritative source; nested account source means the linked account's source. FAQ timing supports a separate Search observation without an invented synchronization schedule.

The predicates are documentation-based examples over supplied data. Local logical checks are not SailPoint parser or tenant tests. No fixed default department/location mappings, login-success claim from a false disabled flag, unlimited results, campaign-filter/API equivalence or automatic existing-campaign update is inferred. Seven open questions remain unresolved. CRT-016 is local and author-reviewed; participant assessment, rendering, tenant execution and publication remain unperformed.

## CRT-017 authored application and scope investigation, November 11, 2026

[CRT-017 record](revisions/CRT-017_Revision_Record.md) develops CAP-06's single-filter foundation, with CAP-04 eligible package units, CAP-05 selection, CAP-07 preview, CAP-08/09 assignment, CAP-15 data/association and CAP-16 query-versus-builder boundaries. The guide supports normal entitlement inclusion/exclusion, identity/attribute scope, case-insensitive Value and display-name entitlement matching. Source/profile conditions preserve containing objects; no cross-source partial role is assumed.

OQ-06 was freshly investigated against the guide, next-generation overview and list-filter metadata. Role-object wording versus holder examples remains unresolved; enum types do not establish actual propagation. New OQ-08 records the mixed-account scope gap separately. All seven earlier questions remain open; there are now eight. The learner covers all criterion families using verified effects or an explicit discriminating evidence boundary. COMPOSITE/AND/OR schema metadata is not taught as arbitrary UI support; the next-generation endpoint remains Experimental.

Local predicates verify supplied holding calculations and transfer logic, not an ISC filter engine. CRT-017 is local and author-reviewed; actual participant assessment, tenant execution, rendering and publication remain unperformed.

## CRT-018 authored application, November 11, 2026

[CRT-018 record](revisions/CRT-018_Revision_Record.md) develops CAP-05/06 combined selection/refinement/normal filter meaning, with CAP-16 query grouping, CAP-04 package eligibility, CAP-07 generation evidence and CAP-15 data/association. Search creation supports an optional attached campaign filter after query/refinement; a filter-content starting route remains distinct. Query AND/grouped cities and documented same-unit filter OR have different meanings.

Expected ordinary holdings are reconciled under supplied conditions and checked locally, not observed in a tenant. No universal evaluation order, inclusion-wins rule, exact empty status, arbitrary composite UI support or automatic campaign refresh is asserted. OQ-06/OQ-08 were revisited and remain open; current descriptions do not establish Role holder/item or cross-account propagation. All eight product questions remain unresolved. CRT-018 is local and author-reviewed; actual learner assessment, rendering, tenant execution and publication remain unperformed.

## CRT-019 authored application, November 11, 2026

[CRT-019 record](revisions/CRT-019_Revision_Record.md) develops CAP-07's generation/observation boundary with CAP-05 dedicated route, CAP-04 reviewable entitlements, CAP-09 permitted unsigned reassignment, CAP-13 report freshness/history and deletion evidence, CAP-15 collected association and CAP-16 Search availability. The explicit snapshot/later-added-manager note and within-a-day guidance belong to the dedicated Manager/Source Owner creation reference. They do not establish a universal expiration, all-field capture schema or automatic routing/refresh for every engine.

Current account data, existing review contents and later report are supplied distinct observations. Changing workflow responsibility/history does not demonstrate source-population refresh. Earlier uncollected access and later grants are distinct causes. Exact unsupported capture fields are left unclaimed. All eight questions remain open; no unsigned-completion, precise remediation phase or manual-recipient conclusion follows. CRT-019 is local and author-reviewed. Actual participant assessment, tenant operation, graphical rendering and publication remain unperformed.

## CRT-020 authored application, November 11, 2026

[CRT-020 record](revisions/CRT-020_Revision_Record.md) develops CAP-07's reusable definition, one-time/recurring generation, actual preview and separate activation, with CAP-01/02 administration and engine/Experimental scope, CAP-04 eligible access, CAP-05 selection/reviewer choice and CAP-15 data/association. Direct create-template, generate-from-template, set-schedule and activate references support distinct operations; activation accepted does not prove completed start. The learner explains API/job/Experimental meanings and keeps Search Preview Ready separate from the API staged prerequisite.

The Search guide explicitly says early preview generation leaves the originally scheduled generation in place. This supports the overlap check, not an invented failure, retry, deletion cascade or template propagation contract. Saved fixed selection and actual generated contents are checked separately. End-date calculation, all-query re-evaluation and every-field copy/update behavior remain unclaimed. Reminder purpose is taught without a universal owner-versus-creator recipient rule. All eight product questions stay open. CRT-020 is local and author-reviewed; actual participant assessment, tenant action, graphical rendering and publication remain unperformed.

## CRT-021 authored application, November 11, 2026

[CRT-021 record](revisions/CRT-021_Revision_Record.md) develops CAP-01 administrative responsibility and authority, CAP-07 preview acceptance/start, CAP-13 settings/reports/communication and CAP-15 collection/link evidence. CAP-04 eligible standalone holdings, CAP-05 route-specific manager behavior, CAP-08/09 assignment/self-review boundaries and CAP-02 Experimental activation requirements support the normal path. Matrix rows are documentation evidence, not a tenant user-level test.

Search creation and dedicated campaign guidance support inspection before start; the operational hold/correct/reinspect branch is the course's evidence-based acceptance reasoning, not an asserted native ISC rule. Actual current/generated comparisons are supplied examples. API staged/role/accepted-job requirements do not establish completed activation or every UI-state equivalence.

Global email Test Address diversion, authorized shared settings and incomplete campaign-specific/conditional values in test emails were inspected directly. Campaign notification enablement alone is not claimed as receipt. Undecided policy is explained without an OQ-01 unsigned-completion verdict. All eight questions remain open; no private engine order, exact remediation timing, template cascade, sample guarantee or exhaustive update claim. CRT-021 is local and author-reviewed; participant assessment, rendered inspection, tenant action and publication remain unperformed.

## CRT-022 authored application, November 11, 2026

[CRT-022 record](revisions/CRT-022_Revision_Record.md) develops CAP-05/08 supported reviewer choice and input, CAP-01/02 authority/scope, CAP-09 assignment/reassignment and CAP-13 current reviewer versus decision history. CAP-04/15 supplies eligible collected/person-linked access. Manager correlation, entitlement primary/additional ownership and governance group membership were freshly inspected alongside certification guidance.

Seven reviewer choices remain type-dependent. Dedicated missing-manager exclusion is not merged with Search Manager creator fallback; primary-owner and account-owner descriptions do not establish a universal hierarchy. Group member action does not prove group quorum/finalization behavior, and current field changes do not prove existing assignment changed. Known membership maintenance is taught without a tenant test. All eight questions stay open.

All twenty-two completed learners in five modules are pushed, published and live-verified under explicit user authorization. The [publication record](PUBLICATION_2026-11-11_TWENTY_TWO_LESSONS.md) records content 80723fe, successful Pages run 43059165625 and complete live results. This is separate from actual learner assessment, tenant action, exhaustive release coverage and the historical per-lesson authoring states.

## CRT-023 authored application and terminal-gap investigation, November 11, 2026

[CRT-023 record](revisions/CRT-023_Revision_Record.md) develops CAP-05/08's route-specific missing manager/owner handling with CAP-15 manager/source/person data, CAP-09 existing-work correction, CAP-04 reviewable access and CAP-01 authority. Dedicated missing-manager exclusion, Search Manager creator fallback, Account Owner source fallback and dedicated included-source owner prerequisites remain separate.

Manager correlation's null/unmatched behavior is verified for the bounded configured match. A retained link is not an absent link. Governance empty-group Org Admin routing does not prove inactive members disappear or establish a particular administrator. A missing reviewer identity error is scoped to the dedicated guidance; invalid/inactive/nonexistent labels are not merged into one fallback trigger.

New OQ-09 records the unestablished terminal Search ownership case after both expected and final source owners are missing. Current creation guidance and targeted searches do not establish all-type/all-engine recipient/status. Access-request approval and forum/user text are not imported. Earlier eight questions remain open, now nine. Verified ordinary cases proceed with explicit boundaries. CRT-023 is local and author-reviewed; no publication, tenant or participant result is claimed.

## CRT-024 authored application, November 11, 2026

[CRT-024 record](revisions/CRT-024_Revision_Record.md) develops CAP-08 own-access controls and CAP-09 reassignment scope, with CAP-01/02 authority/boundary, CAP-04 eligible review unit, CAP-07 generated coverage, CAP-13 actor evidence and CAP-15 person/account association. Understanding Certifications supports automatic separation and bounded manager/owner/admin routing, plus the distinct manual any-own-access block. Signed-off restriction and other required conditions are not replaced by passing a self comparison.

The directly inspected Work Reassignment guide supports as-created automatic own-access handling and the multiple-identity certification-group exception for member redirects. Its access-request per-member behavior is not imported. Group member-specific split/quorum/permission mechanics and an administrative random-selection pool remain unclaimed; actual generated own work/assignee/actor are required evidence. Source-scoped boundaries do not constitute a new proven defect.

All nine existing product questions remain unresolved. These self-review branches do not resolve OQ-09's different terminal ownership case or OQ-01/02 completion/remediation questions. Local CRT-023/024 preserve the twenty-two-entry publication. No push, tenant execution, participant pass, graphical review or exhaustive release claim is made.

## CRT-025 authored application, November 11, 2026

[CRT-025 record](revisions/CRT-025_Revision_Record.md) develops CAP-09 exact existing-work handover with CAP-01/02 action authority/Experimental scope, CAP-04 eligible units, CAP-07 current work, CAP-08 self-review, CAP-13 assignee/actor/report freshness and CAP-15 person/account inputs. Direct whole-certification and identity-campaign subject/item operations have distinct unit/actor/response contracts. Whole-certification needs ORG_ADMIN/CERT_ADMIN; the checked subject/item references also permit this certification's reviewers.

Administrative signed-off/self-review restrictions remain scoped to the documented action. A different finer API does not establish an unsupported bypass or all-state permission. Supplied before/after decisions are verified examples, not universal reset/copy or same-ID behavior. Asynchronous tracking response is not the complete assignment/coverage/recipient outcome.

The three-holding transfer distinguishes all work, one subject with two items and the single requested item. No unsupported selector, payload, hidden queue, fixed timing, blanket retry or notification is invented. Nine existing product questions stay unresolved. Local CRT-023 through CRT-025 preserve the twenty-two-entry reader; no push, tenant action or participant/graphical result is claimed.

## CRT-026 authored application, November 11, 2026

[CRT-026 record](revisions/CRT-026_Revision_Record.md) develops CAP-09 absence/departure continuity with CAP-01/02 authority/availability, CAP-04 individual eligibility, CAP-07 existing generated work, CAP-08 own-access/group boundaries, CAP-13 current assignment/history/actor/report freshness and CAP-15 person/account inputs. Administrative and user-help Work Reassignment directly establish type-specific as-created redirection, one configuration per person/type, replacement, period/time zone/no end date, retained prior work after end/delete/disable and retained configurations on site disable. Manual/API moves retain their own conditions. No retroactive all-work scan, return-to-original promise or hidden timing sequence.

Loop prevention and four automatic redirects are distinguished from further necessary own-access handling. Multiple-identity certification groups do not apply members' redirects. User-help history's Assignee is the first configured identity and its view covers 90 days; actual final reviewer requires current work evidence. Inactive direct-report visibility and unchanged governance membership do not establish a completed departure handover. The normal example and independent changed-backup transfer supply assignments rather than claim tenant execution. Nine existing product questions remain unresolved. Local CRT-023 through CRT-026 preserve the published twenty-two-entry reader; no push or participant/graphical/tenant result is claimed.

## CRT-027 authored application, November 11, 2026

[CRT-027 record](revisions/CRT-027_Revision_Record.md) develops CAP-14 review context with CAP-01/02 action authority/availability, CAP-04 unit/origin, CAP-07 generation timing, CAP-10 decision/finality distinction, CAP-13 meaningful evidence and CAP-15 person/account/collection. Eight freshly inspected references plus four scoped same-day account/package references establish twelve primary supports. Eight flag meanings, peer/attribute recommendation context and 90-day source activity retain their distinct meanings and conditional visibility. Empty/unavailable data is not a zero, source use is not every-entitlement use, and common access does not establish current authorization.

The recovery-profile transfer contrasts valid uncommon annual duty with an added unapproved deletion capability. No automatic package replacement, overlap/removal promise, exact insight scoring/setup, all-engine snapshot propagation or new unsigned-completion verdict. Nine existing questions remain unresolved. Local CRT-023 through CRT-027 preserve the published twenty-two-entry reader; no push, tenant action or participant/graphical result is claimed.

## CRT-028 authored application, November 11, 2026

[CRT-028 record](revisions/CRT-028_Revision_Record.md) develops CAP-04 unit/origin and CAP-10 action meaning, with CAP-01/02 authority/Experimental availability, CAP-03 legacy composition, CAP-07 generated work, CAP-11/12 removal boundary, CAP-13 decision/report evidence and CAP-15 person/account inputs. Eleven fresh references and two same-day account-data references establish thirteen scoped supports. Direct Decide and Finalize bodies separately document decision versus finalization/initiation, with administrative roles or this certification's reviewers; no payload/state/ACK contract or UI/private mapping is inferred.

OQ-01 unsigned-manager preservation versus Understanding wording and OQ-07 common-entitlement retention versus profile deprovisioning wording remain conflicts after fresh inspection. OQ-02 records the bounded direct finalization support without resolving universal phase timing. All nine questions stay open. Supplier transfer and automatic Warehouse rule require actual intended scope and result evidence; no instant removal/account deletion, automatic replacement, shared-definition edit or rule override follows from a label. Local CRT-023 through CRT-028 preserve the twenty-two-entry reader; no push, tenant or observed learner/graphical result is claimed.

## CRT-029 authored application, November 11, 2026

[CRT-029 record](revisions/CRT-029_Revision_Record.md) develops CAP-10 decision-quality and CAP-13 comment/actor/report evidence, with CAP-01/02 authority/Experimental action scope, CAP-03 composition instructions, CAP-04 units, CAP-07 generated work, CAP-09 handover, CAP-11/12 decision/result boundary and CAP-15 person/account inputs. Eight fresh references plus three same-day account/profile checks provide eleven scoped supports. Direct Decide supports multiple items without establishing UI select-all, payload flags, atomicity or comment copying; direct Finalize remains separate.

Configured comment requirements do not validate the reason. Business criteria are supplied organization rules, not automatic ISC decision policy. Four-item and Invoice/handover examples require exact capability, task, scope, saved explanation and actor evidence. Nine existing questions stay open; no universal unsigned completion, all-engine comment enum, private process or target-removal result. Local CRT-023 through CRT-029 preserve twenty-two published learners; no push, tenant action or observed learner/graphical result is claimed.

## CRT-030 authored application, November 11, 2026

[CRT-030 record](revisions/CRT-030_Revision_Record.md) develops CAP-10 normal save/sign-off with CAP-01/02 authority/Experimental scope, CAP-04 eligible items, CAP-07 generated work, CAP-09 signed-state handover restriction, CAP-11/12 initiation versus removal, CAP-13 first-action/sign-off/actor evidence and CAP-15 person/account inputs. Ten fresh sources and three same-day scoped references provide thirteen supports. Direct Complete is an overdue administrative 202-accepted operation, distinct from direct Finalize; neither its body nor SDK default snippets resolves OQ-01's saved-unsigned outcome. No UI/API enum or private sequence is inferred.

Normal next-generation review decisions become read-only on sign-off; broader reviewer edit wording is newly tracked as OQ-10. All nine earlier questions remain open, making ten current questions. The learner explicitly bounds administrator completion and requires exact engine/type/options/result evidence; it does not silently select discard or preservation. R-30 and Warehouse reasoning separate item decisions, assigned sign-off, campaign state and actual account access. Local CRT-023 through CRT-030 preserve twenty-two published learners; no push, tenant or observed learner/graphical result.

## CRT-031 authored application and publication authorization, November 11, 2026

[CRT-031 record](revisions/CRT-031_Revision_Record.md) develops CAP-14 context/uncertainty and CAP-09 permitted handover with CAP-01/02 actor/availability, CAP-04 eligibility/origin, CAP-07 generated work, CAP-08 own-review restriction, CAP-10 finality, CAP-13 actual decision/assignment evidence and CAP-15 account inputs. Eight freshly inspected references plus three same-day account/profile supports provide eleven scoped sources. Advice from owners, recommendation reasons, source events and actual reviewer assignment have distinct meanings; none supplies unverified authorization or an automatic account change.

All ten questions remain open. Publication of all thirty-one complete learners is explicitly authorized; the expanded six-module manifest passes local checks, deployment/live verification pending in the current publication record. Prior same-day scoped lesson evidence remains preserved, without an exhaustive update/tenant availability claim. No automatic deadline extension, universal missing-panel default, signed-work reopening or manual own-access bypass. No tenant or observed learner/graphical result.
