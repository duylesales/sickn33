---
Title: "They Want to Build Their Own Model From Scratch. Should You Join?"
Keywords: eigen taalmodel bouwen, train your own llm job, foundation model netherlands, digital sovereignty ai, pretraining versus fine tuning role, OnlyAIJobs
Buyer Stage: Decision
Target Persona: B (Experienced AI or ML engineer)
Content Format: Decision Guide
---

# They Want to Build Their Own Model From Scratch. Should You Join?

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "They Want to Build Their Own Model From Scratch. Should You Join?",
  "description": "Ambitions to train an in-house model range from well-founded to fantasy. The questions that separate them, what the work really involves, and what you gain even if the project fails.",
  "author": {"@type": "Organization", "name": "OnlyAIJobs", "url": "https://onlyaijobs.eu"},
  "publisher": {"@type": "Organization", "name": "OnlyAIJobs", "url": "https://onlyaijobs.eu"},
  "datePublished": "2027-01-14",
  "mainEntityOfPage": {"@type": "WebPage", "@id": "https://onlyaijobs.eu/blog/company-that-wants-to-build-its-own-model"},
  "inLanguage": "en",
  "about": [{"@type": "Thing", "name": "In-house model development ambitions"}, {"@type": "Place", "name": "Netherlands"}],
  "mentions": [
    {"@type": "Organization", "name": "OnlyAIJobs"},
    {"@type": "Thing", "name": "Pretraining and fine-tuning"},
    {"@type": "Thing", "name": "Retrieval-augmented generation"},
    {"@type": "Thing", "name": "Compute budget"},
    {"@type": "Thing", "name": "Data licensing and rights"},
    {"@type": "Legislation", "name": "EU Artificial Intelligence Act"},
    {"@type": "Thing", "name": "Digital sovereignty"},
    {"@type": "Thing", "name": "Dutch language technology"},
    {"@type": "Thing", "name": "Model evaluation"},
    {"@type": "Thing", "name": "Total cost of ownership"}
  ]
}
</script>

Somewhere between the second and third conversation, the ambition is stated: the organisation wants its own model. Not a purchased service, not an API — their own, trained on their data, running on their infrastructure. The reasons given are usually sovereignty, privacy, cost or the fact that general models handle their domain badly. Some of those reasons are excellent. The gap between the ambition and what the organisation can actually resource is where careers get spent, and closing that gap in an interview takes about four questions.

## First, Establish What They Actually Mean

The phrase covers four very different projects, and people use it interchangeably.

**Pretraining from scratch.** Training a foundation model on a large corpus. Enormously expensive, requires a specialist team and a compute budget that few organisations outside a handful of institutions can justify.

**Continued pretraining.** Taking an existing open-weights model and training it further on domain or language data. Substantial, feasible for a serious organisation, and increasingly common.

**Fine-tuning.** Adapting an existing model for specific tasks with modest data. Well within reach of a competent team.

**Retrieval and orchestration.** Not training at all — putting the organisation's knowledge in front of an existing model. This solves a large share of what people believe requires training.

Ask which of the four is meant. If the answer is the first and the organisation is not a research institute or a very large company with a dedicated team, ask what compute has been secured, and listen carefully to the answer.

## Why Dutch Organisations Want This

**Data cannot leave.** Healthcare, government, defence-adjacent work and parts of finance operate under constraints that make external services difficult. This is the strongest reason and it is often genuine.

**The language.** General models handle Dutch less well than English, and domain Dutch — clinical, legal, technical, municipal — considerably less well again. An organisation with a large Dutch corpus has a real basis for adaptation.

**Sovereignty and dependency.** A strategic preference against depending on a foreign provider whose terms, pricing and availability can change. A legitimate consideration, increasingly discussed in Dutch public and semi-public organisations.

**Cost at volume.** At sufficient scale, running your own model can be cheaper than paying per request. The threshold is higher than most people assume.

**Control over behaviour,** including the ability to document and explain the system, which matters under the AI Act's obligations for providers.

## When It Is Justified

- The data genuinely cannot be sent elsewhere, and the use case is core.
- The organisation has a large, licensed, high-quality corpus in a domain or language where general models underperform.
- Usage volume is high enough that the economics work.
- There is a team, not a person, and a compute budget that has been approved rather than discussed.
- Someone has done the evaluation work to show that existing options are insufficient — with numbers, not impressions.

## When It Is Not

- Nobody has tried retrieval with an existing model first.
- The corpus is smaller than people think, or the organisation does not have clear rights to use it.
- Compute is "being looked into".
- There is no evaluation plan, so success would be unmeasurable.
- The driver is a board's desire to be seen doing something ambitious.
- Nobody has costed maintenance: models need retraining, monitoring and support for years.

## The Four Questions That Settle It

**How much usable, rights-cleared data is there, in what form?** Ask for the size and the licensing position. Organisations routinely overestimate both, and personal data in the corpus brings its own obligations.

**What compute is secured, and how?** An approved budget, a partnership, a national facility, a cloud commitment — or nothing. This single answer separates most serious projects from aspirational ones.

**How will you know it is better?** A project without an evaluation set is not a project. Ask what the baseline is and who built it.

**Who maintains it in three years?** The build is the smaller part of the cost.

If these four are answered concretely, the ambition is probably real. If two or more are vague, you would be joining a project that has not yet been decided, whatever the vacancy says.

## What the Work Is Really Like

Less modelling and more data engineering than candidates expect. Collecting, cleaning, deduplicating and documenting a corpus; sorting out rights and personal data; building evaluation sets in the target domain and language; running experiments with long feedback cycles; and explaining repeatedly to management why progress is not visible this month.

If the project is continued pretraining or fine-tuning, the technical core is more accessible than it sounds, and the difficulty sits almost entirely in the data and the evaluation.

## What You Gain Even If It Fails

This is the reassuring part. The transferable skills in this work are the ones employers are short of: large-scale data pipeline engineering, corpus construction, rights and privacy handling at scale, evaluation design in a specific domain and language, and cost-aware infrastructure work.

A project that ends without a deployed model can still leave you with demonstrably strong experience — provided you can point to the corpus, the evaluation framework and the infrastructure you built, rather than only to an ambition.

## The Risk

Two years on a project that produces no usable system, in an organisation that then loses interest, is a real possibility and a difficult CV entry. It is worse if the work was purely experimental, with nothing deployed, measured or reused.

Mitigate it the way you would any speculative role: insist that something reaches users along the way — a retrieval system, a fine-tuned task model, an evaluation suite the organisation adopts — so that the year has an artefact attached regardless of whether the grand ambition survives.

## When to Accept

- The ambition is continued pretraining or fine-tuning, with data and compute secured.
- The constraint driving it is real: data that cannot leave, or a language and domain gap that has been measured.
- There is a team and a named sponsor with budget.
- An evaluation baseline exists.
- You would own a substantial piece — corpus, evaluation, infrastructure — that stands on its own.
- The organisation has shipped something before, in any technology.

## When to Decline

- Pretraining from scratch with no secured compute and a small team.
- No rights-cleared data, or a corpus nobody has measured.
- No evaluation plan and no baseline.
- The driver is visibility rather than a constraint.
- You would be the only person, expected to deliver something that requires a team.
- Nothing would reach users for two years by design.

## What Happens After the First Version

The question employers answer least well is what the model's life looks like once it exists, and it determines whether your work becomes infrastructure or a artefact nobody dares touch.

**Retraining has a cadence and a cost.** Language changes, processes change, the corpus grows. Somebody must decide how often to retrain, run it, evaluate it and decide whether to promote the result — and that is a standing commitment rather than a project.

**Serving is a permanent bill.** Inference infrastructure, scaling for peaks, redundancy and the engineers who keep it running. Organisations that compared training cost against a per-request price often forget this half.

**The evaluation suite must be maintained.** Test sets age as the domain moves, and an evaluation that no longer reflects reality is worse than none, because it produces confident numbers.

**Security and dependency updates continue.** Serving stacks and libraries need patching like any other production system.

**Obligations may attach.** Where an organisation develops a model and places it on the market or puts it into service under its own name, it can find itself in the provider role under the AI Act, with the documentation and conformity duties that follow. Building internally does not remove regulatory questions; it moves them in-house.

**Team size is the real constraint.** A model built by three people needs more than zero people to stay alive, and the second year is where projects quietly die because everyone moved on to the next initiative.

Ask who owns the model in year three and what that team looks like. An organisation that has thought about this is serious; one that has not is planning a build rather than a capability — and a build that nobody maintains is the most expensive way to arrive back where you started.

## Open Weights Changed the Calculation

One reason these projects have become plausible for ordinary organisations is that capable open-weights models exist to build on. That shifts the question from "can we train a model" to "which base model do we adapt, and under what licence".

Ask which base model is intended and what its licence permits — terms vary considerably, and some restrict commercial use, redistribution or particular applications. An organisation that has not read the licence of the model it plans to build its strategy on has not yet started the project.

Ask also what happens when a better base model appears, because one will. A plan that assumes a single adaptation, once, tends to be overtaken within a year; a plan built around a repeatable pipeline — corpus, adaptation, evaluation — survives the next release and is the version worth joining.

## Real example

### An engineer in Amsterdam who asked about compute in the first interview

An engineer interviews at a public-sector organisation that wants "its own language model" for processing Dutch case documents that cannot be sent to external services.

He asks the four questions. The corpus is several hundred thousand documents, internally held, with the rights position reviewed by legal. Compute is a committed allocation through an existing arrangement, approved for two years. The plan is continued pretraining of an open-weights model, not training from scratch. And an evaluation set has already been built by a colleague, with a baseline using a general model showing clear weaknesses on their document types.

Two answers are weaker: maintenance beyond the project has not been discussed, and the team would be three people.

He accepts, on the condition that a retrieval-based system using the existing evaluation set is delivered in the first six months, so that the organisation has something working while the larger effort proceeds.

That interim system is still in use. The adapted model arrives fourteen months later and performs considerably better on their documents than the general baseline — and the evaluation set, he says, was the thing that made every argument in the project resolvable.

## Key Takeaways

- Establish which of four projects is meant: pretraining from scratch, continued pretraining, fine-tuning, or retrieval with an existing model.
- Legitimate drivers are data that cannot leave, a measured language or domain gap, high volume economics, sovereignty concerns and documentable control.
- Four questions settle feasibility: how much rights-cleared data, what compute is secured, how success will be measured, and who maintains it in three years.
- The work is mostly corpus engineering, rights and privacy handling, and evaluation design — all highly transferable even if the model never ships.
- Insist that something reaches users within the first months, so the year produces an artefact regardless of whether the larger ambition survives.

## Where to Start

Ask which of the four projects is meant before you accept, then compare with employers near you already running language technology in production rather than planning it.

Browse current AI, machine learning and data jobs by category and distance, free and without an account, at [onlyaijobs.eu/jobs](https://onlyaijobs.eu/jobs).

## Frequently Asked Questions

### (Scenario: candidate offered a model-building role) Should I join a company that wants to train its own model?
It depends which project is meant. Continued pretraining and fine-tuning are feasible for serious organisations; pretraining from scratch without secured compute and a team is not.

### (Scenario: candidate assessing feasibility) What should I ask?
How much rights-cleared data exists and in what form, what compute is secured and how, how success will be measured against a baseline, and who maintains the result in three years.

### (Scenario: candidate weighing alternatives) Why would an organisation not just use an existing service?
Data that cannot leave the organisation, weak performance on Dutch domain material, volume economics, strategic independence, or the need to document and control the system.

### (Scenario: candidate worried about risk) What if the project fails?
The transferable value is real — corpus engineering, rights handling, evaluation design and infrastructure — provided something concrete was built. Insist on an interim system that reaches users.

### (Scenario: candidate expecting modelling work) What does the job actually involve?
Mostly data: collecting, cleaning, deduplicating and documenting a corpus, resolving rights and personal data questions, and building domain evaluation sets with long experiment cycles.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {"@type": "Question", "name": "Should I join a company that wants to train its own model?", "acceptedAnswer": {"@type": "Answer", "text": "It depends which project is meant — continued pretraining and fine-tuning are feasible; scratch pretraining rarely is."}},
    {"@type": "Question", "name": "What should I ask?", "acceptedAnswer": {"@type": "Answer", "text": "Rights-cleared data volume, secured compute, the evaluation baseline and who maintains it in three years."}},
    {"@type": "Question", "name": "Why would an organisation not just use an existing service?", "acceptedAnswer": {"@type": "Answer", "text": "Data that cannot leave, weak Dutch domain performance, volume economics, independence and control."}},
    {"@type": "Question", "name": "What if the project fails?", "acceptedAnswer": {"@type": "Answer", "text": "Corpus engineering, rights handling and evaluation design still transfer — insist on an interim system."}},
    {"@type": "Question", "name": "What does the job actually involve?", "acceptedAnswer": {"@type": "Answer", "text": "Mostly corpus construction, rights and privacy work, and domain evaluation with long cycles."}}
  ]
}
</script>
