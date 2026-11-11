# How do campaign filters include or exclude review content?

You are preparing an access review. The selected people have several permissions, but the request concerns only report-export access.

How do you keep that review focused?

A **campaign filter** is a saved set of conditions used to include or exclude content when a certification campaign is generated. A **certification campaign** organizes access-review work and assigns it to reviewers.

The person configuring the campaign selects its filter. The filter helps determine what reaches the review; the reviewer's later decision assesses the included access, such as whether a separately reviewable permission should be kept or removed.

Let's follow the filter through a small set of permission records.

## Start with the people and their access

In SailPoint Identity Security Cloud (ISC), an **identity** is the record representing a person. An **account** is that person's record in an application.

A **source** holds the connection settings and collected information for a managed system. An **entitlement** is a piece of access recorded from that system.

Our example uses these entitlement display names:

- View Reports allows the account to view reports.
- Export Reports allows it to export reports.
- Read Cases allows it to read support cases.

A **display name** is the readable label shown for the entitlement. It can differ from the value stored on the application account. Here, Export Reports represents the stored permission value RPT.EXPORT.

The selected people have this access:

| Identity | Department | Source and account | Held entitlements |
|---|---|---|---|
| 1501 | Finance | Reporting Production, rep-1501 | View Reports; Export Reports |
| 1502 | Finance | Reporting Production, rep-1502 | View Reports |
| 1503 | Operations | Reporting Production, rep-1503 | Export Reports |
| 1503 | Operations | Support Production, case-1503 | Read Cases |

Identity 1503 has two accounts in different systems.

For this example, the account links and collected permissions are correct. All three identities are selected, and all five listed permission holdings would otherwise be included. Each entitlement is held separately and can be reviewed individually.

A **holding** here means that a particular account belonging to a particular person has the permission. No package, automatic access requirement or other restriction changes these five holdings.

The reviewers are suitable, permitted to perform the reviews and not reviewing their own access.

## First decide what the condition matches

A **filter criterion** is one test used by a filter. It needs to identify what is being tested and what counts as a match.

For the report-export request, the criterion is:

- Type: Entitlement.
- Source: Reporting Production.
- Operation: Equals.
- Entitlement display name: Export Reports.

The type says that the condition concerns an entitlement. The source distinguishes this system's access from similarly named access elsewhere.

The **comparison operation** describes how a value is tested. Equals asks whether the value matches the specified value; Contains asks whether the specified text occurs within it.

Under the supplied records, the criterion matches two holdings: Export Reports on rep-1501 and Export Reports on rep-1503.

It does not match View Reports or Read Cases.

So far, we have identified the matches. We still need to say what the filter should do with them.

## Inclusion keeps the matching content

Choose **Inclusion** for this entitlement criterion.

An **inclusion filter** keeps the content that meets the specified condition. In this entitlement example, only holders of the matching entitlement are included, and only the matching entitlement is presented for review.

The resulting work contains:

- Identity 1501's Export Reports holding on rep-1501.
- Identity 1503's Export Reports holding on rep-1503.

Identity 1502 has no matching export holding in the supplied records, so it contributes no export item to this review.

Identity 1503's Read Cases permission is also outside this result. The person holds the selected entitlement, but that does not make all their other access part of an entitlement-inclusion result.

Notice the two connected effects: the filter narrows both the relevant people and the access presented for them.

Creating the saved filter is not enough on its own. The intended campaign must actually use that filter. Check its selected configuration and the generated work.

## Exclusion omits the matching content

Start again with the original five holdings. Use the same entitlement criterion, but change the filter mode to **Exclusion**.

An **exclusion filter** omits the content that meets its condition.

The two Export Reports holdings are left out. The work that remains is:

- Identity 1501: View Reports on rep-1501.
- Identity 1502: View Reports on rep-1502.
- Identity 1503: Read Cases on case-1503.

All three people still have other review content in this supplied result.

Why does 1503 remain? Because this condition excludes the matching entitlement, not every person who happens to hold it.

The inclusion and exclusion results follow from the same matches:

```text
Starting work: five entitlement holdings
                   |
                   v
Match Reporting Production / Export Reports
                   |
          +--------+--------+
          |                 |
          v                 v
      Inclusion         Exclusion
      Keep the two      Omit the two
      export holdings   export holdings
          |                 |
          v                 v
      Two holdings      Three other
      for review        holdings remain
```

The branches describe the two separate filter choices. They are not consecutive steps, and the arrows are not a private ISC job sequence.

The starting holdings and matching criterion are unchanged. The mode changes which content is kept for the review.

## Excluding a person is a different instruction

Suppose the request is instead to leave identity 1503 out of this campaign.

Using the original five holdings, an **Identity** exclusion for 1503 leaves out that person's review content. Both Export Reports and Read Cases for 1503 are outside the campaign.

Identity 1501's Export Reports remains because the filter did not exclude that entitlement across other people.

That is different from the earlier entitlement exclusion, which kept 1503's case-reading review and removed 1501's export review.

An **Identity Attribute** criterion also works through person information. An attribute is a named value, such as department, recorded on an identity.

With these supplied departments, an Identity Attribute exclusion for Department Equals Operations excludes identity 1503's work. A Department Equals Finance inclusion selects 1501 and 1502.

A person-level criterion does not mean “review only the permission that caused me to think of this person.” You still need the intended access scope for the selected people.

Before choosing a criterion, name the required effect: leave out a permission, or leave out a person's review work. Those are different boundaries.

## The operation and the value matter too

Return to an entitlement inclusion on Reporting Production.

Equals Export Reports selects that displayed entitlement in this example. Contains Reports matches both View Reports and Export Reports.

With Contains Reports, the report-viewing holdings for 1501 and 1502 now belong to the matching review scope too. Read Cases is still outside it.

The word you compare can change the review even when the source and mode stay the same.

Where offered for the selected criterion, Starts With is another comparison: the value must begin with the supplied text. Contains can find that text later in the value as well.

The documented filter builder compares its Value text without regard to case. Changing Export Reports to export reports does not create a different case-sensitive requirement there.

That does not make all similarly named permissions equivalent. Equals and Contains still express different tests.

For entitlement criteria, check the **display name** used by the filter. Entering RPT.EXPORT is not automatically the same condition as matching the displayed label Export Reports.

Confirm the actual entitlement record, source, stored value and displayed label before accepting the result. If display names change, inspect the saved filter and its new matches instead of assuming it still expresses the intended selection.

## Account attributes belong to accounts

A person's department is identity information. An account can have its own attributes, such as a category used to distinguish temporary accounts.

An **Account Attribute** criterion identifies a source, an account attribute, an operation and a value.

Consider a separate example with just one source and one account per identity. The source has a collected account attribute named accountCategory:

- Identity 1601's account has accountCategory temporary and View Reports.
- Identity 1602's account has accountCategory standard and View Reports.

The review request excludes the temporary-account content from this campaign. With a supported Account Attribute exclusion for that source, accountCategory Equals temporary, the first account's matching review content is omitted. The second account's View Reports remains under these supplied conditions.

The attribute name and values must actually exist on the selected source. An identity attribute called Department is not automatically an account attribute available to the filter.

If one person has several accounts or access in other systems, inspect those generated items separately. Do not infer whether all their work is excluded or whether their other accounts are retained from this single-account example.

An account condition needs account evidence, not a guess based on a person's job title.

## Packages change which item can be filtered

An **access profile** groups entitlements from one source. A **role** can group profiles and direct entitlements, including access across sources.

Suppose Export Reports is held through a requested access profile that can be reviewed here, without a separate grant of the entitlement. Requested means the person received the package through an access request. The profile is the review item; its export component is not another standalone item.

An Entitlement filter for standalone Export Reports does not split it out of that package. **Standalone** means held outside the containing profile or role in the access arrangement being considered.

Use the appropriate **Access Profile** criterion when the reviewable object you need to include or exclude is the profile. Inspect the whole package: including or omitting it concerns its complete review scope.

The way the package was assigned still matters. Profiles granted through a role are not separate profile items. Profiles granted through a **lifecycle state**, the identity's configured status and associated access requirements, are not individually included in certifications either.

A filter cannot make an otherwise non-reviewable component into an independent review item.

## A source criterion is broader than one entitlement

The **Source** criterion addresses access associated with a selected system. The documented source-inclusion example includes entitlements and access profiles from that source.

For our original records, source-focused inclusion of Reporting Production would cover the View Reports and Export Reports holdings. It would not be a report-export-only selection.

Support Production's Read Cases belongs to another source.

Also remember that a role can contain access from several sources. A source condition does not establish that ISC will split a cross-source role into separately reviewable pieces.

Confirm the actual reviewable objects rather than treating a system boundary as a permission or package boundary.

## Check the intended effect of a role criterion

There are two different role-related requests:

“Leave this role item out of the review.”

“Leave everyone who holds this role out of the review.”

The second request also affects unrelated access belonging to those people. The first request concerns the role item.

Before relying on a **Role** criterion, establish its supported effect for the campaign you are creating. Check a role holder who also has unrelated access: did only the role item stay out, or did that person's other work stay out too?

Do not decide between those effects from the setting's name. If the required effect has not been established, the role-related scope is not yet verified.

Selecting a role as an access item to find its holders is also a different choice from applying a Role campaign-filter criterion. Confirm which control is being used.

## More conditions do not automatically mean a narrower filter

The documented filter builder treats its separate criteria as OR alternatives: matching any listed criterion is enough for that filter match.

For an exclusion filter, that means adding another criterion can exclude more content.

Do not assume that two criteria mean both must match. A Search query's grouping rules do not establish what the filter builder supports.

Mixed criterion types can affect different units, such as people and entitlements. Establish the actual grouping and resulting contents before using a combined rule.

A person condition can leave out all of that person's review work. An entitlement condition can omit one access item. Account for that difference when checking a combined filter.

## Check the generated result and the access outcome separately

A **preview** is generated campaign work available for inspection before the review starts. Use it to check the filter's real result.

For the export-inclusion example, look for 1501 and 1503's Export Reports holdings and confirm that the unrelated items are absent. For the export-exclusion example, confirm the three retained holdings, including 1503's Read Cases.

A **reviewer** is the person or group responsible for assessing the included access. Correct filter contents do not prove that the work reached a suitable reviewer.

If an expected item is absent, check the selected filter, its mode, source, criterion type, operation, value and the actual access arrangement.

Changing a saved filter definition does not, by itself, prove that existing generated work changed. Inspect the configuration and the work produced through the supported generation or correction process.

These examples concern the documented campaign-filter functionality where it is available. Available campaign types, permissions and actual source data still matter.

Finally, leaving Export Reports outside a campaign does not remove RPT.EXPORT from either application account. It also does not approve that permission's continued use.

The filter controls review content. A review decision records the assessment of included access. Any required account change needs its own supported action and verified result.

## Try a package and a changed label

A different review contains:

- Identity 1711's requested Warehouse Operator access profile, which contains View Stock and Adjust Stock.
- Identity 1712's standalone Adjust Stock entitlement.
- Identity 1713's Read Cases entitlement on Support Production.

View Stock permits reading recorded stock quantities; Adjust Stock permits changing them. The warehouse access belongs to Warehouse Production. Each supplied review object is otherwise eligible, with correct current account associations and suitable reviewers.

A separate review is planned for the standalone adjustment holdings. The request for this campaign is: “Leave standalone Adjust Stock decisions out. Keep the package and other access reviews.”

What does an Entitlement exclusion for Warehouse Production, Equals Adjust Stock, need to accomplish?

It omits 1712's standalone adjustment item. It does not split Adjust Stock out of 1711's Warehouse Operator profile. That profile and 1713's Read Cases remain in this supplied result.

Now change the request to leave all adjustment-bearing review objects out.

The profile also needs attention because it contains adjustment access. Excluding the whole profile would omit its viewing scope from this campaign too. Decide whether that broader omission meets the request and how any remaining required review will be covered.

The accounts' permissions have not been changed merely by leaving these items out.

Finally, the standalone entitlement's displayed label changes from Adjust Stock to Stock Adjustments. Its stored permission value remains STOCK.ADJUST. Inspection shows that the saved filter still compares the old display text using Equals.

That text condition no longer matches the new display name. An unchanged stored permission value does not make the old label comparison correct.

Correct the intended criterion through the supported process and check the generated work again. The evidence you need is the right review content, not merely a saved filter with a familiar name.
