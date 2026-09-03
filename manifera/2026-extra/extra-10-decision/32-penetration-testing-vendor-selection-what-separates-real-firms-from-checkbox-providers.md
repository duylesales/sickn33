---
title: "Penetration Testing Vendor Selection: What Separates Real Firms From Checkbox Providers"
keywords: "penetration testing vendor, CREST certified pentest, OSCP OSCE, pentest report quality, red team vs pentest, security testing methodology"
buyer_stage: "Decision"
target_persona: "Security Lead"
---

# Penetration Testing Vendor Selection: What Separates Real Firms From Checkbox Providers

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Penetration Testing Vendor Selection: What Separates Real Firms From Checkbox Providers",
  "description": "A Security Lead's guide to distinguishing genuine penetration testing firms from automated-scan providers, covering certifications, methodology, report quality, and retesting practices.",
  "author": {"@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com/"},
  "publisher": {"@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com/"},
  "datePublished": "2026-08-18",
  "mainEntityOfPage": {"@type": "WebPage", "@id": "https://www.manifera.com/blog/penetration-testing-vendor-selection-what-separates-real-firms-from-checkbox-providers"}
}
</script>

Last year's pentest report ran to 40 pages, listed twelve findings, all "informational" or "low," and cost €8,000. Six months later, a real attacker found a critical authentication bypass in an endpoint that report never mentioned. Somewhere between "we did a pentest" and "we are actually secure" sits a gap that most procurement processes never manage to close.

The penetration testing market has a structural problem: the buyer, usually you, often cannot easily distinguish a rigorous manual assessment from a rebranded vulnerability scan, because both arrive as a PDF with a similar cover page and a CVSS-scored findings table. The checkbox providers know this, and they've built a business model around it — cheap, fast, compliance-satisfying reports that create the appearance of security testing without the substance. This article gives you the specific, checkable signals that separate the two before you sign, not after an incident reveals the gap.

## The "Checkbox Pentest" Business Model

A checkbox provider's economics depend on volume: run automated scanning tools (Nessus, Burp Suite's automated crawler, OpenVAS) against your assets, wrap the tool's own output in a templated report, and move to the next client within days. This is genuinely useful as a vulnerability scan — it is not a penetration test, because it never attempts exploitation, chaining of low-severity findings into a critical path, or business-logic flaws that no automated tool can recognize (broken authorization between tenants, price manipulation in a checkout flow, privilege escalation through a legitimate but misused workflow). The tell is turnaround time: a genuinely manual assessment of a moderately complex application takes a team of two testers 5 to 10 working days minimum; a report delivered in 48 hours for the same scope was not manually tested.

## Certifications That Actually Signal Competence

Individual tester certifications matter more than firm-level marketing claims. OSCP (Offensive Security Certified Professional) demonstrates hands-on exploitation capability through a genuinely difficult practical exam; OSCE and OSWE demonstrate advanced web and exploit-development skill. At the firm level, CREST accreditation (the UK/EU-recognized standard) requires the firm to demonstrate methodology, tester vetting, and quality assurance processes, not just individual certifications — it's a meaningfully higher bar than a firm simply listing certified individuals on a website. Ask specifically which certified tester will be assigned to your engagement, by name, not which certifications the firm holds in aggregate across staff who won't touch your project.

## Methodology: Automated Scanning Dressed Up as Manual Testing

Ask the vendor to describe their methodology against a named standard — OWASP Testing Guide or OWASP ASVS for web applications, PTES (Penetration Testing Execution Standard), or NIST SP 800-115 — and ask them to walk through what manual steps happen after the automated scanning phase completes. A real methodology includes manual verification of every automated finding to eliminate false positives, plus dedicated time for business-logic testing that has no automated equivalent: can a standard user access another tenant's data by manipulating an ID in a request, can a workflow be replayed or reordered to bypass a payment step. If a vendor's answer to "what do you do that a scanner doesn't" is vague, the engagement will be a scan with a report wrapper.

## What a Real Report Looks Like

Findings should include CVSS 3.1 or 4.0 scoring with the full vector string (not just a severity label), a clear proof-of-concept demonstrating actual exploitation — request/response pairs, screenshots of data accessed, not just "this endpoint appears vulnerable" — and remediation guidance specific enough for your engineers to act on without a follow-up call. A genuine report also documents what was tested and explicitly what was out of scope, and includes an executive summary that translates technical findings into business risk language your leadership can actually use. A report with only severity labels and generic remediation text copied from a vulnerability database is evidence of a template, not an assessment of your specific application.

## Retesting and the Remediation Verification Gap

A pentest that ends at report delivery leaves a critical gap: you have no independent confirmation that your fixes actually worked. Require retesting of critical and high findings as part of the engagement scope, not as a separately priced add-on negotiated after the fact, and require it to happen within a defined window (30-60 days is typical) after remediation. Ask what percentage of the firm's clients purchase retesting — a firm whose clients rarely retest is either doing perfect remediation guidance (unlikely) or its clients don't trust the retest is worth paying for, which tells you something about perceived value.

## Scoping: Why "We Test Everything" Is a Red Flag

A vendor who agrees to an unbounded scope without asking detailed questions about your architecture, authentication model, and specific areas of concern is not being accommodating — they're signaling they'll run the same generic playbook regardless of what you actually need tested. A rigorous vendor will push back on vague scoping, ask about your threat model, prior findings, and recent architecture changes, and propose a scope that concentrates tester time on your highest-risk surfaces rather than spreading thin, superficial coverage across everything.

## Making the Final Call

Price is a legitimate constraint, and a smaller firm or a scoped engagement is not automatically a checkbox provider — the signal to watch is whether the price reflects a defensible amount of manual tester time for your scope's complexity, not whether it's cheap in absolute terms. Weight certifications of the assigned individual tester, a named methodology with described manual steps beyond automation, and included retesting most heavily; a vendor confident in their work will not resist any of these being written explicitly into the statement of work.

Manifera works alongside specialized, CREST-affiliated penetration testing partners as part of a broader security testing program for client applications, ensuring assessments are scoped to actual architecture and risk rather than a generic checklist. If you're building out a security testing program alongside active development, our [custom software development](https://www.manifera.com/services/custom-software-development/) team can help structure testing into the delivery pipeline itself.

## Frequently Asked Questions

### How can I tell if a pentest vendor just ran an automated scan?

Turnaround time is the clearest tell — a genuinely manual assessment of a moderately complex application takes a team of two testers 5 to 10 working days minimum. A report delivered in 48 hours, findings that mirror common scanner output verbatim, and generic remediation text copied from a vulnerability database all indicate automated scanning dressed up as manual testing.

### What certifications should the individual tester on my engagement hold?

OSCP demonstrates hands-on exploitation capability through a hands-on practical exam; OSCE and OSWE indicate advanced web and exploit-development skill. Ask which certified tester will be assigned to your specific engagement by name, not which certifications exist somewhere across the firm's broader staff.

### What's the difference between CREST accreditation and individual certifications?

CREST accreditation is a firm-level standard requiring demonstrated methodology, tester vetting, and quality assurance processes across the organization, which is a meaningfully higher bar than a firm simply employing individuals who hold certifications like OSCP.

### Should retesting be included in a penetration testing engagement?

Yes, it should be scoped in upfront, not offered as a separately priced add-on after the report is delivered. Without retesting of critical and high findings within a defined window after remediation, you have no independent confirmation that your fixes actually closed the vulnerabilities.

### Is a vendor willing to test "everything" in an unbounded scope a good sign?

No, it's usually a red flag. A rigorous vendor pushes back on vague scoping and asks detailed questions about your architecture, authentication model, and threat model, then proposes a scope that concentrates tester time on your highest-risk surfaces rather than spreading thin coverage across everything.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {"@type": "Question", "name": "How can I tell if a pentest vendor just ran an automated scan?", "acceptedAnswer": {"@type": "Answer", "text": "Turnaround time is the clearest tell — a genuinely manual assessment of a moderately complex application takes a team of two testers 5 to 10 working days minimum. A report delivered in 48 hours, findings that mirror common scanner output verbatim, and generic remediation text copied from a vulnerability database all indicate automated scanning dressed up as manual testing."}},
    {"@type": "Question", "name": "What certifications should the individual tester on my engagement hold?", "acceptedAnswer": {"@type": "Answer", "text": "OSCP demonstrates hands-on exploitation capability through a hands-on practical exam; OSCE and OSWE indicate advanced web and exploit-development skill. Ask which certified tester will be assigned to your specific engagement by name, not which certifications exist somewhere across the firm's broader staff."}},
    {"@type": "Question", "name": "What's the difference between CREST accreditation and individual certifications?", "acceptedAnswer": {"@type": "Answer", "text": "CREST accreditation is a firm-level standard requiring demonstrated methodology, tester vetting, and quality assurance processes across the organization, which is a meaningfully higher bar than a firm simply employing individuals who hold certifications like OSCP."}},
    {"@type": "Question", "name": "Should retesting be included in a penetration testing engagement?", "acceptedAnswer": {"@type": "Answer", "text": "Yes, it should be scoped in upfront, not offered as a separately priced add-on after the report is delivered. Without retesting of critical and high findings within a defined window after remediation, you have no independent confirmation that your fixes actually closed the vulnerabilities."}},
    {"@type": "Question", "name": "Is a vendor willing to test \"everything\" in an unbounded scope a good sign?", "acceptedAnswer": {"@type": "Answer", "text": "No, it's usually a red flag. A rigorous vendor pushes back on vague scoping and asks detailed questions about your architecture, authentication model, and threat model, then proposes a scope that concentrates tester time on your highest-risk surfaces rather than spreading thin coverage across everything."}}
  ]
}
</script>
