# Are we reviewing an entitlement, an access profile or a role?

A review item says Reporting Access. Its details show permission to view reports and permission to export them.

Are you deciding whether one permission should remain, whether the whole reporting package should remain, or whether the person should keep a role that includes that package?

The answer changes the scope of the decision. Let's identify the object before deciding what should happen to its access.

## Start with the right in the application

An **account** is a person's record in a system. **Access** is what that account can do.

SailPoint Identity Security Cloud (ISC) connects information about the person through an **identity**. A **source** is ISC's configured representation of a system or collection of account data.

An **entitlement** represents an access right from a source. It might represent membership in a group that allows an account to export reports.

For our reporting source, reports-view permits viewing reports and reports-export permits exporting them. Those meanings are established by the application's access configuration.

The entitlement identifies a represented right. To understand a person's access, you also need the identity, source and exact account that holds it.

An entitlement's name alone does not establish that every account holding it has the same current business need.

## An access profile groups related rights from one source

An **access profile** is a named bundle of related entitlements from one source.

Suppose the Reporting Access profile contains reports-view and reports-export from the reporting source.

The profile gives those rights a package name that can be used when assigning and reviewing access. Its contents explain what that package actually permits.

The access profile is a package defined in ISC. The account in the reporting application holds the underlying rights. Giving the profile a friendly name does not replace those rights with a new application account.

This distinction is useful in a review. Seeing one profile item can mean that several underlying rights are involved.

## A role can organize access across sources

A **role** groups related access, such as the access needed for a defined work responsibility. In ISC, a role can contain access profiles, direct entitlements, or both. Its access can come from one source or multiple sources.

For example, the Report Reviewer role contains:

- Reporting Access from the reporting source, including reports-view and reports-export.
- Case Read from the case-management source, including cases-read, permission to read cases.

Here, each access profile has entitlements from its own source. The role brings the two packages together.

The person has a correctly associated reporting account and a correctly associated case-management account. The underlying rights belong on those respective accounts.

The example's role contents look like this:

```text
Report Reviewer role
|
+-- Reporting Access profile
|   Reporting source
|   +-- View reports
|   +-- Export reports
|
+-- Case Read profile
    Case-management source
    +-- Read cases
```

The branches mean “contains.” This role uses access profiles, but roles do not universally require that middle layer: a role can also contain direct entitlements.

When you inspect a real role, follow its actual contents. Do not assume its name describes every permission or that all of its access reaches one application.

## An assignment connects the person with the access object

A package definition says what access it includes. An **assignment** connects that access object with an identity.

For a role, these are different facts:

The role definition contains Reporting Access and Case Read.

The identity has an assignment to that role.

Reviewing this person's role assignment asks whether this person should continue to hold the role. It does not, by itself, ask whether the role definition should change for everyone.

**Assignment origin** means how the person received that access. A role might have been requested and approved, or it might have been assigned automatically because the identity met configured criteria.

The object type tells you what is being reviewed. The assignment origin helps explain which review actions are available and what continues to control the access.

## First consider an individually reviewed entitlement

Suppose the reporting account holds reports-export outside any containing access profile or role. No automatic requirement is keeping it, and the campaign includes it as an individual entitlement item.

A **certification campaign** organizes access reviews. A **certification** is an assigned review, and its **reviewer** is the person responsible for assessing the access. A **review item** is the particular access presented for a decision.

For this item, the question is whether the intended person should continue to hold reports-export through that reporting account.

**Approve** accepts keeping the reviewed access. **Revoke** records that the reviewed access should be removed.

The decision's target is that entitlement relationship. It does not mean “delete the account” or “remove every reporting permission.”

The reviewer still needs current business evidence. Correctly identifying the entitlement does not establish whether the person needs it.

## Now consider a requested access profile

Change the access context. The person holds Reporting Access through an approved access request. That requested profile is the generated review item.

An **access request** asks for a supported access change. In this case, the approved request originally provided the reporting package.

The review now asks whether the person should keep the profile, including both viewing and exporting reports.

If neither capability is still needed, Revoke for the profile can be appropriate. After the required review confirmation and applicable processing, its removal work concerns the package's access on the reporting account.

For this example, no other assignment keeps those entitlements.

Now suppose export is no longer needed but viewing remains part of the person's approved work. Revoking the whole profile would also affect viewing in this example.

That is a different requirement. Establish how the needed viewing access will be preserved before treating removal of the complete package as the correct outcome.

A profile decision cannot be interpreted as an isolated decision about whichever component first attracted the reviewer's attention.

## A profile can also be detected from access already held

Not every reviewable profile began with a personal request.

Where access-profile detection applies, ISC can recognize that an identity already holds all the entitlements making up a profile and represent that access through the profile.

Detection identifies the package in access already present. The detection record is not proof that a new grant was just sent to the application.

Requested and detected profiles can be certifiable, meaning eligible for the supported certification review. Inspect the actual profile association and origin rather than assuming a request must exist whenever a profile appears.

## A requested role is a broader assignment decision

Change the context again. The person requested Report Reviewer, and the approved role assignment supplied its reporting and case-reading access.

The campaign presents that requested role for an assignment review.

The decision now concerns this identity's role assignment and the access it provides across the relevant sources.

Suppose the reviewer confirms that none of the role's capabilities are needed anymore. No other assignment requires the example rights.

Revoke can be appropriate for that requested role assignment. **Remediation** is the work needed to carry out the required change. Here, following that work means checking the relevant reporting access and case-reading access on their respective accounts.

One successful change in the reporting application would not establish that the case-management access was removed too.

**Provisioning** means changing access in systems. A certification decision, its required confirmation, the resulting provisioning work and the actual account results are different evidence.

Revoking this person's role assignment does not delete the role definition or revoke everyone else's assignment to it.

## Automatic assignment changes the review action

Suppose Report Reviewer is instead assigned automatically through configured membership criteria.

**Membership criteria** are conditions used to determine who should receive the role. For example, a configured criterion can compare an identity's work-function value with the value required for that role.

ISC evaluates the identity information and access configuration during **identity processing**. The role's assignment requirements therefore continue to control who should hold it.

In a certification, a role assigned through automated membership criteria can only be **acknowledged**. Acknowledge records that the reviewer examined this automatically controlled access. It does not override the membership criteria or request removal of the role.

If the access is inappropriate, identify whether the person's data or the configured role requirement is wrong. An authorized correction belongs there, with its resulting access work and account outcome verified.

Do not falsify accurate identity data simply to make one permission disappear.

If the criterion itself is wrong, changing it can affect other identities that use the same rule. Establish the intended scope before changing a shared requirement.

## Contained access is not a second independent decision

If Reporting Access was granted through Report Reviewer, it is part of that role's access. It does not appear as a separate individually certifiable profile simply because it has its own name.

Likewise, entitlements contained in the person's access profiles or roles are not offered as independent entitlement decisions to bypass their containing object.

Another automatic origin is a **lifecycle state**, a configured stage in the person's relationship with the organization that can define access requirements. Profiles granted through the person's lifecycle state do not appear individually in certifications.

This is why a review can show a role while you know its account has several underlying permissions. The individual permission names are not necessarily separate decision items.

A missing component item does not establish that the person lacks that capability. Follow the containing access object, the assignment origin and the campaign's actual selection.

| Actual review context | What is being judged? | Meaning to preserve |
|---|---|---|
| Individually certifiable entitlement | This person's right on the specified source account | A decision about that entitlement is not a decision to delete the account |
| Requested or detected profile | This person's reviewed access package | Inspect all included rights and other requirements before assuming the full removal effect |
| Requested role assignment | This person's assignment to the role | Its access can reach multiple sources; the role definition and other people's assignments remain separate |
| Criteria-assigned role | The automatically controlled role presented for review | Acknowledge does not replace the criteria or remove the assignment |

## Reviewing a role's contents is a different job

A **role-composition review** examines the role itself: what it contains, its description and the membership criteria associated with it.

That differs from deciding whether one identity should keep a requested assignment to an otherwise appropriate role.

For example, if the role gives every member an unnecessary export capability, the concern may be the shared role definition. Removing one person's assignment would not correct that definition for the remaining members.

The **role owner** is responsible for the role. Changes to its definition also need the appropriate platform authority and an understood impact on the people using it.

In the current campaign split, role-composition campaigns use the legacy certification experience. Identify the campaign type and supported engine before interpreting its actions as though it were an ordinary identity-access review.

Do not turn “this person no longer needs the role” into “remove this access from the role for everyone” without establishing that broader requirement.

## Try a role with only part of its access no longer needed

Payments Approver was granted to an identity through an approved request.

The role contains two access profiles. Invoice Approval comes from a payments source and contains invoice-read and invoice-approve, allowing invoice reading and approval. Supplier View comes from a supplier source and contains supplier-view, permission to view supplier information.

The person still needs to read invoices and view suppliers. An appropriate reviewer confirms that approving invoices is no longer needed. The role is the presented review item. The account associations are correct, and no other assignment supplies these rights.

Someone proposes revoking the entire role and reporting that only invoice-approve was removed.

Does the proposed explanation match the decision's scope?

No. The requested role assignment includes the invoice-reading and supplier-viewing access as well. In this supplied context, revoking it would affect rights that are still needed.

Establish an authorized access arrangement that preserves the remaining approved capabilities while removing invoice approval. For example, separate approved profiles for invoice reading and supplier viewing could preserve those rights without invoice approval, if those profiles exist and are authorized for this person.

Inspect the actual replacement contents and plan the required assignment changes. A change to the shared role definition would need a separate justification and impact assessment.

Then follow the actual required changes on the correct accounts. A saved decision or one successful application update does not establish the complete intended outcome.

Now change the assignment origin: the same role is automatically assigned through membership criteria.

You cannot treat Acknowledge as a Revoke decision for invoice-approve. Inspect the relevant identity data and role requirements, identify the appropriate authorized correction and verify its access results.

The starting check remains concrete: identify the review item, inspect its contents, establish why this person holds it, and match the intended change to the full scope of that object.
