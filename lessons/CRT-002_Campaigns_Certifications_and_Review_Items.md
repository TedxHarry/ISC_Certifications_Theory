# A campaign, a certification and a review item: what is being assigned?

An administrator says, “The campaign has started.” A reviewer says, “I have finished my certification.” A report still shows an access item waiting for a decision.

Those statements can all be true. They describe different amounts of work.

Let's connect them, starting with the access someone is being asked to review.

## Start with a person, an account and a permission

An **account** is a person's record in an application or system. **Access** is what that account is allowed to do.

For example, an account in a reporting application may have permission to view reports and a separate permission to export them. Being able to read a report and being able to take a copy out of the application are different capabilities.

SailPoint Identity Security Cloud (ISC) represents the person through an **identity**. It connects information about that person with their accounts and access. An **entitlement** represents an access right from a system, such as permission to export reports.

An access review brings those connections together. A permission may remain on an account after the person's work changes. The review asks whether this particular person should continue to have this particular access now.

The person whose access is being examined is the **review subject**. The person responsible for judging it is the **reviewer**, also called the certifier. These are different jobs: having access does not make someone the appropriate person to approve their own access.

For the records below, the accounts are correctly connected to their identities, and the access information is suitable for the review. Each permission can be reviewed individually. It is not bundled into a larger access package that must be reviewed as a whole, and no separate automatic access requirement would keep or restore it.

## One access decision needs a clear target

Suppose the review contains permission to export reports for account reports-user-1, belonging to identity-1.

Here, identity-1 is simply a label for one person's ISC record. reports-user-1 identifies that person's account in the reporting application. The permission is called reports-export.

The **review item** is the individual piece of access presented for a decision, together with the context needed to identify whose access it is.

Reading only “reports-export” loses part of the question. You also need to know the person and account it concerns.

The useful question is:

“Should the person represented by identity-1 continue to have permission to export reports through account reports-user-1?”

If that access is still appropriate, **Approve** records acceptance of keeping it. If it should be removed, **Revoke** records that decision.

The decision applies to the reviewed access relationship. Approving this item does not approve every permission on the account. Revoking it does not, by itself, mean the entire account should be deleted.

## A certification puts review work in someone's hands

A reviewer may have several permissions to assess. ISC collects the relevant review items into an assigned review.

That assigned review is a **certification**.

Imagine being assigned a review containing two items: permission to view reports and permission to export reports. You examine each item and decide whether it should remain.

You might approve viewing because the person still needs to read reports, and revoke exporting because their work no longer requires taking copies out. Finishing the assigned review means dealing with its contents and confirming the review as required.

So when someone says, “My certification has two items,” they mean that their assigned review contains two access decisions to work through.

The word certification can also describe the general activity of checking access. When you are working with campaign records, use the more precise meaning: the certification is the assigned review.

## A campaign organizes the related reviews

A **certification campaign** brings a set of assigned reviews together for an organized access review.

Its purpose might be to check whether selected reporting access is still appropriate. An administrator defines the intended review scope, meaning which people or access should be included, and the relevant campaign settings.

ISC uses the configured choices to generate the reviews and their contents. Starting the campaign makes that prepared review work available for reviewers to carry out.

Generation and starting answer different questions. “What review work has been prepared?” concerns the generated contents. “Has the review work been opened for reviewers?” concerns starting it.

For our example, the campaign is already generated and started. Its saved records contain two assigned reviews, A and B, with appropriate reviewers. Neither reviewer is reviewing their own access.

An assigned review can contain access for several identities. The number of reviews and their contents are things to inspect in the generated campaign. Do not calculate them by assuming there must always be exactly one review per person.

Let's look at the three access items in those two reviews.

| Assigned review | Person represented in ISC | Reporting account | Access being reviewed |
|---|---|---|---|
| Review A | identity-1 | reports-user-1 | reports-view: view reports |
| Review A | identity-1 | reports-user-1 | reports-export: export reports |
| Review B | identity-2 | reports-user-2 | reports-view: view reports |

Review A is assigned to one reviewer. Review B is assigned to a different reviewer. There are two assigned reviews and three review items in one campaign.

The relationship looks like this:

```text
Reporting access campaign
|
+-- Review A
|   Assigned to reviewer A
|   |
|   +-- Item: view reports
|   +-- Item: export reports
|
+-- Review B
    Assigned to reviewer B
    |
    +-- Item: view reports
```

The branches mean “contains.” They show how the work is organized, not the order in which decisions must happen. The table supplies the person and account context for each item.

Now read the relationship from the bottom upward. An item receives an access decision. That item belongs to an assigned review. The review belongs to the campaign.

A decision on one item therefore tells you something about that item. It does not establish that every item in the review, or every review in the campaign, is finished.

## Why does “view reports” appear twice?

The two reports-view rows concern different accounts belonging to different people.

One decision asks whether identity-1 should keep viewing reports through reports-user-1. The other asks whether identity-2 should keep viewing reports through reports-user-2.

The capability has the same name, but the people and accounts being assessed differ. The reasons for keeping it can differ too.

Suppose the reviewer confirms that identity-1 still needs to view reports. That supports a decision about the first relationship. It supplies no evidence that identity-2 needs the same permission.

This is why a repeated access name alone does not establish a duplicate review item. Compare the subject, account and access context before deciding that two rows represent the same work.

The opposite counting mistake is also easy to make. Review A contains two permissions for one person. There are two items to decide on, although only one person's access is involved in this review.

## How does this connect to what someone sees in ISC?

The campaign view lets an authorized administrator work with the campaign and monitor the reviews it contains.

A reviewer's assigned certification is the work they need to examine. Within it, the reviewer follows the identity and access details to reach the individual decisions.

For identity access certifications, the reviewer experience can organize the contents around identities or around access items. Starting with a person helps answer, “What access is being reviewed for this person?” Starting with an access item helps answer, “Whose access to this item is being reviewed?”

Changing that grouping does not give somebody another permission. It changes how the review information is presented.

There is a record behind each useful part of the screen: the campaign identifies the overall review, the assignment identifies who has review work, and the item connects an access decision with its subject.

That connection is useful when a question sounds vague. If someone says, “The review is missing,” first establish whether they mean the whole campaign, an assigned certification, or one expected access item. Each question calls for a different check.

## Who is responsible for which part?

Preparing the review, judging access and carrying out a removal require different kinds of work.

An administrator needs the appropriate ISC permissions to define, generate and start campaigns. **Cert Admin** and **Org Admin** are administration levels relevant to that work.

The **campaign creator** is the person who created it. A **campaign owner** has responsibility for the campaign. Those labels help identify responsibility; they are not substitutes for checking what an account is permitted to do in ISC.

The **reviewer** is assigned to assess the review contents. That requires enough relevant knowledge to judge whether the access should remain. The person holding the access is still the subject of that decision.

A **source** is ISC's configured representation of a system whose account and access information it manages. A **source owner** is responsible for that source. An **access owner** is responsible for the particular access object.

A source or access owner may have useful knowledge about what a permission allows. Whether such an owner is assigned to review depends on the supported campaign design and configured reviewer choices. The owner label alone does not tell you who currently holds this review.

After a valid removal requirement is established, **remediation** is the work needed to carry out the required access change. That can involve an automated change or work assigned to someone who must make the change in the system.

The assigned reviewer and the person carrying out a manual removal can therefore have different responsibilities. Find the actual removal work and its assignment when you need to establish who must act.

One person may perform several of these jobs. Even then, keep the jobs clear. Knowing how to manage the campaign does not, by itself, supply the business reason for keeping a permission. Knowing the business reason does not, by itself, grant permission to administer the campaign.

## The assigned reviewer and the decision maker can differ

The **decision maker** is the person recorded as having made a particular decision.

Often this is the assigned reviewer. However, a review can change hands, and its decision history may include work done before the change. An authorized administrator may also make a decision that is recorded under their own name.

Suppose a record shows that reviewer A made a decision, and the certification is now assigned to reviewer B. Those facts do not necessarily conflict.

The assignment answers, “Who currently has this review responsibility?” The decision history answers, “Who performed this recorded decision?”

If you need to explain an earlier decision, inspect its recorded actor and time. Copying the current assignee's name would not establish who did the earlier work.

## What does “finished” mean in our campaign?

Return to the two reviews and three items.

Suppose review A now has these recorded decisions:

- Approve reports-view.
- Revoke reports-export.

The reviewer has also completed the required review confirmation. **Sign-off** is the reviewer's confirmation of the review decisions. For this example, review A's completion is confirmed in its review record.

Review B's reports-view item is still undecided, meaning no decision has been recorded for it.

We can now make two precise statements:

- One of the two assigned reviews is confirmed complete.
- Two of the three review items have recorded decisions.

These statements count different units. One counts assigned reviews; the other counts item decisions.

They are counts from the supplied records, not a rule for how every ISC progress percentage is calculated. When reading a percentage or status, check what that particular view or report counts.

Can we say the whole campaign is complete? No. One review still has undecided work, and we have not established the campaign's completion state.

Can we say reports-export has been removed from the application? No. We know that review A contains a Revoke decision and its review completion is confirmed. We have not supplied evidence of the application's access change.

A review decision, a completed assigned review, the campaign's completion state and the account's actual access answer different questions. Keep each statement attached to the record that supports it.

## Use the distinction to choose your next check

Suppose someone reports, “There are two certifications, but only one reviewer.”

Is that automatically an error? The count alone cannot tell you. Two separate assigned review records could name the same current reviewer. Count the review records and inspect their assignments before treating the number of people as the number of reviews.

Now suppose someone says, “The item is complete, so the campaign is complete.”

Ask which item they mean, what its status establishes, and what the other review records show. An item-level result does not supply the state of the whole collection.

Or someone says, “I own the source, so I should be able to start this campaign.”

There are two separate facts to check. Ownership concerns responsibility for the source. Starting a campaign requires the applicable platform permission. Inspect the person's allowed actions rather than inferring them from the owner label.

In each case, naming the right unit turns a broad claim into something you can check.

## Try it with a different set of review records

A campaign contains three assigned reviews:

- Review P contains two items.
- Review Q contains one item.
- Review R contains three items.

The assignment records show that one reviewer holds P and Q, and another reviewer holds R. P has two saved item decisions, but there is no evidence of its required review confirmation. Q and R have no decisions.

How many campaigns, assigned reviews, reviewers and item decisions are represented? What additional evidence would establish that P is complete?

There is one campaign, three assigned reviews and two currently assigned reviewers. The reviews contain six items in total: two plus one plus three.

Two of those six items have saved decisions. They are both in P. Counting people would give two, but counting assigned review records gives three because one person holds two reviews.

P's saved decisions show that its items have received decisions. To establish P's completion, inspect the review's confirmation and completion record. The supplied facts do not establish that step. Q and R still have undecided work.

Finally, suppose one of P's saved decisions is Revoke. What would you need before saying the permission has actually gone?

You would need evidence of the applicable removal work and the resulting access on the correct system account. The decision alone identifies what should change. The account outcome establishes whether that required change happened.
