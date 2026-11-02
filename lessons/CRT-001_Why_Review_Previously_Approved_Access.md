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

## Connect the person with the permission ISC shows

SailPoint Identity Security Cloud, or **ISC**, keeps an **identity** representing the person. This identity connects information about them with their accounts and access.

The person's reporting account is still a record in the reporting application. ISC's identity and the application's account are separate records. The identity tells us which person we are discussing; the linked account tells us where their access exists.

ISC represents an access right as an **entitlement**. For example, reports-export is an entitlement meaning permission to export reports.

An administrator sets up a **source** in ISC to manage account data from the reporting application. The source is ISC's configuration for that data. The application remains the system where the account holds its working permissions.

ISC reads account information from the application and records it against the source. This collection is called **account aggregation**. Here, the collected information shows that the reporting account holds reports-export.

ISC also needs to connect that account to the correct person's identity. This association is called **account correlation**. Without the correct association, we could be discussing an account using the wrong person's responsibilities.

For this example, both the association and collected information are correct. We know which person owns the account, which account we are reviewing and which permission it holds.

Reading the permission into ISC has not granted it or approved it. It has given ISC information about access that already exists, so someone can review whether it should remain.

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

## If access remains, find out which step has not succeeded

Suppose the review records Revoke, but a current check of the account still shows reports-export. No evidence of completed removal work has been supplied.

The required outcome has not yet been established. The reviewer may have made the right decision while the removal remains unfinished or has failed.

Check whether the review was finished and confirmed. Then follow the applicable removal work and inspect the result for the correct application account and permission.

These checks help you establish where the difference began. From the facts above alone, you cannot say that the connection failed, that a task was ignored or that a particular campaign setting caused the problem. You need the evidence for the actual step.

The old approval does not cancel the current Revoke decision. Equally, the current Revoke decision does not prove the application changed.

## Use each record to answer the question it can answer

The information about an access review serves different purposes. Keeping those purposes clear helps you choose what to inspect.

| What you need to know | What you inspect | What it tells you |
|---|---|---|
| Why access was originally given | The earlier request and approval, when available | Why the access was accepted at that time |
| Whether the person needs it today | What the permission allows and the person's current approved work | Whether keeping it is justified now |
| What the reviewer decided | The review item and its recorded decision | Whether the reviewer chose to keep or remove the access |
| Whether the required removal happened | Review confirmation, removal work and the correct account's current permissions | Whether the decision reached the intended account outcome |

For example, the earlier approval can explain the original reporting task. To decide about continued export, you need information about today's task. To confirm removal, you need evidence about the account after the change.

One record cannot answer all those questions simply because it says approved, revoked or complete. Establish what the label describes before using it as evidence.

## A changed job title can leave the decision unanswered

Suppose the person's job title changed, and the account still holds reports-export. Nobody has yet checked whether they still need to export reports during a handover or another continuing task.

A title change gives us a reason to investigate. It has not established that the permission is unnecessary. It also has not established that keeping it is justified.

Find out what reporting work remains, what that work requires and who has enough knowledge to confirm it. Then connect those facts with the permission.

In this situation, gathering the missing information is part of doing the review properly. Choosing an answer without that information would make the decision look more certain than the facts support.

## Two access records can describe different moments

A certification includes reports-export. Later, an application administrator checks the account and confirms that the export permission has been removed.

Both observations can be correct. The review used information available when its access data was collected or generated. The administrator checked the account after the later change.

Before treating the records as a contradiction, confirm that they concern the same person, account and permission. Then compare when the data was collected, when the review was generated and when the later application check occurred.

Also check the later account information in ISC after the relevant source collection and processing. Do not assume that every visible ISC record reads the application live or that an already generated review automatically changes when the source changes.

This matters in both directions. Earlier data can show access that has since been removed. Missing or incomplete data can also leave actual account access out of what someone is inspecting.

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
