# X-05: reconciling items across a campaign's certifications

November 13, 2026. Prepared before drafting.

Completion update: [CRT-059](../lessons/CRT-059_Reconciling_Review_Items_Across_an_Entire_Campaign.md) is complete locally with an editable flow and [claim/review evidence](revisions/CRT-059_Revision_Record.md). The pre-draft scope is retained below. No publication or actual learner/tenant validation is implied.

## Distinct useful task

042/044 explain counts, API/report scope and evidence.058 completes paging within one assigned certification. None traces complete campaign membership followed by complete child-item collection and an independently expected account/access set.

Add one focused read-only task reference. Do not repeat the full058 arithmetic or create a scripting course. Preserve the thirty-main sequence and all published work. This ordinary continuation stays local.

## Current primary checks

Fresh relevant clauses inspected in List Certifications, List Review Items, their exact official Python SDK methods and Standard Collection Parameters.

List Certifications is Experimental GET /certification-campaigns/v1/certifications and returns only certifications the caller is authorized to review. Non-admin callers must include reviewer-identity=me. The SDK supports campaignRef.id eq/in filtering, limit/offset/count and certification-specific sort fields. A campaign filter does not expand permission scope; a response total is query/caller scoped.

Child List Review Items is Experimental, identity-campaign scoped, with ORG_ADMIN/CERT_ADMIN or actual-certification-reviewer callers and its own collection parameters. Reset child paging for each certification. Do not copy parent sort fields/filters into the child endpoint or borrow Search searchAfter support.

No universal admin full-scope guarantee, account-to-certification cardinality, global item-ID uniqueness, atomic snapshot, report/API row equivalence or mutable-state history is inferred. General pagination's explicit record-offset definition is retained.

## Complete learner brief

Question: How do you reconcile review items across an entire campaign?

Use a supplied fixed identity campaign with three known expected certifications, R1/R2/R3, and six expected items: two/three/one. Inputs are an independently checked campaign/review/item inventory, unchanged collection, no excluding status/reviewer filters and an authorized investigator whose actual visibility covers the set.

Define campaign/certification/item, IDs, source/account/entitlement, API/GET/query/header and paging locally. Select the actual campaign by campaignRef.id; identify scope before requests. A non-admin personal view is a bounded result.

First collect both parent pages at limit2, offsets0/2. Reconcile all expected parent IDs before child collection. Then retrieve all child pages separately, resetting offset for each certification. Retain certification ID with item ID and actual identity/source/account/access context. Use one working comparison table and an editable two-level collection flow.

The ordinary result matches all three certifications and six intended relationships. It proves presence for this collection, not decisions, final sign-off or source removal.

Changed case1: a missing R3 leaves five retrieved items even when R1/R2 are complete. Changed case2: six rows contain one unexpected account while the required account is missing. Matching totals cannot close that gap. Changed collection/reassignment needs dated interpretation; do not silently merge different versions.

The final transfer begins with a personal list total and asks for all-campaign completeness. Verify authorized scope and expected certification set before claiming full collection.

## Boundaries and completion

Reuse existing214 meanings, refining Expected baseline and Reconciliation locations. Parent/item ID pairs are a practical record association, not an invented native object. No new glossary quota.

Complete learner/asset/evidence, reconcile current local59 versus published58 and run meaningful checks. No060 stub or automatic publication. After the two focused X-05 units, proceed to the combined specialist/core overlap, consistency and beginner-readability pass for051–059, adding content only for an actual gap.

No tenant API, secrets, decision writes, real participant test or publication claim.
