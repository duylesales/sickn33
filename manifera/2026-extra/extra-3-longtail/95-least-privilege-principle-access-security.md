---
title: "The Access Permission Nobody Remembers Granting Is Usually the One That Gets Exploited"
keywords: "GDPR compliance, software services, custom software development company, software development company"
buyer_stage: "Decision"
target_persona: "C"
---

# The Access Permission Nobody Remembers Granting Is Usually the One That Gets Exploited

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "The Access Permission Nobody Remembers Granting Is Usually the One That Gets Exploited",
  "description": "Why excess access permissions accumulate quietly in most systems, and a 1975 security principle that remains the standard defense against the specific risk they create.",
  "author": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com/" },
  "datePublished": "2026-08-17",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://www.manifera.com/blog/least-privilege-principle-access-security" }
}
</script>

A thorough security audit of a system that's been running in production for a few years routinely turns up access permissions nobody can immediately explain or account for — a service account with broader database access than its current function requires, a former contractor's credentials still technically active months later, an integration granted admin-level access for a one-time task that was simply never revoked afterward. None of these were ever granted maliciously. Each was, individually, a perfectly reasonable decision at the specific moment it was actually made. Together, they represent exactly the kind of accumulated risk a foundational security principle, formalized decades before modern cloud computing even existed, was specifically designed to prevent from the start.

## Why Excess Access Accumulates Even in a Well-Run System

Access permissions tend to consistently accumulate rather than shrink over a system's entire life for a simple, structural reason: granting access to solve an immediate problem is usually quick and low-friction, while revoking access once it's no longer needed requires someone to notice the access is unnecessary, remember to act on that observation, and actually follow through — a chain of steps considerably more prone to being skipped than the original granting decision was. This asymmetry means a system's actual access footprint tends to grow monotonically over time by default, not because anyone is being careless, but because the natural friction of granting versus revoking access points consistently in one direction.

## The Security Principle That Names the Correct Default

Computer scientists Jerome Saltzer and Michael Schroeder, in a foundational 1975 paper on the protection of information in computer systems, articulated the principle of least privilege: every program and every user should operate using the least amount of privilege necessary to complete their task, and no more. The principle's reasoning is direct — any privilege granted beyond what's strictly necessary doesn't provide any corresponding benefit under normal operation, since the excess access isn't being used for anything, but it does provide a corresponding cost under an abnormal one: if that account or system is ever compromised, the damage an attacker can do is bounded by the privileges available to compromise, not by what the account actually, legitimately needs.

Saltzer and Schroeder's principle remains, five decades later, the standard baseline for access control system design specifically because its logic doesn't depend on any particular technology — it's a statement about the asymmetric relationship between the near-zero benefit of excess privilege under normal conditions and the real, sometimes catastrophic cost of that same excess privilege under a breach condition. This asymmetry is precisely why "just in case" access — granting broader permissions than currently needed on the theory that it might save a future request — is a systematically bad trade under the principle: the hypothetical future convenience is real but small, while the compromise-scenario cost of that same excess access is uncertain in timing but potentially large when it does materialize.

## Why This Matters Specifically for GDPR and Regulated Data

Least privilege directly supports GDPR's data minimization principle at the access-control layer specifically, not just the data-collection layer most compliance conversations focus on: an account or integration with access to more personal data than its function requires is a data minimization gap even if the underlying data collection itself was fully justified and properly disclosed. A GDPR compliance review that checks data collection practices but doesn't audit actual access permissions against actual current need is examining only part of the relevant picture, leaving exactly the kind of accumulated excess-access risk this principle addresses unexamined.

## What Actually Implementing Least Privilege Requires

- **Grant access scoped to current task, not anticipated future need**, resisting the "just in case" instinct that predictably produces the excess-access accumulation this principle is designed to prevent.
- **Conduct periodic access reviews, not just initial provisioning discipline**, since the principle addresses a static allocation decision, but the real risk accumulates over time as roles change and tasks end without a corresponding revocation.
- **Automate revocation tied to specific triggers** — contract end dates, role changes, project completion — rather than relying on someone remembering to manually revoke access once it's no longer needed.
- **Audit service accounts and integrations with the same rigor as human user accounts**, since these often carry broad, rarely-reviewed access and represent a specific, common blind spot in access control discipline.

## Why Saltzer and Schroeder's Original Framing Still Outperforms Newer Alternatives

Saltzer and Schroeder's 1975 paper actually articulated several security design principles together, and it's worth noting why least privilege specifically has proven more durable in practice than some of its companion principles from the same paper — it's stated as a default posture rather than a specific technical mechanism, which means it survives changes in the underlying technology in a way a more implementation-specific rule wouldn't. The principle doesn't say anything about databases, cloud platforms, or APIs, none of which existed in their modern form in 1975 — it says access should default to the minimum necessary, a statement general enough to apply cleanly to a mainframe terminal in 1975 and a cloud IAM policy in 2026 without modification.

This generality is exactly why the principle keeps getting rediscovered and re-cited across every subsequent era of computing security literature, including in the zero trust architecture Kindervag formalized decades later, which explicitly incorporates least privilege as one of its core mechanisms rather than treating it as a separate, older idea. A CISO evaluating a modern security framework is very likely, whether the framework's own literature makes this explicit or not, evaluating a specific technical implementation of a design principle that predates essentially every technology the implementation actually runs on — which is a genuinely useful thing to know when deciding how much confidence to place in the underlying reasoning, independent of whatever specific vendor or platform happens to be implementing it today.

## Manifera's Approach: Building Least Privilege Into Access Architecture From the Start

- **Amsterdam (Governance/Access Discipline as Standard Practice):** Dutch project leads implement least-privilege access architecture as a default standard, connecting it explicitly to GDPR data minimization requirements during compliance-focused engagements.
- **Vietnam (Execution/Scoped, Auditable Access Implementation):** The engineering pod implements granular, scoped access controls and builds in periodic review mechanisms, rather than defaulting to broad access for development convenience.

This is Dutch Management × Vietnamese Mastery applied to access control architecture itself: governance that treats least privilege as a standing discipline connected directly to compliance requirements, paired with execution that implements genuinely scoped, auditable access as standard practice. Explore Manifera's approach to secure [custom software development](https://www.manifera.com/services/custom-software-development/) for regulated industries.

## Case Study: A Patras Insurer's Access Audit Discovery

Achaïki Asfaleies, a Patras-based insurer, commissioned a routine security audit ahead of a scheduled GDPR compliance review and found forty-three active accounts and service integrations with access to customer personal data considerably broader than their current function actually required, including credentials belonging to two former contractors whose engagements had ended over a year earlier, and an analytics integration retaining full database read access from an initial setup task completed eighteen months prior.

Manifera's Amsterdam team, engaged for the subsequent remediation, implemented a least-privilege access architecture with scoped permissions tied to specific current roles, along with an automated review process triggered by contract end dates and role changes, closing the specific gap that had allowed access to accumulate silently over several years without anyone deliberately deciding it should.

> *"Nobody had granted any of this maliciously. Every single one of the forty-three was a reasonable decision at the time it was made. The problem was that revoking access was never anyone's job the way granting it had been."*
> — **CISO, Achaïki Asfaleies**

Achaïki Asfaleies now runs a formal quarterly access review as standard practice and has automated revocation tied to contract and role-change events, directly addressing the structural asymmetry between easy granting and neglected revoking that had allowed the original gap to accumulate over several years without anyone noticing.

## Access Granting vs. Access Revocation Discipline

| Aspect | Access Granting | Access Revocation |
|---|---|---|
| Typical friction | Low, quick to approve | High, requires deliberate follow-up |
| Default behavior without discipline | Happens readily | Often skipped or delayed |
| Risk if imbalanced | Accumulated excess privilege | N/A |
| Fix | Scope to current task only | Automate triggers, periodic review |

## Auditing Your Own System's Access Footprint

Commission a genuine, thorough access audit examining current permissions against current actual need, not just initial provisioning decisions made long ago — the gap between the two tends to grow silently over a system's life without anyone deciding it should. [Talk to one of our senior architects](https://www.manifera.com/contact-us/) about a least-privilege access architecture review.

## Frequently Asked Questions

### (Scenario: CISO discovering excess access during a routine audit) Why do systems consistently accumulate excess access permissions over time even without any specific security failure?

Granting access is quick and low-friction, while revoking it requires someone to notice it's unnecessary and follow through — an asymmetry that means access footprints tend to grow by default unless deliberately and periodically reviewed.

### (Scenario: compliance officer connecting access control to GDPR) How does the principle of least privilege connect specifically to GDPR compliance?

It supports data minimization at the access-control layer — an account with more access to personal data than its function requires is a minimization gap even if the underlying data collection itself was fully justified and disclosed.

### (Scenario: IT manager trying to prevent this accumulation proactively) What's the most effective way to prevent excess access from accumulating in the first place?

Automate revocation tied to specific triggers like contract end dates and role changes, rather than relying on someone remembering to manually revoke access once a task or engagement ends.

### (Scenario: security lead trying to prioritize a review) Should service accounts and integrations be reviewed with the same rigor as human user accounts?

Yes, and often with more, since service accounts and integrations frequently carry broad access granted for a specific setup task and are reviewed far less often than human accounts, making them a common, underexamined blind spot.

### (Scenario: founder trying to understand the real risk of excess access) What's the actual risk of an unused excess permission that's never being actively exploited?

The risk isn't in normal operation — it's that if the account is ever compromised, the damage an attacker can do is bounded by the account's total privileges, not by what the account legitimately uses, making unused excess access a pure liability with no offsetting benefit.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "(Scenario: CISO discovering excess access during a routine audit) Why do systems consistently accumulate excess access permissions over time even without any specific security failure?", "acceptedAnswer": { "@type": "Answer", "text": "Granting access is low-friction while revoking requires deliberate follow-up — an asymmetry that makes access footprints grow by default." } },
    { "@type": "Question", "name": "(Scenario: compliance officer connecting access control to GDPR) How does the principle of least privilege connect specifically to GDPR compliance?", "acceptedAnswer": { "@type": "Answer", "text": "It supports data minimization at the access-control layer, since excess access to personal data is a minimization gap on its own." } },
    { "@type": "Question", "name": "(Scenario: IT manager trying to prevent this accumulation proactively) What's the most effective way to prevent excess access from accumulating in the first place?", "acceptedAnswer": { "@type": "Answer", "text": "Automate revocation tied to specific triggers like contract end dates and role changes, rather than relying on manual follow-through." } },
    { "@type": "Question", "name": "(Scenario: security lead trying to prioritize a review) Should service accounts and integrations be reviewed with the same rigor as human user accounts?", "acceptedAnswer": { "@type": "Answer", "text": "Yes, and often with more — service accounts frequently carry broad access and are reviewed far less often than human accounts." } },
    { "@type": "Question", "name": "(Scenario: founder trying to understand the real risk of excess access) What's the actual risk of an unused excess permission that's never being actively exploited?", "acceptedAnswer": { "@type": "Answer", "text": "If the account is ever compromised, damage is bounded by total privileges, not actual use, making unused excess access a pure liability." } }
  ]
}
</script>
