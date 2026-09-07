---
Title: "Referral Flows and the Abuse You Should Expect"
Keywords: SaaS referral program implementation, referral fraud prevention, self referral abuse, credit and reward accounting, viral loop engineering, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: Technical Solo Founder / Indie Hacker
---

# Referral Flows and the Abuse You Should Expect

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Referral Flows and the Abuse You Should Expect",
  "description": "A referral programme is a feature that pays out money, which makes it the one part of your product strangers have a direct financial incentive to attack. What to decide before launching one, the abuse patterns that appear within days, and the accounting that keeps rewards from becoming a liability.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-03-12",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/referral-flows-and-the-abuse-you-should-expect" }
}
</script>

Most features fail quietly when they are wrong. A referral programme fails expensively, because it is the one part of your product that hands out money, and the internet contains a reliable population of people who will find that out faster than your first genuine referrer does. Within days of launching one, someone will create accounts with plus-addressed emails to refer themselves, and if the reward is a credit against a real invoice, that is your money.

None of this is an argument against referrals. They work, particularly for products with an obvious "you should try this" moment. It is an argument for treating the feature as what it actually is — a small payments system with an incentive attached — rather than as a marketing widget that can be bolted on in an afternoon.

## Decide What Triggers a Reward, and Make It Late

The single most consequential decision is the qualifying event, and the instinct to reward early is where most programmes go wrong.

**Reward on signup** is the worst option available. It costs you something for an account that may never be used, and it is trivially farmed. Anyone can create signups.

**Reward on activation** — the referred customer completes a meaningful action — is defensible for products where activation genuinely takes effort, and harder to fake than a signup.

**Reward on first payment** is the safest default. Money changing hands is expensive to fake, aligns your cost with actual revenue, and makes the programme self-funding by construction.

**Reward after a retention period** — first payment plus 30 days, so refunds and immediate cancellations do not leave you paying for churned revenue — is stronger still, at the cost of a delay that reduces enthusiasm.

Whatever you choose, the qualifying event has to be something your product records reliably and can evaluate later, not a moment you happen to notice. And the rule needs a stated position on the awkward case that will certainly arise: the referred customer pays, then charges back or refunds within a week. If the reward has already been paid, you have lost twice.

## The Abuse Patterns That Show Up First

These are not exotic. Each appears in ordinary consumer products within the first weeks.

**Self-referral through email tricks.** Gmail treats `name+anything@gmail.com` as the same inbox, and many domains ignore dots. One person can generate an unlimited supply of apparently distinct addresses. Normalising addresses before comparing them removes the easiest version of this.

**Circular referrals.** Two people refer each other, both collect. Detecting this is straightforward — a referral where the referred party has already referred the referrer — and worth checking explicitly.

**Referral hijacking.** Someone appends their own referral code to your homepage URL and posts it where people already intending to sign up will see it, collecting rewards for customers you were getting anyway. This is not fraud exactly, but it is a real cost with no new revenue behind it.

**Cookie stuffing and last-touch capture.** If your attribution takes the most recent referral code seen, a scraper can overwrite genuine referrals wholesale. First-touch attribution, recorded at signup, is more resistant.

**Disposable email services.** Endless valid-looking addresses that receive mail once. Blocking known disposable domains handles the low-effort cases.

You cannot eliminate abuse, and trying to will produce false accusations against real customers. The realistic aim is to make the cheap attacks unprofitable and to *see* the rest, which means recording every referral with enough context — timestamps, addresses, and the signals you would want later — to review a suspicious cluster after the fact.

## Rewards Are Accounting, Not a Number in a Column

The implementation shortcut is a `credit_balance` field that goes up when someone qualifies and down when it is used. It works for a month and then produces disputes you cannot resolve, because a single number carries no history and no explanation.

The alternative is not complicated: record every change as a separate entry — what happened, when, how much, why, and what it relates to — and derive the balance by summing them. Now "why do I have €30" has an answer, a reversal is a new entry rather than a silent edit, and your own accounting has a trail.

Three further decisions belong in that design. **What form does the reward take?** A credit against future invoices is much simpler than cash, avoids money-transmission questions entirely, and is what most B2B products should use. **Does it expire?** A stated expiry keeps an unbounded liability from accumulating, and must be communicated at the time it is earned. **What happens on cancellation?** Unused credit on a cancelled account should generally lapse, and saying so up front prevents an argument later.

Getting this wrong has a specific consequence founders underestimate: rewards owed are a liability on your books, and an unlimited, non-expiring, undocumented one is exactly the kind of thing that surfaces awkwardly in an investor's due diligence or an accountant's year-end review.

There is also a tax dimension worth a conversation with your accountant rather than a blog post — credits against invoices and cash payouts are treated differently, and the answer varies by jurisdiction.

## Concurrency, Idempotency, and Paying Twice

Referral logic is unusually exposed to double-processing, because the qualifying event often arrives as a webhook from your payment provider — and webhooks are retried by design.

If your handler credits the referrer each time it receives a payment notification, a provider retry after a timeout credits twice for one payment. The fix is standard practice: record which provider event ids have been processed and ignore repeats. It is a small amount of code that almost no generated implementation includes, because a code generator asked for "credit the referrer when payment succeeds" writes exactly that and nothing about the second delivery of the same message.

The same concern applies to reward redemption. Two simultaneous requests spending the same credit can both succeed if the check and the deduction are separate steps, which is the same class of problem as a usage limit that fails under a bulk import — and it is why reward balances belong in a transaction rather than in two sequential operations.

Building a referral programme that resists both abuse and its own retries is a small, well-understood piece of production engineering, and it is worth doing before the feature is public rather than after the first exploit. LaunchStudio, backed by Manifera's 11+ years of production engineering, implements reward logic, attribution, and webhook handling that hold up when strangers start testing them. [Describe your project](https://launchstudio.eu/en/#contact) for a review within one business day.

## Whether to Build One at All Yet

A referral programme amplifies whatever your product already does. If existing customers are not spontaneously recommending you, an incentive rarely creates that; it buys a thin layer of low-intent signups on top of nothing.

Two questions are worth answering honestly before building. **Has anyone referred someone without being asked?** If yes, a programme formalises something real. If no, the constraint is the product or the audience, and the referral feature will not move it. **Is the reward meaningful relative to your price?** Ten percent off a €9 plan motivates nobody; a free month of a €99 plan might. If the reward that would actually motivate someone is more than you can afford, you do not yet have a viable programme.

A cheaper starting point that costs almost nothing: a shareable link with basic attribution and no reward at all. You learn whether anyone shares, and who, before deciding what a reward should be — and the attribution you build for it is the same infrastructure the paid version would need.

## Real example

### €2,400 of Credits and Forty Accounts From One Person

Sander de Wit launched a referral programme for Bonnetje, a receipt-scanning tool for freelancers, built in Cursor. The reward was €20 in account credit per referral, paid on signup, with no verification.

Within eleven days, one participant had generated 40 signups using plus-addressed variants of two Gmail accounts and three disposable email domains — €800 in credits. Two other participants ran smaller versions of the same approach. Total credits issued reached roughly €2,400, of which about €300 corresponded to genuine customers.

Because the reward was a credit balance stored as a single number, there was no record of which credit came from which referral, so reversing the fraudulent portion required reconstructing it from signup timestamps and email patterns by hand. Two legitimate customers were briefly caught in the cleanup.

**Result:** the qualifying event moved to first payment plus 30 days, email addresses normalised before comparison, disposable domains blocked, self- and circular referrals rejected, and credits converted to an entry-based ledger with expiry. The programme relaunched and produced 34 paying customers over the following four months with no material abuse.

> "I built a marketing feature. What I had actually built was a way for strangers to withdraw money from my business, and it took eleven days for someone to notice before I did."
> — **Sander de Wit, Founder, Bonnetje**

**Cost & Timeline:** referral logic, ledger, and abuse controls rebuilt in 4 business days.

## Frequently Asked Questions

### What should trigger a referral reward?

First payment, or first payment plus a retention period, in nearly all cases. Rewarding on signup is trivially farmed and costs money for accounts that may never be used.

### How do people abuse referral programmes in practice?

Plus-addressed and dotted email variants for self-referral, circular referrals between two accounts, disposable email domains, and posting referral links where people already intending to sign up will see them.

### Should rewards be cash or account credit?

Account credit is simpler for most products: it avoids money-transmission questions, is easier to reverse when a referral turns out to be fraudulent, and keeps the cost tied to your own pricing.

### Why does my referral system sometimes reward twice for one payment?

Payment providers retry webhooks by design. Unless the handler records which event ids it has already processed, a retry credits the referrer again. This is standard practice that generated implementations usually omit.

### Should I build a referral programme before launch?

Usually not. If customers are not already recommending the product unprompted, an incentive rarely creates that behaviour. A shareable link with attribution and no reward is a cheap way to find out first.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "What should trigger a referral reward?", "acceptedAnswer": { "@type": "Answer", "text": "First payment, or first payment plus a retention period. Rewarding on signup is trivially farmed and costs money for accounts that may never be used." } },
    { "@type": "Question", "name": "How do people abuse referral programmes in practice?", "acceptedAnswer": { "@type": "Answer", "text": "Plus-addressed and dotted email variants for self-referral, circular referrals between two accounts, disposable email domains, and posting referral links where people already intending to sign up will see them." } },
    { "@type": "Question", "name": "Should rewards be cash or account credit?", "acceptedAnswer": { "@type": "Answer", "text": "Account credit is simpler for most products: it avoids money-transmission questions, is easier to reverse for fraudulent referrals, and ties the cost to your own pricing." } },
    { "@type": "Question", "name": "Why does my referral system sometimes reward twice for one payment?", "acceptedAnswer": { "@type": "Answer", "text": "Payment providers retry webhooks by design. Unless the handler records processed event ids, a retry credits the referrer again. Generated implementations usually omit this." } },
    { "@type": "Question", "name": "Should I build a referral programme before launch?", "acceptedAnswer": { "@type": "Answer", "text": "Usually not. If customers are not already recommending the product unprompted, an incentive rarely creates that. A shareable link with attribution and no reward is a cheap way to test first." } }
  ]
}
</script>
