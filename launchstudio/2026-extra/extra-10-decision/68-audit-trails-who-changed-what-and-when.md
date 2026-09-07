---
Title: "Audit Trails: Who Changed What, and When"
Keywords: SaaS audit trail implementation, activity log customer facing, append only audit log, enterprise security questionnaire audit, record history versioning, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: SaaS Founder Scale-Up
---

# Audit Trails: Who Changed What, and When

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Audit Trails: Who Changed What, and When",
  "description": "An audit trail answers the question every business customer eventually asks about their own team, and the one you will need when a customer disputes what happened. What to record, why it must be append-only, and how it differs from technical logging.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-03-30",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/audit-trails-who-changed-what-and-when" }
}
</script>

At some point a customer will email to say that a price was changed, a record was deleted, or a status was set incorrectly, and ask who did it. There are two possible replies. One is a screen showing that a named colleague changed that field, from this value to that value, at 14:32 on Tuesday. The other is an admission that your product does not know.

The second answer costs you more than the individual incident. It tells a business customer that your product cannot support the ordinary internal accountability their other tools provide, and it removes your ability to resolve any dispute — including the ones where your product is blamed for something a member of their team did.

## Audit Trail Is Not Technical Logging

These are frequently conflated and serve different purposes, which leads to products that have one and believe they have both.

**Technical logs** record what the system did: requests served, errors raised, queries executed. They are written for engineers, are usually retained for days or weeks, are noisy, and are not something a customer should ever see.

**An audit trail** records what people did in business terms: "Sanne changed the invoice status from Draft to Sent." It is written for customers and for disputes, is retained for months or years, is deliberately sparse, and is shown in the product.

You can answer "why did the server return an error at 14:32" from logs. You cannot answer "who changed this price" from logs, because the log records that an update endpoint was called, not what the record looked like before. Building one does not give you the other.

## The Fields That Make an Entry Useful

An audit entry is a small, fixed structure, and every field earns its place.

**Who.** The person, not just the account — on a team account "someone at Acme" is useless. Include whether the action was taken by a person, by the system, or by an administrator on their behalf, because that distinction is the first thing anyone asks.

**What.** The action, in language the customer uses. "Invoice status changed", not "PATCH /invoices/4821".

**Which record.** Identified in a way that still makes sense if the record is later deleted — including a human-readable reference, since an internal identifier alone becomes meaningless once the record is gone.

**Before and after.** The single most valuable field and the one most often omitted. "Price changed" is a fraction as useful as "Price changed from €450 to €45", which immediately reveals a missing digit.

**When.** A server-side timestamp in UTC, displayed in the viewer's timezone. Never a time supplied by the browser.

**Context.** Where the action came from — the interface, the API, an import, an administrator. This is what distinguishes a deliberate edit from a bulk operation that swept a record up.

Deliberately excluded: the full contents of the record, and anything sensitive. An audit trail that stores complete before-and-after copies of records containing personal data becomes a second, long-lived database of that data, subject to the same obligations as the first — and one that a deletion request must also reach.

## Append-Only Is the Property That Makes It Worth Anything

An audit trail that can be edited proves nothing. If a record can be altered or removed after the fact, it cannot settle a dispute, because the answer to "did someone change the log" is always "possibly."

In practice this means the audit table permits inserts and nothing else: no updates, no deletes, enforced at the database level rather than by convention. Entries are never modified to reflect a correction; a correction is a new entry. Retention is by policy — old entries removed after a defined period — not by anyone deciding a particular entry should not exist.

This is also why an audit trail should not depend on the application remembering to write to it. If entries are added only where a developer inserted a call, coverage will be incomplete in exactly the places that matter, because the paths nobody thought about are the paths where surprising things happen. Database triggers, or a single layer through which all writes pass, give coverage that does not depend on anyone's diligence.

Getting this right — append-only enforcement, complete coverage, before-and-after values without storing sensitive content — is a well-defined piece of production work that AI-generated products almost never include, since a prototype writes an activity entry only where the prompt happened to mention it. LaunchStudio, backed by Manifera's 11+ years of production engineering, implements audit trails that hold up when a customer, an auditor, or a security questionnaire asks. [Describe your project](https://launchstudio.eu/en/#contact) for a review within one business day.

## What to Record, and What Not To

Recording everything produces a log nobody can read and a table that grows faster than your actual data. Recording too little leaves the gaps that matter.

Worth recording: changes to anything with money attached; changes to permissions and membership; deletions of anything; status changes that drive a business process; exports and downloads of customer data; administrative access to an account; and authentication events such as password changes and new-device logins.

Not worth recording: reads of ordinary records, which multiply enormously and rarely answer a question — with the exception of products handling health, financial, or other sensitive data, where who *viewed* a record is often the central question. Also not worth recording: view and navigation events, which belong in analytics, and every keystroke of a draft, which belongs in versioning if you need it at all.

A reasonable starting point is a dozen or so event types covering money, permissions, deletions, and access. That is enough to answer the questions customers actually ask, and small enough that the trail stays readable.

## Show It to Customers

An audit trail kept only for your own support purposes captures a fraction of its value. Exposed in the product, it becomes a feature.

Two views cover most needs. **Per record**: a history section on an invoice, project, or client showing what changed and who changed it. This is where disputes are resolved, and it resolves them without anyone contacting you. **Per account**: a filterable activity view for owners, showing everything that happened across their organisation.

For business customers this is a purchasing consideration, not a nicety. Any prospect with more than a handful of employees will eventually ask whether they can see who did what, and increasingly it appears in security questionnaires as a checkbox item. Products that already have it answer in a sentence; products that do not either lose the deal or promise a roadmap item.

One caution: showing the trail means members of an organisation can see each other's actions, which is usually intended but should be deliberate. Restricting the account-wide view to owners, while leaving per-record history visible to anyone with access to that record, is a sensible default.

## Real example

### The Discount Nobody Admitted To

Karel Boonstra ran Prijslijst, a quoting and price-list tool for wholesale suppliers, built in Cursor and sold to distributors with sales teams of five to twenty people.

A distributor discovered that a customer-specific price list had been changed: eleven products discounted by roughly 40%, applied across four months of orders and costing them approximately €31,000 in margin. Four people had access. All four denied making the change. The product recorded only the current values, with no history and no record of who had edited what.

The dispute could not be resolved. The distributor concluded, without evidence either way, that the product had done it, and cancelled. Two similar accounts asked whether user-level change history existed, and one deferred renewal pending it.

**Result:** an append-only audit trail with before-and-after values covering price changes, permission changes, deletions, exports, and logins, enforced at the database level with triggers rather than application calls. Per-record history was exposed on every price list and a filterable account activity view added for owners. The cancelled account did not return; the deferred renewal completed, and audit capability became a standard answer in subsequent enterprise questionnaires.

> "Four people, one wrong price list, and my product could not tell anyone which of them did it. I lost the customer over something I would have had for free if I had recorded it from the start."
> — **Karel Boonstra, Founder, Prijslijst**

**Cost & Timeline:** audit trail implementation and customer-facing history delivered in 4 business days.

## Frequently Asked Questions

### Is an audit trail the same as server logging?

No. Logs record what the system did, for engineers, and are kept briefly. An audit trail records what people did, in business terms, for customers and disputes, and is kept far longer. Having one does not give you the other.

### What should an audit entry contain?

Who acted, what they did in the customer's language, which record, the before and after values, a server-side timestamp, and the context such as interface, API, import, or administrator.

### Why must an audit trail be append-only?

Because an editable record proves nothing. If entries can be changed or removed after the fact, the trail cannot settle a dispute. Corrections are added as new entries, never by modifying existing ones.

### Should every action be recorded?

No. Focus on changes involving money, permissions, deletions, status changes driving a business process, data exports, administrative access, and authentication events. Reads are usually excluded unless the product handles sensitive data, where views may be the central question.

### Do customers actually want to see the audit trail?

Business customers with teams do, and it increasingly appears in security questionnaires. Exposing per-record history also resolves internal disputes without anyone contacting your support.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "Is an audit trail the same as server logging?", "acceptedAnswer": { "@type": "Answer", "text": "No. Logs record what the system did, for engineers, kept briefly. An audit trail records what people did in business terms, for customers and disputes, kept far longer. One does not provide the other." } },
    { "@type": "Question", "name": "What should an audit entry contain?", "acceptedAnswer": { "@type": "Answer", "text": "Who acted, what they did in the customer's language, which record, before and after values, a server-side timestamp, and the context such as interface, API, import, or administrator." } },
    { "@type": "Question", "name": "Why must an audit trail be append-only?", "acceptedAnswer": { "@type": "Answer", "text": "An editable record proves nothing. If entries can be altered after the fact the trail cannot settle a dispute. Corrections are new entries, never modifications." } },
    { "@type": "Question", "name": "Should every action be recorded?", "acceptedAnswer": { "@type": "Answer", "text": "No. Record changes involving money, permissions, deletions, business-process status changes, exports, administrative access, and authentication events. Reads are usually excluded unless the data is sensitive." } },
    { "@type": "Question", "name": "Do customers actually want to see the audit trail?", "acceptedAnswer": { "@type": "Answer", "text": "Business customers with teams do, and it appears increasingly in security questionnaires. Per-record history also resolves internal disputes without involving your support." } }
  ]
}
</script>
