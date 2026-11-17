# Complete manual removal and verify each result

Two removals are due for the same person. You finish the first one. Can you now mark the work complete?

Let's make the answer visible. We will remove Export Reports from one source first, check what remains on the other, and complete each task only when all the work it asks for is done.

## Understand the work you are completing

A **campaign** groups access reviews. A **certification** is an assigned review inside it. Its reviewer decides whether existing access should remain. **Revoke** means the reviewed access should be removed.

That decision still needs to reach the system holding the account. **Manual fulfillment** means an authorized person makes the change instead of ISC writing it automatically. ISC records a task describing the required work.

The reviewer and the person completing the task may be different people. The reviewer confirms the business need. The person doing the removal must identify the correct account and have permission to change it.

Here, CSV files represent two simulated applications. Editing a file models the external change; uploading it lets ISC read the changed account data. We can check the ISC review, task and collected result. We cannot use those files to prove removal from a real reporting application.

## Establish the starting accounts

Use the prepared Generic manual-upload sources and the original five test identities. A **source** is ISC's configuration and collected account information for a managed system. An **identity** is ISC's record for a person. An **entitlement** is an individual access value.

We will use these two sources:

- **A:** `certlab-reports-csv`.
- **B:** `certlab-owner-reports-csv`.

A starts with three accounts and five permission holdings. B starts with four accounts and six holdings. A holding means one account having one permission.

| Account and person | A holdings | B holdings |
|---|---|---|
| certlab-account01 / certlab-employee01 | Read Reports, Export Reports | Read Reports, Export Reports |
| certlab-account02 / certlab-employee02 | Read Reports, Export Reports | Read Reports, Export Reports |
| certlab-account03 / certlab-employee03 | Read Reports | Read Reports |
| certlab-account04 / certlab-manager02 | No account | Read Reports |

The same account names on A and B belong to different source records. The two Export entitlements also use the same value, `certlab-report-export`, but they are separate objects.

Think of the instruction as “remove this permission from this account on this source.” Losing the source from that sentence can send you to the wrong place.

Use an authorized training administrator, reviewer `certlab-manager01` and the prepared `certlab-manager02` session. Employee02's recorded manager must be manager01. Both sources should name manager02 as owner. Verify working sign-in separately; importing a manager's people record does not establish a working user session.

Compare actual account data with the original files:

- `lab-data/baselineA/report_accounts.csv`.
- `lab-data/baselineB/owner_review_accounts.csv`.

If restoration is needed, use each source's complete private starting file, prepared against that source's downloaded template. This keeps the required columns and original values together. Resolve earlier outstanding removals before restoring access. Keep the people records and manager links unchanged.

These rights must remain individual entitlements. A role or access profile can package permissions; a lifecycle rule can assign access based on a person's employment state. Check that none independently requires these rights. Also check that no temporary review redirect sends manager01's work elsewhere. Those conditions would introduce a different review or removal problem.

## Set a clear removal requirement

For this exercise, employee02's bulk-export work has ended on **both** simulated applications. The person still needs to view reports on both.

The requested change is therefore:

| Source | Account | Remove | Keep |
|---|---|---|---|
| A | certlab-account02 / employee02 | Export Reports | Read Reports |
| B | certlab-account02 / employee02 | Export Reports | Read Reports |

All other accounts and permissions must remain unchanged.

This requirement concerns two separate existing holdings. Removing A Export does not remove B Export. Sharing a person, label and value does not join their permissions.

Record these supplied work facts in your private run notes. They give the reviewer a reason for each Revoke and give the operator a precise change to perform.

## Create only the two required review items

As administrator, open **Search > Certification Campaigns > New Campaign > Identities**. Under **Using a Search Query**, select **Create Campaign**, then **Specific Identities that I Select**.

Find the person with:

```text
name.exact:"certlab-employee02"
```

This asks for the exact identity name. Inspect the result and add only employee02 using **+ Add To Campaign**. Check **Added to campaign**, then choose **Certify Selected Identities**.

Use **Refine Access Items**. Select the Export Reports entitlement from A and the separate Export Reports entitlement from B, then use **+ Add to Campaign**. Check the added list, source and actual entitlement ID before continuing. Do not select Read or all access.

Name the configuration `certlab-012-two-source-removal-run01`. Set Manager as reviewer, a future deadline, the option to maintain undecided access and the available requirement for Revoke comments. If comments are required on every choice, follow that actual setting.

Use approved training notifications, no extra filter and no optional recommendations. Generate an immediate preview and save the template without a schedule.

Check the preview against both rows of the removal requirement. It must contain employee02's A Export and B Export, with the correct accounts and reviewer. Two rows with the wrong source would still be wrong.

Record the actual campaign and assigned certification IDs. When the preview is correct, select **Start Campaign**.

In manager01's session, open **Certifications > Active** and the assigned work. Inspect each item's source, account and permission. Record Revoke on both, explaining that bulk-export work ended on the named application while Read remains required.

Check the saved choices and comments, then use **Finish** to submit each actual assigned certification. This final submission is the reviewer's **sign-off**. A saved Revoke is still a draft until that submission is complete. Verify the resulting state and time.

## Open the actual removal tasks

In the task recipient's session, open **Task Manager**, or **My Tasks** on the dashboard. Open the relevant certification-removal work and expand **Show Details** where available.

The administrator can also inspect **Admin > Dashboard > Tasks**, using **To Do** for unfinished work.

Match every requested removal to:

- The finalized review and its decision.
- The source and account, using actual IDs where available.
- The entitlement value and requested action.
- The actual task ID and recipient.

Read the whole requested list. Do not assume two rejected holdings produce exactly two tasks, or that the task title tells you everything it contains.

The documented normal manual route assigns work to the source owner. Still inspect the actual recipient. Manager01 reviewing the access does not mean manager01 owns the removal work.

If a recipient cannot carry out the task, establish who can before proceeding. An administrator may use the unfinished task's **Actions > Reassign**, selecting the verified operator and a reason. Record the old and new recipient and reopen the task to check the assignment. Moving a removal task is different from moving a review that needs decisions.

Reassignment also does not grant application permissions. In this CSV exercise, a recipient may prepare the correct file while an authorized training administrator performs its upload. Record both actors. There is no need to give the reviewer broad administrator rights.

If no matching task appears, first check the sign-off and source removal path. Do not create a guessed replacement task or mark an unrelated one complete.

## Complete A first and leave B unchanged

Keep both original files. Make a new working copy of **A's complete private account file**. Preserve its required columns and all unrelated values.

Remove only the holding where:

```text
source: certlab-reports-csv
account: certlab-account02
employeeNumber: certlab-employee02
groups: certlab-report-export
```

In the supplied repeated-row layout, this removes the Export row for account02. Keep that account's Read row. Do not delete the account, delete the entitlement definition or disable the person.

The value comparison is:

`lab-data/baselineA/report_accounts_after_employee02_export_removal.csv`.

That file describes the expected values. Use your actual source template, including its extra required columns, for upload.

Before uploading, check the source named in the task and on the upload screen. Use the task's supported CSV upload step when present. Otherwise, the authorized administrator can open A under **Admin > Connections > Sources** and use **Account Management > Account Aggregation**.

Use one path and follow its collection through completion. **Aggregation** reads account data into ISC; it is how ISC learns the file's changed holdings. An accepted upload alone does not establish the collected result. If collection fails, inspect the source's aggregation history and error before continuing. Leave the task open while the required result is unverified.

Inspect A's actual accounts. Account02 must have Read and no Export. Account01 must still have both, and account03 must still have Read. All three accounts must remain correctly linked to their people.

Now inspect B without changing it. Account02 must still have both Read and Export. B must still have all four accounts and six holdings.

Your partial result is **A four holdings, B six holdings**. Only one of the two requested removals has been fulfilled.

## Decide what can be closed at this point

Return to the actual tasks and compare each task's full requested list with the verified result.

If A has its own task containing only the A removal, that task's work is now established. The recipient can select **Mark Complete** and inspect its completed state. The administrator's equivalent action is **Actions > Mark as Complete**.

B's unfinished task must remain open.

If any actual task includes more than the completed A change, do not close the whole task while any requested item remains unfinished. Record which item is complete and which remains in your run notes or available work comments. Do not assume an individual-item completion control exists.

This rule follows the work inside the task. It does not depend on a predicted number of tasks.

Marking work complete records a claim that its instructions were carried out. It is not the action that removes a real permission. The task guide also warns that completing before the changed file is collected can lead to another work item if the update does not follow in time. Keep the simple order: make the correct change, check its collected result, then close the fully fulfilled task.

## Finish B using B's own file

Make a new working copy of **B's complete private account file**. Remove only employee02/account02's `certlab-report-export` holding on B.

Compare the remaining values with:

`lab-data/baselineB/owner_review_accounts_after_employee02_export_removal.csv`.

B must retain four accounts and five holdings. In particular, keep manager02/account04's Read. Source ownership does not make that account disposable.

Upload through B's actual supported path and follow its aggregation through completion. Check the source before submitting. Reopen the account data and verify employee02 now has Read without Export.

Check the whole resulting set:

| Account | Final A | Final B |
|---|---|---|
| account01 / employee01 | Read + Export | Read + Export |
| account02 / employee02 | Read only | Read only |
| account03 / employee03 | Read only | Read only |
| account04 / manager02 | No account | Read only |

The full account names still use `certlab-`. Both sources keep their Read and Export entitlement definitions. Other people still use Export, so removing its definition is not the required account change.

Close each remaining task only after every requested change inside it has passed its checks. Inspect the recipient's **Completed** tab or the administrator's **Completed** filter. Keep actual task IDs and completion times.

Do not close other training tasks merely because they mention the same person or Export label.

## Try the wrong-file question before reading the answer

Someone says:

“A is correct now. Both sources have the same account names and Export value. Upload A's changed file to B and mark the rest complete.”

Would that produce the required B result? Identify a specific account or holding that makes the proposal wrong. Do not carry out the upload.

<details markdown="block">
<summary>Read the reasoning</summary>

A's changed file contains three accounts and four holdings. B needs four accounts and five holdings after its removal.

A has no manager02/account04 Read row. Copying its complete account set into B would therefore omit a required B account and holding. Source-specific schemas or required fields may differ too.

Even if an upload were accepted, acceptance would not establish that the right records were retained. The safe change starts with B's own complete template and removes only B employee02 Export.

A's successful change also says nothing about whether B's task was fulfilled. Check B itself and the actual task scope.

</details>

## Put the result and the records together

From **Admin > Certifications > Campaigns**, find this campaign and use **Actions > Download Reports**. Generate fresh decision/status, sign-off and remediation reports as available for the recorded campaign.

Compare them with the actual tasks and account observations. A report downloaded before the latest change will not update itself.

Your evidence should make this sequence understandable:

1. Employee02 held Export on A and B before the review.
2. The reviewer finalized two justified Revoke decisions.
3. The actual manual work identified the correct source accounts and rights.
4. A changed first while B Export remained outstanding.
5. B changed later; all required retained holdings remained.
6. Each task was closed only after its full requested work was established.

Keep actual IDs, actors, observations and times in private run notes. Save the original and changed source-bound file versions, collection results, task details and fresh reports.

A completed campaign describes review progress. A completed task records fulfillment. Collected account data shows what ISC currently knows. Here, the file is the simulated external account record; none of these proves an actual reporting application's current authorization.

If a report and account observation disagree, keep that mismatch visible. Check their source/account IDs, observation times, latest collection and task state before declaring completion.

## When you have a real manual target

The CSV exercise can finish without AD. A real manual-removal result needs a separately ready target where an authorized person can inspect and change the actual permission.

The planned AD fixture, called C here, uses source `certlab-ad-lab`, two ordinary accounts and three non-nested test security groups:

- `certlab-ad-e01`, linked to employee01, holds `certlab-ad-read` and `certlab-ad-exp-ok`.
- `certlab-ad-e02`, linked to employee02, holds `certlab-ad-read` and `certlab-ad-exp-fail`.

These are four scoped direct memberships. The group names are test labels; they do not prove report access in an application.

Run this variant only when the actual dedicated source has a supported, verified manual-fulfillment setup and can still collect AD membership data. Its ordinary automatic-write setup is not already a manual setup.

Changing a direct source to manual fulfillment can affect all provisioning on that source. Use separately prepared, approved source configuration with the relevant integration support. Do not disable provisioning, provoke a connector failure or guess an API edit to force this exercise.

Also verify private source/account/group bindings, the original four memberships, working reviewers, the actual task recipient and an authorized directory operator. No earlier member-write Deny, pending removal, nested group or automatic assignment should affect the test. If these conditions are missing, record the live variant as Not run.

For a ready manual target:

1. Prepare campaign `certlab-012-native-manual-run01` using employee01/02 and only C's ExpOK/ExpFail entitlement objects. Use Manager review, an immediate checked preview and an unscheduled template. The supplied need ends these two test memberships; both Read memberships remain required.
2. Have manager01 record and finalize both Revoke decisions. Inspect the actual manual tasks and match their full membership instructions before touching AD. An automatic operation instead of manual work means this variant's starting path is wrong.
3. As the authorized directory operator, open **Active Directory Users and Computers**, locate the verified ExpOK group, open **Properties > Members**, select only `certlab-ad-e01` and use **Remove**. Check the selected account and group before confirming.
4. Reopen the group on the recorded directory controller and inspect the actual membership. ExpOK must no longer contain e01. Read must still contain e01; e02 must still retain Read and ExpFail. Four scoped memberships have become three. If another controller is used, account for replication before interpreting a difference.
5. Collect the connected source's account data and inspect the matching ISC record. Apply the same task-scope rule: only fully fulfilled work can close.
6. Remove only `certlab-ad-e02` from the verified ExpFail group using the same checked group-member action. Observe it absent in AD, retain both Read memberships and collect C again. The final scoped set is two Read memberships. Do not upload a CSV to this connected source.
7. Reconcile target observations, collection, actual task completion and fresh reports. Record the operator who changed AD and the recipient who closed the task if they differ.

This demonstrates manual directory changes followed by ISC reconciliation. A connector's successful read does not turn the human's removal into an automated write.

## Restore the training starting state

Preserve the signed review, task history, partial/final observations and reports first. Resolve all outstanding CLB-012 removal work before adding the test rights back. Otherwise, an old instruction may still ask for their removal after reset.

Upload A's complete private original account file to A through **Account Management > Account Aggregation**. Follow the collection through successful completion, then inspect A's three accounts/five holdings in ISC.

Upload B's complete private original account file to B through its own **Account Aggregation** page. Follow that collection through completion, then inspect B's four accounts/six holdings, including manager02 Read. Employee02 must again have Read and Export on both sources. Restoring files on your computer alone does not update the collected accounts in ISC.

The restored data is preparation for another training run. It does not change the reason or final decisions in this completed historical review.

Keep signed history. Retire only this exercise's unused, unscheduled saved configurations after checking that no generation or work remains. Deleting a campaign is not a reversal of its tasks or account changes.

If you ran the live manual variant, resolve its tasks first. Have the authorized directory operator restore only e01 to ExpOK and e02 to ExpFail. Check four scoped memberships in AD, collect C and reconcile ISC. Keep both Read memberships and the approved source configuration; do not silently switch the source back to automatic fulfillment.

Before ending, explain which removal happened first, what was still unfinished at that time, why a particular task could or could not close, and which evidence proves the final account state. That explanation should follow the source and requested work all the way through.
