# Who becomes the reviewer, and why?

An access review is ready to be assigned. The employee has a manager, the application has a source owner and the permission has an access owner.

Which one should receive the work?

Start with the campaign's reviewer choice. Those people have different responsibilities, and ISC does not send the same review to all of them merely because their names appear somewhere in its records.

The chosen reviewer option tells ISC which responsibility or relationship to use. The relevant data supplies the person or group. The generated assignment shows who actually received the work.

## Follow one manager assignment

An **access review** asks whether someone still needs particular access. The **reviewer**, also called the **certifier**, assesses that access.

A **campaign** organizes the reviews. An assigned review is a **certification**, and each **review item** identifies access awaiting assessment.

An **identity** is ISC's person record. An **account** is the record used to access an application. ISC represents account permissions as **entitlements**.

Suppose the campaign is meant to review Reporting Production access for two people:

- Identity 2701 has View Reports on account rep-2701. This permission allows reading reports.
- Identity 2702 has Export Reports on account rep-2702. This permission allows exporting report contents.

Both entitlements are individually reviewable in this example. They are not contained in a role or access profile, which group access, and no automatic access requirement changes their reviewability.

The account data is current in ISC, and each account is connected to the correct person. In ISC, a **source** represents a system or collection of account data; here it is Reporting Production.

Both people's identity records identify 2710 as their manager. This is a person-to-person relationship in ISC, not just the word “manager” in someone's job title.

The administrator creates a Search identity campaign and selects the supported **Manager** reviewer option.

The relevant relationship is now clear. For each selected person, the manager choice uses that person's recorded manager as the intended reviewer, subject to the route's supported controls.

In our ordinary case, 2710 is available, permitted to review and would not be reviewing their own access. No reassignment changes the result.

The administrator generates campaign C-1 and inspects the actual work. Both people's intended access is assigned to 2710.

That final inspection completes the reasoning: selected people, chosen reviewer option, relevant relationship and actual assignment all agree.

## Where did the manager relationship come from?

ISC needs an established link to the manager's identity.

**Manager correlation** establishes that link by matching an employee's manager reference from source data with a configured attribute on the intended manager's identity.

For example, the source can identify a manager through a staff identifier. Matching that identifier to the manager's ISC identity tells ISC which person the reference means.

A manager's name in an unrelated text field is not, by itself, proof that the relationship was established correctly. Inspect the person's actual manager relationship when an assignment looks wrong.

The relationship also needs to be meaningful for the review. A technically correct manager link does not tell the manager what Export Reports allows or why the person uses it. The reviewer still needs enough access and business context to make a decision.

## The other owners still have their own jobs

In this example, administrator 2740 created C-1 and is also its campaign owner.

The **creator** identifies who created the campaign. The **campaign owner** is responsible for the campaign. These are different responsibilities even when one person fills both.

Identity 2720 is the recorded **source owner** for Reporting Production, responsible for that source. Identity 2730 is the **primary owner** of the Export Reports entitlement, responsible for that access object.

Those responsibilities can help the campaign succeed. The source owner can help explain the application. The entitlement owner can explain what the permission permits. The campaign owner can coordinate the review.

But C-1 uses Manager. With valid manager links and no condition changing the ordinary route, its review work goes to 2710.

Follow that relationship in the diagram:

```text
SELECTED PEOPLE AND ACCESS
2701: View Reports on rep-2701
2702: Export Reports on rep-2702
        |
        | supported reviewer choice: Manager
        v
RELEVANT ISC IDENTITY DATA
2701's manager -> 2710
2702's manager -> 2710
        |
        | generate campaign C-1
        v
ACTUAL ASSIGNED REVIEW WORK
2710 is assigned both people's intended access
        |
        | inspect identities, accounts, items and assignee
        v
CONFIRMED ROUTING RESULT

OTHER RECORDED RESPONSIBILITIES
2740: creates and owns campaign C-1
2720: owns the Reporting Production source
2730: primary owner of Export Reports

Those responsibilities do not replace the selected
Manager rule in this ordinary example.
```

The main arrows follow the chosen Manager rule to the resulting assignment. The ownership records below supply context; they are not extra automatic recipients in this case.

If you intended the entitlement owner to assess this access, inspect the supported reviewer choices for that campaign type. Merely recording an entitlement owner does not change a campaign that uses another rule.

## Choose the responsibility that matches the question

The right reviewer needs to answer the review's actual question.

A manager may know whether an employee's current work needs Export Reports. The permission owner may know exactly what Export Reports allows. Both kinds of knowledge are useful, but they are different.

Some choices have a **fallback**, an alternative recipient used when the expected ownership information is missing. The actual alternative depends on the reviewer option and campaign route.

The Search creation flow documents these reviewer choices. The available choices depend on the campaign type:

| Reviewer choice | Information that supplies responsibility |
|---|---|
| Manager | The reviewed person's manager relationship |
| Individual | The specific identity selected as reviewer |
| Source Owner | The recorded owner of the relevant source |
| Access Owner | The primary owner of the access item, with the documented fallback when ownership is missing |
| Account Owner | The recorded owner of the account, with the documented source-owner fallback if no account owner is configured |
| Role Owner | The owner of the role for the supported role-review route |
| Governance Group | The selected configured group and its members |

Read the choice together with the campaign type. This table is not a promise that every campaign presents every option.

Also separate the people or access selected for review from the reviewer choice. Selecting a permission identifies access to assess. Choosing Access Owner identifies the responsibility used to route that assessment.

Changing who should review does not establish that the intended people, accounts and permissions are included. Check those separately.

## What does each owner option mean in practice?

**Source Owner** starts from the system represented by the source. A source-focused review can put work with the people responsible for that system.

That does not make every source owner an expert on every employee's current job. If the decision needs business context, arrange for that context to be available.

**Access Owner** starts from the access object being reviewed. An entitlement, an access profile and a role are different objects. An access profile groups entitlements; a role can group access used for a business function.

Identify the actual reviewed object and its recorded primary owner. Do not substitute a component permission's owner for the owner of a containing object without checking the supported route.

An entitlement can have additional owners as well as a primary owner. The documented Access Owner reviewer description refers to the primary owner. A list of additional owners is not evidence that every listed person received a separate review.

**Account Owner** concerns responsibility for an account. This matters particularly when the account represents a program or service rather than an employee's personal login.

A human can be responsible for a service account without being the person whose everyday employee account it is. Confirm the actual ownership record and campaign type instead of treating the account's name as proof.

**Role Owner** is relevant to the supported role-review route. Reviewing a role's composition asks whether its definition and included access are appropriate. Reviewing a person's role assignment asks whether that person should hold the role. These are different questions.

The current documented role-composition route is marked legacy. Check that route's actual reviewer options rather than assuming a role owner automatically receives every review involving a role.

**Individual** makes the selected person's identity explicit. It can be useful when a particular knowledgeable person should assess the work. Confirm that person's availability and permitted review responsibility; a selected name alone does not establish those things.

## A governance group needs real members who can act

A **governance group** is a configured group of identities that can make governance decisions.

For supported campaign types, a selected group can receive review responsibility, and a member can perform the action on behalf of the group.

Suppose Reporting Review Group contains members 2760 and 2761. The group is selected for a supported campaign, and both members are appropriate for the work.

The assignment identifies the group responsibility. If 2761 records a decision, that person's action still needs to be traceable.

The group also has an owner in its configuration. Check the membership list rather than assuming that naming a group owner made that person a member or the only reviewer.

A practical readiness check is whether the intended people are actually in the group and available to work. Governance-group membership does not automatically update merely because an identity becomes inactive or disabled.

Keep membership and individual action evidence separate. Knowing that two people belong to the group does not tell you which one made a particular access decision.

## The selected rule may not be the final assignment

The ordinary Manager example had complete data and no special routing condition. Real reviews can contain other conditions.

If a manager is missing, first establish the route. The dedicated Manager Campaign excludes identities without managers. The Search flow's Manager option documents assignment to the campaign creator when a manager is missing.

That difference explains why “Manager was selected” is insufficient evidence that every intended person was assigned to their manager.

ISC also prevents **self-certification**, reviewing one's own access. Own-access cases can therefore leave the ordinary assignment path. Inspect the actual resulting responsibility instead of trying to force the original reviewer to approve themselves.

A configured **work reassignment** can also redirect responsibility as certifications are generated. It is an arrangement for someone else's work to be handled by a designated person during the configured scope.

These conditions have different inputs. A missing manager, a reviewer's own access and a configured work reassignment should not be treated as the same cause.

When something unexpected appears, inspect the particular condition and generated assignment. Do not assume a universal owner hierarchy applies to every campaign type.

## Current responsibility and the decision maker can differ

Return to C-1. Suppose 2710 has saved an Approve decision on View Reports.

**Approve** records a decision that the reviewed access should be retained. It does not, by itself, tell you that every item in the assigned review is finished.

Later, an authorized administrator reassigns the review containing View Reports to permitted identity 2750 because the original reviewer is unavailable.

**Reassignment** changes responsibility for existing review work. **Sign-off** means confirming or finalizing the assigned review's decisions.

In this example, the campaign is active, the review has not been signed off and 2750 would not be reviewing their own access. The documented reassignment action does not allow a review that has already been signed off to be reassigned.

After the permitted action, the administrator checks that the current reviewer is 2750.

A fresh campaign status report can distinguish that current reviewer from the **decision maker**, the person who recorded an earlier decision. The View Reports decision was made by 2710, so that history can still name 2710.

There is no conflict between those facts. One identifies current responsibility; the other identifies who performed a recorded action.

Likewise, changing a current manager or owner field is not proof that an existing review was reassigned. Inspect that review and use a supported action for its state if responsibility needs correction.

## Reviewing access does not grant administration rights

A reviewer needs permission to perform the assigned review. That is different from permission to create campaigns, reassign work or change source configuration.

A **Cert Admin** is a certification-administration user level. An **Org Admin** has broader administrative responsibility. Check the documented permission for the particular action and the actual user's assigned access.

Being the campaign owner, source owner or entitlement owner does not establish every administrative permission.

For example, a source owner can be the intended reviewer for a supported campaign without being authorized to change every source setting. A manager's assignment to review employees does not, by itself, make that manager a campaign administrator.

Establish the review assignment and the permissions needed for the task. Do not grant broad administration merely to compensate for an incorrect assignment.

## Work through a different routing result

A Warehouse Production review asks whether employees 2801 and 2802 still need Adjust Stock. That entitlement allows changing stock quantities.

Both people hold it on correctly linked warehouse accounts. It is individually reviewable, current in ISC and not contained in a role or access profile.

Their current work and need are to be assessed by manager 2805. The entitlement's primary owner is 2811. Administrator 2820 creates and owns the campaign.

The Search identity campaign supports Manager and Access Owner. The administrator chooses Access Owner. The generated work is inspected and assigned to 2811.

Someone reports, “Routing failed. It should have gone to 2820 because 2820 owns the campaign.”

What is actually wrong? What should be checked after correction?

### Follow the choice that was made

The supplied assignment agrees with Access Owner: the relevant primary owner is 2811.

That is not evidence of failed routing. The chosen responsibility does not match the stated requirement for manager assessment.

Campaign owner 2820 is responsible for the campaign. That fact does not override the chosen reviewer option in this ordinary case.

Confirm the requirement with the responsible people. If manager assessment remains the requirement, use the supported Manager choice, confirm both manager relationships and inspect the resulting review responsibility.

Do not assume that editing saved instructions changed an already generated campaign. Use the supported correction for its actual state and verify the intended existing or newly generated work.

The review's **scope** is the people, accounts and access it is meant to include. Check that both people's intended accounts and Adjust Stock holdings remain in scope. Correcting the assignee does not establish correct access coverage.

Now change one fact. A later observation shows that both people's current manager is 2806, while inspection of existing review work still shows 2805 as assigned reviewer.

The current manager field describes today's relationship. The review assignment describes responsibility for that existing work. The difference needs investigation against the required reviewer and generation history.

If responsibility should move, use the permitted correction for the review's state and verify the new assignment. A changed relationship alone is not proof that the existing review moved.

To explain who received a review, connect the campaign type, the chosen reviewer option, the relevant input and the actual assignment. To explain a decision, also identify the person who recorded it.
