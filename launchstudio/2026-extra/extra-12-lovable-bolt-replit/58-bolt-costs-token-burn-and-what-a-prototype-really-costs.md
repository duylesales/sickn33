---
Title: "Bolt Costs: Token Burn and What a Prototype Really Costs"
Keywords: bolt costs, token usage, prompt efficiency, prototyping budget, AI development cost, LaunchStudio, Manifera
Buyer Stage: Awareness
Target Persona: AI-Native Founder (Non-Technical)
---

# Bolt Costs: Token Burn and What a Prototype Really Costs

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Bolt Costs: Token Burn and What a Prototype Really Costs",
  "description": "Where the credits go when building with Bolt, why the second half of a project costs more than the first, the habits that halve consumption, and how to compare the total against hiring someone.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-01-07",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/bolt-costs-token-burn-and-what-a-prototype-really-costs" }
}
</script>

The first evening with Bolt feels free. A working application appears for the cost of a subscription that seemed reasonable, and the natural conclusion is that software has become cheap.

Then the project gets bigger, each change costs more than the last, and a founder who budgeted twenty euros a month is buying credits in the third week wondering where they went.

Nothing has gone wrong. The cost structure of these tools is simply not the one people assume, and understanding it changes both how much you spend and how far you get.

## Why Costs Grow With the Project

The mechanism is straightforward once stated. Each time you ask for a change, the tool sends a substantial amount of your project to the model as context — the files it thinks are relevant, sometimes considerably more — and you pay for that context on every request.

A project with six files is cheap to change. The same project with sixty files costs several times as much per change, even for an identical request, because more is being sent each time.

Two consequences follow. The second half of a project costs materially more than the first, which is the opposite of what people budget for. And a small fix late in a project can cost more than a whole feature did at the start, which is the specific surprise that produces the complaints.

## Where the Credits Actually Go

In our experience of watching founders build, consumption divides roughly like this.

**Iteration on things that are nearly right.** Asking for an adjustment, then another, then reverting — each round costing a full pass over the context. This is the largest category by a distance.

**Debugging.** Describing a problem, receiving a fix that does not work, describing it again. Expensive because the loop is long and each turn carries the whole project.

**Large refactors.** Asking for something structural across many files, which sends and returns a great deal.

**Rebuilding what was lost.** A session that goes wrong, no version control, and the work is done again.

Notice that only one of these is producing new functionality. Most consumption is correction, and that is where the savings are.

## The Habits That Halve Consumption

**Use version control from the beginning.** This is the largest single saving. A repository means a session that goes wrong is reverted rather than rebuilt, and the difference over a project is substantial.

**Ask for one thing at a time, specifically.** "Add a delete button to the invoice row that asks for confirmation and calls the existing delete function" costs a fraction of "improve the invoice page", because the second produces a broad change you will then iterate on.

**Describe the fix, not the symptom.** When you know what is wrong, say so. "The total is wrong because the VAT is calculated before the discount" is one turn; "the total is wrong" is four.

**Do the small things yourself.** Changing a label, a colour, a number — if you can find the line, edit it. A round trip for a one-word change is the most expensive way to edit text ever devised.

**Keep the project tidy.** Fewer files, less dead code, no abandoned features. Everything that exists is potentially context on every request.

**Start a new session for a new area.** Long conversations accumulate history that travels with every message.

## Budget for the Whole Thing, Not the Tool

The subscription is the visible number and rarely the largest one. A realistic budget for taking a prototype to a live product includes the tool for a few months, the hosting and database once real usage begins, the model API if your product has an AI feature, a domain and email, and the hardening work covered throughout this series — which for most products is where the significant money is, whether paid to someone else or paid in your own time.

Set against that: an agency quote for the same product is typically €20,000 to €50,000 and three to six months. Prototyping yourself and paying for the production work is frequently a fifth of that and considerably faster, which is the actual economic case and is strong enough not to need the pretence that the tool alone is sufficient.

## Know When to Stop Prompting

There is a point in most projects where the tool stops being the efficient way to make progress: the same problem recurring across sessions, changes that break something else each time, or a structural issue the model cannot see because it only ever receives part of the picture.

Recognising that point saves both money and weeks. It is usually visible as a pattern — three sessions on one bug, or a growing reluctance to touch a particular part of the application.

That is the moment to read the code yourself, or to have someone read it. The underlying problem is generally structural and small, and an hour of human attention resolves what another twenty prompts will not.

## The Cost That Is Not on the Invoice

Credits are the visible expense and, for most founders building this way, not the largest one. Time is.

Three weeks spent on a bug that a person would find in twenty minutes is three weeks not spent on customers, and at the stage where a product is looking for its first ten users that is the expensive resource. The example above describes exactly this: the credits were annoying, the calendar was the real loss.

The calculation worth making periodically is therefore not "how much am I spending" but "what is this month producing". A month that adds two features and finds five customers is a good month regardless of the bill. A month that produced no new functionality because it was consumed by correction is a month to change something about, and the change is usually to stop prompting and read.

There is a related asymmetry founders underrate. Building the prototype is genuinely fast — days rather than months, and the tools deserve the credit they get. Everything after it, the work this series describes, runs at ordinary software speed regardless of the tool. Budgeting as though the second phase inherits the speed of the first is the single most common planning error in AI-built products, and it produces launch dates that slip by months rather than weeks.

Plan the prototype in days and the production work in weeks, and the whole thing still compares extremely well to any alternative.

## Compare the Real Alternatives

Founders debating cost usually compare the tool subscription against nothing. The useful comparison is against the ways this product could otherwise exist.

**An agency.** €20,000 to €50,000 for a product of this size, three to six months, with a specification agreed in advance and change requests priced. High confidence, slow, and the thing you get is what you asked for at the start, which for a first product is rarely what you actually need.

**A freelance developer.** €400 to €800 a day in the Netherlands, so €8,000 to €20,000 for four to six weeks. Faster and cheaper than an agency, and dependent on finding a good one who is available.

**Prototyping yourself, then paying for production work.** A few hundred euros of tool credits over two months, plus €800 to €7,500 for hardening and launch. This is the arrangement most of the founders in this series ended up with, and it is typically a quarter to a fifth of the agency route.

**Building it entirely yourself, including production.** Cheapest in money, most expensive in calendar, and it is the right answer only if you are technical enough to do the hardening properly — which, on the evidence of the incidents throughout this series, is a higher bar than it appears.

The honest summary: the tools have not made software free. They have made the exploratory half of it very cheap, which is a large and real change, and they have left the other half where it was.

## Setting This Up

For a founder building with Bolt, the practices that control cost are: version control from the first day so nothing is ever rebuilt, one specific request at a time, describing causes rather than symptoms, small edits made by hand, a tidy project with abandoned work deleted, new sessions for new areas, a budget covering hosting, database, model APIs and production work rather than the subscription alone, and a rule for when to stop prompting and read the code.

LaunchStudio takes over at exactly that point, under the Launch Ready package from €800. The engineers are Manifera's — eleven years, 160+ projects, from Amsterdam and Ho Chi Minh City.

[Tell us where your prototype has stalled](https://launchstudio.eu/en/#contact). Three sessions on one bug is usually a structural problem, not a prompting problem.

## Real example

### €740 in a Month, Then €60

Lucas Verdonschot built Inruilwaarde with Bolt: a tool that used-car dealers use to estimate trade-in values from vehicle data and their own sales history, for 14 dealers in Noord-Brabant.

His first month cost €48. His fourth cost €740, and the product was not obviously four times better. He had no version control, so two sessions that went wrong had been rebuilt by hand over several days. He asked broad questions — "make the valuation page better" — and then spent six or seven turns correcting the result. He changed labels and colours by prompting. And a bug in the mileage adjustment had consumed three separate sessions across two weeks without being fixed.

Two business days of work, then a changed way of working: the project exported into a repository with history, so a bad session is now reverted in seconds; the mileage bug read by a person and found in twenty minutes — a rounding applied twice, in two places, which the tool had been alternately fixing in one and reintroducing in the other; 11 abandoned files and a half-built feature deleted, reducing the context carried on every request; the data access consolidated so queries live in one place rather than across nineteen components; and a working agreement with himself — one specific request at a time, small edits by hand, a new session per area.

**Result:** monthly tool spend fell from €740 to about €60 and stayed there through a further four months of development. Lucas's assessment is that version control accounted for most of the saving, and that the three weeks lost to the mileage bug cost more than the credits did.

> *"I spent three weeks and a lot of money asking a tool to fix a bug it could not see, because it was two lines in two different files and it only ever looked at one of them."*
> — **Lucas Verdonschot, Founder, Inruilwaarde (Tilburg)**

**Cost & Timeline:** €1,600 (repository setup with history, diagnosis and fix of the recurring calculation bug, project cleanup, data access consolidation, working practices documented) — completed in 2 business days.

## Frequently Asked Questions

### Why does Bolt get more expensive as my project grows?

Because each request sends part of your project to the model as context, and there is more of it. The same change costs several times more in a sixty-file project than in a six-file one.

### What is the biggest saving available?

Version control. A session that goes wrong is reverted rather than rebuilt by hand, and rebuilding lost work is one of the largest consumers of credits in a typical project.

### Should I use the tool for small text changes?

No. Editing a label or a colour by hand costs nothing; a round trip for a one-word change is the most expensive way to edit text.

### How do I know when to stop prompting?

When the same problem survives three sessions, or when each change breaks something else. That pattern indicates a structural issue the model cannot see, and an hour of human reading resolves it.

### What should a realistic budget include?

The subscription, hosting and database, model APIs if you have an AI feature, a domain and email, and the production hardening work — which is usually the largest item, in money or in your own time.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Why does Bolt cost more as the project grows?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Each request sends project context to the model and there is more of it, so identical changes cost several times more in a large project."
      }
    },
    {
      "@type": "Question",
      "name": "What saves the most on AI tool costs?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Version control — a bad session is reverted instead of rebuilt, and rebuilding lost work is a major consumer of credits."
      }
    },
    {
      "@type": "Question",
      "name": "Should small text changes be prompted?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No. Edit labels and colours by hand; a round trip for a one-word change is the most expensive possible edit."
      }
    },
    {
      "@type": "Question",
      "name": "When should I stop prompting and read the code?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "When a problem survives three sessions or each change breaks something else — that indicates a structural issue the model cannot see."
      }
    },
    {
      "@type": "Question",
      "name": "What belongs in a realistic prototype budget?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "The subscription, hosting and database, model API costs, domain and email, and the production hardening work — usually the largest item."
      }
    }
  ]
}
</script>
