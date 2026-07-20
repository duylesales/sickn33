---
Title: "Security and AI: Why the Second Word Needs the First One's Help"
Keywords: security and ai, ai and security, ai secure, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: Technical Solo Founder / Indie Hacker
---

# Security and AI: Why the Second Word Needs the First One's Help

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Security and AI: Why the Second Word Needs the First One's Help",
  "description": "A technical deep-dive into why security and AI-generated code don't automatically reinforce each other, using missing consent logging in an elder-care coordination platform as the concrete case.",
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
  "datePublished": "2026-07-25",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://launchstudio.eu/en/blog/security-and-ai-why-the-second-word-needs-the-first-ones-help"
  }
}
</script>

Security and AI sound like they belong together in a sentence, and increasingly they're marketed that way — "AI-powered security," "secure by design." What that phrasing tends to obscure is a much less flattering truth for founders building with AI coding tools: the AI half of that pairing doesn't reinforce the security half automatically. Someone still has to specifically ask for consent tracking, data retention limits, and access logging, because none of those show up as a natural consequence of a feature simply working.

## Why Consent Logging Is a Separate Requirement From "It Works"

A feature that lets a family member grant a caregiver access to an elderly relative's care schedule and health notes can work completely correctly — the access grant happens, the caregiver sees what they're supposed to see — without ever recording when and how consent for that access was actually given. Functionally, the feature is complete. From a compliance and accountability standpoint, something essential is still missing.

## Why This Distinction Matters More With Health-Adjacent Data Specifically

Health-adjacent personal data carries a higher bar under GDPR than ordinary account information, generally requiring a clearer, demonstrable basis for processing it and often an audit trail proving that basis exists. An AI coding tool generating an access-sharing feature has no inherent awareness of that heightened bar unless the prompt specifically described it — it simply builds the sharing mechanism as described, consent trail included only if consent trail was explicitly part of the description.

## Why a Working Feature Provides False Reassurance Here

Founders naturally judge a feature's completeness by whether it does what it's supposed to do, and a care-access sharing feature that successfully grants and revokes access passes that test easily. The specific, separate question — can we later prove who consented to what, and when — never gets tested by ordinary use, because using the feature normally never requires retrieving that historical record.

## Why This Gap Tends to Surface at the Worst Possible Moment

Missing consent records rarely cause a visible problem during day-to-day operation. They become urgently visible during a dispute, a regulatory inquiry, or a data subject access request — precisely the moments when a founder most needs to demonstrate exactly what happened and why, and precisely the moments when discovering the record was never kept is most damaging.

## What a Proper Fix Actually Adds

Closing this gap means adding a specific, append-only audit log recording every consent grant, modification, and revocation, tied to a timestamp and the identity of who authorized it — implemented alongside the existing access-sharing feature rather than replacing any part of it. [LaunchStudio](https://launchstudio.eu/en/) builds exactly this kind of consent and audit logging as part of its GDPR-focused review process, backed by Manifera's 11+ years of experience with compliance-sensitive B2B systems.

Manifera's compliance-adjacent engineering work is delivered through the Ho Chi Minh City development center on Pho Quang Street, with client scoping conversations handled from the Amsterdam headquarters at Herengracht 420.

[Schedule a free 15-minute introduction call](https://launchstudio.eu/en/#contact).

## Real example

### An AI-Native Founder in Action: The Care Access Nobody Could Trace

Bas, a former home-care coordinator turned founder in Almere, built ZorgVerbind, an AI-assisted elder care coordination platform built with Cursor, letting family members grant professional caregivers access to a relative's schedule and care notes.

A family dispute over who had authorized a particular caregiver's access prompted a request Bas couldn't fulfill: a clear record of when and by whom that access had originally been granted. LaunchStudio's review confirmed the access-sharing feature worked correctly but kept no historical consent trail at all — only the current state of who currently had access.

**Result:** LaunchStudio added an append-only audit log capturing every access grant, change, and revocation going forward, and worked with Bas to document the platform's data-handling practices accordingly, closing the compliance gap without altering how families and caregivers actually used the sharing feature.

> *"The feature itself worked exactly as intended the entire time. It just never occurred to me that 'worked' and 'can prove what happened six months ago' were two completely different things."*
> — **Bas Terpstra, Founder, ZorgVerbind (Almere)**

**Cost & Timeline:** €2,400 (consent and access audit logging implementation) — completed in 8 business days.

---

## Frequently Asked Questions

### Would a data protection officer consider missing consent logging a technical gap or a governance gap?

Both, and the overlap is the point — it's a governance requirement (demonstrating lawful basis for processing) that has to be satisfied through a technical mechanism (an actual audit trail), so neither framing alone fully captures why this needs deliberate engineering attention rather than a policy document alone.

### Does this kind of gap apply only to health-adjacent products, or more broadly?

It applies most acutely to health-adjacent and other sensitive-data products because of the heightened compliance bar, but any product processing personal data under an explicit consent basis benefits from the same kind of auditable trail, since "we're pretty sure this was authorized" is a weak position in any dispute.

### Manifera has worked with research-adjacent clients like TNO on data-sensitive projects — does that background inform how consent logging gets designed?

Yes — projects involving sensitive research data have long required exactly this kind of demonstrable, auditable consent trail, and that same design pattern transfers directly to a founder-built elder care platform facing analogous, if smaller-scale, obligations.

### Is this the kind of gap CEO Herre Roelevink refers to when describing the shift from building software to architecting it responsibly?

Yes, precisely — a consent log isn't a feature a user directly interacts with or notices, which is exactly the category of invisible architectural decision Roelevink has repeatedly pointed to as the harder, less obvious part of building software today.

### Could a founder add basic consent logging themselves without a full audit, just by keeping a spreadsheet?

A manual record can serve as a stopgap, but it doesn't scale reliably and is prone to being forgotten or falling out of sync with the actual state of the system — an engineered, append-only log tied directly to the access-granting code itself is what actually guarantees the record can't silently drift out of accuracy.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Is missing consent logging a technical gap or a governance gap?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Both — it's a governance requirement satisfied through a specific technical mechanism, an actual audit trail."
      }
    },
    {
      "@type": "Question",
      "name": "Does this gap apply only to health-adjacent products?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Most acutely there, but any product processing data under explicit consent benefits from an auditable trail."
      }
    },
    {
      "@type": "Question",
      "name": "Does research-adjacent client experience inform consent logging design?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes, sensitive research data projects have long required demonstrable, auditable consent trails."
      }
    },
    {
      "@type": "Question",
      "name": "Does this reflect the shift toward responsible architecture the CEO describes?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes, a consent log is exactly the kind of invisible architectural decision that framing points to."
      }
    },
    {
      "@type": "Question",
      "name": "Can a founder substitute a manual spreadsheet for proper consent logging?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "It can serve as a stopgap, but it doesn't scale reliably or stay in sync with the system's actual state."
      }
    }
  ]
}
</script>
