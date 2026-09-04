---
Title: "Accessibility Isn't Optional Anymore: What EU Founders Need at Launch"
Keywords: EU accessibility act SaaS, WCAG 2.2 AA checklist, EN 301 549 compliance, web accessibility startup, accessibility cheap wins, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: AI-Native Founder (Non-Technical)
---

# Accessibility Isn't Optional Anymore: What EU Founders Need at Launch

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Accessibility Isn't Optional Anymore: What EU Founders Need at Launch",
  "description": "A practical, cheap-wins-first guide to the European Accessibility Act, EN 301 549, and WCAG 2.2 AA basics for non-technical founders, covering exactly which fixes are inexpensive and which require a deeper accessibility pass.",
  "author": {
    "@type": "Organization",
    "name": "LaunchStudio",
    "url": "https://launchstudio.eu/en/"
  },
  "publisher": {
    "@type": "Organization",
    "name": "Manifera",
    "url": "https://www.manifera.com"
  },
  "datePublished": "2027-01-19",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://launchstudio.eu/en/blog/accessibility-what-eu-founders-need-at-launch"
  }
}
</script>

Does your signup button have a visible focus outline when someone tabs to it with a keyboard instead of a mouse? Most founders reading that question just tried tabbing through their own product for the first time to find out, and a meaningful share found nothing — no outline, no highlight, just a cursor that silently jumps somewhere invisible. That single missing detail is enough to make a product unusable for anyone who navigates by keyboard, whether from a motor impairment, a screen reader, or simply a preference — and it's one of maybe a dozen specific, genuinely cheap fixes that separate an inaccessible product from a reasonably compliant one.

The European Accessibility Act (EAA) became applicable in June 2025, and it isn't a niche concern anymore for anyone selling digital products or services to EU consumers — it applies broadly to e-commerce, banking, and a wide range of consumer-facing digital services, with specific exemptions mainly for microenterprises providing services (not products) under certain size thresholds, an exemption worth checking carefully rather than assuming applies by default. Whether or not your specific product is legally in scope today, the direction of travel is unambiguous, and the practical case for fixing the cheap stuff now is strong regardless of the legal threshold: these fixes are inexpensive, they materially widen your addressable market, and retrofitting them later, once a product has grown, costs meaningfully more than building them in now.

## What the Law Actually Points To: EN 301 549 and WCAG 2.2 AA

The EAA doesn't invent its own accessibility standard from scratch — it points to EN 301 549, the European standard for digital accessibility, which for web content largely incorporates WCAG (Web Content Accessibility Guidelines) at the AA conformance level, currently version 2.2. This matters practically because it means founders don't need to interpret a vague legal principle — WCAG 2.2 AA is a specific, published, testable checklist with clear pass/fail criteria for most items, which is unusually concrete as compliance frameworks go. The four organizing principles worth knowing, because they explain why the specific fixes below matter rather than feeling arbitrary: content must be **perceivable** (available through more than one sense — not conveyed by color alone, images have text alternatives), **operable** (usable via keyboard alone, not just mouse or touch), **understandable** (predictable navigation, clear error messages), and **robust** (works correctly with assistive technology like screen readers). Every specific fix below maps back to one of these four principles, which is a useful mental check when a new feature ships and you're wondering whether it needs an accessibility pass.

## The Cheap Wins: What Costs Almost Nothing and Fixes the Most

A specific, prioritized list, ordered roughly by cost-to-fix versus impact, because "improve accessibility" as a directive is useless without concrete targets. **Labels on every form field** — every input needs a visible, programmatically associated label (not just placeholder text, which disappears once someone starts typing and isn't reliably read by screen readers), and this is typically a one-line HTML attribute fix per field, not a redesign. **Color contrast** — WCAG AA requires a 4.5:1 contrast ratio for normal text against its background (3:1 for large text), and a huge share of AI-generated interfaces default to trendy but low-contrast combinations — light gray text on white backgrounds looks clean in a design mockup and fails contrast checks immediately; free browser extensions and online checkers verify this in seconds per color pair. **Keyboard navigation** — every interactive element (buttons, links, form fields, custom dropdown menus) needs to be reachable and operable using only the Tab key and Enter/Space, with a logical tab order matching the visual layout; this is where AI-generated custom components most often fail, because a visually polished custom dropdown or modal built without keyboard handling in mind looks identical to a compliant one until someone actually tries to use it without a mouse. **Visible focus states** — the outline or highlight showing which element is currently focused via keyboard, frequently stripped out by default CSS resets that developers (or AI tools) apply for aesthetic reasons without realizing they've removed a load-bearing accessibility feature; restoring a visible focus style is typically a few lines of CSS. **Alt text on meaningful images** — every image conveying information (not purely decorative ones) needs a text alternative describing its content or function, which is a content-writing task, not an engineering one, and can be done directly by a non-technical founder reviewing their own site. **Descriptive link and button text** — "click here" and "learn more" repeated across a page are indistinguishable to a screen reader user navigating by a list of links; specific text like "Read the pricing breakdown" costs nothing extra to write and fixes a real navigation problem.

## The Harder Wins: What Needs More Than an Afternoon

Beyond the cheap fixes, a smaller set of items genuinely requires more sustained attention, and it's worth knowing these exist rather than assuming the cheap wins above constitute full compliance. **Screen reader testing** — running your actual product through a real screen reader (VoiceOver on Mac, NVDA free on Windows) surfaces problems that automated checkers miss entirely, particularly around custom interactive components, dynamic content updates, and whether the reading order matches the logical order; this takes real time, doesn't need to happen constantly, but should happen at least once before a serious launch. **Form error handling** — errors need to be announced to assistive technology when they occur (not just shown visually in red text), associated clearly with the specific field that has the problem, and described in plain language rather than a generic "invalid input"; this often requires actual development work in how form validation is wired, not just a styling change. **Complex interactive components** — custom-built modals, multi-step wizards, drag-and-drop interfaces, and data tables with sorting/filtering need specific ARIA (Accessible Rich Internet Applications) attributes to communicate their state and behavior to assistive technology correctly, and AI coding tools frequently generate the visual behavior of these components without the underlying ARIA wiring, because the wiring is invisible in a demo and easy to skip. **Video and audio content** — captions for video, transcripts for audio, and avoiding auto-playing content with sound are all requirements that need planning at the content-production stage, not just a technical fix after the fact.

## Where AI Coding Tools Systematically Get This Wrong

It's worth naming a pattern specific to the AI-native founder audience directly: Lovable, Bolt, Cursor, and v0 all generate visually polished interfaces extremely well, and all of them, by default, under-prioritize the invisible-in-a-demo accessibility layer — focus states, ARIA attributes, semantic HTML structure, keyboard handling for custom components. This isn't a flaw specific to any one tool; it reflects what these tools are optimized to produce quickly, which is something that looks right in a browser to a sighted mouse user, because that's the feedback loop the tools and their prompts are built around. The practical implication: don't assume a beautiful AI-generated interface is accessible just because it looks clean and modern — modern, minimal design and accessible design frequently pull in different directions (low-contrast text, icon-only buttons with no labels, custom-styled form controls that lose native keyboard behavior), and a deliberate accessibility pass, even a quick one using the cheap-wins list above, is necessary regardless of how polished the AI-generated output looks.

## The Business Case Beyond Compliance

Framing accessibility purely as a legal risk to manage undersells the actual upside, and it's worth making the business case explicitly because it changes how founders prioritize the work. Roughly one in six people in the EU reports some form of disability, a meaningfully large addressable market segment that an inaccessible product simply cannot serve regardless of how good the core offering is. Many of the fixes above also improve the product for everyone, not just users with disabilities — better color contrast helps anyone using a phone in bright sunlight, clear error messages reduce support tickets from every user, keyboard navigation benefits power users who prefer not to reach for a mouse, and descriptive link text improves SEO because search engines parse link context the same way assistive technology does. Accessibility work with this framing stops looking like a compliance tax and starts looking like ordinary product quality work that happens to also satisfy a legal requirement — which is a more sustainable way to prioritize it than treating it as a checkbox to clear once and never revisit.

## A Practical First-Pass Checklist for This Week

For a founder who wants to act on this immediately rather than filing it away as "eventually": tab through your entire product using only the keyboard and note every place focus becomes invisible or unreachable; run your homepage and signup flow through a free automated checker (WAVE or axe DevTools, both free browser extensions) and fix what it flags, understanding that automated tools catch roughly a third of real issues and manual review still matters; check contrast on your primary text and button colors using a free contrast checker; review your form fields for actual associated labels, not just placeholder text; and write real alt text for every meaningful image rather than leaving it blank or filling it with the filename. None of this requires hiring anyone, and doing it this week rather than "eventually" catches the cheapest, highest-impact fixes before the product has grown large enough to make them expensive to retrofit everywhere at once.

Auditing an AI-generated interface against WCAG 2.2 AA and fixing the gaps that don't show up in a demo but do show up under a keyboard or screen reader is exactly the kind of last-mile work [LaunchStudio](https://launchstudio.eu/en/) folds into production hardening, backed by Manifera's 11+ years of experience building accessible production systems for enterprise and public-sector clients.

[Use the price calculator](https://launchstudio.eu/en/#calculator) to see what an accessibility pass costs alongside the other launch-readiness work your product needs.

## Real example

### An AI-Native Founder in Action: The Beautiful Interface Nobody With a Keyboard Could Use

Esmee van Dijk built Taallink, a language-exchange matching platform for adult learners, using v0 for the interface and Supabase for the backend, and was proud of how clean and modern the design looked — soft gray text, minimal borders, custom-styled dropdown menus for language and level selection. A university partner considering Taallink for their international student services program asked, during a routine review, whether the platform met EN 301 549 requirements, since public-sector-adjacent partnerships in several EU member states carry accessibility obligations that flow down to vendors.

A LaunchStudio accessibility review found the soft gray text failed contrast requirements across nearly every page, the custom language-selection dropdown couldn't be operated by keyboard at all (a mouse click was the only way to open or select from it), and none of the focus states had survived the CSS reset applied during initial styling. None of these problems were visible in a normal sighted, mouse-driven demo — which is exactly why they'd gone unnoticed through months of active development and user testing.

**Result:** Manifera's engineers fixed contrast ratios, rebuilt the dropdown with native keyboard support and proper ARIA attributes, and restored visible focus states across the app in under a week, and Esmee passed the university partner's accessibility review on the next submission.

> *"I'd tested Taallink with real users for months and nobody caught this, because everyone who tested it used a mouse. The first time I tabbed through my own signup flow, I couldn't even find where I was."*
> — **Esmee van Dijk, Founder, Taallink (Leiden)**

## Frequently Asked Questions

### Does the European Accessibility Act apply to my small SaaS product if I only have a handful of customers?

It depends on your service type and company size — the Act includes exemptions for microenterprises (fewer than 10 employees and under €2 million annual turnover) specifically providing services, though this exemption doesn't apply to certain product categories, so it's worth checking your exact situation rather than assuming exemption by default. Even where exempt, the cheap fixes covered above are worth doing regardless, since they widen your addressable market and cost little.

### What's the difference between WCAG AA and WCAG AAA, and do I need AAA?

AA is the level referenced by EN 301 549 and most legal accessibility requirements, covering the practical majority of real-world barriers. AAA is a stricter, more comprehensive level that most organizations, including large enterprises, don't fully achieve — AA is the realistic and legally relevant target for a small SaaS product, not AAA.

### Can automated accessibility checkers catch everything I need to fix?

No — automated tools like WAVE or axe DevTools typically catch around a third of real accessibility issues, mainly structural and markup problems like missing labels or contrast failures. Issues around logical reading order, custom component behavior, and genuine usability with a screen reader require actual manual testing to catch.

### How much does a proper accessibility audit and fix typically cost for a small product?

It varies significantly by how many custom interactive components your product has, but the cheap-wins list in this article (contrast, labels, focus states, alt text, basic keyboard navigation) typically takes a developer a few days to fix on a small product, while custom components needing full ARIA implementation add meaningfully more time depending on how many exist.

### Should I hire a specialized accessibility consultant, or can a general developer handle this?

For the cheap wins and most standard components, a competent general developer familiar with WCAG basics can handle the work without a specialist. Bring in dedicated accessibility expertise specifically for complex custom components, screen-reader-specific testing at scale, or if you're in a sector (public-sector-adjacent, banking, e-commerce at real scale) where a formal accessibility conformance statement is expected.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "Does the European Accessibility Act apply to my small SaaS product if I only have a handful of customers?", "acceptedAnswer": { "@type": "Answer", "text": "It depends on your service type and company size. The Act includes exemptions for microenterprises providing services, though this doesn't apply to certain product categories, so check your exact situation. Even where exempt, the cheap fixes are worth doing regardless." } },
    { "@type": "Question", "name": "What's the difference between WCAG AA and WCAG AAA, and do I need AAA?", "acceptedAnswer": { "@type": "Answer", "text": "AA is the level referenced by EN 301 549 and most legal requirements, covering the practical majority of real-world barriers. AAA is stricter and rarely fully achieved even by large enterprises, so AA is the realistic target for a small SaaS product." } },
    { "@type": "Question", "name": "Can automated accessibility checkers catch everything I need to fix?", "acceptedAnswer": { "@type": "Answer", "text": "No. Automated tools typically catch around a third of real issues, mainly structural problems like missing labels or contrast failures. Logical reading order, custom component behavior, and genuine screen reader usability require manual testing." } },
    { "@type": "Question", "name": "How much does a proper accessibility audit and fix typically cost for a small product?", "acceptedAnswer": { "@type": "Answer", "text": "It varies by how many custom interactive components exist, but the cheap-wins list (contrast, labels, focus states, alt text, keyboard navigation) typically takes a developer a few days on a small product, while custom ARIA implementation adds more time." } },
    { "@type": "Question", "name": "Should I hire a specialized accessibility consultant, or can a general developer handle this?", "acceptedAnswer": { "@type": "Answer", "text": "A competent general developer familiar with WCAG basics can handle cheap wins and most standard components. Bring in dedicated expertise for complex custom components, screen-reader-specific testing at scale, or sectors expecting a formal conformance statement." } }
  ]
}
</script>
