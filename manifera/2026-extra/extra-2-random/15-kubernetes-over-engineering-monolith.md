---
title: "Your Kubernetes Cluster Is Running a Monolith: The Over-Engineering Trap"
keywords: "dedicated team services, custom software development solutions, full stack development architecture, software at scale, custom software engineering"
buyer_stage: "Consideration"
target_persona: "CTO"
---

# Your Kubernetes Cluster Is Running a Monolith: The Over-Engineering Trap

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Your Kubernetes Cluster Is Running a Monolith: The Over-Engineering Trap",
  "description": "A CTO's guide to recognizing when a team has over-engineered Kubernetes infrastructure around an application that is still architecturally a monolith, and how to right-size infrastructure complexity to actual scale.",
  "author": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com/" },
  "datePublished": "2026-07-25",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://www.manifera.com/blog/kubernetes-over-engineering-monolith" }
}
</script>

Twelve microservices, a service mesh, and a platform team of four people, all deployed around an application that still shares one database and deploys as a single unit — congratulations, you've built a monolith with extra steps and a much bigger AWS bill.

**The Pain:** A CTO inherited an infrastructure setup that, on paper, looks like textbook cloud-native architecture: Kubernetes, Istio, a dozen "microservices," Helm charts for everything. In practice, every one of those services shares the same database, deploys in lockstep because of tightly coupled contracts, and a single schema migration requires touching all twelve. The platform team spends more time debugging the service mesh than the product team spends shipping features.

**The Agitation:** Infrastructure complexity without the architectural decoupling to justify it is pure overhead — no resilience benefit, no independent scaling benefit, just cost. Mid-market companies running Kubernetes platforms sized for a scale they haven't reached routinely spend €150,000-€300,000 a year more than a right-sized architecture would require, in cloud spend, platform-engineering headcount, and the incident response time lost debugging distributed-systems failure modes that a monolith would never have exposed them to.

## The Architectural Mandate

Microservices are a solution to an organizational scaling problem — multiple teams needing to deploy independently without blocking each other — not a technical best practice to adopt by default. Kubernetes and a service mesh are the operational cost of buying that independence: real distributed-systems complexity (network partitions, eventual consistency, distributed tracing, service discovery) in exchange for real organizational benefit (independent deploy cadences, blast-radius isolation, per-service scaling). When an architecture pays that cost without collecting the benefit — because the "services" still share a database, still deploy together, still can't fail independently — it's over-engineering in the most literal sense: engineering effort spent on complexity the situation didn't require.

The architectural mandate is to evaluate infrastructure complexity against Conway's Law and actual team topology, not against what's trendy on conference stages. A single team of six to ten engineers, shipping one product, does not need twelve independently deployable services — it needs a well-modularized monolith with clean internal boundaries, which delivers the majority of the maintainability benefit people associate with microservices (clear ownership boundaries, testable modules, independent internal teams working without stepping on each other) without paying for network calls where function calls used to work, or a platform team's worth of Kubernetes operational overhead.

The diagnostic questions that actually matter: Do these services scale independently under real load, or does traffic to one always correlate with traffic to the others? Do they deploy independently, or does a change to one routinely require coordinated deployment of several? Do they fail independently, or does one going down take the others with it because of a shared database or synchronous call chain? If the honest answer to all three is "no," the system is a distributed monolith — the worst of both worlds, carrying microservices' operational tax without any of its actual benefits.

Right-sizing doesn't mean never adopting Kubernetes — it means adopting it when the team topology and scaling requirements actually justify it, and building the modular monolith first so that the eventual extraction, if and when it's needed, has clean boundaries to extract along. A monolith with well-defined internal module boundaries can be split into real, independently-deployable services later at a fraction of the cost of retrofitting boundaries into a tangled distributed system that was split too early. The sequencing matters: boundaries first, distribution second, and only when team scale or genuinely divergent scaling requirements demand it.

The economic mandate follows directly: infrastructure complexity has an ongoing carrying cost — platform engineering headcount, cloud spend for redundant control planes, cognitive overhead for every engineer who has to reason about a distributed system instead of a single deployable — and that cost should be weighed against actual, measured organizational need, not adopted preemptively against a scale the company might reach in three years.

## The Hybrid Hub: How Manifera Executes This

- **Amsterdam (Governance/Strategy):** Dutch architects assess actual team topology and scaling needs against current infrastructure, own the right-sizing decision, and act as an IP and quality shield against infrastructure complexity sold for its own sake.
- **Vietnam (Execution/Velocity):** Autonomous pods in Vietnam execute the consolidation — whether that's simplifying an over-built Kubernetes setup or modularizing a monolith's internal boundaries — with the technical discipline the migration requires.

This is Dutch Management × Vietnamese Mastery: architecture decisions grounded in what the organization actually needs, executed by a team that can rebuild the infrastructure layer without disrupting what's currently shipping. Explore how [Manifera's offshore software development teams](https://www.manifera.com/services/offshore-software-development/) approach infrastructure right-sizing for growth-stage companies.

## Case Study & Testimonial

### A The Hague Insurtech's Platform Team Overhead

Zeker Verzekeringen, a The Hague-based insurtech platform, had built out a full Kubernetes and service-mesh infrastructure two years earlier, anticipating rapid scale that hadn't materialized at the pace projected. Twelve "microservices" shared one Postgres instance and deployed together via a coordinated release train every two weeks — functionally a monolith, but with a four-person platform team required just to keep the cluster, mesh, and CI pipelines running, consuming nearly a third of total engineering headcount for infrastructure that delivered no independent-deploy benefit.

Manifera's pod audited the actual coupling between services and found none of the three independence criteria — independent scaling, independent deployment, independent failure — were being met. The Amsterdam team defined a consolidation plan: collapsing the distributed monolith into a well-modularized single deployable with clean internal boundaries, while preserving the option to re-extract services later if team growth justified it. The Vietnam pod executed the consolidation over eight weeks, reducing the platform team's operational burden enough to reassign two engineers back to product work, and cutting cloud infrastructure spend by 40%.

> *"We were paying microservices tax on a monolith. Getting that back let us put two engineers back on the roadmap."*
> — **CTO, Zeker Verzekeringen**

## Legacy Agency vs. Manifera Pod

| Criteria | Legacy Agency / Bad Practice | Manifera Pod |
|---|---|---|
| Architecture decision basis | Trend-driven ("everyone uses Kubernetes") | Team topology and measured scaling need |
| Service boundaries | Fragmented services sharing one database | Clean module boundaries, extraction-ready |
| Platform overhead | Dedicated platform team maintaining unused complexity | Right-sized infrastructure matching actual scale |
| Deployment reality | Coordinated release trains across "independent" services | True independent deployability, or honest monolith |
| Cost profile | High cloud and headcount spend for no operational benefit | Infrastructure cost matched to organizational benefit |
| Migration path | No plan to right-size once mismatch is recognized | Sequenced consolidation with future re-extraction option |

## The Economics

Running Kubernetes and a service mesh for an application that hasn't earned the organizational complexity to justify it is a recurring cost with no corresponding revenue or resilience benefit — mid-market companies in this position commonly spend €150,000-€300,000 a year more than necessary once platform-engineering headcount, redundant control-plane cloud spend, and the incident-response time lost to distributed-systems failure modes are added up. That's cash burning quietly every month with nothing to show for it except a more impressive architecture diagram. Right-sizing infrastructure to actual team and scaling needs typically pays for the consolidation project itself within two to three quarters. [Talk to Manifera](https://www.manifera.com/contact-us/) about auditing whether your infrastructure complexity matches your actual scale.

## Frequently Asked Questions

### (Scenario: CTO suspecting the team has over-built infrastructure) How do we tell if we've over-engineered our infrastructure for our actual scale?

Check whether your "independent" services actually scale, deploy, and fail independently under real conditions. If a change to one routinely requires coordinated deployment of several, or they all share a database, you're carrying distributed-systems complexity without collecting its benefits.

### (Scenario: CTO worried that consolidating infrastructure looks like a step backward) Won't simplifying our Kubernetes setup look like we're moving backward technically?

Right-sizing infrastructure to actual need is a sign of engineering maturity, not regression. The teams that get burned are the ones that keep paying for complexity they don't need because reversing course feels uncomfortable, not the ones that correct course once the mismatch is measured.

### (Scenario: CTO planning for future growth while consolidating now) If we consolidate now, won't we just have to re-split into microservices later anyway?

Possibly, and that's fine, as long as the consolidation preserves clean internal module boundaries. A well-modularized monolith can be split into real independent services later at a fraction of the cost of retrofitting boundaries into a system that was distributed prematurely and tangled since.

### (Scenario: CTO trying to estimate savings from infrastructure right-sizing) How much could we realistically save by right-sizing our infrastructure?

It varies by current overhead, but companies carrying unused Kubernetes and service-mesh complexity commonly recover 30-40% of related cloud spend plus the ability to reassign platform-engineering headcount back to product work, which is often the larger benefit.

### (Scenario: CTO deciding whether now is the right time to invest in real microservices) When does it actually make sense to adopt microservices and Kubernetes?

When you have multiple teams that need to deploy independently without blocking each other, and measurable, divergent scaling requirements across different parts of the system — not before. Team topology and real scaling data should drive the decision, not industry trend-following.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "(Scenario: CTO suspecting the team has over-built infrastructure) How do we tell if we've over-engineered our infrastructure for our actual scale?", "acceptedAnswer": { "@type": "Answer", "text": "Check whether your independent services actually scale, deploy, and fail independently under real conditions. If a change to one routinely requires coordinated deployment of several, or they all share a database, you're carrying distributed-systems complexity without collecting its benefits." } },
    { "@type": "Question", "name": "(Scenario: CTO worried that consolidating infrastructure looks like a step backward) Won't simplifying our Kubernetes setup look like we're moving backward technically?", "acceptedAnswer": { "@type": "Answer", "text": "Right-sizing infrastructure to actual need is a sign of engineering maturity, not regression. The teams that get burned keep paying for complexity they don't need because reversing course feels uncomfortable." } },
    { "@type": "Question", "name": "(Scenario: CTO planning for future growth while consolidating now) If we consolidate now, won't we just have to re-split into microservices later anyway?", "acceptedAnswer": { "@type": "Answer", "text": "Possibly, and that's fine as long as the consolidation preserves clean internal module boundaries. A well-modularized monolith can be split into real independent services later at a fraction of the cost of retrofitting boundaries into a prematurely distributed system." } },
    { "@type": "Question", "name": "(Scenario: CTO trying to estimate savings from infrastructure right-sizing) How much could we realistically save by right-sizing our infrastructure?", "acceptedAnswer": { "@type": "Answer", "text": "It varies by current overhead, but companies carrying unused Kubernetes and service-mesh complexity commonly recover 30-40% of related cloud spend plus the ability to reassign platform-engineering headcount back to product work." } },
    { "@type": "Question", "name": "(Scenario: CTO deciding whether now is the right time to invest in real microservices) When does it actually make sense to adopt microservices and Kubernetes?", "acceptedAnswer": { "@type": "Answer", "text": "When you have multiple teams that need to deploy independently without blocking each other, and measurable, divergent scaling requirements across different parts of the system, not before. Team topology and real scaling data should drive the decision." } }
  ]
}
</script>
