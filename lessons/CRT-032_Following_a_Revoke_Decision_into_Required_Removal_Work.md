# Revoke was selected. What should happen next?

A review shows Revoke, but the person can still use the permission in the application.

Where should you look first?

First, check whether the reviewer finished and signed off the review. Then check when the removal should happen and how it should reach the application. Access still being present tells you that you need to investigate. It does not tell you which step is missing.

## Establish exactly what should change

SailPoint Identity Security Cloud, or **ISC**, keeps an **identity** representing a person and associates their accounts with it. An **account** is a record in a particular system. Its permissions determine what someone using it can do.

Identity 4801 owns account `pur-4801` in Procurement Production. ISC manages its collected account information through a **source**, its configuration representing that application or account-data collection. The actual procurement application is the **target system**, where the permission must eventually change.

The account holds two **entitlements**, access rights represented from the source:

- **View Orders** permits reading purchase orders.
- **Approve Orders**, with identifying value `ORD_APPROVE`, permits authorizing purchase orders for processing.

Approve Orders is the name of an application permission. Approve or Revoke in the certification is the reviewer's decision about keeping that permission.

A **certification campaign** organizes access reviews. A **certification** is an assigned review within it. A **review item** is a unit on which a decision is recorded.

In this example, View Orders and Approve Orders appear as separate review items. The account information is current, and ISC has associated the account with the correct person. The permissions are reviewed individually; neither comes from a bundle or an automatic assignment. No other assignment requires the account to keep them. The reviewer has permission to perform this review, understands the access and is reviewing somebody else's account.

The responsible business owner confirms that identity 4801's current duty requires reading orders but no longer authorizes approving them. The intended result is therefore specific: `pur-4801` should retain View Orders and lose Approve Orders. The account itself should remain available for reading.

This is the **removal requirement**: which reviewed access must be removed, from which account and source, under the applicable conditions and timing. Keeping those details together prevents a broad statement such as “remove procurement access” from becoming a change to the wrong account or permission.

## Confirm the decision that is meant to take effect

The reviewer records Approve for View Orders and Revoke for Approve Orders. **Approve** accepts continued access to the reviewed item. **Revoke** records that the reviewed access should be removed.

Initially, the certification is unsigned. That means the assigned review has not been finalized, even though these choices have been saved.

**Sign-off**, also called finalization, confirms the assigned review's decisions. Here, the reviewer signs off. We then check the certification itself: it shows that the review was finalized, with View Orders approved and Approve Orders revoked. Its records identify who signed off and when. This check matters because clicking a button and confirming its saved result are separate things.

Now we have a confirmed removal decision for `ORD_APPROVE` on `pur-4801`. We still need evidence of the work that carries it out.

**Remediation** is that required change work. The documented next-generation finalization operation confirms the decisions and initiates needed remediation. Initiating work does not prove that the target account has already changed.

ISC has different campaign implementations, so check which one you are using and how it starts removal work. The documentation does not give one timing sequence that we can safely apply to all of them. Sign-off alone is not a reason to say that removal has finished, or that it must wait until every other reviewer finishes.

Administrator completion of an unsigned review also needs its own verified handling. It is a different path from the normal reviewer sign-off established for this example. A saved Revoke and a campaign completion label alone cannot establish what happened to that item.

## Check whether the removal is due

Some supported review actions allow a **revocation date**, a specified date for taking access away. A person may remain authorized during an approved handover period, with removal intended afterward.

Where that option is supported, inspect the actual saved date and time and establish which time zone is used. Do not assume the date was retained merely because somebody intended to choose it. This reviewer date-setting option is not available for individually reviewed entitlements.

Our Procurement example concerns an individual entitlement. No future removal date applies here, so we cannot use a scheduled date to explain the waiting. We need to find the removal work and check its result.

The question is different when a review item supports removal on a future date. Access still being present before that saved removal time does not, by itself, mean removal failed. Once that time has passed, inspect the work and its result. Reaching a date does not prove that a change succeeded.

Keep the review deadline separate from a revocation date. The deadline concerns when review work is due. A revocation date, where supported, concerns when the reviewed access is to be removed. Neither date is evidence that the account has changed.

## Find the path that can make the change

**Provisioning** is work that changes accounts or access in an external system. In this situation, it is used to remove an existing permission rather than grant a new one.

A **connector** is the supported integration used to read or change data for a source. Reading account information and changing it are separate capabilities. Being able to collect the account's permissions does not establish that ISC can remove them.

For automatic removal, check three things: can this source perform this particular change, is its ability to make changes enabled as required, and does the integration have permission to change this account? Support for one operation, such as creating an account, does not prove support for every access change.

For `pur-4801`, assume those checks have passed. The configured connection can send a change to remove `ORD_APPROVE` in Procurement Production. Next, inspect that operation: which account and permission did it name, was it processed, and what result did the application return?

In a manual path, an assigned person must make the required change in the application. A **manual fulfillment task** records that human work. Inspect the actual task, required account/access and recipient rather than assume that the person who reviewed the item must also remove it.

The source owner recorded in ISC can be relevant to manual work. Some routing also depends on the particular provisioning path and ownership configuration. Establish the actual assignment for the task in question; a generic ownership label is not sufficient proof of who received it.

A failed automatic operation is not, by itself, proof that a manual task has been created as a replacement. Find the work that actually exists. Do not close the investigation by assuming another route took over.

The diagram connects the removal requirement to the work and evidence needed. The two delivery branches describe supported alternatives; they are not a promise that every failed operation automatically switches branches.

```text
Finalized removal requirement
  Procurement Production / pur-4801 / ORD_APPROVE
  Remove Approve Orders; retain View Orders
                         |
                         v
Check applicable trigger and timing
  No deferred date in this entitlement example
                         |
                         v
Identify the supported configured delivery path

Automatic path                 Manual path
  Authorized account change      Assigned person/task
  Inspect operation/result      Inspect action/task result
              |                       |
              +-----------+-----------+
                          v
Verify the actual target account
  Approve Orders absent; View Orders retained
                          |
                          v
Check later ISC collection and report freshness
  A new observation is different from the removal action
```

## Inspect what each record actually establishes

A review decision tells you what was chosen. A sign-off record tells you the assigned review was finalized. A provisioning event or manual task tells you about the work used to deliver the change.

Read its target and result. An operation concerning another account, or removing another entitlement with a similar display name, is not the required outcome for `pur-4801` and `ORD_APPROVE`.

The following observations lead to different next checks:

| Observation | What it establishes | Useful next check |
|---|---|---|
| Revoke is saved, but the assigned review is unsigned. | The choice was saved, but the reviewer has not signed off. | Check the review state and the permitted way to finalize it. |
| A supported future removal time is verified and has not arrived. | The approved timing has not yet made this removal due. | Confirm the retained authorization and plan the check at the actual due time. |
| The removal is due, and an operation is pending or reports an error. | This record does not yet show successful completion. | Check the account, permission and operation details before choosing a correction. |
| A manual task or service-desk ticket is marked complete. | The work record was closed through that path. | Confirm the required change on the actual target account. |

The Campaign Remediation Status Report illustrates why field meaning matters. Its Finished status can follow connected-source revocation or the completion of a manual task or service-desk ticket. Read what caused that status. Do not describe every Finished row as the same kind of direct observation of the application.

Likewise, an accepted change request is not evidence that every required permission changed. If there are several target changes, inspect their individual results. Do not infer that all succeeded from one successful operation.

An error or delay also does not authorize a blind repeat. Establish the current work and account state, then use the supported correction for that operation. An uncertain response can require checking what already happened before attempting the same change again.

## Check the account, then check what ISC now knows

For the ordinary Procurement example, suppose the subsequent operation result identifies the correct source, `pur-4801` and `ORD_APPROVE` and reports successful removal. A current application check confirms that Approve Orders is absent and View Orders remains.

Together, these results show that order approval was removed from the correct account while justified viewing was retained. They do not describe an account deletion or every other account the person owns.

Now consider what ISC displays. **Account aggregation** collects account information from a source. If the displayed entitlement information came from before the application change, it may still describe the earlier permission set.

Check when the account information was collected and whether a later collection has brought the changed permissions into ISC. Reading the account after removal is different from sending the removal change. Also keep checking which account and person the information belongs to. A newer collection time does not, by itself, prove that the account is associated with the correct person.

Campaign reports have their own generation time. Regenerate a report after relevant campaign changes when you need its updated status. Do not treat an old downloaded report, a current account view and a newly completed task as observations made at the same time.

Before reporting success, you should be able to explain which decision was finalized, when removal was due, what work carried it out and what changed on the correct account. If the records disagree, compare their times and the accounts or permissions they describe. That helps you find what still needs checking.

## Work through a removal scheduled for later

Identity 4901 owns account `inv-4901` in Invoice Production. Its requested **Invoice Approval** access profile contains Read Invoices, which permits reading invoice records, and Approve Invoices, which permits authorizing invoices for processing. An access profile is a bundle of entitlements from one source.

The person needs both permissions during a handover, until an approved future removal time. After the handover ends, the person needs neither permission in this profile. The account information is current and linked to the correct person. No other assignment requires either permission to remain. The reviewer has permission to review this profile, understands it and is reviewing somebody else's access.

In this review, a future revocation date is supported. Inspection confirms the intended removal time was saved, its time zone is understood and the review was finalized. An account check made before that time still shows both permissions.

Someone calls this a failed revocation because Revoke and sign-off are already recorded. What would you explain?

The supported removal time has not arrived. The account still holding the permissions before that time does not establish failure. Verify that the continued authorization and saved timing still match the handover, then check the appropriate processing and account result when removal is due.

Now inspect the account after that same confirmed removal time. Both permissions are still present. Can the date and sign-off tell you which operation failed?

They cannot. Establish what work was initiated for this profile and account, whether it has run, and what its actual results say. The observation requires investigation, but it does not distinguish pending work, a failed change, an incorrect target or another cause by itself. Do not guess a retry or task recipient from the elapsed time.

Finally, change the delivery path. The actual removal work is a manual task, and the task or associated service-desk ticket is marked complete. No application check has been supplied.

That closure is evidence about the work record. To establish the required result, check that `inv-4901` no longer has the reviewed profile's permissions in the application. Keep the intended scope clear: this example requires both profile capabilities removed after handover, not deletion of the account or a claim about unrelated permissions.

Revoke tells us what should be removed. We then need to confirm that the review was finalized, check when removal is due, follow the work that makes the change and verify the result on the correct account.
