# Can the reviewer understand what this access actually permits?

A review item is called Finance Users. Its description says “Finance access.”

The person works in Finance. Is that enough to approve it?

We still do not know what the permission allows. It could provide report viewing, access to supplier bank details or the ability to approve payments. Those are different capabilities, even when they belong to the same application.

Before deciding whether the person should keep the access, let's establish what they would be keeping.

## First identify the account and the permission

An **account** is a record used to access an application or system. Its **access** determines what someone using that account can do.

SailPoint Identity Security Cloud (**ISC**) keeps an **identity** representing the person and connects it with their accounts. A **source** is the configuration in ISC for the system or collection of account data being managed.

An **entitlement** represents an access right from a source. For this example, the production finance account finance-026 holds an entitlement with the value FIN_GRP_42. The account is correctly linked to the person's identity.

The entitlement's **display name** is the readable label shown for it: Finance Users. Its **entitlement description** is the text intended to explain the access: Finance access.

Keep the source and entitlement value with that readable label. A similar name in another system can refer to different access. The application permission and its identifying value give you something specific to investigate.

A **certification campaign** organizes access reviews. A **certification** is an assigned review within that campaign. The **reviewer** assesses its **review items**, the access presented for decisions.

Here, the item is this individual entitlement on the person's finance account. It is not included through a larger package or required by an automatic assignment. The campaign includes it, and an appropriate reviewer is authorized to decide while the review is open, without reviewing their own access.

We know which access is under review. Its capability is the part that needs clarification.

## Turn “Finance access” into an explanation

Begin with the application configuration and someone responsible for understanding that permission.

In this example, that investigation confirms that FIN_GRP_42 allows viewing and downloading supplier-payment reports from the production finance system. Those reports include supplier bank account numbers.

It does not allow changing supplier details or approving payments. Those boundaries have been checked in the application; we are not guessing them from the group name.

Now compare the descriptions:

| Detail | Before clarification | After the application's capability is confirmed |
|---|---|---|
| Display name | Finance Users | Supplier payment report export |
| Description | Finance access | Allows viewing and downloading supplier-payment reports, including supplier bank account numbers, in the production finance system. Does not allow changing supplier details or approving payments. |
| Entitlement value | FIN_GRP_42 | FIN_GRP_42 |

The entitlement value remains the same. We have made the meaning clearer.

Notice what the revised description gives the reviewer. It names the actions, the reports involved, the sensitive information included and the production system. It also prevents confusing report export with payment approval.

A description such as “Read-only access” could still hide an important capability here. Someone may be unable to edit a bank account number but able to download it. Reading, exporting and changing data have different consequences.

Describe the capability the application actually provides. If the permission reaches every supplier-payment report, do not describe it as access only to one team's reports unless that restriction really exists.

## Find the person who can confirm the meaning

An **access owner** is responsible for an access object, such as an entitlement, profile or role. An owner who understands the application can help establish what that access provides and why the organization offers it.

The **source owner** is responsible for the source recorded in ISC. That person may help locate the application administrator or other person who knows the actual permission configuration.

These responsibilities do not automatically make someone the reviewer for this particular certification. Inspect the assigned review to establish who must make its decision.

The responsibilities also answer different questions. The person who understands FIN_GRP_42 can confirm its report and data scope. The reviewer needs evidence about the account owner's current work as well.

If the owner field is blank or the recorded owner cannot explain the permission, identify the appropriate responsible contact through the organization's process. A person's name in the field does not, by itself, prove that the description has been checked.

Likewise, being responsible for access does not automatically give someone permission to edit its details in ISC. The correction needs an authorized operator and an accountable source for the information.

## Separate the access purpose from this person's need

The **business purpose** of access is the work it is intended to support.

For FIN_GRP_42, the purpose in this example is reconciling supplier-payment records with bank information. That explains why such a permission exists.

It does not establish that every Finance employee needs it.

Suppose the person's current responsibility includes that reconciliation, and the reviewer verifies that the work requires the bank details and export capability this permission provides. Under those facts, there is a reason to consider keeping it.

**Approve** accepts keeping the reviewed access. **Revoke** records that the reviewed access should be removed. Choosing between them needs both a correct understanding of the permission and evidence about this person's present need.

Now change the person's responsibility. They only check report totals and no longer perform bank-detail reconciliation.

The description is still accurate, but the reason for this person to hold that broad access has changed. A Finance department label cannot establish that bank details and export are still needed.

Establish what narrower access would meet the continuing requirement, whether it is available and whether the person is authorized to receive it. Correct wording alone does not solve an access arrangement that is too broad.

## Use identity information to understand the work

An **attribute** is a named piece of information on a record. Department, manager and work function are examples of identity attributes. A value such as Finance tells you what that field contains for the person.

ISC can present identity details to help a reviewer. The documented defaults include email, lifecycle state and manager; administrators can configure additional identity attributes for display.

A **lifecycle state** is a configured stage in the person's relationship with the organization, such as active employment. It can explain their status, but an active state alone does not justify every permission.

Additional information such as department or work function can help connect the person to the work. It still needs the right interpretation.

For example, department Finance is broader than responsibility for bank-detail reconciliation. A displayed job title can also be out of date or too general to settle the question.

If the displayed information conflicts with the person's confirmed current work, investigate its source and freshness. Do not change accurate person information just to make an access decision look consistent.

The useful question is what this person actually needs to do now, using which account and which capabilities.

## Check the whole item when access is packaged

An **access profile** is a named bundle of entitlements from one source. A **role** can group profiles, direct entitlements or both, from one or multiple sources.

A review item can represent one of these packages rather than a single permission.

If an item called Finance Reporting includes both ordinary report viewing and supplier bank-detail export, inspect both capabilities. A description that mentions only viewing would leave the reviewer with an incomplete understanding of the package.

You can inspect the included entitlements to understand what the item provides. That inspection does not turn every component into a separate decision.

The review decision applies to the actual item presented. If only part of a package remains needed, establish an authorized arrangement that preserves the required access before treating removal of the whole package as the intended result.

A clearer package description should explain its important included capabilities. It should not make broad access appear narrow by describing only its least sensitive component.

## Understand what a privilege indicator is telling you

**Privileged access** allows sensitive actions or access to sensitive information. Examples include administering a system, changing important configuration or accessing protected records.

The supplier bank details in our finance example need careful attention even though the permission cannot approve a payment or edit a supplier.

**Privilege classification** is how ISC categorizes an entitlement's privilege using configured methods or manual handling. It is information about the access that helps guide investigation.

It is not a statement that this person has an approved business reason to keep it.

A review may show a Contains Privileged Access flag on a profile or role. That points you to included access that is marked as privileged. Inspect the contents to establish which permission creates the concern and what it allows.

It does not mean every included permission has the same capability or sensitivity.

If no privilege flag appears, continue checking the actual permission. Classification may be unset or incomplete. The absence of an indicator cannot establish that an export excludes sensitive data.

Application privileges also do not establish permission to administer ISC. Someone can have powerful rights in the finance system without having authority to change ISC campaign settings.

## Read additional fields as information about a specific record

**Metadata** is information describing an access object. An entitlement could have a configured data-category field or a business-process tag.

These are examples of fields an organization might configure, not guaranteed built-in fields on every review.

If configured by the administrator, the reviewer can inspect an entitlement's Additional Attributes. The reviewer can also inspect an entitlement inside a profile to see its configured additional information.

Keep the fields attached to the right object. Department on the identity describes the person. Data category on the entitlement describes the access. Neither field replaces the other.

Storing information on an access object does not establish that every field is available in the reviewer's screen. Check what the actual review presents.

A field saying “Report totals only” does not outweigh confirmed evidence that the permission exports supplier bank details. Investigate the conflicting value, who maintains it and which information is current.

## Flags and recommendations help with specific questions

An **access flag** draws attention to information about the reviewed access.

For example, New Access means the access has not been certified previously. It does not, on its own, tell you the date the application granted it.

A recommendation is suggested decision-support information. If it is available, inspect the reason behind it rather than treating the suggestion as an explanation of the permission.

Some richer context depends on configuration and other licensed services. Source activity, where available, may help show how an account used a source. An activity observation still needs a time range and an understood meaning.

Recent use does not establish that access is still required. An absence of recorded activity also needs interpretation before treating it as proof that the person never needs the permission.

Use the available information to answer a specific question. It cannot replace understanding the access and the person's present responsibilities.

## Correct the description, then check what the review shows

An **entitlement catalog** is the collection of entitlement records and their details in ISC. The account's membership and the catalog's description are different information: one tells us that the account holds FIN_GRP_42, and the other explains that access.

Entitlement collection can bring names and descriptions from the source. An authorized administrator can also correct the readable display name and description in ISC.

For the finance example, the responsible contact confirms the report capability and the authorized operator updates the appropriate entitlement record. The reviewer then needs to establish what the actual review item shows.

Changing an entitlement's display name or description in ISC does not send those wording changes to the application. It does not remove FIN_GRP_42 from finance-026 or reduce the data that the application permits it to export.

A generated review and the current catalog can also show information from different points in time. Check the presented item after a correction; do not assume that saving a new description rebuilt an existing campaign.

If the old wording remains, establish how the campaign's context and supported correction process should be handled with the responsible administrator. Record the clarification through the permitted process rather than claiming the visible record has changed when it has not.

Where supported, ISC can use generative AI (GenAI) to suggest entitlement descriptions. Those descriptions need approval before they update the entitlement. The actual application capability still needs validation; polished wording is not evidence that the suggestion is accurate.

Here is how the two kinds of understanding meet:

```text
Application capability
        |
        v
Confirmed item meaning
        |
        v
What this access allows
        |
        +----------+
                   v
             Review judgment
                   ^
                   |
          Person's current need
```

The arrows show information used for judgment, not internal ISC job stages. The description carries the access meaning, while current work evidence explains whether this person needs it. Neither answer can supply the other.

## When you still cannot explain the permission

Sometimes the description is vague, the owner is unavailable or two records disagree.

State the specific missing fact. “Need confirmation whether this permission downloads bank account numbers” is more useful than “Access unclear.”

Bring that question to the responsible access or application contact and involve the person managing the campaign when the missing information affects completion. Follow the organization's process for unresolved decisions and deadlines.

Do not invent an answer to finish a row. A blank description is not evidence that access is harmless, and uncertainty alone does not establish that removal is the correct business outcome.

A useful record explains the exact item, the capability confirmed, the person's relevant need, the evidence used and any unresolved point. An old approval or a generic comment such as “same as last time” cannot supply missing current information.

## Try a package whose name understates its access

A person holds a requested access profile called Basic Support on a case-management source. The review presents that profile for a decision.

Its description says “Read assigned cases.”

The profile actually contains two entitlements:

- case-read permits reading cases assigned to the person.
- case-bulk-export permits exporting all customer-case records, including customer contact details.

The application configuration and responsible access owner confirm those capabilities. The case-management account is correctly associated with the person, and the rights are already held. The reviewer confirms that the person only needs assigned-case work. No other assignment requires the example permissions.

No privilege flag is visible.

Someone proposes approving the profile because the description mentions only reading, then correcting the description afterward.

What needs correction in that reasoning?

The description leaves out the bulk export capability and its wider data scope. The missing privilege flag does not narrow what the application allows. The reviewer would be accepting a package containing both permissions, even though only the assigned-case capability has a confirmed need.

Correct the profile's description through the authorized process so that it describes the complete package. Inspect the actual review details and preserve the clarification in the appropriate decision record.

That addresses the explanation. The access requirement needs separate work: establish an authorized narrower arrangement for assigned-case reading, and assess how the broad package should be handled through the supported process.

Revoking the whole profile would also affect the needed reading permission under these conditions. Do not claim that either approving the broad package or revoking it without a preservation plan meets the stated requirement.

Now suppose an administrator changes Basic Support to “Assigned-case reading and full case export.” Has case-bulk-export been removed?

No. The name is more accurate, but the application account still needs its actual permissions checked after any separately authorized access change.

The result we need is an understandable record and an access arrangement justified by the person's work. Correcting one does not establish the other.
