---
Title: "AI Development: Building a Process After Your First Hire"
Keywords: ai development, first hire, engineering process, onboarding, small team, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: SaaS Scale-Up
---

# AI Development: Building a Process After Your First Hire

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "AI Development: Building a Process After Your First Hire",
  "description": "A founder who built everything alone now has a colleague, and the habits that worked for one person do not work for two. The minimum process, what to write down first, and what to leave until later.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-03-01",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/ai-development-building-a-process-after-your-first-hire" }
}
</script>

Everything worked when there was one of you. Decisions happened in your head, context lived in your memory, and the process was whatever you did that day.

The first hire changes all of it at once, and the change is usually experienced as a slowdown: you are answering questions all day, the new person is uncertain, and the product is moving less than it did when you were alone. That phase is normal and it lasts about a month.

What determines whether it lasts a month or a quarter is how much of what was in your head is now written down.

## Write Down the Three Things First

In the first week, before anything else, three documents.

**How to run it.** Setup, environments, the commands, where things are deployed. Without this the first days are spent getting the product running, which is both expensive and demoralising.

**How this codebase works.** The conventions file this series keeps recommending: patterns, naming, the chosen library for each job, the rules that must not be broken, and the product's vocabulary. This is what stops two people producing two codebases, as the two-person team article describes.

**What the product is for.** Who the customers are, what they use it for, what matters to them. A developer who understands the business makes better decisions in the dozens of small ambiguities that arise daily, and this is the document founders least expect to need.

Everything else can wait. These three, in the first week, in the repository.

## Give Them Something Real Immediately

The instinct is to start a new person on something safe and peripheral. It wastes the first fortnight.

The better first task is small, real and in the middle of the product: a bug a customer reported, a small feature someone asked for. It is deployed within days, which establishes that the whole path works — environment, review, deployment — and it teaches more about the codebase than reading it would.

Pair on the first one, or at least walk through it together afterwards. The point is not supervision; it is that the conversation surfaces the things neither of you knew needed explaining.

## The Minimum Process for Two People

As the two-person article in this series argues, most of what is written about engineering process is for larger organisations. At two people, the useful set is short.

**Branch per change, reviewed before merge.** Five minutes on the diff, with real scrutiny for money, permissions, deletion, outbound communication and schema.

**A shared list of what is next**, in priority order, that both can see. Not a ticketing system — a list.

**A short daily conversation.** What each is doing, what is blocked. Ten minutes.

**A weekly look at what shipped and what is next.** This is where priorities get adjusted, and it is the meeting that prevents a month of building the wrong thing.

That is the whole process. Anything more at this size costs more than it returns.

## Decide Who Decides

The question that causes the most friction after a first hire, and it is rarely discussed explicitly.

Which decisions are the founder's, which are the developer's, and which are joint? Product direction and priorities are yours. Implementation approach within a task is theirs. Architecture, schema changes, adding a dependency or a service, and anything affecting customers are joint.

Say this out loud in the first week. A developer who does not know whether they may choose a library will either ask about everything, which costs your day, or choose without asking, which occasionally produces a decision you would have made differently.

## Expect to Be Slower for a Month

The founder's own output falls during onboarding, and knowing that in advance prevents the wrong conclusion.

You are answering questions, reviewing work, and writing down things you never had to articulate. That is the investment, and it pays back in the second month when the other person is productive and the third when they are independent.

The mistake is to skip the investment in order to keep shipping, which produces a developer who is dependent indefinitely and a founder who is permanently interrupted.

## Hiring Someone Who Uses the Same Tools

A question specific to this moment: should your first developer use AI tools the way you have been?

Almost certainly yes, and it is worth establishing in the interview rather than assuming. A developer who works this way will be faster in your codebase and will understand its character — the duplication, the generated patterns, the places where a session went a particular way — rather than treating it as evidence of incompetence.

Three things to agree in the first week.

**The conventions file is authoritative.** Their assistant reads it, and anything it produces that contradicts it is corrected rather than accepted.

**The same review standard applies.** Generated code is reviewed like any other, with the same scrutiny on money, permissions, deletion, outbound communication and schema. A change nobody read is a change nobody read, regardless of who typed it.

**Judgement is not delegated.** The tools write; the person decides. This is the distinction the review article in this series describes, and it is the expectation to state explicitly with someone new.

The developer to be cautious of is not the one who uses these tools heavily. It is the one who cannot explain what their assistant produced — because that is the person who will, in six months, have added a great deal to your product that nobody can account for.

## What to Add at Five People, Not Before

Founders anticipating growth sometimes install the process of a larger company early, which slows two people down to prepare for a team that may never exist.

The things genuinely worth adding later, and roughly when.

**A ticketing system with states** — around four or five people, when a shared list stops being sufficient because nobody can see what is in progress.

**Formal review with named approvers** — when there are enough people that "the other person looks at it" is ambiguous.

**On-call rotation** — when incidents are frequent enough that one person cannot absorb them, and when there is more than one person who can resolve them.

**Environments beyond three, and release branches** — when releases are coordinated across several people working to different schedules.

**Written architecture decisions in a formal process** — when the codebase is large enough that nobody has read all of it, which is later than people think.

**Estimates and planning rituals** — when commitments are being made to people outside the team.

Until then, the short list in this article is sufficient, and every addition beyond it is overhead paid daily for a benefit that arrives at a size you have not reached. The signal to add something is a recurring problem it solves, not an anticipation of one.

## Keep the Customer Contact

One risk arrives quietly with a first technical hire: the founder stops being the person who talks to customers about the product, because there is now somebody whose job that seems to be.

It is worth resisting. The founder's knowledge of what customers need is the thing that made the product work, and it decays quickly when it becomes second-hand. A feature request that reaches a developer through a summary loses the hesitation, the context and the thing the customer said afterwards — which is frequently where the actual requirement was.

Two practical arrangements. The founder stays in the support conversations, at least in the reading, for considerably longer than feels necessary. And the developer joins some customer conversations directly, which is the fastest way for them to acquire the context the business document only sketches.

The second is the one that pays. A developer who has heard three practice managers describe the same frustration builds something different from one who read a ticket, and the difference is visible in the product.

This is also the answer to the question of what the founder does while the developer builds. Not supervision — customers, which is the work that was being neglected during the two years of building alone, and the reason for hiring in the first place.

## Setting This Up

In the first month after a first hire: three documents in the first week — how to run it, how the codebase works, what the product is for; a small real task deployed within days, paired or walked through; branch-per-change with a five-minute review and real scrutiny for the five expensive categories; a shared priority list; a ten-minute daily conversation and a weekly review of what shipped; an explicit statement of which decisions belong to whom; and an acceptance that your own output falls for a month.

LaunchStudio produces exactly these documents when handing a product to a client team, which is the same problem in a different order. Behind it is Manifera — eleven years, 120+ engineers, 160+ projects, from Herengracht 420 in Amsterdam.

[Ask us to write the onboarding documents](https://launchstudio.eu/en/#contact) before your first developer starts.

## Real example

### Six Weeks of Interruptions

Nienke Baaijens built Zorgcontract in Lovable: contract and rate administration between care providers and health insurers, used by 34 providers.

She hired her first developer after two years alone. There was no documentation of any kind — no README, no conventions, nothing about the business — because she had never needed any.

The first six weeks were worse than working alone. Her developer asked between fifteen and thirty questions a day, most of which she could answer in a sentence and none of which she had written down. He spent the first three days getting the product running. He built two features in a way that did not match the rest of the codebase, because nothing described how the rest of the codebase worked, and both had to be reworked. And he twice made decisions she would have made differently — adding a charting library and changing a table structure — because nobody had said which decisions were his.

Her own output during those weeks was close to zero.

Two business days, then a different trajectory: a README covering setup and environments, written with the developer so the gaps were found by the person who had them; a conventions file written from the existing code, including the chosen library for each job and four rules that must not be broken; a two-page document describing the care sector, the customers, what they use the product for and what matters to them; a shared priority list; branch-per-change with five-minute reviews; an explicit division of decisions with architecture, schema, dependencies and anything customer-facing agreed jointly; and the two reworked features used as the worked examples in the conventions file.

**Result:** questions fell to three or four a day within a fortnight. By month three the developer was working independently on whole features and Nienke's own output had recovered and exceeded where it was when she worked alone. Her note is that the business document, which she had thought unnecessary, turned out to be the one that reduced questions most — because most of them had been about what customers actually needed rather than about code.

> *"He asked me thirty questions a day for six weeks, and I could answer every one in a sentence. Not one of those sentences existed anywhere except in my head."*
> — **Nienke Baaijens, Founder, Zorgcontract (Amersfoort)**

**Cost & Timeline:** €2,400 (README written jointly, conventions file from existing code with worked examples, business and customer context document, priority list and review process, decision boundaries) — completed in 2 business days.

## Frequently Asked Questions

### What should I write down before a first hire starts?

How to run the product, how the codebase works, and what the product is for — the last being the one founders skip and the one that reduces questions most.

### What should their first task be?

Something small, real and central — a reported bug or a requested feature — deployed within days. It establishes the whole path and teaches more than reading the code.

### How much process does a two-person team need?

Branch per change with a five-minute review, a shared priority list, a ten-minute daily conversation, and a weekly review. Anything more costs more than it returns.

### What causes the most friction after a first hire?

Undefined decision boundaries. Say explicitly which decisions are yours, which are theirs, and which are joint — architecture, schema, dependencies and anything customer-facing being joint.

### Why is my own output falling?

Because onboarding is the work. Expect a month of reduced output, and do not skip it to keep shipping — that produces permanent dependency and permanent interruption.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What documentation should exist before a first hire?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "How to run the product, how the codebase works, and what the product is for — the last reduces questions most."
      }
    },
    {
      "@type": "Question",
      "name": "What should a new developer's first task be?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Something small, real and central, deployed within days — it establishes the whole path and teaches the codebase faster than reading."
      }
    },
    {
      "@type": "Question",
      "name": "How much process does a two-person team need?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Branch per change with a short review, a shared priority list, a daily ten-minute conversation and a weekly review."
      }
    },
    {
      "@type": "Question",
      "name": "What causes friction after a first hire?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Undefined decision boundaries — state which decisions are the founder's, the developer's, and which are joint."
      }
    },
    {
      "@type": "Question",
      "name": "Why does my output drop after hiring?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Onboarding is the work. Expect a month of reduced output; skipping it produces permanent dependency and interruption."
      }
    }
  ]
}
</script>
