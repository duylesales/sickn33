---
Title: "Lovable Hosting: Logs You Can Search When It Matters"
Keywords: lovable hosting, structured logging, request id, error tracking, observability, log retention, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: Technical Solo Founder / Indie Hacker
---

# Lovable Hosting: Logs You Can Search When It Matters

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Lovable Hosting: Logs You Can Search When It Matters",
  "description": "A customer reports a problem from last Tuesday and your logs cannot answer. Structured logging, request identifiers, what never to log, and the retention that decides whether an investigation is possible.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-10-31",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/lovable-hosting-logs-you-can-search-when-it-matters" }
}
</script>

The email says: last Tuesday afternoon I tried to save a quotation and it disappeared. Can you check what happened?

In most AI-built products the honest answer is no. Not because the event was not logged, but because what was logged is a wall of undifferentiated text, retained for a day or two, with no way to find one customer's afternoon inside it.

Logging is one of those disciplines that costs almost nothing to set up correctly and is very difficult to add retrospectively, because the value is entirely in what was recorded at the time. The month you spend without it is a month you cannot investigate.

## Print Statements Are Not Logs

The default in generated code is a bare print or console statement, usually left over from debugging. It produces a line of text with no context: not who, not when in any useful sense, not which request, not which environment.

The alternative is one line of structure rather than prose. A log entry should be a record with fields — the event, the severity, the time, the request identifier, the user and account, and whatever is specific to the event — rather than a sentence with values interpolated into it.

The practical difference appears the first time you need to search. Structured entries can be filtered: show me errors for this account in this hour. Text lines can only be scanned, and scanning ten thousand lines for a name that may be spelled differently in three places is not an investigation.

## The Request Identifier Is the Single Best Habit

If you adopt nothing else, adopt this.

Generate an identifier at the start of every request, attach it to every log entry produced while handling that request, and return it to the client in a header and in any error message the user sees.

Three things follow. A customer reporting a problem can quote the code they saw, and you can retrieve every log line from that exact request. A single request that touches an endpoint, a database call, a payment provider and a background job is reconstructible as one story rather than four unrelated fragments. And when the same error appears a hundred times, you can tell whether it is one user retrying or a hundred users affected — which changes what you do next.

For background jobs, carry the identifier from the request that created the job, so the chain remains intact across the asynchronous boundary.

## What to Log, and at Which Level

Four levels are enough and each has a purpose.

**Error** for something that failed and needs attention: an unhandled exception, a payment that could not be recorded, a job that exhausted its retries. These should be rare enough that each one is worth reading.

**Warning** for something recoverable but notable: a retry that succeeded, a deprecated path used, a slow external call.

**Info** for business events you will want to count or trace: a user signed up, an invoice was issued, an import completed with this many rows. These are the entries that answer questions weeks later.

**Debug** for development, disabled in production, because at volume it is both expensive and unreadable.

The common failure is logging at info level on every step of every request, which produces volume nobody reads and a bill nobody expected. Log the boundaries and the decisions, not the narration.

## What Must Never Be Logged

Logs are copied, forwarded to third-party services, retained on somebody else's infrastructure and read by whoever has access. Treat them as a place data escapes.

Never log passwords, tokens, session cookies, API keys, full card numbers or complete request bodies from forms containing personal data. Be careful with anything special under the GDPR — health, biometric, or any information about a person's circumstances — because a support ticket logged in full becomes a record of somebody's medical situation held for ninety days in a search index.

Two practical measures. Configure your error tracking to scrub fields by name — password, token, authorization, and the fields specific to your product — before transmission. And log identifiers rather than values: a user's identifier rather than their name and email, an invoice identifier rather than its contents. You can look up the details in your own database when you genuinely need them, with the access controls that apply there.

## Retention Is a Decision, Not a Default

Platform log retention is frequently one day on free tiers and a week on cheap ones. That is shorter than the time it takes a customer to report a problem.

Decide deliberately. Thirty days of application logs covers nearly every support investigation. Ninety days suits products where customers report slowly or where you may need to demonstrate what happened. Security-relevant events — sign-ins, permission changes, admin actions, data exports — deserve longer and belong in your own database as an audit trail rather than in a log service, because they are business records rather than diagnostics.

The other half of the decision is deletion. Logs containing any personal data are personal data, and keeping them indefinitely is neither defensible nor useful. State the period, enforce it, and mention it in your privacy documentation.

## Errors Need a Different Tool

Logs are for reconstruction. Error tracking is for noticing.

The distinction matters because an error buried in a log stream is an error nobody sees. A dedicated error tracker groups occurrences of the same problem, tells you how many users are affected, shows the stack trace with the code, and notifies you the first time something new appears.

For a small product this is the highest-value monitoring available, and the free tiers are adequate for a long time. The setup that makes it useful: the release version attached to each event so you can see which deploy introduced a problem, the user and account attached so you can tell whether it is one customer or all of them, the request identifier so you can find the corresponding logs, and personal data scrubbed before it leaves your application.

## Make the Product Say What Happened

The last piece is user-facing and it is what turns a bad support conversation into a short one.

When something fails, show the user a message that says what happened in plain language and includes the request identifier. Not a stack trace, not "an error occurred", but something like: we could not save your quotation — reference 8f2a41 — please try again or send us this code.

Customers quote the code. You find the request in seconds. And the difference in tone is considerable: a product that produces a reference number reads as one where somebody is paying attention.

## Three Numbers Worth Watching Every Week

Logs answer questions about the past. A small number of metrics tell you whether to ask one, and for a product of this size three are enough.

**Error rate as a proportion of requests.** Not the absolute count, which grows with traffic, but the share. A step change in that ratio after a deploy is the clearest signal you will get that something you shipped is wrong.

**Response time at the slow end** — the 95th percentile rather than the average. Averages hide the experience of the customers most likely to complain, and a page that is fast for nine users in ten and terrible for the tenth looks healthy on an average.

**Volume of the thing your product exists to do.** Quotations created, appointments booked, documents processed. This is the number that catches failures no technical metric sees: a broken form still returns 200 responses quickly while nobody completes it.

That third one deserves the emphasis. Most serious outages in small products are not crashes — they are something that stopped working while everything continued to look fine. A daily count of the core action, compared against the same day last week, catches them in hours rather than when a customer writes.

None of this needs a dashboard product. A query, a weekly glance, and an alert on the business number when it deviates sharply covers the ground that matters at this scale.

## Setting This Up

For an existing product this is typically one day: structured logging replacing print statements, a request identifier generated per request and propagated through database calls, external calls, background jobs and error reports, log levels applied deliberately with debug disabled in production, sensitive fields scrubbed by name before anything leaves the application, retention set consciously with security events moved to a durable audit trail in your own database, an error tracker configured with release, user and request context, and user-facing error messages carrying the reference.

LaunchStudio sets this up as part of production readiness, and under the €49 per month managed arrangement the error alerts come to us first. The engineers are Manifera's — eleven years, 120+ engineers, and production systems for clients including Vodafone, TNO and CFLW.

[Ask us to investigate something that happened last week](https://launchstudio.eu/en/#contact). Whether we can is the test.

## Real example

### The Quotation That Disappeared

Willemijn Stoffels built Prijsopgave in Lovable: quotation software for garden landscaping and paving companies, 52 firms producing around 1,100 quotations a month.

A landscaper in Alphen aan den Rijn reported that a quotation for €14,000 of work had vanished after he saved it. He had spent forty minutes on it. He rebuilt it, lost the job to a competitor who quoted first, and told Willemijn he was considering leaving.

She could not investigate. Her logs were unstructured text retained for 24 hours, the report arrived four days later, and there was no way to search by customer even within the window. She could not tell him whether it had been saved, whether it had failed, or whether he had made a mistake — and not knowing was worse for the relationship than a defect would have been.

Two business days: structured logging across the application with event, severity, timestamp, request identifier, user and account on every entry; request identifiers generated per request and carried into database operations, the PDF generation service and background jobs; log levels applied so production emits errors, warnings and business events rather than narration; scrubbing of fields by name before transmission, since the previous setup had been logging full form bodies including customers' addresses; retention raised to 30 days, with sign-ins, permission changes, quotation status transitions and exports written to an audit table in her own database retained for two years; error tracking configured with release, user and request context; and user-facing error messages carrying a short reference code.

**Result:** the original cause was never established, but the pattern was — three weeks later an identical failure was captured in full, showing a PDF generation timeout that returned a success response to the browser while the save was rolled back. It was fixed in an afternoon. The landscaper stayed, mainly because he received a specific explanation and a reference number rather than an apology.

> *"A customer lost forty minutes of work and I could not tell him anything. Not what went wrong, not whether it was his mistake or mine. That conversation was the expensive part, not the bug."*
> — **Willemijn Stoffels, Founder, Prijsopgave (Alphen aan den Rijn)**

**Cost & Timeline:** €2,000 (structured logging, request identifier propagation, level policy, field scrubbing, retention and audit trail, error tracking with context, user-facing references) — completed in 2 business days.

## Frequently Asked Questions

### What is the single most useful logging change?

A request identifier attached to every entry and returned to the user. It turns scattered lines into one reconstructible story and lets a customer quote a reference you can search.

### How long should logs be kept?

Thirty days covers most support investigations; ninety suits slower-reporting customers. Security events — sign-ins, permission changes, exports — belong in a longer-lived audit table in your own database.

### What should never appear in logs?

Passwords, tokens, session cookies, API keys, card numbers and full request bodies containing personal data. Log identifiers instead of values and scrub sensitive fields by name before transmission.

### Do I need error tracking as well as logs?

Yes. Logs let you reconstruct; error tracking tells you something is happening, groups occurrences, and shows how many users are affected. The free tiers are adequate for a long time.

### Should error messages show a reference to the user?

Yes. A short code the customer can quote converts a vague report into a searchable request, and it reads as a product somebody is looking after.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What is the most useful logging improvement?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "A request identifier on every log entry, returned to the user, so a whole request is reconstructible and customers can quote a searchable reference."
      }
    },
    {
      "@type": "Question",
      "name": "How long should application logs be retained?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Thirty days for most support work, ninety where customers report slowly. Security events belong in a longer-lived audit table in your own database."
      }
    },
    {
      "@type": "Question",
      "name": "What must never be written to logs?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Passwords, tokens, cookies, API keys, card numbers and full request bodies with personal data. Log identifiers and scrub sensitive fields by name."
      }
    },
    {
      "@type": "Question",
      "name": "Is error tracking needed alongside logging?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes — logs reconstruct what happened, error tracking notices it, groups occurrences and shows how many users are affected."
      }
    },
    {
      "@type": "Question",
      "name": "Should users see an error reference code?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. It turns a vague report into a searchable request and signals that the product is being looked after."
      }
    }
  ]
}
</script>
