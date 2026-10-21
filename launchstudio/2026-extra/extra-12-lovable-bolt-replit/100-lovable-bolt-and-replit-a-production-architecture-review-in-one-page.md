---
Title: "Lovable, Bolt and Replit: A Production Architecture Review in One Page"
Keywords: production architecture review, AI-built app checklist, Lovable production readiness, Supabase review, SaaS due diligence, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: AI-Native Founder (Non-Technical)
---

# Lovable, Bolt and Replit: A Production Architecture Review in One Page

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Lovable, Bolt and Replit: A Production Architecture Review in One Page",
  "description": "One hundred articles condensed into a review a founder can run in a day: ten areas, the question that matters in each, the red flags that predict incidents, a simple scoring method, and how to turn the result into a ninety-day plan.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-03-31",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/lovable-bolt-and-replit-a-production-architecture-review-in-one-page" }
}
</script>

This series has covered a hundred topics, from Mollie versus Stripe to load testing, from row level security to handover documents. Each article stands on its own. Together they describe what it takes for a product built with Lovable, Bolt or Replit to become something businesses can depend on.

That is a lot to hold in mind, and few founders read a hundred articles before deciding what to fix next. This final article condenses the series into a single review: ten areas, the one question that matters most in each, the red flags that most reliably predict incidents, a scoring method, and a way to turn the result into a plan.

It is designed to be run in a day by a founder, ideally with someone who can read the code. It will not find everything. It will find the things that, across the products described in this series, most often became expensive.

## How to Run the Review

Set aside a day. Open the product, the Supabase dashboard, the hosting platform, the repository and your billing. For each of the ten areas below, answer the key question honestly, check the red flags, and give the area a score:

- **Green** — the area is in good shape; nothing urgent.
- **Amber** — gaps exist, but they are unlikely to cause an incident in the next three months or would be cheap to recover from.
- **Red** — a gap that could cause data exposure, data loss, lost revenue or a failed customer audit, or that would be expensive or impossible to reverse.

Write one or two sentences of evidence per score. "Backups: red — automated backups enabled, never restored, no copy outside Supabase" is useful; "backups: probably fine" is not.

Be strict. The point of the review is to find the red areas before a customer, an attacker or an auditor does.

## 1. Code and Change Control

**Key question:** if the last change broke something, could you undo it in five minutes and see exactly what changed?

**Red flags:**
- The code exists only inside the builder tool, with no Git repository the company owns.
- Changes go straight to production without a test or review, from an editing session.
- Nobody reads the diff of AI-generated changes; large changes touch dozens of files.
- No tests for authorisation, money or the main flow.

Most other areas depend on this one. A product whose code is in a repository, with small reviewed changes, a short test suite and a CI gate, can fix everything else safely. The Git, code review, tests and CI articles in this series describe the minimum.

## 2. Data Separation Between Customers

**Key question:** can a user of one customer, by any means — interface, API, changed ID in a URL — see or change another customer's data?

**Red flags:**
- Tables without row level security, or with policies that are `true` for authenticated users.
- Organisation IDs taken from the request rather than from the user's membership.
- The service role key in frontend code, a public repository or an integration partner's hands.
- No test that signs in as one organisation and attempts to read another's data.

This is the area where AI-built products fail most often and most seriously. The IDOR, row level security, team membership and roles articles in this series describe the fixes; the cross-organisation test is the evidence.

## 3. Authentication and Access

**Key question:** when someone leaves a customer's organisation, or your own company, does their access actually end?

**Red flags:**
- Removing a user hides them from a list but leaves their membership and sessions intact.
- Invitation links that never expire or work for anyone who receives them.
- Password reset flows that reveal whether an account exists or accept reused tokens.
- Admin functions protected only by hiding buttons.
- Critical accounts — domain, hosting, database — owned by one person.

The session, password reset, invitations, SSO and admin panel articles cover this area.

## 4. Secrets and Configuration

**Key question:** if your repository and your frontend bundle were published tomorrow, would any secret be in them?

**Red flags:**
- API keys or service role keys in client code, committed files or old commits.
- One set of credentials shared by development and production.
- Keys that have never been rotated, including ones held by former collaborators.
- No list of which secrets exist and what each one can do.

The secret rotation, environment variables and Replit secrets articles describe how to reach green.

## 5. Payments and Money

**Key question:** if your payment provider and your database disagree, would you know — and which one would be right?

**Red flags:**
- Webhooks accepted without signature verification.
- No idempotency, so a retried webhook or double click creates a second charge or entitlement.
- Access granted by the frontend after checkout rather than by a verified server event.
- No monthly reconciliation between provider, database and accounting.
- VAT, invoice numbering and credit notes handled ad hoc.

The eight payment articles at the start of this series, and the accounting integration article, cover the details. In this area, red usually means money is already being lost quietly.

## 6. Backups, Recovery and Continuity

**Key question:** when did you last restore a backup, and how long did it take?

**Red flags:**
- Backups enabled but never restored.
- No copy of the database or uploaded files outside the main platform.
- Uploaded files on a container filesystem rather than object storage.
- No plan for the loss of a critical supplier — email, payments, AI provider, the builder itself.

A product that has never restored a backup does not know whether it has one. The backups, object storage and vendor lock-in articles describe what green looks like.

## 7. Reliability and Operations

**Key question:** if the product broke at seven on a Monday morning, who would know first — you or your customers?

**Red flags:**
- No uptime monitoring from outside the platform.
- Scheduled jobs and background work without run records or alerts on absence.
- Logs that cannot be searched by customer or request.
- Releases that go to all customers at once, with rollback as the only remedy.
- No status page or agreed way to inform customers during an incident.

The monitoring, logs, cron, background work, feature flags and status page articles cover this area.

## 8. Performance and Scale

**Key question:** how does the product behave with your largest customer's data, at their busiest hour — and with a customer twice that size?

**Red flags:**
- Lists that load every row; queries without indexes on the columns they filter.
- Row level security functions that run a subquery per row.
- Database connections opened directly rather than through the pooler.
- Third-party calls inside user requests.
- No load test before onboarding a customer larger than any before.

The indexes, pagination, connection pooling and load testing articles describe how to find and fix these before customers do.

## 9. Privacy and Compliance

**Key question:** if a customer's data protection officer asked tomorrow for your processing agreement, subprocessor list and retention periods, could you send them within a day?

**Red flags:**
- No processing agreement template, no subprocessor list, no records of processing.
- No defined retention periods; data kept forever by default.
- Analytics, session replay or AI logging sending personal data to unlisted providers.
- No tested process for deletion requests, access requests or data breach notification.
- An AI feature in a context covered by the EU AI Act without a documented assessment.
- No accessibility review although customers fall under the European Accessibility Act.

The compliance articles in the middle of this series, and the analytics and exports articles, describe the documents and processes that make this area green.

## 10. Product Maturity for Larger Customers

**Key question:** what would a customer with ten times your average size need that you cannot give them today?

**Red flags:**
- One role per user; no scoping by location or department.
- No SSO, while prospects send questionnaires asking for it.
- No full data export; manual queries run to answer customer requests.
- Imports that write directly to production without preview.
- An API that is the auto-generated database interface rather than a versioned contract.
- AI features without an evaluation set, so model changes are untested.
- Documents regenerated on download rather than stored when issued.

The final articles in this series — i18n, teams, roles, SSO, imports, exports, documents, accounting integrations, API versioning, AI evaluation — describe what larger customers typically ask for, in roughly the order they ask.

## Turning Scores Into a Plan

A review produces a list. A plan decides the order. Three rules make the order sensible.

**Red before amber, and irreversible before reversible.** Data exposure, data loss and uncollectable money cannot be undone; a slow page can. Fix the reds in areas two, four, five and six before anything else, even if they look less urgent than a customer's feature request.

**Foundations before features.** Area one — code in a repository, tests, review — makes every later fix safer and faster. If it is red, it comes first, because changing anything else without it is how new incidents are created.

**Follow the revenue for the rest.** Among ambers and area ten, prioritise what the next significant customer or the next renewal depends on. A prospect waiting for SSO justifies the SSO work this quarter; a theoretical enterprise feature does not.

Put the result into a ninety-day plan: reds in the first month, the ambers that block revenue in the second, the remaining ambers and the next maturity step in the third. Estimate each item in days, assign each to a person, and review progress every two weeks. Most products of the size described in this series can move every red to green within the first month.

## What Moving From Red to Green Typically Costs

Founders reasonably ask what the plan will cost before committing to it. Across the products described in this series, the effort per area falls into fairly consistent ranges for a small or medium Lovable, Bolt or Replit product.

| Area | Typical effort from red to green |
|---|---|
| Code and change control | 1–3 days: repository, small test suite, CI gate |
| Data separation | 2–4 days: policy rewrite, membership model, cross-organisation tests |
| Authentication and access | 1–3 days: removal, invitations, session handling, admin checks |
| Secrets and configuration | 0.5–2 days: rotation, environment separation, inventory |
| Payments and money | 2–5 days: webhook verification, idempotency, reconciliation |
| Backups and continuity | 1–3 days: off-platform exports, restore test, exit plans |
| Reliability and operations | 1–3 days: monitoring, job alerts, searchable logs, flags |
| Performance and scale | 2–5 days: indexes, pagination, pooling, load test |
| Privacy and compliance | 2–4 days: agreements, registers, retention, analytics clean-up |
| Larger-customer maturity | Per feature: 2–6 days each for roles, SSO, exports, API and similar |

The figures are effort, not elapsed time, and they assume the code is in a repository; if area one is red, it comes first and makes the others cheaper. A product with three reds and several ambers typically needs ten to twenty days of work to reach a state a demanding customer will accept — a fraction of a rebuild, and usually less than the value of the contract that prompted the review.

The numbers also explain why the order matters. Fixing data separation costs a few days before an incident; after one, it costs the same few days plus notification, investigation, legal advice and a customer relationship.

## Who Should Do the Review

A founder can answer most key questions alone, and doing so is valuable: it reveals what the founder does not know about their own product. The red flags in areas two, three, four and eight, however, require reading code, policies and query plans. Someone who has seen these problems in other products finds them in hours rather than days, and recognises the ones that look harmless.

The best arrangement is usually both: the founder answers the key questions and gathers the evidence, then someone experienced reviews the code-level red flags and challenges the scores. An outside review also produces a document that customers, investors and acquirers increasingly ask to see.

## Repeat It

A review is a snapshot. Products built with AI tools change quickly, and an area that was green in spring can turn amber by autumn after a few months of fast feature work.

Repeat the review every six months, and before any moment that raises the stakes: a large customer's onboarding, a procurement process, an investment round, an acquisition conversation, a regulatory change. Keep each review's scores and evidence, so the next one starts from the last and the trend is visible.

The goal is not a product without risk. It is a product whose risks are known, ranked and shrinking — which is what customers, investors and auditors are really asking about when they ask whether it is "production ready".

## Setting This Up

For a Lovable, Bolt or Replit product, a review following this structure is typically one to two days: the ten areas scored green, amber or red with written evidence, code-level checks of data separation, authentication, secrets and performance by someone experienced, a cross-organisation access test, a backup restore test, a review of payment webhooks and reconciliation, a privacy document check, a list of what larger customers would need, a ninety-day plan ordered by irreversibility, foundations and revenue, and a date for the next review.

LaunchStudio runs this review for founders who want to know where they stand, and then does the work that turns red into green — fixed price, from €800 for the Launch Ready package. Behind it is Manifera — eleven years, 160+ projects, 120+ engineers, from Herengracht 420 in Amsterdam and Ho Chi Minh City.

[Ask us for a production architecture review](https://launchstudio.eu/en/#contact) and receive the scores, the evidence and the ninety-day plan.

## Real example

### Three Reds Before a School Board Said Yes

Sophie Mulder built Leerlingvolg in Lovable: pupil progress tracking, parent communication and support plans for primary schools, used by 85 schools.

A school board responsible for 40 schools wanted to adopt the product across all of them, subject to a review by its information security and privacy officers. Sophie had a questionnaire with 120 questions and a deadline of six weeks, and no clear idea which answers would be a problem.

The review took two days. Three areas scored red. Six tables containing pupil data had row level security policies that allowed any authenticated teacher to read records from other schools through the API, although the interface never showed them. Backups had never been restored, and uploaded support plans lived in a single storage bucket with no copy elsewhere. And there was no processing agreement template, no subprocessor list and no retention periods — for a product holding data about children, including special educational needs. Nine areas scored amber, among them untested scheduled jobs, keys shared between environments and an analytics script with session replay switched on.

**Result:** the ninety-day plan put the three reds in the first three weeks: policies rewritten and verified with a cross-school test suite, nightly encrypted exports of the database and files to a second provider with a timed restore, and a processing agreement, subprocessor list, records of processing and retention register drafted with a privacy lawyer. Session replay was removed and environments separated in the same period. The questionnaire was answered in week five with evidence for each answer, the board's officers raised four minor points, and the contract for 40 schools was signed in week seven — roughly doubling the product's revenue. A second review six months later scored no red areas.

> *"I knew there would be questions I could not answer. I did not know that teachers could read other schools' pupil files through the API. Two days of review told me exactly where to start."*
> — **Sophie Mulder, Founder, Leerlingvolg (Amersfoort)**

**Cost & Timeline:** €1,800 (production architecture review across ten areas with code-level checks, cross-organisation access test, backup restore test, privacy document assessment, scored report with evidence and ninety-day plan) — completed in 2 business days.

## Frequently Asked Questions

### What is a production architecture review?

A structured check of the areas that most often cause incidents in AI-built products — code control, data separation, access, secrets, payments, recovery, operations, performance, privacy and readiness for larger customers — each scored with evidence.

### How long does a review take?

One to two days for most Lovable, Bolt or Replit products: a day for a founder to answer the key questions and gather evidence, and time for someone experienced to check the code-level red flags.

### What should be fixed first?

Red areas that are irreversible — data exposure, data loss, uncollectable money — and the foundation of code control, then whatever the next significant customer or renewal depends on.

### Can a founder run the review alone?

Partly. A founder can answer the key questions; data separation, authentication, secrets and performance require reading code and policies, where an experienced reviewer finds problems much faster.

### How often should the review be repeated?

Every six months, and before any high-stakes moment such as a large customer's onboarding, a procurement process, an investment round or an acquisition.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What is a production architecture review for an AI-built app?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "A scored check of code control, data separation, access, secrets, payments, recovery, operations, performance, privacy and enterprise readiness, with evidence."
      }
    },
    {
      "@type": "Question",
      "name": "How long does a production readiness review take?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Typically one to two days, combining the founder's answers with an experienced check of code-level risks."
      }
    },
    {
      "@type": "Question",
      "name": "What should be fixed first after a review?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Irreversible red areas and code control first, then what the next significant customer or renewal depends on."
      }
    },
    {
      "@type": "Question",
      "name": "Can founders review their own product?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Partly — code-level areas like data separation, authentication, secrets and performance benefit from an experienced reviewer."
      }
    },
    {
      "@type": "Question",
      "name": "How often should a production review be repeated?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Every six months and before high-stakes moments such as large onboardings, procurement, investment or acquisition."
      }
    }
  ]
}
</script>
