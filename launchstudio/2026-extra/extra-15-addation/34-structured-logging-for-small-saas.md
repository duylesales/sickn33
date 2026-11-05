---
Title: "Structured Logging for Small SaaS"
Keywords: structured logging saas, logging best practices startup, supabase edge function logging, audit vs application logs, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: AI-Native Founder (Non-Technical)
---

# Structured Logging for Small SaaS

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Structured Logging for Small SaaS",
  "description": "Logs are how you find out what happened when something goes wrong, but AI-built apps usually log either nothing useful or far too much, including personal data. This guide explains structured logging for a small SaaS: what to log, log levels, request IDs, where logs go, retention, privacy, the difference between application and audit logs, and how to search logs during an incident.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-05-21",
  "inLanguage": "en",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/structured-logging-for-small-saas" },
  "citation": [
    { "@type": "CreativeWork", "name": "OWASP Logging Cheat Sheet", "url": "https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html" },
    { "@type": "CreativeWork", "name": "OpenTelemetry documentation", "url": "https://opentelemetry.io/docs/" },
    { "@type": "CreativeWork", "name": "Supabase: Logging", "url": "https://supabase.com/docs/guides/telemetry/logs" },
    { "@type": "CreativeWork", "name": "OWASP Top 10 2021: A09 Security Logging and Monitoring Failures", "url": "https://owasp.org/Top10/A09_2021-Security_Logging_and_Monitoring_Failures/" }
  ]
}
</script>

When something goes wrong in production, founders ask the same questions. What happened? When did it start? Which customers were affected? Was it a bug, a provider outage or someone trying to break in? The answers live in logs, or they do not exist at all.

In many AI-built apps, the logs are not helpful. Some apps log nothing beyond what the hosting platform records automatically. Others are full of `console.log` statements left over from building, printing entire request bodies, user objects and API responses, including email addresses, tokens and personal data. Neither helps during an incident, and the second creates privacy and security risks of its own.

Structured logging is a simple discipline that fixes both problems. This guide explains how a small SaaS can log the right things, in the right format, in the right place.

## Key Takeaways

- **Structured logs are machine-readable records,** usually JSON, with consistent fields such as timestamp, level, event, request ID and user ID.
- **Log events, not data dumps.** Record what happened and the identifiers needed to investigate, not entire objects.
- **Use a request ID** to connect all log lines from one request across frontend, functions and database.
- **Keep personal data, secrets and payment details out of logs,** and define retention periods.
- **Separate application logs from audit logs.** Application logs help you debug; audit logs record who did what, for security and compliance.

## Why Logging Matters More Than It Seems

The OWASP Top 10 includes "Security Logging and Monitoring Failures" as one of the most significant web application risks. Without adequate logging, breaches go undetected, incidents cannot be investigated and you cannot answer basic questions from customers or regulators. Under GDPR breach rules, for example, being unable to show whether exposed data was actually accessed forces you to assume the worst.

Logs also matter for ordinary operations: debugging customer issues, understanding performance problems and verifying that background jobs and webhooks did what they should.

## Unstructured vs Structured Logs

An unstructured log line looks like this:

```
Payment failed for user jan@example.nl order 4821 amount 49.00
```

It is readable by a human, but hard to search, filter or aggregate, and it contains an email address.

A structured log line looks like this:

```json
{"ts":"2028-05-21T09:14:03Z","level":"warn","event":"payment_failed","request_id":"req_8f2c","user_id":"usr_391","order_id":"ord_4821","provider":"mollie","reason":"insufficient_funds"}
```

Every field can be searched and filtered. You can count failed payments per provider, find all lines for one request or see whether failures cluster at a particular time. And the user is identified by an internal ID, not an email address.

## What to Log

Focus on events that help you understand the system's behaviour:

| Category | Examples |
| --- | --- |
| Requests | Method, route, status code, duration, request ID |
| Business events | Order created, payment succeeded or failed, subscription changed, export generated |
| Integrations | Webhook received and processed, external API call failed, retry scheduled |
| Background jobs | Job started, completed, failed, with duration and attempt number |
| Authentication | Sign-in success and failure, password reset requested, MFA enabled |
| Errors | Error type, message without sensitive data, stack trace reference |
| Security signals | Access denied, rate limit hit, invalid webhook signature |

Use consistent event names, just as you would for analytics, and document them.

## What Not to Log

| Never log | Why |
| --- | --- |
| Passwords, tokens, API keys, session cookies | Anyone with log access could impersonate users or services |
| Full payment card numbers, IBANs | Financial data with strict handling rules |
| Health data, national ID numbers | Special category or highly sensitive personal data |
| Full request and response bodies | Often contain all of the above |
| Email addresses and names by default | Unnecessary personal data; use internal IDs |
| AI prompts and outputs containing customer content | Personal and confidential data in large volumes |

AI-built apps frequently contain `console.log(user)`, `console.log(req.body)` or `console.log(response)` statements from development. Search for them and remove or replace them before launch.

## Log Levels

Use a small set of levels consistently:

- **error:** something failed that needs attention, such as an unhandled exception or a failed payment webhook
- **warn:** something unexpected that the system handled, such as a retry or a rejected input
- **info:** normal significant events, such as an order created or a job completed
- **debug:** detailed information for development, normally disabled in production

Too many errors that are not really errors cause alert fatigue; too few hide real problems.

## Request IDs and Correlation

A single user action can involve the browser, a Next.js or Vite frontend, one or more Supabase edge functions, the database and external services. To follow one request through all of them, generate a request ID at the start, pass it along in headers and include it in every log line.

```typescript
const requestId = req.headers.get("x-request-id") ?? crypto.randomUUID();
log.info("export_requested", { request_id: requestId, user_id: user.id, format: "csv" });
```

Return the request ID in error responses and show it to users in error messages, such as "Reference: req_8f2c". When a customer contacts support with that reference, you can find exactly what happened.

For more advanced setups, OpenTelemetry provides a standard way to connect logs, traces and metrics across services, which many observability tools support.

## A Minimal Logger

You do not need a heavy library to start. A small helper that writes JSON lines with consistent fields is enough for most AI-built apps:

```typescript
type Fields = Record<string, unknown>;

function write(level: string, event: string, fields: Fields = {}) {
  console.log(JSON.stringify({ ts: new Date().toISOString(), level, event, ...fields }));
}

export const log = {
  info: (e: string, f?: Fields) => write("info", e, f),
  warn: (e: string, f?: Fields) => write("warn", e, f),
  error: (e: string, f?: Fields) => write("error", e, f),
};
```

Most hosting platforms, including Supabase edge functions and Vercel, capture console output, so JSON lines become searchable in their log explorers or can be forwarded to a dedicated log tool.

## Where Logs Go

| Option | Suitable for | Notes |
| --- | --- | --- |
| Platform log explorers (Supabase, Vercel) | Early stage | Built in, limited retention and search |
| Dedicated log management tools | Growing products | Better search, alerts, longer retention, extra cost |
| Your own database table | Audit logs and business events | Queryable, under your control, mind volume |
| Object storage archive | Long-term retention | Cheap, slower to search |

For a small SaaS, platform log explorers plus a database table for audit events often suffice at launch. Move to a dedicated tool when you need longer retention, cross-service search or log-based alerts. Choose a provider with EU data storage and sign a processing agreement.

## Application Logs vs Audit Logs

These two are often confused, but they serve different purposes:

| | Application logs | Audit logs |
| --- | --- | --- |
| Purpose | Debugging and operations | Accountability and security |
| Audience | Developers | Customers, auditors, security teams |
| Content | Requests, errors, performance, jobs | Who did what to which record, when |
| Retention | Short, for example 14 to 30 days | Longer, as agreed with customers or required |
| Integrity | Best effort | Append-only, protected from modification |
| Access | Engineering team | Often visible to customer admins |

B2B customers increasingly expect audit logs, and security questionnaires ask about them. Our guide on [audit logs for B2B SaaS](https://launchstudio.eu/en/blog/audit-logs-for-b2b-saas) explains how to build them.

## Retention

Define how long logs are kept and make sure the platform enforces it:

- **Application logs:** typically 14 to 90 days, long enough to investigate incidents and recurring issues
- **Security-relevant logs:** often longer, for example 6 to 12 months, depending on customer requirements and risk
- **Audit logs:** as agreed with customers or required by sector rules

Shorter retention reduces privacy risk and cost. Document your retention periods in your records of processing.

## Searching Logs During an Incident

When something breaks, a structured approach saves time:

1. **Define the time window** from first report or alert.
2. **Filter by level and event,** for example all `error` events on the payment webhook route.
3. **Group by field,** such as error reason or affected customer, to see the scope.
4. **Follow request IDs** from failing requests through all services.
5. **Compare with deploy times,** since many incidents start with a release.
6. **Record what you find** in the incident log.

With structured logs, these steps take minutes. With unstructured logs, they can take hours.

## Alerts Based on Logs

Logs become far more valuable when a few of them trigger alerts automatically. You do not need many; start with patterns that indicate customer impact or security problems:

| Alert condition | Why it matters |
| --- | --- |
| Any `error` on payment webhook processing | Customers may have paid without receiving access |
| More than a few failed sign-ins for one account in a short period | Possible credential stuffing or brute force |
| Invalid webhook signatures | Someone may be sending forged events |
| Background job failures after all retries | Work such as emails, exports or imports did not happen |
| Sudden spike in `access_denied` events | Possible probing, or a broken permission after a release |
| No `info` events from a critical job for longer than expected | The job may have stopped running entirely |

The last row is easy to overlook. Some of the most damaging failures produce no errors at all: a scheduled job simply stops running. An alert on missing events catches that.

Route alerts to a channel someone watches, and review them after each incident to tune thresholds. An alert that fires every day without action needed should be adjusted or removed.

## Common Mistakes

**Logging everything during development and never cleaning up.** Production logs full of personal data and noise.

**No request IDs.** Impossible to connect a user's report to the relevant lines.

**Inconsistent field names.** `userId`, `user_id` and `uid` in different functions make searches unreliable.

**Swallowing errors without logging.** The error never appears anywhere.

**Unlimited retention.** Personal data kept indefinitely in logs nobody reads.

## How LaunchStudio Helps

LaunchStudio sets up logging as part of every production launch: removing sensitive debug output, adding a structured logger with consistent fields, request IDs across frontend and functions, logging for webhooks and background jobs, audit logging where customers need it, retention settings and log-based alerts for critical failures.

The **Launch Ready** package (€800-€3,500) includes logging alongside security hardening and deployment; **Launch & Grow** (€2,500-€7,500 plus €49 per month) adds managed hosting, monitoring and priority support. Use the [price calculator](https://launchstudio.eu/en/#calculator) for an estimate.

LaunchStudio is backed by Manifera, a software development company with 11+ years of experience, 160+ delivered projects and 120+ engineers, operating production systems for enterprise clients. Founders meet the team at Herengracht 420 in Amsterdam; engineering happens at the development centre on Pho Quang Street in Ho Chi Minh City, with a hub on Tras Street in Singapore.

## Real example

### An AI-Native Founder in Action: The Webhook That Failed Silently for Eleven Days

Joris Peters built Leskaart with Bolt and Supabase: a booking and subscription tool for dance and yoga studios in the Netherlands, where members buy class cards and subscriptions through Mollie. One studio owner noticed that several members had paid for ten-class cards but their accounts still showed zero classes.

Investigating was painful. The Mollie webhook edge function printed the entire incoming request and the full member object with `console.log`, including names, emails and phone numbers, so the logs were full of personal data but contained no clear record of whether processing had succeeded. There were no request IDs, error handling returned a 200 response even when the database update failed, and log retention was the platform default. It took two days to reconstruct that a schema change had broken card crediting eleven days earlier, affecting 63 payments across five studios.

LaunchStudio replaced the debug output with a structured logger that recorded webhook receipt, verification, processing result and duration with internal IDs only. Request IDs were generated for every request and returned in error messages. The webhook handler now returned an error status when processing failed, so Mollie retried, and logged a structured error that triggered an alert. A database table recorded each payment's processing state for reconciliation, retention was set to 30 days for application logs, and a daily job compared Mollie payments with credited cards and alerted on mismatches. The 63 affected payments were credited and members notified.

**Result:** Two months later, a provider timeout caused a handful of webhook failures. The alert fired within minutes, Mollie retried successfully, and the reconciliation job confirmed no missing credits. Joris found the full story in the logs in under five minutes.

> *"My old logs were full of my customers' phone numbers and told me nothing. Now they tell me exactly what happened, and nothing about anyone's personal life."*
> - **Joris Peters, Founder, Leskaart (Arnhem)**

**Cost & Timeline:** €2,400 (Launch Ready package: structured logging, request IDs, webhook error handling, reconciliation job, alerts and data cleanup) - completed in 7 business days.

## Frequently Asked Questions

### What is structured logging?

Structured logging means writing log entries in a consistent, machine-readable format, usually JSON, with defined fields such as timestamp, level, event name, request ID and relevant identifiers. It makes logs easy to search, filter and analyse, especially during incidents.

### Can I log user email addresses?

Avoid it by default. Use internal user IDs instead, which let you look up the user in your database when needed without spreading personal data across logs. Logs are often accessible to more people and kept in more places than your main database.

### How long should I keep logs?

Application logs are typically kept for 14 to 90 days. Security-relevant and audit logs are often kept longer, depending on customer contracts and risk. Define retention explicitly, enforce it in your platform and document it in your records of processing.

### How does Manifera's experience help with logging and operations?

Manifera has operated production systems for enterprise clients for 11+ years, where incidents must be investigated quickly and logs must meet security requirements. LaunchStudio applies that experience to give small SaaS products logging that helps during incidents without creating privacy risks.

### Does logging affect my product's visibility?

Indirectly. Good logging helps you find and fix problems faster, which improves reliability and user experience. Reliable products earn better reviews and fewer complaints, which influence how customers, search engines and AI answer engines perceive your company.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What is structured logging?",
      "acceptedAnswer": { "@type": "Answer", "text": "Writing log entries in a consistent machine-readable format, usually JSON, with fields such as timestamp, level, event, request ID and identifiers." }
    },
    {
      "@type": "Question",
      "name": "Can I log user email addresses?",
      "acceptedAnswer": { "@type": "Answer", "text": "Avoid it by default; use internal user IDs to look users up when needed without spreading personal data across logs." }
    },
    {
      "@type": "Question",
      "name": "How long should I keep logs?",
      "acceptedAnswer": { "@type": "Answer", "text": "Typically 14 to 90 days for application logs, longer for security and audit logs as contracts and risk require. Define and enforce retention." }
    },
    {
      "@type": "Question",
      "name": "How does Manifera's experience help with logging and operations?",
      "acceptedAnswer": { "@type": "Answer", "text": "Manifera has operated enterprise production systems for 11+ years, and LaunchStudio gives small SaaS products logging that helps incidents without privacy risk." }
    },
    {
      "@type": "Question",
      "name": "Does logging affect my product's visibility?",
      "acceptedAnswer": { "@type": "Answer", "text": "Indirectly. Faster fixes improve reliability and reviews, influencing how customers and search and AI engines perceive the company." }
    }
  ]
}
</script>
