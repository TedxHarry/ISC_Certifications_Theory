# CSV-first lab strategy

Version1.0. November14,2026.

## User's chosen starting conditions

The user wants fresh sources and fresh synthetic test data. They report full administrator access and an Expert Ambassador tenant with all access/options. They prefer to avoid onboarding another connected system now and can onboard AD if a required learning outcome needs it.

Adopt fresh manual CSV-upload sources for the initial phase. Do not reuse existing application sources or existing employee data. AD is a proposed later connected-system extension, not an onboarded dependency or a task performed in this phase.

CSV is the data format. The setup must identify the actual supported file-source type and manual-upload connection mode; do not mix its steps with a VA/SFTP-backed file-fetch connector.

## Initial source/data arrangement

Create two fresh isolated sources when executing CLB-002:

- A CSV authoritative people source, with an identity profile and manager mapping. It supplies the three test employees and two test managers from baselineA.
- A CSV review-account source, with a configured entitlement attribute and separate entitlement metadata where required. It supplies the three simulated application accounts and five initial direct holdings.

Plan three data artifacts: people accounts, review accounts and the review-source entitlement catalogue. The catalogue is data for the second source, not a third application source.

The required columns, account/identity keys, manager matching, multivalue representation and entitlement flags must match the created source schemas. CLB-002 and the [baselineA package](lab-data/baselineA/README.md) now define the canonical contract using Generic/manual upload, repeated rows for multiple group values and separate catalogue metadata. The three supplied fixtures are locally reconciled. Actual source-template alignment, private email binding and successful tenant import remain untested; they are not universal ready-to-upload files.

Reviewer sign-in is a separate setup requirement. Creating a CSV identity does not, by itself, establish a usable authenticated reviewer session. Arrange the approved training logins when binding the two manager aliases.

## What CSV can teach

CLB-010 reuses A's existing four-holding expected-result comparison after a final four-item review: three Approve and employee02 Export Revoke. Its earlier unsigned draft changes when new work information establishes employee01's export need. It includes actual-task checks, one simulated external CSV update, collection before task closure and restoration after outstanding work is resolved. B and all canonical files remain unchanged. Bulk submission is not inferred from another product or an API: use individual actions unless the actual tenant provides a verified multi-item control. No new CSV or native model is added, and all runtime outcomes remain unexecuted.

CLB-009 uses native ISC review assignment and a temporary Certifications Work Reassignment rule over the existing two A Read holdings. Three instances test existing-work transfer, work generated during the rule and work after deletion. Both employees still need Read; final approvals require no account-file change. A saved choice and its actual maker are inspected separately from current responsibility. Feature/rule scope and working reviewer sessions are prerequisites; a global enablement change cannot silently activate unrelated rules. All operations remain unexecuted, and no new CSV is added.

CLB-008 keeps all seven CSVs and both application baselines unchanged. The injected faults are campaign selections: one intended identity is omitted and one extra A permission is selected. Correcting people produces four review holdings; narrowing access then produces the two required Exports. This teaches diagnostic evidence and controlled repairs without corrupting account correlation, changing manager data or granting/revoking rights. All preview/configuration writes and cleanup remain unexecuted; no new source or file is added.

CLB-007 reuses the existing A input and four-holding expected-result comparison for a separate between-cycle application-change simulation. Its file edit is not caused by a review decision or manual task. The same two-person/A Export selection should produce two holdings before collection and one after the changed data is collected and verified. A dedicated007 template is saved and reused for one future scheduled preview; no earlier template is changed and no recurring job is left behind. Saving the schedule, observing generation and activating a campaign are separate outcomes. No new data file or actual scheduler run is claimed by authoring.

CLB-006 reuses the unchanged A/B files for a preview-only filter comparison. A temporary native profile packages B Read and Export; selected identity processing should detect it for the two people already holding both. This is a planned native ISC model change, not a CSV permission grant or automatic file write. Actual detection, resulting review units and restoration must be observed during execution. No new CSV, source, activation or reviewer decision is needed. The lesson retires its temporary previews/configurations, profile and filters and restores direct representation before later baseline-dependent work.

CLB-005 reuses A and B without new source/data files. Its two selected people have eight fixture holdings across the two sources, but the requested A Export subset contains only two. The A expected result from003 is reused; B stays unchanged. The chosen Search generation flow saves an unscheduled template as a separate object during eventual execution, not during authoring.

CLB-004 extends preparation with one isolated additional Generic/manual-upload source, certlab-owner-reports-csv, using [baselineB](lab-data/baselineB/README.md). It reuses the five prepared people, adds the source owner's account only on that new source and avoids deleting a fixture account to restore003. It is a third CSV source after the initial pair, not a connected-system/AD dependency. A files and their source are unchanged. B has two initial inputs and one expected result file.

CSV files supply real account/access data to ISC. The reviews, saved choices, final confirmation, generated tasks, reassignment, templates, native model changes, reports and supported campaign APIs are actual ISC operations when performed.

The external application is represented by files in this first phase. Updating and recollecting a file demonstrates the changed source representation. It does not establish that a permission or group membership changed in an external live system.

| Work | CSV phase | Boundary or extension |
|---|---|---|
| Identity data, account aggregation/correlation and manager links | Use the fresh people/review sources and controlled data changes. | Bind and verify actual schemas/mappings and resulting identities. |
| Manager/source-owner/targeted campaigns and filters | Use collected CSV holdings as review data. | Verify actual generated scope, reviewer/type/engine and independent own-access handling. |
| Decisions, comments, sign-off, reassignment and absence | Perform actual supported ISC review operations. | The intended reviewers need their own permitted access. |
| Templates, recurrence, monitoring and reports | Perform actual supported ISC operations over CSV-backed data. | Campaign schedules and account-file collection are different mechanisms. |
| Manual-task workflow and reconciliation | Inspect actual task/recipient, perform a labelled simulated external change in the account file, complete work truthfully and collect the revised file. | Evidence proves the task/file/ISC result, not a real application's access removal. Inspect the actual task; uploading a CSV is not assumed to close it. |
| Profile/role review units and composition | Exercise the actual supported native ISC model/review path with CSV-backed entitlements. | Any external permission effect remains file simulation until a real target is connected. |
| Uncorrelated-account review | Use an intentionally unmatched account and the available supported review route. | Verify actual correlation/representation/selection; do not confuse reviewing access with repairing ownership. |
| Campaign API investigation/automation | CSV-backed campaigns can be the subject of supported ISC API operations. | Exact engine/API/authority still applies. Native campaign writes are different from source-account write-back. |
| Automated source changes and target write failures | Not demonstrated by manual CSV upload. | CLB-011 requires a supported connected target, proposed AD, and observed account/group operations. |
| Retained-access behavior and full target-outcome capstone | CSV can exercise native decisions/models and reconciliation. | Connected variants in013/017 are needed to prove actual external removal/retention and write-related recovery. |
| Machine accounts and specialist context | Treat as feature-specific preparation. | Verify source classification/grouping and actual context feeds. All-feature access does not make ordinary account CSVs into activity/cloud evidence. |

## Two outcome levels

CSV outcome: the intended review was generated, suitable reviewers finalized justified decisions, actual manual work was inspected where generated, the simulated account file was updated, and refreshed ISC data/reports were reconciled.

Connected-system outcome: the required change actually reached the target, retained rights were checked, actual operation/error/recovery evidence was examined, and fresh source observations agree.

Use these outcome names in lab records and assessment. Do not mark a connected-system outcome passed on CSV evidence alone. A learner can finish the CSV phase without claiming completion of CLB-011 or the connected variants of013/017.

The17 main/6 specialist planning IDs remain; this is an environment/verification split, not a quota-driven curriculum expansion. Job-dependent context remains conditional on the actual workflow and available data.

## First CSV manager-review result

BaselineA still starts with three account records and five holdings. The supplied business need supports four retained choices and one removal choice.

Use the Read Reports/Export Reports labels as meanings in a simulated application. Do not claim that these values grant or remove access in a real reporting product.

After actual review finalization and inspection of any required manual task, update only the rejected holding in a new account-file version. Preserve the approved holdings, collect the updated file and compare the actual ISC result with the expected four remaining holdings.

Keep original and revised files with their purpose/version. Editing a file is the simulated external action in this phase, not an automated ISC write to that file. Preserve task/evidence history, and do not assume all campaign metadata refreshes automatically after collection.

CLB-003 now supplies report_accounts_after_employee02_export_removal.csv as an expected comparison fixture alongside the three initial inputs. It is not an actual task result or an initial-baseline file. Preserve the real full template in the private upload copy and perform the change only after the justified review/manual work is inspected.

The exact manual-task sequence, recipient and account refresh must be tested in this tenant during the lab run. This design is not a passing tenant result.

## Deferred connected-system extension

CLB-011 is now authored with [baselineC](lab-data/baselineC/README.md): a planned native two-user/three-group fixture and four scoped direct memberships. It is not another CSV import. Two export-labelled test memberships are removed through actual connector writes, with one object-only permission failure and evidence of retry or a new corrective operation after the cause is fixed. Group labels do not prove a downstream reporting capability. All C execution/setup remains not run; original A/B files and the23-unit inventory are unchanged.

Use one isolated AD lab source and limited test accounts/groups if the user proceeds with onboarding. It can support the real source-account/group-change outcomes required by011 and connected verification in013/017.

Check connector capability, connectivity, enablement, actual operation authority, account targeting and reset before running those exercises. Full ISC administrator access does not itself provide AD connectivity or AD service-account permissions.

No AD source, account, group, VA or integration credential is created by adopting this plan. Other licensed contexts may need their own actual data; AD is not a universal replacement for them.

## Primary checks, November14

- [Source definitions and ownership](https://documentation.sailpoint.com/saas/help/sources/index.html): file-based sources are disconnected/read-only; flat-file work and source-owner responsibilities are documented.
- [Delimited File capabilities](https://documentation.sailpoint.com/connectors/delimited_file/saas/help/index.html): account/schema/entitlement loading supports a file-data baseline; its own connection-specific instructions must not be conflated with generic upload.
- [Account loading](https://documentation.sailpoint.com/saas/help/accounts/loading_data.html): manual flat-file upload and source-specific template/schema checks.
- [Certification remediation](https://documentation.sailpoint.com/saas/help/certs/understanding_certifications.html#certification-remediation): supported automated versus manual paths; no automatic target change inferred from sign-off.
- [ISC AD capabilities](https://documentation.sailpoint.com/connectors/active_directory/help/integrating_active_directory/supported_features.html): connected account/group entitlement operations, subject to supported configuration.

These are scoped documentation checks, not observations of the user's tenant. No runtime permission, successful import, generated task, AD write or end-user ability is claimed.

## Effect on previous preparation

This user preference supersedes the initial open choice of existing target versus new setup. The first phase now explicitly uses fresh CSV sources and simulated external account data. Earlier author/design review records retain their historical scope.

The actual tenant remains uninspected, and all lab execution counts remain zero. No repository or publication is created by this revision.

## CLB-012: staged manual fulfillment

The [012 learner file](lessons/CLB-012_Complete_Manual_Removal_and_Verify_Each_Result.md) reuses existing A/B account files and expected results. Both employee02 Export holdings are rejected, then only A changes first: A five/B six → A four/B six → A four/B five. All accounts, all Read and employee01 Export remain; B account04 owner Read is required. Task completion follows the full requested scope of each actual task, not a predicted task count or label. The wrong-file case is reasoned about without a wrong upload. Reset restores five/six only after outstanding work is resolved.

CSV performs no automatic real-target change. No new file or AD dependency is added to the main path. The conditional native manual variant needs separately verified supported C manual configuration;011's automatic setup does not establish it. A failed automatic write is not a manual-task setup. No configuration conversion, task generation or live result is claimed.

## CLB-013: explain one retained right

The [013 lesson](lessons/CLB-013_Investigate_Access_That_Remains_After_Revocation.md) reuses A's five-holding starting set and four-holding comparison. A native independent profile contains A Read+Export, detected for employee01/02. An enabled Standard role contains only direct A Read, with mapped identificationNumber Equals certlab-employee02 as its sole assignment criterion. Verify the actual model/account associations; no CSV grant or request is used to fabricate them.

Expected review units for employee02 are the profile (Revoke) and automatic role (Acknowledge). Only Export is removed in the simulated file; Read is retained under the verified role. A5→4→5 and B6 unchanged are account-set expectations, not proven native retention. Current profile/role association, actual work and historical review records are distinct. Inspect/retire temporary model and all resulting work before reset. No tenant-wide propagation setting changes.

The separately ready C automatic variant uses a C Read+ExpFail profile and C Read role for employee02, proving actual ExpFail removal while Read and employee01's two memberships remain: C4→3→4. No CSV edit, manual removal or failed write passes that connected outcome. Conflicting independent-profile-overlap guidance remains OQ-07; this case does not close it. Seven canonical CSVs remain unchanged.

## CLB-014: progress and overdue work

The [014 lesson](lessons/CLB-014_Monitor_Campaign_Progress_and_Handle_Unfinished_Work.md) reviews all five A holdings through their two existing managers. At the partial checkpoint four choices are entered, one item is undecided and only employee03 Read belongs to signed work. After final confirmation the choices are four Approve/one Revoke and all five items belong to signed work. These are fixture-level item counts, not predicted dashboard percentages or certification counts.

Campaign notifications are off deliberately. The manual Email control is inspected as an unsent local mail draft; no delivery or resend is claimed. The one rejected holding uses the existing A comparison, with collection/task reconciliation A5→4→5 and B6 unchanged. Reset precedes a separate one-item entirely blank overdue campaign. A real deadline and supported maintain-only completion are required for that outcome; no clock change or saved-unsigned decision assumption. Five unique holdings produce six planned review occurrences across the two campaigns, not six account permissions. No new CSV/model/connected-system dependency or tenant action.

## CLB-015: index the actual case

The [015 lesson](lessons/CLB-015_Build_an_Evidence_Trail_Someone_Else_Can_Verify.md) assembles existing compatible completed evidence before considering another run. Actual wider review scope is retained, not relabelled as a two-item review. If no usable history exists, a compact employee02 A Read/Export capture has one Approve/one Revoke and the existing A5→4→5 account result, with B6 unchanged. Expected files remain comparisons, not runtime evidence.

The private index links available real IDs, actors, source/account/right, event/observation and download times, work, collection and any later reset. No universal common correlation ID or complete screenshot package is promised. A working-copy B Read reference cannot prove retained A Read; original records stay unchanged and missing historical proof remains qualified. Existing-case analysis has no tenant reset; only a fresh capture restores its own scoped baseline.

Optional existing C evidence matches actual automatic e01 ExpOK removal to live target observations and later records. A normal C4→3 checkpoint and eventual reset4 do not justify omitting any intervening fault/recovery events. No new AD run, CSV, native model, actual evidence package or publication is created by authoring.

## CLB-016: correction depends on state

The [016 lesson](lessons/CLB-016_Correct_or_Retire_a_Campaign_Without_Losing_the_Truth.md) starts from A5/B6 with employee02 still needing A Read+Export. A deliberately wrong four-holding A+B preview never starts; its exact zero-work campaign and separate unscheduled template are retired after evidence/state checks. A new two-item A-only review saves then finalizes two justified approvals without an account change.

New work facts after sign-off end only A Export. Before a new instruction, inspect actual account/pending work. A separate one-item review records Revoke, preserves the earlier signed approval and follows actual manual scope/collection/closure A5→4→5, B6 unchanged. The two active campaigns contain three decision occurrences across two A holdings; the wrong preview is not an active review. No new CSV, model, AD requirement, signed edit or mail. Deletion of a preview is not demonstrated cancellation of future generation/tasks; OQ-10/11 stay open.

## CLB-017: independent crossed-source project

The [017 learner task](lessons/CLB-017_Complete_and_Defend_an_Independent_Certification_Project.md) gives business needs, original A/B data and a staged reviewer-absence/confirmation update without a query, menu walkthrough or worked output. The separate [assessor guide](author/assessments/CLB-017_Assessor_Guide.md) owns exact expected decisions/sets and critical criteria. No new learner-facing output CSV is supplied.

The assessor model removes A employee01 Export and B employee02 Export, retaining the opposite two Exports and all Read/accounts. A4/B5 totals alone are insufficient: the older A comparison also has four holdings but removes the wrong employee's right. Source-specific full private files must follow the actual reviewed facts. Existing unsigned work moves from manager01 to authorized manager02; actual history/decision-maker effects are observed, not assumed.

CSV/file completion is separate from ready C automatic membership completion, reset readiness and observed/self-checked/assisted assessment. A safe handover is not a completed removal. Main17 files are authored; no native task, file operation, score, learner pass or live result is claimed. Seven canonical CSVs remain unchanged.

## CLS-001: isolated unmatched-account review

The [CLS-001 lesson](lessons/CLS-001_Review_Uncorrelated_Account_Access_and_Track_Ownership.md) adds a dedicated non-authoritative Generic/manual-upload D source with [three CSV files](lab-data/baselineD/README.md), bringing the canonical course total to10. Its target certlab-uc-account01 has an external key absent from authoritative people; certlab-uc-control01 matches employee01. Two accounts/three holdings become two Read holdings after only target Export removal, then reset three. No new people CSV/profile/login or AD prerequisite.

The dedicated Uncorrelated Accounts route and actual reviewer option must be verified. Source-owner responsibility or explicit selection is recorded honestly; no guessed manager fallback. A shadow representation is not a verified human, and actual grouping is inspected. Limited Read purpose/custody/follow-up supports the supplied review facts while individual ownership remains unverified. Approval does not repair correlation or configure expiry. D file/task/collection evidence proves only the simulated external result; A/B seven files and C remain unchanged.

## CLS-002: native machine setup with CSV permission data

The [CLS-002 lesson](lessons/CLS-002_Review_Service_Account_Access_and_Preserve_the_Service.md) adds fresh E and [three CSVs](lab-data/baselineE/README.md). Canonical total13. Explicit accountKind/ownerKey fields supply classification/owner inputs; they do not create native relationships by file naming. Original A/B/D ten CSVs and native C remain unchanged.

The full conditional workflow uses service-only native classification, a unique searchable owner match and the documented no-maintained-application-data route: an unmapped Machine Identity creates a single-account uncorrelated application identity during classification. This is a native machine representation, distinct from D's ordinary unmatched account. No made-up human, authoritative machine profile, application-administration entitlement grant or connector-wide subtype is required.

Source owner manager01 differs from machine-account owner manager02. Actual Account Owner routing and source-owner fallback are inspected; explicit Individual selection, when supported, is not automatic-owner proof. Human control stays correlated to employee01. Continuing nightly Read and ended Export migration are supplied business facts, not actual program execution evidence.

After actual signed review/matching work, exact service Export removal changes E three holdings to two Read holdings; reset restores three after work resolution. Retain classifier/owner metadata and inspect native identity/grouping/ownership after collection. CSV edit remains simulated external work; native classification/review/task checks require real ISC observations. Actual program continuity requires a connected target/job. No runtime result is claimed.

## CLS-003: catalogue-only F and a native role correction

The [CLS-003 lesson](lessons/CLS-003_Review_a_Roles_Contents_and_Verify_the_Correction.md) uses a [new F catalogue and native contract](lab-data/baselineF/README.md). One additional two-row definition CSV brings canonical total14; no account CSV is added. F has zero accounts/holdings and the standard role has zero assignments under a verified no-match uid criterion, with requests off. This avoids detecting profiles or changing permissions on earlier populated fixtures.

Two native profiles contain separate F Read/Export definitions. The current documented legacy role-composition route reviews one role's design, with actual unit decomposition inspected. Reviewer manager02 and selected actual authorized remediation administrator have separate responsibilities. The real task/comment/native edit, rather than a changed CSV, must establish Export profile detachment from that role.

Role references2→1→2; both profile objects and catalogue definitions stay, account/holder/assignment counts remain0. Global propagation and tenant-wide processing stay untouched. Member rollout and actual application access changes require their own impact/operations/target evidence. Prior13 CSVs, C native membership contract and other sources remain unchanged. All native setup/execution/recipient/correction/reset facts remain not run.

## CLS-004: evidence limits and scoped recommendation inclusion

The [CLS-004 lesson](lessons/CLS-004_Use_Activity_and_Recommendations_to_Support_a_Review.md) reuses original A/B, with no new data source or fixture. Canonical14 CSVs/3 JSON remain unchanged. Two exact A Export holdings are reviewed; continuing recurring duty supports employee01 retention and a later supplied migration-complete confirmation supports employee02 removal. A5→4→5/B6 and full task/result/reset proof remain required when executed.

An actual Search campaign control can include available recommendations without changing global settings. The flag alone does not establish a reason/icon or a usable peer model. Native Activity Insights collects events through supported preparation; account CSV values or an added lastUsed column do not provide that event history. Blank data differs from verified zero, source activity differs from Export use, and observation time differs from data/model freshness.

The complete CSV path practises context/absence capture and an unresolved business-fact checkpoint. Actual recommendation-detail and activity interpretation have independent statuses, not run without genuine in-scope data. No invented icons/counts/event dates, peer manipulation, unrelated-source usage or new AD/cloud/DAS setup. No native or CSV operation occurred. Next CLS-005 needs current read-only API contracts and evidence reconciliation.

## CLS-005: read existing CSV review history through supported APIs

The [CLS-005 lesson](lessons/CLS-005_Investigate_a_Certification_Through_Read_Only_APIs.md) requires an actually executed compatible two-A-Export next-generation review, preferably a real CLS-004 instance. No such history is created by authoring. The [planned request contract](author/contracts/CLS-005_Read_Only_Request_Plan.json) adds five current experimental GET templates, not an executable import or observed response. Canonical14 CSVs remain unchanged; JSON contracts/assets total4.

Read campaign, parent-filtered certifications, each certification/items and decision summaries. Preserve complete pagination/actual authority, distinct subject-summary versus identity IDs and exact source-account-right bindings. Review decisions, sign-off, manual task fulfillment, historical A4/B6, later resetA5/B6 and current data remain separate evidence. No similarly named task resource is presumed to prove manual removal.

No new source/AD, event data, account file, CSV upload, campaign/decision/task mutation or tenant reset. Actor/token/current experimental availability remain real prerequisites. Offline consistency is not an authenticated GET or runtime proof. Next automation can repeat this bounded read process only after its manual actual contract works.

## CLS-006: automate the read capture, preserving the outcome boundary

The [CLS-006 guide](lessons/CLS-006_Automate_a_Bounded_Read_Only_Evidence_Collection.md) provides a [Python standard-library collector](tools/collect_certification_evidence.py), [blank private configuration](author/contracts/CLS-006_Config_Example.json) and [offline tests](author/tests/test_collect_certification_evidence.py). Canonical14 CSVs unchanged; JSON assets/contracts total5. No new source/AD/data fixture or account/CSV mutation.

An actual compatible signed next-generation case and working manual read capture are prerequisites. Fixed GET routes, manually pinned host/campaign/certification/source/account/person/entitlement/reviewer IDs, complete pages/counts, signed-state/summary checks and repeated parent/child observations bound the capture. Default configuration check sends no network; explicit live mode uses hidden token input. Standard HTTPS origin/TLS retained, redirects/proxy forwarding disabled. Private output must be new; partial evidence preserved.

Capture checks and25 passing offline test methods do not establish real actor authority, business decision quality, UI comparison, external removal or actual repeatability. Actual request/target/fulfillment results remain not run. Earlier historical A4/B6 versus later resetA5/B6 stay separate. All23 initial learner files are authored; final course audit and actual environment/lab/learner validation remain.

## CLB-018: ownership-based review without another data source

The [access-owner lesson](lessons/CLB-018_Complete_an_Access_Owner_Review.md) reuses A's original5/expected4 holdings and unchanged B6. Primary-owner metadata is a separate scoped edit, not another CSV grant or source owner change; recorded ownership restoration is checked. Optional group review certifies only employee01/02 A Read, two approvals with no account edit, using a new dedicated governance group. Existing14 CSVs and five JSON contracts/assets remain unchanged. Current learner count24; actual owner/group/campaign operations remain unexecuted.
