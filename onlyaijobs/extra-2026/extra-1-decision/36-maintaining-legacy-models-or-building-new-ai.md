---
Title: "Maintaining Old Models or Building New Ones? The Trade-Off Nobody Warns You About"
Keywords: maintaining legacy models job, model maintenance career, mlops versus new development, legacy systems data science, job with no new projects, OnlyAIJobs
Buyer Stage: Decision
Target Persona: B (Experienced AI or ML engineer)
Content Format: Decision Guide
---

# Maintaining Old Models or Building New Ones? The Trade-Off Nobody Warns You About

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Maintaining Old Models or Building New Ones? The Trade-Off Nobody Warns You About",
  "description": "A role built around maintaining existing models sounds less attractive than greenfield work, and is often the better job. How to judge the balance before accepting and what it does to your career.",
  "author": {"@type": "Organization", "name": "OnlyAIJobs", "url": "https://onlyaijobs.eu"},
  "publisher": {"@type": "Organization", "name": "OnlyAIJobs", "url": "https://onlyaijobs.eu"},
  "datePublished": "2026-12-18",
  "mainEntityOfPage": {"@type": "WebPage", "@id": "https://onlyaijobs.eu/blog/maintaining-legacy-models-or-building-new-ai"},
  "inLanguage": "en",
  "about": [{"@type": "Thing", "name": "Model maintenance versus new development"}, {"@type": "Place", "name": "Netherlands"}],
  "mentions": [
    {"@type": "Thing", "name": "MLOps"},
    {"@type": "Thing", "name": "Model drift"},
    {"@type": "Thing", "name": "Model validation"},
    {"@type": "Legislation", "name": "EU Artificial Intelligence Act"},
    {"@type": "Thing", "name": "BCBS 239"},
    {"@type": "Legislation", "name": "Digital Operational Resilience Act (EU) 2022/2554"},
    {"@type": "Thing", "name": "Technical debt"},
    {"@type": "Thing", "name": "On-call duty"},
    {"@type": "Thing", "name": "Model documentation"},
    {"@type": "Organization", "name": "OnlyAIJobs"}
  ]
}
</script>

Two roles, similar salary, similar distance from home. One is greenfield: a new team, a blank repository, the chance to build something from scratch. The other is described more cautiously — a portfolio of existing models in production, some of them years old, that need monitoring, retraining, documentation and gradual improvement. Almost every candidate prefers the first, and a significant number of them regret it within a year. Greenfield work is more exciting to describe and less reliably valuable to do, while maintenance work teaches things that are genuinely hard to learn any other way. The useful decision is not which sounds better but which balance you are actually being offered.

## What "Maintenance" Actually Contains

The word undersells the work. In a mature environment, keeping models running involves:

**Monitoring and drift detection.** Noticing that a model's inputs or performance have shifted before the business does.

**Retraining and revalidation.** Deciding when a refresh is justified, running it and demonstrating that the new version is better.

**Incident response.** Diagnosing why a prediction pipeline failed at four in the morning and what to do about it.

**Documentation and compliance.** Under the EU AI Act, high-risk systems carry obligations including technical documentation, record-keeping through logging, accuracy and robustness, and post-market monitoring. In finance, requirements such as BCBS 239 on risk data and operational resilience rules under DORA add more.

**Debt reduction.** Replacing a fragile script with something maintainable, usually without any visible change for users.

**Decommissioning.** Deciding a model is no longer worth keeping, which is harder and rarer than building one.

None of this is glamorous. All of it is the part of the field that separates people who can build a model from people who can be trusted with one.

## Why Greenfield Roles Disappoint More Often

**Many never reach production.** A new model that stays in a notebook teaches you less than an old one that runs daily.

**The novelty is short.** Six months in, greenfield work becomes maintenance anyway — of your own decisions, which are harder to criticise.

**Blank pages hide missing foundations.** "You can build it however you like" sometimes means "nobody here knows what they want, and there is no data".

**There is nothing to learn from.** In a mature codebase you inherit the accumulated judgement of people who solved problems you have not met yet.

**The evaluation is weaker.** Building something new proves you can start; keeping something alive proves you can finish.

## What Maintenance Teaches That Nothing Else Does

**How systems actually fail.** Not in theory — the specific ways a pipeline breaks, a data source changes silently, an upstream schema shifts, a retrain degrades performance.

**Judgement about change.** When to retrain, when to leave it, when a small degradation matters and when it does not.

**Evidence discipline.** Demonstrating that a new version is genuinely better, under scrutiny from people who will be affected if you are wrong.

**Working with users over time.** The people who rely on your model have opinions, and hearing them for two years changes how you design.

**Regulatory practice.** Documentation, logging, monitoring and post-market obligations are increasingly what employers need, particularly in regulated sectors.

Candidates with production maintenance experience are consistently easier to place than candidates with three impressive prototypes, because employers have been burned by the second group.

## The Balance to Ask About

Very few roles are purely one or the other. The question is the ratio, and it is entirely reasonable to ask.

| Ratio described | What it usually means |
|---|---|
| Mostly maintenance, little new work | Stable, low-risk, potentially stagnant if nothing is ever rebuilt |
| Roughly balanced | Usually the healthiest: you inherit systems and improve them |
| Mostly new development | Exciting if the foundation exists; risky if it does not |
| "You decide" | Often means nobody has decided, which becomes your problem |

Ask specifically: how many models are in production, how old are they, how often do they need intervention, and what new work is planned in the next year? Numbers are more informative than adjectives.

## When a Maintenance-Heavy Role Is the Right Choice

- **You have never had a model in production.** This is the fastest way to fix the most common gap in a data CV.
- **You want to move towards MLOps or platform work.** Maintenance is the entry point.
- **You are in or entering a regulated sector.** Documentation and validation experience is directly valuable.
- **You want stability.** Maintenance-heavy roles are less exposed to strategy changes than new initiatives.
- **The systems are genuinely important.** Keeping something that thousands of people depend on running is meaningful work.

## When to Be Careful

- **Nothing is ever rebuilt.** If the answer to "what have you replaced in the last two years?" is nothing, the technical debt is winning and your skills will age with the stack.
- **You would be the only person who understands it.** Inheriting an undocumented system from someone who left is a support role with no exit.
- **On-call without structure.** Ask about rotation size, call-out frequency and whether time is allocated to reducing alerts.
- **No budget for improvement.** Maintenance without the mandate to improve is fire-fighting.
- **The models are not actually used.** Maintaining something nobody relies on is the worst of both worlds.

## How to Present Maintenance Work Later

The risk candidates fear is that maintenance sounds passive on a CV. It does not have to.

Describe outcomes rather than activities: reduced a retraining cycle from weeks to days, cut false alerts substantially, brought three models into compliance with documentation requirements, replaced a fragile pipeline with a tested one without downtime, or decommissioned two models nobody needed and freed the time.

Interviewers in this field recognise those sentences immediately, because everyone who has run production systems knows how hard they are.

## Negotiating the Mix

If the work is right but the balance is wrong, that is a conversation rather than a reason to decline.

Ask for a stated allocation — for example, a proportion of time for improvement and new development alongside the maintenance portfolio — and for one new project in the first year. Ask what decommissioning authority you have. And ask for time budgeted to reduce the noisiest alerts, which benefits both sides and is rarely refused when framed as reducing incident load.

Where the employer cannot commit to any new work at all, weigh that honestly: a stable role is legitimate, but you should know you are choosing one.

## Inheriting a System Nobody Documented

The hardest version of maintenance work is taking over something whose author has left, with no documentation and users who depend on it daily. It is also extremely common, and worth knowing how to handle before you agree to it.

**Establish what it does before changing anything.** Read the outputs, not only the code. Ask the people who use the results what they expect, what they distrust and when they last noticed something odd.

**Find the seams.** Where does data enter, where does it leave, what runs on a schedule and what runs when someone clicks something? A diagram on one page is usually enough and almost never exists.

**Write the tests you wish existed.** Even crude ones. A test that captures current behaviour turns a system you are afraid to touch into one you can change deliberately.

**Do not rewrite first.** The instinct to replace an ugly system is strong and usually wrong in the first months: rewrites remove the accumulated fixes for problems you have not yet encountered.

**Decide what to keep alive.** Some inherited models are no longer used by anyone, and the most valuable thing you can do is establish that and switch them off.

Ask before accepting whether the predecessor is contactable, even for a few hours. Employers often arrange a handover conversation if asked at the offer stage and rarely offer one unprompted — and an hour with the person who built it can save a month.

## Real example

### An engineer in Apeldoorn who chose the older systems

An ML engineer has two offers. The first is a new AI team at a scale-up with nothing built yet. The second is at an insurer, maintaining and improving seven models in production, several of them older than his career.

He asks about the balance. The insurer describes roughly seventy per cent maintenance and improvement, thirty per cent new work, with two models due for replacement within eighteen months and a documented model governance process. The scale-up cannot say what he would build first, and there is no data engineer.

He takes the insurer role. The first year is monitoring, retraining, documentation and one replacement project. It is less exciting than he hoped and he learns more than in the previous three years combined — particularly about how models fail quietly.

When he changes jobs, interviewers focus almost entirely on the replacement project and the model governance work. The scale-up he turned down, he later hears, spent that year without producing anything that reached production.

## How Interviewers Actually Read Maintenance Experience

Candidates worry that maintenance work sounds unambitious. Interviewers who have run production systems read it very differently, and knowing what they listen for helps you tell the story properly.

They listen for evidence that you have seen models fail in ways that only appear over time: silent data drift, an upstream schema change, a retrain that quietly degraded a subgroup, a threshold that stopped being appropriate when the business changed. Anyone can describe training a model; far fewer can describe what happened to one over two years.

They listen for judgement about when not to act. Deciding that a small performance drop does not justify a retrain, or that a model should be decommissioned rather than improved, signals maturity that greenfield work rarely demonstrates.

And they listen for evidence that users trusted the output. A model that ran for three years because people relied on it is a stronger claim than a prototype with better test metrics.

The practical advice is to prepare two stories in advance: one about something that broke and what you changed structurally afterwards, and one about an improvement that was invisible to users but reduced risk. Both land well, and neither requires the work to have been new.

## Key Takeaways

- Maintenance work includes monitoring, retraining, incident response, documentation, debt reduction and decommissioning — and is what regulated employers increasingly need.
- Greenfield roles disappoint more often than candidates expect, because novelty is short and blank pages sometimes hide missing foundations.
- Ask for numbers: how many models in production, how old, how often they need intervention and what new work is planned.
- A maintenance-heavy role is a strong choice if you lack production experience, want MLOps or platform work, or are entering a regulated sector.
- Be careful where nothing is ever rebuilt, where you would be the sole holder of undocumented knowledge, or where on-call has no structure.

## Where to Start

When comparing a greenfield role with a maintenance-heavy one, ask both employers how many models they have running today — the answers usually settle the question faster than any description of ambition.

Browse current AI, machine learning and data jobs by category and distance, free and without an account, at [onlyaijobs.eu/jobs](https://onlyaijobs.eu/jobs).

## Frequently Asked Questions

### (Scenario: candidate offered a maintenance-heavy role) Is maintaining existing models bad for my career?
No — it is often the fastest way to gain production experience, which is the most common gap in data CVs and the thing employers trust most.

### (Scenario: candidate attracted to greenfield work) Why do greenfield AI roles disappoint?
Many never reach production, the novelty fades within months, and a blank page can conceal missing data, unclear goals or absent engineering support.

### (Scenario: candidate comparing offers) What should I ask about the balance of work?
How many models run in production, how old they are, how often they need intervention, what is planned for replacement and what new work exists in the next year.

### (Scenario: candidate worried about their CV) How do I describe maintenance work convincingly?
By outcomes: reduced retraining time, fewer false alerts, models brought into compliance, fragile pipelines replaced without downtime, unused models decommissioned.

### (Scenario: candidate seeing warning signs) When is a maintenance role a bad idea?
When nothing is ever rebuilt, when you would be the only person who understands an undocumented system, or when on-call has no rotation structure or improvement budget.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {"@type": "Question", "name": "Is maintaining existing models bad for my career?", "acceptedAnswer": {"@type": "Answer", "text": "No — it is often the fastest route to production experience, which employers trust most."}},
    {"@type": "Question", "name": "Why do greenfield AI roles disappoint?", "acceptedAnswer": {"@type": "Answer", "text": "Many never reach production and a blank page can hide missing data and support."}},
    {"@type": "Question", "name": "What should I ask about the balance of work?", "acceptedAnswer": {"@type": "Answer", "text": "Number and age of production models, intervention frequency and planned new work."}},
    {"@type": "Question", "name": "How do I describe maintenance work convincingly?", "acceptedAnswer": {"@type": "Answer", "text": "By outcomes: faster retraining, fewer false alerts, compliance, replaced pipelines."}},
    {"@type": "Question", "name": "When is a maintenance role a bad idea?", "acceptedAnswer": {"@type": "Answer", "text": "When nothing is rebuilt, knowledge is undocumented and on-call lacks structure."}}
  ]
}
</script>
