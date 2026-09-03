---
title: "Product Design Vendor Contracts: IP and Iteration Clauses to Verify"
keywords: "design vendor contract, IP ownership work for hire, design iteration clauses, Netherlands vendor contract, scope creep protection"
buyer_stage: "Decision"
target_persona: "Founder"
---

# Product Design Vendor Contracts: IP and Iteration Clauses to Verify

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Product Design Vendor Contracts: IP and Iteration Clauses to Verify",
  "description": "A founder's checklist for the IP ownership, iteration, scope, and exit clauses in a product design vendor contract, including how Dutch and EU contract norms differ from US vendor expectations.",
  "author": {"@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com/"},
  "publisher": {"@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com/"},
  "datePublished": "2026-08-18",
  "mainEntityOfPage": {"@type": "WebPage", "@id": "https://www.manifera.com/blog/product-design-vendor-contracts-ip-and-iteration-clauses-to-verify"}
}
</script>

You paid a design agency €40,000 for your product's design system. Eighteen months later, you want to switch development vendors, and the new team asks for the Figma source files and the component library. The agency's contract says you own "the deliverables" — which, on closer reading, means the exported PNGs and PDFs they sent you, not the editable source files, not the design tokens, and not a license to keep using their proprietary component framework. You own the picture of your product, not the product's design system.

This is not a rare contract dispute — it's the default outcome of the vendor-drafted templates most design agencies send founders, because those templates are optimized for the agency's downstream business, not for the founder's ability to walk away cleanly. Founders read design contracts for price and timeline and skim the legal boilerplate, on the reasonable assumption that "we hired them, so we own what they made." That assumption is wrong often enough that it deserves specific, deliberate verification before signature, not after a dispute.

The clauses that matter here are not exotic — they're standard contract mechanics that get glossed over because design engagements feel more collaborative and less adversarial than, say, a construction contract. That feeling is exactly why founders under-scrutinize them.

## IP Ownership: Work-for-Hire vs. Licensed Use

The single most consequential clause in a design vendor contract is the IP assignment language, and it comes in two structurally different forms that founders routinely conflate. A true work-for-hire (or, in most EU jurisdictions where the US "work for hire" doctrine doesn't directly apply, an explicit IP assignment clause) transfers full ownership of the created work to the client upon payment, meaning the client can modify, resell, relicense, or hand the files to a different vendor without restriction. A licensed-use clause instead grants the client a right to use the deliverables — often "for the purposes of operating the product" — while the vendor retains underlying ownership, which limits what the client can do with the work later, including handing it to a competing vendor for extension.

The practical test: search the contract for the word "assign" (or, in Dutch/EU contracts, "overdracht" of intellectual property rights) applied to the finished work, not just "license" or "grant the right to use." If the contract only grants a license, ask explicitly whether that license is exclusive, perpetual, and irrevocable — a non-exclusive or revocable license on your own product's design system is a serious liability, because it means the vendor could theoretically license the same design system elsewhere, or the license could lapse under conditions buried in a termination clause.

## Who Owns the Figma Files, Design Tokens, and Component Library

IP assignment language often talks about "the deliverables" without defining what that term includes, and this is where founders get burned. A contract should explicitly list: the editable Figma (or equivalent) source files, not just exported images or a shared view-only link; the design tokens (color, spacing, typography values) as a standalone asset, since these increasingly live in code or a separate token-management tool and get overlooked as "just design files"; and the component library itself, including any custom components, variants, and interaction specs built specifically for your product.

A common and reasonable vendor carve-out is their own proprietary tooling or a generic component framework they reuse across clients — that's fair to exclude from assignment, since it isn't specific to your product. What's not reasonable is a contract silent on whether you get editable source files at all, defaulting to view-only Figma access that vanishes when the vendor relationship ends. Ask explicitly, before signing, what file formats and access rights you'll have on day one after final payment — not "we'll figure that out at offboarding," which is the point at which you have the least leverage to negotiate.

## Iteration Clauses: What Counts as a "Round"

Iteration disputes are the most common source of mid-project friction, and they're avoidable with a precisely worded clause. A vague contract that promises "revisions included" without defining a round invites disagreement the moment feedback gets granular — is a founder's ten separate comments on one screen one round or ten? A well-drafted clause defines a round explicitly: typically, one consolidated set of feedback per deliverable, submitted within a defined window (commonly 5-10 business days after delivery), with a stated number of included rounds per phase (2-3 rounds is standard for a design phase) before additional rounds bill at a stated hourly or day rate.

The other detail worth verifying is what counts as a revision versus a new request. Refining an existing screen based on feedback is a revision; asking for an entirely new screen or a materially different direction is scope expansion, and a contract that doesn't distinguish the two lets a vendor bill "revision" work as extra while the client experiences it as reasonable feedback on work already commissioned. Ask the vendor to walk through, concretely, an example of what would trigger extra billing under their definition — their answer reveals whether the clause is genuinely fair or written to maximize change-order revenue.

## Scope Creep Protection and Kill Clauses

Scope creep protection works in the founder's favor when the contract defines the deliverables specifically enough that "in scope" and "out of scope" aren't matters of interpretation — named screens or flows, a stated number of breakpoints, a defined platform list (web only, or web plus native mobile), rather than open language like "a modern, responsive design for the product." Change requests outside that defined scope should trigger a written change order with its own price and timeline impact before work starts, not get absorbed silently and then surface as a late invoice or a blown deadline.

A kill clause (termination for convenience) protects the founder's exit, and it deserves as much attention as the IP clause, because it determines what you're left holding if the engagement isn't working. Look for: a reasonable notice period (30 days is typical, not 90), a clear statement that IP assignment for work already paid for survives termination regardless of the reason for exit, and a defined handoff obligation — the vendor delivering current-state files and documentation within a set window after termination, rather than "as agreed." A contract with no termination-for-convenience clause at all, only termination for cause, effectively locks you into the relationship even if it's failing to deliver, since proving "cause" in a vague creative engagement is genuinely difficult.

## Deliverable Format Ownership

Format ownership is the detail that turns "we own the design" into something practically usable. A contract should specify not just that you own the deliverables, but in what format you receive them: native editable files (Figma project files with edit access transferred, not duplicated into a read-only export), any custom code for a design system if one was built (React/Vue component code, not just visual specs), and documentation sufficient for a different vendor to pick up the work — a style guide, component usage notes, and naming conventions, not tribal knowledge that only exists in the original team's heads.

This matters most at vendor transition, which is precisely when founders discover gaps. If the contract doesn't require documentation as a deliverable, you likely won't get any, because documentation takes real time to produce and vendors won't volunteer unbilled hours for it. Make documentation and full source file transfer an explicit, named deliverable with its own line in the contract, not an assumption folded into "final handoff."

## Dutch/EU Contract Norms vs. US Vendor Expectations

Founders who've previously worked with US-based vendors often carry assumptions that don't map cleanly onto Dutch and EU contract norms. Work-for-hire as a specific legal doctrine, automatically vesting IP in the commissioning party, exists in US copyright law but has no direct equivalent under Dutch or most EU copyright frameworks — under Dutch law (Auteurswet), the creator generally retains moral rights regardless of contract terms, and economic rights transfer to the client only through an explicit written assignment clause, never by default or by implication from payment alone. This makes explicit IP assignment language non-negotiable in a Dutch or EU vendor contract in a way US founders may not think to double-check, because their prior experience assumed transfer was automatic.

Dutch commercial contracts also tend toward more moderate liability caps and more balanced termination terms than the aggressive, vendor-favorable boilerplate common in some US agency contracts, reflecting both civil law tradition and Dutch business norms around proportionality. Payment terms customarily follow standard EU B2B norms (30-day payment terms are common and, under EU late payment directives, carry statutory interest for late payment) rather than the shorter net-15 terms common in some US agency relationships. None of this means Dutch/EU contracts are automatically friendlier to founders by default — it means the specific protections differ, and a founder assuming US contract conventions apply by default will miss where explicit language is actually required under Dutch law, particularly around IP assignment.

## Making the Final Call

None of these clauses require a specialized IP lawyer to catch on a first read — they require reading the contract with the specific question "what happens if I need to leave this vendor in a year" rather than only "what am I paying and when do I get it." The clauses worth insisting on before signature are explicit IP assignment (not license) covering source files and design tokens by name, a precisely defined iteration round, a scope definition specific enough to make change orders unambiguous, and a termination-for-convenience clause with a real handoff obligation. A vendor who resists making these specific is telling you something about how the relationship will go if it ever gets difficult.

Manifera's engagement contracts assign full IP ownership of source files, design tokens, and component libraries to the client on final payment, with iteration rounds and scope defined in writing before work begins — the same standard we'd want if we were the founder signing. If you're reviewing a vendor contract and want a second read on what's actually being assigned versus licensed, our [our way of working](https://www.manifera.com/about-us/our-way-of-working/) page walks through how we structure engagements, or you can [get in touch](https://www.manifera.com/contact-us/) directly.

## Frequently Asked Questions

### Does "work for hire" automatically apply to a design vendor contract in the EU?
No. The US work-for-hire doctrine has no direct equivalent under Dutch or most EU copyright law. Under the Dutch Auteurswet and comparable EU frameworks, economic rights transfer to the client only through an explicit written IP assignment clause, and moral rights generally remain with the creator regardless of contract terms. Founders working with EU-based vendors need explicit assignment language, not an assumption that payment alone transfers ownership.

### What's the difference between owning "the deliverables" and owning the source files?
Owning "the deliverables" as vaguely defined often means only the exported images or PDFs a vendor sends, not the editable source files behind them. A contract needs to explicitly name editable Figma (or equivalent) source files, design tokens, and component library code as owned assets, or a founder may end up with unusable static exports instead of a working design system.

### How many rounds of revisions should be included in a design contract?
Two to three rounds per phase is standard, but the number matters less than the definition of what counts as one round — typically one consolidated set of feedback per deliverable submitted within a defined window. Without that definition, disputes arise over whether granular, ongoing feedback counts as one round or many.

### What should a kill clause in a design vendor contract include?
A reasonable notice period (commonly 30 days), explicit confirmation that IP assignment for already-paid work survives termination regardless of cause, and a defined handoff obligation requiring current-state files and documentation within a set window. A contract with only termination-for-cause, and no termination-for-convenience option, can lock a founder into an underperforming vendor relationship.

### How do Dutch contract norms differ from what a founder might expect from a US vendor agreement?
Dutch and EU commercial contracts tend toward more balanced liability caps and termination terms than aggressive US agency boilerplate, but require more explicit language around IP assignment, since transfer is never automatic under Dutch copyright law the way US work-for-hire can be. Payment terms also typically follow 30-day EU B2B norms rather than shorter US net-15 conventions.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {"@type": "Question", "name": "Does \"work for hire\" automatically apply to a design vendor contract in the EU?", "acceptedAnswer": {"@type": "Answer", "text": "No. The US work-for-hire doctrine has no direct equivalent under Dutch or most EU copyright law. Under the Dutch Auteurswet and comparable EU frameworks, economic rights transfer to the client only through an explicit written IP assignment clause, and moral rights generally remain with the creator regardless of contract terms. Founders working with EU-based vendors need explicit assignment language, not an assumption that payment alone transfers ownership."}},
    {"@type": "Question", "name": "What's the difference between owning \"the deliverables\" and owning the source files?", "acceptedAnswer": {"@type": "Answer", "text": "Owning \"the deliverables\" as vaguely defined often means only the exported images or PDFs a vendor sends, not the editable source files behind them. A contract needs to explicitly name editable Figma (or equivalent) source files, design tokens, and component library code as owned assets, or a founder may end up with unusable static exports instead of a working design system."}},
    {"@type": "Question", "name": "How many rounds of revisions should be included in a design contract?", "acceptedAnswer": {"@type": "Answer", "text": "Two to three rounds per phase is standard, but the number matters less than the definition of what counts as one round — typically one consolidated set of feedback per deliverable submitted within a defined window. Without that definition, disputes arise over whether granular, ongoing feedback counts as one round or many."}},
    {"@type": "Question", "name": "What should a kill clause in a design vendor contract include?", "acceptedAnswer": {"@type": "Answer", "text": "A reasonable notice period (commonly 30 days), explicit confirmation that IP assignment for already-paid work survives termination regardless of cause, and a defined handoff obligation requiring current-state files and documentation within a set window. A contract with only termination-for-cause, and no termination-for-convenience option, can lock a founder into an underperforming vendor relationship."}},
    {"@type": "Question", "name": "How do Dutch contract norms differ from what a founder might expect from a US vendor agreement?", "acceptedAnswer": {"@type": "Answer", "text": "Dutch and EU commercial contracts tend toward more balanced liability caps and termination terms than aggressive US agency boilerplate, but require more explicit language around IP assignment, since transfer is never automatic under Dutch copyright law the way US work-for-hire can be. Payment terms also typically follow 30-day EU B2B norms rather than shorter US net-15 conventions."}}
  ]
}
</script>
