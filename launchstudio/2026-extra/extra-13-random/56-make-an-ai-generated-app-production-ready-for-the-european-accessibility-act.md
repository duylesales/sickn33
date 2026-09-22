---
Title: "Make an AI Generated App Production Ready for the European Accessibility Act"
Keywords: make an ai generated app production ready, make ai generated app production ready, european accessibility act, wcag ai website, accessible webshop, bolt accessibility, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: AI-Native Founder (Non-Technical)
---

# Make an AI Generated App Production Ready for the European Accessibility Act

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Make an AI Generated App Production Ready for the European Accessibility Act",
  "description": "The European Accessibility Act applies to many consumer-facing digital services, including e-commerce. This decision guide explains whether it applies to your AI-built app, the typical accessibility gaps in AI-generated interfaces, and how to fix them without redesigning.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-11-25",
  "inLanguage": "en",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/make-an-ai-generated-app-production-ready-for-the-european-accessibility-act" }
}
</script>

AI-generated interfaces look polished. They also tend to fail people who use screen readers, navigate by keyboard, need larger text or cannot distinguish low-contrast colours. Since June 2025, the European Accessibility Act (EAA) has made accessibility a legal requirement for many consumer-facing digital services in the EU, including e-commerce. For founders who want to make an AI generated app production ready, accessibility has moved from "nice to have" to a decision you need to make consciously.

This is a practical guide, not legal advice.

## Decision 1: Does the EAA Apply to You?

The EAA covers specific products and services, including e-commerce services (selling goods or services online to consumers), consumer banking, e-books, passenger transport services and electronic communications. It applies from 28 June 2025, implemented in national law — in the Netherlands through amendments to existing legislation.

Two points matter most for founders:

- **Consumer-facing e-commerce** — webshops, booking and ordering platforms where consumers buy — is broadly in scope.
- **Microenterprises providing services** — fewer than 10 employees and annual turnover or balance sheet of no more than €2 million — are exempt from the service requirements.

So a solo founder's webshop may be exempt today, but growth changes that, and B2B customers, public-sector buyers and partners increasingly require accessibility regardless. Many founders choose to meet the standard early rather than retrofit later.

## Decision 2: Which Standard Will You Follow?

In practice, the EAA's requirements for websites and apps are met by following the harmonised European standard EN 301 549, which incorporates WCAG 2.1 level AA. WCAG is the reference most developers and tools use. Targeting WCAG 2.1 AA (or 2.2 AA) is the sensible choice.

## Decision 3: What Needs Fixing to Make an AI Generated App Production Ready?

AI-generated interfaces repeat the same accessibility gaps. The most common:

- **Missing text alternatives.** Images, icons and icon-only buttons without alt text or accessible labels; screen readers announce "button" with no meaning.
- **Form fields without labels.** Placeholders used as labels disappear when typing and are not reliably announced.
- **Low contrast.** Fashionable light-grey text on white fails contrast requirements.
- **Keyboard traps and invisible focus.** Custom dropdowns, modals and date pickers that cannot be operated by keyboard, or focus outlines removed for aesthetics.
- **Clickable divs.** Elements that look like buttons but are not buttons, so keyboards and assistive technology ignore them.
- **Missing structure.** No proper headings, landmarks or page titles, making navigation by screen reader difficult.
- **Error messages that are not announced.** Validation errors shown only in red, not linked to fields or announced.
- **Motion and timing.** Carousels that cannot be paused, session timeouts without warning.

Most of these can be fixed without changing the visual design at all.

## Decision 4: How Will You Test?

Automated tools (such as axe or Lighthouse) catch roughly a third to half of issues — missing labels, contrast, structure. The rest need manual checks: navigate every critical flow by keyboard only, test with a screen reader (VoiceOver on Mac or iPhone, NVDA on Windows), zoom to 200%, and check error handling. Decide which flows are critical — typically browsing, product details, basket, checkout, account and contact — and test those thoroughly.

## Decision 5: What Will You Publish?

Services in scope must provide information on how they meet accessibility requirements, commonly in an accessibility statement. Even outside the EAA's scope, a statement describing your conformance level, known limitations and a contact route for accessibility problems is good practice and valued by buyers.

## Decision 6: How Will You Keep It Accessible?

AI tools can reintroduce accessibility problems with each regeneration. Add automated accessibility checks to your CI, include accessibility in your AI tool's project rules ("all interactive elements must be native buttons or links with accessible names"), and recheck critical flows after major changes.

## Why It Also Makes Business Sense

Around one in five people in the EU has some form of disability, and many more have temporary or situational impairments. Accessible checkouts convert better for everyone: clear labels, visible focus, good contrast and understandable errors reduce abandonment. Accessible structure also helps search engines and AI answer engines understand your pages.

## Mapping WCAG to AI-Generated Components

To make an AI generated app production ready for accessibility, it helps to know which WCAG success criteria AI-built interfaces most often fail and how to fix them:

| WCAG criterion (2.1/2.2 AA) | Typical failure in AI-built UIs | Fix |
| --- | --- | --- |
| 1.1.1 Non-text content | Icon buttons without names; images without alt | `aria-label` on icon buttons; meaningful alt text |
| 1.3.1 Info and relationships | Divs styled as headings; inputs without labels | Semantic headings; `<label>` linked to inputs |
| 1.4.3 Contrast (minimum) | Light grey text on white | Darken text to at least 4.5:1 |
| 1.4.11 Non-text contrast | Faint input borders, focus rings | Stronger borders and focus indicators |
| 2.1.1 Keyboard | Custom dropdowns and date pickers | Accessible component libraries or proper keyboard handling |
| 2.4.3 Focus order | Modals not trapping or returning focus | Focus management in dialogs |
| 2.4.7 Focus visible | `outline: none` everywhere | Visible focus styles |
| 3.3.1 Error identification | Errors shown only in red | Text errors linked to fields |
| 4.1.2 Name, role, value | Clickable divs | Native buttons and links |
| 4.1.3 Status messages | Toasts not announced | `aria-live` regions |

Most fixes are small code changes. Using an accessible component library — for example Radix UI or React Aria primitives, which many AI tools already build on — resolves many keyboard and focus issues at once.

## Testing With Real Assistive Technology

Automated tools find a portion of issues; manual testing finds the rest. A practical manual test for each critical flow:

1. **Keyboard only:** Tab through the whole flow. Can you reach and operate everything? Is focus always visible? Does focus move sensibly into and out of dialogs?
2. **Screen reader:** with VoiceOver (macOS/iOS) or NVDA (Windows), listen to the page. Are headings, buttons, form fields and errors announced meaningfully?
3. **Zoom to 200% and 400%:** does content reflow without horizontal scrolling or overlapping?
4. **Reduced motion and high contrast settings:** does the interface remain usable?

Record results per flow. Repeat after major design changes.

## Writing an Accessibility Statement

An accessibility statement describes the standard you aim for (for example WCAG 2.1 AA), the current conformance status, known limitations with planned fixes and dates, how the statement was prepared (self-assessment or external audit) and a contact for accessibility problems with an expected response time. Keep it honest and dated. A statement that lists two known issues and a plan builds more trust than one that claims full conformance without evidence.

## Accessibility in the Development Process

To keep accessibility from regressing — especially with AI tools regenerating components — build it into the process:

- **Linting:** eslint-plugin-jsx-a11y flags common problems in code.
- **Automated tests:** axe checks in end-to-end tests of critical flows.
- **Project rules for AI tools:** "Use native buttons and links; every input needs a visible label; do not remove focus outlines."
- **Design tokens:** colours that already meet contrast requirements.
- **Definition of done:** keyboard check for every new interactive component.

These measures cost little per feature and prevent expensive remediation later.

## Who Is Exempt, and Why Many Comply Anyway

Microenterprises providing services are exempt from the EAA's service requirements, but many small businesses still choose to comply. Reasons include growth (crossing the threshold later means retrofitting), procurement (public bodies and larger companies increasingly require accessibility from suppliers), market size (a significant share of customers benefit) and SEO, since semantic, accessible pages are easier for search engines to understand.

## Documents and Content, Not Just Code

Accessibility also covers content: PDFs such as invoices and terms should be tagged and readable; videos need captions; images in product listings need descriptive alt text; and plain, clear language helps everyone. For webshops generated with AI tools, product descriptions and images uploaded by staff are an ongoing source of accessibility issues — a short guideline for whoever manages content keeps the site accessible after launch.

## Prioritising Fixes When Time Is Short

If you cannot fix everything at once, prioritise by impact on completing critical tasks. Blockers first: anything that prevents a keyboard or screen-reader user from completing checkout, signup or contact (keyboard traps, unlabelled required fields, inaccessible payment steps). Then major barriers: missing error announcements, low contrast on essential text, missing focus visibility. Then improvements: alt text quality, heading structure, captions for non-essential videos. Document the plan in your accessibility statement with target dates.

## Accessibility and Third-Party Components

Payment forms, chat widgets, cookie banners, embedded maps and video players often come from third parties and are frequently less accessible than your own code. Check them in your manual tests. Choose providers with documented accessibility support, configure them for accessibility where options exist, and mention unavoidable limitations in your statement. A cookie banner that traps keyboard focus can make an otherwise accessible site unusable — and it is one of the first things users encounter.

## Costs in Perspective

For a typical AI-built webshop or booking app, bringing critical flows to WCAG 2.1 AA takes days rather than weeks when done alongside other production work, because most fixes are local to components. The cost of retrofitting later is higher: components multiply, content accumulates and each new AI-generated screen repeats the same patterns. Addressing accessibility at production readiness — and adding guardrails so new components inherit it — is the most economical path.

## The Business Case in One Line

An accessible checkout sells to more people, ranks better, satisfies procurement and keeps you on the right side of the European Accessibility Act — which makes it one of the few production improvements that pays back on several fronts at once.

## Where to Begin This Week

Pick your single most important flow — usually checkout or signup — and run the four manual tests on it: keyboard only, screen reader, 200% zoom and reduced motion. Write down every barrier you find, fix the blockers first and add an automated axe check to that flow so it stays fixed. Then repeat for the next flow. Within a few weeks, the paths that matter most to your business will be usable by everyone, and your AI-generated interface will have guardrails that keep it that way as it evolves.

## Where LaunchStudio Fits

LaunchStudio fixes accessibility in AI-built interfaces without redesigning them: labels, alternatives, contrast adjustments within your brand palette, keyboard support, focus management, semantic structure, announced errors, and automated checks in CI — followed by manual testing of critical flows and help drafting an accessibility statement. It fits naturally alongside security and payment hardening in a Launch Ready project.

LaunchStudio is powered by Manifera, a software development company with 11+ years of experience delivering web applications for organisations with formal requirements, from Amsterdam, Singapore and Ho Chi Minh City. See [Manifera's web app development](https://www.manifera.com/services/web-app-develop/) and the [European Commission's EAA page](https://ec.europa.eu/social/main.jsp?catId=1202) for the official overview.

[Send us your prototype link](https://launchstudio.eu/en/#contact) and we will tell you, free of charge, how far your checkout is from WCAG AA.

## Real example

### An AI-Native Founder in Action: A Second-Hand Book Webshop and a Screen Reader

Rosa Veenstra, a former librarian in Drachten, built Boekenbus in Bolt: a webshop for second-hand books with a subscription "surprise box," search by genre and author, and a mobile-first checkout. It had grown to 14 staff across packing and customer service and turnover past €2 million, putting it outside the microenterprise exemption.

A customer who is blind emailed to say she could not complete a purchase. Rosa asked LaunchStudio to review. An automated scan found 212 issues; manual testing confirmed the customer's experience. Icon-only buttons for "add to basket" and "next" had no labels; form fields used placeholders as labels; the genre filter and address autocomplete were custom components that trapped keyboard focus; the pale grey text on cream failed contrast throughout; checkout errors appeared only in red with no announcement; and product images had no alt text.

Over nine business days, LaunchStudio's engineers added accessible names and alt text (generating book-cover alt text from title and author data), replaced placeholder-only fields with visible labels, rebuilt the filter and autocomplete on accessible patterns, adjusted text colours to meet contrast within Rosa's palette, linked and announced validation errors, added headings and landmarks, and put axe checks in CI. The customer who reported the problem tested the checkout with them before release. Rosa published an accessibility statement.

**Result:** Boekenbus's checkout meets WCAG 2.1 AA for its critical flows. Checkout completion on mobile rose by about 9% in the following quarter — for all customers — and the customer who reported the issue became a regular subscriber.

> *"I built the shop for book lovers and forgot that some of them read with their ears. The fixes didn't change how it looks, only who can use it."*
> — **Rosa Veenstra, Founder, Boekenbus (Drachten)**

**Cost & Timeline:** €2,500 (Launch Ready package: accessibility remediation, CI checks, manual testing and statement support) — completed in 9 business days.

## Frequently Asked Questions

### Does the European Accessibility Act apply to my AI-built webshop?

If you sell to consumers online and are not a microenterprise (fewer than 10 employees and no more than €2 million turnover or balance sheet), it very likely does. Confirm your situation with an adviser.

### What standard should an AI-built app meet for the EAA?

In practice, EN 301 549, which incorporates WCAG 2.1 level AA. Targeting WCAG 2.1 or 2.2 AA is the common approach.

### Can accessibility be fixed without redesigning my app?

Usually yes. Most issues — labels, alt text, keyboard support, focus, structure, error announcements — are fixed in code without visible design changes. Contrast adjustments can typically stay within your brand palette.

### How does Manifera approach accessibility work?

As part of production quality: automated checks, manual keyboard and screen-reader testing of critical flows, and guardrails so regressions are caught. Manifera applies these practices in its broader web application work.

### Does accessibility improve SEO and AI answer engine visibility?

Often, yes. Semantic structure, headings, alt text and clear labels help search engines and AI answer engines understand your content, alongside helping users.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Does the European Accessibility Act apply to my AI-built webshop?",
      "acceptedAnswer": { "@type": "Answer", "text": "Very likely if you sell to consumers and are not a microenterprise; confirm with an adviser." }
    },
    {
      "@type": "Question",
      "name": "What standard should an AI-built app meet for the EAA?",
      "acceptedAnswer": { "@type": "Answer", "text": "In practice EN 301 549, incorporating WCAG 2.1 AA." }
    },
    {
      "@type": "Question",
      "name": "Can accessibility be fixed without redesigning my app?",
      "acceptedAnswer": { "@type": "Answer", "text": "Usually yes; most fixes are in code without visible design changes." }
    },
    {
      "@type": "Question",
      "name": "How does Manifera approach accessibility work?",
      "acceptedAnswer": { "@type": "Answer", "text": "Automated checks, manual keyboard and screen-reader testing and regression guardrails." }
    },
    {
      "@type": "Question",
      "name": "Does accessibility improve SEO and AI answer engine visibility?",
      "acceptedAnswer": { "@type": "Answer", "text": "Often; semantic structure and labels help machines understand content." }
    }
  ]
}
</script>
