# ISC Certifications Theory

A beginner-focused theory course on SailPoint Identity Security Cloud access reviews and certification campaigns.

This workspace contains the approved course direction and the authoring foundation. Learner lessons will be written one complete file at a time. CRT-001, CRT-002 and CRT-003 are written and author-reviewed. CRT-002 and CRT-003 revision 1.0 are local and unpublished. The separate [GitHub repository](https://github.com/TedxHarry/ISC_Certifications_Theory) is created. The [reading site](https://tedxharry.github.io/ISC_Certifications_Theory/) is live with CRT-001 revision 1.0.

## Start here

- [Course design and provisional contents](COURSE_DESIGN.md): purpose, learning outcomes, 50 candidate topics and job-dependent depth.
- [Teaching specification](TEACHING_SPECIFICATION.md): required explanation, tone, independence and quality standards.
- [Course register](COURSE_REGISTER.md): what is actually written, reviewed and next.
- [Operational task coverage](OPERATIONAL_TASK_COVERAGE.md): 24 routine task families mapped to planned topics.
- [Authoring guide and first lesson brief](author/AUTHORING_GUIDE.md): how to produce and review the next complete lesson.
- [Coverage register](author/COVERAGE_REGISTER.md): concept ownership, flows, evidence and overlap checks.
- [Terminology register](author/TERMINOLOGY_REGISTER.md): consistent meanings and primary teaching locations.
- [Capability and update register](author/CAPABILITY_AND_UPDATE_REGISTER.md): engine/availability checks and unresolved product questions.
- [Official source map](AUTHOR_SOURCE_MAP.md): scoping references and their limits.

## Working structure

- lessons/: completed learner lesson Markdown files only; no unwritten-lesson stubs.
- assets/: editable diagrams and reference aids produced when needed.
- author/revisions/: per-lesson coverage, source, example, review and verification records.

The empty-directory markers are repository housekeeping, not learner content.

## Current position

Authoring foundation established October 29, 2026.
Candidate core topics: 50, grouped provisionally into 10 modules.
Specialist depth routes: 5, required where the learner's role needs them.
Learner lessons written and author-reviewed: 3, CRT-001, CRT-002 and CRT-003 revision 1.0. Published: CRT-001 only. Actual learner validation is pending.
Current local continuation: [CRT-003, Follow one review from access data to a verified outcome](lessons/CRT-003_From_Access_Data_to_a_Verified_Outcome.md).
Next: CRT-004, How is a certification different from an access request or lifecycle rule?
Forty-seven current candidate topics remain unwritten; the inventory can change with coverage needs.

Module and lesson counts are flexible. Preserve complete coverage and clear explanation as the structure develops.

## Publication

The user authorized repository creation and GitHub Pages publication on October 30, 2026. This folder is the separate ISC_Certifications_Theory repository, with its own origin remote. Pages deployment and live verification are recorded in [the initial publication record](author/PUBLICATION_2026-10-30_INITIAL.md).

Run npm ci, npm test and node author/verify-site.mjs for local checks. After deployment, node author/verify-site.mjs --live checks published lesson text, diagrams, tables, links, assets and author-content exclusions. Only lessons listed in _data/course.yml appear in the reader. The manifest remains CRT-001 only; CRT-002 and CRT-003 have not been pushed. The live check compares local assets with deployed assets, so use it after the intended publication snapshot is deployed, not to test unpublished continuation assets.

The existing ISC_Theory_TedxHarry course is a separate project. Its files and publishing destination are not used for this course.
