# CRT-004 revision and verification record

Revision 1.0. October 30, 2026.
Learner: [Certification, access request or lifecycle rule?](../../lessons/CRT-004_Certifications_Access_Requests_and_Lifecycle_Rules.md).
Editable visual: [three starting points](../../assets/CRT-004_Request_Review_and_Lifecycle_Starting_Points.txt).
Authority: [teaching specification](../../TEACHING_SPECIFICATION.md), [prepared brief](../AUTHORING_GUIDE.md).

## Publication followed by local continuation

The user requested push and continuation. CRT-002/003 were published before this lesson was written. Content be8e69d3c63c1b9b03e3c40e800c3092b34ea73d built successfully in workflow 41020384730. The full live check passed for three lessons, 343 normalized content units, three diagrams/tables/assets, CSS, sixteen internal link visits and author-route exclusions.

An initial checker failure was traced to Markdown bullet markers, while the actual live list items contained the correct text. The narrow correction and publication-status evidence were pushed as ca6890b0c0033683c5a8133d85bb17ff2d5cb1ed. Its Pages workflow 41020752145 also completed successfully. No learner content was altered to resolve the checker issue.

CRT-004 is the next local complete learner, not part of that published snapshot. Earlier learners, assets, per-lesson records, publication evidence and reader/manifest/tool files remain preserved during this local continuation. No source/tenant mutation or participant assessment is involved.

## Actual scope and coverage

COV-01's comparison is primary. Supporting COV-06/07/20/22/23/24 meanings explain why different assignment origins change what can be reviewed and what control should be investigated. Detailed access-model configuration, approval routing, lifecycle implementation, campaign timing, overlap/removal procedures and API contracts remain with their primary topics.

| Understanding developed | Actual saved teaching |
|---|---|
| Person/account/access foundations | Start with the access someone needs: identity, account, entitlement, source and single-source access profile. |
| Concrete package meaning | Reporting Export contains reports-view and reports-export; viewing and exporting are explained. |
| Request starting point | An access request asks for a change: unmet reporting need, requestable profile and correct recipient account. |
| Requester versus recipient | Same section: submitting person versus person receiving access; identical here, potentially distinct in supported requests for others. |
| Configured approver | Same section: judges requested recipient access; approval process is configured, not universally one manager step. |
| Approval versus delivered grant | Same section: proposed grant accepted, provisioning work, successful account rights supplied separately. |
| Provisioning includes removal | Same section: access changes include granting and removing. |
| Removal requests | Same section: supported removal requests have their own intent/configured process; they are not certifications. |
| Current review versus earlier request | A certification asks about access the person already has: later need must be established again. |
| Campaign, certification and item | Same section introduces the needed meanings before decisions rely on them. |
| Correct unit of review | Requested Reporting Export is one profile item; its entitlements are contents, not two separately reviewable items here. |
| Revoke and Approve | Both supported by supplied current need; resulting removal work and account evidence remain separate. |
| Package scope when need changes | Check what the review item includes: keeping view while removing export requires planning for the full package's effect. |
| Lifecycle state/LCS meaning | Lifecycle-based access starts with a configured requirement: business stage, configured access requirements and actions. |
| Calculation/mapping/manual state | Same section: identity data mapping or authorized manual assignment can establish state; mapping meaning is supplied. |
| Identity processing | Same section: evaluates identity data/configuration and initiates required access work. |
| Birthright example | Enabled configured active state requires Employee Portal with portal-use; no separate personal request in this example. |
| State name versus behavior | Same section: active label does not prove which access that configuration requires. |
| Why access can be restored | Why can lifecycle-required access come back?: manual target removal leaves the current state's profile requirement intact. |
| Persistence scope | Same section explicitly excludes a universal continuous-retry claim for account enable/disable actions. |
| Lifecycle certifiability | That also affects what a certification can review: current LCS profile not an individual profile decision; its encapsulated contents not separate entitlement decisions. |
| Origin and access model | Same section explains assignment origin and configured packages/requirements; absence of an item does not prove absence of access. |
| Parallel control flows | These controls work alongside each other: editable diagram shows separate inputs, not sequential mandatory phases; table identifies the question and evidence for each control. |
| Diagnose the appropriate control | Use the starting question to choose what to inspect: missing grant, old approval, restoration, inaccurate personnel input and inappropriate inactive-state proposal. |
| Independent changed evidence | Two-package invoice/portal transfer rejects both an old-approval shortcut and falsifying correct lifecycle data; explains required invoice-removal evidence. |

Routine task support: task 1 (clarify review/change intent), 13 (origin-related absence and package meaning), 14 (judge current need and decision scope), 17 (decision versus required removal) and 20 (retained/restored access requirement). These are foundations, not full task procedure coverage.

## Fresh primary checks, October 30, 2026

| Official reference | Claim used and limit |
|---|---|
| [Managing requests for roles and access profiles](https://documentation.sailpoint.com/saas/help/requests/config_ap_roles.html) | Requestable profile, configured approval, recipient grant and supported removal process. No universal approval step count, global policy bypass or request timing asserted. |
| [Requesting access](https://documentation.sailpoint.com/saas/user-help/requests/request_center.html) | Requester/recipient context, supported requests for others and request for access. No assumed common screen across all tenants or request interfaces. |
| [Requesting access removal](https://documentation.sailpoint.com/saas/user-help/requests/requesting_access_removal.html) | Supported removal requests exist and differ from periodic review. No claim that every assignment is request-revocable. |
| [Managing access profiles](https://documentation.sailpoint.com/saas/help/access/access-profiles.html) | Related entitlement bundle from one source; request and lifecycle origins; review/removal applies to the package in this bounded example. No JIT, deleted-profile or overlap policy generalized. |
| [Setting up lifecycle states](https://documentation.sailpoint.com/saas/help/provisioning/lifecycle.html) | State mapping/manual assignment, identity processing, configured profile grants and persistence while state applies. Account enable/disable actions are not a persistent retry mechanism. No universal state-name behavior, exact recalculation schedule or immediate successful restoration promised. |
| [Understanding certifications](https://documentation.sailpoint.com/saas/help/certs/understanding_certifications.html) | Requested access profile can be certified; LCS profile is omitted individually and encapsulated entitlements are not individually certifiable. No unsigned or exact remediation-trigger outcome taught. |
| [Certifications overview](https://documentation.sailpoint.com/saas/help/certs/index.html) | Assigned review/campaign meaning, current-access judgment and broad confirmation/follow-up. Engine/availability conditions remain scoped. |
| [Provisioning overview](https://documentation.sailpoint.com/saas/help/provisioning/index.html) | Access changes can originate in requests, certifications and automatic configuration. No private backend, retry schedule or universal manual recipient rule invented. |

The first guessed removal-help URL was unavailable; following the official Requesting Access page's removal link supplied the successful canonical reference above. No failed URL is treated as verified source content.

OQ-01–05 remain open. This lesson requires no universal unsigned outcome, campaign-remediation phase order, manual-task recipient or target-tenant availability conclusion. Its lifecycle enforcement and omission claims are tied to the documented model, not observed in a tenant.

## Supplied conditions, changed cases and answers

Reporting request: both rights initially absent; requestable standing profile, correct account association, appropriate configured approver, supported authorized grant and successful account result. No delayed start or additional activation.

Later review: requested profile remains held, both reporting needs have ended, no other requirement retains it. Revoke concerns the whole profile. Changed need preserves viewing as a separate requirement to resolve before a full-profile removal; no answer pretends that the profile item is an individual export entitlement.

Lifecycle case: active state and Employee Portal profile correctly configured/enabled; portal-use required while that state applies. Manual removal does not change that requirement. A wrong source status, wrong calculation and wrong package requirement are different investigations; correct lifecycle information must not be falsified to remove one requested package.

Independent transfer: Invoice Approval gives invoice-approve through the person's payments-system account; Employee Portal comes from correct active lifecycle state and remains needed. Current invoice need is confirmed ended, profile is reviewable and no other assignment requires that right. Revoke plus supported follow-up is justified; old approval and inactive-state workaround are not. No completed account removal is inferred solely from a saved decision.

The diagram's three branches agree with the prose and comparison table. Its first branch shows an approved grant request, without excluding the separately explained removal-request variant.

## Saved-file beginner author read-through

The complete saved learner was read from opening through the transfer answer in contiguous portions, then reread after edits. This was a simulated author review, not an observed participant. The same neutral permissions remain explained at each necessary point; no prior lesson or fictional biography is required.

The read-through led to these changes: replaced an unexplained integration reference with the actual ISC-to-system connection; removed an early lifecycle term before its explanation; made the whole-profile removal effect clearer when viewing is still needed; simplified the success and section wording; explained individually certifiable as separate review decisions; changed the comparison question to plain language; and established the payments-system account before relying on it in the transfer answer.

The requested package's successful grant is supplied separately from approval. Both original permissions are no longer needed before the main Revoke case. The partial-need case preserves viewing as work to resolve, rather than silently removing it. The LCS example supplies an enabled configured requirement and does not generalize profile persistence to account actions. The transfer changes the access package and rejects both an old-approval shortcut and an inaccurate-state workaround, with final account evidence still required.

Actual independent beginner validation remains pending. No learner pass, tenant execution or graphical CRT-004 review is claimed.

## Verification and publication state

Final saved-package verification completed October 30, 2026:

- All 22 Markdown documents were checked for consistent tables outside code blocks: 532 table rows have consistent columns. All 101 relative Markdown links resolve to real files.
- CRT-004's inline diagram matches its editable text asset; maximum width is 28 characters. The three separate starting points agree with the prose and comparison table. The first branch's approved-grant scope and the separately explained removal request remain explicit.
- The learner has no source/course URL, revision footer, unfinished marker, fictional biography or prerequisite announcement. Definitions and reasoning needed for the examples remain inline.
- Design and register retain the same 50 ordered unique candidate topic IDs. There are four complete learner files and four per-lesson records; 46 current candidate topics remain unwritten. CRT-005 has no stub. The five open product questions are preserved.
- Four existing reader-navigation tests passed during the preceding publication preparation. The full live verification then passed for the three published lessons, 343 content units, three diagrams/tables/assets and sixteen internal link visits, with four representative author-route exclusions. Both Pages workflows succeeded as recorded above.
- After adding local CRT-004, node author/verify-site.mjs passed locally for the unchanged three-lesson publication manifest: 343 content units, three diagrams, three tables and four local text assets. This does not claim a graphical CRT-004 review; its separate saved-file/diagram/coverage checks are recorded here. The live checker was not rerun against the unpublished new asset.
- Tracked and new learner/asset/record whitespace checks passed.
- Scope since the publication follow-up: 40 starting authored/site files become 43. Exactly nine course/author metadata files change and three CRT-004 files are added. The other 31 starting files remain byte-identical, including all previous learner/asset/per-lesson records, both publication evidence files, the manifest, reader design and corrected site verifier. No starting file is removed.
- Local HEAD and remote main remain ca6890b0c0033683c5a8133d85bb17ff2d5cb1ed. The staging area is empty. No commit or push includes CRT-004.

CRT-004 is local and unpublished. CRT-001 through CRT-003 remain published and live-verified. Actual independent beginner validation, tenant execution and graphical CRT-004 publication review have not occurred. Source checking, structural checks and simulated author review are separate from observed learner understanding.

## Next

CRT-005: How does application access become information ISC can review? Prepare its primary data-path brief and fresh claim checks at the next continuation; do not create a stub.
