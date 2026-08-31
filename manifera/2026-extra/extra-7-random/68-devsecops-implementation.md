---
title: "DevSecOps Implementation: Moving Security Left Without Slowing Delivery Down"
keywords: "DevSecOps implementation, DevSecOps pipeline, security in CI/CD"
buyer_stage: "Consideration"
target_persona: "VP of Engineering"
---

# DevSecOps Implementation: Moving Security Left Without Slowing Delivery Down

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "DevSecOps Implementation: Moving Security Left Without Slowing Delivery Down",
  "description": "A VP of Engineering's guide to implementing DevSecOps in a way that catches vulnerabilities early without turning the CI/CD pipeline into a bottleneck.",
  "author": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com/" },
  "datePublished": "2026-08-20",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://www.manifera.com/blog/devsecops-implementation" }
}
</script>

Most failed DevSecOps rollouts fail for the same reason: someone bolts a security scanner onto the CI pipeline, sets it to block the build on any finding above low severity, and within two sprints engineers are either drowning in false positives or have quietly figured out how to bypass the gate entirely. DevSecOps implementation done well isn't about adding a gate — it's about redesigning the pipeline so security checks run at the right stage, with the right severity thresholds, and give engineers a fix path instead of just a blocker.

**The Pain:** A VP of Engineering under pressure to "shift security left" often inherits or launches a DevSecOps initiative that's really just a new set of scanning tools pointed at the existing CI/CD pipeline, and without a genuine redesign of how, when, and against what severity thresholds those tools run, the initiative either creates so much pipeline friction that engineers route around it, or generates so much low-value noise that real findings get lost — either outcome leaves the organization no more secure than before the initiative started, just slower.

**The Agitation:** A DevSecOps rollout that engineers actively work around — disabling a check locally, merging past a failed gate with an override, silencing an entire scanner because of noise — doesn't just fail to reduce risk, it actively undermines security culture, since engineers who've learned that security gates are obstacles to route around rather than signals to trust are less likely to take the next genuine finding seriously, compounding the very risk the initiative was meant to reduce.

## What a Working DevSecOps Pipeline Actually Looks Like

**Security checks staged to match their cost of fixing.** The cheapest place to catch an issue is the IDE, via linting and pre-commit hooks for the fastest, cheapest checks; the pull request stage runs SAST and dependency scanning against the specific diff; and the deploy stage runs DAST and infrastructure-as-code scanning against the full running system — a working pipeline distributes checks across these stages by cost and speed, rather than running everything at every stage and creating unnecessary friction.

**Severity thresholds calibrated to actually block, not just warn.** A gate that blocks the build on every finding, including low-severity informational ones, trains engineers to treat all failures as noise; a gate that blocks only on high and critical severity findings, while surfacing medium and low findings as visible but non-blocking, preserves developer trust in the gate while still stopping the findings that matter.

**A defined remediation SLA, not an indefinite backlog.** Findings that don't block the build still need an owner and a deadline based on severity — critical findings remediated within days, high within a couple of weeks, medium on a longer cycle — otherwise non-blocking findings accumulate into a permanent, ignored backlog that defeats the purpose of surfacing them at all.

**Infrastructure as code scanned with the same rigor as application code.** Misconfigured cloud infrastructure — an overly permissive security group, a publicly exposed storage bucket — causes as many real-world breaches as application-layer vulnerabilities, and a genuine DevSecOps pipeline scans Terraform, CloudFormation, or equivalent IaC definitions in the same pull-request gate as application code, not as a separate, easily-skipped process.

**Security champions embedded in each team, not centralized in one silo.** A pipeline can flag issues, but resolving them well requires context a central security team doesn't have — a working DevSecOps model trains one or two engineers per team as security champions who triage findings with local context and escalate genuinely ambiguous ones, keeping remediation fast without requiring every team to wait on a central bottleneck.

## The Hybrid Hub: How Manifera Executes This

- **Amsterdam (Governance/Strategy):** Dutch leads design the pipeline's staged security architecture and severity thresholds, calibrated to block on what matters without training engineers to route around the gate.
- **Vietnam (Execution/Velocity):** Engineers in Ho Chi Minh City implement the staged scanning across IDE, PR, and deploy stages, and embed security champion practices directly within delivery teams.

This is Dutch Management × Vietnamese Mastery: European pipeline governance that calibrates security gates to preserve both trust and velocity, paired with execution capacity that implements it across the full CI/CD lifecycle. Learn more about [Manifera's dedicated teams](https://www.manifera.com/services/dedicated-teams/) and how a well-implemented DevSecOps pipeline catches real risk without becoming a bottleneck engineers learn to bypass.

## Case Study & Testimonial

### An Aarhus Logistics Platform's Pipeline Engineers Stopped Trusting

Aarhus DevOps ApS, a Danish logistics software provider, had rolled out a DevSecOps pipeline that blocked every build on any scanner finding, and within two months engineers had learned to add broad suppression comments to bypass the gate entirely — the VP of Engineering discovered that over 80% of recent findings had simply been suppressed rather than resolved, and genuine high-severity findings were buried in the same noise as trivial ones.

Manifera's team restaged the pipeline around severity-calibrated blocking, moved low-value checks to non-blocking visibility with a remediation SLA, and trained security champions on each of the client's three delivery teams. Suppression comments dropped to near zero within a quarter, and the two critical vulnerabilities the old noisy pipeline had missed during the review period were caught and fixed before reaching production.

> *"We had a pipeline that technically ran every scan you could ask for, and engineers had learned to ignore all of it. Manifera didn't add more scanning — they fixed the thresholds so the gate actually meant something again."*
> — **VP of Engineering, Aarhus DevOps ApS, Denmark**

## Bolted-On Scanning vs. Manifera's Calibrated DevSecOps Pipeline

| Criteria | Bolted-On Scanning | Manifera's Calibrated DevSecOps Pipeline |
|---|---|---|
| Check staging | Everything run at every stage | Distributed by cost — IDE, PR, deploy |
| Severity thresholds | Blocks on all findings, including low | Blocks only on high/critical, surfaces the rest |
| Non-blocking findings | Accumulate indefinitely, ignored | Owned with a defined remediation SLA |
| Infrastructure as code | Often unscanned or separate process | Scanned in the same PR gate as app code |
| Engineer trust in the gate | Erodes, leads to workarounds | Preserved through calibrated blocking |

## The Economics

A DevSecOps pipeline engineers route around costs the same engineering time as one that works, while providing none of the risk reduction — the cost isn't the tooling, it's the wasted pipeline friction and the false sense of security a bypassed gate creates. Recalibrating an existing pipeline's staging and thresholds is typically a matter of weeks, not a rebuild. [Talk to Manifera](https://www.manifera.com/contact-us/) about a DevSecOps implementation that catches real risk without slowing your delivery down.

## Frequently Asked Questions

### (Scenario: VP of Engineering whose security pipeline is generating constant developer pushback) Why do DevSecOps rollouts often fail even when the right scanning tools are in place?

Because the tools are typically bolted onto the existing pipeline without redesigning when checks run and what severity actually blocks the build, creating either excessive friction or noise that gets ignored.

### (Scenario: VP of Engineering deciding where in the pipeline to run different security checks) Where should different types of security checks run in a CI/CD pipeline?

Fast checks like linting belong in the IDE and pre-commit hooks, SAST and dependency scanning belong at the pull request stage against the diff, and DAST and infrastructure scanning belong at deploy against the full running system.

### (Scenario: VP of Engineering whose team has started suppressing scanner findings) Why does blocking the build on every severity level backfire?

Because it trains engineers to treat all failures as noise, leading them to bypass or suppress the gate entirely, which buries genuinely critical findings in the same noise as trivial ones.

### (Scenario: VP of Engineering evaluating whether infrastructure is covered by the security pipeline) Why does infrastructure-as-code need the same scanning rigor as application code?

Because misconfigured cloud infrastructure, like an exposed storage bucket, causes as many real-world breaches as application vulnerabilities, and skipping IaC scanning leaves that entire category unaddressed.

### (Scenario: VP of Engineering deciding how to staff security ownership across teams) What is a security champion and why does the model matter?

A security champion is an engineer embedded within a delivery team who triages findings with local context, keeping remediation fast without funneling every issue through a central security bottleneck.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "(Scenario: VP of Engineering whose security pipeline is generating constant developer pushback) Why do DevSecOps rollouts often fail even when the right scanning tools are in place?", "acceptedAnswer": { "@type": "Answer", "text": "Tools are bolted on without redesigning when checks run and what severity blocks the build, causing friction or ignored noise." } },
    { "@type": "Question", "name": "(Scenario: VP of Engineering deciding where in the pipeline to run different security checks) Where should different types of security checks run in a CI/CD pipeline?", "acceptedAnswer": { "@type": "Answer", "text": "Fast checks in the IDE, SAST/dependency scanning at the PR stage, DAST/infrastructure scanning at deploy." } },
    { "@type": "Question", "name": "(Scenario: VP of Engineering whose team has started suppressing scanner findings) Why does blocking the build on every severity level backfire?", "acceptedAnswer": { "@type": "Answer", "text": "It trains engineers to treat all failures as noise, leading to bypasses that bury genuinely critical findings." } },
    { "@type": "Question", "name": "(Scenario: VP of Engineering evaluating whether infrastructure is covered by the security pipeline) Why does infrastructure-as-code need the same scanning rigor as application code?", "acceptedAnswer": { "@type": "Answer", "text": "Misconfigured cloud infrastructure causes as many real breaches as application vulnerabilities." } },
    { "@type": "Question", "name": "(Scenario: VP of Engineering deciding how to staff security ownership across teams) What is a security champion and why does the model matter?", "acceptedAnswer": { "@type": "Answer", "text": "An embedded engineer who triages findings with local context, avoiding a central security bottleneck." } }
  ]
}
</script>
