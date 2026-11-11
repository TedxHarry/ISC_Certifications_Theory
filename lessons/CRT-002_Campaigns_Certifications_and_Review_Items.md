# A campaign, a certification and a review item: what is being assigned?

Suppose you are asked to review someone's reporting access. You need to decide whether they should still be able to view reports and whether they should still be able to export them.

Those are two access decisions. SailPoint Identity Security Cloud (ISC) can put them together into a review assigned to you. An administrator can organize your review and other people's assigned reviews in one campaign.

The item, the assigned review and the campaign describe different parts of that work. Let's follow the connections.

## Start with one permission someone already has

An **account** is a person's record in an application or system. **Access** is what that account is allowed to do.

In a reporting application, viewing a report and exporting a report are different permissions. Viewing allows the person to read the report. Exporting allows them to take a copy out of the application. Needing one permission does not automatically establish a need for the other.

ISC keeps an **identity** representing the person. It connects information about them with their accounts and access.

ISC represents an access right as an **entitlement**. In this example, reports-view means permission to view reports, and reports-export means permission to export them.

We need to review these permissions because the person's work may have changed while their account access remained. The decision needs to connect what the permission allows with what the person does now.

## One review item gives you a particular decision to make

Suppose the person is represented by identity-1 in ISC. Their reporting account is reports-user-1, and it holds reports-export.

These labels identify different records. identity-1 identifies the person in ISC. reports-user-1 identifies their application account. reports-export identifies the permission on that account.

Together, they tell us what we are deciding: whether this person should keep permission to export reports through this account.

ISC presents access for a decision as a **review item**. The item needs enough context to establish whose access is being reviewed and which access the decision concerns.

For the examples here, the accounts are correctly linked to their identities and the access information is accurate. Each permission is available as its own review item with Approve and Revoke choices. The permissions are not being reviewed through a larger package, and nothing else requires them to remain or would restore them after removal.

If the person still needs the export permission for approved work, **Approve** accepts keeping that reviewed access. If the permission should be removed, **Revoke** records that decision.

The decision concerns the particular access shown in that item. Approving reports-export here does not approve every other permission on the account. Revoking it does not ask for the whole account to be deleted.

The person whose access is being examined is the **review subject**. The person responsible for judging it is the **reviewer**, also called the certifier. These responsibilities differ, and someone holding access should not be assumed to be its reviewer. In our supplied records, the reviewers are not reviewing their own access.

## A certification is the review assigned to someone

Now add the viewing permission for the same person and account. The reviewer has two items to examine: reports-view and reports-export.

ISC can collect the items into an assigned review. That assigned review is called a **certification**.

You receive the review and work through its contents. You might approve viewing because the person still needs to read reports, and revoke exporting because their current work no longer requires taking copies out.

Making those decisions deals with the individual items. Finishing the assigned review also requires the review's confirmation step: the reviewer confirms that they have completed its decisions.

A certification therefore gives someone a defined set of review work. Its items identify the access questions inside that work.

You may hear certification used more broadly for the activity of reviewing access. When following campaign records, keep the assigned review in mind. It is the record whose contents and current reviewer you need to inspect.

## The campaign brings the assigned reviews together

A **certification campaign** organizes a set of assigned reviews for a particular access-review purpose.

For example, an administrator may arrange a campaign to check selected reporting access. They define the **scope**: which people or access should be included. They also configure how that campaign should operate.

ISC uses those choices to **generate** the reviews and their items. Generation prepares the actual review work. You can then inspect which reviews were created, who has been assigned and what access they contain.

**Starting** the campaign opens the prepared work for reviewers to carry out. Having generated review contents and having started the review are different facts to check.

For our example, generation and starting are already complete. The actual campaign records show Review A assigned to reviewer A, and Review B assigned to reviewer B.

Review A contains two permissions for the first person. Review B contains one permission for a different person:

| Assigned review | Person represented in ISC | Reporting account | Permission being reviewed |
|---|---|---|---|
| Review A | identity-1 | reports-user-1 | reports-view: view reports |
| Review A | identity-1 | reports-user-1 | reports-export: export reports |
| Review B | identity-2 | reports-user-2 | reports-view: view reports |

There is one campaign, two assigned reviews and three review items. We count the review records to get two. We count the permission questions inside them to get three.

```text
Reporting access campaign
|
+-- Review A: reviewer A
|   identity-1 / reports-user-1
|   |
|   +-- Item: view reports
|   +-- Item: export reports
|
+-- Review B: reviewer B
    identity-2 / reports-user-2
    |
    +-- Item: view reports
```

The branches mean contains. The campaign contains the reviews; each review contains its items. They do not show an order in which the reviewers must make decisions.

This grouping is supplied by the example's generated records. In an actual campaign, inspect the grouping ISC produced. An assigned review can contain access for more than one identity, so do not assume that the number of reviews must equal the number of people whose access is included.

## The same permission name can appear in different decisions

reports-view appears twice in the table. One item concerns the first person's account, and the other concerns the second person's account.

The first reviewer might confirm that the first person needs viewing access for their work. That gives a reason to keep viewing on reports-user-1. It does not tell us whether the second person needs viewing on reports-user-2.

The permission has the same meaning, but the people, accounts and work requirements differ. Compare those details before deciding that repeated names represent duplicate items.

The reverse counting mistake is also possible. Review A has only one person's access in this example, but it contains two items. One person can have several permissions requiring separate decisions.

Count the actual items and review records. A familiar access name or a count of people cannot replace that inspection.

## Connect the screen with the work it represents

In the campaign view, an authorized administrator works with the overall campaign and monitors the assigned reviews it contains.

The reviewer opens their assigned certification and examines its contents. The details connect each decision with the relevant identity, account and access.

For identity access certifications, the reviewer experience can organize the information around identities or around access items. Starting with a person helps you see the access being reviewed for them. Starting with an access item helps you find the people whose access to it is being reviewed.

Changing the grouping changes how you examine the information. It does not give anyone an additional permission or create another access grant.

This helps when someone reports, “The review is missing.” First establish what they expected to find. Is the campaign missing, is an assigned certification missing from their work, or is an expected access item absent from an existing certification?

Those observations point to different records. Checking the campaign alone will not establish that a particular item was included or that the expected person received the review.

## Explain progress using the unit you actually checked

Return to Review A and Review B. Suppose the reviewer of A has recorded Approve for reports-view and Revoke for reports-export.

The reviewer has also finished and confirmed Review A. This confirmation is called **sign-off**. In this example, A's review record confirms completion.

Review B still has no decision for its viewing item. That item is **undecided**.

We can now say that two of the three review items have decisions. They are the two items inside A. We can also say that one of the two assigned reviews is confirmed complete.

These statements count different things. The first counts item decisions; the second counts completed assigned reviews. Neither statement is a formula for every progress percentage ISC displays. Check the meaning of the particular status, view or report you are reading.

Review A's completion does not establish completion of the whole campaign. B still has undecided work, and the campaign's own completion state needs to be checked.

A's Revoke decision also does not establish that exporting has been removed from the application account. The required removal work must be carried out and its account result verified.

That work is called **remediation**: acting on the removal or change required by the review. Depending on the supported connection and configuration, it can involve an automated change or a task assigned to someone who makes the change in the application.

So when someone says something is complete, identify what they mean. A saved decision, a confirmed review, the campaign's completion and a successful account change each need the corresponding evidence.

## The people involved have different responsibilities

An administrator prepares and manages the campaign. A reviewer judges whether the access should remain. The person holding the access is the subject of that judgment. Someone may also need to carry out a manual removal.

One person can do more than one of these jobs, but each job still needs its own authority and information.

For campaign administration, ISC permissions determine what actions someone can perform. **Cert Admin** and **Org Admin** are administration levels relevant to defining, generating and starting campaigns. Check the permissions for the action being attempted.

The **campaign creator** is the person who created the campaign. The **campaign owner** has responsibility for the campaign. Those labels help you find the relevant person, but a responsibility label alone does not prove that their account can perform every administrative action.

The reviewer needs enough knowledge of the permission and the subject's current work to make the access decision. Having permission to administer ISC does not, by itself, explain whether the subject needs report export.

Other owners may help explain the access. A **source** is ISC's configuration for the system or account data it manages. The **source owner** is responsible for that source. An **access owner** is responsible for the particular access object.

For example, the owner responsible for reporting access may understand what export allows. Whether that owner actually receives this review depends on the supported campaign design and its configured reviewer choices. Inspect the assignment instead of inferring it from the owner label.

The person assigned a manual removal task can also differ from the reviewer. Follow the actual removal work and its assignment to establish who needs to make that change.

If someone says, “I own the source, so I should be able to start this campaign,” check their ISC permissions for starting it. Ownership of the source and permission to start the campaign are separate facts.

Likewise, knowing the business reason for access does not automatically authorize someone to change campaign settings. Both the assigned work and the allowed action matter.

## The current reviewer may not be the person who made an earlier decision

The **decision maker** is the person recorded as having made a particular decision.

Suppose reviewer A makes a decision and the review is later assigned to reviewer B. The assignment now names B, while the earlier decision history still names A. Both records can be correct.

The assignment tells you who currently has the review responsibility. The decision history tells you who performed that recorded decision and when.

An authorized Cert Admin or Org Admin can also make a decision that is recorded under their own name, even when someone else is the assigned reviewer.

To explain an earlier decision, inspect its recorded actor and time. Using the current reviewer's name would not establish who did the earlier work.

The same distinction helps with review counts. If two certification records are now assigned to one person, there are still two assigned reviews. One person can hold both. Count the review records before treating a difference between reviewer count and review count as an error.

## Work through another set of assignments

A campaign contains three assigned reviews:

- Review P contains two items.
- Review Q contains one item.
- Review R contains three items.

One reviewer currently holds P and Q. A different reviewer holds R.

P has two saved item decisions, but no evidence of its required review confirmation has been supplied. Q and R have no decisions.

Explain how many campaigns, assigned reviews, current reviewers and items these records describe. Then explain what is still missing before you can say that P is complete.

There is one campaign and three assigned reviews. There are two current reviewers because one person holds two of the reviews.

There are six items altogether: two in P, one in Q and three in R. Two of those six items have saved decisions, both in P.

Those saved decisions show that P's items have received decisions. They do not establish that the reviewer finished and confirmed P. Inspect P's confirmation and completion record before claiming that its assigned review is complete. Q and R still contain undecided work.

Now suppose one of P's saved decisions is Revoke. To say the permission is gone, you also need evidence of the required removal work and the resulting access on the correct application account.

The saved decision tells you what should change. The account result tells you whether the change actually happened. Keep that account check connected to the particular item, even when you are reporting progress for the whole campaign.
