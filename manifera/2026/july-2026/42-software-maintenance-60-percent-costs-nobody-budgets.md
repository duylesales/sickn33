---
Title: "Software Maintenance: The 60% of Costs Nobody Budgets For"
Keywords: software maintenance, TCO, total cost of ownership, software lifecycle, legacy maintenance, Manifera
Buyer Stage: Awareness
Target Persona: B (CEO / COO)
Content Format: Eye-Opener Analysis
---

# Software Maintenance: The 60% of Costs Nobody Budgets For

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Software Maintenance: The 60% of Costs Nobody Budgets For",
  "description": "An analysis of why software maintenance consumes 60-80% of total lifecycle costs, what drives those costs, and how to budget and manage maintenance to prevent it from consuming your engineering capacity.",
  "author": {"@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com"},
  "publisher": {"@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com"},
  "datePublished": "2026-08-11",
  "dateModified": "2026-08-05"
}
</script>

A CEO commissions a custom software application. The development firm quotes €120,000 and 16 weeks. The CEO budgets €120,000 and moves on. Eighteen months later, the application has consumed an additional €180,000 in maintenance — bug fixes, security patches, framework upgrades, infrastructure scaling, new feature requests from users who interact with the real product differently than anyone predicted. The CEO is stunned: the software cost €300,000, not €120,000. The development cost was only 40% of the total.

This is not an exception. It is the rule. The IEEE Computer Society puts maintenance at 60-80% of the total lifecycle cost of a software system — a figure Gartner's long-standing IT-spending research independently corroborates, finding that a similar 60-80% of enterprise IT budgets goes toward "keeping the lights on" for existing systems rather than building anything new. More recent industry analyses suggest the pressure has only increased: several 2025 IT-spending studies put the "run" share of enterprise IT budgets at 70% or higher. Yet most project budgets account only for the initial build.

## Why Maintenance Costs So Much

Software is not a building. You do not construct it once and let it stand for decades with occasional painting. Software exists in a dynamic ecosystem of operating systems, browsers, frameworks, APIs, security threats, and user expectations that change continuously. Standing still is falling behind.

**The four types of maintenance:**

1. **Corrective maintenance (20-25% of effort).** Bug fixes. Users discover edge cases, data corruptions, and workflow failures that testing did not catch. The more complex the software, the more bugs surface post-launch.

2. **Adaptive maintenance (25-30% of effort).** Changes required because the environment changed. iOS 20 deprecates an API your app relies on. PostgreSQL 18 changes a default configuration that breaks your queries. AWS retires a service you depend on. You did not choose to make these changes — the ecosystem forced you.

3. **Perfective maintenance (30-35% of effort).** Enhancements and new features requested by users after they experience the real product. This is the most valuable type of maintenance — it responds to actual usage data rather than pre-launch assumptions.

4. **Preventive maintenance (10-15% of effort).** Proactive improvements to prevent future problems: refactoring fragile code, updating deprecated dependencies before they become vulnerabilities, improving monitoring to catch issues earlier.

**This is not an abstract split.** Stripe's Developer Coefficient study — a 2018 survey of more than 1,000 developers and 1,000 C-level executives across five countries — found that engineers spend an average of 17.3 hours of a 41.1-hour work week, or roughly 42% of their time, on maintenance and "bad code" rather than shipping new functionality. Even allowing for the survey's age, the direction of travel since 2018 has been toward larger codebases, more dependencies, and more integrations per application — not fewer — so the underlying pressure this figure describes has not gone away.

## The Maintenance Budget Formula

A reliable formula for maintenance budgeting:

**Annual maintenance cost = 15-25% of the original development cost.**

| Original Build Cost | Annual Maintenance (Low) | Annual Maintenance (High) | 5-Year TCO |
|--------------------|------------------------|--------------------------|-----------|
| €50,000 | €7,500/year | €12,500/year | €87,500-€112,500 |
| €100,000 | €15,000/year | €25,000/year | €175,000-€225,000 |
| €200,000 | €30,000/year | €50,000/year | €350,000-€450,000 |
| €500,000 | €75,000/year | €125,000/year | €875,000-€1,125,000 |

**The first year is the most expensive** — typically 25-35% of the build cost — because the highest volume of bugs and usability issues surface from real-world usage. Years 2-5 stabilise at 15-20% if the original build quality was high.

## What Drives Maintenance Costs Up

Certain architectural and organisational decisions during initial development dramatically inflate long-term maintenance costs:

**1. No automated tests.** Without tests, every change is a gamble. Developers spend far longer verifying changes manually and still miss regressions. The most rigorous evidence here is not a rule of thumb but a controlled industrial study: Microsoft Research and IBM (Nagappan, Maximilien, Bhat & Williams, 2008) tracked four production teams that adopted test-driven development and found their pre-release defect density dropped 40-90% compared to comparable teams that did not — at the cost of 15-35% more initial development time. That trade — modestly more expensive to build, substantially cheaper to maintain — is exactly the bet a maintenance budget should be making.

**2. Undocumented architecture.** When the original developers leave (and they always leave), the new team must reverse-engineer the system from code alone. This extends bug fix times from hours to days. A 2-page architecture overview and inline code comments save hundreds of hours over 5 years.

**3. Framework lock-in to abandoned frameworks.** Choosing a trendy framework that loses community support within 2 years means maintaining an application that nobody else can work on. Stick to established, well-supported frameworks with large communities.

**4. Single-developer dependency.** If one person built the entire system and holds all the knowledge, their departure triggers a maintenance crisis. Enforce pair programming, code reviews, and documentation from day one.

**5. Technical debt accumulation.** Every shortcut taken during development increases future maintenance cost. Ward Cunningham, who coined the term in 1992, described the mechanism precisely: "A little debt speeds development so long as it is paid back promptly with a rewrite... the danger occurs when the debt is not repaid. Every minute spent on not-quite-right code counts as interest on that debt." A 30-minute hack today becomes a 10-hour investigation when it breaks in production 18 months later — that gap is the compounding interest Cunningham was describing.

## The Maintenance Cost Multiplier: Why Two €100,000 Builds Diverge So Sharply

The five factors above are not independent, equally-weighted risks — they compound. A useful way to budget for this is to treat each factor as a multiplier on your baseline maintenance cost (the 15-25% formula above), rather than a binary "good practice / bad practice" checkbox. This mirrors how insurers price actuarial risk: each factor shifts the expected cost, and the factors stack.

| Risk Factor | Typical Cost Multiplier | Mechanism |
|---|---|---|
| No automated tests | 1.3-1.4x | Manual regression testing on every change; undetected defects surface in production |
| Undocumented architecture | 1.2-1.3x | New developers spend days, not hours, understanding the system before they can safely change it |
| Single-developer dependency | 1.2-1.3x | Departure triggers a knowledge-recovery period with elevated bug rates and slower delivery |
| Abandoned/unsupported framework | 1.3-1.5x | Security patches, hiring, and third-party integrations all become harder over time |
| High technical debt (deadline-driven shortcuts) | 1.2-1.4x, compounding annually | Interest accrues: each subsequent change takes longer than the last, per Cunningham's original metaphor |

**Applying the framework:** a €100,000 build with clean architecture, automated tests, and no single-developer dependency lands near the low end of the 15-25% annual formula — roughly €15,000-€20,000/year. The same €100,000 build shipped with no tests, no documentation, and one overworked developer who quietly cuts corners under deadline pressure can realistically combine two or three of these multipliers (say, 1.3 × 1.25 × 1.3 ≈ 2.1x), pushing annual maintenance toward €30,000-€40,000 — and the gap widens every year the debt goes unpaid. The multiplier framework is not a precision instrument; it is a way to make an otherwise invisible decision (cut the testing budget to hit a launch date, or not) visible in the currency a CFO actually budgets in.

## Managed Maintenance: The Retainer Model

Rather than hiring full-time developers to maintain an application that requires intermittent attention, many companies use a retainer model with a development partner:

**Monthly retainer structure:**

| Tier | Hours/Month | Best For | Typical Cost |
|------|------------|----------|-------------|
| Basic | 10-20 hours | Bug fixes, security patches, minor updates | €2,000-€4,000 |
| Standard | 20-40 hours | Above + small feature additions | €4,000-€8,000 |
| Premium | 40-80 hours | Above + major features, architecture improvements | €8,000-€16,000 |

The retainer model provides predictable monthly costs, guaranteed availability (no scrambling to find developers when something breaks), and institutional knowledge retention (the same team that maintains your application month after month builds deep familiarity with the codebase).

## Reducing Maintenance Through Better Building

The most effective way to reduce maintenance costs is to build better software from the start. The investments that pay for themselves within 12-18 months:

- **Automated test suite** — initial investment: roughly 15-35% more development time, in line with the Nagappan et al. industrial TDD study cited above. Payoff: substantially fewer defects reaching production, which is where most bug-fix time is actually lost.
- **CI/CD pipeline** — initial investment: 1-2 weeks. Payoff: deployments go from risky 4-hour affairs to routine 10-minute operations.
- **Comprehensive logging and monitoring** — initial investment: 2-3 days. Payoff: issues are detected in minutes instead of discovered by angry customers.
- **Architecture documentation** — initial investment: 1-2 days. Payoff: new developers become productive in weeks instead of months.
- **Dependency management policy** — initial investment: half a day. Payoff: prevents the nightmare of upgrading 3-year-old dependencies with breaking changes.

## Long-Term Maintenance With a Distributed Team

Maintenance work — bug fixes, small features, dependency updates — is ideal for distributed teams because it consists of well-defined, independently deliverable tasks.

Manifera's [custom software development](https://www.manifera.com/services/custom-software-development/) includes post-launch maintenance retainers managed from Amsterdam with engineering execution in Ho Chi Minh City. This gives European companies enterprise-grade maintenance at 40-60% lower cost than local-only teams.

Discuss maintenance options — [manifera.com/contact-us](https://www.manifera.com/contact-us/).

---

## Frequently Asked Questions

### How do we budget for software maintenance if we have never built custom software before? (Scenario: CFO creating a 3-year technology budget for the first time)

Use the 20% rule: budget 20% of the initial development cost per year for maintenance. If the build costs €100,000, allocate €20,000/year for years 1-3. In year 1, expect to use most of this budget (bug fixes, usability improvements). In years 2-3, the budget covers security patches, framework upgrades, and incremental feature development. If you spend significantly less than budgeted, your application is unusually stable. If you spend significantly more, the original build quality may have been poor.

### Should we maintain software in-house or outsource maintenance? (Scenario: Startup CEO deciding whether to hire a full-time developer for maintenance)

If maintenance requires less than 40 hours/month consistently, outsourcing via a retainer is more cost-effective than a full-time hire. A full-time developer in Western Europe costs €70,000-€100,000/year including benefits — that is €140-€200/hour of productive work when accounting for vacation, training, and idle time. A retainer at €80-€120/hour with a flexible monthly allocation costs less and provides access to multiple specialists instead of depending on one generalist.

### What happens if we stop maintaining software entirely? (Scenario: CEO considering cutting the maintenance budget to reduce costs)

Three things happen within 12-18 months: (1) Security vulnerabilities in unmaintained dependencies accumulate, eventually leading to a data breach or compliance failure. (2) Platform changes (new browser versions, OS updates, API deprecations) gradually break functionality, degrading user experience. (3) Users leave because competitors continue improving their products. Software that is not maintained does not remain static — it degrades.

### How do we transition maintenance from the original development team to a new team? (Scenario: CTO replacing their development agency with a new partner)

Plan a 4-6 week transition period: Week 1-2, the new team reads all documentation, sets up their development environment, and deploys to staging independently. Week 3-4, the new team fixes 3-5 small bugs with the original team available for questions. Week 5-6, the new team handles routine maintenance independently while the original team remains on standby. The critical prerequisite: the original team must have created adequate documentation. If they did not, budget an additional 2-4 weeks for the new team to document the system as they learn it.

### At what point should we rebuild instead of continuing to maintain? (Scenario: CTO spending 50% of engineering budget on maintenance of a 7-year-old application)

Consider rebuilding when maintenance costs consistently exceed 30% of the total engineering budget AND the application cannot be incrementally modernised. However, a full rewrite is almost always more expensive and time-consuming than expected. The safer path: identify the 3 most problematic modules, rebuild them as independent services, and gradually migrate functionality. This strangler fig pattern achieves the benefits of a rewrite with 30% of the risk.

### Does investing more upfront in testing and documentation actually pay off, or is that just developer preference? (Scenario: CFO pushing back on a 20%-longer timeline requested for "engineering quality")

The evidence says yes, and it is more rigorous than most engineering claims: a 2008 Microsoft Research and IBM study (Nagappan, Maximilien, Bhat & Williams) tracked four industrial teams that adopted test-driven development on production codebases and measured a 40-90% reduction in pre-release defect density compared to similar teams that did not, at a cost of 15-35% more initial development time. Translated into budget terms: paying roughly 20% more to build correctly is, on average, a substantially better trade than saving 20% at launch and paying for it repeatedly for years afterward through the maintenance cost multipliers above. The catch is that this only shows up on the CFO's numbers 12-18 months after launch — which is exactly why it gets cut under deadline pressure in the room where the original budget is set.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "How do we budget for software maintenance if we have never built custom software before?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Use the 20% rule: budget 20% of initial development cost per year. €100,000 build = €20,000/year for maintenance. Year 1 is highest (bug fixes), years 2-3 cover security patches and incremental features."
      }
    },
    {
      "@type": "Question",
      "name": "Should we maintain software in-house or outsource maintenance?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "If maintenance needs less than 40 hours/month, outsourcing via retainer is more cost-effective. A full-time developer costs €70,000-€100,000/year. A retainer provides flexible allocation and access to multiple specialists instead of one generalist."
      }
    },
    {
      "@type": "Question",
      "name": "What happens if we stop maintaining software entirely?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Within 12-18 months: security vulnerabilities accumulate leading to breaches, platform changes break functionality, and users leave for competitors. Unmaintained software does not remain static — it degrades."
      }
    },
    {
      "@type": "Question",
      "name": "How do we transition maintenance from the original development team to a new team?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Plan 4-6 weeks: Weeks 1-2 documentation review and environment setup. Weeks 3-4 small bug fixes with original team available. Weeks 5-6 independent operation with standby support. Requires adequate existing documentation."
      }
    },
    {
      "@type": "Question",
      "name": "At what point should we rebuild instead of continuing to maintain?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "When maintenance exceeds 30% of engineering budget AND cannot be incrementally modernised. Full rewrites are always costlier than expected. Safer: rebuild the 3 worst modules as independent services using the strangler fig pattern."
      }
    },
    {
      "@type": "Question",
      "name": "Does investing more upfront in testing and documentation actually pay off, or is that just developer preference?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. A 2008 Microsoft Research/IBM study (Nagappan, Maximilien, Bhat & Williams) tracked four industrial teams using test-driven development and found a 40-90% reduction in pre-release defect density versus comparable teams, at a cost of 15-35% more initial development time. Paying roughly 20% more upfront is a better trade than paying repeatedly for years through elevated maintenance costs."
      }
    }
  ]
}
</script>
