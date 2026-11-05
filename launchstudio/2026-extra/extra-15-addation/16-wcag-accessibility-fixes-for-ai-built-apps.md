---
Title: "WCAG Accessibility Fixes for AI-Built Apps"
Keywords: wcag fixes lovable app, accessibility ai generated code, wcag 2.1 aa react, accessible components shadcn, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: AI-Native Founder (Non-Technical)
---

# WCAG Accessibility Fixes for AI-Built Apps

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "WCAG Accessibility Fixes for AI-Built Apps",
  "description": "AI builders such as Lovable, Bolt and v0 generate attractive interfaces that often fail WCAG 2.1 AA in predictable ways: missing labels, clickable divs, removed focus outlines, low contrast, inaccessible modals and silent status messages. This guide lists the most common failures, the fixes, how to test and how to keep new screens accessible.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-05-03",
  "inLanguage": "en",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/wcag-accessibility-fixes-for-ai-built-apps" },
  "citation": [
    { "@type": "CreativeWork", "name": "W3C WCAG 2.1", "url": "https://www.w3.org/TR/WCAG21/" },
    { "@type": "CreativeWork", "name": "WAI-ARIA Authoring Practices Guide", "url": "https://www.w3.org/WAI/ARIA/apg/" },
    { "@type": "CreativeWork", "name": "WebAIM Million report", "url": "https://webaim.org/projects/million/" },
    { "@type": "CreativeWork", "name": "Deque axe-core", "url": "https://github.com/dequelabs/axe-core" }
  ]
}
</script>

AI builders are very good at producing interfaces that look finished. Spacing is consistent, colours are pleasant, components animate smoothly. What they are much less reliable at is producing interfaces that everyone can use: people who navigate with a keyboard, people using screen readers, people with low vision who zoom to 400%, people with colour blindness and older users with less precise motor control.

That gap matters more than ever. The European Accessibility Act now applies to many consumer-facing services, public-sector buyers require WCAG conformance, and accessibility problems quietly reduce conversion for all users. The encouraging part is that AI-generated apps tend to fail in the same places, so a focused set of fixes, applied at the component level, resolves most problems.

This guide covers those fixes in the order we apply them.

## Key Takeaways

- **Most accessibility failures live in a few shared components:** buttons, inputs, modals, menus, tabs, toasts and tables. Fix them once and every screen improves.
- **The six most common WCAG failures** on the web are low contrast, missing alt text, missing form labels, empty links, empty buttons and missing document language, according to WebAIM's annual analysis of a million home pages.
- **Automated tools find only part of the problem.** Keyboard and screen reader testing are required for WCAG 2.1 AA.
- **Accessible component libraries help, but customisation breaks them.** Many AI-built apps start from accessible primitives and then override the parts that make them accessible.
- **Prompts and project rules prevent regressions.** Tell your AI builder the accessibility rules once, in writing.

## Why AI-Generated Interfaces Fail Accessibility

There are three reasons, and they explain where to look.

**Training data.** AI models learn from enormous amounts of public code, and much of the public web is inaccessible. WebAIM's annual "Million" study consistently finds detectable WCAG failures on the vast majority of home pages, averaging dozens of errors per page. Models reproduce what they have seen.

**Prompts focus on looks.** "Make the dropdown look like Linear's" says nothing about keyboard behaviour. The model optimises for visual similarity.

**Customisation of good primitives.** Lovable and v0 often generate components based on shadcn/ui and Radix primitives, which are designed to be accessible. Problems appear when later prompts replace a Radix dialog with a custom `div`, remove focus outlines because they "look ugly", or wrap a button in a clickable `div` to add an animation.

## Fix 1: Buttons and Links That Are Real Buttons and Links

**The failure.** Clickable `div` or `span` elements with `onClick` handlers. They cannot be reached with the Tab key, do not respond to Enter or Space, and screen readers do not announce them as interactive.

**The fix.** Use `<button>` for actions and `<a href>` for navigation. If a design requires a non-button element, that is a sign the design should change, not the semantics.

```tsx
// Before
<div className="card-action" onClick={archive}>Archive</div>

// After
<button type="button" className="card-action" onClick={archive}>Archive</button>
```

**Icon-only buttons** need an accessible name, either visible text, an `aria-label`, or visually hidden text:

```tsx
<button type="button" aria-label="Delete invoice 2041" onClick={remove}>
  <TrashIcon aria-hidden="true" />
</button>
```

Note the specific label. "Delete" repeated twenty times in a table is confusing; "Delete invoice 2041" is clear.

## Fix 2: Form Labels and Errors

**The failure.** Inputs with placeholder text instead of labels. When the user starts typing, the placeholder disappears, and screen readers may not announce it at all. Errors shown only as red borders.

**The fix.** Every input gets a visible `<label>` connected by `htmlFor` and `id`. Errors are written in text, connected to the field with `aria-describedby`, and the field is marked `aria-invalid`.

```tsx
<label htmlFor="email">Email address</label>
<input
  id="email"
  type="email"
  autoComplete="email"
  aria-invalid={!!errors.email}
  aria-describedby={errors.email ? "email-error" : undefined}
/>
{errors.email && <p id="email-error">Enter an email address like name@company.nl</p>}
```

Two details matter: the `autoComplete` attribute helps users with motor and cognitive disabilities fill forms quickly, which WCAG 2.1 requires for common personal data fields, and the error message says how to fix the problem, not only that something is wrong.

## Fix 3: Visible Focus

**The failure.** `outline: none` or `focus:outline-none` applied globally because the browser's default ring did not match the design. Keyboard users can no longer see where they are.

**The fix.** Never remove focus indicators without replacing them. Use `:focus-visible` so the indicator appears for keyboard users without showing on mouse clicks, and make it clearly visible against every background.

```css
:focus-visible {
  outline: 2px solid #1d4ed8;
  outline-offset: 2px;
}
```

Search the codebase for `outline-none` and `outline: none`. In AI-generated projects, it is often present on dozens of elements.

## Fix 4: Colour Contrast

**The failure.** Light grey secondary text, placeholder text, disabled-looking but active buttons, brand colours on white that fail the 4.5:1 ratio for normal text, and icons or input borders below the 3:1 ratio required for non-text elements.

**The fix.** Adjust the design tokens, not individual elements. Most AI-built apps define colours in a Tailwind configuration or CSS variables. Change `muted-foreground`, `border` and brand shades to compliant values once, and the whole app follows. A slightly darker brand colour usually keeps the identity intact while passing contrast checks.

Also check that information is never conveyed by colour alone: a red or green status dot needs a text label or icon as well.

## Fix 5: Modals, Drawers and Menus

**The failure.** Custom modals that do not move focus into the dialog, let the Tab key escape to the page behind, cannot be closed with Escape and do not return focus to the button that opened them. Dropdown menus that only open on hover.

**The fix.** Use proven primitives such as Radix Dialog, Dropdown Menu and Popover, which handle focus trapping, Escape, `aria-modal` and focus return. If the project has replaced them with custom versions, restore the primitives and reapply the styling. The WAI-ARIA Authoring Practices Guide describes the expected keyboard behaviour for each pattern if you need to verify it.

## Fix 6: Status Messages and Toasts

**The failure.** "Saved", "Payment failed" or "3 results found" appear visually but are never announced to screen reader users.

**The fix.** Render status messages inside a live region. Many toast libraries do this correctly by default; custom implementations often do not.

```tsx
<div role="status" aria-live="polite">{statusMessage}</div>
```

Use `role="alert"` only for urgent errors that should interrupt the user.

## Fix 7: Headings, Landmarks and Page Titles

**The failure.** Headings chosen by visual size, so a page jumps from `h1` to `h4`; card titles as `h2` while the actual sections have no headings; every page with the same document title; missing `lang` attribute on the `html` element.

**The fix.** One `h1` per page describing its purpose, then logical `h2` and `h3` levels. Use `header`, `nav`, `main` and `footer` landmarks. Set a unique page title per route, such as "Invoices - Acme Dashboard", and set `lang="nl"` or `lang="en"` to match the content. Screen reader users navigate by headings and landmarks, so this structure is how they find their way around.

## Fix 8: Images and Icons

**The failure.** Missing `alt` attributes, file names as alt text, or decorative images announced with long descriptions.

**The fix.** Informative images get concise alt text describing their purpose. Decorative images get `alt=""`. Decorative icons next to text get `aria-hidden="true"`. Charts need a text summary or data table alternative.

## Fix 9: Tables and Data Grids

**The failure.** Data tables built from nested `div` elements, so screen readers cannot associate cells with headers. Sortable columns with no indication of sort state.

**The fix.** Use real `<table>`, `<th scope="col">` and `<td>` markup for tabular data. Indicate sort state with `aria-sort` on the active column header, and make sort controls buttons.

## Fix 10: Zoom, Reflow and Touch Targets

**The failure.** Layouts that break at 200% zoom, require horizontal scrolling at 320 pixels wide, or disable pinch-zoom with `maximum-scale=1`. Tiny touch targets in mobile views.

**The fix.** Remove zoom restrictions from the viewport meta tag, test at 400% zoom on desktop, use responsive layouts that reflow, and give interactive elements comfortable target sizes, particularly in mobile navigation and table actions.

## How to Test

| Method | What it finds | Time |
| --- | --- | --- |
| Automated scan (axe, Lighthouse) | Contrast, missing labels and alt text, invalid ARIA | Minutes per page |
| Keyboard-only walkthrough | Unreachable controls, focus traps, invisible focus | 15-30 minutes per journey |
| Screen reader test (NVDA, VoiceOver) | Missing names, silent status, confusing structure | 30-60 minutes per journey |
| Zoom and reflow test | Broken layouts, hidden content | 10 minutes per page |
| Contrast check of design tokens | Systemic colour problems | Once per theme |

Automated tools such as axe-core catch a meaningful share of issues quickly but not all; keyboard and screen reader testing are necessary for confidence.

## Keeping New Screens Accessible

Fixes only last if new code follows the same rules. Three measures help:

- **Project instructions for your AI builder** listing the rules: semantic buttons and links, labels for every input, never remove focus outlines, use the existing accessible components, meet WCAG 2.1 AA contrast.
- **Automated checks in the pipeline** that run axe on key pages and fail the build on serious violations.
- **A short manual check** with the keyboard whenever a new interactive component is introduced.

For the legal side, our guide to the [European Accessibility Act for SaaS and webshops](https://launchstudio.eu/en/blog/european-accessibility-act-for-saas-and-webshops) explains who is covered and what documentation is expected.

## What It Costs

LaunchStudio's **Launch Ready** package (€800-€3,500) covers an accessibility audit of key journeys, component-level fixes, design token adjustments, automated checks in your pipeline, an accessibility statement draft and 48 hours of support. **Launch & Grow** (€2,500-€7,500 plus €49 per month) adds managed hosting, monitoring and ongoing support. Use the [price calculator](https://launchstudio.eu/en/#calculator) for an estimate.

LaunchStudio is backed by Manifera, a software development company with 11+ years of experience, 160+ projects and 120+ engineers. Founders work with the team at Herengracht 420 in Amsterdam; engineers are based at Manifera's development centre on Pho Quang Street in Ho Chi Minh City, with a hub on Tras Street in Singapore.

## Real example

### An AI-Native Founder in Action: The Municipal Permit Portal That Failed Its Accessibility Check

Hanna Bakker, a former policy adviser, built Vergunningloket with v0 and Supabase: a portal that helps small municipalities let residents apply for event and terrace permits, upload documents and follow their application. A municipality in Drenthe wanted to adopt it, but its procurement required WCAG 2.1 AA, verified by an external accessibility test before go-live.

The external test failed the portal on 31 criteria. The document upload area was a styled `div` that could not be reached by keyboard, the multi-step form used placeholders instead of labels and showed errors only as red outlines, focus outlines had been removed project-wide, the municipality's teal brand colour failed contrast on white, the confirmation dialog let focus escape behind it, and status updates such as "Document uploaded" were silent for screen reader users. Every page had the same title, and the `lang` attribute was set to English on Dutch pages.

LaunchStudio replaced the upload area with an accessible file input and button pattern, added visible labels, `autoComplete` attributes and linked text errors to every form step, restored Radix dialogs with correct focus handling and introduced a `:focus-visible` style across the app. The design tokens were adjusted to a compliant teal, live regions announced uploads and step changes, page titles became unique per step and the language was set correctly. Axe checks were added to the deployment pipeline, and accessibility rules were written into the v0 project instructions.

**Result:** The portal passed the external retest with no failures at level A or AA, eleven business days after work started. The municipality went live, and two neighbouring municipalities adopted Vergunningloket within the year, both citing the accessibility report.

> *"v0 made the portal look professional. Making it usable for every resident was the part that actually won the contract."*
> - **Hanna Bakker, Founder, Vergunningloket (Assen)**

**Cost & Timeline:** €3,200 (Launch Ready package: accessibility remediation of all journeys, design token changes, pipeline checks and retest support) - completed in 11 business days.

## Frequently Asked Questions

### Are apps built with Lovable or v0 accessible by default?

Partly. They often use accessible primitives such as Radix-based components, which is a good start, but generated and customised code commonly introduces clickable divs, missing labels, removed focus outlines and low contrast. A focused audit and component fixes are usually needed to reach WCAG 2.1 AA.

### Can automated tools confirm my app meets WCAG 2.1 AA?

No. Automated tools detect a useful portion of issues, such as contrast and missing labels, but cannot judge keyboard flow, focus order, meaningful alt text or screen reader experience. Manual keyboard and screen reader testing are needed for a reliable assessment.

### How long do accessibility fixes take for an AI-built app?

For a typical app, one to two weeks. Because most problems live in shared components and design tokens, fixing those resolves issues across many screens at once. Apps with many custom components or complex data tables take longer.

### Why does Manifera's experience matter for accessibility work?

Manifera has delivered public-facing systems for 11+ years where accessibility was part of acceptance testing. LaunchStudio uses that experience to fix root causes in components and tokens rather than patching individual pages.

### Do accessibility fixes improve search and AI visibility?

Usually, yes. Proper headings, landmarks, descriptive links, alt text, page titles and correct language attributes help search engines and AI answer engines understand content, so accessible pages are often easier to index and cite.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Are apps built with Lovable or v0 accessible by default?",
      "acceptedAnswer": { "@type": "Answer", "text": "Partly. Accessible primitives help, but generated and customised code often adds clickable divs, missing labels, removed focus outlines and low contrast, so fixes are usually needed." }
    },
    {
      "@type": "Question",
      "name": "Can automated tools confirm my app meets WCAG 2.1 AA?",
      "acceptedAnswer": { "@type": "Answer", "text": "No. They catch part of the issues; keyboard and screen reader testing are needed for a reliable assessment." }
    },
    {
      "@type": "Question",
      "name": "How long do accessibility fixes take for an AI-built app?",
      "acceptedAnswer": { "@type": "Answer", "text": "Typically one to two weeks, because fixing shared components and design tokens resolves issues across many screens at once." }
    },
    {
      "@type": "Question",
      "name": "Why does Manifera's experience matter for accessibility work?",
      "acceptedAnswer": { "@type": "Answer", "text": "Manifera has delivered public-facing systems with accessibility acceptance testing for 11+ years, and LaunchStudio fixes root causes in components and tokens." }
    },
    {
      "@type": "Question",
      "name": "Do accessibility fixes improve search and AI visibility?",
      "acceptedAnswer": { "@type": "Answer", "text": "Usually yes. Headings, landmarks, alt text, page titles and language attributes help search and AI engines understand and cite content." }
    }
  ]
}
</script>
