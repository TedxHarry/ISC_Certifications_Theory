# What was captured when this review was generated?

An account has three permissions today. You open its access review and find only two.

You might first think that the review is broken. Before reaching that conclusion, check when the third permission was added and when the review was generated. Also check whether ISC had collected that permission before generation.

Those questions matter because a review and the account being reviewed are different records. The account can change while people are still working on the review.

## Start with the account, then the review

An **account** is a record used to access a system. A person might have an account in a reporting application, for example.

A permission determines something that the account is allowed to do. ISC can represent a permission as an **entitlement**. View Reports could allow reading reports, while Export Reports could allow downloading their contents.

A **source** is ISC's representation of a connected system or account-data collection. Through that connection or a data load, ISC collects account information. Collecting account records is called **account aggregation**.

ISC also needs to know which person owns an account. Connecting an account to the person's ISC **identity**, their person record, is called **account correlation**. A permission collected on an account is not automatically evidence that it belongs to the intended person. That account-to-person connection must be correct.

An **access review** asks someone to assess access. The **reviewer** is the person responsible for making that assessment. A **review item** is a particular access holding presented for a decision: for example, identity 2001's Export Reports entitlement on account rep-2001.

A **certification campaign** organizes review work. Generating the campaign creates that work from the selected scope and the data used for generation. The campaign settings describe what should be reviewed; the generated reviews show what was actually included.

Keep that last distinction in mind. An instruction to review access and an actual list of access awaiting decisions are two different things.

## Follow one review from its starting point

Consider a dedicated Manager Campaign. Its purpose is to let managers review their employees' access.

In this example, identity 2001 belongs to a person whose manager is identity 2101. The person's Reporting Production account is rep-2001. It has two permissions:

- View Reports, which allows reading reports.
- Export Reports, which allows exporting report contents.

Both permissions are individually reviewable entitlements here. They are not contained in an access profile or role, which are ways of grouping access, and no automatic access requirement changes the example.

Before generation, the administrator, who configures and manages the campaign, confirms that ISC has collected both permissions, linked the account to identity 2001 correctly and recorded manager 2101. The campaign is intended to review this person's eligible access, rather than only one named permission. The required people and access are included in its scope.

The administrator generates campaign C-1. These labels simply help us distinguish the example records.

On inspecting the generated work, the administrator finds review R-1 assigned to manager 2101. It contains two items: View Reports and Export Reports for identity 2001.

Now the reviewer has a definite list to work through. Generating the campaign has not granted either permission. Those permissions already existed; generation has created work to assess them.

## What changes after generation?

Later, someone grants Manage Report Settings to account rep-2001. This permission allows changing the reporting application's configuration.

The person also moves under manager 2102.

There are now several facts to check separately. The target application confirms that the account has all three permissions. A later completed collection confirms those permissions in ISC, and the person's current ISC identity records manager 2102.

The administrator then inspects the existing review R-1. In this example, it still contains its original two items and is still assigned to 2101.

| Record inspected | What is found |
|---|---|
| Current Reporting Production account | View Reports, Export Reports and Manage Report Settings |
| Current ISC account and identity information | Three permissions; manager 2102 |
| Existing review R-1 | View Reports and Export Reports; assigned to 2101 |

Each row answers a different question.

The first tells us what the application account currently has. The second tells us what ISC currently knows. The third tells us what work exists in this particular review.

Finding three permissions in the first two places does not, by itself, prove that the third permission has been added to R-1.

For the dedicated Manager/Source Owner campaign route, SailPoint describes generation as a **snapshot in time** and explicitly notes that managers added after generation do not appear in that generated campaign. In this context, a snapshot means that generation establishes review work at a particular point.

That gives us a reason to inspect the existing assignment instead of assuming that a later manager update rerouted it. It does not establish that every displayed field is permanently frozen in every campaign type. A particular label, identity detail or other field may behave differently. Check the behavior for the campaign route and field involved.

The important practical question is precise: **what does this existing review actually contain now?**

## Follow the records through time

```text
BEFORE GENERATION
Source account: View Reports + Export Reports
        |
        | collected and linked to identity 2001
        v
Confirmed ISC inputs: those two permissions; manager 2101
        |
        | campaign C-1 is generated
        v
Review R-1: two items; assigned to 2101

LATER, TWO RECORDS ARE INSPECTED
Current source and ISC data        Existing review R-1
Three permissions:                Two original items:
  View Reports                      View Reports
  Export Reports                    Export Reports
  Manage Report Settings          Still assigned to 2101
Current manager: 2102

SUPPORTED WORKFLOW CHANGE
Responsibility for R-1 is reassigned to 2102
        |
        v
New campaign report: current reviewer 2102
Earlier decision remains recorded as made by 2101

A new report describes campaign work.
It does not itself add the third permission to that work.
```

The upper part follows the data used to generate the original work. Two permissions were collected and linked to the person, then two review items were found in R-1.

The middle part compares later records. The current account and ISC data have changed. The existing review still has its earlier contents in this example.

The lower part shows a different kind of change: changing who is responsible for the review. We will follow that change shortly.

The arrows do not mean that every permission change automatically travels into an existing review. Each arrow describes the action written beside it.

## A newly generated campaign can still use old information

Suppose a permission was granted before campaign generation, but ISC had not collected it yet.

The permission existed in the application. It was missing from the information available for the review.

Generating a campaign today does not establish that every source was read today, or that every included record describes exactly the same moment. You need to check the observations behind the data.

There are three times worth keeping separate:

1. **Source observation:** when the account and its permissions were actually observed or collected.
2. **Review generation:** when the campaign's review work was created.
3. **Report generation:** when a report describing campaign work was produced.

For a campaign created through Search, there is another useful check: whether the required information was available in Search when the selection was made. Search finds identity and access records using information prepared for searching. A change elsewhere in ISC may take time to appear there.

You do not need to guess how many minutes the update should take. Look for the actual changed value in the place used for selection, then inspect the generated work.

For example, a successful account collection is useful evidence that a source was processed. It is not enough, on its own, to prove that the expected permission was collected, attached to the correct account and connected to the correct person. Inspect those particular records when coverage is in doubt.

A recent generation date cannot repair missing inputs.

## Does the old review now cover the person's current access?

Return to R-1. Its two original items can still be valid records of the access selected when it was generated. But the campaign's original list and the person's full current access are no longer the same list.

If the requirement is to review the person's current reporting access, Manage Report Settings needs attention. Finishing decisions on View Reports and Export Reports would not establish that anyone assessed the third permission.

First establish the requirement. Is the review intended to assess the access selected at generation, or must the process also cover access added during the review period? The organization needs a clear rule for that situation.

Then compare the required access with the actual review work. Depending on the campaign's state and supported options, the administrator may need corrected or additional review work. Confirm its contents after creation.

Do not treat “snapshot” as permission to ignore a gap. It explains why two records can differ; you still have to decide whether the review meets its purpose.

## A manager change and a review reassignment are different actions

Manager 2102 is now recorded on the person's identity. That describes the current reporting relationship.

Review R-1 is still assigned to 2101 in this example. That describes responsibility for existing review work.

To move that responsibility, an authorized administrator uses supported **reassignment**: changing the person responsible for a review.

**Sign-off** means the reviewer confirms or finalizes their assigned review's decisions. A saved decision and sign-off are separate events.

For this example, the campaign is active, R-1 has not been signed off, and 2102 is a permitted reviewer who would not be reviewing their own access. The administrator reassigns R-1 and checks that its current reviewer is now 2102.

A signed-off review cannot be reassigned using this action.

The manager field and the assignment now agree, but that agreement has a specific explanation: the existing review was reassigned and the result was checked. A manager-field change alone was not evidence of that action.

The new reviewer also needs enough current business information to assess the access. Correct assignment helps put the work in the right hands; it does not automatically tell that person whether Export Reports is still needed.

## Some review information is expected to change

Before reassignment, suppose 2101 had saved an Approve decision for View Reports. Approve records the reviewer's decision that the access should be retained.

After reassignment, 2102 is the current reviewer. That does not mean 2102 made the earlier decision.

A campaign status report can distinguish the **current reviewer** from the **decision maker**, the person who actually recorded a decision. In this example, the current reviewer is 2102, while the earlier decision was made by 2101.

There is no contradiction. One field describes present responsibility; the other describes a recorded action.

This is why “snapshot” must not be understood as “nothing in a campaign can ever change.” Decisions can be recorded and supported reassignment can change responsibility. Those changes are different from adding later source access to the review's contents.

Likewise, an access decision is not evidence that the target application has already changed. If a reviewer chooses Revoke, that records a removal decision. Actual removal and confirmation of the resulting account state require their own evidence.

## Why a new report can still show the old two items

A report is a view of campaign information. Its generation date tells you when that report was produced.

Suppose the administrator downloaded a report before R-1 was reassigned. That downloaded file does not rewrite itself when the assignment changes. The administrator needs to generate a fresh report to see the latest campaign state.

After reassignment, the new report can show 2102 as the current reviewer and preserve 2101 as the earlier decision maker.

But R-1 still has two review items in this example. Producing a report after the account gained a third permission does not itself create an item for that permission.

Think of the question each action answers:

- Inspecting the current source account asks, “What access does the account have now?”
- Inspecting the existing review asks, “What access is included in this review?”
- Generating a fresh campaign report asks, “What does the campaign currently record?”

A report produced today can describe review work generated earlier. Its recent date does not turn that earlier work into a complete assessment of all access held today.

## What if the generated preview is already old?

A **preview** lets the administrator inspect generated campaign work before starting the review for reviewers.

The dedicated Manager/Source Owner campaign guidance recommends starting within a day of preview generation and planning to delete and recreate a preview if it is older. This is guidance for that route, rather than a universal rule that every campaign expires after 24 hours.

The reason is understandable: the longer generated work waits, the more opportunity there is for access or reporting relationships to change before anyone starts reviewing.

Before replacing work, check its actual state and preserve required evidence. Deleting a campaign can lose its decisions and reports. An unused preview and a campaign containing review activity need different consideration.

Also distinguish generating later from generating now and starting later. A schedule for future generation determines when work is to be generated; an already generated preview contains work that has already been created. A date on a schedule is not proof that generation completed or that reviewers can already act.

After any supported correction or new generation, inspect the resulting people, accounts, access and assignments. A changed setting or a completed generation action is not a substitute for checking the work you intended to create.

## Try a different missing-access problem

A Warehouse Production campaign, W-1, is intended to review the selected people's warehouse access.

Its generated work contains one item: identity 2201's View Stock permission, which allows reading stock information.

Later investigation establishes these facts:

- Identity 2201 gained Adjust Stock after W-1 was generated. Adjust Stock allows changing stock quantities.
- Identity 2202 already had Adjust Stock before W-1 was generated. However, the account and permission were not collected and linked to 2202 in ISC until later.
- Both people were within the intended selected population. The permissions are individually reviewable, and no access-package or filter exclusion explains their absence.
- Current source and ISC observations now confirm three holdings: 2201 has View Stock and Adjust Stock; 2202 has Adjust Stock.
- Inspection of W-1 still finds only its original View Stock item. A newly generated report also contains only that item.

Why are the two Adjust Stock holdings absent? Does the new report prove that the report is broken? What evidence would support a review of all three current holdings?

### Work through the two omissions separately

For 2201, the access changed after generation. The original work could not assess an access holding that the person had not yet received.

For 2202, the permission existed before generation, but the relevant account/access information had not reached ISC and been linked to that person. The original inputs were incomplete for the intended review.

These are different causes. Calling both a snapshot would hide the second problem: a review can capture the information available to it and still fail to cover access that should have been known.

The new report's single item agrees with the inspected campaign work. Its recent generation date does not make the missing permissions part of W-1, so the item count alone does not establish a reporting fault.

To investigate, compare the actual source grant history, relevant collection and account-link evidence, generated contents and report date. Do not infer when access was granted merely from when ISC first displayed it.

If the requirement is now to review all three current holdings, confirm the current inputs and arrange supported corrected or additional review work. Then verify that the resulting work contains the intended person, account and permission for each of the three holdings.

Changing a filter or generating another report would not, by itself, establish that coverage.

When records disagree, identify the record, the time it represents and the action that could change it. That gives you a reason for the difference and a clear next check.
