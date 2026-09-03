---
title: "M&A Technical Due Diligence: Vendor Contracts That Survive an Acquisition"
keywords: "M&A technical due diligence, vendor contract assignability M&A, acquisition software vendor risk, technical due diligence checklist M&A, vendor contract change of control clause"
buyer_stage: "Decision"
target_persona: "CFO"
---

# M&A Technical Due Diligence: Vendor Contracts That Survive an Acquisition

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "M&A Technical Due Diligence: Vendor Contracts That Survive an Acquisition",
  "description": "A CFO's guide to technical due diligence on software vendor contracts during M&A, covering change-of-control clauses, assignment versus novation, key-person risk, and the vendor liabilities that surface after close if they aren't caught before.",
  "author": {"@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com/"},
  "publisher": {"@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com/"},
  "datePublished": "2026-09-03",
  "mainEntityOfPage": {"@type": "WebPage", "@id": "https://www.manifera.com/blog/m-and-a-technical-due-diligence-vendor-contracts-that-survive-an-acquisition"}
}
</script>

A buyer closes a $40M acquisition of a SaaS business, and in week two of integration discovers the target's core platform is built on a customer-facing product that a single outsourced development contractor — a two-person shop with no succession plan and a contract that requires the vendor's consent to assign — has exclusive knowledge of. The change-of-control clause in that vendor agreement gave the contractor the right to terminate on 30 days' notice once the acquisition closed, and they exercised it, unhappy with the new parent company's payment terms. The acquirer now has a platform nobody on staff can maintain, six months of institutional knowledge walking out the door, and a purchase price that didn't discount for any of this because nobody read the vendor contract's change-of-control clause during diligence. This is the specific, recurring failure mode that vendor-contract due diligence exists to catch — and it is caught reliably only when it's treated as its own diligence workstream, not folded into general IT due diligence as an afterthought.

For a CFO running or overseeing acquisition diligence, vendor contract risk sits in an uncomfortable gap: it's too technical for the legal team to fully evaluate alone, too contractual for the technical team to evaluate alone, and it rarely gets the dedicated attention that financial and commercial diligence receive by default. The result is that vendor contract risk is one of the most common sources of unpleasant post-close surprises in software-dependent acquisitions — and one of the most preventable, because the relevant contract language is sitting in the data room the entire time.

## Change-of-Control Clauses: The Single Most Consequential Line Item

The change-of-control clause is the provision that determines what happens to a vendor contract the moment ownership of the acquired company changes — and it varies enormously between "nothing, the contract continues unaffected" and "the vendor may terminate on notice, renegotiate pricing, or require consent before the contract survives the transaction." Every material vendor contract in the target's stack — development vendors, hosting and infrastructure providers, key SaaS tools embedded in the product, and any licensing agreements the product itself depends on — needs its change-of-control language reviewed individually, because there is no reliable default assumption; each vendor's standard paper handles this differently, and even within one vendor's contract portfolio, individually negotiated agreements often diverge from their own standard terms.

Flag any contract where change-of-control triggers a vendor's unilateral termination right, a pricing renegotiation right, or a consent requirement, and quantify the business impact if that right is exercised. A vendor contract covering a commodity tool with three viable alternatives is a minor flag. A vendor contract covering deeply embedded, hard-to-replace technical capability — as in the case above — is a material risk that should influence either the purchase price or the deal structure itself.

## Assignment vs Novation: A Distinction That Actually Matters

Buyers frequently assume a vendor contract simply "transfers" in an acquisition, but the legal mechanism matters. An asset purchase typically requires each material contract to be formally assigned or novated to the buying entity — assignment transfers the contract as-is (and many contracts require vendor consent for this), while novation replaces the original contract with a new one between the vendor and the buyer, extinguishing the original party's obligations. A stock/share purchase, by contrast, usually leaves the target entity's contracts untouched since the legal entity itself doesn't change — but the change-of-control clause discussed above can still trigger even in a share deal, since "control" of the entity has changed even though the entity itself remains the contracting party.

Confirm which contracts require active assignment or novation as part of closing mechanics, obtain vendor consent to assign well before close rather than discovering a consent requirement during integration, and build any vendor renegotiation risk into the closing timeline rather than treating it as a post-close cleanup item.

## Key-Person and Concentration Risk in Vendor Relationships

Beyond the contract language itself, technical due diligence should assess how concentrated the target's technical delivery is in a small number of people or a single vendor relationship — the scenario in the opening example. Ask directly: if this vendor relationship ended tomorrow, how long would it take to find, onboard, and bring a replacement to full productivity on this codebase, and what institutional knowledge would be irrecoverable in that transition? A target that depends on a single freelancer or small shop with no documentation, no source code escrow, and no transition provisions carries materially more integration risk than one built by a vendor with a documented codebase, standard handoff processes, and a broader bench.

This is also where verifying actual code and IP ownership matters — confirm the target genuinely owns the IP its vendors built, that work-for-hire or IP assignment language is present and enforceable in every development vendor contract, and that no vendor retains rights that could complicate the acquirer's ability to modify, resell, or relicense the software post-close.

## Source Code Escrow and Documentation as Risk Mitigants

For any vendor relationship flagged as high-concentration risk, check whether a source code escrow arrangement exists — a third-party-held copy of source code and build documentation, releasable to the buyer under defined trigger conditions (vendor insolvency, contract termination, sustained SLA failure) — and if one doesn't exist, factor the cost and negotiation effort of establishing one into the post-close integration plan. Escrow doesn't replace institutional knowledge, but it materially reduces the tail risk of a vendor relationship ending abruptly with no fallback.

Equally, assess the state of technical documentation independent of any single person's availability — architecture diagrams, deployment runbooks, and onboarding materials that would let a new team (whether in-house or a new vendor) become productive without depending on the outgoing vendor's cooperation during a transition that may be adversarial.

## Building Vendor Risk Into the Purchase Price and TSA

Where diligence surfaces genuine vendor concentration or contract risk, that risk should show up somewhere concrete — either as a purchase price adjustment, an escrow holdback tied to successful vendor transition, or specific representations and warranties in the purchase agreement that give the buyer recourse if a vendor risk that wasn't disclosed materializes post-close. For carve-out or complex integrations, a Transition Services Agreement (TSA) with the seller, covering continued vendor relationship support for a defined transition window, is a standard mechanism for buying time to build a durable replacement relationship rather than inheriting an abrupt vendor cutoff on day one.

Manifera frequently steps into exactly this kind of post-acquisition gap — see our [dedicated teams](https://www.manifera.com/services/custom-software-development/) model for how an acquirer can stand up durable, documented development capacity to replace a concentrated or at-risk vendor relationship without a hard cutover.

## Making the Final Call

Vendor contract risk in M&A is not a legal footnote — it's an operational and financial risk that belongs in the same diligence rigor as financial statement review, and it's one of the more tractable risks to catch because the evidence is contractual and sitting in the data room. A CFO running diligence should insist on individual change-of-control review for every material vendor contract, explicit confirmation of assignment or novation mechanics, and a concentration risk assessment of key vendor and personnel dependencies — before the purchase price is finalized, not after the first vendor exercises a termination right the diligence team never read.

## Frequently Asked Questions

### What is a change-of-control clause and why does it matter in M&A?
It's the contract provision defining what happens to a vendor agreement when ownership of the contracting company changes — it can allow the vendor to terminate, renegotiate pricing, or require consent, and terms vary significantly even across contracts from the same vendor. Every material vendor contract needs this clause reviewed individually during diligence, since there's no reliable default assumption about how it will behave.

### What's the difference between contract assignment and novation in an acquisition?
Assignment transfers an existing contract to the buyer as-is, often requiring the vendor's consent; novation replaces the original contract with a new one between the vendor and buyer, extinguishing the seller's obligations entirely. An asset purchase typically requires one of these mechanisms for material contracts, while a share purchase usually leaves the contracting entity's agreements untouched, though change-of-control clauses can still trigger.

### How should key-person or vendor concentration risk be evaluated in diligence?
Ask what would happen if a critical vendor relationship ended tomorrow — how long a replacement would take to reach full productivity, and how much institutional knowledge exists only outside any documentation or escrow arrangement. A target with a single, undocumented vendor relationship carries materially more integration risk than one with documented handoff processes and source code escrow in place.

### What is source code escrow and when should a buyer require it?
It's a third-party-held copy of source code and build documentation, releasable to the buyer under defined trigger conditions like vendor insolvency or contract termination. It should be required for any vendor relationship flagged as high concentration risk during diligence, particularly where a single small vendor or freelancer holds exclusive knowledge of a business-critical system.

### How should unresolved vendor risk affect the deal itself?
It should show up concretely — as a purchase price adjustment, an escrow holdback tied to successful vendor transition, specific representations and warranties giving recourse if undisclosed risk materializes, or a Transition Services Agreement giving the buyer time to build a replacement relationship. Vendor risk identified but left unaddressed in the purchase agreement structure is risk the buyer has simply chosen to absorb without compensation.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What is a change-of-control clause and why does it matter in M&A?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "It's the contract provision defining what happens to a vendor agreement when ownership of the contracting company changes — it can allow the vendor to terminate, renegotiate pricing, or require consent, and terms vary significantly even across contracts from the same vendor. Every material vendor contract needs this clause reviewed individually during diligence, since there's no reliable default assumption about how it will behave."
      }
    },
    {
      "@type": "Question",
      "name": "What's the difference between contract assignment and novation in an acquisition?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Assignment transfers an existing contract to the buyer as-is, often requiring the vendor's consent; novation replaces the original contract with a new one between the vendor and buyer, extinguishing the seller's obligations entirely. An asset purchase typically requires one of these mechanisms for material contracts, while a share purchase usually leaves the contracting entity's agreements untouched, though change-of-control clauses can still trigger."
      }
    },
    {
      "@type": "Question",
      "name": "How should key-person or vendor concentration risk be evaluated in diligence?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ask what would happen if a critical vendor relationship ended tomorrow — how long a replacement would take to reach full productivity, and how much institutional knowledge exists only outside any documentation or escrow arrangement. A target with a single, undocumented vendor relationship carries materially more integration risk than one with documented handoff processes and source code escrow in place."
      }
    },
    {
      "@type": "Question",
      "name": "What is source code escrow and when should a buyer require it?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "It's a third-party-held copy of source code and build documentation, releasable to the buyer under defined trigger conditions like vendor insolvency or contract termination. It should be required for any vendor relationship flagged as high concentration risk during diligence, particularly where a single small vendor or freelancer holds exclusive knowledge of a business-critical system."
      }
    },
    {
      "@type": "Question",
      "name": "How should unresolved vendor risk affect the deal itself?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "It should show up concretely — as a purchase price adjustment, an escrow holdback tied to successful vendor transition, specific representations and warranties giving recourse if undisclosed risk materializes, or a Transition Services Agreement giving the buyer time to build a replacement relationship. Vendor risk identified but left unaddressed in the purchase agreement structure is risk the buyer has simply chosen to absorb without compensation."
      }
    }
  ]
}
</script>
