---
title: "The Insurtech Project That Was Sold as a New App and Turned Out to Be a Legacy Integration"
keywords: "custom software development, software development company, custom software engineering, software product"
buyer_stage: "Consideration"
target_persona: "C"
---

# The Insurtech Project That Was Sold as a New App and Turned Out to Be a Legacy Integration

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "The Insurtech Project That Was Sold as a New App and Turned Out to Be a Legacy Integration",
  "description": "Why insurtech projects framed as building new software are usually, underneath, primarily legacy system integration projects — and why that reframing changes how they should be scoped.",
  "author": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com/" },
  "datePublished": "2026-08-11",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://www.manifera.com/blog/insurtech-legacy-integration-real-project" }
}
</script>

An insurtech founder pitches, with real confidence, a new claims app, a new customer portal, a new underwriting interface — and every one of those projects, underneath the confident pitch, is actually a legacy core-system integration project wearing a modern UI as its convincing public face. Insurance, as an industry, runs largely on decades-old policy administration and claims systems that any new application inevitably has to talk to, and that integration is usually the majority of the real engineering effort, not an afterthought behind the visible interface.

## Why the New Interface Is Rarely the Hard Part

Building a clean, modern claims-submission interface is, by 2026 engineering standards, genuinely straightforward and well-understood work. What's hard is getting that interface to correctly read from and write to a policy administration system that may be running on decades-old architecture, with data models, business rules, and integration points that were never designed with modern API access in mind. The interface a founder shows investors is the visible 20% of the project; the legacy integration is usually the invisible 80%.

## What Legacy Insurance System Integration Actually Involves

- **Carefully reverse-engineering undocumented business rules** embedded deep inside legacy policy administration systems — rules about coverage calculations, eligibility, and pricing that exist only as code, never as documentation, often written by engineers long since gone from the company.
- **Building genuinely robust middleware to bridge modern API expectations and messy legacy system realities**, since many core insurance platforms expose data through mechanisms (batch files, older SOAP APIs, direct database access) that don't map cleanly to how a modern application expects to communicate.
- **Ongoing data reconciliation between systems** when a new application needs to maintain its own data model alongside the legacy system's actual source of truth, requiring careful synchronization logic to avoid the two silently falling out of sync.
- **Regulatory continuity** — carefully ensuring that a new customer-facing layer doesn't inadvertently bypass compliance checks and business rules the legacy system enforces, often in genuinely non-obvious ways.

## Why Projects Scoped Without This Reality Fail Their First Estimate

A project scoped simply as "build a claims portal," without accounting for legacy integration complexity, will reliably blow past its estimate almost immediately once real development starts, because the actual bottleneck — understanding and safely integrating with the legacy core system — wasn't part of the original scope at all. The interface work usually proceeds roughly on schedule; the integration work, discovered painfully mid-project, becomes the unplanned, dominant majority of the actual timeline.

## The Systems-Thinking Model for What's Actually Below the Surface

Systems theorist Donella Meadows, in her influential work on systems thinking later compiled in "Thinking in Systems," popularized what practitioners often call the iceberg model: a way of understanding that visible events sit atop several deeper, invisible layers — underlying patterns, the structures that produce those patterns, and the mental models that shaped those structures in the first place — with each deeper layer being harder to see but more powerful in determining what actually happens than the visible event on its own. Meadows' central point was that intervening only at the visible-event layer produces shallow, temporary fixes, while understanding and addressing the structural layers underneath produces changes that actually last.

An insurtech project pitched as "build a claims portal" is, almost by definition, describing only the visible-event layer of the iceberg — the interface a user will actually click on. The structural layer underneath, largely invisible from a feature list or a pitch deck, is the legacy policy administration system's actual data model, its embedded business rules, and the specific mechanisms (batch files, older protocols) it uses to communicate with anything else. A team that scopes only the visible interface, the way Adriabroker's original vendor did, is building confidently at the tip of the iceberg while remaining completely unaware of the much larger mass of structural complexity sitting below the waterline, invisible until development actually begins and the team collides with it directly.

This framing explains precisely why a two-week legacy-integration discovery phase changes a project's entire trajectory rather than being a minor scoping refinement: it's the specific activity of deliberately diving below the visible-event layer to map the structural layer before committing to a plan built only on what's visible from the surface. Manifera's insistence on legacy-system-focused discovery before quoting an insurtech project is, in Meadows' terms, a refusal to scope a project based on the iceberg's tip alone — precisely the discipline that let Adriabroker's second attempt succeed where the first, built entirely on visible-surface assumptions, could not.

## Manifera's Approach: Scoping the Real Project From the Start

- **Amsterdam (Governance/Discovery):** Dutch project leads run discovery specifically and deliberately focused on legacy system integration complexity before ever quoting an insurtech project, treating the core-system integration as the primary scoping question rather than an assumed-simple technical detail.
- **Vietnam (Execution/Legacy Integration Depth):** The engineering pod has genuine, direct hands-on experience building middleware specifically for legacy insurance and financial systems, deeply understanding the specific patterns — batch processing, older protocol standards — these particular systems commonly and reliably use.

This is Dutch Management × Vietnamese Mastery applied to insurtech development itself: discovery that correctly identifies where the real project complexity lives, paired with execution depth in legacy system integration specifically. Explore [custom software development](https://www.manifera.com/services/custom-software-development/) for insurtech at Manifera.

## Case Study: A Trieste Insurer's Reframed Claims Project

Adriabroker, a Trieste-based insurance broker, had originally budgeted a claims-portal project as primarily a straightforward UI build, based on a previous vendor's confident estimate that hadn't investigated the underlying legacy policy system in any real detail — an estimate that proved wildly, embarrassingly optimistic once the vendor finally discovered the legacy system's real claims data model well into active development.

Manifera's Amsterdam team ran a two-week legacy-integration discovery phase before quoting the remaining work, identifying the actual, full scope: custom middleware needed to bridge the legacy system's batch-file claims processing with the modern portal's real-time expectations. The Vietnam pod built that middleware alongside the portal, delivering a genuinely working, accurately scoped project instead of a portal stalled indefinitely by an integration nobody had ever properly assessed in the first place.

> *"We'd been sold a claims portal project. What we actually needed was someone willing to say, up front, that the portal was the easy 20% and the legacy integration was the hard 80%."*
> — **CTO, Adriabroker**

Adriabroker's CTO now opens every new project scoping conversation by explicitly asking vendors to describe the iceberg — what's visible in the pitch versus what structural work sits underneath — before allowing any timeline or budget discussion to begin.

## Asking Vendors to Show You the Iceberg, Not Just Its Tip

A practical technique borrowed directly from Meadows' framework: ask a prospective vendor not just what the project will build, but to explicitly separate their answer into "what the user will see" and "what has to be true underneath for that to work reliably." A vendor who has genuinely done discovery can answer the second half specifically — naming the legacy system's actual data model quirks, its integration mechanisms, its embedded business rules — because they've already been below the waterline themselves. A vendor who hasn't done real discovery can typically only answer the first half, describing screens and features fluently while going vague, general, or evasive the moment the conversation moves to what's underneath.

This single technique reliably surfaces the exact gap that cost Adriabroker months on their first attempt: a proposal that sounded complete because it described the visible tip accurately, while the actual project — the much larger structural mass below the surface — had never been examined by anyone before the contract was signed. Applying Meadows' iceberg model this directly and this early in a vendor conversation costs almost nothing and catches almost exactly the failure mode this article describes before any real budget commitment has been made.

## New-App Framing vs. Integration-Reality Framing

| Framing | New-App Framing | Integration-Reality Framing |
|---|---|---|
| Where most effort is assumed to be | The new interface | Legacy system integration |
| Discovery focus | UI/UX requirements | Legacy system data model and business rules |
| Estimate accuracy | Frequently optimistic, integration surfaces mid-project | More accurate, integration complexity scoped upfront |
| Typical outcome without proper scoping | Blown timeline and budget | Realistic, deliverable project plan |

## Scoping Your Next Insurtech Project Honestly

Before quoting or committing to a timeline for any insurtech project, insist on a genuine, legacy-integration-focused discovery phase — the new interface is rarely where the real complexity or risk actually lives. [Talk to Manifera](https://www.manifera.com/contact-us/) about scoping the integration reality of your project.

## Frequently Asked Questions

### (Scenario: insurtech founder scoping a new project) Why did our claims portal estimate turn out to be so far off from the actual timeline?

Most likely because the original estimate focused on the visible interface work and didn't adequately investigate the legacy policy or claims system integration, which is typically the majority of the real engineering effort.

### (Scenario: CTO trying to scope a new insurtech project accurately) What should a discovery phase for an insurtech project actually investigate?

The legacy system's data model, business rules, available integration mechanisms (API, batch file, direct database access), and any undocumented logic embedded in the existing system — not just the requirements for the new customer-facing interface.

### (Scenario: founder trying to understand why legacy integration is so complex) Why is integrating with a legacy insurance system harder than integrating with a modern SaaS API?

Legacy systems often expose data through mechanisms not designed for real-time modern access — batch files, older protocols — and embed business logic in code rather than documentation, requiring reverse-engineering before safe integration is possible.

### (Scenario: CTO evaluating a vendor's insurtech experience) What should I ask a vendor to assess their legacy insurance integration experience specifically?

Ask for a specific example of a legacy system they've integrated with, what integration mechanism it used, and how they handled reconciling data between the legacy system and the new application's data model.

### (Scenario: founder worried about regulatory risk in a new customer-facing layer) How do we make sure a new customer portal doesn't bypass compliance logic the legacy system enforces?

Map the legacy system's compliance-relevant business rules explicitly during discovery, and ensure the new layer either calls through to those rules or faithfully replicates them, rather than assuming the interface layer is compliance-neutral.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "(Scenario: insurtech founder scoping a new project) Why did our claims portal estimate turn out to be so far off from the actual timeline?", "acceptedAnswer": { "@type": "Answer", "text": "Most likely because the original estimate focused on the visible interface and didn't adequately investigate the legacy system integration, typically the majority of the real effort." } },
    { "@type": "Question", "name": "(Scenario: CTO trying to scope a new insurtech project accurately) What should a discovery phase for an insurtech project actually investigate?", "acceptedAnswer": { "@type": "Answer", "text": "The legacy system's data model, business rules, available integration mechanisms, and undocumented logic embedded in the existing system." } },
    { "@type": "Question", "name": "(Scenario: founder trying to understand why legacy integration is so complex) Why is integrating with a legacy insurance system harder than integrating with a modern SaaS API?", "acceptedAnswer": { "@type": "Answer", "text": "Legacy systems often expose data through mechanisms not designed for real-time access and embed business logic in code rather than documentation." } },
    { "@type": "Question", "name": "(Scenario: CTO evaluating a vendor's insurtech experience) What should I ask a vendor to assess their legacy insurance integration experience specifically?", "acceptedAnswer": { "@type": "Answer", "text": "Ask for a specific example of a legacy system they've integrated with and how they handled reconciling data with the new application's data model." } },
    { "@type": "Question", "name": "(Scenario: founder worried about regulatory risk in a new customer-facing layer) How do we make sure a new customer portal doesn't bypass compliance logic the legacy system enforces?", "acceptedAnswer": { "@type": "Answer", "text": "Map the legacy system's compliance-relevant business rules explicitly during discovery, and ensure the new layer calls through to or faithfully replicates them." } }
  ]
}
</script>
