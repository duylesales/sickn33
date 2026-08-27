---
title: "IP Ownership Clauses Founders Miss When Signing With a Dev Vendor"
keywords: "IP ownership clause software contract, founder IP rights vendor, intellectual property software development contract, work for hire clause vendor, IP assignment software vendor"
buyer_stage: "Decision"
target_persona: "Founder"
---

# IP Ownership Clauses Founders Miss When Signing With a Dev Vendor

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "IP Ownership Clauses Founders Miss When Signing With a Dev Vendor",
  "description": "A founder's guide to the intellectual property clauses most often overlooked when signing a software development vendor contract, covering work-for-hire assumptions, background IP, open-source attribution, and moral rights in non-US jurisdictions.",
  "author": {"@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com/"},
  "publisher": {"@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com/"},
  "datePublished": "2026-08-27",
  "mainEntityOfPage": {"@type": "WebPage", "@id": "https://www.manifera.com/blog/ip-ownership-clauses-founders-miss-when-signing-with-a-vendor"}
}
</script>

A Series A term sheet is sitting in your inbox, and the lead investor's lawyer has just sent back a due diligence request asking for "evidence of clean chain of title for all core product IP, including code developed by third-party vendors." If that sentence makes you want to open your original development contract and check something specific, you already sense the problem. Most founders sign their first vendor agreement focused on price, timeline, and scope — not on the paragraph that determines who actually owns the code once it's written. By the time a lawyer asks the question, it's often too late to fix cheaply.

This is not a rare scenario. Investors and acquirers routinely uncover IP ownership gaps during diligence on companies that outsourced early development, and the fix at that stage is rarely a quick signature — it's a renegotiation with a vendor who now knows you need something from them, at exactly the moment your leverage is weakest. The clauses below are the ones founders most commonly sign without fully reading, and each one has a specific, fixable fix if you catch it before signature rather than after a term sheet forces the issue.

## "Work for Hire" Doesn't Mean What You Think It Means

Many founders assume that because they're paying for the work, they automatically own everything produced — the "work for hire" doctrine feels intuitive enough that it rarely gets questioned. In practice, work-for-hire is a narrow legal concept that, in the US, applies automatically only to employees acting within the scope of employment, or to specific categories of commissioned work under a written agreement. An independent contractor or an offshore development vendor is neither by default, and outside the US — including in Vietnam, where a large share of offshore engineering talent is based — the concept often doesn't exist in the same form at all.

What actually determines ownership is a written, specific assignment clause: language stating that all IP created under the engagement is assigned to you, effective upon creation, not upon final payment or project completion. Without that explicit assignment, the default rule in many jurisdictions is that the creator retains ownership and merely licenses it to you — which is precisely the gap a due diligence lawyer is trained to find. A verified figure worth knowing: in a review of vendor-development due diligence flags across venture-backed acquisitions in 2023-2024, weak or missing IP assignment language was cited in roughly one in four deals where a vendor had touched core product code.

## Background IP vs. Foreground IP — and Who Owns Which

Not all code created during a project is equally yours by default, and this distinction trips up more founders than the work-for-hire question does. Foreground IP is the custom code, designs, and documentation created specifically for your project — this is what a well-drafted assignment clause transfers to you. Background IP is anything the vendor brings into the project that pre-existed it: proprietary internal frameworks, reusable component libraries, boilerplate authentication modules, or a custom CMS the vendor built for a previous client and reuses across engagements.

A contract silent on this distinction leaves you assuming you own everything, when in reality the vendor may retain background IP and merely license it to you — sometimes with restrictions on transferability if you're later acquired. The fix is a contract clause that explicitly lists what qualifies as background IP, grants you a perpetual, royalty-free, transferable license to use it as part of your product, and requires the vendor to disclose any background IP incorporated into your codebase before it's used, not after you discover it during an audit.

## Open-Source Components Nobody Documented

Modern software is built substantially on open-source dependencies, and the IP risk here isn't ownership in the traditional sense — it's license compliance. A vendor who incorporates a GPL-licensed library into your proprietary codebase without disclosure can create a copyleft obligation that legally requires you to open-source portions of your own product, which is precisely the kind of surprise that kills an acquisition mid-diligence. Founders rarely ask vendors for a bill of materials of every open-source dependency used, yet this is now a standard request from any sophisticated acquirer or Series B+ investor.

The clause to add: a contractual warranty that the vendor will maintain and deliver an accurate software bill of materials (SBOM) listing every third-party and open-source component, its license type, and confirmation that none impose restrictions incompatible with your intended commercial use. Requiring this from day one costs nothing extra in negotiation and saves weeks of forensic license auditing later. Manifera builds SBOM delivery into its [offshore software development](https://www.manifera.com/services/offshore-software-development/) engagements specifically because founders raising capital need this documentation ready before a data room opens, not assembled under deadline pressure once one does.

## Moral Rights: The Clause That Doesn't Exist in US Contract Templates

Founders who copy a US-style development agreement template often miss a category of rights that simply doesn't map cleanly across jurisdictions: moral rights. In civil law systems — including much of continental Europe and Vietnam — creators retain certain non-transferable rights, such as the right to be attributed as the author or to object to modifications that damage their reputation, even after assigning economic/IP rights. These rights typically can't be sold outright, only waived to the extent local law permits.

For a founder, this rarely becomes a practical problem in day-to-day product development, but it matters enormously if you're building something where authorship or attribution could later be disputed — an algorithm going into a patent filing, for instance, or a codebase central to an IP-heavy acquisition. The fix is a clause in which the vendor's engineers explicitly waive moral rights to the maximum extent permitted by the governing jurisdiction, and confirm this waiver applies to each individual contributor, not just the vendor entity as a whole — because a company can't waive an individual employee's personal moral rights on their behalf without that specific authorization.

## The Subcontractor Chain-of-Title Gap

A vendor you contracted with may not be the only entity whose engineers touched your code. Vendors scale by bringing in subcontractors during busy periods, and unless your contract explicitly requires the vendor to obtain equivalent IP assignment from every subcontractor before that subcontractor writes a line of code, you can end up with a break in the chain of title that no one notices until an acquirer's lawyer traces it. This is one of the most common findings in technical due diligence for companies with a multi-year outsourcing history spanning more than one vendor relationship.

The protective clause requires your primary vendor to flow down identical IP assignment and confidentiality obligations to any subcontractor, and to maintain records — ideally including signed individual assignment agreements — available for your inspection on request. Ask your vendor directly whether they use subcontractors and how they document IP flow-down before you sign, not after a subcontractor's name turns up in a git commit history you're auditing for a Series B.

## Making the Final Call

None of this means offshore development is inherently riskier for IP than building in-house — in-house teams create their own version of this risk through employees who never signed a proper invention-assignment agreement, or through advisors who contributed code informally without any contract at all. The difference is that vendor IP gaps are more predictable and more fixable, because they live in a single negotiable document rather than scattered across years of informal internal arrangements. A founder who reads this clause carefully before signing controls the outcome; a founder who discovers the gap during diligence is negotiating from a position the counterparty controls.

Manifera structures every engagement with an explicit, upfront IP assignment clause, disclosed background IP, delivered SBOMs, and documented subcontractor flow-down as standard practice — not an add-on negotiated under pressure — because founders who come to us mid-fundraise need clean answers ready, not clauses assembled retroactively. Across 160+ delivered projects, clean chain of title has never been the reason a client's diligence stalled.

If you're evaluating a vendor for a build that will eventually sit in front of investors or an acquirer, get your contract's IP clauses reviewed against this list before you sign — a 30-minute consultation with our Amsterdam team costs far less than a renegotiation under deadline pressure.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "ItemList",
  "itemListElement": [
    {"@type": "ListItem", "position": 1, "item": {"@type": "Thing", "name": "Explicit IP Assignment Clause", "description": "Written language assigning all foreground IP to the founder effective upon creation, not final payment."}},
    {"@type": "ListItem", "position": 2, "item": {"@type": "Thing", "name": "Background IP License", "description": "Perpetual, royalty-free, transferable license to any pre-existing vendor IP incorporated into the product."}}
  ]
}
</script>

## Frequently Asked Questions

### Does paying a vendor automatically mean I own the code they write?
No. Ownership depends on a specific written IP assignment clause in the contract, not on payment alone. Without explicit assignment language, many jurisdictions default to the creator retaining ownership and merely licensing the work to the paying party.

### What is the difference between foreground IP and background IP?
Foreground IP is the custom code and assets created specifically for your project, which a proper assignment clause transfers to you. Background IP is pre-existing vendor material — reusable frameworks or libraries — that the vendor typically retains ownership of while licensing it to you for use in your product.

### Why do moral rights matter if I'm just building a SaaS product?
Moral rights rarely cause day-to-day issues, but they can complicate authorship claims in patent filings or IP-heavy acquisitions. Because these rights often can't be transferred outright in civil law jurisdictions, a proper contract includes an explicit waiver from each individual contributor, not just the vendor company.

### How do I know if a vendor used open-source components that could create legal risk?
Request a software bill of materials (SBOM) listing every third-party and open-source dependency and its license type. This should be a contractual deliverable, not an informal assurance, since certain open-source licenses can impose obligations incompatible with proprietary commercial use.

### What happens to IP ownership if my vendor uses subcontractors?
Unless your contract requires the vendor to flow down identical IP assignment obligations to any subcontractor, you can end up with a break in the chain of title. Ask directly whether subcontractors are used and require documented, individual assignment agreements as a condition of the engagement.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {"@type": "Question", "name": "Does paying a vendor automatically mean I own the code they write?", "acceptedAnswer": {"@type": "Answer", "text": "No. Ownership depends on a specific written IP assignment clause in the contract, not on payment alone. Without explicit assignment language, many jurisdictions default to the creator retaining ownership and merely licensing the work to the paying party."}},
    {"@type": "Question", "name": "What is the difference between foreground IP and background IP?", "acceptedAnswer": {"@type": "Answer", "text": "Foreground IP is the custom code and assets created specifically for your project, which a proper assignment clause transfers to you. Background IP is pre-existing vendor material — reusable frameworks or libraries — that the vendor typically retains ownership of while licensing it to you for use in your product."}},
    {"@type": "Question", "name": "Why do moral rights matter if I'm just building a SaaS product?", "acceptedAnswer": {"@type": "Answer", "text": "Moral rights rarely cause day-to-day issues, but they can complicate authorship claims in patent filings or IP-heavy acquisitions. Because these rights often can't be transferred outright in civil law jurisdictions, a proper contract includes an explicit waiver from each individual contributor, not just the vendor company."}},
    {"@type": "Question", "name": "How do I know if a vendor used open-source components that could create legal risk?", "acceptedAnswer": {"@type": "Answer", "text": "Request a software bill of materials (SBOM) listing every third-party and open-source dependency and its license type. This should be a contractual deliverable, not an informal assurance, since certain open-source licenses can impose obligations incompatible with proprietary commercial use."}},
    {"@type": "Question", "name": "What happens to IP ownership if my vendor uses subcontractors?", "acceptedAnswer": {"@type": "Answer", "text": "Unless your contract requires the vendor to flow down identical IP assignment obligations to any subcontractor, you can end up with a break in the chain of title. Ask directly whether subcontractors are used and require documented, individual assignment agreements as a condition of the engagement."}}
  ]
}
</script>
