# The review says Revoke, but access still works. How do we investigate?

A reviewer says, “I revoked that access yesterday, but the person can still use it.”

Start by finding out what revoked means in the records. The reviewer may have saved a removal choice. The review may have been finally confirmed. A removal operation may have run. Or the application may have changed while an older record still shows the permission.

Those are different observations.

You need to connect the decision with the exact account change that was required, then find where the observed result differs.

## Name the result you are trying to establish

In SailPoint Identity Security Cloud, or **ISC**, an **identity** represents a person or another managed subject. An **account** is the record through which that person or service uses an application.

A **campaign** organizes access reviews. A **certification** is an assigned review within it. A **review item** is an access entry on which a reviewer records a choice.

Suppose account **req-960** on **Requests Production** has two permissions:

- Read Requests allows viewing request records.
- Export Requests allows downloading those records in bulk.

These permissions are represented as **entitlements**, meaning permissions or memberships that ISC manages.

The current business requirement is to remove bulk export while retaining viewing.

That is the result to verify. Disabling the whole account might prevent export, but it would also remove the viewing capability that should remain.

For this example, the identity owns the correct account, both permissions are eligible for individual review, and no other assignment requires export. There is no later grant that explains continued export.

Keep those conditions with the investigation. If they differ in a real case, the explanation may differ too.

## Check what the reviewer actually completed

**Revoke** records that the reviewed access should be removed. **Sign-off** is the final confirmation of the assigned review's choices.

In the ordinary next-generation review flow, saving a choice and signing off are separate actions.

Inspect the exact item and review. A selected button is not evidence of a saved choice. A saved Revoke is not, by itself, a final confirmation.

Also inspect the required timing. A supported future revocation date can explain why some removal work is not yet due. Do not invent that explanation for every item: the documented reviewer flow does not allow setting a revocation date for entitlements.

In our example, an appropriate, authorized reviewer who is independent of the access saved Revoke for Export Requests and Approve for Read Requests. Approve accepts continued reading access. The reviewer successfully signed off at 09:30. The removal is due, and matching removal work exists.

All example times use one day and the same time zone, America/Chicago. They are supplied records, not service completion targets.

The next-generation finalization operation initiates needed remediation. **Remediation** is the work required to carry out the review's removal decision.

That does not establish that the application has already changed. Use the actual work and engine-specific conditions rather than predicting every removal from the campaign's overall status.

## Follow the work to the application

A **source** is ISC's configured representation of a system or its account data. A **connector** is the supported integration used to read data or make changes.

**Provisioning** is work that changes external accounts or access. Removing Export Requests through the connector is a provisioning operation.

In this case, the source supports automated removal and provisioning is enabled. We inspect the operation associated with the finalized export decision.

The connector uses a technical integration account to interact with Requests Production. That account is different from req-960, whose permission is being removed. It also has different authority from the human reviewer.

Permission to review access does not give the integration account permission to change the application.

Here are the relevant supplied observations:

| Time | Evidence | What it establishes |
|---|---|---|
| 09:30 | Saved Revoke and successful final confirmation | The reviewer confirmed the removal decision |
| 09:40 | Matching removal attempt rejected by Requests Production | The requested change was refused |
| 09:45 | Current application evidence still shows Export Requests | The required removal has not happened |

The application returns a 403 response and an error explaining that the integration account lacks permission to remove the membership.

An **API** is an interface through which software requests data or operations. An **HTTP response code** is the request-level result returned by a web interface.

Here, the application's own operation record establishes that this request was refused before any change was made. That is a supplied fact about this application. A code alone should not be used to invent the complete outcome of every source operation.

The decision was finalized, the correct work reached the correct target, and the application refused it because the integration account lacked the required write authority.

That explains why export still works.

## Correct the cause before making another attempt

**Account aggregation** reads account data into ISC. Rerunning it would read the account data again; it would not give the integration account the missing removal permission.

Signing the review again would also miss the cause. The review's confirmation is already established.

The responsible administrator instead checks the configured integration account and the application's authorization for the actual removal operation.

The approved correction gives that integration the specific authority it needs through the supported configuration process. There is no reason to assume that broad administrator access is required.

Before another attempt, inspect existing work. Confirm whether a retry is already scheduled or running, whether any earlier attempt has an uncertain result, and whether the removal requirement is still valid.

In our example, that check establishes that no other attempt is outstanding and that export still needs to be removed. A supported controlled retry is then performed.

The supplied later evidence shows:

- At 10:15, the removal operation succeeds.
- At 10:20, current application evidence shows export absent and viewing retained.
- A later supported account collection brings those changed holdings into ISC.

The successful operation and matching current source evidence support the required account result. The later collection supports the updated ISC representation.

Preserve the original failure and the correction evidence. Replacing an old error with an unsupported “resolved” note would hide how the result was established.

## If no matching removal attempt is visible

Return to the confirmed requirement and the work that should carry it out.

Check whether the review really contains the saved Revoke, whether final confirmation occurred, and whether the relevant removal is due.

Then establish which delivery path applies. A source may support automated changes, or it may require a person or service desk process to make the change.

Reading accounts successfully does not establish that the source can write the required change. Inspect provisioning capability, the configured operation and its actual authorization.

If the applicable path is manual, look for the actual assigned task or ticket. Do not wait for an automated connector operation that is not responsible for this change.

Also check your evidence scope. A query for the wrong source, account or time can hide the relevant work. Permission to see one review does not necessarily expose every operational record.

A due item with no established work needs investigation into the actual triggering and processing conditions. Generating a fresh campaign report does not create the missing removal attempt.

Avoid resolving this uncertainty by assuming that every engine waits for the same campaign phase or completes within the same interval.

## If work is pending, failed or only partly successful

**Pending** and **failed** describe different situations, and their exact meaning belongs to the field being read.

In Search account activity, an overall Pending status concerns work scheduled but not yet attempted. The nested Account Request Status describes an individual part of the larger activity and has its own meanings.

Inspect the specific source account and operation rather than treating every status label as interchangeable.

If some changes succeeded and others failed, the result is a **partial outcome**. List the required changes separately and establish the result of each one.

A completed change on another account does not prove that req-960 lost export. Likewise, one failed change does not mean all other successful changes should be repeated.

A **retry** is another attempt at the work. Some errors are recognized as retryable under the provisioning service or connector's rules; others are not.

For example, the **Web Services SaaS connector** integrates ISC with applications through web APIs. It has specific retry handling for some rate-limit and service-unavailable responses. That connector policy is separate from the provisioning service's retry handling.

Do not turn one documented policy into a promise that every failure will retry or recover on a fixed schedule. A missing authorization normally needs its actual cause addressed, as in our supplied case.

A **timeout** means the expected response did not arrive within a waiting limit. It does not, by itself, prove that the application made no change.

Before repeating uncertain work, inspect the current target and supported operation evidence. Establish what actually happened and how the applicable process handles another attempt.

Also inspect the returned details. A successful web response can still contain an application error if the integration's response handling is not interpreting it correctly. Match the connector's result with the source's documented response and account evidence.

## If the work says complete

Ask which work completed and what established that result.

In Search, an individual **Account Request Status** of Finished can describe a confirmed result that succeeded or failed. Read the accompanying outcome.

The **Campaign Remediation Status Report** uses Finished differently. It can follow verification of removal on a connected source, or a manual task or service desk ticket being marked complete.

A person marking a task complete is reporting that work was done. Inspect the relevant account evidence if it does not establish the required change.

Where ISC's supported source confirmation verifies the exact removal, that is useful evidence. You do not need to require an interactive user login for every account.

Keep the claim within what was checked. A task closure, completed batch or campaign completion cannot independently establish that every rejected permission is absent.

If several items need removal, account for each required result. One corrected item does not establish that the whole set is complete.

If required work remains open, identify its actual owner, current status, next action and result to verify. Do not close the investigation merely because a higher-level record looks complete.

## Check whether another path still provides the access

An **access profile** packages entitlements, and a **role** groups access for a responsibility.

**Effective access** concerns what the account can still do through all relevant paths. Removing one assignment may not remove every path to a capability.

For example, a separately assigned profile may be revoked while a role still requires one of the same permissions. The documented role-over-profile behavior retains access required by the role.

Inspect the actual assignment, the reviewed object, its contents and the resulting source permissions. Do not assume that every similar-looking permission comes from the same grant.

For overlap between independent access profiles, establish the behavior of the exact supported process and engine. Do not infer a universal retention or removal rule from the role example.

A **lifecycle state** is a configured business stage, such as active employment, that can control access. An automatic role uses membership criteria to decide who belongs.

Removing a permission manually does not necessarily change a rule that still requires access. Automatic-role access is acknowledged in the review rather than individually revoked through that item.

If the current requirement conflicts with the governing rule, resolve the actual requirement, assignment or rule through the approved process. Do not enter false identity data merely to make membership stop matching.

## Distinguish retained access from access added again

A **regrant** means access was added again after it had actually been removed.

To establish that sequence, look for evidence of the earlier absence and the later addition. Then identify the source of the new grant, such as an authorized request, an automatic assignment or a change made directly in the application.

Two observations that both show export present do not prove a regrant. The first removal may never have happened.

This distinction changes the next action. A failed removal needs its delivery cause corrected. A later grant needs its own authorization and governing conditions examined.

Do not retry the old removal blindly when new evidence shows a separate grant or a changed business requirement.

## Check the account, observation and session

A person may have more than one account. Verify which account performed the operation and which account the review targeted.

An ordinary account losing export does not establish that a separate administrator account also lost it.

Next compare observation times. Aggregation reads the account's holdings into ISC; provisioning performs the change.

In our main example, an account extract from 09:20 still shows export. That was true before the 10:15 correction. Downloading that file later does not make its account information current.

After the correct source result is established, refresh the relevant collected data through the supported method and check what was actually collected. A newly generated campaign report has its own generation time; it does not establish a new application observation.

Finally, ask what “still works” means.

A **session** is an application's continuing signed-in interaction with a user. Remaining signed in does not, by itself, establish that the rejected export operation is still allowed.

Check the named capability using appropriate, authorized application evidence. A visible button or an open page may not establish that the protected operation succeeds.

Application permission checks, cached information and session handling depend on the source. Removing one entitlement is not a universal instruction to end every session. Any needed session handling requires the application's supported procedure.

The diagram keeps these questions connected:

```text
Match the exact account, permission and expected outcome
                         |
              Is the removal finalized and due?
                         |
          Find the actual required work and its state
                         |
       +-----------------+------------------+
       |                 |                  |
  Not attempted     Failed/unknown     Reported complete
       |                 |                  |
  Check scheduling  Inspect operation  Establish what
  and ownership     and target result  completed means
       |                 |                  |
       +-----------------+------------------+
                         |
           Inspect current account permission
                         |
       Still present? Check the cause with evidence:
       failed change / wrong account / another grant
       returned access / old observation / session
                         |
         Correct the cause through a supported path
                         |
           Verify removal and required retained access
```

Follow the branch supported by the evidence. A rejected write and an old account extract need different corrections.

Do not use campaign deletion as a shortcut for stopping, retrying or reversing source work. The documented deletion removes campaign evidence; its effect on particular queued or in-flight operations must be established separately.

Preserve the records and handle outstanding work through its actual supported process.

## Try a profile removal that leaves reading available

Account **stock-970** on **Inventory Production** has a separately requested **Temporary Stock Support** profile.

The profile contains Read Stock, which allows viewing quantities, and Adjust Stock, which allows changing quantities.

A separate automatic **Stock Viewer** role requires Read Stock. It does not grant the Temporary Stock Support profile. There are no other relevant grants in this supplied example.

The requirement is to remove temporary adjustment while retaining role-required reading. An authorized reviewer, independent of this account, saves Revoke for the temporary profile and signs off. The removal is due and the work completes.

Current assignment and source evidence show:

- The temporary profile is removed.
- Adjust Stock is absent.
- Stock Viewer still applies.
- Read Stock remains.

Someone proposes retrying the profile removal until reading stops.

Compare the result with the requirement: temporary adjustment is gone, while role-required reading remains. The supplied result matches that requirement.

The remaining Read Stock is explained by the role. It is not evidence that the temporary profile removal failed, and the records do not show a removal followed by a regrant.

Now the business requirement changes: this person should no longer read stock.

Repeating the completed profile removal does not address the separate role. Inspect why the identity still meets that role's criteria and obtain the approved correction to the actual governing data, policy or supported assignment.

A correction to identity data must reflect the person's real situation. A change to shared role policy may affect other identities, so account for that scope. The role's Acknowledge item does not provide an individual override.

The earlier temporary-profile requirement was achieved. The new reading-removal requirement remains open until its governing path is corrected and current source evidence verifies that reading is absent.

That is the result to report, with the remaining responsibility and next action made explicit.

