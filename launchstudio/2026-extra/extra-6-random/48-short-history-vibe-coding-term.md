---
Title: "A Short History of 'Vibe Coding' and Where the Term Actually Came From"
Keywords: ai coding, vibe coding history, ai coding term origin, no-code ai builders
Buyer Stage: Awareness
Target Persona: AI-Native Founder (Non-Technical)
---

# A Short History of 'Vibe Coding' and Where the Term Actually Came From

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "A Short History of 'Vibe Coding' and Where the Term Actually Came From",
  "description": "An explainer on the origin of the term vibe coding within ai coding culture, what it actually describes, and how the popular usage has drifted from its original, narrower meaning.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2026-07-25",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/short-history-vibe-coding-term" }
}
</script>

The phrase spread faster than its definition did. Within a matter of months, "vibe coding" went from a specific, fairly narrow description of a particular way of working with ai coding tools to a catch-all label for almost anything involving AI and software — which means most people using the term today are using a much blurrier version of it than the one it started as.

Worth untangling, especially for founders who get called "vibe coders" as either a compliment or a dismissal, often without much precision behind either.

## What the term originally described

In its original, more precise sense, vibe coding described a specific workflow: describing what you want in natural language and letting an AI tool generate the actual code, largely without reading or writing that code yourself — building by describing outcomes and vibes rather than by writing syntax. The emphasis was on the experience of building without traditional programming knowledge as the primary skill, guided instead by iterative description, testing what came out, and refining the description until the result matched the intent.

That's narrower than how the phrase gets used now. Today it's applied loosely to almost any AI-assisted development — including plenty of workflows where a skilled engineer is very much reading and refining the generated code, which is a meaningfully different activity than the original description was pointing at.

## Why the term spread beyond its original meaning

Popular terms almost always drift wider than their original definition, and "vibe coding" had ingredients that made it especially likely to spread fast: it was catchy, it captured something real happening at scale for the first time, and it applied to a broad and growing population of people building software with AI tools, at every skill level. Once journalists, commentators, and the founders themselves started using it as shorthand for "building with AI" in general, the more specific original meaning — building purely by description, without engaging with the underlying code at all — got absorbed into the broader, vaguer usage.

That drift isn't necessarily a problem. Language does this. But it does mean the term is now doing double duty: sometimes describing a genuinely distinct way of building software, and sometimes just standing in for "used an AI tool," which describes a much wider and more varied group of people.

## What the original, narrower usage actually captures

The original sense of the term is useful precisely because it identifies something real: a founder who has never written a line of code, describing a product entirely through natural language prompts, and ending up with a working application. That's a genuinely new category of builder that didn't really exist at scale before AI coding tools matured — someone whose primary skill is describing what they want clearly, not writing code.

## Owen's origin story

Owen Jacobs, a founder in Ermelo, built KassaKoppel — a point-of-sale integration tool — using Cursor, as one of the earlier wave of builders who fit the original, narrower definition closely. He started with zero coding background, building purely by describing what he wanted in plain language and iterating based on what came out. He didn't read the generated code, didn't debug it directly, and didn't have a technical background to fall back on when something didn't work — he adjusted his description and tried again.

That's the original sense of the term in practice: not a vague label for "built something with AI," but a specific description of Owen's actual process — outcome-focused, description-driven, and genuinely distinct from how a software engineer using the same AI tools would work, reading and adjusting code directly rather than only ever describing outcomes.

## Why the distinction still matters for founders today

Knowing which version of "vibe coding" applies to your own situation is more than a semantic exercise. A founder who fits the original, narrower definition — building purely by description with no direct engagement with the code — faces a specific set of risks that a founder who's actively reading and reviewing generated code doesn't face in the same way: no independent verification that the code does what it's supposed to, no built-in check on security or edge cases, and no way to sanity-check the AI tool's claims against the actual implementation.

That's not a reason to avoid building this way — it's exactly how products like Owen's KassaKoppel get built and succeed. It's a reason to know when a second, qualified set of eyes should look at the result before real customers and real data depend on it.

Our engineers in Singapore, alongside teams in Amsterdam and Ho Chi Minh City, work with founders across the entire spectrum — from the original, narrower sense of vibe coding to founders who code alongside AI tools directly. LaunchStudio brings Manifera's enterprise-grade engineering standard to both. If you're building the way Owen did — by describing outcomes rather than reading code — you can [send us your prototype link and we'll give you free advice](https://launchstudio.eu/en/#contact) on what to check before you scale.

## Real example

### An AI-Native Founder in Action: Building Entirely by Description

Owen Jacobs had never written code before starting KassaKoppel. His process with Cursor was purely conversational: describe what the point-of-sale integration needed to do, look at what came back, describe what needed to change, and repeat. Within weeks he had a working tool that connected small retailers' point-of-sale systems to their inventory and accounting software — genuinely useful, and built without Owen ever opening the underlying code himself.

As KassaKoppel started handling real transaction data from retail clients, Owen brought the project to LaunchStudio for a review, precisely because he knew his own process had never included anyone reading the code directly. Manifera's engineers found the integration logic solid overall, but identified a handful of gaps typical of description-driven building: transaction retry logic that could, in rare failure cases, process the same sale twice, and insufficient validation on data coming from certain point-of-sale hardware models.

The team fixed the retry logic, added proper validation, and gave Owen a plain-language summary of what had changed and why — matching the same description-first style he'd used to build the product in the first place.

**Result:** KassaKoppel now handles transaction retries correctly across all supported hardware, and Owen continues building new features purely by description, with periodic reviews as a standing checkpoint.

> *"I built this whole thing by talking to Cursor, not by reading a single line myself. Having someone actually check it afterward was the missing piece."*
> — **Owen Jacobs, Founder, KassaKoppel (Ermelo)**

**Cost & Timeline:** €950 (transaction logic review and validation fixes) — completed in 6 business days.

---

## Frequently Asked Questions

### What did "vibe coding" originally mean, more precisely?

It originally described building software purely by describing desired outcomes in natural language to an AI tool, without reading or writing the underlying code directly, as opposed to the broader, looser usage that now covers almost any AI-assisted development.

### Is "vibe coding" now used as a negative or dismissive term?

It's used both ways depending on context, sometimes as a neutral or even celebratory description of a new kind of builder, and sometimes dismissively to suggest a lack of technical rigor. Neither usage reflects the term's original, more specific meaning.

### Does building this way mean a product is automatically less secure?

Not automatically, but a founder who never reads the underlying code has no personal way to verify security or edge-case handling, which makes an independent review more important than it would be for a founder actively reviewing the code themselves.

### How does Manifera work with founders who built purely by description, like Owen?

Manifera's engineers, working from Singapore, Amsterdam, and Ho Chi Minh City, review the resulting codebase directly and translate findings into plain language, matching the description-first style the founder is already used to.

### Where can I learn more about how LaunchStudio helps AI-built products reach production?

You can explore LaunchStudio's process and packages directly on the [LaunchStudio site](https://launchstudio.eu/en/#process) to see how a review and production launch typically works.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "What did \"vibe coding\" originally mean, more precisely?", "acceptedAnswer": { "@type": "Answer", "text": "It originally described building software purely by describing desired outcomes in natural language to an AI tool, without reading or writing the underlying code directly, as opposed to the broader, looser usage that now covers almost any AI-assisted development." } },
    { "@type": "Question", "name": "Is \"vibe coding\" now used as a negative or dismissive term?", "acceptedAnswer": { "@type": "Answer", "text": "It's used both ways depending on context, sometimes as a neutral or even celebratory description of a new kind of builder, and sometimes dismissively to suggest a lack of technical rigor. Neither usage reflects the term's original, more specific meaning." } },
    { "@type": "Question", "name": "Does building this way mean a product is automatically less secure?", "acceptedAnswer": { "@type": "Answer", "text": "Not automatically, but a founder who never reads the underlying code has no personal way to verify security or edge-case handling, which makes an independent review more important than it would be for a founder actively reviewing the code themselves." } },
    { "@type": "Question", "name": "How does Manifera work with founders who built purely by description, like Owen?", "acceptedAnswer": { "@type": "Answer", "text": "Manifera's engineers, working from Singapore, Amsterdam, and Ho Chi Minh City, review the resulting codebase directly and translate findings into plain language, matching the description-first style the founder is already used to." } },
    { "@type": "Question", "name": "Where can I learn more about how LaunchStudio helps AI-built products reach production?", "acceptedAnswer": { "@type": "Answer", "text": "You can explore LaunchStudio's process and packages directly on the LaunchStudio site to see how a review and production launch typically works." } }
  ]
}
</script>
