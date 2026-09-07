---
Title: "Two-Way Sync and Who Wins When Both Sides Change"
Keywords: two way sync conflict resolution, bidirectional integration design, sync loop prevention, last write wins problem, one way sync vs two way, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: Technical Solo Founder / Indie Hacker
---

# Two-Way Sync and Who Wins When Both Sides Change

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Two-Way Sync and Who Wins When Both Sides Change",
  "description": "Customers ask for two-way sync as though it were one-way twice. It is a different problem: conflicts, loops, deletions with no clear meaning, and identity matching across systems. What to decide before building, and why one-way sync is often the better answer.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-04-13",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/two-way-sync-and-who-wins-when-both-sides-change" }
}
</script>

"Can it sync both ways?" sounds like a request for twice as much of something you already do. It is not. One-way sync has a single source of truth and a simple job: make the other side match. Two-way sync has no source of truth, which means every question it faces — what happened, which version is correct, is this a new record or an existing one — has to be answered by rules you invent, and the wrong rules destroy customer data quietly.

This is one of the few features where the right response to a customer request is often a different feature. Before building, it is worth establishing what they actually need, because a substantial share of two-way requests are satisfied by one-way sync plus the ability to edit in one place.

## The Four Problems That Do Not Exist One-Way

**Conflicts.** The same record is changed in both systems between syncs. Someone updated the phone number in your product; someone else updated it in their CRM. Both are legitimate, they disagree, and something has to decide.

**Loops.** Your product writes to their system, which fires a change notification, which your product receives and applies, which triggers another write. Without loop prevention this runs continuously, and the first sign is usually a rate-limit ban or a bill.

**Deletion ambiguity.** A record present last sync is now absent. Was it deleted deliberately, moved out of a filtered view, archived, or is it missing because a request failed? Treating all four as deletion destroys data; treating none as deletion means deletions never propagate.

**Identity.** Is this contact in their system the same person as this contact in yours? Without a shared identifier you are matching on email or name, and both produce false matches — one person with two addresses, two people at the same company sharing an inbox.

Each has established solutions. All of them require decisions from you, and the cost of the feature is mostly in making those decisions well rather than in the code that implements them.

## Choosing a Conflict Rule and Telling the Customer

Four workable approaches, in increasing order of effort.

**Last write wins.** Whichever change is more recent is kept. Simple, and it silently discards the other edit. Acceptable for low-stakes fields, dangerous for anything a business depends on — and unreliable in practice, since clocks on two systems disagree and "more recent" is often not knowable to the precision required.

**One side always wins per field.** Your product owns the appointment time, their system owns the customer's address. Predictable, explainable, and usually the best answer for a first implementation, because it converts an unbounded problem into a table of decisions.

**Merge at field level.** If they changed the phone and you changed the email, keep both. Works when different fields are genuinely independent, fails when fields relate to each other.

**Ask the customer.** Flag the conflict and let a person decide. The only approach that never loses data, and unusable at volume — but a good fallback for high-value records where the automatic rule is uncertain.

Whatever you choose, the customer must be told, in the interface, before they connect. "Changes made in your CRM will overwrite changes made here" is a sentence that prevents a category of angry emails, and its absence is why customers experience sync as a system that eats their work.

And keep a record of every sync decision: what was changed, in which direction, and why. Without it, "the address is wrong and I do not know how it got that way" is unanswerable, and sync problems are almost always reported in exactly that form.

## Loops, Identity, and the Machinery Underneath

Loop prevention is not optional. The standard techniques are to tag writes as originating from sync so the resulting notification is ignored, and to compare content before writing so that an incoming change identical to what you already hold produces no write at all. Both should be in place before the first two-way connection goes live, because a loop discovered in production is a loop that has already made several thousand requests.

Identity requires a mapping table: your identifier, their identifier, and when they were last reconciled. Matching should happen once, at connection, ideally with the customer reviewing ambiguous cases. Matching on the fly by email every sync is how one person becomes two records, or two people become one.

Deletion needs a stated policy, and the safest is usually not to propagate deletions at all in the first version — mark the record as no longer present in the other system and let a human act. Deletion is the one operation where a bug is irreversible, and the conservative choice costs little.

Then there is the machinery: sync is background work, needs to be resumable after failure, must respect the other system's rate limits, and should never assume it completed. A sync that silently stops is functionally identical to no sync at all, so connection health and last-successful-sync time belong in the product where the customer can see them.

Building sync that resolves conflicts predictably, avoids loops, maintains identity, and reports its own health is a substantial and well-understood piece of engineering — considerably more than the "connect two APIs" that the request implies. LaunchStudio, backed by Manifera's 11+ years of production engineering, builds integrations of this shape, including the reconciliation and reporting that make them trustworthy. [Describe your project](https://launchstudio.eu/en/#contact) for a review within one business day.

## Ask What They Actually Need

Before committing, the useful question is not "do you want two-way sync" — everyone says yes to that — but "where do you want to make changes?"

Most answers reveal a one-way need. A customer who wants appointments booked in your product to appear in their calendar, and never edits them in the calendar, needs one-way sync. A customer who maintains contacts in their CRM and wants them available in your product needs one-way sync in the other direction. Two-way is genuinely required only when both systems are legitimately edited by different people for different reasons.

Where two-way is required, three scoping decisions reduce the difficulty substantially. **Sync a subset of fields**, not whole records: the four fields that matter, not everything. **Sync a subset of records**, filtered by something meaningful, so the volume and the blast radius are smaller. And **start one-way, add the second direction later**, once the identity mapping and monitoring have proven themselves on the easier problem.

A useful intermediate for many products: one-way sync plus a link back to the record in the other system. Customers get the data where they need it and an obvious place to make changes, which is often what they wanted when they asked for two-way.

## Real example

### The Loop That Made 90,000 Requests in a Weekend

Bas Kuipers ran Klantbeeld, a light CRM for regional installation companies, built in Lovable. A customer wanted contacts synchronised with their accounting package, and two-way sync was implemented straightforwardly: on change, write to the other side.

It ran for nine days before the customer edited a contact in the accounting package while Klantbeeld was writing an update to the same record. Each write triggered the other side's change notification. Over the weekend the two systems exchanged roughly 90,000 requests, the accounting provider suspended the integration for abuse, and the contact's address had been overwritten forty times, ending on a value that had been correct three months earlier.

Two other problems appeared during the investigation. Contacts had been matched by email on every sync, and eleven records where two employees shared a company address had been merged into one, mixing two people's history. And a contact deleted in the accounting package because of a duplicate had propagated a deletion into Klantbeeld, removing the record that carried all the service history.

**Result:** the integration was rebuilt as one-way from the accounting package for contact details, with Klantbeeld owning service history and appointments; a persistent identity mapping created with customer review of ambiguous matches; loop prevention through origin tagging and content comparison; deletions surfaced for human confirmation rather than propagated; and a sync log visible to the customer.

> "They asked for two-way sync and I said yes without asking what they would edit where. It turned out the answer was that they only ever edited one side."
> — **Bas Kuipers, Founder, Klantbeeld**

**Cost & Timeline:** sync redesign and data reconciliation delivered in 5 business days.

## Frequently Asked Questions

### Is two-way sync just one-way sync in both directions?

No. It introduces conflicts, loops, ambiguous deletions, and identity matching, none of which exist one-way. The engineering cost is several times higher and most of it is in deciding rules rather than writing code.

### What is the safest conflict resolution rule to start with?

Assigning ownership per field — your product owns some fields, the other system owns others — is predictable and explainable. Last write wins is simplest but silently discards edits and depends on clocks that disagree.

### How do sync loops happen?

Your write triggers a change notification from the other system, which your product applies, triggering another write. Tagging sync-originated writes and comparing content before writing prevents it, and both must be in place before going live.

### Should deletions propagate between systems?

Not in a first version. A record's absence has several possible meanings, and deletion is the one operation that cannot be undone. Surfacing it for a person to confirm is the safer default.

### How do I know whether a customer really needs two-way sync?

Ask where they intend to make changes. If edits happen in one system and are only read in the other, one-way sync is sufficient, and a link back to the source record often satisfies what they were asking for.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "Is two-way sync just one-way sync in both directions?", "acceptedAnswer": { "@type": "Answer", "text": "No. It introduces conflicts, loops, ambiguous deletions, and identity matching, none of which exist one-way, and most of the cost is in deciding rules rather than writing code." } },
    { "@type": "Question", "name": "What is the safest conflict resolution rule to start with?", "acceptedAnswer": { "@type": "Answer", "text": "Ownership per field, where each system owns particular fields. Last write wins is simplest but silently discards edits and relies on clocks that disagree." } },
    { "@type": "Question", "name": "How do sync loops happen?", "acceptedAnswer": { "@type": "Answer", "text": "A write triggers a change notification from the other system, which is applied and triggers another write. Tagging sync-originated writes and comparing content before writing prevents it." } },
    { "@type": "Question", "name": "Should deletions propagate between systems?", "acceptedAnswer": { "@type": "Answer", "text": "Not in a first version. Absence has several possible meanings and deletion cannot be undone, so surfacing it for human confirmation is safer." } },
    { "@type": "Question", "name": "How do I know whether a customer really needs two-way sync?", "acceptedAnswer": { "@type": "Answer", "text": "Ask where they intend to make changes. If edits happen in one system and are only read in the other, one-way sync with a link back to the source record is usually enough." } }
  ]
}
</script>
