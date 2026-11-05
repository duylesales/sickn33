---
Title: "Restaurant Ordering App: From Prototype to Production"
Keywords: restaurant ordering app, bestel app restaurant laten maken, qr ordering netherlands, online ordering without commission, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: AI-Native Founder (Non-Technical)
---

# Restaurant Ordering App: From Prototype to Production

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Restaurant Ordering App: From Prototype to Production",
  "description": "Restaurant owners and hospitality founders are building their own ordering apps with AI tools to avoid platform commissions. This guide explains what production requires: menus with allergen information, pickup, delivery and table ordering flows, time slot capacity, payments with iDEAL and wallets, VAT rates, kitchen workflows, peak-hour performance, refunds and integrations.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-06-29",
  "inLanguage": "en",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/restaurant-ordering-app-from-prototype-to-production" },
  "citation": [
    { "@type": "CreativeWork", "name": "Regulation (EU) No 1169/2011 on food information to consumers", "url": "https://eur-lex.europa.eu/eli/reg/2011/1169/oj" },
    { "@type": "CreativeWork", "name": "NVWA: Allergen information", "url": "https://www.nvwa.nl/onderwerpen/allergenen" },
    { "@type": "CreativeWork", "name": "Belastingdienst: VAT rates", "url": "https://www.belastingdienst.nl/wps/wcm/connect/bldcontenten/belastingdienst/business/vat/vat_in_the_netherlands/calculating_vat/vat_tariffs" },
    { "@type": "CreativeWork", "name": "Mollie: Payment methods", "url": "https://www.mollie.com/payments" }
  ]
}
</script>

Restaurants, takeaways and cafés have a strong reason to want their own ordering app: commissions. Delivery platforms bring customers but take a significant share of each order. A restaurant owner, or a founder who knows hospitality, can now build an ordering system with Lovable or Bolt in a few weeks: menu, cart, checkout, order screen for the kitchen. Some build for their own restaurant, others for a group of local restaurants or as a product sold to many.

The demo always works on a quiet Tuesday afternoon. Production is Friday at 18:30, when forty orders arrive in fifteen minutes, the kitchen is already full, a customer wants to know whether the curry contains peanuts, a payment fails halfway, and a delivery driver is waiting for an order that the system shows as ready but the kitchen has not started.

This guide explains what a restaurant ordering app needs to handle real service. It is general information; check food and tax rules with the relevant authorities and your accountant.

## Key Takeaways

- **Allergen information is a legal requirement** for food sold to consumers in the EU, including non-prepacked food, and must be available before the order.
- **Capacity matters more than features.** Time slots, kitchen capacity and order throttling prevent overloaded evenings.
- **Payments must be confirmed by webhooks,** not by redirects, and orders should only reach the kitchen once payment is confirmed or explicitly set to pay on pickup.
- **VAT rates differ** between food and certain drinks, which affects receipts and reporting.
- **Peak-hour reliability** requires efficient queries, realtime updates that scale and tested failure handling.

## Typical Ordering Flows

| Flow | How it works | Key requirements |
| --- | --- | --- |
| Pickup | Customer orders online, chooses a time, collects | Time slots, preparation time, ready notifications |
| Delivery | Customer orders for delivery to an address | Delivery zones, minimum order, fees, driver handover |
| Table ordering | Guest scans a QR code at the table and orders | Table identification, adding to an open bill, pay now or later |
| Pre-orders and catering | Orders days in advance, larger quantities | Lead times, deposits, special requests |

Most restaurants start with pickup and delivery; table ordering adds complexity around open bills and service staff.

## Menus and Allergen Information

EU rules on food information to consumers require that information on certain allergens is available for food sold to consumers, including food that is not prepacked, such as restaurant dishes. The Dutch food authority, the NVWA, provides guidance on how this applies to restaurants and online ordering. For an ordering app, practical requirements include:

- **Allergen data per dish,** for the regulated allergens, maintained by the restaurant
- **Visibility before ordering,** not only after checkout
- **Modifiers and options** that change allergens, such as sauces or toppings, reflected correctly
- **Clear wording** and an option for customers to contact the restaurant with questions
- **Change history,** so the restaurant can show what information was displayed when

The restaurant remains responsible for the accuracy of its information, but your app must make it easy to maintain and display correctly.

Menus also need availability rules: dishes sold out tonight, items only available at lunch, seasonal specials and options with extra prices.

## Time Slots and Kitchen Capacity

The most common operational failure is accepting more orders than the kitchen can produce. Design capacity into ordering:

- **Time slots** for pickup and delivery, each with a maximum number of orders or items
- **Preparation time** per dish category, used to calculate earliest available slots
- **Dynamic throttling,** letting staff pause new orders or extend preparation times during rush periods
- **Capacity enforced in the database,** so two customers cannot both take the last place in a slot. Our guide on [preventing double bookings](https://launchstudio.eu/en/blog/preventing-double-bookings-in-a-booking-app) explains the transactional patterns, which apply equally to order slots.

## Payments

Online ordering in the Netherlands typically needs iDEAL, cards and wallets such as Apple Pay and Google Pay, through a provider such as Mollie or Stripe.

Essential rules:

- **Calculate totals on the server** from menu prices, options, delivery fees and discounts. Never trust a total sent from the browser.
- **Send orders to the kitchen only after payment confirmation** through a verified webhook, or mark them clearly as unpaid when pay-at-pickup is allowed.
- **Handle failed and abandoned payments** by releasing the time slot after a short period.
- **Process webhooks idempotently,** so a retried webhook does not print the same order twice.
- **Support refunds,** full and partial, for cancelled items or late deliveries, with clear records.

For tipping, decide how tips are recorded and distributed, and keep them separate from revenue in reporting.

## VAT on Food and Drinks

In the Netherlands, food and most non-alcoholic drinks typically fall under the reduced VAT rate, while alcoholic drinks fall under the standard rate. An ordering app should:

- **Assign VAT rates per product,** maintained by the restaurant
- **Show prices including VAT** to consumers
- **Calculate VAT per rate** on receipts and in reports
- **Handle delivery fees** with the VAT treatment the restaurant's accountant advises

Check current rates and rules with the Belastingdienst or an accountant, as they can change.

## Kitchen and Service Workflow

The customer-facing side gets the attention, but the kitchen side determines whether service runs smoothly:

- **Kitchen display or printer integration,** showing new orders immediately, grouped by preparation station if needed
- **Order status steps:** received, in preparation, ready, picked up or out for delivery
- **Realtime updates** to staff screens and customer order pages, designed to scale during peaks
- **Sound and visual alerts** for new orders that staff cannot miss in a noisy kitchen
- **Manual override** for staff to adjust times, mark items unavailable and contact customers

Test with actual kitchen staff during a real service before going live.

## Peak-Hour Performance

Ordering traffic is spiky: lunch, dinner, Friday and Saturday evenings, holidays and sports events. Common performance problems in AI-built ordering apps:

- Menus loaded with all items, images and options in one heavy request
- Unoptimised images from phones, several megabytes each
- Availability calculations running full table scans
- Realtime subscriptions on whole tables
- Order confirmation emails sent synchronously, slowing checkout

Cache menus, optimise images, index availability queries, scope realtime subscriptions and send emails from background jobs. A load test before a big promotion is worthwhile, as described in our guide on [load testing an AI-built app](https://launchstudio.eu/en/blog/load-testing-an-ai-built-app-before-launch).

## Customer Data and Marketing

Ordering apps collect names, phone numbers, addresses and order history. Use them carefully:

- **Collect what the order needs,** such as a phone number for pickup and an address for delivery.
- **Ask for marketing consent separately** and record it.
- **Offer guest checkout** if possible, which many customers prefer.
- **Define retention** for order data and delete or anonymise old customer data.

## Delivery Specifics

Delivery adds its own requirements on top of pickup:

- **Delivery zones** defined by postcode ranges or a radius, with different fees or minimum order values per zone
- **Address validation,** ideally with postcode and house number lookup, to reduce failed deliveries
- **Delivery time estimates** combining preparation time, driver availability and distance
- **Driver handover,** with a screen or printout listing orders, addresses, phone numbers and payment status
- **Status updates** to customers when the order leaves the restaurant
- **Failed delivery handling,** such as customers not answering the door, with a clear policy

If drivers are employees or contracted couriers, give them access only to the orders they deliver and only for as long as needed. Customer addresses and phone numbers are personal data and should not remain visible on drivers' devices after delivery.

## Table Ordering

QR-based table ordering is popular in cafés and casual restaurants, and it brings additional considerations. Each table needs a unique, hard-to-guess code, so guests cannot place orders on other tables. Orders should be added to an open bill for the table, which several guests can contribute to and pay together or separately. Staff need to see which tables have open bills, mark items served and close the bill, sometimes with payment at the counter. Clearly distinguish orders paid immediately from orders added to a bill, so the kitchen and staff know what has been paid.

## Multi-Restaurant Platforms

If you build for several restaurants, add:

- **Data isolation per restaurant** with Row Level Security
- **Payments to each restaurant,** through a platform product such as Mollie Connect or Stripe Connect, with your fee
- **Restaurant onboarding** with menus, allergens, opening hours and payment setup
- **Reporting per restaurant** and for your platform

## Reporting for Restaurant Owners

Owners want simple answers: how much did we sell, which dishes sell best, how many orders per hour, how much was refunded and what do we owe in VAT? A daily and weekly report with revenue per channel, VAT per rate, refunds, tips and popular items covers most needs, along with an export for the accountant. Base reports on confirmed payments and local business days in the Amsterdam time zone, so late-night orders are counted on the right day.

## Launch Checklist

| Area | Check |
| --- | --- |
| Menu | Allergen data complete, options and availability correct |
| Capacity | Slots and preparation times configured, throttling available |
| Payments | Webhook-confirmed orders, refunds tested, wallets enabled |
| VAT | Rates per product correct, receipts show VAT per rate |
| Kitchen | Display or printer tested during service, alerts audible |
| Performance | Images optimised, menu cached, peak test done |
| Privacy | Consent for marketing, retention defined |
| Support | Staff know how to pause orders and contact customers |

## How LaunchStudio Helps

LaunchStudio takes restaurant ordering apps from prototype to production: allergen and menu data models, capacity-aware time slots enforced in the database, payment integration with iDEAL and wallets confirmed by webhooks, VAT per product, kitchen workflows with realtime updates, performance optimisation for peaks, multi-restaurant data isolation and platform payments.

Ordering platforms typically fall within **Launch & Grow** (€2,500-€7,500 plus €49 per month), which includes payments, managed hosting, monitoring and priority support. Use the [price calculator](https://launchstudio.eu/en/#calculator) for an estimate.

LaunchStudio is backed by Manifera, a software development company with 11+ years of experience, 160+ delivered projects and 120+ engineers, including transaction-heavy systems for clients in Europe and Asia. Founders meet the team at Herengracht 420 in Amsterdam; engineering happens at the development centre on Pho Quang Street in Ho Chi Minh City, with a hub on Tras Street in Singapore.

## Real example

### An AI-Native Founder in Action: The Friday Night That Nearly Ended the Pilot

Dewi Sutanto runs an Indonesian restaurant in Rotterdam and built Pesanan with Lovable and Supabase to take pickup and delivery orders without paying platform commissions. After three quiet weeks of testing, she promoted it on social media. On the following Friday evening, 63 orders arrived in about forty minutes, almost all for pickup between 18:00 and 19:00.

The kitchen could not keep up. There were no time slots, so every customer chose "as soon as possible", and orders appeared on the kitchen tablet as soon as checkout started, including several where payment later failed. Two customers received orders containing peanuts because the allergen field was free text that some dishes left empty and the satay sauce option added peanuts without updating the information. Duplicate orders printed when Mollie retried webhooks, and menu photos of several megabytes made the app slow on mobile networks.

LaunchStudio introduced pickup and delivery slots with capacity per fifteen minutes, enforced in a database function, and preparation times per dish category, with a "pause orders" button for staff. Orders reached the kitchen only after a verified Mollie webhook confirmed payment, processed idempotently, and unpaid orders released their slot after ten minutes. Allergens became structured data per dish and option, shown before adding to the cart, with a change history. Menu images were compressed and cached, VAT rates were set per product for food and alcoholic drinks, and realtime updates to the kitchen display were scoped to open orders.

**Result:** The next Friday promotion brought 81 orders, spread across slots the kitchen could handle, with no failed-payment orders reaching the kitchen and no duplicates. Dewi now saves the platform commission on most of her takeaway revenue, and two neighbouring restaurants have asked to use Pesanan.

> *"The app worked perfectly until it worked too well. Now it tells customers when we can actually cook their food."*
> - **Dewi Sutanto, Founder, Pesanan (Rotterdam)**

**Cost & Timeline:** €4,800 (Launch & Grow package: capacity slots, webhook-confirmed orders, structured allergens, VAT per product, image optimisation and kitchen realtime updates) - completed in 12 business days.

## Frequently Asked Questions

### Do I have to show allergen information in my ordering app?

Yes, for food sold to consumers in the EU, information on regulated allergens must be available, including for non-prepacked food such as restaurant dishes, and it should be available before the order is placed. The restaurant is responsible for accuracy; the app should make it easy to maintain and display.

### How do I stop my kitchen from being overwhelmed by online orders?

Use time slots with capacity limits, preparation times per dish category and a way for staff to pause orders or extend times during rush periods. Enforce slot capacity in the database so concurrent orders cannot exceed it.

### When should an order be sent to the kitchen?

After payment is confirmed through a verified webhook from your payment provider, or immediately if the restaurant explicitly allows pay on pickup and the order is marked as unpaid. Never rely on the customer's redirect after payment as confirmation.

### How does Manifera's experience help with ordering systems?

Manifera has built transaction-heavy systems for clients for 11+ years, where peak loads, payments and capacity must work together. LaunchStudio applies that experience to restaurant ordering, so busy evenings run smoothly for customers and kitchens.

### Does my own ordering app help my restaurant's visibility?

It can. An ordering page on your own domain, with structured menu information, opening hours and location, helps search engines and AI answer engines show your restaurant directly to customers, rather than only through delivery platforms.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Do I have to show allergen information in my ordering app?",
      "acceptedAnswer": { "@type": "Answer", "text": "Yes; EU rules require regulated allergen information for food sold to consumers, available before ordering." }
    },
    {
      "@type": "Question",
      "name": "How do I stop my kitchen from being overwhelmed by online orders?",
      "acceptedAnswer": { "@type": "Answer", "text": "Use time slots with capacity limits enforced in the database, preparation times and a staff pause button." }
    },
    {
      "@type": "Question",
      "name": "When should an order be sent to the kitchen?",
      "acceptedAnswer": { "@type": "Answer", "text": "After webhook-confirmed payment, or immediately if marked unpaid for pay on pickup." }
    },
    {
      "@type": "Question",
      "name": "How does Manifera's experience help with ordering systems?",
      "acceptedAnswer": { "@type": "Answer", "text": "Manifera has built transaction-heavy systems for 11+ years, making peaks, payments and capacity work together." }
    },
    {
      "@type": "Question",
      "name": "Does my own ordering app help my restaurant's visibility?",
      "acceptedAnswer": { "@type": "Answer", "text": "It can; structured menu, hours and location on your own domain help search and AI engines show your restaurant." }
    }
  ]
}
</script>
