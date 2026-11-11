# Start with people or start with access items?

Suppose you are asked to review access for the Finance team.

You would first need to find the people in Finance. Then you would decide which of their access needs review.

Now change the request: review everyone who can export reports, whichever department they belong to.

Starting with Finance would miss an Operations employee who also has export access. This time, the export permission is the useful starting point.

Both requests concern access. The difference is how you find the people whose access you need to review.

In SailPoint Identity Security Cloud (ISC), a **certification campaign** organizes this review work. It brings selected access to reviewers, who decide whether keeping it is appropriate. Before you create that work, you need a clear answer to two questions:

- Whose access should be reviewed?
- Which access belonging to those people should be reviewed?

Let's follow those questions through a small set of records.

## First, understand the information you are choosing from

An **identity** is ISC's record for a person. It can include information such as department and links to that person's application accounts.

An **account** is the record through which someone has access in an application. One person can have accounts in several applications. ISC connects to each managed system through a **source**, which holds its configuration and the account information collected from it.

A permission recorded as an **entitlement** describes a particular piece of access, such as membership of a group that allows report export. The application determines what that permission actually allows.

Here are the records available for our comparison. The numbers identify identities; they are not job titles or reviewer IDs.

| Identity | Department recorded in ISC | Account and source | Access on that account |
|---|---|---|---|
| 501 | Finance | rep-501, Reporting | RPT.VIEW: view reports; RPT.EXPORT: export reports |
| 502 | Finance | rep-502, Reporting | RPT.VIEW: view reports |
| 502 | Finance | case-502, Case Management | CASE.READ: read cases |
| 503 | Operations | rep-503, Reporting | RPT.EXPORT: export reports |

Read identity 502's two rows together. This is one person with two accounts. The Reporting permission and the Case Management permission belong to different accounts, but both accounts are linked to identity 502.

For this example, the account links are correct, the collected permissions agree with the current application records, and the departments are correct. Each listed permission is separately reviewable. No access package, automatic requirement or exclusion changes how these permissions appear.

## Start with people when the question names a group of people

Our first request is:

“Review the access of people in Finance.”

You select **Identities** as the campaign's starting point. A **query** is a search instruction used to find records that match a condition. Here the condition is that the identity's department is Finance.

The matching identities are 501 and 502.

Identity 503 is outside this selection because its department is Operations. It does not become a Finance identity just because it shares a permission with identity 501.

The query has answered the first question: whose access are we considering?

It has not yet answered the second question: which of their access should be reviewed?

You can choose **Certify All Access**, or narrow the access through **Refine Access Items**. Refining means keeping only the access items needed for the intended review.

For this comparison, choose all access. With the reviewable permissions and other conditions supplied above, the generated work contains:

- Identity 501: RPT.VIEW and RPT.EXPORT on rep-501.
- Identity 502: RPT.VIEW on rep-502 and CASE.READ on case-502.

There are two people and four permission holdings in this supplied result. A *holding* here means a particular person has the permission through the named account.

Why is CASE.READ included? We selected identity 502 and then chose all access. We did not restrict the access to Reporting. Identity 502's Case Management access therefore belongs in this example's result too.

The word Finance selected people. It did not select an application or a permission.

## Start with access when the question names what people hold

Now use the second request:

“Review the people who hold Reporting export access, wherever they work.”

You select **Access Items** as the starting point, then find the RPT.EXPORT entitlement belonging to the Reporting source.

You are choosing an access object: ISC's record describing that permission. It is different from each account's record of having the permission.

There is one selected entitlement definition. In our data, two people hold it: identities 501 and 503. ISC can use the selected access to establish the people included through this route.

Identity 502 is absent because neither of its accounts has this export permission.

Department did not determine this selection. Identity 503 is included because it holds the chosen permission, even though it belongs to Operations.

Now comes a choice that is easy to overlook. This route also lets you choose all access or refine the access for the resulting people.

Again, choose all access so that we can compare the same setting. The supplied generated work contains:

- Identity 501: RPT.VIEW and RPT.EXPORT on rep-501.
- Identity 503: RPT.EXPORT on rep-503.

Notice RPT.VIEW for identity 501. We started with export, but the later choice brought that person's other reviewable access into the campaign as well.

The selected export entitlement helped find the people. It did not, by itself, guarantee an export-only review.

## Compare the actual results

| Selection and later access choice | People included in this example | Permission holdings in this example |
|---|---|---|
| Finance identities, then all access | 501 and 502 | 501: Reporting view and export; 502: Reporting view and Case Management read |
| Reporting export entitlement, then all access | 501 and 503 | 501: Reporting view and export; 503: Reporting export |

Both selections produced two people. They did not produce the same people.

A total of two cannot show you whether identity 502 or identity 503 was included. You need the actual identity references.

The access contents differ too: four holdings in the first result and three in the second. These counts describe our supplied records. They are not a rule for how many certifications, screen rows or accounts every campaign must create.

A **certification** is the assigned review work within a campaign. A **review item** is an access item presented for a decision. ISC may organize that work according to the campaign and reviewer configuration, so inspect the generated work rather than calculating its grouping from these example counts.

The relationship to follow is:

```text
Decide what the review must answer
                 |
       +---------+----------+
       |                    |
       v                    v
Select identities     Select access objects
       |                    |
       |             Find their included holders
       |                    |
       +---------+----------+
                 |
                 v
       Resulting people in scope
                 |
                 v
       Choose their access to review
       (all eligible access or refine)
                 |
                 v
       Inspect generated people,
       access items and reviewers
```

Follow either branch down. Both lead to people whose access is in scope. Both still need an access-scope choice. Finally, the generated work tells you what was actually included and who received it.

The arrows show how to reason through the choices. They do not describe private services inside ISC or the exact order of its background jobs.

## What if the request needs both conditions?

Suppose the request is more specific:

“Review only the Reporting export permission of Finance people who hold it.”

Return to the table. Identity 501 meets both conditions. Identity 502 belongs to Finance but lacks export access. Identity 503 has export access but is outside Finance.

Neither of our two earlier results meets this narrower request.

The first selected Finance people and included their other access. The second included an Operations holder and also identity 501's view permission.

You need selection that respects both the intended people and the intended access. The supported query and refinement choices must be configured to produce that result. Then check that the generated work contains identity 501's Reporting export holding, without the extra people or permissions.

Refining access is therefore a separate decision with a practical purpose: it prevents a correctly selected person's unrelated access from becoming review work.

Do not assume that a precise-sounding campaign name supplies those conditions. Naming a campaign “Finance export review” does not make its saved selection match those words.

## Look at what the query returns

A search can use access information while still returning identities.

For example, you could search identity records for people who hold the chosen Reporting export entitlement. The condition concerns access, but the returned records are people. That is still identity selection.

Alternatively, you could search entitlement records and select the export entitlement itself. The returned record is the access definition; its included holders are determined through the access-item route.

Ask: “Am I selecting person records, or am I selecting permission or package records?”

The answer comes from the record type and results, not from whether the word export appears in your query.

Also distinguish all matching results from specific results you selected. If a query returns three access objects but you add only one, you have chosen that one object. Finding something in a search does not necessarily mean it was added to the campaign.

Use the exact source and object reference when confirming the choice. Two systems can both have a permission called Export. Selecting the test system's Export permission does not select the production system's permission.

## Packages change which object you need

So far, each entitlement was held separately. Real access can also be grouped.

An **access profile** groups entitlements from one source into an access package. A **role** can group access profiles and direct entitlements, including access across sources.

Suppose identity 504 has Reporting export through a Reporting Analyst access profile. Export is a component of that package.

If you select the export entitlement as a standalone item, you cannot assume identity 504 will be included through that selection. *Standalone* means held outside a containing access profile or role for the selection being considered. Access held through a package needs the appropriate containing object selected.

The same issue can occur one level higher. If an access profile comes through a role, selecting only the profile does not establish that the role's holders will be included.

This explains why “everyone who can export” needs more thought than finding an entitlement with Export in its name. You need to know how people hold that access.

Look at the entitlement, any containing profile or role, and the person's actual access records. If ISC has detected a full set of entitlements as an access profile, treating that person as holding only standalone entitlements can also give the wrong expectation.

You are trying to match the review to the real access arrangement. A shared capability does not guarantee that everyone has the same separately reviewable object.

## Reviewing role holders is different from reviewing the role's design

An access-item campaign can start with a role to find people who hold it. The question is whether those people should keep that access.

Where role-composition campaigns are available, that campaign asks a different question: is the role itself designed appropriately? It can examine the access included in the role and its membership criteria, which are the conditions used to determine membership.

Selecting a role in one context does not make these two review purposes interchangeable.

The way the person received the role also matters to the available decision. A role obtained through an access request, a submitted request to receive that access, can be approved or revoked in a review. A role assigned through automatic membership criteria can only be acknowledged there. Acknowledge records that the reviewer has seen it; it does not remove the role. The membership criteria still control whether the person receives it.

Choosing the right starting object does not change those controls.

## Before sending the campaign to reviewers

A **preview** is generated review work you can inspect before starting the campaign. A saved query or a saved template contains instructions; it is not proof that the intended people and access reached that work.

Use the business request to check the preview. For the export-only Finance request, look for the actual identity, source, account and access references. Check an expected inclusion and a deliberate exclusion: why is 501 present, and why are 502 and 503 absent?

If an expected person is missing, follow that person's evidence. Is the department correct? Is the right account linked to the right identity? Was the permission collected? Is it part of a profile or role? Was the correct object actually selected? Does an access restriction remove it?

An empty search result only tells you that the search found no matching records under its conditions. It does not prove that nobody has the permission in the application.

There is another boundary: people-based selection does not establish coverage of every account in a system. An uncorrelated account has not been linked to a person identity in ISC. Service or machine accounts may need an account-focused review route with its own requirements. Do not treat missing people-based results as a complete account inventory.

Reviewer selection remains a separate responsibility. The **reviewer** is the person or group assigned to judge the access. Being included for review does not mean a person should review their own access.

For our comparison, assume a suitable authorized reviewer outside the selected population is assigned in both campaigns. In actual work, the available reviewer choices depend on campaign type. Check the generated assignee as well as the contents.

These examples follow the Search campaign choices where the described functionality is available. A tenant's available engine and campaign types determine which choices it offers; the business question and the actual generated result still need to agree.

## Try a different access object

You receive this request:

“Review the Production Deploy role for everyone who holds it, including contractors. Include only that role in this review.”

The supplied records show:

- Identity 701 is an employee and holds the requested Production Deploy role.
- Identity 702 is a contractor and holds the same requested role.
- Identity 701 also holds a separate Reports View access profile.
- The role and profile are reviewable here, with correct account associations and no rule or exclusion changing the supplied result.

The Production Deploy role gives access needed to deploy software into production. Its ISC record describes the role. Identities 701 and 702 each have a holding of that role.

Consider a proposal to select employees and choose all access. Would it meet the request?

First compare the people. An employee-only selection misses contractor 702 even though 702 holds the role and is explicitly included in the request.

Then compare the access. All access for identity 701 can also bring in the separate Reports View profile. The request asks only for the deployment role.

An appropriate design must include both role holders and restrict the review to the intended role holdings. Selecting the role through the supported access-item route is a useful starting point; you still need the later access choice and generated work to match the role-only requirement.

One selected role definition does not mean one person. There are two supplied holders. Nor does it mean you are reviewing the role's internal design: the request concerns whether each holder should keep it.

Now add identity 703. This person has one of the role's component permissions directly, outside the role, but does not hold the role itself.

Should 703 automatically join this role-holder review?

No. Having one permission that is also used inside a role does not establish a holding of that role. The request names role holders. You would need evidence of that holding to include 703 on that basis.

If the request changed to “review everyone with production deployment capability,” you would investigate the direct permission and other ways of receiving that capability too. You could no longer assume that the role-holder population answers the whole question.

That is the decision to carry into campaign design: first establish what the request means, then choose the records and access that actually answer it.
