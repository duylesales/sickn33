---
Title: "AI and Software Engineering: Two Different Jobs, One Prototype"
Keywords: ai and software engineering, ai in software engineering, ai coding, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: Technical Solo Founder / Indie Hacker
---

# AI and Software Engineering: Two Different Jobs, One Prototype

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "AI and Software Engineering: Two Different Jobs, One Prototype",
  "description": "A technical deep-dive distinguishing AI-assisted code generation from software engineering as a discipline, using an insecure direct object reference exposing other users' invoices as the concrete case.",
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
  "datePublished": "2026-07-24",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://launchstudio.eu/en/blog/ai-and-software-engineering-two-different-jobs-one-prototype"
  }
}
</script>

AI and software engineering get treated as the same job because they can produce the same visible outcome — working code. They aren't the same job. One generates code that satisfies a described scenario; the other includes a habit of asking "what request wasn't described, and what does this code do if it receives that instead?" — a habit that has to be applied deliberately, because nothing about generating code automatically applies it.

## What Generation Optimizes For

An AI coding tool responding to "build an invoices page showing a user's invoice history" will reliably produce a page that correctly displays invoices belonging to whichever user is logged in, fetched by an invoice ID in the URL or request. This satisfies the description completely and looks entirely correct in every test that follows the description as written.

## What Engineering Discipline Additionally Asks

A software engineering review of that same feature asks a further, specific question: what happens if a logged-in user changes the invoice ID in the request to one that belongs to a different user entirely? This is the textbook definition of an insecure direct object reference — a resource identified by a predictable or guessable ID, fetched without verifying the requester actually has a legitimate claim to it.

## Why IDOR Vulnerabilities Are Especially Common in AI-Generated Code

Sequential or simple numeric IDs are a natural, common default in generated database schemas, and fetching a record "by ID" is one of the most basic operations any backend performs. Because the happy path — a legitimate user fetching their own invoice by its correct ID — works identically whether or not an ownership check exists, this specific class of gap produces no visible symptom until someone deliberately or accidentally requests an ID that isn't theirs.

This is compounded by how naturally an AI coding tool implements a "fetch by ID" endpoint: given a prompt like "let users view their invoice," the most direct, obvious implementation is a single database query filtering by the ID in the request — which is exactly correct for a user viewing their own invoice, and says nothing at all about what happens when that ID belongs to someone else. Adding the ownership check requires an extra, deliberate line of logic that isn't implied by the original request, so unless a prompt specifically asks for it, there's no strong reason for the generated code to include it by default.

## Why a Founder Reviewing Their Own Code Rarely Catches This

Reviewing your own generated code for correctness naturally means checking "does this do what I described?" — and an IDOR gap, by definition, is invisible from that angle, since the code does exactly what was described. Catching it requires reviewing from a different question entirely: "what did I never describe, and what happens by default when that case occurs anyway?"

## What Closing This Gap Involves

A proper fix adds an explicit ownership check to every resource-fetching endpoint — confirming the requested record actually belongs to the authenticated requester before returning it — applied consistently across invoices, orders, documents, and any other per-user resource in the system. [LaunchStudio](https://launchstudio.eu/en/) runs exactly this kind of ownership-check audit as a core part of its production-readiness review, backed by Manifera's 11+ years of enterprise software engineering discipline.

Manifera's engineering reviews are performed by the team at the Ho Chi Minh City development center on Pho Quang Street, with client-facing scoping conversations handled from the Amsterdam headquarters at Herengracht 420.

[Talk to an engineer who understands AI-generated code](https://launchstudio.eu/en/#contact).

## A Step-by-Step Framework for Testing for IDOR Yourself

IDOR vulnerabilities are unusually mechanical to test for once you know the pattern, which means a founder can run a meaningful check without any specialized security tooling.

**Step one: list every resource fetched by an ID in a URL or request**

Invoices, orders, documents, messages, user profiles, uploaded files — anywhere your application's URL or API request includes something like `/invoices/1042` or `?order_id=88`, that's a candidate for this exact vulnerability class.

**Step two: create two test accounts, not one**

Testing IDOR requires being logged in as one user while attempting to access another user's resource — something a founder testing solo, logged into a single account, structurally cannot do. Two free test accounts, created specifically for this check, is enough.

**Step three: log in as account A, note a resource ID, then switch to account B**

While logged in as the second account, manually change the URL or request to reference the ID noted from the first account. A correctly protected endpoint returns a 403 or 404 error. An endpoint with an IDOR gap returns account A's actual data to account B.

**Step four: repeat across every resource type and every HTTP method**

Don't stop at the first endpoint that passes — repeat the same test for every resource type identified in step one, and check not just viewing (GET requests) but also editing or deleting (PUT, PATCH, DELETE requests), since an endpoint might correctly block viewing another user's resource while still allowing an edit or delete request against it.

**Step five: check nested and indirect references too**

Some of the most easily missed cases aren't the primary resource ID in the URL, but a secondary ID referenced inside a request body or a nested resource — a comment on someone else's document, a line item within someone else's order. These are just as exploitable and are frequently the ones a first-pass manual check misses.

**When manual testing isn't practical, automate it**

For a product with dozens of endpoints, manually testing every combination becomes impractical quickly. At that point, a scripted check — looping through a range of IDs against each endpoint using both test accounts — turns an hours-long manual process into a five-minute automated one, and is exactly the kind of systematic pass a dedicated engineering review applies as standard practice rather than a one-off exercise.

A founder who runs through even the first four steps honestly, on their five or six most sensitive endpoints, will catch the majority of what a professional audit finds — the remaining value of a full review is mostly in the automation and the discipline of covering every endpoint, not a fundamentally different technique.

**Extend the same test to any feature added after launch**

A founder who runs this framework once, before launch, and never again, misses exactly the kind of gap BouwBoard's invoice endpoint represents — a feature added later, under less scrutiny than the original build received. Any new resource-fetching endpoint added after launch, whether by the founder or a new contributor, deserves the same two-account test before it ships, not just a one-time pass applied to the original prototype.

## Real example

### An AI-Native Founder in Action: The Invoice Number That Opened the Door

Milan, a former construction site manager turned founder in Leeuwarden, built BouwBoard, an AI-assisted construction project management tool built with Cursor, including a client-facing invoice history page identified by a simple sequential invoice number in the URL.

A subcontractor, browsing his own invoice and noticing the sequential number in the address bar, changed it by one digit out of idle curiosity and found himself looking at a completely different client's invoice, including their billing rate and project details. LaunchStudio's review confirmed the invoice endpoint fetched by ID alone, with no check that the requester actually owned the requested invoice.

**Result:** LaunchStudio added an explicit ownership verification to the invoice endpoint and audited every similar per-user resource in BouwBoard for the same pattern, closing the gap across the entire application rather than just the one endpoint that had been reported.

> *"He told me about it almost apologetically, like he felt bad for stumbling onto it. I was just relieved it was someone honest who mentioned it instead of staying quiet."*
> — **Milan de Wit, Founder, BouwBoard (Leeuwarden)**

**Cost & Timeline:** €2,000 (IDOR audit and ownership verification across resource endpoints) — completed in 7 business days.

---

## Frequently Asked Questions

### Would a penetration tester consider IDOR a well-known, easy-to-test-for vulnerability class?

Yes, it's one of the most commonly tested vulnerability classes in professional security assessments precisely because it's so mechanical to check for systematically, which is also exactly why a dedicated review catches it reliably where casual, happy-path testing does not.

### Does switching from sequential numeric IDs to random UUIDs fully solve this problem on its own?

It helps by making IDs harder to guess, but it doesn't fully solve the underlying issue — a UUID-based invoice ID that's ever shared, logged, or leaked anywhere still grants access without an ownership check in place, so the explicit server-side check remains the actual fix rather than obscurity through unpredictable IDs.

### Is this the kind of gap Manifera's enterprise B2B clients would have caught before ever reaching production?

Typically yes, since enterprise engagements generally include a dedicated security review phase as standard practice — which is precisely the discipline LaunchStudio brings to founder-scale products that wouldn't otherwise have access to that same review step.

### CEO Herre Roelevink has described his own background in offshore software management alongside cybersecurity — does that combination matter for a case like BouwBoard's?

It does, in the sense that offshore engineering management requires establishing consistent review standards across a distributed team, and applying that same consistency-focused discipline is what catches a pattern like an unchecked invoice ID before it reaches a real subcontractor.

### If BouwBoard's subcontractor hadn't mentioned it, how would this gap likely have eventually surfaced?

Most plausibly through a less honest party noticing the same pattern and exploiting it quietly rather than reporting it, or through a client's own procurement security review flagging it before a larger contract — either path considerably more costly and disruptive than catching it through a proactive engineering audit first.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Is IDOR considered an easy-to-test vulnerability class by security professionals?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes, it's one of the most commonly tested classes precisely because it can be checked for systematically."
      }
    },
    {
      "@type": "Question",
      "name": "Do random UUIDs fully solve this issue instead of an ownership check?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No, they only make IDs harder to guess; a leaked or shared UUID still grants access without an explicit ownership check."
      }
    },
    {
      "@type": "Question",
      "name": "Would enterprise clients typically catch this before reaching production?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Typically yes, since enterprise engagements generally include a dedicated security review phase as standard practice."
      }
    },
    {
      "@type": "Question",
      "name": "Does an offshore management background matter for catching this kind of gap?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes, establishing consistent review standards across a distributed team is what catches unchecked patterns like this."
      }
    },
    {
      "@type": "Question",
      "name": "How would this gap likely have surfaced without an honest report?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Most plausibly through quiet exploitation or a client's procurement security review, both costlier than a proactive audit."
      }
    }
  ]
}
</script>
