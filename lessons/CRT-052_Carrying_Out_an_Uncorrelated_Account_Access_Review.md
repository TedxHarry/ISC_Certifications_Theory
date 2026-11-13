# How do you carry out an uncorrelated-account access review?

A reporting account still has permission to read and export reports. ISC cannot connect it to an identity established from the organization's trusted person data.

Should its access be removed?

The missing connection gives us a reason to investigate. It does not tell us what the account does or whether its permissions are still needed.

An uncorrelated-account certification lets a reviewer assess that existing access. Let's follow the work from selecting the account to checking the result.

## Establish what is missing

An **account** is a record used to access an application. Its permissions determine what someone using it can do.

Here, an **identity** is ISC's record for a person. An **authoritative source** supplies the trusted information used to establish those identities, such as personnel records. An **authoritative identity** is established from that information.

**Account correlation** associates an application's account with the appropriate identity. An **uncorrelated account** lacks the authoritative identity association.

ISC can still represent it through an **uncorrelated identity**, a placeholder record used for the unmatched account information. Seeing a name in that record does not establish that ISC has identified a known employee. Do not assume every placeholder represents exactly one account; inspect the actual accounts associated with it.

There are different reasons for the missing association. The matching data might be wrong, the intended person record might be missing, or the account might no longer have a valid use. The reason needs evidence.

## Define which account and access need review

Our account is rpt-old-14 in Reporting Production.

The **source** is ISC's configuration for this reporting system and its account information. It uses an account-data file, so ISC can read the account data but cannot write changes into the application.

The latest collection shows two **entitlements**, access rights represented from the system:

- RPT.READ permits reading reports.
- RPT.EXPORT permits exporting report contents.

A current application check agrees with that information. The two permissions are independently reviewable in this example. They are not included through a larger package or required by another automatic assignment.

The agreed requirement is to review these permissions on this production account and carry out any justified removal. It is not an instruction to attach every unmatched account to an employee.

Keep the source and account identifier together. A similarly named test account would be a different target.

## Prepare the dedicated campaign

A **certification campaign** organizes access-review work. The administrator needs permission to create and manage it.

Open **Search**, then its **Certification Campaigns** area, and choose **New Campaign**. Select **Uncorrelated Accounts** as the campaign type. Select the relevant source, then inspect the uncorrelated accounts listed for it.

For our requirement, select Reporting Production and rpt-old-14. Use **Certify These Accounts** to continue to the campaign details.

The starting records are source accounts. Selecting a department's employee identities would not establish that this unmatched account was included.

Before relying on the selection, compare it with the intended account list. If an expected account is absent, check its source, current collected information and actual correlation status. It may have been linked correctly since the earlier list was prepared.

Do not undo a correct association merely to make the account appear in an uncorrelated-account campaign.

## Give the review the right responsibility and settings

The available reviewer choices depend on the campaign type. In this supported setup, the administrator selects **Source Owner**.

The **source owner** is the person recorded as responsible for that source in ISC. Here, that person understands the reporting application's permissions, is permitted to review the work and can obtain information about the account's business purpose.

That knowledge matters. An ownership label alone would not tell us whether rpt-old-14 is still used for an approved task.

Give the campaign a clear name and description identifying the intended production-account review. Then set the choices that affect this work:

- The deadline states when reviewers are expected to finish.
- Comment requirements determine when a reason must accompany a decision. Our campaign requires reasons for removal.
- The handling of undecided items determines the supported administrative treatment of unfinished work when the campaign is completed.
- Notification settings control the configured messages; they do not establish that the review reached the correct person.

For this example, the approved policy maintains undecided access at administrative completion while unresolved questions are followed up. Maintaining an undecided permission is not evidence that someone assessed and approved its current need.

Choose the preview-generation option that fits the intended start. A scheduled preview prepares work; an administrator still needs to start the generated campaign.

## Inspect the generated work before starting

A **preview** is generated review work available for inspection before reviewers begin.

Check the actual source, rpt-old-14 account, intended permissions and assigned reviewer. The account being present somewhere in ISC does not prove those two permissions reached this campaign.

If the work contains another account or has reached the wrong person, investigate that difference before starting. A matching number of accounts is not enough.

Once the generated work matches the requirement, the administrator starts the campaign.

The reviewer opens **Certifications** and selects the assigned review in **Active**. This assigned certification is the review within the campaign. The **Uncorrelated Identities** view lets the reviewer examine access associated with an unmatched identity record. An **Access Items** view instead starts with an access item and shows the associated uncorrelated accounts.

Whichever view is used, follow it to Reporting Production and rpt-old-14. The placeholder's display name cannot replace checking the actual account.

## Investigate the need before deciding

The reviewer establishes what rpt-old-14 was created to do.

In our example, the responsible application and project owners confirm that it supported a temporary reporting project. The project has ended. They verify that no continuing approved reporting work or automated process needs this account's reading or export permission.

Those facts supply the reason for removal. The missing identity association alone would not.

Recent activity would need interpretation too. An account can still be used after its authorized purpose ends. Conversely, a legitimate emergency account may have little recent use.

Here, both reviewed permissions lack a current authorized need. The reviewer selects **Revoke** for RPT.READ and RPT.EXPORT and records the confirmed project-end reason against the required items.

**Revoke** records that the reviewed access should be removed. **Approve** accepts keeping the reviewed access when supported by a current need. Approve does not create a missing person association, and Revoke does not mean the whole account has been disabled or deleted.

The reviewer also completes the required final confirmation, or **sign-off**. Saving the two choices and confirming the review are separate actions.

## Follow the work that can change this application

Our source reads a file; it cannot remove permissions directly in the reporting application.

The required account changes therefore need human action. **Remediation** is the work to carry out the review's required removal.

Suppose the review has been confirmed, the removal is due and an actual manual-removal task is available in **Task Manager**. Check its instructions, target account and actual assignment.

Here, the task has reached a person authorized to administer reporting accounts. That person must change rpt-old-14 in Reporting Production. Do not assume that the reviewer and the worker are always the same person, or infer the task recipient solely from a title.

The worker removes the two specified permissions through the authorized application process and records the work.

Closing the task reports completion of that work. We still need evidence of the account result.

```text
Select the intended source account
  No authoritative identity association
                   |
                   v
Review its actual access and current purpose
                   |
                   v
Record and confirm supported access decisions
                   |
                   v
Follow the required removal work
                   |
                   v
Check the application account
and updated account data in ISC

Separate ownership work:
  Verify and repair a person link where justified.
  Approve/Revoke does not create that link.
```

The main arrows connect the access review to its required result. Correcting a person association is separate work with its own evidence; it is not another effect of selecting Approve or Revoke.

## Verify the result and account for what remains

Suppose a current application check now shows that rpt-old-14 still exists but lacks RPT.READ and RPT.EXPORT.

That establishes the specified permission-removal result. It does not establish that the account cannot sign in, has no other possible access or has been deleted.

If the broader requirement is to retire the account, the responsible team must also carry out and verify the separately authorized disablement or deletion. Do not describe two entitlement decisions as proof of that larger outcome.

ISC also needs accurate information after the change. **Account aggregation** reads account information into ISC. For this file-based source, obtain a new file reflecting the actual changed account, then import and process it through the supported source procedure.

Keep rpt-old-14 represented accurately in that file. Dropping its row merely to make it disappear from a list would not establish what happened in the application.

In our successful example, the updated account data also shows the two permissions absent. The decision, manual work and current account evidence now agree.

The account may remain uncorrelated. Its two permissions have been reviewed and removed; nobody has established a new authoritative person association. An unchanged uncorrelated-account count is not, by itself, evidence that the access review failed.

Reconcile the campaign's decisions and final confirmations, the removal result and any remaining work. Record the owner of a separate account-retirement or data-correction issue if one remains. A campaign's completed status cannot supply missing application or ownership evidence.

## What if a valid person and current need are found?

Now consider rpt-active-22 on the same source.

The responsible business owner confirms that a current worker needs its RPT.READ permission for an approved reporting duty. The application evidence identifies the exact account. The account's staff identifier contains a verified data error, so it has not been associated with the correct available identity.

Should the reviewer remove reading simply because the account is uncorrelated?

No. The supplied current need supports keeping that reading access. The missing association needs correction, but it is a different problem.

The access review can record a justified Approve for the reviewable reading permission. That decision does not correct the staff identifier or link the account.

For ownership maintenance, an authorized administrator goes to **Admin > Connections > Sources**, selects the source, and opens **Uncorrelated Accounts** under **Account Management**. They examine the configured matching information and verified person/account records, then choose the appropriate correction: fix inaccurate data and perform the relevant correlation processing, or use the supported manual-correlation process where appropriate.

Manual correlation creates a persistent association. It should follow established ownership, not a guess from a similar display name.

After the permitted correction, inspect the intended identity's accounts and the updated uncorrelated-account evidence. An accepted upload or a reduced count alone is not proof that rpt-active-22 was linked to the right person.

If the repair occurs before generating the campaign, reassess the current eligible population. If review work already exists, inspect its actual contents and supported handling; do not assume that changing the link rebuilt the earlier review.

Finally, change the evidence. Suppose nobody can establish who uses rpt-active-22 or whether its access supports an approved duty.

The justified Approve conclusion above no longer follows. Identify the missing facts, involve the responsible application/business contacts and keep the unresolved work visible under the campaign's process. The absence of a person link does not supply either an approval or a removal reason.

The practical questions stay separate: what access should this account keep, who or what does it belong to, and what evidence establishes each required change?
