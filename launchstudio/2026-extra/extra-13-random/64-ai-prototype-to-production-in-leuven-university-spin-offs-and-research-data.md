---
Title: "AI Prototype to Production in Leuven: University Spin-Offs and Research Data"
Keywords: ai prototype to production, leuven spin-off, research data security, university startup belgium, cursor, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: Technical Solo Founder / Indie Hacker
---

# AI Prototype to Production in Leuven: University Spin-Offs and Research Data

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "AI Prototype to Production in Leuven: University Spin-Offs and Research Data",
  "description": "Leuven's spin-offs often start as research tools built quickly with AI. This article covers what changes when an academic AI prototype goes to production for paying customers: research data agreements, institutional IP, multi-institution access, reproducibility and EU hosting.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-12-03",
  "inLanguage": "en",
  "contentLocation": { "@type": "Place", "name": "Leuven, Belgium" },
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/ai-prototype-to-production-in-leuven-university-spin-offs-and-research-data" }
}
</script>

Leuven is one of Europe's densest spin-off ecosystems. Research groups turn lab tools into companies, and increasingly those tools begin as something a PhD researcher built in Cursor to save their group time: a data pipeline with a dashboard, an equipment booking system, an annotation tool. It works for the lab. Then other labs want it, a spin-off is founded, and moving that AI prototype to production means meeting expectations no internal tool ever faced.

## AI Prototype to Production: What Changes When a Lab Tool Becomes a Product

Inside one research group, a tool has one owner, one set of trusted users and data that never leaves the building. As a product it gets:

- **External customers,** often other universities, hospitals and companies, each with their own procurement and data protection officers.
- **Formal ownership questions,** because the tool was built at a university.
- **Data that belongs to someone else,** usually under agreements that specify where it may be stored and who may see it.
- **Uptime expectations,** because experiments and bookings now depend on it.

## Institutional IP Comes First

Code written by university staff or students during their research usually falls under the institution's IP policy. Before a spin-off sells the product, the technology transfer office typically needs to license or assign the rights. This is not a technical step, but it shapes everything technical afterwards: which repository is the product's official home, which contributors need to sign agreements and whether earlier versions remain university property.

For AI-assisted code, it is also worth documenting which AI tools were used and under which terms, since procurement teams increasingly ask.

## Research Data Has Rules Attached

Research data often arrives with conditions: data processing agreements, data transfer agreements, ethics approvals, consortium rules. Typical requirements include storage in the EU or even in a specific country, access limited to named people, audit logs, deletion at the end of a project and no reuse beyond the stated purpose.

A prototype built for one group rarely enforces any of this. Everyone in the lab can see everything, data lives wherever the database was created, and nothing is deleted.

## Multi-Institution Access Control

When several institutions use one platform, the core requirement is strict separation: each institution — and often each project within it — sees only its own data. Researchers may belong to several projects at different institutions, with different roles in each. Access must be enforced on the server, ideally in the database with row-level security keyed to institution and project membership.

Institutions also prefer their own logins. Single sign-on through SAML or OpenID Connect — in Belgium frequently via federations such as Belnet's — is often a condition of adoption.

## Reproducibility and Versioning

Researchers need to know which version of a pipeline produced which result. Production means versioned releases, recorded parameters for each run, and a way to reproduce an old analysis even after the software has changed. AI-generated code that is regenerated freely makes this hard unless releases are tagged and changes are reviewed.

## Uptime and Support for Academic Customers

Shared equipment bookings, sample tracking and analysis pipelines have deadlines attached: a grant report, a conference submission, a beam-time slot. Monitoring, backups with tested restores and a clear support channel matter even for a small spin-off.

## Leuven, Amsterdam and Beyond

For Flemish spin-offs, the Dutch market is often the second market, and many research customers sit across both countries. LaunchStudio is backed by Manifera, whose European office at Herengracht 420 in Amsterdam is around two and a half hours from Leuven by train, with engineering at its development centre in Ho Chi Minh City and a hub in Singapore. Manifera's work with TNO, the Dutch applied research organisation, gives its teams experience with research-grade expectations. See [Manifera's portfolio](https://www.manifera.com/portfolio/).

## Research Data Agreements in Practice

When moving an AI prototype to production for academic customers, data agreements shape the architecture. Common agreement types and their technical consequences:

| Agreement | Typical conditions | Technical consequence |
| --- | --- | --- |
| Data processing agreement (DPA) | Process only on instructions, security measures, sub-processor approval | Documented processors, access control, breach procedure |
| Data transfer agreement | Specific datasets, permitted uses, no onward sharing | Dataset-level access, usage logging, export controls |
| Consortium agreement | Partners' rights to data and results | Per-partner separation, attribution in results |
| Ethics approval conditions | Pseudonymisation, retention limits, consent scope | Pseudonymised identifiers, retention jobs, consent records |

Map each active agreement to the controls that satisfy it, and keep that mapping with your documentation. When an institution's legal team asks how their conditions are met, the answer is ready.

## Pseudonymisation and Minimisation for Research Platforms

Research platforms often need to link data about the same person or sample without exposing identities. Pseudonymisation replaces direct identifiers with codes, with the linking key stored separately and accessible to very few people. Combine it with minimisation: store only fields needed for the research purpose, aggregate where possible and remove data at the end of the project. Note that pseudonymised data is still personal data under GDPR; the measures reduce risk but do not remove obligations.

## Implementing Institutional Single Sign-On

Academic SSO usually runs through SAML or OpenID Connect, often via national or international federations. Practical steps:

1. Choose an auth provider that supports SAML/OIDC federation (many managed providers do).
2. Register your service with the relevant federation or directly with each institution's identity provider.
3. Map attributes — name, email, affiliation, sometimes role — to your user model.
4. Handle users who belong to several institutions or change institutions.
5. Keep a fallback login for external collaborators without institutional accounts.
6. Deactivate users automatically when their institutional login stops working.

SSO also answers a common question from institutions: "what happens when a researcher leaves?"

## Reproducibility Engineering

For research tools, reproducibility is a production requirement. Tag every release; record, for each analysis or pipeline run, the software version, parameters, input dataset versions and environment; store outputs with those references; and make it possible to rerun an old configuration. Containers help freeze environments. When AI tools regenerate code, tagged releases and recorded parameters ensure that results produced last year remain explainable.

## Hosting Choices for Academic Customers

Institutions increasingly prefer EU hosting, sometimes specific countries, and occasionally on-premises or national research cloud infrastructure. Design the application so it can run on standard infrastructure — containers, managed Postgres, S3-compatible storage — rather than depending on a single proprietary platform. This flexibility can decide procurement: an institution with strict requirements may ask for a dedicated deployment.

## Pricing and Procurement in Academia

Academic procurement has its own rhythms: budgets tied to grants and fiscal years, purchasing thresholds, framework agreements and approval by several departments. Offer clear pricing per institution or per facility, a pilot option, standard documents (DPA, security overview, accessibility statement) and invoicing that fits grant accounting. Spin-offs that make procurement easy often win against more feature-rich competitors.

## Security Expectations From University IT

University IT and security teams typically ask about authentication (SSO, MFA for admins), encryption in transit and at rest, logging and monitoring, vulnerability management, backup and recovery, incident notification and data location. Many also run their own security scans against suppliers' public endpoints. Prepare a concise security overview and fix obvious findings — missing headers, outdated TLS configurations, exposed admin paths — before the first institutional review.

## From One Lab to Many: Scaling Considerations

As more institutions join, expect new demands: per-institution configuration, custom reports, integration with local systems (booking, finance, identity), and support across time zones for international consortia. A tenant-aware architecture from the start — every table scoped to an institution, configuration per tenant — makes this growth incremental rather than a redesign.

## Handling Sensitive Research Domains

Some research tools touch especially sensitive areas: clinical data, genetic data, data about children or vulnerable groups. In these domains, expect additional requirements such as data protection impact assessments, stricter access controls, audit trails of every access, restrictions on data leaving institutional infrastructure and, for medical contexts, possible questions about medical device regulation if the software influences diagnosis or treatment. Scope these early with the institution's data protection officer and research ethics contacts, and design the platform so sensitive modules can be isolated.

## Documentation Researchers Actually Use

Research users want to understand how the tool works before trusting its results. Provide clear documentation of methods, algorithms and assumptions; version-specific release notes; example datasets; and guidance on citing the software. Offering a stable citation (for example a DOI for software releases) and a methods page increases adoption in academic communities and supports publications that use your tool.

## Support Models for Academic Customers

Academic users often work irregular hours and in international collaborations. A practical support model for a small spin-off includes a documented help centre, a shared support inbox with response-time targets, a status page for incidents and scheduled maintenance windows communicated in advance — ideally outside periods such as grant deadlines or conference submissions that you can learn from your customers.

## Measuring Adoption Within Institutions

Track usage per institution and per facility: active users, bookings or analyses per month, features used and support requests. Share summaries with institutional contacts, who often need evidence of value for renewals and budget discussions. Declining usage at one institution is also an early signal to reach out before a renewal is at risk.

## From Spin-Off to Sustainable Company

Many spin-offs begin with grant funding and a single champion inside the university. Sustainability requires paying customers beyond the original lab, robust operations and a product that works without its founder answering every question. Production readiness — tenancy, SSO, documentation, monitoring and clear agreements — is what makes that transition possible, turning a successful research tool into a company that institutions can depend on for years.

## A Starting Checklist for Leuven Founders

Before signing a second institution: IP licence or assignment settled with the tech transfer office; tenant separation enforced and tested; SSO available; hosting region matching agreements; processors documented; retention implemented; releases versioned; monitoring active; and a security overview ready to send.

## Why It Matters for the Research Itself

Production readiness is not only a commercial concern for a research spin-off. When institutions trust the platform — its data separation, its reproducibility, its uptime during critical experiments — more researchers use it, more data flows through it and the scientific value of the tool grows. The engineering work that makes procurement easier is the same work that makes results more reliable. For a founder who started in the lab, that alignment between good science and good software is often the most persuasive reason to take production seriously from the very first external customer onwards.

## Where LaunchStudio Fits

LaunchStudio takes lab-built tools to production: institution- and project-level access control, SSO, EU hosting in the region your agreements require, access logging, retention and deletion, versioned releases and monitoring. Institutional IP is handled by your tech transfer office; LaunchStudio makes sure the technical setup matches what those agreements promise. The [KU Leuven Research & Development](https://lrd.kuleuven.be/en) office is the usual first stop on the IP side.

If your spin-off is about to sign its first external institution, [describe your project](https://launchstudio.eu/en/#contact) and we will reply within one working day.

## Real example

### An AI-Native Founder in Action: A Lab Booking Tool Adopted by Other Universities

Pieter-Jan Maes, a postdoctoral researcher in Leuven, built LabAgenda with Cursor: a booking and usage-tracking system for shared lab equipment such as microscopes and sequencers, with automated cost allocation to research grants. His own department used it for two years. When three other research institutes in Belgium and the Netherlands asked to use it, he founded a spin-off with support from the university's tech transfer office.

The first institute's data protection officer sent a questionnaire, and the answers were uncomfortable. All institutions' bookings, grant numbers and usage notes were in one table visible to every logged-in user. Users logged in with email and password rather than their institution's credentials. The database ran in a US region. There was no access log, grant data was never deleted, and deployment meant Pieter-Jan pushing from his laptop.

Over eleven business days, LaunchStudio's engineers introduced institution and facility tenancy with row-level security and per-facility roles, added SSO via OpenID Connect for institutional logins alongside a fallback for external users, migrated the database to an EU region with backups and a tested restore, added access logging and configurable retention per institution, and set up versioned releases through a CI pipeline with staging. The tech transfer office finalised the licence to the spin-off in parallel.

**Result:** All three institutes signed within two months. LabAgenda now manages bookings for 41 facilities, and its data-handling description has been reused in every subsequent procurement.

> *"In the lab, trust was implicit because we all knew each other. Selling it meant writing that trust down and enforcing it in the code."*
> — **Pieter-Jan Maes, Founder, LabAgenda (Leuven)**

**Cost & Timeline:** €3,200 (Launch Ready package with tenancy, SSO, data migration, logging and release pipeline) — completed in 11 business days.

## Frequently Asked Questions

### Who owns code a researcher wrote with AI tools at a university?

Usually the institution, under its IP policy, until it is licensed or assigned to a spin-off. Check with your technology transfer office before selling the product.

### Do research customers require EU hosting?

Often, and sometimes in a specific country, depending on data agreements and ethics approvals. Check each agreement before choosing a region.

### Is single sign-on necessary for academic customers?

It is frequently expected, because institutions want staff to use their own credentials and to lose access automatically when they leave.

### How does Manifera's research experience help Leuven spin-offs?

Manifera has worked with TNO and other organisations with research-grade requirements, so its engineers are familiar with data agreements, access logging and reproducibility expectations.

### How can a spin-off become visible to other institutions through search and AI assistants?

Publish clear pages describing what the tool does, which institutions use it and how data is handled, with structured data. Researchers and procurement teams increasingly ask AI assistants for tool recommendations, which draw on exactly that information.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "Who owns code a researcher wrote with AI tools at a university?", "acceptedAnswer": { "@type": "Answer", "text": "Usually the institution until licensed or assigned to a spin-off; check with the tech transfer office." } },
    { "@type": "Question", "name": "Do research customers require EU hosting?", "acceptedAnswer": { "@type": "Answer", "text": "Often, sometimes in a specific country, depending on data agreements and ethics approvals." } },
    { "@type": "Question", "name": "Is single sign-on necessary for academic customers?", "acceptedAnswer": { "@type": "Answer", "text": "It is frequently expected so staff use institutional credentials and lose access automatically." } },
    { "@type": "Question", "name": "How does Manifera's research experience help Leuven spin-offs?", "acceptedAnswer": { "@type": "Answer", "text": "Work with TNO and similar organisations brings familiarity with data agreements, logging and reproducibility." } },
    { "@type": "Question", "name": "How can a spin-off become visible to other institutions through search and AI assistants?", "acceptedAnswer": { "@type": "Answer", "text": "Publish clear, structured pages on what the tool does, who uses it and how data is handled." } }
  ]
}
</script>
