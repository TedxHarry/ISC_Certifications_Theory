# A template, a schedule and a running campaign are different things

You save a campaign and choose a date for it. On that date, a reviewer says there is no review to work on.

Where would you look first?

Check what the date was meant to trigger. In the Search campaign creation flow, scheduling a campaign preview arranges its generation. An administrator still needs to start the generated campaign.

A saved plan, a request to prepare review work and work that reviewers can act on are different stages. Let's follow them in order.

## First, what are we preparing?

An access review asks someone to decide whether people still need particular access. That person is the **reviewer**.

A **campaign** organizes the reviews. Within it, a reviewer receives an assigned review, also called a **certification**. Each **review item** identifies access to assess, such as one person's permission to export reports from a particular account.

The person configuring and managing the campaign is an administrator. They need permission to perform the relevant certification actions. Being named as the campaign owner, the person responsible for the campaign, does not by itself establish every administrative permission.

Before anyone reviews access, the administrator specifies who and what should be reviewed, how reviewers should be chosen and the settings for the work.

Those instructions need to become actual review items and assignments. ISC calls that preparation **generation**.

Generation and reviewer decisions do different jobs. Generation prepares the work; reviewers later assess it.

## A template keeps instructions you want to use again

Suppose you need to review Reporting Production access for identities 2301 and 2302. An **identity** is ISC's person record.

Each person has an account, their record for accessing that application:

- Account rep-2301 belongs to identity 2301 and has View Reports, which allows reading reports.
- Account rep-2302 belongs to identity 2302 and has Export Reports, which allows exporting report contents.

ISC represents these permissions as **entitlements**. In this example, both are individually reviewable. Neither is contained in a role or access profile, which are ways of grouping access.

In ISC, a **source** represents a connected system or collection of account data. Here, account collection has brought the Reporting Production accounts into ISC and linked them to the correct people. Campaign generation needs those records to know which person has each permission.

The administrator saves template T-1 using the Search identity-campaign route. T-1 contains the selected identities 2301 and 2302, their eligible access scope, reviewer choice and review settings.

Here, **template** means a reusable campaign definition: saved instructions for preparing campaign work. The administrator can use it again instead of rebuilding the same configuration.

For this example, the saved selection contains those two specific identities. The access choice covers all their eligible access. The supported Individual reviewer option selects identity 2391, a permitted reviewer who is not reviewing their own access. Identity 2390 is the campaign owner.

T-1 is only an example label. The useful distinction is between the saved definition and a particular campaign generated from it.

At this stage, the administrator has chosen to save the template without generating a preview. There is no generated review from this action for reviewer 2391 to complete.

Saving the instructions has not granted or removed either reporting permission.

## A schedule says when to prepare the work

Now the administrator schedules T-1 to generate a preview tomorrow morning in the chosen time zone.

A **schedule** supplies timing instructions for generation. It can arrange one future occurrence or recurring occurrences, meaning generation is planned to repeat.

For example, a monthly review process needs a new review cycle each month. A recurring schedule avoids having to request every generation manually. It does not decide whether the resulting contents are correct.

We will call T-1's timing instructions S-1. This label helps us discuss the example; you do not need to expect a separate schedule ID displayed in every interface.

After saving S-1, the administrator checks the scheduled date, time zone and recurrence. This proves what is planned. It does not prove that tomorrow's generation has already happened.

The same applies after the planned time passes. The clock reaching a scheduled time is not evidence that a usable preview was successfully produced. Look for the actual resulting campaign.

## What appears when generation finishes?

Suppose the scheduled generation completes and produces campaign C-1 in preview.

A **preview** is generated campaign work available for administrative inspection before reviewers begin. It is more than a summary of the instructions: you can inspect the people, access and reviewer assignments that were actually produced.

In C-1, the administrator finds:

| Person and account | Access item found | Assigned reviewer |
|---|---|---|
| Identity 2301, rep-2301 | View Reports | 2391 |
| Identity 2302, rep-2302 | Export Reports | 2391 |

These are supplied results for our example. They show two intended items and the expected reviewer.

Why inspect them when the template already names the people and reviewer?

Because a correct instruction and a correct result are different pieces of evidence. Missing account data, an incorrect person-account connection or a changed access situation can affect what there is to review. A saved name or item count alone cannot settle that.

The administrator compares the actual contents with the intended review. They also check that the reviewer and review settings are appropriate before starting.

If an item is missing, investigate the relevant selection, collected access and reviewability. Starting a campaign does not make a missing item appear merely because it was expected.

## Starting makes the prepared work available for review

Once C-1 is ready, an authorized administrator starts that campaign.

Starting is also called **activation**. It moves the campaign into the stage where its assigned reviewers can perform their review work.

The actions are connected:

```text
SAVED TEMPLATE T-1
People/access selection + reviewer choice + review settings
        |
        | schedule requests generation at a future time
        v
GENERATION WORK
        |
        | actual completed preview is inspected
        v
CAMPAIGN C-1 IN PREVIEW
People + accounts + access items + assigned reviewers
        |
        | administrator checks and starts this campaign
        v
CAMPAIGN C-1 RUNNING
Reviewers can work on its assigned reviews

LATER REUSE OF T-1
        |
        | another generation completes
        v
SEPARATE CAMPAIGN C-2 IN PREVIEW
Inspect this cycle's contents and assignments
        |
        | its own authorized start, then result checked
        v
CAMPAIGN C-2 RUNNING

The schedule triggers generation.
Each generated campaign needs its own verified start.
```

Follow the first path downward. The template supplies the instructions. The schedule determines when generation should be requested. Completed generation gives the administrator actual campaign work to inspect. The administrator then starts that particular campaign.

The second path shows a later cycle. Another generation creates a separate campaign, C-2. It needs its own contents check and start.

In the Search interface, Preview Ready identifies previews available for the documented start action. An **API** is an interface that software uses to request actions or read records. The next-generation activation API uses the term staged for its required campaign state. Use the state and permitted action documented for the interface you are using; do not assume every status word is interchangeable.

There is also a difference between requesting activation and confirming the result. The next-generation activation operation submits a job, meaning work for ISC to process. Its accepted response confirms the request was accepted; it does not say activation has already finished. Inspect the campaign's resulting state before reporting that it is running.

That API is marked Experimental, meaning SailPoint may change how it works and what a request must contain. Check its current requirements before using it. For the review process, keep the requested action and the verified result separate.

## Which creation choice fits the work?

The Search creation flow offers choices for saving, scheduling and immediate generation. Their purposes differ:

| What you need | Choice and resulting responsibility |
|---|---|
| Keep the definition for later | Save as a template only. Request generation when needed. |
| Prepare work at a future time | Save a template and schedule preview generation. Inspect the result and start the generated campaign. |
| Prepare work now and retain the definition | Generate a preview now and save a template. Inspect and start this campaign; the definition remains reusable. |
| Prepare an immediate review without retaining a template | Use the immediate generation/start option without a saved template. Confirm the actual generated contents and launch result. |

The interface may combine choices in one creation journey. Do not infer the outcome only from choosing an option: inspect what was saved, generated or started.

When you already have a generated preview in the documented Search start flow, Start Campaign is the action that launches it. A preview date alone does not replace that action.

You do not have to save a template for every one-off campaign. Its value is reuse. Likewise, a saved template does not need a schedule if the administrator intends to generate from it manually when required.

## Keep the dates attached to the right actions

A **generation time** is when review preparation is planned or performed.

A campaign's **due date** is the deadline set for the review work. It answers a different question: when should the review be finished?

You might plan generation before the intended launch so an administrator has time to inspect the preview. That preparation time is useful only if someone is responsible for the inspection and start.

Choose the schedule's time zone deliberately. “09:00” without its time zone is incomplete information when administrators and reviewers work in different locations.

For recurring work, confirm the actual recurrence and future dates. Quarterly means one cycle every three months. For example, the planned months could be January, April, July and October. Check that the saved schedule matches the intended calendar.

Also read each date's label in the scheduling and campaign details. A scheduled generation date and a campaign due date control different parts of the process. If the scheduling form also asks for an end date, check what that field controls in the actual configuration.

A pre-generation reminder email is a planning message. It is not proof that a preview has finished generating or that a reviewer can already open assigned work.

## Generating early does not remove the planned occurrence

Suppose T-1 is scheduled for tomorrow, but an administrator needs an early look today and generates a preview now.

The Search scheduling guidance explicitly says that an early generation does not prevent a preview from also being generated at the originally scheduled date and time.

That gives you two things to consider: the early campaign and the remaining schedule.

If the early campaign meets an urgent need, inspect and start it as appropriate. Then check whether the later scheduled generation is still wanted. Use the supported schedule controls if the plan needs to change, and verify the saved result.

Do not assume that starting the early campaign cancelled the schedule. Do not assume that tomorrow's occurrence will refresh that early campaign. Look for the actual generated campaign records and distinguish them.

Otherwise, the same access may appear in separate review cycles unintentionally. The problem is not that the permission was granted twice; separate campaigns can create separate review work about access that already exists.

## Reusing a template does not reuse the last cycle's decisions

Imagine that the first cycle's View Reports item was approved. **Approve** means the reviewer decided that the person should retain that reviewed access.

When another campaign is generated from T-1, the earlier approval does not establish that the new cycle has been reviewed. It belongs to work in the earlier campaign.

That is why you identify the particular campaign, account, access item and review period when discussing a decision. “This was approved before” may be useful history; it does not answer whether the person still needs the access for the present review.

The people and permissions may also change between cycles.

A template using two specific selected identities is different from a requirement to find everyone who currently meets a business condition. For the latter, examine how the actual saved selection is defined and what generation returns. Do not assume every reusable template automatically finds new joiners.

Likewise, reusing a template does not guarantee fresh source data. Confirm the information needed for the new cycle and inspect its actual output.

## Which record needs the correction?

Suppose the reviewer choice needs changing.

Before changing anything, identify the intended target. Are you correcting future generation, existing preview C-1 or an already running campaign?

Changing a template describes a change to the reusable instructions. Changing a schedule concerns future timing. Neither action, by itself, proves that an existing campaign's contents or assignment changed.

Inspect the particular generated campaign. If it needs correction, use the supported action for its current state and verify the result. A running campaign may already contain decisions worth preserving, so it should not be treated as disposable merely because its template is reusable.

There is no need to guess whether every setting is copied, linked or refreshed in the same way. Ask a concrete question: “Did the intended reviewer change in this particular campaign?” Then check the record that can answer it.

## Work through a changed requirement

A Warehouse Production template, T-2, contains only selected identity 2401 and that person's eligible warehouse access. It has a weekly preview-generation schedule.

The business now wants both identities 2401 and 2402 reviewed. Each holds View Stock on their own warehouse account. View Stock allows reading stock information. Both permissions are standalone entitlements, collected and correctly linked in ISC, with suitable permitted reviewers.

An administrator generates an early campaign, C-early, before the scheduled occurrence. Its preview contains only 2401's View Stock item. The administrator starts it.

Later, the administrator changes the saved template to include 2402 and says:

“The early campaign is running, so the weekly occurrence will use it. Both people are covered now.”

Which parts of that statement need correction? What should be checked before telling the business that both people have review work?

### Follow each record

C-early was inspected with only 2401's item. Starting it made that generated work available; it did not establish that 2402's access was included.

Changing T-2 is evidence about the saved instructions. Check that the revised saved selection actually includes both intended people and access. Then inspect any later generated work rather than assuming it changed C-early.

The early generation also did not cancel the planned occurrence. Check the actual schedule and decide whether the next generation is still required. Do not assume that occurrence will reuse the running campaign.

Suppose a later generation completes and the administrator inspects C-next. It contains 2401's View Stock and 2402's View Stock with appropriate assignments, but it is still in preview.

That is evidence that the new generated work covers both people. It is not yet evidence that the assigned reviewers can act in that campaign. Its authorized start and resulting state still need checking.

There may now be overlapping work for 2401 across C-early and C-next. Decide how those campaigns should be handled under the actual review requirement and supported correction options. Preserve decisions and needed evidence; do not blindly delete either campaign to hide the overlap.

If a reviewer reports that work is missing, establish which campaign and assignment they mean. Check the actual running state and permitted reviewer access. An email, a template edit or a scheduled date cannot answer all of those questions.

When someone asks whether a campaign is ready, identify the particular generated campaign and check its contents and current state. A saved template explains the plan; the generated campaign shows how far that plan has actually progressed.
