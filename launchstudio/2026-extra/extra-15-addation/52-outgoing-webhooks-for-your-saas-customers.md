---
Title: "Outgoing Webhooks for Your SaaS Customers"
Keywords: outgoing webhooks saas, build webhooks for customers, webhook signing hmac, webhook retries ssrf, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: AI-Native Founder (Non-Technical)
---

# Outgoing Webhooks for Your SaaS Customers

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Outgoing Webhooks for Your SaaS Customers",
  "description": "B2B customers increasingly ask SaaS products to notify their systems when something happens, through webhooks. This guide explains how to design and build outgoing webhooks in an AI-built SaaS: event design, payloads, signing, retries, delivery logs, ordering, versioning, protecting your servers from SSRF, endpoint management for customers and when to use a managed webhook service.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-06-08",
  "inLanguage": "en",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/outgoing-webhooks-for-your-saas-customers" },
  "citation": [
    { "@type": "CreativeWork", "name": "Standard Webhooks specification", "url": "https://www.standardwebhooks.com/" },
    { "@type": "CreativeWork", "name": "OWASP Server-Side Request Forgery Prevention Cheat Sheet", "url": "https://cheatsheetseries.owasp.org/cheatsheets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet.html" },
    { "@type": "CreativeWork", "name": "RFC 2104: HMAC", "url": "https://www.rfc-editor.org/rfc/rfc2104" },
    { "@type": "CreativeWork", "name": "Stripe: Webhooks best practices", "url": "https://docs.stripe.com/webhooks" }
  ]
}
</script>

At first, customers are happy to log in to your product and look at their data. As they rely on it more, they want your product to talk to their other systems. When an order is placed, update the ERP. When a form is submitted, create a ticket in the helpdesk. When a payment arrives, notify the accounting system. When a candidate moves to the next stage, inform the HR platform.

The standard way to do this is webhooks: your product sends an HTTP request to a URL the customer provides, describing an event that just happened. You have probably consumed webhooks from Stripe or Mollie. Building your own outgoing webhooks is the other side of the same contract, and doing it well requires more than sending a POST request whenever something changes.

This guide explains how to design and build outgoing webhooks that customers can rely on, and that do not create security risks for your own systems.

## Key Takeaways

- **Webhooks notify customers' systems about events** in your product, enabling integrations without polling your API.
- **Sign every delivery** so customers can verify that it came from you and was not tampered with.
- **Deliver asynchronously with retries,** using a queue, exponential backoff and a delivery log.
- **Protect your infrastructure from server-side request forgery,** because customers choose the destination URLs.
- **Give customers control:** endpoint management, event selection, secret rotation, delivery history and manual replays.

## When Customers Ask for Webhooks

Webhooks become important when:

- Customers integrate your product with their own systems or automation tools
- Data in your product needs to reach other systems quickly, without someone exporting it
- Polling your API repeatedly would be inefficient for both sides
- Partners build integrations on top of your product

If you already offer an API, webhooks complement it. The API lets customers ask for data; webhooks tell them when something changed. Our guide on [offering an API to your SaaS customers](https://launchstudio.eu/en/blog/how-do-i-offer-an-api-to-my-saas-customers) covers the API side.

## Designing Events

Start with a small set of meaningful events, named consistently:

| Event | When it fires |
| --- | --- |
| `order.created` | A new order is placed |
| `order.status_changed` | An order moves to a new status |
| `invoice.paid` | An invoice is marked as paid |
| `contact.updated` | A contact's details change |
| `form.submitted` | A form submission is received |

Principles:

- **Use past-tense, domain-level events,** not low-level database changes. Customers care that an order was created, not that a row was inserted.
- **Fire events after the change is committed,** so customers never receive events for changes that were rolled back.
- **Document every event** with an example payload.

## Payload Design

Each delivery should include:

- **A unique event ID,** so receivers can deduplicate
- **The event type**
- **A timestamp** of when the event occurred
- **The account or workspace** it belongs to
- **The data:** either the relevant object, or a reference to it

There are two styles:

**Fat payloads** include the full object, which is convenient for receivers but means sending potentially sensitive data and handling changes in object structure.

**Thin payloads** include only the event type and object ID, and receivers fetch the details through your API. This is more secure and avoids stale data, but requires an API and an extra request.

Many products use a middle ground: include the key fields needed for common integrations, plus the ID for fetching more. Avoid including data the customer has not configured access to, and never include secrets or authentication tokens.

## Signing Deliveries

Receivers need to verify that a webhook came from your product. The common approach:

1. Generate a secret per endpoint and show it to the customer once.
2. For each delivery, compute an HMAC signature, typically HMAC-SHA256, over the timestamp and the raw request body using the endpoint's secret.
3. Send the signature, timestamp and event ID in headers.
4. Receivers recompute the signature and compare, rejecting deliveries with invalid signatures or timestamps that are too old, which prevents replay attacks.

The Standard Webhooks specification, supported by several companies, describes a consistent format for headers and signatures. Following it makes your webhooks easier for customers to integrate, because they can use existing libraries.

Support **secret rotation:** allow customers to generate a new secret, and for a transition period, sign deliveries with both old and new secrets.

## Asynchronous Delivery With Retries

Never send webhooks inline in the request that caused the event. If the customer's endpoint is slow or down, your user's action would be slow or fail. Instead:

1. **Record the event** in an events table when the change is committed.
2. **Create delivery records** for each subscribed endpoint.
3. **A worker sends deliveries** from a queue.
4. **On failure,** such as a timeout or a non-2xx response, retry with exponential backoff, for example after a minute, five minutes, thirty minutes and several hours, up to a defined maximum.
5. **After repeated failures,** mark the delivery as failed, notify the customer and optionally disable the endpoint after a sustained period of failures.

Use short timeouts, for example ten seconds, so slow endpoints do not tie up workers. Document your retry schedule so customers know what to expect.

## Ordering and Duplicates

Webhooks are typically delivered **at least once,** which means duplicates can occur, for example when a delivery succeeded but the response was lost. Receivers must deduplicate using the event ID. Document this clearly.

Strict ordering is hard to guarantee with retries: an `order.status_changed` event retried later may arrive after a newer one. Include timestamps and, where useful, a version or sequence number per object, so receivers can ignore stale updates. Alternatively, encourage receivers to fetch the current state through your API when they receive an event.

## Protecting Your Servers From SSRF

Outgoing webhooks have a security risk that founders often overlook. Customers choose the URL your servers call. A malicious user could enter an internal address, such as a cloud metadata endpoint, `localhost` or an address in your private network, and use your webhook system to reach systems that should never be exposed. This is server-side request forgery, and OWASP provides detailed guidance on preventing it.

Protections:

- **Require HTTPS URLs** for endpoints.
- **Resolve the hostname and block private, loopback, link-local and metadata IP ranges** before sending, and check again at delivery time, since DNS can change.
- **Do not follow redirects,** or validate redirect targets with the same rules.
- **Send from an isolated worker** with limited network access, ideally without access to internal services.
- **Limit response sizes** and do not expose response bodies from customers' endpoints in ways that could leak information.

## Customer-Facing Endpoint Management

Customers, often their developers, need to manage webhooks themselves:

- **Add, edit and delete endpoints,** with URL validation
- **Choose which events** each endpoint receives
- **View and rotate the signing secret**
- **See delivery history:** event, status, response code, timing and number of attempts
- **Replay** individual deliveries or all failed deliveries in a period
- **Send test events** to verify their integration

Restrict endpoint management to admin roles, and record changes in an audit log. Our guide on [audit logs for B2B SaaS](https://launchstudio.eu/en/blog/audit-logs-for-b2b-saas) explains why.

## Versioning

Once customers build integrations, changing payloads can break them. Plan for change:

- **Add fields freely,** and document that receivers should ignore unknown fields.
- **Never remove or rename fields** without a new version.
- **Version payloads,** for example with an API version setting per endpoint or account.
- **Announce deprecations** well in advance.

## Documentation Customers Need

Webhooks are only as useful as their documentation. Customers' developers, or the automation tools their teams use, need:

- **A list of all events** with descriptions of when each fires
- **Example payloads** for every event, in the current version
- **Headers and signature verification instructions,** with code samples in common languages
- **The retry schedule** and how deduplication by event ID should work
- **Timeout expectations,** such as "respond with a 2xx status within ten seconds and process asynchronously"
- **Ordering guidance,** explaining how to handle out-of-order events
- **Versioning and deprecation policy**
- **How to test,** including sending test events from the dashboard

Good documentation reduces support requests considerably and makes your product look more mature to technical evaluators. Publish it on a public developer page so it can be found before customers sign up.

## Build or Use a Managed Service?

Managed webhook services handle signing, retries, delivery logs, customer portals and SSRF protection, and can be integrated through an API. They save significant development time and are often worth it for products where webhooks are central. Building in-house gives more control and avoids another processor of customer data. Evaluate data location and processing agreements if you choose a managed service, especially for European customers.

For a first version, a well-built in-house system with a queue, signing, retries, logs and SSRF protection is usually achievable within a production launch scope.

## Common Mistakes in AI-Built Apps

**Sending webhooks synchronously** in the request handler, so user actions fail when a customer's endpoint is down.

**No signatures,** so customers cannot verify deliveries.

**No retries,** so a brief outage at the customer's side loses events permanently.

**No SSRF protection,** turning the webhook system into a tool for probing your infrastructure.

**Database triggers calling external URLs directly,** mixing transactional logic with network calls.

**Full objects with sensitive fields in payloads,** sent to endpoints with weak security.

## How LaunchStudio Helps

LaunchStudio builds outgoing webhook systems for AI-built SaaS: event design, events and deliveries tables, queue-based workers with retries and backoff, HMAC signing following common standards, SSRF protection, endpoint management screens with delivery history and replays, audit logging and documentation for customers' developers.

These implementations typically fall within **Launch & Grow** (€2,500-€7,500 plus €49 per month), which includes managed hosting, monitoring and priority support. Use the [price calculator](https://launchstudio.eu/en/#calculator) for an estimate.

LaunchStudio is backed by Manifera, a software development company with 11+ years of experience, 160+ delivered projects and 120+ engineers, with extensive integration experience for enterprise clients. Founders meet the team at Herengracht 420 in Amsterdam; engineering happens at the development centre on Pho Quang Street in Ho Chi Minh City, with a hub on Tras Street in Singapore.

## Real example

### An AI-Native Founder in Action: The Order Platform Whose Webhooks Could Reach Its Own Database

Ilse Vermeer built Groothandelportaal with Cursor and Supabase: a B2B ordering platform for food wholesalers, where restaurants and shops place orders online. Wholesalers wanted orders sent automatically to their warehouse and accounting systems, so Ilse asked Cursor to add webhooks. The agent added a database trigger that called each wholesaler's configured URL directly whenever an order row changed.

Problems appeared quickly. When one wholesaler's warehouse system was slow, order placement slowed for that wholesaler's customers, and when it was down, orders failed with errors. Webhooks had no signatures, so wholesalers could not verify them, and there were no retries, so events sent during outages were lost and orders went missing in warehouses. Payloads contained full order rows, including internal margin fields. A security review found that the URL field accepted any address, including internal ones, which could be used to make the platform's servers send requests into private networks.

LaunchStudio replaced the trigger with an events table written in the same transaction as order changes, and a worker that delivered events from a queue with short timeouts and exponential backoff over 24 hours. Deliveries were signed with HMAC-SHA256 using per-endpoint secrets in a format compatible with the Standard Webhooks specification. Endpoint URLs were validated to require HTTPS and resolved against blocked private and metadata ranges at registration and delivery, with redirects disabled and the worker isolated. Payloads were redesigned to include customer-facing order fields only, and wholesalers received a settings screen with event selection, secret rotation, delivery logs and replay.

**Result:** Order placement became independent of wholesalers' systems, and no events have been lost since the change. Two wholesalers integrated their warehouse systems within a week using the documentation, and the SSRF risk was closed before it was ever exploited.

> *"I thought webhooks were a single line of code. They turned out to be a small product of their own, with security risks I'd never have spotted."*
> - **Ilse Vermeer, Founder, Groothandelportaal (Zwolle)**

**Cost & Timeline:** €5,100 (Launch & Grow package: event model, delivery worker with retries, signing, SSRF protection, endpoint management, payload redesign and documentation) - completed in 13 business days.

## Frequently Asked Questions

### What is the difference between an API and webhooks?

An API lets customers request data from your product when they need it. Webhooks let your product notify customers' systems when something happens. Most integrations use both: webhooks to learn about changes and the API to fetch details or act on them.

### How do customers know a webhook really came from my product?

Sign each delivery with an HMAC signature using a secret unique to the endpoint, and include a timestamp. Customers recompute the signature with their copy of the secret and reject deliveries that do not match or are too old.

### What happens if a customer's endpoint is down?

Deliveries should be retried with increasing delays over a period such as 24 hours. Customers should see failed deliveries in a log and be able to replay them. After sustained failures, notify the customer and consider disabling the endpoint.

### How does Manifera's experience help with webhook systems?

Manifera has built integration platforms for enterprise clients for 11+ years, where reliability and security of data exchange are essential. LaunchStudio applies that experience so webhooks are dependable for customers and safe for your own infrastructure.

### Do webhooks help my SaaS get found and chosen?

Yes, for B2B buyers. Integration capabilities are frequently a selection criterion, and clear developer documentation for webhooks and APIs is the kind of content buyers, search engines and AI answer engines look for when evaluating tools.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What is the difference between an API and webhooks?",
      "acceptedAnswer": { "@type": "Answer", "text": "An API lets customers request data; webhooks notify their systems when something happens. Most integrations use both." }
    },
    {
      "@type": "Question",
      "name": "How do customers know a webhook really came from my product?",
      "acceptedAnswer": { "@type": "Answer", "text": "Sign deliveries with an HMAC signature using a per-endpoint secret and a timestamp; customers recompute and compare." }
    },
    {
      "@type": "Question",
      "name": "What happens if a customer's endpoint is down?",
      "acceptedAnswer": { "@type": "Answer", "text": "Retry with increasing delays, show failures in a log with replay, and notify or disable after sustained failures." }
    },
    {
      "@type": "Question",
      "name": "How does Manifera's experience help with webhook systems?",
      "acceptedAnswer": { "@type": "Answer", "text": "Manifera has built enterprise integration platforms for 11+ years, making webhooks reliable for customers and safe for infrastructure." }
    },
    {
      "@type": "Question",
      "name": "Do webhooks help my SaaS get found and chosen?",
      "acceptedAnswer": { "@type": "Answer", "text": "Yes. Integration capabilities and clear developer documentation are what B2B buyers and AI engines look for." }
    }
  ]
}
</script>
