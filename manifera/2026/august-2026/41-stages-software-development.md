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
  "dateModified": "2026-08-06"
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
**Actual Financial Impact:** Determines 60% of the project's final cost.

When an agency skips a rigorous Discovery phase to "save money," they are passing the cost downstream with compound interest. If a database schema error is caught during Discovery, it costs a whiteboard conversation to fix. If that same error is discovered in Phase 4 after the UI is built and APIs are wired, it costs a multi-week refactor of the entire stack.

This isn't a Manifera talking point — it is one of the most replicated findings in software engineering economics. Barry Boehm's research at TRW, later corroborated with data from IBM, GTE, and the Bell Labs Safeguard program and published in *Software Engineering Economics* (1981), showed the relative cost of fixing a defect rises roughly an order of magnitude with each phase it survives undetected — a requirements-phase fix costs close to nothing, while the same defect found after delivery can cost up to 100x more to correct, with the ratio compressing to roughly 1:4 on small, tightly-scoped projects. And the Standish Group's long-running CHAOS Report data on why projects fail supports the same conclusion from the opposite direction: incomplete requirements (13.1%) and lack of user involvement (12.4%) are consistently the two largest cited failure factors — ahead of lack of resources (10.6%) and unrealistic expectations (9.9%). Both point to the same operational truth: money spent finding the right requirements before Phase 3 begins is the highest-leverage euro in the entire budget.

As the old programming adage puts it, only half-jokingly: 
> *"Weeks of coding can save you hours of planning."* 

At Manifera, we enforce a strict 2-4 week Discovery phase led by our Dutch architects before any offshore engineering begins. We map the data models, define the API contracts, and lock the architecture. We over-invest in Phase 1 to brutally suppress the costs in Phases 3 and 4.

### Phase 2: Design & Prototyping (The Validation Phase)

**Executive Expectation:** 10% of budget.
**Actual Financial Impact:** The primary defense against building the wrong product.

You do not want your developers deciding how a complex workflow should operate while they are writing the code. UI/UX design is mathematically cheaper than engineering. A designer can iterate through three versions of a dashboard in Figma in 16 hours. An engineering team requires 160 hours to build, test, and tear down those same three versions in code. 

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

The data backs this operationally, not just financially. DORA's long-running State of DevOps research — based on annual surveys of tens of thousands of engineering professionals — has repeatedly found that elite-performing teams meeting their own reliability targets are roughly 3.7x more likely to practice continuous testing than lower-performing teams. Automated testing is not a QA nice-to-have; it is one of the handful of technical capabilities DORA's research consistently links to both faster delivery and fewer production incidents simultaneously — the two outcomes most executives assume trade off against each other.

Building automated tests costs money upfront. But it is the only mechanism that prevents Phase 5 maintenance costs from spiraling out of control.

### Phase 5: Deployment & Maintenance (The Eternal Burn)

**Executive Expectation:** 10% of budget. ("The project is done.")
**Actual Financial Impact:** 50%+ of the 3-year Total Cost of Ownership.

This is not a Manifera exaggeration — it is the most consistent finding in software cost research over four decades. The IEEE Computer Society puts the maintenance share at 60–80% of total software lifecycle cost, and multiple independent studies (Schach 1999 at 67%, Galorath 2022 at 75%, Pigoski 2001 above 80%) converge on the same range regardless of decade or methodology. Gartner's own IT spending research separately estimates that organizations spend 55–80% of their IT budgets keeping existing systems running rather than building anything new. Over a system's full operational life, cumulative maintenance spend commonly runs two to four times the original build cost.

Software is not a building; it does not stay standing just because you finished construction. Software is a living organism in a hostile environment. Dependencies become deprecated. APIs change. New browser versions break old CSS. Security vulnerabilities (CVEs) are discovered daily.

If your team built a chaotic, undocumented, untested codebase in Phase 3 (because you forced them to rush), Phase 5 becomes a nightmare. Every new feature request takes 3x longer because the developers must untangle spaghetti code. Every bug fix creates two new bugs. Eventually, the codebase becomes so fragile that the team declares "bankruptcy" and demands a total rewrite.

You saved €40,000 in Phase 3, only to spend €120,000 in Phase 5 on a rewrite.

## The Cost-of-Change Curve: How to Read Your Own Project's Risk

Boehm's cost-of-change research is not just a historical curiosity — it is a diagnostic tool you can apply to your own project plan today. The core insight is that the multiplier is not fixed; it depends on project size, defect type, and how tightly coupled your architecture is. Use the table below to estimate where your own project sits, and to decide how much Discovery investment is actually justified.

| Phase Where Defect Is Found | Illustrative Relative Cost (Boehm, 1981; small/simple projects) | Illustrative Relative Cost (large/complex, tightly coupled systems) |
|---|---|---|
| Requirements / Discovery | 1x (baseline) | 1x (baseline) |
| Design | ~1.5–3x | ~5–10x |
| Coding | ~2–5x | ~10–25x |
| Testing / QA | ~4–10x | ~25–50x |
| Production / Post-launch | ~4–15x | ~40–100x |

**How to use this table:** If your system is small, has few integrations, and low regulatory exposure (an internal tool, a marketing site), the multiplier is closer to the left column — a rushed Discovery phase is a real but survivable risk. If your system is large, tightly coupled, touches regulated data, or feeds other systems downstream (an ERP, a core banking module, a healthcare record system), the multiplier is closer to the right column — and every week saved by skipping Discovery can cost 10-40x that amount when the resulting defect surfaces in production. This is precisely why Manifera scales Discovery-phase rigor to system criticality rather than applying a flat percentage of budget to every project regardless of risk profile.

## The Hybrid Offshore Solution

The traditional local European agency is too expensive in Phase 3. The pure freelance offshore model is a disaster in Phases 1, 4, and 5.

Manifera’s [custom software development](https://www.manifera.com/services/custom-software-development/) model solves this lifecycle imbalance:
- **Phase 1 & 2 (Architecture/Design):** Led by senior Dutch experts who ensure the foundation is flawless.
- **Phase 3 (Development):** Executed by elite Vietnamese engineering pods at a 40-60% cost reduction compared to EU rates.
- **Phase 4 & 5 (QA/Maintenance):** Governed by strict European CI/CD standards, automated testing, and zero-trust security policies to keep long-term costs flat.

Stop optimizing for the cost of typing. Start optimizing the entire lifecycle.

---

## Frequently Asked Questions

### (Scenario: CFO reviewing an agency proposal) Why does the Discovery phase cost so much if no code is being written?
Because architectural mistakes are exponentially more expensive to fix once code is written. Spending €15,000 on Discovery to perfectly map database schemas, API contracts, and user flows prevents a €70,000 emergency rewrite in Month 6. Discovery is not an "extra" cost; it is an insurance policy against architectural failure.

### (Scenario: CEO wondering why development seems slow) Why is the team spending time writing "automated tests" instead of building features?
Manual testing does not scale. If developers do not write automated unit and integration tests (which takes time upfront), every new feature will eventually break an old feature, and nobody will know until a user complains. Automated testing slows down Phase 3 slightly to prevent Phase 5 from becoming a paralyzing, expensive nightmare of regression bugs.

### (Scenario: Product Manager pushing for a faster launch) Can we skip UI prototyping in Figma and just design it in the code?
No. Designing in code is the most expensive way to iterate. A UI designer can build, test, and scrap three different interface concepts in 16 hours. An engineering team might take 160 hours to do the same thing in code. Prototyping in Phase 2 protects the Phase 3 budget from being wasted on UI experimentation.

### (Scenario: CTO planning long-term budgets) How much should I budget for Phase 5 (Maintenance) annually?
The industry standard is 15-20% of the initial build cost per year, assuming the code was written with clean architecture and automated tests. If the initial build was rushed and lacks tests (high technical debt), maintenance costs can easily exceed 40% of the initial build cost annually just to keep the system running, not including new features.

### (Scenario: Founder comparing offshore quotes) Why do some offshore agencies quote 50% less for the exact same project?
Because they are quoting only for Phase 3 (coding) and skipping the rest. They will skip Phase 1 (Architecture), rely on you for Phase 2 (Design), skip automated testing in Phase 4 (QA), and leave you with a fragile, undocumented codebase that collapses in Phase 5. The lowest upfront quote mathematically guarantees the highest Total Cost of Ownership.

### (Scenario: CTO deciding how much Discovery is "enough") How do I know if my project needs a longer Discovery phase or if I'm over-investing?
It depends on how expensive a late-discovered defect would be for your specific system. Use Boehm's cost-of-change research as a diagnostic: for small, loosely coupled systems with low regulatory exposure, the relative cost of fixing a defect late versus early is roughly 4-15x — a 1-2 week Discovery phase is usually sufficient. For large, tightly coupled, or regulated systems (core financial platforms, healthcare records, systems with many downstream integrations), that multiplier can reach 40-100x, which justifies a 3-4+ week Discovery phase even though it delays the first line of code. The right question is never "how much does Discovery cost," it is "what does a Phase 4 or Phase 5 defect in this specific system cost us if we skip it."

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
        "text": "The industry standard is 15-20% of the initial build cost per year for clean codebases. If the build was rushed and lacks automated tests, maintenance can exceed 40% annually just to keep the system running."
      }
    },
    {
      "@type": "Question",
      "name": "Why do some offshore agencies quote 50% less for the exact same project?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Because they only quote for coding. They skip architecture discovery, skip automated testing, and deliver a fragile codebase. The lowest upfront quote mathematically guarantees the highest Total Cost of Ownership in the maintenance phase."
      }
    },
    {
      "@type": "Question",
      "name": "How do I know if my project needs a longer Discovery phase or if I'm over-investing?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "It depends on how expensive a late-discovered defect would be for your system. Based on Boehm's cost-of-change research, small, loosely coupled, low-regulation systems carry a relative cost-of-change of roughly 4-15x, meaning a 1-2 week Discovery phase is usually sufficient. Large, tightly coupled, or regulated systems can see multipliers of 40-100x, justifying a 3-4+ week Discovery phase. The right question is what a late-stage defect would cost in your specific system, not a flat percentage of budget."
      }
    }
  ]
}
</script>
