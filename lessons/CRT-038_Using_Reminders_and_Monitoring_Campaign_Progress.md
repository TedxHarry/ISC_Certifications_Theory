# How do reminders and progress monitoring help the campaign?

A reviewer says, “I have selected a decision for every item.”

That sounds like finished work. Before you record the review as finished, there is one more thing to check: did the reviewer also submit the final confirmation?

Now consider another reviewer who has one item left. They understand how to use the page, but they do not know whether the person still needs that permission. Another reminder may bring them back to the page. It will not supply the missing information.

This is why monitoring matters. You need to find what remains unfinished, understand what is preventing it from moving forward, and choose a useful next action.

## First, know which work you are watching

An access review asks whether existing access is still appropriate. An **account** is the record through which a person or service uses an application. **Access** means what that account is allowed to do. For example, a permission to export customer records allows someone to download those records in bulk.

In SailPoint Identity Security Cloud, or **ISC**, a **campaign** organizes a set of these reviews. A **certification** is an assigned review within the campaign. It contains **review items**, the individual access entries on which a reviewer must act.

One certification can contain many items. This matters when you count progress: ten completed item decisions and ten completed certifications are different amounts of work.

The **reviewer** examines the assigned items and records decisions. For an individually reviewed permission, **Approve** means accepting continued access under the reviewed conditions. **Revoke** records that the access should be removed. Choosing Revoke does not itself prove that the application account has changed.

After reviewing the items, the reviewer gives the required final confirmation, called **sign-off** or **finalization**. In ISC's newer, next-generation certification experience, saving the choices and finalizing the review are separate actions. A review with saved choices but no final confirmation is **unsigned**.

If removal is required, **remediation** is the work that carries it out. Depending on the connected system, an integration may make the change, or a person may receive work to change the account. The actual removal needs evidence of its own.

The **campaign owner** is responsible for the campaign according to its configuration. That person or another authorized coordinator follows its progress. Responsibility for following up does not automatically give someone permission to reassign work, change settings or complete other people's reviews. Use the actions allowed for the actual campaign and your assigned responsibilities.

## Let's examine one campaign

Suppose a campaign is active and its deadline has not passed. The deadline is the date by which the review is due.

There are three assigned certifications. The underlying access data and assignments have been checked. Each reviewer has the knowledge and permission needed for their own review and is not reviewing their own access.

The items in this example are permissions that can be reviewed individually. At the time you inspect the campaign, the records show:

| Assigned certification | Item decisions saved | Final review confirmation | What still needs attention |
|---|---|---|---|
| A, containing four items | Four of four | Not signed off | Reviewer must confirm the completed decisions |
| B, containing two items | One of two | Not signed off | One decision needs more information, then the review needs final confirmation |
| C, containing four items | Four of four | Signed off | One required access removal is still pending |

These are supplied example counts, not a reproduction of an ISC screen or its percentage calculation.

There are nine saved item decisions out of ten. You can calculate that nine out of ten is 90%. But what does that percentage describe? Only the share of items with saved choices in this example.

It does not mean 90% of the assigned certifications are signed off. Only C is signed off, so one of the three assigned reviews has reached that point.

It also does not mean that 90% of required removals have happened. C contains one removal requirement, and that removal is still pending.

Whenever you read a progress figure, ask, “What is being counted, and what has to happen before one unit counts as complete?” An item choice, a signed review and a completed removal answer different questions. The label and underlying records determine what the figure can tell you.

Counts also need a time. A report generated before a reviewer finished may still show unfinished work. If you use that report tomorrow without checking for later changes, you may contact someone about work they have already completed.

## Follow the unfinished work to its cause

Start with certification A. The reviewer has saved four choices. There is no remaining item decision to chase in the supplied records.

Ask the reviewer to check that the choices are correct and finish the required sign-off. In the normal next-generation reviewer flow, finishing submits the decisions and moves that certification to the reviewer's Completed tab. If the reviewer chooses to save and return later, the final confirmation has not happened.

After the reviewer says they have finished, check the actual review state. An acknowledgement in an email is useful communication; the recorded sign-off establishes that the review was finalized.

Now look at B. The remaining item is permission to export customer records. The reviewer knows what exporting allows, but has not yet established whether the person's current work requires it.

The useful follow-up asks for that missing fact. For example, the relevant business owner may confirm whether bulk exports are still part of the person's assigned work. The reviewer can then assess the permission against the organization's review criteria, record the reason and complete the review.

“Please approve everything before the deadline” would hide the gap. A progress target cannot establish whether access is justified.

If the reviewer is unavailable or the assignment is wrong, asking more often will not solve the problem. A permitted coordinator needs to investigate the assignment and, where supported, arrange a suitable replacement. **Reassignment** changes who is responsible for the selected review work. The replacement needs relevant knowledge, permitted access and independence from the access being reviewed. Check the actual resulting assignment and what the replacement can open.

Finally, look at C. The reviewer has signed off. In this example, the required removal is due, but has not been completed.

The next person to contact is the person responsible for the actual removal work, or the support team responsible for its automated delivery. First identify the affected account, application, permission and existing operation or task. Ask what is preventing that particular change.

Sending C's reviewer another request to sign off would not move this removal forward. The unfinished work is now elsewhere.

The following map shows how you choose the follow-up. Its arrows describe your investigation, not an automatic routing process inside ISC.

```text
Inspect current campaign and assigned review records
                         |
              What remains unfinished?
                         |
       +-----------------+------------------+
       |                 |                  |
 Item decision      Final review       Required removal
    missing        confirmation missing    pending
       |                 |                  |
 Find missing      Check choices and   Inspect actual
 facts or correct  permitted sign-off  operation/task
 review assignment      |                  |
       |                 |                  |
 Reviewer decides  Reviewer finalizes  Delivery owner
 with a reason     the actual review   resolves due work
       |                 |                  |
       +-----------------+------------------+
                         |
           Recheck the relevant result
```

The three branches can exist in the same campaign at the same time. An unsigned review may also contain undecided items, as B does. In that case, the remaining decisions need attention before the reviewer can finish.

## What an automatic reminder does

A **notification** tells someone that an event happened or work needs attention. A **reminder** brings unfinished work back to their attention.

ISC has different certification messages for different events. Campaign-start messages announce ready review work. Reassignment messages tell a recipient about transferred work. An **email template** supplies the subject and body of a particular message; whole-certification and subject/item transfers have separate templates. A **subject** is the person or other object whose access is being reviewed. A transfer of selected items need not transfer the whole review.

The Certification Due reminder follows a schedule: it begins one week after the review starts and repeats weekly for unfinished active certifications. It is not sent after the deadline. Campaigns lasting fewer than seven days do not receive these scheduled reminders, and this schedule is not editable.

The campaign's notification choice matters too. If notification emails were disabled when the campaign was created, those campaign reminder emails will not reach reviewers through that process.

For a short campaign, waiting for the weekly reminder can therefore leave no useful time for follow-up. The coordinator needs to check work early enough to resolve missing information or an assignment problem before the actual deadline.

Receiving a reminder tells the reviewer to return to the work. The reviewer still needs to inspect the current items, make justified decisions and finish the required confirmation.

The message does not choose decisions, transfer responsibility, extend the deadline or remove an account permission. Those changes require their own supported actions and recorded results.

## When someone says, “I did not receive the email”

First check the work, rather than infer its existence from the mailbox.

Confirm the correct ISC environment, campaign and current assigned reviewer. Ask whether that person can open the actual active certification. A missing message and a missing assignment are different problems.

Then establish which message was expected and when. A reassignment message follows a transfer. A weekly Due reminder is not expected on the second day merely because a deadline is approaching.

Next, inspect the relevant notification controls with the person authorized to manage them:

- The campaign's email choice can suppress its reminders.
- A first subject word of `no_send` or `Stop`, in any letter case, suppresses an email template even when process notifications are enabled.
- Global Email Settings distinguish **Intended Recipients** from **Test Address**. Test Address redirects all notification emails to that address. It changes email delivery, not review assignment.

An enabled campaign setting alone therefore does not prove that an email reached the reviewer. If the controls allow the expected message, investigate available dispatch, address and mail-delivery evidence with the appropriate support team. A message can be generated yet rejected or diverted by the receiving mail system. Do not invent a delivery result when evidence is missing.

Template test messages have limited context: process-specific values may be empty and conditional sections omitted. A successful template test alone cannot establish that a real certification message reached its actual reviewer.

Because the global delivery setting affects other processes too, a correction needs a permitted operator and the organization's change procedure. Follow up on the resulting delivery and review work.

## Make a manual follow-up useful

From the documented campaign reviewer view, the **Email** action opens your default email application with the reviewer's address filled in. Opening that composer is not proof that you sent the message or that the recipient received it.

Before following up, check that you are contacting the current reviewer. A report can retain the person who made an earlier decision even after responsibility moves. The Campaign Status Report separates **Current Reviewer**, who is now assigned, from **Decision Maker**, who recorded a decision.

Also read the field's meaning before relying on the word Complete. For example, the report's **Decision Made** field describes item status. A Complete value there is not a sign-off record for every certification or proof that rejected access is absent from the application.

A useful follow-up identifies the campaign, assigned review, actual due date and specific unfinished action. For B, it should identify the export permission and the information still needed. For A, it should identify the missing final confirmation. Include only information the recipient is permitted to receive.

After contact, check whether the requested result happened. Did the missing fact arrive? Did the correct reviewer finalize the review? Did the removal owner resolve the actual pending work?

Keep a short record of the issue, responsible person, agreed next action and next check time. These are useful coordination details; they do not replace the review's own decisions, comments and history.

If the work is unlikely to finish in time, raise the specific problem with the authorized campaign owner or administrator. Explain what remains, why, who is responsible and what help is needed. Asking for more time in an email does not change the deadline stored on the campaign. Verify any approved change in the actual campaign, where the platform permits it.

## Try a different situation

A campaign runs for four days. On day two, a reviewer says they received no weekly reminder.

An older report names the original reviewer. Current review records show that the certification was validly reassigned to a suitable replacement yesterday. The replacement can open it, but has received no campaign email.

You check the settings with an authorized administrator. Campaign emails are enabled, but global Email Settings still use a Test Address from an earlier email test.

Should you restart the campaign? Which facts explain the missing messages, and what needs attention now?

Start by separating the messages. A weekly Due reminder is not expected in this four-day campaign. Its absence does not show that campaign generation or assignment failed.

For the replacement, investigate the expected reassignment message. The original campaign-start message concerned the reviewer assigned at that earlier time; the replacement should not have to receive that old message to start reviewing now.

Test Address redirects notification emails, so the replacement's empty inbox does not establish that no reassignment message was generated. Check the transfer event and actual delivery evidence. The supplied current assignment and the replacement's ability to open the certification establish where the review work is now.

Use the replacement's current responsibility when arranging follow-up. The old report is a record from before the transfer; it is not the right basis for sending the original reviewer another completion request.

Have the permitted administrator arrange the approved email-setting correction and verify delivery for the relevant real process. Coordinate any needed manual follow-up with the replacement while there is time to review properly. Check the remaining item decisions and final confirmation in ISC afterward. Nothing in the supplied facts calls for a campaign restart or automatic approval of its items.

Now change one fact. The replacement completes all decisions and signs off. One rejected permission is still present on the application account, and its removal work is due.

The email issue and review finalization are no longer the remaining access problem. Follow the matching removal operation or assigned task, establish the cause and verify the account outcome. A corrected mailbox and a signed review do not establish that this permission has been removed.
