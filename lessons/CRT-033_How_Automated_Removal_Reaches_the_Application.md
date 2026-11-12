# How does automated removal reach the application?

A reviewer selects Revoke for permission to change stock quantities. Later, that permission must disappear from the person's warehouse account.

How does a choice in an ISC review become a change in another application?

Let's follow the information that makes the change possible. The review supplies the decision. ISC's provisioning work carries out the required change through a configured connection. The warehouse application must accept that change on the correct account.

## Start with the permission that must change

SailPoint Identity Security Cloud, or **ISC**, maintains an **identity** representing a person. An **account** is a record in an application through which the person can use that application. Accounts in other systems can be associated with the identity.

Identity 5101 owns the account with sign-in name `wh-5101` in Warehouse Production. In that application, the account's identifying value is `acct-8842`. The sign-in name helps us recognize the account; `acct-8842` is the verified account reference used by this example's removal operation.

The account currently has two **entitlements**, rights that ISC represents from the application:

- **Stock Read** permits viewing stock quantities.
- **Stock Adjust**, identified by value `STOCK_ADJUST`, permits changing stock quantities.

The person's current work requires viewing quantities but no longer authorizes changing them. We want to remove Stock Adjust while keeping Stock Read and the account itself.

A **certification campaign** organizes access reviews. A **certification** is an assigned review within the campaign. Here, the two entitlements appear as separate review items. A reviewer who understands the access and is allowed to review it approves Stock Read and selects Revoke for Stock Adjust. The reviewer is reviewing somebody else's access.

For this case, the account data is current and linked to the correct person. Neither entitlement is included through an access bundle or required by an automatic assignment, and no other assignment requires Stock Adjust to remain.

The reviewer has signed off, meaning the review's decisions are finalized. We have also checked that the applicable removal work has started and is due; no future removal date applies. These facts give us a specific change to follow:

Remove `STOCK_ADJUST` from `acct-8842` in Warehouse Production.

## A source tells ISC which connection to use

The warehouse application holds the actual account and enforces its permissions. ISC holds information about that account so it can manage and review access.

A **source** is ISC's configuration for a system or collection of account data. The Warehouse Production source identifies the connection used for this application. A **connector** is the integration that knows how to read or change data through that connection.

This separation matters when two sources represent different environments. Warehouse Production and Warehouse Test may contain similar account names and permission labels. A successful change in Test would leave the Production account unchanged.

Within the right source, the operation must also identify the right account. The ISC identity ID identifies the managed person. It does not automatically serve as that person's account identifier in every application. One person can have several accounts with different identifiers.

The source's **account schema** describes the account fields and how ISC interprets them. Its configured **Account ID** is used to reference accounts in that source's context. A display name is not enough to establish the operation's target.

For our removal, the verified application account reference is `acct-8842`. We check how the configured operation uses that reference. We do not substitute 5101 merely because it is the person's ISC identity ID.

Now look at the permission. Stock Adjust is the readable name; `STOCK_ADJUST` is its identifying value here. The operation needs the right kind of access, such as a group membership, and the right value within it. Removing another right with a similar label would not meet the requirement.

## Provisioning turns the requirement into an application change

**Provisioning** is work that changes accounts or access in another system. Removing access through that process is also called deprovisioning. In this review, **remediation** means carrying out the required removal.

The change needs enough information to answer: which source, which account, which permission and what action? The connector then uses the supported operation for that application.

For this example, Warehouse Production uses the Web Services SaaS connector. A working Remove Entitlement operation has already been configured for the warehouse application's interface.

An **API**, or application programming interface, lets software request data or actions from another system. An **API endpoint** is the address used for a particular interaction. Through its configured operation, this connector sends the account reference and entitlement value in the form the warehouse API expects.

Here, the intended instruction is “remove this account's Stock Adjust membership.” It is not “delete the Stock Adjust permission from the whole application” or “delete the person's account.”

The endpoint, request format and response handling belong to this integration's configuration. Applications do not all expect the same kind of web request or the same fields. The word Remove in a review cannot tell you the exact request that a particular target API expects.

The connector therefore connects the business decision to a technical operation. It uses the configured destination, account identification and permission value to request the required change. If any of those are wrong, an operation can fail or affect something other than the reviewed access.

## The connection needs permission to make this change

A connector may be able to read an account without being able to change its permissions.

Reading allowed ISC to collect Stock Adjust and include it in a review. Removing Stock Adjust requires the application's supported write operation, enabled provisioning where required and sufficient permission for the connection to perform that operation.

For this Web Services SaaS source, provisioning must be enabled for changes. That source setting does not create missing removal-operation configuration or grant permission inside the warehouse application.

The connection also uses **integration credentials**, such as a configured account and password or an API token. These let the application recognize the software connection.

**Authentication** checks who is connecting. **Authorization** determines what that connection is allowed to do.

The reviewer signs in to ISC to make the access decision. The warehouse user signs in with their own account to do warehouse work. The integration uses its configured credentials to communicate with the warehouse application. These are different responsibilities; approving a review does not give the integration extra warehouse permissions.

For our normal case, the supported removal operation is configured, provisioning is enabled, the connection can reach the application and its credentials permit removing this membership from `acct-8842`.

Suppose the same credentials could read stock memberships but could not remove them. The earlier successful collection would still make sense. It proves a read was possible, not that this write is authorized.

The correction should address the actual missing operation or permission. Giving the integration unrestricted application administration is not a conclusion you can draw from one denied removal. Likewise, changing a source-wide provisioning setting needs its own authorized configuration process; it is not a harmless way to retry one item.

## Follow the request and the response

With the normal conditions in place, the configured operation sends the required change to the warehouse application. The application processes it and returns a response through the connector.

A request and its result can arrive at different times. **Asynchronous processing** means the work continues separately from the action that submitted it. Returning to a page or seeing that work was submitted does not establish the final account result.

Also, a response can have more than one part to inspect. In a Web Services integration, HTTP is the protocol used for the web request and response. An HTTP success code can accompany a response body, the returned content, that contains an application error. The connector's error handling must recognize that error. Otherwise, the success code can hide a failed change.

So read what the operation actually reports. Did it address the right account and entitlement? Does the response establish removal, report a rejection or leave the result uncertain?

For this example, suppose the operation result identifies `acct-8842` and `STOCK_ADJUST` and reports successful removal. A current check in Warehouse Production confirms that the account no longer holds Stock Adjust and still holds Stock Read. Those example results support the intended change.

The following diagram follows the change and the evidence you inspect. It does not prescribe one internal service sequence, request count or processing duration for every source.

```text
Finalized, due removal
  Warehouse Production / acct-8842 / STOCK_ADJUST
                         |
                         v
ISC provisioning work
  Remove Stock Adjust from this account
                         |
                         v
Configured connector operation
  Correct destination, account and entitlement value
  Supported write enabled; connection authorized
                         |
                         v
Application receives the change
  Application result returns through the connector
                         |
                         v
Inspect activity and operation details
  Correct target? Success, error or unresolved work?
                         |
                         v
Check the actual account
  Stock Adjust absent; Stock Read retained
                         |
                         v
Check later account information in ISC
  Read the changed source state; compare times
```

Some integrations use a **virtual appliance**, or **VA**, a virtual machine running on the organization's infrastructure. In a VA-based connection, that appliance provides a route between ISC and the connected systems. It regularly checks for requested work such as provisioning. Its connectivity and health can therefore matter to delivery.

Use the architecture of the actual source when investigating. Do not add a VA step to every connector merely because another source uses one.

## Read the activity behind the review

The review page tells you what the reviewer decided. Source settings tell you how a connection is configured. Activity details tell you about the work that attempted the change.

For direct-connected certification removal, the documented Activities view is under Admin > Identity Management > Activities. Provisioning Activity reports also provide event details. Open the relevant record rather than stop at a campaign percentage.

Match the work to the review using its source, account, permission, action and time. A person's name alone does not distinguish their ordinary account from an administrator account. Check the available operation details and errors for the actual target.

Account Activity distinguishes overall **Status**, progress **Stage** and **Account Request Status** for individual parts of the work. Keep those fields separate.

For Account Request Status specifically:

| Value | Meaning |
|---|---|
| Committed | The requests were sent to the connectors. |
| Finished | The source results were confirmed; they can be successful or failed. |
| Retry | The action failed and ISC intends to try again. |

These values are not three mandatory steps in every operation. Finished requires reading the result, and Retry is a recorded intention rather than proof of a later successful change.

An activity can cover more than one account or change. Follow the relevant part and its errors. One successful account change cannot establish a different account's removal.

## When the expected result is missing

Return to the actual operation before choosing a correction.

If there is no matching removal activity, first check the review's finalized decision, the applicable trigger and timing, the chosen source and the work you can see. An empty view is not enough to conclude that the target rejected a request.

If the operation reports a connection or permission error, inspect that error in the context of the configured destination and credentials. A failure to contact the application and a response denying a particular change point to different checks.

If the response is uncertain, inspect the current account as well as the activity. Repeating the change immediately could overlook work that already succeeded. Use the supported recovery for that source and operation.

If an operation reports success but the expected access remains, compare the exact account, permission value, result and observation time. A different target, older data or another access path are possibilities to establish, not causes to assume.

A failed automatic attempt does not prove that somebody has received a manual task. Check for actual assigned work before relying on that route.

## Check what the application has and what ISC has collected

After removal, the warehouse application and ISC may be displaying information collected at different times.

**Account aggregation** reads account information into ISC. If the account's displayed permissions came from a collection before removal, Stock Adjust may still appear in that older information.

Compare the current application account with the time and result of later collection. Reading the changed account is different from sending the removal instruction. Do not run another removal solely because an old observation still lists the right.

Equally, do not report success solely because a label disappeared in one view. Keep the evidence connected: the correct decision, the correct operation and account, its result, and a current observation of the required permission change.

## Try the same reasoning with two accounts

Identity 5201 owns `rep-5201` and `adm-5201` in Reporting Production.

The reporting account holds Read Records, which permits reading records, and Export Records, identified by `REC_EXPORT`, which permits exporting records. Its current duty needs reading but no longer authorizes export.

The administrator account has separately justified Export Records access for its current administrative duty. That account's export permission should remain.

The data and account associations are current and correct. These are standalone permissions, with no package or automatic assignment requiring export on the reporting account. A permitted reviewer who owns neither account finalizes Revoke for Export Records on `rep-5201`. The removal is due and uses an automated connection.

An activity's Account Request Status says Finished. Its details name `rep-5201` and `REC_EXPORT`, but report that the integration was denied permission to remove the membership. A current application check still shows export on that account.

Can you report that the review's removal succeeded?

No. Finished does not resolve the error into success. The detailed result and current account both show that the required removal has not been achieved. Investigate the specific write permission and supported correction. Preserve the account, its justified reading and the administrator account's separately justified export. Do not infer a manual task or choose a blind retry.

Now change one fact. The operation reports successful removal, but its target is `adm-5201`. There is no result for `rep-5201`.

That success concerns the wrong account. The intended removal remains unproved, and the change to justified administrator access needs its own correction through the organization's process. A shared identity and matching permission name do not make the two accounts interchangeable.

When following an automated removal, keep asking: which application account did this operation change, which right did it address, and what evidence shows the required result?

