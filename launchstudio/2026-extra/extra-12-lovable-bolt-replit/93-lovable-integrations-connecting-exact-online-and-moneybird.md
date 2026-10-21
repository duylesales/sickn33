---
Title: "Lovable Integrations: Connecting Exact Online and Moneybird"
Keywords: lovable integrations, Exact Online API, Moneybird API, accounting integration, OAuth refresh tokens, VAT codes, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: AI-Native Founder (Non-Technical)
---

# Lovable Integrations: Connecting Exact Online and Moneybird

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Lovable Integrations: Connecting Exact Online and Moneybird",
  "description": "The integration Dutch B2B customers ask for most is the one with their accounting package. Which side owns what, mapping ledger accounts and VAT codes, OAuth tokens that rotate, duplicate prevention, sync status customers can see, and when a unified accounting API is the better choice.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-03-17",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/lovable-integrations-connecting-exact-online-and-moneybird" }
}
</script>

Ask a Dutch B2B customer what would make your product indispensable, and a large share will say the same thing: "If it talked to our accounting package." Invoices typed twice — once in your product and once in Exact Online or Moneybird — are the most common manual task your customers have, and the most common reason a bookkeeper resists a new tool.

The integration looks simple in a demonstration: connect the account, send an invoice, see it appear. AI tools can produce that in an afternoon. What they produce rarely survives a month of real use. Tokens expire and the connection silently stops. A timeout sends the same invoice twice. A hard-coded VAT code books revenue in the wrong place in half your customers' administrations. And nobody can see which invoices arrived and which did not, so the bookkeeper stops trusting the integration and goes back to typing.

This article covers how to build an accounting integration that bookkeepers trust: the decisions to make before writing code, the mapping that differs per customer, the token handling that keeps the connection alive, duplicate prevention, visibility, and when to buy rather than build.

## The Landscape

The Dutch market for small and medium business accounting is concentrated in a handful of packages.

**Exact Online** — the largest, used by many accountancy firms on behalf of their clients, with a comprehensive REST API organised around divisions (administrations), relations, sales entries and sales invoices.

**Moneybird** — popular with freelancers and small businesses, with a clean modern API organised around administrations, contacts and sales invoices.

**Twinfield, SnelStart, e-Boekhouden.nl, AFAS** — each significant in particular segments, each with its own API and its own conventions.

Start with the one most of your customers use — ask them rather than guess — and design the integration so a second package can be added without rewriting the first. Most products need two within a year.

## Decide Who Owns What

The most important decisions are made before any code, and AI-generated integrations skip them entirely.

**Who owns invoice numbering?** Either your product issues the invoice with its own number and sends it to the accounting package as a booking, or the accounting package issues the invoice and your product creates it there. Both are valid; mixing them produces two numbering sequences and a bookkeeper who cannot reconcile anything. For products that generate and send invoices themselves — with their own PDFs, as the document generation article in this series describes — the usual answer is that your product owns numbering and pushes a sales entry or invoice with your number as the reference.

**Who owns customers?** When a new customer is created in your product, is a relation created in Exact? When an address changes in Exact, does it change in your product? Pick a direction per field, or the two systems will overwrite each other.

**Who owns payment status?** Payments usually arrive in the bank account that the accounting package reads. If your product needs to show whether an invoice is paid, the status comes from the accounting package — by polling or webhook — not from a guess.

**What happens after an invoice is sent to accounting?** Usually it should be locked in your product. Editing an invoice that has already been booked creates a difference that only a credit note can fix, as the refunds article in this series describes.

Write these decisions down, show them in the integration settings, and explain them to customers. "Invoices are created in [Product] and booked in Exact as sales entries; payments are read back from Exact every hour" answers most of a bookkeeper's questions before they ask.

## Mapping Is Per Customer

The second failure of generated integrations: they assume every administration is set up the same way. They are not.

**Ledger accounts (grootboekrekeningen).** Revenue for services might be 8000 in one administration, 8100 in another, and split across three accounts by product line in a third. Your product must let each organisation map its revenue categories to its own ledger accounts.

**VAT codes (btw-codes).** In Exact, VAT codes are configured per administration, and the code for "21% high rate" is not the same everywhere. A hard-coded VAT code books VAT incorrectly in some administrations and fails in others. Fetch the available VAT codes from the customer's administration through the API, let the customer map each of your VAT rates — 21%, 9%, 0%, reverse charge, intra-EU — to one of theirs, and validate the mapping before the first sync.

**Journals and cost centres.** The sales journal to book in, and optionally cost centres or projects, again differ per administration.

**Divisions and administrations.** An accountancy firm's Exact login can see dozens of client administrations. The customer must choose which division the integration writes to, and the integration must never write to any other.

Build a mapping screen that loads the real lists — ledger accounts, VAT codes, journals — from the connected administration and stores the customer's choices. Validate it before activation and again whenever a sync fails because a mapped code no longer exists.

## OAuth Tokens That Stay Alive

Both Exact Online and Moneybird use OAuth 2.0: the customer signs in to their accounting package, approves access, and your product receives an access token and a refresh token. This is the part of the integration that most often breaks in production.

**Store tokens encrypted, per organisation.** Refresh tokens are long-lived credentials to a customer's entire bookkeeping. Encrypt them at rest, never expose them to the browser, and keep them out of logs. The secrets articles in this series apply in full.

**Refresh before expiry, not after failure.** Exact access tokens are short-lived — minutes rather than hours. Refresh them shortly before they expire rather than waiting for a request to fail.

**Handle rotating refresh tokens.** When a refresh token is used, Exact issues a new one and the old one stops working. If two processes refresh at the same time — a scheduled sync and a user action, or two workers — one succeeds, the other uses a now-invalid token, and depending on timing the stored token can end up being the invalid one. The connection is then broken until the customer re-authorises. This is the single most common reason Exact integrations "randomly disconnect".

The fix is to serialise refreshes per organisation:

```sql
-- inside a transaction in the worker
select pg_advisory_xact_lock(hashtext('exact-token:' || :organisation_id));
-- re-read the token row; if another process already refreshed it, use the new token
-- otherwise refresh, store the new access and refresh token, then commit
```

**Detect a dead connection and say so.** When refresh fails permanently — the customer revoked access, the user who connected left their firm — mark the connection as disconnected, stop syncing, and tell the customer's administrator in the product and by email. A connection that fails silently for three weeks produces three weeks of missing bookings.

**Connect with a role account where possible.** If the connection is tied to the personal Exact login of one employee, it breaks when they leave. Advise customers to connect with an account that belongs to the function rather than the person.

## Never Book the Same Invoice Twice

A request to create an invoice in the accounting package can time out after the package has already created it. Retry naively and the invoice exists twice. Bookkeepers notice duplicates quickly, and few things destroy trust in an integration faster.

Three measures prevent it.

**An outbox per organisation.** Instead of calling the API inside the user's action, write a sync job — "push invoice 2028-0142 to Exact" — to a table, and let a worker process it, as the background work article in this series describes. The user's action never waits on the accounting package.

**Store the remote ID.** When creation succeeds, store the ID the accounting package returned on your invoice record. A job for an invoice that already has a remote ID is not executed again.

**Check before creating on retry.** If a previous attempt timed out without a response, search the accounting package for an invoice with your reference — your invoice number in the reference field — before creating a new one. Both Exact and Moneybird let you store your own reference and filter on it.

```ts
const existing = await exact.findSalesEntry({ division, yourRef: invoice.number });
if (existing) return markSynced(invoice, existing.id);
const created = await exact.createSalesEntry(division, mapInvoice(invoice, mapping));
await markSynced(invoice, created.id);
```

## Matching Customers to Relations

Every booking refers to a relation — the debtor in the accounting package. Getting this wrong produces the second most common complaint after duplicate invoices: duplicate relations.

The naive approach creates a new relation in Exact for every customer in your product the first time an invoice is sent. In an administration that already contains that customer — entered by the bookkeeper years ago, with its own debtor number and payment history — the result is two debtors for one company, with invoices split between them and an outstanding balance nobody can read.

Match before creating. When a customer in your product is first synced, search the administration for an existing relation by the most reliable identifier available: the KvK number, then the VAT number, then an exact name and postcode match. If exactly one match is found, link it and store the relation ID. If several are found, or the match is uncertain, ask the customer's administrator to choose in the integration settings rather than guessing. Only create a new relation when nothing matches.

Once linked, store the remote relation ID on your customer record and use it for every subsequent booking. Decide which system owns address and contact details — usually the accounting package, because that is where the bookkeeper maintains them — and avoid writing changes in both directions, which produces an endless cycle of small overwrites.

The same principle applies to articles and products if you book invoice lines against items in the accounting package: match by article code, link, store the ID, and never create silently.

## Rate Limits and Volume

Accounting APIs limit how many calls you may make. Exact Online applies limits per minute and per day for each company connection; Moneybird applies its own. A month-end run that pushes four hundred invoices for one customer in a tight loop hits the limit, and generated code often treats the resulting error as permanent failure.

Respect the limits deliberately: process each organisation's queue at a controlled rate, read the rate limit headers the API returns, back off when told to, and spread bulk work over time. Batch where the API allows it. And cache what changes rarely — ledger accounts, VAT codes, journals — rather than fetching them before every booking.

## Show Sync Status to the Customer

The integration is only trusted if the bookkeeper can see what happened. Every invoice in your product should show its sync status: not yet sent, queued, booked in Exact with a link, or failed with a reason the customer can act on.

"Failed: VAT code 4 does not exist in administration 'Bakker Schoonmaak B.V.' — update the VAT mapping in Settings → Exact" is a message a customer fixes in two minutes. "Error 400" is a message that becomes a support ticket, then a phone call, then a reason to cancel.

Add a sync overview per organisation — the last successful sync, the number of pending and failed items, and a button to retry failed items once the cause is fixed — and an alert to you when an organisation's failures exceed a threshold.

## Reconcile Regularly

Even with all of the above, two systems drift: an invoice deleted in Exact by a bookkeeper, a booking edited by hand, a sync that failed and was never retried. The reconciliation article in this series describes the principle for payment providers; it applies equally here.

Once a week or once a month, compare: invoices in your product for the period, with their amounts, against bookings in the accounting package with your reference. List what is missing, what is duplicated and what differs in amount. Show the result to the customer's administrator, or at least to you. It turns silent drift into a short list someone can resolve.

## Build or Buy

Building directly against each accounting API gives you full control and no per-connection cost. It also means implementing OAuth, rate limiting, mapping and quirks separately for every package your customers use.

**Unified accounting APIs** — services that expose one API across many accounting packages, including European ones with good coverage of Dutch software such as Chift, alongside others like Codat and Apideck — handle connections, token refresh and many of the differences between packages. They charge per connection and become a subprocessor of the financial data passing through them, which belongs in your subprocessor list and processing agreements as the subprocessors article in this series describes.

The usual decision: build directly if nearly all customers use one package and that integration is central to your product; use a unified API if customers are spread across four or five packages, or if accounting integration is useful but not your core. Either way, keep your own outbox, mapping and sync status — those are your product's responsibility regardless of who handles the connection.

## Registration, Partners and Sandboxes

Exact Online requires apps to be registered in its App Center before they can connect, and listing your integration publicly involves a review. Moneybird has a developer programme and test administrations. Plan for this: registration takes time, and connecting real customer administrations during development is how test bookings end up in someone's ledger.

Develop and test against sandbox or test administrations. Keep production credentials and test credentials separate, as the environment variables article in this series describes, and never point a development environment at a customer's real administration.

## Setting This Up

For a Lovable product adding an accounting integration, this is typically four to six days for the first package: ownership decisions written down for numbering, customers, payment status and post-sync editing; a mapping screen per organisation that loads real ledger accounts, VAT codes, journals and divisions from the connected administration and validates choices; OAuth tokens encrypted at rest, refreshed before expiry and serialised per organisation to survive rotation; disconnection detected and communicated; an outbox with remote IDs and reference lookups to prevent duplicates; rate-limited processing with backoff and cached reference data; sync status per invoice with actionable errors and a per-organisation overview; scheduled reconciliation; invoices locked after booking; and development against sandbox administrations. A second package takes two to three days on the same foundation.

LaunchStudio builds and repairs accounting integrations for products whose customers live in Exact and Moneybird. Behind it is Manifera — eleven years, 160+ projects, 120+ engineers, from Herengracht 420 in Amsterdam.

[Tell us which accounting package your customers use](https://launchstudio.eu/en/#contact) and we will tell you what a dependable integration involves.

## Real example

### Three Hundred and Twelve Duplicate Invoices

Iris Meijer built Schoonmaakplanner in Lovable: scheduling, time registration and invoicing for commercial cleaning companies, used by 44 companies.

The Exact Online integration had been generated in an afternoon and demonstrated well. In production it had three problems. Roughly once a week, a customer's connection broke and had to be re-authorised, because the nightly sync and an invoice sent by a user occasionally refreshed the token at the same moment. When Exact responded slowly, the integration retried, and the invoice was created twice. And every booking used VAT code "2", which in most administrations meant 21% but in four customers' administrations — set up by different accountancy firms — meant something else.

The damage surfaced at the end of a quarter, when accountants for nine customers found 312 duplicate sales invoices and a set of misbooked VAT amounts in their VAT returns. Two customers said they would cancel unless it was fixed.

Four business days: token refresh serialised per organisation with an advisory lock, tokens encrypted at rest, and disconnections detected and reported to the customer's administrator; an outbox with the Exact ID stored on each invoice and a lookup by invoice number before every retry; a mapping screen that loads each administration's VAT codes, revenue ledger accounts and sales journal through the API, with validation before activation; rate-limited processing per organisation; sync status on every invoice with actionable error messages and a sync overview per customer; invoices locked after booking, with corrections issued as credit notes; a weekly reconciliation report listing missing, duplicated and differing bookings; and a scripted list of the 312 duplicates with their Exact IDs for the accountants to remove.

**Result:** the accountants removed the duplicates and corrected the VAT bookings within the quarter's filing window, and both customers who had threatened to cancel stayed. In the following six months there were no duplicate bookings and no token-related disconnections. Because the integration now sat behind a single connector interface, a Moneybird connector followed in three days, and six new customers in the next quarter named the accounting integration as a reason for choosing the product.

> *"It worked perfectly in the demo. Three months later nine accountants found three hundred and twelve invoices twice, and four administrations had our VAT on the wrong code."*
> — **Iris Meijer, Founder, Schoonmaakplanner (Den Bosch)**

**Cost & Timeline:** €4,600 (serialised token refresh and encrypted storage, outbox with idempotent bookings, per-administration mapping of VAT codes, ledger accounts and journals, rate-limited sync, visible sync status, post-booking locks, weekly reconciliation, duplicate cleanup list) — completed in 4 business days.

## Frequently Asked Questions

### Which accounting packages should a Dutch B2B product integrate with?

Start with the one most of your customers use — usually Exact Online or Moneybird — and design for a second. Twinfield, SnelStart, e-Boekhouden.nl and AFAS matter in particular segments.

### Why do Exact Online connections keep disconnecting?

Usually because refresh tokens rotate and two processes refresh at the same time, leaving an invalid token stored. Serialise token refreshes per organisation and re-read the token before refreshing.

### How do I avoid duplicate invoices in the accounting package?

Send bookings through an outbox, store the remote ID on each invoice, and before retrying a timed-out request search for an existing booking with your invoice number as reference.

### Can VAT codes be hard-coded?

No. VAT codes differ per administration. Load them from the connected administration and let each customer map your VAT rates to their codes, validated before the first sync.

### Should I use a unified accounting API?

If your customers use four or five different packages, or accounting integration is useful but not core, a unified API saves considerable work. Keep your own outbox, mapping and sync status either way.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Which accounting packages should a Dutch SaaS integrate with?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Start with the one most customers use — usually Exact Online or Moneybird — and design so a second package can be added."
      }
    },
    {
      "@type": "Question",
      "name": "Why do Exact Online integrations disconnect?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Rotating refresh tokens refreshed concurrently leave an invalid token stored; serialise refreshes per organisation."
      }
    },
    {
      "@type": "Question",
      "name": "How can duplicate invoices in accounting software be prevented?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Use an outbox, store the remote ID, and look up existing bookings by your invoice reference before retrying."
      }
    },
    {
      "@type": "Question",
      "name": "Can I hard-code VAT codes in an accounting integration?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No — VAT codes differ per administration; load them via the API and let each customer map your rates to their codes."
      }
    },
    {
      "@type": "Question",
      "name": "When should I use a unified accounting API?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "When customers are spread across several packages or the integration is not core — while keeping your own outbox, mapping and sync status."
      }
    }
  ]
}
</script>
