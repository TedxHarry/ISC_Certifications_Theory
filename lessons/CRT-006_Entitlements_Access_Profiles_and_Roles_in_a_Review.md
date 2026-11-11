# Are we reviewing an entitlement, an access profile or a role?

A person still needs to view reports, but no longer needs to export them. In the access review, you find an item called Reporting Access. Its details include both permissions.

Would selecting Revoke remove only export access, or would it also affect viewing?

To answer, we need to know what the item represents. A review can ask about one permission, a package of permissions or a role containing access to more than one system. Let's build that connection from the account upward.

## Begin with what the account can do

An **account** is a person's record in an application or system. Its **access** determines what someone using that account can do.

For example, the reporting application uses two permissions:

- reports-view allows the account to view reports.
- reports-export allows the account to export reports.

These meanings come from the application's access configuration. A readable name helps us discuss a permission, but we still need to establish what it actually allows.

SailPoint Identity Security Cloud (**ISC**) keeps an **identity** representing the person. That identity connects the person's information with their accounts and access. A **source** is the configuration in ISC for the system or collection of account data being managed.

ISC represents an access right from a source as an **entitlement**. If membership in an application group allows exporting reports, that membership can be represented as an entitlement in ISC.

Keep the person, source and account together when inspecting this access. Two accounts can hold reports-export, while only one account's owner still needs to export reports. The permission's meaning can be the same even though the business reason for keeping it differs.

## Put the reporting permissions into one package

Suppose the reporting work requires both viewing and exporting. An administrator defines a package called Reporting Access in ISC and includes reports-view and reports-export.

That package is an **access profile**: a named bundle of related entitlements from one source.

The profile lets ISC refer to the two permissions together. A person can receive Reporting Access as one package, and a review can ask whether they should keep that package.

The package is defined in ISC. The actual reporting account holds the permissions used by the application. Creating a package name does not create a different reporting account or replace the application's permissions.

When someone holds Reporting Access, inspect its contents to understand the access involved. In this example, the package includes both viewing and exporting. Its friendly name does not make export a separate decision inside a review of the complete profile.

An access profile takes its entitlements from one source. To bring reporting access and access from another system together, ISC can use a role.

## Bring access from different systems together

A **role** groups access for a responsibility or purpose. It can contain access profiles, direct entitlements, or both. Its access can come from one source or multiple sources.

Consider a role called Report Reviewer. Here, it contains two access profiles.

Reporting Access comes from the reporting source and includes reports-view and reports-export. Case Read comes from the case-management source and includes cases-read, which allows reading cases.

The role combines those packages. The reporting permissions belong on the person's reporting account; the case-reading permission belongs on their case-management account. Both accounts are correctly linked to the person's identity in this example.

Here are the contents:

```text
Report Reviewer role
|
+-- Reporting Access profile
|   Reporting source
|   +-- reports-view
|   |   View reports
|   +-- reports-export
|       Export reports
|
+-- Case Read profile
    Case-management source
    +-- cases-read
        Read cases
```

Each branch means “contains.” It is a map of this role's access, not the order in which ISC changes the accounts.

This role happens to use profiles for both sources. A role can also include an entitlement directly, without putting it inside an access profile first. Follow the actual contents of the role you are examining.

## Connect the role with one person

The Report Reviewer role can exist in ISC before a particular person receives it. Its **role definition** describes the shared role, including its contents and configured requirements.

An **assignment** connects an access object, such as a role, with an identity. A **role assignment** means that this identity holds that role.

For example, the shared Report Reviewer definition contains Reporting Access and Case Read. One person's assignment connects their identity to that role and the access it provides.

This gives us two different questions. Does this person still need the role? And is the role itself designed with the right access?

Removing one person's assignment addresses the first question. Editing the shared role definition addresses the second and can affect other people who hold it.

We also need to establish how the assignment came about. **Assignment origin** means how the person received the access. An approved request and an automatic membership rule are different origins.

## First review one permission

A **certification campaign** organizes access reviews. When ISC generates the campaign's review work, a **certification** is an assigned review within it. The **reviewer** is the person responsible for that review.

Inside the assigned review, a **review item** presents access for a decision.

Suppose the item is reports-export on the person's reporting account. Here, that entitlement is held outside an access profile or role, and no automatic requirement keeps it. The campaign includes it as an individually reviewable item. The account belongs to the correct identity, and an appropriate reviewer is assigned without reviewing their own access.

The question is whether this person still needs to export reports using that account.

**Approve** accepts keeping the reviewed access. **Revoke** records that the reviewed access should be removed. The reviewer needs evidence about the person's current work to choose between them.

For this item, Revoke concerns reports-export on the specified account. Other reporting permissions are outside that decision. Removing a permission also does not mean deleting the account.

The item tells you the scope of the decision. The person's current work tells you whether keeping that access is justified.

## Now review the reporting package

Consider a different situation. The person holds Reporting Access through an approved **access request**, which asks for access to be added or changed. That request originally provided the package containing viewing and exporting.

The generated review item is the Reporting Access profile.

Open its details and follow both permissions. The review asks whether the person should keep the package, so the decision concerns reports-view and reports-export together.

If neither permission is still needed, revoking the profile can match the intended change. In this example, no other assignment requires either permission.

The review decision must be confirmed through the required review process. The resulting removal work then needs to reach the reporting account. Selecting Revoke alone does not demonstrate that the application has removed the permissions.

Return to the question at the beginning: what if the person still needs viewing, but no longer needs exporting?

The package still contains both. Revoking the complete profile would also affect viewing in this example. The review cannot be described as removing only export while leaving the rest untouched.

Establish an authorized way to retain viewing without export. That could involve an approved viewing-only package, if one exists and is suitable for this person. Inspect its actual contents and the required assignment changes before relying on it.

The reason to pause is concrete: the intended change is smaller than the access covered by this review item.

## A profile can appear even without a request

Suppose an account already has reports-view and reports-export. Where **access profile detection** applies, ISC can recognize during identity processing that the identity holds all the entitlements in Reporting Access and associate that profile with the identity.

**Identity processing** is ISC's evaluation of identity information and access configuration. Here, it is recognizing a complete set of permissions already held.

Detection explains the package represented in ISC. It does not establish that ISC has just sent a new instruction to add those permissions to the application.

Requested and detected profiles can be **certifiable**, meaning eligible for certification review. Whether the profile appears also depends on what the campaign selects and how the person holds the profile.

If Reporting Access appears in a review, inspect how the person holds it. The item alone is not proof that a personal access request exists.

## Review a requested role across its accounts

Now consider a person who requested the Report Reviewer role. The request was approved, and the person holds the role's reporting and case-reading access.

The campaign presents that requested role assignment for review.

The item concerns this person's role assignment, including the access it provides through Reporting Access and Case Read. Inspect both profiles and their underlying permissions before deciding.

Suppose the reviewer confirms that the person no longer needs any of those capabilities. No other assignment requires these example permissions. Revoke can then match the intended removal of this person's requested role assignment.

**Remediation** is the work needed to carry out the required change. **Provisioning** means making access changes in the systems. For this role, the removal work must account for the relevant permissions on both the reporting account and the case-management account.

If the reporting change succeeds but cases-read remains on the case-management account, we have not established the complete intended result.

Follow the evidence through the required review confirmation, the resulting change work and the actual account permissions. A recorded decision and a successful update to one application answer different questions.

The shared Report Reviewer definition still exists for other people. Revoking this identity's assignment is not a decision to delete the role or remove everyone else's assignment.

## An automatic role follows a rule

Change how the role is assigned. Instead of an approved request, a configured rule determines who should receive Report Reviewer.

The rule uses **membership criteria**, meaning the conditions an identity must meet for automatic assignment.

For a simple example, the criterion requires an identity value called workFunction to equal ReportReview. A named piece of information such as workFunction is an **attribute**; ReportReview is the value being compared.

During identity processing, ISC evaluates the person's information against the configured requirement. A matching identity qualifies for the role under that rule. The role's configured access is then governed by that automatic assignment.

The review action changes because the rule continues to control membership. A role assigned through automated membership criteria can only be **acknowledged** in the certification.

The **Acknowledge** action records that the reviewer examined this automatically controlled access. It does not request removal or override the membership rule.

If the role seems wrong for the person, identify which part is wrong. Does workFunction incorrectly say ReportReview, or is the rule assigning too much access to people whose work function really is ReportReview?

In the first situation, correct the inaccurate information through the authorized process and establish that ISC has received the corrected value. The relevant identity processing then needs to evaluate the person against the role criteria again. Inspect the resulting assignment and account permissions to establish what changed.

In the second situation, changing accurate person information would hide the real problem. Investigate which people should receive the role and which permissions it should contain.

Changing a shared rule can affect other identities that meet it. Establish the intended impact before making a correction, then verify the resulting assignments and application access. Acknowledge itself does not make those changes.

## Why the component permissions are not separate decisions

When the person receives Reporting Access through Report Reviewer, the profile is included through that role. ISC does not present it as a separate individual profile decision that bypasses the role.

The same applies to entitlements included through the person's profiles or roles. They are not separate individual entitlement decisions merely because their names can be found in the account's permissions.

For the Report Reviewer example, a role review can therefore concern viewing reports, exporting reports and reading cases without showing three independent entitlement decisions.

Another automatic access requirement can come from a **lifecycle state**: a configured stage in the person's relationship with the organization, such as an active employment state. That state can require access profiles.

Profiles included in the person's assigned lifecycle state do not appear individually in certifications. Their underlying permissions are not independent entitlement decisions to bypass that requirement either.

If you cannot find a component as its own item, follow how the person holds it. Check the containing role or profile, any automatic requirement and what the campaign actually selected.

Absence from the item list does not prove absence from the application account.

The main review contexts now fit together:

| What the item represents | Question for the reviewer | Scope to check |
|---|---|---|
| Individual entitlement | Does this person still need this permission? | Exact source account and permission |
| Requested or detected access profile | Does this person still need this package? | All permissions included in the reviewed profile |
| Requested role assignment | Does this person still need this role? | This identity's assignment and the access it provides across its sources |
| Role assigned through membership criteria | Has the reviewer examined the automatically controlled access? | Acknowledge records the review; the criteria continue to govern assignment |

For a removal decision, also inspect other assignments and requirements before predicting the final permissions. The examples above exclude another assignment keeping the same rights; a different arrangement needs its own investigation.

## Sometimes the shared role itself needs review

Suppose export is unnecessary for everyone using Report Reviewer, rather than only for one person. That raises a question about the role's shared contents.

A **role-composition review** examines the role itself, including its description, membership criteria and included access. It is a different job from reviewing one person's assignment.

The **role owner** is responsible for the role. Responsibility and platform permission remain separate: changing the definition also requires appropriate authority in ISC and an understood effect on the people using it.

Role-composition campaigns currently use the legacy certification experience. “Legacy” identifies the older campaign experience alongside the newer certification engine. Check the actual campaign type and supported experience before interpreting its actions.

A proposed role-definition correction also needs its own application and outcome checks. Do not assume that saving a changed definition immediately changes every member's account permissions.

If only one person has changed responsibilities, removing their assignment and editing the shared role are different possible changes with different effects. Establish the actual requirement before changing something shared.

## Try the decision with invoice access

A person holds a requested role called Payments Approver. It contains two profiles:

- Invoice Approval, from a payments source, contains invoice-read and invoice-approve. These allow reading and approving invoices.
- Supplier View, from a supplier source, contains supplier-view, which allows viewing supplier information.

The person still needs to read invoices and view suppliers. An appropriate reviewer confirms that approving invoices is no longer needed.

The role is the item presented for review. The person's accounts are correctly linked to their identity, and no other assignment supplies these permissions.

Someone proposes revoking Payments Approver and recording that only invoice-approve was removed.

Before accepting that explanation, follow the contents of the role. Which continuing permissions would the proposed decision also affect?

The role includes invoice-read and supplier-view as well as invoice-approve. Under these conditions, removing the whole assignment would affect both capabilities the person still needs. The proposed explanation is narrower than the actual decision.

An authorized replacement arrangement must preserve invoice reading and supplier viewing without invoice approval. Separate approved profiles for those remaining capabilities could serve that purpose if they exist and are authorized for this person.

Inspect those profiles before relying on their names. A replacement called Invoice Read must actually exclude invoice-approve. Plan the necessary assignment changes and verify the resulting rights on both source accounts.

Changing the shared Payments Approver definition would be a different decision, with consequences for other people who use it. One person's changed work does not establish that everyone should lose invoice approval.

Finally, check the intended result: the correct payments account can still read invoices but cannot approve them, and the correct supplier account can still view supplier information. A saved review decision or one completed application update cannot establish all of that.

Now change one fact: Payments Approver is assigned automatically through membership criteria.

The review uses Acknowledge for that role. Selecting it does not remove invoice-approve. Investigate whether the person's information or the shared role requirement needs an authorized correction, preserve the continuing access and verify the resulting account permissions.

In either situation, start with what the review item contains and why this person holds it. Then match the intended access change to the decision or governing requirement that actually controls it.
