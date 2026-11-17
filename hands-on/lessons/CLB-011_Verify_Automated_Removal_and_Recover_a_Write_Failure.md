# Verify automated removal and recover a write failure

A reviewer has rejected a group membership and finished the review. Has the membership actually disappeared from Active Directory?

To answer that, we need to follow the write operation and inspect the directory itself. A completed review and a completed directory change are different results.

A **certification** is an assigned access review, and a **campaign** organizes those reviews. **Sign-off** is the reviewer's final confirmation of the decisions.

We'll first observe a normal removal. Then we'll block the connector's ability to change one group's membership. After inspecting the failure, we'll restore that ability and check whether ISC will try again or needs a new removal instruction.

## Use a real connected training source

**Active Directory**, or AD, is Microsoft's directory service. It stores objects such as user accounts and security groups. A group has a list of members. Adding a user to that list gives the user a **direct membership**; removing the user from the list removes that membership. We will check those lists, without using groups nested inside other groups.

The groups below are isolated test objects. Their names do not establish that they grant reading or exporting in a real reporting application. Removing one membership also does not prove that every downstream permission or existing user session has changed.

Use these actors:

- An authorized ISC administrator to prepare campaigns and inspect operations.
- `certlab-manager01`, with a working reviewer session.
- An authorized AD administrator who can prepare the test objects and change permissions on the one fault group.
- The connector's technical account, whose AD permissions allow the integration to change membership. This is separate from the employee account being reviewed.

Your ISC administrator role does not supply the technical identity's AD permissions.

Use source `certlab-ad-lab`, called **C** below. A **source** contains the integration settings and collected account data. Its **connector** communicates with AD. Use **Direct Connection** so the integration can read AD and perform supported changes there.

Keep C **non-authoritative**: its accounts will be linked to people who already have ISC identities. The people CSV remains the **authoritative source**, supplying the records used to build those identities. We are adding AD accounts to those people, rather than creating another set of people from AD.

The existing CSV review sources are **A**, `certlab-reports-csv`, and **B**, `certlab-owner-reports-csv`. Leave both unchanged throughout this exercise.

Before starting, you need an actual training AD environment, prepared integration components and authorized AD access. The connection checks below use those prepared components. An ISC administrator role alone does not provide them. A flat-file source or an edited CSV cannot demonstrate this directory write.

## Prepare the four scoped memberships

In the approved training directory, use a dedicated organizational unit called `ISC-CertLab`. An **OU** is a directory container that lets you keep the test objects together.

In **Active Directory Users and Computers**, create the OU under the approved training parent if it does not already exist. Inside it, prepare two ordinary user accounts and three ordinary security groups.

Use the account logon names `certlab-ad-e01` and `certlab-ad-e02`. Keep credentials in the approved private setup, outside the course files.

Enable **View > Advanced Features**. In each user's properties, use **Attribute Editor** to set `employeeID`:

- e01: `certlab-employee01`.
- e02: `certlab-employee02`.

These values will connect the AD accounts to existing ISC identities. The AD logon name does not have to equal the ISC identity name.

Create ordinary, non-nested Global security groups with the full names below. We will use three shorter labels while following the operations:

- **Read** means `certlab-ad-read`.
- **ExpOK** means `certlab-ad-exp-ok`, the group for the normal removal.
- **ExpFail** means `certlab-ad-exp-fail`, the group for the blocked removal and recovery.

These labels refer to the same three groups, not additional objects. Use their **Members** tabs to establish the starting set:

| AD account | Existing ISC identity | Direct test-group memberships |
|---|---|---|
| `certlab-ad-e01` | `certlab-employee01` | `certlab-ad-read` and `certlab-ad-exp-ok` |
| `certlab-ad-e02` | `certlab-employee02` | `certlab-ad-read` and `certlab-ad-exp-fail` |

Use the same group names as their SAM account names. The AD attribute `sAMAccountName` is the short account or group identifier. Keep these groups separate from primary, privileged, protected or built-in groups.

We count four direct memberships among these three test groups. This is not a claim that the users have only four directory permissions. Leave their unrelated built-in memberships outside the exercise.

The planned values are also recorded in `lab-data/baselineC/expected_memberships.json`. It is a setup specification, not an import file or an actual AD export.

Record the actual object identifiers and **distinguished names**, or DNs, privately. A DN identifies an object's directory location; the short name alone is not enough to distinguish similarly named objects.

## Check the connection, correlation and write authority

**Provisioning** means changing access on the connected system. Here, the change is removing one user from an AD group's membership list. We need both a working connection and permission to make that change.

If the isolated source has not been prepared, open **Admin > Connections > Sources > Create New**, select Microsoft Active Directory and configure `certlab-ad-lab`.

Use **Direct Connection** with the actual prepared Virtual Appliance cluster. A **Virtual Appliance**, or VA, runs the connector communication in the connected environment.

Use the prepared AD connection details: the actual directory forest/domain, connection credentials and TLS settings that protect the connection. **IQService** is a Windows service used by the AD connector for provisioning. The connector requires it for provisioning, so verify its installation, connection settings and permissions for this training setup. Do not substitute invented endpoints or copy connection values from another domain.

Restrict user and group search scopes to the test subtree. Inspect the group-membership search scope as well. Set `certlab-manager02` as the **source owner**, the person responsible for the source in ISC. Keep the source non-authoritative.

In **Base Configuration**, verify **Enable Provisioning** is enabled for this isolated source. The connector starts with provisioning disabled; a successful connection does not by itself establish that writes are enabled or allowed.

Ensure AD `employeeID` is collected. Under the source's **Account Management > Account Correlation**, match account `employeeID` to identity **Identification Number** (`identificationNumber`).

**Account correlation** links an account to its person. Here, e01's `employeeID` value `certlab-employee01` must match that person's Identification Number in ISC; check e02 in the same way.

An **entitlement** is an access value ISC can govern. For AD groups, use the actual collected group objects and values, not the CSV reporting entitlements with similar names.

**Aggregation** reads current data from AD into ISC. Run the source's entitlement and account aggregations to collect the groups, accounts and memberships. Inspect the actual account-to-person links and all four test memberships. Reading those values successfully does not prove that the connector can change them.

Both employee identities must retain their existing manager01 relationship. Use memberships that are not automatically granted or restored by a role, access profile, lifecycle setting or another process. Otherwise a separate rule could add a membership back after our removal and confuse the test result.

AD checks the permissions of the security identity making a change. That identity is called the **principal**. Record the actual principal used for membership writes by inspecting the configured connection and service accounts. When another service participates, do not assume the write always uses the same account as the directory connection.

The AD administrator must verify its normal permission to read and change membership on the two removable groups. AD stores a group's members in its `member` property. Preserve the baseline permissions for later comparison.

A holding means one account having one entitlement. Keep CSV source A at five holdings and B at six. Neither source is changed in this exercise.

## Prove one ordinary removal first

The supplied review instruction is to retain both users' Read membership and remove their other test membership. Start with e01: retain `certlab-ad-read` and remove `certlab-ad-exp-ok`. Later, we will apply the same instruction to e02's Read and ExpFail memberships.

As ISC administrator, open **Search > Certification Campaigns > New Campaign > Identities > Using a Search Query > Specific Identities that I Select**.

Find `certlab-employee01` with:

```text
name.exact:"certlab-employee01"
```

Inspect the actual identity, select it and use **+ Add To Campaign**. Check **Added to campaign**, then select **Certify Selected Identities**. Under **Refine Access Items**, add only C's Read and ExpOK group entitlements and inspect the added access list.

Name the campaign `certlab-011-normal-run01`. If a supplied run name already exists, use an unused run suffix and record it; preserve earlier review history. Select **Manager** so the employees' recorded manager receives the review. Use a future due date and **Maintain** for undecided access, so a missing decision does not instruct removal. Use the approved training comment/notification settings. Leave extra filters and recommendations off.

A saved **template** holds campaign settings. A **preview** is the generated review work you inspect before releasing it to reviewers. Save this template without a future schedule and generate its preview immediately. Record the template and generated campaign references separately. Check exactly two intended memberships and manager01's assignment before **Start Campaign**.

In manager01's **Certifications > Active** session, approve Read and revoke ExpOK based on the supplied need. Record a removal reason identifying the group membership and the retained Read membership.

Check the choices and use **Finish** for every actual assigned certification. Record final confirmation rather than treating a saved choice as sign-off.

**Remediation** is the work that carries out the review's required change. Follow it across these stages:

1. The reviewer finalizes the removal decision in ISC.
2. ISC sends the required change through the connected provisioning path.
3. The connector authenticates to AD under its technical identity.
4. AD checks that identity's authority and changes the target group's membership.
5. The operation result returns; a later collection can reconcile ISC's account data.

Those are different places to inspect. The review page cannot replace the directory observation.

Open **Admin > Identity Management > Activities**. Find the actual certification-related change and inspect the source, e01 account, group value and removal operation. Record its ID, times and detailed result.

You can also use **Search > Reports > Provisioning Activity** to inspect the matching event.

If the result is a manual task instead of a connector write, inspect the source, provisioning enablement and fulfillment configuration. That is not the automated outcome being tested here. Do not perform a manual group edit and label it automatic removal.

In AD Users and Computers, inspect ExpOK's **Members** on the domain controller used for the write. Confirm e01 is absent, e01 remains in Read and e02's two test memberships are unchanged.

Record the controller and observation time. If another controller is used, account for replication before concluding the write succeeded or failed.

Aggregate C and compare the current ISC account data. Three scoped memberships should remain. Do not proceed to the fault until this normal connector-mediated removal has been proved.

## Block only one group's membership write

Look at two different questions about ExpFail. Its **Members** list says whether e02 belongs to the group. Its **Security** settings say who may change that list. We will leave e02 in Members while preventing the connector from editing that group's membership.

AD stores the membership list in the group's `member` property. The permission to edit it is **Write Members**. An **access-control list**, or ACL, holds the object's permission entries. Each **access-control entry**, or ACE, allows or denies an operation for a particular principal.

We will add one Deny entry for the actual connector write principal, covering only the `member` property of `certlab-ad-exp-fail`. Keep reading allowed. This lets ISC continue collecting the group while its attempt to remove e02 is blocked.

As AD administrator, record that group's existing security entries and the principal's effective permissions. Record the actual principal identifier, group DN, controller and time.

On that group only, open **Properties > Security > Advanced > Add**. Select the exact effective write principal, choose **Deny** and scope the entry to **This object only**.

Select only **Write Members**, the write permission for the group's `member` property. Inspect the resulting entry before applying it. If the actual interface cannot isolate that property, principal and object scope, do not substitute a broader Deny.

Keep inheritance, read permissions, other principals and other properties unchanged. Do not place the fault on the OU, change a shared credential, stop the VA or IQService, or disable provisioning to manufacture an error.

Reopen the security settings and verify the one added entry. Check effective member-write denial while the group can still be read.

The exact entry you added is what you will remove. A saved baseline is evidence for comparison, not an instruction to overwrite unrelated later permission changes.

## Capture the failed removal

Create `certlab-011-fault-run01` using only employee02 and C's Read plus ExpFail entitlements. Use the same Manager and preview-first settings.

Check the current account, both memberships and reviewer. Start the checked campaign.

Manager01 approves Read, revokes ExpFail with a reason and finalizes all actual assigned work.

Inspect the exact e02/ExpFail account request in **Activities**, including its error and operation result. The expected fault is a membership write denied on the one group. Record the actual message; do not substitute a sample error string.

Check AD directly. ExpFail should still contain e02, and Read should still contain both users. The scoped membership count stays three.

A successful write would mean the planned fault did not take effect. An unrelated connection or authentication error would be a different fault. Preserve what actually happened and investigate that cause rather than label every failure a passing result.

Do not remove e02 manually from AD to make the account check pass. That would change the outcome from automated recovery to manual remediation.

## Read the account request, not just the headline

An activity can contain several account or attribute results. Inspect the exact source/account/group removal rather than rely on an overall campaign label.

Important account-request states include:

| State | What it tells you |
|---|---|
| Pending or Committed | Work is in progress or has been sent; establish the eventual result. |
| Retry | The attempt failed and another attempt is scheduled. |
| Failed | The action failed and will not be retried through that request. |
| Finished | A result was returned; inspect whether it reports success or failure. |

A “finished” label without the detailed result is insufficient evidence of successful removal.

ISC retries errors it recognizes as retryable. A permission error is not automatically entitled to the same handling as a temporary connection problem. Inspect the actual classification.

Do not look for a universal Retry button or change retry-error configuration to turn this exercise into a different one.

## Restore authority before choosing the recovery action

On ExpFail's security settings, remove only the explicit Deny entry added for this run. Compare with the saved baseline and verify the connector's effective membership-write authority has returned.

Leave the user in ExpFail while establishing what ISC will do next. Restoring authority did not itself remove the membership or resubmit the request.

If the exact operation is in **Retry**, follow that existing work after the permission correction. Do not create a second removal while it is pending. Inspect its actual attempt/result and the AD group.

If it is still pending or its outcome is uncertain, establish that outcome before issuing anything else.

If the request is **Failed** and has no pending or scheduled attempt, it will not try again through that request. Use a fresh explicit removal instruction. In this lab, prepare `certlab-011-recovery-run01`:

- Collect and verify that e02 still holds ExpFail.
- Select only `certlab-employee02` and only C's ExpFail entitlement.
- Keep Manager as reviewer and reference the original campaign/activity failure in the description and review reason.
- Inspect the one-holding preview, start it and have manager01 reaffirm Revoke and Finish.
- Track the new connector operation and inspect the actual AD result.

This is a new, traceable corrective review. It is not an edit of the old signed review or a retry of the same failed operation. Preserve the original error as failed history and link the successful new work to it.

If a supported fresh preview or operation cannot be established, retain recovery as incomplete. Do not claim a manual group edit or a changed status field established connector recovery.

## Verify the result and the rights that remain

After a successful retry or the new corrective operation, e02 must be absent from ExpFail. Both users must still be direct members of Read, and e01 must remain absent from ExpOK.

Check the actual target first, then aggregate C and reconcile current ISC records. Compare the rejected memberships as well as those deliberately retained.

The scoped counts should follow this sequence:

| Point in the exercise | Direct memberships among the three test groups |
|---|---|
| Original | Four |
| Normal ExpOK removal succeeded | Three |
| ExpFail write was denied | Three |
| Recovery removed ExpFail | Two, both Read |
| Training reset after outstanding work is resolved | Four |

Keep the original operation error, permission restoration and successful recovery result together. Record whether recovery was an existing retry or a new operation. Their identifiers and explanations should not be made interchangeable.

If ISC and AD disagree, preserve both observations and their times. A new collection reads the directory; it does not prove that the earlier write occurred.

## A successful read is not a successful repair

The source can aggregate accounts while the narrow member-write permission is denied. Someone therefore concludes that the connector is healthy and marks the failed removal resolved after restoring the ACE.

What is still missing?

<details markdown="block">
<summary>Compare your reasoning</summary>

Reading the group and changing its membership require different authority. The successful aggregation did not prove that the write was permitted.

Removing the Deny allowed the connector to write again. It did not tell ISC to repeat an operation already marked Failed with no further attempt. Inspect whether work is pending or retrying, or whether a fresh explicit removal is required.

Then establish the actual connector-mediated removal, retained Read memberships and refreshed ISC account data. A configuration repair, successful operation and reconciled target state are separate facts.

</details>

## Reset after earlier removals are resolved

Preserve the campaigns, final choices, operation details, target observations, actual errors, ACL comparison and recovery references. Keep signed history, including the original failed operation.

Confirm all review work is finalized and no pending, retrying or queued removal remains for these memberships. A deleted campaign is not proof that outstanding writes were cancelled.

Confirm the added Deny is absent and the effective permissions match the approved baseline.

Only then should the AD administrator restore the two original test memberships through the groups' **Members > Add** controls: e01 to ExpOK and e02 to ExpFail. Retain both Read memberships.

This restoration is a deliberate training reset after recovery, not the automated-removal proof.

Aggregate C and verify all four scoped memberships and original correlations. Check CSV A still has five holdings and B six; neither file needs an edit.

Retain the isolated AD source, OU, users and groups as the native baseline for later work. Remove only unused 011 unscheduled templates if retiring the saved configurations. Do not delete accounts or the OU as routine reset.

If an operation, fault entry or setting cannot be accounted for, record the outstanding work and responsible person before ending the run. The automated outcome passes only when the real write, failure, correction and target evidence have all been established.
