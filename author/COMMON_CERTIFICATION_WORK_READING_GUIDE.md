# Common certification work: reading-guide design and verification

November 13, 2026. Local navigation work, not a new learner lesson or publication.

## Purpose and ownership decision

The user requested common certification work and continued after060/061. The register called for mapping remaining requests before another lesson. Compared the24-family task map with the two normal walkthroughs,049 targeted-project practice, existing investigation/finality/report explanations and051–053 specialist workflows.

The existing teaching meets these selected requests. Add a homepage task finder rather than another synthesis lesson. No062 learner, new compulsory module, new reading route, glossary entry or repeated lesson body is needed. Local61/30/28/3 and published59/30/26/3 remain.

The design is a content-reader enhancement. Preserve the existing field-guide palette, type, main Start action and route order. A standalone guide would add another destination before reaching the lesson; a fourth sequential route would imply additional required study. A collapsed homepage disclosure gives direct task entry without imposing either.

## Task map and honest destination labels

_data/common_work.json owns task wording, group/order, lesson IDs and format labels. _data/course.yml remains the sole owner of lesson URLs and lesson route/order. The shared include resolves targets by permanent ID; no URL is copied into the guide data.

| Work request | Existing learner destination | Format |
|---|---|---|
| Run a review: Run a periodic manager review | CRT-060 | Walkthrough |
| Run a review: Review access to one application | CRT-061 | Walkthrough |
| Run a review: Review everyone holding particular access | CRT-049 | Practice |
| Help reviewers finish the right work: Check campaign progress | CRT-042 | Explanation |
| Help reviewers finish the right work: Follow up as the deadline approaches | CRT-038 | Task reference |
| Help reviewers finish the right work: Find why the reviewer or person is wrong | CRT-045 | Investigation |
| Help reviewers finish the right work: Handle a reviewer who is away or has left | CRT-026 | Task reference |
| Help reviewers finish the right work: Investigate missing or unexpected access | CRT-045 | Investigation |
| Help reviewers finish the right work: Explain an unclear permission | CRT-009 | Task reference |
| Help reviewers finish the right work: Check whether saved decisions are final | CRT-030 | Explanation |
| Follow removals and close the review: Check what removal work is required | CRT-032 | Explanation |
| Follow removals and close the review: Follow a manual access-removal task | CRT-034 | Task reference |
| Follow removals and close the review: Investigate failed removal or remaining access | CRT-046 | Investigation |
| Follow removals and close the review: Verify that the intended access was removed | CRT-037 | Explanation |
| Follow removals and close the review: Choose the right reports and evidence | CRT-044 | Explanation |
| Follow removals and close the review: Handle overdue and unfinished reviews | CRT-039 | Explanation |
| Other review types: Review uncorrelated-account access | CRT-052 | Walkthrough |
| Other review types: Review a program or service account | CRT-053 | Walkthrough |
| Other review types: Review what a shared role contains | CRT-051 | Walkthrough |

These19 entries resolve to18 distinct existing learners; two different mismatch questions intentionally use045.049 is explicitly labelled Practice. A walkthrough label is used only for a complete coached workflow. The guide is a curated entry point, not a statistical ranking or a claim that every organization uses every review type.

Manager and source-owner work are local060/061, already authored completely. The remaining entries reuse existing teaching. Reports, counts, unfinished work and remaining access keep the scoped limitations taught by their destination lessons. No new SailPoint behavior is asserted.

## Interaction and presentation contract

Place Common certification work after the introduction and before the main lesson list. The parent and four task groups start collapsed. The main thirty-lesson Start link stays primary. Groups are Run a review, Help reviewers finish the right work, Follow removals and close the review, and Other review types.

Use native details/summary controls and ordinary links. Multiple groups may remain open; there is no forced sequence, new JavaScript, modal, external font or dependency. Keyboard and touch use the same controls. Use the existing CSS tokens, visible focus, document scroll and compact list treatment.

Do not alter lesson content, adjacent navigation, side-panel grouping, public term data or term-help behavior. The guide is outside the lesson prose, so it may link to the existing lessons without adding course links inside them.

The include omits the entire panel if guide data is absent. Every configured destination must exist in the current manifest; tests catch missing/empty data or accidental placeholders before publication. Reading still works with JavaScript disabled.

## Acceptance and evidence limits

Check data IDs, required text, destination resolution, honest Practice labelling, native closed disclosures, generated links and unchanged main/reference/practice contents. Verify the guide at desktop and narrow-phone widths, including keyboard/touch expansion and following a destination.

Keep the published59-topic site unchanged on ordinary continuation. The actual Jekyll build and public behavior must be checked after a requested publication. Local template/browser checks do not establish independent learner comprehension.

## Executed checks

All19 task labels, descriptions and destination types were reread. Short descriptions use ordinary work questions; terms such as access profiles and roles replace an ambiguous reference to packages. The guide introduces no new product behavior.

All17 automated tests pass: the13 existing navigation/term-help checks and four task-finder checks. These validate complete authored destinations, unique task/group IDs, manifest-derived URLs, Practice labelling, native closed groups, unchanged reading-route lists and omission of missing/empty guide data.

The saved-template Chromium preview checked desktop1365x900 and touch viewports390x844/320x844. Keyboard Space/Enter and touch open the parent and task groups; multiple groups can stay open. Hover does not expand the finder. The manager task opens060 with its correct current reference group and061 as its next reference. Disclosures and navigation also work with JavaScript disabled. No page errors occurred.

At200% text on the320px viewport, the existing closed Show lessons control initially extended8px beyond the layout viewport because of its9rem minimum width. Bounded that minimum by the container width; the repeat check shows320px layout/body widths. Both narrow widths now stay within the layout viewport at normal and200% text. Desktop and390px screenshots were visually inspected for readable hierarchy, spacing, wrapping and the visible Practice label.

This preview renders the saved Liquid templates and uses Marked for the destination's Markdown. It is not a local Jekyll build, a Pages deployment, physical-device observation, screen-reader testing or independent learner evidence.

The local content verifier remains61 learners/6,850 normalized units/61 diagrams and assets/63 learner tables. The structural pass checks275 source files,191 Markdown files,1,116 relative links and256 table groups/2,896 rows. Fences, table widths, destination files, whitespace and the61-entry inventory reconcile.32 coverage rows/24 task families/214 author meanings/109 helper meanings/17 capabilities/11 questions remain unchanged.

Hashes against the271-file start-of-task snapshot preserve all61 learner bodies, all61 teaching assets, the manifest, layouts, existing tests, term-help data/script and earlier author evidence. Eight existing navigation/current-state files change; four guide/data/include/test files are added. No062 learner exists. git diff --check passes. The current README file-count description is corrected to61 local/59 published; earlier dated author records retain their historical states.

Next return to existing018/049/050 practice cases to assess independent reasoning and answer separation. Do not create062 or publish on an ordinary continuation.
