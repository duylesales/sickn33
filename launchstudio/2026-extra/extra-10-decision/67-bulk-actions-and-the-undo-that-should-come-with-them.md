---
Title: "Bulk Actions and the Undo That Should Come With Them"
Keywords: bulk delete SaaS safety, select all danger, undo bulk action, batch operation background job, confirmation dialog design, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: AI-Native Founder (Non-Technical)
---

# Bulk Actions and the Undo That Should Come With Them

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Bulk Actions and the Undo That Should Come With Them",
  "description": "A bulk action turns one careless click into hundreds of changes, and select-all is the most dangerous control in most products. What a safe bulk operation needs: scoped selection, honest confirmation, background execution, partial-failure reporting, and a way back.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-03-28",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/bulk-actions-and-the-undo-that-should-come-with-them" }
}
</script>

Customers ask for bulk actions as soon as they have enough records to make one-at-a-time work tedious, and the request sounds modest: a checkbox column, a select-all box, and a delete button. What that adds to your product is a control that converts a single misjudged click into hundreds of irreversible changes, operating on data you cannot regenerate, usually with a confirmation dialog that nobody reads.

The feature is worth building — the tedium it removes is real, and customers who have to click through 400 records one at a time will eventually stop using the product. But bulk operations sit in the small category of features where the ordinary standard of care is not enough, and where the difference between a good implementation and a generated one is measured in customer data.

## What "Select All" Actually Means

The first ambiguity is the one that causes the most damage, and it is invisible in the interface: does the select-all checkbox select the 50 rows currently visible, or all 12,000 rows matching the current filter?

Both behaviours exist in real products. Both are defensible. What is not defensible is leaving the customer to guess, which is exactly what a bare checkbox does. Someone who filters to "inactive clients", sees 50 rows, ticks select-all, and presses delete may be deleting 50 records or 12,000 — and will find out afterwards.

The fix is to be explicit in words: "50 rows on this page selected. Select all 12,000 matching your filter?" as a distinct second action. Then the destructive step states the number it will actually affect: "Delete 12,000 clients?" rather than "Are you sure?". A count is the single most effective safety mechanism available here, because it is the one piece of information that distinguishes the intended action from the catastrophic one, and it costs nothing to display.

## Confirmation That Actually Confirms

A dialog asking "Are you sure?" with OK and Cancel is a reflex, not a decision. People dismiss it without reading, particularly the second and subsequent times.

Proportionate confirmation looks different depending on scale and reversibility. For a small, reversible action — archiving twelve items — no dialog at all is often correct, replaced by a confirmation *after* the fact with an undo option. For a large or irreversible action, the confirmation should require thought: state the number, state what will happen to related data, and for genuinely destructive operations require typing something, such as the count or the word delete.

Two supporting details matter. Name the consequences that are not obvious: "this will also remove 4,300 invoices belonging to these clients" is the information the customer actually needs, and it is precisely what cascade rules do silently. And never make the destructive option the default focus, so that a stray Enter keypress cannot trigger it.

## Prefer Reversible Operations

The strongest safety measure is not a better dialog. It is making the action recoverable, so that the confirmation matters less.

**Soft delete** — marking records as deleted and hiding them, with a purge after a defined period — turns the worst possible bulk mistake into a recoverable one. It costs a column and some query filters if designed in early, and it is the single highest-return decision in this whole area.

**Archive instead of delete** where the customer's real intent is "get these out of my way." Most bulk deletions are motivated by clutter rather than a genuine need to destroy data, and offering archive as the prominent action with delete available but quieter matches what people actually want.

**Undo windows** for bulk changes: tag every record affected by one operation with a shared identifier, and offer "undo this change" for a period afterwards. This is straightforward when designed in and effectively impossible to retrofit, because after the fact there is no record of which rows a given action touched.

That last point generalises. A bulk operation should leave a trace — what was done, to how many records, by whom, when, and which specific records were affected. Without it, "someone deleted 300 clients last Thursday" is unanswerable, and so is any attempt to reverse it.

## Bulk Operations Are Background Work

The same constraint that governs imports and exports applies here. Updating 5,000 records inside a web request will hit a platform timeout, and the failure mode is the worst one available: some records changed, some not, the customer looking at an error with no idea which is which.

The right shape is to accept the request, perform the work in the background in batches, and report progress. This also allows the operation to be throttled so a large bulk update does not degrade the product for everyone else — a real consideration, since one customer's cleanup of 40,000 records can saturate a shared database.

Then there is partial failure, which bulk operations produce far more often than single ones. Of 500 records, seven fail — one is referenced by something that prevents deletion, another has already been changed by a colleague. The customer must be told precisely: "493 updated, 7 could not be changed", with the seven identified and the reason given. What must never happen is a green success message covering an operation that partly failed, which is the standard behaviour of a generated implementation that wraps the loop in a single try block.

Building bulk operations that run in the background, report partial failures honestly, and can be undone is ordinary production engineering, and it is consistently absent from AI-generated products where the feature is implemented as a loop inside a request handler. LaunchStudio, backed by Manifera's 11+ years of production engineering, builds these paths with proper batching, progress, and reversal. [Describe your project](https://launchstudio.eu/en/#contact) for a review within one business day.

## Authorisation Applies Per Record, Not Per Request

A quieter risk: bulk endpoints frequently accept a list of record identifiers and act on them without verifying that the requester is entitled to each one.

In a single-record operation, the check usually exists because the record is fetched and its ownership is apparent. In a bulk operation the implementation tends to become "delete where id in this list", and if permission is checked once for the request rather than for every identifier, a modified request can reach records belonging to another account entirely.

The rule is that every record in a bulk operation must pass the same authorisation check it would as a single operation, enforced on the server. Where the database supports row-level policies, letting them apply to bulk statements is the most reliable way to get this right, because it removes the possibility of the check being forgotten.

The same applies to who is permitted to perform bulk actions at all. On team accounts, mass deletion is a reasonable thing to restrict to owners, since the blast radius of a member's mistake is proportionally larger.

## Real example

### Two Hundred Clients Deleted by a Filter That Had Not Applied

Tomas Rietveld ran Adresboek Pro, a contact-management tool for recruitment agencies, built in Lovable. A customer asked for bulk delete to clean up dormant contacts, and it was added in an afternoon: checkboxes, a select-all box, a delete button, and an "Are you sure?" dialog.

A recruiter filtered to contacts not touched in two years, saw 43 results, ticked select-all, and deleted. The filter had been applied to the visible page but the select-all sent every contact id the frontend had loaded — 214 records, including active clients on other pages of the same unfiltered list.

The deletion was permanent. The related notes and placement history were removed by cascade rules nobody had reviewed. The operation ran inside the request and timed out after 180 of 214 records, showing an error, so the recruiter clicked delete again on what remained. Nothing in the system recorded which records had been affected.

Recovery required restoring a backup from that morning into a separate database, identifying the missing contacts, and reinserting them — losing the notes added between the backup and the deletion.

**Result:** soft delete with a 30-day recovery window, explicit page-versus-filter selection with the affected count stated, typed confirmation for deletions over 50 records, background execution with progress and partial-failure reporting, per-record authorisation, and operation tagging enabling a one-click undo.

> "The dialog said 'Are you sure?'. It could not tell her she was about to delete 214 records instead of 43, because nobody had asked it to count."
> — **Tomas Rietveld, Founder, Adresboek Pro**

**Cost & Timeline:** bulk operation rebuild with soft delete and undo delivered in 4 business days.

## Frequently Asked Questions

### What should a select-all checkbox actually select?

Whichever you choose, say it in words. Selecting the current page while implying everything matching the filter, or the reverse, is the most common cause of accidental mass changes. Offer selecting all matching records as a separate, explicit action.

### Are confirmation dialogs enough to prevent bulk mistakes?

No. Generic dialogs are dismissed reflexively. Stating the exact number affected, naming cascading consequences, and requiring typed confirmation for large destructive actions works considerably better — and reversibility works better still.

### Should bulk delete be a real delete?

Rarely. Soft deletion with a recovery window turns the worst mistake into an inconvenience, and most bulk deletions are motivated by clutter, which archiving serves better than destruction.

### Why do bulk operations fail halfway through?

Because they are commonly implemented inside a web request, which platforms terminate after a fixed period. Running them as background work in batches, with progress and partial-failure reporting, avoids leaving the customer unable to tell what changed.

### Is there a security risk specific to bulk actions?

Yes. Bulk endpoints often check permission once for the request rather than for each record identifier supplied. Every record must pass the same authorisation check it would individually, enforced on the server.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "What should a select-all checkbox actually select?", "acceptedAnswer": { "@type": "Answer", "text": "Whichever you choose, state it in words. Ambiguity between the current page and everything matching a filter is the most common cause of accidental mass changes." } },
    { "@type": "Question", "name": "Are confirmation dialogs enough to prevent bulk mistakes?", "acceptedAnswer": { "@type": "Answer", "text": "No. Generic dialogs are dismissed reflexively. Stating the exact count, naming cascading consequences, and requiring typed confirmation for large destructive actions works better, and reversibility better still." } },
    { "@type": "Question", "name": "Should bulk delete be a real delete?", "acceptedAnswer": { "@type": "Answer", "text": "Rarely. Soft deletion with a recovery window turns the worst mistake into an inconvenience, and most bulk deletions are about clutter, which archiving serves better." } },
    { "@type": "Question", "name": "Why do bulk operations fail halfway through?", "acceptedAnswer": { "@type": "Answer", "text": "They are commonly implemented inside a web request, which platforms terminate after a fixed period. Background execution in batches with progress and partial-failure reporting avoids the ambiguity." } },
    { "@type": "Question", "name": "Is there a security risk specific to bulk actions?", "acceptedAnswer": { "@type": "Answer", "text": "Yes. Bulk endpoints often check permission once per request rather than per record. Every record must pass the same authorisation check it would individually, enforced on the server." } }
  ]
}
</script>
