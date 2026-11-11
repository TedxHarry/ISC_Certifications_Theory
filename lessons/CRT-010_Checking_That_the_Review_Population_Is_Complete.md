# How do we establish that the review population is complete?

You expected three people in a review. The campaign shows three.

The totals match, but one intended person could be missing while someone else has taken their place.

Before relying on the review, compare who and what should be included with who and what was actually generated. A correct total cannot tell you whether those are the same records.

## Start with the people and access you intend to assess

The **review population** is the people, accounts and access intended for the review.

“Review Finance access” leaves too much open. Does that mean every employee in Finance, every account in the finance application or everyone who can export payment reports? Those choices produce different populations.

Let's use a specific requirement: assess supplier-payment report export access on production finance accounts belonging to active Accounts Payable employees, as held at 09:00.

An **account** is a record used to access an application or system. Its **access** determines what someone using it can do. In this example, PAY.EXPORT permits downloading supplier-payment reports.

The requirement identifies the people, the production system, the permission and the time being assessed. It also tells us that an Accounts Payable employee without that permission does not belong in this particular access population.

We are checking whether the intended access reaches the review. Whether each person still needs it is a later decision.

## Build the expected list from evidence

An **expected baseline** is the list of records that should be accounted for, supported by the agreed requirement and evidence.

For the 09:00 finance review, current personnel records identify the active Accounts Payable employees. Application account information establishes which of their production finance accounts held PAY.EXPORT at that time.

Those checks give us three expected relationships:

- Person 1041, account finance-041, PAY.EXPORT.
- Person 1042, account finance-042, PAY.EXPORT.
- Person 1043, account finance-043, PAY.EXPORT.

The numbers identify records, not job responsibilities. Each account belongs to the stated person, and the production application and permission are the same throughout this example.

Keep the evidence for the list and when it applies. An employee list alone does not establish who holds export access. A list of export-capable accounts alone does not establish which owners meet the people requirement.

Also ask whether the evidence itself covers the intended system and account types. An extract that left out an application division or accounts with additional administrative permissions would make the expected list incomplete before you compare it with the campaign.

## Avoid using the same mistake as both lists

SailPoint Identity Security Cloud (**ISC**) keeps an **identity** representing a person and connects it with their accounts. A **source** is the configuration in ISC for the system or collection of account data being managed.

A **query** selects records according to search conditions. A campaign query might use the department information held on ISC identities.

Suppose that information is outdated for a person. If you use the same query to build both the expected list and the campaign, both lists can omit that person. They will agree because they share the same mistake.

Check the expected population against information that can establish the business requirement independently. For this example, that means checking the relevant personnel and application records, including their observation times.

“Independent” does not mean collecting an unrelated spreadsheet and assuming it is correct. Establish where the records came from, what they cover and why they support this review.

## Follow the access into ISC before comparing the campaign

ISC represents a source access right as an **entitlement**. **Account aggregation** collects account information into ISC, including the permission values the source provides.

The account's collected data needs to show PAY.EXPORT. A successful collection operation alone does not establish that the intended account and value arrived.

**Account correlation** matches and links the source account with the person's identity. Correct permission data on an account linked to the wrong person would still produce the wrong review context.

For our finance example, the three expected accounts and their export values are present in ISC and correctly linked. That lets us move to campaign selection rather than guessing that collection failed.

A **certification campaign** organizes access reviews. A **certification** is an assigned review within it. Its **reviewer** is responsible for assessing the access, and a **review item** is the access presented for a decision.

An administrator selects the people and access for the campaign. **Access refinement** chooses which access to include for selected people. A **campaign filter** can include or exclude people or access according to its configured conditions.

These settings determine the generated work. Check the actual selected records and effects; the business requirement written in a campaign's name does not enforce itself.

## Compare the records when the totals match

In this example, PAY.EXPORT is individually reviewable. It is not contained in a profile or role, and no automatic requirement keeps it. The campaign is intended to include that entitlement for the required people, without another exclusion. Its people selection uses the active status and Accounts Payable department value recorded in ISC, then includes PAY.EXPORT.

Inspecting the complete generated contents instead finds 1041/finance-041, 1042/finance-042 and 1099/finance-099.

Now compare both directions:

| Person and finance account | Expected from the 09:00 requirement? | Present in the generated review? | Finding |
|---|---|---|---|
| 1041 / finance-041 | Yes | Yes | Matching relationship |
| 1042 / finance-042 | Yes | Yes | Matching relationship |
| 1043 / finance-043 | Yes | No | Expected relationship missing |
| 1099 / finance-099 | No | Yes | Unexpected relationship included |

There are three expected relationships and three generated relationships. Only two match.

**Reconciliation** means comparing the actual records and explaining their differences. Looking for missing expected records is one direction. Looking for unexpected included records is the other.

A **coverage gap** is intended review content that has not been adequately accounted for. Here, 1043's export access has not reached the review.

The unexpected 1099 entry also needs investigation. It does not compensate for the missing person, and it does not mean that person's actual export access should automatically be removed.

Campaign inclusion and whether access is justified are different questions.

## Use the difference to locate the cause

The baseline says 1043 was an active Accounts Payable employee at 09:00. ISC's department value used by selection still says Accounting, so the query did not select that identity.

For 1099, the personnel evidence says the person was outside Accounts Payable at 09:00. ISC's department value still says Accounts Payable, so the query selected them.

These facts explain why the selection differs. They do not yet establish why the values in ISC are outdated.

An **attribute** is a named piece of information such as department; the value is the department recorded for that person. Inspect the original person record, which incoming field supplies ISC's department attribute and when that value was updated. Establish whether the correct value reached ISC.

Correct the actual data or selection issue through the authorized process. Then verify the required generated contents. Saving a corrected attribute or query does not prove that an existing campaign has been rebuilt.

A different missing relationship could lead elsewhere: absent account data points to collection; the wrong person link points to correlation; correct data excluded by the campaign points to its selection or filter.

Locate the difference before choosing the correction.

## Compare the right units when access is packaged

An **access profile** is a bundle of entitlements from one source. A **role** can contain profiles, direct entitlements or both, from one or multiple sources.

An account can have several permissions represented through one profile or role review item. Therefore, the number of permission values does not have to equal the number of review items.

Trace each intended permission to the reviewable object that includes it. Inspect the actual contents and assignment, not only the package name.

Some roles are assigned automatically through **membership criteria**. These are configured conditions that determine who receives the role. In a certification, such a role uses **Acknowledge**, which records examination of automatically controlled access without requesting removal.

A **lifecycle state** is a configured stage in the person's relationship with the organization and can require access profiles. Profiles required through the person's current state do not appear individually in certifications.

If the business requirement includes assessing those automatic requirements, the absence of individual items needs an appropriate governance response. Do not report that every requirement was individually certified simply because all visible items received decisions.

The baseline describes the access that needs accountability. The supported review model determines how that access can be presented and handled.

## Check exclusions and campaign prerequisites

Some exclusions are deliberate. An approved requirement might cover only production accounts, with test-system access handled separately.

Keep the reason and responsible coverage for that boundary. If the requirement actually includes test accounts, silently removing them from the expected list would conceal a gap.

The campaign route also matters. The documented dedicated Manager Campaign excludes identities without a manager relationship. That relationship records who manages the person.

The separate Search campaign route with Manager selected as reviewer handles missing-manager cases differently. Check the chosen route rather than assuming that every manager-reviewed campaign excludes the same people.

Similarly, do not assume that selecting all people overrides contained-access rules, or that a saved inclusion condition proves the intended access was generated.

Explain each excluded expected record. A convenient explanation of how it was omitted is not evidence that omitting it meets the business requirement.

## Do not lose accounts whose owner or type differs

An **uncorrelated account** has not been matched and linked to an established identity in ISC. It can still have actual permissions in the application.

If an export-capable account lacks a person link, you cannot simply conclude that it is outside a people-based requirement. Establish its ownership and whether it belongs in that requirement.

A **machine or service account** is used by an application or process rather than as a person's ordinary login. If the requirement covers all production export accounts, these accounts need explicit consideration too.

ISC provides supported review approaches for uncorrelated and machine accounts where available. Establish the appropriate campaign capability and responsible owner for the actual environment.

A review limited to identified employees can be complete for that agreed population without covering every account in the application. Describe that limit clearly.

When the broader requirement includes an unresolved account, record the gap, responsible person and required follow-up. Calling it an exception does not make it reviewed.

## Inspect the complete generated work

A **preview** contains generated campaign information available for validation before starting the campaign. Inspecting a proposed query or a saved definition is not the same as inspecting that generated content.

Check the campaign you actually intend to use. Confirm its identity, generation context and actual items, along with the relevant settings.

One reviewer's assigned certification is only part of the campaign. An expected item found in another assigned review is different from an item never generated.

People, accounts, access items and assigned certifications are different counting units. One person can have several accounts, a package can contain several permissions, and one reviewer can have more than one assigned review.

Use the details needed to establish coverage rather than assuming that each displayed row means one person-account-permission relationship.

Here is the comparison we are making:

```text
Expected account/access list
            |
            v
Identify correct review units
            |
            v
Compare ALL generated work
            |
            v
Matching / missing / unexpected
            |
            v
Explain and verify differences
```

The arrows guide the evidence check. They are not a fixed sequence of internal ISC jobs. The generated work must be compared against the expected list; it must not replace that list as the definition of what should have been included.

## Make sure the evidence is the whole result

**Pagination** returns a collection of records in portions, or pages. If an authorized tool returns only the first page, that page is not evidence of the complete population.

Establish how the particular screen, export or read-only API returns its results. Check for page boundaries, retrieval limits, filters and whether you have included every assigned review needed for the comparison.

An **API** is an interface through which software requests data or operations. Its records also have a scope. An API that returns only campaigns from the newer certification system cannot establish that an older, legacy campaign does not exist just because it returns no matching record.

Use supported evidence for the campaign version actually in use. Keep identifiers for the actual records, source/account references and relevant times; names alone can repeat.

If the population changes during retrieval, account for that change before treating several pages as one consistent observation. Do not silently combine a morning expected list with a later, different access population.

Sampling can help check whether selected descriptions or account links are correct. It cannot establish that every expected record is included.

For full coverage, compare the complete intended population and complete generated relationships, then investigate the differences. A sample provides evidence about what was sampled.

## Keep configuration evidence separate from coverage evidence

A campaign composition report describes campaign configuration, such as settings and the filter used. That is useful for explaining how the campaign was configured.

It is not, by itself, an independently justified list of every person-account-access relationship the business intended to review.

Campaign status evidence describes the work within that campaign. If every generated item is decided, the missing 1043 relationship still has no decision because it never became part of that work.

Likewise, an older downloaded report does not automatically show later campaign changes. Check when the report was generated and which current records it represents. Use supported reports or other authorized observations that contain the details needed for the comparison.

Keep the requirement, expected baseline, actual generated references, differences and their resolutions together. For an unresolved difference, preserve its status, responsible owner and next action.

The person responsible for validating scope should have evidence of that comparison. An authorized administrator performs any necessary campaign correction or start action under the organization's process.

Completeness does not decide whether every included permission should remain. It establishes whether the intended access has been accounted for so that the appropriate assessment can happen.

## Try two people with three accounts

The requirement is to assess inventory-adjustment access on all production warehouse accounts belonging to two operators, as held at 14:00. It explicitly includes their administrative accounts.

STOCK.ADJUST permits changing inventory quantities. STOCK.VIEW permits viewing inventory.

The evidence establishes these relationships at 14:00:

| Person | Account | How the adjustment access is held |
|---|---|---|
| 201 | warehouse-201 | Requested Stock Control profile containing STOCK.VIEW and STOCK.ADJUST |
| 202 | warehouse-202 | Individual STOCK.ADJUST entitlement |
| 202 | warehouse-202-admin | Individual STOCK.ADJUST entitlement |

The accounts and identity links are correct. The individual entitlements are outside other packages and automatic requirements.

The generated review includes Stock Control for 201 and STOCK.ADJUST for 202. The person count is two, matching the intended operator count.

Inspection of the actual review details establishes that the 202 item covers warehouse-202 only. The warehouse-202-admin relationship is not included in the generated review.

Can the matching person count establish completeness?

No. Both intended people appear, but one intended account's adjustment access is missing. Trace the administrative account through collected data, association, actual selection and generated contents to find where it was omitted.

Do not add an expected separate STOCK.ADJUST item for 201 merely to match the permission count. Stock Control contains that permission and is the relevant profile item.

Now change the evidence: checking all assigned reviews finds the administrative account's adjustment access in another certification. It was outside the view you first inspected. The account is included in the campaign, so its absence from that first view does not establish a campaign-wide gap.

Finally, return to the missing-admin case and change one fact. Application history shows that warehouse-202-admin received STOCK.ADJUST at 14:15, after the agreed 14:00 observation point.

That relationship would not belong in the 14:00 expected baseline. Establish how the later grant should be assessed under the review requirement and supported process; do not call it a failure to include access held at 14:00.

Each conclusion follows a particular comparison: the intended time, the exact accounts and permissions, and the access the generated items actually cover.
