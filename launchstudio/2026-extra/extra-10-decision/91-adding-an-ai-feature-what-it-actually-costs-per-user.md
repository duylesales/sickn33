---
Title: "Adding an AI Feature: What It Actually Costs Per User"
Keywords: AI feature cost per user, token cost estimation saas, LLM pricing margin, context window cost, caching AI responses, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: AI-Native Founder (Non-Technical)
---

# Adding an AI Feature: What It Actually Costs Per User

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Adding an AI Feature: What It Actually Costs Per User",
  "description": "An AI feature is the first part of most products with a real marginal cost per use, which changes the arithmetic of a flat subscription. How to estimate it before building, where the cost actually accumulates, and the controls that keep it bounded.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-05-15",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/adding-an-ai-feature-what-it-actually-costs-per-user" }
}
</script>

Most software has essentially no marginal cost: the thousandth customer costs almost the same to serve as the hundredth. An AI feature breaks that. Every use spends money at a provider, the amount depends on how much text goes in and comes out, and a heavy user can consume more than they pay you — which is a genuinely unfamiliar situation for anyone whose pricing intuition was formed on ordinary SaaS.

The good news is that the arithmetic is knowable in advance, and doing it takes an hour. The common failure is not that AI features are unaffordable; it is that nobody calculated before building, and the number is discovered from an invoice.

## Estimate Before You Build

Three inputs give you a usable figure.

**How much goes in and out per use.** Providers charge for input and output separately, usually with output several times more expensive. A rough conversion: a page of text is on the order of 500 to 800 tokens. Add up your instructions, whatever customer data you include, any conversation history, and the expected response.

**How often a customer uses it per month.** Estimate high. Founders consistently underestimate, and the customers who use a feature at ten times your assumption are the ones who determine whether the economics work.

**The provider's price per million tokens**, which varies by an order of magnitude between the small fast models and the large capable ones.

Multiply, and compare to your subscription price. If a summarisation feature costs €0.004 per use and a customer uses it 200 times a month, that is €0.80 against a €29 plan — comfortable. If each use involves a large document and costs €0.09, the same customer costs €18, and your margin has effectively gone.

Then do the calculation again for the heaviest plausible customer rather than the average one. Averages hide the case that hurts, and with a flat subscription a small number of heavy users determine the outcome.

## Where the Cost Actually Accumulates

Four patterns account for most unexpected spend, and all are avoidable.

**Sending too much context.** The most common by far. Including an entire document, a full conversation history, or a large data extract in every request multiplies input cost with no corresponding improvement in the answer. Sending the relevant portion is usually both cheaper and better.

**Growing conversation history.** In a chat-style feature the naive implementation resends the whole conversation on each turn, so the twentieth message costs many times the first. Summarising older turns, or keeping a window, bounds it.

**Using an expensive model for simple work.** Classification, extraction, and short rewrites are handled well by smaller models at a fraction of the price. Reserving the largest model for the tasks that genuinely need it often cuts cost by most of it without a noticeable quality change.

**Retries and duplicate requests.** A failed call retried three times costs four times. A user double-clicking a Generate button pays twice. Both are ordinary engineering problems with ordinary solutions, and both are absent from generated implementations.

Two reductions are worth building in from the start. **Cache identical requests**: if two customers ask the same thing of the same document, the second can be free. **Use the provider's prompt caching** where a large fixed portion of your input repeats across calls, which most major providers now support at a substantial discount.

## Pricing a Feature That Costs You Money

Once the cost is known, the pricing decision has four shapes, each appropriate in different circumstances.

**Include it with limits.** Simplest and best for most products: the feature is part of the plan, with a stated monthly allowance. Predictable for the customer, bounded for you.

**Charge per use.** Honest and it aligns cost with revenue, and it makes customers hesitate before each use, which for a feature you want adopted is a real drawback.

**A credit system.** Customers buy credits consumed by AI actions. Flexible, and it introduces an entire billing mechanism — balances, expiry, top-ups — that must be built and accounted for properly.

**Higher tier only.** Effective if AI is a differentiator rather than a core function, and it keeps the cost concentrated among customers paying more.

Whichever you choose, the limit must be enforced in your code rather than described on a pricing page, and the customer should be able to see their remaining allowance before they hit it. A feature that stops working with no warning, on a plan that advertised it, generates more support than the feature was worth.

Getting the estimation, limits, caching, and enforcement right before an AI feature reaches customers is a small piece of production work with a direct financial return. LaunchStudio, backed by Manifera's 11+ years of production engineering, builds AI features with cost controls that hold under real use. [Describe your project](https://launchstudio.eu/en/#contact) for a review within one business day.

## Controls That Cap the Worst Case

Estimation tells you what to expect. Controls determine what happens when reality disagrees.

**A per-account monthly limit**, enforced before the call is made, so one customer cannot consume the budget.

**A global daily cap**, so total spend has a ceiling regardless of where usage comes from — this is the control that turns a weekend incident into a nuisance.

**Authentication before any metered call.** An AI feature reachable without an account will be found and used at your expense, usually within days.

**Alerts on daily spend rate**, not monthly totals, since a monthly threshold is crossed after the damage is done.

**A kill switch**, so the feature can be disabled without a deployment when a provider misbehaves or costs run away.

Together these are perhaps a day of work, and they convert an open-ended liability into a bounded cost. The alternative — relying on the provider's own budget alerts — notifies you after spending has occurred, which is a report rather than a control.

## Real example

### €0.02 Per Summary, and €1,240 in a Month

Lena Fischer ran Vergaderpunt, a meeting-notes tool for consultancies, built in Bolt. It summarised uploaded transcripts using a large model, included in a €39 monthly plan.

Her estimate had been €0.02 per summary based on a test transcript of about two pages, with an assumption of 30 summaries per customer per month — roughly €0.60 per customer. The first full month with 40 customers produced a model bill of €1,240, against €1,560 in subscription revenue.

Three causes. Real transcripts were 20 to 60 pages rather than two, so input cost was roughly fifteen times the estimate. The feature resent the full transcript with every follow-up question, so a customer asking three questions paid four times. And six customers were using it far more than assumed, one producing 340 summaries in the month.

**Result:** transcripts chunked with only relevant sections sent per question, a smaller model used for the initial extraction with the large model reserved for the final summary, prompt caching applied to the fixed instructions, identical requests cached, and a plan allowance of 100 summaries a month with visible usage and paid top-ups. Cost per customer fell to about €1.90 and the heaviest user moved to a higher tier.

> "My estimate was right for the document I tested with. Every real customer uploaded something twenty times bigger, and I found out from an invoice."
> — **Lena Fischer, Founder, Vergaderpunt**

**Cost & Timeline:** AI cost optimisation and usage limits delivered in 3 business days.

## Frequently Asked Questions

### How do I estimate an AI feature's cost before building it?

Multiply the expected input and output size per use by the provider's per-token prices, then by realistic monthly usage. Run the calculation for the heaviest plausible customer as well as the average, since a flat subscription is decided by the heavy users.

### Where does unexpected AI cost usually come from?

Sending far more context than necessary, resending growing conversation history, using an expensive model for simple tasks, and retries or duplicate requests that pay for the same work repeatedly.

### Should an AI feature be included in the plan or charged separately?

Including it with a stated monthly allowance suits most products: predictable for the customer, bounded for you. Per-use charging aligns cost with revenue but discourages the adoption you want.

### What stops a single customer from consuming my whole budget?

Per-account limits enforced in your own code before the call is made, plus a global daily cap. Provider budget alerts report spending after it has happened and are not a control.

### Can AI costs be reduced without lowering quality?

Usually substantially: send only relevant context, use smaller models for extraction and classification, apply prompt caching for repeated instructions, and cache identical requests.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "How do I estimate an AI feature's cost before building it?", "acceptedAnswer": { "@type": "Answer", "text": "Multiply expected input and output size per use by the provider's per-token prices and by realistic monthly usage, running the calculation for the heaviest plausible customer as well as the average." } },
    { "@type": "Question", "name": "Where does unexpected AI cost usually come from?", "acceptedAnswer": { "@type": "Answer", "text": "Sending more context than necessary, resending growing conversation history, using an expensive model for simple tasks, and retries or duplicate requests." } },
    { "@type": "Question", "name": "Should an AI feature be included in the plan or charged separately?", "acceptedAnswer": { "@type": "Answer", "text": "Including it with a stated monthly allowance suits most products, being predictable for customers and bounded for you. Per-use charging aligns cost but discourages adoption." } },
    { "@type": "Question", "name": "What stops a single customer from consuming my whole budget?", "acceptedAnswer": { "@type": "Answer", "text": "Per-account limits enforced in your code before the call, plus a global daily cap. Provider budget alerts report spending after the fact." } },
    { "@type": "Question", "name": "Can AI costs be reduced without lowering quality?", "acceptedAnswer": { "@type": "Answer", "text": "Usually substantially: send only relevant context, use smaller models for extraction and classification, apply prompt caching, and cache identical requests." } }
  ]
}
</script>
