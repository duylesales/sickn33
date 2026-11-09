---
Title: "How Do I Handle Refunds and Chargebacks in My SaaS?"
Keywords: saas refunds chargebacks, refund policy saas eu, sepa direct debit storno, stripe dispute evidence, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: AI-Native Founder (Non-Technical)
---

# How Do I Handle Refunds and Chargebacks in My SaaS?

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "How Do I Handle Refunds and Chargebacks in My SaaS?",
  "description": "Refunds and chargebacks are part of every paid SaaS product, and AI-built apps often handle them manually or not at all. This guide explains refund policies for consumers and businesses in the EU, implementing refunds and credit notes correctly, revoking access, SEPA direct debit reversals, card chargebacks and disputes, evidence that wins disputes, preventing disputes and the metrics to watch.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-08-07",
  "inLanguage": "en",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/how-do-i-handle-refunds-and-chargebacks-in-my-saas" },
  "citation": [
    { "@type": "CreativeWork", "name": "Directive 2011/83/EU on consumer rights", "url": "https://eur-lex.europa.eu/eli/dir/2011/83/oj" },
    { "@type": "CreativeWork", "name": "European Payments Council: SEPA Direct Debit", "url": "https://www.europeanpaymentscouncil.eu/what-we-do/sepa-direct-debit" },
    { "@type": "CreativeWork", "name": "Stripe: Disputes and fraud", "url": "https://docs.stripe.com/disputes" },
    { "@type": "CreativeWork", "name": "Mollie: Refunds and chargebacks", "url": "https://docs.mollie.com/docs/refunds" }
  ]
}
</script>

**Short answer:** write a clear refund policy that respects consumer rights where they apply, implement refunds through your payment provider's API with matching credit notes and access changes, and treat chargebacks and direct debit reversals as events your app must process automatically. Collect evidence, such as terms acceptance, usage logs and communication, so you can respond to disputes, and reduce disputes in the first place with clear billing descriptors, renewal reminders and easy cancellation. Most AI-built SaaS products handle refunds manually and ignore chargebacks until one arrives; designing for them early saves money and stress.

## Key Takeaways

- **Consumer rights apply to consumers,** including a withdrawal period for many online purchases with specific rules for digital services and content; business customers usually rely on your terms.
- **Refunds must update everything:** payment provider, invoices and credit notes, VAT, access and usage limits.
- **SEPA direct debits can be reversed** by the payer within defined periods, which your app must detect and handle.
- **Card chargebacks** come with deadlines and fees; good evidence improves the chance of winning.
- **Prevention is cheaper than disputes:** recognisable descriptors, receipts, reminders before renewals and simple cancellation.

## Refund Policies: Consumers and Businesses

**Consumers in the EU** generally have a right of withdrawal for distance contracts, commonly 14 days, under EU consumer rules implemented in Dutch law. For digital services and digital content, specific rules apply: for example, the right of withdrawal can end once the service has been fully performed, or once supply of digital content has started, when the consumer has expressly agreed and acknowledged losing the right. Implementing this correctly requires clear information and recorded consent at checkout. ConsuWijzer, the Dutch consumer authority's information service, explains consumer rights in plain language.

**Business customers** do not have the same statutory withdrawal right. Refunds follow your terms and contracts, which should state:

- Whether payments are refundable, and under which conditions
- How cancellations work, such as at the end of the current period
- What happens with annual prepayments when a customer cancels
- How downgrades are handled

Many SaaS companies offer goodwill refunds beyond legal requirements, for example within the first days of a subscription. Whatever you decide, write it down, show it before purchase and apply it consistently. Consult a lawyer for your terms.

## Implementing Refunds Correctly

A refund is more than sending money back. When a refund happens, your app should:

1. **Create the refund through the payment provider's API,** full or partial, with an idempotency key so retries do not refund twice.
2. **Record the refund** in your database, linked to the original payment.
3. **Issue a credit note** linked to the original invoice, with consistent VAT, instead of editing or deleting the invoice.
4. **Update access:** end or adjust the subscription, revoke features or credits paid for by the refunded amount, according to your policy.
5. **Notify the customer** with the amount, method and expected timing.
6. **Update reporting and accounting exports.**

Process refund status through webhooks, because refunds can fail or take time, especially for some payment methods.

## Partial Refunds and Proration

Common scenarios:

- **Mid-period cancellation with partial refund:** calculate the unused portion with clear rounding rules.
- **Downgrade with credit:** apply a credit to the next invoice instead of a refund.
- **Refund of a specific item,** such as an add-on or usage overage.

Use your billing provider's proration logic where possible, and store amounts in cents. Our guide on [money, rounding and currency bugs](https://launchstudio.eu/en/blog/money-rounding-and-currency-bugs-in-saas) explains the pitfalls.

## SEPA Direct Debit Reversals

Many Dutch SaaS products collect subscriptions by SEPA direct debit. Under SEPA rules, payers can request a refund of an authorised direct debit from their bank within eight weeks without giving a reason, and longer for unauthorised debits. These reversals arrive at your payment provider and are typically reported to your app through webhooks as chargebacks or reversals.

Your app should:

- **Detect reversals** through webhooks and mark the payment as reversed
- **Update the subscription status,** for example to past due
- **Notify the customer** and offer an alternative payment method, such as an iDEAL payment link
- **Pause or limit access** according to your policy after a grace period
- **Track reversal fees** charged by your provider

A reversal is often a mistake or a bank account change rather than a dispute. Friendly communication recovers many payments.

## Card Chargebacks and Disputes

When a cardholder disputes a charge with their bank, the payment provider notifies you, often deducting the amount and a dispute fee immediately. You typically have a limited time to respond with evidence. Common dispute reasons include fraud, product not received, subscription cancelled and unrecognised charge.

Your app should:

- **Receive dispute events** through webhooks and alert the team
- **Collect evidence automatically:** customer details, terms acceptance, login and usage history, invoices, communication and cancellation records
- **Submit evidence** through the provider's dashboard or API before the deadline
- **Decide when to accept** small disputes rather than contest them
- **Record outcomes** for analysis

Stripe and Mollie document their dispute processes and evidence requirements.

## Evidence That Helps

| Dispute reason | Useful evidence |
| --- | --- |
| Fraudulent | Authentication details, such as 3D Secure, IP addresses, account history, previous undisputed payments |
| Product not received | Login records, usage logs, delivered features or credits |
| Subscription cancelled | Cancellation policy, records showing no cancellation request, renewal reminders sent |
| Unrecognised | Billing descriptor, receipts, customer account details, communication |
| Not as described | Product description at purchase, terms, support history |

Usage logs and audit trails are valuable here, which is another reason to keep them. Our guide on [audit logs for B2B SaaS](https://launchstudio.eu/en/blog/audit-logs-for-b2b-saas) explains how to record them.

## Preventing Disputes

Most disputes are avoidable:

- **Recognisable billing descriptor,** so customers recognise your charge on their statement
- **Receipts** for every payment, with clear product name and support contact
- **Renewal reminders** before annual renewals and trial conversions
- **Easy cancellation** in the app, without hunting for a support email
- **Responsive support,** so customers ask you before asking their bank
- **Strong customer authentication** for card payments, such as 3D Secure, which can shift fraud liability
- **Fraud checks** on suspicious sign-ups, such as many trials from the same card
- **Clear pricing and terms** at checkout

## Designing the Cancellation Flow

Cancellation is where many disputes begin. If customers cannot find how to cancel, they ask their bank instead. A good cancellation flow:

1. **Is easy to find** in account or billing settings.
2. **Explains the consequences:** when access ends, what happens to data and whether any refund applies.
3. **Offers relevant alternatives** without pressure, such as pausing, downgrading or switching to annual billing.
4. **Asks briefly why,** with optional reasons, which helps improve the product.
5. **Confirms immediately** on screen and by email, with the end date of access.
6. **Updates the payment provider** so no further charges occur, verified by webhook.

Making cancellation hard may slightly reduce churn in the short term, but it increases disputes, damages reputation and can conflict with consumer protection expectations. Several EU and Dutch consumer rules push towards cancellation being as easy as subscribing.

## Refund Decisions by the Team

For refund requests outside automatic rules, give your team a simple decision guide: which situations qualify for full or partial refunds, who can approve exceptions and how to record the reason. Consistency prevents arguments and helps spot patterns, such as a feature that repeatedly disappoints customers.

## Handling Disputes on Marketplaces

If your SaaS is a marketplace or platform that processes payments for others, decide who is responsible for refunds and disputes: the platform or the seller. Platform payment products such as Stripe Connect and Mollie Connect support different models, and your terms must reflect your choice. Our guide on [Stripe Connect for marketplaces](https://launchstudio.eu/en/blog/stripe-connect-for-marketplaces-built-with-ai) covers the structure.

## Metrics to Watch

- **Refund rate:** refunds as a share of payments, by plan and channel
- **Dispute rate:** disputes as a share of card payments; card networks and providers monitor merchants with elevated dispute rates, and high rates can lead to fees or account restrictions
- **Reversal rate** for direct debits
- **Dispute win rate**
- **Reasons,** to identify fixable causes, such as unclear descriptors or missed cancellations

## Free Trials and Refund Requests

Many refund requests and disputes come from trials that converted into paid subscriptions without customers noticing. Send a reminder a few days before a trial ends, show the price and date clearly, and make it easy to cancel before conversion. Customers who knowingly continue rarely dispute; customers who are surprised often do. If you collect payment details at trial start, be particularly clear about what will happen when the trial ends.

## Common Mistakes in AI-Built SaaS

**Refunds done manually in the provider dashboard,** while the app still grants access and the invoice remains unchanged.

**Editing or deleting invoices** instead of issuing credit notes.

**Ignoring reversal and dispute webhooks,** so access continues after money is gone.

**No evidence trail,** making disputes unwinnable.

**Cancellation hidden or impossible in the app.**

**Refunds without idempotency,** causing double refunds on retries.

## Testing Refund and Dispute Flows

Use your payment provider's test mode to simulate refunds, partial refunds, direct debit reversals and disputes on staging. Verify that access, invoices, credit notes, emails and reports all update correctly for each case before relying on the flows in production.

## How LaunchStudio Helps

LaunchStudio implements refund and dispute handling in AI-built SaaS: refund flows through Stripe or Mollie with idempotency, credit notes with correct VAT, access and entitlement updates, webhook processing for refunds, SEPA reversals and disputes, automated evidence collection, cancellation and renewal reminder flows, and reporting on refund and dispute rates.

These implementations typically fall within **Launch & Grow** (€2,500-€7,500 plus €49 per month), which includes payments, managed hosting, monitoring and priority support. Use the [price calculator](https://launchstudio.eu/en/#calculator) for an estimate.

LaunchStudio is backed by Manifera, a software development company with 11+ years of experience, 160+ delivered projects and 120+ engineers, including payment and billing systems for clients in Europe and Asia. Founders meet the team at Herengracht 420 in Amsterdam; engineering happens at the development centre on Pho Quang Street in Ho Chi Minh City, with a hub on Tras Street in Singapore.

## Real example

### An AI-Native Founder in Action: The Fitness App That Kept Granting Access After Reversals

Iris Bos built Thuisfit with Bolt and Supabase: a subscription app with home workout programmes, billed monthly by SEPA direct debit through Mollie after a first iDEAL payment, and annually by card for some users. As subscribers grew to around 3,000, Iris noticed that revenue in Mollie did not match active subscribers in her app.

The investigation revealed several gaps. Direct debit reversals were not processed by the app, so users whose banks reversed payments kept full access, some for months. Refunds were done manually in the Mollie dashboard, without updating access or invoices. Card disputes from annual subscribers were usually lost because Iris had no evidence, and several came from customers who did not recognise the charge because the descriptor showed an old company name. There was no in-app cancellation; users had to email, and some disputed charges instead.

LaunchStudio added webhook handling for refunds, reversals and chargebacks, updating subscription status and access automatically, with friendly emails offering an iDEAL payment link after reversals and a grace period before access paused. Refunds moved into an admin action that called the Mollie API with idempotency, created credit notes and adjusted access. Evidence collection compiled terms acceptance, login and workout history and receipts for disputes. The billing descriptor was updated, renewal reminders were sent two weeks before annual renewals, and users could cancel in the app in two clicks.

**Result:** Within two months, revenue and active subscriptions reconciled, recovered reversed payments covered the project cost several times over, and card disputes dropped sharply. Iris won most of the remaining disputes using the automated evidence.

> *"I was paying the price of being easy to dispute and hard to cancel. Fixing both turned out to be good for customers and for revenue."*
> - **Iris Bos, Founder, Thuisfit (Amersfoort)**

**Cost & Timeline:** €4,200 (Launch & Grow package: refund, reversal and dispute webhooks, credit notes, evidence collection, descriptor and renewal reminders, in-app cancellation) - completed in 10 business days.

## Frequently Asked Questions

### Do I have to offer refunds for my SaaS subscription?

For consumers, EU rules give a withdrawal right for many online purchases, with specific conditions for digital services and content that affect when it ends. For business customers, refunds follow your terms. Write a clear policy, show it before purchase and apply it consistently; consult a lawyer for your terms.

### What happens when a SEPA direct debit is reversed?

The payer's bank returns the money, your payment provider notifies you and usually charges a fee. Your app should mark the payment as reversed, update the subscription, contact the customer with an alternative payment option and adjust access according to your policy.

### How do I win a chargeback dispute?

Respond before the deadline with evidence that fits the dispute reason: authentication details, usage logs, terms acceptance, cancellation records, receipts and communication. Automated evidence collection makes this fast and consistent.

### How does Manifera's experience help with billing operations?

Manifera has built payment and billing systems for clients for 11+ years. LaunchStudio applies that experience to make refunds, reversals and disputes flow automatically through the app, keeping revenue, access and accounting aligned.

### Do refund and cancellation practices affect my reputation?

Yes. Easy cancellation and fair refunds reduce disputes and negative reviews, while hidden cancellation and unrecognised charges generate complaints that customers, review sites, search engines and AI answer engines pick up.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Do I have to offer refunds for my SaaS subscription?",
      "acceptedAnswer": { "@type": "Answer", "text": "Consumers have EU withdrawal rights with specific digital rules; business refunds follow your terms." }
    },
    {
      "@type": "Question",
      "name": "What happens when a SEPA direct debit is reversed?",
      "acceptedAnswer": { "@type": "Answer", "text": "The bank returns the money; mark it reversed, update the subscription, contact the customer and adjust access." }
    },
    {
      "@type": "Question",
      "name": "How do I win a chargeback dispute?",
      "acceptedAnswer": { "@type": "Answer", "text": "Submit reason-specific evidence before the deadline, ideally collected automatically." }
    },
    {
      "@type": "Question",
      "name": "How does Manifera's experience help with billing operations?",
      "acceptedAnswer": { "@type": "Answer", "text": "Manifera has built billing systems for 11+ years, automating refunds, reversals and disputes." }
    },
    {
      "@type": "Question",
      "name": "Do refund and cancellation practices affect my reputation?",
      "acceptedAnswer": { "@type": "Answer", "text": "Yes; fair practices reduce disputes and negative reviews that search and AI engines pick up." }
    }
  ]
}
</script>
