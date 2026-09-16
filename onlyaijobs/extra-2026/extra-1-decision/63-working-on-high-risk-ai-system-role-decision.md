---
Title: "The Role Is on a High-Risk AI System. Should You Take It?"
Keywords: high risk ai act job, annex iii ai system role, ai compliance data scientist, human oversight role, regulated ai work netherlands, OnlyAIJobs
Buyer Stage: Decision
Target Persona: B (Experienced AI or ML engineer)
Content Format: Decision Guide
---

# The Role Is on a High-Risk AI System. Should You Take It?

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "The Role Is on a High-Risk AI System. Should You Take It?",
  "description": "Credit decisions, hiring tools, public benefits, critical infrastructure: AI systems that affect people carry formal obligations and personal exposure. What that means for the job, and how to judge the employer.",
  "author": {"@type": "Organization", "name": "OnlyAIJobs", "url": "https://onlyaijobs.eu"},
  "publisher": {"@type": "Organization", "name": "OnlyAIJobs", "url": "https://onlyaijobs.eu"},
  "datePublished": "2027-01-01",
  "mainEntityOfPage": {"@type": "WebPage", "@id": "https://onlyaijobs.eu/blog/working-on-high-risk-ai-system-role-decision"},
  "inLanguage": "en",
  "about": [{"@type": "Thing", "name": "Working on high-risk AI systems"}, {"@type": "Place", "name": "Netherlands"}],
  "mentions": [
    {"@type": "Organization", "name": "OnlyAIJobs"},
    {"@type": "Legislation", "name": "EU Artificial Intelligence Act"},
    {"@type": "Thing", "name": "Annex III high-risk categories"},
    {"@type": "Thing", "name": "Human oversight"},
    {"@type": "Thing", "name": "Technical documentation"},
    {"@type": "Legislation", "name": "General Data Protection Regulation (GDPR)"},
    {"@type": "Thing", "name": "Data protection impact assessment"},
    {"@type": "GovernmentOrganization", "name": "Autoriteit Persoonsgegevens (Dutch Data Protection Authority)"},
    {"@type": "Thing", "name": "Model monitoring"},
    {"@type": "Thing", "name": "Works council (ondernemingsraad)"}
  ]
}
</script>

The work is interesting and the stakes are unusual: a model that influences who gets credit, which applications a recruiter sees first, how a benefits case is prioritised, when a piece of infrastructure is inspected. Roles like these are multiplying in the Netherlands, partly because organisations are formalising systems they already had, and partly because regulation has forced the subject onto management agendas. They are also different from ordinary data roles in ways that vacancies rarely spell out. More of your week goes into documentation, evaluation and oversight design than into modelling. Your work gets read by people whose job is to find fault with it. And decisions you make can affect individuals who have no idea you exist.

## What "High-Risk" Actually Refers To

Under the **EU Artificial Intelligence Act**, certain uses are classified as high-risk, including systems used as safety components of regulated products and a list of areas set out in **Annex III**. Those areas cover, among others, employment and worker management, access to education, creditworthiness and certain essential services, some public-sector benefit decisions, law enforcement, migration and asylum, and the management of critical infrastructure. Certain biometric applications are covered too, and a separate category of practices is prohibited outright, including some emotion-inference applications in the workplace.

Two points matter for a candidate. First, the obligations differ depending on whether your employer is the **provider** of the system — building or placing it on the market — or the **deployer** using it. Second, the obligations are being phased in over time, and the detail of dates and implementing guidance changes, so treat any specific timeline you are told as something to verify rather than as settled fact.

Ask which role your employer plays for the system you would work on. It determines what your job actually consists of.

## What Changes in the Daily Work

**Documentation becomes a deliverable.** Not a README, but a record of data sources, design choices, known limitations, test results and what the system must not be used for.

**Data governance gets serious.** Provenance, representativeness, how gaps and errors were handled, what was excluded and why.

**Evaluation is formalised.** Accuracy, robustness, performance across subgroups, behaviour on edge cases, and a repeatable process rather than a notebook someone ran once.

**Logging and traceability.** Systems must record enough that an individual decision can be reconstructed later.

**Human oversight is designed, not assumed.** Somebody must be able to understand, override and stop the system, and you will be part of specifying how that works in practice rather than on paper.

**Monitoring continues after launch.** Drift, incidents, complaints, corrective action.

On top of the AI Act, privacy law applies in parallel: impact assessments under the **GDPR**, transparency towards people affected, and the rules on decisions with significant effects that are based solely on automated processing. In the Netherlands, the **Autoriteit Persoonsgegevens** has been an active voice on algorithmic systems, particularly in the public sector.

## Why This Work Is Professionally Valuable

The market for people who can do this properly is considerably tighter than the market for people who can train models.

You develop evaluation practice that stands up to external scrutiny, documentation skills that most engineers lack entirely, an understanding of governance that translates across sectors, and the experience of defending technical choices to auditors, regulators, a works council or a supervisory board. That combination travels: finance, healthcare, energy, public administration and any employer facing an audit will pay for it.

There is also a less measurable benefit. Working under scrutiny makes you better. Knowing that a stranger will read your validation design changes how you write it.

## The Costs, Stated Honestly

**Pace.** Changes that would take an afternoon elsewhere take weeks, because the documentation and sign-off travel with them.

**Proportion of the week spent not modelling.** For many of these roles, the modelling is a minority of the work. Candidates who wanted a research-like job are frequently disappointed.

**Scrutiny.** Your work is reviewed by people whose incentive is to find weaknesses. This is uncomfortable before it becomes useful.

**Exposure to consequences.** When a system that affects people goes wrong, it goes wrong publicly. Dutch public administration has lived through exactly this, and the memory shapes how these projects are run.

**Ambiguity.** Guidance is still developing, and you will make judgement calls without a definitive answer available.

## The Responsibility Question

Candidates ask, reasonably, what happens if the system causes harm. The obligations under the AI Act rest on organisations rather than on individual employees, and formal accountability sits with the provider or deployer, not with the engineer who wrote the feature pipeline. That is the legal shape of it in general terms, and the specifics of any individual situation belong with a lawyer.

The practical exposure is different from the legal one. If something goes wrong, you will be asked what you knew, what you raised and what was decided. Three habits protect you and improve the work at the same time.

**Write down limitations.** Every system has them; a written record of what the model cannot do is the single most useful artefact when something is later used outside its intended purpose.

**Escalate in writing.** A concern raised verbally in a meeting does not exist six months later.

**Keep your evaluation evidence.** Test sets, results, decisions about thresholds and who approved them.

If an employer treats these habits as friction rather than as professional practice, that tells you what kind of place it is.

## Questions to Ask Before Accepting

- **Is the organisation the provider or the deployer of this system?**
- **Who owns compliance, and is it a real function with people and budget?** If the answer is "the data team, informally", the role includes a job nobody has resourced.
- **What documentation exists today?** Ask to hear the honest answer rather than the intended one.
- **How is human oversight implemented in practice — who overrides, how often, and what happens then?**
- **What happens when I say a system is not ready?** The most revealing question in the interview.
- **Has this system been assessed, audited or examined externally, and what came out of it?**
- **Is there legal and privacy expertise I can consult, or would I be interpreting the rules alone?**
- **Have the works council and the affected departments been involved?**

## Signals the Employer Is Serious

- Compliance, privacy and legal colleagues are in the room and know the system.
- Documentation exists and is maintained rather than produced before an audit.
- There is a defined process for pausing or withdrawing a system.
- People can describe a case where the answer was "not yet".
- Monitoring runs after launch, with someone reading the output.
- The organisation talks about the people affected, not only about the regulator.

## Signals to Walk Away From

- The plan is to build first and document later.
- Compliance is described as a box-ticking exercise or an obstacle.
- Nobody can say who is accountable for the system.
- The system is already in use and its documentation does not exist.
- The employer wants a technical person to sign off on decisions that are not theirs to make.
- The application sits close to a prohibited practice and the reaction to that observation is impatience.

## When It Is Worth Taking

- You want to build expertise that is scarce and becoming more valuable in the Dutch market.
- The organisation is serious, resourced and honest about where it stands.
- The application genuinely helps people, which makes the constraints easier to live with.
- You have the temperament for careful work and written argument.
- You want a route towards lead, governance or advisory roles later.

## When to Decline

- You mainly want to do research or fast experimentation; this is not that job.
- The employer is treating the obligations as paperwork.
- You would be the only person carrying responsibility that belongs to the organisation.
- The system's purpose is one you cannot professionally defend.
- There is no budget for the work the rules require.

## Where This Experience Leads

It is worth knowing what this work opens up, because the career paths are less obvious than for ordinary engineering roles and several of them are well paid and undersupplied in the Netherlands.

**Model validation and second-line roles.** Dutch banks and insurers maintain independent validation functions that review models built elsewhere in the organisation. The work is analytical, senior and specifically requires the ability to assess someone else's system rigorously.

**Responsible AI and governance leads.** Increasingly common in larger organisations, combining technical judgement with documentation, oversight design and the ability to explain systems to boards and regulators.

**Audit and assurance.** Accountancy and advisory firms have built practices around examining algorithmic systems, and they hire people who have been on the inside of one.

**Public-sector algorithm work.** Dutch government bodies maintain algorithm registers and oversight arrangements, and they need people who can both build and explain.

**Supervisory and advisory roles,** including at regulators and in policy-adjacent organisations, where practical engineering experience is scarce.

What all of these have in common is that they are difficult to enter without having done the work under real scrutiny. A candidate who has maintained documentation that survived an external examination has something most engineers cannot claim, and the supply of such people is not growing as fast as the demand.

## Real example

### An engineer in Utrecht who asked what happens when he says no

An engineer is offered a role at an organisation providing risk scoring used in decisions about individuals. The work is technically interesting and the salary is good. He is uneasy about the exposure.

He asks his questions. The organisation is the provider of the system. There is a compliance lead with a budget, a lawyer who has read the technical documentation, and an internal register of systems. Documentation exists and is out of date by about six months, which the compliance lead says openly.

Then he asks what happened the last time someone said a system was not ready. The answer is specific: a release was postponed by two months after the team found that performance differed across groups in the test population, and the postponement was supported by management.

He accepts. His first year is roughly forty percent modelling, forty percent evaluation and documentation, and twenty percent explaining the system to people who challenge it. He finds the last part unexpectedly satisfying.

Two years later, he is asked to advise on a second system, and the postponement story is one he now tells to candidates he interviews.

## Key Takeaways

- High-risk classification under the AI Act covers areas such as employment, creditworthiness, essential services, critical infrastructure and parts of the public sector, with obligations differing for providers and deployers.
- The work shifts towards documentation, data governance, formal evaluation, logging, human oversight design and post-launch monitoring.
- Legal accountability sits with organisations rather than individual engineers, but your practical exposure is what you knew, raised and recorded — so write down limitations and escalate in writing.
- The most revealing interview question is what happens when someone says a system is not ready.
- Decline when compliance is treated as paperwork, when documentation is deferred, or when responsibility that belongs to the organisation is being placed on one technical person.

## Where to Start

If regulated AI work interests you, look for employers who already maintain documentation and monitoring rather than those planning to start — and see which of them are within reach of where you live.

Browse current AI, machine learning and data jobs by category and distance, free and without an account, at [onlyaijobs.eu/jobs](https://onlyaijobs.eu/jobs).

## Frequently Asked Questions

### (Scenario: candidate offered a regulated AI role) What does high-risk mean under the AI Act?
It covers AI used as safety components of regulated products and listed areas in Annex III, including employment, creditworthiness, essential services, critical infrastructure and parts of the public sector. Obligations differ for providers and deployers and are phased in, so verify current timelines.

### (Scenario: candidate worried about liability) Am I personally responsible if the system causes harm?
Obligations rest on organisations rather than individual employees, and specifics belong with a lawyer. Your practical exposure is what you knew and raised, so record limitations and escalate in writing.

### (Scenario: candidate assessing the employer) How do I tell whether an employer takes this seriously?
Compliance is a resourced function, documentation is maintained rather than produced before audits, monitoring runs after launch and someone can describe a time the answer was "not yet".

### (Scenario: candidate weighing the work) Will I still be doing technical work?
Yes, but often as a minority of the week. Expect substantial time on evaluation, documentation, oversight design and explaining the system to people who challenge it.

### (Scenario: candidate thinking about career value) Is this experience valuable elsewhere?
Very. Evaluation that survives external scrutiny, documentation practice and governance literacy transfer across finance, healthcare, energy and the public sector.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {"@type": "Question", "name": "What does high-risk mean under the AI Act?", "acceptedAnswer": {"@type": "Answer", "text": "Safety components of regulated products plus listed Annex III areas; obligations differ for providers and deployers and are phased in."}},
    {"@type": "Question", "name": "Am I personally responsible if the system causes harm?", "acceptedAnswer": {"@type": "Answer", "text": "Obligations rest on organisations; your practical exposure is what you knew and raised, so record and escalate in writing."}},
    {"@type": "Question", "name": "How do I tell whether an employer takes this seriously?", "acceptedAnswer": {"@type": "Answer", "text": "Resourced compliance, maintained documentation, real monitoring and a history of saying 'not yet'."}},
    {"@type": "Question", "name": "Will I still be doing technical work?", "acceptedAnswer": {"@type": "Answer", "text": "Yes, though often a minority of the week alongside evaluation, documentation and oversight design."}},
    {"@type": "Question", "name": "Is this experience valuable elsewhere?", "acceptedAnswer": {"@type": "Answer", "text": "Very — scrutiny-proof evaluation and governance literacy transfer across regulated sectors."}}
  ]
}
</script>
