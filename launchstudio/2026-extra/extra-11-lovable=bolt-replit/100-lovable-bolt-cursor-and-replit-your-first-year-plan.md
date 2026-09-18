---
Title: "Lovable, Bolt, Cursor and Replit: Your First Year Plan"
Keywords: Lovable, Bolt, Cursor, Replit, ai app security, lovable hosting, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: AI-Native Founder (non-technical)
---

# Lovable, Bolt, Cursor and Replit: Your First Year Plan

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Lovable, Bolt, Cursor and Replit: Your First Year Plan",
  "description": "A year of an AI-built product, in the order the work actually arrives: prototype, first customer, first business contract, first integration, first spike. What to do at each point and what to defer.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-09-10",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/lovable-bolt-cursor-and-replit-your-first-year-plan" }
}
</script>

Most advice about building products this way is a list of everything that could be wrong, delivered all at once. It is accurate and it is useless, because you cannot do forty things and you should not try.

What follows is the same material arranged by when it actually matters. The organising idea is simple: work becomes urgent at specific thresholds, and those thresholds are events in your business rather than dates in a calendar. Before the threshold, doing the work is premature. After it, not doing the work is the reason something goes wrong.

Five thresholds, in the order they arrive.

## Stage One: Nothing Exists Yet

**What you are doing:** finding out whether anyone wants this.

Use the generative tools — Lovable, Bolt — and use them freely. Build the thing, show it to ten people who have the problem, and listen. Iterate as fast as the tooling allows.

**Do not:** buy a domain and set up hosting and configure analytics before you have shown anybody anything. Do not build multi-tenancy for customers you do not have. Do not worry about the database.

**Two exceptions, because they cost nothing now and a fortnight later.** Register the domain in your own company's name from the start, if you register one at all. And if there is any realistic chance your customers will be companies rather than individuals, build the organisation-and-membership model rather than attaching everything to a user — this is the single most expensive thing to retrofit.

**Spend:** platform subscriptions, and less than you think. Most ideas should die here, cheaply.

## Stage Two: The First Paying Customer

The threshold that changes everything, because now somebody else's money and data are involved.

**Do this, in this order, and it is roughly a week:**

Access rules, written and verified by attempting to break them from a second account. This is the single most common serious flaw in AI-built products and the one with the worst consequences.

Secrets moved server-side, with any key that reached the browser rotated. Then spending caps at every metered provider.

Data made durable: an external managed database in an EU region, uploads in object storage rather than beside your code, and backups verified by actually restoring one and timing it.

A custom domain with HTTPS, and the deployed address — never a preview link — given to customers.

Error tracking and uptime monitoring, which is twenty minutes and will immediately show you something broken you did not know about.

If you take payments: webhook signatures verified, events deduplicated, amounts determined by your server.

**Do not yet:** build an API, worry about launch-scale traffic, or write a security policy.

## Stage Three: The First Business Contract

A Dutch company with a procurement process wants to buy, and the questions arrive.

**What becomes urgent:** tenant isolation enforced in the database rather than in application code, and tested. An audit trail on anything holding money, permissions or personal data. Two-factor authentication at least for administrators. A subprocessor list, which you have never written and which will surprise you. Retention and erasure implemented rather than described. And a four-to-six page security document answering the questions before they are asked.

**What this buys you:** the ability to answer a questionnaire in two days instead of three weeks, which is frequently the difference between winning and losing the contract. Founders consistently underestimate how much of enterprise sales is simply responding competently.

**Be honest about gaps.** A stated gap with a date is accepted; a vague answer is not.

## Stage Four: More Than One Person

A colleague, a freelancer, or a customer whose staff need separate logins.

**What becomes urgent:** version control as the source of truth with small reviewable commits; a staging environment with its own anonymised data; a rollback you have actually performed and timed; separate accounts for every person with same-day removal when they leave; and logic moved out of generated screens so two people — or two tools — stop overwriting each other.

This is also where the tooling mix settles: generative tools for surfaces, editorial tools like Cursor for anything structural, and a rule that a screen graduates to real code the moment somebody depends on what it calculates.

## Stage Five: Scale, in Whatever Form It Arrives

A launch, a seasonal peak, a customer ten times larger than the others, or simply three years of accumulated data.

**What becomes urgent:** connection pooling, and knowing your actual ceiling from a load test rather than an assumption. Indexes on what you filter by, including the columns your access policies filter on. Dashboard aggregates pre-computed rather than scanned on every page view. Exports moved to background jobs. Static pages served statically. Feature flags so an expensive feature can be switched off under load.

**And the unglamorous one:** a maintenance arrangement, because a year of a live product contains thirty to sixty dependency updates, a platform deprecation, a certificate event, an integration that stops, and at least one silent failure.

## What Stays True at Every Stage

**Review what changed, not just whether it works.** Dependencies added, configuration touched, anything near access rules or credentials.

**State constraints when you prompt.** "This table is owner-only. This runs on the server. Do not add dependencies without telling me." Given up front, they are honoured; applied afterwards, they are corrections.

**Keep every account in your own name.** Domain, database, payments, email, repository. It is what makes every other decision reversible.

**Never send a preview link to a customer.**

**And keep building.** None of this argues for slowing down. It argues for a small number of things being true at the point where being wrong stops being free.

## The Eight Findings That Repeat Everywhere

Across projects built with every one of these tools, the same problems appear. Knowing the list is useful in itself, because you can check your own product against it this afternoon.

**Access rules absent or permissive.** Any signed-in user able to read other customers' records, usually because a policy was written to make an empty list stop being empty.

**A privileged key in the frontend.** The service key, the payment secret, or a metered API key present in files any visitor downloads.

**Data written beside the application.** Uploads and generated files in the project directory, disappearing at the next rebuild, with the database row still pointing at them.

**Backups that exist and have never been restored.** An untested backup is a belief about a file.

**A webhook with no signature verification.** Anyone who finds the address can tell your product that they paid.

**No logging and no error tracking.** So nothing can be reconstructed afterwards, and failures are reported by customers or not at all.

**Records owned by users rather than organisations.** Which works until a customer's colleague needs access, and then becomes shared logins.

**An aggregate with no tenant filter.** A dashboard number, a total, an export — counting the whole table, which is how cross-customer leaks happen in products whose main lists are correctly filtered.

None of these are failures of the tools, and none require unusual skill to fix. They are all the same category of thing: consequences of a request that was about making a feature work, answered by a system with no reason to consider anything else.

Check the eight. Whatever the answer, you will know something about your product that you did not know this morning, and the ones that come back clean are as informative as the ones that do not.

## What Each Stage Costs

For realistic planning: stage two — the week of production readiness — is typically €1,500 to €3,000. Stage three, the enterprise-readiness work, €3,000 to €6,000 depending on how much tenancy and audit work is needed. Stage four and five are usually smaller, €1,500 to €4,000 each, because the foundation exists by then.

LaunchStudio prices these as fixed scopes in bands from €800 to €7,500 — roughly 20% of what a traditional agency charges for comparable work — with managed hosting at €49 per month for the parts that never finish. Every account stays in your name, the codebase stays conventional, and you keep building with your own tooling afterwards.

Behind it is Manifera: eleven years, 160+ production projects, 120+ engineers, clients including Vodafone, TNO, CFLW, Statler BI and Xpar Vision, working from Amsterdam Herengracht 420, Singapore and Ho Chi Minh City.

[Tell us which stage you are at](https://launchstudio.eu/en/#contact) and you will get a specific list of what matters now and what can wait, usually within one business day. Or look at how the [packages](https://launchstudio.eu/en/#packages) map onto these stages.

## Real example

### A Year, in the Order It Actually Happened

Lianne de Ruiter built Bezoekregistratie with Lovable: visitor registration for offices and factories — sign-in at reception, host notification, evacuation lists, contractor checks.

**February.** Prototype in nine days, shown to four facility managers she knew. Two said they would pay. Cost: a platform subscription.

**April, first paying customer.** A logistics company in Veenendaal, €180 per month. This triggered the production readiness week: access rules written and tested from a second account, which found that any signed-in user could read every visitor record; a service key removed from the frontend; the database moved to an EU region with backups restored and timed; visitor photographs moved out of the project directory into object storage, which turned out to matter because four months of them had already been lost to redeploys; a custom domain; error tracking, which surfaced a host-notification failure affecting one browser. €2,400, six days.

**July, first business contract.** A manufacturer with a procurement process and 41 questions. Tenant isolation moved into database policies, an audit trail added to visitor records — which the manufacturer's safety officer cited as the deciding feature, because evacuation lists must be defensible — two-factor authentication, a subprocessor list that surfaced an analytics tool she had forgotten, retention and erasure, and a five-page security document. €4,900, eleven days. Contract signed six weeks later at €1,100 per month.

**October, a colleague joined.** Version control, staging with anonymised data, a tested rollback, separate accounts, and the notification logic moved out of a generated screen after it was overwritten by a layout change. €1,800, four days.

**January, scale.** The manufacturer opened two further sites and a contractor audit produced 900 sign-ins in a morning. Connection pooling, indexes including the policy columns, the daily dashboard pre-computed, exports moved to background jobs. €2,100, five days. Then managed hosting at €49 per month.

**Result:** eleven customers by the anniversary, €4,300 monthly recurring revenue, and total engineering spend of €11,200 across the year.

> *"Every piece of work I paid for became urgent about a week before I did it. The only one I regret is the four months of visitor photographs I lost before anyone told me files do not survive a redeploy."*
> — **Lianne de Ruiter, Founder, Bezoekregistratie (Veenendaal)**

**Cost & Timeline:** €11,200 across four engagements over twelve months, plus €49 per month managed hosting from month eleven.

## Frequently Asked Questions

### When should I stop building and make the product production-ready?

At the first paying customer. Before that, most of this work is premature; after that, somebody else's money and data are involved, and the access rules in particular are the flaw with the worst consequences.

### What is the one thing to get right before I have customers?

If your customers might be companies rather than individuals, build the organisation-and-membership model from the start. It is the most expensive thing to retrofit, and the request for colleague access arrives within months.

### What do I need before a business contract?

Tenant isolation enforced in the database, an audit trail, two-factor authentication for administrators, a subprocessor list, retention and erasure, and a short security document. Together they turn a three-week questionnaire ordeal into a two-day reply.

### What changes when a second person joins?

Version control as the source of truth, a staging environment with anonymised data, a tested rollback, separate accounts with same-day removal, and business logic moved out of generated screens so two people or two tools stop overwriting each other.

### What does a year of this cost?

Typically €1,500–€3,000 for production readiness, €3,000–€6,000 for enterprise readiness, and €1,500–€4,000 each for the team and scale stages — with managed hosting at €49 per month. Roughly 20% of a traditional agency's price for comparable work.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "When should I stop building and make the product production-ready?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "At the first paying customer — before that most of the work is premature, and after it someone else's money and data are involved."
      }
    },
    {
      "@type": "Question",
      "name": "What is the one thing to get right before I have customers?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "The organisation-and-membership model, if your customers might be companies. It is the most expensive thing to retrofit."
      }
    },
    {
      "@type": "Question",
      "name": "What do I need before a business contract?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Database-enforced tenant isolation, an audit trail, two-factor authentication, a subprocessor list, retention and erasure, and a short security document."
      }
    },
    {
      "@type": "Question",
      "name": "What changes when a second person joins?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Version control as the source of truth, staging with anonymised data, a tested rollback, separate accounts, and logic moved out of generated screens."
      }
    },
    {
      "@type": "Question",
      "name": "What does a year of this cost?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Roughly €1,500–€3,000 for production readiness, €3,000–€6,000 for enterprise readiness, and €1,500–€4,000 per later stage, plus €49 per month hosting."
      }
    }
  ]
}
</script>
