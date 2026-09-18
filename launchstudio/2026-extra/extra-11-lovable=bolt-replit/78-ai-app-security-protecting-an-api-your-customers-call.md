---
Title: "AI App Security: Protecting an API Your Customers Call"
Keywords: ai app security, public api, rate limiting, authentication, supabase security, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: Technical Solo Founder / Indie Hacker
---

# AI App Security: Protecting an API Your Customers Call

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "AI App Security: Protecting an API Your Customers Call",
  "description": "An API has no interface to hide behind: every endpoint is reachable, every parameter is editable, and the caller is a program. Authentication, authorisation per object, limits, versioning and what your error messages give away.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-08-19",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/ai-app-security-protecting-an-api-your-customers-call" }
}
</script>

A web application has a certain amount of accidental protection. Most visitors use the buttons that exist, follow the paths the interface offers, and never think about what lies underneath. That protection is thin, and it is real.

An API has none of it. Every endpoint is documented, or discoverable. Every parameter is editable. The caller is a program, so it can make ten thousand requests while you are asleep, and it will find the endpoint you forgot to protect because it is trying all of them.

This is not an argument against offering one. Products that integrate win business that products that do not cannot reach. It is an argument for building it deliberately rather than exposing what already exists.

## Every Endpoint, Not Every Screen

The central shift in thinking.

In a web application it is possible — common, even — for protection to live in the interface. A page not linked anywhere, a button hidden from users without a role, a form that only submits valid combinations. None of that exists in an API. Protection must be in the code that handles the request, on every endpoint, without exception.

The practical consequence: when you publish an API, every endpoint that exists becomes part of it, including the ones your own frontend uses and the ones left over from a feature you removed. Inventory them first. The endpoints nobody remembers are the ones without checks.

## Authentication Before Authorisation, and Both Per Object

Two separate questions, and confusing them is the most damaging API mistake.

**Authentication** asks who is calling. Solved with an API key or a token.

**Authorisation** asks whether this caller may do this, to this specific object. A key identifies a customer; it does not mean that customer may read record 4,182.

The failure is almost universal in generated APIs: an endpoint verifies the key, then fetches whatever identifier the request contains. A valid customer asks for another customer's invoice and receives it, because the code checked that they were somebody rather than that they were the right somebody.

Every endpoint that accepts an identifier must verify that the authenticated caller may access that object. This must be enforced server-side — in the database through policies, or in the query itself — and it should be tested by making that exact request from a second account.

## Limits Are Not Optional

A program calling you does not get tired.

**Rate limits per key,** so one caller's bad loop does not degrade everybody. Return a clear signal — the standard response code and a header saying when to retry — so well-behaved clients back off correctly.

**Pagination, enforced.** An endpoint returning everything is a performance problem and a bulk-extraction tool. Set a maximum page size and apply it even when the caller asks for more.

**Payload limits,** on body size, array lengths and nesting depth. Deeply nested structures can consume disproportionate resources.

**Timeouts and query cost limits,** so one expensive request cannot occupy your database indefinitely.

**Quotas for expensive operations,** particularly anything calling a model provider or generating documents, where the cost per request is real money.

## Validate Everything, Especially What Looks Structural

The caller is not a browser and will not be constrained by your form.

Validate types, ranges, formats and enumerated values on every field, and reject unknown fields rather than ignoring them — that rejection catches both integration bugs and attempts to set fields you did not intend to expose. This last case is worth naming: an update endpoint that accepts a whole object and applies it to a record lets a caller modify any column, including the tenant, the owner, the price or the role. Accept a defined list of fields, always.

## What Your Errors Give Away

Error responses are an information channel, and generated implementations are generous with them.

A message distinguishing "no such record" from "record exists but you may not see it" confirms the existence of other customers' data. A stack trace reveals your framework, your file layout and sometimes your query. A database error quotes your schema. An authentication failure that says whether the account exists helps an attacker enumerate your customers.

Return a generic message and a consistent code to the caller; log the detail on your side, where it belongs and where it is actually useful.

## Versioning, or Every Change Becomes an Incident

Once customers' systems call yours, your API is a contract. Renaming a field breaks somebody's production at a time you did not choose.

Version from the first day, even with a single version. Add fields rather than changing them. When something must change, run both versions for a stated period, tell customers in advance, and use your last-used-per-key data to see who is still on the old one.

This is a security matter as much as a product one, because the alternative — customers who cannot upgrade — leads to old endpoints kept alive indefinitely, unmaintained, and eventually forgotten.

## Documentation Is a Control, Not Just Marketing

Clear documentation reduces support and reduces risk, because integrators who understand your model build correctly.

Document authentication, scopes, rate limits and their headers, error codes and their meanings, pagination, versioning policy, and webhook signature verification. Include a short "how to keep your key safe" note: server-side only, never in a browser or mobile app, rotate on staff changes. Many integration leaks come from a developer at your customer who simply did not know.

## Test It Like Somebody Trying to Get In

Before you publish, and after any significant change.

Call every endpoint without a key. Call it with a valid key belonging to a different customer, requesting the first customer's objects by identifier. Send an update containing fields you do not intend to be settable, including the tenant and the role. Request ten thousand records in one page. Send a malformed body, then an enormous one. Call your rate limit until it triggers, and confirm the response is a clear signal rather than a crash. Read the errors you get back and check they reveal nothing.

Anything that succeeds is a finding. A written note of these checks is also the artefact a business customer's reviewer will want to see.

## Watching Traffic You Cannot See

A web application tells you when something is wrong, because people complain. An API does not. The caller is a program at a company you have never visited, and when it breaks, their developer investigates for two days before anyone contacts you.

**Record per-key metrics.** Requests, errors, response times, and which endpoints. This single view answers most support questions before they are asked and turns "your API is slow" into a conversation about a specific endpoint at a specific hour.

**Alert on shape, not only on failure.** A key that has called you every ten minutes for a year and stops is a broken integration nobody has reported. A key that suddenly makes fifty times its usual volume is a loop, a migration, or a compromise. Both are worth knowing about within the hour rather than at month end.

**Watch error rates per customer, not in aggregate.** One integration failing every request is invisible in a total that includes 33 healthy ones — and it is the customer about to cancel.

**Publish a status page.** Hosted somewhere other than your own infrastructure, so it works during the event it describes. Integrators check a status page before opening a ticket, which saves you the ticket.

**Give them a test environment.** A sandbox with fictional data lets customers build and test without touching production, and removes a category of accident where someone experiments against live records. It also means a new integrator's first week generates no risk at all.

**Watch deprecation uptake.** When you version, your last-used-per-key data tells you exactly who is still on the old version, so a deprecation becomes five targeted emails rather than a broadcast and a hope.

None of this is elaborate. It is the difference between finding out from your own dashboard and finding out from a customer who has already decided you are unreliable.

## Building an API You Can Publish Safely

For a product that already has one, or an internal one about to be exposed, this is bounded work: every endpoint inventoried including forgotten ones, authentication and per-object authorisation enforced server-side on each, field-level validation with unknown fields rejected and mass assignment eliminated, rate limits and quotas per key with standard headers, enforced pagination and payload limits, errors made generic outward and detailed in your logs, versioning introduced with a deprecation policy, documentation written including signature verification, and the whole surface tested adversarially from a second account.

LaunchStudio does this for products whose customers have started asking for integrations. The engineers are Manifera's: eleven years of building APIs that enterprise customers connect to, for clients including Vodafone, TNO and CFLW, from Amsterdam and Ho Chi Minh City.

[Tell us what your API exposes](https://launchstudio.eu/en/#contact) and you will get a specific list, usually within one business day, or see the [packages](https://launchstudio.eu/en/#packages).

## Real example

### A Delivery-Slot API That Answered for Every Webshop

Tim Roozendaal built Bezorgtijd with Lovable: a delivery-slot and route-capacity service used by 34 Dutch webshops around Tilburg and Breda, mostly furniture, garden supplies and appliance retailers. Their shops called his API to show available delivery windows at checkout.

Each webshop had a key. Endpoints verified the key and then used the identifiers in the request. A webshop asking for order 88,412 received it, whoever it belonged to.

A developer at one webshop found it while debugging. He had typed an order number from a paper note into a test request, received an order for a different retailer, and recognised the competitor's name in the delivery address.

Eight business days of work: authorisation added per object on all 23 endpoints — seven of which were internal endpoints his own frontend used and which had become public the moment the API was published, including one that listed every capacity record in the system; the update endpoints changed to accept a defined field list after testing showed a caller could set the owning webshop on an order; rate limits added per key with standard retry headers, after logs showed one integration polling every two seconds around the clock; pagination enforced with a maximum page size, replacing an endpoint that had been returning 40,000 capacity rows; errors made generic outward with detail moved to logs, since responses had been quoting column names; versioning introduced with the existing behaviour frozen as version one; documentation written including key-safety guidance, after two webshops were found to be calling the API from browser JavaScript with the key in the page; and the whole surface tested from a second account.

Those two webshops had effectively published their keys to every visitor of their shops. Both keys were rotated and the integrations moved server-side.

**Result:** the reporting developer's employer expanded to three of its sister companies, and Tim's per-key usage view now catches polling misconfigurations within a day rather than at invoicing.

> *"Seven endpoints my own website used quietly became public the day I published an API, and one of them listed every delivery slot for every retailer I had."*
> — **Tim Roozendaal, Founder, Bezorgtijd (Tilburg)**

**Cost & Timeline:** €4,400 (per-object authorisation across 23 endpoints, field-list updates, rate limiting and pagination, error handling, versioning, documentation, adversarial testing) — completed in 8 business days.

## Frequently Asked Questions

### What is the most common API security flaw?

Checking authentication but not authorisation. The endpoint verifies the key, then trusts the identifier in the request — so a valid customer can fetch another customer's records by changing a number.

### Do my internal endpoints become public when I publish an API?

Effectively yes. Anything reachable is part of your surface, including endpoints your own frontend uses and leftovers from removed features. Inventory them, because the forgotten ones are the ones without checks.

### Why should an update endpoint reject unknown fields?

Because accepting a whole object lets a caller set columns you never intended to expose — the owning customer, the price, a role. Accept a defined list of fields on every write.

### What limits does a public API need?

Rate limits per key with standard retry headers, enforced pagination with a maximum page size, payload and nesting limits, timeouts, and quotas on expensive operations such as model calls or document generation.

### What should error responses contain?

A generic message and a consistent code. Distinguishing "not found" from "not permitted" confirms other customers' data exists, and stack traces or database errors reveal your schema. Keep the detail in your logs.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What is the most common API security flaw?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Authentication without per-object authorisation — the key is verified, then the identifier in the request is trusted, letting one customer fetch another's records."
      }
    },
    {
      "@type": "Question",
      "name": "Do my internal endpoints become public when I publish an API?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Effectively yes. Everything reachable is part of the surface, including frontend endpoints and leftovers from removed features."
      }
    },
    {
      "@type": "Question",
      "name": "Why should an update endpoint reject unknown fields?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Accepting a whole object lets callers set columns you never intended to expose, such as the owning customer, the price or a role."
      }
    },
    {
      "@type": "Question",
      "name": "What limits does a public API need?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Per-key rate limits with retry headers, enforced pagination, payload and nesting limits, timeouts, and quotas on expensive operations."
      }
    },
    {
      "@type": "Question",
      "name": "What should error responses contain?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "A generic message and consistent code. Detailed errors confirm other customers' data exists and reveal your schema; keep detail in logs."
      }
    }
  ]
}
</script>
