# ISC Certifications Theory

A beginner-focused theory course on SailPoint Identity Security Cloud access reviews and certification campaigns.

This workspace contains the approved course direction and the authoring foundation. Learner lessons are written one complete file at a time. CRT-001 through CRT-008 are written and author-reviewed. CRT-001 through CRT-006 revision 1.0 remain the published, historically live-verified snapshot. CRT-001/004 revision 1.1 and CRT-007/008 revision 1.0 are local. The separate [GitHub repository](https://github.com/TedxHarry/ISC_Certifications_Theory) and [reading site](https://tedxharry.github.io/ISC_Certifications_Theory/) are live.

The clearer explanation applies to every existing and future lesson. New-topic writing is paused while the earlier lessons are revised one at a time. [CRT-001 revision 1.1](lessons/CRT-001_Why_Review_Previously_Approved_Access.md) is the latest local rewrite; [its record](author/revisions/CRT-001_Revision_1_1_Record.md) preserves the original coverage and separates author checks from learner assessment. CRT-004's accepted revision and current-style CRT-008 are preserved. CRT-002 is next in the [revision queue](COURSE_REGISTER.md).

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
Learner lessons written and author-reviewed: 8, CRT-001/004 locally at 1.1 and the other six at 1.0. Published: CRT-001 through CRT-006 revision 1.0. The user's feedback on CRT-004 1.1 is positive; independent learner assessment remains pending.
Current local learner: [CRT-008, One person has two accounts. Which account's access is under review?](lessons/CRT-008_One_Person_Two_Accounts_and_the_Correct_Review_Target.md).
Current revision: [CRT-001](lessons/CRT-001_Why_Review_Previously_Approved_Access.md), revision 1.1, local.
Next task: rewrite CRT-002, then CRT-003/005/006/007. Five revisions remain. CRT-009 is the next unwritten topic and is parked until the revision pass is complete.
Forty-two current candidate topics remain unwritten; the inventory can change with coverage needs.

Module and lesson counts are flexible. Preserve complete coverage and clear explanation as the structure develops.

## Publication

The user authorized repository creation and GitHub Pages publication on October 30, 2026. This folder is the separate ISC_Certifications_Theory repository, with its own origin remote. Pages deployment and live verification are recorded in [the initial publication record](author/PUBLICATION_2026-10-30_INITIAL.md), [the CRT-002/003 publication record](author/PUBLICATION_2026-10-30_CRT-002_CRT-003.md), [the CRT-004 publication record](author/PUBLICATION_2026-10-30_CRT-004.md), [the CRT-005 publication record](author/PUBLICATION_2026-10-31_CRT-005.md) and [the CRT-006 publication record](author/PUBLICATION_2026-10-31_CRT-006.md).

Run npm ci, npm test and node author/verify-site.mjs for local checks. After deployment, node author/verify-site.mjs --live checks published lesson text, diagrams, tables, links, assets and author-content exclusions. Only lessons listed in _data/course.yml appear in the reader. The manifest includes CRT-001 through CRT-006. CRT-007/008 are complete locally and are not part of this publication; local CRT-001/004 revision 1.1 also differs from their published 1.0. The live check compares local content and assets with deployed files, so use it after the intended publication snapshot is deployed, not to test unpublished changes.

The existing ISC_Theory_TedxHarry course is a separate project. Its files and publishing destination are not used for this course.
