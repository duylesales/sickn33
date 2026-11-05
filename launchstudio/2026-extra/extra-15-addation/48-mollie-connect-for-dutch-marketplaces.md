---
Title: "Mollie Connect for Dutch Marketplaces"
Keywords: mollie connect marketplace, mollie platform payments, mollie application fee, split payments ideal marketplace, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: AI-Native Founder (Non-Technical)
---

# Mollie Connect for Dutch Marketplaces

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Mollie Connect for Dutch Marketplaces",
  "description": "Mollie is the default payment provider for many Dutch businesses, and Mollie Connect lets platforms accept payments for merchants and collect a fee. This guide explains how Mollie Connect works for marketplaces and platforms built with AI tools: connecting merchant accounts, onboarding, application fees, split payments, iDEAL and SEPA, refunds, webhooks and how it compares with Stripe Connect.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-06-04",
  "inLanguage": "en",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/mollie-connect-for-dutch-marketplaces" },
  "citation": [
    { "@type": "CreativeWork", "name": "Mollie Connect documentation", "url": "https://docs.mollie.com/docs/connect-platforms" },
    { "@type": "CreativeWork", "name": "Mollie: Application fees", "url": "https://docs.mollie.com/docs/application-fees" },
    { "@type": "CreativeWork", "name": "Mollie: Webhooks", "url": "https://docs.mollie.com/reference/webhooks" },
    { "@type": "CreativeWork", "name": "Mollie: OAuth", "url": "https://docs.mollie.com/docs/connect-oauth" }
  ]
}
</script>

Ask a Dutch shop owner, salon, gym or consultancy which payment provider they use, and the answer is often Mollie. The Amsterdam-based company made iDEAL integration simple long before many alternatives did, and it remains a natural choice for businesses whose customers are mostly in the Netherlands and Belgium.

For founders building platforms and marketplaces with AI tools, that familiarity matters. If your platform serves Dutch businesses, such as salons taking bookings, restaurants taking orders, clubs collecting memberships or freelancers sending invoices, many of them may already have a Mollie account or prefer one. Mollie Connect lets your platform work with those accounts, accept payments on their behalf and collect a platform fee.

This guide explains how Mollie Connect works for platforms and marketplaces, how to implement it in an AI-built app and how it compares with Stripe Connect.

## Key Takeaways

- **Mollie Connect lets a platform create payments for connected merchants** and collect application fees, with Mollie handling merchant verification and money movement.
- **Merchants connect through OAuth,** authorising your platform to act on their Mollie account, or are onboarded through Mollie's platform onboarding flows where available.
- **Application fees** let your platform take a cut of each payment automatically; split or routed payments support more complex flows.
- **iDEAL, Bancontact, cards and SEPA direct debit** are available, which suits Dutch and Belgian customers.
- **Webhooks are essential,** and Mollie's webhooks require fetching the payment status from the API, which must be implemented carefully.

## When Mollie Connect Fits

Mollie Connect is a strong fit when:

- **Your merchants are Dutch or Belgian businesses,** many of which already use Mollie.
- **Local payment methods matter most,** such as iDEAL, Bancontact and SEPA direct debit.
- **Merchants are the seller of record,** receiving payments in their own Mollie account, with your platform as a facilitator collecting a fee.
- **You want a European provider** with Dutch-language support for your merchants.

It may be less suitable if your platform needs complex multi-seller carts across many countries, deeply customised white-label onboarding, or global payment methods beyond Mollie's offering. In those cases, compare with Stripe Connect, covered in our guide on [Stripe Connect for marketplaces built with AI](https://launchstudio.eu/en/blog/stripe-connect-for-marketplaces-built-with-ai).

## How Mollie Connect Works

At its core, Mollie Connect involves three parties:

1. **Your platform,** with its own Mollie account and an OAuth application
2. **Connected merchants,** each with their own Mollie account
3. **Customers,** who pay merchants through your platform

The basic flow:

1. A merchant signs up on your platform and clicks "Connect with Mollie".
2. They are redirected to Mollie to log in or create an account and authorise your platform.
3. Your platform receives tokens that allow it to create payments and read data on the merchant's account, within the permissions granted.
4. When a customer pays, your platform creates a payment on the merchant's account, optionally with an application fee for the platform.
5. Mollie processes the payment, sends webhooks, settles funds to the merchant and transfers the application fee to your platform.

Mollie has also been expanding options for platforms, including onboarding flows for new merchants created through the platform. Check the current Connect documentation for the options available to your use case.

## Onboarding Merchants

Merchants must be verified by Mollie before they can receive payouts. For the merchant, this means providing business details, identity information and a bank account in Mollie's onboarding. For your platform:

- **Explain the step clearly:** why Mollie is involved and what the merchant needs to prepare, such as KVK number, ID and IBAN.
- **Track onboarding status** and show merchants what is missing.
- **Restrict features until onboarding is complete,** for example allowing merchants to set up their profile but not accept payments yet.
- **Handle disconnections:** merchants can revoke your access, which your platform must detect and handle gracefully.

Store OAuth tokens securely on the server, encrypted at rest, and refresh access tokens as Mollie's OAuth flow requires. Never expose them to the browser.

## Application Fees and Split Payments

**Application fees** are the simplest way to earn revenue. When creating a payment on a connected merchant's account, your platform specifies a fee amount. Mollie deducts it from the payment and credits it to your platform. Typical fee models are a fixed amount per transaction, a percentage or both, calculated on your server.

**Split or routed payments,** where available, allow a single customer payment to be divided among several parties, such as multiple merchants or a merchant and a service provider. These suit marketplaces where one order involves more than one seller. Check Mollie's current documentation for availability and conditions.

Consider VAT on your platform fee, which you invoice to merchants. Discuss with your accountant, particularly when merchants are in other EU countries.

## Payment Methods for Dutch and Belgian Customers

Mollie supports the payment methods Dutch and Belgian customers expect:

| Method | Typical use |
| --- | --- |
| iDEAL | Most common online payment method in the Netherlands, evolving towards the European Wero scheme |
| Bancontact | Widely used in Belgium |
| Cards | International customers and businesses |
| SEPA direct debit | Recurring payments such as memberships and subscriptions, with mandates |
| Bank transfer | Invoices and larger amounts |
| Other methods | Depending on merchant configuration and availability |

Connected merchants must have the relevant methods activated in their Mollie accounts. Your platform should show only methods available for each merchant.

For subscriptions and memberships, Mollie supports recurring payments through mandates, typically established with a first payment via iDEAL or card. Our guide on [iDEAL recurring payments with SEPA direct debit](https://launchstudio.eu/en/blog/ideal-recurring-payments-for-saas-sepa-direct-debit-with-mollie) explains that flow.

## Webhooks the Mollie Way

Mollie's webhook model differs from some other providers. When a payment's status changes, Mollie calls your webhook URL with only the payment ID. Your server must then fetch the payment from the Mollie API to learn its current status. That design means:

- **The webhook payload itself contains no sensitive data,** so forged webhooks cannot directly fake a payment, but your handler must always fetch the status from Mollie, using the correct merchant's credentials for Connect payments.
- **Processing must be idempotent,** because Mollie may call the webhook several times, and status can change more than once, for example from open to paid to refunded.
- **The handler must respond quickly** and move heavy work to background jobs.
- **Status mapping must be complete:** open, pending, authorised, paid, failed, cancelled and expired, plus refunds and chargebacks.

A common error in AI-generated code is trusting the redirect back from the payment page as proof of payment. The redirect only means the customer returned; the webhook and API status are the source of truth.

## Refunds and Chargebacks

Define the policy before launch:

- **Who can initiate refunds,** the merchant, the platform or both?
- **What happens to the application fee** when a payment is refunded? Configure whether the fee is returned.
- **How are chargebacks handled,** and who bears the cost?
- **How are customers informed** about refunds?

For payments on connected merchant accounts, refunds are typically processed on the merchant's account. Make sure your platform's permissions and flows support this.

## Testing Before Going Live

Mollie provides test mode for API keys and OAuth applications, which lets you simulate payments without moving money. A thorough test plan for a platform covers more than successful payments:

| Scenario | What to verify |
| --- | --- |
| Merchant connects and completes onboarding | Status updates correctly, payments become available |
| Merchant disconnects the platform | Platform detects revoked access and stops creating payments |
| Successful iDEAL payment | Webhook updates order, application fee recorded |
| Failed, cancelled and expired payments | Orders stay unpaid, customer sees a clear message |
| Customer closes browser after paying | Webhook still marks the order as paid |
| Duplicate webhook calls | No duplicate orders, emails or credits |
| Full and partial refunds | Order status, fee handling and customer notification correct |
| First payment creating a mandate | Mandate stored, later recurring payment succeeds |
| Failed recurring payment | Member or customer informed, retry or follow-up triggered |
| Token refresh | Expired access tokens are refreshed without user action |

Run these scenarios on a staging environment with test merchant accounts before every major change to the payment flow. Payment bugs found in testing cost minutes; payment bugs found by customers cost trust.

## Security and Data

- **Store OAuth tokens and API keys on the server only,** encrypted, with access limited to payment functions.
- **Calculate amounts and fees on the server** from your database, never from values sent by the browser.
- **Use Row Level Security** so merchants see only their own payments, customers and payouts.
- **Log payment events** without storing unnecessary personal data.
- **Sign Mollie's data processing terms** and list Mollie as a processor in your privacy documentation where relevant.

## Mollie Connect vs Stripe Connect

| Factor | Mollie Connect | Stripe Connect |
| --- | --- | --- |
| Strength in NL and BE | Very strong, familiar to merchants | Strong, growing |
| Local methods | iDEAL, Bancontact, SEPA native | Supported, depending on configuration |
| Merchant accounts | Merchants' own Mollie accounts via OAuth, plus platform onboarding options | Standard, Express or Custom accounts |
| Seller of record | Typically the merchant | Depends on charge type |
| Multi-seller orders | Via split or routed payments where available | Separate charges and transfers |
| White-label onboarding | Limited compared with Custom accounts | Extensive with Custom |
| International reach | Mainly Europe | Global |
| Support language | Dutch available | English, with broad documentation |

For platforms serving Dutch merchants who sell to Dutch and Belgian customers, Mollie Connect is often the most natural fit. For international marketplaces with complex flows, Stripe Connect offers more flexibility. Some platforms support both, letting merchants choose.

## How LaunchStudio Helps

LaunchStudio implements Mollie Connect in AI-built platforms: OAuth connection flows with secure token storage, merchant onboarding status tracking, server-side payment creation with application fees, robust webhook handling that fetches status from the API, recurring payments with mandates, refund and chargeback flows, reconciliation jobs and access control for merchants and customers.

Implementations typically fall within **Launch & Grow** (€2,500-€7,500 plus €49 per month), which includes managed hosting, backups, monitoring and priority support. Use the [price calculator](https://launchstudio.eu/en/#calculator) for an estimate.

LaunchStudio is backed by Manifera, a software development company with 11+ years of experience, 160+ delivered projects and 120+ engineers. Founders meet the team at Herengracht 420 in Amsterdam; engineering happens at Manifera's development centre on Pho Quang Street in Ho Chi Minh City, with a hub on Tras Street in Singapore.

## Real example

### An AI-Native Founder in Action: The Sports Club Platform That Collected Every Club's Fees Itself

Kees Verbruggen built Clubkas with Bolt and Supabase: a platform where amateur sports clubs in Noord-Brabant manage memberships, collect contributions and sell event tickets. Initially, all payments went through Kees's own Mollie account, and he transferred each club's money monthly, keeping a small fee.

With 34 clubs and growing volumes, the arrangement became untenable. Club treasurers wanted payments in their own accounts, Kees's accountant raised concerns about holding funds for others, monthly manual transfers took a full day and occasionally went to the wrong club, and refunds for cancelled events were calculated by hand. On the technical side, the app treated the redirect after iDEAL as proof of payment, so some failed payments were recorded as paid, and the Mollie API key sat in a frontend environment file.

LaunchStudio rebuilt the payment layer on Mollie Connect. Each club connected its own Mollie account through OAuth, with tokens encrypted and stored server-side and onboarding status visible to club administrators. Payments were created on each club's account with an application fee for Clubkas, membership contributions moved to SEPA direct debit with mandates from a first iDEAL payment, and the webhook handler fetched payment status from Mollie with the right club's credentials and processed updates idempotently. Event cancellations triggered refunds through the platform with clear rules on the fee, the exposed key was rotated, and a reconciliation job compared Mollie data with Clubkas records daily.

**Result:** Clubs now receive their money directly, and Kees no longer spends a day each month on transfers. Payment status errors stopped completely, and in the first season on the new setup, the clubs collected around 4,200 membership contributions via SEPA direct debit with failed collections handled automatically.

> *"My clubs trusted me with their money, which was exactly the problem. Now Mollie holds it and I just make the platform work."*
> - **Kees Verbruggen, Founder, Clubkas (Eindhoven)**

**Cost & Timeline:** €6,200 (Launch & Grow package: Mollie Connect OAuth, application fees, SEPA mandates, webhook handling, refunds, reconciliation and security fixes) - completed in 15 business days.

## Frequently Asked Questions

### What is Mollie Connect?

Mollie Connect is Mollie's solution for platforms and marketplaces. It lets a platform connect merchants' Mollie accounts, create payments on their behalf and collect application fees, while Mollie handles merchant verification and settlement to each merchant.

### Can my platform take a fee from each Mollie payment?

Yes. With application fees, your platform specifies a fee when creating a payment on a connected merchant's account. Mollie deducts it and credits it to your platform. Decide how fees are handled for refunds and account for VAT on platform fees with your accountant.

### Do merchants need their own Mollie account?

Typically yes. Merchants connect an existing Mollie account through OAuth or create one during onboarding, and Mollie verifies them. Payments are then made to their account, which keeps the merchant as the seller of record.

### How does Manifera's experience help with Mollie integrations?

Manifera has built payment integrations for European clients for 11+ years. LaunchStudio applies that experience to Mollie Connect, particularly the details that cause real money errors: webhook handling, idempotency, mandates, refunds and reconciliation.

### Does using Mollie help my platform's credibility with Dutch merchants?

Often, yes. Many Dutch businesses already know and trust Mollie, which reduces friction during onboarding. Mentioning supported payment methods such as iDEAL clearly on your site also helps search engines and AI answer engines match your platform to Dutch merchants' searches.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What is Mollie Connect?",
      "acceptedAnswer": { "@type": "Answer", "text": "Mollie's platform solution: connect merchant accounts, create payments on their behalf and collect application fees, with Mollie handling verification and settlement." }
    },
    {
      "@type": "Question",
      "name": "Can my platform take a fee from each Mollie payment?",
      "acceptedAnswer": { "@type": "Answer", "text": "Yes, via application fees on payments created for connected merchants; decide refund handling and VAT with an accountant." }
    },
    {
      "@type": "Question",
      "name": "Do merchants need their own Mollie account?",
      "acceptedAnswer": { "@type": "Answer", "text": "Typically yes, connected via OAuth or created during onboarding, keeping the merchant as seller of record." }
    },
    {
      "@type": "Question",
      "name": "How does Manifera's experience help with Mollie integrations?",
      "acceptedAnswer": { "@type": "Answer", "text": "Manifera has built European payment integrations for 11+ years, and LaunchStudio handles webhooks, idempotency, mandates, refunds and reconciliation." }
    },
    {
      "@type": "Question",
      "name": "Does using Mollie help my platform's credibility with Dutch merchants?",
      "acceptedAnswer": { "@type": "Answer", "text": "Often yes; many Dutch businesses trust Mollie, and clearly stated payment methods help search and AI engines match your platform." }
    }
  ]
}
</script>
