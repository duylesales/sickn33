---
Title: "Case Study: Escaping Vendor Lock-In for a Legacy-to-AI SaaS Migration"
Keywords: Vendor Lock-In, Legacy Migration, AI SaaS Migration, Code Ownership, Supabase, Open Architecture, LaunchStudio, Manifera, Bolt, Postgres
Buyer Stage: Decision
---

# Case Study: Escaping Vendor Lock-In for a Legacy-to-AI SaaS Migration

Fatima spent six years running a boutique tailoring and alterations booking service out of Rotterdam before she decided to turn the internal scheduling tool she'd commissioned in 2019 into a standalone SaaS product for other appointment-based businesses. There was just one problem: she didn't own the software she'd been using. This is the story of how a founder trapped by vendor lock-in in a legacy system used an AI builder to reimagine her product, and then partnered with LaunchStudio to build a backend she would actually own — end to end.

## The Legacy Trap

In 2019, Fatima hired a small local development agency to build a booking and scheduling tool for her tailoring business. The agency delivered a working PHP application, hosted it on their own servers, and handled every update for a monthly retainer. It worked fine — until Fatima realized, five years later, that she had a product idea worth spinning out, and discovered exactly how little control she actually had over what she'd paid for.

The agency held the only deploy keys. The codebase lived in a private repository Fatima had never been given access to. The database schema was undocumented, riddled with agency-specific conventions nobody outside that shop could easily interpret, and hosted on infrastructure billed directly to the agency, with no export tooling and no API for pulling her own data out in a usable format. When Fatima asked for a full code handoff so she could take the product to a new team, the agency quoted her €9,000 for "codebase preparation and handoff documentation" — on top of what she'd already paid them for five years of retainer fees. When she pushed back, they became slower to respond to basic maintenance requests. She was, in the plainest sense, locked in: dependent on a single vendor for a system she had commissioned but never controlled.

This is a strikingly common pattern for founders coming out of the 2015-2020 generation of small-agency custom software, and it doesn't only affect old PHP monoliths. The same lock-in shows up today in a different form: AI builders that generate a working frontend but store data in a database format the founder can't export, or hosting environments where the builder platform itself is the only party with production access. The tooling changes; the trap — depending entirely on one party for access to your own product — stays the same.

## Reimagining the Frontend

Rather than pay the ransom or start a costly custom rebuild from a blank page, Fatima took a different route. She used **Bolt** to prototype a completely reimagined version of the booking product — multi-tenant from day one, so any small business (not just tailors) could sign up, configure their own services, and manage a calendar. Over five weeks of evenings and weekends, she built a genuinely impressive frontend: a drag-and-drop calendar, automated SMS reminders via a third-party API, and a clean multi-tenant onboarding flow. It was, in terms of pure product thinking, a significant improvement over what the agency had built her in 2019.

But Fatima had learned her lesson about ownership. Before she let a single real customer sign up, she wanted a backend architecture that was hers — genuinely, verifiably, portably hers — regardless of who built it or who hosted it going forward.

## Building an Architecture With No Lock-In

Fatima brought the Bolt-generated frontend to **LaunchStudio (by Manifera)** with one explicit, non-negotiable requirement: whatever backend the team built had to be built on standard, open, exportable technology, with Fatima holding full ownership of every credential, every repository, and every piece of infrastructure from day one.

The engineering team's approach centered on three principles that directly reversed the pattern from her 2019 experience:

1. **Standard, portable data layer.** The team built the backend on Supabase — which is itself standard Postgres under the hood, not a proprietary format. Every table, every row, every migration file is standard SQL that could be exported and run on any Postgres instance anywhere, with no proprietary export tooling required and no agency-specific schema conventions that only one team could read.

2. **Fatima owns every credential.** The team set up the Supabase project, the Stripe account for handling multi-tenant subscription billing, the hosting environment, and the GitHub repository all under Fatima's own accounts and organizational ownership, not the agency's. LaunchStudio engineers worked as collaborators with scoped access — never as the sole keyholders. If Fatima ever wants to switch engineering partners again, every key, every repo, and every account transfers with zero renegotiation and zero ransom.

3. **Documented, standard conventions.** Rather than agency-specific naming and undocumented shortcuts, the team followed standard Row Level Security patterns scoped to `auth.uid()` and `organization_id` for multi-tenant isolation, with schema and API documentation any competent engineering team could pick up without a costly handoff period.

Beyond the ownership architecture, the LaunchStudio team hardened the actual production risks in Fatima's Bolt-built frontend: they implemented proper RLS policies so one tenant's customer bookings could never be queried by another tenant, replaced a client-side-only SMS trigger with a server-side queued job (preventing duplicate reminder texts when a user's connection blipped), and moved the third-party SMS API key out of client-visible code into a secured Edge Function.

## The Result: A Product Fatima Actually Owns

Within three weeks, Fatima had a multi-tenant booking SaaS product with a completely open, portable architecture. She onboarded her first four paying business customers — including a hair salon and a physiotherapy practice — within the first month after launch, each configuring their own services and calendars independently through the multi-tenant onboarding flow.

More importantly for the underlying lesson: Fatima now has a written, tested plan for what happens if she ever needs to switch engineering partners again. Every credential is hers. Every line of the schema is standard, documented Postgres. There is no single vendor who can hold her business hostage the way the 2019 agency did. That portability isn't a bonus feature — for a founder who has already lived through vendor lock-in once, it was the entire point of the engagement.

## Why Architecture Choices Made Early Matter Later

Fatima's story illustrates a principle that applies well beyond her specific situation: the choice of *how* a backend is built matters as much as *whether* it works on launch day. A backend built on proprietary, closed infrastructure can look identical to a standard Postgres/Supabase backend in a demo — both handle logins, both process payments, both feel fast. The difference only becomes visible years later, exactly when a founder needs to switch vendors, raise investment that requires code ownership diligence, or bring on a technical co-founder who needs real access.

Founders using AI builders today are in an unusually good position to avoid this trap entirely, because most modern AI-builder platforms (Lovable, Bolt, Cursor, v0, Replit Agent) default to standard, open backends like Supabase or Postgres rather than proprietary databases — but only if the engineering team that hardens the backend afterward preserves that openness rather than layering on new lock-in during the hardening process itself. The right question to ask any development partner isn't just "will this work" — it's "who holds the keys when we're done."

## Key Takeaways

- Vendor lock-in isn't limited to old, closed-source legacy systems — it can just as easily reappear in AI-builder projects if the hardening process introduces proprietary hosting or undocumented, agency-specific conventions.

- The clearest sign of lock-in is a single party holding the only deploy keys, the only database access, or the only account credentials for a system the founder nominally owns.

- Standard Postgres/Supabase architecture is inherently more portable than proprietary databases, because the underlying data can be exported and run on any Postgres instance with no special tooling.

- Full code and credential ownership should be a non-negotiable requirement from day one of any engineering engagement, not an afterthought negotiated during an eventual, costly handoff.

- A migration from a legacy, locked-in system to an AI-built frontend with an open backend architecture can be completed in weeks, not months, without sacrificing the ownership guarantees that prevent the same trap from recurring.

## Escape Vendor Lock-In Without Starting From Zero

If a previous agency — or a previous tool — is the only party with the keys to your own product, that's fixable without a costly rebuild.

LaunchStudio is operated by **Manifera**, an international software engineering company founded in 2014 and led by Founder & Managing Director **Herre Roelevink**. As Roelevink puts it: *"We see a shift in software needs. The challenge is no longer turning good ideas into software. It's now about the architecture and security needed to bring those products to maturity. We have eleven years of experience in exactly that."* Combining "Dutch management with Vietnamese mastery," Manifera maintains headquarters in **Amsterdam, the Netherlands** (Herengracht 420), an Asia hub in **Singapore** (100 Tras Street), and a primary development center in **Ho Chi Minh City, Vietnam** (Pho Quang Street). Through LaunchStudio, senior engineering teams take your existing AI-built frontend and build a production-ready backend on open, standard infrastructure — with every credential, repository, and account owned by you from day one — turning a prototype, or an escape from a locked-in legacy system, into a portable MVP in 1 to 3 weeks. [Get a free quote today](https://launchstudio.eu/en/#contact) or see how Manifera's [custom software development team](https://www.manifera.com/services/custom-software-development/) approaches legacy migrations and open-architecture rebuilds.

## Real example

### An AI-Native Founder in Action: Veterinary Records Platform

Adebayo, a veterinarian who had spent a decade practicing before turning entrepreneur, was locked into a proprietary veterinary records system built by a regional software vendor in 2017. The vendor charged an annual licensing fee, stored patient records in a closed database format with no export function beyond a limited PDF report, and refused to provide API access for a mobile companion app Adebayo wanted to build for pet owners. Switching vendors would have meant manually re-entering years of patient history for the veterinary clinics using the system.

Adebayo used **v0** to design a modern replacement interface and brought it to **LaunchStudio (by Manifera)** to build the backend. The team built a data migration pipeline that extracted the legacy vendor's records via its limited PDF export and OCR processing, restructured the data into a standard, documented Postgres schema, and implemented RLS policies scoping each clinic's records to its own staff accounts. Every credential — database, hosting, API keys — was set up under Adebayo's own organizational accounts from the start.

**Result:** Adebayo migrated three clinics off the legacy vendor with zero data loss and launched a companion mobile app for pet owners that the old proprietary system could never have supported.

**Cost & Timeline:** €4,200 (Relaunch & Scale Package) — migrated and launched in 15 business days.

---

---

---
## Frequently Asked Questions

### What counts as vendor lock-in in a software product?

Vendor lock-in means a single party — a development agency, a software vendor, or a builder platform — holds the only access to critical parts of your product: the deploy keys, the database, the hosting account, or the source code repository. If you cannot switch providers or bring in a new engineering team without that party's cooperation (or a large handoff fee), you are locked in, regardless of how well the product currently works.

### Can AI builders also create vendor lock-in?

Yes, though it's less common than with legacy custom-built systems. Most modern AI builders like Lovable, Bolt, Cursor, and v0 default to open, standard databases like Supabase or Postgres, which is a strong starting point. Lock-in can still creep in afterward if the team that hardens the backend for production uses proprietary hosting, keeps credentials under their own accounts instead of the founder's, or documents nothing, effectively becoming the only party who can maintain the system.

### How do you migrate off a legacy system that has no export function?

It depends on what access exists. Options range from using an existing (even limited) export feature like a PDF or CSV report and reconstructing the data with OCR or parsing scripts, to negotiating API or database access from the vendor, to in the worst case manually re-entering critical records. The specific approach depends heavily on the legacy system in question, which is why an engineering team experienced with legacy migrations should assess it case by case.

### Why does it matter whether the backend uses standard Postgres versus a proprietary database?

Standard Postgres (including Supabase, which is Postgres under the hood) can be exported and run on any compatible hosting provider with standard tools, with no proprietary format to reverse-engineer. A proprietary database format ties your data to one vendor's infrastructure and tooling, meaning any future migration requires that vendor's cooperation, adding real switching costs and risk that a standard-format database avoids entirely.

### How long does a legacy-to-AI SaaS migration typically take?

For most small-to-mid-sized legacy systems paired with an already-functional AI-builder frontend, a full migration including data transfer, RLS-based multi-tenant security, and production hosting typically takes 10 to 15 business days under LaunchStudio's Relaunch & Scale package, though the exact timeline depends on the complexity and accessibility of the legacy data.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What counts as vendor lock-in in a software product?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Vendor lock-in means a single party — a development agency, a software vendor, or a builder platform — holds the only access to critical parts of your product: the deploy keys, the database, the hosting account, or the source code repository. If you cannot switch providers or bring in a new engineering team without that party's cooperation (or a large handoff fee), you are locked in, regardless of how well the product currently works."
      }
    },
    {
      "@type": "Question",
      "name": "Can AI builders also create vendor lock-in?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes, though it's less common than with legacy custom-built systems. Most modern AI builders like Lovable, Bolt, Cursor, and v0 default to open, standard databases like Supabase or Postgres, which is a strong starting point. Lock-in can still creep in afterward if the team that hardens the backend for production uses proprietary hosting, keeps credentials under their own accounts instead of the founder's, or documents nothing, effectively becoming the only party who can maintain the system."
      }
    },
    {
      "@type": "Question",
      "name": "How do you migrate off a legacy system that has no export function?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "It depends on what access exists. Options range from using an existing (even limited) export feature like a PDF or CSV report and reconstructing the data with OCR or parsing scripts, to negotiating API or database access from the vendor, to in the worst case manually re-entering critical records. The specific approach depends heavily on the legacy system in question, which is why an engineering team experienced with legacy migrations should assess it case by case."
      }
    },
    {
      "@type": "Question",
      "name": "Why does it matter whether the backend uses standard Postgres versus a proprietary database?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Standard Postgres (including Supabase, which is Postgres under the hood) can be exported and run on any compatible hosting provider with standard tools, with no proprietary format to reverse-engineer. A proprietary database format ties your data to one vendor's infrastructure and tooling, meaning any future migration requires that vendor's cooperation, adding real switching costs and risk that a standard-format database avoids entirely."
      }
    },
    {
      "@type": "Question",
      "name": "How long does a legacy-to-AI SaaS migration typically take?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "For most small-to-mid-sized legacy systems paired with an already-functional AI-builder frontend, a full migration including data transfer, RLS-based multi-tenant security, and production hosting typically takes 10 to 15 business days under LaunchStudio's Relaunch & Scale package, though the exact timeline depends on the complexity and accessibility of the legacy data."
      }
    }
  ]
}
</script>
