# CLS-004: Use activity and recommendations to support a review

Someone still needs an account for a quarterly task. The account may show little recent activity because the next run has not happened yet.

Another person may use the application every day but no longer need its Export permission. Their remaining work may require only Read.

These are different situations. To review them well, we need to understand what the information on the screen can tell us, then connect it to the person's current work.

You will inspect the context available for two Export permissions, record any gaps, make justified decisions and follow the one required removal. The application accounts are represented by CSV. It supplies permission values for ISC to collect; it does not create an application-usage history.

## Separate the permission, the signal and the reason

An **identity** is ISC's record for a person. An **account** is that person's record in a managed system. A **source** holds ISC's connection configuration and collected account data for that system.

An **entitlement** is a permission ISC tracks. We will review Export, meaning permission to download reports in bulk.

The account data can show that someone has Export. It cannot establish why they still need it.

**Approve** records that the access should be kept; **Revoke** records that it should be removed. An **undecided** item has no recorded choice. The reviewer needs enough evidence to justify that choice.

Two additional kinds of information can help:

A **recommendation** is guidance based on identity information and access patterns. ISC can compare the person with **peers**, identities it treats as comparable, and examine how common this access is in that group. A **model** is the method used for that comparison. Read the displayed explanation to understand the actual recommendation.

**Activity Insights** collects activity **events**, records of things that happened, such as logins, from supported sources. This can help show whether an identity used a source. You still need to establish what events and accounts the information covers.

Neither one is the person's current business authorization. That comes from an approved work requirement and someone responsible for confirming it.

Keep the questions separate as you work:

| Information | What it helps establish | What still needs checking |
|---|---|---|
| Collected Export holding | The account is recorded as having Export. | Whether the person still needs it. |
| Recommendation | How the access compares with the model's patterns. | Whether the person's actual duty justifies it. |
| Source activity | Activity captured for the source and period shown. | Whether it proves use of this particular permission. |
| Current work confirmation | Why the person should retain or lose access. | Whether the confirmation is authorized, current and specific enough. |

## Prepare the two review items

Use your approved training tenant and an administrator allowed to create the campaign and collect the test source. `certlab-manager01` needs a working reviewer session. `certlab-manager02` is A's **source owner**, the person responsible for that source in ISC. Verify the actual recipient and authorized performer of any removal task later.

The prepared five people belong to certlab-people-profile, fed by certlab-people-csv. Verify employee01 and employee02 are associated with their correct accounts and manager01 is their stored manager. Importing a person does not itself provide a working reviewer login.

A **holding** means one account has one permission. Restore and inspect these original baselines after resolving any outstanding earlier work:

- A, **certlab-reports-csv**: account01 has Read+Export for employee01; account02 has Read+Export for employee02; account03 has Read for employee03. Three accounts, five holdings.
- B, **certlab-owner-reports-csv**: its original four accounts and six holdings remain unchanged. All B access is outside this review.

The full account names use the `certlab-` prefix. Original values are in `lab-data/baselineA/report_accounts.csv` and `lab-data/baselineB/owner_review_accounts.csv`. Keep complete private source-template copies outside the reusable course folder.

An access profile bundles permissions. Roles and lifecycle states can require access automatically, for example because someone has a job role or is in an active-employment state.

On A, confirm these are direct, individually reviewable entitlements. No temporary profile, role or lifecycle requirement should replace their review unit or require Export to be granted again. Reconcile earlier access-model changes before starting.

Our review includes exactly:

| Person | Source | Account | Permission | Reviewer |
|---|---|---|---|---|
| certlab-employee01 | A | certlab-account01 | certlab-report-export | certlab-manager01 |
| certlab-employee02 | A | certlab-account02 | certlab-report-export | certlab-manager01 |

Read, employee03, manager access and all B holdings stay outside the selected review.

Use these supplied training work facts:

Employee01 has an approved recurring report-export duty. The duty continues between runs. Record a planned next-run or reconfirmation point in your private training notes.

Employee02 had Export for a migration. At the first checkpoint, confirmation of any continuing Export need is still pending.

These are exercise facts, not events observed in a real reporting application. We will keep employee02's choice open until the missing work confirmation arrives.

## Ask ISC to include recommendations when available

A **certification campaign** organizes access review work, its reviewers and its deadline. A **certification** is an assigned review inside it.

Open **Search > Certification Campaigns > New Campaign > Identities**. Under **Using a Search Query**, choose **Create Campaign**, then **Specific Identities that I Select**.

Run:

`name.exact:"certlab-employee01" OR name.exact:"certlab-employee02"`

The query finds candidates with those exact identity names. Inspect their actual IDs and use **+ Add To Campaign** for only those two. Check **Added to campaign**, then select **Certify Selected Identities**. Finding a person in Search does not by itself add that person to the review.

Choose **Refine Access Items** and add only A's certlab-report-export entitlement. Check its actual source and object ID. B has a similarly named permission, so selecting by display name alone is insufficient.

Name the campaign **certlab-cls004-context-run01**. If that name already exists, use an unused run suffix and record it; preserve earlier history.

If the licensed campaign offers **Include Recommendations in your campaign**, enable it for this campaign and record the saved setting. If the control is unavailable, record that fact. Keep global settings and identity attributes unchanged.

The setting asks ISC to include available guidance in the campaign. It does not approve or remove access, and it does not guarantee a recommendation for each item. Our small training dataset may not provide a useful peer comparison.

Choose **Manager** when offered so the employees' recorded manager receives the review; verify manager01's actual responsibility. Choose a permitted future due date, the date by which the reviewer should finish. Maintain undecided access so an item without a decision keeps its access when the campaign is completed under that setting. Require Revoke comments and turn campaign emails off. If all decisions require comments, explain both.

A **preview** shows the generated review contents; a **template** preserves settings for reuse. Generate a preview now and save an unscheduled template. Record the saved-template and generated-campaign references separately. Do not schedule another run.

Check the two exact A Export holdings and actual reviewer. Check that Read and B are excluded. Two holdings do not necessarily mean two separately assigned certifications.

Start only the correct preview. Preserve its actual campaign ID and configuration.

## Inspect the context before entering a final choice

Sign in as manager01. Open **Certifications > Active**, select the assigned review and inspect the two Export items.

For each item, start with the person's identity, A source, exact account and entitlement details. A recommendation about a different account or source cannot establish the need for this holding.

In private notes, record the following as you inspect:

- The actual identity, source, account, entitlement and campaign references.
- The current permission holding and available account-collection time.
- The campaign's recommendation setting and what the reviewer actually sees.
- Any displayed recommendation and its explanation, or the fact that none is shown.
- Any genuine source-activity information, its period, scope and available update time.
- What remains unknown and what work confirmation you need.

Record your observation time separately from the data's time. Looking at a panel today does not establish that its events or model calculation are current today.

If the interface does not show a data-update time, write “not shown.” Do not substitute the observation time.

### Open a recommendation rather than following its colour

If **Recommended** or **Not Recommended** appears, select the icon and read its reasons.

Record the actual explanation for this identity and access item. Avoid replacing it with a general comment such as “AI said yes.”

A peer-based recommendation can help identify an unusual permission. An unusual permission can still be justified by a specific assigned duty. A common permission can also be unnecessary for one particular person.

If no icon appears, record “no recommendation shown.” That is different from Not Recommended. Check campaign inclusion and actual feature/data availability. With recommendations available, a person who has no peer group may also have no icon; absence alone does not establish which cause applies.

Do not change manager links, add fake peers, remap identity attributes or broaden the campaign to manufacture a recommendation.

Your recommendation-detail practice is complete only when you have inspected a genuine in-scope explanation. If none is available, keep that outcome recorded as not available for this run.

### Establish what the activity information measures

For genuine activity information associated with the reviewed source, inspect its meaning before using it.

The certification feature can show the number of days an identity was active during a 90-day period. Several counted logins on the same day still describe one active day, so days active is different from a login count. Source activity also does not establish that the person used Export; the activity could concern Read.

Record the actual period and metric shown. Check which identity, source and accounts it covers, which events are collected and whether collection has gaps. Use verified source configuration or source-owner information where the panel does not answer those questions.

If the account coverage or last update is unknown, retain that limit in your notes.

Keep these situations distinct:

An explicit zero for a verified period means the displayed metric recorded no counted activity in that scope.

A blank panel or missing feed gives you no such measurement.

**Account aggregation** reads account and permission data into ISC. Its completion time tells you when that collection finished, not when activity events were last collected.

Our supplied A CSV has no Activity Insights event feed. Uploading its permissions again cannot create login or usage evidence. Adding a column called lastUsed would still be ordinary supplied account data, rather than a configured Activity Insights event collection.

If A unexpectedly displays activity, verify the actual ingestion and account association before trusting it. Do not copy another source's activity into A's evidence.

If genuine usage data is unavailable, record that outcome. You can complete the CSV review using confirmed work requirements, while practice with actual Activity Insights data remains not run. Collecting real activity later requires a separately prepared supported source and its own matching review scope.

### Apply the same checks to other context

If a relevant flag or additional attribute is genuinely present, inspect what it means and where its value came from.

A sensitivity flag can tell you to examine a permission carefully. It does not establish that the permission is unnecessary. Keep the exact item, source, meaning and known update time with the observation.

There is no need to add cloud, data-security or other product integrations just to fill the screen.

## Pause where the business fact is missing

Before final submission, compare your notes for the two people.

Employee01 has a confirmed continuing duty. Low activity, missing usage data or a Not Recommended signal would need explanation, but would not by themselves cancel that authorization.

For employee02, the missing fact is whether any Export work continues. An activity count or peer recommendation cannot answer that question for us.

**Sign-off** is the reviewer's final submission. An **unsigned** review has not received that confirmation; saving a choice alone does not provide it. Leave employee02's item undecided and the assigned review unsigned. Preserve this checkpoint and record the question the responsible manager or application owner needs to answer.

A useful question is specific:

> Does employee02 have any continuing approved task that requires Export on this account after the migration?

If a real answer remains unavailable, follow the organization's escalation or handover process before the deadline. A missing answer is not a reason to invent one or submit an unsupported decision.

## Use the confirmed work to complete the review

Now use the next supplied training confirmation:

Employee02's migration is complete. The responsible owner confirms there is no other continuing Export duty. Read remains required.

You can now justify both choices:

Approve employee01's Export because the approved recurring export duty continues. Record the planned reconfirmation point. This note does not configure an automatic expiry in ISC.

Revoke employee02's Export because its purpose has ended and the responsible owner confirmed no other continuing requirement. Retain Read and the account.

Include any actual optional signals in the explanation with their limits. If a recommendation disagrees, explain the verified work fact that determines the choice. If no recommendation or activity is available, say that plainly without presenting absence as inactivity.

For example, employee02's reason can state:

> Migration complete; no continuing approved Export task confirmed by the responsible owner. Remove this account's Export and retain Read. Activity Insights usage data was unavailable in this CSV exercise.

Use that last sentence only if it matches your actual observation.

Inspect the saved choices, then finish and sign off through the actual final confirmation for all assigned work. Preserve the decisions, reasons and sign-off evidence.

If actual authorization or account facts differ from the supplied training case, investigate before applying these expected choices.

## Follow the removal and verify what remains

Return to the administrator's session and inspect the actual work in **Admin > Dashboard > Tasks**. A **manual task** instructs an operator to carry out the required removal. The recipient can open it in **Task Manager**. Match the campaign, A source, employee02's account, Export permission, actual recipient and full task scope.

If matching work is missing, investigate sign-off, campaign state and the removal path before editing any file.

The authorized task performer removes only employee02's Export row from the complete private A account file. `lab-data/baselineA/report_accounts_after_employee02_export_removal.csv` shows the expected values for comparison.

This edit simulates the external application's permission change. It does not prove a real application's Export ability changed.

Upload through the task's supported file step, or have the authorized administrator open A under **Admin > Connections > Sources > Account Management > Account Aggregation**. Follow successful collection and verify:

- A retains all three accounts and all three Read holdings.
- Employee01 retains A Export.
- Employee02 no longer has A Export.
- A has four holdings; B still has its original six.
- Both A entitlement definitions and the correct account/identity associations remain.

Only after the full listed work is fulfilled and checked should the recipient use **Mark Complete**. An authorized administrator can use **Actions > Mark as Complete**. Inspect the completed state and preserve the changed full private file, task, collection and account observations with your context notes.

Record the outcomes separately: the CSV review/removal result, any actual recommendation-detail inspection, and any actual Activity Insights data inspection. Completion of one does not establish the others.

## Work through a signal that disagrees

Suppose employee02 has a favourable recommendation and recent source activity, but the owner has confirmed the Export migration ended.

Does that mean the review should approve Export?

<details markdown="block">
<summary>Connect the evidence to the permission</summary>

The recommendation describes a statistical pattern. The source activity describes events in its recorded scope. Neither establishes another continuing authorized Export duty.

The person may still use Read. That could explain source activity without establishing Export use.

Check the owner confirmation and whether any other approved Export requirement exists. If none exists, the ended purpose supports Revoke despite those signals. Retain the current authorized Read access.

If the facts conflict or the confirmation is incomplete, investigate before deciding. The lesson is to explain a supported decision, rather than always agree with or always ignore a recommendation.

</details>

This is a reasoning case. Do not alter data to force a favourable icon or manufacture activity.

## Restore the baseline and preserve the evidence

Keep the signed review, actual context observations, unavailable-data notes, work confirmations and removal proof. Resolve all outstanding tasks and operations before restoration.

Restore the complete private original A account file and follow aggregation through successful completion. Verify three accounts and five holdings: Read+Export for employee01/02, Read for employee03. B must still have its original four accounts/six holdings.

Recheck account associations and manager links. Keep the later training restoration time separate from the earlier removal result.

Retire only this run's unneeded unscheduled template in **Search > Certification Campaigns > Saved/Scheduled**, matching its saved reference and actual run name after checking no generation remains. Keep the separate completed campaign, its reports and task history.

No global recommendation setting, model, activity feed or identity mapping needs resetting. A recommendation or Activity Insights outcome that was not available remains not run; do not turn the completed CSV result into a claim that those features were tested.
