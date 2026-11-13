# How do you enable and troubleshoot certification recommendations?

You open a certification expecting a recommendation, but no icon appears beside the access item.

That does not yet tell us whether the person should keep the access. First we need to establish whether recommendations were available and enabled for this review, and whether the analysis could provide one.

Let's follow those checks.

## Establish which recommendation is missing

SailPoint Identity Security Cloud (ISC) keeps an **identity** representing a person and associates their application **accounts** with it. A **source** is ISC's configuration for the system or account data being managed.

Our review concerns account rep-24 on Reporting Production. It holds REPORT.READ, an **entitlement** representing permission to read production reports. The application owner has confirmed that capability.

A **certification campaign** organizes access reviews. A **certification** is an assigned review within it.

A **certification recommendation** is a suggestion supplied through the Access Recommendations service to help the reviewer assess existing access. It is different from recommending new access in the Request Center.

For this example, the person already holds REPORT.READ, and the assigned reviewer is permitted to assess it. The missing information is a recommendation about that held access.

Changing whether REPORT.READ can be requested would answer a different question.

## Check availability and campaign type first

Confirm that the organization has the Recommendations service available for this use.

Then establish the actual campaign type. A **role** groups access, and a **role-composition review** assesses what that role contains. An **uncorrelated-account review** assesses accounts that are not associated with an identity established from trusted identity information, such as personnel data.

Recommendations are not available for those two review types. They assess different subjects from the ordinary employee-access review in our example.

Do not spend time looking for a recommendation switch to overcome an unsupported review type. Use the review's actual contents and accountable business evidence to make the appropriate assessment.

For the normal case here, the review comes from a supported Search identity campaign, and the service is available.

## Find the control that belongs to this creation route

A campaign created from **Search** uses **Include Recommendations in your campaign** in its campaign details. For a supported identity or access-item campaign, an administrator with the required authority selects this option during creation.

A dedicated manager or source-owner campaign uses a different control. An **Admin** or **Certification Admin** opens **Admin > Global > System Settings > Feature Settings > Other Features** and checks **Enable Certification Recommendations**.

These controls belong to different creation routes. Finding the Search option selected in one campaign does not establish the system setting used by the dedicated manager route.

The manager/source-owner control is a system setting, so confirm that the intended change is appropriate for those campaigns generally. It is broader than the option on one Search campaign.

Activity Insights has its own configuration for collecting observed activity. Enabling it does not select the certification recommendation setting.

For our REPORT.READ investigation, the administrator confirms that the earlier Search campaign was created with recommendations excluded.

We have found that recommendations were excluded from that campaign. We still need to establish what can be changed for its existing review work.

## Prepare the next intended review with the correct setting

For the next approved reporting-access review, the administrator uses the supported Search identity route and selects **Include Recommendations in your campaign** before generating the campaign.

The intended person, rep-24 account and REPORT.READ must still be selected correctly. A recommendation setting does not bring missing accounts or permissions into the review.

Inspect the generated preview for the intended content and reviewer before starting. A **preview** is prepared review work available for inspection before reviewers begin.

Once the campaign starts, the assigned reviewer opens **Certifications > Active**, selects the review and checks the actual recommendation context.

In our example, an icon is now present. Selecting **Recommended** or **Not Recommended** in the **Decision** column opens the reasons supplied for the suggestion.

We have checked an actual result in the example: the intended review contains a recommendation whose reason the reviewer can inspect. Merely saving the creation option would not establish that result.

For an existing campaign, establish its supported handling with the campaign administrator. Do not assume that changing a current setting recalculates or replaces every previously generated recommendation.

## Understand which information supports the analysis

A **peer group** is a comparison group identified through similarities in identity and access information.

The analysis uses information about identities and their access. It can help identify patterns, such as access held by people with similar characteristics.

An **identity attribute** is a named piece of information, such as department or work function. A recorded value describes what ISC currently knows about that person; it may need checking against the person's actual duties.

SailPoint's **AI core identity attributes**, used by its artificial intelligence features, are four selected identity attributes. Where configured, they are used across several features, including certification recommendations. They help organize comparisons in a way that fits the organization's structure and access needs.

An authorized configuration owner can inspect these selections under **Admin > Identity Management > Identity Profiles** using **Edit AI Core Attributes**. This is configuration shared with other AI features, so changing it is broader than repairing one missing icon.

Check which inputs the organization actually uses and whether their values are accurate. A recorded department of Finance, for example, cannot reliably describe a person who moved into an unrelated support job if that value was never updated.

Correct the inaccurate information through its responsible data process. **Aggregation** collects information from a source; identity mappings determine how source information supplies identity values.

AI configuration changes also need processing before their results are visible. Recheck the resulting data and actual recommendation rather than assuming that saving a selection immediately changed an existing review.

Do not alter accurate attributes merely to obtain a preferred suggestion.

## Use the reason to investigate the access

For our next reporting review, the visible recommendation supports keeping REPORT.READ because similar identities hold that access.

The reviewer still establishes whether this person's current work requires reading these production reports.

Suppose the responsible business owner confirms an ongoing reporting duty requiring that capability on rep-24. That supplies a reason to keep the access. **Approve** accepts keeping the reviewed access; the recommendation supports investigation rather than making the decision.

Now change the business fact. The reporting duty ended, but the person's recorded department and held access still resemble those of the reporting team.

The comparison may still look persuasive. It cannot supply the missing current authorization.

Check whether the person has another approved reason to hold REPORT.READ. If not, the reviewer can reach a justified removal decision through the supported review process. **Revoke** records that the reviewed access should be removed; it is not proof that the application account has already changed.

Record the current-work evidence and the reason for the human decision. “The icon said so” leaves that reasoning unexplained.

## When the setting is right but the icon is still absent

First confirm the exact campaign, creation route and supported service. A screenshot of a different campaign's setting would not settle this review.

Then check the identity and access information used for the comparison. An enabled supported setup does not guarantee that every item will have a usable recommendation.

An identity without a comparable peer group can have no recommendation icon. A person with unusual specialist duties can therefore need a review based on their permission and approved work even when no recommendation is available.

Establish the cause for the actual case instead of applying that explanation to every blank row. Record what you verified, and keep an unexplained result open for investigation.

If the setup and data appear correct but the result is unexplained, keep the campaign and review identifiers, the relevant configuration, and the specific person/item observation when involving the responsible administrator or support team.

There is no need to invent a default decision while investigating. Permission meaning and current authorized work remain the basis for the review.

The checks connect like this:

```text
Confirm available service and supported type
                   |
                   v
Identify how the campaign is created
                   |
          +--------+--------+
          |                 |
          v                 v
Search identity or     Manager or
access-item route     source-owner route
          |                 |
          v                 v
Campaign setting      System feature setting
          |                 |
          +--------+--------+
                   |
                   v
Check the identity/access information used
                   |
                   v
Inspect the actual assigned review
                   |
          +--------+--------+
          |                 |
          v                 v
Reason available      No reason/icon available
Open and interpret    Investigate the missing
it with current need  information; do not guess
```

The two control branches are alternatives determined by campaign creation. They are not two switches that every campaign must use in sequence.

## Try a different creation route

A manager campaign has no recommendation icons. Someone shows you a Search campaign where **Include Recommendations in your campaign** is selected and concludes that recommendations must already be enabled everywhere.

What does that screenshot establish?

It shows the option selected for that Search campaign. It does not establish the system feature setting used for the dedicated manager campaign.

Check the manager route's actual setting, service availability, review type and input data. Then inspect the review itself.

Now suppose those checks pass, and the particular identity has no comparable peer group. Switching the setting off and on does not create evidence that the access is unnecessary. The reviewer still needs an explanation of the permission and the person's current approved work.

A missing icon is a question about available decision support. It is not the access decision.
