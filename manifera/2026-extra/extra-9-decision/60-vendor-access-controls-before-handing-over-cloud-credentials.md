---
title: "Vendor Access Controls: What to Verify Before Handing Over Cloud Credentials"
keywords: "vendor cloud access controls, cloud credentials vendor security, third-party access management, vendor security due diligence, cloud vendor IAM policy"
buyer_stage: "Decision"
target_persona: "Security Lead"
---

# Vendor Access Controls: What to Verify Before Handing Over Cloud Credentials

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Vendor Access Controls: What to Verify Before Handing Over Cloud Credentials",
  "description": "A Security Lead's verification checklist for a DevOps or development vendor's access control practices before granting cloud credentials, covering least-privilege IAM, just-in-time access, offboarding, audit logging, and secrets management.",
  "author": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com/" },
  "datePublished": "2026-08-27",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://www.manifera.com/blog/vendor-access-controls-before-handing-over-cloud-credentials" }
}
</script>

Eleven months. That's how long a former contractor's AWS console access sat active after a vendor engagement at a European healthtech company had already ended — a root-adjacent IAM user created during onboarding for "convenience," never scoped down, and never removed during offboarding because no one owned that step in the vendor relationship. Nothing malicious happened during those eleven months, as far as the subsequent audit could determine. But the exposure had existed the entire time, invisible until a routine access review finally caught it, and the postmortem made clear the root cause wasn't a technical failure — it was the absence of an access control agreement specific enough to prevent it in the first place.

This scenario is common enough that it should shape how every Security Lead approaches handing cloud credentials to a development or DevOps vendor, not treated as an unlucky edge case. The convenience of broad access during a fast-moving engagement is real, and it is exactly the tradeoff that creates lingering exposure long after the convenience is forgotten. This article covers what to verify — and what to demand in writing — before a vendor gets anywhere near your cloud environment.

## Least-Privilege IAM, Not Convenience Access

The single most common access control failure in vendor relationships is granting broad permissions upfront to avoid the friction of scoping access precisely, with the intention of tightening it later — a step that, in practice, rarely happens once the engagement is underway and everyone is focused on delivery rather than access hygiene. Ask the vendor directly how they scope IAM permissions for a new engagement: do they request the minimum access needed for the current phase of work, with a defined process for requesting additional scope as the project evolves, or do they default to broad administrative access "to move faster." A vendor with a mature security practice will have a standard least-privilege onboarding process they can describe specifically, including how they determine what access level a given task actually requires, rather than defaulting to the broadest role available to avoid follow-up requests.

## Time-Boxed and Just-in-Time Access

Standing access — credentials that remain valid indefinitely regardless of whether they're actively being used — is a materially larger attack surface than time-boxed access that expires automatically and must be actively renewed. Ask whether the vendor supports just-in-time access provisioning, where elevated permissions are granted for a specific task or time window and automatically revoked afterward, rather than persistent credentials that sit active for the full duration of the engagement whether or not they're in daily use. This matters especially for any access tier above routine deployment permissions — production database access, infrastructure administrative rights, anything touching customer data directly — where the cost of a credential compromise is highest and the operational need for standing access is usually lowest.

## MFA, SSO, and Offboarding Guarantees in Writing

Multi-factor authentication and single sign-on integration for vendor access should be non-negotiable baseline requirements, not points of negotiation — but the more consequential and more frequently overlooked question is offboarding: what is the vendor's documented process for access removal when an individual engineer rotates off your project, or when the engagement ends entirely, and how quickly does it actually happen in practice versus on paper. Ask for the offboarding SLA in writing — a specific number of hours or days, not "promptly" — and ask how the vendor verifies deprovisioning was actually completed, since a documented process that isn't verified is only slightly better than no process at all. The eleven-month gap in the scenario above existed precisely because no one on either side owned the verification step.

## Audit Logging You Control, Not Just the Vendor

Relying solely on a vendor's internal audit logs for visibility into what their team did with your credentials creates a dependency on the vendor's own record-keeping being both accurate and available to you on request — a reasonable assumption most of the time, but not one worth building your only layer of accountability on. Insist on independent audit logging on your side of the access boundary: cloud provider-native logging (CloudTrail, Azure Activity Log, or equivalent) covering every action taken under vendor-provisioned credentials, retained and reviewable by your own security team regardless of what the vendor separately tracks. This gives you an independent record that doesn't depend on the vendor's cooperation or continued existence as a company to remain available during a future investigation.

## Secrets Management and Credential Rotation Practices

Ask specifically how the vendor stores and handles credentials during the engagement — a dedicated secrets manager with access logging, or credentials shared over email, chat, or a shared document, which happens more often than most Security Leads assume, particularly under project deadline pressure. Also ask about rotation cadence: are shared credentials rotated on a defined schedule, and immediately upon any team member change, or do they persist unchanged for the life of the engagement. A vendor's answer to this single question is often a reliable proxy for their overall security maturity, since secrets handling practices tend to reflect an organization's broader security culture rather than existing as an isolated policy.

## Network-Level Controls: VPN, Bastion Hosts, and IP Allowlisting

Identity and access management is only one layer of a complete vendor access strategy — network-level controls add a second, independent barrier that remains effective even if a credential is somehow compromised. Ask whether the vendor connects through a dedicated VPN or bastion host rather than accessing your cloud console or infrastructure directly from the open internet, and whether their access can be restricted to specific IP ranges tied to their known office or remote-work infrastructure rather than accepted from anywhere in the world. For particularly sensitive environments, consider requiring that vendor access route through infrastructure you control end to end — a jump host or bastion instance in your own environment that logs every session, rather than relying entirely on the vendor's own network security posture, about which you have limited visibility and no direct control. This layered approach means that even a fully compromised vendor credential, on its own, isn't sufficient for an attacker to reach your production environment, since the network path itself imposes an additional, independently monitored barrier that a stolen password or API key alone can't bypass.

## What a Real Access Control Clause Looks Like in the Contract

Verbal assurances about access control practices are only as durable as the person who gave them; a contract clause is durable regardless of staff turnover on either side. A strong access control clause specifies the least-privilege scoping approach, MFA and SSO requirements, a numeric offboarding SLA with a verification step, independent audit logging rights retained by your organization, and a defined secrets management and rotation standard — each as a specific, checkable commitment rather than a general statement that the vendor "follows security best practices." Push back on any vendor contract that describes access security only in general terms; specificity in this clause is a leading indicator of whether the practice behind it is real.

Manifera's development engagements are provisioned under least-privilege, time-boxed access as standard practice, with documented offboarding SLAs and independent client-side audit logging built into how we structure cloud access from day one — a discipline shaped by working with regulated European clients in finance and healthcare across our [offshore software development](https://www.manifera.com/services/offshore-software-development/) engagements. Our [about us](https://www.manifera.com/about-us/our-way-of-working/) page details how our Amsterdam-based team owns the access governance conversation directly with your security function, rather than leaving it to be negotiated informally between engineers mid-project.

If your organization is about to grant a development vendor access to production cloud infrastructure and wants a documented access control agreement in writing before day one, talk to Manifera's team about how we structure vendor access for security-sensitive engagements.

## A Quarterly Access Review, Not Just an Onboarding Checklist

Everything above covers what to verify before granting access. Just as important, and far more often skipped, is a recurring review while the engagement is active — the eleven-month gap in this article's opening scenario wasn't caught at onboarding, it was caught by a routine review that should have happened much sooner. Run this four-point check quarterly for any active vendor engagement with cloud access:

1. **Cross-reference active credentials against current vendor headcount on your project.** Any credential tied to someone who's rotated off is a finding, not a formality — flag and revoke within the same review cycle.
2. **Spot-check that access scope still matches current project phase.** Permissions granted for an early infrastructure-setup phase often remain long after that phase ends and are never scoped back down.
3. **Confirm MFA and SSO enrollment is still active for every vendor account**, not just verified once at initial provisioning.
4. **Pull your own independent audit log** (not the vendor's) and sample a handful of actions against what the vendor's team reports doing — a mismatch here is a higher-priority finding than almost anything else on this list.

A quarterly cadence catches drift within roughly 90 days instead of eleven months. Assign this review to a named owner on your security team, not "whoever remembers" — the original healthtech incident had a documented offboarding process on paper; what it lacked was anyone specifically accountable for checking that the process had actually run.

## Frequently Asked Questions

### What is least-privilege access for a development vendor?

Least-privilege access means granting a vendor only the specific permissions needed for their current phase of work, with a defined process to request additional scope as the project evolves, rather than defaulting to broad administrative access for convenience.

### Why is just-in-time access more secure than standing vendor credentials?

Standing credentials remain valid indefinitely whether or not they're actively used, creating a larger attack surface over time. Just-in-time access grants elevated permissions for a specific task or window and revokes them automatically afterward, minimizing the exposure window.

### How quickly should a vendor deprovision access after an engagement ends?

There's no single universal number, but the SLA should be specific and stated in writing, typically within 24 to 48 hours, with a verification step confirming deprovisioning actually occurred rather than relying on an unverified internal process.

### Should I rely on a vendor's own audit logs for access accountability?

No, not exclusively. Maintain independent, cloud provider-native audit logging on your own side of the access boundary, covering every action taken under vendor-provisioned credentials, so accountability doesn't depend solely on the vendor's own record-keeping.

### What should an access control clause in a vendor contract specify?

It should specify the least-privilege scoping approach, MFA and SSO requirements, a numeric offboarding SLA with a verification step, independent audit logging rights retained by your organization, and a defined secrets management and rotation standard.

### (Scenario: A Security Lead is deciding how often to review active vendor access after signing a strong access control contract) How often should I review a vendor's active access permissions during an ongoing engagement, not just at onboarding?

Quarterly, at minimum, with a named owner on your security team responsible for running it. A strong contract clause at signing doesn't self-enforce — the eleven-month exposure gap in this article's scenario existed despite a documented offboarding process, because no one was specifically accountable for verifying it actually ran.

### (Scenario: A quarterly access review finds a credential still active for a contractor who rotated off the project two months earlier) What should I do if a quarterly access review finds a credential still active for someone who's already left the vendor's team?

Revoke it immediately within the same review cycle and treat it as a process failure worth raising with the vendor directly, not just a housekeeping fix. A single missed revocation is a signal worth investigating for a pattern — ask the vendor to walk through why their offboarding process didn't catch this specific case.

### (Scenario: A Security Lead wants to compare the vendor's self-reported activity log against independent cloud provider logs) How do I actually compare a vendor's self-reported activity against my own independent audit log?

Sample a handful of specific actions or time windows from your own cloud provider-native logging (CloudTrail or equivalent) and ask the vendor to independently confirm what their team did during those same windows without showing them your log first. A mismatch between the two accounts, even a small one, is a higher-priority finding than most other items on a routine review.

### (Scenario: An engagement was scoped for an initial infrastructure buildout phase six months ago, and the project has since moved into steady-state maintenance) Does access scope need to be reviewed even if a vendor's permissions were correctly minimal at the start of the engagement?

Yes. Permissions that were appropriately scoped for an early, more intensive project phase often remain unchanged long after the project moves into a lower-access-need phase like steady-state maintenance. Access scope should shrink as project needs shrink, and that adjustment rarely happens automatically without a scheduled review to trigger it.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What is least-privilege access for a development vendor?",
      "acceptedAnswer": { "@type": "Answer", "text": "Least-privilege access means granting a vendor only the specific permissions needed for their current phase of work, with a defined process to request additional scope, rather than defaulting to broad administrative access for convenience." }
    },
    {
      "@type": "Question",
      "name": "Why is just-in-time access more secure than standing vendor credentials?",
      "acceptedAnswer": { "@type": "Answer", "text": "Standing credentials remain valid indefinitely whether or not they're used, creating a larger attack surface over time. Just-in-time access grants elevated permissions for a specific task or window and revokes them automatically afterward." }
    },
    {
      "@type": "Question",
      "name": "How quickly should a vendor deprovision access after an engagement ends?",
      "acceptedAnswer": { "@type": "Answer", "text": "The SLA should be specific and stated in writing, typically within 24 to 48 hours, with a verification step confirming deprovisioning actually occurred rather than relying on an unverified internal process." }
    },
    {
      "@type": "Question",
      "name": "Should I rely on a vendor's own audit logs for access accountability?",
      "acceptedAnswer": { "@type": "Answer", "text": "No, not exclusively. Maintain independent, cloud provider-native audit logging on your own side of the access boundary so accountability doesn't depend solely on the vendor's own record-keeping." }
    },
    {
      "@type": "Question",
      "name": "What should an access control clause in a vendor contract specify?",
      "acceptedAnswer": { "@type": "Answer", "text": "It should specify least-privilege scoping, MFA and SSO requirements, a numeric offboarding SLA with a verification step, independent audit logging rights, and a defined secrets management and rotation standard." }
    },
    {
      "@type": "Question",
      "name": "How often should I review a vendor's active access permissions during an ongoing engagement, not just at onboarding?",
      "acceptedAnswer": { "@type": "Answer", "text": "Quarterly, at minimum, with a named owner on your security team responsible for running it. A strong contract clause doesn't self-enforce, which is exactly how an eleven-month exposure gap can persist despite a documented offboarding process on paper." }
    },
    {
      "@type": "Question",
      "name": "What should I do if a quarterly access review finds a credential still active for someone who's already left the vendor's team?",
      "acceptedAnswer": { "@type": "Answer", "text": "Revoke it immediately within the same review cycle and raise it with the vendor as a process failure, not just a housekeeping fix. A single missed revocation is worth investigating for a broader pattern." }
    },
    {
      "@type": "Question",
      "name": "How do I actually compare a vendor's self-reported activity against my own independent audit log?",
      "acceptedAnswer": { "@type": "Answer", "text": "Sample specific actions or time windows from your own cloud provider-native logging and ask the vendor to independently confirm what their team did during those windows without showing them your log first. Any mismatch is a high-priority finding." }
    },
    {
      "@type": "Question",
      "name": "Does access scope need to be reviewed even if a vendor's permissions were correctly minimal at the start of the engagement?",
      "acceptedAnswer": { "@type": "Answer", "text": "Yes. Permissions scoped for an early, intensive project phase often remain unchanged after the project moves into a lower-access-need phase like steady-state maintenance, and that adjustment rarely happens without a scheduled review." }
    }
  ]
}
</script>
