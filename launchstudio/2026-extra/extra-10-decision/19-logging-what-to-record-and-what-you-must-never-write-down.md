---
Title: "Logging: What to Record, and What You Must Never Write Down"
Keywords: structured logging best practices, never log passwords, PII in logs, log retention policy, sensitive data logging compliance, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: Technical Solo Founder / Indie Hacker
---

# Logging: What to Record, and What You Must Never Write Down

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Logging: What to Record, and What You Must Never Write Down",
  "description": "A practical checklist for founders on what a production log line should contain, how long to keep it, and the specific categories of data — tokens, passwords, card numbers, full personal records — that should never appear in a log at all.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-02-25",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/logging-what-to-record-and-what-you-must-never-write-down" }
}
</script>

"Wait — is my own password sitting in a log file somewhere?" is a question founders ask exactly once, usually while searching production logs for something unrelated, spotting a familiar string, and realizing it's the password they typed testing their own login form last week. It isn't a hypothetical scare story. `console.log(req.body)` — or its equivalent in any framework — is one of the most common debugging patterns in AI-generated code, added to understand why an endpoint is behaving unexpectedly, and left in because it worked and nobody thought to remove it before launch.

It logs whatever the request actually contained, which on a login endpoint is a password, and on a checkout endpoint can be a card number if the payment integration isn't fully tokenized upstream. Logs live longer than founders expect, get copied to more places than founders realize, and get read by more tools — including third-party log aggregation services — than almost any other piece of a product's infrastructure.

## The Two Questions Every Log Line Should Answer, and the One It Never Should

A useful production log line answers two questions when something goes wrong: what happened, and enough context to reproduce or understand it without needing to ask the affected user for details they may not remember. "Payment failed" is nearly useless six weeks from now. "Payment failed: order_id=8842, user_id=1193, reason=card_declined, provider=stripe" is immediately actionable — it names the order, the account, the specific failure reason, and which system reported it, letting you jump straight to the relevant Stripe dashboard entry instead of guessing.

The question a log line should never answer is "what exactly did this user type into this field" when that field could reasonably contain a secret. This is a categorical rule, not a judgment call made per field: if a field's contents include a password, a session token, an API key, a full card number, or a government ID number, that value doesn't appear in a log line under any circumstances, regardless of how useful it would be for debugging in the moment. The debugging value never outweighs the exposure, because logs live longer, get replicated to more places, and get read by more tools and more people than almost any other piece of your infrastructure — including, in many setups, third-party log aggregation services that see your raw log stream by design.

## The Never List, Specifically

Four categories deserve zero exceptions, because each has a distinct, serious failure mode if it leaks.

**Passwords, in any form — plaintext, or even a hash, in a log line.** A password should never exist as a discrete value anywhere outside the authentication code path that immediately hashes it; a log statement anywhere in that path that includes the raw request body captures it in plaintext, permanently, in a system with far weaker access controls than your actual user table.

**Session tokens, API keys, and JWTs.** These are the credentials that let someone act as your user or your service without a password at all — logging an `Authorization` header verbatim, which a naive request-logging middleware does by default, hands anyone who can read your logs a working, unexpired session for the account that made the request. This is functionally equivalent to logging a password, just less obviously so, which is exactly why it's more commonly missed.

**Full payment card numbers, CVVs, or any raw card data.** If your integration is properly built on Stripe, Mollie, or a similar provider using tokenization (Stripe Elements, Checkout, or a hosted payment page), your own servers should genuinely never see a full card number to begin with — it goes directly from the customer's browser to the payment provider. If a card number is appearing in your logs at all, that's a signal your payment integration is handling raw card data server-side in a way that also has PCI-DSS compliance implications independent of the logging question, and it needs architectural attention, not just a logging fix.

**Full personal records in a single log line** — a complete user profile, a full medical intake form, an entire address plus government ID plus date of birth logged together as one object because "log the user object" was the easiest debugging line to write. Individually, some of these fields might be fine to reference by ID; logged together as a complete record, a single log line becomes a complete personal data exposure if that log is ever breached, forwarded incorrectly, or accessed by someone who shouldn't see it — which under GDPR is itself a reportable personal data processing activity worth minimizing on principle, not just as a security hedge.

## What Structured Logging Actually Means, and Why It's Not Optional at Scale

Most AI-generated logging is unstructured: a string, concatenated with some variables, written to standard output — `console.log('User ' + userId + ' failed login')`. It's readable by a human scrolling through a handful of lines, and it becomes nearly useless the moment you have more than a trivial amount of traffic, because there's no reliable way to search, filter, or aggregate free-text strings across thousands of log lines without brittle text matching.

**Structured logging** writes each log entry as a consistent object — typically JSON — with named fields: `{"level": "error", "event": "login_failed", "user_id": 1193, "reason": "invalid_password", "timestamp": "..."}`. The practical payoff shows up the first time you need to answer a real question under time pressure: "how many failed logins happened for this account in the last hour" is a filterable query against structured fields, and an unreadable scroll-and-guess exercise against free-text strings. Every serious logging platform (Datadog, Better Stack, Axiom, or your hosting provider's built-in log viewer) is built around structured fields, and adopting the format costs almost nothing if you start early — it's a logging library configuration choice, not a rewrite — and a genuine retrofit if you wait until you have thousands of unstructured log lines and no consistent shape to search across.

The discipline this enables directly supports the never-log-secrets rule above: a structured logger with a defined schema per event type makes it obvious, at the point you're writing the log call, exactly which fields you're including — versus `console.log(req.body)`, which includes everything in the request by default, secrets included, because nobody had to decide field-by-field what belongs in the log.

## Retention: How Long Is "Long Enough," and What Long Is Actually Risky

Log retention is a decision most prototypes never make explicitly — logs simply accumulate on whatever platform's default applies, which might be a few days on a free hosting tier, or indefinitely if logs are being forwarded to cheap, unmanaged storage nobody's reviewing.

Too little retention is a real operational cost: if a customer reports an issue from four days ago and your logs only go back 48 hours, you've lost the ability to investigate it, which is a genuine debugging capability tradeoff, not just a compliance nuance. Too much retention is a different kind of cost: every day a log line sits in storage is another day it's a target if your logging infrastructure or a third-party log service is ever breached, and under GDPR, personal data — including personal data that ends up in logs, like an email address in an error message — is supposed to be retained no longer than necessary for the purpose it was collected for, which "we never set a retention policy so it's still there from two years ago" does not satisfy.

A reasonable default for most early-stage products: 30 to 90 days of readily searchable log retention for operational debugging, with anything beyond that either discarded automatically or moved to cheaper archival storage only if there's a specific, documented reason (a compliance requirement, an ongoing investigation) to keep it longer. Most logging platforms let you configure this retention window directly rather than requiring custom cleanup scripts — the fix here is usually setting a number that currently isn't set at all, not building new infrastructure.

## Error Messages Shown to Users vs. What Gets Logged Behind Them

A related, frequently conflated decision: what a user sees when something fails versus what your system records about that failure. AI-generated error handling often does one of two wrong things — it shows the user a raw stack trace or database error message (which can leak internal architecture details, table names, or occasionally query fragments containing other data), or it shows a generic "something went wrong" with nothing useful logged behind it, leaving you unable to investigate the report that inevitably follows.

The correct split: the user sees a clear, generic, actionable message ("we couldn't process your payment, please try again or contact support"), while the full technical detail — the actual exception, the stack trace, the relevant IDs — goes into your structured log, tagged with a unique error reference ID that's also shown to the user, so a support conversation can jump straight from "the user quoted error ref abc123" to the exact log line describing what actually happened, without ever exposing internal detail in the response itself.

## A Pre-Launch Logging Audit You Can Run in an Hour

Search your entire codebase for `console.log`, `print`, or your language's equivalent, applied to full request or response objects, and check each one against the never-list above — password fields, `Authorization` headers, full card data, complete user records. Confirm your logging output is structured (JSON with named fields), not free-text string concatenation, at least for anything you'd realistically need to search or filter later. Check what retention period your hosting platform or logging service is actually configured for right now — not what you assume it is — and set an explicit number if none exists. Confirm error responses shown to users never include raw stack traces or database error text, and that a matching, more detailed version is captured in your logs under a shared reference ID. And specifically test your payment flow's logs: trigger a failed payment in a sandbox environment and check exactly what appears in your logs about that transaction.

That last check catches the single most consequential version of this problem, because payment logging failures are the ones with financial and compliance weight behind them, not just an embarrassing debugging habit.

## Getting This Right Without a Rewrite

Fixing logging is almost always a narrow, contained pass — auditing existing log statements, removing or redacting the ones that capture sensitive fields, standardizing on structured output, and setting a retention policy — rather than a rearchitecture of anything your product does. It fits comfortably inside LaunchStudio's Launch Ready scope for most single-product audits, and it's one of the fastest fixes to apply precisely because it touches logging calls specifically, not the business logic surrounding them.

It's also one of the findings [Manifera's engineers](https://www.manifera.com/services/custom-software-development/) flag most consistently in a first review of AI-generated code, because the pattern that causes it — logging the full request object for convenience during development — is nearly universal, and nearly universally forgotten before launch. If you're not sure what your product is currently writing to its logs, [describe your project and get a reply within one business day](https://launchstudio.eu/en/#contact) on what a logging audit would actually find.

## Real example

### An Indie Hacker Finds His Own Password in His Logs

Jakub Wróbel built Notarize, a small e-signature tool for freelance contractors, using Cursor, with a debug logging line on the login endpoint — `console.log('Login attempt:', req.body)` — added early in development to troubleshoot an authentication bug and never removed once the bug was fixed.

Preparing for a routine security review ahead of an enterprise pilot, Jakub searched his own production logs for his test account's email address out of curiosity about how much traffic he'd generated during testing. What came back included his own password, in plaintext, from a login attempt weeks earlier — proof that every user's password, for every login attempt, successful or not, had been written to a log file forwarded to a third-party logging service the entire time the product had been live.

The fix removed the debug line entirely, replaced it with a structured log entry recording only the user ID, timestamp, and success or failure outcome, added a lint rule flagging any future `console.log` call applied directly to a request body, and — because the exposure had already happened — forced a password reset for all existing accounts as a precaution, communicated plainly to users as a proactive security measure.

**Result:** the enterprise pilot's security questionnaire, which specifically asked about logging practices, could be answered accurately and favorably instead of requiring a scramble to fix the same issue under a prospect's deadline.

> "I found my own password in a log file I'd forgotten existed. That's the moment 'I'll clean up the debug logs eventually' stopped being a someday task."
> — **Jakub Wróbel, Founder, Notarize (Wrocław)**

**Cost & Timeline:** Launch Ready engagement, logging audit and remediation — delivered in 3 business days.

## Frequently Asked Questions

### How do I search my existing logs for accidentally captured secrets?

Search your log storage or aggregation tool for the literal strings "password", "token", "authorization", and "card" (case-insensitive) across recent log history, and check each result — most logging platforms support this kind of full-text search directly in their dashboard without any code changes needed to run the check.

### Is it enough to just mask sensitive fields with asterisks in the log output?

Masking helps but isn't the same as never capturing the value — if the masking happens after the value is already logged (a common bug), or if the masking logic misses a field, the raw value can still be written. The safer approach is deciding at the point of writing each log statement which fields to include at all, rather than logging everything and masking afterward.

### Do error tracking tools like Sentry have this same risk?

Yes — Sentry and similar tools capture request context, including headers and body data, by default unless configured otherwise, so the same never-list applies there. Most of these tools support explicit data scrubbing rules, which should be configured deliberately rather than assumed to work out of the box.

### How long should I actually keep my application logs?

30 to 90 days of readily searchable retention covers most operational debugging needs for an early-stage product. Beyond that, keep logs only if there's a specific, documented reason, and set an explicit retention policy on your logging platform rather than leaving it at an unexamined default.

### Can LaunchStudio audit my logging without seeing my actual customer data?

Yes — a logging audit typically reviews the code that generates log statements and the configuration of your logging pipeline, rather than requiring access to your live customer data itself, which keeps the review focused on what could leak rather than what already has.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "How do I search my existing logs for accidentally captured secrets?", "acceptedAnswer": { "@type": "Answer", "text": "Search your log storage or aggregation tool for the literal strings password, token, authorization, and card, case-insensitive, across recent history. Most logging platforms support full-text search in their dashboard without any code changes." } },
    { "@type": "Question", "name": "Is it enough to just mask sensitive fields with asterisks in the log output?", "acceptedAnswer": { "@type": "Answer", "text": "Masking helps but isn't equivalent to never capturing the value, since masking applied after logging or missing a field still leaves the raw value written. It's safer to decide which fields to include at the point of writing each log statement rather than masking afterward." } },
    { "@type": "Question", "name": "Do error tracking tools like Sentry have this same risk?", "acceptedAnswer": { "@type": "Answer", "text": "Yes. Sentry and similar tools capture request context including headers and body data by default unless configured otherwise, so the same never-log rules apply. Most support explicit data scrubbing rules that should be configured deliberately." } },
    { "@type": "Question", "name": "How long should I actually keep my application logs?", "acceptedAnswer": { "@type": "Answer", "text": "30 to 90 days of readily searchable retention covers most operational debugging needs for an early-stage product. Beyond that, keep logs only for a specific documented reason and set an explicit retention policy rather than an unexamined default." } },
    { "@type": "Question", "name": "Can LaunchStudio audit my logging without seeing my actual customer data?", "acceptedAnswer": { "@type": "Answer", "text": "Yes. A logging audit typically reviews the code generating log statements and the logging pipeline configuration, rather than requiring access to live customer data, keeping the review focused on what could leak rather than what already has." } }
  ]
}
</script>
