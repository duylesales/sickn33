---
title: "Design-Development Handoff: Vendor Questions That Prevent Rework"
keywords: "design to development handoff, design tokens, Figma Dev Mode, design system documentation, UX vendor engineering rework, redline specs"
buyer_stage: "Decision"
target_persona: "CTO"
---

# Design-Development Handoff: Vendor Questions That Prevent Rework

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Design-Development Handoff: Vendor Questions That Prevent Rework",
  "description": "A CTO's checklist of questions to ask a UX vendor before signing, covering design tokens, component specs, breakpoint documentation, accessibility annotations, and edge-case coverage that prevents late-stage engineering rework.",
  "author": {"@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com/"},
  "publisher": {"@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com/"},
  "datePublished": "2026-08-18",
  "mainEntityOfPage": {"@type": "WebPage", "@id": "https://www.manifera.com/blog/design-development-handoff-vendor-questions-that-prevent-rework"}
}
</script>

Your engineering team gets a Figma link two weeks before the sprint starts. It has forty polished screens, no documented spacing scale, no defined states beyond the happy path, and a Slack message that says "let us know if you have questions." Six weeks later, three sprints have gone to rebuilding components that don't match across screens, nobody agreed on what the error state looks like, and the design vendor's contract has already ended. This is not a hypothetical — it is the single most common failure mode in outsourced UX engagements, and it is almost entirely preventable with the right questions asked before the contract is signed.

For a CTO, the handoff moment is where design cost quietly becomes engineering cost. A vendor who charges €15,000 less for the design phase but hands off unstructured screens can easily cost your team three to four extra sprints of rework, at a fully loaded cost that dwarfs the original savings. This decision matters because handoff quality is almost entirely predictable in advance — it shows up in how a vendor answers a short set of concrete questions, not in how polished their final screens look. The questions below are the ones that separate a vendor who understands engineering handoff from one who has only ever designed for other designers.

## Where Handoff Breaks: The Hidden Cost of "Just Send the Figma File"

The core problem is that a Figma file, by itself, is a design artifact, not a specification. It shows you what one state of one screen looks like at one breakpoint. It does not tell an engineer what the spacing scale is, whether a value is a one-off or part of a system, what happens when the content is twice as long as the placeholder text, or what the component looks like when it's loading, empty, or in an error state. Engineering teams that receive only screens end up reverse-engineering the design system from pixel measurements — eyeballing whether a margin is 16px or 18px, guessing whether a slightly different shade of gray on two screens was intentional or an oversight. Every one of those guesses is a potential rework ticket three sprints later when a designer notices the inconsistency in QA. The fix isn't asking vendors to work harder; it's asking, before signing, exactly what handoff artifacts are included in the deliverable and getting a specific, itemized answer rather than "full specs, of course."

## Design Tokens: The Single Question That Predicts Rework

Ask directly: do you define and deliver design tokens, and in what format? Design tokens — named, structured values for color, spacing, typography, radius, and elevation, typically stored as JSON or delivered via Figma variables — are the difference between a design system that scales and one that has to be manually kept in sync forever. A vendor who works in tokens can hand off a file where `color.background.danger` and `spacing.md` are named, versioned values that map directly onto variables in your codebase, whether you're using CSS custom properties, a Tailwind config, or a Style Dictionary pipeline. A vendor who works purely in hardcoded hex values and pixel measurements is handing you a snapshot, not a system — every future design change means someone manually re-measuring and re-implementing rather than updating a token value that propagates. This single question, asked directly in a vendor call, reliably separates design system-literate teams from portfolio-driven ones.

## Component Library and Design System Specs

Screens are compositions of components, and if the vendor hasn't documented the components themselves — states, variants, and composition rules — your engineering team will build one-off implementations per screen instead of a reusable library. Ask specifically whether the deliverable includes a documented component library: every button variant and its states (default, hover, active, disabled, loading), every form field with its validation states, and explicit rules for how components compose (does a card always contain a specific header pattern, or is that ad hoc per screen). A vendor delivering true design system specs will show you a Figma component library with organized variants, not a page of screens where each button was drawn separately with slightly different padding. This is the deliverable that determines whether your frontend team builds ten reusable components or forty near-duplicate ones.

## Responsive and Breakpoint Documentation

Most design handoffs show one desktop frame and one mobile frame per screen, with no documentation of what happens in between, or how specific elements behave at intermediate widths. Ask the vendor how they document responsive behavior: do they define explicit breakpoints (commonly 375px, 768px, 1024px, 1440px, or a project-specific scale), and for each breakpoint, do they specify layout changes, not just show a static frame? The critical follow-up question is about reflow logic — does a three-column grid become two columns then one, and at what exact width does each transition happen? Vendors without a real answer will have engineers making these calls ad hoc during implementation, guessing at intent, and getting overridden by the vendor's designer in a late review cycle after the component is already built.

## Accessibility Annotations Aren't Optional Anymore

WCAG 2.2 AA compliance is increasingly a contractual and, in regulated sectors and public-facing EU services, a legal requirement under the European Accessibility Act, which reaches full enforcement in June 2025 for a wide range of digital products and services sold in the EU. Ask whether the vendor provides accessibility annotations alongside the visual design: documented focus order, ARIA roles and labels for custom components, color contrast ratios verified against WCAG 2.2 thresholds (4.5:1 for normal text, 3:1 for large text and UI components), and keyboard interaction patterns for anything beyond standard form elements. A vendor who treats accessibility as something engineering "handles during implementation" is pushing a substantial amount of design decision-making — and rework risk — downstream to your team, at the exact point in the process where it's most expensive to fix.

## Redline Tools: Figma Dev Mode vs. Zeplin vs. Nothing

Ask which tool the vendor uses for developer handoff specifically, and get a live demo, not a description. Figma's Dev Mode (built into modern Figma workspaces) lets engineers inspect exact spacing, generate CSS/iOS/Android code snippets, and see linked component variants directly from the design file — but only if the vendor has actually structured the file with auto layout and named layers, not a flat canvas of ungrouped shapes. Zeplin remains a strong option for teams wanting a dedicated handoff layer separate from the working design file, with explicit redlines and asset export baked in. The red flag is a vendor with no defined handoff tool at all, relying on engineers to eyeball a static Figma file or, worse, exported PNGs. Ask to see a sample handoff file from a past project in Dev Mode or Zeplin directly during the vendor evaluation call — this single fifteen-minute demo tells you more about rework risk than any slide in their deck.

## Edge Cases: Empty, Error, and Loading States That Sink Timelines

The gap between a design that looks finished and a design that is actually implementable almost always lives in the states nobody designs by default: what does this screen look like with zero data (empty state), what does it look like when the API call fails (error state), what does it look like while data is loading (loading state, and is it a skeleton, a spinner, or a progressive reveal), and what happens with unusually long or short content (text overflow, truncation rules). These states are typically 30-40% of the actual screens an engineering team needs but are the first thing cut when a design vendor is running behind schedule, because they don't showcase well in a portfolio. Ask explicitly, screen by screen if necessary, whether empty, error, and loading states are included in the contracted deliverable, and get it written into the scope of work rather than assumed. This is the single most common source of late-stage "wait, what should this actually look like" Slack threads that stall a sprint.

## Getting Handoff Scope Into the Contract, Not Just the Kickoff Deck

Every vendor sounds cooperative in a kickoff meeting. The commitments that hold up are the ones written into the statement of work with specific artifacts named, not the ones described verbally as "close collaboration." Before signing, ask the vendor to itemize the handoff deliverable in the contract: number and format of screens including edge-case states, whether design tokens are included and in what format, which handoff tool will be used and at what fidelity, and what happens if engineering finds a gap during implementation — is there a defined support window, or does every clarification become a new billable request once the contract officially ends. Vendors confident in their handoff process rarely object to this level of specificity; the ones who push back or want to keep the scope of work vague are often the ones planning to under-deliver on exactly this part of the engagement, because it's the least visible line item in a sales pitch and the most expensive one to skip.

## Making the Final Call

No vendor question list eliminates handoff friction entirely — even excellent design teams miss edge cases, and even strong engineering teams occasionally over-interpret ambiguity as a problem rather than a reasonable judgment call. The goal of asking these questions before signing isn't a perfect handoff; it's making the scope of the handoff artifact explicit and contractual, so gaps get caught in a kickoff conversation rather than discovered mid-sprint. A vendor who answers all six questions above fluently and can demo their handoff process live is worth a premium over one who answers with "don't worry, we'll figure it out together" — that sentence is where rework budgets go to die.

Manifera pairs design and engineering under one roof specifically to close this gap, so the team handing off tokens and specs is accountable to the same delivery timeline as the team building against them. If your next project needs a partner who treats handoff as a deliverable, not an afterthought, [our web app development team](https://www.manifera.com/services/web-app-develop/) is a good place to start that conversation.

## Frequently Asked Questions

### What are design tokens, and why do they matter for engineering handoff?
Design tokens are named, structured values for color, spacing, typography, and other visual properties — stored as JSON or Figma variables — that map directly onto variables in your codebase. Without tokens, engineers work from hardcoded pixel and hex values, which makes future design changes require manual re-implementation across every screen rather than a single updated value.

### Should we insist on Figma Dev Mode, or is Zeplin an acceptable alternative?
Either is acceptable as long as the vendor uses one consistently and the file is structured properly — auto layout, named layers, organized components — since a badly structured file breaks Dev Mode's inspection features regardless of the tool. Ask for a live demo of a past handoff file during the vendor evaluation call rather than accepting a description of their process.

### How much of a typical screen count should be empty, error, and loading states?
Edge-case states (empty, error, loading, and content-overflow variants) typically account for 30% to 40% of the actual screens an engineering team needs to implement a feature completely, even though they're often absent from a vendor's initial deliverable. Get these explicitly scoped into the contract rather than assumed as included.

### Why does accessibility need to be specified at the design stage rather than left to engineering?
Accessibility decisions — focus order, ARIA roles for custom components, keyboard interaction patterns, color contrast — are structural to a component's design, not surface-level additions engineers can bolt on afterward. Leaving them undocumented at handoff means engineering either guesses at intent or the component gets rebuilt later once a compliance review catches the gap, both of which are more expensive than specifying it upfront.

### What's a reasonable red flag if a vendor can't answer these handoff questions clearly?
A vendor who responds to specific handoff questions with reassurance rather than concrete process ("don't worry, we'll work closely with your team") rather than naming a tool, format, or documented artifact is signaling that handoff has not historically been a structured part of their delivery. That gap reliably shows up as rework cost on your engineering team's timeline, not theirs.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {"@type": "Question", "name": "What are design tokens, and why do they matter for engineering handoff?", "acceptedAnswer": {"@type": "Answer", "text": "Design tokens are named, structured values for color, spacing, typography, and other visual properties — stored as JSON or Figma variables — that map directly onto variables in your codebase. Without tokens, engineers work from hardcoded pixel and hex values, which makes future design changes require manual re-implementation across every screen rather than a single updated value."}},
    {"@type": "Question", "name": "Should we insist on Figma Dev Mode, or is Zeplin an acceptable alternative?", "acceptedAnswer": {"@type": "Answer", "text": "Either is acceptable as long as the vendor uses one consistently and the file is structured properly — auto layout, named layers, organized components — since a badly structured file breaks Dev Mode's inspection features regardless of the tool. Ask for a live demo of a past handoff file during the vendor evaluation call rather than accepting a description of their process."}},
    {"@type": "Question", "name": "How much of a typical screen count should be empty, error, and loading states?", "acceptedAnswer": {"@type": "Answer", "text": "Edge-case states (empty, error, loading, and content-overflow variants) typically account for 30% to 40% of the actual screens an engineering team needs to implement a feature completely, even though they're often absent from a vendor's initial deliverable. Get these explicitly scoped into the contract rather than assumed as included."}},
    {"@type": "Question", "name": "Why does accessibility need to be specified at the design stage rather than left to engineering?", "acceptedAnswer": {"@type": "Answer", "text": "Accessibility decisions — focus order, ARIA roles for custom components, keyboard interaction patterns, color contrast — are structural to a component's design, not surface-level additions engineers can bolt on afterward. Leaving them undocumented at handoff means engineering either guesses at intent or the component gets rebuilt later once a compliance review catches the gap, both of which are more expensive than specifying it upfront."}},
    {"@type": "Question", "name": "What's a reasonable red flag if a vendor can't answer these handoff questions clearly?", "acceptedAnswer": {"@type": "Answer", "text": "A vendor who responds to specific handoff questions with reassurance rather than concrete process (\"don't worry, we'll work closely with your team\") rather than naming a tool, format, or documented artifact is signaling that handoff has not historically been a structured part of their delivery. That gap reliably shows up as rework cost on your engineering team's timeline, not theirs."}}
  ]
}
</script>
