---
Title: "Language School Booking and Payments App"
Keywords: taalschool software, language school booking system, cursus inschrijving betaling app, crkbo btw vrijstelling software, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: AI-Native Founder (Non-Technical)
---

# Language School Booking and Payments App

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Language School Booking and Payments App",
  "description": "Language schools and course providers manage levels, placement tests, group courses, private lessons, attendance, certificates and payments from students, employers and funders. This guide explains what a production-ready booking and payments app for a Dutch language school needs: course and level structure, capacity, teacher availability, instalments and employer invoices, VAT considerations for education, attendance records, multilingual interfaces and data protection.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-07-04",
  "inLanguage": "en",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/language-school-booking-and-payments-app" },
  "citation": [
    { "@type": "CreativeWork", "name": "Council of Europe: Common European Framework of Reference for Languages", "url": "https://www.coe.int/en/web/common-european-framework-reference-languages" },
    { "@type": "CreativeWork", "name": "CRKBO: Central Register for Short Vocational Education", "url": "https://www.crkbo.nl/" },
    { "@type": "CreativeWork", "name": "DUO: Inburgering", "url": "https://www.inburgeren.nl/" },
    { "@type": "CreativeWork", "name": "Belastingdienst: VAT exemption for education", "url": "https://www.belastingdienst.nl/" }
  ]
}
</script>

Language schools come in many shapes: small schools teaching Dutch to expats and newcomers, schools offering English or Spanish to professionals, in-company training providers, online tutors, and providers of civic integration courses. Most share the same administrative burden: placing students at the right level, filling groups, scheduling teachers, collecting payments from students, employers or funders, tracking attendance and issuing certificates.

Founders with teaching experience increasingly build their own systems with Lovable, Bolt or Cursor. The first version usually handles course listings and online sign-up with payment. Production adds the complexity that schools actually face: courses that run for weeks with instalments, companies paying for employees, attendance records that funders or employers require, teachers with availability constraints, and students who need the interface in several languages.

This guide explains what a production-ready language school app needs. It is general information; check tax and funding rules with advisers and the relevant authorities.

## Key Takeaways

- **Course structure revolves around levels,** commonly expressed using the Common European Framework of Reference (CEFR), from A1 to C2.
- **Group courses need capacity management;** private lessons need teacher availability and booking rules.
- **Payments come from several sources:** students paying in instalments, employers paying invoices and sometimes funding arrangements.
- **VAT treatment of education can differ,** for example depending on registration in the CRKBO register; confirm with an accountant.
- **Attendance and progress records** often matter for employers, funders and certificates, and should be accurate and auditable.

## Course and Level Structure

| Element | Description |
| --- | --- |
| Language and level | For example Dutch A2, English B2, based on CEFR |
| Course type | Group course, private lessons, intensive course, in-company training |
| Format | Classroom, online, hybrid |
| Schedule | Number of sessions, day and time, start and end dates |
| Location | Classroom, company location, online meeting link |
| Capacity | Minimum and maximum participants |
| Price | Course fee, materials, exam fees |

A placement step often precedes enrolment: a short online test, an intake conversation or both. The result determines which courses a student can book. Store placement results with the date and method, so teachers and students understand the basis for the level.

## Group Courses and Capacity

Group courses have both maximum and minimum capacity. A course with too few participants may be cancelled or merged; a full course needs a waiting list. Requirements:

- **Capacity enforced in the database,** so concurrent enrolments cannot exceed the maximum
- **Waiting lists** with automatic offers when places become available, using temporary holds
- **Minimum participant monitoring,** with a decision date for confirming or cancelling the course
- **Communication** to enrolled students about confirmation, changes and cancellations
- **Refunds or transfers** when courses are cancelled

The patterns from [preventing double bookings](https://launchstudio.eu/en/blog/preventing-double-bookings-in-a-booking-app) apply directly to course capacity.

## Private Lessons and Teacher Availability

For private or small-group lessons:

- **Teacher availability** as recurring weekly patterns with exceptions
- **Lesson duration and buffers** between lessons
- **Booking rules,** such as minimum notice and cancellation deadlines
- **Lesson packages,** for example ten lessons purchased in advance, with remaining balance tracked
- **Online lesson links** generated per booking

Time zones matter for online lessons with students abroad. Store times with time zones and show them clearly in each person's local time.

## Payments and Instalments

Language courses can be expensive enough that students prefer to pay in instalments:

- **Full payment at enrolment** by iDEAL or card
- **Instalments** through SEPA direct debit with a mandate collected at enrolment
- **Deposit plus remainder** before the course starts
- **Lesson packages** paid upfront and consumed over time

Handle failed payments with reminders and clear consequences, such as access to course materials pausing after a grace period. Calculate amounts on the server and store them in cents.

## Employer-Paid Courses

Many students, especially expats and professionals, have their course paid by their employer. Support:

- **Enrolment with company details,** including a contact person, purchase order number and invoice address
- **Invoices to companies** with payment terms, rather than payment at checkout
- **Group enrolments** of several employees
- **Reports to employers** on attendance and progress, with the student's knowledge
- **Validation of VAT numbers** for business customers in other EU countries

Be transparent with students about what information is shared with their employer, and share only what the agreement requires.

## VAT and Education

VAT on education in the Netherlands can depend on the type of education and the provider. Some vocational education by providers registered in the CRKBO register may be exempt from VAT, while other courses fall under VAT. The details matter for prices, invoices and reporting, so:

- **Configure VAT treatment per course type,** as advised by your accountant
- **Show correct prices** to consumers and businesses
- **Issue invoices** that reflect the applicable treatment

Our guide on [VAT and invoices for SaaS in the Netherlands](https://launchstudio.eu/en/blog/btw-and-invoices-for-saas-in-the-netherlands-what-your-checkout-needs) covers invoice requirements in general.

## Civic Integration Courses

Schools offering civic integration courses for newcomers work within a specific framework, with rules on quality marks, funding arrangements and reporting set by Dutch authorities. If your app serves these schools, involve them closely in requirements, because funding, attendance and reporting rules affect enrolment, payment and record-keeping. Check current information on the official integration website and with the relevant agencies.

## Attendance, Progress and Certificates

- **Attendance per session,** recorded by teachers, with reasons for absence where relevant
- **Progress notes and assessments** linked to CEFR levels
- **Certificates** issued when completion criteria are met, with verification details
- **Reports** for students, employers and, where applicable, funders
- **Audit trail** of changes to attendance and results, because these records can have financial or legal consequences

## Course Materials and Online Learning

Many language schools combine classroom or live online lessons with materials between sessions: exercises, audio, video, vocabulary lists and homework. If your app provides these:

- **Store materials in private storage,** available only to students enrolled in the course, with signed links
- **Respect licences** for textbooks and published materials, which often restrict copying and sharing
- **Track homework submission** and teacher feedback per student
- **Keep materials available** for a defined period after the course, then remove access
- **Make audio and video accessible,** with transcripts or captions where possible

For live online lessons, generate meeting links per session through your video provider's API, restrict them to enrolled students and avoid publishing them openly.

## Cancellations, Transfers and Refunds

Students cancel, change levels, move to another group or stop halfway. Clear rules, implemented consistently, avoid disputes:

| Situation | Typical policy to define |
| --- | --- |
| Cancellation before the course starts | Full or partial refund, depending on notice period |
| Cancellation after the course starts | No refund, partial refund or credit, as stated in terms |
| Course cancelled by the school | Full refund or transfer to another course |
| Level change after the first sessions | Transfer to a more suitable group without extra cost, if capacity allows |
| Missed private lesson without notice | Lesson counts as used, if cancellation deadline passed |
| Employer-paid course cancelled | Credit note to the employer, according to the agreement |

Show the policy at enrolment, record acceptance, and implement refunds and credit notes through your payment provider and invoicing, linked to the original payment.

## Teachers and Their Hours

Teachers may be employees or freelancers. The app can support scheduling, but also the administration behind it: hours taught per teacher, substitutions, travel to in-company locations and, for freelancers, monthly overviews that become their invoices. Give teachers a clear view of their own schedule and hours, and keep their personal data separate from students' views.

## Multilingual Interfaces

Students of a language school, by definition, may not yet speak the language well. Offer the interface in several languages, such as Dutch and English, and consider others common among your students. Send emails in the student's preferred language. Our guide on [multilingual SaaS with i18n](https://launchstudio.eu/en/blog/multilingual-saas-dutch-and-english-i18n-for-ai-built-apps) explains the technical setup.

## Youth Courses

Some schools also teach children and teenagers, for example exam preparation or holiday courses. For students under 16, parents or guardians should handle registration, payment and consent, receive communication and see progress. Teachers' contact with minors should follow the school's safeguarding policy, and data about minors deserves extra care in visibility and retention.

## Roles and Data Protection

| Role | Access |
| --- | --- |
| Student | Own courses, lessons, payments, progress and certificates |
| Teacher | Own courses and lessons, students in them, attendance and notes |
| Coordinator | All courses, scheduling, enrolments |
| Finance | Payments, invoices, refunds |
| Employer contact | Enrolled employees' agreed information |

Language school data includes contact details, nationality or language background in some cases, payment information and progress. Collect only what you need, store it in the EU, protect it with Row Level Security and define retention, especially for former students.

## Measuring How the School Is Doing

A few indicators help school owners steer: fill rate per course, share of courses cancelled for too few participants, conversion from placement test to enrolment, attendance rates, completion and certificate rates, and revenue per teacher hour. With these numbers available in the app, owners can decide when to open extra groups, which levels to promote and where students drop out.

## Launching for a New School

When onboarding a school, import existing students, courses and schedules carefully, set up payment and invoicing details, configure VAT per course type and run one enrolment period in parallel with the old process. Ask teachers to try attendance recording in their first week and collect feedback quickly; teachers' adoption determines whether attendance data is reliable.

## How LaunchStudio Helps

LaunchStudio takes language school apps from prototype to production: course and level models, placement records, capacity and waiting lists enforced in the database, teacher availability and private lesson booking, payments with instalments and lesson packages, employer invoicing, VAT configuration per course type, attendance and certificates with audit trails, multilingual interfaces and role-based access.

Language school platforms typically fall within **Launch & Grow** (€2,500-€7,500 plus €49 per month), which includes payments, managed hosting, monitoring and priority support. Use the [price calculator](https://launchstudio.eu/en/#calculator) for an estimate.

LaunchStudio is backed by Manifera, a software development company with 11+ years of experience, 160+ delivered projects and 120+ engineers, working across the Netherlands, Singapore and Vietnam with multilingual teams. Founders meet the team at Herengracht 420 in Amsterdam; engineering happens at the development centre on Pho Quang Street in Ho Chi Minh City, with a hub on Tras Street in Singapore.

## Real example

### An AI-Native Founder in Action: The Dutch Course for Expats That Employers Could Not Invoice

Anna Kowalska, a Polish-born Dutch teacher in Eindhoven, runs a language school teaching Dutch to international employees of technology companies in the Brainport region. She built Taalklas with Bolt and Supabase: students choose a course by level, pay online and receive lesson links. It worked well for individual students.

The school's growth, however, came from companies, and the app could not serve them. Employers wanted to enrol groups of employees, receive one invoice with a purchase order number and see attendance. Instead, employees paid with their own cards and claimed expenses, which several companies refused. Group courses were sometimes overbooked because enrolment checked capacity in the browser. Students joined online lessons in different time zones and missed sessions because times were shown without time zones. VAT was applied uniformly to all courses, although Anna's accountant had advised a different treatment for some course types.

LaunchStudio added company accounts with contact persons, invoice addresses, VAT number validation and purchase order references, so employers could enrol several employees and receive invoices with payment terms. Course capacity and waiting lists were enforced in the database with temporary holds during payment. Teachers recorded attendance per session, and employers received monthly attendance reports that students were informed about at enrolment. Lesson times were stored with time zones and shown in each student's local time, VAT treatment became configurable per course type as advised by the accountant, and the interface and emails were offered in Dutch and English.

**Result:** Three technology companies moved their Dutch training budgets to Anna's school within two months of the change, bringing around 120 employee students. Overbooked courses stopped, and missed online lessons due to time confusion disappeared.

> *"My students were individuals, but my customers were companies. Once the app could invoice them properly, the school grew faster than I could hire teachers."*
> - **Anna Kowalska, Founder, Taalklas (Eindhoven)**

**Cost & Timeline:** €5,600 (Launch & Grow package: company accounts and invoicing, capacity and waiting lists, attendance reports, time zone handling, VAT configuration and multilingual interface) - completed in 14 business days.

## Frequently Asked Questions

### How should a language school app handle course levels?

Model courses by language and level, commonly using CEFR levels from A1 to C2, and store placement results with date and method. Use placement results to recommend or restrict which courses a student can book.

### Can employers pay for their employees' courses through the app?

Yes, with company accounts, invoice details, purchase order references and payment terms. Employers can enrol several employees and receive one invoice. Tell students clearly what information, such as attendance, is shared with their employer.

### Do language courses include VAT?

It depends on the type of education and the provider. Some vocational education by providers registered in the CRKBO register may be exempt, while other courses are subject to VAT. Configure VAT per course type based on your accountant's advice.

### How does Manifera's experience help with education platforms?

Manifera has built booking, payment and reporting systems for clients for 11+ years, with multilingual teams in three countries. LaunchStudio applies that experience to language schools, where capacity, payments from multiple sources and accurate records come together.

### Does a booking app help a language school get found?

It can. Course pages with clear levels, schedules, locations and prices, marked up with structured data, help prospective students and companies find suitable courses, and search engines and AI answer engines can surface them when people search for language courses.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "How should a language school app handle course levels?",
      "acceptedAnswer": { "@type": "Answer", "text": "Model courses by language and CEFR level, store placement results and use them to guide bookings." }
    },
    {
      "@type": "Question",
      "name": "Can employers pay for their employees' courses through the app?",
      "acceptedAnswer": { "@type": "Answer", "text": "Yes, with company accounts, invoices, PO references and payment terms, informing students about shared data." }
    },
    {
      "@type": "Question",
      "name": "Do language courses include VAT?",
      "acceptedAnswer": { "@type": "Answer", "text": "It depends; some CRKBO-registered vocational education may be exempt. Configure per course type with your accountant." }
    },
    {
      "@type": "Question",
      "name": "How does Manifera's experience help with education platforms?",
      "acceptedAnswer": { "@type": "Answer", "text": "Manifera has built booking, payment and reporting systems for 11+ years with multilingual teams." }
    },
    {
      "@type": "Question",
      "name": "Does a booking app help a language school get found?",
      "acceptedAnswer": { "@type": "Answer", "text": "It can; structured course pages help students, companies and AI engines find courses." }
    }
  ]
}
</script>
