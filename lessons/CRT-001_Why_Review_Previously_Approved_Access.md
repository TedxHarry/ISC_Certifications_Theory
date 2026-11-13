# Why review access that somebody already approved?

A person was given permission to export reports because they needed it for their work. Later, their responsibilities changed. Someone else now prepares the reports, but the person's application account still has the export permission.

The original approval may have been correct. It explained why the person needed access then. We still need to find out whether they need it today.

An access review connects that question with the permission that remains on the account.

## Changing the work does not automatically change the account

An **account** is the person's record in an application or system. **Access** means what that account is allowed to do.

In our example, the account can export reports: it can take report information out of the reporting application. That permission made sense when exporting reports was part of the person's job.

Moving the work to someone else changes who is responsible for the reports. Removing the permission requires a separate change in the application. Until that change happens, the account can continue to hold the permission.

This is why the earlier approval is useful information, but not enough information for today's decision. We know why access was given. We still need to know what the person does now and whether that work requires export.

A handover could be one reason to keep the permission temporarily. A continuing reporting task could be another. If neither applies, the permission may have remained after its purpose ended. The permission's presence alone cannot tell us which explanation is true.

## Connect the person with the account

SailPoint Identity Security Cloud, or **ISC**, keeps an **identity** representing the person and connects it with their application accounts.

The account is where the permission exists. The identity helps establish whose work should justify that permission. Check that you are discussing the correct person and account.

ISC represents an access right as an **entitlement**. Here, reports-export means permission to export reports. The account already has it; showing that access in ISC does not grant or approve it.

## What does an access certification ask the reviewer to do?

An **access certification** is an assigned review of whether a person should keep the access shown. The person responsible for making its decisions is the **reviewer**, also called the certifier.

The review is asking about the person's access. Confirming that their account exists would not answer whether they should still be allowed to export reports.

A **certification campaign** organizes a set of assigned reviews. An administrator defines which access should be included and arranges the reviews for the relevant reviewers.

The particular access presented for a decision is a **review item**. In this example, the item is reports-export on the person's reporting account. The reviewer can choose Approve or Revoke for it. Nothing else in ISC requires the person to keep this permission or would restore it after removal.

The reviewer needs to understand what the permission allows and what the person needs for their current work. A manager may know the current responsibilities. A system owner may know the meaning of the permission. The assigned reviewer needs the relevant information for this decision, whichever people help establish it.

For reports-export, that means finding out whether the person still has an approved reason to export these reports.

## Follow the reason for removing or keeping access

Suppose the reviewer confirms that the person no longer prepares or exports reports. There is no continuing reporting task and no handover that requires the permission.

We now have the information needed to connect the account with the work. The account still has export permission, but the person's current responsibilities no longer need it.

The reviewer chooses **Revoke**. This records the decision that the access being reviewed should be removed.

The reason for Revoke is the confirmed lack of a current need. The permission is not being removed simply because it is several months old or because the person's job title changed.

Now change the situation. The reviewer confirms that the person still performs an approved reporting task that requires export.

In that case, **Approve** can be appropriate. It means the reviewer accepts that the person should keep the access shown for review. The current task explains why keeping it is justified.

Approve is a decision about the reviewed access. It does not ask ISC to create unrelated permissions the person is missing.

Both decisions need a reason connected to the current work. Automatically keeping everything because it was approved before leaves today's need unanswered. Automatically removing everything can take away access people still need.

The age of an approval does not settle the decision in either direction. An old permission can still be needed, and a recently approved permission can become unnecessary if the work changes.

## Selecting Revoke does not show that the permission is gone

Return to the case where the person no longer needs export and the reviewer has selected Revoke.

There are now two separate records to consider. The review records what the reviewer decided. The application account still holds the permission until the required account change is carried out.

The reviewer also needs to finish and confirm the assigned review. This confirmation is called **sign-off** or **finalization**. It tells ISC that the reviewer has completed their decisions.

The campaign's process determines when the decisions lead to removal work. To carry out the decision, the reporting application needs to stop allowing this account to export reports.

The work needed to act on the required removal is called **remediation**. Where ISC has a connection that supports and is authorized to make the change, it can carry out the removal automatically. Where the change requires human action, someone receives a task to make it in the application.

Whichever path applies, we need to follow the actual work and check its result. A recorded decision and an application change are separate results.

Suppose the required review steps are complete, the removal work succeeds and a check of the intended reporting account confirms that reports-export is absent. That gives us evidence that the required permission removal happened.

It does not mean the whole account was deleted or that its other permissions were removed. The required change in this example concerns the export permission.

The earlier approval and the successful later removal fit together like this:

```text
Earlier: export needed for work
        |
        v
Access was approved

Today: export no longer needed
        |
        v
Reviewer records Revoke
        |
        v
Finish and confirm the review
        |
        v
Carry out required removal
        |
        v
Check the application account
        |
        v
Export permission is absent
```

The first part explains why access was originally given. The second part follows the later review through the steps needed for the successful removal described above. The campaign's processing determines when removal work begins; the arrows do not promise that every step happens immediately.

At the final check, someone verifies the account's actual permission. A Revoke decision by itself cannot supply that evidence.

## Why a later review can still be needed

An approval or review answers a question using the work and access information available at that time. The person's work can change again afterward.

They may finish a project, move to another responsibility or receive more access. A permission that was justified during one review may therefore need another decision later.

A periodic review repeats the assessment at planned intervals. A focused review can examine a particular group of people or set of access. The purpose is to check the intended access against the current need and follow any required changes through to their results.

Completing a campaign does not make every account permanently correct. Nor does the number of items completed tell you, by itself, whether the decisions made sense.

When helping organize a review, establish what access needs assessment, who can judge its current need and how the required outcomes will be verified. That connects completing the review with the business problem it is meant to address.

## Apply the reasoning to a different permission

A person's account can update supplier bank details. This permission was approved for a temporary task.

The task has now ended. The assigned reviewer confirms that the person has no continuing approved responsibility requiring bank-detail updates. The account still has the permission, and it is available as an individual review item. Nothing else requires the person to keep it.

Someone argues that another review adds nothing because the original approval was correct.

How would you explain what the review is checking now? What decision do the supplied facts support, and what evidence would show that its required outcome happened?

The original approval explains why the person could update supplier bank details for the temporary task. The task's completion and the confirmed lack of a continuing need explain why the same permission should now be reviewed for removal. A correct earlier approval and a justified later Revoke can both make sense.

The review decision needs to be completed and confirmed through the applicable process. The required removal then needs to be carried out. To establish the outcome, check that the intended account no longer has permission to update supplier bank details. A recorded Revoke alone does not prove that result.

Now change one fact. The temporary task has ended, but someone mentions another responsibility that may require the same permission. No information confirming that responsibility has been supplied.

The ending of the first task no longer gives us the complete answer. Establish whether the other work is approved and needs bank-detail updates before claiming a definite keep-or-remove conclusion. The review needs a reason supported by the current facts.
