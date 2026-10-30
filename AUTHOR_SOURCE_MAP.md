# ISC certifications author source and verification map

Authoring source reference 2.2. Checked October 29, 2026.
Purpose: evidence planning for the theory course and its authoring foundation, not verification of unwritten lessons.
No tenant actions, test campaign, provisioning change or published course was performed.

## Primary source map

| Official source | Planned coverage |
|---|---|
| [Certifications overview](https://documentation.sailpoint.com/saas/help/certs/index.html) | CRT-001–004; object meanings, broad review/remediation responsibilities, engine migration and legacy role-composition boundary. |
| [Understanding certifications](https://documentation.sailpoint.com/saas/help/certs/understanding_certifications.html) | CRT-006/007/024/028/030/032–037; certifiable access, grant origins, self-certification, automated/manual remediation and sign-off. |
| [Starting a manager or source-owner campaign](https://documentation.sailpoint.com/saas/help/certs/starting_campaign.html) | CRT-011/012/019/021/023; prerequisites, manager/source-owner scope, missing-manager behavior and generated snapshot. |
| [Starting a campaign from Search](https://documentation.sailpoint.com/saas/help/certs/starting_search_campaign.html) | CRT-013–021/022/023; identity/access selection, reviewer choices, templates/schedules, preview generation and activation; extensions X-01–03. |
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

Current local learner: [Why review access that somebody already approved?](lessons/CRT-001_Why_Review_Previously_Approved_Access.md). [Per-lesson coverage and source evidence](author/revisions/CRT-001_Revision_Record.md). Six official pages were freshly reviewed for the bounded purpose, object, ownership, decision and outcome claims. The individual record includes loading/account-correlation references supporting the introductory data path.

This first learner is complete and author-reviewed; initial publication is verified. It has one editable diagram, one evidence table, four changed-condition cases and an independent supplier-bank-detail transfer with an uncertainty branch. Actual learner validation remains pending. The initial Pages publication and responsive reader are verified in the publication record. No tenant operation occurred.

Next is CRT-002. Other planned topics and the exhaustive release audit remain uncompleted. Original foundation counts above record the setup stage, not today's authored learner count.

## Initial publication request, October 30, 2026

The user authorized a new ISC_Certifications_Theory repository, push and Pages publication before local CRT-002 authoring. The repository is created and the publication manifest includes CRT-001 only. [Publication evidence](author/PUBLICATION_2026-10-30_INITIAL.md) records the build and live checks. Earlier no-repository/local-only statements describe their dated authoring stages. Actual learner validation remains pending.

Initial publication verified October 30, 2026: content 98f1a263e6e8990ab99506de40f2c757a635b18c built successfully in workflow 41007230219. All 104 normalized CRT-001 content units, its diagram/table/asset, internal links and four representative author-route exclusions passed live checks. Desktop/mobile review found no page-wide horizontal overflow; native panel toggle worked and the mobile table scrolled within its own region. Actual learner validation is still unperformed.
