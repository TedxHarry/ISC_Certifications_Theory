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

An administrator configures a **source** in ISC for the reporting application. The source holds the settings for the account data ISC manages. It is separate from the application itself.

A **connector** provides the supported way to read that system or its account-data file. Using that connection, ISC collects the account information. This collection is called **account aggregation**.

The collected information identifies reports-user-1 and its reports-export permission. ISC represents this access right as an **entitlement**.

Collection tells ISC about access the account already holds. It has not granted the permission. It also describes what was read at that time; later application changes need updated collection.

## Connect the account information to the correct person

**Account correlation** associates an account with an identity. Configured matching settings can compare an account's employee number with the corresponding identity value.

For this example, the association has been checked and is correct. ISC connects reports-user-1 and its export permission with the intended person.

Collection and correlation answer different questions: what does the account hold, and whose account is it? A correct permission shown under the wrong person could be judged using the wrong responsibilities. Neither the permission nor the correct identity link establishes that the person still needs export.

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

The reviewer opens the assigned certification and examines reports-export.

The account information shows what the person has. The reviewer also needs to know what work they do now and whether it requires exporting reports.

Here, the reviewer confirms that the reporting responsibility has ended, with no continuing task or handover requiring export. Those facts support **Revoke**, the decision that the reviewed access should be removed. The reviewer records that reason with the item.

If a continuing approved task still required export, **Approve** could be appropriate instead. It accepts keeping the reviewed access; it does not request missing permissions.

We will follow the Revoke case through the required removal.

## Establish that removal work exists before following it

Selecting Revoke records a decision. The reviewer also needs to finish and confirm the assigned review. This confirmation is called **sign-off**, or finalizing the review.

A saved decision and a confirmed review are different results. Knowing that Revoke was selected does not tell you that the review's confirmation step was completed.

The campaign's process determines when confirmed decisions lead to removal work. Inspect the review confirmation, the relevant processing state and the actual activity or task created for the removal.

For the example we now follow, the review is confirmed and the removal work has been created and is ready to be carried out. We have established both facts before investigating the application change.

**Remediation** is the work needed to act on the review's required removal or correction. Here, it means removing reports-export from reports-user-1.

Follow that same permission and account into the removal record. Work that changes another account, even one belonging to the same person, would not establish the required outcome for reports-user-1.

## Follow the path that can make the application change

Changing account access in an application is called **provisioning**. It includes removing permissions as well as granting them.

If the configured connection supports this removal and is authorized to make it, ISC sends the change to the application. The application processes it for reports-user-1. Follow the operation and its recorded result: receiving a request does not necessarily mean the account change is finished.

Now suppose ISC can read the account information but cannot write this access change. Knowing that export exists does not give ISC the ability to remove it.

In the configured manual path, ISC creates a task for a person to make the change. Check the actual task assignment to establish who must act. That worker identifies reports-user-1, removes export through the authorized application process and records the work.

Automatic and manual paths have the same required account outcome. They differ in who carries out the application change and which work record you follow.

## Verify the application account, then check ISC's updated information

The application whose access must change is the **target system**. In our successful example, an authorized administrator checks reports-user-1 after the removal. Its current permission list no longer contains reports-export.

That is evidence about the correct account after the change. A completed manual task or an operation record helps explain the work; the account check establishes the permission result.

Suppose ISC still shows export. Check when its account data was collected. Information read before removal can still describe the earlier permission.

Collect and process updated account information through the supported source process. For a file-based source, use a new file reflecting the changed accounts. Importing the old file again would only repeat the old information.

Here, the refreshed ISC account data also shows export absent. The reviewed permission was removed from reports-user-1. This does not establish that every other account or route to similar access is absent.

The historical review item can remain in the campaign as evidence of what was assessed. Its presence there is different from the current account still holding the permission.

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

## Work through a manual task involving two accounts

A person has payments-basic and payments-approval accounts. The review concerns invoice-approve on payments-approval, allowing approval of supplier invoices. It is individually reviewable, and nothing else requires it to remain.

The reviewer confirms that the duty has ended, records Revoke and finalizes the review. The configured process creates the required manual removal task.

Later, the task is marked complete. Its note says, “Checked payments-basic; invoice approval is absent.” ISC's account data was collected before that task finished.

Can you establish that the required removal happened?

The task identifies payments-approval; the note describes payments-basic. Checking the other account cannot establish the result on payments-approval.

Obtain current evidence for invoice-approve on payments-approval. If the permission remains, investigate and complete the required work through the authorized process. If it is absent, the target result is established for that observation. Clarify the misleading note and refresh ISC's older account data.

The supplied records do not tell us which result is true. They tell us exactly which account needs checking.
