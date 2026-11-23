---
Title: "Stages Software Development: The 5 Phases Where 80% of IT Budgets Are Burned"
Keywords: stages software development, software development lifecycle, software project budget, technical debt, custom software development, Manifera
Buyer Stage: Awareness / Budget Planning
Target Persona: B (CEO / CFO / Founder)
Content Format: Financial Analysis & Lifecycle Audit
---

# Stages Software Development: The 5 Phases Where 80% of IT Budgets Are Burned

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Stages Software Development: The 5 Phases Where 80% of IT Budgets Are Burned",
  "description": "A financial audit of the software development lifecycle. Exposes the discrepancy between where executives think their IT budget goes (coding) versus where it is actually burned (discovery failures and maintenance debt).",
  "author": {"@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com"},
  "publisher": {"@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com"},
  "datePublished": "2026-09-10",
  "dateModified": "2026-11-23",
  "citation": [
    "https://www.cs.umd.edu/~basili/publications/journals/J82.pdf",
    "https://www.math.unipd.it/~tullio/IS-1/2004/Approfondimenti/CHAOS.html",
    "https://dora.dev/capabilities/test-automation/",
    "https://en.wikipedia.org/wiki/Software_maintenance"
  ]
}
</script>

Ask a CEO to visualize the **stages software development**, and they will picture a room full of engineers typing code. Consequently, when the CEO attempts to reduce the IT budget, they focus entirely on the coding phase: "Can we hire cheaper engineers? Can we code faster? Can we use AI to write the code?"

This is a fundamental misallocation of financial attention. 

In a standard enterprise software project, the actual writing of syntax accounts for less than 20% of the Total Cost of Ownership (TCO) over a three-year lifespan. If you slash the coding budget by half by hiring the cheapest agency you can find, you save 10% of your total budget. But in doing so, you explode the costs in the other 80% of the lifecycle.

If you want to control IT budgets, you must stop looking at the cost of typing and start looking at the cost of the entire lifecycle. Here is the true financial breakdown of the 5 phases of software development.

## The Budget Burn: Expected vs. Actual

Most executives enter a software project with a distorted expectation of where the money goes. 

### Phase 1: Discovery & Architecture (The Highest ROI Phase)

**Executive Expectation:** 5% of budget. ("Just gather some requirements and let's start building.")
**Actual Financial Impact:** Shapes most of the project's final cost.

When an agency skips a rigorous Discovery phase to "save money," they are passing the cost downstream with compound interest. If a database schema error is caught during Discovery, it costs a whiteboard conversation to fix. If that same error is discovered in Phase 4 after the UI is built and APIs are wired, it costs a multi-week refactor of the entire stack.

This isn't a Manifera talking point - it is one of the best-known findings in software engineering economics. Barry Boehm first quantified it in *Software Engineering Economics* (1981), and twenty years later he and Victor Basili summarised it as the first item of their "Software Defect Reduction Top 10 List" in IEEE Computer: "Finding and fixing a software problem after delivery is often 100 times more expensive than finding and fixing it during the requirements and design phase." The Standish Group's 1995 CHAOS report reaches the same conclusion from the opposite direction: among the reasons respondents gave for impaired, eventually cancelled projects, incomplete requirements (13.1%) and lack of user involvement (12.4%) topped the list, ahead of lack of resources (10.6%) and unrealistic expectations (9.9%). Both point to the same operational truth: money spent finding the right requirements before Phase 3 begins is the highest-leverage euro in the entire budget.

As the old programming adage puts it, only half-jokingly:

> *"Weeks of coding can save you hours of planning."* 

At Manifera, we run a dedicated Discovery phase led by our Dutch architects before any offshore engineering begins. We map the data models, define the API contracts, and lock the architecture. We over-invest in Phase 1 to brutally suppress the costs in Phases 3 and 4.

### Phase 2: Design & Prototyping (The Validation Phase)

**Executive Expectation:** 10% of budget.
**Actual Financial Impact:** The primary defense against building the wrong product.

You do not want your developers deciding how a complex workflow should operate while they are writing the code. UI/UX design is far cheaper than engineering. As an illustration, a designer might iterate through three versions of a dashboard in Figma in around 16 hours, while an engineering team could need ten times as long to build, test, and tear down those same three versions in code. 

If you are paying developer hourly rates to experiment with user interfaces, your budget is bleeding. 

### Phase 3: Development & Coding (The Implementation Phase)

**Executive Expectation:** 70% of budget. ("This is where the real work happens.")
**Actual Financial Impact:** 20% of the 3-year Total Cost of Ownership.

This is the phase everyone obsesses over. It is also the phase most heavily impacted by the decisions made in Phases 1 and 2. 

If you hire a cheap, unstructured [offshore software development](https://www.manifera.com/services/offshore-software-development/) team, they will quote you a phenomenally low price for Phase 3. They achieve this price by skipping automated testing, ignoring CI/CD pipelines, and writing procedural, tightly-coupled code. The immediate invoice is small. But they have just armed a financial time bomb that will detonate in Phase 5.

### Phase 4: Testing & QA (The Reality Check)

**Executive Expectation:** 5% of budget. ("Just click around and make sure it works.")
**Actual Financial Impact:** The difference between a smooth launch and a brand-destroying catastrophe.

Manual testing does not scale. If a QA team has to manually verify 50 workflows every time a developer commits code, your deployment cycle will grind to a halt. Professional engineering pods automate this phase. They write End-to-End (E2E) tests in Cypress or Playwright. They run Static Application Security Testing (SAST) in the deployment pipeline. 

The data backs this operationally, not just financially. DORA, the research program behind the annual State of DevOps reports, lists test automation as a core technical capability. Its guidance states that "running tests continuously as part of a pipeline contributes to quick feedback for developers, a short lead time from check-in to release, and a low error rate in production environments," and that its research shows test automation "drives improved software stability, reduced team burnout, and lower deployment pain." Automated testing is not a QA nice-to-have; it is one of the few capabilities linked to both faster delivery and fewer production incidents at the same time - the two outcomes most executives assume trade off against each other.

Building automated tests costs money upfront. But it is the only mechanism that prevents Phase 5 maintenance costs from spiraling out of control.

### Phase 5: Deployment & Maintenance (The Eternal Burn)

**Executive Expectation:** 10% of budget. ("The project is done.")
**Actual Financial Impact:** 50%+ of the 3-year Total Cost of Ownership.

This is not a Manifera exaggeration - it is one of the most consistent findings in software cost research. Academic reviews put software maintenance at 80 to 90 percent of total lifecycle cost (Ulziit et al., 2015, as summarised in the software maintenance literature), and IT budget benchmarks have long shown that most corporate IT spending goes to running existing systems rather than building new ones. Over a system's full operational life, cumulative maintenance spend can easily exceed the original build cost several times over.

Software is not a building; it does not stay standing just because you finished construction. Software is a living organism in a hostile environment. Dependencies become deprecated. APIs change. New browser versions break old CSS. Security vulnerabilities (CVEs) are discovered daily.

If your team built a chaotic, undocumented, untested codebase in Phase 3 (because you forced them to rush), Phase 5 becomes a nightmare. Every new feature request takes 3x longer because the developers must untangle spaghetti code. Every bug fix creates two new bugs. Eventually, the codebase becomes so fragile that the team declares "bankruptcy" and demands a total rewrite.

You saved €40,000 in Phase 3, only to spend €120,000 in Phase 5 on a rewrite.

The practical lesson for a CFO is to budget Phase 5 as an ongoing operating cost from the first day of the project, not as an afterthought once the system is live. Ring-fence a fixed share of each sprint for dependency updates, security patches, and refactoring, and track whether that share is growing. A steadily rising maintenance share is the earliest financial signal that the codebase is accumulating debt faster than the team is paying it down.

## The Cost-of-Change Curve: How to Read Your Own Project's Risk

Boehm's cost-of-change research is not just a historical curiosity - it is a diagnostic tool you can apply to your own project plan today. The core insight is that the multiplier is not fixed; it depends on project size, defect type, and how tightly coupled your architecture is. The ranges below are illustrative planning values, not measured data: the upper end is anchored on Boehm and Basili's "often 100 times" finding for large systems, and the multiplier is much lower on small, simple ones. Use them to estimate where your own project sits, and to decide how much Discovery investment is actually justified.

**Illustrative Cost-of-Change Multipliers:**

| Phase Where Defect Is Found | Small, simple systems | Large, tightly coupled systems |
|---|---|---|
| **Requirements / Discovery** | 1x (baseline) | 1x (baseline) |
| **Design** | ~1.5-3x | ~5-10x |
| **Coding** | ~2-5x | ~10-25x |
| **Testing / QA** | ~4-10x | ~25-50x |
| **Production / Post-launch** | ~4-15x | ~40-100x |

**How to use this table:** If your system is small, has few integrations, and low regulatory exposure (an internal tool, a marketing site), the multiplier is closer to the left column - a rushed Discovery phase is a real but survivable risk. If your system is large, tightly coupled, touches regulated data, or feeds other systems downstream (an ERP, a core banking module, a healthcare record system), the multiplier is closer to the right column - and every week saved by skipping Discovery can cost 10-40x that amount when the resulting defect surfaces in production. This is precisely why Manifera scales Discovery-phase rigor to system criticality rather than applying a flat percentage of budget to every project regardless of risk profile.

## A Lifecycle Budget Checklist for Your Next Proposal

Knowing where the money goes is only useful if it changes how you read the next proposal on your desk. Before you approve a software budget, ask the vendor - or your own team - these five questions. Each one maps to a phase where cost is usually hidden rather than removed.

1. **What exactly is delivered in Discovery, and who signs it off?** A credible answer names concrete outputs: a data model, API contracts, a prioritised backlog, and the assumptions that were tested with real users. "Requirements gathering" with no artefacts is a warning sign. Our guide to [outsourcing product discovery](https://www.manifera.com/outsourcing-product-discovery-why-the-first-4-weeks-determine-software-success/) covers what a strong first month should produce.
2. **Which design decisions will be validated before code is written?** Ask to see the prototype plan. If the answer is "we will figure out the screens during development," you are paying engineering rates for design work.
3. **What percentage of the Phase 3 estimate is automated testing and CI/CD?** If it is zero, the quote is not cheaper; it has moved cost into Phases 4 and 5.
4. **What does the maintenance plan look like in year two?** A serious partner will discuss dependency updates, security patching, monitoring, and who owns incidents. If maintenance is not in the proposal, it is not in the price either.
5. **How will technical debt be measured and reported?** Debt that is never measured is never paid down. Agree on a few indicators up front, such as test coverage on critical paths, deployment frequency, and the share of each sprint spent on unplanned fixes. We explain how to turn those numbers into a board-level case in our article on [tech debt ROI](https://www.manifera.com/tech-debt-roi-how-to-measure-and-justify-refactoring-to-the-board/).

None of these questions require technical expertise to ask. They require only the discipline to look past the Phase 3 number. A proposal that answers all five clearly may look more expensive on day one, but it is usually the cheaper option over three years, because the costs are visible instead of deferred. For a broader view of how process discipline affects delivery, see our piece on [modern software development processes](https://www.manifera.com/software-development-processes-why-move-fast-and-break-things-is-dead/).

## The Hybrid Offshore Solution

The traditional local European agency is too expensive in Phase 3. The pure freelance offshore model is a disaster in Phases 1, 4, and 5.

Manifera’s [custom software development](https://www.manifera.com/services/custom-software-development/) model solves this lifecycle imbalance:

- **Phase 1 & 2 (Architecture/Design):** Led by senior Dutch experts who ensure the foundation is flawless.
- **Phase 3 (Development):** Executed by elite Vietnamese engineering pods at a significantly lower rate than equivalent EU engineering capacity.
- **Phase 4 & 5 (QA/Maintenance):** Governed by strict European CI/CD standards, automated testing, and zero-trust security policies to keep long-term costs flat.

Stop optimizing for the cost of typing. Start optimizing the entire lifecycle.

Planning a new build or reviewing a proposal? Talk to our architects about your project budget - [manifera.com/contact-us](https://www.manifera.com/contact-us/).

---

## FAQs

### Why does the Discovery phase cost so much if no code is being written? [Scenario: CFO reviewing an agency proposal]
Because architectural mistakes are exponentially more expensive to fix once code is written. Spending €15,000 on Discovery to perfectly map database schemas, API contracts, and user flows prevents a €70,000 emergency rewrite in Month 6. Discovery is not an "extra" cost; it is an insurance policy against architectural failure.

### Why is the team spending time writing "automated tests" instead of building features? [Scenario: CEO wondering why development seems slow]
Manual testing does not scale. If developers do not write automated unit and integration tests (which takes time upfront), every new feature will eventually break an old feature, and nobody will know until a user complains. Automated testing slows down Phase 3 slightly to prevent Phase 5 from becoming a paralyzing, expensive nightmare of regression bugs.

### Can we skip UI prototyping in Figma and just design it in the code? [Scenario: Product Manager pushing for a faster launch]
No. Designing in code is the most expensive way to iterate. A UI designer can build, test, and scrap three different interface concepts in 16 hours. An engineering team might take 160 hours to do the same thing in code. Prototyping in Phase 2 protects the Phase 3 budget from being wasted on UI experimentation.

### How much should I budget for Phase 5 (Maintenance) annually? [Scenario: CTO planning long-term budgets]
A common planning range is 15-20% of the initial build cost per year, assuming the code was written with clean architecture and automated tests. If the initial build was rushed and lacks tests (high technical debt), maintenance costs can easily exceed 40% of the initial build cost annually just to keep the system running, not including new features.

### Why do some offshore agencies quote 50% less for the exact same project? [Scenario: Founder comparing offshore quotes]
Because they are quoting only for Phase 3 (coding) and skipping the rest. They will skip Phase 1 (Architecture), rely on you for Phase 2 (Design), skip automated testing in Phase 4 (QA), and leave you with a fragile, undocumented codebase that collapses in Phase 5. The lowest upfront quote very often leads to the highest Total Cost of Ownership.

### How do I know if my project needs a longer Discovery phase or if I'm over-investing? [Scenario: CTO deciding how much Discovery is "enough"]
It depends on how expensive a late-discovered defect would be for your specific system. Use Boehm's cost-of-change research as a diagnostic: for small, loosely coupled systems with low regulatory exposure, the cost of fixing a defect late rather than early is a modest multiple, and a 1-2 week Discovery phase is usually sufficient. For large, tightly coupled, or regulated systems (core financial platforms, healthcare records, systems with many downstream integrations), Boehm and Basili found late fixes are often 100 times more expensive, which justifies a 3-4+ week Discovery phase even though it delays the first line of code. The right question is never "how much does Discovery cost," it is "what does a Phase 4 or Phase 5 defect in this specific system cost us if we skip it."

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Why does the Discovery phase cost so much if no code is being written?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Architectural mistakes are exponentially more expensive to fix once code is written. Spending €15,000 on Discovery to map schemas and APIs prevents a €70,000 emergency rewrite later. It is an insurance policy against failure."
      }
    },
    {
      "@type": "Question",
      "name": "Why is the team spending time writing 'automated tests' instead of building features?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Manual testing does not scale. Automated testing slows down the coding phase slightly to prevent the maintenance phase from becoming an expensive nightmare of regression bugs. It ensures new features don't break old ones."
      }
    },
    {
      "@type": "Question",
      "name": "Can we skip UI prototyping in Figma and just design it in the code?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No. Designing in code is the most expensive way to iterate. A designer can scrap three UI concepts in 16 hours; an engineering team takes 160 hours to do the same. Prototyping protects the engineering budget from being wasted on experimentation."
      }
    },
    {
      "@type": "Question",
      "name": "How much should I budget for Phase 5 (Maintenance) annually?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "A common planning range is 15-20% of the initial build cost per year for clean codebases. If the build was rushed and lacks automated tests, maintenance can exceed 40% annually just to keep the system running."
      }
    },
    {
      "@type": "Question",
      "name": "Why do some offshore agencies quote 50% less for the exact same project?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Because they only quote for coding. They skip architecture discovery, skip automated testing, and deliver a fragile codebase. The lowest upfront quote very often leads to the highest Total Cost of Ownership in the maintenance phase."
      }
    },
    {
      "@type": "Question",
      "name": "How do I know if my project needs a longer Discovery phase or if I'm over-investing?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "It depends on how expensive a late-discovered defect would be for your system. Based on Boehm's cost-of-change research, small, loosely coupled, low-regulation systems carry a modest late-fix multiplier, so a 1-2 week Discovery phase is usually sufficient. For large, tightly coupled, or regulated systems, late fixes are often 100 times more expensive, justifying a 3-4+ week Discovery phase. The right question is what a late-stage defect would cost in your specific system, not a flat percentage of budget."
      }
    }
  ]
}
</script>
