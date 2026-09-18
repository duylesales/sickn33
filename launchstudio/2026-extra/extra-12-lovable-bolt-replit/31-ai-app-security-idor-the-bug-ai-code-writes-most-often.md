---
Title: "AI App Security: IDOR, the Bug AI Code Writes Most Often"
Keywords: ai app security, IDOR, broken access control, authorisation checks, object ownership, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: Technical Solo Founder / Indie Hacker
---

# AI App Security: IDOR, the Bug AI Code Writes Most Often

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "AI App Security: IDOR, the Bug AI Code Writes Most Often",
  "description": "Change the number in the URL and you see someone else's record. Why AI-generated endpoints omit ownership checks, how to find every one in an afternoon, and the pattern that stops it recurring.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-11-14",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/ai-app-security-idor-the-bug-ai-code-writes-most-often" }
}
</script>

Open a record in your own product and look at the address bar. There is an identifier in it. Change it to a different one and reload.

If you see somebody else's data, you have an insecure direct object reference — and if you are running an application built largely by AI tools, the odds are meaningfully better than even. In security reviews of Lovable, Bolt and Cursor-built products, this is the most frequently found serious flaw, ahead of exposed keys and public storage buckets.

It is also the easiest to exploit. No tools, no skill, no knowledge of security. A curious customer with a browser finds it by accident, and some of them will look further before telling you.

## Why Generated Code Does This

Ask a tool to build a page showing an invoice and it writes exactly that: take the identifier, fetch the invoice, render it. The request is satisfied. The code is correct in the sense of doing what it was asked.

Nobody asked "and verify that the person requesting it is entitled to see it", so nobody wrote it. Authorisation is not a feature; it is an absence, and absences are precisely what a request-driven tool does not produce.

It compounds. Once one endpoint follows the pattern, later sessions imitate it, and the twentieth endpoint has the same shape as the first because consistency is what the model is good at. So the flaw is rarely in one place — it is a property of the whole application.

## Authentication Is Not Authorisation

The common misunderstanding: "my endpoints require login, so they are protected".

Authentication answers who you are. Authorisation answers whether you may do this to this thing. A logged-in user is still a stranger to every record that is not theirs, and an application that checks only the first has made every customer an administrator of everyone else's data.

The check that is missing is always the same shape: does the object identified in this request belong to the account making it?

## Finding Every One in an Afternoon

This is mechanical rather than clever.

List every endpoint and page that takes an identifier — a record id, a document reference, a file path, a slug, anything that names a specific thing. In a typical AI-built product this is thirty to sixty locations.

Create two accounts in two different organisations. In the first, note the identifiers of a handful of records. Then, signed in as the second, request each one.

Every case that returns data rather than a refusal is a finding. Do it for reading, and then repeat for updating and deleting, which are usually worse and are frequently overlooked because the interface offers no obvious route to them.

Include the endpoints your interface does not call directly: exports, PDF generation, file downloads, the API your mobile app uses, webhook handlers, anything an earlier version left behind.

## Make the Ownership Part of the Query

There are two ways to fix each case, and one of them is better.

The fragile fix: fetch the record, then compare its owner to the current user, then decide. It works, and it must be repeated correctly in every handler, forever, by everyone including the next AI session.

The durable fix: make the query itself unable to return another account's rows. Fetch the invoice *where the id is this and the organisation is the session's organisation*. There is no comparison to forget, because a record that does not belong to the caller simply is not found.

In Supabase, row-level security is this idea enforced by the database, which is why it is worth the effort of getting right: a policy applies to every query from every code path, including ones written later by someone who never read your conventions. Application-level checks and database policies together are belt and braces, and for a product holding other people's data both are justified.

## Unguessable Identifiers Are Not a Fix

A frequent response is to switch from sequential integers to random identifiers so that nobody can guess another record's id.

Do it — sequential identifiers leak your volume and invite enumeration — but do not mistake it for a solution. Identifiers appear in URLs that get shared, in exports, in support tickets, in referrer headers, in a customer's browser history on a shared computer. An unguessable identifier that grants access to whoever holds it is a capability, and capabilities leak.

The authorisation check must exist regardless. Random identifiers make casual discovery harder; they do not make access controlled.

## The Nested Case Everyone Misses

Even products with ownership checks routinely miss one pattern: an object reached through a parent.

The endpoint checks that the project belongs to your organisation, then fetches a task by the identifier supplied — without confirming that the task belongs to that project. Substitute another organisation's task identifier and the check passes while the wrong record is returned.

The rule: every identifier in the request is validated against the path that reached it, not just the first one. In practice that means the query constrains the child by its parent, and the parent by the account.

## Stop It Coming Back

Fixing today's findings is half the work. The other half is ensuring that the endpoint written next month has the check.

Three things achieve this at small-product scale. A shared helper that fetches records scoped to the current account, so the natural way to write a query is the safe one — and the unsafe one requires deliberate effort. Row-level security in the database as the layer that does not depend on anyone remembering. And a test that walks every endpoint as a second-organisation user and fails the build if anything returns data.

That last one takes an afternoon to write and is the single most valuable test an AI-built product can have, because it keeps working while the code around it is rewritten by tools that have never read your security notes.

## Fields Have Permissions Too

Once record-level access is right, one layer remains and it is easy to overlook: which fields within a record a given user may read or write.

The reading side appears when an endpoint returns a whole row. A team member with limited permissions opens a colleague's profile and the response contains a salary field, an internal note or a risk score — hidden by the interface, plainly visible in the network tab. The fix is to return the fields appropriate to the requester rather than the whole record, which is one more reason to expose shaped views rather than tables.

The writing side is more dangerous and is called mass assignment. An endpoint that accepts a body and applies every key in it to the record allows a user to send fields nobody intended them to set — a role, an account identifier, a subscription tier, a verified flag. Generated code does this constantly, because passing the whole body to an update is the shortest thing to write.

The fix is a list rather than a filter: state explicitly which fields this endpoint accepts and ignore everything else. Never a list of fields to exclude, which is a list of what somebody remembered on the day.

Test it directly. Take a legitimate update request, add a field the user should not control — `role: "admin"` is the classic — and send it. If the value is applied, you have found a privilege escalation, and it is usually one line from being closed.

Do the same for the fields your interface merely hides. A disabled input, a column removed from a table, a section shown only to managers — each is a presentation choice, and the server must make the same decision independently or the choice is advisory.

## Setting This Up

For an existing product this is typically one to two days: an inventory of every endpoint taking an identifier, systematic cross-account testing for read, update and delete including exports, downloads and legacy endpoints, each finding fixed by scoping the query rather than by comparing after fetching, nested identifiers validated against their parents, row-level security policies covering every table with cross-tenant verification, sequential identifiers replaced where they appear in URLs, a scoped data-access helper adopted as the default pattern, and an automated cross-account test wired into your checks.

LaunchStudio does this in every security review, and it is the finding we expect rather than hope for. The engineers are Manifera's — eleven years, 120+ engineers, clients including Vodafone, TNO and CFLW.

[Ask us to open one of your records from another account](https://launchstudio.eu/en/#contact). It is ten minutes and it is the test that matters most.

## Real example

### The Invoice Number in the URL

Coen Bleeker built Factuurstroom in Lovable: invoicing and payment follow-up for freelancers and small agencies, 380 users across the Netherlands.

Invoices were reachable at a URL ending in a sequential number. Every endpoint required a valid session and none checked ownership. A user signed in to their own account could enter any number and see the corresponding invoice — the client's name and address, the line items, the amounts, and the freelancer's own bank details.

A user found it by mistyping his own invoice number and landing on somebody else's. He tried three more, then wrote to Coen. He had, in the process, seen four invoices belonging to three different businesses.

Two business days: an inventory of 47 endpoints taking identifiers, of which 31 had no ownership check; all of them fixed by scoping queries to the session's account rather than comparing after fetching, with a shared data-access helper introduced so the default way to fetch a record is the scoped one; nested cases corrected, including invoice lines and payment records that had been fetched by identifier without validating the parent invoice; row-level security enabled and policies written on all 14 tables, having previously been enabled on four; sequential invoice identifiers in URLs replaced with random ones while keeping the human-readable invoice number as a separate display field; an automated test added that signs in as a second-organisation user and requests every known identifier, failing the build on any response containing data; and access logs reviewed for the preceding period to determine the scope of exposure.

**Result:** log review found 61 cross-account requests over fourteen months, of which 54 came from the four users who had found it by mistyping and stopped. The remaining seven came from one account over one evening. Coen notified the affected businesses and the Autoriteit Persoonsgegevens. The automated test has since failed twice on new endpoints, both caught before deployment.

> *"Anyone who could log in could read every invoice in the system by typing a different number. I had spent a week on two-factor authentication and left the front door of every record open."*
> — **Coen Bleeker, Founder, Factuurstroom (Nijmegen)**

**Cost & Timeline:** €3,800 (endpoint inventory and cross-account testing, 31 authorisation fixes with scoped data access, nested identifier validation, row-level security across all tables, identifier replacement, automated cross-tenant test, access log review and incident documentation) — completed in 2 business days.

## Frequently Asked Questions

### What is an IDOR?

An endpoint that returns or modifies an object based on an identifier in the request without checking that the requester is entitled to it. Changing the number in a URL and seeing someone else's record is the classic symptom.

### Do login requirements protect against it?

No. Authentication establishes who you are; authorisation establishes what you may do. A logged-in user is still a stranger to every record that is not theirs.

### Do random identifiers solve the problem?

No. They prevent casual guessing, but identifiers leak through shared URLs, exports, support tickets and browser history. The ownership check must exist regardless.

### What is the most durable fix?

Scope the query so another account's rows cannot be returned, rather than fetching and then comparing. Add row-level security in the database so the rule applies to code paths written later.

### How do I stop it recurring?

A shared scoped data-access helper so the easy way is the safe way, database policies that do not depend on memory, and an automated test that requests every endpoint as a second-organisation user.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What is an insecure direct object reference?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "An endpoint that acts on an object named in the request without checking the requester is entitled to it — changing an id in the URL reveals another user's record."
      }
    },
    {
      "@type": "Question",
      "name": "Does requiring login protect against IDOR?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No. Authentication says who you are; authorisation says what you may access. Logged-in users are still strangers to other accounts' records."
      }
    },
    {
      "@type": "Question",
      "name": "Do random identifiers fix IDOR?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No. They stop casual guessing, but identifiers leak through shared links, exports and support tickets. The ownership check is still required."
      }
    },
    {
      "@type": "Question",
      "name": "What is the most durable way to fix it?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Scope the query to the caller's account so foreign rows cannot be returned, and enforce the same rule with row-level security in the database."
      }
    },
    {
      "@type": "Question",
      "name": "How do I prevent IDOR from reappearing?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "A scoped data-access helper as the default pattern, database policies independent of memory, and an automated cross-account test in your build."
      }
    }
  ]
}
</script>
