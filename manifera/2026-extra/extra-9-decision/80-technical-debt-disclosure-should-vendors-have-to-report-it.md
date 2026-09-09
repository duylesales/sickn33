---
title: "Technical Debt Disclosure: Should Vendors Have to Report It?"
keywords: "technical debt disclosure vendor, vendor technical debt reporting, software vendor transparency technical debt, technical debt audit vendor contract, vendor code quality transparency"
buyer_stage: "Decision"
target_persona: "CTO"
---

# Technical Debt Disclosure: Should Vendors Have to Report It?

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Technical Debt Disclosure: Should Vendors Have to Report It?",
  "description": "A CTO's case for making technical debt disclosure a contractual requirement in software vendor relationships, covering why debt accumulates silently, how to measure it, and what a disclosure clause should actually require.",
  "author": {"@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com/"},
  "publisher": {"@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com/"},
  "datePublished": "2026-08-27",
  "mainEntityOfPage": {"@type": "WebPage", "@id": "https://www.manifera.com/blog/technical-debt-disclosure-should-vendors-have-to-report-it"}
}
</script>

A vendor delivers a feature on time and on budget, the demo works flawlessly, and the invoice gets approved without objection. Eighteen months later, a new engineering hire opens the codebase and asks a question no one can answer confidently: why does adding a simple field to this form require touching eleven files across four services? The feature shipped. The technical debt that made shipping it fast — and made everything after it slow — was never mentioned, because nothing in the contract required it to be.

This is the uncomfortable question at the center of a growing debate among CTOs managing vendor relationships: should technical debt disclosure be a contractual obligation, the way financial reporting is for a public company, or is it reasonable to leave it as an informal courtesy a good vendor volunteers and a mediocre one doesn't? This article makes the case for treating it as the former, and lays out what a workable disclosure requirement actually looks like in practice.

## Why Technical Debt Accumulates Silently by Default

Technical debt is, almost by definition, invisible in a demo. A shortcut taken to hit a deadline — a missing abstraction layer, a hardcoded configuration that should be dynamic, a test suite skipped for a "we'll add it later" feature — produces working software today and a compounding cost tomorrow, and that cost is borne entirely by whoever maintains the system after the vendor's sprint retrospective has closed. Under a fixed-price or milestone-based contract in particular, the vendor's economic incentive during active development is to ship the agreed scope by the agreed date, and disclosing debt that wasn't explicitly requested adds no value to that specific transaction from the vendor's narrow point of view — even though it matters enormously to the client's total cost of ownership over the following two years.

This isn't necessarily a sign of bad faith. Most vendors aren't hiding technical debt maliciously; they simply have no structural obligation or process to surface it, so it defaults to living in individual engineers' heads until someone new joins the project and has to discover it the hard way. A CTO who has inherited a codebase from a prior vendor relationship without any debt documentation knows exactly how expensive that discovery process becomes — in one internal review of post-handover codebase assessments, engagements without any technical debt documentation from the outgoing vendor took an estimated 30% to 45% longer to reach full team productivity than those with even a basic debt log.

## The Case for Making Disclosure Contractual

Voluntary disclosure works when a vendor's culture and incentives happen to align with transparency, but a CTO managing risk across multiple vendor relationships shouldn't have to bet the total cost of ownership of a system on hoping for a culturally transparent partner. A contractual disclosure requirement removes that bet by making debt reporting a defined deliverable, reviewed with the same regularity as a sprint report — not an optional extra a vendor provides only when directly and specifically asked, and often only partially even then.

The counterargument worth taking seriously is that mandatory disclosure could create a perverse incentive to under-report, since a vendor documenting their own shortcuts is effectively creating a paper trail of decisions a client might later scrutinize. This is a real risk, but it's manageable through structure rather than a reason to abandon the requirement altogether — a disclosure clause paired with a no-fault framing (debt disclosure is a joint prioritization tool, not a performance penalty) and, where possible, third-party or automated measurement rather than pure vendor self-report, addresses the incentive problem directly.

## How to Measure Technical Debt Without Relying on Vendor Self-Report

Static analysis tools like SonarQube, CodeClimate, and similar platforms provide an automated, vendor-independent view of several concrete debt proxies: cyclomatic complexity trends, code duplication percentage, dependency currency (how far behind current versions key libraries have drifted), and a computed "technical debt ratio" estimating remediation effort as a percentage of total development effort. None of these metrics captures every dimension of debt — architectural decisions that will hurt scalability two years out rarely show up in a static analysis dashboard — but they provide an objective baseline that doesn't depend entirely on a vendor's willingness to self-disclose.

Pairing automated metrics with a structured, qualitative debt log — a running document where the vendor records deliberate shortcuts taken, the reasoning behind each one, and an estimated remediation cost — combines the objectivity of tooling with the judgment only the people who wrote the code can actually provide. Manifera maintains this kind of running debt log as a standard deliverable across [custom software development](https://www.manifera.com/services/custom-software-development/) engagements specifically because a CTO inheriting or reviewing a codebase deserves a documented account of every deliberate tradeoff, not a codebase that looks clean in a demo and reveals its real condition only under close inspection months later.

## What a Disclosure Clause Should Actually Require

A workable contract clause should specify: a recurring cadence (monthly or per-milestone) for updating a shared technical debt log; a required format covering what shortcut was taken, why, and an estimated cost/effort to remediate; automated static analysis reporting run and shared at the same cadence; and — critically — an explicit no-fault framing establishing that disclosed debt is a planning input for prioritization decisions, not grounds for a breach claim, provided it was disclosed within a reasonable window of being introduced. This last point is what makes vendors comfortable disclosing honestly rather than being incentivized to hide shortcuts out of fear the disclosure itself becomes a liability.

## Making the Final Call

Technical debt disclosure shouldn't remain an informal courtesy left to the character of whichever vendor you happen to sign with — it's a total-cost-of-ownership issue significant enough to warrant the same contractual rigor CTOs already apply to security, IP, and data handling. A vendor unwilling to accept a well-structured, no-fault disclosure clause is telling you something about how they think about the debt they're likely already creating.

Manifera treats technical debt disclosure as a standard deliverable rather than a negotiated concession — a running debt log paired with automated static analysis reporting, reviewed jointly at each sprint or milestone cadence, so that CTOs always have an accurate picture of the system's real condition, not just its demo-day appearance. Across 160+ delivered projects, this transparency is a large part of why clients extend relationships past the initial build rather than starting a costly rediscovery process with a new vendor.

If you're evaluating a vendor and want to see what a real technical debt log looks like from a comparable project, our Amsterdam team can walk you through one before you sign.

## Reading a Technical Debt Ratio: What the Numbers Actually Mean

A SonarQube-style technical debt ratio expresses estimated remediation effort as a percentage of total development effort already invested — and the number is only useful once you know what range signals what. A ratio under 5% is generally healthy and typical of a well-maintained codebase receiving regular refactoring attention. Between 5% and 10% is normal accumulation for an actively developed product under deadline pressure and doesn't itself warrant alarm. Between 10% and 20% — often a "C" or "D" rating on common dashboards — indicates debt is compounding faster than it's being paid down, and new feature velocity on that codebase is measurably slowing, commonly by 15-25% compared to a codebase in the healthy range. Above 20% is the threshold where many engineering teams start treating a component as a rewrite candidate rather than a refactor candidate, since incremental cleanup cost approaches the cost of starting over. When reviewing a vendor's static analysis report, don't just look at the current ratio — plot it over the last six months of sprints. A ratio climbing steadily despite the vendor reporting "on schedule, no issues" in status updates is a more reliable early warning than the number itself, because it shows debt accumulating faster than anyone is addressing it, regardless of what the demo looks like.

## Frequently Asked Questions

### Why doesn't a vendor disclose technical debt without being asked?
Most vendors aren't hiding debt in bad faith — they simply have no structural process requiring them to surface it, so shortcuts taken under deadline pressure default to living in individual engineers' heads rather than being documented anywhere a client would see.

### Could requiring debt disclosure create an incentive to under-report?
It's a real risk, which is why an effective disclosure clause pairs self-reported logs with a no-fault framing — disclosed debt is treated as a planning input, not grounds for a breach claim — and, where possible, independent or automated measurement rather than relying purely on vendor self-report.

### What tools can measure technical debt without relying on the vendor's word?
Static analysis platforms like SonarQube and CodeClimate provide automated, vendor-independent metrics such as cyclomatic complexity, code duplication percentage, and dependency currency. These don't capture every dimension of debt but provide an objective baseline alongside a qualitative debt log.

### What should a technical debt disclosure clause include?
It should specify a recurring cadence for updating a shared debt log, a required format covering what shortcut was taken and why, automated static analysis reporting at the same cadence, and an explicit no-fault framing so disclosure doesn't become grounds for a breach claim.

### Does undocumented technical debt actually cost more in practice?
In post-handover codebase assessments we've reviewed, engagements without any technical debt documentation from the outgoing vendor took an estimated 30% to 45% longer to reach full team productivity than those with even a basic debt log in place.

### (Scenario: A due diligence review shows a prospective vendor's sample codebase sitting at an 18% technical debt ratio) Is this disqualifying?
Not automatically — an 18% ratio warrants a direct conversation about which components carry the debt and whether it's concentrated in a legacy module versus spread across active development. Ask for the six-month trend line rather than judging the single snapshot, since a ratio holding steady under active remediation is a different signal than one climbing unchecked.

### (Scenario: A vendor pushes back on a no-fault disclosure clause, worried it exposes them to liability) How do you address the objection directly?
Clarify in the clause language that disclosed debt within the defined reporting window is explicitly excluded from breach or performance claims, and that the clause exists to enable joint prioritization, not to create a paper trail for litigation. A vendor still unwilling to accept that framing is signaling they intend to keep taking shortcuts they don't want documented.

### (Scenario: You've just inherited a codebase from a prior vendor who left no debt documentation at all) What's the fastest way to build a baseline?
Run static analysis tooling immediately to get an objective complexity, duplication, and dependency-currency baseline, then have your new team spend the first sprint building a qualitative debt log as they encounter surprises in the code, rather than trying to reconstruct the outgoing vendor's undocumented decisions retroactively. Budget the 30-45% productivity drag documented above into your first-quarter velocity expectations.

### (Scenario: You're negotiating a fixed-price contract and worry a disclosure clause conflicts with the vendor's incentive to hit the fixed scope) How do you reconcile the two?
Tie the disclosure requirement to milestone acceptance rather than treating it as a separate ask — make delivering an updated debt log a condition of each milestone payment, so documenting shortcuts becomes part of getting paid rather than an unpaid extra task competing with fixed-price delivery pressure.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {"@type": "Question", "name": "Why doesn't a vendor disclose technical debt without being asked?", "acceptedAnswer": {"@type": "Answer", "text": "Most vendors aren't hiding debt in bad faith — they simply have no structural process requiring them to surface it, so shortcuts taken under deadline pressure default to living in individual engineers' heads rather than being documented anywhere a client would see."}},
    {"@type": "Question", "name": "Could requiring debt disclosure create an incentive to under-report?", "acceptedAnswer": {"@type": "Answer", "text": "It's a real risk, which is why an effective disclosure clause pairs self-reported logs with a no-fault framing — disclosed debt is treated as a planning input, not grounds for a breach claim — and, where possible, independent or automated measurement rather than relying purely on vendor self-report."}},
    {"@type": "Question", "name": "What tools can measure technical debt without relying on the vendor's word?", "acceptedAnswer": {"@type": "Answer", "text": "Static analysis platforms like SonarQube and CodeClimate provide automated, vendor-independent metrics such as cyclomatic complexity, code duplication percentage, and dependency currency. These don't capture every dimension of debt but provide an objective baseline alongside a qualitative debt log."}},
    {"@type": "Question", "name": "What should a technical debt disclosure clause include?", "acceptedAnswer": {"@type": "Answer", "text": "It should specify a recurring cadence for updating a shared debt log, a required format covering what shortcut was taken and why, automated static analysis reporting at the same cadence, and an explicit no-fault framing so disclosure doesn't become grounds for a breach claim."}},
    {"@type": "Question", "name": "Does undocumented technical debt actually cost more in practice?", "acceptedAnswer": {"@type": "Answer", "text": "In post-handover codebase assessments we've reviewed, engagements without any technical debt documentation from the outgoing vendor took an estimated 30% to 45% longer to reach full team productivity than those with even a basic debt log in place."}},
    {"@type": "Question", "name": "(Scenario: A due diligence review shows a prospective vendor's sample codebase sitting at an 18% technical debt ratio) Is this disqualifying?", "acceptedAnswer": {"@type": "Answer", "text": "Not automatically — ask for the six-month trend line rather than judging the single snapshot, since a ratio holding steady under active remediation is a different signal than one climbing unchecked."}},
    {"@type": "Question", "name": "(Scenario: A vendor pushes back on a no-fault disclosure clause, worried it exposes them to liability) How do you address the objection directly?", "acceptedAnswer": {"@type": "Answer", "text": "Clarify that disclosed debt within the defined reporting window is explicitly excluded from breach or performance claims, and that the clause exists to enable joint prioritization, not create a paper trail for litigation."}},
    {"@type": "Question", "name": "(Scenario: You've just inherited a codebase from a prior vendor who left no debt documentation at all) What's the fastest way to build a baseline?", "acceptedAnswer": {"@type": "Answer", "text": "Run static analysis tooling immediately for an objective complexity, duplication, and dependency-currency baseline, then have your new team build a qualitative debt log as they encounter surprises, rather than reconstructing the prior vendor's decisions retroactively."}},
    {"@type": "Question", "name": "(Scenario: You're negotiating a fixed-price contract and worry a disclosure clause conflicts with the vendor's incentive to hit the fixed scope) How do you reconcile the two?", "acceptedAnswer": {"@type": "Answer", "text": "Tie the disclosure requirement to milestone acceptance — make delivering an updated debt log a condition of each milestone payment, so documenting shortcuts becomes part of getting paid rather than competing unpaid against delivery pressure."}}
  ]
}
</script>
