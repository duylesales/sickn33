---
title: "The English-Only Codebase: Why Market Expansion Costs Ten Times More Than It Should Have"
keywords: "custom software development company, offshore software development company, software architecture, internationalization"
buyer_stage: "Consideration"
target_persona: "CEO"
---

# The English-Only Codebase: Why Market Expansion Costs Ten Times More Than It Should Have

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "The English-Only Codebase: Why Market Expansion Costs Ten Times More Than It Should Have",
  "description": "A CEO's guide to why a codebase built without internationalization from day one turns a straightforward market-expansion decision into a multi-quarter engineering retrofit.",
  "author": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com/" },
  "datePublished": "2026-08-20",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://www.manifera.com/blog/internationalization-retrofit-market-expansion-cost" }
}
</script>

The board approved German market entry as a two-quarter initiative. Engineering discovered, three weeks in, that every user-facing string in the application was hardcoded directly into component templates, with no translation infrastructure anywhere in the codebase — the two-quarter plan quietly became a four-quarter plan before a single German user ever saw the product.

**The Pain:** A CEO greenlit expansion into a new market based on a commercial timeline — sales pipeline, localized marketing, a launch date communicated to the board — without engineering having flagged that the product was never built with internationalization in mind. Every date format, currency display, pluralization rule, and user-facing string is hardcoded in English throughout the codebase, because internationalization was never on a roadmap when the company only operated in one market and nobody thought to build for a future that wasn't yet funded.

**The Agitation:** Retrofitting internationalization into a codebase that was never designed for it is dramatically more expensive and slower than building it in from the start, because every hardcoded string, every date-formatting assumption, and every currency-display shortcut has to be found and fixed individually across the entire application — a search-and-rework exercise that scales with the size of the codebase, not with the complexity of the target market. A CEO who committed to a market-entry timeline based on the commercial plan alone, without validating the technical retrofit cost, discovers the real timeline only after the board commitment is already public.

## The Internationalization Retrofit Mandate

The first mandate is a full internationalization audit before committing to any market-entry timeline publicly — a systematic scan of the codebase for hardcoded strings, date and number formatting assumptions, currency handling, and pluralization logic, producing an honest estimate of retrofit scope before a date gets attached to a board slide.

The second mandate is migrating to a proper internationalization framework — externalizing every user-facing string into translation resource files, replacing hardcoded date and currency formatting with locale-aware libraries — as a foundational infrastructure project, not a per-feature patch applied inconsistently as new markets get added one at a time.

The third mandate is treating internationalization infrastructure as reusable investment, not a one-market cost — once the framework is properly in place, adding a third and fourth market becomes materially cheaper than the first retrofit, because the hard architectural work is already done and subsequent markets are primarily translation and locale-specific business-rule work, not another engineering excavation through the codebase.

The fourth mandate is separating the commercial timeline from the technical timeline explicitly in board communication going forward — a market-entry date should be set only after engineering has validated the retrofit scope, not before, so the company never again finds itself explaining to a board why a committed date needs to move because of a technical discovery that should have been made before the commitment.

## The Hybrid Hub: How Manifera Executes This

- **Amsterdam (Governance/Strategy):** Dutch architects run the internationalization audit and translate the findings into a realistic timeline the CEO can commit to publicly, before any date reaches a board slide.
- **Vietnam (Execution/Velocity):** Autonomous pods in Vietnam execute the internationalization migration — externalizing strings, implementing locale-aware formatting, building the reusable framework that makes every subsequent market cheaper than the first.

This is Dutch Management × Vietnamese Mastery: European commercial-technical alignment that prevents a market-entry date from being set before the retrofit cost is known, paired with execution capacity that builds internationalization as reusable infrastructure, not a one-off patch. Learn more about [Manifera's custom software development](https://www.manifera.com/services/custom-software-development/) and how a properly scoped internationalization foundation makes every future market expansion faster than the last.

## Case Study & Testimonial

### A Stockholm SaaS Company's German Launch Discovery

Nordisk Affärsplattform AB, a Stockholm-based B2B SaaS company, had announced a German market launch to its board as a two-quarter initiative, only to discover during technical scoping that the entire application had hardcoded English strings, US-style date formatting, and no currency-locale handling anywhere in the codebase — a retrofit that would genuinely require closer to five months of dedicated engineering work before a single translated screen could ship.

Manifera conducted the internationalization audit within two weeks, then executed the full migration to a proper i18n framework — externalized strings, locale-aware date and currency formatting, and a translation-management workflow — over fourteen weeks. The CEO was able to communicate a revised, accurate timeline to the board early enough to manage expectations, and the company's subsequent French market entry, using the now-reusable i18n infrastructure, took six weeks rather than the original German retrofit's fourteen.

> *"The German launch date moved, and that was an uncomfortable board conversation. But it was one honest conversation instead of a missed deadline nobody saw coming — and by the time France came around, the hard part was already built."*
> — **CEO, Nordisk Affärsplattform AB, Sweden**

## Hardcoded English Codebase vs. Manifera's Reusable I18n Foundation

| Criteria | Hardcoded English Codebase | Manifera's Reusable I18n Foundation |
|---|---|---|
| First market-expansion cost | High, full codebase retrofit required | High but one-time, absorbed into foundational build |
| Subsequent market cost | Same high cost repeated per market | Dramatically lower, primarily translation work |
| Timeline predictability | Discovered mid-project, disrupts commitments | Assessed upfront, before any date is committed |
| String and format handling | Scattered, hardcoded throughout the app | Centralized, locale-aware, systematically managed |
| Board communication risk | Technical surprise undermines commercial timeline | Aligned before any public commitment is made |

## The Economics

Retrofitting internationalization into a codebase never built for it typically costs €70,000-€130,000 and four to six months for the first market, largely because the work is a discovery-and-rework exercise across the entire application rather than a contained project. Once that foundational investment is made properly, each subsequent market typically costs a fraction of that — often 20-30% — because the framework, not the codebase, does the heavy lifting going forward. The real cost of skipping the audit isn't just the retrofit itself, but the board credibility cost of a publicly committed date moving because of a technical discovery that should have been made before the commitment. [Talk to Manifera](https://www.manifera.com/contact-us/) about auditing your internationalization readiness before the next market-entry date reaches a board slide.

## Frequently Asked Questions

### (Scenario: CEO who committed to a market-entry date before an i18n audit) How do we avoid committing to a market-entry timeline that engineering later has to walk back?

Run a full internationalization audit before any date is communicated publicly or to the board — the audit typically takes one to two weeks and gives an honest basis for a commercial timeline, rather than discovering the real scope mid-project.

### (Scenario: CEO trying to understand why the retrofit is so much more expensive than expected) Why is retrofitting internationalization so much more expensive than building it in from the start?

Because every hardcoded string, date format, and currency assumption has to be found and fixed individually across the entire existing codebase, a search-and-rework exercise that scales with codebase size rather than being handled once during initial architecture.

### (Scenario: CEO planning multiple future market expansions) Does the internationalization investment pay off across multiple future markets, or is it a one-time cost per market?

It's genuinely reusable investment — once the framework is properly built, subsequent markets are primarily translation and locale-specific business-rule work, typically costing a fraction of the first market's retrofit cost.

### (Scenario: CEO trying to align commercial and engineering timelines going forward) How should commercial and technical timelines be aligned for future market-entry decisions?

Commit to a public market-entry date only after engineering has validated the technical scope, not before, so commercial planning and technical reality are never in conflict by the time a date is public.

### (Scenario: CEO trying to estimate the cost of an internationalization retrofit) What does a typical internationalization retrofit cost and take for the first target market?

For a mid-complexity application, typically €70,000-€130,000 and four to six months, with each subsequent market costing significantly less once the reusable framework is in place.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "(Scenario: CEO who committed to a market-entry date before an i18n audit) How do we avoid committing to a market-entry timeline that engineering later has to walk back?", "acceptedAnswer": { "@type": "Answer", "text": "Run a full internationalization audit before any date is communicated publicly, typically one to two weeks, giving an honest basis for the commercial timeline." } },
    { "@type": "Question", "name": "(Scenario: CEO trying to understand why the retrofit is so much more expensive than expected) Why is retrofitting internationalization so much more expensive than building it in from the start?", "acceptedAnswer": { "@type": "Answer", "text": "Every hardcoded string and format assumption has to be found and fixed individually across the entire existing codebase, a search-and-rework exercise scaling with codebase size." } },
    { "@type": "Question", "name": "(Scenario: CEO planning multiple future market expansions) Does the internationalization investment pay off across multiple future markets, or is it a one-time cost per market?", "acceptedAnswer": { "@type": "Answer", "text": "It's reusable investment. Once the framework is built, subsequent markets are primarily translation work, costing a fraction of the first market's retrofit." } },
    { "@type": "Question", "name": "(Scenario: CEO trying to align commercial and engineering timelines going forward) How should commercial and technical timelines be aligned for future market-entry decisions?", "acceptedAnswer": { "@type": "Answer", "text": "Commit to a public market-entry date only after engineering has validated the technical scope, not before." } },
    { "@type": "Question", "name": "(Scenario: CEO trying to estimate the cost of an internationalization retrofit) What does a typical internationalization retrofit cost and take for the first target market?", "acceptedAnswer": { "@type": "Answer", "text": "Typically €70,000-€130,000 and four to six months, with each subsequent market costing significantly less." } }
  ]
}
</script>
