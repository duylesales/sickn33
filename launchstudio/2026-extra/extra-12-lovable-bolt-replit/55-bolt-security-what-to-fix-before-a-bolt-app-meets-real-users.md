---
Title: "Bolt Security: What to Fix Before a Bolt App Meets Real Users"
Keywords: bolt security, bolt.new, prototype hardening, exposed keys, authorisation, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: Technical Solo Founder / Indie Hacker
---

# Bolt Security: What to Fix Before a Bolt App Meets Real Users

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Bolt Security: What to Fix Before a Bolt App Meets Real Users",
  "description": "Bolt produces a working application in minutes, optimised for demonstration rather than exposure. The specific gaps its output leaves, in the order they matter, and what a day of hardening covers.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-01-01",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/bolt-security-what-to-fix-before-a-bolt-app-meets-real-users" }
}
</script>

Bolt is exceptional at the thing it is for: describing an application and having a working version exist minutes later, running in a browser, complete enough to show someone.

That output is optimised for demonstration. It has to work immediately, which means every decision that trades speed for safety is made in favour of speed — not carelessly, but because the alternative would produce something that does not run in the first minute.

The gap between a Bolt prototype and an application strangers can use is real, well-defined, and usually a day or two of work. The problem is that nothing about the prototype indicates the gap exists, because it looks finished.

## Where the Credentials Are

Start here, because it is both the most common and the most consequential.

Bolt applications frequently hold API keys in frontend code — a database key, a model API key, a payment key — because that is the shortest path from nothing to a working feature. Everything in that code is downloadable by anyone who opens your site.

Check three places: the code itself, the built output, and the deployed JavaScript on your live site. Search for the provider names and for anything resembling a key.

Anything found there is compromised and must be rotated, not merely moved. And moving it means the operation that used it becomes a server-side function that checks who is asking before doing anything.

## Nobody Is Checking Who You Are

The second gap is authorisation, and it is structural rather than accidental.

A prototype demonstrates a feature to a person who is allowed to use it. There is no second user, so there is no question of whether this user may see this record — and the generated code contains no such check.

Take the systematic approach described elsewhere in this series: two accounts in two organisations, and a walk through every endpoint requesting the other's records. Reading, updating and deleting. In a Bolt application straight from the prototype, expect most of them to succeed.

The fix is to scope every query to the requesting account, and if you are on Supabase, to enable row-level security with policies rather than relying on application code alone.

## Validation Lives in the Browser

Generated forms validate in the interface, which is where the developer can see it working. The server accepts whatever it is sent.

That means required fields can be empty, numbers can be negative, strings can be any length, an email can be anything, a price can be whatever the client says, and a status can be a value your product does not have.

Every endpoint needs its own validation, defined server-side, rejecting anything that does not match. A schema validation library makes this a few lines per endpoint, and it closes a category of problem that ranges from corrupted data to a customer paying one euro for a hundred-euro plan.

## Everything Is Public by Default

Three defaults worth checking specifically in a Bolt application.

Storage buckets, which are typically created public because that made the upload work in the demonstration.

API routes, which frequently have no authentication requirement at all — they were called from the interface and nothing suggested that anyone else might call them.

And the deployed preview itself, which is a public URL that may still exist, containing an earlier version of your application with an earlier set of credentials.

## No Limits Anywhere

A prototype has one user doing reasonable things. A live application has whoever finds it.

Rate limits on authentication endpoints, on anything that sends email or SMS, and on anything that calls a model API. Size limits on uploads and on request bodies. A maximum number of rows an endpoint will return. Timeouts on every external call.

None of these exists in generated output and each of them is the difference between a bad afternoon and a bill or an outage.

## The Order to Fix Things

If you have a day, spend it in this order.

Credentials out of the frontend and rotated. Authorisation on every endpoint. Server-side validation. Storage and route defaults corrected. Rate and size limits. Then sessions, dependencies, logging and everything else in the broader production-readiness list.

The first two account for the overwhelming majority of what actually goes wrong, and they are the two that a prototype is structurally guaranteed to lack.

## What the Prototype Is Still Good For

None of this is an argument against building the prototype in Bolt. It is an argument about what happens next, and the distinction is worth stating because founders sometimes overcorrect into rebuilding from scratch.

The prototype has done something valuable and expensive to reproduce: it has established what the product should do, in a form the customer has seen and agreed to. That knowledge is embedded in the code, the data model and the interface, and throwing it away to start again with a framework you chose carefully is usually a mistake measured in weeks.

The realistic assessment, made by reading the code rather than by reputation: is the structure sound enough to build on? For most Bolt output the answer is yes. The data model is reasonable, the screens are the right screens, the flows are the right flows. What is missing is everything that only matters once other people are involved, and adding it is additive work rather than a rewrite.

The cases where a rebuild is genuinely right are narrower than they feel: a data model that cannot represent what the business actually needs, or an application so tangled that changing one thing reliably breaks another. Both are visible on inspection, and neither is the usual outcome of a weekend of prototyping.

So the sequence that serves most founders: prototype in Bolt, show it, confirm the product is right, then harden the thing you have rather than admiring it and starting over.

## Ask the Agent to Harden It, Carefully

An obvious question: can the tool that built the prototype also fix it? Partly, and the limits are worth knowing before you rely on it.

What works well. Adding server-side validation to an endpoint, when you name the endpoint and state the rules. Moving a specific operation behind a server function. Adding rate limiting to a route. Writing a policy for a table when you describe who should see what. These are contained, well-specified tasks with a great deal of prior art, and the output is usually correct.

What does not work. Asking it to "make this secure", which produces confident changes that address whatever the model associates with the word rather than what your application actually lacks. Asking it to find the problems, which it does inconsistently — it will notice a missing validation and miss the service role key in the frontend, because the key is doing its job.

So the productive division is that you decide what to fix, from a checklist, and the agent does each fix as a named task. That is considerably faster than writing it yourself and it does not require you to trust a judgement the tool is not in a position to make.

One caution specific to this work: verify each change rather than accepting it. A policy that looks right and permits everything, or a validation that runs after the database write, are both plausible-looking output — and both are exactly the kind of defect that the original prototype already demonstrated the tool can produce.

The practical arrangement, then: keep the checklist in the repository so it is available to every session, work through it item by item, and test each result yourself. The tool supplies speed; the list supplies judgement, and the list is the part that has to come from outside the tool.

## Setting This Up

For a Bolt application heading towards real users this is typically one to two days: every credential found in code and bundle, rotated and moved server-side with the operations that used them rewritten as authorised functions; systematic cross-account testing with authorisation added to every endpoint and row-level security enabled where applicable; server-side validation on every input; storage buckets made private with signed access; API routes requiring authentication; old preview deployments retired; rate limits, size limits and timeouts applied; and a short written record of what was checked so the next person knows.

LaunchStudio does exactly this work under the Launch Ready package, from €800, typically in under a week. The engineers are Manifera's — eleven years, 120+ engineers, clients including Vodafone, TNO and CFLW, from Herengracht 420 in Amsterdam.

[Send us your Bolt project](https://launchstudio.eu/en/#contact) and we will tell you what a stranger can currently do with it.

## Real example

### A Demo That Went Live

Quinten Aardema built Leveranciersportaal with Bolt in a weekend: a portal where a food wholesaler's 90 suppliers submit price lists, certificates and delivery schedules.

He built it to show the wholesaler what was possible. They liked it, asked when it could go live, and he answered "next week" — because it worked.

The review before launch found what a weekend prototype contains. The Supabase key in the frontend was the service role key, granting unrestricted database access to anyone who opened the page. None of the 23 endpoints checked which supplier was asking, so any logged-in supplier could read every competitor's price list by changing a number. Certificates uploaded by suppliers went to a public bucket with predictable filenames. Validation was entirely in the browser, so a negative price and a delivery date in 1970 were both accepted. There were no rate limits on anything, and the endpoint that emailed the wholesaler about new submissions could be called repeatedly by anyone who found it.

Two business days: the service role key rotated and removed, with all database access moved behind server-side functions using an anonymous key and policies; row-level security enabled with policies on all nine tables; authorisation added to all 23 endpoints, scoped to the requesting supplier; server-side validation on every input with a schema per endpoint; the certificate bucket made private with generated identifiers and signed URLs; rate limits on authentication, submission and notification endpoints; upload size limits; timeouts on external calls; the original public preview deployment retired, which still held the old credentials; and a one-page record of what was checked.

**Result:** the portal launched a week later than planned with 90 suppliers, and has run for two years. Quinten's view is that the week's delay was the best decision in the project, because a price list leak between competing suppliers would have ended the relationship with the wholesaler immediately.

> *"It worked perfectly. That was the whole problem — there was nothing to see, and any supplier could have read every competitor's prices by changing one number in the address bar."*
> — **Quinten Aardema, Founder, Leveranciersportaal (Venlo)**

**Cost & Timeline:** €2,900 (credential rotation and server-side migration, row-level security, authorisation across 23 endpoints, server-side validation, storage privatisation with signed access, rate and size limits, preview retirement, documentation) — completed in 2 business days.

## Frequently Asked Questions

### Is Bolt insecure?

No more than any prototyping tool. It optimises for producing something that works immediately, which means the checks that matter only when strangers arrive are absent. The gap is predictable and closeable.

### What is the first thing to check?

Where your API keys are. Search the deployed JavaScript on your live site for provider names and key patterns. Anything found there must be rotated, not just moved.

### How do I test authorisation?

Create two accounts in two different organisations, note the record identifiers in one, and request them as the other — for reading, updating and deleting. Anything that returns data is a finding.

### Why is browser validation not enough?

Because the server accepts whatever it is sent, regardless of what the interface allows. Anyone can call your endpoints directly with any values, including prices and statuses.

### How long does hardening a Bolt app take?

One to two days for a typical prototype, in a fixed order: credentials, authorisation, validation, defaults, limits. The first two cover most of what actually goes wrong.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Is Bolt insecure?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No more than any prototyping tool — it optimises for immediate working output, so checks that matter only with real users are absent."
      }
    },
    {
      "@type": "Question",
      "name": "What should I check first in a Bolt app?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Where API keys are. Search the deployed JavaScript for provider names and key patterns; anything found must be rotated."
      }
    },
    {
      "@type": "Question",
      "name": "How do I test authorisation in a prototype?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Two accounts in two organisations: request one's records as the other for read, update and delete. Any data returned is a finding."
      }
    },
    {
      "@type": "Question",
      "name": "Why is browser-side validation insufficient?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "The server accepts whatever it receives. Endpoints can be called directly with any values, including prices and statuses."
      }
    },
    {
      "@type": "Question",
      "name": "How long does it take to harden a Bolt app?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "One to two days: credentials, authorisation, validation, defaults, limits — the first two cover most real risk."
      }
    }
  ]
}
</script>
