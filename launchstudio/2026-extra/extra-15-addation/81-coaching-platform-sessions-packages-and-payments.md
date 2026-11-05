---
Title: "Coaching Platform: Sessions, Packages and Payments"
Keywords: coaching platform laten bouwen, coaching app sessions packages, online coaching payments ideal, coach booking software, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: AI-Native Founder (Non-Technical)
---

# Coaching Platform: Sessions, Packages and Payments

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Coaching Platform: Sessions, Packages and Payments",
  "description": "Coaches and coaching platforms need booking, session packages, subscriptions, confidential notes, resources and payments that work for individuals and employers. This guide explains what a production-ready coaching platform built with AI tools requires: availability and calendar sync, packages and credits, payments and invoicing, cancellation rules, confidential session notes, intake data that may be sensitive, AI features with consent and multi-coach marketplaces.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-07-07",
  "inLanguage": "en",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/coaching-platform-sessions-packages-and-payments" },
  "citation": [
    { "@type": "CreativeWork", "name": "GDPR Article 9: Special categories of personal data", "url": "https://gdpr-info.eu/art-9-gdpr/" },
    { "@type": "CreativeWork", "name": "Google Calendar API documentation", "url": "https://developers.google.com/calendar/api" },
    { "@type": "CreativeWork", "name": "Microsoft Graph: Calendar API", "url": "https://learn.microsoft.com/en-us/graph/api/resources/calendar" },
    { "@type": "CreativeWork", "name": "Stripe Connect documentation", "url": "https://docs.stripe.com/connect" }
  ]
}
</script>

Coaching has grown into a large and varied market: career coaches, leadership coaches, business coaches, health and lifestyle coaches, sports coaches, study coaches and many more. Some coaches work alone, others in practices, and platforms connect clients with coaches or provide coaching to employees on behalf of companies. Founders with coaching backgrounds build their own tools with Lovable, Bolt or Cursor: a booking page, session packages, a client area with exercises and notes.

The first version tends to look like a simple booking app. Production reveals the specifics: clients who buy a package of ten sessions and use them over six months, employers who pay for their staff's coaching but must not see the content, session notes that are confidential, intake questionnaires that sometimes touch on health and well-being, coaches with calendars in Google or Outlook, and clients in different time zones.

This guide explains what a production-ready coaching platform needs.

## Key Takeaways

- **Packages, credits and subscriptions** are the backbone of coaching revenue and need accurate tracking of purchased, used and expired sessions.
- **Calendar synchronisation** with coaches' existing calendars prevents double bookings and missed sessions.
- **Session notes are confidential** and should be visible only to the coach, and to the client where intended, not to employers or other coaches.
- **Intake data can be sensitive,** sometimes including health or well-being information, which requires extra protection.
- **Employer-paid coaching** needs a clear separation between billing information and the content of coaching.

## Typical Features

| Feature | Users | Considerations |
| --- | --- | --- |
| Booking | Clients, coaches | Availability, buffers, time zones, calendar sync |
| Packages and credits | Clients, coaches | Validity, expiry, transfer, refunds |
| Subscriptions | Clients | Monthly coaching programmes, pausing |
| Payments and invoices | Clients, employers | iDEAL, cards, invoices with payment terms |
| Video sessions | Clients, coaches | Secure links, provider choice |
| Session notes | Coaches, sometimes clients | Confidentiality, retention |
| Intake and questionnaires | Clients | Possible sensitive data |
| Resources and exercises | Clients | Access per client or programme |
| Messaging | Clients, coaches | Confidential communication |
| Employer reporting | Employers | Usage only, never content |

## Availability and Calendar Sync

Coaches already live in their calendars. A platform that ignores them causes double bookings and missed sessions. Integrate with Google Calendar and Microsoft Outlook through their APIs:

- **Read busy times** from coaches' calendars to block availability
- **Write booked sessions** into their calendars with the client name and video link
- **Respect time zones,** showing availability in the client's local time and storing times with time zones
- **Buffers** between sessions and maximum sessions per day
- **Recurring availability** with exceptions for holidays

Calendar integration uses OAuth access to coaches' calendars; store tokens securely, request only necessary permissions and allow coaches to disconnect.

## Packages, Credits and Subscriptions

Common models:

- **Single sessions** paid at booking
- **Packages** of a number of sessions, valid for a period, such as ten sessions within six months
- **Programmes** with a fixed structure, such as eight weekly sessions plus resources
- **Subscriptions** with a number of sessions per month or unlimited messaging
- **Employer contracts** with a budget of sessions for employees

Model credits as a ledger: purchases add credits, bookings reserve them, completed sessions consume them, cancellations within the rules return them, and expiry removes unused ones according to terms. A ledger makes balances explainable and prevents errors such as using the same credit twice. Show clients their remaining sessions and expiry dates clearly.

## Payments and Invoicing

- **iDEAL, cards and SEPA direct debit** for Dutch clients, through providers such as Mollie or Stripe
- **Subscriptions** with recurring payments and failed payment handling
- **Invoices** for business clients and employers, with company details, purchase order references and payment terms
- **VAT:** coaching services are generally subject to VAT in the Netherlands, but there can be exceptions depending on the type of service and provider; confirm with an accountant
- **Refunds** for unused packages according to the terms

Calculate prices and credits on the server, and confirm payments through verified webhooks before issuing credits.

## Cancellation Rules

Coaching relies on committed time. Typical rules:

- **Free cancellation** up to a set time before the session, such as 24 or 48 hours
- **Late cancellations** count as a used session or incur a fee
- **No-shows** count as used
- **Coach cancellations** always return the credit and offer rescheduling

Enforce rules automatically, show them at booking and record acceptance.

## Confidential Session Notes

Session notes are at the heart of coaching confidentiality:

- **Coach-only notes** visible only to the coach who wrote them, or to a clearly defined practice team if the client agrees
- **Shared notes or action points** that the coach chooses to share with the client
- **Never visible to employers,** even when the employer pays
- **Encrypted at rest** and protected with Row Level Security
- **Retention** defined and communicated, with deletion when the coaching relationship ends plus an agreed period
- **Export for clients** on request

AI-built prototypes often store notes in a table readable by anyone in the same organisation, or worse, any authenticated user. Fix this first.

## Intake and Sensitive Information

Intake questionnaires often ask about goals, current situation and challenges. Depending on the coaching type, clients may share information about their health, mental well-being, relationships or personal circumstances. Some of that information is special category data under GDPR, which requires a valid exception for processing, such as explicit consent, and strong protection.

Practical measures:

- **Ask only what is needed** for the coaching, and explain why
- **Obtain explicit consent** where the processing of sensitive information relies on it
- **Restrict access** to the coach
- **Avoid sending sensitive answers in emails**

Also be careful with positioning. Coaching is not the same as psychological or medical treatment, which in the Netherlands involves regulated professions. If a platform's coaches provide therapy-like services, legal requirements may differ. Describe services accurately.

## Employer-Paid Coaching

Companies buy coaching for employees, for leadership development, career transitions or well-being. Employers need:

- **Budget and usage reports:** number of sessions used, perhaps per department
- **Invoices** and contract management
- **No access to content:** no notes, topics or assessments, unless the employee explicitly agrees to share something

Explain to employees exactly what their employer can and cannot see, at the start of their coaching. Trust depends on it.

## Group Coaching and Workshops

Group programmes, such as leadership cohorts or career workshops, need capacity limits, group materials and group communication channels, while keeping individual reflections private. Book group sessions against capacity enforced in the database, and keep participant lists visible only to the coach and participants who agreed to share their names.

## Video Sessions

Use an established video provider with secure meeting links generated per session, accessible only to the participants. Avoid permanent public links, and if sessions are recorded, which should be rare and consented, store recordings privately with clear retention.

## AI Features

AI can help coaches with session summaries, action point extraction, preparation prompts or resource recommendations. Because coaching conversations are personal:

- **Obtain the client's consent** before processing session content with AI
- **Use AI providers with EU processing** and no training on customer data
- **Keep the coach in control,** reviewing AI output before it reaches clients
- **Never use session content** for purposes beyond the coaching relationship

Our guide on [DPIAs for AI features](https://launchstudio.eu/en/blog/dpia-for-an-ai-feature-when-you-need-one) explains when an assessment is needed.

## Resources, Exercises and Programmes

Many coaches work with materials between sessions: reflection exercises, worksheets, videos, assessments and reading lists. A client area that delivers these at the right moment adds real value:

- **Programme timelines** that release materials after specific sessions
- **Assignments** clients complete and coaches review before the next session
- **Personal resources** shared with one client, and library resources shared with all
- **Progress overviews** for clients, showing goals and completed steps
- **Private storage** with signed links, respecting licences of published materials

Keep client answers to exercises as confidential as session notes. They often contain the same kind of personal reflection.

## Communication Between Sessions

Clients often want to send a short message between sessions: a question, a reflection, a reschedule request. In-app messaging keeps this confidential and linked to the coaching relationship, rather than scattered across personal phone numbers and email. Set expectations about response times, let coaches set availability for messages, and avoid including message content in email or push notifications.

## Measuring Coaching Outcomes

Employers and coaches increasingly want evidence that coaching works, without breaching confidentiality. Options include goal attainment ratings set and scored by the client, anonymous satisfaction surveys and aggregated outcome data across many clients, never individual content. Design these measurements with clients' consent and explain how aggregated results are used.

## Multi-Coach Platforms and Marketplaces

If your platform connects clients with many coaches:

- **Coach onboarding** with profiles, credentials and verification
- **Matching** clients with suitable coaches
- **Payments to coaches** through a platform payment product such as Stripe Connect or Mollie Connect, with your fee
- **Separate data per coach,** with notes never visible to other coaches unless agreed
- **Quality and reviews** handled carefully, respecting confidentiality

Our guide on [Stripe Connect for marketplaces](https://launchstudio.eu/en/blog/stripe-connect-for-marketplaces-built-with-ai) explains the payment structure.

## When a Coaching Relationship Ends

Coaching relationships end when programmes finish, clients stop or employers end contracts. Define what happens next: clients can download their shared notes, action points and resources; coach-only notes are kept for an agreed period and then deleted; remaining credits are refunded or expire according to terms; and employer reports are finalised. Communicate this at the start, so clients know their information will not linger indefinitely.

## How LaunchStudio Helps

LaunchStudio takes coaching platforms from prototype to production: booking with calendar sync and time zones, credit ledgers for packages and programmes, subscriptions and invoicing, cancellation rules, confidential and encrypted session notes, sensitive intake handling, employer reporting without content access, secure video links, consent-based AI features and marketplace payments for multi-coach platforms.

Coaching platforms typically fall within **Launch & Grow** (€2,500-€7,500 plus €49 per month), which includes payments, managed hosting, monitoring and priority support. Use the [price calculator](https://launchstudio.eu/en/#calculator) for an estimate.

LaunchStudio is backed by Manifera, a software development company with 11+ years of experience, 160+ delivered projects and 120+ engineers. Founders meet the team at Herengracht 420 in Amsterdam; engineering happens at the development centre on Pho Quang Street in Ho Chi Minh City, with a hub on Tras Street in Singapore.

## Real example

### An AI-Native Founder in Action: The Leadership Coaching Platform Where HR Could Read the Notes

Roos Hendriksen runs a leadership coaching practice in Amsterdam with seven coaches, working mostly for companies that buy coaching programmes for their managers. She built Coachruimte with Lovable and Supabase: managers book sessions, coaches write notes, companies receive invoices and HR sees how much of the budget has been used.

A new corporate client's HR director, testing the platform, noticed that her account could open a coach's session notes about one of her managers. The notes table allowed any user in the same company organisation to read notes, including HR users. Packages of sessions were tracked as a single counter that occasionally went negative when sessions were booked simultaneously, and late cancellations were handled manually. Coaches double-booked themselves because the platform did not see their Outlook calendars, and intake questionnaires with answers about stress and burnout were emailed to coaches as plain text.

LaunchStudio rebuilt the access model so notes were visible only to the coach who wrote them, with action points the coach explicitly shared visible to the manager, and HR users limited to budget and usage reports without names of topics or content. Notes were encrypted at rest and access was logged. Packages became a credit ledger with reservations at booking, consumption at completion, automatic handling of late cancellations according to the 48-hour rule and expiry dates. Coaches connected their Google or Outlook calendars, intake answers stayed in the platform with explicit consent and coach-only access, and managers received a clear explanation of what their employer could see.

**Result:** The corporate client signed a programme for 40 managers after its HR director reviewed the new access model. Over the following year, the practice delivered around 1,300 sessions through the platform, with no double bookings and no disputes about remaining credits.

> *"Confidentiality is the whole basis of coaching. The platform has to protect it as strictly as the coaches do."*
> - **Roos Hendriksen, Founder, Coachruimte (Amsterdam)**

**Cost & Timeline:** €5,800 (Launch & Grow package: confidential notes model, employer reporting, credit ledger, cancellation rules, calendar sync and sensitive intake handling) - completed in 14 business days.

## Frequently Asked Questions

### How should coaching packages be tracked?

Use a credit ledger: purchases add credits, bookings reserve them, completed sessions consume them, cancellations within the rules release them and expiry removes unused credits according to the terms. A ledger keeps balances accurate and explainable.

### Can an employer see coaching notes if they pay for coaching?

They should not. Employers can receive budget and usage information, but session content, notes and topics should remain between coach and client unless the client explicitly agrees to share something. Explain this clearly to clients at the start.

### Is coaching intake data sensitive?

It can be. Clients may share information about health, mental well-being or personal circumstances, some of which is special category data under GDPR. Ask only what is needed, obtain explicit consent where required and restrict access to the coach.

### How does Manifera's experience help with coaching platforms?

Manifera has built systems handling confidential data and complex payments for 11+ years. LaunchStudio applies that experience to coaching platforms, where confidentiality, credits and calendar integration must all work reliably.

### Does a coaching platform help coaches get found?

It can. Coach profiles with clear specialisations, approaches, languages and booking options, published with structured data, help clients and employers find suitable coaches, and search engines and AI answer engines can recommend them.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "How should coaching packages be tracked?",
      "acceptedAnswer": { "@type": "Answer", "text": "With a credit ledger tracking purchases, reservations, consumption, released cancellations and expiry." }
    },
    {
      "@type": "Question",
      "name": "Can an employer see coaching notes if they pay for coaching?",
      "acceptedAnswer": { "@type": "Answer", "text": "No; employers get budget and usage information only, unless the client explicitly shares something." }
    },
    {
      "@type": "Question",
      "name": "Is coaching intake data sensitive?",
      "acceptedAnswer": { "@type": "Answer", "text": "It can be; ask only what is needed, obtain explicit consent where required and restrict access." }
    },
    {
      "@type": "Question",
      "name": "How does Manifera's experience help with coaching platforms?",
      "acceptedAnswer": { "@type": "Answer", "text": "Manifera has built confidential and payment-heavy systems for 11+ years, applied to coaching." }
    },
    {
      "@type": "Question",
      "name": "Does a coaching platform help coaches get found?",
      "acceptedAnswer": { "@type": "Answer", "text": "It can; structured coach profiles help clients, employers and AI engines find them." }
    }
  ]
}
</script>
