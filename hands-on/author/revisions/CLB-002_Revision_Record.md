# CLB-002 author and data record

Revision 1.0. November 14, 2026.
Learner: [Prepare fresh CSV sources and prove the review data](../../lessons/CLB-002_Prepare_Fresh_CSV_Sources_and_Prove_the_Review_Data.md).
Prepared [brief](../briefs/CLB-002_Reviewable_Baseline_Brief.md).
Dataset: [baselineA package](../../lab-data/baselineA/README.md).

## Authored result and execution boundary

The complete setup procedure, explanations, three canonical CSV fixtures, changed-case reasoning and restoration instructions exist. No tenant session was accessed. No source, identity, profile, invitation, collection, owner change, campaign or screenshot was produced by this authoring turn.

The files define concrete values and intended field meanings. They are locally reconciled fixtures, not a universal source template or tested import. The learner downloads the actual Generic source templates and prepares private schema-aligned copies. Reviewer email binding and authentication are explicit setup work, not claimed outcomes.

## Primary checks performed

Official ISC administrator and Generic connector documentation was opened for the affected instructions on November 14. The failed guessed identity-profile path was replaced using official navigation with the setup path below. Unrelated IdentityIQ and File Access Manager search results were not used.

| Reference | Bounded support |
|---|---|
| [Source setup](https://documentation.sailpoint.com/saas/help/sources/config_sources.html) | Standard source creation and authoritative-source/profile relationship. |
| [Generic creation](https://documentation.sailpoint.com/connectors/flat_file/va/help/connecting.html) | Generic name/description/owner setup; recommendation-file import is not account aggregation. |
| [Account schema](https://documentation.sailpoint.com/saas/help/accounts/schema.html) | Schema fields/flags and selecting account keys before aggregation. |
| [Account loading](https://documentation.sailpoint.com/saas/help/accounts/loading_data.html) | Manual account upload, template download, aggregation history and optimized versus full re-evaluation boundary. |
| [Identity profiles](https://documentation.sailpoint.com/saas/help/setup/identity_profiles.html) | Source/profile creation, required uid/email/lastname, mappings, supported local sign-in, preview and Apply Changes. |
| [Account correlation](https://documentation.sailpoint.com/saas/help/accounts/correlation.html) | Explicit account/identity pairing and default name-match fallback. A saved rule alone is not a proven repair. |
| [Manager correlation](https://documentation.sailpoint.com/saas/help/sources/manager_correlation.html) | Both Manager Name mapping and source manager pairing are required. |
| [File structure](https://documentation.sailpoint.com/connectors/flat_file/va/help/flat_file_structure.html) | Header/order and grouped account rows. |
| [Multiple values](https://documentation.sailpoint.com/connectors/flat_file/va/help/handling_multi_value_attributes.html) | One value per repeated account row with consistent scalar values. |
| [Entitlement loading](https://documentation.sailpoint.com/saas/help/loading_entitlements/aggregating_entitlements.html) | Separate catalogue/template, ID matching and the flat-file single-type boundary. |
| [Registration](https://documentation.sailpoint.com/saas/help/common/users/inviting_users.html) | Unique reachable user addresses and the supported manual identity-invitation route. |
| [Managing identities](https://documentation.sailpoint.com/saas/help/identities/identity_mgmt.html) | Enable Identity for an approved disabled test reviewer before registration; ISC login state is separate from source access. |
| [Generic introduction](https://documentation.sailpoint.com/connectors/flat_file/va/help/index.html) | Connector scope and dependency caveat recorded below. |

These checks support bounded instructions. They are not a claim that the user's tenant shows the documented labels or accepted a file.

## Documentation differences preserved for execution

The Generic introduction lists a virtual-appliance prerequisite. Its creation page does not select a cluster. The lesson chooses Generic/manual upload and tells the operator to establish any actual required dependency; it does not promise no VA or silently switch to Delimited File SaaS/SFTP. Record the selected mode and actual dependency during execution.

The Generic import page has both schema-upload wording and conflicting statements about schema alteration. The current ISC schema/account-loading guides supply the scoped workflow used here. Preserve the actual downloaded templates rather than treating the narrow canonical headers as mandatory schema replacements.

The generic schema guide and entitlement-type guide describe linking with different emphasis. This lab retains the actual built-in single entitlement association for groups and proves the resulting records; it does not guess another connector's type name or create extra flat-file types.

No runtime result is inferred for sign-in enablement, task routing, default feature availability or review grouping. Those remain actual setup/run checks. No inherited theory verification item was closed.

## Beginner author reading and changes

Read the saved learner from opening through restoration and the full worked answer. Rechecked the edited supporting explanations.

The opening names a concrete result and explains a permission holding. CSV, source, identity profile, authoritative source, schema, String, entitlement, aggregation, identity processing and both kinds of correlation have local meanings. Later references to access profiles, roles and lifecycle grants explain why the simple baseline excludes them.

Employee02 is followed through the supplied key values, its identity, report account, rights and manager. The worked case states accounts are unassigned, names differ and the intended pairing is absent. Correct descriptions cannot repair that missing ownership link. The answer avoids assuming a rule save re-correlates existing records.

The initial source owner is the existing operator, avoiding the circular prerequisite of selecting manager02 before importing it. The later owner selection uses the actual manager02 identity. Registration is separate from creating its CSV record. No imaginary password or usable mailbox is supplied.

The final actor pass added the documented Enable Identity step for a disabled test manager rather than leaving the learner with an unexplained instruction to resolve enablement. Rechecked the changed passage and its separation of ISC login access from reporting permissions.

No continuing company/character, course/source links in learner prose, invented screenshot, fixed diagram quota or unexplained passing result was added.

## Local data reconciliation

The three fixtures have five people rows, five account-permission rows representing three accounts, and two catalogue definitions. All keys are unique where required. Every manager reference resolves; there are no manager cycles. Repeated account scalars agree, account rows are contiguous and every permission value has catalogue metadata.

Read appears on three accounts and Export on two. Removing only employee02's Export produces four holdings and preserves all three Read holdings. This is a local fixture calculation, not an ISC decision or application change.

SHA-256 of the saved canonical files:

- people.csv: c44d4a13e1826ce68ba2725ad5ef591d6240c1ff8784b13566f8331951409ff3
- report_accounts.csv: 80ac3d6690e476328b6468e3abd0056438ae1e0333bfb1b71dcfb8c3ac96045e
- report_entitlements.csv: 502245ed0cf8a6fb0b31e1469d3da62ce506ca4347404aef1bec1c5a21fb83de

## Actual state

Local package checks passed23 files,19 Markdown documents,39 relative links,22 consistent table groups across230 rows, two complete learner files and23 matching design/register planning IDs. CSV structure, key/reference checks, repeated-row grouping and the five-to-four holding calculation passed. These are local author/data checks. The separate theory repository remains clean at1f1028a89ba8d266c80710dc5424dcafd160760d.

Authored and source/language reviewed:002 revision1.0. Canonical fixtures authored:3. Actual source-template binding/import: not run. Tenant execution, repeated run, reviewer sign-in test and independent learner validation: not run. Local only; no repository, Pages deployment or push.
