# Design and explain a complete periodic access review

A quarterly review can have finalized decisions while a required removal is still pending. To explain its outcome, connect the access review with the account changes it needs to produce.

Let's follow one quarterly review through those connections.

The examples use supplied records and outcomes. The account and campaign labels identify the records being discussed; they are not values to enter in an ISC tenant.

## Establish the result before selecting the campaign

The requirement is:

“Every quarter, review who still needs bulk export in Reporting Production and Archive Production. Remove unjustified export while retaining the reading access people still need.”

Export Reports allows downloading reporting data in bulk. Export Archive allows downloading archived files in bulk. Read Reports and Read Archive allow viewing the corresponding records.

In SailPoint Identity Security Cloud, or **ISC**, an **identity** represents a person or another managed subject. An **account** is the record through which that person or service uses an application.

A **source** is ISC's configured representation of a system or its account data.

An **entitlement** represents a permission or membership. The export permissions in this example can be reviewed individually.

The requirement concerns existing access and current need. It does not ask the reviewer to grant access to people who lack it.

The approved sources, people, accounts and access define the review's **scope**. The application inventory identifies this complete required set for the agreed observation point:

| Account | Source | Required export review |
|---|---|---|
| rep-1001 | Reporting Production | Export Reports held by an employee |
| rep-1002 | Reporting Production | Export Reports held by a contractor |
| arc-1003 | Archive Production | Export Archive held by an employee |
| rep-admin-1004 | Reporting Production | Export Reports held by a privileged account |

Each account belongs to a different identity in this initial example. The privileged account supports work requiring higher authority; it is not interchangeable with an ordinary account.

The inventories confirm that these are the export holders in the approved scope. Accounts with only reading access and accounts in test systems are outside this review. No automation account is hidden from this supplied inventory.

If another export holder is discovered, account for it rather than silently preserve the original count.

An **access profile** packages entitlements, and a **role** groups access for a responsibility. A **lifecycle state** is a configured business stage that can control access.

Here, none of those relationships prevents individual export review or requires the rejected export to remain. That condition is checked before relying on an entitlement-level decision.

**Revoke** records that the reviewed access should be removed. Its required result here is precise: the named export permission must be absent from the correct account, while justified reading remains. Disabling the whole account would not meet that requirement.

## Confirm the data that will become review work

A **connector** is the integration used to read source data or make changes. **Account aggregation** reads account information into ISC.

Compare both application inventories with the actual collected source accounts and holdings. Keep their observation and collection times with the comparison.

A successful aggregation job is not sufficient if it omitted one of the required accounts.

**Account correlation** associates an account with its owning identity. Inspect those associations too. A correctly collected export permission attached to the wrong person would create the wrong review subject.

For this example, the four accounts, identity links and export values are correct and current for generation. The application owners have also confirmed the meaning of each permission.

That establishes the input evidence. It does not yet establish that the campaign selected the right records.

The ISC engineer owns collection and association checks. The application owners confirm source inventory and permission meaning. The business owner confirms the review requirement and how current need will be judged.

Those responsibilities are recorded separately from permission to operate ISC.

## Choose a route that answers this question

A **campaign** organizes access reviews. A **certification** is an assigned review within it. A **review item** is an access entry on which a decision is recorded.

A broad department-based manager review would answer a different population question. The contractor may not be in the employee department used for selection, and source ownership alone does not establish knowledge of every person's current task.

For this project, choose a supported Search-based identity review. Its selection finds the identities holding the named export permissions on the approved sources.

Then restrict the access being reviewed to the relevant export items. Selecting the people and selecting their reviewable access are separate choices.

The exact query, source references and access selection are checked against the inventory. Do not assume that a readable query description proves the generated account-level result.

The expected set remains four specific source-account-export relationships. Each identity has one relevant account in this initial case, so there is no untested assumption about unrelated accounts being included or excluded.

A **campaign filter** can further include or exclude review content. Use one only when it implements an agreed boundary. Adding a filter merely because the option exists can remove required work.

This design does not change shared role contents or depend on a profile being treated as an individual entitlement. Those would require a different decision unit and supporting evidence.

## Assign the judgment to a suitable reviewer

The verified available reviewer option for this example is Individual. The selected reviewer, identified as **R-90**, understands both applications and the current work requirements.

Business and application owners supply relevant context. R-90 remains responsible for the actual recorded choices.

R-90 is authorized to perform the review and owns none of the accounts being reviewed. Actual generated assignments are checked for independence and visibility.

Using a named reviewer here is a deliberate response to the requirement. It is not a general claim that Individual is available for every campaign type or that a manager is unsuitable for every review.

If the design used managers instead, the actual manager relationships and route-specific missing-manager handling would need verification. A missing relationship should not accidentally turn the campaign creator into the intended business reviewer.

Agree the criteria before the choices are made. Export must support a current authorized task on the correct account. A job title, past approval or recent use alone does not establish the whole justification.

Also agree who will supply missing context and who can take over through a supported action if the reviewer becomes unavailable.

The administrator who can generate or start the campaign is not automatically the person qualified to judge every export permission.

## Prepare the two removal paths

**Approve** accepts continued access to the reviewed item. **Revoke** records that the reviewed access should be removed.

**Remediation** is the work needed to carry out that removal. **Provisioning** changes external accounts or access.

Reporting Production has a supported, enabled write connection. Its integration account, the technical identity used by the connector, is authorized for the required removal operation.

Archive Production can be read through ISC, but changes use the applicable manual process. The actual work recipient and authorized archive operator are identified.

Before launch, verify each path using appropriate controlled checks and production-specific configuration evidence. A passing read connection does not prove write authority, and a manual operator's name does not prove that person can perform the change.

For the archive path, the instruction must identify the exact account and permission, the reading access to retain and the result evidence to provide.

The two paths have different operations and responsible actors. Both must satisfy the same business requirement about their respective accounts.

A successful automated removal cannot stand in for an unfinished manual removal.

## Keep reusable instructions separate from this quarter's campaign

A **template** stores reusable campaign instructions. A generated campaign is the actual instance produced from them.

Save the validated selection, reviewer and settings as **T-910**. Generate this quarter's campaign as **C-910**.

Those labels refer to different records. Editing T-910 later is not evidence that C-910's contents changed.

The quarterly schedule concerns generation of a new preview. In the documented Search flow, an authorized administrator must still start the campaign after the required checks.

A **preview** is generated review work available for inspection. **Activation** starts reviewer work.

For this example, the proposed business targets are final reviewer confirmation by working day 10 of the agreed review window and verified required removals by working day 15. Actual dates and the applicable time zone are recorded.

These are agreed work targets, not ISC processing guarantees. Reviewer availability and both removal paths must support them.

Record notification and comment settings, who monitors progress and who handles unfinished work. If never-decided items are configured to be maintained at administrative completion, that policy must not be described as fresh informed reviewer approval.

All choices in this cycle will be saved and finally confirmed before the deadline. We therefore do not depend on an assumed result for saved but unsigned work at administrator completion.

## Validate the actual preview before starting

Inspect C-910 against the independent inventory.

Confirm the four expected account-export relationships, absence of unintended access, correct descriptions and R-90's actual assignment.

In the supplied preview, one certification assigned to R-90 contains four distinct identity subjects and four export items. A **subject** identifies whose access is being examined within that assigned review.

That grouping is an example result, not a rule that every four identities produce one certification or four certifications.

Check the real grouping and every required item.

Also inspect the deadline, actual supported review decisions, notification arrangements, comment requirements and readiness of automated and manual fulfillment.

An **acceptance criterion** states the result that evidence must establish. Here, the inclusion criterion concerns the full four-item set; the independence criterion concerns the actual recipient; the fulfillment criterion includes the ability to remove export while retaining reading.

A few successful samples do not replace full population reconciliation.

If a required check fails, correct the affected data or instructions through the supported process and inspect the actual resulting work. Do not make an unverified preview acceptable by changing the expected list to match it.

In this supplied project, the checks pass for the current inputs and instance. The accountable owner accepts readiness, and the authorized administrator starts C-910.

The running result is then observed. A request to start would not, by itself, establish that the campaign became active.

## Follow the decisions and their reasons

R-90 examines each account and current business evidence.

For rep-1001, the employee still has an authorized reporting task that needs bulk export. Approve is recorded with that reason.

For rep-1002, the contractor's remaining work requires viewing reports, but the earlier export assignment has ended. Revoke is recorded for Export Reports, while the removal instruction preserves reading.

For arc-1003, the one-time archive export activity is finished. Viewing is still justified, so Export Archive receives Revoke with the completed task identified in the reason.

For rep-admin-1004, approved administration still requires export on that privileged account. The decision is Approve. The reason concerns this account's authorized work, not a blanket approval of every account the person owns.

There are four saved item choices: two approvals and two removal decisions.

**Sign-off** is the final confirmation of the assigned review's choices. ISC's newer, next-generation flow separates that confirmation from saving the choices.

R-90 checks the complete set and signs off successfully before the deadline. The final confirmation record belongs with the item choices and their reasons.

The required removal work is then traced through the supported path. The next-generation finalization operation initiates needed remediation, but it does not prove that either application has changed.

## Do not close the review-to-removal trace at sign-off

The actual required work exists for both rejected items in this example.

For rep-1002, inspect the matched Reporting operation. The removal succeeds, and current source evidence establishes that Export Reports is absent while Read Reports remains.

For arc-1003, the manual task is still pending. Current Archive evidence shows export remains.

The accurate progress statement is:

“The four item choices are finalized. One of the two required removals is verified. Archive removal is still outstanding.”

It would be wrong to call both removals complete because the reviewer signed once, or to treat the two Approve decisions as two successful removals.

The archive operator now performs the required application change, verifies that reading remains, and records completion with the supporting evidence.

Inspect the correct Archive account and the result time. In the supplied later evidence, Export Archive is absent and Read Archive remains.

A task close can contribute to the record of work. Its status alone is not independent proof of the account permission. Similarly, the Campaign Remediation Status Report's Finished value can reflect a manual task or service desk ticket being completed.

Where supported automated source confirmation establishes the exact removal, use that evidence within its scope. Interactive user login is not required for every account.

Then collect the changed account information through the applicable method and generate updated reports where needed. Collection time, report generation time and actual account-observation time remain separate facts.

There is no assumed fixed delay for every source.

## Reconcile the whole result

The final check returns to the approved requirement and actual decision set:

| Account | Final export choice | Supported outcome |
|---|---|---|
| rep-1001 | Approve | Justified export retained |
| rep-1002 | Revoke | Export absent; required reading retained |
| arc-1003 | Revoke | Export absent; required reading retained |
| rep-admin-1004 | Approve | Justified privileged export retained |

Both due removals are now verified. The retained approvals and required reading are also accounted for. No unresolved item is silently excluded from this supplied cycle.

Keep the relevant campaign instance, review/item identifiers, current reviewer and actual decision maker, reasons, final confirmation, operation or task, account evidence and times connected.

The **Campaign Composition Report** helps explain configuration. The **Campaign Status Report** helps explain item choices and actors. The **Certification Sign Off Report** concerns final confirmation. Remediation and provisioning evidence help explain the required changes.

Read each field in the context of its report. A generic Complete value does not establish every result in the table.

Confirm the actual campaign state separately from the achieved account outcomes. The administrator performs any applicable completion handling for that engine and state; no administrative choice replaces the already finalized reviewer decisions in this example.

Business closure means the agreed scope and required outcomes have been accounted for, with any remaining work explicitly owned and accepted. Here, the evidence supports the complete supplied result.

Retain the evidence through the organization's approved process and hand the next cycle's preparation to the responsible owners. Campaign deletion is not required to prove closure.

The diagram connects the design and the two delivery paths:

```text
Quarterly requirement and current account baseline
                         |
       Current source data and correct identity links
                         |
       Saved instructions T-910 -> generated C-910
                         |
       Validate actual items, reviewer and readiness
                         |
          Authorized start, decisions and sign-off
                         |
             Two required export removals
                         |
           +-------------+---------------+
           |                             |
  Reporting Production           Archive Production
  Authorized connector write     Assigned manual work
           |                             |
  Verify rep-1002 result         Verify arc-1003 result
           |                             |
           +-------------+---------------+
                         |
       Reconcile all decisions and account outcomes
                         |
       Retain evidence and prepare the next cycle

One completed branch does not complete the other.
Each new cycle needs current inputs and actual coverage.
```

Follow each removal to its own result. A completed branch or a newer report does not complete the other branch.

## Explain why this design fits

The population follows current export holdings on the approved sources, rather than department membership alone.

The review unit follows the actual independently reviewable entitlements. If access were represented through a profile or automatic role, those conditions would need a different assessment.

Reviewer responsibility follows knowledge, authority and independence. Application consultation supplies context without pretending to create an extra configured approval stage.

Fulfillment follows each source's actual capability. The automated and manual paths are separately prepared and verified.

Closure follows the full required set and account outcomes. It does not follow only a counter, signature or campaign badge.

These connections are the reasons behind the chosen settings and operations.

## Prepare for a different next cycle

The two rejected export permissions remain removed. No new grant restores them.

Before the next quarter's generation, the person behind rep-1001 receives a second account, **rep-admin-1005**, with Export Reports.

The application inventory now contains five accounts belonging to the same four identities. Only three accounts hold the export permissions: rep-1001, rep-admin-1004 and the new rep-admin-1005.

Those three export accounts belong to two identities, because rep-1001 and rep-admin-1005 share an owner.

The latest collected ISC data still contains only the original four accounts, including the two whose export was removed. It does not yet contain rep-admin-1005.

Reusing T-910 or counting familiar identity records does not establish coverage of the new account.

First establish the missing data. Use the supported collection path to obtain rep-admin-1005, verify its association and export holding, and compare the data with the current inventory.

Then inspect the distinct new cycle's actual preview. In the supplied corrected result, all three current account-export relationships appear and the reviewers remain independent. The two accounts without export are not misreported as current export holders.

Do not infer that every cross-account filter or identity selection behaves the same way. Establish the actual selected accounts and items for the route being used.

The earlier C-910 closure remains evidence about its original scope and observation point. The new account creates work for the new cycle; it does not make an old report current.

Carry forward validated instructions and lessons learned. Reestablish the current inputs and results that those instructions depend on.

