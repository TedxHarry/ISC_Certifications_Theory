# Monitor campaign progress and handle unfinished work

A campaign has five items. Four choices have been entered. Is the review almost finished?

Let's check who has actually submitted their work. A saved choice, a finished review and a completed access removal answer different questions. A daily progress check needs to keep them separate.

## Give each progress number a meaning

A **campaign** organizes access reviews. A **certification** is an assigned review inside that campaign. A **review item** identifies access that needs a decision.

**Approve** records that access is appropriate. **Revoke** records that it should be removed. An **undecided** item has no recorded choice.

A reviewer can save choices and return later. Those saved choices are a **draft** until the reviewer makes the final submission, called **sign-off**, through **Finish**. An **unsigned** review has not received that final confirmation, even if it contains saved choices.

After a finalized Revoke, there is another job: carry out the removal. **Remediation** is that fulfillment work. It may still be unfinished after the review is complete.

When you see a count or percentage, first ask what it is counting. One reviewer may have several items to decide before finishing one assigned review. Counting that person's choices is different from counting their submitted review. Neither count tells you whether a rejected permission has been removed.

## Start with five known holdings and two reviewers

An **identity** is ISC's record for the person. An **account** is the record in the managed system. A **source** holds ISC's configuration and collected account data for that system.

An **entitlement** represents an individual right. Here, Read Reports uses `certlab-report-read`, and Export Reports uses `certlab-report-export`. A **holding** means one account having one of those rights. An account with Read and Export therefore has two holdings.

Use source A, `certlab-reports-csv`, with these permissions recorded individually:

| Person | A account | Existing permissions | Manager reviewer |
|---|---|---|---|
| certlab-employee01 | certlab-account01 | Read Reports and Export Reports | certlab-manager01 |
| certlab-employee02 | certlab-account02 | Read Reports and Export Reports | certlab-manager01 |
| certlab-employee03 | certlab-account03 | Read Reports | certlab-manager02 |

A must have three accounts and five holdings. Source B, `certlab-owner-reports-csv`, must keep its original four accounts and six holdings.

Use the three employee identities and two manager identities shown by the training setup. Check the manager links in the table and both managers' ability to sign in. Imported people records alone do not establish working reviewer sessions.

A's **source owner**, the person responsible for that source in ISC, should be `certlab-manager02`. The training administrator must be able to inspect campaign/reviewer records, reports and manual tasks, and perform the permitted source upload.

If restoration is needed, resolve earlier outstanding work first. Use the complete private starting files prepared against each source's actual template. A's original values are in `lab-data/baselineA/report_accounts.csv`; B's are in `lab-data/baselineB/owner_review_accounts.csv`.

Keep the rights as individual entitlements rather than bundled review items. Check that earlier test profiles or roles do not change what is being reviewed, and that no reassignment setting sends the work to someone else. Inspect the actual account-to-person links and manager relationships before creating the campaign.

## Create the campaign with a known notification setting

Open **Search > Certification Campaigns > New Campaign > Identities**. Under **Using a Search Query**, select **Create Campaign**, then **Specific Identities that I Select**.

Find the three people:

```text
name.exact:"certlab-employee01" OR name.exact:"certlab-employee02" OR name.exact:"certlab-employee03"
```

The query finds those exact identity names. Inspect and add only the three intended results using **+ Add To Campaign**. Check **Added to campaign**, then choose **Certify Selected Identities**.

Choose **Refine Access Items**. Select only A Read and A Export, add them to the campaign and inspect the added list. B's matching labels are not the same access objects.

Name the configuration `certlab-014-progress-run01`. If a supplied run name already exists, use an unused run suffix and record it; preserve earlier history. Choose **Manager** so the recorded manager of each employee receives the review.

The **deadline** is the date by which reviewers should finish. Choose a permitted future date with enough time for this exercise, and record its time zone.

Select the option to maintain undecided access when completing the campaign. If an administrator closes the campaign without a decision on an item, this setting keeps that access. Keeping access this way does not mean the manager reviewed and approved it. Set the available requirement for Revoke comments, following an all-comments requirement if that is what the tenant offers.

For this campaign only, turn notification emails **off**. This gives us a known cause to examine when a reviewer says no email arrived. Do not change tenant-wide email settings or reviewer addresses.

Use no extra filter or optional recommendations. A saved **template** stores the campaign settings. A **preview** is the generated review work you inspect before releasing it to reviewers. Choose the option to generate a preview now and save it as a template, without a future schedule. Record the template and generated campaign references separately.

Verify all five holdings from the starting table. Manager01 must be responsible for employee01/02's four items; manager02 must be responsible for employee03's Read. Inspect the actual certification IDs and grouping. Five items do not imply five certifications.

When the preview is correct, select **Start Campaign**. Record the actual activation time.

## Leave a deliberate partial state

Use these supplied work facts:

- Employee01 still needs both Read and Export.
- All three employees still need Read.
- Employee02's current Export need has not yet been confirmed.

In manager01's **Certifications > Active** session, open the assigned work. Record Approve for employee01 Read, employee01 Export and employee02 Read.

Leave employee02 Export undecided. There is no confirmed answer yet, so do not invent a choice.

Save and exit without using **Finish** on any of manager01's assigned certifications. Reopen the work to verify the three saved choices and the unanswered item.

Now use manager02's session. Approve employee03 Read, check its reason and finish all of manager02's actual assigned work for this campaign. Verify final submission.

You have now created a useful difference:

- Four choices have been entered across the campaign.
- One item is undecided.
- Only employee03's Read belongs to a finalized review.
- Manager01's three recorded choices remain unsigned.

Manager01's three approvals count as entered choices, but saving them did not finalize those reviews. Manager02's one approval has been submitted. That is why four choices are recorded while only one item belongs to finalized work. The interface may count whole certifications rather than individual items, so inspect what its percentage measures.

## Inspect progress as the administrator

Open **Admin > Certifications > Campaigns** and the named campaign.

Inspect the reviewer details. In Table view, select the campaign name to open its reviewers. In Cards view, use the campaign's **Details** action.

Locate manager01 and manager02 by their actual identities, then inspect their assigned certifications and states. Keep the campaign ID, reviewer, certification ID and affected items together.

Generate fresh available reports through the campaign's **Actions > Download Reports**:

- **Campaign Composition Report:** check the saved deadline, notification setting and treatment of undecided access.
- **Campaign Status Report:** inspect item decisions, current reviewer, decision maker and any status comments.
- **Certification Sign Off Report:** inspect who submitted which review and the recorded sign-off time.

In the status report, **Decision Made** is an item status such as Open, Complete or Error. The separate **Decision** column records the choice, such as Approve or Revoke. Complete in the first column does not, by itself, establish that the reviewer submitted the whole certification. Check the sign-off report's **Sign Off Date** and the corresponding review state as well.

In the sign-off report, **Owner** means the person assigned the review. That is a different responsibility from owning source A. After administrative completion, inspect who is actually recorded as **Reviewer**.

Compare the administrator's view with the saved work you inspected in each reviewer session. Record how the actual report represents unsigned choices; do not assume every screen exposes drafts in the same way.

If a count differs, check that you are looking at the same campaign, people and items. Check what the field counts and when the report was generated. Do not change access just to make a dashboard match your calculation.

Keep source/account identifiers with item observations. Report times may use GMT while your notes use local time. Record each time zone and compare the times in the same zone before deciding that events happened in the wrong order.

## Choose the next action from the unfinished work

At this checkpoint, manager01 needs two things. First, a business answer about employee02 Export. Then final submission of the assigned reviews.

Manager02 has already submitted the required Read review. Asking manager02 to repeat it would not resolve manager01's unfinished work.

Your next-action note can be brief:

“Manager01: confirm employee02's Export need, record the justified choice, then finalize all assigned work in this campaign. Manager02's assigned work is signed off.”

Do not use administrator completion to skip the deliberate unsigned state. Have the actual reviewer finish it through the normal path. If administrative completion is needed for a different real case containing unsigned choices, establish the supported handling for that campaign before acting.

## Investigate the missing email without confusing it with assignment

In manager01's session, confirm that the assigned active work is visible. Then return to the administrator's session and inspect the campaign's saved notification setting.

Emails were turned off for this campaign. The absence of an automatic email therefore fits the configuration. It does not prove the review was never assigned.

With campaign emails enabled, current guidance describes an activation email and reminders every seven days until the reviewer signs off, the certification expires or an administrator completes the campaign. Check the assigned work directly rather than waiting for a reminder to establish that it exists.

For a manual follow-up, use the campaign reviewer's **Email** action. In Table view, it is under **Actions > Email** for that reviewer; Cards view provides an Email button.

This opens the computer's default email application with the recipient filled in. It is not an ISC button that silently resends a system notification.

Inspect the intended training address and prepare a draft naming this campaign, its actual deadline, the missing confirmation and the need to finish saved work. Close the draft without sending it for this exercise.

If the mail application does not open, inspect the local email-handler setup. That result alone says nothing about whether ISC assigned the certification.

If the review itself is missing, check the signed-in identity, campaign activation, actual recipient and any reassignment. That is a different investigation from missing mail.

## Obtain the answer and finish the remaining reviews

Use this supplied follow-up confirmation: employee02 no longer needs bulk export. Read remains required.

In manager01's session, record Revoke on employee02 A Export with a reason explaining that change and the need to retain Read. Recheck the other three justified approvals.

Before final submission, you have five item choices but still only employee03's item in finalized work. After manager01 finishes every actual assigned certification, all five items should belong to submitted reviews.

Keep the item counts separate:

| Checkpoint | Choices entered | Undecided items | Items in finalized reviews |
|---|---|---|---|
| First partial checkpoint | 4 | 1 | 1 |
| Employee02 Export decided, manager01 still unsigned | 5 | 0 | 1 |
| All reviewers have finished | 5 | 0 | 5 |

These are your own counts from the known items and verified submissions. Read any platform percentage according to the unit that platform field uses.

Generate fresh status and sign-off evidence. Confirm the final four Approve/one Revoke, both reviewers' completed responsibilities and the actual campaign state.

A campaign leaving the active-review list does not, by itself, prove that the rejected Export permission has already been removed.

## Keep the removal on a separate list

Return to the administrator's session and inspect the actual removal work for employee02, A account02 and Export. Manager02 has finished their assigned review, but also owns source A. Deciding whether access is needed and carrying out a removal are separate responsibilities. Inspect who actually received the task.

The recipient can use **Task Manager**; the administrator can use **Admin > Dashboard > Tasks**, with **To Do** for unfinished work. A **manual task** instructs an operator to make a change that ISC cannot write to this file-based source itself.

Record the complete task scope and actual recipient. Do not infer the number of tasks from the one rejected holding.

Before fulfillment, A may still show five holdings. You can therefore have completed reviewer work and an unfinished removal at the same time.

For this CSV source, make the simulated external change in a new copy of A's complete private account file. Remove only employee02/account02's Export holding. Preserve its Read and all other account values.

Use `lab-data/baselineA/report_accounts_after_employee02_export_removal.csv` as a value comparison, keeping the actual source template's required columns in the upload file.

Upload through the task's supported file step. Alternatively, the authorized administrator can open A under **Admin > Connections > Sources**, then use **Account Management > Account Aggregation**. **Aggregation** reads the changed account information into ISC. Follow it through successful completion and inspect the current accounts before closing the task. If collection fails, inspect its history/error and leave fulfillment unresolved.

Verify A's three accounts/four holdings: employee01 Read+Export, employee02 Read only and employee03 Read only. B must still have four accounts/six holdings.

The actual recipient can now use **Mark Complete** for fully fulfilled work and inspect its Completed state. An administrator's equivalent is **Actions > Mark as Complete**. Do not close a task whose requested work remains incomplete.

Regenerate available remediation evidence after the change. If that report is not offered in the current campaign state, record its availability and use the actual task and account evidence. Do not force another completion action just to obtain a report. A remediation status of Finished can reflect a manual task being marked complete. It is not independent proof that a real application permission changed.

Here, the revised file and collected account record prove the simulated result. A real application's outcome needs observation on that application.

Preserve the review, task and checkpoint records. Resolve outstanding work, then restore A's complete private original file and run aggregation. Follow it through successful completion and verify the original account values: employee01 Read+Export, employee02 Read+Export and employee03 Read. Check A five/B six before starting the separate deadline exercise.

Keep the signed campaign history. In **Search > Certification Campaigns > Saved/Scheduled**, remove only the now-unneeded, unscheduled template named `certlab-014-progress-run01`, or the unused run name you recorded. Match its saved reference and confirm no generation remains before using its delete action. This removes the reusable settings, not the completed campaign whose history you are preserving.

## Practise one post-deadline completion separately

After the deadline, a review may still need attention. Check its actual state: reaching the date and an administrator deliberately completing unfinished work are separate events.

Use a separate one-item campaign so the earlier unsigned choices cannot be confused with this test.

After the main baseline is restored, create `certlab-014-overdue-maintain-run01` through the same identity selection flow, using:

```text
name.exact:"certlab-employee01"
```

Add only employee01 and refine access to only A Read. Choose Manager, notification emails off and the option to maintain undecided access when completing the campaign.

Use a suitable permitted future deadline and record its actual value/time zone. Generate an immediate one-item preview, keep the saved template unscheduled, verify manager01's responsibility and start the campaign.

Leave this item completely unanswered. Do not save Approve or Revoke, and do not sign off.

This part needs the actual configured deadline to pass. You can finish the normal monitoring work while that date is still ahead. Record the deadline part as Not run until its required condition and actions have actually occurred.

Do not change the computer clock, backdate an unsupported field or alter a tenant scheduler to manufacture an overdue result.

## Close the blank overdue review and record why

Once the recorded deadline has passed, inspect the campaign's actual state and available actions. Recheck the one-item scope, maintain setting and absence of any reviewer choice or sign-off.

For this training case, maintain the still-required Read while closing the overdue review. Record the administrator's reason, manager01 as the responsible follow-up reviewer and the need to obtain a proper later review.

Keeping access is not evidence that manager01 completed the review.

For the documented maintain-at-completion configuration, use the campaign's **Actions > Complete**. Read the confirmation before submitting it. It must maintain the one intended undecided item, not revoke access or complete another campaign.

Confirm through **Complete Campaign** only when that scope and effect are correct.

A configuration allowing a choice may instead offer **Complete & Maintain Access** or **Complete & Revoke Access**. Those alternatives follow the saved campaign configuration. Our exercise uses maintenance; it does not test blanket revocation.

If the campaign is already closed, or the expected supported control is absent, inspect and record the actual state and actor before doing anything else. Do not invent a replacement control or count an unperformed administrative action as passed.

Generate fresh composition, status and sign-off reports as available. Inspect how the actual administrator, owner, maintained-access outcome and time are recorded. Do not relabel an administrative outcome as the reviewer's own choice.

Check that employee01 Read remains, A still has five holdings and B still has six. No removal is justified by this maintenance action. Investigate any unexpected work before declaring the exercise resolved.

This review had no saved choices. Do not use its outcome to predict what happens when an administrator completes a different review containing saved but unsigned choices.

Keep the historical records, actual deadline observation and the administrator's reason. After all work is accounted for, remove only the now-unneeded, unscheduled `certlab-014-overdue-maintain-run01` template, or its recorded replacement name, from **Saved/Scheduled**. Match the saved reference and check no generation remains; preserve the completed campaign. No account-file change is needed for the expected maintained-access result.

## Decide what a progress claim actually proves

Suppose someone says:

“Every reviewer has finished. We can report that every rejected permission has been removed.”

What else do you need to check?

<details markdown="block">
<summary>Read the reasoning</summary>

Reviewer submission finishes the review decisions. The removal list may still contain manual tasks or automatic operations that are unfinished or failed.

Match each finalized rejection to its actual work and current account result. In this exercise, check employee02 A Export absent and all required Read retained after the simulated file change and collection.

For a live system, inspect that system as well. A finished review or closed manual task alone cannot prove its current authorization.

</details>

At the end, your progress explanation should name the remaining work, the person responsible, the evidence needed and the next action. “The campaign is 80% complete” is useful only after you know what that percentage is counting.
