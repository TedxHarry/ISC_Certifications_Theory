# What happens when selection rules and filters are combined?

You open a saved campaign setup and find a people query, a chosen list of access items and an exclusion filter.

Each setting looks reasonable. Yet the generated review does not contain the access you expected.

Which setting explains the difference?

Follow one person's access through the choices. Find out whether the person was selected, whether they hold the intended access, whether that object was chosen and whether a filter leaves it in the review.

The final result needs to answer the business request. One setting that looks correct cannot establish the whole result.

## Give each choice a clear job

In SailPoint Identity Security Cloud (ISC), an **identity** is a record representing a person. Their **accounts** hold access in applications. The identity can also have **attributes**, named values such as department and location, that help you find the intended people.

A **source** contains the connection settings and collected account information for a managed system. An **entitlement** is a piece of access recorded from that system, such as a permission to export reports.

A **certification campaign** organizes review work. Its saved configuration describes the intended contents and assignments. The generated work contains the actual access items assigned to **reviewers**, the people or groups responsible for assessing them.

Three choices can contribute to that configuration:

A **query** finds records matching conditions. If it returns identities, you are finding people, even when a condition concerns their accounts or access.

**Access refinement** chooses which access to include for the selected people.

A **campaign filter** is a saved set of criteria used to include or exclude review content. A criterion is a test; its type identifies what is tested, such as an entitlement or an identity.

The filter mode says what to do with a match. Inclusion keeps matching review content. Exclusion leaves it out. The criterion type determines whether the test concerns a person or a particular access item.

Those controls need to express a consistent request.

## Follow one complete setup

The request is to review report-viewing access for Finance people in Chennai or Pune. A separate review is planned for export access, and Support access is outside this campaign.

The saved setup chooses both report entitlements and has an export exclusion attached.

Here is the supplied data:

| Identity | Department | Location | Source and account | Existing access |
|---|---|---|---|---|
| 1801 | Finance | Chennai | Reporting Production, rep-1801 | View Reports; Export Reports |
| 1801 | Finance | Chennai | Support Production, case-1801 | Read Cases |
| 1802 | Finance | Pune | Reporting Production, rep-1802 | View Reports |
| 1803 | Operations | Chennai | Reporting Production, rep-1803 | Export Reports |
| 1804 | Finance | Chennai | Reporting Production, rep-1804 | Export Reports |
| 1804 | Finance | Chennai | Support Production, case-1804 | Read Cases |
| 1805 | Finance | Mumbai | Reporting Production, rep-1805 | View Reports |

View Reports permits viewing reports. Export Reports permits exporting them. Read Cases permits reading support cases.

The permissions, locations, departments and account links are correct in the data being used. Every listed entitlement is separately reviewable here. None is supplied through a larger access package or an automatic access rule in this example. No other restriction changes these holdings.

The display names identify distinct entitlements within their specified sources. The intended reviewers are suitable, allowed to perform the reviews and not reviewing their own access.

## First find the intended people

Attribute mappings determine how source information supplies the identity values. In this example, department and location are available as searchable identity attributes with the technical names `department` and `location`.

The people query is:

`attributes.department.exact:"Finance" AND (attributes.location.exact:"Chennai" OR attributes.location.exact:"Pune")`

The fields identify the department and location information on the identity. For these plain text values, `.exact` requires the complete value, including case. Use the actual mapped attribute names and stored values for the ISC environment you are working in.

Read the query as Finance **and** one of the two named cities.

AND requires both the department condition and the grouped city condition. OR allows either city within the parentheses.

The matching identities are 1801, 1802 and 1804.

Identity 1803 has an accepted location but the wrong department. Identity 1805 has the accepted department but a different location.

For this setup, all three matching identities are actually added. They have six holdings available: three for 1801, one for 1802 and two for 1804.

A **holding** means that a particular person has access through the named account.

The query has established the people selection. It has not yet made this a report-viewing-only review.

## Then inspect the chosen access objects

The saved refinement chooses the View Reports and Export Reports entitlements from Reporting Production.

Among the selected people, four holdings fit those choices:

- 1801: View Reports and Export Reports on rep-1801.
- 1802: View Reports on rep-1802.
- 1804: Export Reports on rep-1804.

Read Cases is not one of the chosen objects. The Support holdings for 1801 and 1804 are outside that access choice, even though both people were selected.

Identity 1805's View Reports holding is also outside the intended work. A matching access name does not establish that its holder was selected.

You need both facts: the intended person and the intended access object.

## Now account for the selected filter

The attached campaign filter is Exclusion, with an Entitlement criterion for Reporting Production, Equals Export Reports.

The criterion matches the two export holdings belonging to 1801 and 1804. Exclusion leaves those holdings out.

The combined setup therefore calls for:

- View Reports on rep-1801, belonging to 1801.
- View Reports on rep-1802, belonging to 1802.

Those are the two expected review holdings for this supplied setup. Compare them with the actual generated work.

Identity 1804 was selected and has access from the chosen list, but its only chosen entitlement matches the exclusion. Nothing remains for a decision in this example.

That does not mean 1804's accounts have no access. The export permission and Support permission still exist in the supplied account records. They are outside this campaign's final intended scope for different reasons.

The checks fit together like this:

```text
People condition:
Finance AND (Chennai OR Pune)
       |
       v
1801, 1802, 1804 actually selected
Six available entitlement holdings
       |
       v
Chosen access:
Reporting Production:
View Reports + Export Reports
Four holdings fit this choice
       |
       v
Exclusion: Export Reports
Source: Reporting Production
       |
       v
Expected review content:
1801 View Reports
1802 View Reports
       |
       v
Compare with actual generated work
```

The arrows trace the meaning of the selected settings and the expected result. They do not describe the timing or order of private ISC background services.

The result follows from the supplied people, access and supported entitlement exclusion. For another criterion type, first check which people or items it can include or exclude.

## Explain one retained item and one omitted item

Take View Reports on rep-1801.

Its owner meets the people query and was added. The account holds the intended entitlement. That entitlement is in the saved refinement. It does not match the export exclusion.

That gives you a reason for every part of its inclusion.

Now take Export Reports on rep-1804.

Its owner also meets the query and was added. The account holds an entitlement in the refined list. This time, the entitlement matches the exclusion.

The filter explains why it is absent from the expected review.

For Read Cases on case-1801, the access choice explains the omission. For View Reports on rep-1805, the people selection explains it.

A missing item does not always have the same cause. Identify the specific condition and record that explain it.

## A matching query result is not always an added person

Suppose the same query still finds 1801, 1802 and 1804, but the campaign creator chooses specific results and adds only 1801 and 1804.

Identity 1802's View Reports would be missing from that saved people selection.

Repeating the query could still display 1802. That would not prove the identity was added to the campaign.

Check the actual all-results or specific-selection choice and saved identities. The query text is one part of the configuration, not the whole configuration.

Likewise, verify that the intended access objects were actually added during refinement and that the intended filter is attached to this campaign.

## What if the access choice and inclusion filter disagree?

Change the saved access choice to Reporting View Reports only. Then imagine an inclusion filter asking for Support Production's Read Cases.

No holding in the chosen reporting-view scope is a Read Cases holding.

Those two restrictions do not describe a common review item. Do not treat the word Inclusion as permission to assume that the access choice has been replaced.

First establish which access the request really requires. Correct the configuration so that the choices agree, then inspect the generated result.

The two choices ask for different access scopes. Resolve that disagreement before relying on the result; an empty or unexpected preview is not evidence that one control always wins.

If the preview contains unexpected Support access, investigate the actual campaign route, saved access choices and selected filter. Do not explain it away with an invented “inclusion always wins” rule.

## OR inside a filter is a separate relationship

Return to the main people selection and the two chosen Reporting entitlements.

Suppose the exclusion filter now has two entitlement criteria:

- Reporting Production, Equals Export Reports.
- Reporting Production, Equals View Reports.

The documented builder treats separate criteria as OR alternatives. An entitlement matching either criterion is an exclusion match.

For these supplied holdings, one criterion matches the exports and the other matches the viewing permissions. Each of the four chosen holdings matches at least one criterion and is therefore an exclusion match.

If you had assumed both criteria must match the same entitlement, you would have predicted the wrong scope. A single entitlement does not need both names for this OR filter to match.

That relationship is different from requiring both the people selection and the intended access choice to be satisfied.

Inside the people query, we deliberately wrote Finance AND an accepted city. Inside this filter, the documented criteria are alternatives. Keep those meanings separate.

More filter criteria can therefore remove more work. They do not automatically make an exclusion harder to satisfy.

## Changing the unit can produce the same count with different content

Keep the original query and the same four refined Reporting holdings. Replace the export exclusion with an Identity exclusion for 1801.

That person-level exclusion leaves out both of 1801's chosen entitlements.

The remaining holdings are:

- 1802: View Reports.
- 1804: Export Reports.

There are two again, but they are not the two holdings requested by the original report-viewing review. The result now omits 1801's View Reports and keeps 1804's Export Reports.

A total of two is not enough evidence. Compare the actual people, source accounts and access objects.

When requirements involve both person exclusions and access exclusions, write down the expected effect of each. A person-level match can affect all their review work; an entitlement-level match can affect a particular item.

For Role criteria or account-attribute combinations, establish the supported affected unit before predicting unrelated work. Check a role holder or a person with several source accounts and unrelated access. Do not assume that every criterion acts like the entitlement examples.

## Confirm which campaign route was used

The Search creation flow offers a query-based route and a route using a campaign filter to determine contents.

In the worked setup, the people query, actual added identities, saved refinement and attached exclusion are all part of the intended configuration.

A filter-based contents route is a different starting choice. Do not borrow a query you ran separately in Search and assume it limits that campaign.

Check the configuration belonging to the actual campaign, rather than whichever query or filter happens to be open on screen.

The query-based and filter-based routes offer different setup choices. Use the supported options available in the campaign you are configuring.

## Use enough controls to express the requirement clearly

For this small fixed example, directly choosing Reporting View Reports for the intended Finance people can express the final access requirement more simply.

A saved setup may contain a broader report selection and a reusable export exclusion. You need to understand that existing combination. You do not need to reproduce every control in a new design without a reason.

Compare the resulting identities and holdings when deciding whether two designs meet the same requirement. Matching counts alone do not establish equivalence.

When the requested scope changes, revisit the relevant people choice, access objects and filter. Changing only the campaign's name does not change any of those instructions.

## Verify the generated work before relying on the plan

A **preview** is generated review work available for inspection before the campaign starts.

For the main request, check that 1801 and 1802 have the exact intended View Reports holdings. Check why the export, Support and out-of-location holdings are absent.

If an expected item is missing, first find the actual person, source account and access object. Then compare the selected people, saved access choice, filter and the data available when work was generated.

A permission held through a package may have a different reviewable object from a separately held entitlement. Older or incorrect account data can also give a different result from the one you calculated.

Check reviewer assignments separately. A correct scope does not establish that the right person received the work.

Saving a corrected definition is not proof that an already generated campaign changed. Use the supported correction or generation process, and inspect the resulting contents and assignments.

Finally, leaving access out of a review neither removes it from the application nor approves its continued use. Required reviews or access changes still need their own evidence.

## Try a different review object

The request is:

“Review the Case Administrator access profile for Support people in Pune, excluding identity 1902.”

An **access profile** groups entitlements from one source. This requested profile on Support Production contains Read Cases and Assign Cases. Read Cases permits reading support cases; Assign Cases permits assigning cases to staff.

Each person received the profile through an access request. Read Cases and Assign Cases were granted together through that profile, rather than as separate entitlement grants.

The profile can be reviewed as one item. Its contained permissions are not separate review items in this arrangement. Selecting a component permission does not split it out of the profile.

The supplied identities are:

| Identity | Department | Location | Existing access |
|---|---|---|---|
| 1901 | Support | Pune | Requested Case Administrator profile |
| 1902 | Support | Pune | Requested Case Administrator profile |
| 1903 | Support | Chennai | Requested Case Administrator profile |
| 1904 | Engineering | Pune | Requested Case Administrator profile |

The data and account associations are correct. The profiles are separately reviewable under these supplied conditions, and suitable permitted non-self reviewers are available.

A proposal uses the correct Support-and-Pune people query, but refines access to the Assign Cases entitlement and adds an entitlement inclusion for Assign Cases.

Does that proposal meet the request? Explain which access object should be reviewed and whose item should remain after the people selection and exclusion. What would you look for in the generated preview?

<details class="practice-answer" markdown="block">
<summary>Compare your reasoning</summary>

No. The component entitlement is not a separate review item in this arrangement. An entitlement selection and filter do not split it out of the containing profile.

Choose the Case Administrator profile as the reviewable object. Preserve the intended Support-and-Pune people selection and the identity exclusion for 1902.

Then verify that 1901's profile is the intended remaining item. Identity 1903 has the wrong location; 1904 has the wrong department; 1902 is explicitly excluded.

</details>

### What changes if the profile comes through a role?

A **role** can group access profiles and direct entitlements, including access across sources.

Keep the same review request, but change one condition: 1901 receives the profile through a role instead of through a separate access request. A profile supplied through a role is reviewed as part of that role, not as an individual profile item.

The plan still selects the Case Administrator profile for Support people in Pune and excludes identity 1902.

Can the corrected profile-only plan still meet the request for 1901? Explain what you would inspect before deciding how to review this access.

<details class="practice-answer" markdown="block">
<summary>Compare your reasoning</summary>

The old profile-only plan no longer matches how 1901 receives the access. Identify the containing role and check its complete access scope before deciding how to meet the request.

Adding more filters does not turn the component back into an independently reviewable profile.

The role may include other access. Establish what a decision on that role would cover before using it to answer a request about one profile. The facts here do not establish the role's complete contents or a safe removal decision.

</details>
