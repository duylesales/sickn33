---
Title: "Plan Limits and What Happens When Someone Hits One"
Keywords: SaaS usage limits implementation, enforcing plan limits, soft limit vs hard limit, metered billing prototype, upgrade prompt design, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: AI-Native Founder (Non-Technical)
---

# Plan Limits and What Happens When Someone Hits One

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Plan Limits and What Happens When Someone Hits One",
  "description": "Choosing what to limit on a lower plan is a pricing decision; enforcing it correctly is an engineering one. A guide to hard versus soft limits, counting usage without breaking under load, and designing the moment a customer runs out of room.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-02-28",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/plan-limits-and-what-happens-when-someone-hits-one" }
}
</script>

"Up to 100 invoices per month" is one line on a pricing page and about four separate engineering decisions underneath it. What counts as an invoice — created, sent, or paid? What is a month — calendar, or since their billing date? What happens at invoice 101 — blocked, charged extra, or allowed with a note? And where is that number actually checked, given that a determined customer can call your API directly?

Founders reasonably treat plan limits as a pricing question, decide them in a spreadsheet, and hand the result to whatever built the product. The result, in most AI-generated prototypes, is a limit that exists as text on the pricing page and a `if (count > 100)` check somewhere in the frontend. That is not a limit. It is a suggestion, enforced only against customers who were never going to exceed it anyway.

## Decide What You Are Counting, Precisely

Ambiguity here produces disputes with customers, which are expensive out of all proportion to the revenue involved. Before implementation, write one sentence per limit that would satisfy an accountant.

Take "100 invoices per month." Does a draft count? Does an invoice that was created, deleted, and recreated count once or twice? If a customer sends the same invoice twice as a reminder, is that one or two? If they downgrade mid-month having already created 140, what happens to the existing 140 — do they disappear, become read-only, or stay untouched?

None of these have universally right answers, but all of them will be asked by a real customer within your first year. Deciding them in advance takes twenty minutes. Deciding them under pressure, with a customer's invoice on the line and a database you have to inspect manually to establish what actually happened, takes an afternoon and some goodwill.

The most common source of dispute is the reset boundary. A calendar-month reset is simpler to explain and to compute; a rolling window from the customer's billing date is fairer but requires that you can accurately count usage in an arbitrary date range, which in turn requires that every countable action carries a reliable timestamp. Prototypes routinely fail this second requirement, because rows are stored without a trustworthy created-at value, or with one set by the browser rather than the server.

## Hard Limits, Soft Limits, and Overage

There are three sane behaviours at the boundary, and the right one depends on what breaks for the customer.

**A hard limit** blocks the action outright. Appropriate where exceeding it costs you real money per unit — AI model calls, SMS messages, video minutes, storage — because there the alternative is a customer with an unlimited ability to spend your money.

**A soft limit** allows the action and prompts an upgrade. Appropriate where the cost to you is negligible and the harm of blocking is high. Blocking someone from creating their 101st contact record to enforce a rule that costs you nothing damages the relationship more than the upgrade is worth.

**Overage** allows the action and charges for it. This is genuinely useful, and considerably more work than it looks: it requires accurate per-unit metering, a way to show the customer what they are accruing *before* the invoice arrives, and a spending cap so nobody receives a bill they did not expect. If you cannot yet show live usage in-product, you are not ready to bill for overage, because the first surprise invoice will cost you the customer.

A pragmatic default for a first launch: hard limits only where your own costs scale, soft limits everywhere else, and overage deferred until you have both metering and a live usage display you trust.

## Where the Check Has to Live

This is the part that separates a real limit from a decorative one, and it is where AI-generated products almost universally get it wrong.

If the only check is in the interface — a disabled button, a hidden "new project" option — then the limit binds nobody who opens the browser's network tab, and more importantly it binds nobody using your product in an unusual but legitimate way: a slow connection retrying a request, two tabs open at once, a bulk import running while a form is submitted. The enforcement must sit on the server, in the code path that actually creates the record, ideally backed by a database-level constraint.

Concurrency is the subtler failure. The naive implementation reads the current count, compares it to the limit, and then inserts. Two requests arriving in the same instant both read 99, both conclude there is room, and both insert — and the customer now has 101 records on a plan that permits 100. Under normal use this is rare enough to look like it works. Under a bulk import, or from a customer who has automated their workflow against your API, it happens constantly. The correct implementations — a transaction, a unique constraint, or an atomic counter — are standard practice, but they require someone to have thought about the case at all, which a code generator working from "limit users to 100 invoices" generally has not.

There is a matching performance problem. Counting rows on every single write is fine at a hundred records and slow at a hundred thousand, and the point at which it becomes slow arrives without warning, usually for your largest and most valuable customer first. A maintained counter or a periodically refreshed usage figure avoids this, at the cost of one more thing to keep correct.

Getting enforcement, concurrency, and counting right is precisely the kind of unglamorous work that determines whether your pricing model actually holds once real customers use it. LaunchStudio, backed by Manifera's 11+ years of production engineering, implements and tests these paths — including the concurrent and bulk-import cases — as part of preparing an AI-built product for launch. [Describe your project](https://launchstudio.eu/en/#contact) and we will review your limit logic within one business day.

## The Moment Itself Is a Conversion Opportunity, Not an Error

When a customer reaches a limit, they have just demonstrated more product usage than almost anyone else. This is the best-qualified upgrade moment you will ever get, and most products squander it with a red error box.

Three things make the difference. **Warn before, not only at.** A notice at 80% — in the product, and by email for account owners — turns a wall into a planned decision, and gives the person who has to ask their manager for budget time to do it. **Name the number.** "You have used 96 of your 100 invoices this month" is actionable; "limit reached" is an obstruction. **Offer the exact next step, with the price.** The upgrade action should be one click from the message, and should show what the plan change costs, prorated from today rather than presented as a new full charge.

Equally important is what should *not* happen: the customer must never lose work. If someone fills in a long form and the limit is only discovered on submission, they have to keep what they typed. The graceful pattern is to detect the condition before they start, or to hold the submitted content and complete it automatically once they upgrade.

## The Downgrade Path Nobody Builds

Every limit implies a question that prototypes almost never answer: what happens to existing data when someone drops to a plan that no longer permits it?

A customer on a 10-user plan downgrades to a 3-user plan while having 8 users. Deleting five people's accounts automatically is unacceptable. Ignoring the limit entirely means the plan means nothing. The workable answer is usually to require the customer to choose — "select which 3 users keep access" — before the downgrade completes, or to keep the excess in a read-only state until they resolve it.

Whichever you choose, decide it before launch and make sure the customer is told during the downgrade, not after. The alternative is the single worst support conversation in subscription software: a customer who saved €40 a month and lost their team's access without ever being asked.

## Real example

### The Limit That Held Until the First Bulk Import

Anouk Verstraeten launched Factuurly, an invoicing tool for freelance collectives, built in Lovable with three tiers separated by monthly invoice volume. It worked exactly as designed for four months.

Then a customer migrating from another system imported 340 invoices in one afternoon on a 100-per-month plan. The limit check read the count, compared, and inserted — once per invoice, with dozens of requests in flight simultaneously. Every check saw a stale count and passed. The account finished with 340 invoices on a plan permitting 100, and a review found four other accounts sitting between 104 and 190 through ordinary two-tab usage.

Worse, the counting query had begun to slow visibly for the three largest accounts, because it counted every invoice ever created rather than the current period, on a table without an index supporting that filter.

**Result:** enforcement moved to the database with an atomic counter per billing period, a proper index added, an 80% warning email introduced, and the five over-limit accounts contacted with a prorated upgrade offer rather than retroactive enforcement — three of the five upgraded. Invoice creation also became measurably faster for the largest accounts.

> "My pricing page had been describing something my product did not actually do. It only became visible when someone used it seriously."
> — **Anouk Verstraeten, Founder, Factuurly**

**Cost & Timeline:** usage-limit enforcement and metering rebuilt in 3 business days.

## Frequently Asked Questions

### Should limits block the action or just prompt an upgrade?

Block where exceeding the limit costs you real money per unit, such as AI calls, SMS, or storage. Prompt where the marginal cost is negligible, since blocking a zero-cost action damages the relationship more than the upgrade is worth.

### Is a limit checked in the interface good enough for launch?

No. Interface checks are cosmetic and are bypassed both deliberately and accidentally, through API use, retries, or two open tabs. Enforcement belongs in the server code path that creates the record, ideally with a database-level constraint.

### How should usage reset — calendar month or billing period?

Calendar month is easier to explain and compute; a rolling billing period is fairer. Either works, provided every countable action carries a reliable server-side timestamp so usage in an arbitrary window can be counted accurately.

### When is overage billing worth building?

Once you can meter accurately and show live usage in-product, and once you have a spending cap. Without those, the first unexpected invoice tends to cost more in lost trust than the overage earns.

### What should happen if a customer downgrades below their current usage?

Ask them to resolve it as part of the downgrade — choosing which users or records to keep — or place the excess in a read-only state. Never remove data automatically to fit the smaller plan.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "Should limits block the action or just prompt an upgrade?", "acceptedAnswer": { "@type": "Answer", "text": "Block where exceeding the limit costs real money per unit, such as AI calls, SMS, or storage. Prompt where the marginal cost is negligible, since blocking a zero-cost action damages the relationship more than the upgrade is worth." } },
    { "@type": "Question", "name": "Is a limit checked in the interface good enough for launch?", "acceptedAnswer": { "@type": "Answer", "text": "No. Interface checks are cosmetic and get bypassed deliberately and accidentally through API use, retries, or two open tabs. Enforcement belongs in the server code path that creates the record." } },
    { "@type": "Question", "name": "How should usage reset, calendar month or billing period?", "acceptedAnswer": { "@type": "Answer", "text": "Calendar month is easier to explain and compute; a rolling billing period is fairer. Either works provided every countable action carries a reliable server-side timestamp." } },
    { "@type": "Question", "name": "When is overage billing worth building?", "acceptedAnswer": { "@type": "Answer", "text": "Once you can meter accurately, show live usage in-product, and enforce a spending cap. Without those, a surprise invoice usually costs more trust than the overage earns." } },
    { "@type": "Question", "name": "What should happen if a customer downgrades below their current usage?", "acceptedAnswer": { "@type": "Answer", "text": "Ask them to resolve it during the downgrade, such as choosing which users to keep, or hold the excess in a read-only state. Never remove data automatically to fit the smaller plan." } }
  ]
}
</script>
