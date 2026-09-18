---
Title: "Bolt and Design Systems: Keeping One Consistent Interface"
Keywords: bolt design system, UI consistency, component library, design tokens, AI generated interfaces, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: AI-Native Founder (Non-Technical)
---

# Bolt and Design Systems: Keeping One Consistent Interface

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Bolt and Design Systems: Keeping One Consistent Interface",
  "description": "Each generated screen is attractive and none of them match. Why AI-built interfaces drift, the small system that stops it, and how to make the tool follow your design instead of inventing one.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-01-15",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/bolt-and-design-systems-keeping-one-consistent-interface" }
}
</script>

Look at five screens of a Bolt application built over three months and count the button styles. Six is common. The blues are slightly different. Some cards have a border, others a shadow. The spacing between elements is a different value on every page.

No individual screen looks wrong. Together they look like five products, and the effect on a customer is not that they notice the inconsistency — it is that the product feels slightly unreliable in a way they could not explain if asked.

The cause is structural and therefore fixable: each screen was generated in its own session, with no knowledge of the decisions made in the previous one.

## Consistency Is Trust

It is worth being clear about why this matters commercially, because "the spacing is inconsistent" sounds like a designer's complaint.

Interfaces that behave predictably are easier to use — a button that looks the same everywhere is one people recognise without reading. Interfaces that look coherent read as made by someone who was paying attention, and a business buyer evaluating a small supplier is looking for exactly that signal. And inconsistency compounds: once there are six button styles, the seventh costs nothing to add, and there is no version of the interface a new screen can match.

## Define Tokens Before Generating More Screens

The system that fixes this is small. It is a set of named decisions, written down once, that everything refers to.

**Colours.** Not a palette of forty, but a handful with roles: primary, a neutral scale for text and backgrounds, and colours for success, warning and error. Six to ten values.

**Spacing.** One scale, used everywhere. A common choice is multiples of four: 4, 8, 12, 16, 24, 32, 48. Every gap in the interface is one of those and never an arbitrary number.

**Typography.** Two or three sizes for headings, one for body, one for small text. One typeface, two weights.

**Radius and shadow.** One or two values each.

That is the whole system for a small product, and it fits on one page. Its value is that it converts an infinite set of choices into a short menu, which is what makes consistency achievable by anyone — including a tool.

## Build the Components Once

Below the tokens sit the components everything is assembled from: button in its two or three variants, input with its label and error state, card, dialog, table, badge, empty state.

Two ways to get them. Adopt a component library that already handles behaviour and accessibility properly — which, as the accessibility article in this series argues, is the single highest-leverage decision available — and apply your tokens to it. Or build the dozen you need yourself, which is a day and means owning their keyboard and screen reader behaviour, which generated components reliably lack.

For almost every small product, adopt the library.

Then the rule: screens are assembled from those components. A screen that needs a button uses the button. If a genuinely new component is required, it is built once, added to the set, and used.

## Make the Tool Follow the System

This is the part that changes what generation produces, and it is why the system is worth having in a product built this way.

Put the tokens and the component list in a file in your repository — the conventions file this series keeps recommending — stating plainly: these are the colours, this is the spacing scale, these are the components, use them and do not introduce new ones.

Coding assistants read it. The difference in output is immediate and larger than founders expect: a session asked to add a screen assembles it from the components that exist rather than inventing a fourth button.

Reinforce it by example. A model writing against a codebase where every screen uses the same components will imitate that, because imitation is what it does well. The consistency becomes self-sustaining once there is a majority pattern to copy.

## Fix What Exists, Then Hold the Line

For an application that already has six button styles, the cleanup is contained.

Inventory what exists: every colour used, every spacing value, every button and input variant. The list is usually shorter than it feels — six buttons, twelve greys, a dozen arbitrary margins.

Choose the canonical version of each, define the tokens, build or adopt the components, and convert screen by screen. A day for a twenty-screen application, and it can be done incrementally: anything you touch gets converted.

Then hold it with the conventions file and the monthly review described elsewhere in this series, checking specifically whether a new colour or a new component appeared.

## Dark Mode and Other Things Tokens Make Cheap

Once the interface refers to named values rather than to literal colours, a set of changes that were previously large become configuration.

Dark mode is the obvious one: define the token values a second time for a dark context and the entire interface follows. Attempting this without tokens means finding every colour in every component, which is why products that skipped the system quote weeks for a feature that should be an afternoon.

The same applies to several others. A customer who wants the product in their own colours — common in white-label arrangements and worth real money — is a token override rather than a fork. A density setting for users who want more on screen is a spacing scale swap. And a contrast adjustment for accessibility is a change to two or three values rather than an audit.

None of these is a reason to build a design system on its own. They are the reason that a system built for consistency keeps paying afterwards, and they are worth knowing about when deciding whether the two days are justified.

The counsel against over-engineering still applies. Define the tokens you use, not the ones a large company would need. A product with eight colours and one spacing scale gets all of the above; a product with a hundred tokens and a theming architecture has built a design system as a project rather than as a tool, and that is a different and usually unnecessary undertaking.

## Content Is Part of the System Too

The inconsistency that founders notice is visual. The one customers notice is in the words, and it drifts for exactly the same reason.

A generated product accumulates three ways of saying the same thing. The button is "Opslaan" on one screen and "Bewaren" on another. Errors are sometimes apologetic sentences and sometimes technical fragments. The thing your product is about is called a client on one screen, a customer on the next and an account in the settings — which is the vocabulary problem the schema article in this series describes, surfacing in the interface where users meet it.

Add a short section to the conventions file. The words your product uses for its concepts, with the ones it does not use listed beside them. The standard labels for common actions. The tone for error messages — what happened, and what to do about it. Whether you address users as "je" or "u", which in Dutch is a decision that must be made once and applied everywhere, and which generated copy will otherwise mix within a single screen.

Half a page, and it does the same work the tokens do: it converts an open question into a short menu, for you and for whatever writes the next screen.

It is also the cheapest of all the work in this article. Nothing needs building, nothing needs converting, and the effect on how finished a product feels is out of proportion to the effort — particularly for a Dutch product, where a mixture of formal and informal address reads as carelessness rather than as variety.

## Setting This Up

For an existing application this is typically one to two days: an inventory of colours, spacing values and component variants in use; a token set defined — six to ten colours, one spacing scale, three or four type sizes, one radius and one shadow; an accessible component library adopted and styled with the tokens, or a dozen components built; screens converted to use them; arbitrary values removed so the only available choices are the defined ones; the tokens and component list written into the repository's conventions file so coding assistants follow them; and a check in the monthly review for newly introduced values.

LaunchStudio does this alongside accessibility work, since the two share the same fix. Behind it is Manifera — eleven years, 160+ projects, with design and engineering from Amsterdam, Singapore and Ho Chi Minh City.

[Send us five screens](https://launchstudio.eu/en/#contact) and we will tell you how many button styles you have.

## Real example

### Eleven Greys

Sanne de Rooij built Stagebureau with Bolt: internship placement administration for vocational colleges, used by 12 institutions to match around 3,000 students a year with host companies.

A college's communications officer reviewed the product before a wider rollout and produced a list of 34 inconsistencies. Sanne's first reaction was that they were cosmetic.

The inventory found eleven distinct greys for text, seven button styles across nine screens, four different card treatments, three input designs with different error handling, and spacing values ranging from 3 to 37 pixels with no pattern. Two screens used a different typeface entirely, from a session where the tool had reached for something else.

More consequentially, the audit found that the inconsistency was hiding a functional problem: the three input designs handled validation errors differently, and one of them showed errors only in colour with no text — which was both an accessibility failure and the reason two colleges had reported that students did not understand why a form would not submit.

Two business days: tokens defined with eight colours including a single grey scale of five steps, a four-multiple spacing scale, three heading sizes and one body size, one radius and one shadow; an accessible component library adopted and styled with those tokens; button, input, card, dialog, table, badge and empty state standardised; all nine screens converted; the stray typeface removed; error handling unified with text alongside colour, which resolved the colleges' complaint; every arbitrary colour and spacing value removed from the codebase so the defined ones are the only ones available; and the tokens and component list written into the repository's conventions file.

**Result:** the communications officer's list went to two remaining items, both accepted. Subsequent AI sessions produce screens that match, which Sanne describes as the change that made the difference — before, every new feature added a variant, and now they do not. Two further colleges signed within the quarter.

> *"I thought it was cosmetic. Then I found out that one of my three input designs showed errors in colour only, and that was why students at two colleges could not work out what was wrong with their forms."*
> — **Sanne de Rooij, Founder, Stagebureau (Zwolle)**

**Cost & Timeline:** €2,600 (interface inventory, token definition, accessible component library adoption and styling, nine screens converted, error handling unification, arbitrary value removal, conventions documentation) — completed in 2 business days.

## Frequently Asked Questions

### Why do AI-generated screens not match each other?

Each is produced in its own session with no knowledge of previous decisions. Every screen is a reasonable answer to its own request, and nothing reconciles them.

### Does interface consistency actually matter?

Yes. Predictable elements are easier to use, coherence signals attention to detail to business buyers, and inconsistency compounds — once six variants exist, there is nothing for a new screen to match.

### What is the minimum design system?

Six to ten colours with roles, one spacing scale, three or four type sizes, one radius and one shadow — plus a dozen components. It fits on a page.

### Should I build components or adopt a library?

Adopt one. It handles keyboard and screen reader behaviour that generated components lack, and styling it with your tokens is far less work than building and maintaining your own.

### How do I stop the drift returning?

Write the tokens and component list into a conventions file in the repository. Coding assistants read it, and the output changes immediately.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Why do AI-generated screens look inconsistent?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Each screen is generated in its own session with no memory of earlier decisions, so nothing reconciles the choices."
      }
    },
    {
      "@type": "Question",
      "name": "Does interface consistency matter commercially?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes — predictable elements are easier to use and coherence signals care to business buyers, while inconsistency compounds with every new screen."
      }
    },
    {
      "@type": "Question",
      "name": "What is the minimum useful design system?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Six to ten role-based colours, one spacing scale, three or four type sizes, one radius and shadow, plus about a dozen components."
      }
    },
    {
      "@type": "Question",
      "name": "Build components or adopt a library?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Adopt one — it supplies the keyboard and screen reader behaviour generated components lack, styled with your own tokens."
      }
    },
    {
      "@type": "Question",
      "name": "How do I prevent design drift returning?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Put the tokens and component list in the repository's conventions file; coding assistants read it and follow it."
      }
    }
  ]
}
</script>
