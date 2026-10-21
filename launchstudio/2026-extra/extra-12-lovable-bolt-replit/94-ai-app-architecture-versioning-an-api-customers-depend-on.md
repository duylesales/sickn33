---
Title: "AI App Architecture: Versioning an API Customers Depend On"
Keywords: ai app architecture, API versioning, breaking changes, OpenAPI, deprecation policy, API keys, webhooks, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: SaaS Scale-Up
---

# AI App Architecture: Versioning an API Customers Depend On

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "AI App Architecture: Versioning an API Customers Depend On",
  "description": "The moment a customer integrates with your product, your database schema stops being yours to change freely. What counts as a breaking change, how to version and deprecate, design choices that make an API easy to evolve, and the checks that stop a refactor from breaking someone else's business.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-03-19",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/ai-app-architecture-versioning-an-api-customers-depend-on" }
}
</script>

At some point a customer asks whether they can connect their own system to your product. Their ERP should create orders automatically, their planning tool should read your schedules, their data warehouse should pull your figures every night. You say yes, and from that day something changes that most founders do not notice until it breaks: part of your product is now used by software you cannot see, written by people you have never met, running business processes you do not know about.

Every change you make to that part — renaming a field, changing a format, tightening a validation — can stop someone else's business from working. Not with an error on your screen, but with a silent failure in their system that they discover days later.

In AI-built products the risk is larger than usual, because the first "API" is often not designed at all: it is the database itself, exposed through Supabase's automatically generated REST interface. This article covers why that is dangerous, what a deliberate API looks like, what counts as a breaking change, how to version and deprecate, and the checks that keep a refactor from breaking a customer.

## The Accidental API

Supabase generates a REST API for every table in your database. It is how the frontend talks to the data, and it is tempting to hand the same endpoint and a key to a customer who wants to integrate: "Just call `/rest/v1/orders`."

This turns your database schema into a public contract. Every column name, every type, every table becomes something a customer's code depends on. The day you rename `pickup_date` to `pickup_at` in a refactor — perhaps at an AI assistant's suggestion, perhaps for good reasons — every integration that wrote `pickup_date` stops working.

It is also frequently a security problem. To make the integration work, founders hand customers either the anon key — which only works if row level security is perfect for every table — or, worse, the service role key, which bypasses row level security entirely and gives full access to every customer's data. The secrets articles in this series describe what follows.

The fix is a deliberate API layer: a separate set of endpoints, designed for integration, that translates between the outside world and your internal schema. Internally you can rename, restructure and refactor freely. The API changes only when you decide it should, under a policy customers can rely on.

## What Counts as a Breaking Change

The core discipline of API versioning is knowing which changes are safe and which are not.

| Change | Breaking? |
|---|---|
| Adding a new endpoint | No |
| Adding an optional request parameter | No |
| Adding a field to a response | No, if clients ignore unknown fields |
| Adding a new value to an enumeration | Often — clients may not handle it |
| Removing or renaming a field | Yes |
| Changing a field's type or format (string to number, date format) | Yes |
| Making an optional parameter required | Yes |
| Changing a default value or the meaning of a field | Yes, even if the shape is identical |
| Changing error codes or status codes | Yes |
| Tightening validation (shorter maximum length, stricter format) | Yes, for clients that relied on the old limit |
| Changing pagination or sort order | Yes |

Two items deserve emphasis. Changes in meaning are breaking even when nothing visible changes: if `amount` used to include VAT and now excludes it, every integration that reads it is wrong, and no schema check will notice. And new enumeration values break clients that switch on known values — a new order status `on_hold` sends a customer's integration into its error branch. Document enumerations as open, and tell customers to handle unknown values gracefully.

## Choosing a Versioning Scheme

Three schemes are common.

**A version in the URL** — `/v1/orders`, `/v2/orders`. Simple, visible, easy to route and to see in logs. The standard choice for most products.

**A version in a header** — `Accept: application/vnd.example.v2+json` or a custom header. Keeps URLs stable but is invisible in a browser and easy for clients to forget.

**Date-based versions** — each API key is pinned to the version current when it was created, and clients opt in to newer dated versions. Elegant for products with frequent small changes and a large integrator base; considerably more work to implement, because every response must be transformed for every supported version.

For a small or medium B2B product, the practical answer is a major version in the URL combined with a strong commitment to additive change. Within `/v1`, you only make non-breaking changes: new endpoints, new optional parameters, new fields. A `/v2` is introduced only when a breaking change is unavoidable, and that should be rare — once every few years, not every few months.

## Design So You Rarely Need a New Version

Most breaking changes are the consequence of early design choices. A handful of decisions at the start make an API easy to evolve additively.

**Wrap responses in an object.** Return `{ "data": [...], "next_cursor": "..." }` rather than a bare array. A bare array cannot gain pagination or metadata later without breaking every client.

**Use cursor pagination from the start**, as the pagination article in this series describes. Offset pagination is slow at scale and switching later is a breaking change.

**Represent money as integer minor units with a currency** — `{ "amount": 125050, "currency": "EUR" }` — never as a float or a formatted string. Changing representation later is breaking; getting it wrong first is a source of rounding errors forever.

**Use ISO 8601 timestamps in UTC** — `2028-03-19T09:30:00Z` — and dates as `2028-03-19`. Never local formats, never Unix timestamps in some places and strings in others.

**Make identifiers strings**, even if they are UUIDs or numbers internally. It leaves room to change their format.

**Return consistent errors with stable codes** — `{ "error": { "code": "order_not_found", "message": "..." } }` — so clients can branch on the code while you improve the message.

**Accept idempotency keys on creating requests.** A client that retries a `POST /orders` after a timeout must not create two orders. An `Idempotency-Key` header, stored with the result for a day, makes retries safe — the same principle as the payment and accounting integration articles in this series.

**Tell clients to be tolerant readers.** Document that new fields and new enumeration values may appear, and that clients should ignore what they do not understand. This is what makes adding fields non-breaking in practice.

## Specification as the Source of Truth

An API without a written specification is an API whose contract exists only in the code — and in AI-built products, the code changes in ways nobody reviews line by line.

Write the API as an OpenAPI specification: every endpoint, parameter, response field, type and error code. Generate the reference documentation from it, so the documentation is never out of date. Generate client SDKs from it if customers want them. And use it in CI.

The most valuable check is an automated comparison of the specification between the current version and the proposed change. Tools such as `oasdiff` classify every difference as breaking or non-breaking; a pull request that introduces a breaking change to `/v1` fails the build.

```yaml
# CI step
- run: oasdiff breaking origin/main:openapi.yaml openapi.yaml --fail-on ERR
```

Add contract tests: requests against the running API that assert responses match the specification. Between the specification diff and the contract tests, a refactor that renames an internal column cannot silently change what customers receive — the test fails, and the developer adds a mapping in the API layer instead.

This matters doubly when AI assistants write code. An assistant asked to "clean up the order model" will rename fields wherever it finds them; the specification check is what tells it — and you — that one of those places is a promise to someone else.

## Deprecation Without Drama

Sometimes a breaking change is necessary. The difference between a well-run API and a frustrating one is how that change is introduced.

**Announce early.** For a B2B product, six to twelve months between announcing the deprecation of a version or field and removing it is reasonable. Customers' IT departments plan in quarters.

**Signal in the API itself.** Return `Deprecation` and `Sunset` headers on deprecated endpoints, with a link to the migration guide. Integrators who monitor their logs see it without reading your newsletter.

**Know who is affected.** Log API usage per key and per version. Before removing anything, you should be able to list every organisation that called it in the last thirty days — and contact them directly, not only through a changelog nobody reads.

**Write a migration guide.** What changed, why, and exactly what a client must do, with examples of old and new requests.

**Run both versions in parallel** for the deprecation period. Usually `/v1` is implemented as a thin compatibility layer on top of `/v2`, translating old field names and formats, so you maintain one implementation and one translation rather than two codebases.

**Remove on the announced date** — after checking the usage log once more. Extending deadlines indefinitely teaches customers that deprecation notices do not matter.

## Webhooks Are an API Too

Many products send events to customers — "order created", "invoice paid" — through webhooks. Everything above applies to them, and they are often forgotten.

Version the payload, ideally with a version field in every event and the ability for a customer to choose the version per endpoint. Sign every delivery so customers can verify it came from you, using the same pattern the webhook security article in this series describes for incoming webhooks. Retry with backoff when the customer's endpoint fails, record every delivery attempt, and show customers a delivery log with the ability to resend. And never put more personal data in a webhook payload than the customer needs — a reference they can use to fetch details through the authenticated API is often better than the full record.

## Keys, Scopes and Limits

An API used by customers needs access control designed for software rather than people.

**API keys per organisation**, created and revoked by the customer's administrator in the product, shown once at creation and stored as a hash — never retrievable afterwards.

**Scopes per key**, mapped to the permission model described in the roles and permissions article in this series: a key used by a reporting tool needs `orders.read`, not the ability to delete customers.

**Rate limits per key**, returned in response headers so well-behaved clients can pace themselves, with `429` responses and a `Retry-After` header when exceeded.

**Usage visible to the customer** — requests per day, errors, last used — so they can see which integrations are active and spot a key that should not be.

And never, under any circumstances, the service role key. It is not an API key; it is the master key to your database.

## Give Integrators a Place to Test

Customers' developers need somewhere to build their integration that is not their production account. Without one, they test against live data — creating test orders that real hauliers plan, sending test invoices to real debtors — or they ask you to clean up after them.

Three arrangements, from simplest to most complete.

**Test mode keys.** Each organisation can create keys marked as test. Requests with a test key operate on a separate, clearly labelled set of data within the same organisation, never trigger outbound effects such as emails, payments or bookings in accounting packages, and are excluded from billing and reports. This is the model payment providers use, and integrators recognise it.

**A sandbox organisation.** A separate organisation per customer, seeded with realistic sample data as the seed data article in this series describes, with its own keys. Simpler to build than test mode, and adequate for most B2B products.

**A public sandbox environment.** A separate deployment against which anyone can test, reset nightly. Worth it once many third parties — not only customers — build integrations.

Whichever you choose, document the differences explicitly: which side effects are suppressed, how test data is reset, and what rate limits apply. And make the boundary absolute in the code: a test key must never be able to read or write production data, and that is a property to test in CI as carefully as organisation separation.

The payoff is fewer support requests during integration projects, and integrations that arrive in production already working — which, for the customer's IT department, is the difference between a product that is easy to integrate with and one that is not.

## A Changelog Customers Can Read

Integrators want to know what changed without reading code. Keep a dated changelog of every API change — additions as well as deprecations — linked from the documentation and, for significant changes, emailed to the technical contacts of affected organisations. Additions matter too: a customer waiting for a new field learns it has arrived from the changelog, not from a support ticket.

## Setting This Up

For a Lovable or Supabase product opening an API to customers, this is typically four to six days: a deliberate API layer separate from the auto-generated database interface, an OpenAPI specification as the source of truth with generated documentation, a major version in the URL with a commitment to additive change, response envelopes, cursor pagination, money as minor units, UTC timestamps, string identifiers and stable error codes, idempotency keys on creating requests, specification diffing and contract tests in CI to block breaking changes, scoped and hashed API keys per organisation with rate limits and visible usage, usage logging per key and version, a written deprecation policy with headers, migration guides and direct notification, versioned and signed webhooks with a delivery log, and a public changelog.

LaunchStudio builds this when a product's first integration customer is about to depend on it. The engineers are Manifera's — eleven years, 120+ engineers, 160+ projects, from Amsterdam and Ho Chi Minh City.

[Ask us whether your customers are calling your database directly](https://launchstudio.eu/en/#contact).

## Real example

### A Renamed Column and Eleven Hundred Missing Orders

Ruud Schipper built Transportplanner in Lovable: transport order management for regional hauliers, used by 26 haulage companies, several of whose largest shippers sent orders automatically from their own systems.

There was no API layer. Shippers' systems called the Supabase REST endpoints directly, and to make it work quickly each shipper had been given the service role key. During a refactor an AI assistant renamed `pickup_date` to `pickup_at` and `weight` to `weight_kg` across the codebase, including the database. The frontend worked; the shippers' systems did not.

Requests from nine shippers failed with errors their systems logged but nobody watched. For two days, around 1,100 transport orders that should have been planned were never created. Hauliers discovered it when shippers phoned to ask why trucks had not arrived. In the review that followed, the service role keys turned out to give every shipper full read and write access to every haulier's data.

Five business days: the service role key rotated immediately and every shipper given a scoped, hashed API key belonging to its haulier's organisation; a dedicated `/v1` API built as edge functions with an OpenAPI specification, generated documentation, envelopes, cursor pagination, UTC timestamps and stable error codes; idempotency keys on order creation so retries could not duplicate orders; a compatibility layer accepting the old field names for six months, with `Deprecation` and `Sunset` headers and a migration guide; usage logging per key so every shipper still using old fields could be contacted directly; specification diffing and contract tests in CI that fail on any breaking change; signed, versioned webhooks for order status updates with a delivery log; and a changelog.

**Result:** the 1,100 orders were recreated from the shippers' logs within a day, and no data was found to have been accessed across hauliers. In the following year the API went through fourteen releases without a single breaking incident; the CI check blocked three pull requests that would have broken it. Two large shippers integrated through the documented API in about a week each, without a call to Ruud.

> *"The assistant renamed two columns because the new names were clearer. They were — and nine shippers' systems stopped creating orders, and nobody noticed for two days."*
> — **Ruud Schipper, Founder, Transportplanner (Tiel)**

**Cost & Timeline:** €6,200 (service key rotation and scoped API keys, versioned API layer with OpenAPI specification, idempotent order creation, six-month compatibility layer with deprecation headers, per-key usage logging, specification diffing and contract tests, signed versioned webhooks, changelog) — completed in 5 business days.

## Frequently Asked Questions

### Can customers integrate with Supabase's auto-generated REST API?

They can, but it makes your database schema a public contract and usually involves handing out powerful keys. Build a separate API layer that maps to your schema, so internal changes do not break customers.

### What counts as a breaking API change?

Removing or renaming fields, changing types or formats, making parameters required, changing defaults or meaning, changing error codes, tightening validation and changing pagination. Adding endpoints, optional parameters and fields is not breaking.

### Should the version be in the URL or a header?

For most B2B products, a major version in the URL — `/v1` — combined with a commitment to only additive changes within a version. Date-based versioning suits products with many integrators and frequent changes.

### How long should a deprecation period be?

Six to twelve months for B2B customers, with deprecation headers, a migration guide, usage logs to identify affected customers and direct notification before removal.

### How do I stop a refactor from breaking the API?

Keep an OpenAPI specification as the source of truth and run a specification diff and contract tests in CI, so any breaking change fails the build before it is deployed.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Should customers integrate via Supabase's generated REST API?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "It turns the database schema into a public contract and often exposes powerful keys; build a separate API layer instead."
      }
    },
    {
      "@type": "Question",
      "name": "What is a breaking API change?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Removing or renaming fields, changing types, formats, defaults, meaning, error codes, validation or pagination. Additions are not breaking."
      }
    },
    {
      "@type": "Question",
      "name": "Where should an API version be specified?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Usually as a major version in the URL, with only additive changes inside a version; date-based versioning suits large integrator bases."
      }
    },
    {
      "@type": "Question",
      "name": "How long should API deprecation take?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Six to twelve months for B2B, with Deprecation and Sunset headers, a migration guide and direct notification of affected customers."
      }
    },
    {
      "@type": "Question",
      "name": "How can CI prevent breaking API changes?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Diff the OpenAPI specification against main and run contract tests, failing the build on any breaking difference."
      }
    }
  ]
}
</script>
