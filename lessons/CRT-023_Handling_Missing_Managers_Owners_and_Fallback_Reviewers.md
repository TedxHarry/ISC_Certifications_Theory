# What happens when a manager or owner is missing?

A campaign is configured for managers to review access. One employee has no manager recorded in ISC.

Does ISC leave the review unassigned, send it to an administrator or leave the employee out?

The answer depends on the campaign route. A missing relationship can cause exclusion in one route and an alternative assignment in another.

Before investigating the result, establish which campaign was created and what information ISC actually had.

## First, identify the missing relationship

An **identity** is ISC's person record. An **account** is the record used to access a system.

Suppose identity 2901 has account rep-2901 in Reporting Production. It holds Export Reports, which allows exporting report contents.

ISC represents this permission as an **entitlement**. It is individually reviewable here, without a containing access profile or role. Those objects group access and can change which object is reviewed.

The account and permission have been collected into ISC and linked to the correct person. The missing information is the person's manager relationship.

An **access review** asks whether the person still needs that access. A **campaign** organizes the reviews, and a **reviewer** is responsible for assessing the assigned work. An assigned review is also called a **certification**.

**Generation** creates the review work and assignments from the campaign's settings and available information. A **preview** lets an administrator inspect that work before starting the campaign.

A missing manager does not mean the person has no account or no access. In this example, Export Reports still exists. The question is how the intended assessment will be assigned or whether it will be included.

A **fallback** is an alternative routing choice used when the expected responsibility cannot be supplied under the applicable rule. **Exclusion** means the person or access is left outside the generated review work.

Those outcomes have different consequences. Excluded access has not received a review merely because the rest of the campaign was generated successfully.

## The same missing manager can produce different results

Consider two documented campaign routes.

The dedicated **Manager Campaign** requires manager relationships. Identities without managers are excluded.

The Search identity-campaign route has a **Manager** reviewer option. For that option, the documented missing-manager alternative is the campaign creator.

The **creator** is the person who created the campaign. That is not a general rule that every missing owner in every campaign sends work to the creator.

In our example, manager information is confirmed absent before generation. Administrator 2940 creates the Search campaign with identity 2901 and the intended Export Reports holding included.

Assume 2940 is a permitted reviewer, is not reviewing their own access and no other reassignment changes the route. The generated work is inspected and found assigned to 2940.

Now compare the two results:

- The dedicated Manager route leaves 2901 outside its generated work because the required manager link is missing.
- The supplied Search Manager result includes the intended work and assigns it to creator 2940.

Neither observation tells you that a manager assessed the access. In the second case, the creator still needs the knowledge and authority to perform the assessment, or the work needs a supported correction.

A fallback can keep work moving while leaving a business-readiness problem to resolve.

## Look at the ISC relationship, not only the source text

A **source** is ISC's representation of a connected system or account-data collection. Source account data can contain a reference identifying an employee's manager.

**Manager correlation** connects that reference to a manager's ISC identity through the configured matching rules.

For a basic attribute-based match, a source reference such as E-2910 can match a staff identifier on manager identity 2910. The resulting manager link tells ISC which person the reference represents.

Three records now matter:

1. The manager reference supplied by the source.
2. The manager relationship established in ISC.
3. The reviewer assigned in the generated campaign.

They are connected, but they are not interchangeable.

If the source sends a bad new reference, do not jump straight to “ISC has no manager.” Inspect the actual relationship.

For the documented attribute-based behavior, a reference changing to null, meaning no value, can clear the manager link. A changed reference that cannot be correlated to a new manager can leave the existing manager link in place.

Consider one correctly configured manager mapping for this employee, with no other source supplying the manager relationship:

| Existing manager link | New source reference | Result of matching | Manager relationship |
|---|---|---|---|
| 2910 | No value | No manager reference remains | No manager link |
| 2910 | E-999 | No matching new manager identity | Existing link to 2910 remains |
| 2910 | E-2920 | Matches manager identity 2920 | Link to 2920 |

The middle row explains an easy mistake. The source value is wrong, but the relationship is not empty. A missing-manager fallback is therefore not established merely by finding E-999 in the source.

Check whether the retained manager is still correct for the person's current work. If not, repair the source/reference or matching configuration and verify the resulting relationship.

These examples concern the documented matching behavior. A custom manager-correlation rule needs its own verified logic; do not assume it handles every value in the same way.

## Trace the branch from the relationship used

```text
CHECK THE ISC MANAGER RELATIONSHIP USED FOR GENERATION
        |
        +-- No manager link
        |       |
        |       +-- Dedicated Manager Campaign
        |       |       -> person is excluded
        |       |
        |       +-- Search identity campaign, Manager reviewer
        |               -> campaign creator is fallback
        |                  (ordinary permitted, non-self case)
        |
        +-- Existing manager link still points to 2910
                |
                -> investigate source reference and matching
                -> do not treat it as a missing-manager case

THEN INSPECT THE ACTUAL GENERATED WORK
Expected person/account/access present?
Who is assigned, or what error is recorded?
Is that person suitable and permitted to review?

Correct the cause and verify the resulting work.
A source-field edit alone does not move an existing review.
```

The first branch starts with no manager link and then distinguishes the campaign route.

The second starts with an existing link. It asks why that link remains, rather than applying a missing-data rule to a relationship that is still populated.

The final check follows both branches into actual evidence. Is the intended person and access present? Who received the work? Was an error recorded?

That check also distinguishes an excluded person from a review that exists but is assigned somewhere unexpected.

## A missing account owner has a different alternative

An **account owner** is the person recorded as responsible for an account.

The owner of a service account can be a human responsible for a program's access. That does not make the service account the human's ordinary employee account.

For a supported Search campaign using **Account Owner**, the documented alternative when no account owner is configured is the source owner.

A **source owner** is the owner recorded on the source: a person or, where supported, a governance group. The account-owner rule is therefore using another ownership record. It is not using the employee's manager merely because that manager exists elsewhere.

Check the actual account ownership, the source ownership and the generated assignment. A statement that “someone owns the application” is insufficient if that person is not recorded in the relevant ISC ownership field.

Also confirm that the source owner can assess the account's purpose and need. Receiving work through a fallback does not supply that knowledge automatically.

## A missing access owner needs the correct object context

**Access Owner** concerns the owner of the access object under review.

A standalone entitlement, an access profile containing entitlements and a role containing access are different objects. First establish which one the review is actually assessing.

The Search guidance describes ownership fallback through role owner, access-profile owner, entitlement owner and source owner.

Read that sequence within the supported route and actual access model. It does not turn a standalone entitlement into a role or split a containing access profile into separate entitlement decisions.

Inspect the ownership fields that apply to the reviewed object and the actual resulting assignee. An entitlement's **primary owner** is its main recorded owner; additional owners are other people listed for it. That additional-owner list is not evidence that each person received a separate certification.

If all relevant ownership records are absent, do not invent a final recipient. In particular, a creator fallback documented for Search Manager reviews does not establish a creator fallback for Access Owner.

Establish the route's supported behavior and inspect the generated work or error. Repair the required ownership through the responsible administrator and verify the resulting review. If the behavior remains unclear, seek authoritative clarification with the exact campaign type, reviewer choice and missing ownership records.

Do not copy an access-request approval escalation chain into certification routing. An access request seeks a change; a certification assesses existing access. Similar reviewer labels do not establish identical missing-reviewer rules.

## Source-owner campaign prerequisites still matter

The dedicated Source Owner Campaign route requires the included sources to have assigned owners before generation.

That is a generation prerequisite. It differs from an Account Owner choice falling back to a source owner.

Suppose an administrator selects three sources for a source-owner campaign, but one has no configured owner. Check and repair the included-source ownership rather than assuming the campaign will route that source to its creator.

A valid fallback elsewhere does not satisfy this route's missing prerequisite.

If a source owner is deliberately changed, confirm both the current source record and the resulting review work. Do not assume a saved ownership change reassigned an already generated certification.

## An empty group and an unusable member list are different

A **governance group** is a configured group whose members can perform supported governance work.

The general governance-group guidance states that work assigned to an empty group routes to an Org Admin. An **Org Admin** is an organization-administration user level. The actual campaign record is still needed to establish which person received the work.

Now consider a group with two listed members who have become inactive.

ISC does not automatically update governance-group membership when an identity becomes inactive or disabled. The group can therefore still contain those two identities.

Do not equate “no suitable active member” with “no members.” The empty-group rule does not, by itself, establish the outcome for a non-empty group containing inactive people.

Inspect the membership, the identities' ability to act and the actual campaign assignment or error. Arrange a supported membership or responsibility correction, then verify the work.

The name of a group or its recorded group owner is not enough to show that an appropriate member can review.

## A person who cannot act is not always a missing value

An owner field may contain an identity reference while the person has left, become unavailable or no longer has the required access.

Those conditions require investigation. A populated field does not prove a usable reviewer, and an unavailable reviewer does not prove an ownership field is empty.

For the dedicated Manager/Source Owner guidance, a reviewer's identity no longer existing can produce an error beside the certification. That is different from the dedicated missing-manager exclusion.

Inspect the recorded error and affected work rather than reporting every problem as “fallback did not run.”

Self-review controls can also change the route. **Self-certification** means reviewing one's own access. ISC prevents that, so a fallback person who would review themselves is not an ordinary permitted recipient.

A configured **work reassignment**, an arrangement directing supported work to another person, can also affect the assignment as certifications are generated.

These conditions explain why a routing investigation needs the actual records and applicable controls, not only the name of the reviewer option.

## Correct both the input and any existing work

Start by deciding who should be responsible under the business requirement. Then establish which record needs changing.

A missing manager may require correcting the source reference or manager matching. A missing source owner requires the actual source ownership to be set. A group with unsuitable members requires the appropriate membership or responsibility change.

Perform those changes through someone authorized for the relevant configuration.

Next, inspect the resulting ISC relationship or ownership. A successful save is not proof the correct person was matched or that every affected review now has that person assigned.

Existing work needs a separate check. **Reassignment** changes the responsibility for a generated review through a supported action.

**Sign-off** is the reviewer's confirmation or finalization of their assigned decisions. The documented reassignment action is available for appropriate preview or active work that has not been signed off, with self-review checks. A signed-off review cannot be treated as unsigned work that can simply be reassigned.

If existing responsibility needs correction, use the action supported for its actual state and verify the resulting assignee. If a corrected campaign must be generated, inspect its contents and assignments before starting it.

Keep any required decisions and evidence when replacing work. Do not delete an active campaign merely to make a routing error disappear.

Finally, confirm that the intended person can perform the review. A recorded assignment, a review decision and a completed change in the target system are separate facts.

## Try an account-owner fallback

Account wh-service-1 in Warehouse Production is used by a stock-processing program. It holds View Stock, which allows reading stock information.

The campaign supports Account Owner as the reviewer choice. The account has no configured owner. Source owner 3010 is recorded, available, permitted and would not be reviewing their own access.

Administrator 3020 creates the campaign with Account Owner selected. There is no work reassignment or other condition changing this ordinary case.

Inspection of the generated preview finds the intended account and access assigned to 3010.

Someone says, “The account owner is missing, so it should have gone to creator 3020.”

Is that conclusion correct? What still needs checking?

### Follow the account-owner rule

The documented alternative for missing Account Owner is Source Owner. The supplied assignment to 3010 agrees with that rule.

The creator is not the documented fallback in this ordinary account-owner case. The creator rule from a Search Manager campaign does not apply merely because both situations involve missing data.

Check that wh-service-1 and its intended View Stock access are actually included, that 3010 is the current source owner and that this person understands the program's access need.

The fallback assignment does not establish that the program still needs the permission. That remains the review decision.

Now change the next cycle's inputs: the account owner is still absent, and source ownership has also been removed. No new campaign result has been supplied.

There is not enough verified information here to name the final assignee or a universal error state. Establish the supported behavior for that campaign route and inspect the actual result. Do not substitute an assumed creator or Org Admin.

Repair the missing responsibility, confirm the relevant owner records and verify the work actually generated for the next cycle. If an existing review also needs correction, inspect its state and assignee separately.

When a reviewer is missing, ask which relationship is absent, which rule uses it, which documented alternative applies and what work actually resulted. Those answers show whether you need to repair input data, review coverage or responsibility for existing work.
