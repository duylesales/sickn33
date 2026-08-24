---
Title: "Case Study: Passing an Enterprise Security Questionnaire in 10 Business Days"
Keywords: Vendor Security Questionnaire, Enterprise Hardening, Row Level Security, SSO, Subprocessor List, LaunchStudio, Manifera, Bolt, Herre Roelevink
Buyer Stage: Decision
---

# Case Study: Passing an Enterprise Security Questionnaire in 10 Business Days

AI builders can get a working SaaS product in front of a prospect faster than ever. But enterprise buyers don't sign off on a demo — they sign off on a questionnaire. This is the true story of Fatima Al-Sayed, founder of an AI sales-enablement platform, who watched a promising six-figure enterprise deal stall in procurement when she was asked to prove, in writing, that her AI-generated backend could be trusted with a Fortune 500 company's data. She could honestly say "yes" to just 11 of the 40 questions. Here is exactly what she fixed, in what order, and how she turned an 11/40 into a closed deal in under three weeks.

## The Deal That Almost Died in Procurement

Fatima built PitchCraft AI, a tool that uses AI to generate and score sales pitch decks against a buyer's public filings and news signals, using Bolt over six intense weeks. The product worked. It worked well enough that a mid-market sales director at a European insurance group championed it internally after a 20-minute demo, and within days Fatima had a verbal commitment to a pilot covering 200 seats.

Then the deal moved to procurement, and procurement forwarded it to the insurer's information security team. What came back wasn't a rejection — it was worse, in the way that only paperwork can be. A 40-item vendor security questionnaire, the kind every enterprise now runs before any SaaS tool touches employee or customer data, with a firm note attached: the internal review board met in 10 business days, and unanswered or unsatisfactory items would default to "no," which would default to a declined vendor.

Fatima opened the spreadsheet expecting to skim through it in an afternoon. She didn't finish reading it in one sitting. It asked about things she had genuinely never thought about while she was three weeks deep in Bolt prompts trying to get her pitch-scoring UI to look right.

## Eleven Out of Forty: What the Questionnaire Actually Asked

The questionnaire was organized into eight sections, and by the time Fatima worked through it honestly, she could confidently mark "yes" on only 11 of the 40 line items — mostly the easy ones, like having HTTPS enforced on her domain and a published privacy policy. The categories that sank her were the ones enterprise security teams care about most:

- **Encryption at rest and in transit**: She could confirm TLS was active on the frontend, but had no documentation of whether her Supabase database enforced encryption at rest, and no answer for how encryption keys were managed or rotated.

- **Row Level Security / tenant isolation**: The questionnaire asked, in plain language, "How is customer data logically isolated from other tenants in a multi-tenant environment?" Fatima's honest answer was that isolation was handled in her application's query logic, not enforced at the database layer — which is exactly the kind of answer that fails a technical review on sight.

- **Incident response plan**: There wasn't one. No documented escalation path, no defined breach-notification timeline, nothing to attach to the questionnaire.

- **Subprocessor list**: The insurer wanted a full list of every third party that touched their data — hosting provider, database vendor, LLM provider, email service — along with confirmation that each had a signed Data Processing Agreement. Fatima had never compiled one.

- **Access control policy**: A written policy describing who inside PitchCraft AI could access production data, how access was granted and revoked, and whether least-privilege principles were enforced. She had none of this in writing.

- **Backup and disaster recovery**: The questionnaire wanted defined Recovery Point and Recovery Time Objectives, and evidence that backups were actually tested by restoring them, not just taken.

- **Penetration test history**: A hard "no" — no third-party security testing had ever been performed.

- **SSO support**: The insurer's IT policy required every vendor touching employee accounts to support enterprise single sign-on (SAML or OIDC). PitchCraft AI only had email-and-password login.

Eleven yeses out of 40 wasn't a failing grade because Fatima had built something insecure on purpose — it was a failing grade because Bolt had built her a working product, not a company that had ever been audited. Those are different things, and enterprise buyers are the first ones to notice the gap.

## Ten Business Days: The Enterprise Hardening Sprint

Fatima contacted LaunchStudio the same afternoon she read the questionnaire, with the review-board deadline circled in red. LaunchStudio's engineers, backed by Manifera, scoped the gap analysis against the questionnaire itself — treating each unanswered item as a work ticket rather than starting from a generic security checklist — and ran the **Enterprise Hardening** package as a focused 10-business-day sprint, without touching Fatima's existing Bolt-built frontend:

1. **Encryption verification, documented**: The team confirmed and documented AES-256 encryption at rest on the Supabase/Postgres layer, enforced TLS 1.2+ with HSTS across every endpoint, and wrote a one-page encryption summary Fatima could attach directly to the questionnaire — turning a vague technical claim into a specific, auditable answer.

2. **RLS-based tenant isolation**: This was the centerpiece of the sprint. Engineers implemented Row Level Security policies scoped to `auth.uid()` and account ID on every table holding customer pitch data, so tenant isolation was enforced by the database itself — not by application code that a bug could bypass. The questionnaire's isolation question went from an uncomfortable explanation to a one-line technical answer with policy code to back it up.

3. **A documented incident response plan**: LaunchStudio drafted a formal IR plan covering detection, internal escalation, customer notification timelines aligned with GDPR's 72-hour breach-notification requirement, and a designated response owner — Fatima herself, until the company was large enough to need a dedicated role.

4. **A complete subprocessor list**: The team compiled every third party in PitchCraft AI's stack — Supabase, Stripe, the LLM provider, the transactional email provider, and the hosting platform — confirmed each had a signed DPA in place, and formatted the list exactly the way enterprise security teams expect to receive it.

5. **A written access control policy**: A short, concrete document specifying role-based access to production systems, mandatory offboarding steps when a team member leaves, and least-privilege defaults for any new hire or contractor.

6. **Automated, tested backups**: Point-in-time recovery was enabled on the database, backup frequency and retention were documented against defined RPO/RTO targets, and the team performed a live test restore to prove the backups actually worked — not just that they existed.

7. **SSO support**: Engineers added SAML-based single sign-on support so the insurer's employees could log in through their own identity provider, satisfying the IT policy requirement that had been a hard blocker.

## Passing the Technical Review

Fatima resubmitted the questionnaire on day nine, one day ahead of the review board's deadline. This time, 37 of the 40 items were honest "yes" answers, each backed by a real document or a real policy she could point to. The remaining three — a completed third-party penetration test, SOC 2 Type II certification, and multi-region failover — she disclosed openly as items on her roadmap for the following quarter, with target dates attached rather than vague promises.

That honesty mattered as much as the fixes themselves. On the technical review call, the insurer's security analyst walked through the RLS policy documentation, the subprocessor list, and the incident response plan line by line, and accepted the three roadmap items without objection because everything else in the submission was verifiable and specific rather than defensive. Three weeks later, the pilot was approved, the contract was signed, and PitchCraft AI had its first enterprise logo.

## The Lesson for AI Founders

Fatima's story is becoming the norm rather than the exception. As more enterprise buyers adopt AI tools built by small, fast-moving teams, their procurement and security departments have compensated by making vendor questionnaires longer and more technical, not shorter. A polished demo built in Bolt, Lovable, or Cursor can win the champion inside the company — but it is the questionnaire, reviewed by people who will never see the demo, that actually decides whether the deal closes.

The founders who lose these deals aren't the ones with worse products. They're the ones who discover the gap between "it works" and "it's provably secure" for the first time when a 10-business-day clock is already running. The founders who win them are the ones who treat the questionnaire itself as the specification — and bring in engineers who already know how to answer it, item by item, before the deadline arrives.

## Key Takeaways

- A vendor security questionnaire tests documented, provable controls — encryption, tenant isolation, incident response, backups, SSO — not whether the product works in a demo.

- Row Level Security enforced in application code, not at the database layer, will not satisfy an enterprise tenant-isolation question — reviewers want policy enforced where a bug in your code can't bypass it.

- A complete subprocessor list with signed DPAs, a written access control policy, and a documented incident response plan are paperwork enterprise buyers require before contract, not optional extras for later.

- Disclosing gaps honestly, with a specific roadmap and dates, passes technical review far more often than vague reassurance — reviewers reward transparency over polish.

- A focused hardening sprint scoped directly against the questionnaire's own line items — rather than a generic security checklist — is what turns a 10-business-day deadline from a threat into a closable timeline.

## Don't Let a Questionnaire Kill Your Enterprise Deal

If an enterprise prospect has gone quiet since procurement got involved, the questionnaire sitting in their inbox is very likely the reason — and the clock on it is shorter than it feels.

LaunchStudio is operated by **Manifera**, an international software engineering company founded in 2014 and led by Founder & Managing Director **Herre Roelevink**. Manifera brings 11+ years of production engineering experience to exactly this kind of gap, having supported enterprise clients including Vodafone and TNO through the same scrutiny your prospect's security team is now applying to you. Combining "Dutch management with Vietnamese mastery," Manifera maintains headquarters in **Amsterdam, the Netherlands** (Herengracht 420), an Asia hub in **Singapore** (100 Tras Street), and a primary development center in **Ho Chi Minh City, Vietnam** (Pho Quang Street). Through LaunchStudio, senior engineering teams take your existing AI-built frontend and implement production-ready security controls, live payment gateways, secure hosting, and monitoring — transforming your prototype into a secure, compliant MVP in 1 to 3 weeks, without a rebuild. [Get a free quote today](https://launchstudio.eu/en/#contact) or see how Manifera's [custom software development team](https://www.manifera.com/services/custom-software-development/) approaches production-hardening for AI-generated codebases.

## Real example

### An AI-Native Founder in Action: Enterprise Sales-Enablement SaaS

Fatima Al-Sayed used **Bolt** to build PitchCraft AI, an AI sales-enablement platform, in six weeks. A large enterprise prospect's procurement team sent over a 40-item vendor security questionnaire covering encryption, tenant isolation, incident response, subprocessors, access control, backups, penetration testing, and SSO — and Fatima could honestly answer "yes" to only 11 of the 40 items, with 10 business days left before the enterprise's internal review deadline.

Fatima partnered with **LaunchStudio (by Manifera)** to close the gap. The Enterprise Hardening sprint verified and documented encryption at rest and in transit, implemented RLS-based tenant isolation at the database layer, drafted a formal incident response plan, compiled a complete subprocessor list with signed DPAs, wrote an access control policy, enabled and tested automated backups, and added SAML-based SSO support.

**Result:** Fatima went from 11/40 to 37/40 honest "yes" answers, with the remaining 3 disclosed as roadmap items the enterprise accepted. She passed the technical review and closed the enterprise deal 3 weeks later.

**Cost & Timeline:** €5,400 (Enterprise Hardening Package) — 10 business days.

---

---

---
## Frequently Asked Questions

### Why do AI-builder prototypes fail enterprise security questionnaires so often?

Tools like Bolt, Lovable, and Cursor are optimized for building working features quickly, not for documenting the controls enterprise security teams require — encryption key management, database-level tenant isolation, incident response plans, subprocessor agreements, and tested backups. A prototype can function perfectly in a demo and still have zero honest "yes" answers on most of a formal questionnaire, because those controls were never built or documented in the first place.

### What is the difference between application-level and database-level tenant isolation?

Application-level isolation relies on the app's own query logic to filter data by account — for example, only fetching rows where a customer ID matches. If there's a bug in that logic, one tenant can see another tenant's data. Database-level isolation, enforced through Row Level Security policies scoped to the authenticated user, rejects unauthorized queries at the database itself, so no application bug can leak cross-tenant data. Enterprise security reviewers specifically look for the second kind.

### Is it okay to answer "no" or disclose a gap on a security questionnaire?

Yes, and it's often better than a vague or evasive "yes." Enterprise reviewers are trained to spot inflated answers, and a confident false "yes" that doesn't hold up under a technical follow-up call does more damage than an honest "not yet, targeted for Q4" with a specific plan attached. Fatima's technical review passed with three honestly disclosed roadmap items precisely because everything else in her submission was verifiable.

### How long does it typically take to prepare for an enterprise security review?

For a founder starting from an AI-builder prototype with no prior security documentation, a focused 10-business-day sprint — scoped directly against the questionnaire's own line items rather than a generic checklist — is realistic for closing the majority of gaps, as it was for Fatima. The exact scope depends on how many items require net-new infrastructure work, like adding SSO or migrating to database-enforced RLS, versus items that only require documenting controls that already exist.

### What is LaunchStudio's relationship to Manifera, and why does that matter for enterprise deals?

LaunchStudio is operated by Manifera, an international software engineering company founded in 2014 by Herre Roelevink, with 11+ years of production engineering experience and enterprise clients including Vodafone and TNO. That matters directly for a story like Fatima's because the same disciplines Manifera applies for enterprise clients — RLS policy design, documented incident response, subprocessor and DPA management — are exactly what an enterprise questionnaire is testing for, just scoped and priced for a founder's timeline and budget.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Why do AI-builder prototypes fail enterprise security questionnaires so often?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Tools like Bolt, Lovable, and Cursor are optimized for building working features quickly, not for documenting the controls enterprise security teams require — encryption key management, database-level tenant isolation, incident response plans, subprocessor agreements, and tested backups. A prototype can function perfectly in a demo and still have zero honest \"yes\" answers on most of a formal questionnaire, because those controls were never built or documented in the first place."
      }
    },
    {
      "@type": "Question",
      "name": "What is the difference between application-level and database-level tenant isolation?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Application-level isolation relies on the app's own query logic to filter data by account — for example, only fetching rows where a customer ID matches. If there's a bug in that logic, one tenant can see another tenant's data. Database-level isolation, enforced through Row Level Security policies scoped to the authenticated user, rejects unauthorized queries at the database itself, so no application bug can leak cross-tenant data. Enterprise security reviewers specifically look for the second kind."
      }
    },
    {
      "@type": "Question",
      "name": "Is it okay to answer \"no\" or disclose a gap on a security questionnaire?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes, and it's often better than a vague or evasive \"yes.\" Enterprise reviewers are trained to spot inflated answers, and a confident false \"yes\" that doesn't hold up under a technical follow-up call does more damage than an honest \"not yet, targeted for Q4\" with a specific plan attached. Fatima's technical review passed with three honestly disclosed roadmap items precisely because everything else in her submission was verifiable."
      }
    },
    {
      "@type": "Question",
      "name": "How long does it typically take to prepare for an enterprise security review?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "For a founder starting from an AI-builder prototype with no prior security documentation, a focused 10-business-day sprint — scoped directly against the questionnaire's own line items rather than a generic checklist — is realistic for closing the majority of gaps, as it was for Fatima. The exact scope depends on how many items require net-new infrastructure work, like adding SSO or migrating to database-enforced RLS, versus items that only require documenting controls that already exist."
      }
    },
    {
      "@type": "Question",
      "name": "What is LaunchStudio's relationship to Manifera, and why does that matter for enterprise deals?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "LaunchStudio is operated by Manifera, an international software engineering company founded in 2014 by Herre Roelevink, with 11+ years of production engineering experience and enterprise clients including Vodafone and TNO. That matters directly for a story like Fatima's because the same disciplines Manifera applies for enterprise clients — RLS policy design, documented incident response, subprocessor and DPA management — are exactly what an enterprise questionnaire is testing for, just scoped and priced for a founder's timeline and budget."
      }
    }
  ]
}
</script>
