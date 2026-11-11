# Why does some access appear differently or not appear at all?

You check an application account and find that it can export reports. Then you open the access review and cannot find a separate export item.

Has the review missed that permission?

It may have. But first, look at how the person holds the access and what the campaign was created to review. The permission might be included in a larger package. A rule might control it automatically. It might have been excluded from this campaign, or added after the information used for the review was collected.

Let's follow those possibilities so that the next check comes from the evidence you have.

## Begin with the account and the review item

An **account** is a record used to access an application or system. Its **access** determines what someone using that account can do.

SailPoint Identity Security Cloud (**ISC**) keeps an **identity** representing the person and connects it with their accounts. A **source** is the configuration in ISC for the system or collection of account data being managed.

An **entitlement** represents an access right from a source. In the reporting application, reports-export allows exporting reports. We know that meaning from the application's access configuration.

Now consider the review. A **certification campaign** organizes access reviews. A **certification** is an assigned review within that campaign, and the **reviewer** is the person responsible for assessing it.

Inside the assigned review, a **review item** presents access for a decision. The item may represent one permission or a package containing permissions.

So finding reports-export on the application account gives us a starting fact: that account has export access. We still need to establish what ISC collected, whose account it is and how that access should appear in this particular review.

## A permission can be reviewed through its package

Suppose reports-view allows viewing reports. ISC includes it in a package called Reporting Read.

An **access profile** is a named bundle of related entitlements from one source. Here, Reporting Read is the access profile, and reports-view is its included permission.

The person asked for Reporting Read through an access request, and the request was approved. The review presents the Reporting Read profile.

When you inspect that profile's contents, you find reports-view. The viewing permission is being considered through the package. You should not expect an additional independent entitlement decision for the same contained permission.

ISC calls this containment **encapsulation**. The permission is inside the access object through which it is managed for the review. Its absence as a separate item does not mean that it has been removed from the account.

A profile can also be **detected**. Where detection applies, ISC recognizes that the person already holds the entitlements making up the profile and associates the profile with their identity. That recognition does not establish that a new permission was just added to the application.

Requested and detected profiles can be reviewed. A profile appearing in the item list therefore does not prove that the person submitted a request for it.

## A role can contain the profile

A **role** groups access for a responsibility or purpose. It can contain access profiles, direct entitlements, or both, from one source or multiple sources.

Suppose Case Read is a profile containing cases-read, which allows reading cases. The person received Case Read through a role called Case Reader.

The review can present Case Reader as the role item. The Case Read profile and its cases-read permission are included through that role. They do not become separate individual decisions just because each has its own name.

This is why you need the **assignment origin**, meaning how the person received the access. Looking only at the permission name does not show whether it came through a requested profile, a role or an automatic requirement.

Inspect the actual role and profile contents. A role can include access to more than one system, so its name alone does not establish all the permissions involved.

## An automatic role has a different action

Now suppose Case Reader is assigned automatically through **membership criteria**. These are configured conditions that determine who should receive the role.

For example, a criterion can require the person's work-function value to match the work responsibility covered by Case Reader. ISC evaluates the person's information against that configured requirement. The rule controls the assignment.

In the certification, a role assigned through automated membership criteria can only be reviewed with **Acknowledge**. This records that the reviewer examined the automatically controlled access. It does not override the rule or ask ISC to remove the role.

A requested role has different supported actions. **Approve** accepts keeping the reviewed access. **Revoke** records that the reviewed access should be removed. The required review confirmation and actual removal work are separate from selecting that decision.

If Case Reader appears with Acknowledge, inspect its assignment origin before treating the absence of Revoke as a fault. Under automatic membership criteria, that is the supported review action.

If the role is inappropriate, investigate whether the person's information is wrong or the configured requirement gives them the wrong access. Correcting the relevant data or rule requires proper authority and checks of the resulting access. Acknowledge does not make that correction.

## Some access is required by a lifecycle state

A **lifecycle state** is a configured stage in the person's relationship with the organization. For example, an active employment state can require access needed while the person is active.

Suppose that state requires an Employee Portal access profile. The profile contains portal-use, which allows using the employee portal.

Profiles included in the person's current lifecycle state do not appear individually in certifications. The contained portal-use permission is not offered as a separate entitlement decision to bypass the requirement.

The access can still be present on the portal account. The absence of an individual review item follows how it is required.

That does not establish that the requirement is appropriate. If it looks wrong, check whether the person is in the correct state and whether that state's configured access matches the intended policy. An authorized administrator needs to correct the state information or access configuration that is actually wrong, then check the resulting access.

## Follow four permissions into one review

Consider one person's reporting, case-management and portal accounts. All three are correctly linked to their identity. ISC's collected account information accurately shows these permissions:

- The reporting account has reports-view and reports-export, allowing viewing and exporting reports.
- The case-management account has cases-read, allowing reading cases.
- The portal account has portal-use, allowing use of the employee portal.

Now follow how the person holds each permission.

They requested Reporting Read, which contains reports-view. Their reports-export permission is held individually, outside a profile or role, with no automatic requirement keeping it.

Case Read contains cases-read and comes through the automatically assigned Case Reader role. Employee Portal contains portal-use and is required by the person's current active lifecycle state.

The campaign selects the person and the eligible example access. No campaign setting excludes those reviewable items. An appropriate reviewer has the assigned review, is not reviewing their own access and has permission to decide while the review is active and open.

With those facts, compare each permission with what the review presents:

| Permission held by the account | How the person holds it | Expected item and action |
|---|---|---|
| reports-view | Requested Reporting Read profile | Reporting Read profile, with Approve/Revoke |
| reports-export | Individual entitlement outside packages and automatic requirements | reports-export entitlement, with Approve/Revoke |
| cases-read | Case Read profile through criteria-assigned Case Reader | Case Reader role, with Acknowledge |
| portal-use | Employee Portal profile required by the current lifecycle state | No individual Employee Portal profile or portal-use entitlement item |

Here, four permissions lead to three review items: Reporting Read, reports-export and Case Reader.

The numbers follow these particular assignments. Another set of packages, people or campaign selections can produce different counts.

More importantly, the three items do not mean that every access requirement has received an individual decision. The lifecycle-state requirement for the portal remains outside those individual decisions.

To check whether the campaign contains what it should, identify the expected packages and permissions first. Then compare them with the generated items. Counting account permissions and review rows alone cannot establish that the intended access is covered.

## A filter can deliberately leave access out

The campaign's **scope** is the people and access it is intended to assess. The administrator selects its contents and can use a **campaign filter** to include or exclude people or access according to configured conditions.

Change one fact in the example. The campaign now applies an entitlement exclusion for reports-export.

The reporting account still has export access. ISC has collected it correctly, and the entitlement can be reviewed individually. The campaign excludes it because of that filter.

This explains the missing review item. It does not establish that the application permission was removed.

It also does not establish that the campaign's scope is right. If the business requirement was to review export access, excluding it would leave that requirement unmet even though the filter worked as configured.

Now consider reports-view, which is inside Reporting Read. Selecting more access does not turn it into an independent entitlement decision. Inspect the profile and the selection or filter that applies to that reviewable package.

**Certifiable access** means access eligible for certification review under the applicable rules. The **access model** describes how access is organized and assigned, including packages and automatic requirements.

Those relationships explain which items can be reviewed separately. A broad inclusion setting does not remove them.

## If ISC lacks the account value, check collection

**Account aggregation** collects account information into ISC. For a permission to be represented on the account, the source must supply the relevant value and ISC must interpret it as account access.

Suppose the reporting application shows reports-export, but ISC's collected record for that same account does not.

Check the exact source and account, what data was returned and how the membership field was interpreted. A completed aggregation does not, by itself, establish that this account and its expected permission values were included correctly.

A listing called Export reports in the **entitlement catalog** answers a different question. The catalog contains entitlement records and their details: what access objects exist and what they mean.

It does not establish that this reporting account holds reports-export. Collecting the permission's description again cannot replace a missing account membership value.

A campaign filter selects review content from the relevant information. It cannot supply an account value that was never collected correctly.

## If the account is linked to the wrong person, check correlation

The account can have the correct permission values but appear under the wrong identity.

**Account correlation** matches and links source accounts with identities in ISC. This association connects the account's permissions to the person whose access is being reviewed.

If the association is wrong, the access can be shown in the wrong person's context. Changing the campaign's filter would not correct whose account it is.

An **uncorrelated** account has not been matched and linked to an established identity in ISC. That account can still exist in the application and have permissions.

Establish the account's ownership and the appropriate supported review context. A missing person link does not prove that nobody has the access.

## Check the assigned review before calling the item missing

A reviewer sees the certification assigned to them. That does not automatically contain every item from every assigned review in the campaign.

If the expected item exists in another certification, it was generated. The next question concerns its assignment and where it is being viewed, rather than whether source data failed to arrive.

The reviewer experience can also arrange the same relationships in different ways. An identity view starts with a person and lists their access. An access-item view starts with a permission or package and lists the identities that hold it.

Compare the actual person, account and access details. A different grouping is not evidence of a new grant or a missing permission.

There is another distinction: an item can exist while an action is unavailable.

**Platform permissions** determine which actions a person may perform in ISC. Along with assignment origin, inspect the assigned reviewer, the review's current state and that reviewer's permissions. A review that is no longer open for decisions is a different situation from an active automatic-role item that uses Acknowledge.

A missing Revoke button alone does not establish why the action is unavailable.

## Compare when the information was observed

Suppose the account information used for generation did not contain reports-export. The review was generated from that information. Later, the application granted export access, and a current account check now shows it.

The current check describes the account after the grant. It does not establish that export was included in the earlier generated review.

Compare the account information available at generation with the current account and the actual review contents. Opening the page again does not establish that its review items were rebuilt using newer access data.

The same applies after a later account aggregation or a filter edit. A saved configuration or newer account value is not proof that an existing campaign has been corrected.

Establish what the campaign was intended to assess and which supported correction is needed. A newly added permission and a collection failure can both produce a difference between today's account and an older review, but they require different explanations.

## Choose the next check from the missing connection

This diagram follows the evidence you need:

```text
Correct account value in ISC?
  No -> inspect collection
  Yes
   |
   v
Linked to correct identity?
  No -> inspect association
  Yes
   |
   v
Which package or requirement
controls this access?
   |
   v
Selected or excluded by
this campaign?
   |
   v
What was generated, when,
and in whose review?
   |
   v
Expected item and action?
```

The arrows guide an investigation. They do not describe a fixed sequence of internal ISC jobs. If the correct account value and identity link are already established, begin with the package, requirement or campaign fact you still need to check.

For reports-view, inspect Reporting Read. For cases-read, inspect Case Reader and its automatic membership. For portal-use, inspect the lifecycle-state requirement.

For reports-export held individually, once collection and ownership are correct, check whether the campaign actually selected it or excluded it, then inspect the generated review and its timing.

Each explanation points to different work. Fixing collection will not decide whether an automatic requirement is appropriate. Broadening a filter will not make a contained permission an independent review item.

Decisions on the visible items apply to those reviewed items. They do not silently settle a collection gap, excluded access or an inappropriate automatic requirement.

## Try three missing items with different explanations

A person holds a requested Ledger Review profile. It contains ledger-read and ledger-export, allowing reading and exporting ledger information.

Their archive-system account also holds archive-export, which allows exporting archive records. This entitlement is outside any profile, role or automatic requirement.

Their current lifecycle state requires the Staff Portal profile. That profile contains portal-use, which allows using the staff portal.

The source accounts belong to the correct identity. The campaign's intended selection covers the person and relevant access, with no exclusion removing the eligible example items.

The generated review contains Ledger Review. You cannot find a separate ledger-export entitlement item, an archive-export item or an individual Staff Portal profile item.

One observation needs careful attention: today's archive account has archive-export, but the account data used to generate the review did not contain it.

Which absences can you explain already, and which one needs more evidence?

The missing separate ledger-export item is expected. Ledger Review contains that permission, so inspect the profile's contents when assessing whether the person should keep the package.

The missing individual Staff Portal item is also expected. The current lifecycle state requires it. That absence does not establish that the portal requirement itself is appropriate.

Archive export needs investigation. The current account has it, but the review's account data did not. Compare the source history and the relevant collection to establish whether the permission was omitted from collection or granted after that observation.

You also need the intended observation point for this campaign. Was it meant to assess access held at generation, or is the review requirement to include this later grant too? A later grant alone does not prove that the earlier campaign was generated incorrectly.

If there is an actual data problem, correct it through the supported process. Then check that the required access has reached the appropriate generated review before relying on its coverage. A catalog entry or a saved source setting does not establish that result.

Now change Ledger Review's origin. It comes through the automatically assigned Ledger Worker role instead of an individual request. The campaign selects that role.

The profile is included through Ledger Worker. Expect the role item with Acknowledge, rather than the earlier separate profile item with Approve/Revoke.

The useful explanation connects the same facts all the way through: the account's permission, the person it belongs to, the package or rule controlling it, and the contents and time of the actual review.
