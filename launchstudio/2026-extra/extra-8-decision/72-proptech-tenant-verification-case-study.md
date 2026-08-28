---
Title: "Case Study: A PropTech Founder Launches Tenant Verification Without Storing Sensitive Data"
Keywords: tenant verification app, PropTech MVP launch, sensitive data handling startup, identity verification SaaS, data minimization compliance, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: SaaS Founder Scale-Up
---

# Case Study: A PropTech Founder Launches Tenant Verification Without Storing Sensitive Data

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Case Study: A PropTech Founder Launches Tenant Verification Without Storing Sensitive Data",
  "description": "A PropTech founder needed to verify tenant identities and income for landlords. The challenge: collecting sensitive data without storing it on your own servers. Here's how LaunchStudio implemented a verification flow that processes personal data without ever keeping it.",
  "author": {
    "@type": "Organization",
    "name": "LaunchStudio",
    "url": "https://launchstudio.eu/en/"
  },
  "publisher": {
    "@type": "Organization",
    "name": "Manifera",
    "url": "https://www.manifera.com"
  },
  "datePublished": "2026-12-31",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://launchstudio.eu/en/blog/proptech-tenant-verification-case-study"
  }
}
</script>

Tom Bakker had a product that landlords wanted — a tenant screening tool that verified identity and income before a lease signing, replacing the unreliable process of asking tenants to email payslips and ID copies. The problem wasn't demand. It was data. The moment HuurCheck stored a passport scan or a salary statement on its own servers, Tom's Lovable-built prototype became a data processor under GDPR with obligations he couldn't meet: mandatory data protection impact assessments, breach notification within 72 hours, data subject access request handling, and the liability that comes with being the custodian of sensitive personal information for thousands of tenants across the Netherlands. He needed verification without custody — a system that confirmed a tenant's identity and income and delivered a result to the landlord without his application ever holding the underlying documents.

## The Founder

Tom Bakker, a former property manager in Eindhoven who had screened tenants manually for eight years. He knew every pain point: landlords asking tenants for documents over email (insecure), tenants reluctant to share payslips with strangers (understandable), and the entire process creating an unencrypted trail of sensitive PDFs sitting in inboxes indefinitely. HuurCheck was designed to make verification fast, trustworthy, and compliant — but compliance was the part his AI tool couldn't generate.

## The Prototype

Built in Lovable, HuurCheck had a clean, functional frontend: landlords created verification requests, tenants received a link to upload documents, and the landlord saw a verification status on their dashboard. The UX was polished. The problem was the backend: the prototype stored uploaded documents (passport scans, payslips, employment contracts) directly in Supabase Storage — a flat file bucket with no encryption at rest, no automatic deletion policy, no access audit trail, and no mechanism to ensure documents were deleted after verification was complete. In its prototype state, HuurCheck was a liability waiting to happen.

## What LaunchStudio Built

The Manifera engineering team restructured HuurCheck's verification backend around a data-minimization architecture: the application facilitates verification without ever storing the sensitive documents on its own infrastructure.

**Third-party verification gateway:** Instead of receiving and storing documents directly, HuurCheck redirects tenants to a KYC (Know Your Customer) verification provider's hosted flow. The provider handles document upload, identity verification, and income confirmation in their certified infrastructure. HuurCheck receives only the verification result — "identity confirmed, income sufficient for the stated rent amount" or "verification incomplete, reason: document expired" — never the documents themselves.

**Result-only storage:** HuurCheck's database stores only the verification outcome, the timestamp, a reference ID (for the tenant to query their own status), and the verification provider's confidence score. No passport images, no salary figures, no employer names. The landlord sees "Verified ✓" or "Not Yet Verified" — the minimum information needed to make a leasing decision.

**Automatic data lifecycle:** Verification results are automatically deleted 90 days after the lease start date (configurable per landlord). The tenant's personal data never enters HuurCheck's database in the first place, and the verification result — the only data that does — has a defined expiration. Tenants can request immediate deletion of their verification record at any time through a self-service endpoint.

**Audit trail without data:** Every verification event (request created, tenant invited, verification initiated, result received, result viewed by landlord, result deleted) is logged with timestamps and actor IDs — but the log contains no personal data, only event types and anonymous identifiers. This satisfies GDPR's accountability requirement without creating a secondary store of sensitive information.

## The Result

HuurCheck launched with a verification flow that processes sensitive tenant data without ever storing it — making the platform a data facilitator rather than a data processor, with a dramatically simpler compliance profile. In the first three months, HuurCheck processed 187 tenant verifications for 34 landlords across Eindhoven, Tilburg, and Den Bosch, with zero sensitive documents stored on HuurCheck's infrastructure at any point.

> *"I thought compliance meant hiring a lawyer and writing a 50-page privacy policy. Turns out the best compliance strategy is never having the data in the first place. LaunchStudio designed the system so I couldn't get in trouble even if I tried."*
> — **Tom Bakker, Founder, HuurCheck (Eindhoven)**

**Cost & Timeline:** €3,500 (Launch & Grow Package, verification gateway integration + result-only storage + data lifecycle + audit trail) — live in 14 business days.

---

[LaunchStudio](https://launchstudio.eu/en/) builds data architectures that minimize liability by design — Manifera's engineers don't just secure data, they design systems that avoid holding it in the first place when possible.

[Tell us what sensitive data your prototype handles and we'll show you what doesn't need to be stored](https://launchstudio.eu/en/#contact) — the safest data is the data you never keep.

---

## Frequently Asked Questions

### If my app needs to process sensitive data, does that automatically make me a GDPR data processor?

It depends on whether you store the data or merely facilitate its processing by a certified third party. An application that redirects users to a KYC provider's hosted flow and receives only a yes/no result has a significantly simpler compliance profile than one that stores the underlying documents.

### Can data-minimization architecture work for any product that handles sensitive information?

In many cases, yes — the principle of "process but don't store" applies to identity verification, payment processing (Stripe handles PCI compliance so you don't have to), health data (HIPAA-compliant providers handle storage), and many other sensitive data categories. The architecture needs to be designed per use case.

### Does not storing sensitive data limit what my product can do?

It limits certain features — you can't display a tenant's payslip to the landlord if you never stored it, for example. But for most verification use cases, the result ("verified" or "not verified") is what the user actually needs, not the underlying document.

### What happens if the third-party verification provider has a data breach?

The breach is the provider's liability, not yours — you're using their certified infrastructure precisely so that your application doesn't bear the compliance burden. Your exposure is limited to the verification results you store, which contain no sensitive personal data.

### How much does using a third-party KYC provider cost compared to handling verification yourself?

KYC providers typically charge €1–€5 per verification. Building and maintaining your own GDPR-compliant document storage, identity verification, and data lifecycle management costs significantly more in development time, infrastructure, and ongoing compliance obligations.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "If my app needs to process sensitive data, does that automatically make me a GDPR data processor?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "It depends on whether you store the data or merely facilitate its processing by a certified third party. An application that receives only a yes/no result has a significantly simpler compliance profile than one that stores the underlying documents."
      }
    },
    {
      "@type": "Question",
      "name": "Can data-minimization architecture work for any product that handles sensitive information?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "In many cases, yes — the principle of 'process but don't store' applies to identity verification, payment processing, health data, and many other sensitive data categories."
      }
    },
    {
      "@type": "Question",
      "name": "Does not storing sensitive data limit what my product can do?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "It limits certain features, but for most verification use cases, the result is what the user actually needs, not the underlying document."
      }
    },
    {
      "@type": "Question",
      "name": "What happens if the third-party verification provider has a data breach?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "The breach is the provider's liability, not yours. Your exposure is limited to the verification results you store, which contain no sensitive personal data."
      }
    },
    {
      "@type": "Question",
      "name": "How much does using a third-party KYC provider cost compared to handling verification yourself?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "KYC providers typically charge €1-€5 per verification. Building your own GDPR-compliant verification infrastructure costs significantly more in development and ongoing compliance."
      }
    }
  ]
}
</script>
