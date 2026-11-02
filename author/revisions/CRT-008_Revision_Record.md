# CRT-008 revision and verification record

Revision 1.0. November 2, 2026. Local authoring; publication not performed.

Learner: [One person has two accounts. Which account's access is under review?](../../lessons/CRT-008_One_Person_Two_Accounts_and_the_Correct_Review_Target.md).
Editable diagram: [one identity, two account outcomes](../../assets/CRT-008_One_Identity_Two_Account_Outcomes.txt).
Authority: [teaching specification 1.1](../../TEACHING_SPECIFICATION.md), [course register](../../COURSE_REGISTER.md) and the user's request to continue after reporting that CRT-004's revised explanation was better.

## Brief prepared before drafting

Learning question: One person has two accounts. Which account's access is under review?

Develop COV-05's exact account/identity foundation: one human identity can have ordinary and administrator accounts on one source; a repeated entitlement label does not prove duplicate review work or identical current need. Teach source/account identifier/right context, collected ownership versus business evidence, account-specific decision and resulting target verification. Explain the connections before relying on ISC terminology.

Supporting COV-02/03/04/06/07/08/09/13/14/20/21/22/25/26/29/31 meanings appear only where the account reasoning needs them. Core recognition of uncorrelated and machine/service accounts is required. Dedicated campaign design, advanced non-human classification, full routing, correlation configuration, account-selection implementation and remediation timing remain with later or specialist topics.

Main neutral example: Reporting source, two accounts correlated to the same person. Account acct-104, readable name reports-daily, supports daily reporting work. Account acct-908, readable name reports-admin, supports separately authorized administration work. Both currently hold reports-export, meaning permission to export reports. Current need is established for export on acct-104 only. Administrative duties alone do not establish an export need on acct-908. No other role/profile/lifecycle requirement retains the example entitlement on either account; the account-specific entitlement decision and target are supplied by the example. Do not promise a universal number or layout of UI rows.

Normal explanation: establish account versus identity and ordinary versus privileged purpose; identify accounts from source context and schema-defined identifying values; trace collection and correlation to generated review context; judge need on the correct account; separate Revoke/sign-off/removal and verify the intended account while checking approved access remains on the other account. Treat UI grouping and object IDs as representations to inspect, not proof of target scope.

Meaningful variations: same readable account name on two sources; wrong identity association; missing authoritative correlation despite a placeholder identity; service account used by a process with a human responsible owner; package-level versus account-level review scope; older ISC data after actual source removal. Do not invent automatic refresh, row-count rules or a guaranteed owner/manager fallback.

Independent transfer: a person's two payments accounts both hold invoice-approve, permission to approve supplier invoices. Current need remains on one account only. Supply a removal operation/result for the wrong account and ask whether the intended outcome is established, which accounts need investigation and what evidence is missing. Change the second account to a service account to test the different purpose/ownership reasoning.

The structure is topic-led. A small account comparison and ownership/desired-outcome diagram are useful here; their number is not a template requirement. No fictional company, named person, learner-facing source links or prerequisite announcement.

## Primary-source checks before drafting, November 2, 2026

| Official reference | Checked claim and teaching limit |
|---|---|
| [Managing sources](https://documentation.sailpoint.com/saas/help/sources/index.html) | An identity can have multiple accounts on a source with different access; uncorrelated accounts can have a shadow identity without authoritative association. No universal UI row structure for certifications inferred. |
| [Source account schemas](https://documentation.sailpoint.com/saas/help/accounts/schema.html) | Configured Account Name and Account ID attributes, source-account reference and entitlement linkage. Teach interpretation of identifiers, not a schema-change procedure or universal immutable source identifier. |
| [Account correlation](https://documentation.sailpoint.com/saas/help/accounts/correlation.html) | Configured account/identity comparisons, unmatched account handling and manual association. Identity linkage does not prove current business need. No universal automatic recalculation after manual correlation claimed. |
| [Loading accounts](https://documentation.sailpoint.com/saas/help/accounts/loading_data.html) | Account collection into ISC, processing/observation time and account data distinct from target changes. No fixed refresh duration or automatic campaign replacement claimed. |
| [Working with certifications](https://documentation.sailpoint.com/saas/user-help/certs/reviewing/index.html) | Identity/access-item views, item detail inspection, uncorrelated and machine account review meanings, decisions and supported context. The account-specific main example supplies its decision scope; no universal separate decision per account or blanket grouping rule. |
| [Starting campaigns](https://documentation.sailpoint.com/saas/help/certs/starting_search_campaign.html) | Dedicated uncorrelated- and machine-account campaign routes, machine/application-identity subject and campaign-specific reviewer options. Phased availability and actual tenant permissions/features remain bounded. No full specialist procedure or fixed reviewer fallback taught. |
| [Managing machine accounts](https://documentation.sailpoint.com/saas/help/machine/accounts.html) | Non-human process/service purpose, conditional Machine Identity Security classification and correlation to application identities. Human accountable owner differs from making a service account a personal employee account. |
| [Managing access profiles](https://documentation.sailpoint.com/saas/help/access/access-profiles.html) | Profile grouping and source account selection. Automatic-assignment multiple-account criteria differ from access-request account selection; neither is a universal certification-revocation targeting rule. |
| [Understanding certifications](https://documentation.sailpoint.com/saas/help/certs/understanding_certifications.html) | Certifiable access depends on assignment origin/container; decisions and actual removal are distinct. No exact engine-wide timing or unsigned-review outcome inferred. |
| [Provisioning overview](https://documentation.sailpoint.com/saas/help/provisioning/index.html) | Supported account/access changes and actual operation/result. No invented private backend, universal manual owner or guaranteed success. |
| [Certification item account details](https://developer.sailpoint.com/docs/api/get-certification-item-account-details-v-1/) | Documents an account-detail read for a particular review item; Experimental, with administrator/certification reviewer authorization. No API call, response schema or universal availability claim. |
| [List review items](https://developer.sailpoint.com/docs/api/list-review-items-v-1/) | Identity-campaign review items and authorized read access; Experimental. This establishes a supported record-inspection route, not a universal one-item-per-account layout or separate decision rule. |
| [Identity profiles](https://documentation.sailpoint.com/saas/help/setup/identity_profiles.html) | Authoritative sources establish identities from their account information. Used only to explain authoritative ownership versus an uncorrelated placeholder; no profile-priority or setup procedure taught. |

Fresh source comparison found an unresolved difference between the reviewer guide and access-profile administration guide about overlapping entitlements during profile revocation. Record OQ-07 in the capability register before later overlap teaching. This lesson's main and transfer examples exclude overlapping automatic/package requirements, so they do not depend on resolving that difference. Earlier OQ-01–06 remain open.

## Actual saved coverage

| Teaching purpose | Saved explanation and reasoning |
|---|---|
| One person, separate accounts and purposes | Start with the person and each account: separate application records associated with one ISC identity; everyday versus authorized administration work. |
| Privilege versus present need and ISC authority | Same section: sensitive application actions do not justify every permission, and application administration does not confer ISC campaign permissions. |
| Exact source/account context | Identify the account before judging its access: Account Name and Account ID explained before the two-account table, source kept with the reference, permission name distinguished from account identity. |
| Duplicate-looking names and different IDs | Same section: test/production source collision, ISC record ID versus source Account ID, readable administration label versus actual purpose and privilege. No immutable-ID or universal API-field claim. |
| Data collection and ownership flow | Follow how the two accounts become review information: aggregation reads held rights; the configured employee-number match uses supplied value 7312 to identify exactly one correct person, allowing both distinct accounts to link to that identity. Both current permissions are supplied. Collection does not grant access or judge need. |
| Legitimate multiple accounts versus duplicates | Same section: two accounts can be legitimate; repeated identity or entitlement names are not sufficient evidence to delete data. |
| Campaign, assigned review, item and UI grouping | Same section: terms locally introduced; identity/access views and item details do not erase account distinctions or prove all intended accounts were selected. |
| Current account-specific need | Decide why the permission is needed on each account: ordinary reporting needs export, administration does not, although administration itself remains authorized. |
| Diagram meaning | Same section: one identity branches to two source/account references; keep/remove labels are desired outcomes rather than completed operations or universal row structure. |
| Decision scope versus business intent | Same section: direct item targeting only acct-908 is a supplied condition; unclear/combined scope must be established before finalization. No separate decision per account promised. |
| Access profile and role boundaries | Same section: package definitions and affected accounts/contents before assuming the item changes one entitlement on one account. Detailed grant-account selection and overlap mechanisms stay outside this lesson. |
| Review confirmation and removal work | Carry the same account reference through removal: Revoke, locally explained sign-off, applicable campaign process, remediation and provisioning; no exact engine-wide trigger. |
| Narrow operation and outcome evidence | Same section: remove export from acct-908 rather than disable/delete an administration account still needed for other work; preserve approved export on acct-104. |
| Why continued access may be expected | Same section: export through acct-104 is intended, so an unspecified successful export test does not prove failure on acct-908. Wrong account changes are not successful business outcomes. |
| Different observation times | Same section: current application, collected ISC and generated review data can describe different times; no automatic refresh/rebuild guarantee. |
| Wrong-person association and responsibilities | If the account is shown under the wrong person: verify reliable ownership facts, correct correlation through authorized work and inspect actual review contents afterward; subject/reviewer/operator are distinct roles. |
| Authoritative versus uncorrelated representation | If ISC cannot associate the account with an authoritative identity: authoritative-source basis explained before authoritative identity; missing match versus still-held access; shadow identity does not prove a known employee link. |
| Dedicated uncorrelated review recognition | Same section: employee selection is not proof of coverage for an unmatched account, supported dedicated campaigns are conditional and correlation is not fabricated to clear a list. No full X-02 procedure claimed. |
| Service/machine purpose and accountable owner | A service account needs a different ownership question: job needs, responsible human, configured classification and application/machine identity; human ownership does not make the account a personal login. |
| Specialist capability and reviewer limits | Same section: available features and campaign type checked; no employee-manager assumption or universal missing-owner fallback. No full X-03 procedure claimed. |
| Independent changed-account transfer | Work through a removal that reached the wrong account: completed pay-210 operation removes approved access while pay-880 retains unwanted access; both mismatches need authorized correction and exact account evidence. |
| Changed subject in transfer | Final paragraph: pay-880 becomes a scheduled-job account; employee administration need is no longer adequate evidence, so reassess purpose, owner, representation and review. |

COV-05's multiple-account/ownership foundation is authored. Supporting distinctions do not complete detailed campaign configuration, correlation implementation, APIs, reviewer routing, overlap or remediation procedures. Routine task support: families 2, 7, 13, 14, 17, 18, 19, 21 and 22. Specialist X-02/X-03 recognition is core, with deeper route work still planned.

## Saved-file readability and consistency review

The complete saved lesson was read in contiguous portions, including the middle, both special-account sections, diagram, comparison table and full worked answer. This is an author review, not an independent beginner or tenant observation. The November 2 user feedback that CRT-004 was better authorizes carrying forward the explanation style; it is not assessment evidence for CRT-008.

The read-through led to separating Account Name from Account ID explanations; explicitly distinguishing reading a permission from granting it; showing the configured employee-number comparison behind two account links; separating campaign from assigned review/reviewer; removing unnecessary account-name wording; grounding authoritative identity in personnel-source records; and keeping recorded account ownership distinct from a support team or personal login. The uncorrelated review paragraph uses the familiar missing-link explanation and does not invent an authoritative employee association. Account scope is established before any purported account-specific Revoke.

Both main accounts have the same permission and same identity, but different supplied current needs. The confirmed direct-entitlement target is acct-908 only; no containing package or automatic requirement keeps it. The transfer changes source, IDs and permission to Payments/pay-210/pay-880/invoice-approve, supplies current before/after account evidence and deliberately identifies the wrong removal target. Its final variation changes the subject to a process and therefore changes the needed evidence rather than prescribing an employee-based decision.

## Verification and publication

The four existing reader-navigation tests passed. The local site verifier passed for the unchanged six-entry reader manifest: 681 content units, six diagrams, six tables and eight locally present text assets. This is a local consistency check, not a live publication or graphical review of CRT-008.

All 34 Markdown files were checked: 175 relative links resolve, and 58 table groups have 781 consistently shaped rows. All eight learner diagrams match real editable text assets. The design and course register retain the same 50 ordered unique candidate IDs; eight learner files exist, leaving 42 current candidate topics unwritten, and CRT-009 has no stub. The terminology register has 94 distinct working terms after adding five; all seven product questions remain open. The lesson has no external source/course URL, unfinished marker, fictional character or revision commentary.

A pre-authoring SHA-256 inventory covered 56 authored/site files, excluding repository internals and installed dependencies. Exactly nine existing course/author metadata files changed and three CRT-008 files were added, bringing the package to 59. The other 47 starting files remain byte-identical, including all seven earlier learner texts/assets, their historical records, CRT-004 revision 1.1, unpublished CRT-007, publication evidence, teaching specification, reader manifest and reader implementation. No starting file was removed. Whitespace checks passed for the tracked changes and three new files.

The user has not supplied an assessment result for CRT-008. Source checks and the saved author read-through do not prove independent learner understanding. No tenant action, commit, push or deployment occurred. CRT-004 1.1 and CRT-007/008 remain unpublished local work; CRT-009 is the next unwritten topic to prepare.
