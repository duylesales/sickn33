---
title: "Wealth Management Software Vendors: Custody Integration Due Diligence"
keywords: "wealth management software vendor, custody integration software, portfolio management platform vendor, wealthtech vendor due diligence, wealth management platform selection"
buyer_stage: "Decision"
target_persona: "Compliance Officer"
---

# Wealth Management Software Vendors: Custody Integration Due Diligence

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Wealth Management Software Vendors: Custody Integration Due Diligence",
  "description": "A compliance officer's due diligence framework for wealth management software vendors, focused on custodian integration mechanics, reconciliation accuracy, SOC 2 reporting, and the fiduciary data segregation questions that determine real operational risk.",
  "author": {"@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com/"},
  "publisher": {"@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com/"},
  "datePublished": "2026-09-12",
  "mainEntityOfPage": {"@type": "WebPage", "@id": "https://www.manifera.com/blog/wealth-management-software-vendors-custody-integration-due-diligence"}
}
</script>

A client's portfolio value shown in your wealth management platform disagrees with their custodian's own statement by a few hundred euros. It happens on a Tuesday, nobody notices for three weeks, and by the time it surfaces, an advisor has already made a rebalancing recommendation based on the wrong number. This is the failure mode that custody integration due diligence exists to prevent, and it is almost never caused by a dramatic system outage — it is caused by a reconciliation process that quietly tolerates small discrepancies until they compound into a client-facing problem. For a compliance officer evaluating wealth management software vendors, the custodian integration layer deserves more scrutiny than the client-facing dashboard, because that is where the actual fiduciary risk lives.

## Understand the Custody Integration Pattern the Vendor Actually Uses

Wealth management platforms connect to custodians — firms like Pershing, Fidelity's National Financial Services, State Street, or a European equivalent depending on jurisdiction — through varying integration patterns, and the pattern matters enormously to data accuracy and timeliness. Some platforms rely on daily batch file feeds (often still in legacy fixed-width or delimited file formats inherited from decades-old custodian infrastructure), others use SWIFT messaging standards (the MT54x series of messages for securities settlement and corporate actions), and increasingly, modern custodians offer REST APIs for more real-time position and transaction data.

Ask the vendor precisely which integration pattern is used for each custodian you work with, since a platform can genuinely have real-time API access to one custodian while relying on overnight batch files for another — a detail that materially affects how current the data an advisor is looking at actually is at any given moment. A vendor that describes their custody integration only in generic terms ("we integrate with major custodians") without being able to name the specific mechanism per custodian has not demonstrated the operational depth this due diligence requires.

## Reconciliation Tolerance and Escalation Is the Real Risk Control

Every custody integration will occasionally disagree with the custodian's own system of record, whether from timing differences (a trade settling but not yet reflected in one system), corporate action processing lags, or genuine data errors. What separates a well-run platform from a risky one is not whether discrepancies occur — they always will — but how the platform detects, tolerates, and escalates them. Ask specifically: what discrepancy threshold triggers an automatic flag, how quickly are flagged discrepancies reviewed by a human, and is there a hard block preventing an advisor from acting on unreconciled data (placing a trade, generating a client report) until the discrepancy is resolved or explicitly overridden with documented justification?

A platform that reconciles nightly but allows advisor-facing screens to display unreconciled data throughout the day without any visual indicator is accepting a real risk that a compliance officer should not accept on the firm's behalf without at least understanding it clearly. Request the vendor's actual historical reconciliation exception rate and average time-to-resolution from an existing client reference, not just a description of the process in the abstract.

## SOC 2 Type II Reports Tell You About Controls, Not Just Security

Wealth management software vendors handling custody-linked data should be able to produce a current SOC 2 Type II report — an independent auditor's assessment of the vendor's controls over a period of time (typically six to twelve months), covering security, availability, processing integrity, confidentiality, and privacy trust principles, as opposed to a SOC 2 Type I report, which only assesses controls at a single point in time and says much less about whether they actually operate reliably over an extended period.

Read the report itself, not just the auditor's summary opinion — the "processing integrity" section is particularly relevant to custody integration, since it covers whether the vendor's data processing (including reconciliation logic) actually produces complete, accurate, and timely results as designed. Pay close attention to any noted exceptions or qualified opinions in the report; a vendor who shares only the summary letter and resists sharing the full report with named exceptions is not giving you what you need to make an informed fiduciary decision on behalf of your firm's clients.

## Fiduciary Data Segregation Across Multi-Custodian, Multi-Advisor Environments

Wealth management platforms increasingly serve multi-custodian environments — a single client's assets held across several custodians, sometimes including "held-away" accounts aggregated through third-party connections like Plaid or Akoya for accounts the firm does not directly custody. This creates a segregation requirement: client data, particularly held-away account credentials and aggregated data, needs to be logically and often physically segregated with access controls that respect which advisors and staff are actually authorized to view which client's complete financial picture.

Ask specifically how the platform handles access control for held-away account data versus custodied account data, whether aggregation credentials are stored using bank-grade encryption and tokenization rather than plaintext credential storage (a genuine and recurring finding in less mature wealthtech platforms), and whether the audit log distinguishes between an advisor viewing data within their authorized book of clients versus an anomalous cross-book access that should trigger internal review.

## Trade Instruction and Settlement Confirmation Integrity

Where the platform supports trade instruction generation — order proposals an advisor approves and routes to the custodian for execution — the integration needs a closed-loop confirmation process: the platform should receive and reconcile actual execution confirmations from the custodian, not merely assume the instruction was executed as sent. A platform that shows a trade as "completed" based solely on successful transmission of the instruction, without waiting for a genuine execution confirmation from the custodian, can display materially incorrect portfolio positions to both advisors and clients in the window between instruction and actual settlement.

With the shift to T+1 settlement now standard for most US equity and corporate bond trades, and similar compression trends across European markets, this confirmation loop has less room for error than it did under longer settlement cycles — a platform's reconciliation and confirmation processes need to keep pace with a shorter window, not just historically adequate batch timing. Ask the vendor directly how their platform's confirmation loop has adapted to T+1, and request specifics rather than a general assurance of readiness.

## Custodian Relationship Portability and Vendor Lock-In

A final due diligence item that compliance officers sometimes leave to procurement alone: how easily can your firm move to a different wealth management platform later while keeping the same custodian relationships, and conversely, how easily can you change custodians while keeping the same platform? Platforms with deep, proprietary custodian-specific integrations can create switching costs on both dimensions. Ask for a documented account of a client who has changed custodians while remaining on the platform, and what that transition actually involved technically and operationally — the honesty and specificity of that answer tells you a great deal about how the vendor thinks about this risk. Where a platform's own integration flexibility falls short of what your firm's multi-custodian strategy requires, purpose-built [custom software development](https://www.manifera.com/services/custom-software-development/) work to extend or bridge that integration layer is often more cost-effective than a full platform migration.

## Making the Custody Call

The client-facing dashboard is the least revealing part of a wealth management platform evaluation. What determines whether the platform is trustworthy as a fiduciary tool is the integration pattern behind each custodian connection, the discipline of the reconciliation and escalation process, the depth of the SOC 2 Type II report behind the summary letter, and how cleanly the platform segregates data across a multi-custodian, multi-advisor environment. A compliance officer who pushes past the demo to these specifics is doing the actual job this decision requires.

Manifera has supported wealth and asset management firms building the reconciliation and custody integration layers that sit underneath advisor-facing platforms, where accuracy and audit trail integrity were non-negotiable design constraints from day one. If your firm needs an independent technical review of a prospective vendor's custody integration architecture, our [about us](https://www.manifera.com/about-us/) page and [contact page](https://www.manifera.com/contact-us/) are good starting points to bring our engineering team into that evaluation before a contract is signed.

## Frequently Asked Questions

### What is the difference between batch file, SWIFT, and API custody integration?
Batch file integration relies on periodic file transfers, often overnight, and introduces data latency. SWIFT MT54x messaging is a longstanding standard for securities settlement and corporate actions. REST APIs, offered by more modern custodians, allow near-real-time position and transaction data. A platform's actual data currency depends on which pattern is used for each specific custodian relationship.

### Why does reconciliation tolerance matter more than whether discrepancies occur at all?
Discrepancies between a platform and a custodian's system of record are a normal, recurring feature of custody integration due to timing differences and corporate action processing. What matters is whether the platform detects, flags, and blocks action on unreconciled data appropriately, rather than allowing advisors to act on unverified figures.

### What should we look for in a vendor's SOC 2 Type II report specifically?
Request the full report, not just the summary opinion, and review the processing integrity section closely, since it addresses whether the vendor's reconciliation logic actually produces complete and accurate results over the audit period. Pay particular attention to any noted exceptions or qualified opinions.

### How has T+1 settlement changed custody integration due diligence?
Shorter settlement cycles compress the window in which a platform must receive and reconcile genuine execution confirmations from the custodian rather than assuming a trade instruction was executed as sent. Ask vendors specifically how their confirmation loop has adapted to T+1 rather than accepting a general readiness assurance.

### How should held-away account data be handled differently from custodied account data?
Held-away accounts, aggregated through services like Plaid or Akoya, should have aggregation credentials stored with bank-grade encryption and tokenization rather than plaintext, and access should be logically segregated with audit logging that distinguishes normal advisor access from anomalous cross-book access.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What is the difference between batch file, SWIFT, and API custody integration?",
      "acceptedAnswer": {"@type": "Answer", "text": "Batch file integration relies on periodic file transfers, often overnight, and introduces data latency. SWIFT MT54x messaging is a longstanding standard for securities settlement and corporate actions. REST APIs, offered by more modern custodians, allow near-real-time position and transaction data. A platform's actual data currency depends on which pattern is used for each specific custodian relationship."}
    },
    {
      "@type": "Question",
      "name": "Why does reconciliation tolerance matter more than whether discrepancies occur at all?",
      "acceptedAnswer": {"@type": "Answer", "text": "Discrepancies between a platform and a custodian's system of record are a normal, recurring feature of custody integration due to timing differences and corporate action processing. What matters is whether the platform detects, flags, and blocks action on unreconciled data appropriately, rather than allowing advisors to act on unverified figures."}
    },
    {
      "@type": "Question",
      "name": "What should we look for in a vendor's SOC 2 Type II report specifically?",
      "acceptedAnswer": {"@type": "Answer", "text": "Request the full report, not just the summary opinion, and review the processing integrity section closely, since it addresses whether the vendor's reconciliation logic actually produces complete and accurate results over the audit period. Pay particular attention to any noted exceptions or qualified opinions."}
    },
    {
      "@type": "Question",
      "name": "How has T+1 settlement changed custody integration due diligence?",
      "acceptedAnswer": {"@type": "Answer", "text": "Shorter settlement cycles compress the window in which a platform must receive and reconcile genuine execution confirmations from the custodian rather than assuming a trade instruction was executed as sent. Ask vendors specifically how their confirmation loop has adapted to T+1 rather than accepting a general readiness assurance."}
    },
    {
      "@type": "Question",
      "name": "How should held-away account data be handled differently from custodied account data?",
      "acceptedAnswer": {"@type": "Answer", "text": "Held-away accounts, aggregated through services like Plaid or Akoya, should have aggregation credentials stored with bank-grade encryption and tokenization rather than plaintext, and access should be logically segregated with audit logging that distinguishes normal advisor access from anomalous cross-book access."}
    }
  ]
}
</script>
