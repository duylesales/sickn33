---
Title: "Selling Physical Products From an AI-Built Storefront"
Keywords: AI built webshop production ready, inventory overselling prevention, EU VAT OSS webshop, shipping and fulfilment integration, right of withdrawal returns, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: AI-Native Founder (Non-Technical)
---

# Selling Physical Products From an AI-Built Storefront

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Selling Physical Products From an AI-Built Storefront",
  "description": "A storefront built with an AI tool can take money long before it can run a shop: stock, VAT, shipping, returns and order records are where the real work sits. This article covers what an e-commerce prototype needs before it sells anything physical.",
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
  "datePublished": "2027-01-21",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://launchstudio.eu/en/blog/selling-physical-products-from-an-ai-built-storefront"
  }
}
</script>

Three emails, one Monday morning, all from real customers of a three-week-old shop. *"I ordered two but you only sent one — where is the other?"* *"Can I have an invoice with my company VAT number on it? My accountant needs it."* *"I'd like to return this, what's the address?"* None of these are about the website. All three are about a shop, and the website — beautiful, fast, built in a weekend with an AI tool — had answers for none of them.

That is the specific shape of the e-commerce launch problem. Selling digital access needs authentication and billing. Selling physical goods needs a shop: stock that reflects a real shelf, tax that satisfies four countries, shipping that doesn't eat your margin, returns that comply with EU law, and an order record you can defend six months later. Here's what that means in practice, starting with a question worth asking honestly.

## Should This Be a Custom Storefront at All?

Some products genuinely need a custom shop: configurators where the customer designs the item, B2B accounts with negotiated pricing, subscriptions bundled with physical goods, unusual delivery logic, or a shopping experience that is the marketing. Many products don't, and for those a hosted platform handles tax, shipping, returns and stock for a monthly fee that costs less than a week of engineering.

The honest test: list the parts of your shop that are genuinely different from every other shop. If the list is short, keep your AI-built storefront as the marketing site and let a hosted checkout handle the commerce. If the list is real — and for a lot of founders it is — then build it properly, knowing the following six areas are the actual work. A custom webshop sits at €1,500–€3,500 on the [LaunchStudio calculator](https://launchstudio.eu/en/#calculator), which is a fair price for a real shop and a poor price for a shop you didn't need.

## Stock Is a Promise, and Overselling Breaks It Loudest

An AI-generated storefront typically stores a stock number and decrements it after payment succeeds. Two things go wrong. First, between the customer adding an item and paying, someone else can buy the last one — so you need a short-lived reservation at checkout, released if payment doesn't complete within a set window. Second, decrementing without a database-level guard lets two simultaneous orders both take the last unit, which is the same race condition that causes double bookings and has the same fix: let the database refuse the second write rather than hoping your code checks in time.

Then there's the shelf. Your stock number is a claim about a physical object in a room, and it drifts: breakages, returns that come back damaged, market stall sales, items you gave away. Production means an adjustment mechanism with a reason and a log, not editing a number in a database. It also means deciding your policy for out-of-stock: hide the product, show it as unavailable, or accept backorders with an honest despatch estimate. Each is fine; none of them being implemented is what generates the "where is my second one" email.

## VAT Is Not One Number

For a Dutch shop, VAT starts simple — 21% standard, 9% on certain goods — and stops being simple the moment you ship abroad. Selling to consumers in other EU countries, you charge Dutch VAT until your cross-border sales pass the €10,000 annual threshold, after which you charge the customer's country's rate and report through the One Stop Shop. Selling to a business in another member state with a valid VAT number, you apply reverse charge, which requires validating that number against the EU's VIES service rather than trusting a text field. And consumer prices in the EU must be displayed including VAT, which changes what a German shopper sees on the same product page.

Your invoices need the shop's details, a sequential number, the VAT breakdown and — for reverse charge — the customer's VAT number and a note of the mechanism. A payment provider's tax product can compute most of this. What it cannot do is decide to collect the VAT number at checkout, or store which country the customer was in. Retrofitting that after 300 orders is the kind of task accountants charge daily rates for.

## Shipping That Doesn't Quietly Eat Your Margin

A flat €4.95 shipping rate is a lovely simplification until someone in Portugal orders four items. Real shipping cost depends on weight, dimensions, destination zone and carrier, and your rate table should reflect at least weight and zone. Decide your free-shipping threshold from your average basket and actual carrier costs, not from what looks generous.

Once orders are real, integrate rather than retype: services like Sendcloud or MyParcel connect a shop to PostNL, DHL and others, generate labels, and return tracking codes you can email automatically. That last part is worth more than it sounds — a tracking email prevents the largest single category of customer service messages in any small shop, which is "has it been sent?". If you're not integrating yet, at minimum export orders in a format you can upload to your carrier, because copying addresses by hand is where typos and mis-delivery come from.

## The Payment Can Fail After the Customer Thinks It Worked

European card payments carry a requirement most prototypes never encounter in testing: Strong Customer Authentication. Under PSD2, many card transactions must be verified by the cardholder's bank — the 3-D Secure step where the shopper approves the payment in their banking app. In a test environment with a test card, that step usually passes silently. With a real customer on a real bank, it introduces a pause, a redirect away from your site, and a return trip back. Prototypes routinely mark the order as paid the moment the customer clicks the button, before the bank has actually confirmed anything, which means you can end up with orders recorded as paid that were never authorised, or customers charged for orders your shop never recorded because they closed the tab during the redirect.

The fix is to treat your own site as the least reliable source of payment truth. The authoritative confirmation is the webhook your payment provider sends server-to-server after the bank settles the outcome, and that webhook must be signature-verified and safe to receive twice, since providers retry. Alongside it you need a visible state for orders that are genuinely pending rather than collapsing everything into paid or failed, and a plan for the failure cases that will happen weekly at any real volume: declined cards, abandoned authentication, and the customer who pays twice because the first attempt looked broken. Deciding how each of those resolves — automatically refund, hold for review, or notify you — is a decision you make once, deliberately, rather than improvising during your first busy weekend.

## The Order Record Is Your Source of Truth

Prototypes tend to build an order as a reference to a cart. That breaks the day you change a product's price or name, because historic orders then show today's data and your accounts stop matching your invoices. An order must copy what was bought at the moment of purchase: product name, variant, unit price, VAT rate, discount, shipping cost and totals, frozen.

Around that, you need states rather than a paid boolean: `awaiting payment`, `paid`, `picking`, `partially shipped`, `shipped`, `delivered`, `cancelled`, `returned`, `refunded`. Partial shipments matter as soon as you have more than a couple of products, and a shop that can't record "one of the two went out on Tuesday" forces you into a spreadsheet within a month. Every state change should send the right email and be visible in an admin view you can use from wherever you actually pack orders.

## Returns Are a Legal Right, Not a Policy You Invent

In the EU, consumers buying online generally have fourteen days from receiving the goods to withdraw from the purchase without giving a reason, and a further fourteen days to return them. Once you're notified, you refund within fourteen days, including the standard delivery cost you originally charged. There are exceptions — personalised goods, sealed hygiene products, perishables — and you must inform customers of the right before they buy, which means a clear returns page and a withdrawal form or equivalent.

For the shop itself, this means a return flow with a state, a refund path that works for the payment method used — iDEAL refunds go back through your provider, not by manual bank transfer — and support for partial refunds when one of three items comes back. Add a restocking step that puts the item back into stock only when it's been checked, because returning it automatically on refund is how you sell a damaged product to the next customer.

## The Unglamorous Reliability Layer

Finally, the things that are boring right up until they aren't. Order confirmation emails must actually arrive, which means an authenticated sending domain with SPF, DKIM and DMARC rather than a script sending from your own address. You need a notification when an order comes in, because a missed order is a real business loss and prototypes send confirmations to customers and nothing to the owner. Card details must never touch your server — use your provider's hosted checkout, which keeps the bulk of PCI obligations away from you and gives Dutch customers the iDEAL flow they expect. And your database needs a backup schedule you have tested restoring from, since an order history is not something you can recreate.

None of this is exciting work, which is exactly why AI tools skip it and why roughly 80% of AI-built projects never reach production — the demo is the easy 40% and this is the rest. The engineers doing this work sit inside Manifera, which has been building commerce and logistics systems for enterprise clients for over a decade, and the same patterns apply whether the shop does thirty orders a month or thirty thousand.

If you have a storefront that looks finished and you're not sure whether it can run a shop, the fastest way to find out is to let someone check. [Send us your store URL and we'll tell you what's missing, at no cost](https://launchstudio.eu/en/#contact) — or browse [Manifera's project work](https://www.manifera.com/portfolio/) if you'd like to see the kind of systems the same team builds at a larger scale.

## Real example

### A Shop Owner in Action: The Weekend That Sold Nine of Six

Bram Tielen makes oak serving boards in a workshop outside Tilburg and built Houtzicht's storefront in Bolt after a marketplace took too large a cut. It looked excellent, and a feature in a Dutch interiors newsletter sent 4,000 people to it in two days. He sold nine of a limited run of six, took three German orders including one from a company that wanted a proper invoice, and charged €4.95 shipping on an order to Austria that cost him €18.

The fix took eleven days and was mostly plumbing. Stock moved to a reserved-at-checkout model with a database constraint that makes overselling impossible and a release timer for abandoned checkouts. Orders became immutable records with frozen prices and a full state machine including partial shipment. VAT handling was rebuilt around country rates, the €10,000 OSS threshold and VIES-validated reverse charge for EU business customers, with invoices generated per order. Shipping moved to a weight-and-zone table connected to a carrier integration that prints labels and emails tracking codes. A returns flow with partial refunds and a manual restock check went in alongside.

**Result:** Houtzicht has not oversold since, the three German customers received compliant invoices, and shipping went from an unmeasured loss to a line item Bram can see per order — he raised his threshold for free delivery and gained roughly four euros of margin on every parcel leaving the country.

> *"I could build the shop. I couldn't build the shop's paperwork, and it turns out the paperwork is most of what a shop is. My accountant is now the calmest person I know."*
> — **Bram Tielen, Founder, Houtzicht (Tilburg)**

**Cost & Timeline:** €2,900 fixed price — stock reservation, order records, VAT and invoicing, shipping rates and returns — live in 11 business days.

---

## Frequently Asked Questions

### How does a shop oversell if the stock number is right?

Because checking stock and reducing it are separate steps, so two simultaneous orders can both see the last item as available. The fix is a short reservation held during checkout plus a database-level constraint that refuses the second write, rather than application code trying to check fast enough.

### When do I have to charge another country's VAT rate?

For consumer sales to other EU countries, once your cross-border sales pass the €10,000 annual threshold you charge the destination country's rate and report through the One Stop Shop. For business customers in another member state with a valid VAT number, you apply reverse charge, which means validating that number rather than accepting whatever is typed.

### Can I just refund customers by bank transfer when they return something?

It's possible but it breaks your reconciliation and doesn't work well for iDEAL or card payments, which should be refunded through the original payment provider so the transaction is linked. You also need partial refunds, since customers frequently return one item from a larger order.

### How long do I have to accept a return?

EU consumers generally have fourteen days from receiving the goods to withdraw and a further fourteen days to send them back, with your refund due within fourteen days of being notified and including the standard delivery charge. Some categories such as personalised or sealed hygiene items are excepted, and you must state the terms before purchase.

### Is a custom storefront worth it compared to a hosted platform?

Only if something about your shop is genuinely unusual — a configurator, B2B pricing, bundled subscriptions or unconventional delivery logic. A custom webshop at €1,500–€3,500 is good value when those needs are real and poor value when a hosted checkout behind your existing marketing site would have done the same job.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "How does a shop oversell if the stock number is right?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Because checking stock and reducing it are separate steps, so two simultaneous orders can both see the last item as available. The fix is a short checkout reservation plus a database constraint that refuses the second write."
      }
    },
    {
      "@type": "Question",
      "name": "When do I have to charge another country's VAT rate?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "For EU consumer sales, once cross-border sales pass the €10,000 annual threshold you charge the destination rate and report through the One Stop Shop. For EU business customers with a valid VAT number you apply reverse charge, which requires validating the number."
      }
    },
    {
      "@type": "Question",
      "name": "Can I just refund customers by bank transfer when they return something?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "It breaks reconciliation and works poorly for iDEAL and card payments, which should be refunded through the original provider so the transaction stays linked. You also need partial refunds for customers returning one item from a larger order."
      }
    },
    {
      "@type": "Question",
      "name": "How long do I have to accept a return?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "EU consumers generally have fourteen days from receipt to withdraw and another fourteen to return the goods, with refunds due within fourteen days of notification including standard delivery costs. Personalised and sealed hygiene items are among the exceptions."
      }
    },
    {
      "@type": "Question",
      "name": "Is a custom storefront worth it compared to a hosted platform?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Only when something about your shop is genuinely unusual, such as a configurator, B2B pricing, bundled subscriptions or unconventional delivery logic. Otherwise a hosted checkout behind your existing marketing site does the same job for less."
      }
    }
  ]
}
</script>
