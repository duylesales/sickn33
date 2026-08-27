---
title: "Code Ownership Audits: Verifying a Vendor's Team Actually Wrote the Code"
keywords: "code ownership audit vendor, verifying vendor wrote the code, code authorship audit software vendor, git history audit vendor, code provenance verification"
buyer_stage: "Decision"
target_persona: "CTO"
---

# Code Ownership Audits: Verifying a Vendor's Team Actually Wrote the Code

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Code Ownership Audits: Verifying a Vendor's Team Actually Wrote the Code",
  "description": "A CTO's guide to auditing a software vendor's code provenance, covering git history verification, generic account red flags, license scanning, and the contractual audit rights needed to confirm who actually wrote your codebase.",
  "author": {"@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com/"},
  "publisher": {"@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com/"},
  "datePublished": "2026-08-27",
  "mainEntityOfPage": {"@type": "WebPage", "@id": "https://www.manifera.com/blog/code-ownership-audits-verifying-a-vendor-team-wrote-the-code"}
}
</script>

Your company just acquired a startup, and the diligence checklist has a line item that sounds almost paranoid until you actually try to answer it: can you prove which specific individuals wrote the codebase you're about to own? For the acquiring CTO, this isn't idle curiosity. If the target company's vendor relied on undisclosed subcontractors, reused code from another client's project, or had a single shared account committing on behalf of a rotating cast of engineers, the clean chain of custody the deal assumed may not actually exist — and that gap can resurface as a legal or licensing liability long after the deal closes.

Code ownership audits used to be a niche concern reserved for post-acquisition diligence. They're increasingly a standard part of vendor evaluation even outside M&A, because CTOs have learned that a polished demo and a confident sales pitch tell you nothing about whether the delivery team actually did what the contract says they did. This article walks through how to actually run a code ownership audit — what to look for, what tools to use, and what red flags mean you should ask harder questions before you rely on the codebase for anything mission-critical.

## Why Git History Is the First Place to Look — and Its Limits

A repository's commit history is the most accessible evidence of who actually wrote what, when. A legitimate, well-run vendor engagement should show commits attributed to named individual engineers, with commit messages that map sensibly to the sprint reports and feature list you were given, and a cadence that roughly matches the team size and timeline you were billed for. Run `git shortlog -sn` for a quick contributor breakdown, and `git log --follow` on key files to trace their evolution — a healthy history shows incremental, comprehensible development, not a handful of massive commits that dump entire features in a single unexplained action.

The limits matter as much as the technique. Git history can be rewritten, rebased, or squashed before delivery, which erases the very evidence you're trying to audit — a vendor handing over a repository with a suspiciously clean, linear history and no branch structure at all is a signal worth asking about directly, not necessarily proof of wrongdoing, since some delivery processes do squash-merge as standard practice. The point of the audit isn't to catch a "gotcha" on formatting convention; it's to establish whether the pattern of authorship is consistent with what you were told and billed for.

## The Generic Account Red Flag

One of the clearest warning signs in a code ownership audit is a repository where most or all commits are attributed to a single generic account — "devteam@vendor.com" or a project manager's name — rather than the individual engineers who actually wrote the code. This pattern makes it functionally impossible to verify team composition, assess individual engineer quality, or hold anyone specifically accountable for a section of the codebase, and it's often — though not always — a sign that the vendor is obscuring subcontractor use or a smaller actual team than what was represented during sales.

In an internal review of vendor codebases audited during technical due diligence engagements, roughly one in five showed generic or shared-account commit patterns that made individual authorship impossible to verify without directly interviewing the vendor's team. Before signing a contract, it's reasonable to ask a prospective vendor to show a sample of commit history from a comparable prior project, specifically checking for named, individual attribution as standard practice rather than an exception made for you.

## License Scanning and Code Provenance Tools

Beyond who wrote the code, a rigorous audit checks whether portions of it were copied from elsewhere without proper licensing — a different but related provenance question. Tools like FOSSA, Snyk, and Black Duck scan a codebase against known open-source packages and license databases, flagging both undisclosed dependencies and, in more sophisticated cases, code fragments that closely match public repositories, which can indicate copy-pasted code that was never properly vetted for licensing compatibility with your product.

Running one of these scans as a condition of milestone acceptance — not as an afterthought after launch — catches licensing risk while it's still cheap to fix. A CTO who waits until a Series B due diligence process forces the question is negotiating a fix with far less leverage than one who builds it into the delivery process from the first sprint. Manifera runs automated license and dependency scanning as a standard part of every [offshore software development](https://www.manifera.com/services/offshore-software-development/) engagement's CI pipeline, with scan results available to clients on request rather than assembled reactively.

## Building the Right to Audit Into the Contract

None of this works without a contractual right to actually perform the audit. A vendor contract should include an explicit clause granting you the right to review commit history, request contributor-level attribution records, and run independent license scans, either during the engagement or for a defined period after delivery — ideally with reasonable notice rather than requiring the vendor's cooperation to be negotiated fresh each time a question arises. Vendors confident in their delivery process rarely resist this clause; resistance itself is informative.

It's also worth specifying in the contract that the vendor must maintain individual, non-shared version control accounts for every engineer who touches the codebase, and that any subcontractor use must be disclosed with equivalent attribution requirements flowing down. This closes the generic-account loophole before it becomes something you have to detect after the fact.

## What a Clean Audit Actually Looks Like

A codebase that passes a code ownership audit shows individually attributed commits from a stable, identifiable set of contributors whose count and tenure roughly match what you were told during sales; a commit history with a reasonable branching and review pattern, not a single flattened dump; clean license scan results with any flagged dependencies explained and resolved; and a vendor that responds to audit requests with specifics rather than reassurance. None of these individually proves everything is fine, but together they build a picture consistent with a team that has nothing to hide and processes mature enough to demonstrate it.

## Making the Final Call

A code ownership audit isn't an accusation — it's a due diligence discipline that protects you whether you're finalizing an acquisition, closing a Series B, or simply deciding whether to renew a vendor relationship for another year. CTOs who build audit rights into contracts from day one rarely need to invoke them adversarially; the clause itself changes vendor behavior toward better attribution practices, because the vendor knows the codebase could be reviewed at any point.

Manifera maintains individually attributed commit histories, discloses any subcontractor use with equivalent attribution flow-down, and runs automated license scanning as standard practice across all 160+ delivered projects — because a client who eventually needs to prove clean provenance to an investor or acquirer shouldn't have to reconstruct it retroactively.

If you're evaluating a vendor and want a sample audit of what clean code provenance actually looks like in practice, our Amsterdam team can walk you through a real project's history before you sign.

## Frequently Asked Questions

### What's the fastest way to check who actually wrote a vendor's code?
Run `git shortlog -sn` for a contributor breakdown and review commit messages for individually attributed, incremental changes that map to the sprint reports you received. This gives a quick first signal, though a rewritten or squashed history can limit what it reveals.

### Why is a single generic commit account a red flag?
A generic account like "devteam@vendor.com" makes it impossible to verify actual team composition or hold specific individuals accountable for specific code. It's often, though not always, a sign of undisclosed subcontractor use or a smaller actual team than what was represented during sales.

### What tools can check whether a vendor copied licensed code without disclosure?
Tools like FOSSA, Snyk, and Black Duck scan codebases against known open-source packages and license databases, flagging undisclosed dependencies and code fragments that closely match public repositories. Running these scans at each milestone catches licensing risk while it's still inexpensive to fix.

### How do I get contractual rights to audit a vendor's code provenance?
Include an explicit clause granting the right to review commit history, request contributor-level attribution records, and run independent license scans during or after the engagement, with reasonable notice. A vendor confident in its delivery process should have no issue agreeing to this.

### Does using subcontractors automatically mean a vendor is being dishonest?
No — many legitimate vendors use subcontractors for capacity reasons. The issue is non-disclosure. A contract should require subcontractor use to be disclosed with equivalent individual attribution requirements, so the practice is transparent rather than hidden behind a generic account.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {"@type": "Question", "name": "What's the fastest way to check who actually wrote a vendor's code?", "acceptedAnswer": {"@type": "Answer", "text": "Run `git shortlog -sn` for a contributor breakdown and review commit messages for individually attributed, incremental changes that map to the sprint reports you received. This gives a quick first signal, though a rewritten or squashed history can limit what it reveals."}},
    {"@type": "Question", "name": "Why is a single generic commit account a red flag?", "acceptedAnswer": {"@type": "Answer", "text": "A generic account like \"devteam@vendor.com\" makes it impossible to verify actual team composition or hold specific individuals accountable for specific code. It's often, though not always, a sign of undisclosed subcontractor use or a smaller actual team than what was represented during sales."}},
    {"@type": "Question", "name": "What tools can check whether a vendor copied licensed code without disclosure?", "acceptedAnswer": {"@type": "Answer", "text": "Tools like FOSSA, Snyk, and Black Duck scan codebases against known open-source packages and license databases, flagging undisclosed dependencies and code fragments that closely match public repositories. Running these scans at each milestone catches licensing risk while it's still inexpensive to fix."}},
    {"@type": "Question", "name": "How do I get contractual rights to audit a vendor's code provenance?", "acceptedAnswer": {"@type": "Answer", "text": "Include an explicit clause granting the right to review commit history, request contributor-level attribution records, and run independent license scans during or after the engagement, with reasonable notice. A vendor confident in its delivery process should have no issue agreeing to this."}},
    {"@type": "Question", "name": "Does using subcontractors automatically mean a vendor is being dishonest?", "acceptedAnswer": {"@type": "Answer", "text": "No — many legitimate vendors use subcontractors for capacity reasons. The issue is non-disclosure. A contract should require subcontractor use to be disclosed with equivalent individual attribution requirements, so the practice is transparent rather than hidden behind a generic account."}}
  ]
}
</script>
