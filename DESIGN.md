# ISC Certifications reading site

English course reader for beginners learning ISC access certifications. The user authorized a new GitHub repository and Pages publication on October 30, 2026, followed by local continuation.

## Visual direction

Reuse the established ISC Theory reader's quiet field-guide treatment. The signature is the lesson's question and decision/outcome diagram, not a decorative hero. White paper, navy text, teal links and restrained grey boundaries keep attention on the explanation.

Canonical tokens are in assets/site.css under :root: paper #ffffff, surface #eff4f8, ink #123047, muted #526574, accent #006c67, rule #d8e2ea, focus #b84c00 and scrollbar thumb #8b9daa.

System sans-serif handles navigation and headings; Georgia/Times handles sustained lesson prose. No external fonts, images, analytics or tracking are needed.

## Layout and interaction

The shared layout owns the header, skip link, course sidebar, main reading column and footer. Desktop has a navigation column and a reading column of at most 53rem. The whole navigation can collapse; the Show lessons control remains reachable. Main modules have native disclosures; task reference and practice have separate disclosures. Only the current lesson's group starts open; home opens the first main module. Do not show empty main modules. On narrow screens the panel starts closed and opens above the lesson.

The manifest owns reading roles and order. Homepage lists main lessons first, with reference and practice in native collapsed groups. Adjacent links stay within the current reading role, so finishing the main route does not silently assign every reference. Preserve permanent IDs and direct URLs across editorial regrouping. No lesson-count quota.

The document owns vertical reading scroll. The desktop module list has a bounded internal scroll region. Tables and preformatted diagrams scroll within their own keyboard-focusable regions. Native details/summary controls support keyboard and touch.

Keep visible focus, operable scrollbars, reduced-motion/forced-colour support, stable scrollbar spacing and print-friendly content. No dashboard, user data entry or destructive actions are introduced.

## Content and publication contract

Keep learner Markdown unchanged by site setup. Jekyll optional front matter renders it with the lesson layout. _data/course.yml lists only lessons included in that publication. Unwritten planning topics have no links or placeholder pages.

Authoring instructions, planning documents, revision records, tests and dependencies are excluded from the reading site, but remain ordinary repository files. A working-edition label describes publication status without inserting author commentary into lesson prose.

Local reader update, November13,2026: _data/term_help.json owns109 curated learner meanings and aliases; assets/term-help.js owns the shared interaction. The script marks recognized phrases and emphasized terms, skips headings/links/code, and preserves article text. Single ordinary words outside emphasis stay unmarked to avoid assigning an API or ISC meaning to an unrelated sentence. All214 author meanings are not claimed as interactive help.

Hold a marked term with the primary pointer or touch, or hold Space/Enter with focus on its button. Release, cancellation, lost capture, focus loss, scrolling, resizing, tab visibility change or Escape dismisses the fixed tooltip. Hover, focus and an ordinary completed click do not leave it open. It has no navigation or external requests. Missing/invalid data or disabled JavaScript leaves readable prose. The popup uses existing palette/type tokens, stays within the viewport and is hidden for print. The header wraps at larger text sizes. Reader CSS and JavaScript URLs include Jekyll's build time to refresh cached assets after publication.

Public repository and Pages URLs use the separate ISC_Certifications_Theory destination; never the other course's remote. The [reader readiness record](author/LOCAL_READER_READINESS_REVIEW_2026-11-13.md) distinguishes local browser observation from an actual Pages build.
