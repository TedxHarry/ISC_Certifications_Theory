# Follow one review from access data to a verified outcome

An account still has permission to export reports, although the person no longer needs it.

You want to review that access and, if it should be removed, establish that the required change actually happened.

Where does ISC get the information? How does that information reach a reviewer? What connects the reviewer's decision to the application's account?

Let's follow the same permission through those steps.

## The permission exists in the application first

An **account** is a person's record in a system. Its **access** determines what that account can do.

In this example, account reports-user-1 holds reports-export, which allows the person to export reports from the reporting application. The desired outcome is to remove that particular permission from that particular account.

SailPoint Identity Security Cloud (ISC) represents the person through an **identity**. The identity connects information about the person with their accounts and access.

The account is correctly associated with its identity. The export permission can be reviewed individually. It is not included inside a larger access package that must be reviewed together, and no other access requirement would keep or restore it.

## First, ISC needs information about that account

ISC manages the connection with the application through a configured **source**. The source represents the system or collection of account data being managed. It is separate from the reporting application itself.

A **connector** provides the integration, meaning the way ISC communicates with that type of system or reads its account-data file. Where supported and configured, it also lets ISC send changes to the system.

**Account aggregation** reads account information into ISC. For example, it can bring in the account's identifier and the permissions it holds. A directly connected source reads from the system; a file-based source imports an account-data file.

An **entitlement** is an access right represented from a system. After the relevant account information has been collected and processed, ISC can represent that reports-user-1 holds the reports-export entitlement.

Reading reports-export into ISC records existing access. It does not give the account that permission.

ISC also needs to connect the account with the right person. **Account correlation** matches and associates a source account with an identity using configured account and identity information.

Collection and correlation answer different questions: “What account information do we have?” and “Whose account is this?” Both need to be right before you rely on this person's access details.

For our example, the collected record includes reports-export and the ownership association is correct.

That tells us what ISC represents about the account. It does not tell us whether the person still needs the permission.

It also does not mean ISC is continuously watching every change in the application. A record read earlier and an account checked now can show different access.

## Next, turn the review requirement into actual review work

Suppose the business requirement is to check selected reporting access and remove permissions that no longer support approved work.

An authorized administrator prepares a **certification campaign**, the organized set of access reviews. The campaign's **scope** determines which people or access are intended to be included.

ISC uses the configured selection and applicable review rules to generate the campaign contents. The result needs checking: the right person, the right account, the expected permission and the right reviewer must actually appear.

For this example, generation produces a **review item** for reports-export on reports-user-1. A review item is the particular access presented for a decision, with the person and account context needed to understand it.

The item belongs to a **certification**, an assigned review within the campaign. Its **reviewer**, also called the certifier, is responsible for assessing the access.

Here, the reviewer has the relevant knowledge to judge current need and is not reviewing their own access. The administrator confirms the generated contents and assignment, then starts the campaign so the reviewer can carry out the work.

Notice what changed. Before generation, there were instructions about what to review. After generation, there were actual review records and an assignment. Starting the campaign opened that prepared work for review.

The application's export permission has not been removed by any of those steps.

## The reviewer connects the permission with today's work

The reviewer opens the assigned certification and examines the item.

The access information answers, “What is this person represented as having?” The reviewer also needs evidence about the person's current work to answer, “Should they keep it?”

For our example, the reviewer confirms that the person no longer exports reports and has no continuing approved task or handover requiring that capability.

The right exists on the account, but the current business need has ended. Those facts support removal.

The reviewer records **Revoke**, meaning that the reviewed access should be removed. A comment can preserve the reason: export is no longer required for the person's current approved work.

Now change that fact. If an approved reporting responsibility still requires export, **Approve** can be appropriate. It accepts continued access under the reviewed conditions. It does not request extra access that is absent from the review.

ISC can organize and record the review work. The presence of a permission alone does not supply the business judgment about whether it is still needed.

## Now follow the decision into removal work

After assessing the items, the reviewer confirms the review decisions. This is **sign-off**, or finalizing the assigned review.

A saved Revoke decision and a finalized review are different observations. If you only know that somebody selected Revoke, you have not established that the required review confirmation happened.

ISC needs to process the confirmed decision into the appropriate removal work. Check the campaign's processing state and the resulting activity or task. Selecting Revoke alone does not establish that a change has been sent to the application.

For our example, the review is finalized and the required removal work has been created and is ready to be carried out. These are confirmed facts in the example. We can now follow that work.

**Remediation** is carrying out the change needed to address the review decision. Here, that means removing reports-export from reports-user-1.

The removal work must retain the correct destination: the reporting system, the account and the right to remove. A decision about one account cannot be satisfied by changing a different account belonging to the same person.

## Who actually makes the change?

The answer depends on the source's supported and configured ability to change account access.

For the first path, the integration supports this removal and has the necessary permission to carry it out.

ISC sends the required access change through the integration. The application receives the operation and processes it. **Provisioning** is the process of changing access in systems; it includes removing access as well as granting it.

In the successful result supplied here, the operation completes and the reporting account no longer holds reports-export.

You would inspect the relevant activity to understand what operation was attempted and its recorded result. Then check the required account outcome. A request that has been accepted for processing does not, by that fact alone, show that the application has finished changing the account.

Now change the source condition. Suppose ISC can read this application's account information but cannot write the required access change.

Knowing that export exists does not give the integration permission to remove it. Reading and writing are separate capabilities.

In the manual-removal path, ISC creates work for a person to carry out in the system. The assigned worker needs to identify the required account and permission, make the authorized change, and record the work performed.

Inspect the actual task assignment to establish who must act. The campaign reviewer and the person carrying out the removal can be different people.

Closing a manual task records something about the task. To establish the required outcome, you still need evidence that the correct account's access changed.

## Bring the account result and ISC's information back together

Suppose an authorized check in the reporting application confirms that reports-user-1 no longer holds reports-export after the removal.

Here, the evidence is the account's permission list inspected by an authorized application administrator after the change. It identifies reports-user-1 and shows that reports-export is absent. A list for a different account, or one captured before the change, would not establish this result.

That is evidence about the account in the system being managed, also called the **target system**.

Now suppose ISC's account record still shows reports-export. Has the permission necessarily returned?

First compare when the information was collected. If ISC's displayed record comes from an aggregation before the removal, it describes the earlier account state. It does not establish that the permission is present now.

The account information needs to be refreshed through the appropriate supported collection process. For a file-based source, that requires a new account-data file representing the changed system state; importing the same old file would repeat old information.

In our successful path, collection and processing after the change show that the exact account no longer holds the entitlement. The decision, change record, target-account check and updated ISC information now support the same outcome.

Be clear about the claim you can make: the reviewed export permission was removed from reports-user-1. Establishing that this person can never export information by any other account or method would require a broader investigation.

A generated review can still contain the earlier permission because that is the access it was created to assess. Do not treat the presence of the item in review history as proof that the live account still holds it.

## Put those connections beside each other

The arrows below mean “follow the information or required work to this next point.” They do not show fixed waiting times or a complete set of engine status changes.

People perform the business judgment and confirmation. The source change can be automated or manual. Verification includes checking evidence; the diagram does not make every step automatic.

```text
Application account access
           |
           v
Collected account data
and identity association
           |
           v
Generated review item
in an assigned certification
           |
           v
Reviewer assesses need
and confirms decisions
           |
           v
Applicable removal work
is ready to be carried out
           |
           v
Automated or manual change
on the required account
           |
           v
Target outcome checked
           |
           v
Updated ISC data checked
```

The campaign has its own progress and completion state alongside this work. Follow that state when managing the overall review. Keep the required account outcome attached to its own evidence, even when a campaign is labelled complete.

For an item that is approved, the removal part of this trace does not apply. Preserve the review decision and its reason; approval accepts keeping the reviewed access.

## Use each record for the question it can answer

| Question | Evidence to inspect | What that evidence alone does not establish |
|---|---|---|
| Was the permission represented for the intended person? | Collected account/access data and its identity association | Current business need |
| Was it included and assigned for review? | Generated item, certification and current assignment | A review decision |
| What did the reviewer decide, and why? | Item decision, recorded actor and explanation | Required review confirmation or actual removal |
| Was the review confirmed and removal work created? | Review confirmation and the applicable removal-work record | Successful change in the application |
| What happened to the access change? | Relevant automated activity or manual task, including its account and result | Correct live account state solely from a generic completion label |
| Does the account now lack the reviewed permission? | Suitable target-account evidence after the change, compared with refreshed ISC data | The absence of every other possible route to a similar capability |

The point is to connect evidence. An activity result helps explain the change; an account check establishes the relevant account state. You need the right account and observation time for both to be useful.

## Where would you look when the path stops?

Suppose the permission exists in the reporting application but is absent from the generated review.

There is no review decision to investigate yet. Check whether ISC collected the right account data, associated it with the right identity, and included that access under the campaign's selection and review rules.

Finding the permission somewhere in ISC is not enough. The generated review needs to contain the intended person/account/access relationship.

Now suppose the item shows Revoke, but you cannot find removal work.

Check the review confirmation and applicable campaign processing state. The known decision does not prove that removal work has been created. Do not label the source operation a failure before establishing that an operation was actually issued.

Change the evidence again. A removal operation exists and reports that the application rejected it.

The point needing attention is now the attempted change. Inspect that operation's target and error, and the integration's permission for the required action. Correcting a reviewer's comment would not fix a denied write.

Finally, suppose the application confirms removal but ISC still shows older account information.

Investigate collection and processing after the change. An earlier account record cannot establish that a successful later removal failed.

Each case starts with a different observation. Start with the stage that lacks the record or result you expected.

## Try a different permission and two accounts

An identity has two accounts in a payments system: payments-basic and payments-approval.

The review concerns invoice-approve on payments-approval. That permission allows approving supplier invoices. It is individually reviewable, and no other access requirement would keep or restore it.

The reviewer confirms that the capability is no longer needed, records Revoke and finalizes the review. The applicable removal process creates a manual task for invoice-approve on payments-approval.

The task is later marked complete. Its work note says, “Checked payments-basic; invoice approval is absent.” ISC's account information was collected before the task was completed.

Can you establish that the required removal happened? What should you check next?

The review and task concern payments-approval. The work note describes payments-basic. A check of the other account does not establish the required account's result.

Start by checking invoice-approve on payments-approval using suitable current target-system evidence, and reconcile the task's recorded work with its actual target. Then obtain updated account information in ISC through the supported collection process.

If payments-approval still holds invoice-approve, the required outcome has not been achieved, despite the task's completed label. Investigate the removal work for that account.

If the target check confirms that payments-approval lacks the permission, the account outcome is established for that observation. You still need to reconcile the misleading task note and refresh ISC's older information.

The question is the same throughout: which permission, on which account, changed as a result of which work, and what evidence supports the outcome now?
