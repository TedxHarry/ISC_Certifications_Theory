# What must be checked before the campaign reaches reviewers?

A campaign preview contains four access items. You expected four. Is it ready to start?

Before saying yes, open the items. One could belong to the wrong account while an intended item is missing. The total would still be four.

The launch check asks a more useful question: does this generated work match the review people are expecting to perform?

## Start with what the review is meant to answer

An **access review** asks whether people still need particular access. A **reviewer** is the person assigned to assess it.

A **certification campaign** organizes that work. An assigned review is also called a **certification**. Within it, a **review item** identifies access awaiting a decision.

For example, a review item could concern one person's permission to export reports from their reporting account. The person, account and permission all matter. Reviewing a similarly named permission on another account would answer a different question.

An **identity** is ISC's person record. An **account** is the record used to access a system. The people, accounts and access a review is meant to include are its **scope**.

Before checking the campaign, put the requirement into concrete words:

“Review the Reporting Production access held by identities 2501, 2502 and 2503. Include their intended production accounts. Exclude Reporting Test. Assign the work to reviewer 2591, who understands this access and can assess the current business need.”

The numbers distinguish the people involved.

The administrator, the person preparing and managing the campaign, needs that requirement before inspecting the result. Otherwise, the generated list can look reasonable without anyone knowing what should have been present.

## Establish what the people actually have

The source-system owner confirms these Reporting Production holdings:

| Person | Production account | Permission and meaning |
|---|---|---|
| 2501 | rep-2501 | View Reports: read reports |
| 2501 | rep-2501 | Export Reports: export report contents |
| 2502 | rep-2502 | View Reports: read reports |
| 2503 | rep-2503 | Export Reports: export report contents |

These are four intended access holdings. A holding means that the particular person has the particular access on the relevant account.

ISC represents these permissions as **entitlements**. Both are individually reviewable in this example. They are not contained in a role or access profile, which group access into larger review objects, and no automatic access requirement changes the example.

Identity 2502 also has Export Reports on account rep-2502-test in Reporting Test. That holding exists, but the requirement excludes it.

In ISC, a **source** represents a connected system or account-data collection. Account collection brings information into ISC. The accounts must also be linked to the correct person records so ISC knows whose access it is preparing for review.

Confirm both relationships. Finding an entitlement in the source's list of permissions does not prove that a particular account holds it. Finding it on an account does not prove that the account is linked to the right person.

The requirement and confirmed holdings give you something to compare with the campaign. They should not be reconstructed merely by copying whatever the campaign happened to generate.

## Inspect the generated work

**Generation** creates campaign review work from the selected scope and available information.

A **preview** lets an administrator inspect that generated work before starting the campaign for reviewers. Saving the campaign settings is a different step: settings describe what should be prepared, while the preview shows what was actually prepared.

Suppose preview C-check contains:

- 2501's View Reports on rep-2501 in Reporting Production.
- 2501's Export Reports on rep-2501 in Reporting Production.
- 2502's View Reports on rep-2502 in Reporting Production.
- 2502's Export Reports on rep-2502-test in Reporting Test.

The total is four. But compare the fourth item with the requirement.

The test-account item is unwanted. Identity 2503's production Export Reports item is missing.

That gives us two findings, not one balancing total. Including an unwanted item does not compensate for omitting another person's access.

For this small campaign, inspect all four holdings and their assignments. A screen may group items by person, reviewer or access object. Follow the underlying person, account, source and access relationships rather than assuming every displayed row represents the same unit.

## Follow the two findings to their causes

In this example, investigation establishes two separate problems.

First, 2503's production permission existed in the application before generation, but it had not yet been collected and associated with the person in ISC. The campaign lacked that input.

Second, the saved campaign choices included all eligible access for the selected people. They did not apply the intended production-only restriction. Because 2502's test-account permission was available and individually reviewable, it appeared in the generated work.

Now the corrections make sense.

The missing production permission requires the relevant data to be collected and connected correctly. The unwanted test permission requires the saved scope to match the production-only requirement.

Changing only the scope would not supply missing account data. Collecting the missing permission would not, by itself, exclude the test account.

After correcting the inputs and scope through supported actions, the administrator deliberately generates a new campaign, C-ready. They inspect it and find exactly the four intended production holdings from the table.

C-ready is a separate example campaign. We are not assuming that a data update or template edit changed C-check automatically.

The administrator checks the actual people, sources, accounts and permissions again. A successful collection, a saved setting or a new generation date is useful evidence about one action. It is not a substitute for inspecting the result that action was meant to produce.

## Check who will receive the work

The configured reviewer choice and the generated assignment also need comparison.

The supported Individual reviewer choice assigns work to a specific selected person. In C-ready, that person is 2591, who is permitted to review, is not reviewing their own access and is actually assigned the expected work.

Then ask whether that person can make a useful assessment. Does 2591 understand what Export Reports permits? Can they establish whether each person still needs it? Are they available during the review period?

An assignment can be technically valid while the assigned person lacks the information needed to decide. Settle that before asking them to approve or revoke access.

**Approve** means deciding the reviewed access should be retained. **Revoke** records a decision that it should be removed. The reviewer needs enough context to choose between them; launch readiness is not permission for the administrator to make those decisions on the reviewer's behalf.

A reviewer rule can also produce an unexpected result when input data is missing. For example, the dedicated Manager Campaign route excludes identities without managers, while the Search route's Manager reviewer option documents assignment to the campaign creator when a manager is missing.

Those are different documented routes. Before accepting an absent person or an unexpected reviewer, establish the route, the relevant manager or owner data and the actual generated work.

Also inspect cases involving a reviewer's own access. ISC has controls to prevent self-certification, meaning reviewing one's own access. Do not try to make the assignment match a spreadsheet by bypassing those controls.

## Choose checks that can find different mistakes

In a large campaign, opening a few familiar items will not establish that every required account was included.

Compare the complete intended and generated populations where the available evidence allows it. Then use selected cases to investigate particular risks and confirm the relationships behind the totals.

A useful selection might include a person with more than one account, a person whose manager changed, an identity with missing ownership information, access held through a role and a person near the boundary of a filter.

Each case has a reason. Multiple accounts can expose a wrong-account mistake. A changed manager can expose a stale assignment. A containing role can explain why a permission is not a separate entitlement item.

A **campaign filter** is saved criteria used to include or exclude review content. Check a case that should pass the relevant criterion and a case that should not. That reveals more than repeatedly inspecting items that all meet the same condition.

There is no universal sample size that proves completeness. A clean sample supports the cases examined. It does not erase a known omission elsewhere.

If a selected case fails, investigate the cause and the other records that could share it. Fixing one visible item is insufficient when the same missing source data or saved condition affects many people.

## Review the deadline and decision settings

The preview's contents can be correct while its settings still make the review difficult to run or different from what was agreed.

The **due date** is the deadline for the review work. Check the actual saved date and how it is displayed to the people using it. Confirm that reviewers have time to assess the work, ask questions and finish it.

A generation date answers when preparation happened. It does not establish how much time reviewers will have after launch.

Next, check when comments are required. If reviewers must explain a removal decision, the setting should support that requirement. A useful comment states why the named access is no longer needed, rather than simply repeating “Revoke.”

Then inspect the policy for **undecided** items, items with no decision. For example, a policy to maintain access to undecided items means leaving those permissions in place when handling unreviewed work at completion. Access can remain even though nobody assessed whether it was needed.

Other supported choices can leave an administrator with a maintain-or-revoke choice for undecided work. That has business consequences. Agree the intended policy before launch instead of discovering it during campaign closure.

Keep undecided work separate from an **unsigned review**. A reviewer may have saved decisions but not performed **sign-off**, the action confirming or finalizing their assigned review's decisions. Those are different facts. Confirm the completion behavior for the actual campaign type before applying a policy to them.

A deadline passing, a saved decision and verified removal in the target system are also different events. Do not describe a launch setting as proof that a later access change has happened.

## Check the communication path, not just its toggle

A campaign email setting tells you whether the configured notifications should be used. It does not prove that the intended person received a usable message.

Check that the planned reviewers can receive the relevant notices and that the message gives them the right campaign context, deadline and way to find their work.

There is a practical setting outside the campaign worth checking: email redirection. ISC's global email settings can redirect notifications to a Test Address. If that remains enabled, a campaign-level email toggle does not make those messages go to the intended reviewers.

Only someone authorized to manage those settings should change them. The setting affects notifications beyond this campaign.

When an email template has been changed, test its presentation using the supported testing process. A template is the saved message layout and text used to create an email.

However, a test email does not populate every campaign-specific value or conditional section. It cannot prove that the complete live notification and assignment path works. Check the relevant configuration and resulting communication separately.

An activation email concerns a campaign that has started. A pre-generation reminder concerns work planned for the future. Neither message should be treated as a replacement for checking the campaign's actual state and assignment.

## Decide what to do with an unresolved finding

Suppose 2503's intended production access is still missing when the planned launch time arrives.

The clock has not changed the requirement. Hold the launch while the responsible people establish the cause and the supported correction, unless an explicitly authorized change to the review requirement permits another approach.

An **exception** is an agreed departure from the normal review requirement. If one is accepted, record what access is affected, why it is outside this campaign, who is responsible for the remaining review and when that work is due. A promised later review is not yet evidence that the access was reviewed.

An exception must not quietly redefine “all production access” as “the items that happened to appear.”

Similarly, if the requirement changes while the preview waits, reassess the affected contents and assignments. Do not assume an older preview follows every current source or manager change automatically.

After correction, inspect the resulting campaign again. Use the current preview and fresh supporting reports available for that route; an old downloaded report does not update when the campaign changes.

## Start the campaign only after the evidence agrees

The checks connect like this:

```text
INTENDED REVIEW
People + source accounts + access + reviewers + settings
        |
        | compare with collected data and generated work
        v
ACTUAL PREVIEW CHECK
Missing work? Unwanted work? Wrong assignment or setting?
        |
        +-- Required work or settings still wrong
        |       |
        |       v
        |   Hold the launch
        |   Correct the cause using supported actions
        |   Inspect the resulting work again
        |       |
        +-------+--> Return to the preview check
        |
        +-- Contents and settings meet the agreed requirement
                |
                v
          Authorized administrator starts this campaign
                |
                | inspect the actual resulting state
                v
          Confirm running work and reviewer access
          Check launch communication separately
```

The branch to hold the launch is an operational decision about an unresolved gap. It is not a claim that ISC automatically detects every business mismatch or blocks the start button.

The return arrow matters. After a correction, you still need to establish that the intended work and settings are now present. Repeating only the generation action would leave that question unanswered.

Once C-ready meets the agreed requirement, the person authorized to launch it starts that particular campaign.

Organizational approval and ISC permission have different roles here. An accountable owner can agree that the review is ready. The account performing Start must also have the required platform authority. Being named as the campaign owner or reviewer is not proof of that authority.

An **API** is an interface through which software requests an action or reads records. The documented next-generation activation API requires an Org Admin or Cert Admin role and a campaign whose state is called staged. That API is marked Experimental, meaning its supported behavior can change.

Its activation request submits a job, work for ISC to process. An accepted request is not confirmation that activation already finished. The Search interface has its own documented Preview Ready and Start Campaign flow. Use the supported action and state for the interface involved.

After requesting the start, verify the actual resulting campaign state. Establish that assigned reviewers can find and open the intended work through the permitted reviewer path. Check communication separately rather than relying only on an email.

Record which campaign was started, who performed the action, when it occurred and what evidence supports the result. This preserves the connection between the accepted preview and the work reviewers actually received.

## Try a launch that looks ready at first

A Warehouse Production review is meant to cover:

- Identity 2601's View Stock permission on ordinary account wh-2601. It allows reading stock information.
- Identity 2602's Adjust Stock permission on elevated account wh-2602-admin. It allows changing stock quantities.

An elevated account has additional permissions for more powerful tasks. These two permissions are standalone, individually reviewable entitlements, with current collected data and correct person-account links in ISC.

Identity 2601 also genuinely holds Adjust Stock on another account, wh-2601-admin. That account is outside the intended review.

The preview contains two items. Someone inspected the first item, 2601's View Stock, and it is correct.

The second item is Adjust Stock on wh-2601-admin, another account belonging to 2601. Identity 2602's intended elevated-account permission is absent.

Campaign email notifications are enabled, but global email settings still redirect messages to a test address. The deadline is tomorrow. Appropriate reviewers have been proposed, but their actual assignments and availability have not been checked.

Should the administrator launch? Which facts need attention first?

### Follow the requirement to the actual work

The matching total of two does not establish correct coverage. The first item passed inspection; the second concerns the wrong person and account.

Compare the saved scope and actual generated contents with the requirement. Investigate why 2602's intended holding is absent and 2601's other account was included. Correct the cause using supported actions, then inspect both intended holdings and their actual assignments in the resulting work.

The correct first item cannot compensate for the second mistake. The deadline does not supply the missing evidence.

Review the time remaining and arrange a workable deadline or an explicitly authorized change to the plan. If the full requirement cannot be met, the responsible owner must decide how the gap will be handled; do not hide it by calling the campaign complete in scope.

The email toggle also leaves a separate gap. An authorized administrator needs to establish the intended global delivery setting and verify the relevant communication path. Changing that setting alone would not repair the wrong review items.

Finally, confirm that the actual assigned reviewers are suitable, available and permitted, then perform and verify the authorized start once the campaign meets its agreed requirement.

Being ready means you can connect the review request to the generated work and account for each difference that affects the requirement. Starting the campaign comes after that explanation holds together.
