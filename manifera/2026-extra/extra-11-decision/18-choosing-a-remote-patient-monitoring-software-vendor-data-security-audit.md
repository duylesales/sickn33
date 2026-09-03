---
title: "Choosing a Remote Patient Monitoring Software Vendor: The Data Security Audit"
keywords: "remote patient monitoring vendor, RPM software vendor selection, patient monitoring data security, connected health device vendor, RPM platform due diligence"
buyer_stage: "Decision"
target_persona: "Security Lead"
---

# Choosing a Remote Patient Monitoring Software Vendor: The Data Security Audit

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Choosing a Remote Patient Monitoring Software Vendor: The Data Security Audit",
  "description": "A security lead's audit framework for evaluating remote patient monitoring vendors against medical device cybersecurity and HIPAA technical safeguard requirements.",
  "author": {"@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com/"},
  "publisher": {"@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com/"},
  "datePublished": "2026-09-10",
  "mainEntityOfPage": {"@type": "WebPage", "@id": "https://www.manifera.com/blog/choosing-a-remote-patient-monitoring-software-vendor-data-security-audit"}
}
</script>

A remote patient monitoring device sitting in a patient's home is a different security problem than a server in a data center, and most security leads evaluating RPM vendors underestimate by how much. That device is on the patient's home Wi-Fi, often behind consumer-grade router security nobody controls, transmitting physiological data continuously to a cloud platform, and — in a growing number of products — running embedded software that hasn't been patched since it shipped. When FDA's postmarket cybersecurity guidance talks about connected medical devices as a persistent attack surface rather than a one-time certification event, RPM is close to the reference case. A vendor's security posture needs evaluating as an ongoing operational practice, not a point-in-time certification you check once during procurement.

Choosing an RPM software vendor means running a real security audit against the full data path — device, transmission, cloud platform, and the clinical workflow consuming the data — not accepting a vendor's self-reported compliance checklist at face value.

## The Attack Surface RPM Actually Creates

Map the actual data flow before evaluating anything else: a sensor or wearable (glucose monitor, cardiac monitor, pulse oximeter, blood pressure cuff) captures physiological data, transmits it via Bluetooth or cellular to a gateway or directly to the cloud, the cloud platform processes and stores it, and a clinical dashboard surfaces it to care teams for action. Each hop is a distinct security domain: device firmware security, transmission encryption, cloud infrastructure security, and application-layer access control. A vendor who can only speak fluently about their cloud platform's security — SOC 2 report, encryption at rest — while giving vague answers about device firmware update mechanisms or Bluetooth pairing security is only auditing half the system.

## HIPAA Security Rule Meets Medical Device Cybersecurity

Two regulatory frameworks apply simultaneously and vendors don't always treat them as connected. HIPAA's Security Rule (45 CFR 164.312) governs the technical safeguards for PHI once it's in the vendor's systems — access controls, encryption, audit logging. Separately, if the monitoring device itself is a regulated medical device (most clinically-oriented RPM devices are at least Class II), FDA's premarket and postmarket cybersecurity guidance applies to the device itself — vulnerability disclosure processes, a maintained Software Bill of Materials (SBOM) per Section 524B, and a documented process for patching vulnerabilities in fielded devices, not just newly manufactured ones. Ask a vendor how these two frameworks intersect in their actual practice: does their HIPAA-driven incident response process also trigger the device-cybersecurity vulnerability disclosure process when relevant, or are these two disconnected compliance tracks run by different teams who don't talk to each other?

## What a Real Security Audit Should Cover

Structure the audit around specifics, not a general questionnaire:

**Encryption.** Confirm TLS 1.2+ (ideally 1.3) for data in transit at every hop — device to gateway, gateway to cloud, cloud to dashboard — and AES-256 or equivalent for data at rest. Ask specifically whether device-to-gateway Bluetooth communication is encrypted and paired securely, since Bluetooth Low Energy implementations vary widely in actual security regardless of the spec's theoretical capability.

**SBOM and vulnerability management.** Request the vendor's current Software Bill of Materials for both the cloud platform and the device firmware, and ask about their CVE monitoring cadence — how quickly do they assess and patch a newly disclosed vulnerability in a third-party component their stack depends on? A vendor without a defined SLA for this (e.g., critical vulnerabilities patched or mitigated within a defined number of days) doesn't have an operational security program, just a policy document.

**Penetration testing cadence.** Ask for evidence of independent, third-party penetration testing — not just internal security review — covering the full stack including the device firmware and mobile companion app, not only the cloud API. Annual testing is a reasonable minimum; verify the most recent report's findings were actually remediated, not just documented.

**Device provisioning and de-provisioning.** When a patient's monitoring period ends or a device is returned, what happens to the data and the device's network credentials? A device that retains stored Wi-Fi credentials or patient-specific tokens after return is a real risk if devices are refurbished and redistributed, which is common practice for cost reasons in RPM programs.

## Vendor Red Flags

Be cautious of a vendor who treats their cloud platform's SOC 2 report as covering the entire system, when SOC 2 scope frequently excludes the device and firmware layer entirely — read the report's system description section to confirm scope rather than assuming. Be cautious of vendors without a public or responsibly-disclosed vulnerability reporting process (a security.txt file, a bug bounty program, or at minimum a documented contact for security researchers) — its absence suggests security isn't operationalized as an ongoing practice. And be skeptical of any vendor who can't produce evidence of a specific past incident response — not because incidents are disqualifying (they're common in any mature security program) but because a vendor's description of how they actually handled a real vulnerability disclosure or near-miss tells you more than a clean-slate claim of zero incidents ever will.

## Questions for the Security Assessment

Beyond the technical audit, ask operationally: who owns security incident response across the device manufacturer (if different from the software vendor) and the platform vendor, and how is that coordination actually tested (a tabletop exercise, or just a shared contact list)? How does the vendor handle end-of-life for older device models still in patient homes when a critical vulnerability is discovered — is there a recall or remote patch process, and has it ever been exercised in practice? What's their data retention and deletion policy for physiological data after a monitoring program ends, and is it enforced technically or just documented as policy?

## Making the Call

RPM security due diligence has to span device, transmission, cloud, and clinical workflow as one connected system, because attackers don't respect the boundaries between a vendor's marketing categories. A vendor confident enough to walk through their SBOM, patch SLA, and most recent penetration test findings in specific detail is signaling a mature program; one who redirects every question back to a SOC 2 report is signaling an incomplete one. Manifera builds connected health platforms with this full-stack security posture in mind, and our [custom software development](https://www.manifera.com/services/custom-software-development/) and [mobile app development](https://www.manifera.com/services/mobile-app-development/) teams treat device-to-cloud security as a single design problem rather than separate workstreams. For the HIPAA contractual side of this evaluation, see our companion article on [the BAA clauses that actually protect you](https://www.manifera.com/blog/hipaa-compliant-software-vendors-the-baa-clauses-that-actually-protect-you).

## Frequently Asked Questions

### Does a vendor's SOC 2 Type II report cover their RPM device security?
Not necessarily — check the report's system description carefully, since SOC 2 scope for a healthcare software vendor is often limited to the cloud platform and doesn't include connected device firmware or Bluetooth transmission security. Ask the vendor explicitly what is and isn't in scope before relying on the report as proof of full-stack security.

### How often should RPM vendors conduct penetration testing?
Annual third-party penetration testing covering the full stack — cloud API, mobile app, and device firmware where feasible — is a reasonable baseline, with additional testing after major architecture changes. Verify that findings from the most recent test were actually remediated, not just documented in a report.

### What happens to patient data when an RPM device is returned or reused?
This should be a documented, technically-enforced process, not just policy — stored credentials, cached patient data, and pairing information need to be wiped before a device is redistributed to another patient, which is common practice in cost-conscious RPM programs.

### Is HIPAA compliance sufficient for a connected medical device, or do we need medical device cybersecurity compliance too?
Both apply and address different things. HIPAA's Security Rule governs PHI protection once data reaches the vendor's systems, while FDA's medical device cybersecurity requirements, including SBOM maintenance under Section 524B, apply to the device itself if it's a regulated medical device. A mature vendor treats these as connected, not separate compliance tracks.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Does a vendor's SOC 2 Type II report cover their RPM device security?",
      "acceptedAnswer": {"@type": "Answer", "text": "Not necessarily. The report's system description should be checked carefully, since SOC 2 scope for a healthcare software vendor is often limited to the cloud platform and doesn't include connected device firmware or Bluetooth transmission security."}
    },
    {
      "@type": "Question",
      "name": "How often should RPM vendors conduct penetration testing?",
      "acceptedAnswer": {"@type": "Answer", "text": "Annual third-party penetration testing covering the full stack, including the cloud API, mobile app, and device firmware where feasible, is a reasonable baseline, with additional testing after major architecture changes. Findings from the most recent test should be confirmed as actually remediated, not just documented."}
    },
    {
      "@type": "Question",
      "name": "What happens to patient data when an RPM device is returned or reused?",
      "acceptedAnswer": {"@type": "Answer", "text": "This should be a documented, technically-enforced process rather than just policy. Stored credentials, cached patient data, and pairing information need to be wiped before a device is redistributed to another patient, which is common practice in cost-conscious RPM programs."}
    },
    {
      "@type": "Question",
      "name": "Is HIPAA compliance sufficient for a connected medical device, or do we need medical device cybersecurity compliance too?",
      "acceptedAnswer": {"@type": "Answer", "text": "Both apply and address different things. HIPAA's Security Rule governs PHI protection once data reaches the vendor's systems, while FDA's medical device cybersecurity requirements, including SBOM maintenance under Section 524B, apply to the device itself if it's a regulated medical device."}
    }
  ]
}
</script>
