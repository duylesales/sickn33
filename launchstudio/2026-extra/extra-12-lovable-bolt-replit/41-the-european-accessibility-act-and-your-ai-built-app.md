---
Title: "The European Accessibility Act and Your AI-Built App"
Keywords: European Accessibility Act, WCAG, accessibility, keyboard navigation, screen readers, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: AI-Native Founder (Non-Technical)
---

# The European Accessibility Act and Your AI-Built App

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "The European Accessibility Act and Your AI-Built App",
  "description": "Generated interfaces look right and fail for anyone not using a mouse. Who the accessibility rules apply to, the checks that find most problems in an hour, and the fixes that are genuinely cheap.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-12-04",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/the-european-accessibility-act-and-your-ai-built-app" }
}
</script>

AI coding tools produce interfaces that look correct. A div styled to resemble a button behaves like a button when clicked with a mouse, and in a screenshot it is indistinguishable from the real thing.

It is not a button. It cannot be reached by keyboard, it is not announced to a screen reader, and pressing enter on it does nothing. For a visitor using a mouse, the product works. For a visitor who is not, a substantial part of it does not exist.

This is the characteristic accessibility failure of generated code, and the reason it persists is that nothing about it is visible to the person who built it.

## Who This Applies To

The European Accessibility Act brings accessibility requirements to a range of products and services sold to consumers in the EU — including e-commerce, banking, transport and telecommunications services — with the obligation applying from mid-2025. The Netherlands implements it through national legislation, and public sector bodies have been covered by their own requirements for considerably longer.

The practical position for a small product: if you sell to consumers, or to public bodies, or to large companies with their own procurement standards, this is either a legal requirement or a commercial one. Microenterprises have some exemptions for services, but the exemption is narrower than founders hope and does not extend to a customer's own obligations.

And the commercial route arrives first. A municipality, a health organisation or a large employer will ask for an accessibility statement long before any regulator does.

## The Standard, in Practice

The reference is WCAG, and the usual target is level AA. Rather than reading the specification, the four principles it is organised around tell you what to check.

**Perceivable.** Content is available to different senses: text alternatives for images, captions for video, sufficient colour contrast, information not conveyed by colour alone.

**Operable.** Everything works by keyboard, nothing traps focus, people have enough time, nothing flashes dangerously.

**Understandable.** Predictable behaviour, clear labels, errors explained in text rather than by a red border.

**Robust.** Works with assistive technology, which mostly means using correct HTML elements rather than styled divs.

## The Hour That Finds Most Problems

Four checks, no tools beyond a browser, and they surface the majority of issues in an AI-built product.

**Unplug the mouse.** Navigate your entire product with tab, shift-tab, enter and space. Can you reach every control? Can you see which element has focus? Can you open a dialog, use it, and close it? Can you complete your main flow? In most generated applications this fails within two minutes, usually at a custom dropdown or a modal.

**Zoom to 200 percent.** Does the layout survive, or does content disappear behind other content? Many customers browse at enlarged text sizes permanently.

**Run an automated checker.** A browser extension finds contrast failures, missing labels and missing alternative text in seconds. It catches perhaps a third of issues, which is a third for almost no effort.

**Turn on the screen reader your operating system already includes** and try your main flow with the screen off. This is uncomfortable and it is the check that teaches the most.

## The Fixes That Are Cheap

Most findings in a generated interface come from a short list, and each fix is small.

**Use real elements.** A button is a `button`, a link is an `a` with an href, a checkbox is an `input`. Every native element brings keyboard behaviour, focus handling and screen reader semantics without any code.

**Label every input.** A visible label associated with its field. Placeholder text is not a label — it disappears when typing starts and is frequently unannounced.

**Fix contrast.** Grey text on white at 4.5:1 for body copy. Generated designs consistently choose light greys that look elegant and fail.

**Make focus visible.** Generated stylesheets often remove focus outlines because they are considered ugly. Replace them with something clearly visible rather than deleting them.

**Describe images meaningfully**, and mark decorative ones as decorative so they are skipped rather than announced.

**Announce errors in text**, associated with the field, rather than signalling them with colour.

**Structure headings properly**, in order, because screen reader users navigate by them.

## Where AI Tools Do the Most Damage

Three patterns worth searching your codebase for specifically.

Custom components built from divs — dropdowns, tabs, accordions, modals — which look right and implement none of the keyboard behaviour their native or properly-built equivalents provide. Using an accessible component library is almost always better than rebuilding these.

Removed focus styles, usually a single line in a stylesheet that disables them globally.

And ARIA attributes applied incorrectly. Generated code sprinkles roles and labels in a way that sometimes helps and frequently makes things worse, because an incorrect role actively misinforms assistive technology. Correct HTML with no ARIA beats styled divs with a lot of it.

## Write the Statement

An accessibility statement — what standard you aim for, what is not yet conformant, how to report a problem, and when it was last reviewed — is required for some organisations and useful for all of them.

Being honest in it is better than claiming full conformance. A statement saying you meet AA with three known exceptions, each with a workaround and a date, reads as a company that has actually looked. A blanket claim reads as a company that has not, and it is easy to disprove.

## Accessibility Is Not Only Permanent Disability

The framing that makes this work feel worthwhile rather than imposed: the people helped by these changes are a much larger group than the one founders picture.

Someone using your product on a train with one hand. Someone whose phone screen is cracked across the bottom third. A user in their sixties with ordinary age-related sight changes, which describes a large share of the Dutch workforce in several sectors. A warehouse worker wearing gloves. Someone with a temporarily broken wrist. Someone in a bright room where a light grey on white is simply invisible.

None of these people identify as disabled and all of them are affected by the same defects. Contrast that fails at 2.8:1 fails for everyone over a certain age. A control reachable only by precise mouse movement fails for anyone using a trackpad on a moving train. A form that signals errors only with colour fails for the one man in twelve with a colour vision deficiency.

This is why the conversion effect described in the example above is common rather than surprising. Accessibility work removes friction that was affecting a substantial minority of users who were quietly failing to complete things and not telling you why.

The practical consequence: treat these as usability defects with a legal dimension rather than as compliance with a usability side effect. It produces better decisions about what to fix first.

## Keeping It From Regressing

The uncomfortable property of accessibility in an AI-built product is that it regresses every time a feature is added, because the tool that adds the feature has the same habits as the one that built the original.

Three measures hold the line without turning every change into an audit.

**An accessible component library as the default.** If your buttons, dropdowns, dialogs and tabs come from a library that handles keyboard and screen reader behaviour, then a new screen assembled from them is accessible by construction. This is by far the highest-leverage decision, and it also means an agent session asked to add a dialog reaches for the right thing because it is what the codebase contains.

**An automated check in the build.** Accessibility linting on your components and an automated scan against key pages, failing on regressions. It catches the contrast change and the missing label, which are the most frequent reintroductions.

**A keyboard pass in your release routine.** One line on the checklist: tab through the thing you changed. Thirty seconds, and it catches what automation cannot.

Write the conventions into your project's instructions file as well — native elements over divs, labels on every input, focus never removed. Coding assistants read it, and the difference in what they generate is immediate and measurable.

## Setting This Up

For an existing product this is typically two to four days: a keyboard-only pass over every flow with findings listed, an automated scan across the main pages, a screen reader pass over the primary journey, custom div-based components replaced with native elements or an accessible library, all inputs labelled, contrast corrected to AA, visible focus restored, images given meaningful alternatives, errors announced in text and associated with fields, heading structure corrected, zoom to 200 percent verified, incorrect ARIA removed, and an accessibility statement published with known exceptions.

LaunchStudio does this as part of production readiness for products selling to consumers and to public bodies. Behind it is Manifera — eleven years, clients including Vodafone, TNO and CFLW, with public sector delivery experience from Amsterdam.

[Ask us to use your product without a mouse](https://launchstudio.eu/en/#contact). It takes ten minutes and the result is usually decisive.

## Real example

### A Tender Lost on the First Criterion

Olaf Rietberg built Buurtmelding in Lovable: a reporting tool municipalities use for residents to report issues in public space, sold to six smaller municipalities.

A larger municipality's tender required conformance with the public sector accessibility requirements and an accessibility statement. Olaf's product was eliminated at the first assessment stage before any demonstration.

The evaluation listed twelve failures. The report form could not be completed by keyboard, because the category selector was a div-based dropdown that responded only to clicks. Focus outlines were disabled globally by a line in the stylesheet. Form fields used placeholder text instead of labels. Body text was #999999 on white, a contrast ratio of 2.8:1. The map-based location picker had no alternative input method at all. Error messages were shown by turning field borders red with no text. And the heading structure jumped from h1 to h4, making the page unnavigable by screen reader.

Six business days: the category selector and three other custom components replaced with an accessible component library; the global focus-removal rule deleted and a visible focus style added; every field given a proper visible label; the palette adjusted so body text reaches 4.6:1 and interactive elements 3:1, with the brand colour darkened slightly; a postcode and street address alternative added alongside the map picker, which turned out to be faster for most residents anyway; errors announced in text, associated with their field and summarised at the top of the form; heading structure corrected throughout; images given alternatives with decorative ones marked; the whole product verified by keyboard, at 200 percent zoom and with a screen reader; and an accessibility statement published naming two remaining exceptions with workarounds and target dates.

**Result:** the product passed the assessment in the following tender round and was selected. More surprisingly to Olaf, reports submitted through the address alternative rather than the map now account for 38 percent of all reports, from residents who evidently found it easier — a conversion improvement he had not anticipated from accessibility work.

> *"I lost a tender before anyone saw the product, on criteria I did not know existed. And the fix that mattered most turned out to be a feature a third of my users prefer."*
> — **Olaf Rietberg, Founder, Buurtmelding (Assen)**

**Cost & Timeline:** €4,800 (accessible component replacement, focus and label remediation, contrast correction, alternative location input, error handling, heading structure, image alternatives, keyboard, zoom and screen reader verification, accessibility statement) — completed in 6 business days.

## Frequently Asked Questions

### Does accessibility law apply to my small product?

If you sell to consumers, public bodies or large organisations with procurement standards, it is either a legal requirement or a commercial one. The microenterprise exemption is narrower than founders expect.

### What is the quickest way to find problems?

Unplug the mouse and navigate your product with the keyboard. Most AI-built applications fail within two minutes, usually at a custom dropdown or a modal.

### Why do generated interfaces fail accessibility?

They use styled divs instead of native elements. A div that looks like a button has no keyboard behaviour and no meaning to assistive technology, and nothing about that is visible in a screenshot.

### Is an automated checker enough?

No. It finds roughly a third of issues — contrast, missing labels, missing alternatives — for very little effort. Keyboard and screen reader testing find the rest.

### Should my accessibility statement claim full conformance?

Only if it is true. A statement naming known exceptions with workarounds and dates reads as credible; a blanket claim is easy to disprove and worse than an honest one.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Does accessibility legislation apply to a small product?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "If you sell to consumers, public bodies or large organisations, it is a legal or commercial requirement. The microenterprise exemption is narrow."
      }
    },
    {
      "@type": "Question",
      "name": "What is the fastest accessibility check?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Navigate the entire product with only a keyboard. Most AI-built applications fail within two minutes at a custom dropdown or modal."
      }
    },
    {
      "@type": "Question",
      "name": "Why do AI-generated interfaces fail accessibility?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "They use styled divs rather than native elements, which look identical but have no keyboard behaviour or meaning to assistive technology."
      }
    },
    {
      "@type": "Question",
      "name": "Is an automated accessibility checker sufficient?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No — it catches about a third of issues. Keyboard and screen reader testing find the rest."
      }
    },
    {
      "@type": "Question",
      "name": "Should an accessibility statement claim full conformance?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Only if true. Naming known exceptions with workarounds and dates is more credible and harder to disprove."
      }
    }
  ]
}
</script>
