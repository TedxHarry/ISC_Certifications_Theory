# When should a campaign be corrected, regenerated or retired?

A campaign contains the wrong accounts. Someone suggests deleting it and starting again.

That may produce another campaign, but it does not explain what went wrong. If the same selection is used again, the same accounts may be missing. If reviewers have already acted, deleting the old campaign also affects evidence and work that you need to understand first.

Start with the particular problem. Then choose the smallest supported change that actually solves it.

## Find the record that needs to change

In SailPoint Identity Security Cloud, or **ISC**, a **campaign** organizes access reviews. A **certification** is an assigned review within that campaign. A **review item** is the access entry on which a reviewer makes a decision.

An **account** is the record through which a person or service uses an application. Its **access** is what it is allowed to do. In this example, Read Orders allows viewing orders, while Change Orders allows editing them.

ISC collects account information through a **source**, a configuration for an application or its account data. The campaign uses information held in ISC. Changing the actual application account is a separate operation.

A **template** holds reusable campaign instructions, such as the selection and reviewer settings. Generating a campaign uses those instructions to produce a particular set of review work.

A **preview** lets an administrator inspect generated work before starting it. **Activation** starts the campaign for review.

These differences help you locate the repair. A wrong account value belongs in the data investigation. A selection that excludes required people belongs in the campaign-definition investigation. A suitable reviewer who is temporarily unavailable presents a different problem again.

Editing one record does not establish that all the other records changed.

## Correct a selection before launching it

Suppose the review requirement includes twelve ordinary accounts on Orders Production. The requirement and the list of accounts have been checked. Read Orders and Change Orders are permissions that can be reviewed individually for these accounts.

Call the existing generated preview **P-810**. Its contents include only ten of the twelve accounts. It has not been activated, and no reviewer decisions or access-removal work exist for it.

The collected data is correct. You find the cause: the saved selection includes people in Operations, but two required account owners belong to Distribution. They were left out because they did not match that condition.

Generating the same instructions again would leave the condition unchanged. First correct the selection to match the approved requirement. If the reusable template contains that selection, an authorized administrator needs to correct that template through the supported operation.

Now generate a replacement preview, **P-811**. **Regeneration** here means producing new campaign work from the corrected inputs. It does not mean rewriting the old preview's history.

Check the replacement's actual contents. Confirm that the twelve required accounts are present, that unrelated accounts have not been added, and that the right permissions and reviewers are included. Equal totals are insufficient: twelve records could still contain the wrong twelve accounts.

Also check the actual deadline and notification choices. A replacement needs its own launch readiness; the old preview's earlier checks cannot prove that the new work is correct.

Keep P-810 out of use while the replacement is being validated. Record why it is being replaced and which campaign takes over the requirement. Starting P-811 and removing P-810 are separate supported actions.

## A field edit has a particular scope

An **API** is an interface through which software asks ISC to read or change something. The **certification engine** is the service processing the campaign. The documented next-generation campaign update API illustrates why current state matters.

Its permitted fields differ between STAGED, a prepared campaign state before activation, and ACTIVE, the running review state. An **undecided item** has no recorded reviewer choice. Recommendations are suggestions that can help a reviewer assess access; enabling them does not make the decision.

| Campaign state | Fields allowed through this update operation |
|---|---|
| STAGED | Name, description, deadline, notification emails, inclusion of decision recommendations, and whether revoking undecided access is allowed |
| ACTIVE | Deadline |

The undecided-access setting concerns whether the administrator can choose a revoke outcome for items without decisions.

These are the fields this particular next-generation update operation allows. Other engines and interfaces need their own supported actions checked.

The operation requires an authorized Org Admin or Cert Admin. When a field update succeeds, it returns the changed campaign record. Check that the intended field and value were actually saved.

Notice what is absent from this operation's listed fields: rebuilding the account population. Editing a name or extending the deadline does not solve P-810's missing accounts.

The template has its own update operation. Generating from it returns a reference to a new campaign. A successful template edit therefore does not prove that an already generated campaign now contains different accounts.

For P-810, keep following the actual replacement contents rather than assuming the definition edit repaired the existing preview.

## Some problems need a smaller correction

Suppose an active campaign's contents are correct, but a reviewer is absent. The assigned certification is unsigned, meaning it has not received the reviewer's final confirmation.

Where the applicable rules permit it, an authorized person can reassign that review to a suitable replacement. **Reassignment** changes responsibility for the selected review work.

The replacement needs relevant knowledge and permitted access, and must not be reviewing their own access. Check the resulting assignment and whether the replacement can open the work.

There is no reason to rebuild every correctly generated review merely because one suitable reviewer is unavailable. The documented reassignment guidance also blocks transferring a certification after it has been signed off. That boundary matters when choosing this repair.

Now consider an active next-generation campaign with a correct population and an approved need for more review time. The scoped update operation supports a deadline change. Verify the actual changed date, including its time zone, and communicate the new due date to the relevant people.

A longer deadline gives time to finish work. It does not add missing accounts or correct unjustified decisions.

## Check whether the reviewer has already finalized the choice

For an individually reviewable permission, **Approve** accepts continued access under the reviewed conditions. **Revoke** records that the access should be removed.

In the normal next-generation review flow, saving choices and giving the final confirmation, called **sign-off**, are separate actions.

If an unsigned reviewer notices a mistaken choice, the documented reviewer flow allows revisiting it before sign-off. The reviewer should correct the actual item, verify the saved result and then finalize the correct decisions.

After sign-off, do not assume that the same editing path remains available. The normal next-generation finalization makes decisions read-only. Broader wording about changes after completion is inconsistent, so a specific post-sign-off correction needs authoritative handling for the actual engine and state.

Also check whether the earlier decision already caused work to change the application account. **Remediation** is the work that carries out a removal requirement. Changing a review record, where permitted, is not evidence that an earlier account change has been reversed.

If access must be restored or removed, arrange the justified, authorized account change through the supported process and verify its result. Preserve the original decision and correction history needed to explain what happened.

## Replacing a campaign requires a handover

A replacement has a new set of work and its own result. Before relying on it, establish which requirement it covers and how it relates to the old campaign.

For example, P-811 replaces P-810's incomplete twelve-account review. That relationship needs to be clear to the campaign owner, the person responsible for the campaign, and to the people coordinating the review.

Identify any old decisions, unsigned reviews, signed confirmations and pending removal work. Do not copy old choices into a new campaign and describe them as newly examined reviewer decisions.

If both campaigns remain visible, tell reviewers which work they should perform under the approved plan. A note saying “use the replacement” does not itself stop the old campaign or transfer its tasks.

The saved schedule needs a separate check too. A **schedule** controls when preview generation occurs. In the documented Search route, generating a scheduled preview early does not cancel the preview planned for the original date.

If the future cycle also needs changing, inspect the saved template and schedule through their own supported actions. Removing one generated campaign is not evidence that the next scheduled generation has stopped.

For manager or source-owner previews, the administration guidance calls for starting within a day of generation or planning to delete and recreate the preview. Apply that guidance to its stated route; it is not a universal promise that every piece of campaign data refreshes after a fixed time.

## Retirement and deletion have different consequences

**Campaign retirement** means deciding that a campaign should no longer be relied on for the review requirement. It describes the management decision. It does not identify a universal ISC button or status.

The supported platform action still needs to be established for the actual campaign. You may need a permitted correction, a replacement, or approved deletion after evidence and outstanding work are accounted for.

**Campaign deletion** removes the campaign through the supported delete operation. The administration guidance warns that its decisions are lost and it disappears from participants' certification views. Its reports are deleted too.

That makes deletion different from keeping an old campaign as historical evidence while identifying a replacement.

Before an approved deletion, preserve the required campaign data, decisions, actual actors, sign-off information and outstanding-work details in the organization's approved location. Include the campaign identifier and relevant times so the saved evidence can be matched to the correct review.

Generate and save the needed reports before deleting the campaign. Check that the saved files are readable and contain the required information. A link back to a campaign that will be removed is not the same as retaining its evidence.

A saved export also does not establish that you can restore the original campaign and resume it later. Evidence retention and platform restoration are separate capabilities.

The documented deletion path does not automatically notify participants. Arrange the appropriate communication under the approved change plan.

For the next-generation Delete API, an authorized administrator supplies the exact campaign identifiers, and the operation returns an accepted response. Check the actual deletion result afterward. Acceptance is not the same as confirmed completion.

## Do not treat cancellation as a reversal of application work

Before using any stop or cancel action, establish which operation it affects. Stopping a preview, stopping future generation and stopping a removal request would be different changes.

The checked deletion guidance does not establish a universal rule for every queued or already submitted removal. Do not infer that deleting the campaign cancels all of that work or restores access that has already changed.

Inspect the existing tasks or requests and the current application account. Where the side effect is not established, get authoritative handling for that particular path before relying on cancellation. A status word alone does not define a supported action.

The following map helps choose the investigation. Its branches are your reasoning, rather than an automatic repair process inside ISC.

```text
Identify the exact defect, campaign and current state
                         |
          What record needs to change?
                         |
       +-----------------+------------------+
       |                 |                  |
 Supported field    Assignment or      Wrong generated
 correction         unsigned choice    population/data
       |                 |                  |
 Check state,       Check actor,       Correct inputs;
 authority and      scope and          validate a new
 allowed field      finalization       generated review
       |                 |                  |
       +-----------------+------------------+
                         |
       Verify actual result and remaining work
                         |
       Before any approved deletion: preserve
       evidence and establish task/account effects
```

If the defect cannot be repaired through the available action, changing an unrelated field will not make it disappear. Keep the missing work visible and choose a supported replacement or escalation.

## Try a case where review work has already started

An active campaign includes a Payments account with **Read Payments**, which allows viewing payment records, and **Release Payments**, which allows authorizing payment release.

Reading remains justified; release does not. A suitable independent reviewer correctly revoked release and signed off. A matching removal request was accepted and sent, but its actual outcome is not yet known.

Elsewhere in the same campaign, required accounts are missing. Someone proposes deleting the campaign and generating a corrected one. They say the old removal will be cancelled and every account will return to its earlier access.

Which facts need attention before relying on that plan?

First preserve the old campaign's decisions and evidence. Identify the exact Payments account, signed decision, existing removal request and current account state. The missing population is a real campaign defect, but it does not invalidate this supplied correct release-removal requirement.

The assertion about cancellation and restoration is unsupported. An accepted or sent request may already have changed the application. Establish what the actual operation has done and the supported handling of any outstanding work.

Validate a replacement against the complete intended account set and appropriate reviewers. Account for the valid old removal requirement rather than assuming a new campaign will automatically take it over. Keep justified reading intact.

Now change the evidence. A reliable current account check shows that release is absent and reading remains. The removal succeeded.

Deleting a campaign record would not establish that release had been restored. Restoring that permission would require a separately justified, authorized change and its own verified result. In the supplied facts, release remains unjustified.

The useful repair therefore addresses the missing review population while preserving the correct removal outcome, its evidence and clear responsibility for any remaining work.
