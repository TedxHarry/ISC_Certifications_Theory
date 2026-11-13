# ISC certifications author source and verification map

Authoring source reference 8.2. Updated November 12, 2026; dated checks below distinguish each stage.
Purpose: evidence planning for the theory course and its authoring foundation, not verification of unwritten lessons.
No tenant action, test campaign or provisioning change was performed. All50 current core topics are authored and prepared for authorized publication in ten modules;49 remain the last observed live snapshot. The [fifty-lesson publication record](author/PUBLICATION_2026-11-12_FIFTY_LESSONS.md) will record deployment/live results. Next is core audit and specialist sequencing. Eleven questions stay open; historical checks remain historical.

## Primary source map

| Official source | Planned coverage |
|---|---|
| [Certifications overview](https://documentation.sailpoint.com/saas/help/certs/index.html) | CRT-001–004; object meanings, broad review/remediation responsibilities, engine migration and legacy role-composition boundary. |
| [Understanding certifications](https://documentation.sailpoint.com/saas/help/certs/understanding_certifications.html) | CRT-006/007/024/028/030/032–037; certifiable access, grant origins, self-certification, automated/manual remediation and sign-off. |
| [Starting a manager or source-owner campaign](https://documentation.sailpoint.com/saas/help/certs/starting_campaign.html) | CRT-011/012/019/021/023; prerequisites, manager/source-owner scope, missing-manager behavior and generated snapshot. |
| [Starting a campaign from Search](https://documentation.sailpoint.com/saas/help/certs/starting_search_campaign.html) | CRT-013–021/022/023; identity/access selection, reviewer choices, templates/schedules, preview generation and activation; extensions X-01–03. |
| [Building a Search query](https://documentation.sailpoint.com/saas/help/search/building-query.html) | CRT-016; category/field/value, exact strings, quoted phrases, Boolean operators, grouping and nested conditions; later query-evidence support remains scoped. |
| [Searchable fields](https://documentation.sailpoint.com/saas/help/search/searchable-fields.html) | CRT-016/044/045; record-specific paths, exact field names and types, identity versus related-account source context. |
| [Search FAQ and data models](https://documentation.sailpoint.com/saas/help/search/search_guide.html) | CRT-016/019/045; repeated account models and Search data timing, without a universal refresh guarantee. |
| [Search overview](https://documentation.sailpoint.com/saas/help/search/index.html) | CRT-016; actual search category/field/nested-query meaning. Availability of optional query assistance needs separate verification when taught. |
| [Using campaign filters](https://documentation.sailpoint.com/saas/help/certs/campaign_filters.html) | CRT-017/018/045; inclusion/exclusion, criteria scope, documented combination behavior and encapsulated access. |
| [Reassigning certifications](https://documentation.sailpoint.com/saas/help/certs/config_reassignment.html) | CRT-024–026; permitted administrative reassignment, self-review checks, signed-off restriction and work reassignment. |
| [Reviewer experience](https://documentation.sailpoint.com/saas/user-help/certs/reviewing/index.html) | CRT-027–031; item context, decisions, acknowledgement, comments, sign-off, overlap and conditionally licensed evidence. |
| [Completing a campaign](https://documentation.sailpoint.com/saas/help/certs/completing_campaigns.html) | CRT-032–044/046; reminders, undecided/overdue completion, actual removal, manual/direct fulfillment, reports and deletion. |
| [Campaign status and reports](https://documentation.sailpoint.com/saas/help/certs/campaign_status_reports.html) | CRT-021/038/040/042–044; composition/status/remediation/sign-off evidence, report freshness and decision-maker distinctions. |
| [Next Generation certification APIs](https://developer.sailpoint.com/docs/api/next-generation-certification-campaigns/) | Engine-aware design and X-05; next-generation object/API scope and current Experimental designation. Exact API contracts need fresh checks when authored. |

Current administration help uses SailPoint Identity Services/Human Fabric headings on established SaaS paths. The approved course name retains ISC. Avoid importing IdentityIQ or File Access Manager behavior from similarly named documentation.

## Engine and capability checks

The overview currently describes phased availability and migration to a new engine. It directs historical campaign/report work and role-composition campaigns to the legacy experience. The next-generation API documentation says its endpoints resolve campaigns generated on that engine and are Experimental during migration.

The proposed normal-example baseline is the next-generation engine where supported. The course teaches stable concepts while tagging affected behavior by applicable engine, campaign type and prerequisites. Use bounded legacy sections for workflows that differ or remain legacy-only. Do not claim every tenant has every screen or every current engine feature.

Before authoring the affected lesson, record:
- Campaign engine and supported campaign type.
- Cert Admin/Org Admin action permissions and campaign creator/owner, reviewer, source/access owner and remediation responsibilities; ownership does not establish administrative permission.
- Generation, preview, schedule and activation behavior.
- Snapshot timing and treatment of subsequent access/reviewer changes.
- Certifiable access and available decision actions by grant origin.
- Missing-owner routing and self-certification prevention.
- Reassignment permissions, granularity and state constraints.
- Decision saving, sign-off, revocation scheduling and completion semantics.
- Automatic/manual remediation eligibility, timing, reports and supported retries.
- Cancellation/deletion, report availability and retention limits.
- Relevant license, phased availability and API-version conditions.

The core does not depend on access recommendations, machine identity licensing or role-composition capabilities. Their purpose is oriented in the core, with deeper mechanics in extensions when relevant.

## Known documentation inconsistency: unsigned decisions

The Understanding Certifications page says unsigned certifications are treated as though no decisions were made at campaign completion. The Completing a Certification Campaign page also contains a note saying a manager's decisions can be preserved when an admin completes an unsigned review.

These passages are materially different. This design does not resolve them by assumption, identify either as universally correct, or claim the difference is definitely caused by engine version.

For CRT-030/039/040:
1. Establish which campaign engine/type the lesson describes.
2. Recheck the current administrative and reviewer documentation.
3. Obtain an authoritative clarification or a permitted controlled observation if the conflict remains.
4. Explain verified behavior and its scope; label unresolved behavior rather than teach an invented universal rule.

An actual tenant test has not occurred. No experiment or live campaign is authorized by this design task.

## Curriculum coverage checks

- Distinct objects: campaign, template, schedule, assigned review, item, account, identity, source, entitlement, access profile, role, reviewer, decision maker, owner, task and operation result.
- Distinct boundaries: represented/live access; selection/refinement/filtering; generation/activation; decision/sign-off; campaign completion/remediation; assignment removal/effective access.
- Routine operations: data readiness, preview checks, reviewer routing/reassignment, decisions/comments, notifications, deadlines, removal, failures, reporting and closure.
- Transfer ability: explain a new case, identify missing evidence, select a layer to investigate, justify the design and create a handoff.
- Theory boundary: mechanism and reasoning, not click-by-click procedures, runnable scripts or claimed production competence without practice.
- Independent reading: local terms, relevant context, no dependency on another lesson or an ongoing fictional story.
- Dynamic form: no universal diagram/table/case/word count.

## Initial status, historical foundation snapshot

Core planned: 50 lessons.
Specialist extensions planned: 5 topic routes; lesson counts follow actual need.
Learner lessons authored: 0.
Primary sources reviewed for curriculum scoping: 10.
Lesson-level technical verification: pending each lesson.
Observed beginner validation: not performed.
Publication: not performed.

## Design review

A separate curriculum builder reviewed both design files. Two material gaps were resolved: an explicit next-generation baseline for normal examples and core permission/responsibility coverage in CRT-002/021/022. These are proposed authoring choices, not choices claimed to have been approved by the user. No additional learner lesson was needed. The unsigned-decision conflict remains an explicit verification requirement before the affected lessons are written.

## Update coverage and readiness requirements, revision 1.1

The user requires content-driven structure without a fixed ten-module limit. The current 50-topic/10-module inventory remains provisional. It is not a certified-complete release inventory or a promise of universal task competence.

Before claiming update completeness, maintain a capability/change register containing: primary source/date, release or availability status, engine, license/prerequisites, affected lesson, changed explanation/example, verification and publication status. Recheck official release information as well as administration/developer guidance. Search results or roadmap announcements alone do not establish generally available behavior. The limited-availability announcement FAQ was discoverable in search during this check, but a direct fetch failed; its complete content has not been verified here.

Keep a task-to-lesson coverage map for common design, scoping, preview validation, reviewer routing, reassignment, decisions/sign-off, deadline handling, removal, failure diagnosis and reporting/closure. Check overlap at CRT-013/014, CRT-030/039/040 and CRT-032/037/046 before fixing final lesson boundaries.

Assess independent understanding using unfamiliar supplied evidence. The learner must identify correct objects/inputs/rules/operations, explain why the result follows, predict a changed condition, choose discriminating evidence and identify uncertainty. Actual learner performance remains unobserved; no pass or readiness claim is recorded.

Theory readiness means independent explanation and reasoned handling of common paper/evidence cases. Production independence additionally requires practice, tenant access/permissions, environment-specific knowledge and organizational procedures. No claim is made that course completion covers every custom task, future release or specialist capability.

## Routine and specialist boundary, revision 1.2

[Operational task coverage](OPERATIONAL_TASK_COVERAGE.md) makes 24 recommended routine task families explicit. This is a planning inventory, not customer-frequency research or evidence of authored/validated coverage.

Common task coverage must include reviewer visibility/permissions as well as assignment, notification problems as well as reminders, and basic read-only API interpretation as well as UI/report evidence. Exact supported operations and authorization are checked for the applicable engine before authoring.

Uncorrelated-account recognition and ownership/scope implications, available review flags/recommendations and basic API/status/ID literacy belong in the core. The dedicated account-review campaign, detailed licensed insight configuration and bulk automation are deeper routes. Role composition and machine-account governance are required depth for relevant jobs, not universally unnecessary topics.

Keep specialist routes conditional on responsibility and environment, with clear entry context and competence outcomes. Do not use 'optional' to omit a term or dependency needed by routine lessons. If a task is not genuinely covered by its mapped topic, revise the lesson boundaries rather than mark it covered by association.

## Local authoring foundation, October 29, 2026, historical setup snapshot

The user authorized setting up ISC_Certifications_Theory before one-at-a-time learner authoring and a later separate repository/push. The existing local folder is used; no duplicate course folder or learner stub is created.

[Teaching specification](TEACHING_SPECIFICATION.md), [course register](COURSE_REGISTER.md) and [authoring guide/CRT-001 brief](author/AUTHORING_GUIDE.md) now govern production. [Coverage](author/COVERAGE_REGISTER.md), [terms](author/TERMINOLOGY_REGISTER.md) and [capabilities/updates](author/CAPABILITY_AND_UPDATE_REGISTER.md) support each learner's author record. Routine task coverage remains in its existing map.

The overview, Understanding Certifications, campaign-completion guidance and next-generation API overview were refreshed during setup. The two unsigned-decision passages remain different; precise remediation-phase timing also needs scoped verification. No source conflict has been resolved by assumption and no tenant test occurred.

Foundation verification completed October 29, 2026: 11 Markdown documents, three empty-directory markers, 50 ordered candidate topics matching the progress register, 24 routine task families, 32 coverage units, 14 capability areas and four open questions. All tables have consistent columns, all 38 relative document links resolve and whitespace checks pass. There are no learner files, lesson stubs, per-lesson revision records or local .git directory.

A separate fresh authoring-readiness reviewer read the package and found no important missing choice or scope gap for CRT-001. The review confirmed its bounded example, reasoning checks, acceptance criteria and separation of source verification, simulated author review and actual learner validation. No tenant actions or file changes were made by the reviewer.

This verifies the authoring foundation, not an unwritten lesson or actual learner performance. Lesson-level verification, exhaustive release completeness, observed learner validation and publication remain pending. The other ISC course was not edited; no repository, commit, remote, push or deployment was created.

## First learner: CRT-001 revision 1.0

First authored learner: [Why review access that somebody already approved?](lessons/CRT-001_Why_Review_Previously_Approved_Access.md). [Per-lesson coverage and source evidence](author/revisions/CRT-001_Revision_Record.md). Six official pages were freshly reviewed for the bounded purpose, object, ownership, decision and outcome claims. The individual record includes loading/account-correlation references supporting the introductory data path.

This first learner is complete and author-reviewed; initial publication is verified. It has one editable diagram, one evidence table, four changed-condition cases and an independent supplier-bank-detail transfer with an uncertainty branch. Actual learner validation remains pending. The initial Pages publication and responsive reader are verified in the publication record. No tenant operation occurred.

At this first-lesson stage, CRT-002 was next. Later authored status appears below. Other planned topics and the exhaustive release audit remain uncompleted. Original foundation counts above record the setup stage, not today's authored learner count.

## Initial publication request, October 30, 2026

The user authorized a new ISC_Certifications_Theory repository, push and Pages publication before local CRT-002 authoring. The repository is created and the publication manifest includes CRT-001 only. [Publication evidence](author/PUBLICATION_2026-10-30_INITIAL.md) records the build and live checks. Earlier no-repository/local-only statements describe their dated authoring stages. Actual learner validation remains pending.

Initial publication verified October 30, 2026: content 98f1a263e6e8990ab99506de40f2c757a635b18c built successfully in workflow 41007230219. All 104 normalized CRT-001 content units, its diagram/table/asset, internal links and four representative author-route exclusions passed live checks. Desktop/mobile review found no page-wide horizontal overflow; native panel toggle worked and the mobile table scrolled within its own region. Actual learner validation is still unperformed.

## Second learner: CRT-002 revision 1.0, October 30, 2026

[Campaigns, certifications and review items](lessons/CRT-002_Campaigns_Certifications_and_Review_Items.md) is complete locally. [Its author record](author/revisions/CRT-002_Revision_Record.md) maps saved teaching to five freshly checked official references: overview, reports, campaign creation, reviewer guidance and Understanding Certifications.

The lesson teaches stable containment and actor distinctions, with supplied review grouping and arithmetic. It does not claim a universal grouping algorithm, platform-permission matrix, progress formula, unsigned-completion policy or removal timing. OQ-01–04 remain open. Source/coverage and complete saved beginner author read-through are recorded; no actual participant or tenant test occurred.

There are now two authored learners, one published learner and 48 unwritten current candidate topics. CRT-003 is next, with no stub. CRT-001 learner/asset/author record and the publication manifest remain unchanged during this local continuation. Both initial Pages builds succeeded; the author follow-up at 9056f7c6c32f83322bbde12bedaadc3ed24d445d completed in workflow 41007516370. CRT-002 has not been committed or pushed.

## Third learner: CRT-003 revision 1.0, October 30, 2026

[Follow one review from access data to a verified outcome](lessons/CRT-003_From_Access_Data_to_a_Verified_Outcome.md) is complete locally. [Its author record](author/revisions/CRT-003_Revision_Record.md) connects the saved trace and worked cases to eleven fresh primary references covering source/account data, correlation, campaign generation/review, removal and verification.

Source/coverage and a full saved-file beginner author read-through are recorded. One editable logical flow and a six-row evidence comparison accompany the normal path, manual branch, missing-stage cases and independent two-account transfer. No actual beginner participant, tenant mutation, source change or CRT-003 graphical publication test occurred.

OQ-01–04 remain open. OQ-05 now records the unestablished scope relationship between certification-specific source-owner task guidance and general provisioning's entitlement-owner/fallback guidance. The learner inspects actual assignment and does not invent a universal recipient rule. The timing diagram is a logical trace with confirmed ready removal work, not an exact engine state machine.

Current total: three authored learners, one published learner and 47 unwritten candidate topics. CRT-004 is next, with no stub. CRT-001/002 learners, assets and per-lesson records are preserved. The publication manifest and live site still list CRT-001 only; CRT-002 and CRT-003 have not been pushed.

## CRT-002/003 publication, October 30, 2026

The user authorized push and then local continuation. Content be8e69d3c63c1b9b03e3c40e800c3092b34ea73d built successfully in Pages workflow 41020384730. The corrected live checker verified three lessons, all 343 content units, three diagrams, three tables, three editable text assets, CSS, sixteen internal link visits and four author-route exclusions. A first false failure exposed Markdown list-marker handling in the checker; inspecting rendered list items established the cause, and rerunning after the narrow fix passed. No learner text was changed.

[The publication record](author/PUBLICATION_2026-10-30_CRT-002_CRT-003.md) records this snapshot. Earlier local-only statements are dated authoring history. Actual learner validation remains pending. CRT-004 follows locally after verified publication.

## Fourth learner: CRT-004 revision 1.0, October 30, 2026

[Certification, access request or lifecycle rule?](lessons/CRT-004_Certifications_Access_Requests_and_Lifecycle_Rules.md) is complete locally. [Its author record](author/revisions/CRT-004_Revision_Record.md) maps the saved comparison and worked cases to eight fresh primary references for requests, supported removal requests, profiles, lifecycle states, certification eligibility and provisioning.

COV-01's comparison is authored. Supporting explanations preserve the requested profile as the review unit, distinguish a grant approval from delivered access and explain current LCS-profile enforcement versus account enable/disable action behavior. Actual assignment origin and configured state requirements govern the omission/restoration examples. No existing open question is closed and no tenant/participant result is invented.

The saved beginner author read-through, edited passages and consistency checks are recorded. Four learners are authored; CRT-001 through CRT-003 are published and live-verified. CRT-004 is local and not pushed. Forty-six candidate topics remain unwritten; CRT-005 is next, without a stub. The published reader, verification tool and previous lesson/asset/record files remain unchanged during this continuation.

## CRT-004 publication, October 30, 2026

The user authorized push and continuation. Content adc71ec17b9ed5a27bc7fa0169bf66b8d174e41c built successfully in Pages workflow 41052833609. Full live validation passed for four lessons, all 453 content units, four diagrams/tables/text assets, CSS, twenty-six internal link visits and four author/control route exclusions. All twelve reviewed learner/diagram/per-lesson-record files retained their hashes. [Publication evidence](author/PUBLICATION_2026-10-30_CRT-004.md) records the scope.

Earlier local-only entries are dated authoring history. CRT-005 continues locally after this verified publication. Actual learner validation and tenant execution remain unperformed.

## Fifth learner: CRT-005 revision 1.0, October 30, 2026

[How application access becomes reviewable information](lessons/CRT-005_From_Application_Access_to_Reviewable_Information.md) is complete locally. [Its author record](author/revisions/CRT-005_Revision_Record.md) maps its actual schema/collection/catalog/correlation explanation to eight fresh official sources. The guessed schema path failed; the canonical official schema reference was obtained through account-loading navigation and verified successfully.

COV-04's data foundation and basic COV-05 ownership association are authored. The learner distinguishes catalog presence from held account values, current source observation from older collection/review history and configuration changes from existing-account reevaluation. Illustrative field names and clock observations are not connector contracts or duration guarantees. CAP-15 records this concrete data/association source scope; OQ-01–05 remain open.

Five learners are authored, four are published and live-verified, and 45 candidate topics remain unwritten. CRT-005 is local and not pushed; CRT-006 is next without a stub. Source/coverage, complete saved beginner author reading and structural checks are recorded, while actual participant/tenant validation remains unperformed. Earlier learner, asset, record and publication files and the four-entry manifest remain unchanged during this continuation.

## CRT-005 publication, October 31, 2026

Content 597642170c9246bc9ab2c6cbe5747abbb8aca3c5 built successfully in Pages workflow 41196568923. Full live validation passed for five lessons, two available modules, all 568 content units, five matching diagrams/tables/assets, CSS, 38 internal link visits and four author/control route exclusions. All fifteen reviewed learner/diagram/per-lesson records retained their hashes. [Publication evidence](author/PUBLICATION_2026-10-31_CRT-005.md) records the scope. Account-schema linkage and optimized-correlation descriptions were refreshed from official sources on publication day; no learner change was required.

Earlier local-only statements describe their dated authoring stages. CRT-006 continues locally after publication. Actual participant validation, tenant execution and exhaustive update completeness remain unperformed.

## Sixth learner: CRT-006 revision 1.0, October 31, 2026

[Entitlement, access profile or role?](lessons/CRT-006_Entitlements_Access_Profiles_and_Roles_in_a_Review.md) is complete locally. [Its author record](author/revisions/CRT-006_Revision_Record.md) maps actual teaching to eight current official references for access objects, assignment origins, eligibility, reviewer actions and composition recognition.

Current role guidance explicitly allows direct entitlements as well as profiles; the example hierarchy is not taught as a mandatory middle layer. The learner preserves single-source profiles, multi-source role scope, one identity's assignment versus a shared definition, requested/detected profile recognition, criteria-role Acknowledge and current legacy composition scope. All five open questions remain open.

Six learners are authored and five are published/live-verified. CRT-006 is local and not pushed; 44 candidate topics remain unwritten and CRT-007 is next without a stub. The complete saved beginner author read-through, examples and file checks are recorded separately from pending actual participant/tenant validation. Earlier learner/asset/record/publication files, the five-entry manifest and reader code remain unchanged during this local continuation.

## CRT-006 publication, October 31, 2026

Content bc61e24a70c0015f1808bf4d4bfc1a35818e3f39 built successfully in Pages workflow 41197281835. Full live validation passed for six lessons, all 683 content units, six diagrams/tables/assets, CSS, 52 internal link visits and four author/control route exclusions. All eighteen reviewed learner/asset/per-lesson records retained their hashes. Current role/profile/eligibility references were refreshed with the continuation checks; no published learner edit was required. [Publication evidence](author/PUBLICATION_2026-10-31_CRT-006.md) records the scope.

Earlier local-only entries describe dated authoring stages. CRT-007 continues locally after this publication. Actual learner validation, tenant execution and exhaustive release completeness remain unperformed.

## Seventh learner: CRT-007 revision 1.0, October 31, 2026

[Why access appears differently or is missing](lessons/CRT-007_Why_Access_Appears_Differently_or_Is_Missing.md) is complete locally. [Its author record](author/revisions/CRT-007_Revision_Record.md) maps saved appearance/eligibility and diagnostic teaching to nine current primary references. COV-07's foundation is authored, with source values, ownership, actual origin/container, selection, review assignment/actions and observation time kept distinct.

The supplied four-right example yields three review units without claiming universal counts or individual review of the LCS portal requirement. The transfer distinguishes containment, lifecycle omission and unresolved collection-versus-later-grant evidence; a later grant alone does not prove the original campaign was wrong.

OQ-01–05 remain open. New OQ-06 records the unit-of-selection wording issue between the Role-filter introduction and member-based examples; this learner teaches a supported single-entitlement exclusion rather than a universal role-filter interpretation. Detailed role-filter claims need scoped verification in CRT-017/018.

Seven learners are authored; six are published/live-verified. CRT-007 is local and not pushed, 43 candidate topics remain unwritten and CRT-008 is next without a stub. Source/coverage and saved beginner author review are recorded; actual participant and tenant validation remain unperformed. Earlier learners/assets/records, publication evidence and the six-entry reader manifest remain preserved during this continuation.

## CRT-004 local explanation revision, October 31, 2026

The user reported that revision 1.0 required repeated reading because of difficult English and technical phrasing, then approved a complete local rewrite. [Revision 1.1 evidence](author/revisions/CRT-004_Revision_1_1_Record.md) records eight freshly checked primary sources, preserved coverage and the author language/flow review. The lesson and its editable diagram were revised locally. Teaching specification 1.1 applies the resulting clarity checks to subsequent work without imposing a fixed layout or reducing technical depth.

Published CRT-004 remains revision 1.0; local revision 1.1 has not been pushed. The feedback is evidence of reader difficulty with 1.0, not a successful assessment of the revised lesson. CRT-007 remains local and unchanged by this rewrite, the candidate count remains 50, and the six product questions remain open.

## Eighth learner: CRT-008, November 2, 2026

The user reported that CRT-004's revised explanation was better and asked to continue. [CRT-008](lessons/CRT-008_One_Person_Two_Accounts_and_the_Correct_Review_Target.md) is complete locally under teaching specification 1.1. [Its record](author/revisions/CRT-008_Revision_Record.md) maps the actual account/identity/source explanation, current need, item scope, target verification and special-account recognition to thirteen official references checked during authoring.

The account-specific main and wrong-account transfer cases supply their precise direct-entitlement targets and exclude package/automatic requirements. Current experimental review-item/account-detail APIs support authorized record inspection, not a universal UI layout or a script prerequisite. Authoritative identities and shadow records remain distinct, and non-human accountability is not employee correlation.

The source comparison adds OQ-07: reviewer and profile-administration guidance disagree about shared-entitlement handling during profile revocation. Its scope remains unresolved for CRT-035/046; no blanket retention/removal rule enters this learner. OQ-01–06 remain open. Eight learners are authored, six are published at revision 1.0, 42 current candidates remain unwritten, and CRT-009 was next at that authoring stage. No push, tenant test or observed independent learner pass is claimed.

## Course-wide explanation pass: CRT-001 revision 1.1, November 2, 2026

The user clarified that the improved explanation applies to all lessons, including the existing ones. New-topic authoring is paused. [CRT-001 revision 1.1](lessons/CRT-001_Why_Review_Previously_Approved_Access.md) is saved locally; [its separate record](author/revisions/CRT-001_Revision_1_1_Record.md) records the prepared brief, six refreshed primary references, preserved coverage, saved author review and local verification. The original revision/publication evidence remains historical.

Next: revise CRT-002, followed by CRT-003/005/006/007. Preserve CRT-004 1.1 and current-style CRT-008. Eight topics remain authored and 42 remain unwritten; five earlier lessons remain to revise. All seven product questions stay open. No source check or local consistency test is presented as an observed learner pass, and no pending work was pushed or deployed.

## Eight-lesson publication, November 2, 2026

At the user's push instruction, content 0ad8a37e497013d6ec08660393f815bc463498e0 published CRT-001/004 1.1 and CRT-002/003/005/006/007/008 1.0. Pages run 41469886314 succeeded. Live verification passed for eight lessons, all 885 content units, eight diagrams/tables/assets, CSS, 86 internal link visits and four author/control route exclusions. [Publication evidence](author/PUBLICATION_2026-11-02_EIGHT_LESSONS.md) records the snapshot. These deployment checks do not resolve the seven product questions or constitute a learner assessment. The next task is CRT-002's rewrite.

## CRT-002 explanation revision, November 11, 2026

[CRT-002 revision 1.1](lessons/CRT-002_Campaigns_Certifications_and_Review_Items.md) is complete locally. [Its new record](author/revisions/CRT-002_Revision_1_1_Record.md) maps the preserved hierarchy, account/person/item context, assigned work, progress, roles/authority and independent six-item transfer to five refreshed official references. The current reviewer versus decision-maker distinction was rechecked against report guidance. No universal grouping, percentage, routing, finality or removal-timing behavior is inferred.

All seven product questions remain open. Eight topics are authored and 42 remain unwritten; four earlier lessons remain to revise. The source/author checks do not establish independent learner performance. No commit, push or deployment occurred. CRT-003's rewrite is next.

## CRT-003 explanation revision, November 11, 2026

[CRT-003 revision 1.1](lessons/CRT-003_From_Access_Data_to_a_Verified_Outcome.md) is complete locally. [Its new record](author/revisions/CRT-003_Revision_1_1_Record.md) maps the preserved process and evidence reasoning to ten current primary references, including the four campaign/reviewer/eligibility references checked during CRT-002 and six reopened data/delivery/snapshot/engine sources. Exact remediation timing and manual-task recipient scope remain unresolved; the learner follows supplied ready removal work rather than an invented universal sequence.

All seven product questions remain open. Eight topics are authored and 42 remain unwritten. CRT-005/006/007 remain to revise; CRT-002/003 1.1 remain local. No independent learner pass, commit, push or deployment is claimed.

## CRT-005 explanation revision, November 11, 2026

[CRT-005 revision 1.1](lessons/CRT-005_From_Application_Access_to_Reviewable_Information.md) is complete locally. [Its new record](author/revisions/CRT-005_Revision_1_1_Record.md) maps all 26 original teaching purposes to the saved revision and eight primary references. Four source/schema/entitlement references were reopened; four data/correlation/eligibility/snapshot checks from today's CRT-003 work were reused within their verified scope. The explanation retains account-held values versus access-object definitions, documented linking conditions, unique correct correlation, optimized reprocessing limits and captured review times.

All seven product questions remain open. No tenant result, exhaustive update audit or participant mastery is claimed. CRT-002/003/005 1.1 remain local; CRT-006 is next, followed by CRT-007. Eight topics are authored and 42 remain unwritten. No commit, push or deployment occurred.

## CRT-006 explanation revision, November 11, 2026

[CRT-006 revision 1.1](lessons/CRT-006_Entitlements_Access_Profiles_and_Roles_in_a_Review.md) is complete locally. [Its new record](author/revisions/CRT-006_Revision_1_1_Record.md) maps all 25 original teaching purposes to saved sections and eight reopened primary references. Direct entitlements in roles, single-source profiles, requested/detected origins, criteria-controlled Acknowledge, lifecycle/role containment and legacy composition scope remain verified within the stated limits. The two official profile-overlap descriptions still conflict; OQ-07 remains open and the examples do not assume overlap protection.

All seven product questions remain open. No tenant test, exhaustive update audit, participant mastery, commit, push or deployment occurred. CRT-002/003/005/006 1.1 remain local. CRT-007 is the one remaining rewrite; eight topics are authored and 42 remain unwritten.

## CRT-007 explanation revision, November 11, 2026

[CRT-007 revision 1.1](lessons/CRT-007_Why_Access_Appears_Differently_or_Is_Missing.md) is complete locally. [Its new record](author/revisions/CRT-007_Revision_1_1_Record.md) maps all 24 original purposes to saved sections and nine primary references. Filter, manager/source campaign, account loading and correlation passages were reopened; today's CRT-006 object/eligibility/Search/reviewer checks were reused within scope, with selection/grouping passages reinspected. Role-filter unit ambiguity remains open; no universal refresh, correction or permission matrix was inferred.

All seven product questions remain open. The existing-lesson rewrite pass is complete locally. Eight topics remain authored, 42 remain unwritten and CRT-009 is next. CRT-002/003/005/006/007 1.1 remain unpublished. No tenant test, exhaustive release audit, independent learner pass, commit, push or deployment occurred.

## CRT-009 authored locally, November 11, 2026

[CRT-009](lessons/CRT-009_Understanding_What_Access_Actually_Permits.md) and [its author record](author/revisions/CRT-009_Revision_Record.md) connect descriptions, business capability, responsible ownership, person attributes, entitlement metadata and actual reviewer judgment. Entitlement management, certification identity details, reviewer context and privilege classification were inspected afresh; profile/role and generated-context checks reuse today's verified scope, with profile/role description/owner passages reinspected. Display/description edits in ISC are not sent to the source. Conditional GenAI suggestions require approval; no model output, missing flag or readable label proves actual capability or need.

Seven primary references support the scoped claims. Detailed scoring/inheritance, insight configuration, automatic snapshot repair and uncertainty policies are not inferred. All seven product questions remain open. Nine topics are authored and 41 remain unwritten. The eight-entry publication manifest and published snapshot are unchanged; CRT-009 and earlier five local rewrites are unpublished. CRT-010 is next.

## CRT-010 authored locally, November 11, 2026

[CRT-010](lessons/CRT-010_Checking_That_the_Review_Population_Is_Complete.md) and [its author record](author/revisions/CRT-010_Revision_Record.md) connect independent expected-population evidence with actual generated people/account/access. Ten primary references cover data/association, selection/containment, campaign-route prerequisites, generated preview, reports and complete-result retrieval. Search campaign, manager/source route and reports were reopened; collection-parameter and next-generation-only API scope were checked. Earlier same-day eligibility/filter/data/reviewer checks are reused within scope.

Reconciliation and sampling limits are engineering reasoning, not an ISC built-in automatic population validator. No exact API contract, universal report columns, Role-filter interpretation or automatic repair is inferred. All seven product questions remain open. Ten topics are authored and 40 remain unwritten. CRT-009/010 and five earlier local rewrites are unpublished; the eight-entry publication manifest is unchanged. CRT-011 is next.

## CRT-011 authored locally, November 11, 2026

[CRT-011](lessons/CRT-011_When_a_Manager_Review_Is_the_Right_Choice.md) and [its record](author/revisions/CRT-011_Revision_Record.md) develop manager business-need judgment and source-to-relationship-to-assigned-review reasoning. Manager correlation and identity-profile mapping, dedicated manager and Search routes, self-review and reassignment were reopened. The documented field-match behavior can retain an existing manager when a changed reference cannot match. Missing-manager Search creator assignment is kept distinct from dedicated-route exclusion and separate self-review controls.

Eight primary references support scoped product claims; earlier same-day reviewer/report/account-data checks are reused. No universal priority/custom-rule, hierarchy expansion, owner fallback, automatic reassignment or exact permission matrix is inferred. All seven product questions remain open. Eleven topics are authored and 39 remain unwritten. CRT-012 is next; CRT-009/010/011 and earlier five rewrites are local and unpublished. The eight-entry publication manifest remains unchanged.

## CRT-012 authored locally, November 11, 2026

[CRT-012](lessons/CRT-012_When_Source_Owners_Should_Review_Access.md) and [its record](author/revisions/CRT-012_Revision_Record.md) develop source-owner purpose, selected source/account/access, recorded ownership and actual assigned work. Dedicated source-owner campaign, source configuration and Search reviewer passages were reopened. The included-source owner prerequisite is kept distinct from other reviewer hierarchies; no creator/manager fallback is invented for a missing source owner.

Ten primary references support scoped product claims; same-day object/data/reviewer/reassignment/report checks are reused. OQ-05's manual-removal recipient question is not resolved from a reviewer label, and all seven product questions remain open. Twelve topics are authored and 38 remain unwritten. CRT-013 is next. CRT-009 through CRT-012 and the five earlier rewrites remain local/unpublished; the eight-entry publication manifest is unchanged.

## CRT-013 authored and publication authorized, November 11, 2026

[CRT-013](lessons/CRT-013_Starting_with_People_or_Access_Items.md) and [its record](author/revisions/CRT-013_Revision_Record.md) develop people-first versus access-first selection, actual returned record types, a separate all/refined-access decision and generated-result checks. Search creation, Understanding Certifications and query-building passages were reopened. Five same-day supporting profile/role/reviewer/account references are reused within scope. The Search page still marks phased availability. No exact query/API/limit contract, role-filter interpretation or universal grouping is inferred.

The main comparison and requested-role transfer preserve object definitions versus holdings, exact source references and container restrictions. All seven product questions remain open. Thirteen topics are authored and 37 unwritten; CRT-014 is next. The user authorized publication of all saved work. See the separate publication record for executed deployment evidence when available.

## Thirteen-lesson publication evidence, November 11, 2026

Content 470c4a5008b7d6d6724cf16ce57c9c4e64fabd5d was pushed and built successfully in [Pages run 43024965366](https://github.com/TedxHarry/ISC_Certifications_Theory/actions/runs/43024965366). The full live verifier passed for thirteen learners, 1555 content units, thirteen diagrams/assets, fifteen tables, 206 internal link visits, CSS and representative author exclusions. The initial live failure was a verifier bug: single-asterisk emphasis was not normalized, although the page correctly rendered the emphasized word. The author-only checker was corrected; the actual learner files were preserved and the full live run then passed. [Publication record](author/PUBLICATION_2026-11-11_THIRTEEN_LESSONS.md) records evidence. No independent learner result, tenant execution, graphical inspection or exhaustive release audit is implied.

## CRT-014 authored locally, November 11, 2026

[CRT-014](lessons/CRT-014_Choosing_Access_for_the_Selected_People.md) and [its record](author/revisions/CRT-014_Revision_Record.md) develop subsequent access refinement, actual holdings, saved per-type choices, container eligibility and generated-work checks. Search creation, Understanding Certifications, filters, reviewer guidance and profile administration were reopened. Three earlier same-day role/account references are reused within scope. Eight references support the stated product claims; the six/two/five holding comparisons and independent account-scope reasoning use supplied inputs, not tenant observations.

No exact query/filter combination, account-selector contract, display-as-completeness guarantee, unsigned completion policy or private backend is inferred. All seven product questions remain open. Fourteen topics are authored and 36 unwritten. CRT-015 is next; CRT-014 is local, and the thirteen-entry publication manifest and live snapshot remain unchanged. No observed participant pass or publication is claimed for this continuation.

## CRT-015 authored locally, November 11, 2026

[CRT-015](lessons/CRT-015_Choosing_a_Campaign_Design_for_the_Business_Question.md) and [its record](author/revisions/CRT-015_Revision_Record.md) develop business-question/subject/access/reviewer/evidence alignment, role holdings versus shared design, legacy composition follow-up and account-type recognition. Search campaign creation, Manager/Source Owner guidance, Understanding Certifications and machine-account configuration were reopened and inspected. Five supporting same-day object/reviewer/account references are reused within scope; nine primary references are mapped to saved teaching.

The composition task's selected permitted remediation owner is scoped to that documented path and does not resolve OQ-05. Role eligibility, type-dependent reviewer options, dedicated/Search missing-manager differences and actual machine classification remain bounded. No universal native role object, account mapping, automatic role rewrite, exact query/filter contract or release-completeness guarantee is inferred. Seven questions stay open. Fifteen authored, 35 unwritten, CRT-016 next; CRT-014/015 and the unchanged thirteen-entry publication manifest retain their distinct local/published states.

## CRT-016 authored locally, November 11, 2026

[CRT-016](lessons/CRT-016_Understanding_What_a_Campaign_Search_Selects.md) and [its record](author/revisions/CRT-016_Revision_Record.md) develop Search category/field/value meaning, exact text, capitalized operators and explicit grouping, same-account nesting, authoritative versus account source, actual saved selection and Search-data timing. Query construction, fields, campaign creation, FAQ/models and overview were reopened; relevant long official-page passages were extracted read-only for inspection. Three same-day data/eligibility references support the local foundations. Eight primary references are reconciled with saved teaching.

CAP-16 records the newly authored query-contract area, separate from configured campaign filters. Local predicate checks confirm supplied logical outcomes and do not execute ISC syntax. No default field mapping, parser/tenant test, fixed synchronization duration, successful-login inference, filter-builder equivalence or automatic campaign update is claimed. All seven questions stay open. Sixteen authored, 34 unwritten, CRT-017 next; CRT-014 through CRT-016 and the thirteen-entry publication retain distinct states.

## CRT-017 authored locally, November 11, 2026

[CRT-017](lessons/CRT-017_Including_and_Excluding_Review_Content_with_Campaign_Filters.md) and [its record](author/revisions/CRT-017_Revision_Record.md) develop saved filter/criterion/mode, documented entitlement inclusion/exclusion, person-level effects, display-name/value comparisons and package/source boundaries. The filter guide, Search creation, Understanding Certifications, next-generation overview and both list-filter references were reopened. Four same-day object/account references are reused within scope; ten primary references map to saved teaching.

Current Role descriptions/examples remain insufficient to settle OQ-06. Schema type/operation enums do not prove runtime affected work or arbitrary UI grouping. New OQ-08 records unestablished account-attribute effects across unrelated accounts/sources; the lesson uses a single-source/single-account case and explicit verification boundary. This is a scope gap, not a claimed product defect. Seven earlier questions remain unresolved, making eight now. Local predicate checks cover supplied five/two/three holdings, person exclusion, package transfer and renamed label, not an ISC filter execution.

Seventeen authored, 33 unwritten, CRT-018 next. CRT-014 through CRT-017 are local; the thirteen-entry manifest and verified live snapshot are preserved. No participant or exhaustive release result is claimed.

## CRT-018 authored locally, November 11, 2026

[CRT-018](lessons/CRT-018_Combining_People_Access_Selection_and_Campaign_Filters.md) and [its record](author/revisions/CRT-018_Revision_Record.md) develop query/actual selected people, refined reviewable objects, supported exclusion and actual generated evidence. Search creation, campaign filters, next-generation overview, query construction and Understanding Certifications were reopened; optional filter attachment and parenthesis passages were specifically inspected. Five same-day field/object/account references are reused within scope. Ten primary references support the mapped claims.

The six/four/two expected-scope trace is a supplied normal deduction, not a tenant observation or universal engine-order rule. The conflicting-inclusion case establishes no common requested item without assigning a winner or empty-result status. Current guide/overview material does not resolve OQ-06/OQ-08; Role and mixed-account effects remain bounded. Same-unit OR, different-unit equal-count results and a role-contained-profile change receive worked reasoning. All eight questions remain open.

Eighteen authored, 32 unwritten, CRT-019 next. No source mutation, participant assessment, push or deployment occurred. Local CRT-014 through CRT-018 and the thirteen-entry publication remain distinct.

## CRT-019 authored locally, November 11, 2026

[CRT-019](lessons/CRT-019_Understanding_the_Data_Captured_When_a_Review_Is_Generated.md) and [CRT-019 record](author/revisions/CRT-019_Revision_Record.md) develop primary COV-13: actual source observation, collected/linked inputs, generated work, later access/manager changes, supported reassignment and later report production. Dedicated Manager/Source Owner creation, Search creation, reports, reassignment, completion, Search FAQ, Understanding Certifications and next-generation overview were reopened. Account loading/correlation reuse same-day verified local meanings; ten references map to saved teaching.

The dedicated-route snapshot and later-manager note does not establish every field's immutability for every engine. Current permission counts and existing review contents are supplied example observations, not a tenant result. Report date is not source freshness or newly generated review coverage. Deletion evidence loss, unsigned reassignment restrictions and historical actor versus current assignee are scoped separately; OQ-01/02/05 are not resolved from those facts. All eight questions remain open.

Nineteen authored, 31 unwritten, CRT-020 next. Local CRT-014 through CRT-019 preserve the thirteen-entry publication. No live campaign action, participant assessment, push or deployment occurred.

## CRT-020 authored locally, November 11, 2026

[CRT-020](lessons/CRT-020_Understanding_Templates_Schedules_Previews_and_Running_Campaigns.md) and [its record](author/revisions/CRT-020_Revision_Record.md) develop primary COV-14 through saved definition, supported generation choices, actual preview, separate start, timing and independent cycles. Search creation/scheduling/start, certifications overview, next-generation create-template/generate/set-schedule/activate references and pre-generation reminder documentation were freshly inspected. Four same-day eligibility/data/association references support local meanings: eleven sources in total.

The early-generation note explicitly preserves the original scheduled occurrence. Direct generation API creates a new campaign; activation submits a job for the documented staged state and is Experimental. Search Preview Ready and API staged are not declared universally interchangeable. Template edits/schedule changes do not, by themselves, prove changes in existing campaign records. No guessed end-date calculation, all-field propagation, dynamic-query promise, payload or private engine sequence is supplied.

Reminder purpose is used without a universal owner/creator recipient inference. All eight existing product questions remain open. Twenty authored, 30 unwritten, CRT-021 next. Local CRT-014 through CRT-020 preserve the thirteen-entry publication; no participant assessment, tenant operation, push or deployment occurred.

## CRT-021 authored locally, November 11, 2026

[CRT-021](lessons/CRT-021_Checking_a_Generated_Campaign_Before_It_Reaches_Reviewers.md) and [its record](author/revisions/CRT-021_Revision_Record.md) develop actual preview acceptance and verified authorized launch. Search creation/start, dedicated manager/source-owner prerequisites, reports, Understanding Certifications, activation API, user-level matrix, email settings/testing and activated-email purpose were freshly inspected. Three same-day account/data/freshness references support local meanings: eleven scoped sources total.

The four-versus-four discrepancy is supplied example evidence, not a tenant result. Separate missing collected input and broad saved access scope require separate corrections and reinspection. Dedicated missing-manager exclusion is not merged with Search Manager creator fallback. Current API role/staged/Experimental/accepted-job requirements remain scoped rather than treated as universal UI labels or a tenant matrix.

Global Test Address diversion and incomplete process-specific/conditional data in presentation tests are verified operational readiness checks. No email was sent or setting changed. Undecided-policy readiness does not resolve the unsigned-completion conflict. All eight questions remain open. Twenty-one authored, 29 unwritten, CRT-022 next; local CRT-014 through CRT-021 preserve the thirteen-entry publication. No push, participant assessment or tenant action occurred.

## CRT-022 authored and publication prepared, November 11, 2026

[CRT-022](lessons/CRT-022_How_ISC_Chooses_the_Reviewer.md) and [its record](author/revisions/CRT-022_Revision_Record.md) develop supported reviewer choice, actual owner/identity/group inputs, generated responsibility, knowledge/authority and decision actor. Search creation, dedicated campaigns, reassignment, Understanding Certifications, reports, entitlement ownership, governance groups and manager correlation were freshly inspected. Five same-day supporting permission/package/account references are reused within scope: thirteen sources total.

All seven reviewer choices are type-scoped. Primary/additional ownership and group owner/member/actor differ; no universal owner hierarchy or group quorum/finalization contract is invented. Current manager/owner changes do not prove existing work moved. The independent Warehouse case distinguishes correct Access Owner execution from a mismatched manager-assessment requirement. All eight questions stay open. Twenty-two authored, 28 unwritten, CRT-023 next.

Explicit user authorization covers pushing complete local CRT-014 through CRT-022 with earlier learners and expanding the reader to five modules. The [publication record](author/PUBLICATION_2026-11-11_TWENTY_TWO_LESSONS.md) separates prepared content from observed deployment/live verification. Earlier author records and source-scoped uncertainties remain historical; no tenant or participant result is claimed.

Publication follow-up, November 11: content 80723fec7f476669b3ba62d3a2e848225c6e545d deployed successfully in Pages run 43059165625. The full live verifier passed for twenty-two learners, 2795 normalized content units, twenty-two exact diagrams/assets, twenty-seven tables, 548 internal link visits, CSS and four representative excluded author/control paths. These are publication-content checks, not a graphical/participant/tenant result. CRT-023 remains next.

## CRT-023 authored locally, November 11, 2026

[CRT-023](lessons/CRT-023_Handling_Missing_Managers_Owners_and_Fallback_Reviewers.md) and [its record](author/revisions/CRT-023_Revision_Record.md) develop missing manager/owner diagnosis, input versus relationship versus work, route-specific exclusion/fallback, group readiness and supported correction. Search creation, dedicated prerequisites/troubleshooting, manager correlation, governance groups, reassignment and Understanding Certifications were freshly inspected. Four supporting same-day data/ownership/report references are reused within scope: ten sources total.

The manager table is bounded to one applicable attribute-based mapping; unmatched changes can retain a prior link while null clears it. General empty-group Org Admin routing does not establish all-inactive-as-empty or an individual administrator. Missing final source ownership in Search Account Owner/Access Owner routes remains unestablished by inspected material and targeted official-source searches. New OQ-09 records that terminal gap; access-request approval escalation and forum/user replies are not certification authority.

Twenty-three authored, 27 unwritten, CRT-024 next. Nine questions remain open. The prior final author-only Pages run 43059772625 is observed successful; publication, earlier evidence and manifest remain unchanged. No push, tenant mutation or participant result occurred.

## CRT-024 authored locally, November 11, 2026

[CRT-024](lessons/CRT-024_Preventing_Self_Certification_and_Checking_Own_Access_Routing.md) and [its record](author/revisions/CRT-024_Revision_Record.md) develop subject/reviewer comparison, automatic own-access separation, bounded manager/owner/admin routing, manual any-own-access block and actual responsibility/decision evidence. Understanding Certifications, reassignment, work reassignment, governance groups, Search creation and reports were freshly inspected. Three same-day account/permission references support local meanings: nine sources total.

The direct work-reassignment guide confirms automatic separation and the multiple-identity certification-group exception for member redirects. Access-request per-member behavior is not imported. Automatic routing and blocked manual action are distinct, not conflicting universal rules. No random-admin pool, group-internal member split/quorum, all-state manual override or API execution is invented. Nine questions remain unresolved.

Twenty-four authored, 26 unwritten, CRT-025 next. Local CRT-023/024, the published manifest and earlier evidence remain preserved. No push, tenant operation, graphical/participant assessment or exhaustive release claim occurred.

## CRT-025 authored locally, November 11, 2026

[CRT-025](lessons/CRT-025_Reassigning_Review_Work_and_Verifying_the_Result.md) and [its record](author/revisions/CRT-025_Revision_Record.md) develop existing-review reason/scope/state/authority/recipient, supported action, actual coverage/history and handover visibility. Reassignment, reports, Understanding Certifications, Work Reassignment and direct whole-certification/subject-item/asynchronous subject-item APIs were freshly inspected. Three same-day account/permission references support local meanings: ten scoped sources.

Whole-certification API authority/task response is distinguished from identity-campaign subject/item reviewer-or-admin scope and response variants. Experimental documentation does not establish every UI, campaign state, decision-copy behavior or identifier preservation. Main and transfer results are supplied evidence rather than a tenant operation. Existing administrative signed-off/self-review rules are kept scoped; finer APIs are not treated as a bypass. Nine questions remain open.

Twenty-five authored, 25 unwritten, CRT-026 next. Local CRT-023 through CRT-025, earlier evidence, published manifest and reader remain preserved. No push, authenticated tenant action, graphical or participant assessment occurred.

## CRT-026 authored locally, November 11, 2026

[CRT-026](lessons/CRT-026_Keeping_Reviews_Moving_During_Absence_and_Departure.md) and [its record](author/revisions/CRT-026_Revision_Record.md) develop existing-work cover versus configured as-created redirection, work type/person/recipient/period/time zone/actor, replacement, end/delete/disable, permanent departure and actual responsibility/history. Administrative and user-help Work Reassignment, certification reassignment, Understanding Certifications, governance groups and reports were freshly inspected; three scoped same-day account/correlation/permission references support local meanings.

User-help history's first configured Assignee and 90-day view are distinguished from the actual current recipient after a chain. Four automatic redirects do not prohibit necessary own-access escalation. Multiple-identity certification groups do not apply members' redirects. No universal inactive/group fallback, API payload, private ordering or automatic return/retroactive transfer is inferred. Nine product questions remain unresolved. Twenty-six authored, 24 unwritten; CRT-027 next. Local CRT-023 through CRT-026 and prior publication remain separate; no push, tenant, graphical or participant result occurred.

## CRT-027 authored locally, November 11, 2026

[CRT-027](lessons/CRT-027_Inspecting_Review_Context_Before_Deciding.md) and [its record](author/revisions/CRT-027_Revision_Record.md) connect exact person/account/access, actual capability, current authorized task, origin and evidence timing to reasoned judgment. Reviewer guidance, Access Recommendations, Activity Insights, cloud details, Understanding Certifications, manager/source-owner generation, privilege classification and entitlement metadata were freshly inspected. Four same-day account/correlation/package references support the local meanings: twelve scoped sources.

Eight documented flags receive plain meanings and useful next questions. New Access concerns previous certification; peer comparisons do not prove current need, source-use observations do not prove use of every permission, and absent data is not zero. Optional data/cloud detail remains conditional. No classification score, group algorithm, universal field freshness, all-type recommendation availability or automatic replacement/removal is inferred. Nine questions remain open. Twenty-seven authored, 23 unwritten; CRT-028 next. Local CRT-023 through CRT-027 preserve prior learners/evidence and published manifest; no push, tenant, graphical or participant assessment occurred.

## CRT-028 authored locally, November 11, 2026

[CRT-028](lessons/CRT-028_Understanding_Approve_Revoke_and_Acknowledge.md) and [its record](author/revisions/CRT-028_Revision_Record.md) develop action meaning by reviewed unit, origin and type, automatic membership requirements, package scope and decision/finality/removal evidence. Understanding, reviewer guidance, roles/role assignment, profiles, completion/reports, next-generation overview, direct Decide/Finalize bodies and Search composition were freshly inspected. Two same-day account-data references support local meanings: thirteen scoped sources.

Direct Experimental Decide and Finalize operations are distinct; finalization initiates needed remediation without proving completed source change. Current unsigned-completion and overlap contradictions remain unresolved. Criteria-role Acknowledge does not remove access or fix data/criteria/contents; requested role Revoke does not edit the shared definition. Legacy composition uses manual work with actual recipient verification. Nine questions remain open; no universal phase timing, package overlap protection, immediate deletion, API payload or actual action is inferred. Twenty-eight authored, 22 unwritten; CRT-029 next. Local CRT-023 through CRT-028 preserve earlier evidence and published manifest; no push, tenant, graphical or participant assessment occurred.

## CRT-029 authored locally, November 11, 2026

[CRT-029](lessons/CRT-029_Recording_Clear_Reasons_and_Checking_Bulk_Decisions.md) and [its record](author/revisions/CRT-029_Revision_Record.md) develop decision criteria, exact item/current facts, useful comment/evidence references and multi-item selection/result verification. Reviewer/report guidance, Search and manager/source-owner comment settings, direct Decide/Finalize bodies, Understanding and reassignment were freshly inspected; three same-day account/profile references support local meanings. Eleven scoped sources; SDK payloads and misrouted aggregate V3 search output are not action-contract evidence.

Decision Comments differs from status Comments; current reviewer differs from historical decision maker and does not identify every text author. No universal bulk UI scope, default shared comment, atomic result, exact comment enum/length or target completion is asserted. Four-item and Invoice transfers expose unjustified copied reasons and misleading package descriptions. Nine questions remain open. Twenty-nine authored, 21 unwritten; CRT-030 next, investigating/bounding unsigned finality. Local CRT-023 through CRT-029 preserve earlier evidence and published reader; no push, tenant, graphical or participant assessment occurred.

## CRT-030 authored locally, November 11, 2026

[CRT-030](lessons/CRT-030_Distinguishing_Saved_Decisions_and_Review_Sign_Off.md) and [its record](author/revisions/CRT-030_Revision_Record.md) develop saved item choices, undecided/unsigned versus sign-off, permitted changes, signer/time, reauthentication and campaign/account evidence. Reviewer, Understanding, completion, next-generation overview, direct Complete/Get/Finalize/List, reports and reassignment were freshly inspected; same-day Decide/loading/correlation provide three supporting checks: thirteen scoped sources.

OQ-01 was actively investigated through both conflicting passages, exact administrative Complete body and targeted ISC searches. Neither SDK defaults nor IdentityIQ metadata/closing behavior resolves the saved-unsigned outcome. Normal next-generation readonly finalization is taught without universal retention/discard or phase timing. New OQ-10 records reviewer editing ambiguity; no unsupported Undo/reopen/after-signoff reassignment is invented. Ten questions remain open. Thirty authored, 20 unwritten; CRT-031 next. Local CRT-023 through CRT-030 preserve earlier evidence and published reader; no push, tenant, graphical or participant assessment.

## CRT-031 authored and publication authorized, November 11, 2026

[CRT-031](lessons/CRT-031_Resolving_Uncertainty_Before_an_Access_Decision.md) and [its record](author/revisions/CRT-031_Revision_Record.md) develop specific missing facts, relevant consultation, true capability/current need and permitted verified reassignment. Reviewer/reassignment guidance, Recommendations, Activity Insights, Understanding, entitlement metadata, reports and manager/source-owner context were freshly inspected; three same-day account/profile supports make eleven scoped sources. No universal pause, default unsure decision, recommendation substitute, own-review bypass or all-state correction is invented.

Ten questions remain open. Thirty-one authored, 19 unwritten; CRT-032 next. User authorizes publication of all complete lessons; [the thirty-one-lesson publication record](author/PUBLICATION_2026-11-11_THIRTY_ONE_LESSONS.md) records local checks and pending deployment/live verification. Prior source and learner records remain historical. No tenant, graphical or participant result is inferred.

## Thirty-one-lesson deployment observed, November 11, 2026

[Current publication record](author/PUBLICATION_2026-11-11_THIRTY_ONE_LESSONS.md) records content 670f0c8cdb7535057ffe285034d33a6762156e98 and successful Pages run 43159502534. Full live checks passed for 31 learners, 3743 content units, 31 diagrams/assets, 38 tables and 1052 internal link visits, CSS and representative author/control exclusions. Previous pending/local-only dated statements describe their authoring checkpoints. Publication does not close ten open questions or establish tenant behavior, exhaustive releases, graphical quality or participant understanding. CRT-032 remains next.
## CRT-032 current scoped verification, November 11, 2026

[CRT-032 record](author/revisions/CRT-032_Revision_Record.md) maps eight freshly inspected primary sources: Understanding, reviewer guide, direct Experimental Finalize, next-generation overview, completion, campaign reports, provisioning overview and monitoring. Same-day loading/correlation/profile sources support meanings, making eleven scoped references. Finalize initiates needed remediation; no universal cross-engine timing or unsigned-administrator-completion result follows. Reviewer date setting is conditional and unavailable for individual entitlements. Report Finished can represent different delivery paths; closed manual work is not direct account evidence. Aggregation/collection observes account data, and newer collection time alone does not prove correct identity association. OQ-01/02/05/07/10 remain bounded; all ten questions stay open. Thirty-two authored, 18 unwritten; CRT-033 next. No push, tenant run, graphical or participant validation.

## CRT-033 scoped verification, November 12, 2026

[CRT-033 record](author/revisions/CRT-033_Revision_Record.md) maps twelve freshly inspected primary sources: provisioning overview, Understanding/completion, monitoring, Search, schema/loading, VA overview and current Web Services SaaS connection/HTTP operations/operation examples/parameters. Old SaaS paths redirected; current explicit paths supply the actual connector scope. Operation-specific account/value/configuration and credentials are distinct from review authority. HTTP success may contain a body error; per-account sent/finished/retry meanings do not form a universal stage sequence. Supplied due work preserves OQ-01/02; routing, overlap, availability and exhaustive updates stay bounded. Thirty-three authored, 17 unwritten; CRT-034 next. No push, tenant or participant result.

## CRT-034 manual-delivery verification, November 12, 2026

[CRT-034 record](author/revisions/CRT-034_Revision_Record.md) maps eight fresh primary checks: Task Manager, monitoring, Understanding, provisioning overview, completion/reports, loading and Managing Sources. Same-day schema support makes nine scoped references. Task Manager file upload/aggregation, complete-listed-work, handover and the 24-hour early-completion note are bounded to the described process. Actual target change, task closure and imported/report data remain different evidence. OQ-05 was investigated through direct conflicting passages, source-owner guidance and targeted primary searches without establishing a universal routing relationship. Ten questions remain open. Thirty-four authored, 16 unwritten; CRT-035 next. No push, actual task, import or learner/tenant result.

## CRT-035 overlap and origin verification, November 12, 2026

[CRT-035 record](author/revisions/CRT-035_Revision_Record.md) maps nine fresh primary checks: reviewer, profiles, roles/automatic assignment, lifecycle states, Understanding/completion, identity processing and correct control-panel page; two same-day collection/activity checks make eleven scoped sources. OQ-07 persists after exact conflicting passages and targeted primary searches: no proven engine/action relationship reconciles independent-profile shared-right outcomes. The narrower role-required-access retention case is taught. Current role removal propagation is state/change/configuration scoped; processing starts work rather than proves delivery. Lifecycle profile enforcement is specific, not universal daily entitlement repair. Thirty-five authored, 15 unwritten; CRT-036 next. No tenant, push or learner observation.

## CRT-036 failure and retry verification, November 12, 2026

[CRT-036 record](author/revisions/CRT-036_Revision_Record.md) maps ten fresh primary references: provisioning overview, monitoring, Search, Web Services SaaS parameters/connection/timeout guide, completion/reports, loading and Understanding. Exact field/status meanings, recognized service retry errors and connector-specific HTTP retry defaults/precedence were inspected. No all-error timer, fixed combined call count, blanket timeout outcome, automatic manual fallback or broad owner rule is inferred. Existing attempts, actual target state and partial successes precede recovery choice. Thirty-six authored, 14 unwritten; CRT-037 next. Ten questions stay open; no actual tenant/notification/source change, push or learner observation.

## CRT-037 removal-evidence verification, November 12, 2026

[CRT-037 record](author/revisions/CRT-037_Revision_Record.md) maps eleven fresh sources: completion/reports, monitoring, loading/schema, identity control panels, Search, Understanding, Task Manager, Entra ID SaaS Feature Management and Microsoft application-dependent access revocation. Same-day profile evidence makes twelve scoped references. Automated source proof, work closure, actual account/effective ability and representation/report times are distinguished. Source schema and supplied native grant show the limit of group-only evidence; session examples do not establish universal logout or prescribe emergency/token procedures. Two new meanings total 166; all ten questions remain open. Thirty-seven authored, 13 unwritten; CRT-038 next. No tenant, push or learner observation.

## CRT-038 progress and notification verification, November 12, 2026

[CRT-038 record](author/revisions/CRT-038_Revision_Record.md) maps nine scoped primary references: completion, report fields, Search creation, reviewer flow, email settings and current Started/Due/whole-reassignment/partial-reassignment templates. Due body confirms weekly timing and short-campaign exclusion; controls, actual assignment, delivery and work outcome differ. Current Started page labels global variables v1; do not infer all current templates are v2. Legacy template links and unrelated exploratory results were excluded from claim evidence. No native percentage, universal permission/escalation rule, unsigned-completion result or full delivery guarantee. Four added meanings total 170. Thirty-eight authored, 12 unwritten; CRT-039 next. All ten questions remain open; no tenant, message, push or observed learner result.

## CRT-039 overdue and unsigned-work verification, November 12, 2026

[CRT-039 record](author/revisions/CRT-039_Revision_Record.md) maps ten fresh scoped primary sources: overview, Understanding, completion, manager/source-owner creation, Search creation, reviewer flow, next-generation overview, direct Complete/Finalize and reports. Understanding's unsigned-as-undecided passage still conflicts with completion's preserved-manager-choice example; direct next-generation bodies do not reconcile them. Complete verifies overdue/admin/accepted-request scope, not a visible per-item unsigned outcome or a borrowed SDK/default payload. Normal review finalization and the no-saved-choice completion case remain narrower supported teaching. One meaning brings 170 to 171. Thirty-nine authored, 11 unwritten; CRT-040 next. Ten questions remain open; no tenant, support response, push or observed learner result.

## CRT-040 completion and closure verification, November 12, 2026

[CRT-040 record](author/revisions/CRT-040_Revision_Record.md) maps eight freshly inspected sources: next-generation overview, Complete, completion help, reports, Understanding, Finalize, monitoring and account loading. Same-day CRT-039 manager/source-owner creation is reused narrowly for untouched maintenance. Normal request completion, admin outcome, report/task closure and actual account truth differ; no universal phase sequence or unsigned-saved result resolves OQ-01/OQ-02/OQ-10. Whole-intended-scope and required-result evidence, accepted follow-up and actual decision actor bound closure claims. One new meaning totals 172; forty authored, 10 unwritten, CRT-041 next. [Forty-lesson publication](author/PUBLICATION_2026-11-12_FORTY_LESSONS.md) is explicitly authorized; deployment and complete live checks must be observed before publication claims. No tenant or learner observation.

## Forty-lesson publication observed, November 12, 2026

All forty complete learners are pushed and live-verified after successful Pages run 43202690075 for content 858267c75695e77d89ff232fca40da0026869c10. Actual live result: 4582 normalized content units, forty exact diagrams/assets, forty-five tables and 1718 internal link visits; CSS and representative author/control exclusions passed. No source contract was changed by publication; ten questions remain open. Forty authored, ten unwritten; CRT-041 next. Historical per-lesson authoring and prior publication records remain unchanged; no tenant or learner observation.

## CRT-041 correction and retirement verification, November 12, 2026

[CRT-041 record](author/revisions/CRT-041_Revision_Record.md) maps twelve fresh primary references: next-generation overview, completion/deletion help, Search and manager/source-owner creation, reports, campaign PATCH/Delete, template PATCH/generation, official scoped PowerShell SDK, reviewer and reassignment guides. The actual SDK body supplies STAGED/ACTIVE edit fields hidden in rendered request details; separate objects/operations prevent implied population rebuild. Deletion removes decisions/views/reports and lacks an established queued/in-flight task rollback contract. OQ-10 remains scoped; OQ-11 records the latter missing side-effect contract rather than inventing a Cancel route. Three meanings total 175; eleven questions remain. Forty-one authored, nine unwritten; CRT-042 next. No tenant action, issue submission, push or learner observation.

## CRT-042 count and status verification, November 12, 2026

[CRT-042 record](author/revisions/CRT-042_Revision_Record.md) maps eleven fresh primary bodies: next-generation overview, reports, official SDK methods and four count/subject/certification models, direct Get Certification/Decision Summary, Understanding and administrative overview. Nine checks preceded drafting; two later bounded Acknowledge and legacy composition. Completed means all decisions in the Certification model, with separate DateSigned; campaign aggregate equivalence/native UI percentage is not inferred. Actor/filter/page/time and denominator identify the counted set. Two new meanings total177; eleven questions remain. Forty-two authored, eight unwritten; CRT-043 next. Authorized publication remains pending deployment observation; no tenant or learner result.

## Forty-two-lesson publication observed, November 12, 2026

All forty-two complete learners are pushed and live-verified after successful Pages run 43260870301 for content 15e521850e62f1914638f0a2c1f5c54458d4482d. Actual live result: 4789 normalized content units, forty-two exact diagrams/assets, forty-eight tables and 1888 internal link visits, CSS and representative author/control exclusions. Publication changes no product contract; eleven questions remain open. Forty-two authored, eight unwritten; CRT-043 next. Historical author/per-lesson/publication evidence is preserved. No tenant, graphical or learner observation.

## CRT-043 actor/history verification, November 12, 2026

[CRT-043 record](author/revisions/CRT-043_Revision_Record.md) maps fourteen fresh primary bodies: reports, reassignment, reviewer/next-generation overview, direct Finalize, Certification/CertificationReviewer/ReviewItem/Reassignment/ReassignmentTrail/ReassignmentTrailReviewer/IdentityReference models, completion and Understanding. Report Reviewer has report-specific meaning; Status Report's exact label corrects CRT-038 locally. Model fields do not establish a complete edit ledger, trail timestamps or a universal Actor contract. DateSigned is separate from Completed and signer identity. Independent all-undecided administrator completion avoids disputed saved-unsigned outcomes. OQ-01/OQ-10 remain open after fresh checks; seventeen capabilities and eleven questions remain. Two meanings total179; forty-three authored, seven unwritten, CRT-044 next. Current forty-two-entry publication preserved; no push, tenant or participant observation.

## CRT-044 report/API evidence verification, November 12, 2026

[CRT-044 record](author/revisions/CRT-044_Revision_Record.md) maps fourteen fresh primary bodies: reports, provisioning monitoring, next-generation overview, report List/Create/Get/Download operations, matching official SDK methods, CampaignReport, Get Certification, List Review Items, Standard Collection Parameters and later Understanding/reviewer checks. Specific remediation/composition availability, report-specific fields and task-versus-source Finished meanings qualify conclusions. Report creation200 means generation started; read200 may return any report status; separate IDs/metadata/permissions/download and endpoint-specific paging matter. Initial Acknowledge search missed lower-case wording; actual body and reviewer passage verify the narrower role explanation. Eight meanings total187; seventeen capabilities and eleven questions remain. Forty-four authored, six unwritten; CRT-045 next. No tenant call, exhaustive release audit, push or learner observation.

## CRT-045 mismatch diagnosis verification, November 12, 2026

[CRT-045 record](author/revisions/CRT-045_Revision_Record.md) maps fourteen fresh primary bodies: manager/source-owner and Search creation, certification reassignment, account loading/correlation, manager correlation, Understanding, filters, reports, Search FAQ, next-generation overview, certification/item reads and Work Reassignment. Actual collected data, resolved manager link, generated/current work and current view have different meanings. Optimized/unoptimized correlation conditions, package eligibility and route-specific fallback/redirect remain scoped. An initial manager URL failed; the actual linked sources/manager_correlation.html body was inspected. Role-filter/mixed-account/terminal-owner ambiguities remain OQ-06/08/09 after fresh body checks; no invented all-engine correction or single refresh rule. Three meanings total190; seventeen capabilities and eleven questions remain. Forty-five authored, five unwritten; CRT-046 next. No tenant, exhaustive update audit, push or learner observation.

## CRT-046 required-removal diagnosis verification, November12,2026

[CRT-046 record](author/revisions/CRT-046_Revision_Record.md) maps fifteen fresh bodies: Understanding/reports/completion, profiles/reviewer guide, Finalize/next-generation overview, provisioning monitoring/overview, Search Account Activity, Web Services SaaS connection/parameters, account loading, Delete and Microsoft application/session revocation. Finalization, actual source write, current permission and collection are separate; service/connector retry and completion fields retain exact scope. Role-over-profile retention is narrower than unresolved independent-profile conflict OQ-07. Fresh deletion/queue searches and direct body do not settle OQ-11; legacy aggregate search pages do not supply next-generation side effects. Main403-before-write is supplied application evidence, not every-source semantics. One meaning total191; seventeen capabilities/eleven questions. Forty-six authored, four unwritten; CRT-047 next. No tenant call, exhaustive update audit, push or learner observation.

## CRT-047 discovery-to-design verification, November12,2026

[CRT-047 record](author/revisions/CRT-047_Revision_Record.md) maps fourteen fresh bodies: manager/source-owner and Search creation, Understanding, next-generation/admin overviews, reports, provisioning overview/monitoring, loading, profiles, completion, account/manager correlation and reviewer guide. Native prerequisites, review units, actual routing, preview/start, read/write/manual result and legacy role-composition recommendation bound design commitments. Proposed targets, exception/dependency record and project responsibilities are organizational teaching practices, not native fields or timers. Tenant-specific availability and unsigned/phase/manual-owner/overlap/terminal-owner/editing questions are not invented away. Four meanings total195; seventeen capabilities/eleven questions. Forty-seven authored, three unwritten; CRT-048 next. No exhaustive release audit, tenant call, push or learner observation.

## CRT-048 readiness/acceptance verification, November12,2026

[CRT-048 record](author/revisions/CRT-048_Revision_Record.md) maps thirteen fresh bodies: dedicated/Search creation, Understanding, reports, next-generation overview/Finalize, account loading/correlation, manager correlation, monitoring, Web Services SaaS connection, reassignment and completion. Preview availability, actual data/routing, finalization/removal, read/write and task/source results retain scope. Organizational case/result labels and checkpoints are not native ISC features or a harmless dry-run. Initial manual task close fails account-result criterion; supplied correction verifies exact test result, not all production work. Unknown replacement identity authority remains unverified rather than invented as failure. Four meanings total199; seventeen capabilities/eleven questions. Forty-eight authored, two unwritten; CRT-049 next. No tenant call, exhaustive currency audit, push or learner observation.

## CRT-049 whole-project verification, November12,2026

[CRT-049 record](author/revisions/CRT-049_Revision_Record.md) maps twelve inspected primary bodies: Search creation, Understanding, campaign status/reports and completion, account loading/correlation, dedicated campaign creation, provisioning monitoring/overview, next-generation finalization/overview and reviewer guidance. CRT-049 develops COV-32 whole-project justification: a current four-account export baseline, supported selection and independent reviewer, inspected preview/start, four finalized choices, automatic and manual fulfillment, retained reading, full reconciliation and evidence-based closure. At the intermediate checkpoint only one of two removals is verified. Both are verified before closure. The changed next cycle preserves both removals: five total accounts/four identities, three export accounts/two export-holder identities. Twelve scoped primary bodies checked; 199 working meanings, seventeen capabilities and eleven unresolved questions remain. All outcomes are supplied teaching illustrations, not tenant execution or observed learner competence. Supported type-dependent selection/routing, preview versus start, finalization versus actual required work, report freshness and configured write/manual conditions bound the example. No universal cross-account propagation, unsigned policy, phase-clock or deletion remedy is inferred. Publication results belong in the separate current record.

## Observed publication boundary, November12,2026

Content 66ecaadfe6ca5c2230abe002801696747b3e5d79 was pushed to main. [Pages run 43276626821](https://github.com/TedxHarry/ISC_Certifications_Theory/actions/runs/43276626821) completed successfully. Full live verification passed for all49 learners:5789 normalized content units,49 diagrams/assets,58 learner tables and2546 internal link visits. Home entries, current-page navigation, CSS and four representative author/control exclusions passed. The first full attempt reached the last diagram asset and received HTTP503; an immediate complete rerun passed without changing content or the verifier. This proves served content/navigation, not graphical layout, learner understanding or tenant operation. Source/engine checks remain scoped; publication does not close the eleven product questions or establish exhaustive release currency.

## CRT-050 scoped changed-condition verification, November12,2026

[CRT-050 record](author/revisions/CRT-050_Revision_Record.md) maps sixteen fresh primary bodies: dedicated/Search creation, certification/work reassignment, Understanding/completion/reports, provisioning monitoring/overview, next-generation finalization/overview, reviewer, profile administration, manager correlation, account loading and filters. CRT-050 connects a missing manager and wrong preview population to truthful data correction/new coverage, unsigned reviewer absence to inspected eligible transfer/final choices, and finalized Revoke to an actual denied target removal, accepted handoff, supported correction/retry and verified outcome. The unfamiliar Warehouse case separates role-required reading from removed profile adjustment, then leaves the broader no-access requirement open until governing assignment/account evidence exists. Sixteen scoped primary bodies, full saved beginner author reading and edited-passage reread;199 working meanings/17 capability rows/11 unresolved questions remain. Examples are supplied illustrations, not tenant operation or observed learner mastery. The unavailable guessed work-reassignment path was replaced by the documented users path. No tenant API/action or exhaustive currency claim.49-entry publication unchanged;050 local.
