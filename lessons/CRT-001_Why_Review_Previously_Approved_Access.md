# Why review access that somebody already approved?

An application account has permission to export reports. That permission was approved because the person needed it for their work.

Their responsibilities have since changed, but the permission is still there.

Was the original approval wrong? It may have been entirely reasonable. It answered whether the person needed that access at the time. It does not tell us whether they need it now.

That is the reason to review existing access.

## An earlier approval tells us about an earlier need

Think about what the permission allows. The person can take information out of the reporting application by exporting it. That capability was useful when preparing reports was part of their responsibilities.

Now suppose someone else prepares those reports. The person's account may still have the same permission unless an appropriate change removes it.

Changing someone's responsibilities and changing their application access are different actions. One does not establish that the other has happened.

There are several possible explanations for the access remaining. It could still support an approved task. It could be needed temporarily for a handover. Or it could have remained after the original need ended.

The account's permission alone cannot tell you which explanation is correct. You need information about both the access and the person's current work.

This is also why “it was approved before” is incomplete reasoning. The earlier approval explains why the permission was granted. The current review asks whether keeping it is appropriate under today's conditions.

## What is ISC asking someone to review?

An **account** is the person's record in a particular application or system. **Access** is what that account is allowed to do.

In SailPoint Identity Security Cloud (ISC), an **identity** represents the person and connects information about them with their accounts and access.

An **entitlement** represents an access right from a system. For our example, the entitlement is reports-export: permission to export reports from the reporting application.

The identity, account and entitlement answer different questions. Which person are we discussing? Which application record belongs to them? What can that account do?

ISC represents the application through a configured **source**. **Account aggregation** reads account information into ISC. **Account correlation** associates an account with its owning identity.

Those connections let a review bring together the person and their represented access.

For our example, the account is correctly associated with the person, and the collected information confirms that it holds reports-export. The permission appears as a **review item**, the particular access presented for a decision, with Approve and Revoke available. No other access requirement would keep or restore that permission.

An **access certification** is an assigned review of whether access remains appropriate. The person doing that work is the **reviewer**, also called the certifier.

A **certification campaign** organizes a set of these assigned reviews. An administrator defines what should be reviewed and arranges for the relevant reviewers to receive it.

The reviewer is being asked to judge the access, not merely confirm that the account exists.

For reports-export, the useful question is: “Does this person still have an approved reason to export these reports?”

## How does the reviewer answer that question?

The reviewer needs enough relevant knowledge to connect the permission with the person's current responsibilities. A manager may understand the work; a system owner may understand what the permission allows. The assigned reviewer must use the information needed for this particular decision.

Let's follow a supplied example. The person no longer prepares or exports reports. The reviewer confirms that there is no continuing reporting task or handover requiring the export permission.

The application information shows that the account still holds reports-export. The current work information shows that the permission is no longer required.

Those facts support removing it. The reviewer records **Revoke**, a decision that the reviewed access should be removed.

Notice why the conclusion follows. The permission is not being removed simply because it is old or because a title changed. It is being removed because its actual capability is no longer needed for the person's approved work.

Now change the work condition. Suppose the reviewer confirms that the person still performs an approved reporting task requiring export.

In that case, keeping the permission can be appropriate. The reviewer records **Approve**, accepting continued access under the conditions being reviewed.

Approve does not mean “create any access this person might be missing.” The permission already exists in this review. The decision concerns whether it should remain.

The useful control is a reasoned decision, supported by the right information. A review in which everything is revoked without understanding the work would not establish that the decisions were appropriate.

## A decision and an application change are different results

Return to the example where the reviewer confirmed that reports-export is no longer needed.

Recording Revoke establishes a decision about access. The application account is a separate record. Its permission must actually be changed to carry out that decision.

**Remediation** is the work needed to carry out the required removal or correction.

The reviewer also needs to finish and confirm the assigned review through its applicable process. This confirmation is called **sign-off** or **finalization**.

The removal needs a supported way to reach the application. Depending on the source's capabilities and configuration, ISC can perform a supported change automatically, or someone can receive a task to make the change in the application.

The important connection is between what was decided and what was actually done. Selecting an item in a review does not itself establish the application's current state.

For a successful removal example, suppose the required review steps are complete, the supported removal work finishes, and a check of the correct application account confirms that reports-export is absent.

That establishes the intended permission removal for this account. It does not mean the whole account was deleted or every other permission was removed.

The three observations fit together like this:

```text
[Earlier approval]
[Export needed for the work]

[Current review]
[Export no longer needed]
              |
[Revoke decision]
              |
[Required review finalization]
[Applicable removal work]
              |
[Application account checked]
[reports-export is absent]
```

The earlier approval explains the original grant. The connected part follows the later decision to its required outcome, under the successful conditions just described.

The final check is a human verification of the account's current permission.

What if the account still has reports-export? The decision may be correct while the removal work is unfinished or unsuccessful.

You would check the review's finalization, the applicable removal work and the correct account's state. You would not conclude that an old approval overrules the new decision, or that selecting Revoke proves the application changed.

## Which information answers which question?

You can keep the reasoning clear by separating the evidence:

| Question | Useful evidence | What that evidence helps establish |
|---|---|---|
| Why was access granted? | Earlier request and approval, when available | The reason accepted at that time |
| Is access still appropriate? | What the permission allows and evidence of current approved work | Whether keeping it is justified now |
| What did the reviewer decide? | The relevant review item and recorded decision | The decision about this access |
| Was the decision carried out? | Review completion, removal work and the correct account's current state | Whether the required outcome happened |

An earlier approval cannot answer every later question. A completed decision record cannot answer every delivery question either.

Dates matter too. Suppose the review shows reports-export, but an application administrator says it was removed afterward.

Those observations may describe different times. The review is based on information collected or generated earlier; a later application check describes a later state.

Compare the same person, account and permission, then establish when each observation was made. Verify the relevant source update and subsequent ISC observation rather than treating every visible record as a live read of the application.

This protects both sides of the decision. Stale information could lead someone to investigate access that is already gone. Missing information could also hide access that still exists.

## Why do this again after one review?

A review answers a question using the access and business information available for that review. Work can change again afterward.

A person may move to another responsibility, finish a project or receive additional access. Access that was justified during the last review can therefore need another assessment later.

Periodic reviews give an organization a deliberate opportunity to ask again. Focused reviews can address a particular population or set of access.

That does not mean every old permission is wrong, or that a completed campaign proves every application account is permanently correct. The value comes from reviewing the intended access with appropriate information and following required changes to their outcome.

When someone asks you to help run a review, your first question is therefore more useful than “How many items can we complete?”

Ask: “What access are we assessing, who can judge its current need, and what evidence will show that the required outcome happened?”

## Try the reasoning with a changed condition

### The earlier approval is still relevant

The account holds reports-export. The reviewer confirms that the person still performs an approved task requiring export.

Should access be revoked just because the approval is several months old?

No. Age alone does not show that the need ended. The evidence supports keeping the permission for the current task. The decision should explain that connection.

### Responsibilities changed, but current need is unclear

The account still holds reports-export. A job title changed, but nobody has established whether export is needed for continuing work.

Does that title change settle the decision?

No. It gives a reason to investigate. Establish the permission's meaning and the current work requirement with someone who has the relevant knowledge. The supplied facts do not justify pretending that continued need has already been confirmed or disproved.

### The review records Revoke, but access remains

The reviewer decided that export is no longer needed. The application account still holds the entitlement. No evidence of completed removal work has been supplied.

Has the intended outcome been established?

No. You know the decision and the observed access, but the delivery evidence is missing. Check finalization and the applicable removal work before identifying the cause. These facts do not yet identify why the change has not happened.

### Two observations describe different times

A review includes reports-export. A later application check confirms that the account no longer holds it.

Must one of the observations be wrong?

No. They may accurately describe different points in time. Confirm the account, permission and observation times, then check how the later source state is reflected in ISC.

## Apply the idea to a different permission

A separate review concerns a permission that allows an account to update supplier bank details.

The permission was approved for a temporary task. That task has ended. The assigned reviewer confirms that the person has no continuing approved responsibility requiring that capability, and the permission is independently reviewable.

Someone says, “It was approved correctly, so another review adds nothing.”

How would you explain the purpose of the review?

The original approval answered whether the access was appropriate for the temporary task. In this case, the reviewer has confirmed both that the task ended and that no continuing approved responsibility needs this permission. Reviewing the existing permission connects that changed need to a current decision.

If removal is required, the decision must be carried out and checked on the correct application account. A recorded Revoke decision by itself does not establish that the bank-detail permission is gone.

In a separate variation, the task has ended but a continuing responsibility is mentioned without supporting information. You would establish that requirement before claiming a definite keep/remove conclusion.

The reason to review approved access is that both work and access can change. Explain the need, make the decision using the relevant evidence, and verify the outcome that decision requires.
