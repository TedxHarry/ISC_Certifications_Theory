# Correct or retire a campaign without losing the truth

You notice a problem in a campaign. Should you edit it, replace it or delete it?

Start by checking what has already happened. A preview that nobody has received is different from a review with saved choices. A signed decision may already have started removal work.

Let's work through those states without treating Delete as an Undo button.

## Find the object before choosing the action

A **campaign** organizes access reviews. A **certification** is an assigned review inside it. A **preview** lets an administrator inspect generated review content before starting the campaign.

A **saved template** holds the configuration for generating a campaign. It is separate from a generated preview. A schedule can generate another preview later.

Each review item needs a choice. **Approve** records that the access should be kept; **Revoke** records that it should be removed.

A reviewer can save those choices as a **draft** and return later. The review is **unsigned** until the reviewer makes the final submission, called **sign-off**, through **Finish**. **Remediation** is the work that carries out a finalized removal decision.

These are the distinctions we need:

| What exists now | What to establish before acting |
|---|---|
| Saved template or future generation | Which configuration/schedule it controls and whether generation is pending. |
| Unstarted preview | Exact scope, no activation, no choices/sign-off and no resulting removal work. |
| Active unsigned review | Current choices, actual reviewer and whether final submission has occurred. |
| Signed review | Historical decision, final actor/time and any resulting work. |
| Task or account operation | Exact requested action and whether it is pending, completed or failed. |

Do not choose an action from the campaign name alone. Record the actual object IDs and state. Use identifiers supplied by the record, report or actual page address. If a field is not exposed, keep the available reference and mark the missing identifier rather than inventing one.

## Use the known accounts and a clear initial need

An **identity** is ISC's record for a person. An **account** is the record in a managed system. A **source** holds ISC's configuration and collected account information for that system.

An **entitlement** represents a specific right. Our two application sources are:

- A: `certlab-reports-csv`.
- B: `certlab-owner-reports-csv`.

Use A's original three accounts/five holdings and B's original four accounts/six holdings. A holding means one account having one permission. On A, employee01 and employee02 each have Read+Export, while employee03 has Read only: two plus two plus one gives five holdings.

Employee02, `certlab-employee02`, has `certlab-account02` on each source. Both accounts hold Read and Export, but they are different source records.

Read uses `certlab-report-read`; Export uses `certlab-report-export`. The same value on B does not make it the A entitlement.

Use the three employee identities and two manager identities from the training setup, with correct manager links and working manager01/02 sign-ins. Importing people records does not by itself establish reviewer sign-ins. Employee02's manager must be `certlab-manager01`.

A **source owner** is the person responsible for the source in ISC. Both sources should be owned by `certlab-manager02`. This responsibility is separate from manager01's job of deciding whether employee02 still needs the access.

The authorized administrator needs campaign creation/deletion, report inspection and the permitted source-upload actions. Keep the selected rights as individual entitlements, without an earlier temporary profile, role, lifecycle grant or review redirect changing the case.

Profiles and roles can package or require permissions. A lifecycle grant comes from a configured business state, such as Active; a review redirect can move review responsibility to another person. Check that earlier exercises have not left those conditions affecting this case.

Resolve earlier outstanding work before restoring a baseline. Use complete private source-template files with values from `lab-data/baselineA/report_accounts.csv` and `lab-data/baselineB/owner_review_accounts.csv`. Inspect the resulting account and identity links.

For this exercise's initial review, employee02 still needs **both A Read and A Export**. B is outside the required review. Later, after sign-off, new work information will change the Export need.

That timing matters. We are not asking the reviewer to sign a choice they know is wrong.

Use unused run names for the three configurations below. If a supplied name already exists, choose an unused run suffix and record it. Keep each saved-template reference separate from its generated campaign reference, including when you remove the unused objects later.

## Prepare a wrong preview and keep it unstarted

Open **Search > Certification Campaigns > New Campaign > Identities**. Under **Using a Search Query**, choose **Create Campaign**, then **Specific Identities that I Select**.

Find:

```text
name.exact:"certlab-employee02"
```

Inspect and add only employee02 using **+ Add To Campaign**. Check the added list and choose **Certify Selected Identities**.

For this controlled preview mistake, use **Refine Access Items** and add Read and Export from **both A and B**. Check that you have the four distinct entitlement objects.

Name the configuration `certlab-016-wrong-preview-run01`. Choose **Manager** so employee02's recorded manager receives the review when the campaign starts. Use a permitted future deadline, the date by which the reviewer should finish.

Choose to maintain undecided access when completing the campaign. Under that setting, an item left without a decision keeps its access; that does not mean the manager reviewed and approved it. Require Revoke comments, or all comments if that is the offered rule.

Turn this campaign's emails off. Use no extra filter or optional recommendations. Choose to generate the preview now and save it as a template, without a future schedule.

Do not select **Start Campaign**.

Inspect the expected four holdings:

| Preview | Employee02 holdings |
|---|---|
| Wrong | A Read, A Export, B Read, B Export |
| Required | A Read, A Export only |

The mistake is the two B holdings. Employee02 has two rights on A and two on B, so selecting both sources produces four items. We only need the two A items. Correcting that selection changes what we ask the reviewer to assess; employee02's B permissions should stay as they are.

Record the actual wrong preview and saved-template IDs, their states and the four source-specific items. Deleting a campaign also deletes its reports. Preserve available scope reports or actual screen observations privately before deletion, outside the reusable course folder.

If the campaign was started or work was created, do not use the unstarted-preview deletion path below. Preserve the evidence and resolve that actual review/work state before continuing. Do not count an unperformed safe-retirement step as passed.

## Generate the correct replacement as a separate object

Create a separate configuration named `certlab-016-current-review-run01` using the same person and settings. This time refine access to **only A Read and A Export**.

Generate its immediate preview and keep its saved template unscheduled. Verify the two exact A holdings and manager01's review responsibility. Record this preview's and template's actual IDs separately.

Do not assume that editing a saved template changes an already-generated preview. A new checked replacement avoids depending on an unverified Edit Preview control.

Keep the correct preview unstarted while you retire the wrong one. Check the names and IDs carefully so cleanup does not remove the replacement.

## Remove only the unused wrong preview

Reopen the exact wrong record and verify that it was never activated, has no reviewer choices or sign-off, and has no related tasks or account requests. Check that its template is unscheduled and no generation is pending.

When those checks are true, you are removing unused review content. There is no submitted decision or resulting removal work to undo.

In **Admin > Certifications > Campaigns**, select only the wrong campaign record. Use **Delete**, then inspect **Delete Campaign** before confirming. The preview page also provides deletion.

Recheck the preview list using the actual ID. The wrong record should be gone; the correct replacement must remain.

Now open **Search > Certification Campaigns > Saved/Scheduled** and remove only the wrong unscheduled template after matching its separate ID and name.

A generated campaign and its template are different objects. Deleting the first is not proof that future generation from the second has stopped.

If a schedule or pending generation unexpectedly exists, account for that actual work before declaring retirement complete. Do not assume a deleted preview cancels a queued job.

Verify A still has five holdings and B six. Neither the review-selection correction nor this zero-work cleanup should require a source-file edit.

## Check the unsigned state before Finish

Start only the correct two-item campaign.

In manager01's **Certifications > Active** session, inspect employee02's A account and both rights. The current facts support Approve on Read and Export.

Record those two choices, save and exit without **Finish**. Reopen the assigned work and verify that the choices are saved but the certification remains unsigned.

The item-level **Completed** tab lists items on which a choice was entered. It does not, by itself, mean the reviewer submitted the whole certification. Check the actual sign-off state.

If a saved choice needs correction while the actual review remains active and unsigned, the supported path is to open that item and use **Revisit Decision** in the decided-items view. Update the choice and reason, save, and inspect the actual result before final submission.

Do not delete an active review merely to change a saved choice. Also do not apply the unsigned correction path to signed work because a tab happens to have the same name.

Our two current choices are justified, so no extra wrong decision is needed for this exercise.

Inspect both choices and reasons, then use **Finish** for all actual assigned work. Verify final submission and record its time.

The current review now has two final Approve choices. A remains five holdings and B six. No removal is justified by these approvals. Preserve the signed record.

## Handle a changed need after sign-off

After the first review is signed off, use this supplied follow-up confirmation: employee02's bulk-export work has ended. Read is still required.

Record this new confirmation after the actual first sign-off, keeping the original campaign/certification references and the reason for the change.

The earlier approval described what employee02 needed when that review was finished. The later removal addresses the changed need.

Keep the signed approval. Before issuing another removal instruction, inspect the current A account and any matching task or operation. If Export is already absent or removal is already pending, establish that state and the appropriate next action instead of blindly creating duplicate work.

For the expected state here, Export is still present and no removal from the two approvals is pending. Create a separate targeted review named `certlab-016-follow-up-run01`.

Use the same exact employee02 selection flow, but refine access to **only A Export**. Choose Manager, a new future deadline, maintain undecided access, the available comment requirement and campaign emails off. Use no extra filter or optional recommendations, an immediate checked preview and an unscheduled saved template.

Verify the one intended Export holding and actual reviewer before starting.

In manager01's session, record Revoke with the new work reason and references to the earlier review in the actual comments or private change record. Use **Finish** and verify the new final submission.

This is a new decision and removal instruction. It does not edit the original sign-off.

If the original decision was a mistake rather than a later changed need, record that honestly. Establish the authorized corrective action from the actual current state. Do not rewrite the reason as a business change merely to make the history look tidy.

## Follow the resulting removal before cleanup

Return to the administrator's session and inspect the actual manual task for employee02, A account02 and Export. A **manual task** asks an operator to carry out a change that this file-based integration cannot write automatically. The recipient can use **Task Manager**; the administrator can inspect **Admin > Dashboard > Tasks**.

Check the complete requested scope, actual recipient and related review. If matching work is already pending, inspect it before creating a duplicate instruction.

Keep the two signed campaigns and their relationship visible. Do not delete either because a task is unfinished.

In this CSV exercise, editing the file simulates an external change. Remove only employee02 Export in a new copy of A's complete private account file. Use `lab-data/baselineA/report_accounts_after_employee02_export_removal.csv` as the expected value comparison, retaining the actual template's required fields.

**Aggregation** reads the changed file into ISC. Upload through the supported task file step or open A under **Admin > Connections > Sources > Account Management > Account Aggregation**. Follow collection through successful completion and inspect the resulting accounts. If it fails, preserve the error and keep the outcome unresolved.

The expected account set is:

- Employee01/account01: Read and Export.
- Employee02/account02: Read only.
- Employee03/account03: Read only.

The full account names use the `certlab-` prefix. All three A accounts remain, with four holdings. Both entitlement definitions remain, and B keeps its four accounts/six holdings.

Only then complete each wholly fulfilled manual task with the recipient's **Mark Complete**, or the administrator's permitted **Actions > Mark as Complete**. Verify its completed state.

A collected CSV result or closed task does not prove a live application's permission changed. A live result also needs a check on that application.

## Preserve the decisions and the change between them

Download fresh available campaign reports through **Admin > Certifications > Campaigns > Actions > Download Reports**. Keep the earlier scope/approval/sign-off alongside the later one-item Revoke, its task and account/file observations.

Reports generated after a change may differ from earlier downloads. Preserve originals and label the event/observation time separately from the download time.

If a report is unavailable in the current state, record the limit and use the actual review/task records. Do not force administrative completion just to obtain another export.

Your case should show:

1. The wrong A+B preview was never started and was retired with its own template.
2. The correct A-only review was finalized with two justified approvals.
3. New work information arrived afterward.
4. A separate targeted review finalized Export removal.
5. Matching work and account observations established the simulated four-holding result.

These records explain the outcome without turning a later decision into an alteration of earlier history.

## Would deleting the old approval help?

Someone says:

“The old campaign says Approve and the new one says Revoke. Delete the old one so the records stop conflicting. That should also take care of any pending work.”

Would you accept that cleanup plan?

<details markdown="block">
<summary>Read the reasoning</summary>

No. The two decisions can be correct at different times. The earlier record supports the initial need; the later record supports the changed requirement.

Deleting the old campaign would remove useful decision history. It does not establish that a pending task or account operation was cancelled or that access was restored.

Keep the signed records, link them through the actual change reason and resolve the exact work separately. Retire only objects whose actual state and purpose make that action appropriate.

</details>

Campaign deletion can remove decisions and participant visibility, and participants are not automatically notified of that deletion. It is therefore not a communication or access-restoration process.

Do not rely on a general Undo or Reopen action for signed certifications. Use the supported procedure verified for the actual state; this case preserves the signed record and makes a separate authorized review.

## Restore the training baseline after work is resolved

Preserve the signed histories, wrong-preview evidence, actual work details, current account observations and relevant reports first.

Resolve all outstanding removal before adding the test Export right back. Otherwise an old instruction could still remove it after reset.

Restore A's complete private original account file and run aggregation through successful completion. Verify employee01 Read+Export, employee02 Read+Export and employee03 Read: three accounts/five holdings. B must remain four accounts/six holdings, with the original identities and manager links unchanged.

Record the reset separately. It prepares another training run; it does not change the historical approvals or revocation.

After checking that no generation or work remains, remove only the now-unneeded unscheduled templates `certlab-016-current-review-run01` and `certlab-016-follow-up-run01`, or their recorded replacement names, from **Saved/Scheduled**. Match each saved-template reference; keep the separate signed campaigns and their reports.

No source, account or entitlement definition needs deletion.

Before ending, explain which object you retired, which signed evidence you kept, what the new decision changed and how you established that no unresolved work could undermine the restored baseline.
