---
Title: "Lovable Developer: Writing a Brief an Engineer Can Quote"
Keywords: lovable developer, project brief, scoping, quotes, hiring a developer, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: AI-Native Founder (Non-Technical)
---

# Lovable Developer: Writing a Brief an Engineer Can Quote

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Lovable Developer: Writing a Brief an Engineer Can Quote",
  "description": "A vague brief produces a vague quote and a difficult project. What an engineer needs to know about your Lovable app to price the work honestly, in one page you can write in an hour.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-02-18",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/lovable-developer-writing-a-brief-an-engineer-can-quote" }
}
</script>

"I built something in Lovable and I need help finishing it" is how most of these conversations begin, and it is not enough to price. The engineer reading it does not know whether you have twenty customers or none, whether money moves through the product, or whether "finishing" means a fortnight or a quarter.

What follows is either a quote with a large margin for uncertainty, or a discovery call that establishes in forty minutes what a page would have said. Both cost you.

The brief that gets an accurate quote takes an hour to write, and writing it is useful even if you never send it.

## What the Engineer Actually Needs

Seven things, in this order.

**What the product does and who uses it.** Two sentences, in plain language, with the type of customer named. "Scheduling software for physiotherapy practices; practice managers book appointments and patients confirm them by email."

**Where it is now.** How long you have been building, how many customers use it, whether money moves through it, and whether it is live. A live product with paying customers is a different engagement from a prototype.

**What you want to happen.** Be concrete: "I want to take payments, be confident it is secure, and launch to 50 practices in March." A goal with a date and a number is quotable; "make it production-ready" is not.

**Access.** A link to the repository, or a note saying it lives in Lovable and has never been exported. This single fact changes the assessment more than any other.

**What you know is wrong.** The bug you cannot fix, the page that is slow, the thing you suspect is insecure. Nobody will think less of you and it saves an hour of discovery.

**Constraints.** Your budget range, your deadline, anything the product must keep — a customer's integration, a design somebody paid for, a platform you cannot leave.

**Who you are in this.** Will you keep building alongside them, hand it over entirely, or something between? This determines how the work is structured and is the question most often left unanswered.

## Say the Budget

Founders withhold the number believing it produces a better price. It produces a worse process.

An engineer who knows you have €3,000 will tell you what €3,000 buys and what it does not, which is a useful conversation. One who does not know will either quote for everything — a number that frightens you — or quote for the minimum and discover mid-project that you expected more.

A range is enough. "Between €2,000 and €5,000, depending on what is necessary" is honest, and any competent supplier will tell you which end your situation falls at.

## Describe the Product, Not the Solution

The most common failure in these briefs is specifying the implementation. "I need you to add Redis caching and move to a microservices architecture" is a brief from someone who has read something, and it constrains the engineer to an approach that may not be the right one.

Describe the problem instead. "The appointment list takes eight seconds for our largest practice." An engineer can then tell you it is a missing index and an hour of work, rather than quoting for the architecture you asked for.

This is also the difference between a supplier who solves your problem and one who builds what you specified. You want the first, and the brief is where you make that possible.

## Include the Boring Facts

Four details that change a quote materially and are almost always omitted.

**How much data.** A product with 500 records and one with 500,000 are different engagements.

**How many customers and how they are separated.** One organisation per account, or several users sharing? Multi-tenancy is the single largest structural factor.

**What it integrates with.** Every external service — payments, email, accounting, an industry system. Integrations are where estimates go wrong.

**Whether anyone else has worked on it.** A codebase with two previous contractors' approaches in it takes longer to work in than one with a single author, even if that author was a tool.

## What You Get Back

A brief like this should produce a quote that names what is included, what is not, what it costs, how long it takes, and what happens if something unexpected is found.

If what comes back is a single number with no breakdown, ask for the itemisation. An engineer who cannot list the work is an engineer who has not thought about it, and a fixed price without a scope is a dispute waiting for a reason.

And expect a good supplier to tell you that part of what you asked for is unnecessary. That is the strongest signal you will get about whether they are solving your problem or selling you hours.

## Give Access Properly

Half the delay in these engagements is administrative, and it is entirely avoidable with twenty minutes of preparation before the work starts.

What a supplier needs, and what to prepare.

**The code**, in a repository they can be added to. If it has never been exported from the building tool, do that first — it is the step that otherwise consumes the first day of a paid engagement.

**A working environment**, or a note explaining what is missing. A supplier who cannot run your product spends their first hours getting it running, at your expense.

**Read access to the relevant dashboards** — hosting, database, payment provider, email — rather than the account password. Most platforms support adding a collaborator, and doing it that way means removing access afterwards is one click rather than a rotation.

**Test accounts** at each permission level, so they can see the product as your customers do.

**A contact** who can answer questions within a day. An engagement where questions wait three days for an answer takes three times as long, and you pay for the waiting.

And agree the offboarding at the same time as the onboarding: access removed and credentials rotated when the work ends, as the secrets article in this series describes. Deciding that at the start makes it routine rather than awkward.

## The Questions That Reveal a Good Supplier

You are assessing them while they assess your brief, and the questions they ask are the most reliable signal available.

The ones that indicate someone who has done this before.

**"Is the product live, and what happens to customers while we work?"** Anyone who does not ask this is planning to work as though nobody is using it.

**"What is the largest account's data volume?"** The performance and correctness problems live there, as several articles in this series describe, and an engineer who asks has met that before.

**"Who else has access to the code and the accounts?"** A security-minded question and a practical one.

**"What happens if we find something serious?"** The answer should be that they tell you immediately with options, rather than either fixing it silently or stopping work.

**"What do you want to be able to do yourself afterwards?"** A supplier who asks this is planning a handover rather than a dependency.

And one thing they should tell you without being asked: what they are not going to do. A quote that includes everything you mentioned, with no boundaries stated, is one where the boundaries will be discovered during the work.

The suppliers to be cautious of are those who quote immediately from a two-sentence description, those who propose a rebuild before reading the code, and those who cannot name what is excluded.

A rebuild proposed before anyone has read the code is the clearest warning of the three. As the Bolt article in this series argues, most AI-built products have a sound enough structure to build on, and a supplier reaching for a rewrite is usually pricing their own comfort rather than your problem.

The exception is a codebase where the data model cannot represent what the business needs, which is visible on inspection and is a genuine reason. If that is the diagnosis, ask them to show you which part and why.

## Setting This Up

Before contacting anyone, write one page covering: what the product does and who uses it, where it is now including customers and revenue, what you want to happen with a date and a number, access to the code or a note that it has never been exported, what you already know is wrong, your budget range and hard constraints, your own intended role afterwards, and the boring facts — data volume, tenancy, integrations, previous contributors. Describe problems rather than solutions.

LaunchStudio quotes from exactly this, and the Launch Ready package starts at €800 for a prototype that needs securing and launching. Behind it is Manifera — eleven years, 160+ projects, 120+ engineers, from Herengracht 420 in Amsterdam.

[Send us your page](https://launchstudio.eu/en/#contact) and we will come back with an itemised quote rather than a discovery call.

## Real example

### Three Quotes That Could Not Be Compared

Machiel Verduijn built Bandenwissel in Lovable: seasonal tyre change scheduling and storage administration for independent garages, with 14 garages using it and around 4,000 stored tyre sets.

He approached three suppliers with the same message: that he had built something in Lovable and needed help making it production-ready.

The quotes were €2,400, €11,000 and €38,000. None of them could be compared, because each had assumed a different scope. The first had assumed a security review. The second had assumed security, payments and a launch. The third had assumed a rebuild, because the enquiry had not mentioned that the product was already live with customers and that a rebuild would mean a migration.

He spent three weeks in calls establishing what each had meant.

Two hours of writing, then a different outcome: a one-page brief stating what the product does and that 14 garages use it daily; that it is live, holds 4,000 records and takes no payments yet; that the goal is to accept payments and onboard 40 garages before the October tyre season, a date with a number; a link to the repository, exported that morning; three known problems named — a slow list page for the largest garage, uncertainty about whether garages could see each other's data, and an email that sometimes does not arrive; a budget range of €4,000 to €9,000; a constraint that the product must stay live throughout; and a statement that he intends to keep building features himself afterwards.

**Result:** the three revised quotes came back at €5,200, €6,800 and €7,500 — comparable, itemised, and all within his range. Two of the three told him unprompted that his slow page was probably an index rather than an architecture problem. He chose the middle quote, and the work took nine days against an estimate of eight.

> *"Three quotes, from twenty-four hundred to thirty-eight thousand, for what I thought was the same question. It was not the same question — I had asked three different things without realising it."*
> — **Machiel Verduijn, Founder, Bandenwissel (Emmen)**

**Cost & Timeline:** €6,800 (security review and remediation, multi-tenant separation, payment integration, email deliverability, performance work, launch support) — completed in 9 business days.

## Frequently Asked Questions

### Should I tell a supplier my budget?

Yes, as a range. Without it you receive either a quote for everything or a quote for the minimum, and neither matches what you actually need.

### What is the single most useful fact to include?

Whether the code is in a repository you control or has never left the tool. It changes the assessment more than anything else in the brief.

### Should I specify the technical solution?

No. Describe the problem — "this page takes eight seconds for our largest customer" — and let the engineer diagnose. Specifying an implementation frequently buys the wrong work.

### What should a good quote contain?

What is included, what is explicitly not, the price, the duration, and what happens if something unexpected is found. A single number with no breakdown is a dispute waiting to happen.

### How do I tell a good supplier from a poor one?

The good ones tell you that part of what you asked for is unnecessary, and ask about your data volume, your tenancy model and your integrations before quoting.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Should I share my budget with a developer?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes, as a range. Otherwise you get a quote for everything or for the minimum, neither matching what you need."
      }
    },
    {
      "@type": "Question",
      "name": "What is the most important fact in a brief?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Whether the code is in a repository you control or has never left the building tool — it changes the assessment most."
      }
    },
    {
      "@type": "Question",
      "name": "Should a brief specify the technical solution?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No. Describe the problem and let the engineer diagnose; specifying an implementation often buys the wrong work."
      }
    },
    {
      "@type": "Question",
      "name": "What should a quote include?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Inclusions, explicit exclusions, price, duration, and what happens if something unexpected is found."
      }
    },
    {
      "@type": "Question",
      "name": "How do I recognise a good supplier?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "They tell you which parts are unnecessary and ask about data volume, tenancy and integrations before quoting."
      }
    }
  ]
}
</script>
