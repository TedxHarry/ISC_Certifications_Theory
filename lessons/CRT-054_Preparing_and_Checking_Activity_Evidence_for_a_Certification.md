# How do you prepare and check activity evidence for a certification?

An account's reporting access appears in a certification, but the activity area has no usable information.

Someone says, “The account was collected successfully. If there's no activity, the person must not use it.”

Let's check that reasoning. Collecting an account tells ISC what access it holds. Collecting activity tells ISC about observed actions. One can succeed while the other is not configured.

Before using an empty panel to support a decision, we need to establish how the activity should reach it.

## Start with the two kinds of information

In SailPoint Identity Security Cloud (ISC), a **source** is the configuration for a system or collection of account data. A **connector** is the integration used to obtain that information.

An **account** is a record used to access a system. ISC associates accounts with an **identity**, its representation of a person in this example.

Our source is Entra Production, using the Microsoft Entra ID SaaS connector. **SaaS** means software as a service; here, the supported connector can provide account and activity information through one configured integration.

The account acct-18 holds the group Reports-Readers. In ISC, that group is represented as an **entitlement**, an access right from the source. The application owner has confirmed that this group permits reading reports in the reporting application.

The collected account information establishes group membership. It does not tell us whether a report was read.

An **activity event** records an observed action, such as a sign-in, with information about who acted and when. **Activity Insights** collects supported activity information and makes it available as context in ISC.

Those observations have their own meaning. A sign-in recorded by Entra is not proof that the person read a report or used every permission granted through the group.

## Confirm the supported collection route

First establish that Activity Insights is available in the ISC environment and that the source's connector supports it.

Do this for the actual connector being used. Two sources for the same product can use different integration types.

Supported applications can use a SaaS connector with activity collection enabled. Other supported arrangements use a separate Activity Insights connector alongside a virtual-appliance connection. A **virtual appliance** is software running on the organization's infrastructure to support applicable integrations.

Our example uses the single SaaS route. We do not add a second activity source simply because another configuration needs one.

The administrator must be permitted to manage the source. That permission is separate from the integration's permission to read information from Microsoft Entra.

## Check what the integration is allowed to read

The connector connects using its configured credentials. These identify the software connection; they are not the employee's credentials being reviewed.

**Authentication** establishes who is connecting. **Authorization** determines which operations that connection can perform.

A connection can read user accounts without having the permissions needed to read sign-in activity.

For the Microsoft Entra ID SaaS Activity Insights feature, confirm the required Entra P1/P2 licensing and the appropriate Microsoft Graph permissions. **Microsoft Graph** is the interface the integration uses to read this Microsoft information.

The activity configuration needs access to user information, licensing information, sign-in logs and application information. For example, **AuditLog.Read.All** permits reading the relevant audit/sign-in information. It is only part of the required permission set.

The permission type must match how the connection authenticates. Required **administrator consent**, approval of the integration's permissions by a Microsoft administrator, must also be in place. The integration administrator should check the complete current requirements for that source.

Do not solve an activity-read problem by giving the employee more access to reports. The missing permission belongs to the software integration.

## Enable collection and check the resulting information

For this example, the administrator finds that Activity Insights was never enabled on Entra Production.

Open the intended source under **Admin > Connections > Sources**. In its **Activity Insights Settings**, select **Enable Activity Insights** and **Save**.

**Account correlation** associates the application account with the appropriate ISC identity. **Aggregation** collects the source's account information. For this Entra SaaS route, test the connection successfully, check that the accounts are associated with the correct identities, and run the account aggregation.

The account association connects this work to the right person. If acct-18 belongs to one person but ISC associates it with someone else, its activity can be interpreted in the wrong person's context. Check the resulting account link.

Saving a setting, testing a connection and observing useful activity are different checkpoints.

For this Entra integration, activity can take up to 24 hours to appear initially and is then updated daily. That timing belongs to this integration. It does not promise that every connector refreshes on that schedule or that enabling collection reconstructs a complete previous 90 days.

Check what was actually collected and which dates it covers.

In our example, the administrator confirms that the required permissions are present, the connection test succeeds and acct-18 is associated with the correct identity. After the integration's processing, usable activity is available for that identity and source.

These are the results we need to establish. Merely finding the checkbox selected would leave the collection outcome unknown.

## Check what the reviewer can actually see

A **certification campaign** organizes access reviews. A **certification** is an assigned review within it.

The reviewer opens **Certifications > Active**, selects the relevant review and inspects the source activity available for the person's reviewed access.

For our example, this is an active review the person is authorized to perform. It contains Reports-Readers on acct-18 from Entra Production.

Check that exact context. Another person's activity or activity from a test source cannot explain this production review.

The two information paths meet at this check:

```text
Account information              Activity information
  Who holds which rights?         Which events were observed?
           |                               |
           v                               v
Collect accounts and access      Collect supported events
           |                               |
           v                               v
Check identity/account link      Check source, identity,
                                 event meaning and dates
           |                               |
           +---------------+---------------+
                           |
                           v
                Inspect the actual review
                What evidence is available?
                           |
                           v
                Use it for the question
                it can actually answer
```

The left side establishes the account and its rights. The right side establishes the available observations. Both need checking before the reviewer can explain what the activity adds.

If activity is available elsewhere in ISC but missing from this review, we have confirmed collection but still need to check the review. With the campaign administrator, check whether the feature is available for this campaign and whether you are inspecting the same source and identity.

Do not assume that changing the source configuration rebuilt an existing campaign. Confirm the supported handling for that campaign before changing or replacing review work.

## Read the measurement before drawing a conclusion

The certification activity context can show how many days an identity was active during a 90-day period.

Suppose our checked view shows activity on two days. That does not mean two logins. Several recorded events on one day can still concern only one active day.

It also does not establish that Reports-Readers was used. Our observation concerns Entra source activity; the permission under review permits reading reports in another application. The activity's event meaning must support the question you are asking.

Check how much of the displayed period has usable records. A panel presenting a 90-day period does not establish that your integration successfully obtained every relevant event for all 90 days.

For our supplied case, the available records support activity on two identified days. We retain that limited statement. We do not call it a complete history of report use.

## When the evidence is missing, find the failed check

Different observations need different follow-up:

| What you establish | What it means for the investigation |
|---|---|
| Activity collection was not enabled | There was no configured activity collection through that setting. Enable it through the authorized process and check the resulting data. |
| The activity read fails because required integration permission is missing | Repair that permission through the integration administrator, then test and check collection again. Account collection alone does not resolve it. |
| Events exist, but the person, source or dates do not match the review | Resolve that mismatch before using the observation. A real event can still concern a different person, system or period. |
| A checked result is zero, and you know which events and dates were covered | None of the measured activity was recorded within that coverage. Assess that result alongside the person's current authorized work. |

A blank or unavailable panel is not the fourth row. It has not established a measured zero.

If permission and connection checks pass but expected events still do not appear, establish whether the source records those events and whether they fall within the integration's supported collection. Retain the relevant error or missing-data evidence when involving the integration team.

Repeatedly generating campaigns would not repair a failed activity read.

## Keep evidence repair separate from the access decision

After the activity becomes usable, we know more about the observation. We still need to know whether this person currently requires report reading.

Confirm the actual permission capability and the person's authorized reporting duties with the responsible application and business contacts.

Recent activity does not supply missing authorization. A person can continue using access after their duty has ended. Equally, a currently authorized task may not occur during the observed period.

Record what the activity establishes, its source and dates, and the current-work evidence used for the decision. State any remaining gap.

If the evidence cannot be resolved before the review deadline, involve the campaign administrator and follow the approved handling for unfinished work. Do not invent an approval or removal merely to fill the row.

## Try an identity with two accounts

An identity has an ordinary Entra account and a separate administration account. The review concerns a group on the administration account.

The activity summary for this identity on the Entra source shows five active days. The integration only began collecting usable information last week.

Can you conclude that the administration group was used on five days and was unused for the rest of the 90-day period?

Neither conclusion follows from those facts.

First establish which accounts and events contributed to the summary. Without that detail, activity shown for the identity on this source does not tell us that the administration account caused those five active days.

Then check which dates have usable records. One week of usable collection cannot establish what happened throughout the earlier period.

The useful next step is to obtain evidence for the administration account and the specific access question, while confirming its current approved purpose. Keep the observation as narrow as the information supports.
