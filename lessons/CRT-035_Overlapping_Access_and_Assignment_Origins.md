# Why can access remain after one assignment is revoked?

A requested access profile has been revoked. One of its permissions is gone, but another permission is still on the account.

That result can be correct. The remaining permission may also be required by a role that the person still holds.

The useful question is not just “Was something revoked?” We need to know which assignment was removed, which account permission we are checking and whether another assignment still requires it.

## Start with the account and its permissions

SailPoint Identity Security Cloud, or **ISC**, maintains an **identity** representing a person. An **account** is a record in an application through which that person can use it.

Identity 5501 owns `doc-5501` in Documents Production. ISC manages information about this application through a **source**, its configuration for the system and its account data.

The account has two **entitlements**, rights represented from the application:

- `DOC_READ`, displayed as **Read Documents**, permits reading documents.
- `DOC_EXPORT`, displayed as **Export Documents**, permits exporting documents in bulk.

The current job requires reading, but bulk export is no longer authorized. We want `DOC_EXPORT` removed from this account while `DOC_READ` remains.

Before choosing how to achieve that, let's find out why the account has those permissions.

## Follow the packages that supply the access

An **access profile** bundles entitlements from one source. In this case, a profile called Document Reading contains `DOC_READ`.

A **role** groups access for a business function. The role Document Staff includes the Document Reading profile.

ISC assigns Document Staff automatically when the person's department matches Operations. The configured condition is a **membership criterion**. The person's current department is correctly recorded as Operations, so they meet it.

This gives us one connection:

Document Staff role → Document Reading profile → `DOC_READ` on `doc-5501`.

There is also a second profile, Document Export. It contains both `DOC_READ` and `DOC_EXPORT`. The person previously requested this profile through an **access request**, a request to obtain access. That request was approved and the access was granted.

The requested profile gives us another connection:

Document Export profile → `DOC_READ` and `DOC_EXPORT` on `doc-5501`.

An **assignment** associates the person with an access object such as that profile or role. **Assignment origin** describes how the person obtained it, such as an approved request or an automatic rule.

We can call each connection a **grant path**: the assignment and package relationships through which a permission is supplied. Following the path helps us identify which assignment is supplying the right.

Here, `DOC_READ` is a **shared entitlement** because both paths include the same right on the same source account. That does not mean the application needs two separate copies of the read permission. It means we found two reasons in the configured access model for this account to have it.

The **access model** is the collection of configured packages and assignment requirements. The account's actual permission and the model's reasons for supplying it are connected, but they are different information.

## Remove the requested profile and preserve the required reading

A **certification campaign** organizes access reviews. A **certification** is an assigned review within it.

In this case, Document Export was requested separately, independently of Document Staff. Its origin has been checked, and it is eligible for review as an access profile.

The reviewer understands the profile, has permission to review it and is reviewing somebody else's access. The person no longer needs its export capability, so the reviewer selects **Revoke**, recording that this reviewed access should be removed.

The review is signed off, meaning the decisions are finalized. Its removal work is due. Current account information and the person/account association are correct.

For the supported role-and-profile case here, access required by an assigned role is retained when a separately assigned access profile is revoked. Document Staff still requires `DOC_READ`. It does not require `DOC_EXPORT`, and no other assignment requires export in this example.

The intended outcome is therefore precise: remove the requested Document Export assignment and its unneeded export permission; retain reading through Document Staff.

**Provisioning** carries out account or access changes in the application. **Remediation** is the work needed to carry out the review's removal decision. Inspect the actual work and the account outcome rather than expect every entitlement named inside the revoked profile to disappear.

Suppose the supported removal finishes, the requested assignment is removed and a current application check shows `DOC_EXPORT` absent while `DOC_READ` remains. These example results fit the requirement. Reading still being present is not evidence that the export removal failed.

The diagram shows the two paths before removal. Its arrows represent assignment and package relationships, not the order in which internal services execute.

```text
Identity 5501: doc-5501 on Documents Production
                         |
       +-----------------+------------------+
       |                                    |
Automatic role: Document Staff       Requested profile:
       |                            Document Export
       v                                    |
Profile: Document Reading                   |
       |                                    |
       +------ DOC_READ <-------------------+
                                            |
                                       DOC_EXPORT

Revoke the requested Document Export profile.
Document Staff still requires DOC_READ on this account.
Check the result: DOC_EXPORT absent; DOC_READ retained.
```

Here, **effective access** means the permissions the account actually retains through the relevant paths and the application's own access controls. Removing one assignment does not establish that every permission associated with it must disappear.

## Check that the shared right really is the same right

A matching display name is not enough to establish overlap.

Read Documents in Documents Test may be a different entitlement from Read Documents in Documents Production. Likewise, `DOC_READ` on a person's administrator account belongs to that account. It is not the permission held on `doc-5501`.

Check the source, account, entitlement type and identifying value. For example, a group membership with one value is not interchangeable with another kind of permission merely because both are displayed as Read Documents.

A second path on another account does not establish that this account's permission should remain.

Also check the assignment rather than only the package definition. A role may contain the right, but that fact alone does not show that this person holds the role or that its access applies to the account being examined.

An authorized administrator can inspect the identity's Access information, the assigned roles/profiles and their details. For roles, assignment details include associated accounts. Connect those records to the actual role or profile contents and the source account.

## Do not apply one overlap rule to every situation

The ordinary example used access required by a role alongside a separately requested profile.

Two independently assigned access profiles are a different situation. Do not promise that their shared entitlement will always be protected merely because both profiles contain it. Establish the supported behavior for the exact removal path, assignment origins and campaign implementation before planning the outcome.

For example, profile A might contain Read and Export, while profile B contains Read and Update. The shared Read permission matters to the user's remaining work. A plan that only says “remove A” has not yet established whether that removal will preserve the required reading in this particular process.

Confirm which assignments and permissions should remain, verify the supported handling and inspect the actual result. Arrange any necessary approved access change explicitly; do not assume ISC will create a replacement read-only package automatically.

A profile can also be **detected** because ISC recognizes that the person already has its required entitlements. A detected profile is not proof that a request for it was approved in the past. Inspect the actual origin instead of treating every profile label as the same kind of grant.

Overlap is a reason to examine the relationships. It is not a universal entitlement-retention guarantee.

## What if the remaining role is no longer justified?

In the main example, Document Staff is still appropriate. Now change that condition: suppose the person's current work no longer justifies that role.

Selecting Revoke on Document Export does not change the rule assigning Document Staff. Its membership criterion still matches the person.

Roles assigned automatically by membership criteria are reviewed using **Acknowledge**. That action examines the access; it does not override the assigning rule. Roles obtained through an access request can instead be approved or revoked through the supported review path.

If the department data is wrong, correct it through the responsible data process. If Operations is the true department but the rule grants too much access, the assignment policy needs an approved correction. Do not invent a false department merely to make a criterion stop matching.

An **attribute** is a named piece of information, such as department. Changing that information can affect other access decisions, not just this review.

**Identity processing** evaluates identity information and the applicable access configuration. It can change assignments and initiate corresponding provisioning. A model correction therefore needs processing and actual account/result checks; saving the rule is not the same as proving that the application access changed.

Equally, do not assume that every manually removed entitlement is automatically restored on the next daily run. Identify the actual assigning mechanism and subsequent work. Automatic role membership and every possible account-permission change are not one universal repair process.

## Lifecycle states are another source of required access

A **lifecycle state** is a configured business stage, such as Active or Leaver, that can drive access behavior.

An Active state might grant a Base Access profile. Profiles granted by the person's current lifecycle state do not appear as independently reviewable profiles in certifications. The state is controlling that access.

Those lifecycle-state profile assignments are enforced while the state applies. If such a profile is removed from an identity that remains in the state, the access is provisioned again. This is a specific lifecycle behavior; it is not a promise about every kind of manual permission removal or its completion time.

When investigating remaining access, inspect the current state and the profiles it requires. Removing a separately requested package does not establish that the lifecycle configuration stopped requiring the same capability.

Use the person's true business status and the approved access policy. Setting a current employee to a leaver state solely to remove one permission could affect many accounts and other justified access.

## A package edit is different from an assignment removal

An assignment connects a person to a package. A package definition states what the package contains. Changing the shared definition can affect many people.

If the issue is one person's unneeded requested profile, do not treat a global package edit as the same action as removing that person's assignment.

Suppose a role contains an Export entitlement, and its owner removes Export from the role definition. The package now describes less access, but what should happen to members who already received Export?

Check **role access removal propagation**, the feature that controls removal after certain role content changes. For this supported change to an enabled role, enabling the feature allows processing to initiate deprovisioning, work to remove the existing entitlement. With propagation disabled, editing that content does not remove the previously granted entitlement.

Check the feature configuration, role state, actual change and processing result before explaining what happened to an existing member's account.

This is a configuration fact to establish, not a setting to switch casually to resolve one review. Confirm the intended affected population and the retained access before a model change, then verify its actual result.

A saved role definition, the person's current assignment and a source-account permission are three different things to inspect.

## Explain the remaining access before choosing a correction

Start with the exact requirement. In the main case, success meant export removed and reading retained. Losing both permissions would have removed justified access.

Then connect the evidence: what was finalized, which assignment changed, which other requirements still apply, what work ran and what the correct account now holds.

**Account aggregation** reads source-account information into ISC. An old collection can still show a permission that the application has already removed. Compare times before concluding that the permission remained or was granted again.

Likewise, present access does not identify its cause on its own. It could be supported retained access, another continuing requirement, incomplete removal or older information. Use assignment, configuration and operation evidence to distinguish them.

## Try a continuing lifecycle requirement

Account `case-5601` in Support Production holds `CASE_READ`, permission to read cases, and `CASE_EXPORT`, permission to export case records.

The person has a separately requested Case Export profile containing both rights. Their Active lifecycle state also grants a Case Base profile containing those same two rights.

Current business need justifies reading only. The data and account association are correct, and an authorized independent reviewer finalizes Revoke for the requested Case Export profile. The removal is due.

In this example, take the following as checked results: the requested assignment has been removed, the current account still holds both rights, and the current lifecycle configuration still requires Case Base with both rights.

Can we say that all requirements for export have been removed?

No. The requested assignment is gone, but the lifecycle configuration still requires export. Its existence needs attention before claiming the desired access outcome. These supplied results are not a general rule predicting the outcome of every lifecycle/profile overlap.

The next action is to establish an approved arrangement that keeps justified reading without requiring export. That may involve correcting the relevant lifecycle access configuration and its affected scope. It does not follow that the person's true lifecycle state should be changed or that a narrower replacement has already been granted.

Follow the approved change through processing, any required provisioning and the actual account result. If the application still has export afterward, inspect that work and the remaining paths rather than assume a review label settled the matter.

Now change one fact: the current application account no longer has `CASE_EXPORT`, but ISC still shows account data from a file exported before the removal. The older display is not proof that another assignment has restored export. Check the current account and collection evidence first.

The question to carry into everyday work is: which requirement still supplies this permission to this account, and what evidence shows the change we actually needed?

