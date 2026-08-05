---
Title: "Cloud Migration Strategy: Moving Enterprise Apps Without Breaking Everything"
Keywords: cloud migration, cloud strategy, AWS migration, infrastructure modernisation, lift and shift, Manifera
Buyer Stage: Consideration
Target Persona: A (CTO / VP Engineering)
Content Format: Strategic Framework
---

# Cloud Migration Strategy: Moving Enterprise Apps Without Breaking Everything

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Cloud Migration Strategy: Moving Enterprise Apps Without Breaking Everything",
  "description": "A strategic framework for CTOs planning cloud migrations — covering the 6Rs of migration, risk assessment, cost modelling, and a phased execution approach that minimises business disruption.",
  "author": {"@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com"},
  "publisher": {"@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com"},
  "datePublished": "2026-08-06",
  "dateModified": "2026-08-05"
}
</script>

A mid-market logistics company decided to migrate to AWS. They hired a cloud architect, planned a "Big Bang" migration weekend, and moved everything at once. On Monday morning, the application was down. The database migration had corrupted 30% of the transaction records. The rollback took 72 hours. The total cost of the failed migration — including lost revenue, emergency consulting, and customer churn — exceeded €500,000. The cloud bill they were trying to reduce was €8,000/month.

Cloud migration is not a technology project. It is a business transformation that happens to involve technology. The companies that succeed approach it with the same discipline they would bring to an acquisition or a market expansion — methodical planning, phased execution, and continuous validation.

## The 6Rs: Choosing the Right Strategy for Each Workload

Not every application should be migrated the same way. Gartner first outlined five migration strategies in 2011; AWS's Stephen Orban expanded the framework to six in a 2016 AWS Enterprise Strategy blog post, and the "6Rs" remains the most practical way to categorise migration strategies a decade later:

**1. Rehost (Lift and Shift).** Move the application as-is to cloud infrastructure. No code changes. The fastest approach (days to weeks per application) but captures the least cloud benefit. Best for: applications with imminent data centre lease expirations that need to move quickly.

**2. Replatform (Lift, Tinker, and Shift).** Make a few targeted optimisations during migration without changing the core architecture. Examples: moving from a self-managed MySQL to AWS RDS, or replacing a local file system with S3. Captures moderate cloud benefits with limited risk.

**3. Refactor (Re-architect).** Rebuild the application to take full advantage of cloud-native services — serverless functions, managed containers, event-driven architectures. Captures maximum benefit but requires the most effort (months per application).

**4. Repurchase.** Replace the on-premises application with a cloud-based SaaS product. Example: migrate from an on-premises CRM to Salesforce. Eliminates maintenance entirely but may require data migration and workflow changes.

**5. Retire.** Shut down applications that are no longer needed. During a migration assessment, most organisations discover 10-20% of their applications are unused or redundant.

**6. Retain.** Keep certain applications on-premises. Some applications have regulatory requirements, latency constraints, or deep hardware dependencies that make cloud migration impractical or uneconomical.

## Cost Modelling: The Cloud Is Not Automatically Cheaper

The number one cloud migration myth: "Moving to the cloud will reduce our infrastructure costs." Sometimes it does. Often it does not — at least not initially. This is not a fringe problem: Flexera's 2025 State of the Cloud Report found that 27% of cloud spend continues to be wasted, a figure that has held remarkably steady in the 27-32% range every year since Flexera started tracking it in 2019, and that 84% of organisations name managing cloud spend as their top cloud challenge. Cloud waste is not a rookie mistake that goes away with experience — it is a structural feature of how cloud billing works that requires active, ongoing management.

**The hidden costs of cloud:**

- **Data transfer costs.** Cloud providers charge for data leaving their network (egress). If your application transfers 10TB/month out of AWS, that is approximately €900/month in egress fees alone.
- **Managed service premiums.** AWS RDS costs 2-3x more than running the same database on a self-managed EC2 instance. You pay for the convenience of automated backups, patching, and failover.
- **Over-provisioning.** Teams that migrate by "lifting and shifting" often provision the same server sizes they had on-premises — ignoring that cloud allows dynamic scaling. A server that ran at 15% CPU utilisation on-premises will run at 15% CPU utilisation on AWS, costing the same amount for 85% wasted capacity.
- **Cost management skills.** Cloud costs require active management. Without someone monitoring reserved instances, spot pricing, and resource utilisation, the Flexera waste figure above (27%+) is exactly what accumulates by default.

**The realistic cost trajectory:** Expect costs to increase 10-20% in the first 6 months (migration overhead, dual-running environments, learning curve). Break-even typically occurs at month 12-18 as teams optimise resource allocation. Cost savings of 20-40% compared to on-premises are achievable by year 2, but only with active cost management — and against a backdrop where Gartner forecasts worldwide public cloud end-user spending will reach $850 billion in 2026, a 21.3% jump from 2025, meaning the pressure to actively manage spend (rather than assume the cloud manages itself) is only increasing industry-wide.

## The Phased Migration Approach

The Big Bang migration — move everything in a single weekend — is how cloud migrations fail catastrophically. The phased approach minimises risk:

**Phase 1: Assessment (4-6 weeks).** Inventory every application, database, and integration. Classify each using the 6Rs framework. Identify dependencies between applications — which apps must move together because they share databases or real-time connections?

**Phase 2: Foundation (2-4 weeks).** Set up the cloud landing zone: networking (VPC, subnets, VPN to on-premises), security (IAM policies, encryption, logging), and cost management (budgets, alerts, tagging strategy).

**Phase 3: Pilot (4-8 weeks).** Migrate 1-2 non-critical applications first. A development environment, an internal tool, or a low-traffic microservice. Learn the process, identify gaps in your runbooks, and build confidence before touching production workloads.

**Phase 4: Migration waves (2-4 weeks per wave).** Group remaining applications into waves of 3-5 applications based on dependencies and risk. Each wave follows the same pattern: pre-migration testing, migration execution, validation, and rollback readiness.

**Phase 5: Optimisation (ongoing).** Right-size instances based on actual utilisation data (not estimates). Implement auto-scaling. Purchase reserved instances for stable workloads. Shut down unused resources.

## The Migration Risk Assessment Matrix: Scoring Workloads Before You Move Them

The phased approach above tells you to sequence migrations from low-risk to high-risk. It does not tell you how to score risk consistently across dozens of applications when everyone contributing to the roadmap has a different intuition about what "risky" actually means. A structured scoring matrix removes that guesswork and gives the Cloud Centre of Excellence a defensible, repeatable way to assign each application to a wave — the same discipline the 6Rs framework brings to strategy selection, applied to sequencing.

**Score each application from 1 (low) to 3 (high) across four dimensions:**

| Dimension | 1 — Low Risk | 2 — Medium Risk | 3 — High Risk |
|-----------|---------------|-------------------|-------------------|
| Business criticality | Internal tool, no revenue impact if down | Supports one department or a secondary revenue stream | Directly processes revenue or is customer-facing at scale |
| Data volume and sensitivity | Under 50GB, no regulated personal data | 50GB-500GB, some personal data | Over 500GB, or regulated data (financial, health, large-scale personal data) |
| Integration complexity | Standalone, 0-1 dependencies | 2-4 upstream or downstream dependencies | 5+ dependencies or real-time integration requirements |
| Team's experience with this workload pattern | Migrated this exact pattern before | Migrated something similar before | First time migrating this specific pattern |

**Reading the total score (sum of all four dimensions, range 4-12):**

| Total Score | Recommended Placement | Rationale |
|--------------|--------------------------|--------------|
| 4-5 | Pilot (Phase 3) | Low blast radius if something goes wrong — ideal for building team confidence and refining runbooks |
| 6-8 | Wave 1-2 | Moderate risk, manageable with standard rollback procedures |
| 9-10 | Wave 3 or later | High risk — schedule after the team has 2-3 successful migrations behind it, with extra validation time budgeted |
| 11-12 | Reconsider Rehost; evaluate Retain or Refactor instead | The risk profile suggests a straight lift-and-shift is the wrong strategy — either keep the workload on-premises for now or invest in re-architecting before moving it |

Running this exercise during Phase 1 (Assessment) routinely reorders what looked like a logical migration sequence — alphabetical, or based on which team asked first — into a genuinely risk-ordered one. It is common for the applications everyone assumed would go first, because they are the newest or best-documented, to score as medium-to-high risk once data sensitivity and integration count are counted honestly rather than assumed.

## Database Migration: Where Everything Gets Complicated

Database migration is the single most technically risky aspect of any cloud migration. Get it wrong and you lose data. Get it right and every other component migration becomes straightforward.

**The three database migration approaches:**

1. **Offline migration.** Schedule a maintenance window, dump the database, transfer the dump file to the cloud, and restore it. Simple and reliable, but requires downtime. Acceptable for databases under 100GB with a 2-4 hour maintenance window.

2. **Online migration with replication.** Set up continuous replication from the on-premises database to the cloud database. When the cloud copy is in sync, cut over DNS to point to the cloud database. Achieves near-zero downtime. AWS DMS (Database Migration Service) supports this for most database engines.

3. **Dual-write migration.** Application writes to both the on-premises and cloud databases simultaneously during the transition period. Reads gradually shift to the cloud database. Complex to implement but provides the safest rollback path.

**Critical: test your rollback plan.** Before every database migration, test that you can restore the on-premises database from the cloud copy. If the migration fails, you must be able to return to the original state within a defined time window.

## Migration Governance: Who Decides What Moves When

Successful cloud migrations require a governance structure that balances speed with risk management:

- **Cloud Centre of Excellence (CCoE).** A cross-functional team (2-3 people) that defines standards, reviews migration plans, and maintains the cloud landing zone. This team does not migrate applications — they enable other teams to migrate safely.
- **Application owners.** The team that owns each application decides the migration strategy and timeline, within the guardrails set by the CCoE.
- **Weekly migration review.** A 30-minute meeting where active migration waves report progress, blockers, and post-migration validation results.

## Cloud Migration With Distributed Engineering Teams

Complex cloud migrations require deep infrastructure expertise — a skillset that is scarce and expensive in Western Europe. Manifera's hybrid model provides European cloud strategy with Vietnamese engineering execution.

Our [dedicated development teams](https://www.manifera.com/services/dedicated-development-teams/) have executed cloud migrations for logistics, fintech, and healthcare clients — all coordinated from our Amsterdam headquarters with implementation in Ho Chi Minh City.

Plan your cloud migration with our team — [manifera.com/contact-us](https://www.manifera.com/contact-us/).

---

## Frequently Asked Questions

### How long does a typical cloud migration take? (Scenario: CTO planning a migration timeline for a 20-application portfolio)

For a portfolio of 20 applications, plan for 6-12 months total: 4-6 weeks for assessment, 2-4 weeks for cloud foundation setup, 4-8 weeks for the pilot migration, and 3-6 months for the remaining migration waves (3-5 applications per wave). The timeline depends heavily on application complexity, data volume, and team experience. Companies that rush cloud migrations to meet arbitrary deadlines consistently experience outages and cost overruns.

### Should we go multi-cloud or single-cloud? (Scenario: CIO concerned about vendor lock-in with AWS)

For most mid-market companies, single-cloud is the pragmatic choice. Multi-cloud doubles your operational complexity, requires expertise in two cloud platforms, and prevents you from using the managed services that provide the most value. The risk of vendor lock-in is real but manageable — use infrastructure-as-code and containerisation to maintain portability. True multi-cloud is justified only if you have regulatory requirements for geographic redundancy or if you are large enough to negotiate pricing leverage between providers.

### What is the biggest mistake companies make during cloud migration? (Scenario: VP Engineering starting their first cloud migration)

Migrating databases and applications together in a single step. Instead, migrate the application first (pointing it to the on-premises database via VPN) and the database second. This separation lets you validate the application works correctly in the cloud environment before adding the risk of data migration. If the application migration fails, you roll back one component. If a combined migration fails, you are debugging two failures simultaneously.

### How do we prevent cloud cost overruns? (Scenario: CFO reviewing a cloud budget that is 40% over projection after 6 months)

Four controls: (1) Implement tagging on every resource — tag by team, environment, and application so you can attribute costs precisely. (2) Set budget alerts at 80% and 100% of monthly budget thresholds. (3) Schedule automated shutdowns for development and staging environments outside business hours (saves 40-60% on non-production costs). (4) Conduct monthly cost reviews where engineering teams justify the resources they are using. Most cloud waste comes from forgotten resources — development instances, test databases, and old snapshots that nobody decommissions.

### Can we migrate to the cloud in phases while keeping some systems on-premises? (Scenario: CTO with a hybrid infrastructure requirement due to regulatory constraints)

Yes — hybrid cloud is a legitimate long-term architecture, not just a transitional state. Use a site-to-site VPN or AWS Direct Connect to create a secure, low-latency connection between your on-premises data centre and the cloud environment. Applications that must remain on-premises can communicate with cloud-hosted services seamlessly. Many financial services and healthcare organisations operate in hybrid mode permanently due to regulatory requirements around data residency.

### How do we decide which applications to migrate first when we have 20+ candidates and no obvious order? (Scenario: CCoE lead building a migration roadmap with several teams lobbying for their application to go first)

Score each application on four dimensions — business criticality, data volume and sensitivity, integration complexity, and the team's prior experience with that workload pattern — each from 1 (low) to 3 (high), giving a total risk score from 4 to 12. Applications scoring 4-5 go in the pilot; 6-8 fill Wave 1-2; 9-10 wait until the team has 2-3 successful migrations behind it; 11-12 should be reconsidered for Retain or Refactor rather than a straight lift-and-shift. This removes the politics from sequencing — teams lobbying to go first because their application is "important" often score as high-risk once data sensitivity and dependency count are counted honestly, which is a useful and objective reason to place them later in the roadmap.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "How long does a typical cloud migration take?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "For 20 applications, plan 6-12 months: 4-6 weeks assessment, 2-4 weeks foundation, 4-8 weeks pilot, and 3-6 months for migration waves of 3-5 applications each. Companies that rush consistently experience outages and cost overruns."
      }
    },
    {
      "@type": "Question",
      "name": "Should we go multi-cloud or single-cloud?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Single-cloud for most mid-market companies. Multi-cloud doubles operational complexity and prevents using the managed services that provide the most value. Use infrastructure-as-code and containerisation for portability. True multi-cloud is justified only for regulatory requirements or pricing leverage."
      }
    },
    {
      "@type": "Question",
      "name": "What is the biggest mistake companies make during cloud migration?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Migrating databases and applications together. Instead, migrate the application first (pointing to on-premises database via VPN), then migrate the database second. This separation lets you validate each step independently and simplifies rollback."
      }
    },
    {
      "@type": "Question",
      "name": "How do we prevent cloud cost overruns?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Four controls: (1) Tag every resource by team, environment, and application. (2) Set budget alerts at 80% and 100%. (3) Auto-shutdown dev/staging outside business hours (saves 40-60%). (4) Monthly cost reviews where teams justify their resources."
      }
    },
    {
      "@type": "Question",
      "name": "Can we migrate to the cloud in phases while keeping some systems on-premises?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes — hybrid cloud is a legitimate long-term architecture. Use site-to-site VPN or AWS Direct Connect for secure, low-latency connections. Many financial services and healthcare organisations operate in hybrid mode permanently due to data residency requirements."
      }
    },
    {
      "@type": "Question",
      "name": "How do we decide which applications to migrate first when we have 20+ candidates and no obvious order?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Score each application on four dimensions — business criticality, data volume and sensitivity, integration complexity, and the team's prior experience with that workload pattern — each from 1 to 3, for a total risk score from 4 to 12. Scores of 4-5 go in the pilot; 6-8 fill Wave 1-2; 9-10 wait until the team has 2-3 successful migrations behind it; 11-12 should be reconsidered for Retain or Refactor rather than a straight lift-and-shift. This removes politics from sequencing decisions."
      }
    }
  ]
}
</script>
