# What information should a reviewer inspect before deciding?

You open a review and see an access item, a person's name and an Approve option. The item has a readable description. There may also be flags, a recommendation or activity information.

What would make keeping that access the right decision?

You need to connect what the account can do with what its owner is currently authorized to do. The information on the screen helps you make that connection. A name, a flag or a recent login answers only part of the question.

Let's follow one review closely before adding those other signals.

## First establish whose access you are looking at

SailPoint Identity Security Cloud, or **ISC**, keeps an **identity** representing a person and associates their accounts with it. An **account** is a record in a particular application or system. Its permissions determine what someone using that account can do.

An identity can have more than one account in the same application. For example, identity 3701 has two accounts in Reporting Production: `rep-3701` for ordinary reporting work and `rep-3701-admin` for separately authorized administration. Those purposes have been confirmed for this example. We are not inferring them only from the account names.

The review item we are inspecting belongs to `rep-3701`. Do not use the administration account's purpose to justify a permission on the ordinary account, or assume that deciding on one account decides on both.

ISC manages collected account information through a **source**, its configuration representing the application or account-data collection. The source, account identifier and access identifier help locate the exact access. A similar display name in a test application could describe something quite different.

Here, the source is Reporting Production and the entitlement value is `EXP-CUST`. An **entitlement** represents an access right from the source. The campaign shows its readable name as Export Customer Reports.

A **certification campaign** organizes access reviews. A **certification** is an assigned review within it, and a **review item** is the unit presented for a decision. The **reviewer** is the person responsible for assessing that work.

In this example, the certification is active and unsigned, meaning the reviewer has not yet finalized it. The reviewer has the required permission, understands the access and is reviewing somebody else's access. Current account information is correctly associated with identity 3701. `EXP-CUST` is eligible for individual review and is not included through a larger package or required by an automatic assignment.

These conditions let us focus on the actual access question: should this person keep this right on this account?

## Read the capability behind the label

Export Customer Reports sounds useful, but useful for which task, with which data?

For this example, the application configuration and responsible application owner confirm that `EXP-CUST` allows downloading production customer reports containing customer names and contact details. It does not allow changing application configuration or administering users.

That gives us a capability we can assess. The person can take a copy of customer information out of the application. Calling it “report access” would hide that consequence.

Read the description and available item details to establish the actions, data and scope involved. If the wording is unclear, ask the person responsible for understanding the permission. An **access owner** is responsible for an access object; a **source owner** is responsible for the source recorded in ISC. They can help locate the person who knows the application's actual configuration. A recorded owner still needs current application information to confirm the explanation.

The reviewer screen can show additional information about an entitlement if administrators have configured it. **Additional Attributes** are those extra fields describing the access. A data-category field, for example, could explain that reports contain customer contact information. That example is an organization-defined field, not a field guaranteed to appear in every tenant.

Keep information attached to the right record. Department on the identity describes the person. A data-category field on the entitlement describes the permission. Neither tells you everything the other one tells you.

If the label says “Totals only” but the confirmed permission exports contact details, investigate the conflicting description. A more reassuring label does not narrow what the application permits.

## Connect that capability to current work

Now consider identity 3701's responsibilities. The person's current duty is to investigate delivery problems: check failed deliveries against customer records and contact the correct customers. The responsible business manager confirms that this work requires downloading these customer reports, including contact details, using `rep-3701`. The organization has authorized that use and the handling of the exported information.

Those are supplied facts for this example. They give the reviewer a specific explanation for keeping the access. “The person works in Operations” would be much weaker: many Operations jobs may have no reason to export customer details.

An **identity attribute** is a named piece of information about the person, such as manager or department. ISC can display identity details in a certification; the documented defaults include email, lifecycle state and manager, with additional attributes configurable by administrators.

A **lifecycle state** describes a configured stage in the person's relationship with the organization. An active state can help establish their status, but it does not authorize every permission. Likewise, a job title helps explain a role without proving every account capability is necessary.

Use the identity information to locate and check the work requirement. If the displayed job title conflicts with a confirmed recent change of duties, resolve that difference with the responsible people and records. Do not assume that the screen or an informal message must always be the newer, more authoritative source.

An earlier access-request approval can explain why the permission was originally granted. The present review asks whether the reason still holds. The previous approver did not decide every future change in this person's responsibilities.

## Check when the information was established

Suppose the account information used here was collected on Monday evening. The campaign was generated on Tuesday morning, and the business manager confirmed the current duty on Wednesday afternoon.

These times describe different events. **Account aggregation** is the collection of account information into ISC. Campaign generation creates the review work from the information and settings used for that campaign. The Wednesday confirmation supplies current business context.

The times in this example come from the relevant collection, campaign and business records. They are not a promise that every review screen displays three timestamp fields.

For manager and source-owner campaign generation, the guidance describes a snapshot of information at generation time. Inspect what the actual generated review contains; changing an identity record or access description does not establish that every existing review field was rewritten. A current-looking page can still be showing work generated earlier.

If the application owner says the permission changed on Wednesday, Monday's description cannot settle its current capability. Establish what changed, which account and permission it affects, and what the reviewer is actually being asked to decide. Involve the campaign administrator if the review content needs correction through the appropriate process.

For the ordinary path in our example, there is no such conflict. The collected account, reviewed entitlement, confirmed application capability and current authorized duty agree. Keeping `EXP-CUST` on `rep-3701` has a reason the reviewer can explain.

**Approve** accepts continued access to the reviewed item. **Revoke** records that the reviewed access should be removed. Neither word replaces the reasoning that led to the choice. A removal decision also needs its later required processing and result checks; selecting it is not evidence that the application has already changed.

The diagram shows the connections in the reviewer's reasoning. The arrows are questions to resolve, not a calculation ISC automatically performs to decide whether access is justified.

```text
Locate the exact reviewed access
  Identity 3701 -> rep-3701
  Reporting Production -> EXP-CUST
                 |
                 v
Confirm what the permission allows
  Export customer reports with contact details
                 |
                 v
Connect it to current authorized work
  Investigating delivery problems needs this export
                 |
                 v
Check the evidence agrees and is current enough
  Account, capability, task and relevant dates
                 |
       +---------+----------+
       |                    |
       v                    v
Facts support keeping   Material gap or conflict
this reviewed access    Clarify before deciding

Flags, activity and recommendations help inspection.
They do not supply a missing business justification.
```

## Check what the decision covers when access is bundled

The review item may be an **access profile**, a bundle of entitlements from one source, or a **role**, which can group access profiles and direct entitlements from one or multiple sources.

Open the item and inspect its important included permissions. You may need one component for a task while another gives much broader access. Establish whether the actual item under decision is justified as a whole. Looking at a component's details does not turn it into a separate review decision.

Also establish **assignment origin**, meaning how the person received the access. The origin helps explain the available review action. For example, a role assigned through automated membership criteria can be acknowledged rather than approved or revoked: the role's membership rules control that assignment. **Acknowledge** records the review of that access; it does not override the rule that assigns the role.

A **Birthright Access** flag points to access granted by automated rules, such as lifecycle-state rules. Use it to investigate the assignment, the actual item and the action available. Do not assume it is a direction to keep all automated access, or that selecting removal elsewhere will stop an automatic rule from requiring it again.

## Read flags as reasons to inspect particular details

An **access flag** draws attention to information about the reviewed access. Read what the flag actually says before deciding what it means for the person.

For example, **New Access** means the access has not previously been certified. It does not tell you when the application granted it. An entitlement can have existed for months before its first certification.

A **Contains Privileged Access** flag on a profile or role points to sensitive access inside that package. **Privileged access** allows sensitive actions or access to sensitive information. Inspect which included permission creates the concern and whether the person's work requires it.

A missing privilege flag does not establish that the permission is harmless. Its **privilege classification**, information about how it has been categorized, can be unset. Continue checking the actual capability.

For other flags, use the same reasoning: identify the fact indicated, then ask what it changes about this account's current need. An end date, for example, does not justify unnecessary access until that date. The available flags and richer detail depend on the configured services.

## Look behind a recommendation

A **certification recommendation** is decision-support information supplied through the relevant Recommendations service. Availability depends on the service, campaign settings and supported review type. You do not need a recommendation to reason about access.

When one is present, open its reasons. The analysis can use identity attributes and **peer groups**, groups used to compare identities with similar access patterns. Knowing that similar people hold the access can help you find a possible business explanation.

It does not establish that this person's current task requires every capability in the item. A person who recently changed duties may still resemble others in the recorded information. Equally, uncommon access may have a valid specialist purpose.

For `EXP-CUST`, suppose the panel recommends keeping access because it is common among the person's peers. The confirmed delivery-investigation duty explains why keeping it is justified in the ordinary example. The peer comparison supports the investigation; it does not replace that explanation.

Now change the business fact. The person has finished that duty and is authorized only to read anonymous report totals. The peer comparison and yesterday's source activity remain the same. They no longer establish a reason to keep exporting customer contact details. Investigate the appropriate narrower access arrangement and the required decision on the actual reviewed item.

A missing recommendation is also missing information, not an approval or a rejection. For example, certification recommendations are not provided for role-composition reviews, which assess what a role contains, or uncorrelated-account reviews, for accounts not linked to their owner's identity. Do not copy a recommendation rule from a different review type or guess why a panel is absent.

## Establish what the activity actually measures

**Source activity** is information about events gathered from the application, such as logins. With Activity Insights and a supported configured source, certification context can show how many days an identity was active over a 90-day period.

That information helps ask whether access is being used. Read its period, source and meaning. A login to Reporting Production does not, by itself, establish that the person exported customer reports, used the administration account or needed every permission on the account.

Recent use also does not establish authorization. A person can continue using access after their duty ends. Conversely, an emergency or annual task can have a valid current authorization without recent use.

Distinguish a recorded zero from an empty or unavailable panel. A zero needs an understood measurement period and coverage. An empty panel does not establish that the application observed no activity. Check whether the necessary source and event information is available before drawing a conclusion.

Use activity to investigate access needs, not to judge how well the person performs their job.

## Work through an unfamiliar review

An identity, 3801, has an ordinary Warehouse account and a separate recovery account, `wh-3801-recovery`. The current review item is the **Recovery Operator** access profile on the recovery account. Account collection and the person/account association have been checked.

The profile contains two entitlements:

- **View Stock** permits reading current stock information.
- **Restore Stock Snapshot** permits replacing production stock quantities with values from saved recovery data.

The application owner confirms those capabilities and their scope. The responsible business owner confirms that identity 3801 has a current, authorized annual recovery duty requiring both capabilities on that recovery account. The approved recovery arrangement also requires this account to remain ready between exercises. The profile was requested and is reviewable as a profile. The assigned reviewer is authorized, is not reviewing their own access and is working on an active unsigned review.

The recommendation reasons describe the access as uncommon. The source-activity panel has no usable data. Someone suggests revocation because “almost nobody has it, and the person hasn't used it.”

What do those observations establish?

The uncommon-access reason identifies a question worth checking. The supplied recovery duty answers why this person can legitimately need uncommon access. The empty activity panel does not establish no use. Even a verified zero over a shorter period would need to be considered alongside the annual duty.

Under the supplied facts, the two confirmed capabilities support keeping this profile on this recovery account. If authorization instead covered only a scheduled exercise period, you would need to check whether continued access outside that period was justified. The annual duty alone would not answer that timing question. The supplied arrangement also does not justify copying the same profile to the ordinary account or giving it to everyone in the department.

Now change the profile contents. The application owner discovers a third entitlement, **Delete All Stock Records**, which allows deleting stock records across all warehouses. The current recovery authorization does not include that action.

Would the valid recovery duty justify approving the whole item unchanged?

The item under decision now includes an unapproved capability. The earlier justification covered viewing and restoring stock, so it does not justify this broader profile as a whole. Confirm the actual contents presented in the review and the current application configuration. Involve the responsible access owner and campaign administrator to establish a supported correction or a separately authorized narrower arrangement. Preserve the required recovery work in that plan rather than assume removing the whole profile is harmless.

Do not claim that a description edit removes the deletion permission, that another profile will automatically be granted, or that selecting Revoke has already changed the account. The useful next evidence is the verified package scope, the current business authorization and the supported action that addresses the extra permission. That connects the review decision to the access the account should actually retain.
