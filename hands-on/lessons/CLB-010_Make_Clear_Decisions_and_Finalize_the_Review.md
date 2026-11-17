# Make clear decisions and finalize the review

A reviewer can make the right choice on one item and still finish the review incorrectly. A copied reason may describe the wrong permission. A group action may include an exception. A saved decision may never be submitted.

Let's keep those steps connected: establish the need, record the choice and reason, check the saved work, then give final confirmation.

## Set up one mixed-access review

A **campaign** organizes access reviews. A **certification** is an assigned review inside the campaign, and a **review item** identifies access that needs a decision.

Use an authorized training administrator, reviewer `certlab-manager01` and the prepared source-owner session `certlab-manager02`. Both user sessions must already work. Keep them separate so the recorded actor is clear.

Use source A, `certlab-reports-csv`. A **source** holds the configuration and collected account data for a managed system. An **identity** is ISC's record for a person. An **account** is that person's record on the managed system. An **entitlement** is an individual access value, such as Read Reports.

Manager02 is A's **source owner**, the identity recorded as responsible for that source. Verify that owner reference before starting.

A **holding** means one account having one permission. A starts with three accounts and five holdings:

- employee01/account01: Read Reports and Export Reports.
- employee02/account02: Read Reports and Export Reports.
- employee03/account03: Read Reports.

The full names use the `certlab-` prefix.

This review includes only employee01 and employee02, each with A Read and Export. That gives four review holdings. Both employees' recorded manager must be manager01.

Employee03's Read is outside this campaign. Source B, `certlab-owner-reports-csv`, remains outside it too, with its original four accounts/six holdings.

Verify the original data from `lab-data/baselineA/report_accounts.csv` and `lab-data/baselineB/owner_review_accounts.csv` against actual ISC records. Use the existing private files that match the complete source templates if restoration is needed.

Check the account-to-identity links, original managers and absence of a certification redirect affecting this assignment. Preserve earlier evidence and resolve outstanding work before restoring changed training data.

Keep the rights as individual entitlements. An access profile packages permissions, and a role can require access for its assigned people. Neither should replace or automatically require these review items here.

## Read the first work confirmation

Read Reports represents viewing reports. Export Reports represents downloading them in bulk. Needing one does not automatically establish a need for the other.

**Approve** records that the reviewed access is appropriate. **Revoke** records that it should be removed. **Undecided** means no choice has been recorded.

The first choices are a **draft**: work saved before the reviewer's final confirmation. That final confirmation is **sign-off**. Until it happens, the assigned review is **unsigned**.

Use these supplied work facts for the first draft:

| Review item on A | Information available now | Justified draft choice |
|---|---|---|
| employee01 Read | Current duties require viewing reports. | Approve |
| employee02 Read | Current duties require viewing reports. | Approve |
| employee01 Export | The previous bulk-export task has ended, with no current export assignment in this first confirmation. | Revoke |
| employee02 Export | The current need has not yet been confirmed. | Leave undecided |

An unanswered question is different from confirmation that a need has ended. Do not turn “I have not checked” into a confident Approve or Revoke.

Record these supplied facts in your run notes. Later in this exercise, new work information will arrive before final submission. The changed choice must follow that new evidence.

## Prepare the four-item campaign

As administrator, open **Search > Certification Campaigns > New Campaign > Identities**. Under **Using a Search Query**, select **Create Campaign**, then **Specific Identities that I Select**.

Find the two people with:

```text
name.exact:"certlab-employee01" OR name.exact:"certlab-employee02"
```

`name.exact` matches the exact identity name; `OR` finds either person.

Inspect and add only the two intended identities using **+ Add To Campaign**. Check **Added to campaign**, then select **Certify Selected Identities**.

Choose **Refine Access Items**. Add only A's Read Reports and Export Reports entitlement objects. Their account values are `certlab-report-read` and `certlab-report-export`. Check the source on both before continuing.

Use an unused run name, such as `certlab-010-decisions-run01`, and record the actual generated campaign and saved-configuration IDs separately. Choose **Manager** as reviewer, a future due date and the option to maintain undecided access.

Set the available comment requirement so Revoke choices require a reason. If the offered setting requires comments on all choices, record that actual requirement and follow it. A required text box does not judge whether the explanation is true.

A **preview** is generated review work for the administrator to inspect before starting the campaign. A **template** saves the campaign's selections and settings for reuse.

Use approved training notifications, no extra campaign filter and no optional recommendations. Generate an immediate preview and save the template; keep that template unscheduled.

Inspect all four expected holdings and manager01's responsibility. Record actual campaign and certification IDs. Do not assume four items mean four assigned certifications.

When the preview matches the requirement, select **Start Campaign**.

## Decide which choices can be grouped

A **bulk decision** applies one action to several selected items. That is useful only when the action fits every selected item.

Use individual decisions for the normal run. The checks below also explain when a combined action would be appropriate if your actual reviewer screen offers it.

The two Read items currently have the same supported choice. Both people need report viewing.

That shared need does not justify approving every reporting permission. Employee01's first Export confirmation supports Revoke, while employee02's Export still needs clarification.

In manager01's session, open **Certifications > Active** and select the correct assigned review. Inspect the identities and their access details. The **Access Items** view can also show the people holding a selected permission.

If the actual reviewer screen offers a multi-item decision action, check exactly which items it would affect before submitting anything. Record its label, selected identities, source accounts and permission.

Check whether a selection applies to visible rows, a page or all matching results. Do not infer that from a filter or count alone, and do not assume it spans separate assigned certifications.

For a Read approval group, the selected set must contain only the two intended A Read holdings. Verify any shared comment applies to both and inspect the saved choice/comment on each afterward.

If no clear multi-item action is available, make these decisions individually and record that no bulk submission was performed. Do not substitute a different product's button or an administrator's campaign-completion action.

The selection reduces repeated clicks only when its scope is established. It does not replace checking each person's need.

## Record the first draft and useful reasons

Approve the two A Read holdings, individually or through the verified selection above.

A useful comment is:

“Current duties require report viewing; retain Read Reports.”

That explanation fits both Read items. It would not justify Export merely because the person works with reports.

Record employee01's draft Export Revoke using the first confirmation. Add a reason such as:

“The previous bulk-export task has ended, with no current export assignment confirmed. Report viewing remains required.”

Use the item's **More Options** control for comments where offered, and **Submit** to save the comment when required. Inspect the actual retained text on the correct item.

Leave employee02 Export undecided while clarification is outstanding.

You should now have three recorded choices: two Approve and one draft Revoke, with one item still undecided. No final reviewer submission has been made.

Keep the assigned reviews unsigned. Use the offered **Exit Certification** or **Exit Campaign** save/exit path. If a completion page appears for one assigned review, use **Save and return later**, not **Finish**.

Return to the work and verify its actual choices, comments and unsigned state. A saved choice should be established by reopening the record, not by remembering which icon you selected.

In the administrator session, inspect A's account data. Expect the original three accounts/five holdings at this draft checkpoint. The saved review choices record an assessment; carrying out the final removal comes later.

## Update the unsigned choice when the facts change

Before final submission, use the following supplied follow-up confirmation:

Employee01 has received a new authorized bulk-export assignment. Export is now required for that work.

Employee02's bulk-export work has ended. No continuing export need exists, but report viewing is still required.

These facts change employee01's draft conclusion and resolve employee02's unanswered question. Record the new confirmation before changing the decisions.

Here, the new assignment is a work responsibility. Account01 already holds Export; we are deciding whether that existing permission should remain. No new ISC role or permission is being granted.

The **Completed** tab inside an identity or access item lists decided items. That label alone does not establish that the assigned certification has been signed off.

Return to manager01's session and confirm that the affected review is still active and unsigned. Within the identity or access-item view, open the **Completed** tab, locate employee01's A Export choice and use **Revisit Decision**. This path corrects an unsigned choice; it does not establish a way to reopen signed work.

Change employee01 Export from Revoke to Approve. Update its explanation:

“A new authorized bulk-export assignment was confirmed before sign-off. Retain Export for that work; the earlier draft reflected the completed previous task.”

Save and reopen the item to verify both the new choice and explanation. Inspect available history so the changed reasoning remains understandable.

Now record employee02 Export as Revoke:

“Bulk-export work has ended and no continuing export need remains. Remove Export while retaining the separately reviewed Read permission.”

These are individual entitlements. Do not expect a future revocation-date option for them.

If the review is already signed off or the expected unsigned correction action is unavailable, stop this correction path and inspect the actual state. Do not use administrator completion or an unrelated interface as an assumed undo.

## Check the whole review before Finish

The final intended choices are:

| Item on A | Final choice | Current reason |
|---|---|---|
| employee01 Read | Approve | Report viewing remains required. |
| employee01 Export | Approve | The new authorized assignment requires bulk export. |
| employee02 Read | Approve | Report viewing remains required. |
| employee02 Export | Revoke | Bulk-export work has ended, while viewing remains needed. |

That is three Approve choices and one Revoke, with no undecided item.

Inspect every actual assigned certification. Check the right person, source, account, item, choice and retained reason. A copied comment about reading would not explain approving employee01's Export.

A common choice also does not require identical wording. The two approvals for employee01 arise from different capabilities and facts.

You may see **Acknowledge** for a role assigned automatically through membership criteria. A role is an access arrangement for its assigned people. Acknowledge records examination of that automatically controlled assignment; it is not a substitute for choosing Approve or Revoke on our individual Read/Export entitlements.

Do not create a role or change access models just to make that action appear.

When each assigned review is correct, complete its supported **Finish** flow in manager01's session. Inspect the actual final state and confirmation time. If the system requires reauthentication, complete that step through the approved reviewer sign-in process.

An unsuccessful final confirmation remains unfinished work. Check the message and permitted next action rather than claiming that saved choices prove sign-off.

In the administrator session, verify all intended reviewer work is finalized and inspect the campaign's resulting state. Do not use administrator bulk completion to conceal an unsigned review.

## Follow the rejected permission into actual manual work

After final submission, follow the required removal work for the rejected holding. **Remediation** is the work that carries out that change.

Inspect the actual manual task for employee02/account02/A Export. The expected source-owner recipient is manager02, but check the actual task and recipient.

In that recipient's **Task Manager** or **My Tasks**, open the full details and match source, account, permission and request. Read every change listed in the task. If no matching work is present, check the actual final confirmation and assignment rather than inventing a completed task.

Keep the original complete private A file. Make a new version and remove only employee02's Export row:

```csv
certlab-account02,certlab-account02,certlab-employee02,certlab-report-export
```

Preserve the full source-template columns in the actual working copy. Keep account02 Read, both account01 rights and employee03 Read. Keep both entitlement definitions and all B data.

The existing `report_accounts_after_employee02_export_removal.csv` supplies the expected four-column comparison. It is not an actual task result or a replacement for a different source template.

This file edit is the simulated application change. ISC has not automatically edited a real reporting account.

Upload the revised complete file through the supported task upload step, or have the authorized administrator use A's **Account Management > Account Aggregation**. **Aggregation** reads account data into ISC. Follow the operation through successful completion and inspect the accounts. If collection fails, inspect its error and keep fulfillment unresolved.

Expect A's three accounts/four holdings, with employee02 Export absent and every intended retained right present. B must remain at four accounts/six holdings.

When every change listed in the actual task has been carried out and verified, its recipient can select **Mark Complete** and inspect the completed state. Keep a task open if any listed work is still unfinished. Uploading data and completing a task are separate actions.

## Read the decision evidence and the account evidence together

Generate fresh available status, sign-off and remediation reports through the campaign's **Actions > Download Reports**.

Check **Decision Comments** for the reviewer's business reasons. A report's separate **Comments** field can describe status issues; it is not necessarily the decision justification.

Check the recorded **Decision Maker**, current **Reviewer**, choice and time. Those fields answer different questions. A new download is needed when you want the state after corrections; an older report can describe an earlier draft.

Keep four facts separate:

The choice was corrected and saved. The reviewer finalized it. The required manual work was completed truthfully. The collected account data shows the intended removal and retained permissions.

A completed review alone does not prove the account outcome. An updated CSV alone does not prove the reviewer signed off. Match the evidence to the fact being claimed.

## Would one common approval reason fit?

At the final stage, someone proposes selecting all four items and approving them with “Reporting access is required.”

Which item fails that proposed decision? Would changing only the comment fix the result?

<details markdown="block">
<summary>Compare your reasoning</summary>

Employee02 Export should be revoked under the confirmed facts. General report-viewing need does not justify bulk export.

The two Read holdings can share a justified Approve action. Employee01 Export is also approved, but because of its new authorized export assignment, not merely because reading is needed.

Changing the wording on an approval would leave employee02's excessive Export approved. The selected action must fit the facts too.

If an incorrect choice is still unsigned, correct it through the supported decision path and verify the saved result before Finish. If final submission already happened, inspect that actual state and follow the supported correction process instead of assuming this unsigned exercise can reopen it.

</details>

## Restore the training baseline after the work is resolved

Preserve the campaign, final choices/reasons, actual sign-offs, reports, task details and both file versions.

Resolve outstanding work that could apply the same removal again before restoring access. Upload the original complete private A file to A through **Account Management > Account Aggregation**. Follow successful collection, then verify A's three accounts/five holdings, B's four accounts/six holdings and the original identity/manager links.

Restoring employee02 Export is a training reset. It does not reverse the signed business decision or erase its history.

Keep the completed campaign evidence. If retiring its saved configuration, remove only this run's unused unscheduled template from **Saved/Scheduled**. Do not delete active work to avoid resolving a required change.

The retained explanation should connect the changed facts to the changed unsigned decision, the final submission and the actual CSV reconciliation result.
