---
title: "Business Intelligence Platform Migration: Vendor Selection Criteria"
keywords: "BI platform migration vendor, business intelligence vendor selection, BI tool migration due diligence, analytics platform migration vendor comparison, BI vendor decision criteria"
buyer_stage: "Decision"
target_persona: "IT Manager"
---

# Business Intelligence Platform Migration: Vendor Selection Criteria

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Business Intelligence Platform Migration: Vendor Selection Criteria",
  "description": "An IT Manager's checklist for choosing a BI platform migration vendor, covering semantic layer conversion, dashboard re-platforming effort, and the retraining cost most migration plans ignore.",
  "author": {"@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com/"},
  "publisher": {"@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com/"},
  "datePublished": "2026-09-13",
  "mainEntityOfPage": {"@type": "WebPage", "@id": "https://www.manifera.com/blog/business-intelligence-platform-migration-vendor-selection-criteria"}
}
</script>

340 dashboards. That's what an IT Manager at a mid-size insurer inherited an inventory of when leadership decided to sunset an aging Cognos environment in favor of Power BI. The vendor's initial proposal quoted the migration primarily on a per-dashboard basis, as if converting a dashboard were a mechanical, uniform task. It isn't. Roughly sixty of those 340 dashboards turned out to depend on complex Cognos Framework Manager semantic model logic — calculated measures, security filters, and multi-fact-table joins — that had no direct one-to-one equivalent in Power BI's data model and needed to be rebuilt conceptually, not just recreated visually. The other 280 were comparatively simple and converted in a fraction of the time the complex ones took. A flat per-dashboard quote hides this variance entirely, and it's the single most common way BI migration budgets blow up.

Choosing a vendor for a BI platform migration — Tableau, QlikView, or Cognos to Power BI, Looker, or ThoughtSpot, or any similar move — requires evaluating the vendor's approach to semantic layer conversion specifically, not just their familiarity with the destination platform's visual dashboard builder.

## The Semantic Layer Is the Migration's Real Complexity

Every mature BI platform has a semantic layer — Cognos Framework Manager, Tableau's data source layer, Power BI's data model with DAX measures, Looker's LookML — that defines how raw tables relate to each other, what business calculations mean (how "active customer" or "gross margin" is actually computed), and who's allowed to see what data through row-level security filters. Migrating dashboards without properly migrating the underlying semantic logic produces dashboards that look identical to the old ones but calculate numbers differently — which is far more dangerous than dashboards that are obviously broken, because incorrect-but-plausible numbers can drive real business decisions before anyone notices the discrepancy.

Ask any migration vendor specifically how they handle semantic layer conversion: do they rebuild calculated measures from the source platform's actual logic definitions, or do they reverse-engineer expected behavior from looking at the rendered dashboard output? The former is slower and more rigorous; the latter is faster but risks silently changing business logic in ways that won't surface until someone notices a number doesn't match what finance expects. For any dashboard feeding a regulatory report or a board-level metric, insist on the rigorous approach and a documented mapping from old calculation logic to new.

## Complexity-Weighted Dashboard Inventory, Not Flat Per-Dashboard Pricing

Before accepting any vendor quote, insist on a dashboard complexity audit as a distinct, priced phase separate from the migration execution itself. This audit should classify every dashboard by real complexity indicators: number of underlying data sources and whether they involve multi-fact-table joins, presence of custom calculated measures beyond simple aggregations, row-level security requirements, and whether the dashboard is standalone or embedded in another application (embedded analytics carry their own licensing and API integration considerations).

A vendor who quotes migration cost before this audit is guessing, the same way an ERP vendor guessing at data migration cost before profiling production data is guessing. Insist the complexity audit happens and gets priced separately, with the migration execution quote following from its findings — a vendor confident in their process will welcome this sequencing because it protects them from underbidding as much as it protects you from a change-order surprise midway through.

## DAX, LookML, and the Skill Gap Nobody Budgets For

Migrating between platforms usually means migrating between fundamentally different calculation languages — Cognos's macro-based calculation language or Tableau's calculated field syntax converting to Power BI's DAX, or to LookML if the destination is Looker. These languages aren't directly translatable one-to-one; DAX in particular has row-context and filter-context evaluation semantics that behave differently from how calculations work in Tableau or Cognos, which means a literal syntax translation can produce a formula that runs without error but returns a subtly wrong number under certain filter combinations.

Ask the vendor directly what proportion of their migration team has production DAX (or LookML, depending on your destination platform) expertise specifically, versus general BI platform familiarity — these are genuinely different skill sets, and a vendor staffed primarily with generalist BI consultants unfamiliar with DAX's evaluation context model will produce calculations that pass a superficial visual check and fail under edge-case filtering.

## User Retraining Cost Is Part of the Migration, Not an Afterthought

BI platform migration isn't just a technical conversion — it changes how every dashboard consumer interacts with the tool, and for organizations with hundreds of report authors and thousands of dashboard viewers, retraining cost is a real, budgetable line item that gets left out of most vendor proposals entirely. Ask vendors whether their scope includes user training and change management, or purely the technical migration — and if it's purely technical, budget separately and realistically for retraining self-service report authors on the new platform's paradigm, which can differ substantially even between visually similar tools.

A realistic retraining plan segments users by need: dashboard viewers typically need minimal retraining (the consumption experience is broadly similar across platforms), while self-service report authors who build their own analyses need substantive retraining on the destination platform's specific modeling and calculation approach, and this second group is where underestimated retraining cost most commonly surfaces as a post-migration productivity dip.

## Embedded Analytics and Licensing Model Shifts

If any of the 340 (or however many) dashboards are embedded in customer-facing or partner-facing applications rather than consumed internally, the migration carries additional licensing and API considerations — embedded analytics licensing models differ substantially between platforms (per-viewer, capacity-based, or embedded-specific SKUs), and the API used to embed dashboards programmatically is platform-specific, meaning embedded integrations need actual re-engineering, not just a dashboard recreation. Inventory embedded use cases separately and get a vendor's specific plan for each one, since this is commonly the most underestimated category in BI migration scoping.

## Making the BI Migration Call

A BI platform migration vendor worth trusting will insist on a complexity-weighted dashboard audit before quoting a firm price, treat semantic layer and calculation logic conversion as the real technical core of the project rather than an afterthought to visual recreation, and address user retraining and embedded analytics as explicit, budgeted scope items rather than gaps discovered mid-project.

Manifera helps IT teams scope and execute BI platform migrations with semantic layer conversion handled as rigorously as the visual migration — see our [custom software development](https://www.manifera.com/services/custom-software-development/) and [web app development](https://www.manifera.com/services/web-app-develop/) capabilities, and our approach to complex technical migrations detailed in [our way of working](https://www.manifera.com/about-us/our-way-of-working/). If you're scoping a BI platform migration and want a complexity-weighted second opinion before signing a vendor contract, [reach out](https://www.manifera.com/contact-us/).

## Frequently Asked Questions

### Why is flat per-dashboard pricing risky for a BI migration quote?
Dashboard complexity varies enormously — dashboards with simple aggregations convert quickly, while those with complex semantic model logic, multi-fact-table joins, or row-level security can take many times longer. A flat per-dashboard quote hides this variance and is a common cause of BI migration budget overruns.

### What's the risk of reverse-engineering calculated measures from a dashboard's visual output instead of its underlying logic?
It can produce a dashboard that looks correct but calculates numbers differently than the original system, especially under edge-case filter combinations. These incorrect-but-plausible numbers are more dangerous than an obviously broken dashboard because they can drive decisions before anyone notices the discrepancy.

### Do we need DAX or LookML specialists specifically, or is general BI platform experience enough?
Specialists matter here because these calculation languages have evaluation semantics — like DAX's row-context and filter-context behavior — that don't map one-to-one from other platforms' calculation syntax. A literal syntax translation can run without error yet return a subtly wrong result.

### Should user retraining be included in the BI migration vendor's scope?
It should at minimum be explicitly addressed, whether the vendor handles it directly or you budget for it separately. Self-service report authors need substantive retraining on the destination platform's modeling approach, and skipping this is a common source of post-migration productivity loss.

### How should embedded analytics dashboards be scoped differently from internal dashboards during migration?
Embedded dashboards require re-engineering the embedding integration itself, since the API used to embed dashboards programmatically is platform-specific, and licensing models for embedded use (per-viewer, capacity-based) differ from standard internal licensing. Inventory and scope these separately from internally consumed dashboards.
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Why is flat per-dashboard pricing risky for a BI migration quote?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Dashboard complexity varies enormously — dashboards with simple aggregations convert quickly, while those with complex semantic model logic, multi-fact-table joins, or row-level security can take many times longer. A flat per-dashboard quote hides this variance and is a common cause of BI migration budget overruns."
      }
    },
    {
      "@type": "Question",
      "name": "What's the risk of reverse-engineering calculated measures from a dashboard's visual output instead of its underlying logic?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "It can produce a dashboard that looks correct but calculates numbers differently than the original system, especially under edge-case filter combinations. These incorrect-but-plausible numbers are more dangerous than an obviously broken dashboard because they can drive decisions before anyone notices the discrepancy."
      }
    },
    {
      "@type": "Question",
      "name": "Do we need DAX or LookML specialists specifically, or is general BI platform experience enough?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Specialists matter here because these calculation languages have evaluation semantics — like DAX's row-context and filter-context behavior — that don't map one-to-one from other platforms' calculation syntax. A literal syntax translation can run without error yet return a subtly wrong result."
      }
    },
    {
      "@type": "Question",
      "name": "Should user retraining be included in the BI migration vendor's scope?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "It should at minimum be explicitly addressed, whether the vendor handles it directly or you budget for it separately. Self-service report authors need substantive retraining on the destination platform's modeling approach, and skipping this is a common source of post-migration productivity loss."
      }
    },
    {
      "@type": "Question",
      "name": "How should embedded analytics dashboards be scoped differently from internal dashboards during migration?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Embedded dashboards require re-engineering the embedding integration itself, since the API used to embed dashboards programmatically is platform-specific, and licensing models for embedded use (per-viewer, capacity-based) differ from standard internal licensing. Inventory and scope these separately from internally consumed dashboards."
      }
    }
  ]
}
</script>
