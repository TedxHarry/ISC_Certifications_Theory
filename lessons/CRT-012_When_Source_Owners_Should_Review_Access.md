# When should source owners review access?

A reporting system is used by people from several departments. Some can download reports, while others can change report definitions and application settings.

You want to establish whether those people should keep that access within this system.

The person responsible for the reporting system can help explain its permissions and assess them against the system's access requirements. That is a useful starting point for a source-owner review.

They still need evidence about the people using the access. Knowing the application does not automatically explain why every account holder needs it.

## Start with the system being reviewed

An **account** is a record used to access an application or system. Its **access** determines what someone using it can do.

SailPoint Identity Security Cloud (**ISC**) keeps an **identity** representing a person and links it with their accounts. A **source** is the configuration in ISC for the system or collection of account data being managed.

The source is not the application itself. The application holds the accounts and enforces their actual permissions. The source in ISC supplies configuration and collected information used to manage and review that access.

A **connector** provides the integration used to read account and access information. Its supported configuration also affects whether ISC can send access changes to the application.

A **source owner** is the responsible owner recorded for that source. During source configuration, an administrator identifies who is responsible for the system.

For example, Reporting Production has owner-610 recorded as its source owner. The label identifies a particular identity in ISC. Recording that ownership does not create a review by itself.

That ownership setting records responsibility. We also need to establish whether the person understands the access, has the business information needed and can perform the assigned review.

## Use source expertise for a source-focused question

A **source-owner review** focuses on access within selected sources, with the appropriate source owners assessing whether that access remains suitable.

It fits a question such as “Which accounts should retain export or administration permissions in the production reporting system?”

The source owner may understand which permissions expose sensitive information, which provide administration and which account arrangements are appropriate for the application.

A manager contributes a different kind of knowledge: what the person currently does and why they might need the access.

For example, the source owner can establish that a permission allows changing report definitions. The person's manager can establish that report administration is no longer part of their job.

Those facts work together. Choosing a source-owner review does not make current work irrelevant, and asking a manager for input does not make the manager the recorded reviewer automatically.

The approach is especially useful for tightly controlled applications whose access requirements need someone familiar with the system. If the owner is only maintaining the connection and cannot explain the permissions, obtain the relevant application expertise before relying on their judgment.

## Keep the ownership and review responsibilities distinct

An **entitlement** represents an access right from a source. An **access owner** is responsible for an access object, such as an entitlement, access profile or role.

An **access profile** is a bundle of entitlements from one source. A **role** can group profiles, direct entitlements or both, across sources.

The owner of one reporting entitlement can differ from the owner of the Reporting Production source.

A **certification campaign** organizes access reviews. A **certification** is an assigned review within it. Its **reviewer** assesses the **review items**, the access presented for decisions.

These records answer different questions:

| Record or responsibility | What it identifies | What still needs establishing |
|---|---|---|
| Source owner | Who is responsible for the source/system | Whether the selected campaign uses that owner as reviewer |
| Access owner | Who is responsible for a particular access object | Whether that object-owner route is the chosen reviewer rule |
| Assigned reviewer | Who has responsibility for this certification | Whether they have suitable information and authority to decide |
| Removal work | The operation or assigned task needed to carry out a change | Who or what must perform it and whether the application changed |

Source ownership does not automatically mean responsibility for every item decision or every later task. Follow the actual campaign assignment and resulting work.

## Follow one source's access into a review

Reporting Production contains information about two application accounts.

Account rep-310 belongs to worker-310 and holds RPT.EXPORT, which permits downloading reports. Account rep-311 belongs to worker-311 and holds RPT.ADMIN, which permits changing report definitions and application settings.

The people work in different departments. Their shared connection for this review is the reporting system, not a shared manager.

**Account aggregation** collects source account information into ISC. **Account correlation** matches and links each account with its owning identity.

For this example, the account values are accurately collected and both identity links are correct. The two entitlements are individually reviewable, outside profiles or roles, with no automatic requirement keeping them.

The administrator selects the intended reporting source and access for the campaign. No exclusion removes these example items. The chosen source-owner route uses the recorded source owner.

The generated review work for these items is actually assigned to owner-610. The review is active and open, owner-610 is authorized to perform it, and neither example item is owner-610's own access.

We have established the information, selection and actual assignment separately. Merely seeing owner-610 in the source configuration would not establish all of that.

## Inspect the source-owner assignment rule you chose

The dedicated Source Owner Campaign lets the administrator select one or multiple sources.

Every included source needs an assigned source owner for this route to generate the campaign. Check that the recorded identity is the appropriate responsible person before generating work.

If a selected source has no owner, address that prerequisite. Do not assume that the campaign creator or an employee's manager will automatically receive its work.

A name added only to make generation possible does not establish knowledgeable, accountable ownership.

Search-based campaigns also offer reviewer options according to the campaign type. Where Source Owner is the supported chosen option, inspect the applicable source ownership and actual generated reviewer.

Do not confuse that with Access Owner. The Access Owner option follows the reviewed access object's ownership rules, which are a different assignment route. A source owner appearing through another route does not make the routes identical.

The sequence to establish for this example is:

```text
Selected source/account/access
              |
              v
Correct collected relationships
and reviewable items
              |
              v
Source-owner reviewer rule
uses recorded source owner
              |
              v
Generated certification
              |
              v
Inspect contents AND assignee
```

The arrows show information and checks needed for this review. They do not prescribe a fixed internal job sequence or promise that later owner changes rewrite existing assignments.

## Judge the access using both kinds of knowledge

The source owner confirms what RPT.EXPORT and RPT.ADMIN allow.

Current work evidence establishes that worker-310 still prepares and distributes the reports, so export is needed. Worker-311 no longer administers the reporting application and does not need the administrative capability.

**Approve** accepts keeping the reviewed access. **Revoke** records that the reviewed access should be removed.

Under those facts, keeping worker-310's export permission and removing worker-311's administration permission can match the intended access outcome.

The source owner's responsibility for the application is not the reason to keep either permission. The reason comes from the capability, the person's work and the application's access requirements.

If the current need is unclear, obtain the missing evidence from the appropriate manager or business contact. A technical description alone does not establish a person's entitlement to sensitive access.

Record a reason that identifies what the person needs and why the actual reviewed permission is appropriate or inappropriate. “I own this source” does not explain that judgment.

## Check each source when the campaign includes several

Suppose the review requirement also includes Reporting Test. That is a separate source with its own owner setting and account information.

Keep production and test references distinct. A readable account name can exist in both systems without identifying the same account or business need.

For the dedicated source-owner route, check ownership for every selected source. The campaign's intended contents and actual generated assignments need to account for each.

If one person owns both sources, that fact does not automatically select both for a campaign. Similarly, selecting several sources does not establish that all their work will belong to one reviewer.

Inspect the actual generated work rather than predicting a universal number of certifications from the number of sources or owners.

The same applies when one application is represented by several sources. Establish which source records cover the intended accounts and permissions before claiming that the application has been fully reviewed.

## Source ownership does not make every permission a separate item

The review still follows ISC's rules for the way access is held.

A permission contained in a person's access profile or role is not automatically an independent entitlement decision. Inspect the actual package and what the presented item covers.

If a package reaches several sources, its scope needs particular attention. Do not reduce a whole-package decision to “remove this one reporting permission” without establishing the actual affected access. Use a supported campaign and reviewer arrangement that can assess the whole presented item.

Some roles are assigned automatically through **membership criteria**, the configured conditions determining who receives them. Their review action is **Acknowledge**, which records examination without overriding those criteria or requesting removal.

A **lifecycle state** is a configured stage in the person's relationship with the organization and can require profiles. Profiles required through the person's current state do not appear individually in certifications.

A source owner can identify an inappropriate requirement or package, but their ownership does not bypass these controls.

Also distinguish a person's assignment from the shared permission definition. Deciding that worker-311 no longer needs RPT.ADMIN does not mean deleting or redesigning RPT.ADMIN for every other account.

## Confirm who is being assessed, especially for unusual accounts

A **review population** is the people, accounts and access intended for the campaign.

Compare that intended population with the complete generated work. A source being selected is not proof that every intended relationship appears.

If an expected account or permission is missing from collected data, investigate collection. If it is linked to the wrong identity, investigate correlation. A correct source-owner field cannot repair either problem.

An **uncorrelated account** has not been matched and linked to an established identity. It can still have actual permissions in the application.

A **machine or service account** is used by an application or process rather than as a person's ordinary login. It needs responsible ownership and an assessment appropriate to that use.

Where supported, ISC provides dedicated review approaches for such accounts. Confirm the actual campaign type and capability; do not assume that selecting a source-owner campaign silently includes every account category.

An employee without a manager relationship is another separate condition. A dedicated Manager Campaign excludes identities without a manager. That is a manager-route prerequisite, not a reason to assume every source-oriented review omits them. Establish what the chosen route and actual generated contents do with that identity.

## An owner change is not proof that existing work moved

A **preview** contains generated campaign information available for validation before starting it. Inspect the actual reviewers and items there, not only today's source settings.

Suppose Reporting Production changes from owner-610 to owner-620 after work was generated. The current source-owner field identifies the newer responsibility. It does not prove that an existing certification has moved to owner-620.

**Reassignment** changes responsibility for supported existing review work. Correcting source ownership and reassigning a certification are different changes with separate evidence.

Use the authorized process for the current campaign state. For example, a reviewer who has signed off has confirmed their completed review; that certification cannot be reassigned through the documented reassignment action.

When the owner is absent or cannot complete the work, arrange a suitable authorized reviewer under the applicable rules. Do not rewrite accurate source ownership merely to redirect one certification.

ISC also prevents someone from certifying their own access. If the source owner has access within the selected population, inspect the actual separate assignment rather than assuming that ownership allows self-review.

## Keep the review decision separate from the actual change

Being a source owner does not automatically grant permission to administer every campaign, change every connector setting or act on a certification assigned to someone else.

It also does not establish that the source connection can write changes to the application.

A source can supply account data for a review while the actual removal requires a supported change process outside that connection. Where automated changes are supported and authorized, the application still needs to receive and apply the intended operation.

After a removal decision, establish what operation or task is required, its actual assignment and the resulting account permissions. The reviewer and the person carrying out a manual change may have different responsibilities.

Check who actually received any manual task. The source owner named as reviewer is not enough to establish that task's assignee.

For worker-311, the required outcome is that the correct reporting account no longer has the inappropriate administrative access. A saved Revoke decision or a completed review is not, on its own, evidence of that result.

## Try a changed owner and a newly included source

Warehouse Production has owner-720 recorded as its current source owner. Earlier, the owner was owner-710.

An existing active review was generated while owner-710 was recorded. Its certification is still assigned to owner-710 and has not been signed off.

The review includes worker-402's warehouse account wh-402 with STOCK.ADJUST, which permits changing inventory quantities. The account data and identity association are correct, the entitlement is individually reviewable outside packages and automatic requirements, and no self-review conflict applies.

Someone says, “The source now says owner-720, so the correct reviewer has the work.”

What does the evidence establish?

It establishes current source ownership. The assigned certification still identifies owner-710. Inspect the campaign and arrange the appropriate supported responsibility change if owner-720 should perform this existing review.

Confirm that the new reviewer is suitable and authorized. The source setting alone does not establish that the assignment changed or that either person made a decision.

Now broaden the requirement to include Warehouse Test. That source has no recorded owner, and the existing generated campaign contains no test-source work.

For a dedicated source-owner campaign including both sources, what needs attention?

Establish responsible ownership for Warehouse Test and satisfy the route's owner prerequisite. Then verify the actual generated inclusion and appropriate assignments for the expanded requirement.

Do not claim the test source is covered because the production campaign is complete. Do not assume a missing test owner sends its work to the creator, or that changing a source setting added test accounts to existing work.

Finally, change the business question. The requirement is to assess one team's current work access across several unrelated applications.

The manager's knowledge of those responsibilities becomes central, with application owners providing the technical meaning where needed. A source-focused review of Warehouse Production alone cannot establish coverage for that broader people-focused question.
