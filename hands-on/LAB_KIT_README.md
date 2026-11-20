# ISC Certifications Hands-On lab kit

Open the extracted `ISC_Certifications_Hands_On` folder. The lesson files end in `.md`; you can read them in a Markdown viewer or a text editor. Keep the folders together so the lesson pictures can open.

Start with these three lessons in `lessons`:

1. `CLB-001_Check_the_Training_Setup_Before_Creating_a_Campaign.md`: inspect the training environment without creating anything.
2. `CLB-002_Prepare_Fresh_CSV_Sources_and_Prove_the_Review_Data.md`: prepare the people, reporting accounts and manager sign-ins.
3. `CLB-003_Complete_a_Manager_Review_and_Check_the_CSV_Result.md`: perform the first review and check its simulated CSV result.

The website numbers lessons in learning order. The file IDs stay fixed, so later file numbers do not always follow that order. Follow the website's lesson list when choosing the next task.

## Find the first data files

Open `lab-data/baselineA`. Start with these three files:

| File | What it describes |
|---|---|
| `people.csv` | Three employees and two managers. |
| `report_accounts.csv` | Three reporting accounts with five permission holdings. |
| `report_entitlements.csv` | The two permissions: Read Reports and Export Reports. |

The fourth CSV, `report_accounts_after_employee02_export_removal.csv`, shows the expected values after the first review's simulated removal. Keep it for comparison. It is not the starting account file or evidence that a review has happened.

The same account appears on two rows when it has two permissions. Five permission rows therefore describe three accounts. The entitlement file describes the permissions; it does not assign them to anyone.

Keep these supplied files unchanged. During setup, download the actual source templates from ISC and make complete private working copies using the supplied values. Replace the synthetic email addresses with approved test addresses as explained in the setup lesson. Use the private working copies for imports and resets.

You can inspect these files before tenant access returns. Creating sources, importing data, arranging reviewer sign-ins and running reviews require access to the training tenant.

## Keep the other folders for their tasks

`lab-data/baselineB` through `baselineF` support later tasks. Each lesson names the starting data it needs. You do not need to prepare all of them for the first review.

`assets` contains the lesson pictures and their editable definitions. `tools` contains a read-only evidence collector for a later specialist lesson. `author/contracts` contains its blank configuration and the API request plan; `author/tests` contains its offline checks. No script or command is needed to read the first three lessons or inspect their CSV files.

For the collector lesson, run its commands from this extracted course folder. Keep private working files and captured evidence in `private`, separate from the reusable files. Keep credentials out of the supplied CSV files.

Expected-value files are comparisons, not tenant observations. For the independent CLB-017 project, derive the result from its own work request. Worked assessor answers are not included in this kit.
