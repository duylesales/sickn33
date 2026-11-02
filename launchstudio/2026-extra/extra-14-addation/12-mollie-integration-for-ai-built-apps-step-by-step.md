---
Title: "Mollie Integration for AI-Built Apps: A Step-by-Step Guide"
Keywords: mollie integration ai app, mollie lovable, mollie webhook, mollie supabase edge function, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: Technical Solo Founder / Indie Hacker
---

# Mollie Integration for AI-Built Apps: A Step-by-Step Guide

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Mollie Integration for AI-Built Apps: A Step-by-Step Guide",
  "description": "A practical Mollie integration guide for apps built with Lovable, Bolt or Cursor: API keys, creating payments in a Supabase edge function, handling Mollie's ID-only webhooks, statuses, refunds and going live.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-01-20",
  "inLanguage": "en",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/mollie-integration-for-ai-built-apps-step-by-step" }
}
</script>

Mollie is the payment provider many Dutch and Belgian founders choose: Amsterdam-based, strong on iDEAL and Bancontact, and clear pricing. AI app builders, however, default to Stripe. Ask Lovable or Bolt for a Mollie integration and you will usually get something that creates a payment and redirects the customer, but not the parts that make it reliable. This guide shows the full Mollie integration, step by step, for an app with a Supabase backend.

## What You Need Before Starting

- A Mollie account with a website profile approved for your domain
- Test and live API keys (they start with `test_` and `live_`)
- A Supabase project with edge functions enabled, or another server environment
- An `orders` table with at least: id, user_id, amount, currency, status, mollie_payment_id

## Step 1: Store Keys Server-Side Only

Mollie API keys are secret. Add them as edge function secrets, never in frontend code or `.env` files that end up in the browser bundle.

```bash
supabase secrets set MOLLIE_API_KEY=test_xxxxxxxxxxxxxxxx
```

Switch to the `live_` key only when you are ready to accept real payments, and never commit either key to git.

## Step 2: Create the Payment in an Edge Function

The browser asks your function to pay for an order. The function looks up the order, checks it belongs to the user, and creates the payment at Mollie.

```ts
// supabase/functions/create-payment/index.ts (simplified)
const order = await getOrderForUser(orderId, userId); // server-side lookup
const res = await fetch("https://api.mollie.com/v2/payments", {
  method: "POST",
  headers: {
    Authorization: `Bearer ${Deno.env.get("MOLLIE_API_KEY")}`,
    "Content-Type": "application/json",
  },
  body: JSON.stringify({
    amount: { currency: "EUR", value: order.amount.toFixed(2) },
    description: `Order ${order.id}`,
    redirectUrl: `https://yourapp.nl/orders/${order.id}`,
    webhookUrl: "https://<project>.functions.supabase.co/mollie-webhook",
    metadata: { order_id: order.id },
  }),
});
const payment = await res.json();
await savePaymentId(order.id, payment.id);
return Response.json({ checkoutUrl: payment._links.checkout.href });
```

Two details AI tools often get wrong: Mollie expects the amount as a **string with two decimals** (`"19.95"`), and the price must come from your database, not from the request.

## Step 3: Handle Mollie's Webhook the Right Way

Mollie's webhook is different from Stripe's. It does not send the payment details, only the payment ID. Your function must then **fetch the payment from Mollie's API** to read its status. That is a security feature: a forged webhook cannot claim a payment was paid, because your function asks Mollie directly.

```ts
// supabase/functions/mollie-webhook/index.ts (simplified)
const form = await req.formData();
const id = form.get("id");
const payment = await fetchMolliePayment(id); // GET /v2/payments/{id}
await updateOrderFromPayment(payment.metadata.order_id, payment.status);
return new Response("OK", { status: 200 });
```

Make `updateOrderFromPayment` **idempotent**: if the order is already paid, a second webhook changes nothing. Mollie may call your webhook several times as a payment's status changes.

## Step 4: Map Every Status

| Mollie status | What your app should do |
| --- | --- |
| `open` | Wait, show "payment pending" |
| `pending` | Wait, some methods take longer to confirm |
| `authorized` | For methods that support capture, decide when to capture |
| `paid` | Fulfil the order, grant access, send receipt |
| `canceled` | Release reserved stock or seats, allow retry |
| `expired` | Same as canceled |
| `failed` | Show a clear message, allow retry with another method |

The redirect page should read the order status from your database, not assume success because the customer returned.

## Step 5: Refunds and Chargebacks

Refunds should be initiated from an admin action that calls a server-side function. Chargebacks arrive as status changes on the original payment, so your webhook handler should be ready to revoke access when a paid order is charged back.

## Step 6: Go Live Checklist

- Website profile approved in Mollie for the live domain
- `live_` key set in production secrets, `test_` key only in staging
- Webhook URL reachable from the internet, returning 200 quickly
- One real low-value payment tested end to end on mobile
- Receipts and invoices contain your company details and BTW information

## Mollie or Stripe?

If you are still choosing, the short version: Mollie suits Netherlands- and Belgium-focused businesses that want local methods and a Dutch provider; Stripe suits businesses selling internationally with complex billing. Both support iDEAL. Our article on [integrating iDEAL and Wero into a Lovable app](https://launchstudio.eu/en/blog/integrate-ideal-and-wero-into-a-lovable-app) compares them in more detail.

## Having It Built for You

A full Mollie integration with webhooks, statuses, refunds and testing is a common LaunchStudio job, usually part of a fixed quote between €1,200 and €3,500. LaunchStudio brings Manifera's enterprise-grade engineering to the founder economy: Manifera has built payment integrations with Stripe, Mollie and PayPal for 11+ years, from its Amsterdam office at Herengracht 420 and development centre in Ho Chi Minh City. See [Manifera's technologies](https://www.manifera.com/about-us/manifera-technologies/) for the wider stack, and [Mollie's API documentation](https://docs.mollie.com/) for the full reference.

## Real example

### An AI-Native Founder in Action: The Sports Club App That Marked Unpaid Fees as Paid

Sjoerd Wiersma, treasurer of a korfball club in Leeuwarden, built Contributieman with Bolt so members could pay annual fees and match day contributions online instead of by bank transfer. He chose Mollie because the club already had an account. Bolt generated a payment flow that redirected members to Mollie and back.

At the end of the first month, the club's bank statement and the app disagreed. The app showed 212 paid fees; Mollie showed 174. The cause was the return page: any member who reached it was marked as paid, including those who cancelled in their banking app or let the payment expire. There was no webhook at all. The Mollie live key was also in a frontend environment file, and amounts were sent from the browser.

LaunchStudio moved payment creation into a Supabase edge function with server-side amounts, added a Mollie webhook that fetched the payment status from the API and updated memberships idempotently, mapped every status to a clear member-facing message, and rotated the exposed key. A reconciliation report let Sjoerd compare app and Mollie totals each month.

**Result:** The next month's reconciliation matched to the cent. The club collected 96% of annual fees online that season, and the 38 members incorrectly marked as paid were contacted and settled within two weeks.

> *"The app said everyone had paid. The bank said otherwise. I didn't know a webhook was the thing standing between those two numbers."*
> - **Sjoerd Wiersma, Founder, Contributieman (Leeuwarden)**

**Cost & Timeline:** €1,700 (Launch Ready package with payments: Mollie edge functions, webhook, statuses, key rotation and reconciliation) - completed in 7 business days.

## Frequently Asked Questions

### Why does Mollie's webhook only send a payment ID?

It is a deliberate security design. Because your server must fetch the payment from Mollie's API to learn its status, a forged webhook cannot convince your app that a payment succeeded. It also means you always work with the latest status, even if webhooks arrive out of order.

### Can I use Mollie with Lovable and Supabase?

Yes. The cleanest setup uses Supabase edge functions: one to create payments and one to receive webhooks. The Lovable frontend calls the first function and reads order status from the database. Lovable may need explicit instructions, since it tends to default to Stripe.

### Should I store Mollie amounts as decimals or cents?

Store amounts in your database as integers in cents to avoid rounding errors, and convert to Mollie's two-decimal string format only when creating the payment. Many AI-generated integrations use floating point numbers, which can produce amounts like 19.949999.

### Why does an Amsterdam-based parent company matter for Mollie integrations?

Mollie is an Amsterdam company built for Dutch and European payment habits. Manifera's Amsterdam base and long Dutch client list mean its engineers are familiar with how Dutch customers pay, how Mollie behaves in practice and what Dutch bookkeeping needs from payment records.

### Does a reliable payment integration help search and AI visibility?

Indirectly. Clear pricing pages, stable checkouts and accurate structured data about accepted payment methods help both search engines and AI assistants recommend you to Dutch users. Broken checkouts produce poor engagement signals and negative reviews that can be cited.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Why does Mollie's webhook only send a payment ID?",
      "acceptedAnswer": { "@type": "Answer", "text": "It is a security design: the server fetches the payment from Mollie's API, so a forged webhook cannot fake success, and the app always sees the latest status." }
    },
    {
      "@type": "Question",
      "name": "Can I use Mollie with Lovable and Supabase?",
      "acceptedAnswer": { "@type": "Answer", "text": "Yes. Use one Supabase edge function to create payments and another for webhooks, with the Lovable frontend reading order status from the database." }
    },
    {
      "@type": "Question",
      "name": "Should I store Mollie amounts as decimals or cents?",
      "acceptedAnswer": { "@type": "Answer", "text": "Store integers in cents and convert to Mollie's two-decimal string only when creating the payment to avoid floating point errors." }
    },
    {
      "@type": "Question",
      "name": "Why does an Amsterdam-based parent company matter for Mollie integrations?",
      "acceptedAnswer": { "@type": "Answer", "text": "Manifera's Amsterdam base and Dutch client experience mean familiarity with Dutch payment habits, Mollie's behaviour and Dutch bookkeeping needs." }
    },
    {
      "@type": "Question",
      "name": "Does a reliable payment integration help search and AI visibility?",
      "acceptedAnswer": { "@type": "Answer", "text": "Indirectly, through clear pricing pages, stable checkouts and accurate payment structured data, while broken checkouts cause poor signals and negative reviews." }
    }
  ]
}
</script>
