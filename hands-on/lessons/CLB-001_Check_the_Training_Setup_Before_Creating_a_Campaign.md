# Check the training setup before creating a campaign

Before you create a review, find out what you can use in the training tenant and what still needs preparation.

A **tenant** is your ISC environment. It contains the configured systems, users, access information and review work for that environment. Being able to sign in is the starting point. We also need the right people, application data and permissions for the task.

Use a desktop or laptop browser for this lab. You will inspect the setup and record what you find. Leave connection settings, account permissions and campaigns unchanged.

## Confirm where you are working

Open the training tenant through your approved sign-in method. Check the tenant name or address against the environment you were given.

Confirm which test objects you can use. A training tenant can contain work belonging to other learners, so identify your own area before preparing anything.

Keep the tenant name or a short alias in your notes. If the permitted test area is unclear, record that as something to establish before making changes.

## Find the campaign choices that are available

A **certification campaign** organizes access-review work. It decides what access will be reviewed and who will review it. A **preview** is the generated work that an administrator can inspect before starting the review.

For the documented manager/source-owner route, open **Admin > Certifications > Campaigns**. If your account can access the creation form, open **Create New** and inspect the available types. Do not generate a preview.

A manager campaign asks managers to review their employees' access.

A **source** holds the connection configuration and account information collected from a managed system. A source-owner campaign focuses the review on access recorded on the selected sources.

If your tenant offers the Search route, open **Search**, locate **Certification Campaigns** in its toolbar and inspect **New Campaign**. Record the types actually offered.

The routes do not necessarily offer the same reviewer choices or selection controls. Write down what you see rather than combine instructions from different creation forms.

Close the form without saving or generating work.

If a menu or type is missing, record that observation. It may require a different permission or may be unavailable in this environment. The next useful check is with the person responsible for the training tenant.

Record any visible **Legacy** label as well. Such a label helps identify a campaign path. If no engine label is shown, leave the engine unconfirmed until you can establish it from the actual setup. The absence of a label alone does not prove which API or behavior applies.

## Identify who will perform each part

For the first manager review, we need an operator who can prepare and start the campaign, and managers who can perform the reviews assigned to them.

A **reviewer** is the person or group responsible for examining the assigned access and recording a decision. Being the campaign administrator does not automatically make someone the right business reviewer.

Identify the intended training users and the work each is allowed to perform. Later setup will use two manager users and three employee records. You do not need to create them during this check.

The people records will be fresh test data. Importing a manager's CSV record does not automatically give that person a working sign-in. Arrange the intended reviewer access separately and confirm it belongs to the approved training scope. Each intended reviewer should be able to sign in through their own approved access and open **Certifications**.

An empty Certifications list can be normal before any work is assigned. It does not prove that a reviewer will be able to see a future campaign. We will check the actual assignment when the preview and active work exist.

If those users have not been prepared, record that the baseline needs user setup. Do not replace them with unrelated existing people to make the inventory look complete.

## Find the people data and the application data

An **identity** is ISC's record for a person or another managed subject. An **application account** is the account through which that person uses a particular application.

A **connector** is the integration used to communicate with a source's system. The source configuration tells ISC how to obtain its account information.

Open **Admin > Connections > Sources** if your account permits it. Inspect the available source-creation choices without creating a source. We will use fresh sources rather than reuse an existing application's data.

There are two useful questions:

- Where will ISC obtain the employee and manager information?
- Where will ISC obtain the application accounts and their permissions?

An **authoritative source** supplies the trusted people information used to build identities. An **identity profile** defines how the source information supplies values on those identities.

The application source supplies the account and access records we want to review. These are related parts of the setup, but they have different jobs.

If an appropriate test identity exists, inspect its source-account association and manager relationship through the tenant's identity view or search.

**Account correlation** connects the application account to the correct identity. **Manager correlation** connects an employee's identity to the manager's identity. Check the resulting relationships, not only whether a manager-looking text value appears in a source record.

For this inspection, record the source name, an appropriate test account or alias, the associated identity and the manager identity where available. Keep credentials and private tenant details out of reusable course notes.

If the tenant has no suitable sources or identities yet, record that clearly. The baseline setup must then include those pieces.

Do not run an aggregation merely to inspect this inventory. **Aggregation** reads account information into ISC and updates the collected records. That is a setup action we will perform deliberately after checking the source, mappings and test scope.

## Use fresh CSV data for the first review

We will prepare two new sources. One supplies the employee and manager records. The other supplies the accounts and permissions we want to review.

A **CSV file** stores rows of values, with a heading for each column. Here, one file describes the people, another describes their application accounts and permissions, and a third supplies the permission names and descriptions. The permission file belongs to the second source.

The application is simulated. For example, an account row can say that a test employee has Read Reports and Export Reports. ISC collects those values and uses them as access data for the review. There is no reporting application behind this file.

The review work in ISC is real: the managers receive work, make choices and confirm their reviews. What differs is how we represent the application result.

Suppose a manager decides that an employee no longer needs Export Reports. We will inspect the work ISC creates, then update a copy of the account file to represent that permission being removed. After collecting the revised data, we can check that ISC shows the expected remaining permissions.

That file edit is a simulated application change. It does not show ISC removing a permission from a real application. Keep both file versions so you can explain what changed.

You do not need to connect AD before preparing these CSV sources. We will need a connected system later to test an actual account change and a failed change.

## Understand how the change will be carried out

With a **manual path**, ISC creates work for someone to carry out the required change. Inspect the actual task and its recipient when it exists. For our simulated application, the external action will be the agreed file edit.

Completing a task and collecting revised data are separate actions. Do not assume that uploading the file automatically completes the task. We will check the actual sequence during the review.

With an **automated path**, ISC sends a supported change to a connected application. The **integration account** is the technical account the connection uses. It needs permission to perform that particular change.

A manual CSV upload cannot demonstrate this automated account change. For that later exercise, we will need a connected test system, such as AD, and a way to inspect the account or group membership there.

Seeing collected accounts proves that ISC has account information. It does not prove that ISC can change the original account.

## Record what is ready and what is still missing

Keep a short inventory that another person can understand.

| Item to record | Useful observation |
|---|---|
| Training environment | The confirmed tenant or alias and permitted test scope. |
| Campaign path | The available route/types and any observed engine label. |
| Actors | Who can prepare the campaign and which training users can review. |
| People information | The authoritative source and identity setup, or a clear statement that they need preparation. |
| Application information | Fresh CSV review source planned; record which account/access setup still needs preparation. |
| Manager relationships | The actual manager identities, or the specific links that still need setup. |
| Result to check | CSV phase: versioned account file and collected ISC rights. Later connected phase: actual external account permissions. |
| How the change will be carried out | CSV phase: inspect actual manual work and make a labelled simulated file change. Connected automation remains a later check. |

Use Not checked, Not available or Needs preparation where those are the facts. Do not turn an unknown into Ready just to complete the table.

The result of this lab is an environment inventory. It is not a completed access review or proof that a removal works.

## Work out the next useful check

You can open the manager-campaign form and see collected application accounts. The source is known to read account data.

However, nobody has yet identified how to inspect the application's current permissions. You also have no evidence that the connection can change access or that a suitable manual operator is available.

Can you say that the automated removal lab is ready? What has been established, and what should be checked next?

<details markdown="block">
<summary>Compare your reasoning</summary>

You have established access to the creation form and the presence of collected account information. Neither fact proves that a permission can be removed from the application.

For an automated-removal exercise, identify how to inspect the actual target account. Then establish a supported change path and its authorized operator or integration account. The exercise must verify the resulting account change.

You can record that ISC can read the account information. You still need to establish how a change will be made and how the application result will be checked. For manual removal, check who receives the task and who is allowed to make the change in the application.

You can still prepare and run the CSV review. Its result will be the actual ISC review and a clearly labelled file simulation. Keep the connected automated-removal exercise pending.

</details>

## Prepare the fresh baseline

The next setup will create the people source, the review-account source, their mappings and the test data. It will also check that each account belongs to the right identity and each employee is linked to the right manager.

Keep your inventory with the lab notes. Before generating review work, verify the imported records, intended reviewers and five starting permission holdings. A successful file upload alone does not establish those relationships.

The CSV setup can proceed without AD. Keep the later connected-account result separate from the results we can check using files.
