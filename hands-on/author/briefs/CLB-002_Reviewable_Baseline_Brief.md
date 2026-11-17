# CLB-002 brief: prepare the fresh CSV baseline

November 14, 2026. Saved before learner prose.
Learner filename: CLB-002_Prepare_Fresh_CSV_Sources_and_Prove_the_Review_Data.md.

## Task and useful result

Create two isolated manually uploaded Generic flat-file sources, a people identity profile, manager/account matching and a meaningful entitlement catalogue. Prove baselineA: five identities, three review accounts and five direct holdings. Arrange the two managers' approved reviewer sessions. No campaign is generated in this lab.

The source type is Generic, using manual file upload. This is not a Delimited File SaaS/VA SFTP connection. The current Generic introduction lists a VA prerequisite while its documented creation steps do not select one. Do not claim a universal no-VA requirement or invent setup fields. Record the actual offered mode/dependencies during tenant validation; a missing requirement affects execution, not local authoring.

## Starting conditions and exact scope

The user reports full admin and all tenant options. No session has been inspected. Use fresh certlab-people-csv and certlab-reports-csv sources plus certlab-people-profile. Check names, usernames, employee keys and email values for collisions before importing. If the fixed course identifiers already exist, reuse only a proven course fixture or choose and consistently document a distinct namespace before import.

Use the existing authorized training administrator as initial source owner. After manager02 is imported and enabled, bind the review source owner to that exact test identity. Do not use a nonexistent identity as an initial creation prerequisite.

Fresh CSV data can meet schema mapping but cannot create reachable mailboxes. Use private prepared copies with five distinct approved email values; at least the two reviewer addresses must be reachable for their registration/notification route. Never publish mailbox bindings, credentials or registration URLs.

## Data contract

Use Generic's existing field meanings: people id/name/givenName/familyName/displayName/email/employeeNumber/manager; review id/name/employeeNumber/groups. All input scalars are strings; groups is multi-valued and an entitlement on the review source.

Canonical fixtures define the needed columns. Download each actual source template before loading and preserve its complete field order. If there are extra columns, copy the fixture data into that template rather than deleting columns or asserting the narrow fixture is a universal upload. Required extra fields need actual valid values. Do not modify account keys after collection.

Group repeated review rows by identical account ID/name/employeeNumber; only groups changes. Five data rows should yield three accounts, not five. Catalogue IDs exactly match the account group values; keep the existing supported single entitlement association and record it rather than inventing another flat-file entitlement type.

Map people.name to uid, people.email to email, people.familyName to lastname, people.givenName to firstname, people.displayName to displayName and people.employeeNumber to identificationNumber. Map Manager Name to people.manager and configure manager matching from account manager to manager identity identificationNumber. Review correlation matches account employeeNumber to identity identificationNumber.

## Authored flow and changed case

Explain first why people and application accounts have separate jobs. Follow employee02 through source row, identity, matched report account, manager identity and two rights. Show expected relationships before asking for proof.

The changed case has three accounts with the correct group values but no employeeNumber matching configured and unassigned accounts. Learner identifies the first failed relationship; changing the group descriptions cannot fix it. Do not force this fault into the live baseline or assume updating a rule relinks existing accounts automatically.

## Evidence, reset and boundaries

Check five complete identities and actual manager links, three correctly owned report accounts, two catalogue values with names/descriptions, five holdings, no role/profile/lifecycle regrant and separate manager sessions. Source owner manager02 is an identity reference, not a typed CSV label. Record source/profile IDs privately.

No target permission is changed and no campaign should exist from this setup. Preserve the verified fixture for reuse. For data restoration, recollect the complete source-bound copies, apply only the test profile's mappings/processing and verify the full baseline. Do not use empty people files, identity/source deletion or campaign deletion as a routine reset. An unexpected existing campaign/task requires its own supported handling before restoration.

Authored/source-reviewed and locally reconciled are separate from imported, tenant-executed and repeated. No fabricated screenshots or result timings. No source/course links in learner prose. Length, tables and explanations follow this setup's needs.

## Primary support

Current official checks are recorded in the source register and the002 revision record: source creation, account schema/loading, identity profile mappings/registration, account/manager correlation, entitlement loading and Generic repeated-row rules. The inconsistent Generic upload-schema wording is not adopted as a separate import mechanism; use the current account/entitlement aggregation paths and actual downloaded templates.
