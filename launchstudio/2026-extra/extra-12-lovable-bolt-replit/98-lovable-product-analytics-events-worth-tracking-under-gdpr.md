---
Title: "Lovable Product Analytics: Events Worth Tracking Under GDPR"
Keywords: lovable product analytics, event tracking, GDPR analytics, session replay, activation metrics, account health, PostHog EU, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: AI-Native Founder (Non-Technical)
---

# Lovable Product Analytics: Events Worth Tracking Under GDPR

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Lovable Product Analytics: Events Worth Tracking Under GDPR",
  "description": "Most AI-built products either track nothing useful or track far too much, including data they should never have collected. Which questions product analytics should answer, how to design a small tracking plan, what never belongs in an event, and how to stay on the right side of GDPR and Dutch cookie rules.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-03-27",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/lovable-product-analytics-events-worth-tracking-under-gdpr" }
}
</script>

Ask a founder of an AI-built B2B product which customers are actively using the product, which features nobody touches, and which accounts are quietly heading for cancellation, and the answer is usually a guess. Either nothing is tracked, or an analytics script was added during the build that records every click on every page — and still cannot answer the question, because the events were never designed.

The second situation is often worse than the first. Analytics tools added with one line of code capture page titles, URLs, form contents and, with session replay switched on, recordings of entire screens. In a product that holds customers' personal data, that means sending names, addresses, health information or financial details to an analytics provider — frequently outside the EU, frequently without a processing agreement, and almost always without the customer knowing.

Product analytics done well is small, deliberate and privacy-conscious. This article covers the questions analytics should answer for a B2B product, how to design events and a tracking plan, what must never be in an event, session replay, consent under Dutch rules, choosing a tool, and turning the data into decisions.

## Start With Questions, Not Events

Analytics exists to answer questions. Write them down first; the events follow from them.

For most B2B products, the important questions are few:

- **Activation.** Do new accounts reach the moment where the product becomes useful to them — the first invoice sent, the first schedule published, the first report shared — and how long does it take?
- **Engagement per account.** Which organisations use the product weekly, which are declining, which have stopped?
- **Feature adoption.** Which features are used, by what share of accounts, and which were built and are ignored?
- **Friction.** Where do users abandon a flow — onboarding, import, checkout — and where do errors cluster?
- **Expansion signals.** Which accounts are approaching plan limits, adding users or using premium features heavily?

Each question points to a handful of events. A product with fifteen to thirty well-designed events can answer all of them. A product with four hundred automatically captured events usually cannot answer any of them reliably.

## Design Events Deliberately

An event records that something meaningful happened. Good events share a consistent structure.

**A clear name in the form object_action** — `invoice_sent`, `schedule_published`, `import_completed`, `member_invited`. Past tense, describing a business action rather than a click: "invoice sent" is meaningful, "button clicked" is not.

**The account and the user**, as identifiers. In B2B, the account — the organisation — is the unit that matters most: it is the customer, the subscription and the churn risk. Every event carries the organisation ID; most analysis is per organisation, not per person.

**A small set of properties that answer the questions** — the plan, the number of lines on the invoice, whether the import came from a template, the source of the action. Properties describe the event, not the people or data involved.

**A timestamp from the server**, not the user's device.

Write the events in a tracking plan — a single document or file listing every event, its properties, when it fires and which question it serves. When someone, or an AI assistant, wants to add an event, the tracking plan is where it is designed and reviewed. Without it, five sessions produce `invoice_sent`, `InvoiceSent`, `sent_invoice`, `invoice-send` and `send_invoice_click`, and no report can combine them.

## Prefer Server-Side Events for What Matters

Events can be sent from the browser or from your server.

**Browser events** capture what the user sees and does in the interface — a page viewed, a step in a wizard, a filter used. They are blocked by ad blockers and privacy settings in a significant share of browsers, and they can be manipulated.

**Server events** are sent when the action actually happens in your backend — the invoice was really sent, the import really completed, the subscription really changed. They are complete, reliable and not affected by blockers.

For the events that answer business questions — activation, engagement, adoption, expansion — send them from the server, in the same function that performs the action. Use browser events only for interface questions, such as where users abandon a multi-step flow.

A practical pattern is to write events to your own table first and forward them to the analytics tool from a background job. Your own copy is complete, queryable alongside your data, and survives a change of analytics provider.

## What Must Never Be in an Event

This is where AI-built products most often go wrong, and the consequences are regulatory rather than technical.

**No personal data of your customers' clients, patients or employees.** Names, email addresses, phone numbers, addresses, dates of birth, notes, diagnoses, salaries. If your product is a care, HR, finance or legal tool, an event containing such data sends special category or sensitive data to a third party.

**No free text.** Search queries, form contents, notes and messages contain personal data unpredictably. Record that a search happened and how many results it returned, not what was searched.

**No URLs or page titles containing identifiers or names.** `/clients/jan-de-vries/medical-history` as a page view is personal data. Configure the analytics tool to strip or normalise paths — `/clients/:id/medical-history` — before anything is sent.

**No email addresses as user identifiers.** Use your internal user ID, or a pseudonymous ID derived from it.

Automatic capture features — "autocapture" of every click, form field and text on screen — are where most of this leaks. Disable them, or restrict them to explicitly allowed elements, in any product that displays personal data.

## Session Replay Deserves Special Caution

Session replay tools record what users see and do — mouse movements, clicks, scrolling and the screen content — and play it back like a video. They are genuinely useful for understanding confusing interfaces.

In a product that displays personal data, they are also a recording of that data. A replay of a care coordinator using a client file contains the client file. Most tools mask form inputs by default but not other text on the screen, and the masking configuration is easy to get wrong.

If you use session replay at all: mask all text by default and unmask only specific static elements; exclude screens that show personal or sensitive data entirely; record only a sample of sessions; keep recordings for a short period; and document it in your privacy information and processing records. For products handling health, financial or children's data, the safest answer is not to use session replay in the application at all, and to use it only on public marketing pages where no customer data appears.

## Consent and the Dutch Rules

Two sets of rules apply to product analytics, and they are often confused.

**The cookie rules** in the Dutch Telecommunications Act — the implementation of the European ePrivacy rules — govern storing or reading information on a user's device, including analytics cookies and similar identifiers. Analytics cookies generally require consent, with a narrow exception for analytics with little or no impact on privacy. The Dutch Data Protection Authority has described conditions for that exception: among others, a processing agreement with the provider, masked or truncated IP addresses, no sharing of data with the provider for its own purposes, and no tracking across sites. Analytics configured this way can be used without a consent banner; analytics that does not meet the conditions needs consent first. The cookie consent article in extra-11 covers the banner side.

**The GDPR** governs the processing of personal data in the events themselves, wherever they are stored. For in-app analytics in a B2B product, the usual basis is legitimate interest in improving and maintaining the service, provided the analytics is limited to what is necessary, does not contain sensitive data, and is described transparently.

Server-side events, written to your own database without cookies and forwarded to an EU-hosted tool under a processing agreement, often avoid the cookie question entirely while staying within GDPR — another reason to prefer them.

Your business customers will also ask. Analytics tools are subprocessors when they receive personal data such as user IDs; list them, as the subprocessors article in this series describes, and offer customers who require it the option to exclude their organisation from analytics.

## Choosing a Tool

The choice depends more on hosting and data handling than on features.

**EU-hosted product analytics** — PostHog in its EU region, or self-hosted, and comparable tools — offer events, funnels, retention and feature flags, with a processing agreement and data in Europe.

**Privacy-focused web analytics** — Plausible, Simple Analytics, a self-hosted Matomo — are excellent for marketing pages and aggregate traffic, and less suited to per-account product analytics.

**Your own database plus a dashboard tool** — events in a Postgres table, queried with SQL or a BI tool. For a small product with server-side events, this is often enough for the first year and keeps all data under your control.

Whichever you choose, check the hosting region, the processing agreement, whether the provider uses your data for its own purposes, and how deletion works when a user or customer asks for it.

## Turn Data Into Decisions

Analytics only pays for itself when someone looks at it and acts. Three views cover most of what a small B2B team needs.

**An activation funnel** — signed up, completed setup, performed the core action for the first time, performed it again in the second week — with the median time between steps. Improve the step where most accounts stop.

**Account health** — per organisation: active users this week compared with the past month, core actions per week, last activity date, features used. Declining accounts are a list for a phone call, often months before a cancellation email.

**Feature adoption** — the share of active accounts using each feature in the past month. Features used by almost nobody are candidates for improvement, explanation or removal, which also reduces what the product has to maintain.

Review them on a fixed rhythm — weekly for account health, monthly for adoption — and record what you decided. A dashboard nobody opens is just a cost and a privacy liability.

## Retention and Deletion

Analytics data tends to be kept forever by default, because nobody decides otherwise. Under GDPR it must be kept no longer than necessary, and it must be included when someone exercises their rights.

**Set a retention period.** Detailed events with user identifiers rarely need to be kept longer than twelve to twenty-five months — long enough to compare a season with the same season last year. After that, aggregate them per organisation and week and delete the individual events. Record the decision in the retention register described in the data retention article in this series.

**Include analytics in deletion.** When a user's account is deleted, or a customer leaves and their data is removed, their events must go too — in your own table and at the analytics provider. Most providers offer deletion by user ID through an API; call it from the same deletion process that removes the account, as the GDPR erasure article in extra-11 describes.

**Include analytics in access requests.** If a person asks what data you hold about them, events linked to their user ID are part of the answer. Pseudonymous IDs reduce the risk of the data but do not take it outside GDPR, because you can link them back.

## Share Usage With Your Customers

The same data that tells you which accounts are thriving is valuable to your customers' administrators — and sharing it is one of the few analytics features that also helps sell the product.

A usage page per organisation — active users this month, the core actions performed, the features used, perhaps the time saved — answers the question a customer's manager asks at renewal: "Are we actually using this?" It helps the champion inside the customer justify the subscription, and it shows administrators which colleagues have not started using the product yet.

Keep it at the level of the organisation's own data, never compared with named other customers, and never showing more about individual employees than their administrator is entitled to see. Aggregated benchmarks — "organisations of your size typically send 40 invoices a month" — can be useful when there are enough customers to make them anonymous.

## Data Quality

Analytics data is only as good as the events. Three habits keep it trustworthy.

**Validate events against the tracking plan**, ideally with a typed function per event in code, so an event with a missing property or a wrong name fails in development rather than polluting production data.

**Test events like features.** When the invoice flow changes, check that `invoice_sent` still fires once — not zero times, not twice.

**Exclude internal and test traffic** — your own organisation, demo accounts, load tests — or every metric is distorted, especially in a product with few customers.

## Setting This Up

For a Lovable product, this is typically two to four days: the business questions written down, a tracking plan of fifteen to thirty events named as object and action with account and user identifiers and a small set of properties, server-side events for business actions written to your own table and forwarded by a background job, browser events only for interface questions, no personal data, free text or identifying URLs in events, autocapture disabled or restricted, session replay excluded from sensitive screens or not used in the application, a cookie and consent assessment against the Dutch rules, an EU-hosted tool under a processing agreement listed as a subprocessor, an opt-out for customers who require it, activation, account health and adoption views with a review rhythm, typed event validation, event tests, and internal traffic excluded.

LaunchStudio sets this up so founders can see which customers are thriving without collecting what they should not. Behind it is Manifera — eleven years, 160+ projects, 120+ engineers, from Herengracht 420 in Amsterdam.

[Ask us what your analytics script is actually sending](https://launchstudio.eu/en/#contact).

## Real example

### Session Recordings of Sick Leave Notes

Naomi Dekker built Verzuimregistratie in Lovable: sick leave and absence registration for small and medium businesses, used by 160 companies to record absences, return-to-work agreements and contact with occupational health services.

An analytics script had been added during the build with default settings: autocapture of every click and page, and session replay switched on. Page URLs contained employee names. Session recordings captured the absence screens — including the free-text notes in which managers recorded what employees had told them about their health. The data went to a provider outside the EU, with no processing agreement and no mention in the privacy statement.

It came to light when the data protection officer of a customer with 400 employees asked for the list of subprocessors and how health-related data was handled. At the same time, Naomi could not answer a simpler question from her own board: which of the 160 companies were actually using the product each week. The tool held 140 differently named events and no reliable organisation identifier.

Three business days: session replay removed from the application entirely and autocapture disabled; the existing data at the old provider deleted, with written confirmation; a tracking plan of 22 server-side events named as object and action, each carrying pseudonymous organisation and user IDs and no names, notes or identifying URLs; events written to a table in the product's own database and forwarded to an EU-hosted analytics tool under a processing agreement, configured to meet the Dutch Data Protection Authority's conditions for low-impact analytics; an opt-out per customer organisation; an assessment documented in the processing register, an updated subprocessor list and privacy statement; activation and account health views; and typed event functions with tests.

**Result:** the incident was assessed with the help of a privacy lawyer and reported to the Autoriteit Persoonsgegevens, and affected customers were informed; the customer's data protection officer accepted the remediation and the customer stayed. The account health view identified nine companies whose usage had dropped sharply; Naomi called each of them, and seven were still customers a year later. The share of new accounts registering their first absence within a week rose from 48% to 71% after the onboarding step where most stopped was redesigned.

> *"I added analytics to find out which customers were active. What it actually did was record managers' notes about their employees' health and send them abroad — and it still could not tell me which customers were active."*
> — **Naomi Dekker, Founder, Verzuimregistratie (Ede)**

**Cost & Timeline:** €3,400 (removal of session replay and autocapture, deletion at the previous provider, 22-event tracking plan with server-side pseudonymous events, EU-hosted analytics with processing agreement, customer opt-out, processing register and privacy documentation, activation and account health views, event validation and tests) — completed in 3 business days.

## Frequently Asked Questions

### Which events should a B2B product track?

The events that answer a few business questions: activation, engagement per account, feature adoption, friction in key flows and expansion signals. Fifteen to thirty well-designed events are usually enough.

### Should events be sent from the browser or the server?

Business actions from the server, where they are complete and reliable; interface interactions from the browser only where needed. Writing events to your own table first keeps a full copy under your control.

### What must never be included in analytics events?

Personal data of your customers' clients or employees, free text such as notes and search queries, identifying URLs and email addresses. Use internal or pseudonymous IDs instead.

### Is session replay allowed under GDPR?

It can be, with strict masking, exclusion of sensitive screens, sampling, short retention and transparency. For products handling health, financial or children's data, it is safer not to use it inside the application.

### Do I need consent for product analytics in the Netherlands?

Analytics cookies generally require consent, unless the analytics meets the Dutch Data Protection Authority's conditions for low privacy impact. Server-side events without cookies, processed under GDPR with a processing agreement, often avoid the cookie question.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What should a B2B SaaS track in product analytics?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Events answering activation, per-account engagement, feature adoption, friction and expansion questions — usually fifteen to thirty."
      }
    },
    {
      "@type": "Question",
      "name": "Should analytics events be client-side or server-side?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Business actions server-side for completeness and reliability; browser events only for interface questions."
      }
    },
    {
      "@type": "Question",
      "name": "What data must stay out of analytics events?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Personal data of end clients or employees, free text, identifying URLs and email addresses — use pseudonymous IDs."
      }
    },
    {
      "@type": "Question",
      "name": "Is session replay GDPR compliant?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Only with strict masking, excluded sensitive screens, sampling, short retention and transparency; avoid it in apps with health or financial data."
      }
    },
    {
      "@type": "Question",
      "name": "Do product analytics need cookie consent in the Netherlands?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Generally yes for analytics cookies, unless they meet the Dutch DPA's low-impact conditions; cookieless server-side events often avoid the issue."
      }
    }
  ]
}
</script>
