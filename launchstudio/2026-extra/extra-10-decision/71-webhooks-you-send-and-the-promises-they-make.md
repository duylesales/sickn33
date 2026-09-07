---
Title: "Webhooks You Send and the Promises They Make"
Keywords: outgoing webhooks design, webhook retry strategy, webhook signature verification, at least once delivery, webhook endpoint failures, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: Technical Solo Founder / Indie Hacker
---

# Webhooks You Send and the Promises They Make

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Webhooks You Send and the Promises They Make",
  "description": "Offering webhooks means committing to deliver events reliably to systems you do not control. What retries, signatures, and ordering guarantees actually require, and why a naive implementation quietly loses events or takes your product down with a customer's slow endpoint.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-04-05",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/webhooks-you-send-and-the-promises-they-make" }
}
</script>

The first customer to ask for webhooks usually frames it as a small thing: send us a request when an order is created, and we will handle the rest. The implementation looks correspondingly small — after saving the order, post the data to their URL. Two lines.

Those two lines make a promise your product cannot keep. They commit you to delivering events to a machine you do not control, which may be slow, offline, misconfigured, or returning errors, and which will occasionally be all four at once. And they attach that unreliable dependency directly to your own order-creation path, so that a customer's broken endpoint becomes your product's failure.

Webhooks are worth offering — for many B2B products they are the difference between being a tool and being part of a workflow. But they are a small piece of distributed-systems work, not a feature you add in an afternoon.

## Never Send From the Request That Caused the Event

The single most important structural decision: the code that creates the order must not be the code that calls the customer's URL.

If it is, three failures follow immediately. A customer endpoint that takes 30 seconds to respond makes your order creation take 30 seconds. An endpoint that is down makes your order creation fail, or leaves it succeeding while the notification vanishes. And a customer with a slow endpoint consumes your server capacity holding connections open, which affects every other customer.

The correct shape is to record the event and hand delivery to a background process. The order is saved, an outgoing delivery is queued, the request returns immediately, and a separate worker attempts the send with retries. Your product's reliability is then independent of every endpoint you deliver to — which is the entire point.

This requires background job infrastructure, which is the real cost of offering webhooks and the reason the feature is not a two-line addition. It is also infrastructure worth having anyway: the same machinery serves imports, exports, bulk operations, and scheduled work.

## Retries, and the Promise You Are Actually Making

Endpoints fail temporarily all the time — a deploy, a restart, a momentary network problem. A single attempt with no retry means those events are lost silently, and the customer discovers days later that their system is missing records.

The standard approach is retry with exponential backoff: try again after a few seconds, then a minute, then several minutes, then hours, over roughly 24 hours, then stop and mark the delivery failed. Add a small random jitter so that a customer coming back online does not receive a thundering burst of simultaneous retries.

Retries mean your delivery guarantee is **at least once**, not exactly once. The same event may arrive twice — because the endpoint processed it but its response was lost, or because a retry raced with a slow success. This is not a defect to be fixed; it is inherent, and every serious webhook provider works this way. What you owe the customer is honesty about it plus the means to cope: a unique event id on every delivery, so the receiver can recognise and ignore a repeat.

Ordering is the other honest limitation. With retries and concurrent delivery, events can arrive out of sequence — an "updated" before its "created". Include a timestamp and a sequence number, tell customers not to assume order, and do not promise strict ordering unless you have built the machinery that guarantees it, which is considerably more work.

## Signatures: How the Receiver Knows It Is You

An endpoint receiving a POST has no idea who sent it. Without verification, anyone who learns the URL can send fabricated events — a fake "payment received", a fake "subscription cancelled" — and the receiving system will act on them.

The standard solution is a signature: a shared secret per customer, used to compute a hash of the request body, sent in a header. The receiver computes the same hash and compares. Include a timestamp in the signed content and reject anything older than a few minutes, so a captured request cannot be replayed later.

Three practical requirements: the secret must be per-endpoint rather than global, it must be rotatable without downtime — which means supporting two valid secrets briefly — and the comparison must be done in a way that does not leak information through timing. None of this is difficult; all of it is routinely absent from generated implementations, which typically send an unsigned POST and consider the feature complete.

There is a matching security concern in the other direction, and it is the one founders miss entirely. Your product will send HTTP requests to URLs that customers supply, which is a capability an attacker can abuse: a customer who registers a webhook pointing at an internal address may be able to make your server reach services that are not publicly accessible. Validating destination URLs — rejecting private address ranges and localhost, resolving hostnames before connecting — is a necessary part of accepting customer-supplied URLs.

Building outgoing webhooks that retry properly, sign correctly, isolate failures, and refuse to be used as a proxy into your own network is a well-defined piece of production engineering. LaunchStudio, backed by Manifera's 11+ years of production engineering, implements event delivery that behaves the way integrators expect. [Describe your project](https://launchstudio.eu/en/#contact) for a review within one business day.

## What the Customer Needs to See

A webhook integration the customer cannot inspect is one they cannot debug, which means every problem becomes your support ticket.

Four things make the difference. **A delivery log**: recent events, the endpoint, the response code, and whether it succeeded, kept for a couple of weeks. **A manual retry button** for failed deliveries, so a customer who fixed their endpoint can replay what they missed without contacting you. **A test event** they can trigger while building. **Notification when an endpoint is failing persistently**, because the common case is a customer whose integration broke weeks ago and who has no idea.

It is also worth disabling an endpoint automatically after sustained failure — several days of every delivery failing — with a clear message. This prevents your queue from filling with deliveries to an address that no longer exists, and it turns an invisible problem into an actionable one.

Payload design deserves one decision, made once. Either send the full object, which is convenient and means the receiver may act on stale data if events arrive out of order, or send an identifier and event type and let the receiver fetch current state, which is always accurate and requires them to make an API call. For most products, sending a useful subset plus the identifier is the pragmatic middle. Whatever you choose, treat the payload shape as a contract: adding fields is safe, removing or renaming them breaks customers silently.

## Real example

### The Slow Endpoint That Took Down Order Creation

Sofie Maes ran Bestelbon, an order-management tool for wholesale food suppliers, built in Cursor. A customer asked for a webhook when an order was placed, and it was added directly to the order-creation handler.

For five months it worked. Then that customer's receiving system was migrated and began responding slowly — 25 to 40 seconds per request, eventually timing out. Because the call was made inline, every order placed by that customer took 30 seconds and then failed, since the handler treated the delivery failure as an error and rolled the whole thing back. Orders were being lost at the busiest point of their week.

Three further problems surfaced. Deliveries were unsigned, so the receiving system had no way to verify origin. There were no retries, meaning any transient failure over five months had silently dropped events — reconciliation later found 61 missing orders in the customer's system. And a second customer had registered a webhook URL pointing at an internal address, which the product had been dutifully attempting to reach.

**Result:** delivery moved to a background queue with exponential backoff over 24 hours, HMAC signatures with per-endpoint rotatable secrets, unique event ids and timestamps on every delivery, a customer-facing delivery log with manual replay, automatic disabling after sustained failure, and destination URL validation. Order creation returned to well under a second regardless of endpoint health.

> "One customer's slow server was making my product fail for that customer, and I had built it that way myself in about ten minutes."
> — **Sofie Maes, Founder, Bestelbon**

**Cost & Timeline:** webhook delivery system rebuilt in 4 business days.

## Frequently Asked Questions

### Can webhooks be sent directly from the code that creates the record?

No. A slow or failing customer endpoint then slows or fails your own operation and consumes server capacity. Record the event and deliver it from a background worker with retries.

### How many times should a failed webhook be retried?

Exponential backoff over roughly 24 hours is the common standard, with jitter to avoid bursts, after which the delivery is marked failed and made available for manual replay.

### Why can the same webhook arrive twice?

Because retries make delivery at-least-once: an endpoint may process an event whose response is lost, prompting another attempt. Include a unique event id so receivers can recognise repeats.

### Do webhooks need to be signed?

Yes. Without a signature the receiver cannot tell a genuine event from a fabricated one sent by anyone who learns the URL. Use a per-endpoint secret, include a timestamp in the signed content, and support rotation.

### Is there a security risk in letting customers supply a URL?

Yes. Your server will make requests to whatever address is given, which can be used to reach internal services. Validate destinations by rejecting private ranges and localhost and resolving hostnames before connecting.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "Can webhooks be sent directly from the code that creates the record?", "acceptedAnswer": { "@type": "Answer", "text": "No. A slow or failing customer endpoint then slows or fails your own operation and consumes server capacity. Record the event and deliver from a background worker with retries." } },
    { "@type": "Question", "name": "How many times should a failed webhook be retried?", "acceptedAnswer": { "@type": "Answer", "text": "Exponential backoff over roughly 24 hours with jitter is the common standard, after which the delivery is marked failed and made available for manual replay." } },
    { "@type": "Question", "name": "Why can the same webhook arrive twice?", "acceptedAnswer": { "@type": "Answer", "text": "Retries make delivery at-least-once: an endpoint may process an event whose response is lost, prompting another attempt. A unique event id lets receivers recognise repeats." } },
    { "@type": "Question", "name": "Do webhooks need to be signed?", "acceptedAnswer": { "@type": "Answer", "text": "Yes. Without a signature the receiver cannot distinguish a genuine event from a fabricated one. Use a per-endpoint secret, sign a timestamp with the body, and support rotation." } },
    { "@type": "Question", "name": "Is there a security risk in letting customers supply a URL?", "acceptedAnswer": { "@type": "Answer", "text": "Yes. Your server will request whatever address is given, which can reach internal services. Validate destinations by rejecting private ranges and localhost and resolving hostnames first." } }
  ]
}
</script>
