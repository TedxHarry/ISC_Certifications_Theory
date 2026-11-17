# BaselineE: native machine classification and one permission removal

Version1.1. November16,2026.
For [CLS-002](../../lessons/CLS-002_Review_Service_Account_Access_and_Preserve_the_Service.md).

## Actual status and scope

Three synthetic CSV value files, not tenant exports, tested imports or universal upload templates. No source, machine classification, application identity, owner assignment, campaign or task has been created. Bind values to actual downloaded templates and preserve required columns privately.

Use fresh non-authoritative Generic/manual-upload source certlab-machine-reports-csv, called E. Source owner is actual certlab-manager01; machine-account owner is actual certlab-manager02. Reuse the original five people and approved working sessions; importing a person does not register a reviewer login. No machine row in the authoritative people feed and no new identity profile.

Inspect actual Generic mode/dependencies, schema/template and licensed native Machine Accounts/certification choices. No blanket no-VA guarantee, connected-write claim or silent connector replacement. Existing A/B/C/D and all people/profile mappings stay unchanged.

## Values and schema

| File | Data rows | Intended values |
|---|---|---|
| machine_report_accounts.csv | 3 | Two accounts/three holdings: service Read+Export, human control Read. |
| machine_report_entitlements.csv | 2 | E-specific Read and Export definitions. |
| machine_report_accounts_after_export_removal.csv | 2 | Two accounts/two Read holdings; only service Export removed. |

UTF-8, comma-separated, LF, one header. Adjacent repeated account names carry identical scalar values. Account schema id/name/employeeNumber/accountKind/ownerKey/environment/purpose are scalar String; groups is multi-valued entitlement with the source's actual supported association. Account ID id; Account Name name. Catalogue id matches groups. Required actual template fields/order remain authoritative.

| Account | employeeNumber | accountKind | ownerKey | Initial access |
|---|---|---|---|---|
| certlab-human-control01 | certlab-employee01 | human | certlab-manager01 | Read |
| certlab-svc-report01 | certlab-machine01 | service | certlab-manager02 | Read+Export |

All environment values training. Human purpose Human control account; service purpose Nightly report reading job. These are supplied exercise facts, not an actual running job.

On E only, configure employeeNumber→identity identificationNumber before collection. Verify control links to employee01 and service key has no authoritative human match, including elsewhere in the actual tenant. Then perform native classification. Ordinary unmatched status is only an intermediate observation, not a completed machine setup.

Before first collection, also check the built-in Account Name-to-identity-name fallback: no existing identity may be named certlab-svc-report01, ignoring capitalization. Inspect prior manual human links. A missing employeeNumber match alone is insufficient. Owner matching through ownerKey→uid establishes responsibility rather than a personal account association.

## Required native ISC configuration

Classification enabled/customized: accountKind equals service. Human control must be excluded. Account owner Account to Identity: ownerKey→uid, provided actual uid target is selectable/searchable and manager02 matches uniquely. Original people uid maps from people.name; do not change global identity mappings to force a match. Verify account owner in the result.

Machine Identity left unmapped, using the documented route without maintained application data. ISC classification creates an uncorrelated application identity for the service account. Inspect actual native identity/account IDs, one-account grouping and access; this is a classified machine representation, distinct from D's ordinary unmatched account. No manually created application identity or user-entitlement grants are needed. Observe application-identity ownership separately; do not infer it from account ownership.

Account Subtype unmapped; no connector-wide subtype, provisioning/password-policy change. Environment mapped from environment; Description from purpose. Save mappings before initial Process Classification. Verify completion, target Machine Accounts/owner02 and control still human/employee01. No manual edits to hide a failed mapping.

## Review, fulfillment and restoration

Use actual Machine Accounts campaign with E only. Account Owner routing when offered must reach manager02. A supported explicit Individual selection of manager02 is recorded as explicit selection, not tested automatic routing. Source-owner fallback manager01 exposes a missing owner and fails intended readiness.

Owner-confirmed exercise facts support continuing nightly Read; Export migration need ended. Approve target Read/Revoke target Export and finalize actual review. Inspect matching full manual work/recipient before editing the complete private E file. Remove only service Export, collect through supported path and verify retained accounts/Read, native machine grouping/owner and human control. Both catalogue definitions remain. File change simulates an external application; no actual program or application permission is verified.

Preserve evidence and resolve outstanding work. If ownership is unchanged, restore the initial private file values. Preserve any legitimate later owner correction and agree a revised training baseline before restoration instead of overwriting it. Collect and prove two accounts/three holdings plus approved native setup. Keep classification/mappings/identity and approved owners; no declassification or account/source/identity deletion as reset. Compare actual identity IDs before claiming continuity.

This package contributes three CSVs. Original ten A/B/D CSVs and native C remain unchanged. No tenant operation, repeated run, learner test or publication is established by this package.
