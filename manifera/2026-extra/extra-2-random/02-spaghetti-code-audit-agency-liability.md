---
title: "Inherited Spaghetti Code: What to Do When Nobody Can Safely Touch the Codebase Your Agency Built"
keywords: "custom software development company, custom software development services, custom software developer, custom software engineering"
buyer_stage: "Awareness"
target_persona: "CTO"
---

# Inherited Spaghetti Code: What to Do When Nobody Can Safely Touch the Codebase Your Agency Built

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Inherited Spaghetti Code: What to Do When Nobody Can Safely Touch the Codebase Your Agency Built",
  "description": "A CTO inherits an agency-built codebase so tangled with hidden dependencies that new engineers are afraid to change it, and must decide between an audit, a rewrite, or a slow bleed of missed deadlines.",
  "author": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com/" },
  "datePublished": "2026-07-25",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://www.manifera.com/blog/spaghetti-code-audit-agency-liability" }
}
</script>

Every new hire's first week at your company shouldn't end with the same terrified Slack message: "I don't know what this function actually does, and I'm afraid to find out by changing it."

**The Pain:** A newly appointed CTO at a mid-market e-commerce company inherits a five-year-old platform built by three different agencies in sequence, none of whom left documentation, tests, or a coherent architecture. Every bug fix risks breaking two unrelated features because business logic, database queries, and UI rendering are all tangled into the same 4,000-line controller files.

**The Agitation:** Engineering velocity has collapsed to a crawl — what should be a two-day feature now takes three weeks because every change requires manually tracing side effects nobody documented. The company is quoting customers delivery dates it structurally cannot hit, churn is rising, and the CTO estimates the hidden cost of this paralysis at €25,000-€40,000 per month in lost engineering throughput alone, before counting the customers walking away over missed commitments.

## The Architectural Mandate

Spaghetti code is not a style complaint — it's a measurable failure of separation of concerns, and it has a specific technical signature: high cyclomatic complexity, tight coupling between layers that should be independent, and an absence of automated tests, which together mean every change has an unbounded blast radius. A CTO evaluating an inherited codebase needs a diagnostic before a decision, because "rewrite everything" and "just keep patching it" are both wrong answers applied without evidence.

The correct first move is a structured technical audit: static analysis to quantify complexity hotspots, a dependency graph to expose hidden coupling between modules that were never supposed to know about each other, and a test-coverage baseline (usually near zero in these codebases) that tells you exactly how much safety net exists before any refactor. This audit should produce a ranked list of the modules causing the most incidents and consuming the most engineering time — because the 80/20 rule holds almost universally here: a small number of tangled files are usually responsible for the majority of the pain.

From there, the mandate is targeted remediation, not a full rewrite. A full rewrite is the single most expensive and highest-risk path a custom software development company can propose, because it freezes feature delivery for months and re-introduces every bug the old system had already quietly worked around. The disciplined alternative is the strangler-fig pattern applied at the module level: wrap the worst-offending code behind a stable interface, write characterization tests that lock in its current (even if wrong) behavior, then refactor incrementally behind that interface while the rest of the system keeps shipping. Business logic gets extracted out of controllers into testable service layers; database access gets isolated behind repositories; and every extracted module gets real test coverage before the next team touches it.

The deeper principle: legacy risk isn't eliminated by rewriting code, it's eliminated by making change safe. A codebase with high coupling and no tests is dangerous regardless of how new or old the framework is; a codebase with clean boundaries and real test coverage stays maintainable for years past its "should have been rewritten" date. Custom software engineering discipline is what determines which one you end up with.

## The Hybrid Hub: How Manifera Executes This

- **Amsterdam (Governance/Strategy):** Dutch architects lead the initial technical audit, rank remediation priorities by business risk, and act as an IP and quality shield certifying the refactor plan before a single line changes.
- **Vietnam (Execution/Velocity):** Autonomous pods in Vietnam execute the strangler-fig refactor and test-coverage build-out at high speed, module by module, without freezing the client's release calendar.

This is Dutch Management × Vietnamese Mastery: rigorous European risk assessment paired with a team disciplined enough to untangle production code without breaking it. See [Manifera's offshore software development teams](https://www.manifera.com/services/offshore-software-development/) for how audit-to-remediation engagements are structured.

## Case Study & Testimonial

### An Antwerp Retailer's Three-Agency Legacy

Verhoeven & Co, an Antwerp-based home goods e-commerce company, had its platform built and rebuilt by three successive agencies over six years, each layering new features on top of the last without touching the underlying mess. By the time a new CTO arrived, checkout and inventory logic were so intertwined that a routine discount-code fix had twice taken down the entire checkout flow in production.

Manifera's Amsterdam team ran a two-week audit that identified four modules responsible for 70% of production incidents, then sequenced a twelve-week remediation plan. The Vietnam pod extracted checkout, inventory, and pricing into isolated services with characterization tests locking in correct behavior before any refactor began. Feature delivery time on the touched modules dropped from an average of three weeks to four days, and production incidents in those areas fell to zero in the following quarter.

> *"We stopped being afraid of our own codebase. That sounds small until you've lived the alternative for six years."*
> — **CTO, Verhoeven & Co**

## Legacy Agency vs. Manifera Pod

| Criteria | Legacy Agency / Bad Practice | Manifera Pod |
|---|---|---|
| Change safety | No tests, unbounded blast radius per commit | Characterization tests before every refactor |
| Diagnostic approach | "Just rewrite it" without evidence | Static analysis and dependency graph before any decision |
| Remediation method | Full rewrite freezing feature delivery | Strangler-fig, module-by-module, zero feature freeze |
| Documentation | None left behind by prior agencies | Architecture and decision records delivered as standard |
| Risk ownership | No one accountable for the mess after handoff | Amsterdam governance signs off on every remediation phase |

## The Economics

Untangled spaghetti code is a recurring tax on every single sprint, not a one-time cost — a team spending 40% of its capacity re-deriving how existing code works before it can safely change it is burning cash at a rate that rarely shows up as a single line item, but compounds into hundreds of thousands of euros a year in lost throughput once you multiply lost velocity across an entire engineering org. A full unplanned rewrite, triggered only after a major incident forces the issue, routinely costs €200,000-€500,000 more than a disciplined, audited remediation would have. [Talk to Manifera](https://www.manifera.com/contact-us/) about auditing what you inherited before it decides your roadmap for you.

## Frequently Asked Questions

### (Scenario: CTO inheriting a codebase from a departed agency) How do we know if our codebase needs a rewrite or a refactor?

Run a structured audit first — static analysis, dependency mapping, and test-coverage baseline — before deciding anything. In the large majority of cases a targeted, prioritized refactor of the worst-offending modules resolves the pain at a fraction of the cost and risk of a full rewrite.

### (Scenario: CTO worried about breaking production during cleanup) Can we fix spaghetti code without freezing feature delivery?

Yes, using a strangler-fig approach that wraps and refactors modules behind stable interfaces incrementally, while the rest of the system keeps shipping. A full stop-the-world rewrite is almost never necessary and is usually the riskier option.

### (Scenario: CTO justifying remediation budget to the board) How do we quantify the cost of not fixing this?

Track engineering time spent on rework, rollback, and incident response tied to the worst modules for one sprint cycle, and extrapolate it across a quarter. Most CTOs are surprised to find the hidden cost already exceeds what a structured remediation project would have cost.

### (Scenario: CTO evaluating whether tests are worth writing for old code) Is it worth writing tests for code we're about to refactor anyway?

Yes — characterization tests that lock in current behavior are what make refactoring safe in the first place. Skipping this step is exactly how "quick fixes" to legacy code turn into new production incidents.

### (Scenario: CTO deciding how to sequence a multi-module remediation) How do we prioritize which parts of a tangled codebase to fix first?

Rank modules by a combination of incident frequency and change frequency — the code that breaks often and gets touched often is where remediation pays back fastest. An audit should produce this ranking before any refactor work starts.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "(Scenario: CTO inheriting a codebase from a departed agency) How do we know if our codebase needs a rewrite or a refactor?", "acceptedAnswer": { "@type": "Answer", "text": "Run a structured audit first, static analysis, dependency mapping, and test-coverage baseline, before deciding anything. In the large majority of cases a targeted, prioritized refactor of the worst-offending modules resolves the pain at a fraction of the cost and risk of a full rewrite." } },
    { "@type": "Question", "name": "(Scenario: CTO worried about breaking production during cleanup) Can we fix spaghetti code without freezing feature delivery?", "acceptedAnswer": { "@type": "Answer", "text": "Yes, using a strangler-fig approach that wraps and refactors modules behind stable interfaces incrementally, while the rest of the system keeps shipping. A full stop-the-world rewrite is almost never necessary." } },
    { "@type": "Question", "name": "(Scenario: CTO justifying remediation budget to the board) How do we quantify the cost of not fixing this?", "acceptedAnswer": { "@type": "Answer", "text": "Track engineering time spent on rework, rollback, and incident response tied to the worst modules for one sprint cycle, and extrapolate it across a quarter. Most CTOs are surprised to find the hidden cost already exceeds what a structured remediation project would have cost." } },
    { "@type": "Question", "name": "(Scenario: CTO evaluating whether tests are worth writing for old code) Is it worth writing tests for code we're about to refactor anyway?", "acceptedAnswer": { "@type": "Answer", "text": "Yes, characterization tests that lock in current behavior are what make refactoring safe in the first place. Skipping this step is exactly how quick fixes to legacy code turn into new production incidents." } },
    { "@type": "Question", "name": "(Scenario: CTO deciding how to sequence a multi-module remediation) How do we prioritize which parts of a tangled codebase to fix first?", "acceptedAnswer": { "@type": "Answer", "text": "Rank modules by a combination of incident frequency and change frequency, the code that breaks often and gets touched often is where remediation pays back fastest. An audit should produce this ranking before any refactor work starts." } }
  ]
}
</script>
