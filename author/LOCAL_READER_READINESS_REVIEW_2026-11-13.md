# Local reader readiness review

November 13, 2026. Local changes only. This record supplements the [combined specialist/core audit](SPECIALIST_CORE_CLARITY_AND_OVERLAP_REVIEW_2026-11-13.md) and [CRT-059 record](revisions/CRT-059_Revision_Record.md).

## Starting state and resulting change

The register requested checks of navigation, term-help interaction and the pending release. Navigation already existed. DESIGN.md and the teaching specification correctly described term help as a future requirement; no script or public dictionary implemented it.

Added the requested interaction to the shared reader, using the existing visual treatment. No learner Markdown, example, diagram, permanent URL, manifest entry or reading-route assignment changed in this pass. The course remains 59 topics: 30 main lessons, 26 task references and three practice cases.

## Interaction and meaning ownership

_data/term_help.json contains 109 curated learner meanings and aliases. They summarize concepts already taught in the course. The author terminology register still has 214 working meanings; this is not a claim that every author entry or every word has a popup. Examples include aggregation, correlation, provisioning, campaign/review/item relationships, decision/finality, machine-account ownership, activity, recommendation, cloud/data context and API evidence.

Meanings use plain text without source links or lesson navigation. Essential definitions and causal reasoning remain in the lessons. Single ordinary words are marked only inside author emphasis; specific phrases and capitalized API labels can be recognized in prose. This avoids treating an ordinary use of “limit” as an API parameter or every use of “account” as a glossary request. Headings, existing links, code and diagrams are skipped.

assets/term-help.js progressively adds native buttons without changing article text. A primary mouse press or touch opens the associated meaning immediately; release closes it. Keyboard users focus a marked term and hold Space or Enter. Hover and focus alone do not open it, and a completed click does not leave it pinned.

Pointer cancellation, lost capture, focus loss, Escape, scrolling, resizing, visibility changes and window blur close the popup. It is a fixed tooltip with a description relationship to the active button. It uses text content, not inserted HTML, has no external data request and is hidden for print. Missing/invalid data or disabled JavaScript leaves the ordinary lesson readable.

The lesson layout embeds the public dictionary and deferred script. The shared stylesheet retains its existing palette and fonts. Build-time version queries on CSS and JavaScript prevent a newly deployed reader from relying on older cached assets. Jekyll's [site variables](https://jekyllrb.com/docs/variables/) document site.time as the build time. This check adds no SailPoint capability claim or resolution of the 11 open product questions.

## Actual browser observations

Used bundled Chromium against a loopback-only preview. The preview rendered the real shared Liquid layouts/includes and all saved Markdown with bundled Marked. Ruby/Jekyll is not installed here, so this was not a Jekyll build and not a public Pages deployment.

Observed desktop at 1365 × 900 and phone layouts at 390 × 844. A separate narrow-phone check used 320 × 740.

- Hover left the meaning closed. A primary mouse hold opened it; moving outside the term and releasing closed it.
- Space and Enter opened help while held; release closed it. Escape closed the active help.
- Real browser touch start/end opened and closed help; touch cancellation closed it. The popup stayed within the 320-pixel and 390-pixel viewport bounds.
- The complete left panel collapsed and reopened. Phone navigation started collapsed; its panel and an individual module expanded and collapsed.
- All 59 direct lesson pages were inspected at 390-pixel width. Each opened the correct navigation group, exposed exactly 59 unique lesson links and kept Previous/Next within its reading route. Article text before and after enhancement was identical on every page. No page-wide horizontal overflow or JavaScript page error was found in this sweep.
- The sweep found 2,583 recognized term controls across 59 pages, with at least one on every page. This measures rendered availability, not a claim that a reader understood the terms.
- Printing hid the active helper. Forced-colour styling retained the term indication. With JavaScript disabled, the lesson remained readable without helper buttons.
- Enlarging text to 200% on a phone exposed a header overflow: the brand and working-edition label competed for one line. Added flex wrapping. After a fresh stylesheet load, document width matched the 390-pixel viewport instead of extending to 405 pixels. Table and diagram overflow stayed inside their own regions.

The cache issue during that inspection also justified the build-time asset queries. Browser interaction was checked by automation and screenshots were visually inspected; no physical-phone, screen-reader or independent learner study was performed.

## Executed checks

Thirteen automated tests pass: the seven existing route/navigation checks and six new term-help checks covering text preservation, matching boundaries, pointer release/cancellation, keyboard/interruption behavior, invalid-data fallback, unique plain-text meanings and layout/data/cache-version integration.

The content verifier passes locally: 59 learners, 6,575 normalized content units, 59 synchronized diagrams/assets and 61 learner tables. The same verifier against the local HTTP preview found all content and made 3,652 successful internal-link visits. It also checked all diagram text assets and the selected author/control URLs returned 404 in that preview. Its live=true output in this check means HTTP verification against localhost, not public-site verification.

Final structural checks pass: 262 course files, 183 Markdown files, 1,086 resolving relative links, 248 consistent table groups and 2,813 table rows. Inventory, route order, primary teaching references, 214 unique author meanings, 32 coverage rows, 24 task families, 17 capabilities and 11 open questions remain reconciled.

Compared with the 258-file pre-reader baseline, exactly ten existing reader/control files changed and four files were added: the public dictionary, shared script, tests and this record. The other 248 files are byte-for-byte unchanged, including all 59 learner bodies, all 59 teaching diagrams, the manifest, previous audit/publication records and original navigation tests. These checks do not establish a Jekyll rendering result or actual learner competence.

## Pending publication scope

The published baseline is main at fc378f4cd1dc1d1c79646912b795fd1158b28cf0. The separate repository remains TedxHarry/ISC_Certifications_Theory. The published edition stays 58 topics in 30/25/3; it has not acquired these local changes.

The complete pending release contains 30 files: 21 modified and nine new. This includes the earlier local059 and specialist/core corrections as well as the reader work. Temporary preview/check scripts are excluded and removed. No commit or push was performed in this pass.

| Release group | Prepared local change |
|---|---|
| Learner content | New CRT-059 revision 1.0; CRT-009/027 revision 1.2; CRT-045/052/053/058 revision 1.1 |
| Teaching asset and manifest | CRT-059's editable diagram and one complete manifest entry; routes become 30/26/3 |
| Reader | Shared layouts, stylesheet, deferred term-help script and 109-meaning public dictionary |
| Tests | Term-help behavior and layout integration tests; original navigation tests retained |
| Author evidence | CRT-059 brief/record, combined specialist/core audit, this reader review and reconciled current control documents |

No lesson is added to fill a module count. The updated teaching specification describes implemented local help without describing it as published. DESIGN.md owns its shared interaction contract. Historical lesson/publication evidence remains historical.

Next publish this prepared scope only when requested. Then observe the actual Pages build and verify all served learner content, assets, navigation and term-help behavior. That deployment verification remains work to perform after publication, not an unperformed local-authoring task or an implied learner test.
