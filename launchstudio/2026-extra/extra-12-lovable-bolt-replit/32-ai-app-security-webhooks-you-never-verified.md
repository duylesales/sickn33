---
Title: "AI App Security: Webhooks You Never Verified"
Keywords: ai app security, webhook signature verification, replay attacks, idempotency, inbound integrations, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: Technical Solo Founder / Indie Hacker
---

# AI App Security: Webhooks You Never Verified

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "AI App Security: Webhooks You Never Verified",
  "description": "A webhook endpoint is a public URL that changes your data when called. Signature verification, replay protection, why the raw body matters, and the outbound side nobody thinks about.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-11-16",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/ai-app-security-webhooks-you-never-verified" }
}
</script>

Your payment provider needs to tell your application when a subscription is paid. It does this by calling a URL you gave it. That URL is on the public internet, it accepts requests from anyone, and what it does with them is grant access, extend subscriptions and record money.

Put that way, the risk is obvious. In practice it is invisible, because the endpoint was created by an AI session, it worked the first time, and nothing about it looks like an open door.

Anyone who discovers the address — and addresses are discovered — can post a message claiming a payment succeeded. If your handler does not verify who sent it, your product will believe them.

## Verify the Signature, Every Time

Every serious provider signs its webhooks. A header carries a signature computed from the request body and a secret only you and they know. Recomputing it and comparing is how you know the message is genuine.

Three details that generated code routinely gets wrong.

**Use the raw body.** The signature covers the exact bytes sent. If your framework parses the JSON before you see it, and you re-serialise it to verify, the result will differ — key order, whitespace, number formatting — and verification will fail intermittently in ways that are maddening to debug. Capture the raw body for the webhook route specifically.

**Compare in constant time.** A normal string comparison returns as soon as it finds a difference, which leaks information about how much of a guess was correct. Every platform has a timing-safe comparison function; use it.

**Reject on failure, loudly.** A handler that logs a verification failure and processes the message anyway is a handler with no verification. Return an error, record it, and alert if failures suddenly appear — a burst of them is either a provider rotating a secret or somebody probing.

## Replay Is the Second Half

A valid signed message stays valid forever. Someone who captures one — from a log, a proxy, an error report — can send it again.

Two defences, used together. Check the timestamp the provider includes and reject anything older than a few minutes, which bounds the window. And record every event identifier you have processed, refusing duplicates, which also gives you the idempotency that retries require.

That second measure is doing double duty, which is why it is worth building properly: providers retry legitimately, and an endpoint that processes the same event twice will grant two months of access or send two confirmation emails regardless of whether the duplicate was malicious or routine.

## Trust the Event, Verify the Facts

Even a genuine webhook should not be taken entirely at face value.

The safer pattern is to treat the message as a notification that something happened, and then ask the provider's API what the current state is. The webhook says a payment succeeded; your code fetches the payment and confirms the amount, the currency, the customer and the status before granting anything.

This costs one API call and closes a category of problem: out-of-order delivery, events that describe an intermediate state, and any discrepancy between what the message claimed and what actually exists. For anything that grants access or records money, it is worth the round trip.

## Respond Fast, Work Later

Providers expect a quick acknowledgement and will treat a slow response as a failure, retrying — which is how one slow handler becomes four concurrent executions of the same work.

Verify the signature, record the event, return success. Then process it in a background job. Your endpoint responds in milliseconds, retries stop being triggered by your own slowness, and a failure in processing becomes a failed job you can inspect and retry rather than a lost event.

The corollary: never call another external service inside the handler. An email provider having a slow afternoon should not cause your payment webhooks to be retried.

## Do Not Expose More Than the Endpoint

Two smaller hardening measures worth the minutes they take.

Restrict by source where the provider publishes its addresses, as a layer beneath signature verification rather than instead of it. And never make the endpoint reveal anything: a handler returning detailed errors tells a prober exactly what your validation expects, which is a free tutorial in how to construct a request that passes.

Keep the URL unremarkable rather than secret. Secrecy is not a control here — the signature is — but there is no reason to name it in a way that invites attention.

## The Outbound Side Has Its Own Problem

If your product calls webhooks that customers configure, you have built something with a different risk: your server will make an HTTP request to any address a customer types.

That is server-side request forgery. A customer can point a webhook at an internal address and use your application to reach things that are not meant to be reachable from outside — a cloud provider's metadata service, an internal admin panel, a database on a private network.

The protections: resolve the hostname and refuse private, loopback and link-local addresses, checking again after any redirect, since a public hostname can redirect to an internal one. Allow only HTTP and HTTPS. Set a short timeout and a response size limit. And do not return the response body to the customer, because a product that fetches a URL and shows you what it found is a scanner for your own network.

On the sending side, sign your own webhooks so your customers can verify them, include a timestamp and an event identifier, and retry with backoff and a maximum — everything this article asks of your providers.

## Rotating a Webhook Secret Without Downtime

Signing secrets need to change occasionally — after a contractor leaves, after an exposure, or simply on a schedule — and the naive rotation breaks every delivery in the gap between changing it at the provider and deploying the new value.

The arrangement that avoids it: accept two secrets during a transition. Your handler tries the current one, and if that fails, the previous one, treating either as valid. Change the secret at the provider, confirm deliveries are verifying against the new one, then remove the old after a few days.

The same shape works for endpoint changes. Run the new URL alongside the old, move the provider's configuration, watch traffic shift, then retire the old endpoint — rather than switching and hoping.

Two things make rotation easy enough that it actually happens. Keep the secrets in environment configuration rather than in code, so rotating does not require a code change and review. And record, somewhere you will find it, which providers send you webhooks, where each endpoint lives, and when its secret was last changed. Most products cannot answer the first of those, which is why nothing is ever rotated.

The related check: know what happens when verification starts failing at three in the morning because someone rotated a secret in a provider dashboard. If the answer is that events are silently discarded, add the alert now — a burst of verification failures should wake somebody, since it means either an attack or an integration that has just stopped working.

## Testing an Endpoint You Cannot Easily Call

Webhooks are awkward to develop against because the sender is someone else's system, and the shortcuts people take to work around that have a habit of reaching production.

Three tools make it ordinary. Provider CLIs can forward real events to a local machine, which is the closest thing to reality and the right default. A tunnel exposes your local server on a temporary public address when the provider offers no forwarding. And a saved set of captured event payloads, checked into the repository, lets you replay a subscription renewal or a failed payment against your handler in a test without any network at all.

That third one is the valuable one, because it is the only way to cover the events you cannot easily cause: a dispute, a reversed direct debit, a subscription that ends after eleven months. Capture each payload once when it genuinely occurs, strip anything personal, and keep it as a fixture.

The habit to avoid: a temporary switch that skips signature verification in development. It is convenient, it is one environment variable away from production, and it is how an unverified endpoint ships. Verify in every environment, using each environment's own secret, and generate correctly signed test payloads instead of bypassing the check.

## Setting This Up

For an existing product this is typically half a day to a day: signature verification on every inbound webhook using the raw body and a timing-safe comparison, rejection on failure with alerting, timestamp and event identifier checks for replay and idempotency, state confirmed against the provider's API before anything is granted, handlers reduced to verify-record-acknowledge with processing in background jobs, source restriction where published, uninformative error responses, and for outbound webhooks address validation against private ranges with redirect re-checking, timeouts, size limits, signing and bounded retries.

LaunchStudio covers webhooks in security review and in payment work, where unverified handlers are among the most common findings. The engineers are Manifera's — eleven years, 120+ engineers, clients including Vodafone, TNO and CFLW.

[Send us your webhook URL](https://launchstudio.eu/en/#contact) and we will tell you whether it believes us.

## Real example

### The Subscription Nobody Paid For

Lieke Ottenhof built Sportschoolbeheer in Lovable: membership and access management for independent gyms and fitness studios, 54 locations with around 8,000 members.

Member subscriptions were activated by a webhook from her payment provider. The handler read the JSON, found the customer reference and the plan, and updated the membership. It did not check the signature — the AI session that wrote it had not been asked to, and the provider's dashboard showed the deliveries succeeding.

The URL appeared in a public repository for four days, in a configuration file committed by a contractor and removed shortly afterwards. Eleven weeks later, someone posted a crafted message to it activating an annual membership at one location. Over the next month the same source activated 23 memberships across nine locations, each worth between €240 and €580 a year, and several were resold.

A gym owner noticed that a member's payment history was empty while their access was active.

Two business days: signature verification added using the raw request body and a timing-safe comparison, with failures rejected, recorded and alerted; timestamp validation rejecting anything older than five minutes; an events table recording every processed event identifier, making replays and retries harmless; the handler reduced to verify, record and acknowledge, with activation moved into a background job; state confirmed against the provider's API before any membership is granted, so a message claiming a payment now triggers a lookup of that payment; the handler's error responses made uninformative; the 23 fraudulent memberships identified by cross-referencing activations against the provider's payment records and deactivated, with the affected gyms notified; and a reconciliation job comparing active memberships to actual payments, run monthly.

**Result:** roughly €9,000 of annual membership value recovered, and the reconciliation job has since caught two genuine discrepancies caused by failed webhook deliveries rather than fraud. Lieke describes the signature check as four lines of code guarding the entire revenue model.

> *"The provider's dashboard said every delivery succeeded, so I believed the integration was fine. It was fine. It just also accepted messages from everybody else."*
> — **Lieke Ottenhof, Founder, Sportschoolbeheer (Breda)**

**Cost & Timeline:** €2,500 (signature and timestamp verification, event deduplication, handler restructuring with background processing, provider state confirmation, fraudulent membership identification and remediation, monthly reconciliation) — completed in 2 business days.

## Frequently Asked Questions

### Why must webhook signatures use the raw body?

Because the signature covers the exact bytes sent. Re-serialising parsed JSON changes key order, whitespace or number formatting, and verification then fails unpredictably.

### How do I stop someone replaying a captured webhook?

Reject messages whose timestamp is older than a few minutes, and record every processed event identifier so duplicates are ignored. The second also gives you idempotency for legitimate retries.

### Should I trust what the webhook message says?

Use it as a notification and confirm the current state with the provider's API before granting access or recording money. It costs one call and closes several categories of problem.

### Why should webhook handlers return immediately?

Providers treat slow responses as failures and retry, producing concurrent executions of the same work. Verify, record, acknowledge, then process in a background job.

### What is the risk in letting customers configure outbound webhooks?

Server-side request forgery — your server will call any address they supply, including internal ones. Resolve hostnames, refuse private ranges, re-check after redirects, and never return the response body.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Why must webhook signature checks use the raw body?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "The signature covers the exact bytes sent; re-serialising parsed JSON alters formatting and makes verification fail unpredictably."
      }
    },
    {
      "@type": "Question",
      "name": "How do I prevent webhook replay attacks?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Reject messages older than a few minutes by timestamp, and record processed event identifiers so duplicates are ignored."
      }
    },
    {
      "@type": "Question",
      "name": "Should I trust the contents of a webhook message?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Treat it as a notification and confirm the current state through the provider's API before granting access or recording money."
      }
    },
    {
      "@type": "Question",
      "name": "Why should a webhook handler respond immediately?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Slow responses are treated as failures and retried, causing concurrent duplicate processing. Verify, record, acknowledge, then work in the background."
      }
    },
    {
      "@type": "Question",
      "name": "What is the danger of customer-configured outbound webhooks?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Server-side request forgery. Validate resolved addresses against private ranges, re-check after redirects, cap timeouts and size, and never return the response body."
      }
    }
  ]
}
</script>
