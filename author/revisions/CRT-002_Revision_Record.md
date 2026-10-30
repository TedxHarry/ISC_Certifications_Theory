# CRT-002 revision and verification record

Revision 1.0. October 30, 2026.
Learner: [A campaign, a certification and a review item: what is being assigned?](../../lessons/CRT-002_Campaigns_Certifications_and_Review_Items.md).
Editable visual: [campaign/review/item hierarchy](../../assets/CRT-002_Campaign_Review_and_Item_Hierarchy.txt).
Authority: [teaching specification](../../TEACHING_SPECIFICATION.md); [prepared author brief](../AUTHORING_GUIDE.md).

## Scope and publication boundary

The user requested creation of the separate ISC_Certifications_Theory GitHub repository, push and Pages publication, then continuation. Initial publication was completed and verified before this lesson was written. The content commit is 98f1a263e6e8990ab99506de40f2c757a635b18c; Pages workflow 41007230219 succeeded. Its author-only follow-up is 9056f7c6c32f83322bbde12bedaadc3ed24d445d; workflow 41007516370 also completed successfully.

CRT-002 is the complete local continuation. It has not been committed, pushed or added to the publication manifest. The live reader still lists CRT-001 only. The [initial publication record](../PUBLICATION_2026-10-30_INITIAL.md), CRT-001 learner/asset/author record and reader implementation remain unchanged during this authoring step.

## Intended understanding and actual scope

Explain the campaign containing assigned certifications, the items within each certification and the person/account/access context of each item. Distinguish the person holding access, assigned reviewer and recorded decision maker. Connect work responsibility with the separate need for platform permission. Use the correct record and counting unit when explaining progress.

COV-02's hierarchy foundation is primary. COV-03's responsibility/permission distinction is authored, not its complete permission matrix or routing mechanisms. CRT-003 still owns the full data-to-outcome path.

## Coverage against saved teaching

| Teaching purpose | Actual saved section or example |
|---|---|
| Why existing permissions need review | Start with a person, an account and a permission: a person's work can change while access remains. |
| Account, access and separate capabilities | Same section: viewing versus exporting reports. |
| Identity and entitlement | Same section: ISC person record connected to accounts; represented system right. |
| Review subject versus reviewer/certifier | Same section: whose access is judged versus who judges it. |
| Conditions for the entitlement example | Correct identity/account association, suitable collected information, individual review eligibility and no other requirement keeping/restoring access. |
| Review item and exact decision target | One access decision needs a clear target: identity-1, reports-user-1 and reports-export; target question stated in full. |
| Approve and Revoke meaning | Same section: continued appropriateness versus removal decision; no blanket account approval or account deletion implied. |
| Certification as assigned work | A certification puts review work in someone's hands: two permissions assessed separately in one assigned review. |
| Campaign purpose and scope | A campaign organizes the related reviews: selected reporting access and common organization/settings. |
| Generation versus start | Same section: prepare the review contents versus open the work to reviewers; no scheduler or exact engine transition promised. |
| Grouping is inspected, not assumed | Same section explicitly permits multiple identities within a review and uses the supplied generated grouping. |
| Concrete containment | Three-row table and editable hierarchy: one campaign, two reviews, three items. Branches mean contains, not execution order. |
| Same permission on different accounts | Why does “view reports” appear twice?: separate subjects/accounts can need different decisions and evidence. |
| One subject can have several decisions | Same section: two different permissions on identity-1's account are two items to decide on. |
| UI versus represented records | How does this connect to what someone sees in ISC?: campaign, assigned work and item details. |
| Identity/access grouping in reviewer view | Same section: view information by person or access without creating another grant. |
| Find the object behind a vague problem | Same section: missing campaign, assigned review or expected item require different checks. |
| Creator, owner and administrative levels | Who is responsible for which part?: definition/generation/start require appropriate permissions; creator/owner labels do not prove them. |
| Source/access owner versus current reviewer | Same section: source meaning, owner responsibilities and campaign-dependent reviewer choices. |
| Remediation responsibility | Same section: carrying out the required change through the applicable automated/manual work; inspect actual assignment. |
| Current assignee versus recorded actor | The assigned reviewer and the decision maker can differ: changed assignment or administrator decision can explain different names. |
| Saved decisions versus confirmed review | What does “finished” mean in our campaign?: review A has two decisions and supplied confirmed completion; review B remains undecided. |
| Progress uses distinct units | Same section: one of two reviews complete; two of three items decided; no universal UI counter formula asserted. |
| Review versus campaign versus target outcome | Same section: neither whole-campaign completion nor actual export removal follows from A's completion. |
| Evidence selection in changed cases | Use the distinction to choose your next check: two reviews/one reviewer, item-level result and source-owner authority. |
| Independent transfer | Three reviews sized two/one/three, two current reviewers, two saved decisions and missing confirmation; worked reasoning identifies all six items and required evidence. |

Supporting introductions touch COV-05/08/14/18/20/21/26/29 only to make this lesson understandable. Grant origins, data collection, selection/filtering, templates/schedules, fallback, self-review routing, reassignment procedures, finality policies, report formulas and full removal mechanics remain with their primary topics.

Routine task foundations: task 7 (which generated records to inspect), task 8 (responsibility versus authority), task 9 (review/item progress units), task 10 (current assignment record) and task 14 (decision tied to a person's exact access). No full operational procedure is marked complete by this introductory support.

## Primary claims checked October 30, 2026

| Official reference | Verified claim used and scope limit |
|---|---|
| [Certifications overview](https://documentation.sailpoint.com/saas/help/certs/index.html) | Campaign is the set of reviews; certification is an assigned review. Cert Admin/Org Admin define, generate and start campaigns; reviewers decide/sign off. No exact engine sequence or tenant availability inferred. |
| [Campaign status and reports](https://documentation.sailpoint.com/saas/help/certs/campaign_status_reports.html) | Access Review is a reviewer's item collection within a campaign. Subject/account/source/access context differs from reviewer. Current reviewer can differ from decision maker after reassignment or administrator action; decision and removal evidence are distinct. Field-by-field report behavior remains for later teaching. |
| [Starting a campaign from Search](https://documentation.sailpoint.com/saas/help/certs/starting_search_campaign.html) | Campaign details and supported reviewer choices depend on campaign type. Owner labels alone do not establish actual assignment. No universal routing or grouping algorithm taught. |
| [Working with certifications](https://documentation.sailpoint.com/saas/user-help/certs/reviewing/index.html) | Identity access contents can be examined by identity or access item; Approve/Revoke and reviewer confirmation concern assigned review work. No universal screen-label, unsigned-completion or edit-after-finality rule asserted. |
| [Understanding certifications](https://documentation.sailpoint.com/saas/help/certs/understanding_certifications.html) | Individual entitlement eligibility depends on the access model. Example excludes encapsulation/other automatic requirements; required change can use automated or manual work. No exact timing, fallback chain or universal removal guarantee taught. |

These are supported object relationships and responsibilities, not invented backend tables, queues or private processing. The neutral record examples and arithmetic are supplied teaching cases, not observed tenant outputs.

OQ-01 unsigned completion and OQ-02 exact remediation timing remain open. OQ-03 environment-specific permissions/availability and OQ-04 exhaustive release completeness are also unresolved. This lesson does not need an unsupported answer to any of them. No role-composition, uncorrelated-account or machine-account procedure is generalized from this human identity-access example.

## Example and answer reconciliation

Main records: one started campaign; review A assigned to reviewer A with identity-1/reports-user-1 and reports-view/reports-export; review B assigned to reviewer B with identity-2/reports-user-2 and reports-view. Correct ownership, appropriate reviewers and no self-review are supplied. Table and diagram agree on review membership and item counts.

Changed state: A has Approve view, Revoke export and supplied confirmed review completion. B has one undecided item. Therefore two of three items have recorded decisions and one of two reviews is confirmed complete. Campaign completion and access removal are not established by those counts.

Repeated access name: reports-view on two different accounts is two distinct access relationships. Evidence of need for one person does not decide the other person's access.

Actor change: an earlier recorded decision maker and a different current assignee can both be correct. Inspect the decision history for the original actor/time.

Transfer: reviews P/Q/R contain 2/1/3 items. One person holds P and Q; another holds R. That is one campaign, three reviews, two current reviewers and six items. P's two saved decisions establish two decisions, not its missing confirmation or the account outcome. No assumption about the deadline policy or automatic grouping is required.

## Complete saved-file beginner author read-through

The full saved learner was read from its opening through the transfer answer, then reread in two contiguous parts after edits. This was a simulated author review, not an observed beginner participant.

Corrections made during that pass:
- Added the simple reason for reviewing existing permission: access can remain after work changes.
- Replaced an unnecessary “usually” claim with a concrete possibility.
- Removed a sentence about what the teaching example lets the course concentrate on.
- Made multiple-identity review contents explicit, avoiding a one-review-per-person assumption.
- Changed “two item decisions” to “two items to decide on” before any recorded decisions exist.

Necessary terms appear with their purpose before later reasoning depends on them. Technical labels identify person/account/permission records without a biography. The diagram's containment meaning is explained, and the narrative connects each count to its evidence. The transfer changes both review sizes and assignment counts, then explains the missing confirmation/removal evidence.

The operational task-map reconciliation was corrected to match its actual row titles: row 9 is progress, row 10 is missing/incorrect reviewer and row 14 is decision understanding. Introductory support does not imply those tasks are fully taught.

Actual learner validation remains pending. No tenant action, practical certification run, uncoached participant assessment or feedback result is claimed.

## Saved-file and scope verification

The saved-file checks completed October 30, 2026:

- All 17 Markdown documents were checked for table consistency outside code blocks; 425 table rows have consistent columns. All 71 relative Markdown links resolve to real files.
- The CRT-002 inline diagram matches its editable text asset; maximum width is 28 characters. The three-row access table, review assignments, main-case counts and independent-transfer answers agree.
- The learner has no source/course link, revision footer, unfinished marker, fictional biography or prerequisite announcement.
- The register retains all 50 unique candidate topic IDs. There are two complete learner files and two per-lesson records. CRT-003 has no stub, and 48 current candidate topics remain unwritten.
- npm test passed all four existing reader-navigation checks. These test reader behavior, not learner comprehension.
- node author/verify-site.mjs passed locally for the unchanged publication manifest: one lesson, 104 content units, one diagram and one table; two local text assets now exist. This check covers the manifest's CRT-001; CRT-002's separate saved-file/diagram/coverage checks are recorded above. The live verifier was not rerun against unpublished CRT-002 assets.
- Tracked-file whitespace checks and new learner/asset/record whitespace checks passed after removing extra trailing blank lines in the new learner and asset.
- Scope audit: 33 starting authored/site files become 36. Exactly nine course/author metadata files change and three CRT-002 files are added. The other 24 starting files remain byte-identical, including CRT-001 learner/asset/record, the publication evidence, manifest, layouts, styles, site tools and tests. No starting file is removed.
- Local HEAD and remote main remain 9056f7c6c32f83322bbde12bedaadc3ed24d445d. The staging area is empty; CRT-002 and its metadata continuation are local working files, not another push.

No CRT-002 graphical publication review has occurred because this lesson is not deployed. Source verification, simulated beginner author review and structural checks do not establish observed learner understanding.

## Outcome and next

Revision 1.0 has complete prose, worked reasoning and author source/coverage review. Actual learner validation and CRT-002 publication remain pending. CRT-003, Follow one review from access data to a verified outcome, is next; prepare its brief and fresh claims before writing. No CRT-003 stub exists.
