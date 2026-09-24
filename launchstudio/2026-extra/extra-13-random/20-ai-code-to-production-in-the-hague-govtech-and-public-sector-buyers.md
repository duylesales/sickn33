---
Title: "AI Code to Production in The Hague: GovTech Startups and Public-Sector Buyers"
Keywords: ai code to production, govtech the hague, public sector software security, BIO baseline, windsurf, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: Technical Solo Founder / Indie Hacker
---

# AI Code to Production in The Hague: GovTech Startups and Public-Sector Buyers

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "AI Code to Production in The Hague: GovTech Startups and Public-Sector Buyers",
  "description": "GovTech founders in The Hague face buyers with formal security, accessibility and data requirements. This article explains what public-sector customers ask for when AI code goes to production — BIO, accessibility, hosting, penetration tests and exit plans — and how to prepare.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-10-20",
  "inLanguage": "en",
  "contentLocation": { "@type": "Place", "name": "The Hague, Netherlands" },
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/ai-code-to-production-in-the-hague-govtech-and-public-sector-buyers" }
}
</script>

The Hague is where Dutch government lives, and it has produced a steady stream of GovTech founders: former civil servants, policy advisers and consultants who saw a problem from the inside and built a tool for it. More and more of those tools start as AI code — a Windsurf or Cursor project assembled quickly to show a municipality what is possible. The pilot goes well. Then procurement sends a questionnaire, and moving that AI code to production becomes a very specific exercise.

Public-sector buyers are not harder to please than other customers; they are more explicit. They write down what they need. That is good news, because it means you can prepare.

## What Public-Sector Buyers Actually Ask For

Questionnaires vary, but Dutch municipalities, provinces, water boards and agencies commonly ask about the same areas:

- **Information security** — often mapped to the BIO (Baseline Informatiebeveiliging Overheid), the government's information security baseline based on ISO 27002.
- **Data protection** — a processing agreement, processor list, data location, retention and a data protection impact assessment if the processing is high-risk.
- **Accessibility** — government websites and apps must meet accessibility requirements based on WCAG, and buyers increasingly ask suppliers for an accessibility statement.
- **Testing** — evidence of security testing, often a recent penetration test for anything facing citizens.
- **Continuity** — backups, recovery times, incident processes and what happens if your company stops.
- **Exit** — how the buyer gets their data back in a usable format if the contract ends.

An AI prototype usually has none of this documented and some of it missing entirely.

## The AI Code to Production Gaps Behind the Questions

Behind the paperwork sit concrete technical requirements. The ones AI-generated GovTech prototypes most often lack:

**Role-based access that matches the organisation.** Municipal users have roles — case handler, team lead, administrator, auditor — with different rights. AI-built apps often have "user" and "admin," enforced partly in the interface.

**Audit logging.** Public bodies must be able to account for who viewed and changed data. An append-only log of access to personal data is frequently a hard requirement.

**Authentication suited to government users.** Many buyers want single sign-on with their own identity provider (often via SAML or OpenID Connect) and multi-factor authentication for administrators. Citizen-facing services may involve DigiD or eHerkenning, which bring their own requirements and assessments.

**Data minimisation and retention.** Personal data should be collected only where necessary and deleted according to a defined schedule — something AI-generated schemas never include.

**Hosting and location.** Buyers typically want data in the EU and sometimes in the Netherlands, with clarity about every sub-processor.

**Accessibility in the interface.** AI-generated interfaces often miss labels, contrast, keyboard navigation and focus management. The [DigiToegankelijk guidance](https://www.digitoegankelijk.nl/) from the Dutch government explains what is expected.

## The Penetration Test Question

For a citizen-facing service or one handling sensitive data, a buyer will often ask for a penetration test by an independent party. Running one on an unhardened AI prototype is a waste of money: the report will list the obvious problems, and you will pay again after fixing them.

The efficient order is: review and harden first, fix the findings, then commission the penetration test on a system that is ready for it. The test then confirms your work rather than cataloguing basics.

## Documentation Is Part of the Product

For GovTech, the documents are not an afterthought; they are part of what the buyer purchases. At minimum, prepare:

- a security overview mapped to the relevant BIO controls,
- a processor list and data processing agreement,
- an accessibility statement,
- a backup and recovery description with realistic recovery times,
- an incident response procedure,
- an exit plan describing data export formats.

Many of these can be short. They must be accurate.

## Why This Is Worth Doing Once, Properly

The Dutch public sector is a large, stable market, and reference customers matter enormously. One municipality that can vouch for your security and continuity opens doors to dozens of others. Doing the production work properly for the first contract turns it into an asset for every subsequent tender.

## Mapping Your App to the BIO

Public-sector buyers often ask how your product relates to the BIO (Baseline Informatiebeveiliging Overheid). You do not need to be certified to answer credibly. A practical approach is a short mapping document that covers the areas buyers focus on most:

| BIO-related theme | What buyers look for | Evidence you can provide |
| --- | --- | --- |
| Access management | Roles, least privilege, MFA for administrators | Role matrix, SSO configuration, MFA policy |
| Logging and monitoring | Who accessed what, alerts on anomalies | Audit log description, sample export, alert list |
| Cryptography | Encryption in transit and at rest | TLS configuration, hosting provider's encryption statement |
| Supplier management | Sub-processors and their locations | Processor list with DPAs |
| Continuity | Backups, recovery objectives, incident handling | Backup schedule, restore test result, incident procedure |
| Secure development | Code review, testing, vulnerability management | CI checks, dependency scanning, pentest or review report |

A two- to four-page mapping like this answers a large share of procurement questions and shows the buyer that you understand their framework.

## Working With DigiD, eHerkenning and Government SSO

GovTech products often need to authenticate either civil servants or citizens and businesses. Civil servants typically log in through the organisation's own identity provider, usually via SAML or OpenID Connect. Citizen and business authentication through DigiD or eHerkenning brings additional requirements: connection through an approved broker or supplier, security assessments and specific agreements. For an early GovTech product, it is often wise to start with staff-facing features via SSO and add citizen authentication through an established broker when the contract requires it, rather than building a direct connection prematurely.

## Accessibility as a Contract Requirement

Dutch government bodies are required to make their websites and apps accessible, and they generally expect the same of suppliers' public-facing services. In practice, buyers look for conformance with WCAG 2.1 level AA and an accessibility statement. AI-generated interfaces often need fixes to form labels, error messages, contrast, focus visibility and keyboard navigation. Plan an accessibility review of critical flows before the first contract, publish a statement listing known limitations and a date for fixing them, and include accessibility checks in your release process so regressions are caught.

## Data Minimisation and Retention for Citizen Data

Public services handle citizens' data under strict expectations. Collect only what the service needs; strip metadata from photos (locations of reporters' homes, for instance); separate identifying data from operational data where possible; and agree retention periods with the buyer, then enforce them automatically. For services that may involve sensitive situations — complaints about neighbours, reports of unsafe situations — consider how the reporter's identity is protected from the person or organisation being reported.

## An Exit Plan Buyers Can Accept

Public buyers must be able to continue if a supplier stops. An exit plan describes how data is exported (formats, frequency, completeness), how long you support the transition, what documentation is handed over and what happens to backups after the contract ends. Offering a regular automated export to the buyer's own storage is a strong answer. For small GovTech suppliers, a credible exit plan is often what reassures a municipality enough to sign despite the company's size.

## Procurement Timing and Thresholds

Public procurement follows rules that depend on contract value. Smaller contracts can often be awarded through simpler procedures, while larger ones require formal tenders with published criteria. For a young GovTech company, early contracts are frequently pilots or small assignments below European thresholds. Use them to build references, documentation and evidence — a restore test, an accessibility statement, a clean penetration test — that you will need when larger tenders arrive. Each successful small contract makes the next procurement dossier easier to complete.

## Building Trust Before the First Contract

Public buyers are cautious with young suppliers, for good reasons: continuity, security and accountability. Several steps build trust before procurement starts. Invite the buyer's information security officer and privacy officer into the pilot early, rather than surprising them at contract time. Share your security mapping and processor list proactively. Offer a named contact for incidents. Keep a changelog of releases so the buyer can see how the product evolves. And be honest about limitations — a documented gap with a plan is far more acceptable to a public body than a claim that turns out to be untrue.

## Designing for Civil Servants' Workflows

Case handlers and team leads use GovTech tools all day, often alongside several other systems. Production readiness includes workflow details that AI prototypes rarely get right: bulk actions with confirmation and undo, keyboard shortcuts for frequent tasks, exports in formats the organisation's other systems accept, clear status histories for each case, and handover between colleagues without losing context. Watching two or three civil servants use the pilot for an hour reveals most of these needs quickly — and fixing them turns a tool people tolerate into one they ask for.

## Security Testing Cadence After Launch

A single penetration test before the contract is rarely enough for a service that changes regularly. A sustainable cadence for a small GovTech supplier is: automated checks on every change (access tests, dependency and secret scanning), a focused internal or partner review before major releases, and an independent penetration test yearly or when the buyer requires it. Record each test, its findings and their resolution; public buyers often ask for this history during contract reviews or renewals.

## Who Should Own What

In GovTech projects, clarity about roles prevents most friction. The buyer is usually the data controller; the supplier is a processor bound by the processing agreement. The buyer defines retention, access policies and user management rules; the supplier implements and operates them. Put this division in writing, including who approves new sub-processors and who communicates with citizens during an incident.

## Where LaunchStudio Fits

LaunchStudio's work for GovTech founders combines technical hardening with the documentation buyers expect: role-based access and audit logging enforced on the server, SSO integration, retention rules, EU hosting, accessibility fixes in the existing interface, and a security overview ready to attach to a questionnaire. When a penetration test is required, the system is prepared for it and findings are handled afterwards.

The engineering comes from Manifera, which has 11+ years of experience delivering software to organisations with formal requirements — including TNO, the Netherlands Organisation for Applied Scientific Research. Manifera's CEO Herre Roelevink has a background in cybersecurity, having co-founded CyberDevOps (now CFLW Cyber Strategies). Manifera's Amsterdam office on Herengracht 420 is under an hour from The Hague Centraal; engineering is carried out at the Ho Chi Minh City development centre. See [Manifera's custom software development](https://www.manifera.com/services/custom-software-development/) for its larger-scale public and enterprise work.

To start, [describe your project](https://launchstudio.eu/en/#contact) — including the buyer's questionnaire if you have one. We respond within one working day.

## Real example

### An AI-Native Founder in Action: A Neighbourhood Reporting Tool Meets Procurement

Hugo Verbeek spent eleven years as a policy adviser before founding BuurtSignaal in The Hague: a tool that lets residents report issues — broken streetlights, illegal dumping, unsafe crossings — and lets municipal teams triage and respond. He built it in Windsurf with a Next.js frontend and Postgres, and ran a pilot with one city district. Residents liked it; district staff liked it more.

When the municipality moved to a formal contract, procurement sent a 90-question security and privacy questionnaire. Hugo could answer about a third. The review LaunchStudio carried out explained why: municipal staff roles were "user" and "admin," with case-handler restrictions only in the interface; there was no audit log; staff logged in with passwords rather than the municipality's identity provider; residents' reports, including photos with location data, were kept indefinitely; hosting was in a US region; and an accessibility scan found missing labels and keyboard traps in the resident form.

Over 21 business days, the team implemented four staff roles enforced in the database, an append-only audit log for access to resident data, SSO via the municipality's OpenID Connect provider with MFA for administrators, automatic removal of location metadata from photos, retention rules agreed with the municipality, EU hosting with tested backups, and accessibility fixes in the existing interface. They also produced a BIO-mapped security overview, processor list, recovery description, incident procedure and exit plan. The municipality then commissioned an independent penetration test, which returned two low-severity findings, fixed the same week.

**Result:** BuurtSignaal signed a three-year contract with the municipality and has since been piloted by two neighbouring municipalities, both of which accepted the existing documentation with minor additions.

> *"The pilot proved residents wanted it. The contract depended on proving the municipality could trust it. Those were two different projects, and I'd only done the first one."*
> — **Hugo Verbeek, Founder, BuurtSignaal (The Hague)**

**Cost & Timeline:** €6,900 (Launch & Grow package: access control, audit logging, SSO, retention, hosting, accessibility fixes and procurement documentation) — completed in 21 business days, plus €49/month managed hosting.

## Frequently Asked Questions

### Do I need ISO 27001 certification to sell to Dutch municipalities?

Not always. Many buyers ask how your security maps to the BIO rather than requiring certification, especially for smaller contracts. Certification may become necessary for larger or more sensitive contracts; a solid, documented baseline is the first step either way.

### Should I commission a penetration test before or after hardening?

After. Testing an unhardened prototype mostly confirms known basics. Hardening first means the test focuses on real residual risk, and you avoid paying for two tests.

### Can AI-generated interfaces meet government accessibility requirements?

Yes, with targeted fixes. AI-built interfaces often miss labels, contrast and keyboard support, but these can be corrected without redesigning the product.

### How does Manifera's experience with TNO help GovTech founders?

Working with an organisation like TNO means working with formal requirements, documentation and security expectations. That experience helps LaunchStudio's engineers anticipate what public buyers will ask and prepare answers that hold up.

### How can a GovTech startup be found by public-sector buyers searching online?

Publish clear pages about the problem you solve, your security and privacy approach, and your accessibility statement, with structured data. Procurement teams and AI answer engines both look for precise, verifiable information from reliable sources.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Do I need ISO 27001 certification to sell to Dutch municipalities?",
      "acceptedAnswer": { "@type": "Answer", "text": "Not always. Many buyers ask how security maps to the BIO; certification may be needed for larger or more sensitive contracts." }
    },
    {
      "@type": "Question",
      "name": "Should I commission a penetration test before or after hardening?",
      "acceptedAnswer": { "@type": "Answer", "text": "After hardening, so the test focuses on residual risk and you avoid paying twice." }
    },
    {
      "@type": "Question",
      "name": "Can AI-generated interfaces meet government accessibility requirements?",
      "acceptedAnswer": { "@type": "Answer", "text": "Yes, with targeted fixes to labels, contrast and keyboard support, without redesigning the product." }
    },
    {
      "@type": "Question",
      "name": "How does Manifera's experience with TNO help GovTech founders?",
      "acceptedAnswer": { "@type": "Answer", "text": "It builds familiarity with formal requirements and documentation, helping anticipate what public buyers ask." }
    },
    {
      "@type": "Question",
      "name": "How can a GovTech startup be found by public-sector buyers searching online?",
      "acceptedAnswer": { "@type": "Answer", "text": "Publish clear pages on the problem solved, security, privacy and accessibility, with structured data, on a reliable site." }
    }
  ]
}
</script>
