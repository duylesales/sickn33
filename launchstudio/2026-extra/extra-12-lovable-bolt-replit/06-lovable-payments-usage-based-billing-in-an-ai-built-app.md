---
Title: "Lovable Payments: Usage-Based Billing in an AI-Built App"
Keywords: lovable payments, usage-based billing, metered pricing, credits, AI cost pass-through, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: Technical Solo Founder / Indie Hacker
---

# Lovable Payments: Usage-Based Billing in an AI-Built App

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Lovable Payments: Usage-Based Billing in an AI-Built App",
  "description": "Metering, credits and pass-through pricing for products whose costs move with usage. What to count, when to count it, and how to bill it without surprising the customer or losing money on your own model calls.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-09-25",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/lovable-payments-usage-based-billing-in-an-ai-built-app" }
}
</script>

Flat pricing is a promise that every customer costs you roughly the same. For a scheduling tool or a CRM that promise mostly holds. For anything that calls a language model, processes documents, sends physical mail or stores video, it does not hold at all — and the customer who breaks it is never the one you expected.

The pattern is familiar to anyone who has shipped an AI feature on a €29 plan: 180 customers behave normally, four use it the way you hoped everyone would, and those four cost more than the other 180 pay. Nothing is wrong with the product. The pricing simply does not describe what the product does.

Usage-based billing fixes that, and it is genuinely more work than a monthly plan. The question is whether your economics require it, and if they do, how to build it without making your product feel like a taxi meter.

## Decide What You Are Counting

The unit is the whole design, and picking badly is expensive to undo because your customers will have learned it.

A good unit has three properties. The customer can predict it — they know roughly how many invoices they will send, or documents they will process, this month. It correlates with what the product costs you to run. And it correlates with the value they get.

Tokens fail the first test badly. No customer knows what a token is or how many their document contains, and pricing in them transfers your supplier's unit of account onto someone who never agreed to learn it. Count the thing the customer did: a document summarised, a report generated, a conversation held, a candidate screened. Absorb the variability inside that unit yourself — it is your job to know that the average document costs you nine cents.

Beware units that punish success in ways customers resent: per-user pricing on a tool meant to be shared across a team produces a customer actively avoiding your product's purpose, and they will tell you so at renewal.

## Credits Are Easier Than Metering, and Usually Better

There are two structures. Pure metering counts what was used and bills it afterwards. Credits are bought or granted in advance and consumed.

For small products credits are almost always the better choice. The customer knows what they spent before they spend it, which removes the anxiety that suppresses usage in metered products. You are paid in advance rather than chasing an invoice. And the accounting is simpler, because a credit purchase is an ordinary sale rather than a variable amount computed at period end.

The common and comfortable arrangement: a monthly plan that includes an allowance — 200 documents on the €49 tier — with the option to buy more when it runs out, and unused allowance expiring at period end while purchased credit top-ups do not. Customers understand it immediately because mobile plans have taught it to everyone.

Pure metering earns its complexity when usage varies by orders of magnitude between customers and you are selling to businesses who expect to be invoiced in arrears. That is a real market; it is just rarely a first-year one.

## Count on the Server, Once, Idempotently

The engineering has three requirements and AI-generated code typically satisfies none.

**Count where the cost occurs.** The counter increments on the server at the moment the expensive operation actually runs, not when the button is clicked. A browser-side counter is a suggestion, and a counter that increments before the work succeeds charges customers for your failures.

**Make it idempotent.** A retried request must not be counted twice. Give every billable operation an identifier that is recorded with the usage row, and refuse to record the same identifier twice. Without this, one timeout at the network level becomes a double charge and an email you cannot answer confidently.

**Record the detail, not just the total.** Every usage event as its own row: what, when, by whom, how much, and a reference to the work. Storing only a running total makes disputes unanswerable and makes any change to your pricing logic a migration you cannot verify. Rows are cheap; a customer asking why their usage doubled is not.

Check the balance in the same server-side entitlement function that handles plans, so that display and enforcement never diverge.

## Telling the Customer Before They Are Surprised

The failure mode of usage pricing is not technical. It is a bill nobody expected, followed by a chargeback and a public complaint.

Three things prevent almost all of it. A visible balance in the product, current rather than daily-batched, showing what has been used and what remains. Notifications at sensible thresholds — 80 percent, 100 percent, and again when overage begins — sent to the person who pays, who is often not the person consuming. And a hard stop that the customer chose, with automatic top-up as an opt-in rather than a default.

For business customers add one more: a monthly statement showing usage by user or project. It converts your invoice from a number they must trust into a document they can check, and it is frequently the reason a finance department approves renewal without a conversation.

## Do Not Let Your Supplier's Pricing Leak Through

If your costs come from a model provider, resist passing their pricing structure to your customer.

Their prices change, sometimes downward and sharply. Their units are not meaningful to your customer. And a product whose price list mirrors a supplier's invites the obvious question about what exactly the customer is paying you for.

Price your unit with enough margin to absorb supplier variation — a comfortable rule is that your revenue per unit should survive your costs doubling — and treat any efficiency you find as margin rather than immediately repricing. Customers value a stable price they can budget more than they value a price that tracks your costs.

## Migrating Customers Onto a New Model

Changing pricing on people who already pay you is the part founders dread, and it is mostly a communication problem with a small amount of code attached.

The code: existing customers need to be able to sit on their old arrangement while new ones arrive on the new one. That means plans are data, not conditionals scattered through your code — a table of plan definitions with allowances and prices, and accounts pointing at one. Retrofitting that is a day; living without it means every pricing change touches your application logic.

The communication: give notice, be specific, and show each customer their own numbers. "From 1 March the €89 plan includes 40 documents and additional bundles cost €35" is abstract. "Over the last three months you processed 11, 16 and 9 documents; your plan includes 40, so your bill will not change" is a message that ends the conversation. Send it individually, generated from their actual usage, and send it at least a month ahead.

For the handful whose bill will rise substantially, a phone call beats an email. Those are the customers with the most invested in your product and the most reason to feel ambushed, and a conversation that explains the economics honestly — this account costs more to serve than it pays — is one most business owners accept, because they run the same arithmetic themselves.

Grandfather generously and for a defined period. The goodwill is worth more than the revenue, and a public reputation for repricing people without warning is very expensive to repair.

## When the Meter Itself Needs Testing

A usage system is one of the few parts of a small product where a bug costs money in both directions, so it deserves a handful of deliberate checks before it goes anywhere near a customer.

Run the same billable operation twice with the same idempotency key and confirm one usage row exists. Force a failure part-way through the expensive work and confirm nothing was counted. Consume an allowance exactly to its limit and confirm the next request is refused rather than allowed by an off-by-one. Cross a period boundary mid-operation and confirm the usage lands in one period only. And reconcile a month of usage rows against your supplier's own invoice — if your counts and their charges disagree by more than rounding, find out why before scaling the customer base that makes the gap larger.

## Setting This Up

For a product that needs metered pricing this is typically four to six days: the billable unit chosen and defined precisely, a usage event table with idempotency keys, server-side counting at the point the work runs, balance checks inside the existing entitlement function, allowance and top-up mechanics with provider integration, thresholds and notifications to the billing contact, a visible balance and usage history in the product, hard stops with opt-in automatic top-up, and a monthly statement for business customers.

LaunchStudio builds usage billing as part of payment integration for products whose costs move with volume — increasingly common now that most new products call a model somewhere. The engineers are Manifera's, eleven years and 160+ delivered projects, with offices in Amsterdam, Singapore and Ho Chi Minh City.

[Tell us what one unit of your product costs you](https://launchstudio.eu/en/#contact) and we will tell you whether flat pricing survives it.

## Real example

### Four Customers on a Flat Plan

Reinier Slootweg built Dossierlezer with Lovable: a tool that reads tender documents and produces a structured summary for construction and engineering firms bidding on public work. Flat pricing, €89 per month, 96 customers.

The model calls were his largest variable cost and he had never measured them per customer. When his provider invoice passed his subscription revenue in month seven, he looked properly: 92 customers averaged 14 documents a month, and four averaged 610. One of those four had automated the upload of an entire archive.

Those four accounts cost him €2,780 that month and paid €356 between them. Raising the flat price would have punished the 92 to subsidise the four, and losing the four was not obviously right either — they were his most engaged users and two were reference customers.

Five business days: documents chosen as the billable unit rather than tokens or pages; a usage event table recording every processed document with an idempotency key, the account, the time, the page count and the cost incurred; counting moved server-side to the point of successful completion, so failed processing is no longer billed; the €89 plan redefined to include 40 documents per month with additional bundles of 25 at €35; balance checks folded into the existing entitlement function; notifications at 80 and 100 percent to the billing contact, with a hard stop by default and opt-in automatic top-up; a usage page in the product showing the current period and the last six; and a monthly per-project statement for the twelve accounts that requested one.

**Result:** the four heavy accounts moved to an average of €411 per month and all four stayed, with one saying the bundle price was cheaper than the internal process it replaced. Of the 92 ordinary customers, 71 never exceeded the included allowance and saw no change. Gross margin over the following quarter moved from negative to 68 percent, and Reinier now knows the cost of a customer before they become a problem.

> *"I was not losing money on the product. I was losing money on four accounts, and I could not see them because everything was one number."*
> — **Reinier Slootweg, Founder, Dossierlezer (Zoetermeer)**

**Cost & Timeline:** €3,750 (unit definition, usage event model with idempotency, server-side metering, allowance and top-up billing, thresholds and notifications, customer-facing usage history, per-project statements) — completed in 5 business days.

## Frequently Asked Questions

### Should I bill in tokens if my costs are in tokens?

No. Customers cannot predict tokens and should not have to learn your supplier's unit. Price the thing they did — a document, a report, a conversation — and absorb the variation inside it.

### Credits or metered billing in arrears?

Credits or an included allowance with top-ups, for almost any product under a few hundred customers. You are paid in advance, the customer knows their spend before spending it, and the accounting is far simpler.

### What stops a customer running up a bill they will not pay?

A hard stop at the limit by default, with automatic top-up as an opt-in. The alternative — unlimited overage with an invoice afterwards — produces exactly the dispute that usage pricing is blamed for.

### Where should usage be counted?

On the server, at the moment the expensive operation completes successfully, with an idempotency key so retries cannot double-count. Never in the browser, and never before the work has succeeded.

### Do I need to change pricing when my model provider gets cheaper?

Not automatically. Stable, predictable pricing is worth more to customers than one that tracks your costs, and the margin gives you room for the next price rise in the other direction.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Should I bill in tokens if my costs are in tokens?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No. Customers cannot predict tokens. Price the action they took — a document, a report, a conversation — and absorb supplier variation inside that unit."
      }
    },
    {
      "@type": "Question",
      "name": "Credits or metered billing in arrears?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Credits or an included allowance with top-ups for most small products: paid in advance, predictable for the customer, and far simpler to account for."
      }
    },
    {
      "@type": "Question",
      "name": "What stops a customer running up a bill they will not pay?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "A hard stop at the limit by default, with automatic top-up offered as an opt-in rather than applied silently."
      }
    },
    {
      "@type": "Question",
      "name": "Where should usage be counted?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Server-side, at successful completion of the billable work, with an idempotency key so a retry cannot count twice."
      }
    },
    {
      "@type": "Question",
      "name": "Should I reprice when my model provider gets cheaper?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Not automatically. Predictable pricing is worth more to customers than one tracking your costs, and the margin covers the next increase."
      }
    }
  ]
}
</script>
