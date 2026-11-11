# Follow one review from access data to a verified outcome

Suppose a person's account still has permission to export reports, although their work no longer requires it. You need to review that access and, if removal is justified, confirm that the account actually loses the permission.

SailPoint Identity Security Cloud (ISC) needs information about the access before it can present the review. Someone then needs to judge the current need. The resulting removal also needs a way to reach the application.

Let's follow the permission through those connections, using reports-user-1 as the account being checked.

## Start where the permission actually exists

An **account** is a person's record in an application or system. Its **access** determines what someone using that account can do.

Here, reports-user-1 is an account in a reporting application. It holds reports-export, meaning permission to export reports from that application. The change we will investigate is removal of this permission from this account.

ISC keeps an **identity** representing the person. This identity connects information about them with their accounts and access.

The identity in ISC and the account in the reporting application are separate records. A decision recorded in ISC needs a corresponding application change before we can say that the account's permission has been removed.

For this example, reports-user-1 is the correct ordinary account for the person. The export permission is available for review on its own. It is not part of a larger package that must be reviewed together, and nothing else requires this person to keep the permission or would restore it after removal.

## ISC first needs to read the account information

An administrator configures a **source** in ISC for the reporting application. The source holds the settings for the system or account data ISC manages. It is separate from the application itself.

A **connector** provides the way ISC communicates with that type of system or reads its account-data file. The source settings describe this particular connection; the connector supplies the supported integration.

For a directly connected source, ISC reads account information from the system. For a file-based source, it imports an account-data file containing that information.

This collection is called **account aggregation**. In our example, the collected information identifies reports-user-1 and shows that it has reports-export.

ISC represents an access right from a system as an **entitlement**. The collected information therefore lets ISC show that this account holds the reports-export entitlement.

Nothing was granted by reading this information. The account already had export permission. Collection gave ISC information about that existing access.

The time of collection matters. Information read earlier describes the account at that earlier time. It does not mean ISC is continuously watching every permission change in the application.

## Connect the account information to the correct person

ISC also needs to establish whose account reports-user-1 is. Making the association between an account and an identity is called **account correlation**.

Configured matching settings compare information on the account with information on identities. For example, a configured match can compare an employee number on the account with the employee number on the identity. The values must establish the correct person for the association to be useful.

For our example, that link is correct. The collected account information belongs to the person whose access we intend to review.

Collection and correlation contribute different information. Collection tells us what ISC has read about the account and its permissions. Correlation connects that account with the person's identity.

A correct permission shown under the wrong person could lead the reviewer to judge it using the wrong responsibilities. That is why the account's held access and its identity link both need checking.

At this point, ISC has information showing that the intended person has reports-export through reports-user-1. We have not yet established whether they need to keep it.

## Turn the review requirement into actual review work

Suppose the requirement is to review selected reporting access and remove permissions that no longer support approved work.

An authorized administrator prepares a **certification campaign**, an organized set of access reviews. They define its **scope**, meaning which people or access should be included, and configure the relevant review choices.

Those settings are instructions about the review. ISC uses them, together with the available access information and applicable review rules, to generate the actual review contents.

A **review item** is the access presented for a particular decision. Here, generation produces an item for reports-export on reports-user-1, connected to the correct person's identity.

The item belongs to a **certification**, which is an assigned review within the campaign. Its **reviewer**, also called the certifier, is responsible for assessing the access.

Before starting the campaign, the administrator checks the generated work. Does it contain the intended person, the correct account and the expected permission? Has the review been assigned to the appropriate reviewer?

In our example, those checks pass. The reviewer has enough knowledge to judge the current need and is not reviewing their own access. The administrator starts the campaign, opening the prepared work for the reviewer.

The settings have now produced review records and an assignment. Starting the campaign has made that work available. The reporting account still has its export permission; none of these steps has removed it.

## The reviewer needs evidence about today's work

The reviewer opens the assigned certification and examines the export item.

The account information explains what access the person has. To decide whether they should keep it, the reviewer also needs to know what the person does now and whether that work requires exporting reports.

Here, the reviewer confirms that the person no longer exports reports and has no continuing approved task or handover requiring that permission.

The account still has the right, but the confirmed work requirement has ended. Those facts support **Revoke**, the decision that this reviewed access should be removed.

The reviewer can record the reason in a comment: exporting reports is no longer required for the person's current work. That explanation connects the decision with the business need instead of leaving a later reader to guess why removal was chosen.

Now suppose the reviewer confirms that an approved reporting responsibility still requires export. **Approve** can then be appropriate. It accepts keeping the reviewed access; it does not request unrelated permissions that the person is missing.

The removal steps below concern the Revoke case. For an approved item, keep the decision and its reason; there is no removal requirement from that Approve decision.

## Establish that removal work exists before following it

Selecting Revoke records a decision. The reviewer also needs to finish and confirm the assigned review. This confirmation is called **sign-off**, or finalizing the review.

A saved decision and a confirmed review are different results. Knowing that Revoke was selected does not tell you that the review's confirmation step was completed.

The campaign's process determines when confirmed decisions lead to removal work. Inspect the review confirmation, the relevant processing state and the actual activity or task created for the removal.

For the example we now follow, the review is confirmed and the removal work has been created and is ready to be carried out. We have established both facts before investigating the application change.

**Remediation** is the work needed to act on the review's required removal or correction. Here, it means removing reports-export from reports-user-1.

Follow that same permission and account into the removal record. Work that changes another account, even one belonging to the same person, would not establish the required outcome for reports-user-1.

## Follow the path that can make the application change

The way removal is carried out depends on the source's capabilities and configuration. Start with a connection that supports this removal and is authorized to make it.

ISC sends the required change through the integration to the reporting application. The application then processes the operation on reports-user-1.

Changing account access in a system is called **provisioning**. It includes removing permissions as well as granting them. In this example, the provisioning work removes reports-export.

Suppose the operation succeeds and the account no longer holds the permission. The operation's recorded result helps us understand what was attempted and how the application responded.

An accepted request is a different observation. It can mean the change has been received for processing, without showing that the account change is finished. Follow the relevant operation and its result instead of treating acceptance as completed removal.

Now change the source condition. Suppose ISC can read this application's account information but cannot write the required access change.

Knowing that reports-export exists does not give ISC permission or capability to remove it. Reading account data and making an account change are separate operations.

In the configured manual-removal path, ISC creates a task for someone to make the change in the application. Inspect the actual task assignment to establish who must act. The reviewer who judged the access and the worker carrying out removal may be different people.

The assigned worker needs to identify reports-user-1, remove its export permission through an authorized action, and record what was done.

Closing the task records that the task was marked complete. To establish that the intended change happened, check the actual account result as well. This is especially useful when a work note is unclear or describes a different account.

## Verify the application account, then check ISC's updated information

In our successful example, an authorized application administrator inspects reports-user-1 after removal. The account's current permission list shows that reports-export is absent.

This identifies the account, the permission and the observation after the change. A list captured before removal or belonging to another account would not establish the same result.

The application where access must change is also called the **target system**. The administrator's check is evidence about that target system's account.

Suppose ISC's account view still shows reports-export. First check when its data was collected. If it was read before removal, the view is showing the earlier account information. It does not establish that export permission has returned.

The account information needs to be collected and processed again through the supported source process. For a file-based source, obtain a new file that reflects the changed application accounts. Reimporting the old file would give ISC the old account data again; it would not establish the current state.

In the successful flow here, the updated collection shows that reports-user-1 no longer holds reports-export. The review decision, removal record, current application evidence and updated ISC information now support the same outcome.

The claim is specific: the reviewed export permission was removed from reports-user-1. Determining whether the person can export similar information through another account or route would require broader checks.

The generated review may still show the permission it was created to assess. That historical item is part of the review evidence. Its continued presence in review history does not prove that the application account still has the permission.

## Connect the records along the flow

```text
Account has export permission
           |
           v
ISC reads account information
and links it to the person
           |
           v
Campaign creates review item
and assigns the review
           |
           v
Reviewer judges current need
and confirms the decisions
           |
           v
Required removal work exists
           |
           v
Remove export automatically
or through an assigned task
           |
           v
Check the application account
           |
           v
Check updated ISC account data
```

The arrows connect the information and work needed for the removal example. They do not prescribe fixed waiting times or every campaign status change.

The reviewer supplies the business judgment and confirmation. The application change can be automatic or carried out by a person. The final checks require evidence; the diagram does not make every step automatic.

The campaign also has its own progress and completion state. Check that state when managing the overall review, while following the account result through its own evidence. A campaign label alone cannot replace the account check.

## Match each question with the record that answers it

| Question | What you inspect | What still needs separate evidence |
|---|---|---|
| What access did ISC collect for this person? | Account information and its identity link | Whether the access is needed for current work |
| Did the permission reach the assigned review? | Generated item, certification and reviewer assignment | Whether the reviewer made a decision |
| What was decided and why? | Item decision, recorded actor and explanation | Review confirmation and actual removal |
| Was removal work created after the required review processing? | Review confirmation and the removal activity or task | Whether the application change succeeded |
| What change was attempted and what result was recorded? | Automated operation or manual task, with account and result | Whether the intended account now lacks the permission |
| Has the required account outcome been established? | Current target-account evidence and subsequently updated ISC information | Whether every other account or route to similar access is absent |

The records help explain different parts of the same work. An operation result tells you about the attempted change. The account check tells you about the resulting permission on the account. Keeping the account reference and observation time with the evidence helps you connect them correctly.

## Investigate the point where the expected result is missing

Suppose the permission exists in the reporting application but does not appear in the generated review.

Check whether ISC collected the intended account and permission, linked the account to the correct identity, and included the access under the campaign's selection and review rules. Finding the permission somewhere in ISC does not establish that this campaign generated the intended item.

Now suppose the review contains Revoke, but you cannot find removal work.

Check the review confirmation and relevant campaign processing. Establish whether an operation or task was actually created before treating this as a failed application change.

If an operation exists and the application rejected it, inspect that operation's account, permission, error and authorization. The problem needing attention is the attempted change. Editing the reviewer's reason would not repair an application denial of the removal operation.

Finally, suppose the application check confirms that the permission is gone, while ISC still shows older data.

Check collection and processing after removal. Establish what data was read and when. Earlier ISC information cannot establish that a successful later application change failed.

These observations lead to different checks because they occur at different points in the flow.

## Work through a manual task involving two accounts

A person's identity has two accounts in a payments system: payments-basic and payments-approval.

The review concerns invoice-approve on payments-approval. This permission allows approving supplier invoices. It is individually reviewable, and nothing else requires it to remain or would restore it after removal.

The reviewer confirms that invoice approval is no longer needed, records Revoke and finalizes the review. The applicable removal process creates a manual task for invoice-approve on payments-approval.

Later, the task is marked complete. Its work note says, “Checked payments-basic; invoice approval is absent.” ISC's account information was collected before the task was completed.

Explain what you can establish from those records and what you need to check before claiming that the required removal happened.

The review and removal task identify payments-approval. The note describes payments-basic. Even a correct check of payments-basic would not establish the result on payments-approval.

Check invoice-approve on payments-approval using suitable current application evidence. Reconcile the task's recorded work with the account it was supposed to change, then obtain updated account information in ISC.

If payments-approval still has invoice-approve, the required account outcome has not been achieved. The task's completed label cannot establish otherwise. Investigate and address the removal work for that account through the authorized process.

If the application check confirms that payments-approval lacks the permission, the account outcome is established for that observation. You still need to clarify the misleading task note and refresh ISC's older information.

The supplied task note does not tell us which of those outcomes is true. The correct next check concerns the intended account, so the later conclusion can follow the evidence rather than the completion label.
