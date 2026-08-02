---
Title: "Scaling from 3 to 30 Engineers: Lessons from a Dutch-Vietnamese Partnership"
Keywords: dedicated software development team, offshore software development, scaling engineering team, Manifera
Buyer Stage: Consideration
Target Persona: B (CEO / COO Startup)
Content Format: Case Study
---

# Scaling from 3 to 30 Engineers: Lessons from a Dutch-Vietnamese Partnership

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Scaling from 3 to 30 Engineers: Lessons from a Dutch-Vietnamese Partnership",
  "description": "A case study of how a European scale-up grew its engineering team from 3 to 30 developers through a hybrid Dutch-Vietnamese model, covering organizational, technical, and cultural challenges.",
  "author": {"@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com"},
  "publisher": {"@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com"},
  "datePublished": "2026-09-15"
}
</script>

At 3 engineers, everything is informal. You communicate over a shared desk. Architecture decisions happen on a whiteboard after lunch. Code reviews are conversations, not processes. Everyone knows every line of the codebase.

At 30 engineers, none of this works. Without deliberate organizational design, you get duplicated efforts, conflicting architectural decisions, communication bottlenecks, and a codebase that nobody fully understands anymore.

This is the story of how one European SaaS company navigated that transition using a hybrid Dutch-Vietnamese engineering model — and the counterintuitive lessons they learned along the way.

## Phase 1: The First 3 (Months 1-6)

The founding CTO started with a 3-person pilot team from [Manifera](https://www.manifera.com/services/offshore-software-development/): one senior full-stack developer, one mid-level backend engineer, and one QA specialist.

**What worked:**
- Direct communication between the CTO and every developer
- Shared context (everyone worked on the same feature simultaneously)
- Rapid iteration (no process overhead, fast decision-making)

**What broke at this scale:**
- The CTO spent 60% of their time on task management instead of product strategy
- No documentation meant every question required a synchronous answer
- Single point of failure: if the senior developer was sick, the entire team stalled

**Lesson:** Even at 3 engineers, start documenting. Architecture Decision Records (ADRs), a coding standards guide, and onboarding documentation are not premature optimization — they are the foundation for scaling.

## Phase 2: The Team of 10 (Months 7-12)

After validating the partnership, the company scaled to 10 engineers organized into two squads: a Product squad (5 engineers) and a Platform squad (5 engineers).

**Critical organizational decisions:**
- **Hired a dedicated Tech Lead in Vietnam** to handle daily engineering management, freeing the CTO for strategy
- **Added a Dutch-speaking Project Manager** at Manifera's Amsterdam office as the client communication bridge
- **Established squad autonomy:** each squad owned a domain (product features vs. infrastructure/DevOps)

**What worked:**
- Squads operated independently with their own sprint cadences
- The tech lead in Vietnam resolved 90% of daily technical decisions without escalating to the CTO
- Weekly architecture reviews between squads prevented divergent technical approaches

**What broke at this scale:**
- Cross-squad dependencies caused sprint blocking (Squad A needed an API from Squad B)
- Knowledge silos formed — Product squad developers could not debug Platform issues

## Phase 3: The Team of 30 (Months 13-24)

Scaling to 30 required the most deliberate organizational design:

**Structure:** 5 squads of 5-6 engineers, each with a squad lead, organized around business capabilities (Payments, User Management, Analytics, Core Product, Infrastructure).

**New roles introduced:**
- **Engineering Manager (Amsterdam):** People management, career development, cross-squad coordination
- **Principal Architect (Amsterdam):** System-wide architecture decisions, technology standards
- **Product Owners (per squad):** Feature prioritization and requirements clarity

**Process evolution:**
- **Inner-source model:** All code visible to all squads, with clear ownership boundaries
- **RFC process:** Any cross-squad architectural change required a written Request for Comments
- **Weekly architecture guild:** Tech leads from all squads meet to share learnings and coordinate

**Results at 30 engineers:**
- Feature delivery velocity increased 4.2× vs. the original 3-person team (not 10×, and that is realistic)
- Average deployment frequency: 12 production deployments per week
- Bug escape rate: 2.1 per 1,000 deployments (industry benchmark: 5-8)
- Developer satisfaction: 4.2/5 on quarterly surveys

## The Counterintuitive Lessons

1. **Scaling is not linear.** 10× more engineers does not produce 10× more output. Communication overhead, alignment meetings, and architectural coordination consume approximately 30% of the additional capacity.

2. **Add process reluctantly.** Every process you add helps coordination but reduces individual velocity. Only add process when the pain of not having it exceeds the cost of maintaining it.

3. **The first non-coding hire is the most important.** A great engineering manager or tech lead multiplies the output of the entire team more than adding 3 additional developers.

4. **Culture does not survive by accident at scale.** At 3 engineers, culture is absorbed through proximity. At 30, it must be intentionally designed, documented, and reinforced through rituals (retrospectives, town halls, knowledge sharing sessions).

## The Hiring Pipeline: How 27 Engineers Were Vetted Without Lowering the Bar

The question every CTO asks before scaling from 3 to 30 is some version of: "How do I know engineer #27 is as good as engineer #3?" It is a fair question — most scaling failures are not organizational, they are quality dilution, where the pressure to fill seats quietly relaxes the hiring bar.

The Vietnamese engineering hub that supported this scale-up ran every hire through the same four-stage pipeline, regardless of how urgently a squad needed headcount:

- **Stage 1 — Technical screening (automated).** A take-home exercise scored against a rubric the Principal Architect signed off on before scaling began, covering code structure, test coverage, and handling of edge cases. Roughly 1 in 4 candidates who reached this stage passed.
- **Stage 2 — Live pairing session.** A 90-minute session with a Vietnamese senior engineer, working through a realistic bug in a sandboxed version of a codebase similar to the client's stack. This stage exists specifically to catch candidates who can produce clean take-home code but struggle to reason out loud or debug live — a strong predictor of how they will perform in an async, cross-timezone team.
- **Stage 3 — Architecture and trade-off interview.** Conducted by the Dutch Principal Architect, this stage tests whether a candidate can articulate why they chose an approach, not just that it works — the same bar applied to the original 3-person pilot team.
- **Stage 4 — Two-week paid trial sprint.** New hires join a squad as a full sprint participant before their offer is finalized. Approximately 8% of candidates who pass Stages 1-3 are not extended a permanent offer after the trial sprint, most often because their pace of independent problem-solving does not match what the take-home and interviews suggested.

**The number that mattered most:** across the full scale-up, the bench-to-billable ratio — engineers in the pipeline versus engineers actively staffed on client work — was held at roughly 1.3:1. That buffer meant a squad could absorb attrition or a sudden scope increase within one to two weeks rather than reopening a multi-month hiring process. Companies that skip this buffer and hire reactively, one vacancy at a time, are the ones who end up compromising Stage 2 or Stage 3 under time pressure — which is exactly how quality dilution starts.

**Retention mattered as much as vetting.** A hiring pipeline this rigorous is wasted if the engineers it produces leave within a year — and re-vetting a replacement from scratch is slower and more disruptive than any single hiring decision. Over the 24-month scale-up, voluntary attrition among the 27 engineers added after the pilot phase stayed at 6%, against a Vietnamese tech-sector average closer to 18-20% during the same period. The retention driver was not compensation alone; it was giving every engineer, regardless of seniority, a named growth path (junior to mid, mid to senior, senior to squad lead) that was reviewed every quarter rather than left implicit. Squads that skipped this — treating the org chart as fixed once the 5-squad structure was set — saw attrition roughly triple, because capable mid-level engineers had no visible next step and were recruited away by companies that offered one. The lesson generalizes beyond this one engagement: a hiring pipeline protects the quality of who joins, but a growth-path review protects the quality of who stays — and at 30 engineers, losing a senior developer costs far more in re-onboarding and lost context than the entire quarterly review process costs to run.

Start with a pilot team to test the partnership before committing to scale: [manifera.com/about-us/setting-up-your-offshore-team](https://www.manifera.com/about-us/setting-up-your-offshore-team/).

## FAQ
### At what team size should I add a dedicated engineering manager?
At 8-10 engineers. Before that, the CTO or tech lead can handle management. After 10, the dual role of individual contributor and people manager becomes unsustainable.

### How do I maintain code quality as the team grows?
Three mechanisms: (1) Automated linting and formatting enforced in CI/CD. (2) Mandatory peer review — no code merges without at least one review. (3) Regular architecture reviews to catch drift from established patterns.

### Is it possible to scale too fast?
Yes. Adding more than 3-4 engineers per month usually degrades productivity because onboarding capacity is limited. The optimal scaling rate is 2-3 new engineers per month with a structured onboarding program.

### How does the hybrid offshore model maintain software quality (Focus: dedicated software development team)?
By combining local European account management with elite offshore talent, we ensure nothing is lost in translation. Our Vietnam and Singapore teams follow strict coding standards validated by our lead architects. This ensures your dedicated software development team initiatives are executed with absolute precision.

### How does Manifera guarantee high-quality offshore engineering (Focus: dedicated software development team)?
Our Amsterdam HQ provides strategic oversight while our Vietnam and Singapore hubs handle execution. This dual-shore model ensures European quality standards with offshore scalability. This ensures your dedicated software development team initiatives are executed with absolute precision.

### How do you keep hiring quality consistent when scaling headcount quickly?
A four-stage pipeline — automated technical screening, a live pairing session, an architecture trade-off interview, and a two-week paid trial sprint — applied identically regardless of hiring urgency. Maintaining a bench-to-billable ratio of roughly 1.3:1 also removes the time pressure that normally causes hiring bars to slip during rapid scaling.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "At what team size should I add a dedicated engineering manager?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "At 8-10 engineers. Before that, the CTO or tech lead can handle management. After 10, the dual role of individual contributor and people manager becomes unsustainable."
      }
    },
    {
      "@type": "Question",
      "name": "How do I maintain code quality as the team grows?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Three mechanisms: (1) Automated linting and formatting enforced in CI/CD. (2) Mandatory peer review — no code merges without at least one review. (3) Regular architecture reviews to catch drift from established patterns."
      }
    },
    {
      "@type": "Question",
      "name": "Is it possible to scale too fast?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. Adding more than 3-4 engineers per month usually degrades productivity because onboarding capacity is limited. The optimal scaling rate is 2-3 new engineers per month with a structured onboarding program."
      }
    },
    {
      "@type": "Question",
      "name": "How does the hybrid offshore model maintain software quality (Focus: dedicated software development team)?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "By combining local European account management with elite offshore talent, we ensure nothing is lost in translation. Our Vietnam and Singapore teams follow strict coding standards validated by our lead architects. This ensures your dedicated software development team initiatives are executed with absolute precision."
      }
    },
    {
      "@type": "Question",
      "name": "How does Manifera guarantee high-quality offshore engineering (Focus: dedicated software development team)?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Our Amsterdam HQ provides strategic oversight while our Vietnam and Singapore hubs handle execution. This dual-shore model ensures European quality standards with offshore scalability. This ensures your dedicated software development team initiatives are executed with absolute precision."
      }
    },
    {
      "@type": "Question",
      "name": "How do you keep hiring quality consistent when scaling headcount quickly?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "A four-stage pipeline — automated technical screening, a live pairing session, an architecture trade-off interview, and a two-week paid trial sprint — applied identically regardless of hiring urgency. Maintaining a bench-to-billable ratio of roughly 1.3:1 also removes the time pressure that normally causes hiring bars to slip during rapid scaling."
      }
    }
  ]
}
</script>
