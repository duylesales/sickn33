---
Title: "Sendcloud Shipping Integration for AI-Built Webshops"
Keywords: sendcloud integration, shipping labels webshop api, postnl dhl webshop app, lovable webshop shipping, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: AI-Native Founder (Non-Technical)
---

# Sendcloud Shipping Integration for AI-Built Webshops

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Sendcloud Shipping Integration for AI-Built Webshops",
  "description": "Dutch webshops built with Lovable or Bolt often handle shipping manually. This guide explains how to connect an AI-built shop to Sendcloud for labels, carriers such as PostNL and DHL, tracking emails, returns and service points.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-03-29",
  "inLanguage": "en",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/sendcloud-shipping-integration-for-ai-built-webshops" },
  "citation": [
    { "@type": "CreativeWork", "name": "Sendcloud API documentation", "url": "https://api.sendcloud.dev/" },
    { "@type": "CreativeWork", "name": "GDPR Article 28: Processor", "url": "https://gdpr-info.eu/art-28-gdpr/" },
    { "@type": "CreativeWork", "name": "Stripe: Receive events in your webhook endpoint", "url": "https://docs.stripe.com/webhooks" },
    { "@type": "CreativeWork", "name": "Mollie API documentation", "url": "https://docs.mollie.com/" }
  ]
}
</script>

A Dutch webshop built in Lovable can look as good as any Shopify store. Then orders arrive, and the founder copies addresses into a carrier website, prints labels one by one and emails tracking codes by hand. Sendcloud, a shipping platform built in Eindhoven and widely used across Europe, connects your shop to carriers such as PostNL, DHL and DPD through one API. Integrating it turns shipping from an evening job into a few clicks.

## Key Takeaways

- **Manual shipping does not scale:** copying addresses into carrier websites and emailing tracking codes by hand takes hours and causes errors.
- **Sendcloud, a shipping platform from Eindhoven, connects webshops to carriers such as PostNL, DHL and DPD** through one API, with labels, tracking, returns and service points.
- **Create parcels only after verified payment webhooks,** idempotently, so unpaid or duplicate orders never ship.
- **Address quality drives delivery quality:** validate postcodes and house numbers and keep house number additions in a separate field.
- **Shipping data is personal data:** send carriers only what they need and list them in your processor documentation.

## What the Integration Should Do

| Step | Without integration | With Sendcloud |
| --- | --- | --- |
| Order paid | Copy address manually | Order sent to Sendcloud automatically |
| Choose carrier | Visit carrier sites | Shipping rules pick carrier and method |
| Print label | One by one | Batch printing |
| Tracking | Email codes manually | Tracking stored in your app, emails sent automatically |
| Returns | Ad hoc | Return portal and labels |
| Service points | Not offered | Customers choose a pickup point at checkout |

## Architecture

- **Trigger:** your payment webhook marks an order as paid
- **Edge function:** creates a parcel in Sendcloud with address, weight and order reference, using API keys stored as secrets
- **Webhook from Sendcloud:** status updates (label created, in transit, delivered) update the order in your database
- **Customer notifications:** tracking emails from your app or Sendcloud's branded notifications
- **Admin screen:** orders ready to ship, with a link to print labels

## Checkout Options

Offer shipping methods and prices at checkout based on destination and weight. For service point delivery, Sendcloud provides a service point picker; store the chosen point with the order so the label is created correctly.

## Address Quality

Most shipping errors start with addresses. Validate Dutch postcodes and house numbers, separate house number additions (such as 12A or 12-2) into their own field and normalise country codes. A postcode lookup at checkout reduces errors and speeds up ordering.

## Returns

If you accept returns, connect Sendcloud's return portal or create return labels from your admin screen, and link returns to orders and refunds so your stock and bookkeeping stay correct.

## Common Mistakes

- Creating parcels before payment is confirmed, shipping unpaid orders
- Sending the full order including personal notes to the shipping platform
- API keys in frontend code
- No idempotency: a repeated webhook creates two labels
- No handling of address errors returned by the carrier

## Why Shipping Becomes a Bottleneck

Small webshops start by shipping a few parcels a week, and manual work feels fine. Growth changes that quickly: seasonal peaks, promotions and new markets can multiply volume overnight. Every manual step - retyping addresses, choosing carriers, printing labels, emailing tracking codes - takes time and introduces errors. Customers notice errors immediately in the form of late or misdelivered parcels, and Dutch online shoppers have high expectations for fast, reliable delivery. Automating shipping is one of the highest-return investments for a growing webshop.

## How a Shipping Platform Fits In

Shipping platforms sit between your shop and carriers. Instead of integrating with PostNL, DHL and DPD separately, you integrate once with the platform. It handles carrier contracts or connections, label formats, tracking events, service point lookups and returns. Sendcloud's API documentation describes the objects involved: parcels, shipping methods, labels, tracking and returns. Your app's job is to send correct parcel data at the right moment and record what comes back.

## Order Lifecycle With Shipping

| Order status | Trigger | Shipping action |
| --- | --- | --- |
| Pending payment | Checkout started | None |
| Paid | Verified payment webhook | Create parcel with address, weight and method |
| Ready to ship | Parcel created | Label available for printing in batch |
| Shipped | Carrier scan event | Tracking email to customer |
| Delivered | Carrier delivery event | Order complete; optional review request |
| Return requested | Customer via returns portal | Return label, refund flow when received |

Keeping this lifecycle explicit in your database makes support, reporting and automation straightforward.

## Address Validation for the Netherlands and Belgium

Dutch addresses are well structured: postcode, house number and optional addition determine the street and city. A postcode lookup at checkout fills in the street and city automatically, reducing typing and errors. Keep the house number addition, such as "A", "bis" or "2-hoog", in its own field, because carriers' systems depend on it. For Belgian addresses, structures differ slightly; validate per country rather than applying Dutch rules everywhere. Good address data is the single biggest factor in delivery success.

## Service Points and Delivery Options

Many Dutch and Belgian shoppers prefer collecting parcels at a service point near home or work. Offering service points at checkout can increase conversion and reduce failed deliveries. Sendcloud provides a service point picker; store the chosen point with the order and pass it when creating the parcel. Offer delivery options clearly with prices and expected delivery days, and make the cheapest or fastest option obvious depending on your audience.

## Returns Without Chaos

Returns are part of e-commerce. A returns portal lets customers request returns themselves, choose a reason and print a label or show a QR code at a drop-off point. Link returns to the original order in your database, trigger refunds only when the return is received or according to your policy, and update stock. Clear return rules on your website reduce disputes and support load.

## Shipping Data and the GDPR

Carriers and shipping platforms process customers' names, addresses, phone numbers and emails. Send only what they need for delivery and notifications, check the platform's processing terms and data location, and list it in your processing records and privacy statement. Keep tracking data only as long as needed for service and legal purposes.

## Monitoring Fulfilment

Track how long orders take from payment to shipment, how many parcels have address errors, delivery failure rates per carrier and return rates per product. Alert when paid orders remain unshipped beyond your promise, for example 24 hours. These numbers show where to improve and help you keep delivery promises during peaks.

## Building the Integration on Supabase

A typical implementation uses an edge function triggered when an order becomes paid. The function checks whether a parcel already exists for the order, creates it through the Sendcloud API with the address, weight, shipping method and order reference, and stores the parcel ID and label status. A second function receives Sendcloud webhooks for status changes and updates the order. API credentials live in edge function secrets, and an `order_shipments` table, protected by Row Level Security, records parcel IDs, tracking numbers, statuses and errors. An admin screen lists orders ready to ship and any that failed.

## Weights, Dimensions and Shipping Rules

Accurate weights and dimensions determine which shipping methods are available and what they cost. Store weight per product, calculate order weight automatically and include packaging. Shipping rules in Sendcloud can then choose methods based on destination, weight and order value, for example PostNL for domestic parcels, a cheaper method for letterbox-size items and a tracked service above a certain value. Review rules after the first month using real data.

## Peak Season Preparation

Before busy periods such as December or major promotions, check that your integration handles volume: batch label printing works, retries are in place for API errors, carrier cut-off times are reflected in delivery promises and your team knows the process. A dry run with test parcels a few weeks ahead prevents stressful surprises.

## Common Mistakes

- Creating parcels from the checkout page instead of after verified payment
- Merging house number additions into the street field
- Sending full order details, including notes, to carriers
- No idempotency, so repeated webhooks create duplicate labels
- No visibility of failed parcel creation

## Summary

Trigger parcels from verified payments, validate addresses, choose carriers with rules, sync tracking back to orders, handle returns cleanly and monitor fulfilment. Shipping then scales with your shop instead of consuming your evenings.

## Communicating Delivery to Customers

Shipping is part of your product experience. Show delivery options and costs before checkout, give realistic delivery dates that reflect carrier cut-off times, send tracking emails with your branding rather than only the carrier's, and make your returns policy easy to find. Clear communication reduces "where is my order?" emails, which often make up a large share of webshop support requests.

## International Shipping

Shipping to Belgium and Germany is usually straightforward through the same platform, with different carriers and prices. Outside the EU, customs declarations, duties and restrictions apply. Start with the markets your customers are in, configure rules and rates per country and check product restrictions for each destination.

## Questions to Ask Before Integrating

Which carriers do your customers prefer? Do you need service points? What are your volume and peak expectations? How will returns work and who pays for them? How will tracking reach customers? Answering these before building lets you configure the platform and your integration in one pass.

## Where to Start Today

Count how many minutes you spend on shipping per order, multiply by monthly orders and by the value of your time. That number usually makes the case for automation by itself.

## The Payoff

Automated shipping frees hours every week, prevents costly delivery errors and lets your shop handle peaks calmly.

## Related Reading

See our iDEAL and Wero integration guide for the payment side of a Dutch webshop.

## Getting It Built

LaunchStudio integrates Sendcloud with AI-built webshops as part of webshop launches; the webshop range in the price calculator is €1,500-€3,500, with shipping integration commonly included. LaunchStudio is powered by Manifera, which has built e-commerce and logistics systems for clients over 11+ years from Amsterdam and Ho Chi Minh City; see [Manifera's portfolio](https://www.manifera.com/portfolio/). Sendcloud publishes its [API documentation](https://api.sendcloud.dev/) for developers. For payments in the same shop, see our [iDEAL and Wero guide](https://launchstudio.eu/en/blog/integrate-ideal-and-wero-into-a-lovable-app).

## Real example

### An AI-Native Founder in Action: The Candle Maker Who Shipped by Hand

Joyce Lambregts makes scented candles in her workshop in Tilburg and built Kaarsenhuisje in Lovable: a webshop with seasonal collections, gift wrapping options and iDEAL checkout. Around the December holidays, orders jumped to about 60 per day. Joyce spent every evening copying addresses into PostNL's website and emailing tracking codes. Three parcels went to wrong addresses because house number additions were lost.

LaunchStudio connected the shop to Sendcloud: paid orders created parcels automatically with weight from the product data, shipping rules chose PostNL for the Netherlands and DHL for Belgium and Germany, a service point option was added at checkout, postcode lookup with separate house number additions reduced address errors, tracking updates flowed back to orders and customers received branded tracking emails. A returns portal handled the occasional broken candle.

**Result:** Joyce's evening shipping work dropped from three hours to about twenty minutes of batch label printing, and address-related delivery problems disappeared through the rest of the season.

> *"I started a candle business, not a data entry business. December almost turned it into one."*
> - **Joyce Lambregts, Founder, Kaarsenhuisje (Tilburg)**

**Cost & Timeline:** €2,050 (Sendcloud integration, shipping rules, service points, postcode lookup, tracking sync and returns) - completed in 6 business days.

## Frequently Asked Questions

### Can I connect Sendcloud to a webshop built with Lovable?

Yes. Your server, typically a Supabase edge function, creates parcels through Sendcloud's API when orders are paid, and Sendcloud's webhooks report status updates back to your app.

### Which carriers can I use through Sendcloud?

Sendcloud connects to many European carriers, including PostNL, DHL and DPD. Available carriers and rates depend on your country, plan and contracts.

### How do I prevent shipping unpaid orders?

Create parcels only after your payment provider's verified webhook confirms payment, never from the checkout page. Make parcel creation idempotent so repeated events do not create duplicate labels.

### How does Manifera approach e-commerce integrations?

With event-driven flows: payments, shipping and bookkeeping triggered by verified events, with retries and admin visibility. Manifera's 11+ years of e-commerce and logistics work inform this design.

### Does shipping information affect how my shop appears online?

Yes. Clear shipping costs, carriers and delivery times on product and policy pages help customers decide, and give search engines and AI assistants useful facts when shoppers compare shops.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Can I connect Sendcloud to a webshop built with Lovable?",
      "acceptedAnswer": { "@type": "Answer", "text": "Yes, via an edge function creating parcels and webhooks reporting status." }
    },
    {
      "@type": "Question",
      "name": "Which carriers can I use through Sendcloud?",
      "acceptedAnswer": { "@type": "Answer", "text": "Many European carriers including PostNL, DHL and DPD, depending on country, plan and contracts." }
    },
    {
      "@type": "Question",
      "name": "How do I prevent shipping unpaid orders?",
      "acceptedAnswer": { "@type": "Answer", "text": "Create parcels only after verified payment webhooks, idempotently." }
    },
    {
      "@type": "Question",
      "name": "How does Manifera approach e-commerce integrations?",
      "acceptedAnswer": { "@type": "Answer", "text": "Event-driven flows with retries and admin visibility." }
    },
    {
      "@type": "Question",
      "name": "Does shipping information affect how my shop appears online?",
      "acceptedAnswer": { "@type": "Answer", "text": "Yes; clear shipping details help customers and give search and AI assistants useful facts." }
    }
  ]
}
</script>
