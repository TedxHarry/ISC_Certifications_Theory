# What happens to overdue, undecided or unsigned reviews?

The campaign deadline was yesterday at 5:00 pm. It is now 9:00 am, and some review work is unfinished.

Has ISC removed the access? Has it approved everything that nobody reviewed? Can the reviewers still finish?

The date alone cannot answer these questions. You need to look at the work that remains and the way this campaign handles it.

Let's look at the date, the saved choices and the final review confirmation separately.

## Three questions that sound similar

In SailPoint Identity Security Cloud, or **ISC**, an access review asks whether existing access is still appropriate. An **account** is the record through which a person or service uses an application. **Access** means what that account is allowed to do.

For example, an account may have permission to read delivery details and a separate permission to export customer addresses. Reading details and downloading an address list are different abilities. Each needs an appropriate business reason.

A **campaign** organizes a set of reviews. A **certification** is an assigned review within it, and a **review item** is an access entry on which the reviewer acts.

The **reviewer** examines the access and records a choice. For a permission that can be reviewed individually, **Approve** accepts continued access under the reviewed conditions. **Revoke** records that it should be removed.

Now ask three separate questions:

- **Has the deadline passed?** If the relevant work is unfinished after its due date, it is overdue.
- **Does this item have a decision?** An item without one is undecided.
- **Has the reviewer given the final confirmation?** A review without that confirmation is unsigned.

In ISC's newer, next-generation certification experience, the final confirmation is called **sign-off** or **finalization**. Saving choices and signing off are separate actions.

This means an unsigned review can contain no decisions, a few decisions or a decision on every item. The word unsigned tells you about the final confirmation. It does not tell you how many item choices exist.

Overdue tells you something different again: the work has missed its due date. It does not describe whether the choices were saved or which permissions the account currently holds.

## Look at the same campaign in more detail

Suppose the campaign is past its deadline, but its actual state still permits reviewers to continue. The assignments and access data have been checked. The reviewers are suitable, authorized and independent of the access being reviewed.

All the times below use the same time zone. The deadline was yesterday at 5:00 pm; you inspect the records today at 9:00 am.

| Assigned review | Item choices at 9:00 am | Final confirmation | Work that remains |
|---|---|---|---|
| R-1, three items | Choices saved for all three | Not signed off | Reviewer needs to confirm the correct choices |
| R-2, two items | Neither has a choice | Not signed off | Reviewer needs to decide both items and finish the review |
| R-3, one item | Revoke recorded | Signed off yesterday at 4:00 pm | Due removal work is pending; the permission is still on the correct application account |

These are supplied example records, rather than a promised ISC screen layout.

R-1 has no undecided items in its saved choices, but the review is unsigned. “The reviewer clicked all the decisions” is therefore not enough to establish that R-1 was finalized.

R-2 has two undecided items and is unsigned. Its problem starts earlier: the reviewer has not yet recorded either choice.

R-3 was signed off before the deadline. Its reviewer has already finished that review. The remaining problem is the required account change.

**Remediation** means carrying out the removal decided in a review. An integration may make that change automatically, or a person may receive work to make it in the application. In either case, a recorded Revoke and actual removal are separate results.

For R-3, follow the existing removal work and the affected account. Its reviewer has already signed off. Calling every unfinished campaign “waiting for the reviewer” would send you to the wrong person.

## Check what changed when the deadline passed

When checking overdue work, use the date recorded on the actual campaign and the time zone needed to interpret it. An old email or an older report may describe an earlier observation.

Then check the campaign's current state. The documented postdeadline choices include allowing reviewers to finish. A campaign can therefore be past its deadline while review work remains available. Do not assume that every reviewer is locked out merely because the clock passed the due time.

That also does not mean every overdue campaign remains editable. The campaign may already have been completed, or a particular action may not be allowed in its current state. Check the actual record and the action permitted for that campaign.

The deadline is also different from a scheduled removal date. Where a particular reviewed access type supports a later revocation date, the required removal has its own timing. For R-3, we have explicitly supplied that removal is due. We are not deriving that fact from the review deadline.

The application account needs its own evidence. A campaign becoming overdue does not establish that the account lost a permission, was disabled or was deleted.

## Letting reviewers finish is an active follow-up

For R-1, the useful action is to have the reviewer check the saved choices and complete the permitted sign-off. If a decision is wrong and still changeable, it needs correction before final confirmation.

For R-2, first find why the decisions are missing. If the reviewer does not understand what a permission allows, get that meaning from someone responsible for the application. If the current business need is unclear, get the relevant work requirement. If the reviewer is absent, arrange a suitable replacement through a supported, authorized handover.

A transfer changes responsibility for selected work. It does not supply the missing business facts or automatically complete the review. Check who is actually assigned afterward and whether they can open the work.

The campaign owner, who is responsible for the campaign according to its configuration, or another authorized coordinator should agree who will resolve each gap and when it will be checked again.

Waiting without a responsible person or next check leaves the same problem in place. Allowing more time to finish a justified decision is a deliberate handling choice. It is not a new deadline unless an authorized, supported change actually updates the campaign.

In the normal next-generation review flow, the reviewer checks all items and submits the final confirmation. Confirm the resulting sign-off in ISC. An email saying “done” is communication from the reviewer; it does not replace the review record.

## What if an administrator completes the campaign?

**Administrator completion** is an action that closes the campaign under the applicable rules. It is different from each reviewer personally finishing their own assigned review.

The configured handling of undecided items matters. The documented administrative choices include:

- **Maintain access to undecided items.** On completion, unresolved items covered by that handling keep their access.
- **Choose to maintain or revoke access to undecided items.** This allows the completing administrator to choose the supported bulk outcome for the affected unfinished items.

For the documented interface, these choices can appear as **Complete**, **Complete & Maintain Access**, or **Complete & Revoke Access**, depending on configuration.

Read the actual action and its confirmation before proceeding. A button called Complete does not tell you, by itself, which permissions will remain.

The person operating it also needs permission. For example, the documented next-generation administrative Complete API requires an Org Admin or Cert Admin role and a past-due campaign. An **API** is an interface through which software requests an operation. This API's conditions do not establish that every reviewer or every campaign owner can perform the same administrative action.

A completion request being accepted is also not proof that every later change has finished. Check the resulting campaign and item records, then any required removal.

Before applying a bulk outcome, establish which items it will affect. This is especially important when unsigned reviews already contain saved choices.

## Saved choices in an unsigned review need particular care

Return to R-1. The reviewer has selected choices for all three items but has not signed off.

Would an administrator's completion preserve those choices? Or would it handle that unsigned review as though its items were undecided?

The current product guidance gives conflicting descriptions. One description treats unsigned reviews as if no decisions were made at completion; another describes saved manager decisions being preserved. These descriptions do not establish one dependable rule for every campaign.

So do not promise that a saved Approve will survive, or that a saved Revoke will be carried out, merely because those choices are visible before administrative completion.

Establish the exact certification engine and supported completion behavior for the campaign. The **engine** is the certification service processing it; ISC has newer next-generation and older legacy campaigns. Use authoritative clarification for the affected path when the guidance does not settle it.

Keep the actual saved choices, reviewer, sign-off state and relevant times available for that investigation. A total such as “three items decided” cannot answer what administrative completion will do to those three choices.

If the review still permits normal finalization, having the suitable authorized reviewer confirm correct decisions provides the ordinary review-completion path. If that is not available, arrange the verified administrative handling rather than guessing the affected set.

## Follow a completion choice where no saved decision is involved

Take a separate, simple campaign. It is overdue and contains one assigned review with two individually reviewable permissions:

- Read Delivery Details allows the account to view delivery information.
- Export Addresses allows the account to download customer addresses.

Neither item has ever received a saved choice in this campaign. There are no other reviews or saved decisions in it. The actual configuration maintains access to undecided items on administrator completion.

An authorized administrator has approval to apply that handling. They check both items, confirm the maintain-access action and verify that completion succeeded with both items maintained under that handling.

In this documented maintain-access path, the previously undecided items are approved as part of completion. The account keeps those permissions. The administrator has resolved the unfinished items using the campaign's rule.

An approved result produced this way does not establish a fresh, informed reviewer's judgment that both permissions are still needed. A completion policy is a way to handle missing decisions. It cannot supply the facts the reviewer never examined.

Maintaining access also does not mean ISC has granted a new permission. These permissions already existed. You still need suitable follow-up if their current need remains unknown.

Now change the conditions. Suppose the actual campaign instead offers the choice to revoke undecided access, and the authorized administrator has an approved reason to use it for these two items.

The administrator must understand that both never-decided items fall into the selected outcome. That includes reading, not only the more sensitive export permission.

After the action, inspect the recorded result and the matching removal work. Verify what happened on the correct account. Selecting the revoke outcome is not itself evidence that either permission has disappeared.

A missed deadline is not a business reason to remove all access. Equally, maintaining it does not prove all of it is justified. The organization needs an authorized decision about the consequences and the follow-up.

## Keep the date, the decision and the account result connected

This map shows the investigation for overdue work. Its arrows are your reasoning steps, not an automatic sequence that ISC always executes.

```text
Deadline passed; unfinished campaign work observed
                       |
      Inspect current state, choices and sign-off
                       |
       What is allowed and authorized now?
                       |
        +--------------+----------------+
        |                               |
 Review work can finish       Administrative completion
        |                               |
 Resolve missing facts        Check configured handling
 Confirm correct choices      and exact affected items
 Obtain permitted sign-off    Verify unsigned-choice handling
        |                               |
        +--------------+----------------+
                       |
        Verify actual review/campaign result
                       |
         If removal is required and due:
                       |
          Follow matching work and verify
          the correct application account
```

A campaign can have some signed reviews while others remain unfinished. The already signed review and its required removal keep their own evidence. Do not classify them as undecided merely because other reviews missed the deadline.

For every conclusion, keep the actual actor and time clear. The person assigned to a review, the person who saved an item choice and the administrator who completed a campaign can be different people.

Use current decision, sign-off and campaign records together. For a removal conclusion, include the relevant operation or task and current account evidence. A newly generated report can summarize older facts; its download time is not the time the application permission changed.

## Try an unfamiliar case

A Dispatch application account holds Read Delivery Details and Export Addresses. Reading is still needed for the person's work. Exporting the address list is no longer justified.

A suitable independent reviewer saved Approve for reading and Revoke for exporting. The review is unsigned. The campaign is past its deadline, and both permissions are still on the correct account.

An operator proposes **Complete & Revoke Access**, saying, “The saved reading approval will definitely be kept. Only exporting will go.”

The exact handling of saved unsigned choices for this campaign has not been established. What can you conclude, and what should happen next?

You can conclude that the review is unsigned, the choices are saved and the account still holds both permissions. You cannot guarantee the proposed action's item-by-item result from those facts.

The operator's assurance depends on the very rule that is missing. Preserve the saved choices and identify the actual campaign engine, configuration, available action and authoritative handling. The need to retain reading makes the affected scope particularly important.

If the review remains available for normal finalization, arrange for the authorized reviewer to confirm the correct choices and finish it. If administrative completion is required, establish its actual consequences and approval before applying it. Neither a blanket maintain choice nor a blanket revoke choice establishes that the review was properly completed with the intended outcomes.

Now you receive additional evidence: the original reviewer successfully finalized the correct decisions through the permitted review flow. The actual removal work is due and has finished. Reliable current evidence shows that this same account retains reading and can no longer export the address list.

That supports a narrower, useful conclusion: the review was finalized and the required access outcome was verified for these two permissions on this account. It does not tell you that every review in the campaign is complete or that every other account has lost export access.

If you had received only a freshly downloaded report, with no evidence of those underlying results, you would still need to establish them.
