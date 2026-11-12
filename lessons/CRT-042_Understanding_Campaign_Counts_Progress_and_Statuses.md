# What are the campaign's counts and statuses counting?

Someone reports that a campaign is “62.5% complete.”

Before using that number to decide what to do next, ask what complete means there. It could describe item choices, finished assigned reviews or some other measured work.

The calculation can be correct while the conclusion drawn from it is wrong. A useful progress statement names what was counted, which work was included and what qualified as finished.

## Start with the thing being counted

In SailPoint Identity Security Cloud, or **ISC**, a **campaign** organizes access reviews. A **certification** is an assigned review within it. A **review item** is an access entry on which a reviewer records a decision.

An **identity** is ISC's record for a person or another managed subject. An **account** is the record through which that person or service uses an application. **Access** means what the account is allowed to do.

For example, Read Cases allows viewing case records. Export Cases allows downloading case records in bulk. Those are different permissions and can require different decisions.

A **subject** is the person or other object being reviewed within the certification. In an identity-oriented review, the subject is the identity whose access is being examined. One subject can have multiple review items, including access from more than one account.

The reviewer can therefore make several decisions for one subject. Completing one item is not the same amount of work as completing every item for that subject.

Likewise, one certification can contain more items than another. Counting certifications gives each assigned review one unit; counting items gives each item one unit.

## Follow one set of counts

Suppose an identity-oriented campaign is active. Its intended contents, account associations and individually reviewable permissions have been checked. The reviewers are suitable, authorized and independent of the access being reviewed.

At the same observation time, you inspect these records:

| Assigned review | Identity subjects | Review items | Saved item choices | Signed off |
|---|---|---|---|---|
| A | Two | Four | Three | No |
| B | One | One | One | Yes |
| C | One | Three | One | No |

The four identity subjects are distinct in this example. These are supplied counts from inspected records, not a reproduction of a particular ISC screen or its percentage formula.

For A, the first subject has two items and both have choices. The second subject has two items, but only one has a choice.

For B, the single subject's single item has a choice. For C, its subject has three items and only one has a choice.

Add the actual item counts:

- There are eight items: four in A, one in B and three in C.
- Five have choices: three in A, one in B and one in C.
- Three still need choices: one in A and two in C.

You can calculate the share of items with choices as:

**5 ÷ 8 × 100 = 62.5%**

Five is the **numerator**, the number meeting the condition you are measuring. Eight is the **denominator**, the whole included set against which you compare it.

Here, the condition is “has a saved choice.” The accurate statement is “five of eight items have saved choices,” or “62.5% of these items have choices.”

That calculation has not counted final review confirmation or access removal.

## Change the unit, and the answer changes

Now count subjects whose items all have choices.

A has one such subject, B has one and C has none. That gives two out of four subjects, or 50%.

Next, count signed assigned reviews. **Sign-off** is the reviewer's final confirmation of the decisions. In ISC's newer, next-generation certification experience, saving choices and signing off are separate actions.

Only B is signed off. That is one out of three assigned reviews, or approximately 33.3%.

The same records therefore support these statements:

- Five of eight items have choices.
- Two of four subjects have choices for all their items.
- One of three assigned reviews is signed off.

The numbers differ because the units and finishing conditions differ. There is no contradiction to resolve.

These calculations explain the supplied records. They do not define every percentage that ISC might display. For an actual screen or report, establish what its label and documented fields measure.

The diagram shows the different counting levels. The links describe containment and separate evidence, not an order in which every ISC process runs.

```text
One campaign
     |
     +--> 3 assigned certifications
               |
               +--> 4 subjects in this example
                         |
                         +--> 8 review items
                                   |
                                   +--> 5 saved choices

Separate checks:
  Subjects with all choices:       2 of 4
  Signed assigned reviews:        1 of 3
  Verified due removals:          check actual work/account
```

In other reviews, adding subject entries is not automatically a count of distinct people. Identify the type of subject and its actual identifier before calling the result a people count. A role groups access for a job or responsibility. A role-composition review examines that group's contents rather than an employee's access; the documented route for that review uses the older, legacy engine.

A count of assigned review records also does not, by itself, establish how many distinct people are assigned to them. Use the actual assignments when that is the question.

## A completed flag can describe item choices

An **API** is an interface through which software reads information or requests an operation. Its returned fields have meanings tied to particular records.

The documented next-generation Certification model separates the following information. These are the documented model's property names, rather than instructions to build an API request.

| Model property | What it describes |
|---|---|
| DecisionsMade and DecisionsTotal | The number of recorded choices and the total decisions in that assigned review |
| Completed | Whether all certification decisions have been made |
| CompletedSubjects and TotalSubjects | Subjects whose item decisions are all complete, compared with all subjects in that review |
| DateSigned | The recorded sign-off date; omitted until the review is signed off |

The recorded choices can be Approve, Revoke or Acknowledge, according to what the reviewed item permits. **Approve** accepts continued access under the reviewed conditions. **Revoke** records required removal. A Revoke still counts as a choice; a decision count is not an approval count.

Some roles are assigned automatically because a person's information matches membership rules. **Acknowledge** records examination of such a role assignment. It counts as a recorded choice, but does not remove the role or override its assignment rule.

Return to A. Suppose its reviewer now makes the missing choice. A has four choices out of four, and both subjects have choices for all their items.

Under the documented model, A can now have Completed set to true while DateSigned is still absent. All item choices exist, but the reviewer has not yet given final confirmation.

The whole campaign now has six choices out of eight. Its signed-review count is still one out of three.

If A's reviewer then successfully signs off, the signed-review count becomes two out of three. The saved-choice count stays six out of eight. Signing did not create an additional item decision in this example.

This is why a completed flag needs its field meaning attached to it. Reading it as “the reviewer signed” would skip the separate sign-off evidence.

## Find the owner of a status label

A **status** records the state of a particular object or operation. Before interpreting it, identify that object.

The next-generation CampaignSummary model has TotalCertifications, CompletedCertifications and the campaign's Status. Those fields concern the campaign and its assigned certifications. They are not item-decision counts.

Do not assume that a campaign aggregate's completed count uses exactly the same condition as an individual review's Completed flag. Use the actual field's supported meaning and the underlying review records when checking sign-off.

The Campaign Status Report has a field called **Decision Made**, whose values describe item status, including Open, Complete and Error. Its separate **Decision** field describes the choice made.

A Complete value on an item row is not the campaign's completed state. It also does not prove that rejected access has disappeared.

Removal work has another result. **Remediation** means carrying out a required access removal. The Campaign Remediation Status Report can show Finished following confirmation on a connected source or closure of a manual task or service desk ticket.

For B, suppose its one choice is a signed Revoke for Export Cases. Removal is due, but reliable current evidence shows the correct application account can still export. All other saved choices in this example are justified approvals.

B's reviewer has finished, but this removal has not achieved its result. For B alone, there is one signed assigned review and zero verified removals out of its one due requirement.

Raising a review-completion figure does not resolve that account problem. Follow the matching removal operation or task and verify the actual permission.

Similarly, an Error label needs the affected record and its details. A report-item error, a campaign-generation error and a failed application change are different starting points for investigation. The word alone cannot identify the repair.

## Check which work the number includes

A useful comparison uses the same campaign, included records, actor scope and observation time.

A filtered view may show only one reviewer or only unfinished work. A list may show one page of results. **Pagination** means returning a larger collection in portions; the rows on the current page may not be the whole collection.

Before using visible rows as the denominator, establish the full included set. A page of ten rows does not prove that the campaign contains ten items.

User scope matters too. The documented next-generation status-summary operation returns information about certifications owned by the signed-in user. It includes active-certification and completed/pending decision counts.

That is not automatically the selected campaign's total or the whole organization's review population. Permission to call an operation and the population it summarizes are different facts.

Date conditions can also overlap with work states. Suppose four reviews are active and two of those four are overdue. **Overdue** means their due date has passed. There are four reviews in that supplied set, not six. The overdue two are part of the four, rather than an additional group.

Use the actual field definitions before combining native counts. Do not assume every pair of labels describes separate groups.

A report has its own observation time. If the campaign changes, generate the report again to see its updated state. Downloading an old file again does not update its contents.

Even a newly generated review report does not prove that the application account was observed at that same moment. Keep the account evidence's own time with a removal conclusion.

## A zero count still needs an explanation

Suppose your selected view contains no review items.

For the ordinary fraction “decided items divided by total items,” the denominator is zero. You cannot use that calculation to claim a meaningful completion percentage.

Find why the set is empty. The selection or filter may exclude the intended records, you may be viewing the wrong campaign, or the relevant data may be missing. Establish the actual cause from evidence.

Likewise, zero pending decisions does not by itself establish sign-off, correct review coverage or completed removal. It answers a narrower question about decisions in the set being counted.

For the intended review requirement, confirm who and what should have been included as well as what the current counters contain.

## Try a changed set of records

An active campaign has two assigned reviews.

X contains nine items, none with a choice. Y contains one item with a saved choice. Neither review is signed off.

An analyst filters the records to Y and reports, “All the items are decided, so the campaign is 100% complete.”

Another person looks at each review separately. X has 0% of its item choices made; Y has 100%. They average those two percentages and report 50%.

Which calculation answers the share of the whole campaign's items with choices?

Start with the included set. Y alone has one choice out of one item. That is 100% for the filtered one-item set. It cannot describe the other nine items.

Across X and Y, there is one choice out of ten items: **1 ÷ 10 × 100 = 10%**.

Averaging 0% and 100% gives each review equal weight, even though X contains nine items and Y only one. Adding the actual item counts answers the item-level question.

The signed-review count is zero out of two. Neither the 100% filtered figure nor the 10% whole-set figure establishes final review confirmation.

Now Y's reviewer signs off successfully. The campaign still has one saved choice out of ten items, while one of two assigned reviews is now signed. The count changed at the review-confirmation level.

Finally, someone downloads a report today and supplies an account extract made yesterday. The newer report download time does not prove a permission changed today.

The useful progress statement identifies the actual set and result: one of ten items has a choice, one of two assigned reviews is signed, and any required account change still needs its own current evidence.
