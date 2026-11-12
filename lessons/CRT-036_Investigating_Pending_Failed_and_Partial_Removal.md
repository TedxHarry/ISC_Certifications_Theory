# How do we investigate pending, failed or partial removal?

An access review says Revoke, but the account still has some of the access. An activity shows an error. Somebody suggests trying the removal again.

Before repeating it, let's establish what happened. Was the work waiting to run? Did one change succeed while another failed? Or did ISC stop waiting for a response without learning the final result?

Those situations need different next actions. The error is a starting point for investigation.

## Write down the change you are trying to establish

SailPoint Identity Security Cloud, or **ISC**, maintains an **identity** representing a person. An **account** is the person's record in an application. A **source** is ISC's configuration for that application or its account data.

Identity 5701 owns `led-5701` in Ledger Production, an application that stores financial transaction records. The account has three **entitlements**, rights represented from the application:

- **Read Ledger** permits reading ledger records.
- **Export Ledger**, identified by `LEDGER_EXPORT`, permits exporting ledger records.
- **Post Adjustments**, identified by `LEDGER_POST`, permits recording corrections to those financial transactions.

The current job needs reading only. Export and adjustment posting are no longer authorized.

A **certification campaign** organizes access reviews. A **certification** is an assigned review within it. Here, each entitlement is reviewed individually. A knowledgeable reviewer with permission to perform this review approves continued reading and selects Revoke for export and adjustment posting, recording that those two rights should be removed. The reviewer is reviewing somebody else's access.

The account data and person/account association are correct. The rights are standalone; no package, automatic assignment or other requirement supplies the two rights being removed.

The reviewer has signed off, meaning the decisions are finalized. We have checked that removal is due and the relevant work exists. The required outcome is:

Keep Read Ledger on `led-5701`; remove `LEDGER_EXPORT` and `LEDGER_POST`.

We need to establish both removals while keeping justified reading. Resolving an error message only helps if the required account change actually happens.

## Find the work behind the review decision

**Provisioning** is work that changes accounts or access in another system. **Remediation** is carrying out the review's required removal.

A **connector** is the integration used to communicate with the application. In this example, the source supports both removal operations, its ability to make changes is enabled and the work targets `led-5701`.

That does not establish that every attempted change will succeed. The application must accept each required change.

The review page records the decision. The activity records describe the work used to carry it out. The application account shows which permissions it now holds.

For direct-connected certification removal, the documented activity view is under Admin > Identity Management > Activities. Provisioning Activity reports also provide event details. Open the relevant work and inspect its source, account, action, time, result and errors.

A person's name alone is not a sufficient match. The person might own several accounts, and similar access names might exist in different environments.

If you cannot find matching work, check the actual decision, finalization, due time, source and available activity evidence. An empty search result does not establish that the application rejected a request. First establish whether the work was created and whether you are examining the right records.

## Read the field as well as its value

**Account Activity** records actions on external accounts. Its overall **Status**, progress **Stage** and **Account Request Status** for individual parts describe different things.

| Field and value | Meaning |
|---|---|
| Overall Status: Pending | Scheduled work has not yet been attempted. |
| Account Request Status: Pending | Work on the account is in progress. |
| Stage: Executing | The action is in progress. |
| Overall Status: Incomplete | Some requested actions succeeded and some failed. |
| Account Request Status: Committed | Requests were sent to the connectors. |
| Account Request Status: Finished | Source results were confirmed, whether successful or failed. |
| Account Request Status: Retry | A failed action is intended to be tried again. |
| Account Request Status: Failed | The action failed and will not be retried through that recorded work. |

Keep each value with its field. The values do not form a required sequence that every removal follows. Finished still requires reading the result. Committed establishes sending, not successful removal.

## Follow a partly completed removal

Suppose the Ledger activity's overall Status is Incomplete. Its details show a successful removal for `LEDGER_EXPORT` and a permission-denied result for `LEDGER_POST`.

A current check in Ledger Production shows:

Read Ledger remains, export is absent and adjustment posting remains.

This is a **partial outcome**: part of the required work succeeded, while another part remains unresolved.

The export removal should not be reported as failed merely because the overall work was incomplete. Equally, its success does not establish that adjustment posting was removed.

We now have a specific remaining problem. The application denied the operation for `LEDGER_POST` on the intended account. The next check concerns that write permission and operation, rather than whether the reviewer was allowed to select Revoke.

The reviewer acts inside ISC. The connector uses its configured **integration credentials**, such as an application account or token, to communicate with the ledger application.

**Authentication** establishes who is connecting. **Authorization** determines what that connection may do. A connection may be recognized by the application yet lack permission for a particular change.

For this example, the integration can perform the export removal but is denied the adjustment removal. Successfully reading the account, or changing another permission, does not establish authority for this operation.

Have an authorized application administrator check why the integration cannot perform this removal and arrange the appropriate correction. Then establish whether an automatic attempt is still planned or a new permitted attempt is needed for the outstanding work. Follow its result on the correct account.

Do not assume the successful export removal was rolled back. The current account already tells us otherwise. Preserve that successful outcome and justified reading while resolving the outstanding adjustment permission.

## Let the actual error guide the next check

A connection error and an application rejection occur at different points.

If the error says the destination could not be reached, inspect the configured destination and the connection's actual availability. That does not establish that the application examined and rejected the permission change.

If the application does respond, inspect what it rejected. Invalid credentials point to authentication. A denied operation points to authorization. An account or entitlement value that does not match the intended target needs an identification or configuration check.

The exact response matters. Do not replace it with a broad diagnosis such as “ISC cannot remove access.”

For a Web Services connection, software communicates through an **API**, an interface for requesting application data or actions. **HTTP** is the protocol used for the web request and response.

An HTTP success code can accompany returned content containing an application error. The connector's response handling must recognize the relevant error conditions. Read that content and the operation details before treating the code alone as a successful removal.

A delay also needs its own evidence. Work that is still active needs tracking. An established failed change needs a supported correction. A missing final response needs the account state checked before another attempt is chosen.

## Understand what a retry can and cannot do

A **retry** is another attempt at the work. A **retryable error** is a failure that the applicable service or connector recognizes as eligible for another attempt.

Retrying can help when the original obstacle is temporary. Repeating a request does not, by itself, grant a missing application permission or correct a wrong account identifier.

Two documented policies illustrate why the scope matters.

At the provisioning-service level, recognized connector errors include `ConnectException` and `NoRouteToHostException`, connection-related errors. For errors treated as retryable there, the documented policy is once per hour, up to three retries. Other queued work can delay the attempt.

That is not a rule that every removal error will be retried, or that the account must be corrected within three hours.

The Web Services SaaS connector has a separate policy for HTTP 429 and 503 responses. HTTP 429 indicates too many requests; HTTP 503 indicates service unavailability.

**Rate limiting** means the receiving service restricts how quickly requests can be made. Repeated requests can therefore add to the condition you are investigating.

For this connector's documented policy, there are up to three retries per request. It first uses a positive `retryDelay`, a configured wait in seconds. Otherwise, it uses a numeric **Retry-After** response value, telling it how many seconds to wait. If neither is valid or present, the default is 30 seconds.

These are different policies, not two numbers to apply to every task. Identify the connector, error, current configuration and work already scheduled. Do not multiply the limits into a promised total call count or assume a new manual attempt is required while automatic work is still active.

If a record says Retry, inspect the later attempt and its result. The word describes intended further work; it does not establish that the later attempt succeeded.

If it says Failed for that individual account request, waiting on an assumed future retry is not a recovery plan. Establish the supported next action for the actual operation.

## A timeout leaves a result to establish

A **timeout** occurs when part of the connection, such as ISC or a connector, stops waiting because its allowed waiting time has been reached.

It tells us about the response wait. It does not, by itself, establish whether the application changed the account.

For example, the application may have received a request while ISC has not obtained its final result. We need operation evidence and a current account check to distinguish an unchanged permission from a change that already happened.

Before another attempt, establish what the current account holds and what work is still active or scheduled. Also check the source's supported handling when the permission is already absent.

Increasing a timeout setting is a configuration change. It may address a communication wait in an appropriate case, but it does not prove the original removal failed or succeeded. It is not a substitute for finding the current outcome.

## Choose a correction that matches the remaining work

The following diagram is an investigation map. It connects the requirement, operation evidence and account check. It is not an internal execution sequence or a promise that every error creates another task.

```text
Required removal
  Correct source / account / entitlement / due decision
                            |
                            v
Find the actual work and its results
  Compare each required change with the current account
                            |
          +-----------------+------------------+
          |                 |                  |
          v                 v                  v
Change confirmed     Work still active    Failed or uncertain
  Preserve result      Track that work     Establish cause/state
  Check retained       Check next result   Choose supported action
  justified access                         Verify new result

If only some changes succeeded, keep each result separate.
A correction is complete only when its required outcome is checked.
```

For the Ledger example, the outstanding right is `LEDGER_POST`. Once the application-permission issue has been corrected through the authorized process, check whether existing work will retry it. If another attempt is required, use the permitted procedure for this source to address that outstanding removal. The available action depends on the actual operation and delivery path.

Suppose its later operation reports success and a current check confirms adjustment posting absent, export still absent and reading retained. Those example results establish the intended account outcome.

Preserve the successful removals and justified reading, with an accurate record of how the required state was reached.

A failed automatic operation is not proof that a manual task or service-desk ticket was created. If a human delivery route is used, find the actual assigned work and establish who has permission to make the application change.

Likewise, a closed manual task is a report of completed work, not a substitute for the target-account result. In the Campaign Remediation Status Report, Finished can follow manual task or ticket closure. Read it in the context of that delivery path.

## Keep the investigation usable for the next person

When work needs to be handed over, include the exact source, account and permission, the required outcome, the relevant activity identifiers and times, the actual error and what is already known about the account.

Include successful parts and outstanding parts separately. State whether another attempt is active or scheduled, or whether that remains unknown. Check the times and time zones when connecting an attempt to a later account observation.

Then establish an appropriate owner for the next action. A source owner, application operator or integration administrator may have different responsibilities and permissions. A generic owner label does not prove that the person can perform this particular correction.

After the change, check current account information and its collection time. **Account aggregation** brings account data into ISC. Reading newer data is different from sending another removal operation.

A stale account view can make completed removal look outstanding. Another assignment that still requires the access is also different from a failed write. Investigate the relevant assignment and operation evidence instead of assuming that either explanation applies.

Keep the original error and the later outcome understandable together. A later successful correction does not mean the earlier denied attempt never happened.

## Try an uncertain response on one of two accounts

Identity 5801 owns `inv-5801` and `adm-5801` in Invoice Production.

The ordinary invoice account has `INV_READ`, permission to read invoices, and `INV_RELEASE`, permission to release invoices for payment processing. Its current duty needs reading but no longer authorizes release. The administrator account's release access is separately justified and should remain.

Current data and account association are correct. The ordinary account's release right is individually reviewed and has no bundle, automatic assignment or competing requirement.

An authorized independent reviewer finalizes Revoke for release on `inv-5801`. Removal is due. The matching work shows that the request was sent to the connector and later reports a timeout. No current application observation or verified retry plan is supplied.

Should you report successful removal, report that the application definitely rejected it, or immediately submit the change again?

The supplied information establishes none of those conclusions. Match the operation to `inv-5801`, `INV_RELEASE` and the relevant time. Inspect its details, current application state and any active or scheduled work. The administrator account is a different target.

Now a current check confirms that `INV_RELEASE` is absent from `inv-5801` and `INV_READ` remains.

The required permission state is now confirmed for that account. The timeout still leaves the earlier response uncertain. Record those facts separately and establish what existing work remains; do not create another removal just to obtain a tidier history.

If instead release is still present, identify the supported next step using the actual error, connection and existing work. Its presence alone does not explain why the request timed out.

A useful investigation ends with a specific statement: what changed, what remains, what evidence supports it and who is carrying out the next required action.

