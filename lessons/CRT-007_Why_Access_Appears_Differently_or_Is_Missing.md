# Why does some access appear differently or not appear at all?

An account can export reports, but the review does not show a separate export permission. Another item appears as a role, with Acknowledge available instead of Revoke.

Those observations do not have one common explanation.

The access may be represented through a package. An automatic requirement may control it. The campaign may exclude it. Or the information needed for the review may not have reached ISC correctly.

Let's work out which explanation the evidence supports.

## Separate what the account has from what the review presents

An **account** is a record in a system. Its **access** determines what it can do.

SailPoint Identity Security Cloud (ISC) represents the person through an **identity**. A **source** is ISC's configured representation of a system or collection of account data.

An **entitlement** represents an access right from that source, such as permission to export reports.

A **certification campaign** organizes access reviews. A **certification** is an assigned review within the campaign. Its **reviewer** examines whether the access remains appropriate.

The **review item** is the actual unit presented for a decision. That unit is not always one underlying entitlement.

There are separate questions to establish: what the account holds, what ISC represents, how the access is assigned, and what this campaign actually presents.

Finding a permission in the application answers only the first of those questions.

## A package can be the review item

An **access profile** groups one or more related entitlements from a single source. A **role** groups related access that can include profiles, direct entitlements or both, across one or multiple sources.

Suppose reports-view permits viewing reports and belongs to a Reporting Read access profile that the person requested.

The review can present Reporting Read as the profile item. You inspect the profile's contents to understand that it includes the viewing right.

The absence of a separate reports-view entitlement item does not mean viewing access disappeared.

This is **encapsulation**: the component is contained within the access object through which it is managed for the review. Treating the component as a second independent decision would ignore that relationship.

An eligible profile may also be detected when ISC recognizes that the person already holds its entitlement set. Requested and detected profiles can be reviewable. A request is therefore not the only explanation for a profile appearing.

## The assignment origin also matters

**Assignment origin** means how the person received the access.

If the Case Read access profile was granted through the Case Reader role, the profile is contained in that role. The role is the relevant review object; Case Read does not become a separate individual profile item just because it has its own name.

Now suppose Case Reader is assigned automatically through **membership criteria**, the configured conditions that determine who should receive it.

A criteria-assigned role can be reviewed with **Acknowledge**. This records review of the automatically controlled access. It does not override the criteria or request removal of the role.

By comparison, a requested role can support **Approve**, accepting continued reviewed access, or **Revoke**, recording that it should be removed.

A role being visible therefore does not establish that Revoke must be available.

Another automatic origin is a **lifecycle state**, a configured stage in the person's relationship with the organization that can have access requirements.

For example, the person's active state can be configured to require an Employee Portal profile. A profile granted through the current lifecycle state does not appear individually in certifications. Its contained entitlement is not offered separately to bypass that requirement.

If the requirement is inappropriate, investigate the correct state, its data and configured access requirements with the authorized administrators. An absent individual Revoke item does not establish that the requirement is correct.

## Follow one set of held access into the review

Consider these supplied records for one identity:

- The reporting account holds reports-view and reports-export, permitting viewing and exporting reports.
- The case-management account holds cases-read, permitting reading cases.
- The portal account holds portal-use, permitting use of the employee portal.

All three accounts are correctly associated with the identity. ISC's collected information accurately represents those four rights for this review.

Reporting Read was requested and contains reports-view. reports-export is outside any containing package or automatic requirement.

Case Read contains cases-read and was granted through the automatically criteria-assigned Case Reader role. Employee Portal contains portal-use and is required by the person's configured active lifecycle state.

The campaign includes the intended person and eligible example access. No campaign filter removes those eligible items, and an appropriate reviewer has the generated review. The review is active and open for decisions, and the reviewer is authorized to make them.

With those conditions, the expected presentation is:

| Access actually held | Controlling assignment | Expected review item and action |
|---|---|---|
| reports-view | Requested Reporting Read profile | Reporting Read profile, with Approve/Revoke |
| reports-export | Individual entitlement, without a containing package or automatic requirement | reports-export entitlement, with Approve/Revoke |
| cases-read | Case Read profile inside criteria-assigned Case Reader role | Case Reader role, with Acknowledge |
| portal-use | Employee Portal profile required by the current lifecycle state | No individual Employee Portal profile or portal-use entitlement item |

The four supplied rights produce three expected review items here: a profile, an entitlement and a role.

That is an explanation of these particular records. It is not a formula for every campaign's item count.

Nor does it mean that the portal requirement has been judged appropriate through an individual certification decision. The requirement remains a separate governance question.

The useful comparison is between the expected review units and the actual generated units, not simply between the number of permissions and the number of rows.

## An intentional exclusion is a different cause

A **campaign filter** applies configured inclusion or exclusion criteria to the campaign. Selection and filtering determine which relevant people or access are included.

Change one condition in the example. The campaign uses an entitlement exclusion that removes reports-export from this campaign.

The reporting account still holds export, and ISC represents it correctly. The entitlement is individually reviewable. However, the filter deliberately excludes it from this review.

That absence is explained by campaign configuration. It is not evidence that the source removed the permission.

You still need to judge whether the exclusion matches the intended review requirement. A filter behaving as configured can produce a campaign that misses access the business intended to assess.

Now consider reports-view, which belongs to Reporting Read. Asking for a broader selection does not turn that contained entitlement into an independent entitlement decision. Follow the reviewable profile and the supported criteria for that object.

An inclusion setting does not make every held right an independently reviewable item.

**Certifiable access** means access eligible for the supported certification review under the configured access model. The **access model** is the organization of access packages and assignment requirements.

## If the data is missing, begin before the campaign

**Account aggregation** reads account information into ISC. An aggregation can finish without establishing that every intended account value arrived correctly.

If reports-export exists in the application but is absent from the relevant collected account record, investigate collection and interpretation first.

Check the exact source and account, the values the connection returned, and whether the membership field was interpreted as entitlement data.

An entitlement description in ISC's catalog is not enough. The **entitlement catalog** contains information about the access objects; its listing does not establish that this account holds one.

If the account and membership are present but connected to the wrong identity, investigate **account correlation**, the association between source accounts and identities.

A permission can be collected correctly yet appear in the wrong person's context because the association is wrong.

If the account is **uncorrelated**, it lacks the intended identity association. It can still have actual access. Establish the appropriate ownership and supported review context rather than treating it as an account with no permissions.

A campaign filter cannot repair missing source values or incorrect ownership.

## Check which review and observation you are looking at

A reviewer's screen is an assigned portion of the campaign, not automatically every review in it.

If the expected item exists in another assigned certification, the issue is different from the item never having been generated. Inspect the actual assignment before calling it missing.

The reviewer experience can also organize information by identity or by access item. Those views arrange related information differently. Compare the actual person/account/access details rather than assuming a different grouping represents a different grant.

If the item exists but its action is unavailable, inspect the assignment, the review's current state and the reviewer's platform permissions as well as its origin. Platform permissions determine what the person can do in ISC. A missing button alone does not prove that the access was automatically assigned.

Time can explain another difference.

Suppose the account information used for a generated review did not include reports-export. The permission was granted later, and a current application check now shows it.

That current check establishes the later account state. It does not prove that the already generated review contains the new entitlement.

Inspect the data and campaign context used at generation, along with the actual review contents. Do not assume a fresh page view or a later account aggregation rebuilt that review.

The same caution applies to a changed filter. Saving a revised filter is not, by itself, proof that an existing campaign's contents have been corrected.

## Use the missing item to choose your next check

The sequence below is a guide to evidence, not a universal order of internal ISC jobs.

```text
Check source/account values
  Missing -> collection
  Present
     |
     v
Check identity association
  Wrong -> ownership
  Correct
     |
     v
Check origin and containment
     |
     v
Check scope and filters
     |
     v
Check generated contents,
time and assigned review
     |
     v
Compare item and action
```

Start with the observation you actually have. If the correct collected relationship is already established, you can move directly to its containing object and campaign context.

For a known individual reports-export entitlement absent from the review, inspect the generated selection and any relevant exclusion once its data and ownership are established.

For reports-view, inspect Reporting Read before assuming a missing independent entitlement.

For cases-read, inspect Case Reader and its automatic assignment. Acknowledge is consistent with that origin; it is not a hidden Revoke operation.

For portal-use, inspect the lifecycle requirement. Its omission from individual decisions is not proof of absent access or automatic approval.

The reviewer can act only on the access and actions presented through the supported review. Decisions on the visible items do not silently settle missing data, excluded scope or an inappropriate automatic requirement.

## Try three absences with different explanations

An identity holds Ledger Review through an approved request. The profile contains ledger-read and ledger-export, allowing reading and exporting ledger information.

The identity also has archive-export on an archive-system account, permitting exporting archive records. That entitlement is outside any containing package or automatic requirement.

The Staff Portal access profile supplies portal-use through the identity's current lifecycle state, permitting use of the staff portal.

The source accounts and their identity associations are correct. The campaign's intended selection includes the relevant person and access, with no exclusion removing the eligible example items.

The generated review contains Ledger Review. It has no separate ledger-export item, no archive-export item and no individual Staff Portal profile item.

One more observation is supplied: a current archive-system check shows archive-export, but the account data used to generate the campaign did not contain it.

Are all three absences expected? What would you inspect before claiming that the intended review content is complete?

Ledger export is contained in the requested Ledger Review profile. Its absence as a separate entitlement item is expected under the supplied conditions. Inspect the profile to assess the package's actual access.

Staff Portal is required through the lifecycle state. Its absence as an individual profile decision is also expected. That does not certify the correctness of the lifecycle requirement.

Archive export needs investigation. The generated campaign did not have the account-held value used by the current application observation. Compare the relevant account collection with the source information and establish whether the permission was missing from collection or was granted after that observation.

Also establish which observation point the campaign was intended to assess. A later grant does not, by itself, mean the earlier campaign generated incorrectly. Whether this review needs to include it depends on the intended timing and supported correction process.

Correct any actual data problem through the supported process, then validate the required generated contents before relying on the review. Neither another catalog listing nor a saved source-setting change proves that archive-export reached this campaign.

Now change Ledger Review's origin. It is granted through an automatically criteria-assigned Ledger Worker role rather than an individual request. The role is included by the supplied selection.

The profile is now contained within that role. Expect the eligible role item with Acknowledge, rather than assuming the old independent profile decision must remain.

The reason for each result comes from its evidence: the held account value, the controlling assignment, the eligible review object and the campaign that was actually generated.
