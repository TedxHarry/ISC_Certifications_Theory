# Transfer review work and handle reviewer absence

A reviewer cannot finish before the deadline. Another suitable person is available, but how do you make sure the waiting review actually reaches them?

There are two jobs to consider. Existing review work needs a handover. Work created during the absence needs a rule telling ISC where to send it.

We'll check both using the same small Read Reports review.

## Identify the work and the people

A **campaign** organizes access reviews. A **certification** is an assigned review inside that campaign. Its **review items** identify the access being assessed.

The **subject** is the person whose access is reviewed. The **reviewer** makes the access decision. Moving responsibility to a new reviewer does not change the subject.

Use an authorized training administrator and two prepared reviewer sessions:

- `certlab-manager01`: the original reviewer.
- `certlab-manager02`: the suitable, available backup.

Both reviewers must be able to sign in through their approved training accounts. Imported CSV identities alone do not establish working logins. Keep their sessions separate from the administrator's session.

For every campaign in this exercise, include only:

| Subject | Source and account | Review item | Ordinary manager reviewer |
|---|---|---|---|
| `certlab-employee01` | `certlab-reports-csv` / `certlab-account01` | Read Reports | `certlab-manager01` |
| `certlab-employee02` | `certlab-reports-csv` / `certlab-account02` | Read Reports | `certlab-manager01` |

An **identity** is ISC's record for a person. An **account** is that person's record on a managed system. A **source** holds that system's configuration and collected accounts. An **entitlement** is an individual access value; here, Read Reports is `certlab-report-read`.

Read Reports allows viewing reports. Both employees still need that permission for their current work. Manager02 understands the need and can act as their backup reviewer. Neither selected item belongs to manager02, so this transfer does not ask the backup to review their own access.

A **holding** means one account having one permission. Keep source A at its original three accounts/five holdings: employee01 Read/Export, employee02 Read/Export and employee03 Read.

Keep B, `certlab-owner-reports-csv`, at four accounts/six holdings. None of its access belongs in this exercise. The original values are in `lab-data/baselineA/report_accounts.csv` and `lab-data/baselineB/owner_review_accounts.csv`, prepared in private copies matching the actual source templates.

Verify both employees' manager01 links and their A account associations. Their normal manager relationship stays with manager01 throughout this exercise. That relationship supplies the ordinary Manager reviewer when no absence instruction applies.

Keep Read as an individual entitlement, without a role or access profile changing the review item. An access profile packages permissions; a role can require access for its assigned people.

Preserve earlier evidence and resolve outstanding work before restoring any changed training baseline.

## Check what the absence rule would affect

**Work Reassignment** stores an instruction for work assigned during a date/time period. Here, **redirect** means sending new review work to the backup instead of the person who would normally receive it.

A review already waiting in manager01's list is existing work, even if it is unfinished. Adding the instruction does not make that earlier review newly assigned work.

Other work-type options cover access-request reviews and manual account-change tasks. For this run, use only **Certifications**, from manager01 to manager02.

The instruction is attached to manager01 and that work type. It is not limited to a campaign whose name starts with `certlab-009`. Check that manager01 has no unrelated certification work or scheduled generation during the practice period.

Inspect both managers' existing certification redirects. Start with none affecting this case. Adding another configuration for the same person and work type replaces the existing one, so do not overwrite an established absence arrangement.

Also check that manager02 does not redirect the received work onward. Otherwise, the final recipient may differ from the first backup you selected.

As administrator, inspect **Admin > Global > System Settings > Feature Settings > Other Features > Enable Work Reassignment**. Record its starting state.

The normal path below uses the feature already enabled. If it is disabled, establish a verified isolated training change before enabling it and saving. Enabling a site feature can make other saved configurations apply. If that effect has not been checked, leave the automatic part not ready; the existing-work handover can still be practised separately. A manual-only attempt does not complete the three-campaign comparison.

Record any approved feature change so it can be accounted for at the end. A broad site switch is not the way to end one person's absence cover.

## Create the work that already exists

We will keep three campaigns separate. The first exists before the absence instruction and needs a separate handover. The second is generated while the instruction applies. The third is generated after it is removed. All three review the same two A Read holdings.

Use unused run names and retain each generated campaign ID separately from its saved configuration. Keep earlier attempts' objects and evidence separate.

Prepare the first campaign as administrator.

Open **Search > Certification Campaigns > New Campaign > Identities**. Under **Using a Search Query**, select **Create Campaign**, then **Specific Identities that I Select**.

Run:

```text
name.exact:"certlab-employee01" OR name.exact:"certlab-employee02"
```

The query finds either exact identity name. Inspect both records, add only those two with **+ Add To Campaign**, check **Added to campaign**, then select **Certify Selected Identities**.

Choose **Refine Access Items**. Add only Read Reports from A, verify its actual source and entitlement object, then continue.

Name this campaign configuration `certlab-009-existing-run01`. Select **Manager** as reviewer, a future due date and the option to maintain undecided access. An undecided item has no decision.

A **template** saves the selections and settings for generating a campaign. It is a separate record from the campaign it produces.

Use approved training notifications, no extra campaign filter and no optional recommendations. Choose **Generate a preview now and save as a template**. Review the summary, generate the preview and keep the saved configuration unscheduled. Record its template ID separately from the generated campaign ID.

Check the two required Read holdings and manager01 assignment. Record actual campaign and certification IDs. Inspect the grouping rather than assume that two holdings produce one or two certifications.

When the contents match, select **Start Campaign**.

In manager01's session, open **Certifications > Active** and inspect the assigned work. Approve employee01's A Read based on the continuing need. **Approve** records that the access is appropriate.

Add a short reason, such as “Report viewing remains required for current work.” Save and exit through the supported save/exit control. Reopen the work to verify the saved choice and comment.

Leave employee02 undecided. Do not select **Finish** or sign off on either review, even if the interface offers a completion page after one choice.

**Sign-off** is the reviewer's final submission. Saving a choice and signing off are different events. Record the actual unsigned state before proceeding.

## Arrange cover for work created during the absence

In manager01's session, open the **User** menu, then **Preferences > Work Reassignment**.

Select **Certifications** as the work type and manager02 in **Assign To**. Check the exact identity.

Use **Start Now** where offered, or an explicit start date/time accepted by the form. Set a finite end date/time that allows the practice to finish. Leave **No end date** off.

Select the intended **Time Zone** and read it back. The initial default comes from the browser; do not assume a displayed clock time uses another administrator's local zone.

Select **Add Reassignment**. Inspect the saved row in **Scheduled Reassignments**, including work type, recipient, start, end and zone. Record it privately.

Before creating new work, establish that the saved period is currently in effect. If its start is still in the future, the automatic test is not ready yet.

An administrator can also configure a person's Work Reassignment from their identity record. The self-service route above is the one used for this run; do not combine its labels with a different screen.

Return to the existing campaign. Its already assigned work should still belong to manager01. Check that actual assignment. Saving a future-work instruction did not, by itself, hand over that earlier review.

## Generate work while the instruction applies

As administrator, create `certlab-009-during-run01` with the same two subjects, only A Read, Manager reviewer and the same remaining settings.

Use a new immediate preview and unscheduled template. Do not select manager02 directly as reviewer; the ordinary Manager choice must still lead to manager01 for this test.

Keep the saved period in effect while generating, inspecting and starting this during-period campaign. Record both generation and activation times against the saved time zone. A run outside that period does not test the intended active-period case.

Inspect the actual assigned reviewer in the preview before activation.

The expected result is manager02 receiving the two Read holdings through automatic work reassignment. Check the scope before starting the campaign. If the assignment differs, investigate the saved work type, active times/zone, original manager assignment and any other redirect before proceeding.

Start the checked campaign and verify manager02 can open its intended work in **Certifications > Active**. Leave its items undecided for now.

Check both campaigns: new work has reached manager02, while the earlier unsigned work remains with manager01. One successful new assignment does not establish cover for the earlier work.

## Hand over the existing unsigned work

Now move the existing campaign's waiting reviews to manager02.

As administrator, open **Search > Certification Campaigns > View previewed/Active > Certification Campaigns**. Select **Cards**, then the relevant **Active** campaign.

Check the exact `certlab-009-existing-run01` campaign and select **Details**.

Inspect the selected review rows and their complete contents. Select only the unsigned work covering the two intended A Read holdings, then **Reassign**. If the actual grouping requires separate actions, inspect and move each eligible review rather than assume one row covers everything.

Choose the actual manager02 identity as recipient. Add a useful reason and your contact identity, for example:

“Manager01 is unavailable for this review period. Manager02 will finish the two employee A Read reviews. Contact the training campaign administrator for the handover.”

Check the selected scope and recipient, then submit **Reassign**.

The administrative reassignment action works on preview or started campaigns whose reviews are unsigned. A signed-off certification cannot be moved through this action. It also blocks moving a certification containing the proposed recipient's own access.

A different API or screen is not a reason to bypass those conditions.

Follow the operation to its result and inspect the current assignment before repeating an uncertain request. A missing confirmation is not proof that the first attempt did nothing.

## Check what arrived, including earlier choices

In manager02's session, open the transferred existing work. Match both intended subjects, A accounts and Read permissions. Record the resulting certification IDs; do not assume they stayed the same.

Check employee01's previously saved choice and comment, employee02's decision state and available history. Record what the actual action retained or changed. Do not assume every reassignment route preserves or resets choices identically.

The **Reviewer** identifies who is currently responsible for the assigned review. The **Decision Maker** identifies whose decision is recorded for a particular item.

If the earlier approval remains, manager01 may still be recorded as its Decision Maker. Manager02 can be the current Reviewer without becoming the author of that earlier decision.

Do not change a valid decision merely to make the new reviewer's name appear on it. If a choice needs a fresh decision, manager02 must assess the access and follow the actual supported state.

Confirm manager01 is no longer responsible for this selected active work. Historical visibility and current responsibility are different checks.

For the automatic redirect, manager01 can inspect **Preferences > Work Reassignment > Reassignment History**. Compare the recorded work and time with the actual current assignment.

The history's **Assignee** field shows the first configured recipient, not every later redirect in a chain. That is another reason we excluded outgoing backup redirects from this normal case.

## End the instruction and inspect a later review

In manager01's **Scheduled Reassignments**, delete only this lab's Certifications row. Confirm the recipient and period before selecting **Delete**. Keep other work types and other people's settings unchanged.

Record the deletion time. Verify the two earlier campaigns still belong to manager02. Deleting the instruction does not return work already assigned to that backup. Reaching the end time has the same boundary for previously redirected work.

Now create `certlab-009-after-run01` with the same two-person/A Read requirement, Manager reviewer and no direct backup assignment.

Generate a fresh preview after deletion. Check its assignment to manager01, then start the checked campaign and verify manager01 can open it.

The expected assignment pattern is:

| Campaign | How its work reaches the reviewer | Reviewer after the instruction is deleted |
|---|---|---|
| Existing | Originally manager01, then separately handed over | manager02 |
| During | Created while manager01's Certifications redirect applied | manager02 |
| After | Created after deletion, using the unchanged manager links | manager01 |

Record the actual result for each campaign. A different result remains an unresolved check, not a reason to rewrite the manager CSV until the table appears to match.

The three campaigns each contain two review occurrences. Across them, that is six occurrences of the same two underlying Read holdings. It is not six different permissions on the accounts.

## Finish the reviews with the right people

Both employees still need Read. This exercise has no justified removal decision.

Manager02 completes the existing and during-period campaigns. Manager01 completes the after-deletion campaign.

For each actual assigned certification, inspect both current need and any saved choice. Approve the Read items that still require a decision, verify comments and complete the supported **Finish** flow. Do not assume finishing one certification finalizes another.

Check every review's actual sign-off state and each campaign's resulting state. The normal fully signed path can move the campaign to Completed. Do not substitute administrator bulk completion for a reviewer who has not finalized.

Use the campaign's **Actions > Download Reports** to generate fresh available status and sign-off reports. Match current reviewer, actual decision maker, decisions and final confirmation with the handover records. Check the displayed time zone when comparing report times with the absence window.

There should be no Revoke choice or resulting access-removal work for this planned outcome. Investigate any such work rather than treating reassignment as its explanation.

Check A still has five holdings and B still has six. Neither handover nor an absence rule was an instruction to alter those permissions.

## Choose the amount of work that should move

A whole assigned review can include several people and permissions. Moving it is appropriate only when the entire selected contents should move.

When the requirement covers a narrower part, the supported reviewer route offers selections by identity or access item: **Certifications > Active > the review**.

Selecting an identity and **Reassign** can move that person's selected review work. Selecting item rows through **More Options > Reassign** targets those items. Check the selection, enter the recipient and reason, then use the offered **Reassign Decision** action.

Those scopes are different. Do not perform another transfer on this lab simply to try every button. Choose the supported action that matches the actual handover requirement.

If the reviewer has left permanently, inventory unfinished reviews and also check the manager or owner records used for future assignment. A temporary redirect does not correct those responsibility records.

## Did deleting the rule finish the handover?

Suppose the during-period campaign reached manager02. The redirect was then deleted.

Someone says, “Manager01 is back, so both earlier campaigns must have returned to manager01, and manager02 must now be the decision maker for the approval saved before transfer.”

Which records would you use to check those claims?

<details markdown="block">
<summary>Compare your reasoning</summary>

Deleting the redirect stops it from applying to newly assigned work. It does not return existing reviews. Check the current assignment of each earlier campaign.

The first campaign only left manager01 because a separate existing-work transfer was performed. Without that action, saving future absence cover would have left that earlier work with manager01.

Reviewer responsibility and decision authorship are also separate. Inspect the actual choice/history and a fresh report. If the approval saved by manager01 remains, its recorded decision maker can still be manager01 even though manager02 now holds the review.

Neither a saved setting nor an email establishes that someone finished the assessment. Inspect the actual signed-off work.

</details>

## Leave no temporary absence instruction behind

Preserve the three campaigns' completed histories, actual reviewer checks, before/after choice evidence, configuration/deletion times, relevant history and fresh reports.

Verify that this lab's Certifications redirect is absent and both managers' original assignment settings remain as recorded. Earlier redirected reviews are accounted for by their final sign-off; they do not need to be reassigned back merely to tidy a list.

Keep the completed campaign evidence. If retiring the unused saved configurations, remove only these three unscheduled 009 templates from **Saved/Scheduled**. Do not delete active reviews as a substitute for finishing or handing them over.

If you changed the site feature, compare its initial state and current dependencies before restoration. Do not disable it while another person's legitimate configuration now depends on it. Record and hand over any unresolved setting or work instead of reporting a complete reset.

Verify the original manager links, account associations and A five/B six holdings. No account-file reset is needed when the inputs stayed unchanged.

The handover is established by the actual recipient being able to continue the intended work, the earlier decisions remaining explainable and every outstanding review having an accountable owner.
