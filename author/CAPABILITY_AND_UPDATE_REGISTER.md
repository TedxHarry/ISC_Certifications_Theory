# Capability, update and open-question register

Version 1.1. October 29, 2026.
Source leads: [official source map](../AUTHOR_SOURCE_MAP.md).
Purpose: stop unsupported current/legacy/availability claims entering lessons.

A documentation scoping check is not a tenant test or final lesson verification. Exact relevant claims must be checked when the lesson is written and before affected publication. No exhaustive release-by-release audit or tenant-specific availability check has been completed.

## Working baseline

Use next-generation campaign examples where supported. Mark a bounded legacy or conditional case when relevant. The current official overview describes phased availability and migration; the next-generation API is marked Experimental. Do not label a capability generally available merely because it appears in documentation.

The administrative help paths currently use Identity Services/Human Fabric headings. This course retains ISC naming and does not import similarly titled IdentityIQ or File Access Manager behavior.

## Capability inventory

All dates below are October 29, 2026. “Scoping checked” means source reviewed for curriculum planning; per-lesson verification and target-tenant execution remain pending.

| Key | Capability / claim area | Engine and availability handling | Primary source and current check | Affected topics |
|---|---|---|---|---|
| CAP-01 | Purpose, campaign/review objects and administrator responsibility | Stable concepts; actual permission/actions checked for applicable engine. | [Overview](https://documentation.sailpoint.com/saas/help/certs/index.html), scoping checked and refreshed during setup. | CRT-001–004/021/022 |
| CAP-02 | Next-generation migration and APIs | Overview describes phased availability; API marked Experimental and engine-scoped. No universal tenant-availability claim. | [Overview](https://documentation.sailpoint.com/saas/help/certs/index.html), [next-generation APIs](https://developer.sailpoint.com/docs/api/next-generation-certification-campaigns/), refreshed during setup. | All affected flows; X-05 |
| CAP-03 | Role-composition review | Current overview/search guidance keeps it legacy; recheck before deeper authoring. | [Search campaign guidance](https://documentation.sailpoint.com/saas/help/certs/starting_search_campaign.html), scoping checked. | CRT-015; X-01 |
| CAP-04 | Certifiable access and assignment origin | Roles/access profiles/entitlements and automated/lifecycle grant behavior need exact example scope. | [Understanding certifications](https://documentation.sailpoint.com/saas/help/certs/understanding_certifications.html), refreshed during setup. | CRT-006/007/028/035 |
| CAP-05 | Manager/source-owner versus targeted selection | Verify campaign-specific data prerequisites, exclusion and fallback behavior; do not combine different routes into one rule. | [Manager/source-owner campaigns](https://documentation.sailpoint.com/saas/help/certs/starting_campaign.html), [Search](https://documentation.sailpoint.com/saas/help/certs/starting_search_campaign.html), scoping checked. | CRT-011–016/023 |
| CAP-06 | Filters and access refinement | Verify criteria scope and grouping/combination; no assumed SQL semantics or inclusion/exclusion precedence. | [Campaign filters](https://documentation.sailpoint.com/saas/help/certs/campaign_filters.html), scoping checked. | CRT-014/017/018 |
| CAP-07 | Generation, templates, schedules and preview | Verify what is generated, when values are captured, and which step requires activation. | [Search campaign guidance](https://documentation.sailpoint.com/saas/help/certs/starting_search_campaign.html), scoping checked. | CRT-019–021 |
| CAP-08 | Reviewer routing and self-certification | Verify owner hierarchy, group behavior, fallback and self-review handling for the exact campaign. | [Understanding certifications](https://documentation.sailpoint.com/saas/help/certs/understanding_certifications.html), [Search](https://documentation.sailpoint.com/saas/help/certs/starting_search_campaign.html), scoping checked. | CRT-022–024 |
| CAP-09 | Reassignment and reviewer visibility | Verify administrative/reviewer action scope, state, permissions and work reassignment. | [Reassignment](https://documentation.sailpoint.com/saas/help/certs/config_reassignment.html), scoping checked. | CRT-025/026/045 |
| CAP-10 | Decisions, sign-off, unsigned completion | Known conflicting passages; see OQ-01. No universal unsigned-completion answer recorded. | [Understanding](https://documentation.sailpoint.com/saas/help/certs/understanding_certifications.html), [Completion](https://documentation.sailpoint.com/saas/help/certs/completing_campaigns.html), conflict refreshed during setup. | CRT-028/030/039/040 |
| CAP-11 | Revocation timing and remediation phase | Verify exact trigger/date/state for the engine; see OQ-02. Do not infer a universal private sequence. | [Understanding](https://documentation.sailpoint.com/saas/help/certs/understanding_certifications.html), [API overview](https://developer.sailpoint.com/docs/api/next-generation-certification-campaigns/), scoped, exact timing unresolved. | CRT-003/032–040/046 |
| CAP-12 | Manual/automatic fulfillment, overlap and failures | Verify source write permission, supported operation, actual task assignment and grant paths. | [Reviewer guidance](https://documentation.sailpoint.com/saas/user-help/certs/reviewing/index.html), [Completion](https://documentation.sailpoint.com/saas/help/certs/completing_campaigns.html), scoping checked. | CRT-033–037/046 |
| CAP-13 | Notifications, deadlines, reports and retirement | Verify settings/state/engine and which report is available when; do not treat status/report fields as universal. | [Completion](https://documentation.sailpoint.com/saas/help/certs/completing_campaigns.html), [Reports](https://documentation.sailpoint.com/saas/help/certs/campaign_status_reports.html), scoping checked. | CRT-038–044 |
| CAP-14 | Specialist capability and rich context | Core recognition is required; exact licensed/phased behavior checked before deeper route claims. | [Search](https://documentation.sailpoint.com/saas/help/certs/starting_search_campaign.html), [Reviewer guidance](https://documentation.sailpoint.com/saas/user-help/certs/reviewing/index.html), scoping checked. | CRT-008/015/027/031; X-01–05 |

## Open questions

| Question | Evidence / unresolved point | Writing treatment and next verification |
|---|---|---|
| OQ-01: Unsigned decisions at administrator completion | Understanding guidance treats unsigned reviews as undecided at completion; completion guidance also says saved manager decisions may be preserved. No authoritative reconciliation or tenant observation exists here. | Establish exact engine/type, recheck current guidance and seek authoritative clarification or explicitly permitted controlled observation. Do not assign either description universally. CRT-030/039/040 need resolution or a clearly verified narrower scope. |
| OQ-02: Exact remediation trigger and campaign phases | Administrative guidance describes initiation at sign-off; developer overview also describes a campaign-level remediation phase after reviewers finish. These may describe different scopes or engines; the relationship has not been established here. | Verify the engine-specific event/state path before exact timing diagrams or claims. Stable purpose and the distinction between decision/delivery/evidence can be taught without inventing that timing. |
| OQ-03: Exact tenant capability and permission matrix | No target tenant, entitlement/license inventory or actual user-level test has been supplied or inspected. | Teach verified documented conditions. Identify prerequisites per affected lesson; do not claim screenshots or behavior observed in a tenant. |
| OQ-04: Exhaustive current-update coverage | Ten primary scoping sources have been reviewed; this is not a release-by-release completeness audit. A discoverable announcement FAQ failed direct retrieval in the earlier check. | Recheck authoritative release information during authoring/publication, maintain the change log below and record unavailable evidence. Do not promote roadmap/search snippets to released behavior. |

These questions affect particular claims. They do not block writing the verified purpose and business reasoning in CRT-001.

## First authored application

CRT-001 revision 1.0 uses CAP-01's stable purpose/objects, a bounded CAP-04 individually reviewable entitlement and CAP-12's distinction between a removal decision and its applicable delivery. Six official pages were freshly checked October 29, 2026 in [the lesson record](revisions/CRT-001_Revision_Record.md).

It explains finishing/confirming a review but makes no exact unsigned-completion or universal remediation-phase timing claim. OQ-01 and OQ-02 remain unresolved, and OQ-03/04 remain pending. This is one bounded learner verification, not a whole-engine, tenant-availability or exhaustive-release validation.

## Update log and authoring protocol

For each actual relevant change, record:
- Capability/change and primary source, publication/update date and verification date.
- Available, limited/phased, legacy, planned or unresolved status, with engine and prerequisites.
- Affected learner IDs/sections, examples, diagrams, decisions and evidence.
- What changed in the teaching, and the exact source/tenant checks actually performed.
- Review and publication status.

Do not create fake release entries to fill a register. No release-completeness claim is recorded at setup. This is a manual authoring/maintenance record, not an automated monitoring service.

Before marking a lesson technically checked, link the concrete claims to sources in its own author record. Record unresolved scope rather than using “verified” for a whole document that contains unchecked behavior.

Never perform a live campaign, source permission change, email, API mutation or remediation experiment merely to clear an authoring note. Such actions need authorization in the actual task context.
