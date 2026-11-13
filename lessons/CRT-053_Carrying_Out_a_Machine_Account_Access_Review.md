# How do you carry out a machine-account access review?

A program runs each morning to produce a report. It signs in to the reporting system using its own account.

That account can read reports and change reporting settings. Reading is still needed. The permission to change settings was added for a temporary repair.

Who should review this access? What should they keep? And how do we remove the unnecessary permission without stopping the approved reporting work?

Let's follow that task.

## Connect the program, its account and its human owner

A **machine account** is an account used by software, such as a program or service. A service account is a common example. The account holds the permissions the software uses in a system.

In SailPoint Identity Security Cloud (ISC), an **application identity** represents a program or service. It is a type of **machine identity**. Related machine accounts can be associated with it, allowing their access to be reviewed in the context of that program.

The application identity is a record about the program. It is not the program running on a server.

A human **account owner** is responsible for the machine account. This responsibility does not turn it into that person's personal login.

Here is our task:

- The program is Daily Reporting.
- Its application identity in ISC is also called Daily Reporting.
- Its machine account is svc-report-07 in Reporting Production.
- Its current account owner understands the reporting job and is permitted to review its access.

The **source** is ISC's configuration for obtaining account information from Reporting Production. In this example it reads an account-data file. It cannot write changes into the reporting application.

Keep those relationships clear. We are assessing the program's access through svc-report-07. Reviewing the human owner's employee account would answer a different question.

## Check that ISC recognizes the intended machine account

An account name beginning with svc does not establish that ISC has classified it as a machine account.

**Classification** identifies which accounts should be treated as machine accounts.

**Attribute mappings** tell ISC where to obtain information such as the responsible owner and the application identity for an account. Associating the account with that identity is its **correlation**. For svc-report-07, we need that association to point to Daily Reporting.

The configured rules and the resulting records both matter. A rule that looks correct is not proof that the account was associated with Daily Reporting.

With the required administrative access, open **Admin > Identity Management > Accounts**, then **Machine Accounts**. Inspect the account, its source, its associated machine identity and its owner.

For this task, those records have already been configured correctly. Verify that the production account belongs to Daily Reporting and has the intended responsible human. If either is wrong, have the authorized administrator correct and check the result before relying on it for this review.

**Aggregation** is ISC's collection of account information from the source. Classification and mapping can be processed when that collection creates or updates account information. Recheck the resulting records when investigating an unexpected change.

If an application-identity mapping was missing, ISC may have created an **uncorrelated application identity** for the account. Such a record does not prove the program is abandoned. Investigate the program and its intended grouping instead of attaching it to an employee simply to remove the unmatched label.

## Establish what the account actually needs

The current application record and the latest imported account data agree that svc-report-07 holds two **entitlements**, the access rights represented in ISC:

- REPORT.READ allows the program to read reports.
- REPORT.ADMIN allows it to change reporting settings.

The reporting-system owner confirms what these permissions do. The person responsible for Daily Reporting confirms what the program must do.

The approved requirement is to read reports each morning. The temporary repair has ended, and no continuing task needs REPORT.ADMIN.

Both rights are independently reviewable in this example. Neither is controlled by a larger access package or another automatic assignment. Establish this scope before interpreting an individual entitlement decision.

We now have a reason to keep one right and remove the other. We did not reach that conclusion merely because one name looks more powerful.

## Create the machine-account campaign

A **certification campaign** organizes access-review work. This workflow uses **Machine Identity Security**. Confirm that the feature is available in your ISC environment and use an administrator permitted to create the campaign.

Open **Search > Certification Campaigns > New Campaign** and choose **Machine Accounts**. Select the intended source and inspect its listed machine accounts. For our task, include Reporting Production and svc-report-07, then use **Certify These Accounts**.

Available reviewer choices depend on the campaign type. In this setup, **Account Owner** is available and selected. Inspect the resulting assignment; knowing who owns the account does not by itself prove who received this review.

Configure the name, description, deadline, decision-comment requirements and treatment of undecided items. Generate a **preview**, the prepared review work you can inspect before starting.

For this example, the agreed policy requires a reason for removal and maintains undecided access at administrative completion. That setting does not mean unfinished access was investigated and approved.

Check the generated account, entitlement content and assigned reviewer against the requirement. Resolve differences before starting the campaign. A correct account count could still contain the wrong production account.

When those checks agree, the administrator opens the checked preview and selects **Start Campaign**. The prepared review can now reach the assigned reviewer. Generating a preview alone does not start that review work.

## Review the program's access

The assigned reviewer opens **Certifications > Active**, then the relevant certification. A certification is the assigned review within the campaign.

In **Machine Identities**, select Daily Reporting and examine its **Entitlements**. Alternatively, **Access Items** starts with an entitlement and shows the machine identities holding it.

The application identity supplies the program context. Still check the source and actual account behind the access. A program may have several accounts, and a similarly named test account is not our production target.

The reviewer uses the confirmed purpose and permission meanings to record:

**Approve REPORT.READ:** the scheduled production report still requires reading.

**Revoke REPORT.ADMIN:** changing reporting settings was needed for the completed repair and has no continuing approved use.

Include the required reason with the removal decision. A useful explanation identifies the ended repair and the account concerned, rather than saying only “not needed.”

Complete all intended review items, then submit and confirm the certification through its finish/sign-off step. Selecting a decision and leaving the page is not enough to assume the review has been finalized.

The final decision requests removal of REPORT.ADMIN. It does not request deletion of svc-report-07 or a change to its password.

## Follow removal to the application

**Remediation** is the work needed to carry out the review's removal decision.

This source cannot write application changes. Its file import tells ISC what access exists; importing the same data cannot remove a permission in the reporting system.

For the continuation of our example, the removal is due and an actual manual task is available in **Task Manager**, assigned to an authorized reporting operator. The task identifies svc-report-07, Reporting Production and REPORT.ADMIN.

The operator confirms that target and follows the approved change procedure to remove REPORT.ADMIN in the application. REPORT.READ stays in place.

Do not infer the task recipient or readiness from the reviewer label. Inspect the actual removal work. If the task has not appeared, investigate delivery and the campaign's applicable processing instead of reporting the change as complete.

The arrows below connect the program, its access records and the human responsible for the review.

```text
Program or service
        |
        | represented in ISC by
        v
Application identity
        |
        | groups
        v
Machine account on a source
        |
        | holds
        v
Application permissions
        |
        | assessed by
        v
Assigned human reviewer
        |
        +--> Keep the permissions still needed
        |
        +--> Remove unnecessary permissions
             through the supported removal work
             and verify the account result
```

For svc-report-07, the two branches mean keeping REPORT.READ and removing REPORT.ADMIN. They do not mean approving or deleting the application identity itself.

## Verify both removal and continued approved use

Check the current application record for the exact production account. REPORT.ADMIN should be absent; REPORT.READ should remain.

Then obtain an accurate new account-data file and import it. Check that the newly collected information agrees with the application result. An old file can continue to show the removed right even when the application was changed correctly.

For this example, the program owner also performs an approved reporting run after the change. It completes successfully using REPORT.READ. That is separately supplied evidence that the required work still runs.

Closing the removal task alone would not establish either the correct account permissions or successful program operation. Likewise, a successful report would not prove REPORT.ADMIN had been removed: the program might still run while retaining excessive access.

Keep the decision reason, actual removal result, refreshed account evidence and approved run result together. If one is missing, describe what is known and what still needs checking.

The campaign administrator separately checks unfinished reviews and removal follow-up before administrative completion. A completed campaign is not a replacement for this account evidence.

## What if the human owner leaves?

Suppose the person responsible for svc-report-07 leaves the organization next month, but Daily Reporting is still approved and must continue.

The ownership record needs attention. That change alone does not establish that the program no longer needs REPORT.READ.

Find the new responsible person and confirm the program's continuing purpose. The authorized administrator opens the account under **Machine Accounts**, selects **Actions > Update Account**, changes **Primary Owner** and selects **Apply**. Check the saved result.

Also check the application identity's owner. Responsibility for the program and responsibility for its account are related records; do not assume that changing one changed the other.

If a review was already assigned, inspect its actual assignee and use the supported reassignment process when needed. Updating an owner record is not evidence that an existing campaign was rebuilt.

The same access decision can remain justified while responsibility changes: keep required reading, retain evidence that the excessive administrative right was removed, and establish who now answers for the account.

## Try a different account

You open a machine certification for a backup program. Its production account needs permission to write backups. The review shows a test-system account with a similar name and no longer has a knowledgeable owner.

Would you approve the displayed permission because production backups are necessary?

First establish the target. The production requirement does not justify access on a different test account. Find who can explain that account's current purpose and inspect its actual permissions.

You also cannot conclude that it should lose every permission merely because the ownership record is incomplete. Resolve the missing responsibility and gather evidence of use. If the review cannot be resolved in time, follow the campaign's approved handling for unfinished work and record the unresolved question.

The decision needs a connection you can explain: this program, this source account, this permission and this current approved task.
