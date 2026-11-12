# Who made the decision, and what was finally signed off?

A review has moved to another person. The current report names that person as the reviewer, but one access decision still names the earlier reviewer.

That can be a correct record of two different actions. One person made the item decision. Another person now has responsibility for the review.

To explain what happened, follow the access item through its choices, any change of responsibility and the final confirmation.

## First, identify the review and the access

In SailPoint Identity Security Cloud, or **ISC**, a **campaign** organizes access reviews. A **certification** is an assigned review within that campaign. A **review item** is an access entry on which someone records a decision.

An **identity** is ISC's record for a person or another managed subject. An **account** is the record through which that person or service uses an application. The **reviewer** examines whether the access is still appropriate.

Suppose an identity has account **doc-9301** on **Document Store Production**. The account has two permissions:

- **Read Documents** allows viewing documents.
- **Export Documents** allows downloading documents in bulk.

These are separate review items in this example. The identity, account and permissions have been checked, and both items are eligible for individual decisions.

Keep those details with the investigation. Two people can have similar names, and two applications can have a permission called Read Documents. A matching permission name alone does not identify the same access.

Start with the campaign and assigned review, then match the identity, application, account and particular item. Otherwise, an apparent change of decision could simply be a different record.

## A saved choice belongs to an item

The first reviewer is identified here as **R-17**. This is an illustrative reference for a person, not a special ISC role.

At 09:00, R-17 checks the work requirement and saves **Approve** for both items. Approve records that the access should be retained. The reason is that the person's current work requires viewing and exporting documents.

At 09:05, an administrator generates and retains a report showing those choices.

All example times use the same local time zone, America/Chicago, on one day. Actual report times may need conversion before comparison.

At this point, the report supports a limited statement: the two items had saved Approve choices attributed to R-17. It does not establish that the assigned review was finally confirmed.

**Sign-off** is the final confirmation of the review's decisions. In ISC's newer, next-generation certification experience, saving all choices and signing off are separate actions.

That separation matters when the facts change before confirmation.

## Responsibility changes before sign-off

At 10:00, responsibility moves from R-17 to **R-22**, another suitable, authorized reviewer who is independent of the access being reviewed.

**Reassignment** means transferring review responsibility. In this example, the transfer was permitted, completed successfully and checked in the current assignment. The review was unsigned.

R-22 is now the person who needs to handle the remaining review work. That does not mean R-22 made every choice already present.

Think about what actually changed: the person responsible for the work changed. A choice saved earlier still describes an earlier action unless a supported operation changes that item record.

The supplied result in this example is that the saved choices remain, with R-17 recorded as their decision maker. Do not assume every transfer in every review type and state preserves choices in exactly this way. Check the actual resulting records.

## New facts lead to a different decision

At 10:30, R-22 learns that the person's current work has changed. Viewing documents is still necessary, but bulk export is no longer needed.

R-22 examines the two items separately.

Read Documents remains justified, so its Approve choice is retained. Export Documents is changed to **Revoke**, meaning the permission should be removed.

R-22 saves a reason explaining that bulk export is no longer required for the current work.

The later item records show R-17 as the maker of the retained Read decision and R-22 as the maker of the changed Export decision. These are supplied observations for this example.

| Item | Record retained at 09:05 | Later saved choice | Later recorded decision maker |
|---|---|---|---|
| Read Documents | Approve by R-17 | Approve | R-17 |
| Export Documents | Approve by R-17 | Revoke | R-22 |

There is no need to make both rows name the same person merely because one person now owns the review work.

The difference explains something useful: the reading choice remained in place, while the export choice was changed after new facts became available.

The earlier Approve for export belongs to the earlier record. It should not be described as the final choice after the successful change to Revoke.

## Final confirmation applies to the resulting set

At 11:00, R-22 checks that the review's items have the correct choices and successfully signs off.

The confirmed set is now:

- Retain Read Documents.
- Remove Export Documents.

R-22 gives the final confirmation in this ordinary reviewer flow. R-17 is still the recorded maker of the retained reading choice.

A **signer** is the person giving that final confirmation. Here, R-22 confirms the resulting set after checking both items.

The signer and the maker of each individual choice can differ. Signing the resulting review does not mean the signer originally entered every choice.

Also, the confirmed Revoke is a decision about what should happen. To say that bulk export has actually stopped working, inspect the required removal work and current account evidence. A signature alone cannot establish the application result.

Here is the relationship between these records:

```text
Match the same campaign, assigned review and access item
                           |
            +--------------+---------------+
            |                              |
     Item's saved choice            Current assignment
     decision maker                 who handles the work now
     reason and decision time
            |
     Final confirmed choices <---- successful sign-off
            |                      confirmation actor and time
            |
     Any required access removal
            |
     Separate task and current account evidence

Earlier saved records can help explain a changed choice.
One current row does not contain every earlier change.
```

The branches separate questions that need different evidence. Follow a required removal beyond the confirmed choice to find out whether the account actually changed.

## Read the report column in its own report

ISC reports make several of these distinctions visible. Be careful with familiar column names: their meaning depends on the report.

In the **Campaign Status Report**, **Reviewer** identifies the person currently assigned to the certification. **Decision Maker** identifies the person who made the item decision.

For the later records in our example, Reviewer is R-22 on both items. Decision Maker is R-17 for reading and R-22 for export.

That answers two separate questions:

“Who should handle this review now?” points to the current assignment.

“Who recorded this particular choice?” points to the item's decision maker.

In the **Sign Off Report**, the column also called **Reviewer** concerns who signed off. Its documented cases can involve an administrator, including administrative completion after the due date.

For our ordinary reviewer example, the confirmation is attributed to R-22. An administrative completion needs its own explanation; an administrator's name in that report does not, by itself, prove that the original reviewer personally confirmed the choices.

The **Owner** column also needs context. In the Campaign Status Report, it identifies the administrator responsible for the source. A **source** is ISC's configured representation of the connected system or its account data.

In the Sign Off Report, Owner identifies the person assigned the certification. Neither use of Owner automatically identifies the maker of every item decision.

Read the report's field meaning before making an actor claim.

## A reason helps explain a choice, but cannot replace its actor

The Campaign Status Report distinguishes **Decision Comments** from **Comments**.

Decision Comments belong to the decision. Comments can describe issues with the item or its processing. A message about a processing problem is not automatically the reviewer's business reason.

For export, a useful reason explains what changed: bulk export is no longer required, while document viewing is still needed.

Now suppose a comment says, “Manager approved.”

That sentence alone does not establish who used ISC to save the choice. It might refer to information obtained from someone else. It also does not tell you which permissions the manager considered or whether the review was signed off.

Match the reason to the exact item, saved choice and recorded decision maker. Where separate business authorization matters, retain the actual supporting approval under the organization's process.

If a choice changes, inspect the reason attached to the resulting record. An old reason for keeping access may no longer explain a later Revoke.

## A current row is not the whole history

**Decision history** means the evidence explaining recorded choices and their changes: what the choice was, who made it, why it was made and when it was recorded.

A current row can show the latest saved choice without listing every earlier change.

For Export Documents, the later Revoke row alone does not show the earlier Approve. The retained 09:05 report helps establish that earlier observation.

Even the two reports do not prove that no intermediate edit occurred. They show the states observed at those times. Claim a complete sequence only when the available evidence actually supports one.

Reassignment evidence answers another question. It can show previous and new reviewers, but a trail of assignment changes is not automatically a history of each item's decisions.

Do not supply missing decision times from the order of names in a list. If the evidence does not establish an exact time, keep that part of the explanation open.

For our supplied example, the records support R-17's earlier Approve, the checked handover, R-22's changed Export choice and R-22's final confirmation. Those facts can be explained without claiming that one report contains every action.

## Compare the right times

There are several different times in this investigation.

**Decision Date** in the Campaign Status Report concerns the decision. **Sign Off Date** in the Sign Off Report concerns final confirmation. The report's generation time concerns the file that was produced.

The reports document these times in GMT. Convert them to one chosen time zone before comparing them with local records, and keep the original zone with retained evidence.

A report generated later can contain a decision made earlier. Generating it does not make all of its item choices new decisions.

Likewise, downloading the same old report again does not refresh its contents. Generate the report again after changes when you need the updated state.

**First Action Date** concerns the first decision, not final confirmation. A generic **Modified** time on a record is also insufficient to identify which specific action changed it.

In the next-generation Certification model, **Completed** means that all item decisions have been made. **DateSigned** is separate and is omitted until sign-off.

DateSigned can establish that a signing time was recorded for that certification. It does not, on its own, identify the signer or show every choice in the confirmed set. Match it with the corresponding review and confirmation evidence.

## When you inspect underlying records

An **API** is an interface through which authorized software reads or changes service records. It can help an administrator inspect details behind a screen, within the interface's supported scope and permissions.

The next-generation SDK models describe a certification's Reviewer separately from its items' decisions. An **SDK** is a library that helps software use those interfaces.

The ReviewItem model includes Decision, Comments and an Actor identity reference. The inspected model does not provide a complete sequence of edits or an item decision timestamp.

Do not treat the presence of Actor as a complete history. Check what the actual operation returns. Compare it with the matching decision-maker and review evidence before saying who performed a particular action.

An **identity reference** identifies a related identity record. Where available, use the record's ID as well as its readable name. A readable name is a label; two records can have the same label.

A certification's current reviewer can also be a **governance group**, a configured group used to assign responsibilities. A group reference is not a statement that every member personally decided every item.

Distinguish a group ID from a person's identity ID. A shared display name does not make them the same actor.

The next-generation interfaces discussed here are marked Experimental. Confirm the actual supported interface, returned fields and permissions before relying on them in an operational investigation.

## Correct an error at the actual stage

Before sign-off, the ordinary reviewer flow allows choices and comments to be revisited. That is how R-22 corrected the export decision in our example.

After ordinary sign-off, the review becomes **read-only**: its saved decisions can be viewed, but the reviewer cannot continue editing them through the normal review flow. The documented reassignment path also does not allow a signed certification to be reassigned.

If a mistake is discovered later, establish the exact campaign type, state and supported correction procedure. Do not promise that every completed review can be reopened or that its earlier decision can simply be overwritten.

Preserve the evidence of what was recorded and determine any separate access correction that is needed. Changing an explanation after the fact cannot make a permission disappear from an application.

## Try a different completion path

A separate campaign is overdue. It contains one certification assigned to governance group **GG-9** and two access items.

Neither item has ever had a saved choice in this campaign. No reviewer has signed off.

An analyst sees the group assignment and a completed result, then writes:

“The group's manager and all its members approved the access and signed the review.”

What evidence supports that statement?

The assignment only tells us which group had the responsibility. The completed result alone does not identify a member who made an informed decision.

Now the investigation establishes the actual path: authorized administrator **A-7** completed the overdue campaign using the approved policy to maintain undecided access. The resulting items are approved under that policy, and the final Sign Off Report attributes the completion to A-7.

The supported explanation is that administrative policy handling produced the outcome. No evidence here establishes that the manager or every group member personally examined and approved the two items.

Do not invent an item Decision Maker value from this description. Read the actual item records if that attribution is needed.

Even if GG-9 and A-7 happen to have the same display label, the group and person remain different records with different IDs and types.

If the requirement was an informed review by someone who understands the work, determine how that requirement will now be fulfilled through a permitted process. Calling a policy-generated outcome “reviewer judgment” would hide the missing work.

For any required access change, check the account result separately. The review's completion record explains how the review ended; the application's current permissions answer what the account can do.

