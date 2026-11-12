# What do we need to discover before designing the campaign?

“Review Support access this quarter and finish by month-end.”

That sounds like a campaign request. It still leaves several decisions open.

Does Support mean people in that department, everyone using a support application, or everyone who can perform a particular sensitive action? Does finish mean the reviewers have confirmed their choices, or that rejected access has actually been removed?

Before choosing campaign settings, make those answers clear. Otherwise, you can build exactly what the screen allows and still miss the business requirement.

This work is **discovery**: establishing the purpose, relevant facts, constraints and unanswered questions that the design must address.

## Start with the decision the review must support

In SailPoint Identity Security Cloud, or **ISC**, a **campaign** organizes access reviews. A **certification** is an assigned review within it. A **review item** is the access entry on which a reviewer records a choice.

The review examines existing access and whether it remains appropriate. It is not automatically a request to grant missing access or redesign every permission in the application.

For the request above, suppose discussion establishes the real objective:

“Confirm who still needs to export or delete case records in Case Management Production, and remove unjustified access while retaining the reading access people still need.”

Now the capability and required outcome are visible.

Read Cases allows viewing case records. Export Cases allows downloading records in bulk. Delete Cases allows deleting them.

An **entitlement** represents a permission or membership such as Export Cases. A readable label is only a starting point; the application owner must confirm what the permission actually allows.

Also confirm the environment. Case Management Production and a similarly named test system are different targets. A review of test access would not meet a requirement about production data.

## Establish who and what must be accounted for

An **identity** is ISC's record for a person or another managed subject. An **account** is the record through which that person or service uses an application.

One person can have an ordinary account and a separate administrator account. Counting people alone does not establish which accounts and permissions were covered.

A **source** is ISC's configured representation of the application or its account data. Keep the actual source and account identifiers with the requirement, alongside readable names.

The people, accounts and access intended for inclusion define the campaign's **scope**.

An **access profile** packages entitlements. Case Analyst contains Read Cases and Export Cases in this example.

Suppose the supplied application inventory identifies these four accounts with export or deletion capability:

| Account | Relevant context | Access that needs attention |
|---|---|---|
| case-981 | Support employee's ordinary account | Export through the requested Case Analyst profile |
| case-982 | Operations contractor's account | Separately held Export Cases |
| case-admin-983 | Support employee's administrator account | Separately held Delete Cases |
| case-bot-984 | Automation account | Export Cases used by a process |

The four rows explain why a department-only selection would be inadequate. The contractor is outside Support, and the automation account is not an employee account. Both still hold a capability named in the requirement.

These are illustrative identifiers and supplied inventory facts. They do not establish that one identity-based query will select every account exactly as required.

Use the inventory to define the expected set. Then choose and validate supported review routes that account for it.

For the automation account, identify the responsible owner and process purpose. In this example, the automation team confirms both, but the review route is still unverified. Confirm the available account-review route and its actual selection behavior. Do not assign the account to an arbitrary employee merely to make it fit an employee campaign.

Likewise, distinguish a deliberate exclusion from an accidental omission. If test accounts are out of scope, record that boundary. If a production export account is deferred, it remains part of the requirement needing explicit handling.

## Find out whether ISC has the information the design depends on

The application inventory and ISC's collected data are different evidence.

A **connector** is the integration used to obtain data or make changes. **Account aggregation** reads account information into ISC.

Discover when the relevant accounts and permissions were last collected, whether that collection succeeded, and whether it covered the application inventory you are relying on.

A new campaign report does not collect a missing account from the source.

**Account correlation** associates an account with its owning identity. For person-based reviews, inspect the actual association. A correct permission attached to the wrong person can produce the wrong subject and reviewer.

If you intend to use managers, inspect the resolved manager relationship too. **Manager correlation** links an employee's identity to their manager using configured matching information.

A manager name in a source field is not enough to establish the correct identity link.

Ask who owns corrections to missing accounts, wrong associations, stale attributes and unclear permission descriptions. Record the actual result needed before those inputs can be trusted.

These answers affect the design. A manager-based approach depends on usable manager relationships; a review of all export holders depends on complete account and access evidence. A configuration cannot compensate for an account that never reached the data used for selection.

## Discover what the reviewer can actually decide

Return to case-981.

The business requirement names Export Cases. ISC represents that person's export access inside the requested Case Analyst profile, together with Read Cases.

An entitlement contained in the person's access profile is not independently certified as though it were a separate holding. The relevant review may concern the profile as a whole.

That changes the question presented to the reviewer. They need to understand the complete package and current need for its capabilities.

Suppose the person still needs reading but no longer needs export. Revoking the profile is not a component-only instruction to remove export, and approving another review item does not automatically grant replacement reading access.

Record this design constraint. The access model or an approved separate fulfillment arrangement may need to support retaining Read Cases without Export Cases. Identify who can authorize and implement that change, and how retained reading will be verified.

A **campaign filter** selects review content to include or exclude. Changing it cannot, by itself, turn a package decision into a different permission model.

Also discover **roles**, which group access for a responsibility, and **lifecycle states**, which represent business stages that can control access. Their assignment rules affect what is reviewable and what a removal can achieve.

Access controlled by automatic role membership can only be acknowledged through that review item. **Acknowledge** records examination; it does not override the membership rule.

You therefore need the actual object, contents and grant origin before promising a particular reviewer action.

## Agree how appropriate access will be judged

Someone must explain why the access is justified.

**Decision criteria** are the organization's agreed conditions for keeping or removing access. They are different from campaign filters, which select the content to review.

For Export Cases, useful criteria might require a current assigned task that needs bulk export, an approved purpose and the correct type of account. The actual criteria need approval from the responsible business and application owners.

Do not replace those answers with “the user has the right job title” or “the permission was used recently.” Those facts can provide context, but neither establishes every part of the justification.

Discover what the reviewer will need: the person's current responsibility, account purpose, permission meaning and supporting evidence. An unclear description is a data problem to address before asking someone to make a confident choice.

Also ask how uncertainty will be handled. A reviewer who cannot establish the current need should have a named route for getting relevant information or transferring responsibility through a permitted action.

A mandatory comment can help retain an explanation. It cannot make an unsupported decision correct.

## Separate knowledge, responsibility and platform permission

The employee's manager may know current work. The application owner may understand what export and deletion allow. The automation owner may understand why a process account needs bulk data.

Discover who has enough knowledge and authority to make the required judgment.

A **reviewer** is assigned the review work. A **source owner** is responsible for the configured source. An **access owner** is responsible for an access object. The administrator preparing the campaign may have a different responsibility again.

Do not assume that the person who can create a campaign understands every access decision, or that a knowledgeable reviewer has permission to administer the campaign.

Confirm independent review of privileged accounts and each person's own access. Supported self-review prevention and reassignment conditions matter when deciding who receives the work.

The selected reviewer rule must also match the intended recipient. Manager, access owner and a named individual are different choices, and available choices depend on campaign type.

For example, the dedicated manager-campaign guidance excludes identities without managers. The Search-based Manager choice documents transfer to the campaign creator when a manager is undefined. A missing-manager case therefore needs the actual route and result.

Consulting both a manager and an application specialist does not, by itself, configure two ordered approval stages. Record how their input reaches the person responsible for the actual review decision.

Discover who handles absence, departure, disputed ownership and unfinished reviews. Confirm the replacement's knowledge, independence and permitted access to the work rather than treating an available name as a suitable reviewer.

## Ask what happens after Revoke

**Approve** accepts continued access to the reviewed item. **Revoke** records that the reviewed access should be removed. **Sign-off** is final confirmation of the assigned review's choices.

ISC's newer, next-generation review flow separates saving choices from that final confirmation.

**Remediation** is the work needed to carry out a removal. **Provisioning** changes external accounts or access. Reading source data and writing a removal are different capabilities.

In our example, the Case Management connection is **read-only**: ISC can collect the account data but cannot use that connection to change the permissions. The application team must perform required changes through the applicable manual process.

That answer changes the plan. You need an actual recipient, a usable removal instruction, authorized application access, capacity to perform the work and evidence of the resulting account permissions.

A manual task or service desk ticket records work responsibility. Marking it complete is not independent proof that every required permission is absent.

For case-981, the instruction must also account for the reading access that should remain. “Remove Case Analyst” and “leave the account able to read but unable to export” are different descriptions of the required result.

Do not promise immediate automatic removal because the account data is visible in ISC.

Discover how failed changes, another assignment keeping access, or a later grant will be handled. Identify who owns investigation and who confirms the final result.

## Give the deadline a precise meaning

“Finish by month-end” can hide several different targets.

Agree when the source evidence must be current, when the preview will be checked, when reviewers should begin, and when their decisions must be finally confirmed.

A **preview** is generated review work available for inspection. **Activation** starts reviewer work. Generating a preview is not the same as starting the campaign.

For this example, suppose the proposed targets are reviewer sign-off by working day 10 of the agreed review window and verified required removals by working day 15. Record the actual dates and time zone with those targets.

Those are business targets, not ISC processing guarantees. The application team still needs to confirm that the manual work and the required change to case-981's permissions can meet them.

If they cannot, resolve the requirement, resources or approved handling before committing to the dates. Moving the reviewer deadline does not automatically make application work faster.

Also agree what happens to never-decided items and saved but unsigned reviews at the deadline. The actual configuration, campaign type and supported completion behavior matter. Administrative maintenance of access is not an informed reviewer's approval of every affected item.

For recurring work, clarify whether the next occurrence must use current population and ownership inputs. Scheduling preview generation does not remove the need for validation and the documented manual start step.

Include reviewer availability and notification arrangements. An email setting alone does not establish that the intended person can see and complete the assigned work.

## Decide what evidence will support the outcome

Ask what the campaign owner and evidence recipient need to establish.

Configuration evidence can explain how the campaign was set up. Item records show choices and recorded decision makers. Sign-off evidence concerns final confirmation. Removal work and current source evidence support the actual account result.

No single word such as Complete establishes all of those facts.

For this request, the evidence needs to account for the intended export and deletion holders, the correct decision objects, suitable reviewers, recorded reasons and final confirmation.

For rejected access, it must also support the actual removed capability and any access that had to remain.

Keep the campaign instance, source, account, item, actor and relevant times connected. A later report download is not necessarily a later account observation.

Agree who prepares and retains the required records, who can receive account information, and how unresolved items are reported. Do not invent a universal retention period from a campaign setting.

This evidence requirement influences the design before launch. If an application cannot provide reliable confirmation of the requested outcome, discover that limitation while the requirement can still be resolved.

## Keep unanswered questions visible

An **assumption** is a belief being relied on without the evidence needed to establish it.

“All these accounts are employees' ordinary accounts” would have missed the administrator and automation cases in our inventory.

A **dependency** is something that must be available or completed for another part of the work to succeed. Correct account data, a supported automation-review route and an approved way to retain reading without export are dependencies in this example.

Record who will resolve each one, what evidence will establish the answer and which design commitment it affects.

An **agreed exception** is an explicitly authorized departure from the requirement with clear limits and follow-up. Record the affected accounts, reason, authorizing person, responsible owner, review date and remaining action under the organization's process.

Suppose an owner proposes leaving case-bot-984 out because its review route has not been confirmed. That does not meet the original all-holders requirement.

The accountable owner must decide whether to resolve the route, arrange another accepted review or authorize a clearly recorded exception with appropriate conditions and follow-up. Do not silently describe the reduced population as complete coverage.

A useful discovery record connects answers with their consequences:

| Established answer or open point | Design consequence | Who supplies the answer or evidence |
|---|---|---|
| Objective concerns export and deletion in production | Department membership alone cannot define the population | Business requirement owner confirms the capability and environment boundary |
| Four supplied accounts hold those capabilities | Account for employee, contractor, privileged and automation access | Application owner supplies the inventory; ISC engineer checks the resulting coverage |
| Case Analyst combines reading and export | Confirm the decision unit and how reading can remain without export | Access model owner agrees the supported arrangement and its effects |
| Connection is read-only | Confirm manual removal ownership, capacity and result evidence | Application fulfillment owner confirms authorized operators and verification |
| Automation review route is unverified | Keep the route check visible before claiming complete supported coverage | ISC platform owner verifies the available route and selected accounts with the automation owner |
| Sign-off day 10 and verified removal day 15 are proposed | Confirm feasibility separately for review and application work | Campaign and application owners agree actual dates, capacity and remaining dependencies |

Use this record to review the proposed design and keep the remaining actions visible. It does not establish that the campaign is ready to start.

The diagram shows how the answers connect:

```text
Business question and required result
                    |
      Current people, accounts and access evidence
                    |
       +------------+-------------------+
       |                                |
What can be reviewed?          Who can judge the need?
Object and grant origin        Knowledge and independence
       |                                |
       +------------+-------------------+
                    |
       Supported scope and reviewer design
                    |
       Removal responsibility and evidence
                    |
       Timing, dependencies and exceptions
                    |
       Recorded design basis for validation

An unanswered requirement stays visible with an owner.
A saved configuration does not prove the requirement.
```

For this example, you can now explain the objective, expected population and major design constraints. The automation route, the way to retain reading without export, and manual-work capacity still need named resolution before the corresponding commitments can be made.

## Try a request about a shared role

A different requester asks:

“Review the Operations Support role so future recipients receive Read Tickets but no longer receive Delete Tickets.”

Read Tickets allows viewing tickets. Delete Tickets allows deleting them.

The proposed plan is to review whether 100 current users should keep the role.

Would that establish the requested result?

An individual role-assignment review concerns a person's holding. The request here concerns the shared **role definition**, meaning the role's configured contents.

One hundred valid decisions that current users may keep the role would not, by themselves, remove Delete Tickets from that definition.

Clarify the intended role contents with the responsible role owner, identify the supported review and correction route, and determine who will perform the approved change.

**Role-composition review** examines the shared role's contents and requirements. Current certification guidance recommends using the **legacy**, or older certification engine, campaign route for role composition. Confirm availability and handling for the actual environment before promising a next-generation implementation.

The current users' access may also need assessment, but that is a separate requirement to make explicit.

Discover what must happen for existing holders as well as future recipients, what legitimate reading access must remain, and how both results will be verified. Do not infer every existing account's updated permissions merely from a saved role edit.

Changing the purpose changed the review unit, the responsible people and the evidence needed. The campaign design should follow those answers.

