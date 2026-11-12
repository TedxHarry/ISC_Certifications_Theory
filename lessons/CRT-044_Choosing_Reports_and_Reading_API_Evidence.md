# Which report answers the question we are asking?

Someone asks you to send the campaign report.

Before choosing a file, find out what they need to establish. They may want to know how the campaign was configured, what the reviewer decided, who confirmed the review, or whether rejected access was removed.

Those questions follow the same review, but they concern different records. Choosing the right report starts with the result you need to explain.

## Follow one permission through the review

In SailPoint Identity Security Cloud, or **ISC**, a **campaign** organizes access reviews. A **certification** is an assigned review within it. A **review item** is an access entry on which a reviewer records a decision.

An **identity** is ISC's record for a person or another managed subject. An **account** is the record through which that person or service uses an application.

Suppose account **ledger-930** on **Ledger Production** has two permissions. View Ledger allows viewing ledger entries. Export Ledger allows downloading those entries in bulk.

The correct identity owns the account, and the two permissions are eligible for separate review decisions in this example. The selected people, accounts and resulting review contents have been checked. A suitable, authorized reviewer who is independent of the access examines current business need.

Viewing is still necessary. Bulk export is no longer needed.

The reviewer records **Approve** for View Ledger and **Revoke** for Export Ledger. Approve accepts continued access; Revoke records that the reviewed permission should be removed.

The reviewer then successfully gives **sign-off**, the final confirmation of the assigned review's choices. We are following an ordinary next-generation review, without an administrator replacing the choices through a completion policy.

An administrator later completes this campaign without replacing those choices. The campaign is identified here as **C-620**, an illustrative label for its ID, not an ID to enter in ISC.

We now need evidence for several parts of that work.

## Explain how the campaign was configured

Start with the **Campaign Composition Report** when the question concerns configuration.

It describes settings such as the campaign's identity, creation and activation dates, deadline, email settings, Search terms and campaign filter.

A **campaign filter** is a configured condition used to include or exclude review content. **Search terms** are the query conditions used when a campaign is created through Search.

For C-620, those settings help explain which selection instructions were used. They also help answer a question such as, “Was this the intended monthly review, with the agreed deadline?”

The report does not replace a comparison of expected access with the actual review items. A correct-looking query can still depend on missing or incorrect account data.

Be especially careful with the **Sources** field. The documented report lists included sources for a source-owner campaign, but shows All for other campaigns. All in that field does not prove that every account and permission in every system was actually reviewed.

Use the configuration to understand the instructions. Use the resulting review records to establish what was included.

This report also has a documented availability exception for campaigns using exclusion rules created by SailPoint support. A missing report needs investigation in the actual campaign type and state.

## Find the choice made on a particular item

Use the **Campaign Status Report** to examine access items and their recorded decisions.

For Export Ledger, match the campaign, assigned review, identity, source, account and item. A **source** is ISC's configured representation of a connected system or its account data.

Then read the decision-related fields.

**Decision** tells you the choice: Approve, Revoke or Acknowledge.

A **role** groups access for a responsibility. When rules automatically control membership in a role, the reviewer can be asked to acknowledge that access rather than choose to remove it through that item. Acknowledge records that examination; it does not override the membership rules.

**Decision Made** is a different field. It describes the item's status using values such as Open, Complete or Error.

For our export item, a Complete item status with a Revoke decision means that a removal choice was recorded. The word Complete there does not establish final sign-off or a changed application account.

The report also separates **Reviewer**, the person currently assigned, from **Decision Maker**, the actor recorded as making the choice. They can differ after a handover.

Read **Decision Comments** for the explanation attached to the choice. The separate **Comments** field can describe report or processing issues.

A row can therefore help you explain which access was reviewed, what was decided, by whom and for what recorded reason. Keep each answer tied to the correct field.

## Establish final confirmation

Use the **Certification Sign Off Report** when the question is whether an assigned review received final confirmation.

Find the matching certification and inspect its confirmation evidence, including **Sign Off Date** and the actor shown by **Reviewer** in this report.

That Reviewer column has a different purpose from the current-assignee column in the Campaign Status Report.

For our ordinary flow, it identifies the reviewer's final confirmation of the choices. The export item's Revoke and the review's sign-off are connected, but separate facts.

The report also has documented administrative cases. It can name an administrator, including when an administrator completes an overdue campaign. Establish the actual completion path before describing the record as the original reviewer's personal confirmation.

**First Action Date** concerns the first decision. It cannot substitute for Sign Off Date.

A confirmed review still leaves a further question: what happened to the permission that was rejected?

## Follow the removal work

**Remediation** means carrying out a change required by the review, such as removing Export Ledger from the account.

Use the **Campaign Remediation Status Report** to examine the state of rejected items. The help describes this report as available after an administrator has completed a campaign.

Match the exact account and access item, then examine **Status**, **Completed** and any **Comments**.

The meaning of Finished depends on the removal path. It can follow verification that access was revoked on a connected source. It can also follow a manual task or service desk ticket being marked complete.

A **manual task** assigns work to a person. A **service desk ticket** records work handled through a service management system. Closing either work record is a different observation from inspecting the application's permission.

In our supplied example, the removal uses a manual task. Someone marks that task complete, and the report shows Finished.

Later, authoritative evidence from Ledger Production shows that ledger-930 still has Export Ledger.

The report has recorded the task's closure. The account evidence shows that the required permission change has not been achieved. Preserve both facts, correct the unfinished removal through the permitted process and verify the resulting account.

After that correction, suppose fresh application evidence establishes that export is absent and viewing remains available. You can now support that specific account result. Generate updated campaign evidence where needed, and interpret any remaining discrepancy in the actual task and reporting path.

There is no need to describe every Finished result as unreliable. Determine what established that status and what that observation proves.

## Examine the operation behind the change

**Provisioning** is work that changes accounts or access in an external system. Removing a permission through a supported integration is one kind of provisioning work.

The **Provisioning Activity report** helps inspect individual provisioning events. You can select an event for more detail, and a downloaded report contains the results of the provisioning-event query.

For a removal investigation, match the event to the intended account, source, operation and time. A successful event involving a different account does not explain our export permission.

Read the event details and errors before deciding what happened. The event records explain the operation within their scope; the conclusion about current access also needs evidence that covers the required account and permission.

That evidence can include supported source confirmation. It does not always require someone to sign in interactively as the affected user.

Provisioning Activity is broader than certification work. A nearby account change may have come from another process. Establish the relationship rather than assuming that matching dates prove the campaign caused it.

Here is a useful starting point for choosing evidence:

| Question | Start with | What still needs checking |
|---|---|---|
| How was this campaign configured? | Campaign Composition Report | Actual included people, accounts and access |
| What choice was recorded on an item? | Campaign Status Report | Correct item, actor, reason and final confirmation |
| Who confirmed the assigned review, and when? | Certification Sign Off Report | Actual reviewer or administrative completion path |
| What is recorded about rejected-item removal? | Campaign Remediation Status Report | What Finished means for this removal path |
| What operation ran, or failed? | Provisioning Activity report and matching task or ticket | Exact account/right and supported result evidence |

The diagram connects each question to its evidence. The branches are choices for your investigation, rather than a sequence of report-generation jobs.

```text
What do you need to establish for this campaign?
                       |
    +------------------+--------------------+
    |                  |                    |
Configuration     Item choices       Final confirmation
    |                  |                    |
Composition       Campaign Status    Certification
Report            Report             Sign Off Report

Required removal work
    |
Campaign Remediation Status Report
    |
Match the actual task, ticket or provisioning event
    |
Establish the result for the correct account/right

For every branch:
match campaign and records, then check scope and time.
```

## Generate and read the right file

Once you know the question, choose the actual campaign and available report.

Check the campaign's ID as well as its readable name. A recurring monthly review can have a similar name to an earlier campaign. The name alone may not identify the intended instance.

In the campaign's report-download flow, select the report and an available file format, request generation, wait for generation to finish, then download the result.

**CSV** is a file of rows and columns that is useful for checking and comparing individual records. **PDF** presents a document for reading and sharing; it can include extra summaries or charts.

The formats can present information differently. Select the one that preserves the detail needed for your question, and check the actual contents.

A download made today can still be an old report. When campaign records change, generate the report again to obtain the updated state.

Report generation also does not refresh the source account or rebuild the campaign's review population. Those involve different records and operations.

Keep the report's generation time with the explanation. Compare decision, sign-off and account-observation times separately. The campaign report documentation uses GMT for its recorded times, so convert to a common zone when comparing local records.

If a report is unavailable, check its type, campaign state, applicable feature availability, permission and any generation error. The specific remediation and composition conditions already discussed matter; a broad statement about campaign reports does not make every file available in every situation.

## Reading records through an API

An **API**, or application programming interface, lets authorized software request data or operations from ISC.

A **request** asks ISC to do something or return information. A **response** is what ISC sends back.

A read request can help establish which review or report record you are inspecting. It does not require changing a reviewer decision.

In the next-generation API, reading one certification uses its certification ID. Reading one campaign report uses both its campaign ID and report ID.

These IDs identify different objects:

- The campaign ID identifies the organized campaign.
- The certification ID identifies an assigned review.
- The report ID identifies a generated report record.

A new report for the same campaign can be a different report object. Do not put a certification ID where the operation expects a report ID.

The named report object in the official software library describes properties including Id, CampaignId, Type, Format, Created and Status. This information is **report metadata**: information describing the report, rather than the report's access-item rows.

Use it to check the campaign association, report type, format, creation time and generation status. A report's Status describes the report job or result; it is not the status of the account permission.

An API response may present records as **JSON**, a text format containing named values and lists. Read the returned fields according to that operation's documented structure. A field called Status is meaningful only after you know which object it belongs to.

## Successful retrieval and a ready report are different results

The next-generation report operations separate listing reports, reading one report record, generating a new report and obtaining a download address.

The list and read operations can return report records regardless of generation status. A successful read therefore does not, by itself, mean the file is ready.

When a new report is needed, generation is a separate operation. It produces a report rather than changing the reviewer's access decision.

That generation request is **asynchronous**: ISC starts the work and the finished result is obtained separately. The documented successful response means generation started, rather than promising that the file is already complete.

Check the actual report record and its documented result. Once ready, obtain the download address through the supported download operation and retrieve the intended file. If generation fails, investigate that job before using an earlier file as though it were the new result.

An **HTTP response status** is the request-level code returned by the web interface. Its meaning depends on the operation.

For example, 200 on a report read means the read succeeded. On the documented report-generation operation, 200 means generation started. Neither statement proves that Export Ledger was removed.

Other responses help identify the next check:

- **401** concerns authentication, such as missing or expired authorization.
- **403** means the caller does not have access to that operation.
- **404** means the requested resource was not found through that request.
- **429** means the request rate was too high. Follow the response's retry guidance.

Do not read a permission error as “the campaign has no items.”

The next-generation report APIs require an organization administrator, certification administrator or report administrator role. By contrast, the certification-read operation also permits the reviewer of that certification.

A reviewer can therefore be permitted to read their certification without having permission to use the campaign report API. Use the permission rules for the actual operation.

These interfaces are marked Experimental and apply to next-generation campaigns. Their documented use requires the X-SailPoint-Experimental header set to true. A **header** carries extra request information, separate from the ID of the record being requested. Here, it explicitly enables use of the experimental interface. Check the supported engine and current interface before operational use.

## Check what the returned set includes

A successful response can contain only the records selected by the request.

A provisioning export reflects its query. A review-item request concerns the selected certification. Neither is automatically a complete list for every campaign.

**Pagination** means returning a collection in portions. If an operation uses it, follow that operation's supported parameters to retrieve the required set. A first page alone does not establish the total.

Do not assume every collection accepts the same paging or filtering parameters. In particular, general pagination guidance does not add parameters to a report operation that does not document them.

An empty result also needs context. It may be the correct result for the chosen campaign, query, time or permitted scope. It does not automatically establish that no review or removal work exists elsewhere.

Keep the original request or query and the relevant IDs with retained evidence. When a file does not expose all those IDs, retain the checked association with the campaign from which it was generated.

Preserve the needed reports before deleting a campaign: the documented deletion also deletes its reports. Retain and share account and identity information only through the organization's permitted evidence process.

## Try a similar name with different records

Two monthly campaigns have similar readable names.

The older campaign, C-610, is completed. Its retained item report shows Revoke for export, and its matching sign-off report records confirmation of that assigned review.

The newer campaign, C-621, is active. You have not yet inspected its current export item.

An analyst downloads the old file today. A provisioning query also returns no events, but the supplied query uses the wrong source and a time range before the newer campaign.

The analyst concludes, “C-621's export removal is complete. There are no failed events.”

Start by matching the evidence. Which campaign does the file actually describe? Does the query cover the source and time relevant to that account?

The old campaign's decision and sign-off cannot establish the newer campaign's choice. Today's download has not changed the old report's generation time or campaign association.

The empty provisioning result answers only the supplied query. It cannot establish success or absence of failure outside that query.

Now a successful API read for C-621 lists only earlier generated report versions. That response establishes which report records were returned; it does not create a fresh report.

Finally, the correct current records for C-621 are obtained. They show that export is included, its item status is Open, and no choice has been saved.

The supported conclusion is that this item still needs a review decision. There is no supplied finalized Revoke in C-621 from which to claim completed removal.

Report the facts with their scope: the older campaign had its own recorded decision and confirmation; the newer campaign's export item is included and undecided; the supplied provisioning query did not cover the relevant work.

That explanation tells the next person what is established and which question still needs action.

