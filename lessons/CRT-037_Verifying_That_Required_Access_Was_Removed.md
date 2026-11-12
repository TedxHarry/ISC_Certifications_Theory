# What evidence establishes that the required removal happened?

A removal record says Finished. Can you now tell the business owner that the access is gone?

First, establish what that record describes. It may report a confirmed change on a connected source. It may record that somebody closed a manual task. Those are different kinds of evidence.

**Verification** means checking the required change against reliable evidence. Let's connect the decision, the work and the account so we can explain what happened with confidence.

## Be precise about what should be different

SailPoint Identity Security Cloud, or **ISC**, maintains an **identity** representing a person. An **account** is that person's record in an application. A **source** is ISC's configuration for a system or collection of account information.

Identity 5901 owns account `rec-5901` in Records Production. Its two **entitlements**, rights represented from that application, are:

- `REC_READ`, Read Records, which permits reading stored records.
- `REC_EXPORT`, Export Records, which permits exporting records in bulk.

Current work needs reading, but bulk export is no longer authorized.

The required outcome is to remove `REC_EXPORT` from `rec-5901` in Records Production while retaining `REC_READ` and the account.

This requirement gives us both sides of the check. We need evidence that export was removed and that justified reading was preserved. An account that lost both rights would not match the intended outcome.

A matching name elsewhere is not enough. Export Records in a test environment, or on another account owned by the same person, would be a permission on a different account.

## Connect the removal to the decision that required it

A **certification campaign** organizes access reviews. A **certification** is an assigned review within the campaign.

Here, the two rights are individually reviewable. A knowledgeable, authorized reviewer who is not reviewing their own account approves continued reading and selects Revoke for export. Revoke records that the reviewed access should be removed.

The account data and person/account association are correct. The rights are standalone, and no package, automatic assignment or other access requirement supplies export in this example.

**Sign-off** finalizes the assigned review's decisions. We have checked the finalized choice for the correct item, who finalized the review and when. Removal is due; no future removal time applies.

That establishes the required decision. It does not establish the application result.

Suppose sign-off was recorded at 10:00. All times in this example refer to the same day and time zone. We can now follow the corresponding removal work rather than match records only by a person's display name.

## Follow the work through to what it confirms

**Provisioning** changes accounts or access in another system. **Remediation**, here, is the work that carries out the required export removal.

A **connector** is the integration used to communicate with the application. This source has a supported, enabled and authorized way to remove the right from the account.

The corresponding operation identifies Records Production, `rec-5901` and `REC_EXPORT`. At 10:12, it reports successful removal.

Inspect what the result means for this source and operation. A request being accepted or sent establishes less than a result confirming the required change.

The detailed activity is useful evidence. A supported automated source confirmation can establish an account result within the scope of what it checked. Verification does not require a person to sign in to every application account.

Where the result does not establish the current permission clearly, obtain appropriate current evidence from the application or a supported account read. Connect it to the exact target and time.

For direct-connected certification removal, the Activities view under Admin > Identity Management > Activities provides work details. Provisioning Activity reports also provide event details. Inspect the relevant part if one activity covers several changes.

**Account Activity** records actions on source accounts. Its **Account Request Status** describes an individual part of the larger activity. A value of Finished includes confirmed results that may be successful or failed. Read the result and errors.

The Campaign Remediation Status Report tracks revoked items. There, Finished can reflect closure of a manual task or a service-desk ticket. A **service-desk ticket** records work in a support system. Its closure tells you about the work record.

A **manual fulfillment task** assigns a person to make a change outside ISC. Closing it reports completed work. To verify manual removal, connect that report to the actual account change and the updated information brought back into ISC.

## Establish what the correct account now holds

At 10:20, a reliable current application check identifies `rec-5901` and confirms that `REC_EXPORT` is absent and `REC_READ` remains.

We have also checked how this application permits bulk export: no other permission or assignment allows it on this account.

Together, the operation result and account evidence support the required outcome. We have not merely found a successful event; we have connected it to the correct account and the intended permission change.

A source-system record, a supported automated confirmation or an authorized application check can provide target evidence. The useful question is what it establishes, not whether it came from a particular kind of screen.

If your evidence concerns a group membership, state that membership result. If your required outcome concerns an ability such as exporting records, establish how the application grants that ability and whether another route remains.

For example, losing an Export group would not establish loss of export capability if a separate application role still grants it. Confirm the relevant assignments and application permission mapping.

An **assignment** is the connection through which a person holds an access object. In ISC, an **access profile** bundles entitlements from one source, while a **role** groups access for a business function. These relationships can explain why a right remains or why a package was removed while some justified access was retained.

The application's own roles and direct permissions are configured there. They are not automatically the same objects as roles defined in ISC.

Inspect how the access was assigned and which account it applies to. **Effective access** is what the account can actually do through the relevant assignments and application permissions. Do not assume that every overlapping package protects a shared right or that every package removal removes all effective access.

## Check what ISC has learned since the change

The application result and ISC's account information may describe different moments.

**Account aggregation** reads account information into ISC. It observes what the source reports; it is different from the operation that removes the right.

Suppose the actual account is collected at 10:30, after the application check. The collection succeeds for this account, and its resulting data shows reading retained and export absent.

That agrees with the application outcome. A collection from 09:40 would describe an earlier state, even if you opened the account page at 10:35.

Check the underlying observation, not just the time somebody viewed or downloaded a record.

The same principle applies to files. A **CSV**, or comma-separated values file, contains rows and columns of reported account data. Uploading it today does not make its contents current if it was exported before the removal.

An aggregation job completing is useful information, but identify whether the intended account and permission were actually represented correctly afterward. The job might concern another source, a different account or data that does not contain the permission you are checking.

The **account schema** describes which account fields ISC stores and how it interprets them. It helps you understand what the collected information can establish. A permission not included in that data is not proved absent from every part of the application.

An authorized administrator can inspect the identity's Access details, associated source accounts and the relevant collection or activity records. A missing Search result alone needs its query, visibility, data coverage and freshness understood before it is treated as evidence of removal.

## Keep report time separate from observation time

At 10:40, a newly generated campaign report reflects the updated campaign information.

That report's generation time is not a new observation of every application account at 10:40. It tells you when that report was produced.

For the completed Records example, the evidence connects as follows:

| Time | Evidence | What it establishes |
|---|---|---|
| 10:00 | Finalized review decision | Export removal was decided for the intended item. |
| 10:12 | Matching removal result | The operation reported successful removal on the intended account. |
| 10:20 | Current application account and permission mapping | Export was absent, reading remained and no other export route was identified in the checked scope. |
| 10:30 | Later collection of that account | ISC's resulting account information agreed with the changed source state. |
| 10:40 | Newly generated campaign report | The report was produced from the available campaign information at that time. |

The order is supplied for this example. It is not a required schedule or a rule that every system confirms access only through these exact five steps.

When comparing real evidence, check time zones and which event each timestamp describes. Task closure, application change, file export, account collection and report generation are different events.

The diagram connects the evidence we need. Its arrows show the reasoning, not an internal sequence of ISC services.

```text
Required outcome
  Records Production / rec-5901
  REC_EXPORT removed; REC_READ and account retained
                           |
                           v
Connect the finalized decision to the removal work
  Same source, account, right and relevant times
                           |
                           v
Establish the current target outcome
  Confirmed source evidence for the required change
  Check other paths if the claim concerns actual ability
                           |
                           v
Reconcile what ISC and the reports now show
  Account data collected after the change
  Report generation time kept separate
                           |
                           v
State the conclusion and its limits
  What was removed, what remains, when it was checked
```

## Separate permission removal from being signed out

If `rec-5901` can still sign in and read records, that is compatible with the intended result. Reading was supposed to remain.

A **session** is the application's continuing signed-in interaction with a user. Ending that session and removing one permission are separate actions.

An open page or a visible Export button does not, by itself, establish that the account can still export. Equally, a missing button is not complete evidence about the application's other ways of performing the action.

Where the required outcome concerns actual ability, use the application's documented permission behavior and an appropriate authorized verification method. A failed check caused by an unavailable server or failed sign-in would not establish that the export permission was removed.

Session behavior depends on the source and application. For example, SailPoint's Microsoft Entra ID SaaS connector has a configuration linking session revocation to account disabling. That is a different operation and setting from revoking one entitlement in a certification.

If the requirement specifically includes ending sessions or stopping existing access immediately, establish the supported application behavior and its separate result. Do not infer that every certification Revoke signs a person out of every application.

## State exactly what your evidence supports

For the Records example, a useful conclusion is:

At 10:20, `rec-5901` in Records Production no longer held `REC_EXPORT` and retained `REC_READ`. The matching operation reported removal, the checked permission mapping showed no other export route and the later collected data agreed.

That statement names the account, the right, the retained access, the time and the supporting evidence.

It does not claim that every account owned by the person was changed, that all sessions ended or that future authorized changes can never grant export again.

If evidence is missing or contradictory, state the specific gap. “The task is closed, but the current account result has not been established” tells the next person what to check.

Likewise, if one of two required removals remains unverified, preserve the distinction between the completed and outstanding parts. A report label or percentage cannot supply the missing account result.

## Try a closed task and a newly uploaded file

Account `time-6001` in Timekeeping Production has Read Time, which permits reading time entries, and a `TIME_EDIT` group membership, which permits correcting time entries.

Current work justifies reading only. The collected group data and person/account association are correct. The group is not included through an access profile or role and is not required by an automatic assignment. An authorized independent reviewer finalizes Revoke for this individually reviewed membership, and removal is due.

A manual task naming that membership is closed at 11:10. A file is uploaded at 11:15, and a campaign report generated at 11:20 says Finished.

The file was exported from the application at 10:30, before the stated removal work. No current account observation is supplied.

Can these records establish that the group was removed?

Not yet. The closed task reports completed work, while the file describes an earlier account state. The new upload and report times do not supply a current application result. Check the intended account and group, the actual change evidence and truthful later account data.

Now suppose a current application check confirms that `TIME_EDIT` is absent and Read Time remains.

That establishes the group-membership result. But the application owner identifies a separately assigned Direct Correction permission that also permits editing. This direct grant is outside the group data collected by this example's configured source. An approved check confirms that the account can still correct time entries.

Has the business outcome, removal of editing ability, been achieved?

The reviewed group has been removed, but editing remains through the direct permission. The narrower membership change is verified; the broader ability-removal requirement is not complete.

Arrange the approved change for the remaining grant, preserve reading and the account, and verify the resulting application behavior and relevant account information. Do not describe that extra grant as automatically discovered or removed by ISC.

Finally, suppose someone merely leaves an old editing page open. Without evidence that the account can still perform the action, that page alone does not establish the remaining permission or its cause.

A confident verification explains what was checked, what changed and what remains outside the evidence. That is how a completion claim becomes something another engineer can assess.

