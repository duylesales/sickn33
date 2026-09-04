---
Title: "Two-Sided Marketplace: The Launch Decisions You Can't Defer"
Keywords: two-sided marketplace launch, marketplace payment splitting, escrow and payouts, seller onboarding KYC, marketplace production ready, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: SaaS Founder Scale-Up
---

# Two-Sided Marketplace: The Launch Decisions You Can't Defer

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Two-Sided Marketplace: The Launch Decisions You Can't Defer",
  "description": "A marketplace has a small set of decisions — money flow, seller verification, dispute liability, contact leakage — that are cheap to make before launch and extremely expensive to change afterwards. This article separates those from the ones you can safely postpone.",
  "author": {
    "@type": "Organization",
    "name": "LaunchStudio",
    "url": "https://launchstudio.eu/en/"
  },
  "publisher": {
    "@type": "Organization",
    "name": "Manifera",
    "url": "https://www.manifera.com"
  },
  "datePublished": "2027-01-06",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://launchstudio.eu/en/blog/two-sided-marketplace-launch-decisions-you-cant-defer"
  }
}
</script>

Every marketplace advisor tells you the hard part is liquidity — chicken and egg, cold start, supply before demand. That advice is correct and it is also the reason a specific category of marketplace dies with healthy liquidity: founders spend all their attention on getting both sides to show up and none on what happens structurally once they do. The first transaction is a party. The second hundred are an operations problem, and the shape of that problem was decided by choices made in a prototype months earlier.

The useful frame for a marketplace launch is not a feature checklist. It is a short list of decisions that are cheap now and brutal later, because changing them means migrating money, re-onboarding a supply side that already trusts you, or telling customers their historic transactions look different now. Here is that list, with the deferrable stuff explicitly named at the end so you can stop worrying about it.

## The Decision Nobody Should Make by Accident: Who Holds the Money

There are three money architectures, and prototypes almost always implement the one that is legally and operationally worst. Architecture one: buyer pays you, funds land in your company account, you pay sellers later by bank transfer. It is trivially easy to build and it means you are holding third-party funds — a regulated activity in the EU, an accounting nightmare, and a business that cannot survive its first cash-flow gap because seller payouts and your runway share one balance.

Architecture two, the one most marketplaces should choose: a connected-accounts model such as Stripe Connect or Mollie Connect, where the buyer's payment is split at authorisation into the seller's balance and your platform fee, and the payment provider handles payouts, seller balances and the regulatory weight. Architecture three: buyer and seller transact directly and you invoice the seller a commission afterwards, which is simple but gives you no leverage over disputes and a collection problem instead of a revenue stream.

Choose deliberately, and choose before you have sellers, because migrating a live marketplace from architecture one to architecture two means re-onboarding every seller through a verification flow they never agreed to when they signed up. That is the single most common reason a marketplace's growth stalls for a quarter in year two.

## Escrow Timing Is a Product Promise, Not a Setting

Once money splits at the payment provider, the next question is when the seller can actually access their share. Instant payout is a great seller experience and an unmanaged fraud exposure. Holding funds until the buyer confirms delivery protects buyers and creates a support queue of "I never confirmed, where's my money" tickets. Most durable marketplaces land on a rule that is boring and written down: funds are released a fixed number of days after the delivery or completion event unless a dispute is opened, with a shorter window for sellers above a trust threshold.

Whatever you pick, it needs three things in the code: an explicit transaction state machine (`pending` → `authorised` → `in_progress` → `completed` → `released`, plus `disputed`, `refunded`, `cancelled`), a scheduled job that moves eligible transactions to released, and both sides seeing the same status and date in their dashboard. Prototypes typically have a boolean called `paid` and a status derived from whatever field the AI tool happened to create, which is exactly the structure that makes your first dispute unanswerable because you cannot prove what state the transaction was in when.

## Dual Onboarding Means You Are Shipping Two Products

Your buyer signup is an email and a password. Your seller signup is a small compliance product: legal entity type, KYC identity documents, a bank account, a VAT number where relevant, and a verification state that can be pending, incomplete, restricted or rejected — each of which needs a screen, an email and a rule about what the seller may do while in it. If your prototype treats sellers as users with a `role` column, you have not yet built the seller side; you have built a label.

The specific traps: sellers who create listings before verification completes and then can't be paid; verification requirements that the payment provider adds after a payout threshold is crossed, so a previously fine seller is suddenly restricted mid-transaction; and no visibility into any of it, so your support team learns about a problem when the seller emails in anger. Production means listening to the provider's account webhooks, storing the requirement state, and blocking or warning in the UI before a buyer's money is involved.

## Refunds, Chargebacks, and the Question of Who Eats Them

A chargeback on a split payment arrives weeks after the seller has been paid out. If your model says the seller bears it, you need the ability to claw back from a future payout or a negative balance — a mechanism that has to exist in your data model, not in an email you send hoping for a bank transfer. If your model says you bear it, that is a real cost line and needs to be priced into your commission.

Write the policy before launch in one paragraph: who is refunded, from whose balance, within what window, and what evidence a seller must supply to contest. Then implement partial refunds, because they are what actually happens — a job half done, a shipment with one item missing — and a refund path that only handles the full amount forces your operations team into manual transfers that break your reconciliation. Add a dispute state that freezes the payout clock so a claim opened on day six can't be outrun by a release scheduled for day seven.

## Trust Artifacts: Reviews That Mean Something and Identity That Was Checked

The reason people transact with strangers on your platform is a small set of signals, and each has a specific integrity requirement. Reviews must be attached to completed transactions, or your marketplace fills with reciprocal five-star trades within a month. Seller identity should be verified through your payment provider's KYC rather than by you collecting passport scans — storing identity documents yourself creates a GDPR liability you have no reason to accept. Ratings need an aggregate that can't be gamed by a burst of new accounts, which in practice means new accounts have a rate limit on reviews and a weighted average that discounts an account's first days.

None of this is exotic engineering. All of it is nearly impossible to add credibly later, because retro-fitting "verified" badges onto a population of sellers who were never verified means either lying or a mass re-verification campaign, and rebuilding a review system means either discarding your existing reviews or keeping ones you can no longer vouch for.

## Leakage: The Incentive You Designed Without Noticing

Every marketplace with a commission creates an incentive to transact off-platform. A 15% fee on a €3,000 job is €450 of shared motive for the buyer and seller to swap phone numbers. You will not eliminate this, and pretending otherwise leads founders to build hostile products. What you can do before launch is make the on-platform path materially better and the off-platform path mildly inconvenient: mask contact details until a booking is confirmed, keep messaging inside the product where the history and dispute evidence live, filter phone numbers and email addresses in early messages, and give buyers something they lose by leaving — payment protection, a guarantee, the dispute process itself.

The fee structure matters here more than the enforcement. Marketplaces with high per-transaction fees and low ongoing value leak badly regardless of contact masking. Marketplaces where the platform holds the payment guarantee, the scheduling and the record leak much less, because leaving costs both parties something concrete. Decide which you are before you set a commission rate, because changing a commission after sellers have priced their offers is its own crisis.

## What You Can Genuinely Defer (Permission Granted)

Not everything is urgent, and marketplace founders routinely delay launch over the wrong things. Ranking and search relevance can be a simple filter and sort until you have enough inventory for ranking to matter. Automated matching, recommendation engines and dynamic pricing are all post-liquidity problems. Multi-currency and cross-border tax handling can wait until you actually cross a border. A mobile app can wait behind a responsive web product. In-app messaging attachments, saved searches, seller analytics dashboards and a public API are all fine as month-three work.

The test is simple: if getting it wrong costs you a feature, defer it. If getting it wrong costs you money that is not yours, a seller's trust, or a legal position in a dispute, it belongs in the launch build. Almost every irreversible marketplace decision sits in the second category, and almost every one founders agonise over sits in the first.

## What Hardening a Marketplace Prototype Actually Costs

A marketplace built in Lovable or Bolt usually arrives with the two sides, the listings and the checkout already looking right, and none of the state machine, connected-accounts flow, webhook handling, dispute states or payout logic underneath. That work sits in the SaaS band of the [LaunchStudio price calculator](https://launchstudio.eu/en/#calculator) — €2,833 to €7,167 — because it is genuine backend engineering rather than configuration, and it lands at roughly a fifth of what an agency charges for the same scope, in one to three weeks rather than one to three quarters. Our engineers have shipped 160+ projects for enterprise clients; marketplace money flow is a well-trodden problem for people who have built payment systems before, and a research project for people who haven't.

The decisions in this article take an afternoon to make and a week or two to implement. Made after launch, they take a quarter and a lot of apologising to your supply side. If you have a marketplace prototype and you are not certain which architecture your payments actually use, that uncertainty is itself the answer. [Send us the link to your prototype and we'll tell you what we find, free](https://launchstudio.eu/en/#contact) — or look at how [Manifera](https://www.manifera.com/portfolio/), the parent company behind LaunchStudio, has handled transactional systems for clients where the money flow had to be right the first time.

## Real example

### A Marketplace in Action: The Payout Run That Exposed the Architecture

Joris Bakker launched VakStroom, a marketplace connecting Dutch homeowners with vetted specialist tradespeople, after building the whole thing in Bolt over two months. Liquidity came faster than expected: 140 tradespeople, roughly 60 jobs a week by the eighth week. Buyer payments landed in the company's business account, and every Friday Joris ran a spreadsheet and made bank transfers to tradespeople himself.

Week nine broke it. Two homeowners disputed jobs after their tradespeople had been paid on the Friday, one payout went to an IBAN with a transposed digit, and a bank compliance officer asked Joris a question about third-party funds that he could not answer well. The rebuild was targeted rather than total: Mollie Connect with split payments at authorisation, a proper transaction state machine with a seven-day release window, an onboarding flow that collected verification through the provider instead of a Google Form, and webhook handling so restricted accounts were flagged before a homeowner could book them.

**Result:** Friday payout runs disappeared entirely, the two open disputes were resolved from held funds instead of Joris's own account, and tradesperson onboarding — previously a three-day manual back-and-forth — became a fifteen-minute self-service flow that let VakStroom add 90 suppliers in the following month.

> *"I had built a marketplace on top of my own bank account and called it a platform. Nobody tells you that the money architecture is the product. It cost me one week to fix and it would have cost me the company to leave."*
> — **Joris Bakker, Founder, VakStroom (Eindhoven)**

**Cost & Timeline:** €5,200 fixed price — connected accounts, transaction states, payout logic and seller verification — live in 13 business days.

---

## Frequently Asked Questions

### Can I launch a marketplace by collecting payments myself and paying sellers manually?

You can run a pilot that way with a handful of transactions, but it means holding third-party funds in your own account, which is a regulated activity in the EU and mixes seller money with your runway. Move to a connected-accounts model before you have sellers you would have to re-onboard.

### How long should I hold funds before releasing them to a seller?

Most marketplaces settle on a fixed window of a few days after the completion event, shortened for sellers above a trust threshold and paused automatically when a dispute is opened. The exact number matters less than having it written down, visible to both sides, and enforced by a scheduled job rather than by someone remembering.

### Who should be liable for a chargeback on a split payment?

That is a policy choice, but whichever you choose has to exist in the data model: if the seller bears it you need clawback against future payouts or a negative balance, and if you bear it the cost belongs in your commission rate. The failure mode is having no mechanism at all and discovering that weeks after the seller has been paid.

### Should I block buyers and sellers from exchanging contact details?

Masking contact details until a booking is confirmed is worth doing, but leakage is mainly a fee-design problem rather than an enforcement one. Marketplaces that hold the payment guarantee, the record and the dispute process leak far less than those charging a high commission for a directory-like service.

### What marketplace features are safe to postpone until after launch?

Search ranking, recommendations, dynamic pricing, seller analytics, multi-currency and a mobile app can all wait. Anything touching money that isn't yours, seller verification, dispute evidence or review integrity cannot, because those are the decisions that require re-onboarding or rewriting history to change later.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Can I launch a marketplace by collecting payments myself and paying sellers manually?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "You can pilot that way with a handful of transactions, but it means holding third-party funds in your own account, a regulated activity in the EU that mixes seller money with your runway. Move to connected accounts before you have sellers you would need to re-onboard."
      }
    },
    {
      "@type": "Question",
      "name": "How long should I hold funds before releasing them to a seller?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Most marketplaces use a fixed window of a few days after completion, shortened for trusted sellers and paused automatically when a dispute opens. The number matters less than having it written down, visible to both sides and enforced by a scheduled job."
      }
    },
    {
      "@type": "Question",
      "name": "Who should be liable for a chargeback on a split payment?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "It is a policy choice, but it must exist in the data model: seller liability requires clawback against future payouts or a negative balance, and platform liability belongs in your commission rate. The failure mode is having no mechanism at all."
      }
    },
    {
      "@type": "Question",
      "name": "Should I block buyers and sellers from exchanging contact details?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Masking contact details until a booking is confirmed helps, but leakage is mainly a fee-design problem. Marketplaces that hold the payment guarantee, the record and the dispute process leak far less than high-commission directories."
      }
    },
    {
      "@type": "Question",
      "name": "What marketplace features are safe to postpone until after launch?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Search ranking, recommendations, dynamic pricing, seller analytics, multi-currency and a mobile app can wait. Anything touching money that is not yours, seller verification, dispute evidence or review integrity cannot."
      }
    }
  ]
}
</script>
