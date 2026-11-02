# How is a certification different from an access request or lifecycle rule?

Suppose a person needs to export reports for their work. They already have an account in the reporting application, but that account does not have permission to export reports.

They need a way to ask for that permission. Later, when their work changes, someone needs to check whether they should keep it. They may also receive other access automatically because they are an active employee.

These are different reasons for giving or checking access. Let's follow what happens in each case.

## First, connect the person, the account and the permissions

An **account** is the person's record in an application. **Access** means what that account is allowed to do. Having an account does not necessarily give the person every permission they need.

SailPoint Identity Security Cloud, or **ISC**, keeps an **identity** for the person. This is ISC's record of that person. It connects information about them with their accounts and access. The identity in ISC and the account in the reporting application are separate records.

For our reporting task, two permissions are relevant. The permission reports-view allows the person to view reports. The permission reports-export allows them to export reports. ISC represents access rights like these as **entitlements**.

An administrator has grouped these two entitlements into a package named Reporting Export. In ISC, this kind of package is called an **access profile**. When the profile is made available for requests, a person can request the package instead of requesting each permission separately.

The entitlements in an access profile come from one **source**. A source is a configuration in ISC used to collect and manage account data for a system or a collection of accounts. Here, the reporting source represents the reporting application's account data. The application itself is still where the person's account and working permissions exist.

So Reporting Export is the package name. Viewing and exporting reports are the permissions inside it. We need to know both, because a decision about the package can affect both permissions.

## The person asks for access they need

The person's reporting account currently has neither permission. In ISC, that account is correctly linked to their identity, so ISC knows whose account it is.

Reporting Export has been made available for requests. The person selects it and submits an **access request**. This records who needs access and which access they want.

The person submitting the request is the **requester**. The person who should receive the access is the **recipient**. Here, they are the same person. Where requesting for others is allowed, you can submit a request for someone else; you are then the requester, and the other person is the recipient.

In this example, the request needs approval. ISC sends it through the approval process configured for that request. The **approver** checks whether the person needs the reporting permissions for their work and approves it.

The approver has now agreed that the person should receive this access. The application account has not necessarily received the permissions yet.

ISC still needs to make the change in the reporting application. In this example, its connection to the application can add these permissions and is authorized to make that change. This request is for access that can start now, without the person having to activate it separately.

Making a change to access in a system is called **provisioning**. Provisioning includes adding access and removing it. Here, the work is to add reports-view and reports-export to the recipient's reporting account.

Suppose that work succeeds. The account now has both permissions, and the person can view and export reports.

There are therefore two results to check: the request was approved, and the account received the permissions. Seeing “approved” on the request tells you about the approval. To confirm that access was provided, check the result of the change and the permissions on the intended account.

The approval process can differ between requests. The organization's settings determine who must approve and which approval steps apply.

An access request can also ask for access to be removed, where that removal is supported. That request follows its configured removal-approval process, if approval is required. So the purpose of an access request is broader than asking for new access: someone is asking for a particular access change.

## Later, someone checks whether the access is still needed

Now suppose the person has stopped doing reporting work. Their account still has the permissions that were granted earlier.

The original request explains why they received access at that time. We now have a different question: should they keep it for the work they do today?

An administrator organizes access reviews in a **certification campaign**. The campaign brings together the access that needs to be reviewed and assigns the reviews to people.

A **certification** is an assigned review within that campaign. The person responsible for making its review decisions is the **reviewer**, also called the certifier.

In this example, ISC has collected information showing the person's reporting access, and the campaign includes their Reporting Export profile. The reviewer sees that profile as a **review item**: the access they must make a decision about, shown with information about the person and their account.

The reviewer checks what Reporting Export allows and whether the person still needs those permissions. Here, the reviewer confirms that the person no longer needs to view or export reports. We have also checked that nothing else in ISC requires this person to keep either permission.

The reviewer selects **Revoke**. This records the decision that the reviewed access should be removed.

Selecting Revoke does not itself show that the reporting account has lost its permissions. The reviewer also needs to finish and confirm the review. This confirmation is called **sign-off**: the reviewer confirms that they have completed their decisions.

The campaign's process determines when those decisions lead to removal work. Whatever the timing, the required change must then be carried out in the reporting application. Recording the decision and changing the account are separate steps.

You will see the term **remediation** for the work needed to act on a review decision. For this Revoke decision, remediation means carrying out the required removal. To confirm the outcome, check that the intended reporting account no longer has the permissions that should have been removed.

Now suppose the reviewer finds that the person still needs both permissions for their current work. In that case, **Approve** means the reviewer accepts that the person should keep the access being reviewed.

Notice what approval means in each situation. In the earlier access request, the approver agreed to give the person the requested access. In this certification, the reviewer agrees that the person should keep the access shown for review. A certification approval does not request an unrelated permission that the person is missing.

A request to remove access and a certification Revoke can both lead to removal. Their starting points are different: one begins with a submitted request for a change; the other begins with an assigned review of existing access. They remain separate records and processes.

## What if only one permission is no longer needed?

Reporting Export contains permission to view reports and permission to export them. In our review, the profile is one item. The two permissions are its contents; they are not separate items with their own decisions here.

Suppose the person still needs to view reports but no longer needs to export them.

If you revoke the whole profile, the removal concerns both permissions. In this example, nothing else in ISC requires the person to keep the viewing permission. Removing the package would therefore also take away viewing access the person still needs.

Before choosing that outcome, establish how the person will keep the approved viewing access. An authorized administrator may need to arrange access that fits the remaining need. Check the effect of that arrangement together with the proposed removal. After all changes are complete, viewing should still be allowed and exporting should no longer be allowed. Do not assume that adding another package with the viewing permission guarantees that result.

The question is therefore more specific than “Does this person need export?” You also need to ask, “What exactly will this decision remove, and what does the person still need?”

## Some access is given because of the person's lifecycle state

Consider access to an employee portal. An organization may decide that everyone in a particular employment stage should receive this access. Asking every person to submit the same request would repeat work that the organization has already decided should happen automatically.

ISC can represent a stage in the person's relationship with the organization through a **lifecycle state**, often shortened to **LCS**. Examples include active employment and termination. Administrators configure what access and account actions belong to a state.

For the portal example, the administrator has enabled an active lifecycle state. In that state's settings, they have selected an access profile named Employee Portal. It contains portal-use, the permission to use the employee portal.

That setting gives ISC an instruction: a person assigned to this state should receive Employee Portal.

How does ISC know which state applies to the person?

One way is to use information received about them. A **mapping** tells ISC which incoming information to use for an identity value. Here, the mapping uses an employment-status field to set the person's lifecycle state. The supplied field value is active, and it matches the active state configured in ISC.

During **identity processing**, ISC evaluates the person's information and the related access settings. In this example, it uses the mapping to establish the active state. It then uses that state's settings to determine that the person should receive Employee Portal.

These are two connected decisions. The employment information helps determine the person's state. The settings for that state determine which access it requires.

ISC then initiates provisioning for the required profile. The person's portal account is available, and the connection supports granting the portal permission in this example. Suppose the change succeeds: the account now has portal-use.

The person did not submit a portal request. The reason for giving access came from the configured lifecycle state. Access given automatically under business conditions like this is called **birthright access**.

A mapping can include a calculation when the incoming information needs to be interpreted. An authorized administrator can also assign a lifecycle state manually. Whichever way a state is assigned, you still need to inspect that state's settings to understand its access effects.

The name active does not, by itself, mean “give Employee Portal.” That access is granted because the administrator configured this state to require that profile. Another configuration can use the same state name with different access requirements.

## Why can portal access return after someone removes it?

Suppose someone removes portal-use directly from the person's account in the portal application. The person remains in the active lifecycle state, and that state still requires Employee Portal.

The account has changed, but ISC's instruction has not changed. ISC still has a reason to provide the portal profile to this person.

Access profiles granted through a lifecycle state are enforced while that state applies. Later processing can generate provisioning work to restore the required access. Whether the account receives it successfully still depends on the connection and the result of that provisioning work. This does not mean the change is immediate.

If you are investigating access that returned, check the person's lifecycle state and whether it requires the profile. Then follow the recorded provisioning operation and the account result. This lets you establish whether the lifecycle requirement actually caused the restoration in the case you are investigating.

If the requirement is wrong, repeatedly removing the permission from the application leaves its cause in place. Find out which part is wrong: the employment information, the mapping or calculation that determines the state, or the profile selected in the state's settings. Have the authorized person correct that part, then check the resulting state and access.

For example, an incorrect employment-status value can lead ISC to assign the wrong state even when the mapping follows its configuration correctly. Changing a certification decision does not correct that incoming employment information.

The continuing enforcement described here concerns lifecycle-required access profiles. Enabling or disabling an account is a different lifecycle action. Those actions execute once; they do not continuously retry to keep an account enabled or disabled. Do not assume that every action configured in a lifecycle state behaves like its required profiles.

## Why might the portal profile be missing from a certification?

We now have two access profiles with different reasons for being assigned. Reporting Export came from an approved request. Employee Portal is required by the person's current lifecycle state.

An **assignment** connects access to the person who receives it. How that assignment came about is called its **assignment origin**. Here, one came from a request and the other came from a lifecycle state. Checking the origin helps you understand which process controls that access.

In these certifications, an access profile required by the person's current lifecycle state is left out of the review. Its entitlements are also not offered as separate review items while they are included in that required profile. The reviewer therefore does not get a separate Employee Portal item to approve or revoke in this example.

The requested Reporting Export profile can be included for review. As before, the reviewer decides about that package as a whole.

So the person can have working portal access without a separate portal profile item in the certification. An item missing from the review does not, by itself, tell you that the person lacks the access.

For an actual missing item, check why the access was assigned and what the campaign was configured to include. A lifecycle requirement is one possible explanation; do not assume it explains every missing item.

If the portal requirement is inappropriate, the investigation needs to reach the settings that require it and the information that puts the person in that state. A certification decision does not change those settings.

You may hear these packages and assignment rules described together as the **access model**. Here, the relevant part of the access model is the instruction connecting the active lifecycle state to Employee Portal.

## Put the three starting points side by side

The diagram follows an approved reporting request, a review of existing reporting access and the configured portal requirement. Each flow has its own starting point.

```text
Person needs reporting access
    |
    v
Reporting request is approved
    |
    v
Start adding report permissions

Person already has report access
    |
    v
Reviewer checks today's need
    |
    v
Decide whether to keep or remove

Person is in the active state
    |
    v
That state requires portal access
    |
    v
Start providing portal access
```

The last line of the request and lifecycle flows means that access-change work is initiated. To know whether access was provided, check the application's account. The certification flow ends with a decision; any required removal still needs to be carried out and checked.

These flows can all apply to the same person. Their active state can require portal access, a request can provide additional reporting access, and a later certification can check whether the reporting access is still needed. The flows are not three steps that every permission must pass through in order.

| Process | Question it answers here | What you check |
|---|---|---|
| Access request | Should the person receive the reporting access they asked for? | Who should receive it, what was requested, required approval and whether the account received it |
| Certification | Should the person keep the reporting access they already have? | What the review item contains, today's need, the review decision and confirmation, and any required removal result |
| Lifecycle-based access | What access should the person's current state provide? | The assigned state, the information used to set it, its required profiles and the resulting account access |

For a supported removal request, the first question changes to whether the requested access should be taken away. It is still a request for a change, rather than a periodic review decision.

## Use the problem to decide where to look

If someone says, “I need reporting access, but I don't have it,” first check how that access can be requested or assigned under the organization's process. If a request already exists, follow its approval and provisioning result. Approving an unrelated certification item will not supply the missing permission.

If someone says, “This access was approved six months ago, so approve it again,” ask what work requires it now. The earlier approval may have been correct. Today's review still needs today's reason for keeping it.

If someone says, “The portal permission returned after I removed it,” check the assignment origin and the current state's requirements, then verify the actual restoration work. Removing a permission and removing the reason ISC must provide it are different changes.

Finally, suppose someone suggests changing an active employee to an inactive state just to remove one project permission. First check whether that state would describe the person correctly. A lifecycle state can affect other access and account actions as well. Find the assignment responsible for the project permission, and use the appropriate process to address that access. Making the person's state inaccurate can introduce other incorrect access changes.

## Work through a different pair of permissions

A person has access to approve supplier invoices in a payments application. They received it through an approved request for an access profile named Invoice Approval. That profile contains invoice-approve, the permission to approve those invoices.

They also have Employee Portal access through their active lifecycle state. Its portal-use permission lets them use the employee portal.

The person is still actively employed and needs the portal, but their work no longer includes invoice approval. The reviewer has confirmed that invoice approval is no longer needed.

The campaign includes an Invoice Approval review item. There is no separate Employee Portal profile item. The account information and lifecycle state are correct, and no other assignment requires the invoice-approval permission.

Someone proposes approving Invoice Approval because its original request was approved. Someone else proposes changing the person to an inactive state to remove access.

What would you do instead? Explain which access should change, which information should stay as it is, and what would prove the change happened.

Start with Invoice Approval. The original request explains why the person received it. The reviewer has now confirmed that the person no longer needs it. These facts support Revoke for that review item, followed by review confirmation and the required removal work.

Next, check the lifecycle state. The person is still actively employed, so the supplied active state remains correct. Changing it to remove the invoice permission would make that information inaccurate and could affect other configured access. The invoice permission came from its separate request; address that access through the appropriate review and removal process.

The portal profile is required by the current state. That explains why it is not a separate profile item in this review. The missing review item does not mean the person's portal access is missing, and the supplied facts give no reason to remove it.

Finally, follow the invoice-removal work to the person's payments account. Confirm that invoice-approve has actually been removed. If all you have is a recorded Revoke decision, you know what the reviewer decided; you do not yet know that the account lost the permission.

Now change one fact: the reviewer finds that the person's current work still requires invoice approval. With that need established, Approve can be appropriate. The reason is the current work that needs the permission. The old request alone would not have answered that question.
