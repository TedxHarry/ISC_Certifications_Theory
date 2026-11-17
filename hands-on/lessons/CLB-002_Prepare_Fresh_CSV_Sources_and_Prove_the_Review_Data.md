# Prepare fresh CSV sources and prove the review data

A certification asks someone whether access is still needed. Before we can ask that question, ISC must know whose account it is, what access the account has and who should review it.

Let's prepare a small set where we can check every relationship. We'll use three employees, two managers and a simulated reporting application. There is no reporting system to connect. Its accounts and permissions will come from CSV files, which store rows of values under column headings.

The result we want is quite specific: five people in ISC, three reporting accounts linked to the right employees, and five permission holdings ready for a review. A holding means one account having one permission. An account with two permissions contributes two holdings.

## Keep the setup small

Use your approved training tenant and an administrator account that can create sources, configure an identity profile and inspect identities. Keep this work within the following new objects:

- People source: `certlab-people-csv`
- Reporting source: `certlab-reports-csv`
- Identity profile: `certlab-people-profile`

A **source** tells ISC where account information comes from and how that information is organized. An **identity profile** tells ISC how trusted people data should populate its identity records.

Check that these names and the supplied `certlab-` test users are not already in use. Also check their employee keys and planned email addresses against existing identities. A fresh source name alone does not prevent its accounts from matching existing people.

If these objects already belong to an earlier course run, inspect them before reusing them. If they belong to something else, choose a different test prefix and update every reference consistently before importing anything.

Check whether existing automatic assignments would grant unrelated access to these new test identities. If they would, arrange an approved isolated setup first. Do not disable shared roles or tenant-wide settings to make this fixture fit.

Do not create a campaign during this setup.

## Understand the two sources before creating them

The people source answers, “Who is this person, and who is their manager?”

The reporting source answers, “Which reporting account belongs to this person, and what permissions does it have?”

Those are different questions. We don't want each reporting account to create another person. The people source will be **authoritative**: it supplies the trusted records from which ISC creates identities. The reporting source will supply additional accounts for those identities.

Use the three supplied files from the baselineA data package:

| File | What it supplies |
|---|---|
| `people.csv` | Three employee records and two manager records. |
| `report_accounts.csv` | Three reporting accounts and their assigned permission values. |
| `report_entitlements.csv` | Names and descriptions for the two permissions. |

An **entitlement** is a particular access value that ISC can govern. Here, the two values mean Read Reports and Export Reports in our simulated application.

The entitlement file describes those permissions. It does not give them to anyone. The account file states who has them.

## Prepare private working copies

The supplied people file uses addresses ending in `example.invalid`. These addresses are synthetic and cannot receive registration messages.

Make private working copies of the files. Replace the five email values with distinct approved test addresses. The two managers need reachable addresses so you can complete their registration. Keep these private copies outside the reusable course files.

Keep the supplied identifiers unchanged unless you deliberately chose a different prefix. In this fixture, an employee's `id`, `name` and `employeeNumber` have the same value, such as `certlab-employee02`. They still have different jobs:

- `id` identifies the source account.
- `name` names that account; the people profile will also use it for the ISC username.
- `employeeNumber` is the person key we will match across the two sources.

These are our source values. They are not the internal object IDs ISC will assign.

Look at employee02's `manager` value. It is `certlab-manager01`. That means “find the identity whose employee key is certlab-manager01,” not “make this text a reviewer.”

Keep the files as UTF-8 CSV text. A text editor is useful for checking the actual headings and commas. Do not add passwords to the files.

## Create the people source

Open **Admin > Connections > Sources > Create New**. Search for **Generic** and select **Configure**, or its **Standard Setup** action where offered. Use the manual flat-file upload option.

Enter `certlab-people-csv` and a description identifying it as the certification training people data. The source owner is the person responsible for that source. Select your existing authorized training administrator as its initial owner. The test managers do not exist yet, so they cannot be selected now.

Continue and save the base configuration. Record the source's actual ID privately so you can distinguish it from another similarly named source.

This procedure uses manual file upload. If the selected setup instead asks for a remote file server, path or credentials to fetch a file, check the source type and connection mode before continuing. Do not mix those instructions into this setup. If your tenant requires a virtual appliance, a component used by some connections, establish that requirement before importing.

The people source will become authoritative through its identity profile. If creation offers an Authoritative Source choice, select it for this people source. We will still create the profile; that checkbox alone does not replace the mappings.

## Match the people file to its account schema

A **schema** lists the fields ISC stores for each account. The file and schema must agree.

Open the people source's **Account Management > Account Schema**. Check the following fields, using **String**, which means text values:

| Field | Meaning in this setup |
|---|---|
| `id` | Stable people-source account key. |
| `name` | Account name and intended ISC username. |
| `employeeNumber` | Unique person key. |
| `givenName` | First name. |
| `familyName` | Last name. |
| `displayName` | Readable name. |
| `email` | Approved test email address. |
| `manager` | The manager's person key, or blank for manager01. |

Use `id` as **Account ID** and `name` as **Account Name**. Set these before collecting accounts. Changing account keys later can break existing references.

The people fields above are single values. Do not mark the manager field as an entitlement or as multiple values.

Use the source's current downloaded account template to prepare the upload. You can download it from **Account Aggregation > Download Account Schema**. Keep its full heading order, including any additional columns. Copy the supplied people values into the matching columns and fill any other required fields.

Do not upload the short sample unchanged if the downloaded template has a different structure. Also do not remove existing columns merely to make the template resemble the sample.

If a needed field is missing, use the schema editor to configure that field on this fresh source before loading data. If the source does not support the required schema, resolve that setup difference first. Save the final template and prepared working file together.

## Tell ISC how the people records become identities

Open **Admin > Identity Management > Identity Profiles > Create New**. Name the profile `certlab-people-profile` and select the people source.

Use manual invitations and the supported site username/password sign-in method for these new test users. Keep the required security controls. Do not select the CSV source as a directory authentication system; it contains records, not working passwords.

Save the profile. On **Mappings**, select the people source for these fields:

| Identity field | People account field |
|---|---|
| User Name (`uid`) | `name` |
| Work Email (`email`) | `email` |
| Last Name (`lastname`) | `familyName` |
| First Name (`firstname`) | `givenName` |
| Display Name (`displayName`) | `displayName` |
| Identification Number (`identificationNumber`) | `employeeNumber` |
| Manager Name | `manager` |

Save and apply changes for this profile. User Name, Work Email and Last Name must be populated; usernames must be unique. Do not configure automatic access grants for these identities.

## Make the manager value resolve to a person

The Manager Name mapping supplies the employee's manager key. ISC also needs to know which field to examine on the manager's identity.

Return to the people source. Open **Account Management > Account Correlation** and find **Manager Correlation**.

Set the identity attribute to **Identification Number** (`identificationNumber`) and the account attribute to `manager`. Save.

Read that pairing from employee02's point of view. Its source account contains `manager = certlab-manager01`. ISC looks for an identity with `identificationNumber = certlab-manager01`. The result should be a link to manager01's identity.

This is **manager correlation**. A matching text label in a record is not enough; inspect the resulting manager identity after processing.

## Load the people and check the result

**Aggregation** reads account data into ISC. For the authoritative people source, **identity processing** applies the profile's mappings to the identity records. We need both the collected account values and the resulting identities to be correct.

On the people source, open **Account Management > Account Aggregation**. Keep account deletion disabled for this initial load. Select the upload control and choose the complete private people file prepared against this source's template.

Follow the actual aggregation status through completion. A file loaded only for correlation recommendations is not the same as an account aggregation.

After collection and identity processing, open **Admin > Identity Management > Identities**. Inspect the five test identities and confirm the required fields. Use the profile's mapping preview if a value differs, then correct the source value or mapping and apply the test profile's changes.

The resulting relationships should be:

| Identity | Manager identity |
|---|---|
| `certlab-employee01` | `certlab-manager01` |
| `certlab-employee02` | `certlab-manager01` |
| `certlab-employee03` | `certlab-manager02` |
| `certlab-manager01` | None in this fixture. |
| `certlab-manager02` | `certlab-manager01` |

If identities are missing or incomplete, inspect this profile's identity exceptions and required mappings first. If a manager is wrong, inspect the employee's manager key, the manager's Identification Number and both manager settings before continuing.

There is no fixed waiting time to memorize. Check processing state and the actual records. Do not repeatedly start imports while an earlier operation is still running.

## Prepare the reporting source

Create another **Generic** manual-upload source named `certlab-reports-csv`. Use the training administrator as its initial owner and record its actual source ID.

Keep this source non-authoritative. Do not create an identity profile for it.

Inspect its account schema:

| Field | Required use |
|---|---|
| `id` | Account ID; String, single value. |
| `name` | Account Name; String, single value. |
| `employeeNumber` | Person key; String, single value. |
| `groups` | Multiple entitlement values held by the account. |

For `groups`, verify **Multi-Valued** and **Entitlement**. The first allows an account to hold more than one value. The second identifies these values as access that ISC can govern. Check that this field uses the source's existing entitlement type, so the account values can link to the permission records we load next. Keep that single type rather than copying a type name from a different connector.

Download the reporting account template and copy the supplied account data into that full structure, just as you did for the people source.

The supplied account file has five data rows. Here are the two for account02:

```csv
id,name,employeeNumber,groups
certlab-account02,certlab-account02,certlab-employee02,certlab-report-read
certlab-account02,certlab-account02,certlab-employee02,certlab-report-export
```

These rows describe one account with two group values. Keep rows for the same account together and repeat the other fields consistently. The supplied file is sorted by account ID; its Account Name values have the same order.

Do not replace the two rows with a single value such as `read|export`. That would change the data representation this setup uses.

## Match each reporting account to its employee

Before aggregating the reporting accounts, open the reporting source's **Account Management > Account Correlation**.

For this fresh source, configure the intended pairing:

Identity **Identification Number** (`identificationNumber`) equals account **employeeNumber**.

Inspect any preset criteria and keep the explicit pairing needed for this fixture. Remove competing criteria only on this new test source. Save.

This is **account correlation**. Account02 carries `employeeNumber = certlab-employee02`; employee02's identity carries the same value in Identification Number. The match should attach that reporting account to employee02.

Notice the difference from manager correlation. Account correlation finds the owner of an account. Manager correlation finds the person who manages an employee.

## Give the permission values useful meanings

The account file uses `certlab-report-read` and `certlab-report-export`. A reviewer also needs readable names and descriptions.

On the reporting source, open **Entitlement Management > Entitlement Aggregation** and download the entitlement template. Prepare it using the supplied catalogue values:

- `certlab-report-read`: **Read Reports**, for viewing reports.
- `certlab-report-export`: **Export Reports**, for downloading reports in bulk.

Keep the template's complete headings and order. The catalogue's entitlement IDs must match the account's `groups` values exactly. A description cannot repair a different ID.

Upload the prepared catalogue and check the resulting entitlement records. Then aggregate the complete reporting account file through **Account Aggregation** and inspect its completion.

You should find two permission definitions. That does not mean there are only two holdings: the same Read Reports permission is held by three accounts.

## Follow one employee through the complete setup

Open employee02's identity. Check the actual records in this order:

1. The people-source account identifies employee02 and supplies its person key.
2. The identity's Identification Number contains that key.
3. The reporting account02 is attached to this identity through the matching key.
4. Account02 holds Read Reports and Export Reports.
5. The identity's manager link opens manager01, not manager02.

That is the connection a future manager review needs. The reporting account supplies the access; its identity tells us who holds it; the manager relationship identifies the intended manager.

Check the other two employees against the complete baseline:

| Reporting account | Identity | Read Reports | Export Reports | Intended manager |
|---|---|---|---|---|
| `certlab-account01` | employee01 | Present | Present | manager01 |
| `certlab-account02` | employee02 | Present | Present | manager01 |
| `certlab-account03` | employee03 | Present | Absent | manager02 |

The employee and manager labels in this table use the same `certlab-` prefix as the file.

Count three reporting accounts and five account-permission holdings. The two managers should have no reporting accounts in this baseline.

Keep these rights as direct entitlements. An **access profile** packages entitlements; a **role** can grant access to its assigned identities; a **lifecycle access grant** requires access because of a person's employment state. We are not using those mechanisms here. Check that none independently requires these test rights, because it could change the review or keep access required after a removal choice.

The application is simulated. These checks establish what ISC collected from the files; they do not prove a permission exists in a real reporting application.

## Give the managers working reviewer access

An identity record does not, by itself, mean that its person can sign in.

Inspect the two manager identities and their profile's sign-in settings. If one of these approved test identities is disabled, find it under **Admin > Identity Management > Identities** and use **Actions > Enable Identity**. Check its resulting state before inviting it. This enables ISC sign-in; it does not grant reporting permissions.

If the chosen registration method is unavailable, resolve that specific test-user setup before calling reviewer access ready. Do not substitute the administrator's account for both managers or give the managers administrator privileges just to perform a review.

For the supported local registration route, open **Admin > Identity Management > Identities**, select each intended manager and use **Actions > Invite Identity**. Check the exact recipient address before sending. Use only the two approved test managers.

Complete each manager's registration through its own invitation and required security steps. Keep passwords, registration links and recovery details private. Sign in as each manager in separate browser profiles or isolated sessions and open **Certifications**. Keep the administrator session separate so you know who performed each action.

An empty review list is expected before assignment. It proves neither a future reviewer assignment nor its visibility; we will check those against the generated campaign.

Now edit the reporting source's owner and select the actual manager02 identity. Save and reopen the source to verify the selection. Source ownership is an ISC reference; writing a name into the CSV does not set it.

## Keep a usable baseline record

Record the two source IDs, profile ID, five identity IDs, actual account associations, manager links, entitlement IDs, source owner, file versions and collection times in your private lab notes. Also record which two sessions you verified.

A small exact inventory is more useful than “aggregation succeeded.” It lets you compare a future preview with the data that should have produced it.

The current work evidence for the first review is:

Employee01 still needs viewing and bulk export. Employee02 still needs viewing, but the export work has ended. Employee03 needs viewing only.

No decision has been recorded yet. Keep those facts with the baseline so a reviewer can explain a choice rather than copy a list of buttons.

## Find the first broken connection

Suppose the two entitlements have good descriptions and all three reporting accounts contain the expected groups. The five people identities also exist and their manager links are correct.

However, the reporting accounts are unassigned. Their account names are `certlab-account01`, `certlab-account02` and `certlab-account03`, which differ from the identity names. The intended employeeNumber matching has not been configured.

Would changing the entitlement descriptions fix this? Which connection needs attention first?

<details markdown="block">
<summary>Compare your reasoning</summary>

The missing connection is between each reporting account and its employee identity.

Descriptions explain what access means. They do not identify the account holder. Configure the intended account employeeNumber-to-identity Identification Number pairing, check its values and use the supported source collection/correlation process to verify all three associations.

Do not assume that saving a criterion alone has repaired previously collected accounts. If unchanged accounts are skipped or an existing association remains, inspect the source's supported re-evaluation procedure before trying again. Do not delete identities or change account IDs to force a match.

The manager links are already correct in the supplied case. Changing them would address a different relationship.

</details>

## Leave the data ready for a review

Keep the two sources and the profile. They are the intended starting setup, so this lab does not delete them at the end.

If you need to restore the data, first inspect whether a later run has created campaigns, tasks or other outstanding work. Complete its supported handling before restoration. Re-upload the complete private source-bound baseline files to their own sources, apply any corrected test-profile mappings, and verify all five identities, manager links, three accounts and five holdings again.

Do not upload an empty people file, change account IDs or delete an identity profile as a shortcut. Those actions can affect identity records and account associations. Restoring a CSV also does not undo signed reviews or restore access in a real external system.

Before starting the review, confirm the full baseline and both manager sessions. If the data is correct but reviewer sign-in remains unresolved, record those as separate results. The account data is prepared; the review is not ready to start.
