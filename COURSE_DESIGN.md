# SailPoint ISC Certifications: Understanding Access Reviews from Scope to Verified Outcome

Course design 2.1. October 29, 2026.
Subject confirmed: ISC access review and certification campaigns.
Status: course direction accepted for local authoring setup; foundation saved. CRT-001 revision 1.0 is authored and reviewed locally; CRT-001 revision 1.0 is published and live-verified.

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
| CRT-014 | Do we need to review everyone selected, or only particular access they hold? | Identity selection versus access refinement; avoiding unintended all-access reviews. |
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

The documentation reviewed during this design contains a material inconsistency about unsigned decisions at administrator completion. Resolve and qualify that behavior for the engine in use before drafting CRT-030/039/040. Do not silently choose one passage or imply a tested tenant result.

Each authored lesson needs a coverage record, primary-source check, complete saved-file beginner read-through, example/diagram consistency check and reasoned assessment. Actual uncoached beginner validation is recorded separately and remains pending until it occurs. A simulated author review cannot claim that a learner understood.

## Delivery plan and next step

The user authorized establishing the local authoring foundation on October 29, 2026. The folder ISC_Certifications_Theory now contains the teaching specification, progress register, author workflow and first brief, coverage/terminology records, capability/update register and routine task map. The first learner, CRT-001 revision 1.0, is saved locally; the separate GitHub repository and Pages site are live with verified CRT-001 revision 1.0.

Use [README](README.md) to navigate the package and [COURSE_REGISTER](COURSE_REGISTER.md) to resume. Write one complete learner lesson at a time with its necessary reference aids, author record and saved-file checks.

CRT-001 has been authored from its prepared brief and has a complete local author record. Continue with CRT-002 after preparing its brief and source checks through [the authoring guide](author/AUTHORING_GUIDE.md). Read the complete saved lesson as an unfamiliar beginner and revise from actual feedback when available. A hands-on course is a separate later project.

On October 30, 2026 the user authorized creating ISC_Certifications_Theory, pushing the saved work and publishing Pages before continuing locally. The new reader reuses the established course layout and lists only completed lessons included in the publication. See [publication evidence](author/PUBLICATION_2026-10-30_INITIAL.md).
