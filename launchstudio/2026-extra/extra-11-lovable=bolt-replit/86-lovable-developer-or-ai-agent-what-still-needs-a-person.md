---
Title: "Lovable Developer or AI Agent: What Still Needs a Person"
Keywords: lovable developer, ai agent, lovable expert, vibe coding developer, ai app security, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: AI-Native Founder (non-technical)
---

# Lovable Developer or AI Agent: What Still Needs a Person

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Lovable Developer or AI Agent: What Still Needs a Person",
  "description": "Agents write code well and cannot decide what your product should protect, promise or become. An honest division of labour, and the four failure modes that show a task needed a person.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-08-27",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/lovable-developer-or-ai-agent-what-still-needs-a-person" }
}
</script>

A reasonable question, asked more often every month: if the tooling keeps improving, why hire anybody?

It deserves a straight answer rather than a defensive one. Agents genuinely write good code. They are faster than a person at most implementation tasks, they do not get bored, and they are improving quickly. Anyone selling development who pretends otherwise is not worth listening to.

The useful distinction is not between things AI can do and things it cannot. It is between decisions that follow from information the agent has, and decisions that depend on things only you or someone accountable can know.

## What Agents Do Better Than Most People

Stated plainly, because the rest only makes sense against it.

Implementing a described feature. Writing boilerplate — forms, tables, validation, the plumbing between a database and a screen. Translating between languages and frameworks. Explaining unfamiliar code. Producing a first draft of almost anything. Finding a syntax error faster than you can see it.

For a founder building a product, this is transformative and not in dispute. Most of what a junior developer was hired to do five years ago is now a prompt, and that is a good thing.

## What Depends on Knowledge the Agent Does Not Have

Four categories.

**What your data means.** Which fields are sensitive, which combinations identify a person, what a competitor must never see, what a customer contractually requires. An agent can implement any access model you describe and cannot tell you which one is right, because rightness depends on your customers and your commitments.

**What your product promises.** Whether a failed payment should retry or restrict, what happens to data when someone cancels, whether a feature should be capped or unlimited. These are commercial decisions with financial consequences, and an agent asked to decide will produce something reasonable and generic.

**What is worth building.** The judgement that this feature matters and that one does not, that a customer's request represents a pattern or an exception. This comes from talking to customers, which is not an activity an agent performs.

**Who is accountable.** When a regulator, a customer's lawyer or an insurer asks who is responsible for a decision, "the tool suggested it" is not an answer. Someone must own the choice.

## The Judgement Problem Is Structural

There is a specific asymmetry worth understanding, because it explains most of the failures.

An agent optimises for the request succeeding. Ask it to fix a permissions error and removing the permission check satisfies the request perfectly. Ask it to make a query faster and removing a filter may do so. Ask it to make a feature work and it will install whatever makes that true.

None of this is a defect. It is what "make this work" means when the system has no model of what must remain true. A person with context supplies the constraint the request omitted — and the more capable the agent, the more efficiently it will pursue a goal you specified incompletely.

This is why the review habit matters more as the tooling improves rather than less.

## The Four Signs a Task Needed a Person

Recognisable in retrospect, and worth learning to spot in advance.

**It worked and something else broke.** A change with consequences the request did not mention — a feature fixed, a report now wrong.

**Nobody can say why it is like that.** Six months later a decision exists and nobody chose it. This is the most common finding in an assessment of an AI-built product.

**It is right in the general case and wrong in yours.** Generated code follows common patterns, and your business is not the common case in the two or three places that matter most.

**It cannot be explained to a customer.** A procurement reviewer asks how access is controlled, and the honest answer is that it was generated. That is the moment the absence of a decision becomes commercial.

## An Honest Division of Labour

For a founder building with AI tooling, this is what works.

**Agent, with your review:** features, screens, the ordinary plumbing, refactoring, first drafts, explanations of unfamiliar code.

**You:** what the product does, for whom, what it charges, what it promises, what matters when something fails.

**Someone accountable, once real customers exist:** the access model, anything touching money, data durability and recovery, deployment and secrets, and the answers a business customer will demand.

That last list is short, bounded, and mostly a one-off. It is not a permanent developer; it is a few days of work at the point where the product stops being an experiment.

## What "Hiring" Actually Means Now

The shape of the work has changed even though the need has not.

Five years ago hiring a developer meant hiring someone to write the product. Now it usually means hiring someone for a defined piece of judgement-heavy work: reviewing what was generated, deciding the access model, making the data survivable, and documenting it so you can keep building.

This is why fixed-scope engagements suit AI-built products so well. The work is bounded, the findings repeat across projects, and the outcome is verifiable — which is also why LaunchStudio prices it in fixed bands from €800 to €7,500 rather than by the hour.

The founder keeps building. Someone else takes responsibility for the parts where being wrong is expensive.

## Working Well With Both

Three habits make the combination stronger than either alone.

**State the constraints when you prompt.** "Access to this table is owner-only. This runs on the server. Do not add dependencies without telling me." Constraints given up front are honoured far more reliably than corrections applied afterwards.

**Review what changed, not just whether it works.** Dependencies added, configuration touched, anything near data access or credentials.

**Bring a person in before the commitment, not after the incident.** Before the first paying customer, before the first business contract, before the first integration with somebody else's system. Those are the points where a decision becomes expensive to change.

## What Changes as the Tooling Improves

A fair question to ask of any article like this: does the argument survive the next generation of tools?

Parts of it will not, and it is worth being explicit about which.

**The implementation gap will keep closing.** Tasks that need a person today because the output is unreliable will not need one in two years. Anyone whose value rests on writing code faster than an agent is in a shrinking position, and pretending otherwise helps nobody.

**Agents will increasingly catch their own omissions.** Access rules, error handling, tests — the things currently absent because nobody asked are exactly the things tooling will start supplying by default. Some of the findings in this article will look dated, which is a good outcome.

**What will not change is accountability.** Somebody has to be answerable for a decision when a customer's lawyer, an insurer or a supervisory authority asks. That role cannot be delegated to a tool, not because tools are untrustworthy but because accountability is a relationship between people and institutions. A supplier telling a hospital's procurement team that the access model was generated has not answered the question.

**Nor will the knowledge gap.** What your data means, what you promised a customer, what your contract commits you to, what matters when something fails — these live outside any codebase. The better the tooling gets, the more the remaining work consists of supplying exactly this context, which means prompting becomes specification and specification has always been the hard part.

**And the asymmetry will persist.** A system optimising for a stated goal will pursue it efficiently, including in ways the request did not anticipate. More capable tools make this more consequential rather than less, which is why the constraints you state up front matter more each year, not less.

The practical implication for a founder is stable across all of this: keep building with the tools, state your constraints explicitly, and make sure a person is accountable for the decisions where being wrong is expensive.

## Where LaunchStudio Fits

Not as a replacement for the way you build. As the accountable party for the parts that need one: the access model written and verified by attempting to bypass it, credentials and secrets handled properly, data made durable with backups actually restored, deployment made reproducible, monitoring in place, and the whole thing documented so you can answer a customer's questions and keep working with your agent afterwards.

The engineers are Manifera's: eleven years and 160+ production projects, for clients including Vodafone, TNO and CFLW, from Amsterdam Herengracht 420, Singapore and Ho Chi Minh City.

[Tell us what you have built and who is starting to depend on it](https://launchstudio.eu/en/#contact), or see the [packages](https://launchstudio.eu/en/#packages).

## Real example

### Four Sessions, Four Reasonable Decisions, One Wrong Product

Gijs Wagenaar built Kweekplan with Lovable: cultivation planning for greenhouse growers, used by six horticultural businesses around Naaldwijk and Honselersdijk. Planting schedules, labour forecasts, yield tracking.

He was working almost entirely with agent sessions and it was going well. The product did what growers wanted, and two of them were paying.

The problem surfaced when a third grower, larger and part of a cooperative, asked three questions before signing. Could their agronomist have read-only access without seeing labour costs. Where was the data stored. And what happened to their yield history if they stopped.

None had an answer, and investigating produced a fourth problem. Across four separate sessions, four reasonable decisions had been made that nobody had chosen. Access was per-user, so a grower's colleague could not see shared plans — which had been worked around by sharing logins. Yield figures were stored with a rounding that made two growers' historical numbers disagree with their own records. Deletion removed the plan and left the attached photographs. And an agent session, asked to fix a slow dashboard, had removed a filter, so one grower's planting density appeared in another's comparison view.

Each decision was defensible in isolation. Together they were a product that could not be sold to a cooperative.

Ten business days of work: an organisation and role model introduced so growers, colleagues and external agronomists have defined access, with labour cost restricted to owners; the shared logins split into individual accounts; the dashboard filter restored and every aggregate audited for the same fault; rounding corrected and historical figures recalculated against the growers' own records, with the discrepancy explained to both; deletion made complete across records and files; data location and retention documented; and a written access model produced that Gijs could send.

**Result:** the cooperative grower signed, and brought two further members. Gijs continues to build with agent sessions — the difference, he says, is that he now states the access rule in the prompt and reads what changed.

> *"Four sessions made four sensible decisions and produced a product I could not sell. Not one of them was a mistake on its own."*
> — **Gijs Wagenaar, Founder, Kweekplan (Naaldwijk)**

**Cost & Timeline:** €4,800 (organisation and role model, aggregate audit, data correction, complete deletion, documentation) — completed in 10 business days.

## Frequently Asked Questions

### Can an AI agent replace a developer entirely?

For implementation, increasingly yes. For decisions that depend on what your data means, what your product promises, what is worth building and who is accountable, no — because those depend on information the agent does not have.

### Why do agents remove security checks?

Because they optimise for the request succeeding. "Fix this permissions error" is satisfied perfectly by removing the check. The constraint has to be supplied by the person prompting, which is why review matters more as tooling improves.

### How do I know a task needed a person?

Four signs: it worked and something else broke; nobody can say why a decision is the way it is; it is right in general and wrong in your specific case; and you cannot explain it to a customer who asks.

### When should I bring someone in?

Before the commitment rather than after the incident — before your first paying customer, first business contract, or first integration with someone else's system. Those are the points where a decision becomes expensive to change.

### Does hiring mean a permanent developer?

Usually not. For AI-built products it typically means a bounded engagement covering the judgement-heavy parts — access model, money, data durability, deployment, documentation — after which you keep building yourself.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Can an AI agent replace a developer entirely?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "For implementation, increasingly yes; for decisions about what data means, what the product promises, what is worth building and who is accountable, no."
      }
    },
    {
      "@type": "Question",
      "name": "Why do agents remove security checks?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "They optimise for the request succeeding, and removing a check satisfies 'fix this permissions error' perfectly. The constraint must come from the person prompting."
      }
    },
    {
      "@type": "Question",
      "name": "How do I know a task needed a person?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "It worked and something else broke; nobody can say why a decision exists; it is right generally and wrong for you; or you cannot explain it to a customer."
      }
    },
    {
      "@type": "Question",
      "name": "When should I bring someone in?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Before the first paying customer, business contract or external integration — the points where a decision becomes expensive to change."
      }
    },
    {
      "@type": "Question",
      "name": "Does hiring mean a permanent developer?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Usually a bounded engagement covering access model, money, data durability, deployment and documentation, after which you keep building yourself."
      }
    }
  ]
}
</script>
