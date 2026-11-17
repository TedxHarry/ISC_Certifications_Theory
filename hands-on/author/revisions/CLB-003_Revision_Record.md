# CLB-003 author and outcome record

Revision 1.0. November 14, 2026.
Learner: [Complete a manager review and check the CSV result](../../lessons/CLB-003_Complete_a_Manager_Review_and_Check_the_CSV_Result.md).
Prepared [brief](../briefs/CLB-003_Manager_Review_Brief.md).
Starting data: [baselineA](../../lab-data/baselineA/README.md).
Editable flow: [canonical diagram](../diagrams/CLB-003_CSV_Review_Flow.json).

## Authored scope

The full normal manager-review procedure, two worked reasoning opportunities, one flowchart and an expected post-review account file exist. Source creation is not repeated. The source-bound002 baseline and two reviewer sessions are execution prerequisites.

No authenticated tenant session was accessed. No filter, campaign, reviewer choice, sign-off, manual task, upload or removal was performed. The outcome CSV is supplied expected data, not a tenant export.

## Current primary checks

Official ISC sources were opened November 14 for the affected steps. Product navigation labels in the current pages use SailPoint Human Fabric. The course remains about ISC; no IdentityIQ, File Access Manager or third-party instructions were adopted.

| Reference | Bounded use |
|---|---|
| [Manager campaign creation](https://documentation.sailpoint.com/saas/help/certs/starting_campaign.html) | Admin creation, manager readiness, preview and activation. Do not infer live scope or engine from documentation. |
| [Campaign filters](https://documentation.sailpoint.com/saas/help/certs/campaign_filters.html) | One Source Equals inclusion criterion, actual filter navigation and OR boundary. |
| [Certification meanings](https://documentation.sailpoint.com/saas/help/certs/index.html) | Campaign versus assigned certification and engine separation. |
| [Certifiable access and remediation](https://documentation.sailpoint.com/saas/help/certs/understanding_certifications.html) | Individual entitlement boundary and supported manual delivery after final confirmation. |
| [Reviewer operations](https://documentation.sailpoint.com/saas/user-help/certs/reviewing/index.html) | Approve/Revoke, comments, Finish and saved-versus-final review state. No post-sign-off edit guarantee. |
| [Task Manager](https://documentation.sailpoint.com/saas/user-help/task_manager.html) | Inspect the assigned task, changed CSV/collection, then Mark Complete. No early task closure exercise. |
| [Campaign completion](https://documentation.sailpoint.com/saas/help/certs/completing_campaigns.html) | Fully signed normal completion and separate removal evidence; administrator unsigned-completion behavior is not exercised. |
| [Campaign reports](https://documentation.sailpoint.com/saas/help/certs/campaign_status_reports.html) | Sign-off/remediation evidence, regenerating reports and matching actual fields. No row-disappearance or instant-refresh guarantee. |
| [Account loading](https://documentation.sailpoint.com/saas/help/accounts/loading_data.html) | Revised full account file on the correct source and observed collection outcome. |
| [Generic multiple values](https://documentation.sailpoint.com/connectors/flat_file/va/help/handling_multi_value_attributes.html) | Removing one repeated group row while retaining the account and its other right. |

## Important source boundaries

The chosen source inclusion criterion isolates baselineA only after the fresh source is verified to contain exactly its three employee accounts. Extra identity criteria must not be described as an AND condition. Wrong, stale or broad generated work remains unstarted.

The current reviewer guide has mixed wording about changes around completion; the lesson uses a normal final sign-off and makes no post-sign-off correction claim. The completion and understanding guides also differ on unsigned administrator completion. The normal path finalizes every assigned review and does not resolve OQ-01 by inference.

The expected manual recipient is the inspected report source owner. Actual task generation, recipient, contents and timing remain runtime checks for this engine/process. Source ownership is not a promise of every administrative permission: the existing training administrator can perform the correct source upload when the owner's task UI lacks that control.

Task Manager documents a changed CSV/aggregation before Mark Complete, and warns of follow-up work if closing occurs first without a timely update. The lesson teaches the ordinary change/collect/check/close path without making a timer-recovery branch part of this first review.

The flowchart tracks employee02's rejected holding. It is not a whole-campaign state machine, a promise that all reviewers finish before any remediation starts, or a proof of backend internals.

## Beginner author reading

Read the saved learner from its opening through restoration, including both complete worked answers. Rechecked all final edited passages.

The explanation introduces campaign/certification, source/identity/profile, entitlement/holding, inclusion filter, undecided item, Approve/Revoke, sign-off, remediation and aggregation near their use. It follows the current-work evidence before revealing the worked choices. Employee02 loses export, not reading or the account.

The role distinction is explicit: manager01 reviews employee02; manager02 reviews employee03 and separately receives the expected source-owner removal work. No fictional company or continuing character is needed.

The final pass removed an assumption that manager01's four holdings must belong to one certification. Each actual assigned object must be finalized. It also placed the preview meaning before generation and made the closing conclusion conditional on actual evidence.

No learner source/course links, invented screenshots, fixed content quotas, universal API contract or passing tenant result was added.

## Data and visual reconciliation

Starting data has five people, three report accounts and five holdings. Four approvals and one Revoke follow from supplied work need. The supplied report_accounts_after_employee02_export_removal.csv contains the same three accounts and four holdings; it differs only by employee02's Export row.

Both permission definitions remain. Account01 keeps Export; all accounts keep Read. The people file is unchanged. The expected output is a narrow canonical fixture; private upload copies still require the actual full source template.

The canonical flowchart passed the pinned 11.16.1 static builder checks and validation against the supplied v2 JSON schema. Its nodes/edges match the inline learner source. No native Mermaid renderer or published-reader rendering is claimed.

## Actual status

Local package validation passed28 files,22 Markdown documents,47 project-local relative links and26 consistent table groups across260 rows. The design/register retain23 matching planning IDs and exactly three complete learner files. All four CSV structures were checked; the saved expected result equals the original account data with only employee02's Export holding removed. Original fixture hashes remain unchanged. The inline Mermaid body matches the statically generated diagram source; JSON schema validation passed. Fences, answer wrappers and source whitespace passed. The separate theory repository remains clean at1f1028a89ba8d266c80710dc5424dcafd160760d.

Authored/source/language reviewed:003 revision1.0. Expected CSV result authored:1, alongside three initial fixture files. Tenant execution, real imports, reviewer sign-off, task completion, repeated run and independent learner testing: not run. Local only; no repository or push.
