# How is a certification different from an access request or lifecycle rule?

A manager approves an access request. A month later, a reviewer approves access in a certification campaign. Another person receives access automatically because of their lifecycle state.

All three involve deciding what access a person should have. But they start with different information and answer different questions.

Let's connect each one with the work it is meant to do.

## Start with the access someone needs

An **account** is a person's record in an application or system. **Access** is what that account is allowed to do.

SailPoint Identity Security Cloud (ISC) represents the person through an **identity**, which connects information about them with their accounts and access.

An **entitlement** represents a particular access right, such as permission to view reports. An **access profile** groups related entitlements from one **source**. A source is ISC's configured representation of the system or account-data collection being managed.

For example, an access profile named Reporting Export contains reports-view and reports-export from a reporting source. Those entitlements allow viewing reports and exporting them.

The profile is a named package. Its name helps a person choose the access, while its contents determine the rights involved.

For the request below, the intended account is correctly associated with the identity. It does not yet have either permission. The profile is available for requests, and ISC's connection to the reporting system supports and is authorized to grant its access. There is no delayed start or additional activation needed.

## An access request asks for a change

The person needs to export reports for an approved piece of work. They submit an **access request** for Reporting Export.

The request identifies what access is wanted and who should receive it. The person submitting it is the **requester**. The person receiving the access is the **recipient**. They are the same person in this example; supported requests for others can make them different.

The request follows its configured approval process. An **approver** evaluates whether the requested access is appropriate for the recipient.

Here, the configured approver confirms the reporting need and approves the request.

That approval accepts the proposed grant. ISC then uses the supported access-change process to provide the profile's entitlements to the recipient's account.

**Provisioning** means changing access in systems. It includes granting access and removing it.

In this example, the change succeeds: the account receives reports-view and reports-export. The person can perform the approved reporting work.

Notice the separate observations: the request was submitted, its required approval was obtained, and the account received the permissions. A record saying “approved” does not, by itself, establish that the grant succeeded in the application.

The approval requirements come from configuration. Do not assume that every access request has the same approver or number of approval steps.

Requests can also ask for supported access removals. In that case, the requested change is to take access away, and the configured removal-approval process applies. A removal request and a certification review remain different records, even when both ultimately require removing the same access.

## A certification asks about access the person already has

Now move forward. The person has stopped doing reporting work. The account still holds the requested Reporting Export profile.

The earlier approval explained why the access was granted. It does not establish that the person needs it today.

An administrator includes the represented access in a **certification campaign**, an organized set of access reviews. A **certification** is one assigned review within that campaign. Its **reviewer**, also called the certifier, examines whether the access remains appropriate.

A **review item** is the particular access presented for a decision with its person and account context.

Here, the review item is the requested Reporting Export access profile. Its two entitlements are the contents of that package; we are not treating them as two separate, individually reviewable items.

The reviewer confirms that the person no longer needs either viewing or exporting reports. No separate automatic requirement or other access assignment is keeping this package for them.

Those conditions support **Revoke**, a decision that the reviewed access should be removed.

After the required review confirmation and applicable campaign processing, the resulting removal work must be carried out. **Remediation** means making the change needed to address the review decision. We still need evidence of the resulting access on the correct account.

Now change the current business need. If the person still has an approved responsibility requiring this reporting package, **Approve** accepts keeping that reviewed access.

Certification Approve does not ask ISC to grant an unrelated missing permission. The item concerns access represented for the review.

The same word, approval, therefore needs its context. Request approval accepts a proposed change. Certification approval accepts keeping the reviewed access under the conditions being assessed.

## Check what the review item includes

Suppose the person no longer needs export but still needs to view reports.

That differs from our removal example, where neither right was needed.

Here, nothing else grants the viewing permission. Removing Reporting Export would therefore remove that permission too. You cannot treat a decision about the whole profile as though it concerns only the entitlement whose name caught your attention.

Establish how the approved viewing access will be preserved before treating removal of the whole package as the right outcome.

The review item, its contents and the person's remaining need must agree. A familiar Revoke button does not make those questions disappear.

## Lifecycle-based access starts with a configured requirement

Some access is intended for everyone who meets a defined business condition. It would be repetitive to ask each person to request it separately.

A **lifecycle state**, often shortened to **LCS**, represents a configured stage in the person's relationship with the organization, such as active employment or termination. The state can have configured access requirements and account actions.

A state can be calculated from mapped identity data or assigned by an authorized administrator. A **mapping** specifies how incoming information is used to set an identity value.

For example, a configured calculation can use personnel-status information to determine that the identity belongs in the active lifecycle state. That state has been enabled and configured to grant an Employee Portal access profile containing portal-use, permission to use the employee portal.

**Identity processing** evaluates identity information and the applicable access configuration. With the state and profile correctly configured, ISC initiates the access work needed for that lifecycle requirement.

There is no separate personal request for the portal package in this example. The configured state requirement supplies the reason for the grant.

This is a form of **birthright access**: access assigned automatically under defined business conditions.

The label active alone does not tell you which access will be granted. You must inspect that state's configuration. One organization can require a portal package in its active state; another configuration can define different requirements.

## Why can lifecycle-required access come back?

Suppose the identity remains in the active state and Employee Portal is still one of that state's required access profiles.

Someone removes the portal access manually in the application. That changes the account, but it does not remove the lifecycle requirement in ISC.

Lifecycle-granted access profiles are enforced while the state applies. Subsequent processing can generate provisioning work to restore the required profile. The actual application result still depends on the supported change path and successful delivery.

If the portal requirement itself is wrong, repeating manual removal leaves the instruction that caused the grant in place.

Investigate whether the identity's state is correct and whether that state should require this package. An authorized correction belongs where the incorrect data, calculation or access requirement is defined.

Do not generalize this into “every lifecycle action is continuously retried.” Account enable or disable actions have their own behavior; the access-profile enforcement described here does not establish a persistent retry rule for those account actions.

## That also affects what a certification can review

Access profiles granted through the person's lifecycle state do not appear as individual profile items in these certifications. Their entitlements are not individually certifiable while they are included in that required profile, meaning they are not offered as separate review decisions.

Our requested Reporting Export profile and lifecycle-required Employee Portal profile therefore have different review behavior because their assignments come from different places.

**Assignment origin** means how the person received the access: through a request, a lifecycle requirement or another supported path.

If Employee Portal is absent as an individual certification item, do not immediately conclude that the person lacks portal access. Check its assignment origin, current lifecycle state and the campaign's actual scope.

A certification decision is not a way to rewrite the lifecycle requirement behind that access.

The **access model** is the configured organization of access packages and assignment requirements. When the wrong requirement is causing access, the investigation must reach that configuration and the data it evaluates.

## These controls work alongside each other

The first branch below follows an approved request for additional access. Removal requests are another request intention. The branches are separate starting points, not three stages that every access item passes through.

```text
A need for additional access
    |
    v
Access request
    |
    v
Approved grant work

Existing reviewable access
    |
    v
Certification decision
    |
    v
Keep / require removal

Assigned lifecycle state
    |
    v
Configured requirements
    |
    v
State-based access work
```

Where a change is required, follow the actual access-change work and the account result. The diagram shows the reason for the work; it does not promise that a grant or removal has already succeeded.

| Control | What starts the reasoning? | Main question | Record or configuration to inspect |
|---|---|---|---|
| Access request | A submitted request for a supported access change | Should this requested change be allowed? | Request, recipient, item, required approvals and resulting access work |
| Certification | Generated review work for represented access | Should the person keep this reviewed access now? | Review item, person/account context, decision, confirmation and required follow-up |
| Lifecycle-based access | An assigned state with configured requirements | What access does this state require under the current configuration? | State value, its data/calculation, configured requirements and resulting access work |

A person's active lifecycle state can justify their portal access while a separate reporting request supplies project access. Later, a certification can question whether the requested reporting package should remain.

The portal requirement does not establish a continuing need for every additional permission on the person's accounts. The reporting request's original approval does not settle today's review. Each control contributes a different part of the access decision.

## Use the starting question to choose what to inspect

Someone says, “The person needs reporting access but does not have it.”

You first need a supported way to request or assign that access under the organization's process. A certification approval is not a substitute for a missing grant request.

Someone says, “This was approved six months ago, so approve it again.”

Ask what work requires the access now. The historic request and the current review answer questions about different times and conditions.

Someone says, “I removed the portal permission, but ISC added it back.”

Inspect the access requirement and assignment origin. If the current lifecycle state still requires Employee Portal, that requirement explains why ISC can generate restoration work. Verify the actual operation and account result rather than assuming every reappearance has this cause.

Now suppose the underlying personnel status is wrong.

A correctly configured calculation can produce the wrong business result from inaccurate input. Establish the correct personnel information and authorized correction, then verify the resulting state and access behavior. Changing a review decision does not repair the personnel record.

Finally, someone says, “Move this person into an inactive state so one project permission goes away.”

Check whether the proposed state actually describes the person. It may affect much more access than that one project permission. Identify the assignment responsible for the project access instead of falsifying the person's lifecycle information to obtain a narrow result.

## Try it with two different access packages

An identity holds these packages:

- Invoice Approval was granted through an approved request. It provides invoice-approve, permission to approve supplier invoices through the person's payments-system account.
- Employee Portal is granted by the identity's active lifecycle state. It provides portal-use.

The person remains actively employed and still needs the portal. Their work has changed, and an appropriate reviewer confirms that invoice approval is no longer needed.

A campaign contains an individually reviewable Invoice Approval item. There is no separate Employee Portal profile item. The account and identity information are accurate, and no other assignment requires invoice-approve.

Two suggestions are made: approve Invoice Approval because its original request was approved, or change the lifecycle state to inactive.

Which suggestion follows the facts? What should you inspect and verify?

Neither suggestion follows.

The current review asks about today's invoice-approval need. The supplied evidence supports Revoke for the requested Invoice Approval package, followed by the required review confirmation and applicable removal work. The original approval explains the earlier grant.

The active lifecycle state remains correct. Changing it to remove one unrelated requested package would make the identity information inaccurate and could affect its other configured access behavior.

Employee Portal's lifecycle origin explains why it is not a separate profile decision in this example. Its absence is not evidence that the portal grant is missing.

To establish the invoice-removal outcome, follow the actual change for invoice-approve on the intended payments-system account and verify its resulting access. Keep that evidence separate from the correct portal requirement.

If the proposed Revoke has only been recorded, the supplied facts do not yet establish that account-level removal happened.
