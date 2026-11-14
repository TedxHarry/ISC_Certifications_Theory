# Local publication readiness: common work and practice revisions

November13,2026. Complete local readiness check; no commit, push or deployment performed.

## Scope and release contents

The user continued after the practice-case review. Check the accumulated local package without adding another learner or changing the separate general ISC course.

| Item | Prepared local change | Published state remains |
|---|---|---|
| CRT-060 | Complete periodic-manager walkthrough, diagram and author evidence | Not included in the59-topic publication |
| CRT-061 | Complete application/source-owner walkthrough, diagram and author evidence | Not included in the59-topic publication |
| CRT-018/049/050 | Revision1.1 final practice questions and closed worked answers | Revision1.0 |
| Homepage task finder | Nineteen work requests leading to eighteen existing lessons, grouped in four closed disclosures | Earlier homepage |
| Publication verifier | Native answer-wrapper handling and a missing-answer/label regression check | Earlier verifier |

Local course:61 lessons in30 main/28 reference/3 practice, fifteen subject groups and nine main-route groups. Published course remains59 in30/26/3. No062 lesson is queued. No coverage, terminology or capability expansion is required for this package.

## A readiness defect found and repaired

The publication verifier built expected learner text from every nonempty Markdown source line. Native details/summary markup was therefore treated as required visible text. A valid rendered answer did not contain its source tags as text, so the check would incorrectly fail after publication.

Added a regression using the real verifier against a small isolated HTTP fixture. Its first run failed with the expected missing details-tag message. The repair removes only supported details/summary tags from expected text and ignores empty normalized units. It keeps the summary label and all answer prose in the required checks.

The repeat test passes a complete closed answer and deliberately rejects a missing native wrapper, an answer that starts open, a missing answer sentence and a missing Compare your reasoning label. The missing-wrapper variant was observed being accepted before adding the structural guard; the regression then failed as intended. The guard now checks the expected number of native answers, their closed state, first summary control and exact label. The fixture and child process are temporary and confined to the excluded tests directory. No published or learner file is changed by the check.

The corrected current content count is6,819 normalized nonempty text units. The earlier6,879 count included50 empty normalized entries and ten wrapper-only entries. All teaching text remains: this count change is a verifier correction, not removal of60 pieces of content. Earlier dated records retain the count their then-current verifier produced.

## Fresh executed checks

All18 automated tests pass, including the new verifier regression and the existing navigation, term-help and common-work checks. Direct local content verification passes61 lessons/6,819 units/61 diagrams/63 learner tables/61 editable assets.

Rendered the actual saved homepage and all61 lessons through the current Liquid layouts, includes, manifest, task data and term dictionary, with Marked used for Markdown. Served those62 pages and63 assets through a temporary local HTTP server. The repaired verifier, with its requests redirected only to that local server, checks all6,819 text units, five correct native/closed answer blocks, exact diagrams/tables, current-lesson markers, homepage destinations, editable assets, author-page404s and3,898 internal link visits. It passes.

The tool's live flag here means checking HTTP responses; it does not make this a public-site observation. No request from that full-course pass was allowed outside the local preview. The helper and server are removed/stopped afterward.

The main route, separate reference/practice destinations and within-route Previous/Next boundaries are checked for every lesson by the existing tests. No permanent ID, filename or reading route changes in this readiness step.

The [task-finder record](COMMON_CERTIFICATION_WORK_READING_GUIDE.md) and [practice record](PRACTICE_CASE_REVIEW_2026-11-13.md) retain the actual local desktop/touch/keyboard/enlarged-text/disabled-JavaScript observations. Their134 reader-source files remain byte-identical during this readiness step. Those prior observations are not claimed as newly repeated physical-device or participant tests.

## Publication destination and package boundaries

Read-only GitHub Pages settings report legacy publishing from main at repository root, status built, for the separate ISC_Certifications_Theory destination. Local HEAD and remote main both remain08a97ff3aa7f568a863e77ab328c3c059c778ddd. No remote mutation, deployment trigger, staging or commit occurred.

The configuration explicitly excludes author records, plans, course-control Markdown, tests, package files and dependencies. The temporary fixture belongs under the excluded tests directory and cleans itself up. Guide targets resolve through permanent IDs to actual authored lessons. No learner placeholder or author-record link is added to the public lesson prose.

Reader-source fingerprint: ea8f1e57adbcaa4ca4d596e915910d19240bc72a861b579b9ae142323a487e35.

This SHA-256 fingerprints the sorted134 source paths and their individual byte hashes: configuration, homepage/404, layouts/includes, course/task/term data, learner Markdown and reader/diagram assets. It is a local source-package identifier, not a compiled Jekyll or deployed-build hash.

## Build and evidence limits

No Ruby, Bundler or Jekyll command is available locally. Docker is installed but its Linux engine is not running; the only listed WSL distribution is docker-desktop. No service was started and no runtime/dependency was installed to work around this. The saved-template preview is not an actual Jekyll/Kramdown build.

During a requested publication, observe the actual Pages build and verify served content and behavior, including all five closed answer blocks and the task finder. Native wrapper parsing is documented in the existing practice record, but production rendering remains a deployment check.

32 concept rows/24 task families/214 author meanings/109 helper meanings/17 capabilities/11 unresolved product questions remain. Source-author checks do not resolve those questions or establish tenant operation, every release update, screen-reader behavior or independent beginner competence. Actual learner validation remains pending.

## Final package checks and result

Final structural and preservation reconciliation passes281 source files,196 Markdown files,1,134 relative links and259 table groups/2,917 rows. Fences, column widths, current inventory, native-answer wrappers, destination files and source whitespace reconcile. The279-file start-of-readiness snapshot preserves274 files exactly; five author/current-state files change and the readiness record plus regression test are added.

All61 learners, all61 teaching assets, the complete134-file reader-source package, manifest/route order, term data, previous tests and historical evidence remain exact. The course stays61/30/28/3 locally and59/30/26/3 published. The regression checks clean up their isolated fixtures and the temporary full-course preview/structural helpers are removed. git diff --check passes and no staged change is introduced.

The local package is prepared for a requested publication. No new learner is scheduled and no ordinary continuation publishes. Independent learner feedback can guide a later focused revision; it is not an invented blocker or an automatic reason to add more lessons.
