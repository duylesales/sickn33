---
Title: "Giving Customers API Keys Before You Have an API Programme"
Keywords: SaaS API keys implementation, hashing API keys storage, scoped api tokens, versioning a public API, first customer api access, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: Technical Solo Founder / Indie Hacker
---

# Giving Customers API Keys Before You Have an API Programme

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Giving Customers API Keys Before You Have an API Programme",
  "description": "One customer asks for API access and suddenly you are running a public interface with permanent commitments. How to give access without promising more than you can support: key storage, scoping, versioning, and the difference between an internal endpoint and a public one.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-04-07",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/giving-customers-api-keys-before-you-have-an-api-programme" }
}
</script>

A customer asks whether they can pull their data programmatically, and the obvious answer is yes — your product already has endpoints, they already have an account, so it is just a matter of giving them a key. That reasoning is where a lot of small products acquire a permanent obligation they never intended.

The endpoints your frontend uses are not a public API. They were designed for one consumer that you control and deploy alongside them, which means they can change whenever convenient. The moment a customer's script depends on them, they become a contract: change a field name and someone's integration breaks at 3am, and you find out from an angry email. The difference between an internal endpoint and a public one is not technical. It is a promise about stability.

None of which means you should refuse. It means deciding, deliberately, how much you are promising.

## Three Levels of Commitment

It helps to see this as a spectrum rather than a yes or no.

**A private arrangement with one customer.** A key, a couple of endpoints, and an explicit understanding — in writing — that this is unsupported, may change with notice, and exists because you agreed to it specifically. Entirely reasonable, and the right answer for the first request.

**A limited documented API.** A small, deliberately chosen set of endpoints, documented, versioned, and treated as stable. More work, and appropriate when several customers want the same thing.

**A public API programme.** Full surface, published documentation, changelog, deprecation policy, developer support. A product in its own right, with its own maintenance cost, and not something to drift into by accident.

Most founders should start at the first level and move only when demand justifies it. The failure mode is starting at level one technically while behaving as though it is level three — giving a key, saying nothing about stability, and then discovering you can no longer change an endpoint because three customers depend on its exact shape.

## Storing Keys Without Storing a Liability

An API key is a credential, and it must be handled like one. The common implementation stores the key as plain text in a table so it can be displayed in the interface later, which turns your database into a set of ready-to-use credentials for every customer's account.

The correct approach is the same as for passwords: store a hash, never the key itself. Show the key once, at creation, with a clear notice that it will not be shown again. If the customer loses it, they generate a new one. To help them tell keys apart in a list, store a short non-secret prefix — the first several characters — and display that.

Three further requirements. **Prefix your keys identifiably**, so a key that leaks into a public repository can be recognised by automated scanners and by you. **Support multiple keys per account with names**, so a customer can rotate without downtime and revoke one integration without breaking another. **Record last use**, which is what lets both of you identify keys that are no longer needed — and provides the first signal that something is using a key nobody remembers creating.

Revocation must be immediate and total. A revoked key should stop working on the next request, which means not caching validation results for longer than a moment.

## Scope: The Question the Customer Should Be Asked

A key that can do everything the account owner can do is the default in generated implementations and the wrong default in general. A customer who wants to pull yesterday's orders into their warehouse system is being handed the ability to delete their entire account.

Two levels of scoping cover most needs without becoming a permissions project. **Read versus write**, which is a single choice at key creation and eliminates most of the risk, since the majority of integrations only read. And **resource scope**, limiting a key to particular kinds of data, where your product has clearly separable areas.

Beyond that, two rules that are easy to get wrong. A key must never exceed the permissions of the account it belongs to — a member's key granting owner-level access is a privilege escalation, and it happens when key validation is implemented separately from the ordinary permission checks. And every account-scoped rule that applies in your interface must apply to key-authenticated requests too, because API traffic is exactly the path where a missing check goes unnoticed.

## Rate Limits Are for the Customer's Protection as Much as Yours

Scripts do things people do not: run in a loop, retry immediately on failure, and request the same page four hundred times because of a bug in someone's pagination.

Without limits, one customer's badly written integration can degrade your product for everyone, and the customer will not know they are doing it. A per-key limit — a few hundred requests a minute is generous for most business products — protects both sides. Return the standard signal when the limit is hit, a 429 status with a header saying when to try again, and include headers showing remaining quota so a well-written client can pace itself.

Two refinements worth having from the start: a lower limit on expensive operations such as exports or reports, and the ability to raise the limit for a specific customer without a deployment, because the first serious integrator will need more and you do not want that to be an engineering task.

## Versioning, or How to Keep the Right to Change Things

Once a customer's code depends on your response shape, you need a way to change it that does not break them. Deciding this before the first key is issued costs nothing; deciding it afterwards costs a customer relationship.

The simplest workable approach is a version in the path — `/v1/orders` — with a stated rule: within a version, fields may be added but never removed or renamed, and behaviour will not change incompatibly. Anything breaking goes into a new version, with the old one supported for a stated period.

Then apply the rule that makes versioning survivable: **treat adding fields as safe and everything else as breaking.** This means telling customers explicitly that their code must tolerate unknown fields, which most libraries do by default, and it means resisting the temptation to rename something for tidiness.

For a first, private arrangement, a lighter commitment is legitimate: a version prefix in the path, plus a written statement that you will give 30 days' notice of breaking changes. That is honest, cheap, and sufficient — provided you actually have a way to contact the people using each key, which is one more argument for keys being named and attached to an account rather than issued informally.

Setting up key storage, scoping, rate limits, and versioning correctly at the point of the first request is a small, bounded piece of work that prevents an ad-hoc arrangement from becoming an unmanageable obligation. LaunchStudio, backed by Manifera's 11+ years of production engineering, builds customer-facing API access that can be maintained. [Describe your project](https://launchstudio.eu/en/#contact) for a review within one business day.

## Real example

### The Key That Could Delete Everything

Daan Verhoeven ran Voorraadsync, a stock-synchronisation tool for online retailers, built in Lovable. A customer wanted to push stock levels from their warehouse system, so he generated a key, stored it in a table, and checked it against that table on incoming requests.

Eleven months later, four customers held keys. A review before an enterprise deal found several problems at once. Keys were stored in plain text, so anyone with database access held working credentials for four customer accounts. Keys carried no scope: a key intended to update stock levels could delete products, change prices, and remove users. There were no rate limits, and one customer's retry loop had been generating around 40,000 requests an hour for three weeks, which turned out to be the cause of the periodic slowness he had been investigating separately. And two of the four keys had not been used in over six months, belonging to integrations that had been decommissioned without anyone revoking access.

**Result:** keys hashed with a displayed prefix, read and write scoping at creation, named keys with last-use tracking and immediate revocation, per-key rate limits with a lower ceiling on expensive endpoints, and a `/v1` prefix with a written stability commitment. All four existing keys were rotated, and the periodic slowness disappeared.

> "I gave someone a key in about five minutes. It turned out I had also given them the ability to delete their own company's product catalogue, and given myself no way to tell whether anyone was still using it."
> — **Daan Verhoeven, Founder, Voorraadsync**

**Cost & Timeline:** API key management, scoping, and rate limiting delivered in 3 business days.

## Frequently Asked Questions

### Can I just give customers access to the endpoints my frontend uses?

Only with an explicit written understanding that they are unsupported and may change. Internal endpoints are designed to change freely; the moment external code depends on them, that freedom is gone.

### How should API keys be stored?

Hashed, exactly like passwords, with the full key shown once at creation and only a short non-secret prefix stored for identification. Storing keys in plain text turns your database into a set of working credentials.

### Should an API key have the same permissions as the account?

No. Read-only should be the default choice, since most integrations only read. A key must also never exceed the permissions of the user it belongs to, which requires key validation to use the same permission checks as the interface.

### What rate limit is reasonable for a small product?

A few hundred requests per minute per key suits most business products, with a lower limit on expensive operations and the ability to raise it per customer without a deployment. Return a 429 with a retry-after header when exceeded.

### How do I keep the right to change my API later?

Put a version in the path, state that fields may be added but never removed or renamed within a version, and commit to a notice period for breaking changes. Named keys attached to accounts give you a way to contact the people affected.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "Can I just give customers access to the endpoints my frontend uses?", "acceptedAnswer": { "@type": "Answer", "text": "Only with an explicit written understanding that they are unsupported and may change. Once external code depends on internal endpoints, the freedom to change them is gone." } },
    { "@type": "Question", "name": "How should API keys be stored?", "acceptedAnswer": { "@type": "Answer", "text": "Hashed like passwords, shown once at creation, with only a short non-secret prefix stored for identification. Plain-text storage turns the database into working credentials." } },
    { "@type": "Question", "name": "Should an API key have the same permissions as the account?", "acceptedAnswer": { "@type": "Answer", "text": "No. Read-only should be the default since most integrations only read, and a key must never exceed the permissions of the user it belongs to." } },
    { "@type": "Question", "name": "What rate limit is reasonable for a small product?", "acceptedAnswer": { "@type": "Answer", "text": "A few hundred requests per minute per key, with a lower limit on expensive operations and the ability to raise it per customer without a deployment. Return 429 with a retry-after header." } },
    { "@type": "Question", "name": "How do I keep the right to change my API later?", "acceptedAnswer": { "@type": "Answer", "text": "Version the path, state that fields may be added but never removed or renamed within a version, and commit to a notice period for breaking changes." } }
  ]
}
</script>
