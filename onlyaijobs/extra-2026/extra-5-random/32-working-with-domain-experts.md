---
Title: "Working With Domain Experts: The Skill That Separates Good AI Engineers From Frustrated Ones"
Keywords: working with domain experts, ai project collaboration, subject matter experts machine learning, stakeholder skills data science, applied ai practice, OnlyAIJobs
Buyer Stage: Awareness
Target Persona: B (Experienced AI or ML engineer)
Content Format: Working Practice Guide
---

# Working With Domain Experts: The Skill That Separates Good AI Engineers From Frustrated Ones

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Working With Domain Experts: The Skill That Separates Good AI Engineers From Frustrated Ones",
  "description": "A working practice guide to collaborating with domain experts on AI projects: why their knowledge is decisive, how to run useful conversations, how to handle disagreement with the data, and how to build lasting working relationships.",
  "author": {"@type": "Organization", "name": "OnlyAIJobs", "url": "https://onlyaijobs.eu"},
  "publisher": {"@type": "Organization", "name": "OnlyAIJobs", "url": "https://onlyaijobs.eu"},
  "datePublished": "2027-06-12",
  "mainEntityOfPage": {"@type": "WebPage", "@id": "https://onlyaijobs.eu/blog/working-with-domain-experts"},
  "inLanguage": "en",
  "about": [
    {"@type": "Thing", "name": "Collaboration"},
    {"@type": "Thing", "name": "Applied machine learning"},
    {"@type": "Place", "name": "Europe"}
  ],
  "mentions": [
    {"@type": "Organization", "name": "OnlyAIJobs"},
    {"@type": "Thing", "name": "Subject matter expert"},
    {"@type": "Thing", "name": "Data quality"},
    {"@type": "Thing", "name": "Requirements"}
  ]
}
</script>

Every experienced applied AI practitioner has the same realisation at some point: the limiting factor on most projects is not modelling ability but understanding of the problem, and that understanding lives in people who have been doing the work for years. Working with domain experts well is therefore not a soft skill appended to the technical job. It is the technical job, because the data you are given only makes sense in the context they hold.

## Why Working With Domain Experts Decides Project Outcomes

Data records a process, and processes have history. A field means what it means because of a decision someone made in 2019. A gap in the series exists because a system was replaced. A cluster of unusual values comes from one office that recorded things differently. None of this is documented, and all of it will distort your model.

Domain experts also know what the output has to be for anyone to use it. A prediction that arrives after the decision has been made, or that cannot be acted on, is worthless regardless of accuracy. They know the decision, its timing, and the cost of being wrong in each direction.

Finally, they know what has been tried. Organisations rarely record failed initiatives, and repeating one wastes months.

## Conversations That Produce Useful Information

Most engineers ask experts for requirements. Better questions ask about work.

- "Walk me through what you do when a case like this arrives."
- "What do you look at first?"
- "When do you overrule the system you have now?"
- "What kind of mistake bothers you most?"
- "What would you check if you had more time?"
- "Tell me about a case that surprised you."
- "If I gave you this number, what would you do differently?"

The last question is the most valuable and the most skipped. If the answer is "nothing", you have found out early that the project has no route to value.

Ask to observe rather than only to interview. An hour watching someone work reveals more than three meetings, because experts describe their process in terms of rules while doing it by judgement.

## Who Counts as a Domain Expert

The label is broader than it looks, and the most useful people are often not the most senior.

**Operators and practitioners** — nurses, planners, inspectors, technicians, claims handlers, customer service staff — know how the process actually runs, including the workarounds. They are the best source for understanding your data's quirks and the eventual user experience.

**Process and subject specialists** — process engineers, underwriters, clinicians, logistics planners — hold the causal model of the domain. They are the people to ask why something happens.

**System and data owners** — the people who administer the source systems — know why fields exist, when they changed and what is actually populated. A conversation with them saves weeks.

**Managers** know the decision the output will support and the constraints around it, but they often describe the process as it should be rather than as it is.

A useful habit is to talk to at least one person from each group before designing anything. Their accounts will differ, and the differences are themselves informative: where the manager's description and the operator's description diverge, you will usually find the part of the process your data does not represent.

## Translating in Both Directions

Collaboration fails as often through your language as through theirs.

Avoid presenting precision, recall and AUC to people who do not use them. Translate into their terms: out of a hundred cases you would flag, roughly seventy are genuine; of the problems that occur, we catch about half. Better still, express it in the quantities they manage — hours of inspection, euros of stock, cases per week.

Equally, learn their vocabulary properly rather than approximating it. In each domain there are terms with exact meanings — a deviation, an incident, a batch, a claim, an episode — and using them loosely undermines confidence quickly. Keep a glossary; it is genuinely useful and it signals respect.

Be careful with the word model. To many people it implies certainty or automation. Saying "a tool that estimates" or "a ranking that suggests where to look first" is often more accurate and less alarming.

And be honest about uncertainty. Experts live with uncertainty daily and are rarely troubled by it. What damages trust is discovering later that a confident presentation concealed a wide range of plausible outcomes.

## Labelling and Expert Time

Many projects need domain experts to label data, and this is where goodwill is most easily spent.

Respect the cost. An expert hour spent labelling is an hour not spent on their job, and their manager is counting. Ask for the minimum that will answer the question, and show what their earlier labelling produced before asking for more.

Design the task properly. Ambiguous instructions produce inconsistent labels that look like model failure later. Write a short guideline with examples, including edge cases, and refine it after a pilot round of twenty items.

Measure agreement. Have two experts label the same subset and check how often they agree. If they agree only seventy per cent of the time, no model will exceed that, and you have learned something important about the problem — often that the category itself is ill-defined.

Use their time where it is most valuable: on the difficult and uncertain cases rather than the obvious ones. Active learning approaches formalise this, but even a simple rule of sending only low-confidence cases for review makes expert input go much further.

Finally, give the labelling back as a resource. A well-constructed, documented labelled set is an asset the organisation will reuse for years.

## Designing Systems Experts Will Actually Use

The adoption failure mode is consistent: a technically sound system that practitioners quietly ignore.

Several design choices prevent it. Fit into the existing workflow rather than adding a separate tool; a prediction in the system someone already uses gets seen, and a dashboard in a new place does not. Show the reasoning, not only the output — the two or three factors that drove the prediction, or the similar past cases — because experts need something to check against their own judgement.

Allow disagreement and capture it. A way to say "I do not agree, and here is why" gives you labelled failure cases and gives them agency. Systems that permit no override are either bypassed or followed uncritically, and both outcomes are bad.

Be explicit about scope. State what the system covers and what it does not, and make it visibly decline when it is outside its competence. Experts trust a tool that knows its limits far more than one that always answers.

And close the loop visibly. When you change something because of feedback, say so to the person who raised it. That single habit does more for adoption than any amount of training material.

## Managing the Political Reality

Not every project is welcomed, and pretending otherwise is naive.

Sometimes a system will change how someone's performance is measured, reduce the discretion they have exercised for years, or be perceived — sometimes correctly — as a step toward reducing headcount. European workplaces often have formal structures through which this is addressed: works councils and employee representation bodies have consultation rights on systems that affect working conditions and monitoring, and involving them early is both a legal requirement in many cases and practically wise.

Even where no formal process applies, address the question rather than avoiding it. State clearly what the system will decide, what remains a human decision, and how performance will or will not be measured using it. Where you do not know, say that you do not know and that you will find out.

Be careful, too, about whose account you accept. If one senior person defines the problem and the people who do the work disagree, you are being pulled into an existing organisational argument. Surface it rather than resolve it privately with a model.

Projects that fail for political reasons rarely look political in the post-mortem. They look like adoption problems.

## Building the Relationship Over Time

The best applied AI practitioners have a small number of domain relationships they have maintained for years, and those relationships are their real advantage.

Practical ways to build them. Spend time in their environment without an agenda occasionally — on the floor, in the ward, at the depot, in the claims room. Share results with them before sharing them upward, so they are never surprised in a meeting. Credit them publicly for insight that came from them. Follow through on small requests; if you said you would check something, check it.

Learn enough of the domain to hold a conversation. You do not need their expertise, but knowing the basic vocabulary, the main constraints and the seasonal rhythm of their work changes how you are received.

And be useful outside your project. A twenty-minute query that saves someone a manual reconciliation each month buys more goodwill than a year of formal stakeholder management.

Over time this changes what you are told. People who trust you mention the anomaly they noticed, the change coming next quarter, the reason a number looks odd. That flow of unrecorded information is the difference between a model that works and one that works only in the backtest.

## What This Means for Your Career

Collaboration ability is increasingly what distinguishes candidates at interview, because modelling skill has become more widely available while domain translation has not.

Hiring managers ask for it directly: describe a time a domain expert changed your approach; how do you explain a model to someone who does not want one; what do you do when the business asks for something you think is wrong. These questions are not filler. Teams have learned that a technically strong hire who cannot work with the rest of the organisation delivers little.

It is also the skill that makes a career portable. Methods change every few years; the ability to enter an unfamiliar domain, understand how work is done and turn that into a specification is what lets someone move from logistics to healthcare to energy without starting again.

If you want to develop it deliberately, the fastest route is to seek projects where you are the only technical person, because there is nowhere to hide from the conversation.

## How OnlyAIJobs Fits an Applied AI Career

OnlyAIJobs is a European job board listing only AI, machine learning and data roles. Vacancies show their exact address and the distance from your home, applications go directly to the employer's own page, browsing is free without an account, and no employer can pay for a higher position in the results.

For applied roles, read vacancy text for evidence of how a team works with the rest of its organisation. Postings that describe the business problem, the users and the decisions being supported usually come from teams that have shipped something people use. Postings that list only technologies often have not yet had that conversation.

To be clear about coverage: listings are currently concentrated in the Netherlands, in cities including Amsterdam, Utrecht, Eindhoven, Groningen, Ede and Capelle aan den IJssel, with employers such as Heijmans, Rexel, AMCS, Boltrics and Holland Innovative among those listing AI and data roles. Employers can list a first vacancy free via info@onlyaijobs.eu.

## Real example

### The variable that was not in the data

A team at a European food producer built a model to predict which batches would fail a quality specification. Performance was mediocre and they could not explain why some failures were entirely unpredictable.

A process operator, asked to look at a list of the missed cases, recognised them within a minute. All had been produced after a changeover from a different product. The changeover cleaning procedure left a variable residue that affected the next batch, and the timing of changeovers was recorded in a planning system nobody had connected to the process data.

Adding a single feature — hours since the last changeover and the product that preceded it — transformed the model.

The data scientist who led the project said afterwards that they had spent eight weeks tuning and one afternoon asking. He now starts every project by showing the worst cases to someone who does the work, before building anything.

## Handling Disagreement With the Data

Sometimes an expert says something the data does not support. Both can be right: the data may not capture the situation, the effect may be real but rare, or the expert may be describing how things used to be.

Treat it as a question rather than a contest. Ask what they would expect to see if they are right, then look for that specifically. Either you find it, which improves the model, or you show them a clear picture, which usually produces a more precise explanation rather than a retreat.

Never win the argument in a meeting with a chart. You need this person for the next two years.

## Key Takeaways

- Data only makes sense in the context that domain experts hold.
- Ask about how work is actually done, not for requirements.
- Observation reveals what interviews miss.
- Disagreement between expert knowledge and data is information, not an obstacle.
- The relationship is long-term; protect it above any individual point.

## Where to Start

Before your next model, spend two hours watching someone do the work it will affect, and show them your ten worst predictions. Browse current AI, ML and data vacancies at [onlyaijobs.eu/jobs](https://onlyaijobs.eu/jobs), and if you hire AI talent, list your first vacancy free via info@onlyaijobs.eu.

## Frequently Asked Questions

### (Scenario: engineer with limited access to experts) What if nobody has time for me?
Ask for thirty minutes with a specific question and a concrete artefact. Vague requests for context get declined; showing ten cases and asking what they see rarely does.

### (Scenario: engineer worried about credibility) How do I ask basic questions without looking ignorant?
Say you are new to the domain and want to get it right. Experts almost always respond well; pretending to understand is what damages credibility.

### (Scenario: engineer facing resistance) What if experts feel threatened by the project?
Address it directly. Explain what the system will and will not decide, and involve them in defining it. Resistance usually reflects a reasonable fear that nobody has answered.

### (Scenario: engineer in a regulated sector) Should expert input be documented?
Yes. In regulated environments, recording who provided domain input and what was decided is part of the evidence trail.

### (Scenario: employer) How do we support this collaboration?
Give experts explicit time for it, include them in project definition, and recognise the contribution in their own objectives rather than treating it as a favour.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {"@type": "Question", "name": "What if nobody has time for me?", "acceptedAnswer": {"@type": "Answer", "text": "Ask for thirty minutes with a specific question and a concrete artefact such as ten cases."}},
    {"@type": "Question", "name": "How do I ask basic questions without looking ignorant?", "acceptedAnswer": {"@type": "Answer", "text": "Say you are new to the domain; pretending to understand is what damages credibility."}},
    {"@type": "Question", "name": "What if experts feel threatened by the project?", "acceptedAnswer": {"@type": "Answer", "text": "Address it directly and involve them in defining what the system will and will not decide."}},
    {"@type": "Question", "name": "Should expert input be documented?", "acceptedAnswer": {"@type": "Answer", "text": "Yes, particularly in regulated environments where it forms part of the evidence trail."}},
    {"@type": "Question", "name": "How should employers support this collaboration?", "acceptedAnswer": {"@type": "Answer", "text": "Give experts explicit time and recognise the contribution in their objectives."}}
  ]
}
</script>
