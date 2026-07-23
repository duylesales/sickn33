---
title: "Bespoke Software Company in Groningen: Rescuing Freelancer Code"
keywords: "bespoke software company, Groningen software development, legacy system rescue, custom software audit, Noord-Nederland IT partner"
buyer_stage: "Decision"
target_persona: "CTO"
---

# Bespoke Software Company in Groningen: Rescuing Freelancer Code

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Bespoke Software Company in Groningen: Rescuing Freelancer Code",
  "description": "A Groningen CTO's system was built by one freelancer who has since disappeared, with no documentation. Here is how a bespoke software company rescues it safely.",
  "author": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com/" },
  "datePublished": "2026-07-24",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://www.manifera.com/blog/bespoke-software-company-groningen" }
}
</script>

What happens to your production system the day the one person who understands it stops answering his phone?

**The Pain:** A CTO at a Groningen energy-transition company inherited a bespoke scheduling and asset-tracking system built four years ago by a single freelance developer — cheap, fast, and, at the time, exactly what a lean scale-up needed. That freelancer has since gone quiet: no forwarding contact, no handover notes, no architecture diagram, no test suite, and a Git history (if one exists at all) that reads like a private diary only he could interpret. The system still runs the business every day. Nobody currently employed has ever opened the codebase.

**The Agitation:** This is not a theoretical risk — it is an active one, and the meter is running. Every week the CTO delays action is a week closer to a server failure, a dependency going out of support, or a data-corruption bug with no one able to safely touch the code to fix it. Rebuilding from scratch is commonly quoted in the Northern Netherlands at €120,000-€180,000 and four to six months — money and time the business does not have if the current system fails first. Meanwhile, operations staff are already running manual spreadsheet workarounds for the parts of the system nobody trusts anymore, quietly burning 15-20 hours a week that should be going into growth, not babysitting a black box.

## The Architectural Mandate

Rescuing orphaned bespoke code is not a rewrite decision — it's a triage decision, and getting it wrong is expensive twice. The correct sequence starts with code archaeology: a structured audit that maps every entry point, database table, external integration, and scheduled job the system actually touches, regardless of what the (usually nonexistent) documentation claims. From there, before a single line changes, the priority is building a characterization test suite — tests that capture what the system *actually does today*, bugs included, so that refactoring has a safety net and regressions get caught before they reach a Groningen production floor.

Once that safety net exists, the system gets decomposed incrementally into a modular monolith with clear domain boundaries — not a big-bang microservices rewrite, which is exactly the kind of overconfident move that creates a second orphaned codebase in eighteen months. Version control gets introduced or cleaned up if it's missing or corrupted. Every non-obvious decision from here forward gets captured as an Architecture Decision Record, so the next engineer — and there will be a next engineer — inherits context instead of archaeology. A CI/CD pipeline (GitHub Actions is the pragmatic default) gets wired in early, not as a nice-to-have but as insurance: it is what prevents this exact bus-factor crisis from recurring, because deployments no longer depend on one person's laptop and muscle memory.

Groningen's business base — energy, agri-tech, logistics, and manufacturing firms built lean and often reliant on a single trusted local freelancer or small shop — makes this scenario far more common here than founders like to admit. The fix isn't finding "another freelancer." It's institutionalizing the knowledge a bespoke software company should have documented the first time.

## The Hybrid Hub: How Manifera Executes This

- **Amsterdam (Governance/Strategy):** Our Dutch architects lead the code archaeology and risk assessment personally, sign off on what gets rebuilt versus preserved, and own the audit trail your board or insurer will eventually ask to see.
- **Vietnam (Execution/Velocity):** A dedicated Autonomous Pod in Ho Chi Minh City writes the characterization tests, executes the incremental refactor, and rebuilds documentation module by module, at a pace no single freelancer could match.

This is Dutch Management × Vietnamese Mastery applied to rescue work specifically: European-grade risk governance deciding what's safe to touch, paired with a Vietnamese engineering bench large enough that no future CTO ever again depends on one irreplaceable person. See how we structure rescue engagements on our [custom software development services page](https://www.manifera.com/services/custom-software-development/).

## Case Study & Testimonial

### The Warehouse System Nobody Was Allowed to Touch

A family-owned logistics company outside Warsaw, Poland, ran its entire warehouse management system on code written by one freelance developer who disappeared after a contract dispute in 2023. The system controlled inbound receiving, pallet tracking, and outbound dispatch for three warehouses — and not one employee could safely modify it. A single failed database migration attempt by an internal junior developer had already caused an 11-hour outage that stalled dispatch for two client accounts.

Manifera ran a two-week code archaeology audit, mapped 40+ undocumented integration points against the company's ERP and three courier APIs, and built a characterization test suite covering the system's actual behavior before touching anything. We then rebuilt the fragile modules on a documented Node.js service layer with automated deployment, while preserving the still-functional legacy core. Total time to a fully documented, team-safe system: nine weeks.

> *"Our old system worked, until the day it didn't and nobody could explain why. Manifera didn't just fix the bugs — they made it so a new hire can actually understand what they're looking at."*
> — **CTO, Logistics Group, Poland**

## The Freelancer Trap vs. the Manifera Pod

| Criteria | Freelancer-Built Legacy System | Manifera Pod |
|---|---|---|
| Documentation | None, or outdated and unreliable | Living architecture docs and ADRs from day one |
| Bus factor | 1 (and that person is gone) | Full pod redundancy, no single point of failure |
| Safety net before changes | None — every edit is a gamble | Characterization tests written before refactoring |
| Deployment process | Manual, undocumented, tribal knowledge | Automated CI/CD, reproducible every time |
| Code ownership and IP | Ambiguous, often never formally transferred | Contractually clear, client-owned from day one |

## The Economics

Run the actual math before deciding to rebuild from zero. A full rewrite in the Northern Netherlands typically runs €120,000-€180,000 and four to six months of parallel-running risk, during which the old system must keep functioning or the business stops. A structured rescue — audit, characterization tests, incremental rebuild — usually costs 35-50% less and ships usable improvements within weeks instead of waiting for a full replacement to go live. Add the hidden cost most CTOs forget: the 15-20 hours a week operations staff currently spend on manual workarounds around the parts of the system nobody trusts, which at a loaded cost of €40/hour is €2,600-€3,500 a month bleeding out quietly, invisible on any invoice.

If your business depends on code that only one absent person ever understood, that is not a maintenance backlog item — it is a solvency risk sitting one server failure away from becoming a headline. Talk to us before that server fails, not after, at our [contact page](https://www.manifera.com/contact-us/).

## Frequently Asked Questions

### (Scenario: Groningen CTO who inherited undocumented freelancer code) How do you safely modify a system when no one currently understands how it works?

We start with a structured code audit and build characterization tests that capture the system's actual current behavior before any refactoring begins. This creates a safety net so changes can be verified against real behavior, not guesswork, before anything reaches production.

### (Scenario: CTO deciding between rescue and full rewrite) Is it cheaper to rescue our old bespoke system or rebuild it from scratch?

In most cases rescue costs 35-50% less than a full rewrite and delivers usable improvements within weeks rather than months. A full rewrite only makes sense when the underlying technology itself is end-of-life or the domain logic has changed so much the old system no longer reflects the business.

### (Scenario: CTO worried about losing institutional knowledge) The original freelancer is unreachable — can you still figure out what the system is supposed to do?

Yes. Code archaeology and characterization testing are built specifically for this situation: we determine intended behavior by observing what the system actually does across real data and integrations, not by relying on documentation that never existed.

### (Scenario: CTO concerned about business continuity during the fix) Will operations have to stop using the current system while you work on it?

No. We rebuild incrementally around the live system, module by module, so the business keeps running on the parts that still work while we replace the fragile parts underneath, with rollback points at every stage.

### (Scenario: Groningen CTO comparing local freelancers vs. a structured pod) Why not just hire another local freelancer to take over the system?

A single freelancer recreates the exact bus-factor risk you're trying to escape. A Manifera Pod distributes knowledge across a governed team with documentation standards, so no future departure can hold your business hostage again.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "(Scenario: Groningen CTO who inherited undocumented freelancer code) How do you safely modify a system when no one currently understands how it works?", "acceptedAnswer": { "@type": "Answer", "text": "We start with a structured code audit and build characterization tests capturing the system's actual current behavior before any refactoring, creating a safety net so changes are verified before reaching production." } },
    { "@type": "Question", "name": "(Scenario: CTO deciding between rescue and full rewrite) Is it cheaper to rescue our old bespoke system or rebuild it from scratch?", "acceptedAnswer": { "@type": "Answer", "text": "Rescue typically costs 35-50% less than a full rewrite and delivers improvements within weeks. A full rewrite only makes sense when the technology is end-of-life or the business logic has fundamentally changed." } },
    { "@type": "Question", "name": "(Scenario: CTO worried about losing institutional knowledge) The original freelancer is unreachable, can you still figure out what the system is supposed to do?", "acceptedAnswer": { "@type": "Answer", "text": "Yes, code archaeology and characterization testing determine intended behavior by observing what the system actually does across real data and integrations, not by relying on nonexistent documentation." } },
    { "@type": "Question", "name": "(Scenario: CTO concerned about business continuity during the fix) Will operations have to stop using the current system while you work on it?", "acceptedAnswer": { "@type": "Answer", "text": "No, we rebuild incrementally around the live system module by module, so the business keeps running on functional parts while fragile parts are replaced with rollback points at every stage." } },
    { "@type": "Question", "name": "(Scenario: Groningen CTO comparing local freelancers vs a structured pod) Why not just hire another local freelancer to take over the system?", "acceptedAnswer": { "@type": "Answer", "text": "A single freelancer recreates the same bus-factor risk. A Manifera Pod distributes knowledge across a governed team with documentation standards so no single departure can hold the business hostage again." } }
  ]
}
</script>
