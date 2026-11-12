# What does completing a campaign actually establish?

You open a certification campaign and see that it is completed.

A colleague asks, “Can we now say that everybody has the correct access?”

Before answering, look at what was completed and what evidence supports that larger claim. The campaign record describes the campaign. The application account describes the access a person can actually use. You need to connect the two.

## Start with the review and the account

In SailPoint Identity Security Cloud, or **ISC**, a **campaign** organizes a set of access reviews. A **certification** is one assigned review within it. A **review item** is an access entry on which the reviewer acts.

An **account** is the record through which a person or service uses an application. Its **access** is what it is allowed to do there. Reading an archive record and exporting a collection of archive records are different permissions.

A **source** is a configuration in ISC for an application or its account data. ISC collects account information through it. A review uses information held in ISC. The actual application remains the place where a permission must work or stop working.

The **reviewer** examines the assigned access and records a decision. For a permission that can be reviewed individually, **Approve** accepts continued access under the reviewed conditions. **Revoke** records that it should be removed.

In ISC's newer, next-generation review experience, the reviewer also gives a final confirmation, called **sign-off** or **finalization**. Saving item choices and finalizing the assigned review are separate actions.

These records answer different questions. A saved Revoke tells you the chosen decision. A successful sign-off tells you the assigned review was finalized. Neither observation, by itself, tells you what the application account currently permits.

## How an ordinary review reaches completion

In the normal documented next-generation flow, a reviewer examines all items, checks the choices and signs off. The finalized review becomes read-only for ordinary decision changes.

If a removal is required, **remediation** is the work that carries it out. ISC may send a supported change to the application, or a person may receive work to make that change. The resulting request or task is a record of work to be done.

In the normal next-generation campaign path, all reviewers must finish their assigned reviews. If no removal is required, the campaign can complete. If removal is required, the documented flow includes a remediation phase and completes the campaign after those requests finish.

That does not make every use of the word completed interchangeable. You still need to know what a completed request establishes. A supported operation may include confirmation from the application. A human task may instead be marked complete by the person carrying out the work.

There is also a separate administrative completion path. An authorized administrator can complete an overdue campaign under its configured rules, including the handling of undecided items. An **undecided item** has no recorded choice. An **unsigned review** has no final review confirmation and may already contain saved choices.

Administrative completion does not establish that every original reviewer personally examined and signed every item. Before drawing that conclusion, inspect the actual decisions, actors and sign-off records.

Exact treatment of saved choices in unsigned reviews needs care: current guidance gives conflicting descriptions. Establish the supported behavior for the actual campaign before applying or describing an administrative bulk result. A visible saved choice alone is not enough to predict it.

The **certification engine** is the service processing the campaign. ISC has newer next-generation and older legacy campaigns. Do not combine one engine's normal review flow, a separate administrator action and a report label into a single guaranteed sequence for every campaign.

## An accepted action is still different from its result

Suppose software requests administrative campaign completion. An **API** is the interface through which it submits that request.

The documented next-generation Complete operation requires an authorized Org Admin or Cert Admin and a campaign that is past due. It returns an accepted response when the system has accepted the request.

Accepted tells you about the request. To establish the result, inspect the campaign afterward. If removal is required, follow its work and account evidence too.

Asking ISC to complete something, seeing that it completed, and establishing what happened to access are separate observations.

The same care applies when using an interface button. A successful result needs the actual campaign record, not only the fact that someone selected an action.

## Follow one completed campaign to the application

Consider an account called **arc-7101** on **Archive Production**. It has two individually reviewable permissions:

- **Read Archive** allows it to read stored archive records.
- **Export Archive** allows it to download archive records in bulk.

The account information and its association with the correct person have been checked. Reading remains needed for the person's current work; bulk exporting does not.

A suitable independent reviewer has permission to perform the review. They approve reading, revoke exporting and successfully sign off on those choices. The campaign's successful completed state is also recorded.

For this application, the required removal is carried out manually. The existing task identifies arc-7101, Archive Production and the export permission. Its assigned operator marks it complete.

You generate the Campaign Remediation Status Report, and the matching row says **Finished**.

There appears to be agreement: the review was finalized, the campaign is complete, and the removal record is finished. Now look at a supplied current application check: arc-7101 still has Read Archive and can still export archive records.

The export removal has not achieved its required result.

The report's meaning explains why this combination needs investigation. Its Finished status can follow removal confirmed on a connected source, or completion of the related manual task or service desk ticket. A **service desk ticket** is a work record in a service-management system. Its closure can report that work is finished without independently demonstrating every account permission.

In this example, you have the manual-task closure and current evidence that export still works. Do not use the campaign or task label to overrule that account evidence.

You also do not need to ask the reviewer to choose Revoke again. The correct finalized decision already exists. Identify why the actual account change is missing and arrange the supported follow-up with someone authorized to make it.

The records below lead to different conclusions. Read the arrows as evidence relationships, not as the order in which ISC runs every process.

```text
Finalized assigned review
        |
        +--> Reviewer confirmed the recorded choices

Completed campaign record
        |
        +--> Campaign reached its recorded completed state

Closed manual removal task
        |
        +--> Work was reported complete

Current correct application account
        |
        +--> Establishes the observed permission result

Connect these records before making a closure claim.
```

A correct outcome here must preserve the account and its justified reading while removing the ability to export archive records. Disabling the whole account would create a different result and interfere with the work that still requires reading.

## Keep the remaining work visible

The **campaign owner** is responsible for the campaign according to its configuration. That person or an authorized coordinator needs an accurate account of what remains.

For the Archive example, the message should be specific:

“The review and campaign are complete. Export removal for arc-7101 on Archive Production remains unresolved. The manual task is closed, but the current account check shows export still works. Reading must remain.”

That statement connects the records and names the gap. It does not claim that the whole campaign failed, or that all access is correct.

Now establish the responsible follow-up person, the required change, the evidence they need and when the result will be checked. Responsibility for coordinating the issue and permission to change the application may belong to different people.

Confirm that the person or team accepts the work. A note saying “sent to support” is not enough to establish that someone is handling the specific account change.

Use the supported work process for the environment. Writing a handover note does not automatically create an ISC task, reopen a closed task or change the application. Inspect any actual task or ticket that is being used and keep its scope connected to the original requirement.

Where delay leaves inappropriate access in place, raise the actual risk and required decision with the authorized owner. Acknowledging or accepting that risk does not mean the permission has been removed. Record the remaining work honestly.

**Closure evidence** means the records that support a specific statement about finished work and any remaining obligations. Here it includes the review decision, the campaign result, the closed task, the account observation and the accepted follow-up. Keep those records connected through the organization's evidence process.

## Finish the account change, then update the evidence

Suppose the authorized application operator now removes Export Archive from arc-7101 and preserves Read Archive. Reliable current evidence confirms that this account can still read but cannot export through the permission paths checked for this requirement.

You can now support the required access outcome for this account. Keep the actual scope and observation time with that conclusion.

ISC's collected account data also needs to reflect the change. **Aggregation** means reading account information into ISC. For a file-based source, the imported file must describe the actual updated account.

Aggregation does not perform the external manual removal. Importing a file that says export is absent while the application still allows it would create misleading information.

After the correct updated account data has been collected, regenerate the relevant report when needed and compare it with the underlying evidence. The time you download a report is not automatically the time the application changed.

A supported automated change can supply reliable application confirmation within its actual scope. You do not have to insist on a separate human login to every account. What matters is whether the evidence establishes the required result for the correct account and permission.

The closure statement can now name the completed review, campaign, resolved export removal and retained reading, with their relevant records and times. It should not become “this person has no other inappropriate access anywhere.” That would require a much wider review and evidence.

## Match the completed work to the requested review

Before making a statement about the whole campaign, check that it covered the intended people, accounts and access. Use the actual campaign and review period, rather than a different campaign with a similar name.

Suppose the request included two production accounts, but the generated campaign included only one. Finishing every item in that campaign would still leave the other account unreviewed. A completed state cannot reveal that omission on its own.

Compare the intended review with the actual contents and results. Explain any exclusion or missing work and arrange the required follow-up. An unresolved omission remains part of the closure account; it should not disappear because the included items were finished.

Likewise, one correctly removed permission is evidence for that permission. To claim all required removals are resolved, account for the whole required set and its exceptions. Equal totals or one successful sample cannot identify which individual changes actually happened.

## Check who made each decision

A person assigned to a certification, a person who saves a decision, and an administrator who completes a campaign can be different people.

For example, a campaign status report can retain an earlier **Decision Maker** after the review has been reassigned. Sign-off evidence can also involve an administrator under the documented conditions.

If your conclusion is “the manager signed off,” check the actual signer and time. An administrator's completion is not the manager's personal confirmation.

Keep policy-handled items distinguishable from items a reviewer examined. **Maintain access to undecided items** is a configured completion choice that keeps affected existing access. In the documented path, previously untouched items can be approved through that handling.

Such an approved result does not supply the business facts that an absent review never established. The campaign's completion record and the quality of the access judgment answer different questions.

## Try a different completed campaign

A Billing account holds **View Invoices**, which allows reading invoices, and **Export Invoices**, which allows downloading invoice data.

The supplied campaign contains only those two items. Neither ever had a saved decision. An authorized administrator used the verified maintain-access completion path, and the campaign completed successfully. Both existing permissions remain.

A current account check agrees with ISC's collected data. A coordinator says, “The campaign is complete and the data matches. The reviewer has confirmed both permissions are appropriate.”

Which part of that statement goes beyond the evidence?

The campaign completed and the account information agrees. But no reviewer examined the two items in this case. Their approved outcome came from the configured completion handling.

You still need the relevant current work requirements and an authorized assessment of whether each ability is appropriate. Matching permission data establishes what the account holds; it does not establish why the person should hold it.

Now someone supplies a newly downloaded report showing both items approved. That does not fill the missing business judgment. Establish how the result was produced and who actually acted, rather than treating the report's newer date as a new review.

If investigation finds that exporting is no longer justified, arrange a permitted correction or access change with clear responsibility and outcome checks. Do not assume a completed review can simply be edited or that a future campaign will automatically resolve the current access.

The useful completion statement stays accurate: the campaign was completed using the configured maintenance rule, both permissions remain, and an informed access assessment is still outstanding.
