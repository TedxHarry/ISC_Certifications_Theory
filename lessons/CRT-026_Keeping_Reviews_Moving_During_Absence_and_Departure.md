# The reviewer is absent or leaves during the campaign. What now?

A reviewer goes on leave while an access review is still open. Someone else agrees to cover the work. You save a work reassignment in SailPoint Identity Security Cloud, or ISC, and expect the replacement reviewer to take over.

Before you rely on that setting, check which work already exists. A setting that redirects work created during an absence does not collect all the unfinished work that was assigned earlier. You can have the right replacement and the right dates, yet still leave an earlier review waiting with the absent person.

Let's follow these two responsibilities separately: arranging a handover for existing reviews, then arranging who receives work created during the absence.

## What is waiting for the reviewer?

An access certification asks whether somebody should continue to have particular access. A **certification campaign** organizes that review work. Within the campaign, a **certification** is an assigned review, and its **review items** are the individual access entries on which decisions are recorded.

The **reviewer**, also called the certifier, is responsible for assessing that assigned work. Going on leave does not answer the access questions. The review still needs someone who understands the access and the person's current need for it.

For a small example, consider Reporting Production, an application whose account information ISC has collected. ISC keeps a representation of that application as a **source**. It connects each account to an **identity**, the record representing the person who owns it.

Identity 3503 owns account `rep-3503`. That account has **Export Reports**, permission to export report contents. In ISC, this access right is represented as an **entitlement**. The campaign includes it as an individual review item. The account information is current, the person/account connection is correct, and this entitlement is eligible for individual review.

The assigned review, R-old, already exists with reviewer 3501. It is active and has not been signed off. **Sign-off** is the reviewer's confirmation that the review's decisions are ready to be finalized. Here, the work still needs attention when 3501 goes on leave.

Backup reviewer 3502 is available, understands the reporting access, has the required permission to review the assigned work and is not being asked to review their own access. These checks matter together. A person can be available without knowing enough to make the decision, or knowledgeable without having the required ISC permission.

## Deal with the review that already exists

R-old is assigned to 3501 now. To hand over that existing responsibility, an authorized person must use a supported reassignment action for that work.

**Reassignment** changes who is responsible for selected review work. The selection matters: a whole certification can contain several people's access. A more specific supported action may move the review work for selected people, or individual review items. Choose the amount of work that matches the required handover and the action your environment supports.

For R-old, the requirement is to move the whole assigned review to 3502. An administrator with the required permission checks the current state and uses the certification reassignment action available in the environment. For this administrative action, the campaign must be in preview or already started, and the certification must still be unsigned. **Preview** means the review work has been generated for checking before the campaign starts. R-old is already active and unsigned, so it meets those state conditions. A signed-off certification cannot be moved through this path. The recipient's own-access check also applies.

The administrator records why the work is moving and who the new reviewer can contact. After the action, they inspect the resulting assignment and confirm that 3502 can open the intended review. They also check its items, saved decisions and decision history so the handover does not leave unexplained missing work or misleading history.

In this example, the resulting record shows R-old assigned to 3502. That changed assignment establishes the handover. Saving a setting for future work would not establish the same result.

## Arrange where newly created work goes

ISC's **Work Reassignment** feature lets you configure automatic redirection for work assigned during a specified period. The configuration says whose work to redirect, which type of work it covers, who should receive it and when the redirection applies.

Think of the configuration as an instruction ISC can use when that work is created. The certification record is the actual review someone receives. You need to check both because a correct instruction and an actual assignment are different records.

For reviewer 3501's absence, the instruction is:

- Redirect **certifications** assigned to 3501 to 3502.
- Begin on Monday at 09:00 and end on Friday at 18:00.
- Interpret both times in **Asia/Kolkata**.

The work reassignment feature must be enabled for the site. A user can configure their own work, a manager can configure work for their team members, and an administrator can configure it on a user's behalf. Use the appropriate actor and scope. Being the owner of a campaign does not, by itself, establish permission for every administration action.

The **Work Item Type** identifies the kind of work being redirected. Certifications, access request reviews and manual provisioning tasks are separate choices. An access request review asks someone to assess a request for access. A manual provisioning task asks someone to carry out a required account or access change. A configuration for certifications does not also arrange cover for those other tasks.

The **Assign To** field identifies the recipient. Start and end fields define the period. The **Time Zone** tells ISC how to interpret those clock times; its default comes from the browser. Read the saved zone instead of assuming a displayed 09:00 means your local 09:00. If a selected region changes its clocks for daylight saving time, take that into account when arranging cover.

The saved configuration appears in the scheduled reassignment list. That confirms which instruction is recorded. Now follow what it does to the review work.

## Follow work created before, during and after the absence

Keep the ordinary reviewer assignment unchanged for this example: it selects 3501. Work reassignment is enabled, and the certification configuration above is active during the absence. No other redirect, group assignment or own-access issue affects these reviews.

R-old existed before the period. It was moved separately to 3502 through the authorized existing-work handover we just followed.

R-new is created during the configured period. It includes identity 3504's account `rep-3504` with **View Reports**, permission to read reports. The account data and person connection are correct, and the entitlement is individually reviewable. Ordinary assignment selects 3501, but the active certification work reassignment redirects the newly created work to 3502. The resulting assignment is checked and shows 3502.

After Friday 18:00, reviewer 3501 has returned and is available. R-after is created for identity 3505's account `rep-3505`, also with View Reports. The ordinary assignment still selects 3501. The absence period has ended, so this configuration no longer redirects the new work. Its resulting assignment shows 3501.

These are the three supplied outcomes:

| Review | When it was created | How it reached its reviewer | Reviewer after the absence ends |
|---|---|---|---|
| R-old | Before the period | Separate, verified handover of existing work to 3502 | 3502 |
| R-new | During the period | Automatic work reassignment to 3502 | 3502 |
| R-after | After the period | Ordinary assignment to returned reviewer 3501 | 3501 |

The end time stops this configuration from redirecting more newly created work. It does not send R-old or R-new back to 3501. Those reviews stay with 3502 unless a separate supported action changes their assignment.

The arrows below show how each review reached its reviewer. They do not show a sequence in which the same review moves through all three rows.

```text
Ordinary assignment selects 3501.
Certification redirect: 3501 -> 3502
Period: Mon 09:00 to Fri 18:00, Asia/Kolkata

BEFORE THE PERIOD
R-old already belongs to 3501
  -> separate authorized existing-work handover
  -> verified reviewer 3502

DURING THE PERIOD
R-new is created for 3501
  -> active certification work reassignment
  -> verified reviewer 3502

AFTER THE PERIOD
R-after is created for returned reviewer 3501
  -> this redirect no longer applies
  -> verified reviewer 3501

R-old and R-new remain with 3502.
Ending the period does not return earlier work.
```

Suppose the administrator had saved only the automatic configuration and had never moved R-old. R-new could still reach 3502 correctly while R-old remained with absent reviewer 3501. Checking one successfully redirected review would miss the unfinished earlier work. That is why absence cover needs an inventory of existing work as well as a future-work setting.

## Replacing or ending the instruction changes future handling

Only one work reassignment configuration can exist for a person and a particular work type at a time. Adding another certification configuration for that same person replaces the previous certification configuration.

For example, 3502 may become unavailable before the original reviewer returns. A new configuration can identify another suitable backup for subsequently created certification work. It does not, merely by replacing the setting, hand over every review already held by 3502. Inspect those existing reviews and arrange any necessary supported transfer separately.

Configurations added by the user, their manager or an administrator appear together for that user. Within their permitted scope, these actors can replace or delete configurations added by another actor. Before adding a replacement, inspect what is already saved and coordinate the change. Two people independently arranging cover can otherwise replace each other's intended recipient or dates.

Deleting the configuration has the same important boundary as reaching its end time: previously redirected work stays with its new reviewer. The original reviewer returning to work does not itself move that work back either. If returning some reviews is necessary, first check who holds them now, what state they are in and whether the proposed handover is supported.

The **No end date** option leaves the configuration in place until it is manually removed. This is useful when redirection should continue without a planned return date. It still needs an accountable person to maintain it. A backup who later changes jobs can become the next unsuitable recipient.

There is also a site-wide control to disable Work Reassignment. Disabling it stops further automatic redirection through this feature and retains the saved configurations. Previously redirected work remains with the new reviewers. The configurations can apply again when the feature is enabled, subject to their relevant conditions and periods.

Manual reassignment and reassignment through an **API**, an interface software uses to request an operation, are separate supported paths. Disabling automatic work reassignment does not prohibit all such actions. Their own permission, state and recipient requirements still apply.

## When the reviewer leaves permanently

A permanent departure needs a handover of unfinished reviews and a check of how future reviewers will be chosen.

Start with the departing person's actual assigned work. Identify the campaigns, reviews and items that still need action. Inspect saved decisions, sign-off state and deadlines, then arrange an eligible replacement for the work that can be reassigned. Confirm the resulting responsibility and that the replacement can inspect the access and complete the review in time.

Next, examine the information used to assign future reviews. A manager review uses a person's recorded manager relationship. An owner-based review can use recorded responsibility for a source or access object, according to its configured reviewer choice. If the departed person is still recorded in one of those positions, that information also needs attention through the appropriate process.

A permanent work redirect can send eligible newly created work elsewhere. It does not establish that the underlying manager or ownership record has been corrected. Keep the work cover and the responsibility data consistent so the organization can explain why future reviews reach their recipients.

Do not infer a handover from an identity becoming inactive or from the person's sign-in being disabled. Those observations do not show who now holds an unfinished certification. An inactive direct report may also be absent from a manager's My Team list. If the manager cannot find the person there, involve an administrator with the necessary authority rather than assume no review work remains.

A **governance group** is a configured group of identities that can share supported review responsibility. If the departing person is a member, inspect the membership and remaining reviewers. Changing an identity's active or disabled status does not automatically maintain that membership. An unavailable member still listed in a group is not evidence that another suitable member has taken responsibility.

## When work does not stop at the first backup

The replacement may have their own work reassignment. If 3501 redirects certification work to 3502 and 3502 redirects it to 3506, following only the first setting can give you the wrong idea about who received the review.

ISC prevents configuration loops such as 3501 sending work to 3502 and 3502 sending it back to 3501. For a long chain, the documented automatic work reassignment limit is four redirects, leaving work with the fifth person. Necessary own-access prevention can still cause further routing. Use that limit to recognize an unexpected chain, then inspect the actual assignment instead of counting arrows and assuming you have found the final reviewer.

Own-access protection matters because a backup may also have access included in the review. In the documented automatic certification reassignment process, that person's own access is separated into another certification and sent to their manager. If the person has no manager, it goes to the campaign owner. If that person is also the campaign owner, ISC sends the work to a randomly selected administrator. The campaign owner is the person responsible for the campaign; that responsibility does not permit them to assess their own access. Check who actually receives the separated work. The backup being a suitable reviewer for everyone else does not make them suitable to assess their own access.

For a manual certification handover, do not assume ISC will use that automatic split to accept a mixed review. The documented manual action blocks moving a certification that contains the proposed recipient's own access. Check the actual selected work and supported action before attempting the transfer.

Group assignment also has a specific boundary: for certifications assigned to a governance group containing multiple identities, the members' individual work reassignment configurations are not applied. A group member's absence setting therefore does not prove the group's certification has moved to that member's backup. Inspect the group assignment, available members and actual reviewer who will act.

## Check responsibility using the right evidence

The settings screen answers, “What redirection instruction is saved?” The current certification assignment answers, “Who holds this review now?” To establish absence cover, you need the second answer as well as the first.

Reassignment History can help trace work that was redirected. Its Assignee column shows the first identity specified in the configuration; further redirections are not listed there. If a chain exists, use the current review assignment to establish the final holder. The history screen displays the past 90 days, so older history may require an administrator's help.

Audit records can show who created or deleted a work reassignment configuration and when an automatic reassignment occurred. Those facts establish configuration or assignment actions. They do not establish that anyone assessed the access.

For decision evidence, distinguish the current **Reviewer** from the **Decision Maker**, the person recorded as making a particular decision. A review can move after somebody has already saved a decision. Changing current responsibility does not make the replacement the author of that earlier decision. Regenerate a campaign report after changes when using it to inspect the updated state.

Finally, confirm that the recipient can open the correct work, understands its access and knows the deadline and unresolved questions. An email alone does not establish all of that. The handover is useful when the right person can continue the required review and the record of earlier actions remains explainable.

## Work through a change of backup

Consider a separate Warehouse review. **View Stock** permits reading stock information. **Adjust Stock** permits changing stock quantities. Current collected accounts are linked to the correct people, and these are independently reviewable entitlements.

Original reviewer 3601 is away. Both backups, 3602 and 3603, understand the access, have the necessary permissions, are available and are not reviewing their own access. No other redirects or group assignment affect this case. All the reviews below remain active and unsigned.

Here is the supplied sequence:

1. W-old was created for 3601 before any absence configuration. It contains identity 3610's account `wh-3610` with View Stock. Nobody manually transferred it.
2. A certification work reassignment to 3602 becomes active. W-one is created during that period for identity 3611's account `wh-3611` with Adjust Stock. Its resulting assignment shows 3602.
3. A manager replaces that certification configuration for 3601 with an active configuration to 3603. W-two is then created for identity 3612's account `wh-3612` with View Stock. Its resulting assignment shows 3603.
4. Reviewer 3601 returns, and the current configuration is deleted. Nobody performs a separate transfer of existing reviews.

Someone says, “The original reviewer has returned, so all three reviews must be back with 3601.” What would you explain, and what would you check before closing the absence handover?

W-old remains with 3601 because it existed before the automatic configuration and was never separately moved. During the absence, that was a gap in cover. W-one remains with 3602: replacing the configuration did not transfer earlier work to 3603. W-two remains with 3603: deleting the current configuration did not send earlier work back to 3601.

Check the current assignment and state of each review, the saved configuration changes and their timing, and the relevant history. Confirm that someone suitable can now complete each outstanding review. If the organization wants the returning reviewer to take back W-one and W-two, arrange and verify the appropriate supported existing-work handover. If the backups will finish them, confirm that responsibility and their remaining capacity instead.

Now change one condition. Suppose the site disabled Work Reassignment while the second configuration was still saved. Would that send W-one and W-two back, or delete the configuration?

Neither follows. Disabling the feature stops further automatic redirects through it, keeps the configuration and leaves earlier work with its assigned recipients. Existing-work handovers still need their own supported action. Before reporting the absence cover as complete, account for the work already waiting, the instruction affecting new work and the people who will actually finish each review.
