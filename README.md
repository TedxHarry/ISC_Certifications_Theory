# ISC Certifications Theory

A beginner-focused theory course on SailPoint Identity Security Cloud access reviews and certification campaigns.

This workspace contains the approved course direction and the authoring foundation. Learner lessons will be written one complete file at a time. CRT-001 through CRT-005 are written and author-reviewed. CRT-001 through CRT-004 revision 1.0 are published and live-verified; CRT-005 revision 1.0 remains local. The separate [GitHub repository](https://github.com/TedxHarry/ISC_Certifications_Theory) is created. The [reading site](https://tedxharry.github.io/ISC_Certifications_Theory/) is live with CRT-001 through CRT-004 revision 1.0.

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
Learner lessons written and author-reviewed: 5, CRT-001 through CRT-005 revision 1.0. Published: CRT-001 through CRT-004. Actual learner validation is pending.
Current local learner: [CRT-005, How does application access become information ISC can review?](lessons/CRT-005_From_Application_Access_to_Reviewable_Information.md).
Next: CRT-006, Are we reviewing an entitlement, an access profile or a role?
Forty-five current candidate topics remain unwritten; the inventory can change with coverage needs.

Module and lesson counts are flexible. Preserve complete coverage and clear explanation as the structure develops.

## Publication

The user authorized repository creation and GitHub Pages publication on October 30, 2026. This folder is the separate ISC_Certifications_Theory repository, with its own origin remote. Pages deployment and live verification are recorded in [the initial publication record](author/PUBLICATION_2026-10-30_INITIAL.md), [the CRT-002/003 publication record](author/PUBLICATION_2026-10-30_CRT-002_CRT-003.md) and [the CRT-004 publication record](author/PUBLICATION_2026-10-30_CRT-004.md).

Run npm ci, npm test and node author/verify-site.mjs for local checks. After deployment, node author/verify-site.mjs --live checks published lesson text, diagrams, tables, links, assets and author-content exclusions. Only lessons listed in _data/course.yml appear in the reader. The manifest includes CRT-001 through CRT-004. CRT-005 is complete locally and is not part of this publication. The live check compares local assets with deployed assets, so use it after the intended publication snapshot is deployed, not to test unpublished continuation assets.

The existing ISC_Theory_TedxHarry course is a separate project. Its files and publishing destination are not used for this course.
