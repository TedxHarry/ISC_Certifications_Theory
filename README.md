# ISC Certifications Theory

A beginner-focused theory course on SailPoint Identity Security Cloud access reviews and certification campaigns.

This workspace contains the approved course direction and the authoring foundation. Learner lessons will be written one complete file at a time. CRT-001 is now written and author-reviewed locally. The separate [GitHub repository](https://github.com/TedxHarry/ISC_Certifications_Theory) is created. Initial Pages deployment is being verified.

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
Learner lessons written: 1, revision 1.0, saved locally. Actual learner validation is pending.
Current: [CRT-001, Why review access that somebody already approved?](lessons/CRT-001_Why_Review_Previously_Approved_Access.md).
Next: CRT-002, A campaign, a certification and a review item: what is being assigned?

Module and lesson counts are flexible. Preserve complete coverage and clear explanation as the structure develops.

## Publication

The user authorized repository creation and GitHub Pages publication on October 30, 2026. This folder is the separate ISC_Certifications_Theory repository, with its own origin remote. Pages deployment and live verification are recorded in [the initial publication record](author/PUBLICATION_2026-10-30_INITIAL.md).

Run npm ci, npm test and node author/verify-site.mjs for local checks. After deployment, node author/verify-site.mjs --live checks published lesson text, diagrams, tables, links, assets and author-content exclusions. Only lessons listed in _data/course.yml appear in the reader.

The existing ISC_Theory_TedxHarry course is a separate project. Its files and publishing destination are not used for this course.
