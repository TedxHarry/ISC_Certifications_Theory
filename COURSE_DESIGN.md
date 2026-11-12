# SailPoint ISC Certifications: Understanding Access Reviews from Scope to Verified Outcome

Course design 7.4. November 12, 2026.
Subject confirmed: ISC access review and certification campaigns.
Status: forty-two topics are authored and author-reviewed. CRT-001–007 are revision 1.1; CRT-008–042 are 1.0. Forty-two are prepared in nine reader modules for authorized publication; forty remain the last live-verified snapshot pending deployment. CRT-043 is next.

Current priority: finish authorized publication, then prepare CRT-043's brief and primary checks for actual decision actor/history and finalization. Eight core candidates remain unwritten; five specialist routes stay planned. Preserve earlier learners/evidence and reader implementation; eleven questions remain open.

[Author source and verification map](AUTHOR_SOURCE_MAP.md).
[Operational task coverage](OPERATIONAL_TASK_COVERAGE.md).
[Teaching specification](TEACHING_SPECIFICATION.md).
[Current position and next lesson](COURSE_REGISTER.md).

## Purpose and audience

This course teaches beginners and freshers how ISC certifications work and how to reason about everyday campaign work. The learner has basic workplace-account knowledge; no prior ISC lesson is required to understand a particular lesson.

The goal is a person who can explain a review, plan its scope, identify the right reviewers, interpret decisions, trace removal and select evidence for the result. Theory prepares that reasoning; actual operation and recovery still need later hands-on practice.

The organizing question is: “How do we establish that the intended access was reviewed by an appropriate person, and that the required outcome happened?”

Completion percentages alone cannot answer that question. The course connects business purpose, represented access, campaign content, reviewer responsibility, final decisions, fulfillment and evidence.

## Teaching approach

Use the approved ISC mentor approach: personal, patient, polite and clear, as if sitting beside one learner. Explain the necessary term before relying on it. Follow what happens, which record or setting is involved, why the result follows and what the next process needs.

Teach directly. No fictional company, employee biography, continuing storyline, prerequisite announcements or comments about the teaching method in learner lessons. Small neutral values, selected records and short supplied situations remain when they explain a mechanism.

Lessons must work independently. Reintroduce supporting meanings in context, without repeating a preliminary glossary. A lesson on removal briefly establishes certification, final decision and provisioning before tracing delivery.

Let the topic decide its shape. No fixed number of headings, diagrams, tables, questions or words. Finish a useful normal mechanism before adding variations where that improves understanding.

The working authoring default is the next-generation certification engine for normal examples where that functionality is supported. Use a clearly marked legacy explanation when that workflow differs or remains legacy-only. Identify the engine before relying on its states or behavior; do not make the learner compare both engines in every lesson.

The current inventory contains 50 planned topics, provisionally arranged into 10 modules. Neither count is a requirement, minimum or maximum. Final modules and lesson boundaries must follow the concepts, dependencies and actual explanation needed. Split an overloaded topic, combine genuine overlap and move topics when that improves learning. Do not preserve ten modules for visual symmetry or fifty lessons for marketing. The CRT identifiers below are planning labels; preserve a lesson's identifier once authored.

## What the learner should be able to do

- Explain campaign, assigned certification, review item, reviewer, decision, sign-off and remediation in their own words.
- Explain how aggregation, account ownership and the access model affect review content.
- Distinguish selecting people from selecting their access.
- Choose a campaign approach for a business review requirement.
- Validate generated content and reviewer assignments before starting a review.
- Explain Approve, Revoke and Acknowledge in the applicable access context.
- Trace a final review decision into automated or manual fulfillment and target verification.
- Investigate missing reviews, wrong reviewers, unresolved decisions and access that remains.
- Build a campaign plan, exception record and evidence pack suitable for an operational handoff.

## What completion can and cannot establish

The intended theory outcome is independent explanation and reasoned handling of common campaign situations using requirements, configuration and supplied evidence. Reading every page does not establish competence by itself.

For the core, the learner should demonstrate that they can:
- Explain the necessary terms in their own words and connect them to the correct records and processes.
- Trace an unfamiliar campaign from collected data through scope, routing, decisions and the required outcome.
- Predict a meaningful changed condition and state the assumptions behind that prediction.
- Choose evidence that distinguishes missing input, incorrect configuration, unfinished work and failed delivery.
- Produce a justified campaign plan, readiness criteria, exception response and evidence-based handoff.
- Recognize when a task depends on unfamiliar engine behavior, licensing, connector capability or authoritative clarification.

An assessment passes when the reasoning identifies the correct objects, inputs, decision/operation, conditions and evidence without inventing a result. Worked examples alone are preparation; use an uncoached changed case to assess transfer.

Production operation also requires hands-on practice, tenant-specific permissions and configuration knowledge, and the organization's change procedures. This theory course cannot promise that a beginner can immediately perform every certification task, every custom integration or any future feature. It should prepare them to investigate unfamiliar work methodically rather than guess.

## Keeping the content current

The design includes the major current certification areas, but it has not passed an exhaustive release-by-release feature audit. Do not describe an outline, a list of sources or an unwritten lesson as proof that all new updates are covered.

Maintain an author update register with the capability/change, primary source and date, availability status, engine, licensing/prerequisites, affected lesson, explanation or example change, and verification status.

Distinguish generally available behavior, limited/phased availability, legacy behavior and planned announcements. Planned functionality is not taught as released. Use the current engine as proposed where supported, with relevant differences explained beside the affected process.

Check official documentation, release information and product announcements before writing and publication, then revise affected explanations when verified behavior changes. A feature list at the back cannot replace updates to the lessons whose flows or outcomes changed.

The update register is a maintenance requirement, not an automated monitoring service. Current certification documentation still signals phased availability, and the next-generation API is marked Experimental. Exact release and tenant coverage must be established, not inferred from a feature's name.

## The processes we connect

The course follows this dependency map, rather than asserting one universal backend transaction:

```text
External account and access data
  -> collection and correct ISC representation
  -> campaign scope, access eligibility and reviewer rules
  -> generated review content and preview validation
  -> active reviewer work and decision finalization

Finalized decisions that require removal
  -> applicable automated provisioning or manual fulfillment
  -> source-system outcome and refreshed ISC observations
```

In parallel, administrators monitor progress, deadlines, exceptions and completion. Campaign status, reviewer sign-off and remediation status are separate evidence. Remediation is not taught as something that universally waits for the whole campaign to close.

For each important UI state, explain what record or operation it represents and how it became available. Cover documented processing, asynchronous work and supported API observations when useful. Do not invent private queues, database tables or microservices.

## Provisional core table of contents

### Module 1. Understand what the review is trying to achieve

Outcome: explain the review's purpose and distinguish its objects and processes.

| Plan ID | Lesson | Coverage |
|---|---|---|
| CRT-001 | Why review access that somebody already approved? | Continuing business need, accumulated access, changed circumstances and the purpose of periodic review. |
| CRT-002 | A campaign, a certification and a review item: what is being assigned? | Campaign container, assigned review, access item, decision and sign-off; creator/owner, administrator, reviewer and remediation responsibilities; responsibility versus permission. |
| CRT-003 | Follow one review from access data to a verified outcome | Actors, input, generation, review, decision finalization, removal and evidence; parallel administrative work. |
| CRT-004 | How is a certification different from an access request or lifecycle rule? | Review of represented access, request approval and access-model enforcement; which control can change what. |

### Module 2. Understand the access that reaches a review

Outcome: explain both visible review content and meaningful omissions.

| Plan ID | Lesson | Coverage |
|---|---|---|
| CRT-005 | How does application access become information ISC can review? | Source accounts, entitlements, aggregation, correlation, freshness and represented versus live access. |
| CRT-006 | Are we reviewing an entitlement, an access profile or a role? | Access objects, their relationships, assignment origins and the review's unit of decision. |
| CRT-007 | Why does some access appear differently or not appear at all? | Certifiable access, role-encapsulated access, lifecycle grants and acknowledgement of automatically assigned roles. |
| CRT-008 | One person has two accounts. Which account's access is under review? | Ordinary and administrator accounts, ownership, identifiers and correct target evidence; recognizing uncorrelated and service/machine-account cases without assuming employee ownership. |
| CRT-009 | Can the reviewer understand what this access actually permits? | Useful descriptions, business meaning, ownership, privileged access context and relevant displayed attributes. |
| CRT-010 | How do we establish that the review population is complete? | Intended baseline, identity/account/access populations, exclusions and reconciliation beyond matching totals. |

### Module 3. Choose the review approach

Outcome: translate the business question into the appropriate campaign design.

| Plan ID | Lesson | Coverage |
|---|---|---|
| CRT-011 | When is a manager review the right choice? | Business knowledge, manager relationships, scope and prerequisite data. |
| CRT-012 | When should source owners review access? | Source ownership, technical/business knowledge, selected sources and focused application reviews. |
| CRT-013 | Start with people or start with access items? | Identity-oriented and access-item-oriented campaign selection; how the review population changes. |
| CRT-014 | Which access should we review for the selected people? | Identity selection versus access refinement; avoiding unintended all-access reviews. |
| CRT-015 | Which campaign design answers this business question? | Comparing designs; assignment review versus role-composition review; recognizing when specialist account reviews are needed. |

### Module 4. Scope, generate and validate the campaign

Outcome: explain why an item is included and establish readiness to start.

| Plan ID | Lesson | Coverage |
|---|---|---|
| CRT-016 | What does this search actually select for the campaign? | Query result meaning, identity versus access searches, test cases and selection errors. |
| CRT-017 | How do campaign filters include or exclude review content? | Supported identity, identity-attribute, account-attribute, source and access criteria; filter scope. |
| CRT-018 | What happens when selection rules and filters are combined? | Documented combination/grouping behavior, inclusions, exclusions, encapsulation and changed-condition examples. |
| CRT-019 | What was captured when this review was generated? | Generated campaign data, snapshot boundaries, changes to access/managers afterward and preview regeneration considerations. |
| CRT-020 | A template, a schedule and a running campaign are different things | Reusable definition, scheduling, generation, preview and activation; what starts automatically in the applicable engine. |
| CRT-021 | What must be checked before the campaign reaches reviewers? | Actual generated identities, items, reviewers, exceptions, representative samples, due dates, comments and notification settings; authorized administration and launch responsibilities. |

### Module 5. Get the review to the right person

Outcome: explain reviewer assignment and repair routing without losing the control's purpose.

| Plan ID | Lesson | Coverage |
|---|---|---|
| CRT-022 | Who becomes the reviewer, and why? | Manager, source/access owner, selected individual and governance-group routes where supported; routing versus decision maker, Cert Admin/Org Admin permissions and ownership responsibilities. |
| CRT-023 | What happens when a manager or owner is missing? | Campaign-specific exclusion and fallback paths, invalid ownership and evidence for the actual assignee. |
| CRT-024 | How does ISC prevent someone reviewing their own access? | Self-certification prevention, splitting/reassignment, fallback responsibility and reassignment restrictions. |
| CRT-025 | When should a review be reassigned? | Administrative and reviewer actions, permitted granularity, current state, sign-off restrictions and recorded responsibility; checking why an assigned reviewer cannot see or access a review. |
| CRT-026 | The reviewer is absent or leaves during the campaign. What now? | Work reassignment versus campaign reassignment, timing, supported behavior and continuity evidence. |

### Module 6. Make and finalize a defensible decision

Outcome: explain a decision's business meaning and whether it is final.

| Plan ID | Lesson | Coverage |
|---|---|---|
| CRT-027 | What information should a reviewer inspect before deciding? | Person, account, access meaning, assignment origin, current need and conflicting or stale evidence; interpreting available flags without treating them as the decision. |
| CRT-028 | What do Approve, Revoke and Acknowledge actually mean? | Available actions by access origin and review type; approval is not a request to grant missing access. |
| CRT-029 | What makes a decision explainable later? | Useful comments, approved decision criteria, bulk decisions and preventing mechanical approval. |
| CRT-030 | Is a saved decision the same as a signed-off review? | Item decision, submitted/final review, permitted changes and engine-specific unsigned-decision behavior. |
| CRT-031 | What if the reviewer cannot confidently decide? | Missing evidence, appropriate consultation/reassignment, access flags and recommendations as decision inputs where available. |

### Module 7. Follow revocation into actual access removal

Outcome: trace the correct access item through delivery and verify the result.

| Plan ID | Lesson | Coverage |
|---|---|---|
| CRT-032 | Revoke was selected. What should happen next? | Decision finalization, applicable removal trigger, immediate versus supported deferred revocation and required timing evidence. |
| CRT-033 | How does automated removal reach the application? | Supported write capability, authorized integration, account/item targeting, operation result and asynchronous completion. |
| CRT-034 | What happens when access must be removed manually? | Assigned task, human source-system action, task closure, changed source data and subsequent ISC observation. |
| CRT-035 | Why can access remain after one assignment is revoked? | Shared entitlements, overlapping access profiles, role/lifecycle origins and required changes to the access model. |
| CRT-036 | How do we investigate pending, failed or partial removal? | Supported retries, denied writes, partial outcomes, remediation ownership and avoiding unsupported retry promises. |
| CRT-037 | What evidence establishes that the required removal happened? | Decision, operation/task, correct target state, refreshed ISC data and remaining effective access; session effects only when relevant. |

### Module 8. Run and close the campaign

Outcome: operate the review without confusing administrative progress with effective access.

| Plan ID | Lesson | Coverage |
|---|---|---|
| CRT-038 | How do reminders and progress monitoring help the campaign? | Notification configuration, reviewer progress, follow-up ownership and interpreting pending work. |
| CRT-039 | What happens to overdue, undecided or unsigned reviews? | Distinct states, configured completion choices, operational consequences and engine-verified behavior. |
| CRT-040 | What does completing a campaign actually establish? | Review sign-off, administrator completion and remediation completion; required follow-up after closure. |
| CRT-041 | When should a campaign be corrected, regenerated or retired? | Wrong scope, wrong generated data, permissible changes and supported cancellation/deletion/retention decisions by state and engine. |

### Module 9. Read the evidence and diagnose problems

Outcome: identify the failing stage and justify the next investigation.

| Plan ID | Lesson | Coverage |
|---|---|---|
| CRT-042 | What are the campaign's counts and statuses counting? | Campaign/reviewer/item units, denominators, state meanings and misleading completion percentages. |
| CRT-043 | Who made the decision, and what was finally signed off? | Decision history, assigned reviewer versus decision maker, reassignment, comments and sign-off evidence. |
| CRT-044 | Which report answers the question we are asking? | Composition, status, sign-off, remediation and provisioning evidence; report-generation time and current state; basic read-only API ID/response/status interpretation with the applicable engine and permissions. |
| CRT-045 | The person, item or reviewer is wrong. Where did the mismatch begin? | Data, ownership, uncorrelated accounts, query, filter, grant origin, routing, reviewer visibility and permissions using a layered diagnostic trace. |
| CRT-046 | The review says Revoke, but access still works. How do we investigate? | Finality, timing, fulfillment, target account, overlap, stale observations and evidence-based closure. |

### Module 10. Reason through a real campaign project

Outcome: produce a defensible plan and handle a changed condition without memorized steps.

| Plan ID | Lesson | Coverage |
|---|---|---|
| CRT-047 | What do we need to discover before designing the campaign? | Business objective, population, systems, access owners, decision criteria, timing, fulfillment responsibilities and evidence needs. |
| CRT-048 | How do we build a campaign readiness and acceptance plan? | Data prerequisites, representative test cases, expected inclusion/routing, valid decisions, delivery checks and change review. |
| CRT-049 | Design and explain a complete periodic access review | Neutral project brief; justify scope, reviewers, exceptions, operation and closure without a fictional-company dependency. |
| CRT-050 | Can you defend the outcome when conditions change? | Teach-back and diagnosis with missing managers, absent reviewers, unresolved decisions, overlap and denied target operations; handoff and improvements. |

## Routine work is the core

Organize teaching around recurring work before launch, during review and after decisions. Every important routine task must have a named coverage location, a reasoned normal path, useful failure conditions and the evidence needed to verify the outcome. See the operational task coverage map.

Common does not mean daily in every organization. This is a recommended operational syllabus, not a measured ranking of how frequently customers perform tasks.

Core coverage includes data/ownership readiness, choosing the review approach, queries and filters, templates/schedules, preview validation, authorized launch, reviewer visibility and routing, reassignment, notifications, decisions/comments/sign-off, deadlines, manual and automated removal, failures, overlap, reports and closure.

Uncorrelated-account recognition and its effect on ordinary scope/ownership investigation are core. Understanding reviewer-visible flags and recommendations where present is core. Basic API literacy for interpreting campaign IDs, access permissions, request/response records and operation/status evidence is core; it does not require scripts or an API endpoint catalogue.

The specialist distinction concerns depth and job responsibility. A learner should recognize a specialist review need, explain its purpose and know the relevant limits after the core. Detailed configuration, unusual scenarios and automation belong in a job-dependent extension. An extension becomes required for a learner whose actual responsibilities need it.

## Specialist extensions

These are deeper routes selected by job or project need. They are not a classification of unimportant or rare work. Essential recognition and operational implications are taught in the core. Complete the relevant extension before claiming readiness for that specialist responsibility.

| Extension | Subject | When it belongs in the learner's route |
|---|---|---|
| X-01 | Role-composition certifications | Core CRT-006/015 explains composition versus assignment. Detailed role-review and manual role-update reasoning is required for role-governance work. Current documentation places this in the legacy engine. |
| X-02 | Uncorrelated-account certifications | Core CRT-005/008/010/045 covers recognition, scope and ownership investigation. This route develops the dedicated account-review campaign and remediation scenarios. |
| X-03 | Machine-account certifications | Core CRT-008/009/015 introduces non-human accounts and ownership questions. Detailed supported campaign behavior is required for machine/service-account governance work. |
| X-04 | Rich decision support | Core CRT-027/031 teaches how to interpret available reviewer context. This route deepens licensed insights, configuration, limitations and unusual cases. |
| X-05 | API and automation depth | Core CRT-042/044/045 includes basic operational API literacy. This route develops bulk/paginated investigations, template/filter/schedule automation and version/engine dependencies; no scripting exercises in this theory course. |

Do not expand these into broad AI, non-human identity or API-development courses. Include deeper treatment only when it answers an actual certification requirement.

## Length and overlap review

Judge length by useful learning and unnecessary repetition, not module count. Every lesson needs a distinct question, a meaningful explanation and an observable outcome. A term requiring only a short contextual explanation does not automatically need a separate lesson.

Review these intersections during detailed planning: campaign orientation versus access refinement (CRT-013/014); decision finality versus deadline/completion handling (CRT-030/039/040); and normal revocation, verification and failure diagnosis (CRT-032/037/046). Preserve different reasoning goals while removing repeated full explanations. These are overlap checks, not decisions to merge unlike processes.

Use a task-to-lesson coverage map to detect missing work and redundant lessons before authoring. Keep specialist depth outside the normal route unless it is needed for common certification work. A learner should not have to complete every specialist route to understand the core.

## How an individual lesson should teach

A lesson on missing reviewers begins with what is missing and the generated campaign's actual assignment. It explains manager/owner inputs and the applicable campaign rules, follows the relevant branch, then identifies which evidence would establish the cause. It does not begin with a list of configuration fields.

A revocation lesson first explains that a review decision and application access are different records. It traces the final decision to the applicable removal work and target observation. It introduces remediation as the work needed to carry out the removal, rather than asking the learner to memorize the term.

Examples must say what exists, which values/settings apply and which outcome is supplied. Change one meaningful condition when useful. Unavailable evidence is a valid conclusion, not an invitation to invent behavior.

Use questions that test reasoning: explain the result, predict a changed case, locate the missing dependency or choose evidence. Worked answers explain why; they do not simply state the correct option.

## Diagrams and supporting reference aids

Use a visual when it makes a relationship or branching flow easier to follow. Planned useful diagrams include campaign/certification/item relationships, generated-content dependencies, reviewer routing, decision/sign-off/remediation boundaries, automated versus manual delivery, overlapping assignments and evidence timing.

These are candidate visuals, not one per lesson or a fixed quota. Editable diagrams need a clear actor, arrow meaning, assumptions and supporting prose.

Develop these aids with the relevant lessons:
- Certification object and terminology map.
- Certifiable-access and assignment-origin comparison.
- Campaign scope/preview validation worksheet.
- Reviewer-routing comparison.
- Decision, sign-off and remediation state map.
- Revocation evidence and troubleshooting trace.
- Campaign project-discovery and closure pack.

Explain needed material inline. Keep authoritative sources and verification dates in author records, not learner lessons. The later site may reuse press-and-hold definitions with touch and keyboard equivalents; essential understanding must remain in the prose.

## Content boundaries and quality controls

Focus the core on routine manager/source-owner and targeted campaigns, scope, reviewer work, decisions, remediation, reports and project reasoning. Include just enough ISC identity/access foundations to support those mechanisms.

Exclude certification-exam preparation, a general IAM history course, IdentityIQ-specific workflows, every connector's internals, full API/SDK tutorials and arbitrary performance benchmarks. Product availability and engine differences are documented conditions, not universal promises.

Use an author capability matrix to separate current-engine, legacy and conditional functionality. Normal examples use the proposed next-generation baseline; legacy examples are bounded and identified. Include a permission/responsibility comparison for Cert Admin, Org Admin, campaign creator/owner, reviewer, source/access owner and remediation owner. Verify which actions each may perform instead of equating an ownership label with an administrative permission. Recheck before authoring and publication. Core explanations teach stable concepts first; place relevant engine differences beside the affected behavior, not in every paragraph.

The documentation contains a material inconsistency about unsigned decisions at administrator completion. CRT-030 freshly investigates OQ-01 and teaches verified normal next-generation reviewer sign-off with a clearly bounded administrator-completion uncertainty. Before specific outcomes in CRT-039/040, establish the exact engine/type behavior. Do not silently choose one passage or imply a tested tenant result. OQ-10 separately tracks ambiguous post-completion editing wording.

Each authored lesson needs a coverage record, primary-source check, complete saved-file beginner read-through, example/diagram consistency check and reasoned assessment. Actual uncoached beginner validation is recorded separately and remains pending until it occurs. A simulated author review cannot claim that a learner understood.

## Delivery plan and next step

The user authorized establishing the local authoring foundation on October 29, 2026. The folder ISC_Certifications_Theory now contains the teaching specification, progress register, author workflow and first brief, coverage/terminology records, capability/update register and routine task map. Forty-two learners are authored and prepared in nine reader modules for authorized publication; forty remain the previous live-verified snapshot pending the new deployment. The [forty-lesson publication record](author/PUBLICATION_2026-11-12_FORTY_LESSONS.md) gives the current snapshot; earlier publication records are historical. See [the thirty-one-lesson publication record](author/PUBLICATION_2026-11-11_THIRTY_ONE_LESSONS.md) for the exact published snapshot and executed checks.

Use [README](README.md) to navigate the package and [COURSE_REGISTER](COURSE_REGISTER.md) to resume. Write one complete learner lesson at a time with its necessary reference aids, author record and saved-file checks.

CRT-001 through CRT-042 have complete author records. The following early-topic descriptions and dated entries preserve their historical scope; the next learner is CRT-043. CRT-002 develops the campaign/assigned-review/item hierarchy and responsibility/permission foundations. CRT-003 follows collected access through review, applicable removal work and exact-account evidence, with automated/manual paths and an independent two-account transfer. CRT-004 develops the request/review/lifecycle comparison, package decision scope and the requirement behind lifecycle-restored access. CRT-005 develops account-schema/collection/catalog/identity connections, information freshness and the missing field in an independent transfer. CRT-006 develops the access object and assignment origin as the basis for decision scope, including role direct entitlements, detection, automatic-role acknowledgement and composition recognition. CRT-007 develops expected representation versus missing data/selection/time evidence through one four-right example and an independent three-absence transfer. Detailed remaining mechanisms stay with their primary lessons. CRT-008 develops exact account/ownership context and core special-account recognition with an independent wrong-account transfer. CRT-009 develops useful descriptions, access ownership, relevant person/access context and privileged-access recognition, with an independent misleading-package transfer. CRT-010 develops independent population baselines and actual people/account/access reconciliation, with retrieval/representation/time limits and a warehouse-account transfer. CRT-011 develops the manager current-need question and data/routing prerequisites, with a changed-manager warehouse transfer. CRT-012 develops source-focused ownership/knowledge, included-source readiness and actual review assignment, with a changed-owner/new-source transfer. The existing-lesson revision pass is complete. CRT-013 develops identity/access-object selection and separate resulting access scope through an entitlement comparison and a requested-role transfer. CRT-014 develops the all/refined-access mechanism, saved choice and package/account boundaries with a production-account transfer. CRT-015 develops requirement-led approach comparison, assignment versus composition, legacy manual follow-up and account-route recognition through an Inventory Reader transfer. CRT-016 develops query categories, exact fields/values, operators/grouping and same-record account conditions with a changed-input transfer. CRT-017 develops filter criteria/modes, person versus item scope, display-name matching, package/source boundaries and a changed-label transfer. CRT-018 connects grouped people queries, actual selection, refined access and supported exclusions through a six/four/two trace and a profile-origin transfer. Continue with the current task in the register, preparing its brief and source checks through [the authoring guide](author/AUTHORING_GUIDE.md). Read the complete saved lesson as an unfamiliar beginner and revise from actual feedback when available. A hands-on course is a separate later project.

On October 30, 2026 the user authorized creating ISC_Certifications_Theory, pushing the saved work and publishing Pages before continuing locally. The new reader reuses the established course layout and lists only completed lessons included in the publication. See [publication evidence](author/PUBLICATION_2026-10-30_INITIAL.md).

The latest push-and-continue request published CRT-002/003 without changing their reviewed content. All three learners are live-verified; [publication evidence](author/PUBLICATION_2026-10-30_CRT-002_CRT-003.md). CRT-004 is now published and live-verified; CRT-005 is published and live-verified; CRT-006 is published and live-verified; CRT-007 is complete locally; CRT-008 is next.

The latest push-and-continue request published CRT-004 unchanged from its author-reviewed learner/asset snapshot. Four lessons are live-verified; [publication evidence](author/PUBLICATION_2026-10-30_CRT-004.md). CRT-005 is now published and live-verified; continue CRT-006 locally.

On October 31, 2026, the latest push-and-continue request published CRT-005 and opened module 2's first available lesson in the reader. All five lessons are live-verified; [publication evidence](author/PUBLICATION_2026-10-31_CRT-005.md). CRT-006 is published and live-verified; CRT-007 is now complete locally; continue CRT-008.

The latest October 31 push-and-continue request published CRT-006 unchanged from its reviewed learner/asset snapshot. Six lessons are live-verified; [publication evidence](author/PUBLICATION_2026-10-31_CRT-006.md). CRT-007 is now complete locally; continue CRT-008.

On November 2, 2026 the user reported the revised CRT-004 explanation better and requested continuation. CRT-008 is complete locally under teaching specification 1.1, covering exact account context, different needs on one person's accounts, ownership and core special-account recognition. It includes a wrong-account removal transfer and preserves the earlier lesson files. No push occurred. Eight topics are authored and 42 current candidates remain unwritten; CRT-009 is next. The dated continuation paragraphs above remain historical.

On November 2, 2026 the user clarified that the improved explanation was intended for all lessons. Moving directly to new CRT-008 had skipped that existing-lesson pass. CRT-001 is now rewritten locally at 1.1 with its original coverage preserved. Continue with CRT-002's rewrite, followed by CRT-003/005/006/007. Preserve CRT-004 and CRT-008; no new topic or publication was added during this scope correction.

Later on November 2, 2026 the user's push instruction published all saved work. The current eight-lesson snapshot is live-verified: CRT-001/004 revision 1.1 and the other six revision 1.0. [Publication evidence](author/PUBLICATION_2026-11-02_EIGHT_LESSONS.md) records content, deployment and checks. This does not complete the five pending rewrites; CRT-002 remains next. Historical local/unpublished statements above describe their dated authoring stages.

On November 11, 2026 CRT-002 was rewritten locally under teaching specification 1.1 with its original hierarchy, actor, authority, progress and transfer coverage preserved. [Revision evidence](author/revisions/CRT-002_Revision_1_1_Record.md) records current sources and author checks. No publication occurred; CRT-003 is next in the four-lesson revision queue. Earlier dated publication/continuation statements remain historical.

On November 11, 2026 CRT-003 was rewritten locally under teaching specification 1.1. Its original data-to-review-to-change-to-evidence coverage, automatic/manual distinction and independent two-account transfer are preserved. [Revision evidence](author/revisions/CRT-003_Revision_1_1_Record.md) records sources and author checks. No publication occurred; CRT-005 is next in the three-lesson revision queue. Earlier dated stages remain historical.

## CRT-005 explanation revision, November 11, 2026

[CRT-005 revision 1.1](lessons/CRT-005_From_Application_Access_to_Reviewable_Information.md) is complete locally. [Its record](author/revisions/CRT-005_Revision_1_1_Record.md) reconciles the original account-data, entitlement, identity-link, review-selection and observation-time teaching, including the different-source transfer. The clearer explanation preserves technical scope. Eight topics are authored and 42 remain unwritten; CRT-006/007 remain to revise. No publication or independent learner pass is claimed.

## CRT-006 explanation revision, November 11, 2026

[CRT-006 revision 1.1](lessons/CRT-006_Entitlements_Access_Profiles_and_Roles_in_a_Review.md) is complete locally. [Its new record](author/revisions/CRT-006_Revision_1_1_Record.md) reconciles all original permission/package/role, assignment-origin/action, containment, composition and account-outcome teaching. The original partial-need payments-role transfer remains. CRT-007 is the one remaining earlier rewrite. Eight topics are authored and 42 remain unwritten. No publication or independent learner pass is claimed.

## CRT-007 explanation revision, November 11, 2026

[CRT-007 revision 1.1](lessons/CRT-007_Why_Access_Appears_Differently_or_Is_Missing.md) is complete locally. [Its new record](author/revisions/CRT-007_Revision_1_1_Record.md) reconciles all 24 original purposes, four-right/three-item example and three-absence transfer. The existing-lesson rewrite pass is complete; CRT-009 is next. Eight topics remain authored and 42 unwritten. Publication and independent learner assessment remain separate and unperformed for the new revision.

## CRT-009 authored locally, November 11, 2026

[CRT-009](lessons/CRT-009_Understanding_What_Access_Actually_Permits.md) is complete at revision 1.0. [Its author record](author/revisions/CRT-009_Revision_Record.md) maps actual COV-08 teaching, seven primary references, six new working meanings and the finance/support examples. Description quality is connected with actual capability and this person's need, with package/privilege/metadata limits and authorized correction versus actual permission change. Nine topics are authored and 41 remain unwritten; CRT-010 is next. No publication or independent learner result is claimed.

## CRT-010 authored locally, November 11, 2026

[CRT-010](lessons/CRT-010_Checking_That_the_Review_Population_Is_Complete.md) is complete at revision 1.0. [Its record](author/revisions/CRT-010_Revision_Record.md) maps COV-09, ten primary references, four new working meanings and actual comparison/transfer checks. Equal totals, complete generated work, account and package scope, exclusions, observation times and whole-result evidence are explained without an invented automatic validator. Ten topics are authored and 40 remain unwritten; CRT-011 is next. Publication and independent learner assessment remain separate.

## CRT-011 authored locally, November 11, 2026

[CRT-011](lessons/CRT-011_When_a_Manager_Review_Is_the_Right_Choice.md) is complete at revision 1.0. [Its record](author/revisions/CRT-011_Revision_Record.md) maps manager purpose/prerequisite COV-10 teaching, eight primary references and five new meanings. Source manager reference, resolved relationship and generated assignment are explained separately; dedicated Manager Campaign and Search Manager missing-manager behavior remain scoped. Stale/nonblank data, changed assignment, current knowledge and authority are tested in the transfer. Eleven topics are authored and 39 unwritten; CRT-012 is next. No publication or observed learner pass is claimed.

## CRT-012 authored locally, November 11, 2026

[CRT-012](lessons/CRT-012_When_Source_Owners_Should_Review_Access.md) is complete at revision 1.0. [Its record](author/revisions/CRT-012_Revision_Record.md) maps source-owner purpose/prerequisite COV-10 teaching, ten primary references and the new source-owner-review meaning. Source/access ownership, actual reviewer and actual removal responsibilities remain distinct. The dedicated route requires owners on included sources; metadata changes do not establish an existing review's scope or reassignment. Twelve topics are authored and 38 unwritten; CRT-013 is next. No publication or observed learner pass is claimed.

## CRT-013 authored, November 11, 2026

[CRT-013](lessons/CRT-013_Starting_with_People_or_Access_Items.md) is complete at revision 1.0. [Its record](author/revisions/CRT-013_Revision_Record.md) reconciles COV-11 selection meaning, eight primary references, local term explanations, the two-path diagram and independent requested-role transfer. Both creation routes retain a later access choice; standalone/container conditions and reviewer responsibility are kept distinct. Thirteen topics are authored, 37 remain unwritten and CRT-014 is next. All saved work is authorized for publication; deployment evidence is recorded after execution. Independent learner assessment remains pending.

## Thirteen-lesson publication, November 11, 2026

All thirteen learners and the five earlier local rewrites are pushed and live-verified. Content 470c4a5008b7d6d6724cf16ce57c9c4e64fabd5d deployed successfully in [Pages run 43024965366](https://github.com/TedxHarry/ISC_Certifications_Theory/actions/runs/43024965366). Live checks passed for 1555 content units, thirteen diagrams/assets, fifteen tables, 206 internal link visits, CSS and representative author/control exclusions. [Publication evidence](author/PUBLICATION_2026-11-11_THIRTEEN_LESSONS.md) distinguishes this from learner assessment or graphical review. CRT-014 remains next; 37 candidate core topics remain unwritten.

## CRT-014 authored locally, November 11, 2026

[CRT-014](lessons/CRT-014_Choosing_Access_for_the_Selected_People.md) is complete at revision 1.0. [Its record](author/revisions/CRT-014_Revision_Record.md) maps COV-11 access refinement, eight primary references and the full saved beginner author read-through. The question was clarified to avoid treating people selection and access scope as alternatives; coverage is preserved. Main and transfer cases distinguish saved choices, existing holdings, actual review items and decisions without a grant or account-row inference. Fourteen topics are authored, 36 remain unwritten and CRT-015 is next. The thirteen-entry reader manifest and published snapshot remain unchanged. Actual learner assessment is pending; no push or tenant action occurred.

## CRT-015 authored locally, November 11, 2026

[CRT-015](lessons/CRT-015_Choosing_a_Campaign_Design_for_the_Business_Question.md) is complete at revision 1.0. [Its record](author/revisions/CRT-015_Revision_Record.md) maps COV-10's approach comparison, nine scoped primary references and complete saved beginner author reading. The new assignment-review term and expanded existing composition meaning distinguish a person's holding from a shared role definition. Manager/source-owner knowledge, selection and reviewer configuration remain complementary choices. Legacy composition and account routes are bounded recognition, not completed specialist procedures. Fifteen topics are authored, 35 remain unwritten and CRT-016 is next. CRT-014/015 remain local; publication is unchanged. No participant pass or tenant execution is claimed.

## CRT-016 authored locally, November 11, 2026

[CRT-016](lessons/CRT-016_Understanding_What_a_Campaign_Search_Selects.md) is complete at revision 1.0. [Its record](author/revisions/CRT-016_Revision_Record.md) reconciles COV-11 query meaning, eight scoped primary references, five new working meanings and the full saved beginner read-through. Literal query examples are based on checked grammar/fields and supplied data, not tenant execution. The same-account diagram and Warehouse transfer test why records match; source data, saved selection and generated campaign remain separate. Sixteen topics are authored, 34 unwritten and CRT-017 next. Local CRT-014 through CRT-016 preserve the thirteen-lesson publication; no participant or tenant result is claimed.

## CRT-017 authored locally, November 11, 2026

[CRT-017](lessons/CRT-017_Including_and_Excluding_Review_Content_with_Campaign_Filters.md) is complete at revision 1.0. [Its record](author/revisions/CRT-017_Revision_Record.md) maps COV-12's filter foundation, ten scoped primary references, four new working meanings and the full saved beginner read-through. All seven criterion families receive meaningful treatment; Role effect and mixed-account propagation are explicitly bounded rather than assigned invented outcomes. OQ-06 remains open and new OQ-08 records the latter scope gap. Seventeen topics are authored, 33 unwritten and CRT-018 next. CRT-014 through CRT-017 remain local; publication, actual learner validation and tenant execution are unchanged.

## CRT-018 authored locally, November 11, 2026

[CRT-018](lessons/CRT-018_Combining_People_Access_Selection_and_Campaign_Filters.md) is complete at revision 1.0. [Its record](author/revisions/CRT-018_Revision_Record.md) maps combined COV-12 reasoning to ten scoped primary references and the full saved beginner author reading. It distinguishes expected scope from actual generated evidence, query grouping from UI alternatives, criterion units and query/filter-content routes. Conflicting restrictions are not used to invent precedence. A Support profile transfer changes the reviewable object and grant origin. Existing 122 meanings are connected without new glossary entries. Eighteen topics are authored, 32 unwritten and CRT-019 next. Eight questions stay open; local CRT-014 through CRT-018 preserve publication and pending participant/tenant status.

## CRT-019 authored locally, November 11, 2026

[CRT-019](lessons/CRT-019_Understanding_the_Data_Captured_When_a_Review_Is_Generated.md) is complete at revision 1.0. [CRT-019 record](author/revisions/CRT-019_Revision_Record.md) maps primary COV-13, ten scoped references and full saved beginner author reading. Source observation, review generation and report production have distinct meanings; current account/identity data is compared with inspected existing work. Dedicated-route snapshot guidance is not generalized into an immutable all-engine field schema. Supported reassignment and decision history demonstrate mutable workflow separately. The independent transfer distinguishes later access from earlier uncollected access. Existing 122 meanings and eight open questions remain. Nineteen authored, 31 unwritten, CRT-020 next. CRT-014 through CRT-019 remain local and the thirteen-entry publication is unchanged; participant and tenant assessment remain pending.

## CRT-020 authored locally, November 11, 2026

[CRT-020](lessons/CRT-020_Understanding_Templates_Schedules_Previews_and_Running_Campaigns.md) is complete at revision 1.0. [Its record](author/revisions/CRT-020_Revision_Record.md) maps primary COV-14, eleven scoped references and complete saved beginner author reading. Reusable instructions, future timing, completed preview and separate activation have distinct actions/evidence. Experimental activation acceptance is not treated as finished activation; early generation does not cancel the documented scheduled occurrence. A Warehouse transfer changes fixed selection and distinguishes running early work from a later preview. Twenty authored, 30 unwritten, CRT-021 next. Existing 122 meanings and eight open questions remain. Local CRT-014 through CRT-020 preserve the thirteen-entry reader and published snapshot; no participant or tenant pass is inferred.

## CRT-021 authored locally, November 11, 2026

[CRT-021](lessons/CRT-021_Checking_a_Generated_Campaign_Before_It_Reaches_Reviewers.md) is complete at revision 1.0. [Its record](author/revisions/CRT-021_Revision_Record.md) maps primary COV-15 and supporting COV-03 to eleven scoped references and full saved beginner author reading. Four expected versus four actual holdings expose distinct missing-input and wrong-scope findings, followed by corrected and reinspected work. Reviewer knowledge/authority, representative cases, deadline/comments/undecided settings, global email redirection/test limits and explicit exceptions lead to verified authorized start. An independent Warehouse case changes the actual account/person, sampled evidence and delivery configuration. Twenty-one authored, 29 unwritten, CRT-022 next. Existing 122 meanings and eight open questions remain; local CRT-014 through CRT-021 preserve the thirteen-entry publication. No participant, graphical or tenant result is inferred.

## CRT-022 authored and publication prepared, November 11, 2026

[CRT-022](lessons/CRT-022_How_ISC_Chooses_the_Reviewer.md) is complete at revision 1.0. [Its record](author/revisions/CRT-022_Revision_Record.md) maps primary COV-16 and COV-03 to thirteen scoped references, full saved beginner author reading and the independent Warehouse requirement/choice mismatch. Seven documented reviewer choices depend on type; actual input/assignment, group members, owners/permissions and historical decision actor remain distinct. Existing 122 meanings and eight questions remain. Twenty-two authored, 28 unwritten; CRT-023 next. The [current publication](author/PUBLICATION_2026-11-11_TWENTY_TWO_LESSONS.md) records all twenty-two learners in five reader modules, content 80723fe, successful deployment and complete live verification. No tenant or observed learner assessment is inferred.

## CRT-023 authored locally, November 11, 2026

[CRT-023](lessons/CRT-023_Handling_Missing_Managers_Owners_and_Fallback_Reviewers.md) is complete at revision 1.0. [Its record](author/revisions/CRT-023_Revision_Record.md) maps COV-16 to ten scoped references and full saved beginner author reading. Missing relationship, unmatched reference retaining an existing manager, deleted reviewer, empty group and inactive listed members require different checks. Route-specific manager exclusion/creator fallback, Account Owner source fallback and source-owner prerequisites are distinguished. New Fallback meaning raises the register to 123; new OQ-09 records unestablished terminal ownership fallback rather than inventing a recipient. Nine questions remain open. Twenty-three authored, 27 unwritten, CRT-024 next. The twenty-two-entry publication/reader remains unchanged; no push, tenant or participant result is claimed.

## CRT-024 authored locally, November 11, 2026

[CRT-024](lessons/CRT-024_Preventing_Self_Certification_and_Checking_Own_Access_Routing.md) is complete at revision 1.0. [Its record](author/revisions/CRT-024_Revision_Record.md) maps primary COV-17 to nine scoped references and full saved beginner author reading. Automatic own-access separation/routing, manual any-own-access block, mixed certification coverage, as-created work redirection and verified multi-member group exception have distinct conditions/results. The Warehouse transfer preserves both intended holdings and requires actual independent responsibility/actor evidence. Existing 123 meanings and nine questions remain. Twenty-four authored, 26 unwritten, CRT-025 next. Local CRT-023/024 preserve the twenty-two-entry publication; no tenant, participant or push result is claimed.

## CRT-025 authored locally, November 11, 2026

[CRT-025](lessons/CRT-025_Reassigning_Review_Work_and_Verifying_the_Result.md) is complete at revision 1.0. [Its record](author/revisions/CRT-025_Revision_Record.md) maps primary COV-18 to ten scoped references and full saved beginner author reading. Main Reporting handover changes only intended responsibility while Support remains; actor/state/own-access, reason, task/result, decision history and recipient visibility are verified separately. Direct Experimental next-generation APIs distinguish whole certifications from identity-campaign subjects/items and action-specific actors. The three-holding Warehouse transfer makes both whole-review and subject-level choices too broad for one item. New Asynchronous processing meaning raises the register to 124; nine questions remain open. Twenty-five authored, 25 unwritten, CRT-026 next. Local CRT-023 through CRT-025 preserve the twenty-two-entry reader and publication. No push, tenant or participant result is claimed.

## CRT-026 authored locally, November 11, 2026

[CRT-026](lessons/CRT-026_Keeping_Reviews_Moving_During_Absence_and_Departure.md) is complete at revision 1.0. [Its record](author/revisions/CRT-026_Revision_Record.md) maps primary COV-18 continuity to nine scoped references and full saved beginner author reading. The before/during/after example separates an existing-work handover from automatic new-work redirection; period expiry does not return earlier work. Replacement, deletion, site disable, no end date, permanent departure, group/chain/self-review boundaries and first-recipient history versus current assignment are connected. The Warehouse transfer changes the backup and then deletes/disables the instruction without inventing a retroactive transfer. Work reassignment raises the register to 125 meanings; nine questions remain open. Twenty-six authored, 24 unwritten; CRT-027 next. Local CRT-023 through CRT-026 preserve the twenty-two-entry publication. No push, tenant or participant result is claimed.

## CRT-027 authored locally, November 11, 2026

[CRT-027](lessons/CRT-027_Inspecting_Review_Context_Before_Deciding.md) is complete at revision 1.0. [Its record](author/revisions/CRT-027_Revision_Record.md) maps COV-20 decision inputs and COV-08 context to twelve scoped references and full saved beginner author reading. Person/source/account/item, verified permission/data/scope and authorized current task establish the ordinary justification before optional signals. Origin, timestamps/conflicts, eight flag meanings, peer recommendation reasons and source activity keep their distinct scope. The annual-recovery profile transfer separates uncommon/missing-use signals from verified need, then adds an unapproved package capability. Nine new registered meanings bring the total to 134; nine product questions remain open. Twenty-seven authored, 23 unwritten; CRT-028 next. Local CRT-023 through CRT-027 preserve the twenty-two-entry publication. No push, tenant or participant result is claimed.

## CRT-028 authored locally, November 11, 2026

[CRT-028](lessons/CRT-028_Understanding_Approve_Revoke_and_Acknowledge.md) is complete at revision 1.0. [Its record](author/revisions/CRT-028_Revision_Record.md) maps primary COV-20 to thirteen scoped references and full saved beginner author reading. Approve accepts continued reviewed access, Revoke records removal and Acknowledge examines automatically controlled role access without overriding criteria. Actual package/origin/type and role-composition boundaries determine scope; saved/finalized decisions and verified target results remain distinct. Supplier transfer rejects a component-only/account-delete interpretation of profile Revoke and a removal interpretation of automatic-role Acknowledge. Revocation date raises meanings to 135; nine product questions remain open, with a bounded direct finalization contract recorded. Twenty-eight authored, 22 unwritten; CRT-029 next. Local CRT-023 through CRT-028 preserve twenty-two published learners. No push, tenant or participant result is claimed.

## CRT-029 authored locally, November 11, 2026

[CRT-029](lessons/CRT-029_Recording_Clear_Reasons_and_Checking_Bulk_Decisions.md) is complete at revision 1.0. [Its record](author/revisions/CRT-029_Revision_Record.md) maps primary COV-20 to eleven scoped references and full saved beginner author reading. Approved decision criteria and current facts support item-specific explanations; mandatory text does not validate reasoning. Four selected items split into justified approvals and distinct removals, with actual selection/result/comment checks. Report Decision Comments, status Comments, current Reviewer and Decision Maker answer different questions. The Invoice transfer rejects a read-only comment for a payment-release package and attribution of an earlier choice to a replacement reviewer. Three new meanings bring the total to 138; nine questions remain open. Twenty-nine authored, 21 unwritten; CRT-030 next with OQ-01 scope investigation required. Local CRT-023 through CRT-029 preserve twenty-two published learners; no push, tenant or participant result is claimed.

## CRT-030 authored locally, November 11, 2026

[CRT-030](lessons/CRT-030_Distinguishing_Saved_Decisions_and_Review_Sign_Off.md) is complete at revision 1.0. [Its record](author/revisions/CRT-030_Revision_Record.md) maps COV-21 to thirteen scoped sources and full saved beginner author reading. Two saved choices plus one undecided become three choices while R-30 remains unsigned; a separately inspected sign-off establishes finalization, not source removal. Normal next-generation read-only decisions, pre-sign-off changes, signer/time, reauthentication and campaign/account distinction are locally explained. OQ-01 remains unresolved after fresh primary/direct-action investigation; new OQ-10 tracks editing ambiguity without an invented reopen operation. Warehouse transfer separates decided/unsigned work from signed work and declines an unsupported administrator-completion removal prediction. Reauthentication brings meanings to 139; ten questions remain open. Thirty authored, 20 unwritten; CRT-031 next. Local CRT-023 through CRT-030 preserve twenty-two published learners; no push, tenant or participant result.

## CRT-031 authored and publication prepared, November 11, 2026

[CRT-031](lessons/CRT-031_Resolving_Uncertainty_Before_an_Access_Decision.md) is complete at revision 1.0. [Its record](author/revisions/CRT-031_Revision_Record.md) maps COV-08/20 to eleven scoped sources and full saved beginner reading. Specific capability/need/data/action gaps lead to relevant consultation, justified decision or verified permitted independent handover; insight signals do not fill missing authorization. The Support transfer distinguishes unknown from confirmed absent need and rejects a manual own-access handover. Consultation brings meanings to 140; ten questions remain open. Thirty-one authored, 19 unwritten; CRT-032 next. User explicitly authorizes pushing all complete work; [current publication record](author/PUBLICATION_2026-11-11_THIRTY_ONE_LESSONS.md) tracks the expanded six-module manifest and pending deployment. Earlier learners, historical evidence and reader implementation remain preserved. No tenant or participant result is claimed.

## Thirty-one-lesson publication observed, November 11, 2026

[Publication evidence](author/PUBLICATION_2026-11-11_THIRTY_ONE_LESSONS.md): content 670f0c8cdb7535057ffe285034d33a6762156e98, successful Pages run 43159502534 and full live verification for 31 lessons, 3743 content units, 31 diagrams/assets, 38 tables, 1052 internal link visits, CSS and representative author exclusions. All complete work is published in six modules. Reader implementation and earlier content/evidence remain unchanged. Thirty-one authored, 19 unwritten; CRT-032 next. No tenant, observed learner assessment or graphical review is inferred.
## CRT-032 authored locally, November 11, 2026

[CRT-032](lessons/CRT-032_Following_a_Revoke_Decision_into_Required_Removal_Work.md) and [its record](author/revisions/CRT-032_Revision_Record.md) develop COV-22: exact removal requirement, normal reviewer finalization, conditional future date and due work, supported automatic/manual delivery and account outcome. The Procurement example removes approval while retaining viewing; an independent Invoice handover separates before-due access, after-due investigation and a closed manual task without target confirmation. Detailed delivery, overlap, recovery and full verification remain CRT-033–037. One new working meaning brings the register to 141; ten questions remain open. Thirty-two authored, 18 unwritten; CRT-033 next. CRT-032 is local only; earlier publication/reader and evidence remain unchanged. No tenant or observed learner assessment is claimed.

## CRT-033 authored locally, November 12, 2026

[CRT-033](lessons/CRT-033_How_Automated_Removal_Reaches_the_Application.md) and [its record](author/revisions/CRT-033_Revision_Record.md) develop COV-23 automatic delivery. Exact source/environment/account/value, connector operation, enabled write, authentication/authorization, response and activity/account evidence are connected in a bounded Web Services SaaS example. Conditional VA architecture and sent/finished/retry field meanings are explained without a universal private sequence. Independent Reporting transfer changes the permission result and then the target account. Nine working meanings bring the total to 150; all ten questions remain open. Thirty-three authored, 17 unwritten; CRT-034 next. CRT-032/033 local only; no push or tenant/participant/graphical assessment.

## CRT-034 authored locally, November 12, 2026

[CRT-034](lessons/CRT-034_Removing_Access_Through_Manual_Fulfillment.md) and [its record](author/revisions/CRT-034_Revision_Record.md) develop COV-23 manual delivery. Actual assignment and target authority, human permission removal, truthful later file/import and task/report completion are distinct. The file-based early-completion note stays scoped; handover transfers removal work rather than review responsibility. Finance transfer tests partial work hidden by closure, inaccurate file data and later stale data. Six new meanings bring the total to 156; OQ-05 was freshly investigated but remains unresolved, along with nine other questions. Thirty-four authored, 16 unwritten; CRT-035 next. No push, tenant, participant or graphical result.

## CRT-035 authored locally, November 12, 2026

[CRT-035](lessons/CRT-035_Overlapping_Access_and_Assignment_Origins.md) and [its record](author/revisions/CRT-035_Revision_Record.md) develop COV-24's same-account grant paths, assignment versus permission, role-over-profile retention, automatic membership/lifecycle control and model versus account outcome. Main Documents case retains role-required reading while removing separately requested export; Support transfer supplies a continuing lifecycle requirement and then stale observation. OQ-07 remains unresolved after fresh conflicting-source investigation; no universal independent-profile outcome is promised. Role content propagation is checked as CAP-17. Three new meanings total 159. Thirty-five authored, 15 unwritten; CRT-036 next. No push, tenant, participant or graphical result.

## CRT-036 authored locally, November 12, 2026

[CRT-036](lessons/CRT-036_Investigating_Pending_Failed_and_Partial_Removal.md) and [its record](author/revisions/CRT-036_Revision_Record.md) develop COV-25 pending/failed/partial investigation. Exact work/account/error/current state separates partial success, ongoing work and uncertain response. Conditional provisioning-service retry guidance and Web Services SaaS per-request handling have distinct scopes. Ledger authorization correction preserves successful export removal and justified reading; Invoice timeout transfer avoids invented success/failure or blind repeat. Five new meanings total 164; ten questions remain open. Thirty-six authored, 14 unwritten; CRT-037 next. No push, tenant, participant or graphical result.

## CRT-037 authored locally, November 12, 2026

[CRT-037](lessons/CRT-037_Verifying_That_Required_Access_Was_Removed.md) and [its record](author/revisions/CRT-037_Revision_Record.md) develop COV-26 exact required outcome, finalized decision, actual work/target, later collected data and effective-ability boundaries. Supported automated source confirmation is valid within its scope; no manual-login requirement for every account. Records timeline separates observation and report times; Timekeeping transfer exposes old file data and a supplied application-native grant outside collected groups. Session behavior is scoped rather than a universal entitlement-removal logout claim. Two meanings total 166; ten questions stay open. Thirty-seven authored, 13 unwritten; CRT-038 next. No push, tenant, participant or graphical result.

## CRT-038 authored locally, November 12, 2026

[CRT-038](lessons/CRT-038_Using_Reminders_and_Monitoring_Campaign_Progress.md) and [its record](author/revisions/CRT-038_Revision_Record.md) develop COV-27's progress/reminder foundations. Three unequal reviews separate nine item choices, one signed certification and pending removal; follow-up addresses the actual missing result. Current notification controls and expected event/timing distinguish missing work from missing email. Four-day handover transfer identifies current reviewer, expected reassignment message and global redirection, then changes remaining work to removal. Four new meanings total 170; ten questions stay open. Thirty-eight authored, 12 unwritten; CRT-039 next. No push, tenant, participant or graphical result.

## CRT-039 authored locally, November 12, 2026

[CRT-039](lessons/CRT-039_Handling_Overdue_Undecided_and_Unsigned_Reviews.md) and [its record](author/revisions/CRT-039_Revision_Record.md) develop COV-27's deadline and unfinished-work distinctions. Three review states separate missed time, saved/absent choices, final confirmation and pending due removal. Postdeadline normal finalization is conditional on actual permitted state; configured administrative completion has separate authority, affected set and evidence. A no-saved-choice campaign explains maintain/changed revoke outcomes without resolving conflicting unsigned-saved treatment. Independent Dispatch case tests an unsupported preserved-reading guarantee. One new meaning totals 171; all ten questions remain open. Thirty-nine authored, 11 unwritten; CRT-040 next. No push, tenant, participant or graphical result.

## CRT-040 authored and publication prepared, November 12, 2026

[CRT-040](lessons/CRT-040_Understanding_Campaign_Completion_and_Closure_Evidence.md) and [its record](author/revisions/CRT-040_Revision_Record.md) develop COV-27 closure meaning through normal engine-scoped completion, administrative/request boundaries, actual target result and accepted follow-up. Archive task closure contradicts current export ability; later truthful source/collected evidence establishes the scoped result. Whole-population and full required-result sets prevent overclaiming from one completed sample. Independent untouched-item Billing completion distinguishes policy approval from informed judgment. One meaning totals 172; all ten questions stay open. Forty authored, 10 unwritten; CRT-041 next. [Authorized publication](author/PUBLICATION_2026-11-12_FORTY_LESSONS.md) expands the manifest to forty complete learners in eight modules; successful deployment/live results still need observation.

## Forty-lesson publication observed, November 12, 2026

Content 858267c75695e77d89ff232fca40da0026869c10 is pushed. Pages run 43202690075 succeeded, and full live verification passed for forty learners, 4582 content units, forty diagrams/assets, forty-five tables, 1718 internal link visits, CSS and representative author/control exclusions. The reader, earlier learners and historical records remain unchanged. Forty authored/published, ten core topics unwritten; CRT-041 next. This is served-content/navigation evidence, not graphical layout, participant understanding or tenant behavior.

## CRT-041 authored locally, November 12, 2026

[CRT-041](lessons/CRT-041_Correcting_Regenerating_and_Retiring_a_Campaign.md) and [its record](author/revisions/CRT-041_Revision_Record.md) develop COV-28 correction/replacement/retirement reasoning. P-810's confirmed selection defect is repaired in the proper definition and a distinct P-811 is validated; active deadline/unsigned assignment corrections stay scoped. Exact SDK edit matrix, signed limits, schedule independence and deleted evidence are explained. Payments transfer preserves a valid removal while investigating unsupported cancel/restore claims. Three meanings total 175; OQ-11 brings questions to eleven. Forty-one authored, nine unwritten; CRT-042 next. Prior forty-lesson publication remains unchanged; no push, tenant, participant or graphical result.

## CRT-042 authored and publication prepared, November 12, 2026

[CRT-042](lessons/CRT-042_Understanding_Campaign_Counts_Progress_and_Statuses.md) and [its record](author/revisions/CRT-042_Revision_Record.md) develop COV-29 units, condition, denominator and observation scope. The A/B/C fixture counts decisions/subjects/signatures separately; native Completed can mean all choices while DateSigned remains absent. X/Y transfer exposes filtered100%, misleading equal-review average and correct1/10 item share. Status belongs to campaign/review/item/work, with user/page/time and zero-denominator boundaries. Two meanings total177; eleven questions stay open. Forty-two authored, eight unwritten; CRT-043 next. [Publication preparation](author/PUBLICATION_2026-11-12_FORTY_TWO_LESSONS.md) adds two complete learners in nine modules; successful deployment and full live checks still need observation.
