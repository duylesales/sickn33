---
Title: "Supabase Security: Edge Functions and Where the Boundary Sits"
Keywords: supabase security, ai app security, edge functions server side, verifying the caller, secrets in functions, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: Technical Solo Founder / Indie Hacker
---

# Supabase Security: Edge Functions and Where the Boundary Sits

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Supabase Security: Edge Functions and Where the Boundary Sits",
  "description": "Edge functions are where the trusted half of an AI-built app lives. Which operations belong there, how to verify the caller inside one, what to validate at the boundary, and the mistakes that make a function as exposed as the browser.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-07-21",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/supabase-security-edge-functions-and-boundaries" }
}
</script>

Every application has a line running through it. On one side is code you control, running on infrastructure you control. On the other is code running on a stranger's device, which they can read, modify and replay at will.

In an AI-built product, that line is frequently invisible, because the tool generated both halves in the same session, in the same language, in files that sit next to each other. Nothing in the editing experience signals that one directory is trusted and another is not. Edge functions are where the trusted half lives, and understanding what belongs there — and what still has to be checked once something arrives — is most of what separates a secure Supabase project from an exposed one.

## What Edge Functions Are Actually For

They run your code on infrastructure you control, close to the user, with access to secrets the browser never sees. That gives you three capabilities the frontend cannot have.

**Holding credentials.** A privileged key, a payment provider's secret, a model API key.

**Making authorisation decisions that cannot be tampered with.** Deciding whether this person may do this thing, in a place they cannot alter.

**Doing work on behalf of a user without exposing how.** Calling a third party, aggregating data across records, performing an operation that requires more privilege than the user has.

Everything else — rendering, interaction, optimistic updates, convenience validation — belongs in the frontend, and moving it to a function makes your app slower without making it safer.

## The Boundary Test: Three Questions

For any piece of logic, ask these in order.

**Does it need a secret?** If yes, it is server-side. There is no arrangement in which a credential reaches a browser safely.

**Does it decide what someone is allowed to do?** If yes, it is server-side. A check the user can edit is not a check.

**Does being wrong cost money or expose data?** If yes, it is server-side, even when the frontend also checks it for a better experience.

Three noes means it can live in the frontend. Most of an application answers no three times, which is why most of it is fine where it is.

## What Must Be on the Trusted Side

**Anything using a privileged key.** The Supabase service role key bypasses every access rule you wrote and belongs only in function environment variables.

**Payment operations.** Creating charges, confirming them, issuing refunds, and receiving webhooks from your provider.

**Calls to metered third parties.** Model APIs, SMS, mapping. Not only for the key, but because a function is where you enforce per-user limits before the cost is incurred.

**Cross-user aggregation.** A report covering data the requesting user cannot individually read.

**Administrative operations.** Anything that grants a role, deletes an account, or acts on another user's behalf.

**Business rules with financial consequence.** Applying a discount, calculating a total, checking eligibility.

## Verifying the Caller Inside the Function

This is the step generated functions most often omit, and its absence turns a server-side function into a public endpoint.

A function deployed in your project can be called by anyone who knows the address. It is not private because it lives on your infrastructure. So the first lines of every function that does anything meaningful must establish who is calling: read the caller's session token, verify it, and derive the user identity from that verification.

Two mistakes recur. Reading a user identifier from the request body rather than from the verified token — which means the caller simply tells you who they are, and can say anything. And verifying that a token exists without verifying that it is valid and unexpired.

Once identity is established, the authorisation question follows: is *this* user allowed to do *this*, to *this* record. That check belongs in the function or in the database policies underneath it, and preferably both.

## Validate at the Boundary

Everything arriving at a function is untrusted, including from your own frontend, because anyone can send a request that looks identical.

Validate the shape, the types and the ranges of every input against a schema. Reject anything unexpected rather than ignoring it, because silently accepting extra fields is how an authorisation flag ends up in a request body. And set explicit limits on size — a function accepting an arbitrarily large payload is a denial-of-service vector and a cost problem.

A useful discipline: share the validation schema between frontend and function, so the browser gets a good experience and the server gets the enforcement.

## Secrets in Functions

Function environment variables are the right place for credentials, and there are three habits worth keeping.

**One place per secret.** If a key exists in a function, a deployment platform and a local file, rotation becomes something you avoid.

**Never log them.** Including in error messages, which is how keys end up in log aggregation tools with wider access than the function itself.

**Least privilege where the provider allows it.** A scoped or restricted key limits what a compromise achieves, and several providers offer them without being asked.

## Cold Starts, Timeouts and Limits

Practical constraints that shape what you put in a function.

Functions that have not run recently take longer on the first request. For an interactive operation, that latency is visible; for a webhook receiver, it is irrelevant. Functions also have execution time limits, which means long work — a large export, a model call that may take a minute, a bulk import — should acknowledge quickly and continue in the background rather than holding a request open until it times out.

Know your limits before you design around them, and design the user-facing behaviour for the slow case rather than the typical one.

## Logging Without Leaking

Functions are where you find out what happened, and where personal data most easily ends up in places it should not.

Log what you need to debug: who called, when, which operation, how long, whether it succeeded, and an error identifier. Do not log request bodies by default, because they contain whatever your users typed. Where you need content for debugging a failure, log it only on failure and delete it on a short schedule.

This matters beyond tidiness: logs are a copy of personal data, with their own retention, their own access and their own place in a privacy questionnaire.

## Reviewing Your Own Functions

Half an hour, and it finds most of what is wrong in a generated project.

List every function in your project. For each: does it verify the caller's token, does it derive identity from the token rather than the request body, does it check authorisation for the specific record, does it validate inputs against a schema, does it use a privileged key and if so is that necessary, does it log anything sensitive, and what happens if it is called a thousand times in a minute.

Then test one: call a function directly, without going through your app, with a modified user identifier. Anything that succeeds is a finding.

## Building the Trusted Half Properly

For most AI-built products this is a short, well-defined piece of work: identifying which operations crossed the boundary in the wrong direction, moving them into functions, adding caller verification and input validation where it is missing, consolidating secrets, adding rate limits, and adjusting logging so it is useful without being a liability.

That is part of the [Launch Ready package](https://launchstudio.eu/en/#packages) — done without touching the interface you built in Lovable, with the codebase left conventional and AI-readable so you keep iterating afterwards. The engineers are Manifera's, with eleven years of production systems behind them for clients including Vodafone, TNO and CFLW, from Amsterdam and Ho Chi Minh City.

If your app has functions and you have never called one directly to see what happens, [talk to an engineer who understands AI-generated code](https://launchstudio.eu/en/#contact).

## When a Function Should Not Exist

The opposite mistake is less dangerous and more common than founders expect: routing everything through functions because server-side sounds safer.

**Reading your own data does not need one.** If row level security correctly restricts a table to its owner, the frontend can query it directly with the public key. Wrapping that in a function adds latency, a cold start and a piece of code to maintain, in exchange for nothing — the policy was already doing the work.

**Simple filtering and sorting does not need one.** The database is better at it than a function passing parameters through.

**Presentation logic certainly does not.** Formatting, totals displayed to a user, optimistic updates. These belong where the user is.

The test is the same three questions in reverse: if the operation needs no secret, decides no permission, and being wrong costs nothing, it belongs in the frontend with a policy protecting the data underneath.

A project with forty functions is usually a project where somebody applied a rule rather than a judgement, and the cost appears as a slow application with a large surface to review. Functions are the trusted boundary, not the default location for code.

## Real example

### A Function That Trusted Whoever Was Calling It

Bram Osinga built Declaratie in Lovable: an expense-claim tool used by seven small accountancy practices around Hilversum, where employees submit claims and practice owners approve them.

Approval was handled by an edge function, which was the correct architectural choice — approving a claim required a privileged key to write to a table employees could not modify directly. The function was well written and did exactly what it was asked.

What it did not do was verify who was calling it. It read a `user_id` and a `role` from the request body and trusted both. Any employee who opened the browser's network tab, copied the approval request and changed two values could approve their own claims, at any amount, as if they were a practice owner.

Nobody had. The review found it before anyone did.

Five business days of work: caller verification added to all six functions in the project, with identity derived from the verified session token and the request body ignored for anything identity-related; authorisation checks added against the specific claim and practice; inputs validated against shared schemas with unexpected fields rejected; the privileged key removed from two functions that did not need it; rate limiting on submission and approval; and logging reduced to metadata, with claim contents logged only on failure and deleted after seven days.

**Result:** the flaw was closed before use, and the practice owners' own accountant — who had asked how approval was controlled — received a written answer that satisfied the question.

> *"The function was on my server, so I thought it was safe. It never occurred to me that anyone could just call it themselves and tell it who they were."*
> — **Bram Osinga, Founder, Declaratie (Hilversum)**

**Cost & Timeline:** €2,300 (caller verification and authorisation across six functions, input validation, key scoping, rate limiting, logging) — completed in 5 business days.

## Frequently Asked Questions

### Are edge functions private because they run on my infrastructure?

No. A deployed function can be called by anyone who knows its address. It is trusted in the sense that it can hold secrets, not in the sense that only your app can reach it — which is why every function must verify its caller.

### How should a function know who is calling?

From the caller's session token, verified inside the function. Never from a user identifier in the request body, because the caller controls that and can claim to be anyone.

### What belongs in a function rather than the frontend?

Anything using a secret, anything deciding what someone is allowed to do, and anything where being wrong costs money or exposes data. Most of an application answers no to all three and is fine in the frontend.

### Do I still need row level security if my functions check authorisation?

Yes. Defence in depth matters here because the automatically generated API is reachable with your public key regardless of your functions. Policies protect the database directly; function checks protect the operation.

### What should a function log?

Metadata by default — caller, operation, duration, outcome, error identifier. Not request bodies, which contain whatever users typed. Log content only on failure, with short retention, because logs are a copy of personal data.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Are edge functions private because they run on my infrastructure?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No — a deployed function can be called by anyone who knows its address. It is trusted to hold secrets, not shielded from callers, so every function must verify who is calling."
      }
    },
    {
      "@type": "Question",
      "name": "How should a function know who is calling?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "From the caller's session token verified inside the function, never from a user identifier in the request body, which the caller controls."
      }
    },
    {
      "@type": "Question",
      "name": "What belongs in a function rather than the frontend?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Anything using a secret, deciding permissions, or where being wrong costs money or exposes data. Most of an app answers no to all three."
      }
    },
    {
      "@type": "Question",
      "name": "Do I still need row level security if my functions check authorisation?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes — the generated API is reachable with your public key regardless of your functions, so policies protect the database while function checks protect the operation."
      }
    },
    {
      "@type": "Question",
      "name": "What should a function log?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Metadata by default — caller, operation, duration, outcome — and content only on failure with short retention, since logs copy personal data."
      }
    }
  ]
}
</script>
