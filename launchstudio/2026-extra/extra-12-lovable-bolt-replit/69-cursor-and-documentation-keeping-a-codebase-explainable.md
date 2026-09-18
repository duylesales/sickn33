---
Title: "Cursor and Documentation: Keeping a Codebase Explainable"
Keywords: cursor documentation, README, architecture decisions, handover, AI readable docs, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: Technical Solo Founder / Indie Hacker
---

# Cursor and Documentation: Keeping a Codebase Explainable

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Cursor and Documentation: Keeping a Codebase Explainable",
  "description": "In a product written largely by tools, documentation is the only record of why anything is the way it is. The four documents worth having, written for both the next person and the next AI session.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-01-29",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/cursor-and-documentation-keeping-a-codebase-explainable" }
}
</script>

In a codebase written by hand, the code carries some of its own explanation. The person who wrote a function chose its structure for a reason, and even without comments the shape reflects an intention.

Generated code does not carry that. It reflects a pattern that was statistically appropriate, and the reason your product does something a particular way exists only in a conversation that has since been closed.

That makes documentation more valuable here, and it has a second audience it did not have before: the tool that will be asked to change this code next month reads the repository, and what it finds determines the quality of what it produces.

## Four Documents, Nothing More

**A README** answering how to run this thing: what it is, what it needs, the commands to set it up and start it, and where the environments are. Written for someone who has never seen the project, which includes you after four months on something else.

**A conventions file** — the one this series keeps recommending — describing patterns, naming, chosen libraries, the rules that must not be broken, and the product's vocabulary. Read by humans and by assistants.

**A decisions log.** A list of choices and why, with dates. Why Supabase rather than a database you run. Why payments go through one provider. Why invoices are immutable. Three sentences each.

**An operations page.** What runs on a schedule, what to do when something breaks, where the backups are and how to restore one, who to contact at each provider. This is the document you will be grateful for at seven on a Sunday morning.

Four files, perhaps six pages in total. More than that will not be maintained.

## Write Down Why, Not What

The code says what it does. Documentation that restates it is a second copy to keep in step, and it will not be kept in step.

What the code cannot say is why. Why this approach rather than the obvious one. Why this limit is 50 and not 100. Why this apparently redundant check exists — because a customer's import produced duplicates in March and this prevents it.

That last category is the most valuable thing you can write, because it is exactly what gets deleted by a future cleanup, human or otherwise. A comment saying "this looks unnecessary; it prevents the duplicate rows described in decision 14" is a comment that saves an incident.

## The Decisions Log Is the Highest-Value Document

It is also the one nobody writes, because at the moment of the decision the reasoning feels obvious and permanent.

Six months later it is neither. The question "why does our product do it this way" arrives from a new developer, from a customer, from an investor, or from you, and the honest answer is usually that nobody remembers.

Keep it trivially light or it will not happen. A file, a dated entry, three sentences: what was decided, what the alternatives were, why this one. Written at the moment, not retrospectively.

The entries that matter most: anything you chose against an obvious alternative, anything you would otherwise re-litigate, and anything a future reader would consider a mistake without the context.

## Write It So the Tools Can Use It

This is the part specific to building this way, and it changes what good documentation looks like.

Assistants read the repository. Documentation that states rules plainly, gives short examples, and uses consistent vocabulary measurably improves what they generate. Documentation that is discursive, or that lives in a wiki somewhere else, does nothing at all.

Three practical consequences. Keep it in the repository, in plain text, alongside the code. State rules as rules — "every endpoint must verify the caller's organisation" rather than a paragraph about the importance of authorisation. And include a short example of each pattern, because a model imitates examples far more reliably than it follows prose.

The same properties make it better for humans, which is convenient, and it means the documentation is written once for both audiences rather than twice.

## Generate the Tedious Parts, Write the Rest

An assistant is good at producing the documentation that describes structure: what this module contains, what this function takes and returns, what these endpoints are. That is genuinely useful and tedious to write.

It cannot write the why, because the why was never in the code. Asking a model to document your decisions produces plausible reasoning that was not yours, which is worse than an empty file — it is a confident record of something that did not happen.

So: generate the reference material, write the decisions yourself. Three sentences at the moment of the decision, which is the only time the reasoning is available.

## The Documentation Your Customers Need

Everything above is internal. A product also needs documentation pointed outwards, and for a small B2B product it does more work than founders expect.

Three pieces, in order of value.

**Getting started.** The shortest path from a new account to the thing your product is for. Not a tour of every feature — one sequence, with the decisions someone must make at each step. This reduces support volume more than any other single page and it is the one most products do not have.

**Answers to the questions people ask.** Taken directly from your support inbox, in the words customers use. As the SEO articles in this series note, these double as content that brings the right visitors.

**A reference for the things people configure.** Integration settings, permissions, import formats, the fields in an export. Dry, specific and consulted rather than read.

Two properties matter more than completeness. It must be current, because documentation describing a previous version of the interface is worse than none. And it should be somewhere a customer can find without asking — public, searchable, linked from inside the product at the point where each thing is done.

For a product with a handful of customers this can be five pages. The test of whether it is enough is simple: when a customer asks something, is there a page you can send them? If the answer is usually no, writing that page after answering is fifteen minutes and it never has to be answered again.

## Documentation as a Handover Asset

There is a moment, eventually, when someone other than you needs to work on the product: a contractor, an employee, an acquirer's technical reviewer, or a partner who will maintain it while you do something else.

What that person receives determines whether the transition takes a week or a quarter, and the difference is almost entirely these documents rather than the code.

With them, a competent developer can be productive in a day: they know how to run it, what the conventions are, why the unusual decisions were made, and what happens when something breaks at night.

Without them, the same person spends two weeks reading code to infer what a page would have told them, and arrives at conclusions that are sometimes wrong — because inferring intention from generated code produces confident misunderstandings, which is the same problem this article opened with.

There is a commercial dimension too. A product one person can explain is a product with a key-person risk, and any serious buyer or investor identifies it immediately. Four documents in a repository are not a substitute for a second person who knows the system, and they are the cheapest available reduction of that risk — which for a founder thinking about selling, raising, or simply taking a holiday, is worth considerably more than the half day it costs.

A useful way to test whether you have enough: hand the repository to someone who has never seen it and ask them to get it running and describe what it does. Whatever they cannot work out is what is missing, and it takes an afternoon to find out.

## Setting This Up

For an existing project this is typically half a day: a README covering setup and environments, a conventions file describing patterns, naming, chosen libraries, inviolable rules and vocabulary, a decisions log seeded with the ten choices you can still remember and their reasons, an operations page covering scheduled work, failure procedures, backups and provider contacts, comments added where code looks unnecessary but is not, reference documentation generated for structure, everything in the repository as plain text, and a habit of writing the decision entry at the moment rather than afterwards.

LaunchStudio produces all four when handing a product back to its owner, because a product you cannot explain is one you cannot hand to anyone. The engineers are Manifera's — eleven years, 160+ projects, from Amsterdam and Ho Chi Minh City.

[Ask us what your project would look like to someone who has never seen it](https://launchstudio.eu/en/#contact).

## Real example

### The Check Nobody Could Explain

Pieter-Jan Osseweijer built Subsidieaanvraag in Cursor: grant application administration for agricultural advisers and their clients, handling around 900 applications a year for 26 advisory firms.

An AI session tidying the validation code removed a condition that looked redundant: a check rejecting applications where the parcel area exceeded a threshold relative to the registered holding. It had no comment and no test, and nothing in the code explained it.

It existed because a provincial authority had rejected 40 applications the previous year for exactly that mismatch, and the check had been added to catch it before submission.

The removal went unnoticed for two months. Thirty-one applications were submitted with the mismatch and rejected, several past the deadline for that round, which for four farms meant missing a funding window entirely.

Three business days: the check restored with a comment explaining what it prevents and a test derived from the authority's published rules; a decisions log started, seeded with fourteen entries covering the choices Pieter-Jan could still reconstruct — why applications are immutable after submission, why the provincial rules are stored as data rather than code, why one provider was chosen for document generation; a README covering setup and environments, which had never existed; a conventions file stating patterns, naming and four inviolable rules; an operations page covering the nightly submission job, backups, restore procedure and provider contacts; comments added to six further pieces of code that looked unnecessary and were not, each referencing its decision entry; and reference documentation generated for the endpoint structure.

**Result:** no further checks have been removed. Pieter-Jan reports that the decisions log has been consulted more often than he expected — twice by an adviser asking why the product behaves a certain way, once by a provincial authority, and repeatedly by himself.

> *"A session removed a check that looked pointless. It was pointless unless you knew that forty applications had been rejected for exactly that reason the year before, and nothing in my product knew that."*
> — **Pieter-Jan Osseweijer, Founder, Subsidieaanvraag (Leeuwarden)**

**Cost & Timeline:** €2,500 (check restoration with rule-derived tests, decisions log with fourteen seeded entries, README, conventions file, operations page, explanatory comments across six locations, generated reference documentation) — completed in 3 business days.

## Frequently Asked Questions

### Why does documentation matter more in an AI-built product?

Because generated code carries no intention. The reason your product works a particular way exists only in a closed conversation, and the next session — human or machine — has no access to it.

### What should I actually write?

Four documents: how to run it, the conventions, a decisions log with dates and reasoning, and an operations page. About six pages in total.

### What is the highest-value document?

The decisions log. Six months later nobody remembers why a choice was made, and that reasoning is what prevents a future cleanup from removing something load-bearing.

### Can I generate documentation with the assistant?

The reference material describing structure, yes, and it is a good use of it. Not the reasoning — a model asked why you made a decision will produce plausible reasoning that was not yours.

### How do I keep documentation from going stale?

Keep it short, keep it in the repository, and write decision entries at the moment rather than retrospectively. Anything longer than a few pages will not be maintained.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Why does documentation matter more in AI-built products?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Generated code carries no intention — the reasons live in closed conversations, inaccessible to the next person or session."
      }
    },
    {
      "@type": "Question",
      "name": "What documentation does a small product need?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "A README, a conventions file, a decisions log with dates and reasoning, and an operations page — about six pages total."
      }
    },
    {
      "@type": "Question",
      "name": "Which document is most valuable?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "The decisions log — it preserves reasoning that would otherwise be lost and prevents future cleanups removing load-bearing code."
      }
    },
    {
      "@type": "Question",
      "name": "Can an assistant write my documentation?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Structural reference material yes; reasoning no — it will produce plausible justifications that were never yours."
      }
    },
    {
      "@type": "Question",
      "name": "How do I stop documentation going stale?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Keep it short and in the repository, and write decision entries at the moment of deciding rather than afterwards."
      }
    }
  ]
}
</script>
