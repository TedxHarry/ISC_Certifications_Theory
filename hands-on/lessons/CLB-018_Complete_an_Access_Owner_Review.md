# Complete an access-owner review

The request is to review one permission: Export Reports. We need to find everyone who holds that permission and ask its responsible owner whether each person still needs it.

That gives us a different starting point from a manager review. We start with the access item, then find its holders. We also need to establish who owns that particular item. The person responsible for the whole application may be someone else.

You will select one Export entitlement, check its owner and generated review, complete the decisions and follow one simulated removal. An optional variation then assigns a small Read review to a team.

## Connect the permission, its holders and its owner

An **identity** is ISC's record for a person. An **account** is their record on a managed system. A **source** holds ISC's connection settings and collected account information for that system.

An **entitlement** is an individual permission ISC tracks. Here, Read allows viewing reports; Export allows downloading reports in bulk. A **holding** means one account has one permission.

The source's owner is responsible for the source. An entitlement's **Primary Owner** is the identity recorded as responsible for that permission. Selecting **Access Owner** as the campaign reviewer tells ISC to use the access item's ownership when assigning the review.

A **campaign** organizes review work. A **certification** is an assigned review inside it. The **review item** is the access that needs a choice.

For this exercise, keep these responsibilities separate:

- Source A's owner: `certlab-manager02`.
- A Export's primary owner for this run: `certlab-manager01`.
- Reviewer setting: **Access Owner**.

The labels manager01 and manager02 do not decide the routing. Manager01 also happens to manage the two employees in this dataset. A review appearing in their account therefore cannot, by itself, prove that you selected Access Owner. Check the saved setting and actual entitlement owner as well.

## Establish the starting accounts and working sessions

Use an authorized training administrator who can edit the selected entitlement, create campaigns and collect the CSV source. Both manager01 and manager02 need working approved sign-ins. Importing their people records does not create those sign-ins.

Use the existing five identities from `certlab-people-profile`, supplied by `certlab-people-csv`. Verify the correct account links and original manager relationships: employee01/02 report to manager01, employee03 reports to manager02.

Use source **A**, `certlab-reports-csv`, with three accounts and five holdings:

| Account and identity | Starting access | Access selected for this review |
|---|---|---|
| certlab-account01 / certlab-employee01 | Read and Export | Export |
| certlab-account02 / certlab-employee02 | Read and Export | Export |
| certlab-account03 / certlab-employee03 | Read | None |

Source **B**, `certlab-owner-reports-csv`, keeps its original four accounts and six holdings. Its similarly named Export is a separate source-specific object and stays outside this review.

Keep A's permissions as direct entitlements. No temporary access profile, role, lifecycle grant or review redirect should change the review unit or require Export to be granted again. A profile packages permissions; a role or lifecycle grant can make access required by a configured condition.

Resolve earlier outstanding work before restoring changed data. Starting values are in `lab-data/baselineA/report_accounts.csv` and `lab-data/baselineB/owner_review_accounts.csv`. Use complete private copies fitted to the actual source templates. The application is represented by CSV; a later file edit will simulate its access change.

## Check and prepare the owner of this exact entitlement

Open **Admin > Access Model > Entitlements**. Find A's Export entitlement, whose value is `certlab-report-export` in the account's `groups` attribute. An **attribute** is a field; its **value** is the permission recorded in that field.

Inspect the source and actual entitlement ID. Do not select B's matching display name. Record A's source ID, the Export object ID, its current Primary Owner and A's source owner in your private notes.

Before changing ownership, check how the recorded state can be restored. If it was unset and the available control cannot clear an owner, agree the reusable training-owner state before editing rather than discovering that reset gap at the end.

If the approved training entitlement does not already have manager01 as Primary Owner, use its **Actions > Edit** control. In **Configuration**, select manager01 as **Primary Owner**, then **Save**. Preserve the previous owner, including whether it was unset, for the reset check.

Change only this test entitlement's owner. Leave its request settings, additional owners, description and other metadata unchanged. Additional owners used in access-request reviews are not a substitute for the primary-owner relationship we are checking here.

Reopen the entitlement and verify the saved identity reference. Keep A's source owner as manager02.

This ownership edit changes responsibility recorded in ISC. It neither grants Export to manager01 nor changes any account's permissions. A should still have five holdings.

Search and generated work can reflect an update later than the saved entitlement view. If they still show the old owner, check the exact record and allow the normal update to appear before preparing a fresh preview. Do not change global mappings or process unrelated identities to force the expected recipient.

## Select the access first, then limit what will be reviewed

Open **Search > Certification Campaigns > New Campaign > Access Items**. Under **Using a Search Query**, choose **Create Campaign**, then **Specific Access Items that I Select**.

Use `*` to find candidates. It means all search results; it does not mean add everything.

Inspect the returned entitlements. Select only A's Export, checking its source and object ID against your private note. Use **+ Add To Campaign**, inspect **Added to campaign**, then select **Certify This Access**.

This selection finds the identities holding that access. It does not yet establish that every other permission those identities have is excluded.

Choose **Refine Access Items**. Add only that same A Export entitlement to the access being reviewed, check the added set and continue.

The two selections answer different questions:

> Who should be included? The holders of A Export.
>
> What should we review for them? Only their A Export.

If you choose all their access instead, you could include Read or B permissions. That would broaden the work beyond this request.

## Choose Access Owner and inspect the actual assignment

Use an unused name such as `certlab-018-access-owner-run01`. Preserve an existing run and choose another suffix if necessary.

Select **Access Owner** as reviewer. Reviewer choices depend on the campaign type and available engine. If this option is missing, check that setup before continuing; selecting an individual would not test ownership-based routing.

Keep campaign emails off and optional recommendations off. Choose a permitted future due date and record its time zone. Maintain undecided access and require a reason for Revoke; follow an all-comments requirement if that is the offered setting.

An **undecided** item has no recorded choice. Maintaining it means the campaign's completion setting keeps its access when no decision has been made.

Generate a preview now and save an unscheduled template. A **template** stores the settings; the **preview** is the generated review work. Record their actual references separately.

Check every generated item before starting:

- Employee01, account01, A Export.
- Employee02, account02, A Export.
- The saved Access Owner mode and manager01 as the actual responsible reviewer.
- No Read, B permission, employee03 or manager account included as a review subject.

Two holdings do not necessarily mean two separately assigned certifications. Inspect the actual grouping and recipients.

An unexpected recipient needs investigation. Compare the selected access object, its saved primary owner, the campaign's reviewer mode and the current preview. With no owner, ISC can use its documented ownership fallback. A fallback recipient is not proof that the intended primary owner was configured correctly.

Do not clear ownership to manufacture a fallback in this run. When the checks agree, select **Start Campaign** on that preview and record its actual campaign ID and start time.

## Review each holder's current need

Use these supplied work facts:

Employee01 has an approved recurring report-export duty. The duty continues between its scheduled runs.

Employee02's migration is finished. The responsible owner confirms there is no other continuing Export duty. Employee02 still needs Read.

These are training facts. Ownership of the permission identifies who should review; it does not automatically answer whether each holder needs it.

Sign in as manager01. Open **Certifications > Active**, select the actual assigned review and match both items to the preview.

**Approve** employee01's Export because its approved duty continues. **Revoke** employee02's Export because its purpose has ended. Explain the removal specifically: retain the account and Read, remove only A Export.

Inspect the saved choices. **Sign-off** is the reviewer's final submission, made through **Finish** and the actual confirmation. A saved choice alone is not that submission. Finalize every assigned certification needed to cover the two holdings and preserve the actual sign-off evidence.

Use available campaign reports and item history to connect the assigned owner, actual decision maker and final submitter. Keep their identities and times separate if work was reassigned or an administrator acted. Missing actor information remains something to obtain, not a name to infer from the campaign setting.

## Follow the rejected holding to the file result

Return to the administrator's session and inspect **Admin > Dashboard > Tasks**. The actual recipient can open the work in **Task Manager**.

A **manual task** asks an authorized operator to carry out the change. Match its campaign, source, employee02 account, Export and complete requested scope. Record the actual recipient. The access reviewer and the removal-task recipient are separate responsibilities; do not assume both are manager01.

If matching work is missing, check sign-off, campaign state and the configured removal path before editing a file.

In a new version of A's complete private account file, remove only employee02/account02's Export holding. The comparison values are in `lab-data/baselineA/report_accounts_after_employee02_export_removal.csv`.

Upload through the task's supported file step, or have the authorized administrator open A under **Admin > Connections > Sources > Account Management > Account Aggregation**. **Aggregation** reads the supplied account data into ISC. Follow it through successful completion before checking the result.

Verify A still has all three accounts and all three Read holdings. Employee01 keeps Export; employee02 no longer has it. That is four A holdings. B still has six. Both A entitlement definitions and the correct account/identity links remain.

This proves the simulated file result when you perform and record the steps. It does not prove that a real reporting application's permission changed.

After the full task scope is fulfilled and checked, the recipient can select **Mark Complete**. An authorized administrator's equivalent is **Actions > Mark as Complete**. Inspect the resulting state. A closed task by itself does not establish the account result you just checked.

## Restore the data and account for the owner change

Preserve the preview, settings, signed choices, task, private file versions, collection and account observations. Resolve all outstanding work before adding Export back for another training run.

Restore A's complete private original file and collect it successfully. Verify the original three accounts/five holdings, original account/manager links and unchanged B four accounts/six holdings.

If you changed Export's Primary Owner, restore the recorded previous owner through the same entitlement edit screen. Reopen the record to check it. If the owner was originally unset, use only the supported clearing control actually available. If you cannot restore that state, keep the ownership reset unresolved or agree an explicit reusable training-owner baseline. Do not guess a write request or claim the original metadata was restored.

Record the later training reset separately from the earlier business decision. Keep the signed campaign and reports. After checking no generation remains, retire only this run's unneeded unscheduled template from **Search > Certification Campaigns > Saved/Scheduled**, matching its saved reference and actual name.

## Optional: let a review team perform a small review

Sometimes responsibility belongs to a team. A **governance group** is a named group of identities allowed to make governance decisions. A member can act on the group's behalf. Group assignment does not mean every member must submit a separate approval.

Use this variation after the main run's work and reset have been accounted for. It reviews only employee01/02's A Read holdings. Both people still need Read, so the expected result is two approvals with no account change.

### Prepare the group and inspect its members

As the administrator, open **Admin > Identities > Governance Groups > Create Group**. Use an unused name such as `certlab-018-review-team-run01`, a clear training description and manager01 as group owner. Save.

Open **Membership > Add Members**, select the actual manager01 and manager02 identities, then **Add**. Check their exact IDs, active status and working sessions. Setting a group owner does not replace this explicit membership check.

Keep this group dedicated to this exercise. Do not associate it with source management, grant sub-admin permissions or change access-request settings. Its task here is certification review.

### Assign only the two Read items to the group

Create a separate campaign through **Search > Certification Campaigns > New Campaign > Identities**. Choose **Create Campaign** under **Using a Search Query**, then **Specific Identities that I Select**.

Find:

```text
name.exact:"certlab-employee01" OR name.exact:"certlab-employee02"
```

Add only those identities, inspect the added list and choose **Certify Selected Identities**. Refine their access to only A's `certlab-report-read` entitlement.

Use an unused name such as `certlab-018-group-read-run01`. Select **Governance Group** as reviewer and the exact group you just prepared. If that choice is unavailable for the actual campaign type, resolve the capability before using this variation.

Keep emails and recommendations off, maintain undecided access, use a permitted future deadline and save an unscheduled template while generating the immediate preview.

Verify two A Read holdings, the selected group and no Export/B access. Record the actual certification grouping, then select **Start Campaign** on the correct preview.

Before making choices, use each member's own **Certifications** session to check that the intended assigned work is reachable. If a member cannot open it, inspect the actual group assignment, membership, active identity and permissions. Do not substitute a direct individual assignment and describe it as a group result.

Have manager01 review both required Read holdings, record justified Approve choices and finish all assigned work covering them. Manager02 does not need to repeat those approvals. Avoid simultaneous edits while learning the shared-review behavior.

### Explain the group responsibility and the human action

As the administrator, open the campaign's **Actions > Download Reports**. Generate fresh available status and sign-off reports after submission, keeping their observation times.

Inspect the configured group reference separately from the actual **Decision Maker** and final sign-off reviewer. A group label tells you who was responsible; the human actor tells you who performed the action. Match the actual fields and history rather than assume one universal report layout.

If the available evidence does not identify the acting member, record that gap. Group membership alone cannot prove who made a particular choice.

Check two approvals, final submission for all actual assigned work, unchanged A five/B six and no removal needed for these decisions. Investigate any unexpected task before ending; do not edit the CSV to make this approval-only case look complete.

Preserve both the group review and earlier Access Owner history. Retire only this variation's unused unscheduled template after checking generation/work. Keep the dedicated group with its approved membership for repetition; do not delete a group referenced by history merely to tidy the list. Confirm it has no unrelated associations or future campaign schedule.

## Check the reasoning behind a familiar recipient

The campaign arrived with manager01. Someone says, “That proves the permission-owner configuration is correct.”

What would you check before accepting that explanation?

<details markdown="block">
<summary>Compare your reasoning</summary>

Manager01 also manages these employees. The same recipient could therefore fit a Manager campaign. A directly selected individual could produce that name too.

Inspect the saved Access Owner setting, the exact A Export object's primary owner and the generated assignment. Also check that the item is the selected direct entitlement rather than a different package or similarly named B permission.

For the optional team case, inspect the selected governance group and the actual member who acted. A correct-looking person name does not replace the configuration and history needed to explain how the work reached them.

</details>
