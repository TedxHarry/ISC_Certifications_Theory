# BaselineD: one unmatched account and one linked control

Version1.1. November16,2026.
For [CLS-001](../../lessons/CLS-001_Review_Uncorrelated_Account_Access_and_Track_Ownership.md).

## Actual status

These three synthetic CSVs are authored values, not tenant exports, tested imports or universal upload templates. No source/account/shadow identity has been created or inspected. Bind values privately to the actual downloaded source templates and complete required fields before importing.

Use a fresh Generic/manual-upload source certlab-uncorrelated-reports-csv, called D. It is non-authoritative and must not be assigned to a new identity profile. Reuse the original verified people/profile data and working manager02 session; no new human or login is created by this package. Set the actual source owner to certlab-manager02 in Base Configuration, not through a CSV column.

Inspect actual Generic mode/dependencies. Do not promise no VA or silently substitute a remotely fetched Delimited File connection. Do not change A/B/C or the authoritative people source.

## Files

| File | Data rows | Meaning |
|---|---|---|
| uncorrelated_report_accounts.csv | 3 | Two accounts/three holdings: target Read+Export and control Read. |
| uncorrelated_report_entitlements.csv | 2 | Source-specific Read/Export definitions, not account assignments. |
| uncorrelated_report_accounts_after_export_removal.csv | 2 | Expected values after only target Export removal; two accounts/two Read holdings. |

UTF-8 CSV with one header, LF line endings and comma separators. Repeated account rows are adjacent with identical scalar fields. The narrow headers define intended values; preserve the real template's column order, additional fields and required values.

Account schema: id/name/employeeNumber are scalar String; groups is a multi-valued entitlement using the actual source's supported single entitlement association. Account ID is id; Account Name is name. Catalogue id values match groups exactly.

## Correlation contract

Before first account collection, set only this fresh source's explicit pairing: account employeeNumber equals identity identificationNumber. Inspect presets/competing criteria. No existing authoritative identity may have certlab-unmatched01, and no manual association should link the target.

Also check the built-in Account Name-to-identity-name fallback before first collection: no existing identity may be named certlab-uc-account01, ignoring capitalization. An unmatched employeeNumber alone does not establish the intended uncorrelated result. Actual tenant checks remain required.

| Account | Account employeeNumber | Intended association | Initial rights |
|---|---|---|---|
| certlab-uc-account01 | certlab-unmatched01 | Uncorrelated; no authoritative person match | Read and Export |
| certlab-uc-control01 | certlab-employee01 | Existing employee01 identity | Read |

The unmatched value is a synthetic external key, not proof of a real employee number. Do not put it in the authoritative people feed, change it to a manager's key or manually link the account merely to reduce the unmatched list.

Expect one unmatched source account and one linked control, then inspect actual shadow/uncorrelated representation. A shadow record is not a new verified human. Actual grouping can differ; no one-shadow-per-account or total-identity-count promise.

## Review and limited authorization

The learner verifies the actual Uncorrelated Accounts route, selects only D and inspects that the correlated control is excluded. Manager02 is the known source owner/custodian, not a proved individual owner of the target account. Inspect actual offered reviewer control/recipient rather than invent a manager.

Supplied exercise facts support only a temporary Read requirement under manager02's named custody with an actual recorded follow-up date; Export need has ended. Individual ownership investigation remains open. One target Read Approve/Export Revoke is the planned review result, not captured decisions. Follow-up is a work obligation, not automatic entitlement expiry.

## Expected change and reset

After actual reviewer finalization and matching manual-work inspection, edit the full private D file to remove only target Export. Compare the expected file's values; do not upload it early or call it a real export. Follow successful collection, inspect two retained accounts/Read holdings, target still uncorrelated and control still linked, then close wholly fulfilled actual work. Both catalogue definitions remain.

Preserve signed/task/data/follow-up evidence and resolve outstanding work before restoring the complete private original D file. Collect and prove two accounts/three holdings, the same unmatched key and linked control. Keep source/people/profile/correlation unchanged and ownership follow-up explicit. No source/identity/account deletion as reset.

That reset assumes the original associations are still valid. Preserve any legitimate later ownership/key correction and agree a revised training starting state instead of restoring obsolete matching data.

This package contributes three CSVs and leaves the seven original A/B files and C native contract unchanged. No real application access change, owner resolution, import, review, task or reset is established by these files.
