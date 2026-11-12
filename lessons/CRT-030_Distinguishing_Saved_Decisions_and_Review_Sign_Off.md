# Is a saved decision the same as a signed-off review?

Every item in a review shows a decision. You save your work and close the page.

Have you finished the review?

You have recorded choices for the items. There is still a separate question: have you confirmed those choices as the final decisions for your assigned review? That confirmation is sign-off.

This difference matters when checking progress, correcting a choice or investigating access that still works after a Revoke decision.

## Start with the records involved

SailPoint Identity Security Cloud, or **ISC**, keeps an **identity** representing a person and associates their application accounts with it. An **account** is the record through which someone accesses a particular application. Its permissions determine what they can do there.

For this example, identity 4401 owns account `rep-4401` in Reporting Production. ISC manages its collected account information through a **source**, its configuration representing that application or account-data collection.

The account has three **entitlements**, access rights represented from the source:

- **View Reports** allows reading reports.
- **Export Reports** allows downloading reports.
- **Change Report Schedules** allows changing when scheduled reports are delivered.

A **certification campaign** organizes access reviews. A **certification** is an assigned review within that campaign. A **review item** is an individual unit on which a decision is recorded.

The assigned certification here is R-30. It contains these three entitlements as separate items for `rep-4401`. The account data is current and correctly associated with identity 4401. The entitlements are individually reviewable, outside larger packages and automatic requirements, with no other assignment supplying them in this example.

R-30 is active. Its authorized reviewer understands the access and is reviewing somebody else's permissions. The reviewer knows that the person's current work needs report reading but no longer needs downloads. They still need confirmation about changing report schedules.

## Saving one item does not finalize the review

The reviewer records **Approve** for View Reports and **Revoke** for Export Reports. Approve accepts continued access to the reviewed item. Revoke records that the reviewed access should be removed.

They leave Change Report Schedules without a decision because the relevant business need has not been established.

The saved review now contains two choices and one **undecided** item. Undecided means no decision is recorded for that item. The reviewer may have opened it, read its details and asked a question; none of those activities supplies a decision by itself.

R-30 is also **unsigned**. That describes the whole assigned review: its decisions have not been signed off. It can contain saved choices even though the reviewer has not finalized the certification.

The two terms answer different questions. Which items still need a decision? Has the assigned review been finalized?

Saving or exiting preserves work through the supported save process. It lets the reviewer return to continue. It does not, by itself, make the assigned review signed off. After returning, inspect the actual retained choices and comments rather than assume an unsaved change survived.

## All items decided can still mean sign-off is pending

The responsible business owner later confirms that identity 4401's current duty includes maintaining report delivery times. The reviewer checks that Change Report Schedules provides the needed capability and records Approve with the appropriate reason.

Now all three items have decisions. R-30 still has not been signed off.

Here are the observations at the two points in this example:

| Point in the review | View Reports | Export Reports | Change Report Schedules | Assigned review |
|---|---|---|---|---|
| First saved work | Approve | Revoke | No decision | Unsigned; one item remains undecided |
| After the business confirmation | Approve | Revoke | Approve | Unsigned; all items have decisions |

The change from two choices to three choices establishes that every item now has a recorded decision. It does not establish finalization. A progress indicator counting item decisions can therefore answer a different question from a sign-off record.

Always identify what a count describes. Three decided items out of three reviewed items is not the same observation as one signed certification out of one assigned certification. These are the supplied counts for R-30, not a rule that every ISC screen uses the same progress calculation.

## Sign-off confirms the assigned review's decisions

**Sign-off**, also called **finalization**, is the separate action confirming the decisions for the assigned certification.

Before taking that action, the reviewer checks the actual items and accounts, the choices and explanations, and any unresolved questions. A choice applied to several items at once or a repeated comment needs the same attention as a choice entered individually. Having no empty decisions does not establish that every decision is correct.

For R-30, the intended choices are View Reports approved, Export Reports revoked and Change Report Schedules approved. The reviewer has confirmed the current business reasons for all three and uses the permitted sign-off action.

In ISC's next-generation certification flow, the newer campaign experience, sign-off makes the certification read-only for review decisions and completes the reviewer's review work. It is more than another way to save the page.

The finalized review can still contain Revoke. Signing off does not mean approving every access item. It confirms the set of decisions, including any required removals.

In this example, a separate inspection of R-30 after the action shows that it is signed off, identifies the person who signed it and records when they did so. Its decisions match the three intended choices. Those observations establish that this assigned review was finalized.

Keep the action request and the resulting record separate. If an error, interrupted session or uncertain response leaves you unsure whether sign-off succeeded, inspect the current certification before taking another action. Do not infer success solely because you selected a button or the work disappeared from one list.

The sequence below follows the three observations for R-30. The account's access outcome remains a separate check.

```text
R-30: three review items on rep-4401

First saved work
  View: Approve | Export: Revoke | Schedules: undecided
  Review is unsigned
                    |
                    v
All item decisions saved
  View: Approve | Export: Revoke | Schedules: Approve
  Review is still unsigned
                    |
                    v
Permitted sign-off, then inspect the result
  Signed review, signer and sign-off time confirmed
  Intended decisions retained

Separate evidence still needed:
  Did the required export removal reach rep-4401?
  Are justified viewing and scheduling rights retained?
```

## Changes before and after sign-off are different situations

While the review remains unsigned and the supported action permits editing, a reviewer can revisit a saved decision. That is useful if new facts change the justification.

Suppose the schedule confirmation is corrected before sign-off. The person can view scheduled deliveries but is not authorized to change their timing. The reviewer should revisit the actual Change Report Schedules item, reassess the choice and record the corrected decision and reason through the permitted process. They then inspect the saved result before finalizing.

That is a change to an unfinished review. It is not evidence that an earlier application change has been reversed. A different choice on the screen and the account's permissions still need to be interpreted separately.

After next-generation sign-off, treat the review decisions as finalized and read-only. Do not assume that an item appearing in a Completed tab means you can freely change a signed review. An item-level completed section and the final state of the assigned certification are different things.

If an error is found after sign-off, identify the exact campaign, certification, account, item and recorded decision. Involve the campaign administrator to establish the supported correction for that state and campaign experience. Preserve the explanation and evidence of what happened. Do not invent an Undo action or assume that reopening a page reopens the review.

Reassignment also has state conditions. The documented administrative certification handover cannot reassign a certification after it has been signed off. Moving responsibility for unsigned work is therefore not a general method for reopening finalized choices.

## Confirming your sign-in may be part of finishing

Some configured reviews require **reauthentication**, which means confirming your identity again through the organization's sign-in service when completing the action.

That confirmation establishes who is performing the action. It does not select the decisions or check their business justification for you.

If the process asks you to confirm your sign-in, complete the required step and inspect the resulting review state. Merely reaching a sign-in prompt does not establish that the certification was signed off.

If you cannot complete sign-off, use the actual error and current assignment, permission and campaign state to investigate. An authorized administrative or reassignment path may be needed where supported. Do not report the review as finalized because all its items have choices.

## A signed review is different from a completed campaign

R-30 is one assigned certification inside a campaign. Another reviewer may still have unfinished work in that same campaign.

Signing R-30 does not sign that other person's certification. Likewise, a campaign being completed through an administrative process does not establish that every assigned reviewer personally signed their work.

Identify the object whose state you are reporting: an item, an assigned certification or the campaign. A label such as Complete needs that context before it can explain anything useful.

The **Certification Sign Off Report**, where available for the campaign, can help establish review-level evidence. It distinguishes the first action date from the sign-off date and identifies the signer separately from the assigned owner. A first decision time is not a finalization time, and an administrator may appear as the signer in supported administrative cases.

The Campaign Status Report provides item decisions and their recorded decision makers. That answers another question: who recorded a particular choice? Do not assume the person currently holding the review made every earlier choice or performed every finalization action.

Use current records. Regenerate a campaign report after changes if you need its updated state. An earlier download can miss a later sign-off.

## Sign-off starts the next responsibility; it does not prove removal

**Remediation** is the work required to carry out a removal decision. In the next-generation flow, sign-off confirms the review's decisions and starts any required removal work. Starting that work does not prove that the application account has changed.

For the ordinary R-30 example, the required account outcome is that `rep-4401` loses Export Reports and retains View Reports and Change Report Schedules. The signed review establishes the confirmed decisions; it does not establish all of those application results.

Follow the applicable removal work and inspect the actual account evidence. A manual task being assigned or an automated operation being requested is not the same observation as the export permission being absent.

Use the actual campaign's removal process to establish when the change should run and where to track it. Do not assume that every campaign engine changes accounts at the moment of sign-off.

## What if an administrator completes while work is unsigned?

Administrator campaign completion is a separate action with its own state, permission and handling of unfinished work. It should not be treated as the reviewer simply selecting Sign Off later.

There is conflicting product guidance about how saved unsigned decisions are handled at administrator completion. One description treats unsigned certifications as undecided; another describes a manager's saved decisions being preserved. That guidance does not establish one answer for every campaign experience and type.

Before relying on either outcome, establish the actual campaign engine and type, its unfinished-access settings and the administrative action being used. Work with the campaign administrator and obtain product clarification where that behavior has not been established. After an authorized completion, inspect the resulting item decisions, actors and review state, then the required access outcome.

For ordinary reviewer work, complete and verify the supported sign-off rather than leave saved choices for an assumed later administrative result. If the reviewer cannot do that, raise the unfinished review while there is time to arrange appropriate handling. A campaign-level completion label alone cannot explain what happened to each saved choice.

## Test the difference on two Warehouse reviews

A running campaign contains these assigned certifications:

- **R-W** reviews identity 4501's account `wh-4501`. Read Stock permits reading stock quantities; Adjust Stock permits changing those quantities. Both items have saved decisions: Read Stock Approve and Adjust Stock Revoke. No sign-off has been recorded.
- **R-S** reviews identity 4502's account `wh-4502`. Read Stock has a saved Approve decision. A current inspection confirms that R-S is signed off and shows its signer and sign-off time.

The source data and account associations are current and correct. These are individually reviewable entitlements with no package, automatic or other assignment supplying the same rights. The reviewers are authorized and are not reviewing their own access. The choices have justified current business reasons. No removal result from the application has been supplied.

Someone reports, “Every item has a decision, so both reviews are finished. R-S is signed, so the campaign is complete and stock adjustment has been removed.”

What does the supplied evidence actually establish?

R-W has all its item decisions saved, but it is unsigned. It has no undecided items in the supplied records; its missing step is finalization. R-S has a saved decision and verified sign-off evidence, so its assigned review is finalized.

R-S's sign-off does not finish R-W or establish campaign completion. It also says nothing about whether Adjust Stock was removed from the different account `wh-4501`. That removal needs the relevant finalized requirement, processing and actual account evidence.

Now change one condition: an administrator completes the campaign while R-W remains unsigned. Can you conclude that its saved Adjust Stock Revoke will be carried out?

The supplied facts do not establish that outcome. Identify the completion path and verified handling of unsigned saved choices, then inspect the actual final decisions and removal work. Do not substitute either “all saved decisions survive” or “all saved decisions disappear” for that missing evidence.

To explain these reviews accurately, keep four observations connected: the saved item choices, the assigned review's sign-off, the campaign's state and the account's resulting access. Each answers a different question.
