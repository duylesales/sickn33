---
title: "Design Systems Development: Why 'We'll Build It Later' Never Actually Happens"
keywords: "design systems development, building a design system, component library development"
buyer_stage: "Consideration"
target_persona: "CTO"
---

# Design Systems Development: Why "We'll Build It Later" Never Actually Happens

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Design Systems Development: Why 'We'll Build It Later' Never Actually Happens",
  "description": "A CTO's guide to why design systems development keeps getting deprioritized, the real cost of skipping it, and what a component library actually needs to include to pay for itself.",
  "author": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com/" },
  "datePublished": "2026-08-20",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://www.manifera.com/blog/design-systems-development" }
}
</script>

Every CTO has said "we'll formalize the design system once things calm down," and the honest truth is that things never calm down — feature pressure is permanent, and a design system built under permanent feature pressure gets built the same way technical debt does: not at all, until the inconsistency and duplicated component work become expensive enough that someone finally blocks a sprint to fix it.

**The Pain:** A CTO overseeing multiple product squads typically discovers, usually by accident, that three different teams have each independently built their own version of a date picker, a modal, or a form input, each with slightly different behavior, accessibility handling, and visual treatment, because no shared, enforced component library existed to make reuse the easier path than rebuilding from scratch.

**The Agitation:** Duplicated UI component work is rarely visible as a single line item, but it accumulates — engineering teams without a design system commonly spend a meaningful double-digit percentage of front-end development time rebuilding components that already exist elsewhere in the codebase, and every duplicated component is also a duplicated accessibility bug, a duplicated inconsistency for users to relearn, and a duplicated maintenance burden the next time a design change needs to propagate.

## What a Design System Needs to Actually Include to Pay for Itself

**A component library with defined states, not just visual specs.** A design system that stops at a Figma file of static screens doesn't reduce engineering rework; a design system that ships a coded component library — with every interactive state, loading state, and error state implemented once — is what actually lets engineers reuse rather than rebuild.

**Accessibility built into the component, not bolted on per-use.** Keyboard navigation, screen-reader labeling, and focus management implemented correctly once in a shared component is dramatically cheaper than fixing the same accessibility gap independently in every team's custom-built version of that component, and it's the difference between a compliant product and a liability discovered during an audit.

**Design tokens that make rebranding a configuration change.** Colors, spacing, and typography expressed as tokens rather than hardcoded values mean a visual refresh becomes a token update propagated automatically, instead of a manual find-and-replace project across every screen in the product.

**Governance that makes the shared library the path of least resistance.** A design system that exists but isn't enforced gets bypassed the first time a deadline is tight; a design system with lightweight governance — a clear contribution process, a design-and-engineering review for new components, visibility into what already exists — stays the default choice because using it is genuinely faster than not using it.

**Versioning and adoption tracking across teams.** A component library that ships silent breaking changes erodes trust fast; proper semantic versioning, a migration path, and visibility into which teams are on which version is what lets a design system scale across more than a handful of squads without becoming its own coordination problem.

A CTO evaluating whether to invest in design systems development should treat it the same as any shared infrastructure investment — the payoff isn't visible in any single sprint, but it compounds every quarter afterward as more teams and more screens draw from the same well instead of digging their own.

## The Hybrid Hub: How Manifera Executes This

- **Amsterdam (Governance/Strategy):** Dutch leads define the token architecture, accessibility standards, and lightweight governance model that keep a design system the path of least resistance rather than a bypassed artifact.
- **Vietnam (Execution/Velocity):** Autonomous pods in Ho Chi Minh City build and maintain the coded component library at the pace needed to keep it ahead of product teams' feature demands, not trailing behind them.

This is Dutch Management × Vietnamese Mastery: disciplined governance that keeps a design system enforced and coherent, paired with execution capacity that builds it fast enough to actually get adopted. Learn more about [Manifera's custom software development](https://www.manifera.com/services/custom-software-development/) and how a properly built design system turns duplicated UI work into shared, reusable infrastructure.

## Case Study & Testimonial

### A Valencia SaaS Company's Component Sprawl

Software Horizontal Valencia SL, a Valencia-based vertical SaaS provider, had grown to six product squads, each maintaining its own slightly different button, form, and modal components, resulting in visible inconsistency across the product and an estimated quarter of front-end sprint capacity spent rebuilding UI elements that already existed somewhere in the codebase.

Manifera built a coded component library with token-based theming and accessibility handling baked into each component, alongside a lightweight contribution and review process that made the shared library faster to use than building custom. Within two quarters, duplicated component work across the six squads had dropped to a small fraction of its previous level, freeing meaningful front-end capacity for actual feature work.

> *"Every squad had its own modal, and none of them behaved quite the same way. Once the shared library was actually faster to use than building your own, adoption wasn't a mandate — it just happened."*
> — **CTO, Software Horizontal Valencia SL, Spain**

## Per-Team Component Building vs. Manifera's Shared Design System

| Criteria | Per-Team Component Building | Manifera's Shared Design System |
|---|---|---|
| Component consistency | Varies by team, visibly inconsistent | Uniform across every product surface |
| Accessibility handling | Re-solved per team, inconsistently | Built once, correctly, into each component |
| Rebranding effort | Manual find-and-replace project | Token update propagated automatically |
| Engineering time on UI | Meaningful share spent rebuilding | Redirected to feature work |
| Adoption | Depends on individual team discipline | Default path via lightweight governance |

## The Economics

A coded design system with proper token architecture and governance typically takes eight to sixteen weeks to establish for a mid-sized product organization, and pays for itself by reclaiming the double-digit percentage of front-end capacity commonly lost to duplicated component work — capacity that compounds as more squads and more screens are added. The investment scales with the organization; the waste it prevents scales faster. [Talk to Manifera](https://www.manifera.com/contact-us/) about design systems development that actually gets adopted.

## Frequently Asked Questions

### (Scenario: CTO discovering multiple teams built the same component independently) Why do multiple teams end up building the same UI component independently?

Because without a shared, enforced component library, rebuilding from scratch is often faster in the moment than discovering and adapting whatever another team already built.

### (Scenario: CTO deciding what a design system needs beyond visual specs) Why isn't a Figma file of screens enough to count as a design system?

Because static visual specs don't reduce engineering rework — only a coded component library with implemented states actually lets engineers reuse rather than rebuild.

### (Scenario: CTO concerned about accessibility compliance across teams) How does a design system reduce accessibility risk?

By implementing keyboard navigation, labeling, and focus management correctly once in each shared component, instead of each team re-solving it inconsistently.

### (Scenario: CTO worried a design system won't actually get adopted) What makes teams actually adopt a shared design system instead of bypassing it?

Lightweight governance and a component library that's genuinely faster to use than building custom, not a mandate alone.

### (Scenario: CTO estimating the timeline for building a design system) How long does it typically take to build a coded design system for a mid-sized product organization?

Roughly eight to sixteen weeks to establish token architecture, core components, and governance.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "(Scenario: CTO discovering multiple teams built the same component independently) Why do multiple teams end up building the same UI component independently?", "acceptedAnswer": { "@type": "Answer", "text": "Without a shared, enforced library, rebuilding from scratch is often faster than discovering and adapting an existing version." } },
    { "@type": "Question", "name": "(Scenario: CTO deciding what a design system needs beyond visual specs) Why isn't a Figma file of screens enough to count as a design system?", "acceptedAnswer": { "@type": "Answer", "text": "Static visual specs don't reduce rework — only a coded component library with implemented states does." } },
    { "@type": "Question", "name": "(Scenario: CTO concerned about accessibility compliance across teams) How does a design system reduce accessibility risk?", "acceptedAnswer": { "@type": "Answer", "text": "By implementing accessibility correctly once per shared component instead of each team re-solving it inconsistently." } },
    { "@type": "Question", "name": "(Scenario: CTO worried a design system won't actually get adopted) What makes teams actually adopt a shared design system instead of bypassing it?", "acceptedAnswer": { "@type": "Answer", "text": "Lightweight governance and a library that's genuinely faster to use than building custom." } },
    { "@type": "Question", "name": "(Scenario: CTO estimating the timeline for building a design system) How long does it typically take to build a coded design system for a mid-sized organization?", "acceptedAnswer": { "@type": "Answer", "text": "Roughly eight to sixteen weeks to establish tokens, core components, and governance." } }
  ]
}
</script>
