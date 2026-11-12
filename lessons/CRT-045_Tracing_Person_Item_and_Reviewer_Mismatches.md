# The person, item or reviewer is wrong. Where did the mismatch begin?

A manager opens a review and finds access belonging to someone outside their team.

You could move the review to another person immediately. But first, find out what is wrong. The account might belong to the wrong identity in ISC. The campaign might have selected the wrong people. Or the account and person might be correct, while the reviewer assignment needs correction.

Each explanation leads to a different repair.

Start by writing down what should be present, what is actually present and which records support the difference.

## Make the mismatch specific

In SailPoint Identity Security Cloud, or **ISC**, an **identity** is the record representing a person or another managed subject. An **account** is the record through which that person or service uses an application.

A **campaign** organizes access reviews. A **certification** is an assigned review within it. A **review item** is an access entry on which a reviewer records a decision.

“The review is wrong” does not yet identify which of those records needs attention.

An **expected result** is what the approved requirement and supporting facts say should happen. An **observed result** is what the inspected records actually show.

For a reviewer problem, a useful statement is:

“This identity's current manager should receive this assigned review, but the generated review is assigned to the previous manager.”

Keep the requirement with that statement. If the campaign deliberately uses an access owner, the person responsible for the access object, a different recipient from the manager may be correct.

Likewise, distinguish “this account belongs to the wrong identity” from “this correctly identified person should not have been selected.” The first concerns account ownership in ISC. The second concerns campaign **scope**, meaning the people, accounts and access intended for inclusion.

Before changing anything, match the actual campaign instance, assigned review, identity, source and account. A **source** is ISC's configured representation of a connected system or its account data.

Use stable record IDs where available, together with readable names. Similar names and repeated permission labels are not enough to identify the same records.

## Follow one wrong-reviewer report

Suppose identity **I-41** owns account **research-930** on **Research Production**.

View Experiments allows viewing experiment results. Export Experiments allows downloading them in bulk. Both are eligible for individual review in this example.

The campaign's people, accounts, permissions and other settings have been checked. The current concern is the reviewer.

A manager campaign, **C-730**, was generated at 09:00. It is still in preview, with no saved decisions or **sign-off**, the final confirmation of a review's choices. **Preview** means the generated work is available for checking before **activation** starts reviewer work.

At 10:00, an administrator reports that I-41's review is assigned to **R-17**, but it should go to **R-22**, the current manager.

The labels here identify example records. They are not values to enter in ISC. All times use one day and the same time zone, America/Chicago.

First inspect the actual assignment and reviewer selection. In this case, Manager is the intended choice. The account belongs to I-41, and neither reassignment history nor a configured work redirect explains a different recipient.

The HR, or human resources, system provides the employee and manager data used here. Compare that information at each relevant point:

| Evidence | Supplied finding |
|---|---|
| HR record changed at 08:30 | Manager reference is M-22, identifying R-22 |
| HR account data last collected into ISC at 08:00 | Manager reference is still M-17 |
| ISC manager relationship used for generation | I-41 is linked to R-17 |
| Review generated at 09:00 | Assigned to R-17 |
| Current assignment inspected at 10:00 | Still R-17 |

The HR manager change happened after collection but before campaign generation. ISC's collected input had not yet caught up with the new requirement.

Generating the campaign did not itself read the changed HR record into ISC.

## Explain the connection between those records

**Account aggregation** reads account information from a source into ISC.

**Manager correlation** establishes the relationship between an employee's identity and the manager's identity using the configured source reference and matching identity information.

In our example, M-17 and M-22 uniquely identify the two managers under the configured mapping. The text in the source field and the resulting manager relationship are separate things to inspect.

The campaign's Manager selection depends on the relevant manager relationship. At generation, that relationship still pointed to R-17.

The assignment is therefore consistent with the supplied old input. The mismatch with the current business requirement began before reviewer assignment, in the manager data available for that generation.

This is the **root cause** established by these records: the cause that explains the mismatch and tells us what needs correction. It is more specific than saying “ISC selected the wrong manager.”

A different set of records could lead elsewhere. If the collected value already identified R-22 but the resolved relationship still pointed to R-17, inspect the configured manager mapping, the matching manager identity and the actual processing result.

A nonempty source value does not establish that it matches the intended manager. Check the resulting identity link.

If both input and relationship were correct, examine the actual campaign's reviewer rule, generation time and any later transfer. Do not keep refreshing source data after the evidence has located the difference somewhere else.

## Repair the input and the existing work

For C-730, the correction has two parts.

First, use the supported collection and relationship-processing path for the HR source. Then inspect the result: the collected reference is M-22, and I-41's manager relationship now points to R-22.

These are supplied successful results for the example. Starting a job alone would not establish them, and there is no fixed refresh time assumed here.

Next inspect the existing review. In this example, its assignment still says R-17.

A corrected manager relationship is not, by itself, evidence that an already generated certification moved to the new manager.

The applicable reassignment path supports transferring unsigned work in preview or a started campaign. Confirm the exact review, permissions and recipient before using it.

R-22 is suitable, authorized and independent of the access being reviewed. The transfer is permitted and completes successfully. The current assignment and the new reviewer's access to the intended work are then checked.

**Reassignment** changes review responsibility. It does not correct an account's ownership, change application permissions or make an earlier item decision belong to a new actor.

For the next cycle, also check a newly generated preview after the corrected inputs are available. In the supplied later preview, the intended review goes to R-22.

Those observations establish two separate results: the existing work is with the correct reviewer, and the later generated work uses the corrected input. Checking only one would leave part of the problem open.

If other employees depended on the same old input, identify their affected reviews and check each required result. One corrected assignment does not establish that the whole campaign is repaired. Equally, do not move unrelated reviews merely because they belong to the same campaign.

## When the person or account is wrong

Before diagnosing selection rules, establish who actually owns the account.

**Account correlation** matches an application's account with its owning identity in ISC. It is different from manager correlation, which links an identity to their manager.

Suppose approved ownership records establish that an application account belongs to I-41, while ISC associates that exact account with I-59.

Moving I-59's review to I-41's manager would not fix the account association. It could make the assignment look more plausible while leaving the wrong subject in the review.

Compare the source's account identifier, the ownership attribute used for matching, the intended identity's corresponding value and the actual correlation configuration.

Find where the mismatch occurs. The source's ownership value may be wrong, the chosen matching attribute may be unsuitable, or an existing manual association may need investigation. Do not assume the same cause for every wrong-owner case.

If correlation criteria change, the follow-up processing matters. An optimized aggregation can skip an unchanged account without reevaluating its correlation. The documented unoptimized aggregation path allows unchanged records to be reexamined.

Use the appropriate supported scope and procedure. An ordinary refresh is not proof that changed correlation logic was applied, and a broad reprocessing run is not the automatic first repair for every campaign issue.

After correcting the association, inspect both the identity's actual accounts and the affected review work. Do not assume the old campaign's subjects and decisions have been rebuilt.

An **uncorrelated account** has no matched owning identity in ISC. That needs investigation, but it does not justify linking a service account to an arbitrary employee. A service account may support an application or automated process and require the appropriate ownership and review route.

## When a person or permission seems missing

A missing row can arise at several points. Follow the relevant evidence rather than treating absence as proof of one cause.

First ask whether the application account actually has the permission. Then inspect whether ISC collected that holding for the correct source and account.

If the permission exists in the application but is absent from collected account data, a campaign filter is not yet the first demonstrated problem.

If the holding is present in ISC, examine selection. A query may select a different population, or a selected group of people may have had only part of their access chosen for review.

Next inspect the campaign filter. An inclusion filter retains matching content; an exclusion filter removes matching content within its supported criteria. Compare the actual saved conditions with the named identity or item.

Check what was used for the generated campaign. Editing a reusable definition today is not evidence that an earlier generated instance has changed.

Also compare times. A permission granted after the campaign was generated may explain a difference between current holdings and the earlier review. Record the actual collection and generation times before describing the row as missing.

A new report describes the campaign's reportable state. It does not add an account that was never selected or collect a permission from the application.

If the actual generated population is wrong, correct the responsible data or selection instructions and use the supported path to generate and validate replacement work. Do not promise that changing one setting rebuilds every active or signed campaign in place.

## Check whether the permission is inside something larger

An **entitlement** represents a permission or membership, such as Read Orders.

An **access profile** packages entitlements. A **role** groups access for a responsibility. A **lifecycle state** describes an identity's stage, such as active employment, and can control access associated with that stage.

These relationships affect what appears as an individually reviewable item.

An entitlement inside the person's access profile or role is not generally presented as a separate item for independent certification. A profile granted through a role is handled through that role, while a profile granted through a lifecycle state does not appear individually in certifications.

You may therefore need to inspect the package that represents the capability, rather than search only for a row with the entitlement's name.

Confirm the actual assignment and contents. Similar labels do not prove that a package contains the permission you are trying to review.

Also establish what the reviewer is permitted to decide on that object. Access controlled by automatically assigned role membership can only be acknowledged through that review item; Acknowledge does not override the membership rule.

A business requirement to examine a capability still matters. If the chosen review route cannot provide the required assessment or decision, agree a supported approach instead of manufacturing a standalone row by changing unrelated filters.

## When the recipient is unexpected

Compare the expected business reviewer with the campaign's actual selection.

Manager, Source Owner, Account Owner, Access Owner and a named individual describe different responsibility choices. A **source owner** is responsible for the configured source; an **account owner** concerns the account; an **access owner** concerns the reviewed access object.

Use the rule for the actual campaign type. For example, the dedicated manager-campaign guidance excludes identities without a manager, while the Search-based Manager choice documents reassignment to the creator when the manager is undefined.

Those are different routes. “Missing manager” is not enough information to predict one universal outcome.

An empty owner field can also trigger a documented fallback in a particular route. Check the applicable sequence and the actual generated assignment. Do not invent a final recipient when all expected ownership inputs are missing.

Next check whether responsibility moved after initial selection.

A **work reassignment** configuration can redirect newly created work during a configured period. Inspect the relevant work type, recipient, dates, time zone and whether the feature was enabled. A valid redirect can explain why the assignee differs from the ordinary manager.

Ending that configuration does not automatically move previously redirected work back. Inspect and handle the existing assignment separately.

Self-review prevention can also change routing. A person must not review their own access, so inspect the actual affected subject and supported independent-recipient handling before calling the routing an error.

For a signed certification, the documented reassignment path is blocked. Establish the supported correction for the actual state rather than promising that completed work can simply be reopened and moved.

## Check the view before declaring the records missing

A report, screen or API response has a scope.

A filtered view may hide an item that is present in the campaign. A retained old report may show an earlier assignment. A collection returned in pages may contain more records than the first page.

Match the campaign and assigned review, clear or account for the relevant display filters, and inspect the necessary records through an authorized view.

An **API** is an interface through which software requests ISC data or operations. If used for this investigation, select the supported operation for the actual object.

The next-generation certification read returns one certification. Its review-item list concerns an identity-campaign certification. These are not all-campaign or all-tenant views.

They require the documented administrator or actual-reviewer access. These next-generation interfaces are marked Experimental and require X-SailPoint-Experimental set to true in a request **header**, which carries extra information with the request. Their scope does not extend to every campaign engine.

A permission error is not an empty review. A successful read is also not evidence that every source has already supplied current data.

Search can reflect changes later than the underlying records. Compare the relevant account or identity record and processing evidence when deciding whether the mismatch is data, generation or display timing. Do not assume one refresh makes every view current.

Here is a way to keep the investigation connected:

```text
Start with the reported mismatch
             |
Match campaign, review, account, item and time
             |
      Compare expected with observed
             |
    +--------+------------------+------------------+
    |                           |                  |
Wrong person/account      Missing/wrong item   Unexpected reviewer
    |                           |                  |
Source ownership          Collected holdings   Selected reviewer rule
Account association       Selection/filter    Manager/owner input
Population selection      Package/origin      Handover/redirect
    |                           |                  |
    +---------------------------+------------------+
                                |
                 Establish the actual cause
                                |
          Correct the affected data, rule or work
                                |
           Inspect current work and future inputs
```

The branches show where to look for different causes. They are not a fixed sequence of ISC's internal services. Follow the branch relevant to the observed difference and preserve evidence of what you find.

## Try a missing-item case with different conditions

An unsigned preview includes the correct ordinary account **order-940** on **Orders Production**.

Read Orders allows viewing orders. It is contained in a separately held **Order Reader** access profile obtained through a request. No role or lifecycle state requires this profile in the supplied case.

The source data is current, the intended person and account are included, and the preview contains Order Reader. There is no standalone Read Orders row.

Someone proposes rerunning aggregation and removing every campaign filter to make the row appear.

First inspect the package. The actual Order Reader item contains Read Orders. The absence of a standalone entitlement row is consistent with the package relationship.

There is no supplied data-collection failure to repair. Examine the full profile's contents and current business need, because the decision concerns that profile. Do not revoke it merely to repair the appearance of the screen.

Now the requirement changes. The review must also include **Export Orders**, a separate, individually reviewable permission allowing bulk download. That holding is correctly collected on the same account.

The saved exclusion filter explicitly matches Export Orders, and the generated preview omits it. That exclusion may have been correct for the earlier requirement; it conflicts with the newly approved scope.

This time, the package explanation does not answer the new problem. Export Orders is separate; the inspected exclusion conflicts with the newly approved scope.

Correct the actual selection instructions through the supported procedure and validate newly generated work. In the supplied replacement preview, Export Orders appears alongside Order Reader, the intended account and other required items remain included, and the reviewer assignments are suitable.

Keep the old and replacement instances distinct. All work in this example is still unsigned and unactivated; handling old work follows the approved retention and retirement process.

Check the result of a correction before saying the problem is fixed. Here, the reading capability was already represented through its profile, while the export capability needed a scope correction. Treating both absences as the same problem would have led to unnecessary changes.

