# How do you trace cloud access paths during a certification?

A reviewer removes a temporary project's cloud access. Later, the person can still read the production archive.

Did the removal fail?

First check which access was removed and how the person can still reach the archive. A cloud resource can be reachable through more than one entitlement. Removing one path does not establish that every path has gone.

## Start with the account, the entitlement and the resource

SailPoint Identity Security Cloud (ISC) keeps an **identity** representing a person. An **account** is their record in a system. A **source** is ISC's configuration for that system or its account information.

Our review concerns cloud-user-31 on the Cloud Production source.

The account belongs to Project-Archive-Readers. That group is represented in ISC as an **entitlement**, an access right from the source.

A **cloud resource** is something in the cloud that permissions allow someone to use, such as a database or storage bucket. Here, the resource is a production archive holding reporting files.

The cloud administrator confirms that Project-Archive-Readers permits reading that archive. It does not permit changing or deleting its contents in this example.

Keep the group and the archive separate. The group is the entitlement being reviewed. The archive is a resource that the group helps the account reach.

## Establish what the cloud detail represents

The **Cloud Enabled** flag identifies access related to cloud infrastructure. It is a reason to inspect the available detail, rather than a conclusion about the person's need.

**SailPoint CIEM**, Cloud Infrastructure Entitlement Management, provides information about effective access to cloud resources.

**Effective access** is what the account can actually do after the relevant grants and restrictions are considered. A group membership by itself does not explain every condition that may affect that result.

A **cloud access path** connects the account's entitlement with the groups, policies or other objects that supply access to a resource. A **policy** specifies which actions are allowed or denied on which resources.

The detail depends on collected cloud information and the account's entitlements. The administrator must connect the supported cloud provider and mark the relevant entitlement types as cloud enabled.

For this task, that setup is complete, CIEM is available, and the reviewer has the required access to its detail. Non-admin users need the applicable **Cloud Gov User** permission.

If the detail is unavailable, involve the responsible administrator to check capability, permission and data readiness. A missing cloud panel does not establish that the account has no cloud access.

## Open the detail for the item actually under review

A **certification campaign** organizes access reviews. A **certification** is an assigned review within it.

The reviewer opens **Certifications > Active** and selects the intended review. In this example, they are permitted to review somebody else's access, and the review has not been finalized.

Project-Archive-Readers is an independently reviewable entitlement here. It is not contained in a larger access package or controlled by another automatic assignment.

For a cloud-enabled entitlement, select **View Details** in the **Cloud Enabled** column. Inspect the resource information for the entitlement, then use **View Access** in the resource's **Access Paths** column.

Confirm the production archive's actual identity and cloud environment. A test archive can have a similar readable name while being a different resource.

In the path view, **Entitlement Path** shows the path from the entitlement under review. **All Paths** shows the paths across the identity's entitlements to the selected resource.

Those views answer different questions: how this reviewed entitlement reaches the archive, and whether another entitlement also reaches it.

Check which cloud account each path uses. Paths shown for the same person should not be treated as belonging to the same account without checking their details.

## Compare the two paths before deciding what removal means

Our current cloud information shows two paths for cloud-user-31:

Project-Archive-Readers supplies reading through the project policy.

Operations-Archive-Readers supplies reading through an operations policy.

The cloud administrator confirms that both paths currently allow reading this same production archive. The applicable policy conditions and restrictions have been checked; we are not assuming access from the group names.

The relationship looks like this:

```text
Same cloud account
        |
        +--> Project-Archive-Readers
        |      entitlement under review
        |              |
        |              v
        |        Project read policy
        |              |
        |              v
        |        Production archive
        |
        +--> Operations-Archive-Readers
               another entitlement
                       |
                       v
                 Operations read policy
                       |
                       v
                 Same production archive

Remove the project path:
  Project membership must be gone.
  Operations reading can remain through its own path.
```

**Entitlement Path** explains the project branch. **All Paths** reveals the additional operations branch to the resource.

The repeated archive label represents the same resource. We have two routes to it, not two different archives.

Also inspect what else the project entitlement reaches. A reason to read this archive would not justify a second production database if the same entitlement also grants that access. The decision must cover the actual entitlement's capabilities.

For our normal example, the confirmed project entitlement reaches only the archive described here.

## Connect the entitlement to current work

The temporary project has ended. The responsible business owner confirms that the person should no longer hold Project-Archive-Readers.

The person's continuing operations duty still requires reading the archive. Operations-Archive-Readers is the approved arrangement for that work.

Under those facts, removing the project membership while keeping operations reading is a sensible result.

The reviewer records **Revoke** for Project-Archive-Readers and explains that the temporary project ended. Revoke records that the reviewed access should be removed. It does not mean “remove every way this person can reach every resource.”

Complete and confirm the review through its finish/sign-off step. That final confirmation is separate from choosing a decision beside one item.

For the continuation of this example, the removal is due and an authorized operator completes the supported change on cloud-user-31. The project group membership is removed.

## Verify the expected result at the account and resource

Check the current cloud account and its membership. Project-Archive-Readers must be absent.

Then use cloud permission and path information collected after the change. Compare it with the current cloud configuration for the production archive.

The project branch should no longer supply the reviewed access. Operations reading should remain through its separate, still-authorized path.

An old path display can disagree with a completed cloud change because it describes an earlier observation. Check when the displayed data was collected before reporting that the removal failed or that the path is already gone.

For this example, the current account and policy checks confirm the project membership is gone and operations reading remains. The newly collected cloud information agrees.

Keep that result precise: the temporary project's entitlement was removed; the separately authorized operations access remains.

The same observation would not satisfy a different requirement to remove all archive access.

## When all access to the archive must end

Now suppose the person also leaves the operations duty. There is no continuing authorization to read the archive.

Removing Project-Archive-Readers still addresses only that entitlement. The operations path needs its own accountable removal work.

Identify the assignment or cloud configuration supplying that path and involve the owner and operator authorized to change it. If it is outside this campaign, record and follow the additional work through the appropriate process.

Do not alter a shared policy without checking its effect on other people and resources. A policy can serve more accounts than the one under review.

To establish that archive access has ended, check the account's current effective permissions across the relevant paths and restrictions. An authorized cloud administrator should also confirm, through the approved verification process, that this account can no longer read this production archive.

A successful change to one membership is evidence for that change. It is not proof that the wider no-access requirement is complete.

## Keep the review decision attached to its actual item

An **access profile** bundles entitlements from one source. If the review item is a profile, the reviewer can open it and inspect a cloud-enabled entitlement inside it.

That inspection helps explain the package. It does not make the cloud resource or each displayed path a separate certification decision.

Likewise, inspecting another entitlement in cloud details does not establish that it was included in this campaign.

Before acting, return to the actual item presented for a decision. If only part of a package should remain, involve the responsible access owner to establish an authorized narrower arrangement. Do not assume the cloud detail screen automatically splits the package or grants replacement access.

## Read cloud activity within its actual coverage

Cloud details may include **Last Accessed** and **Last Activity** information. Where supported, these describe the last resource access and the kind of activity, such as reading, writing or administration.

The activity detail has coverage limits. Last-access and activity dates are displayed for AWS resources that write to **CloudTrail**, the AWS activity-recording service. Some source records can also lack the resource information needed for full activity detail.

An empty date is therefore not proof that the resource was never used.

Even a verified read yesterday would not establish that the person's authorization continues today. Use activity to clarify what happened, and current work evidence to establish what should remain allowed.

## Try a similar-looking resource

A review concerns the production archive. Someone opens a path view for a test archive with the same readable name and sees no recent activity.

They propose approving the production entitlement because “only the test archive is reachable.”

Check the resource identifier and environment first. The test resource's paths do not establish the production entitlement's scope.

Then inspect the entitlement's actual production paths and permissions. Missing activity in the test view answers neither whether production access exists nor whether it is still required.

The useful explanation connects the reviewed entitlement, the correct account, the actual resource, its permissions and the person's present authorized work.
