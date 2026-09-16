---
Title: "Half the Job Is Labelling Data. Is That a Step Backwards?"
Keywords: data labelling job, annotatie kwaliteit machine learning, annotation guidelines role, data centric ai career, inter annotator agreement, OnlyAIJobs
Buyer Stage: Decision
Target Persona: A (Career changer or early-career AI professional)
Content Format: Decision Guide
---

# Half the Job Is Labelling Data. Is That a Step Backwards?

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Half the Job Is Labelling Data. Is That a Step Backwards?",
  "description": "Annotation work is dismissed by candidates and decisive for model quality. How to tell a serious data quality role from cheap labelling, and what it builds in a Dutch AI career.",
  "author": {"@type": "Organization", "name": "OnlyAIJobs", "url": "https://onlyaijobs.eu"},
  "publisher": {"@type": "Organization", "name": "OnlyAIJobs", "url": "https://onlyaijobs.eu"},
  "datePublished": "2027-01-14",
  "mainEntityOfPage": {"@type": "WebPage", "@id": "https://onlyaijobs.eu/blog/role-heavy-on-data-labelling-decision"},
  "inLanguage": "en",
  "about": [{"@type": "Thing", "name": "Data labelling and annotation roles"}, {"@type": "Place", "name": "Netherlands"}],
  "mentions": [
    {"@type": "Organization", "name": "OnlyAIJobs"},
    {"@type": "Thing", "name": "Data annotation"},
    {"@type": "Thing", "name": "Inter-annotator agreement"},
    {"@type": "Thing", "name": "Annotation guidelines"},
    {"@type": "Thing", "name": "Active learning"},
    {"@type": "Thing", "name": "Data-centric AI"},
    {"@type": "Legislation", "name": "General Data Protection Regulation (GDPR)"},
    {"@type": "Thing", "name": "Domain experts"},
    {"@type": "Thing", "name": "Model evaluation"},
    {"@type": "Thing", "name": "Quality assurance"}
  ]
}
</script>

The role is described as machine learning, and then the detail arrives: a substantial part of the first year is building the labelled dataset. Defining categories, writing guidelines, organising domain experts to annotate, measuring whether they agree, fixing the cases where they do not, and doing it again when the definitions turn out to be wrong. Candidates hear this as a downgrade — the unglamorous part, the thing you do before the real work. In practice it is the work that determines whether the model is any good, it is badly done almost everywhere, and the people who can do it well are far rarer than the people who can train a model.

## What These Roles Actually Involve

**Defining the target.** What exactly counts as the thing you are predicting. This sounds trivial and is where most projects quietly fail.

**Writing guidelines.** A document that lets different people label the same case the same way, including the edge cases nobody thought of until they appeared.

**Organising annotators.** Frequently domain experts — nurses, claims handlers, inspectors, technicians — whose time is expensive and who have other jobs.

**Measuring agreement.** Where annotators disagree, and whether the disagreement is noise or a sign that the definition is broken.

**Building a gold set.** A carefully adjudicated evaluation set that becomes the organisation's standard for years.

**Sampling strategy.** Which cases to label next, which is where active learning and simple prioritisation earn their keep.

**Sometimes managing a vendor,** and always managing quality.

## Why It Is Undervalued

The field's incentives reward modelling. Papers, courses and interviews focus on architectures, and labelled data is treated as an input that exists. In real organisations it does not exist, and creating it is most of the project.

There is also a status story: labelling is seen as work for someone cheaper. That view survives until a team discovers that its model is performing at the level of its label noise, and that no architecture will fix a target variable nobody defined properly.

## The Dutch Context

Two things make this work more substantial here than the stereotype suggests.

**Annotation is usually done by domain experts, not by an anonymous workforce.** Much of the valuable Dutch data is specialised — clinical notes, insurance claims, inspection reports, municipal records — and only people who do the job can label it. That makes the role partly about working with busy professionals, which is a genuinely senior skill.

**Personal data constrains where labelling can happen.** Under the **GDPR**, sending records containing personal data to an external annotation provider raises questions of lawful basis, processor arrangements and international transfers. Many Dutch organisations therefore keep annotation internal, which means someone has to design and run it — and that someone is the role being offered to you.

Where employees do the annotating as part of their work, there may also be internal consultation to consider, particularly if the resulting system will affect how their work is measured.

## The Two Versions of the Role

**Owning data quality.** You define targets, write guidelines, design the process, measure agreement, build the evaluation set and use it to drive model work. You are the person who decides what "correct" means for the organisation. This is a strong role at any level.

**Being the cheap annotator.** You label, in volume, to someone else's guidelines, with no influence over the definitions and no involvement in the modelling. This is real work and it is not a machine learning role, regardless of the title.

The distinguishing question is whether you would own the guidelines and the evaluation set, or only produce labels against them.

## What It Builds

**Judgement about what models can learn.** After defining a few targets you develop an instinct for which problems are learnable and which are definitional disputes in disguise.

**Evaluation skill,** the most portable capability in applied AI. The gold set you build is the evaluation set, and the person who built it understands the model's limits better than anyone.

**Domain fluency,** acquired faster than through any other activity, because you read hundreds of real cases.

**Process design and stakeholder work,** since you are asking busy professionals to give you their time.

**Credibility.** In organisations where nobody had measured label quality, being the person who did changes how your technical opinions are received.

## The Risk

Title drift is real. Someone hired to build a labelling function can become the labelling function, particularly if the modelling is done by others. After two years, a CV describing annotation management without modelling or deployment is harder to place than the work deserves.

Guard against it explicitly: agree that you own the modelling that uses the data, or at least the evaluation, and set a point at which the annotation process is handed over as a running system rather than remaining your job.

## Questions to Ask

- **Would I own the guidelines and the definitions, or apply someone else's?**
- **Who annotates, and how is their time secured?** An unfunded promise of expert time is the most common failure in these projects.
- **Is agreement measured today?** If not, nobody knows how good the current data is.
- **Would I build the evaluation set, and would I use it?**
- **Who does the modelling?**
- **What happens when the definitions turn out to be wrong?** They will.
- **How does annotation work given privacy constraints?** Internal, external, pseudonymised — the answer shows whether anyone has thought it through.
- **What proportion of my year is this, and what follows it?**

## When to Accept

- You would own definitions, guidelines and the evaluation set.
- Expert annotator time is committed by their managers, not hoped for.
- The modelling is yours, or the path to it is explicit.
- You want domain depth quickly, which this provides better than anything else.
- The organisation has never measured label quality, which means visible early wins.
- You are early in your career and want to learn what actually makes models work.

## When to Decline

- You would label to someone else's guidelines in volume.
- No expert time is allocated and you would be annotating clinical or technical material yourself without qualification to judge it.
- Nobody intends to measure agreement.
- The role has no modelling component and no agreed end.
- The title says data scientist and the work is exclusively annotation management, with no plan to change.

## How to Make It Senior Work

Treat the guidelines as a product: versioned, with examples, edge cases and a changelog. Measure agreement from the start and report it, because it converts an invisible quality question into a number people can act on.

Adjudicate disagreements with domain experts rather than resolving them yourself, and record the reasoning — that record becomes the organisation's definition of the concept.

Automate the mechanical parts and prioritise the informative cases, so that expert time goes where it changes the model.

Publish quality metrics alongside model metrics, so nobody can present a performance figure without the context of what it was measured against.

And write it up internally. Data quality work is invisible unless someone makes it visible, and the person who makes it visible is the person associated with the result.

## Where the Labels Come From Changes Everything

Before accepting, find out where the labels are supposed to originate. Each source has a different cost and a different failure mode, and the answer tells you what the job really is.

**Domain experts annotating deliberately.** The highest quality and the most expensive. The binding constraint is their availability, so ask whether their managers have committed time in writing. An unfunded promise of expert hours is the most common way these projects stall.

**Historical outcomes as labels.** Using what actually happened — the claim was fraudulent, the machine failed, the customer left. Cheap and abundant, with a serious trap: the historical record reflects past decisions, so a model trained on it learns the previous process, including its errors and its blind spots.

**Operational byproduct.** Labels that fall out of how people already work: a ticket category, a disposition code, a checkbox. Free, plentiful and often unreliable, because nobody filling in that field was thinking about your model.

**Customer or user feedback.** Useful and biased towards the people who bother to respond.

**External vendors.** Fast and scalable where the task is general, and constrained where the data contains personal information or requires domain expertise — which covers much of the interesting Dutch material.

**Model-assisted labelling.** Pre-labelling with an existing model and having people correct it. Efficient, and it introduces anchoring: reviewers accept plausible-looking suggestions and error rates settle at whatever the assisting model does badly.

A serious role involves choosing among these deliberately, combining them, and measuring the quality of each. A weak role assumes the labels are simply available and discovers in month four that they are not.

## Real example

### An annotator-turned-lead in Nijmegen who measured agreement first

A career changer joins a healthcare organisation for a role described as machine learning, and discovers that the first year is building a labelled corpus of clinical notes with three specialist nurses.

She starts by measuring agreement on a sample the previous attempt had produced. The nurses agree on roughly two thirds of cases — the rest are definitional disputes nobody had resolved, largely about when a complication counts as related to the procedure.

That measurement changes the project. The definition is rewritten with the nurses over three sessions, the guidelines gain twenty documented edge cases, and agreement rises substantially.

The model trained on the corrected data performs far better than the earlier attempt, not because the modelling changed but because the target finally meant one thing.

Two years later she leads the team. In interviews for that promotion, the thing that was discussed most was the agreement measurement — because it was the point at which the organisation learned what its data was worth.

## Key Takeaways

- Labelling roles are dismissed by candidates and decisive for model quality; label noise sets a ceiling no architecture can lift.
- In the Netherlands, annotation is often done by domain experts and kept internal because of privacy constraints, which makes the work more substantial than the stereotype.
- The serious version means owning definitions, guidelines and the evaluation set; the weak version means producing labels to someone else's rules.
- It builds evaluation skill, domain fluency, process design and credibility faster than most modelling work.
- Guard against title drift: agree that you own the modelling or the evaluation, and set a point at which the annotation process becomes a running system rather than your job.

## Where to Start

Vacancies rarely say how much of the work is data definition, so ask in the first conversation — and compare with employers near you whose labelled data already exists.

Browse current AI, machine learning and data jobs by category and distance, free and without an account, at [onlyaijobs.eu/jobs](https://onlyaijobs.eu/jobs).

## Frequently Asked Questions

### (Scenario: candidate offered an annotation-heavy role) Is data labelling work beneath a data scientist?
No. Label quality sets the ceiling on model performance, and few people do it well. The question is whether you own the definitions and evaluation or merely produce labels.

### (Scenario: candidate assessing the role) How do I tell a serious role from cheap labelling?
Ask whether you would own the guidelines, the definitions and the evaluation set, who does the modelling, and whether annotator agreement is measured today.

### (Scenario: candidate thinking about skills) What does this work build?
Evaluation skill, judgement about what is learnable, rapid domain fluency, process design and credibility with stakeholders — all of which transfer.

### (Scenario: candidate worried about their CV) What is the risk?
Becoming the labelling function permanently. Agree ownership of the modelling or evaluation, and a point at which the annotation process is handed over as a running system.

### (Scenario: candidate in a regulated domain) Can annotation be outsourced?
Often not straightforwardly. Personal data raises questions of lawful basis, processor arrangements and transfers, which is why many Dutch organisations keep annotation internal.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {"@type": "Question", "name": "Is data labelling work beneath a data scientist?", "acceptedAnswer": {"@type": "Answer", "text": "No — label quality caps model performance; the question is whether you own definitions and evaluation."}},
    {"@type": "Question", "name": "How do I tell a serious role from cheap labelling?", "acceptedAnswer": {"@type": "Answer", "text": "Ask who owns guidelines and the evaluation set, who models, and whether agreement is measured."}},
    {"@type": "Question", "name": "What does this work build?", "acceptedAnswer": {"@type": "Answer", "text": "Evaluation skill, domain fluency, process design and stakeholder credibility."}},
    {"@type": "Question", "name": "What is the risk?", "acceptedAnswer": {"@type": "Answer", "text": "Becoming the labelling function permanently; agree ownership and a handover point."}},
    {"@type": "Question", "name": "Can annotation be outsourced?", "acceptedAnswer": {"@type": "Answer", "text": "Often not easily — personal data raises lawful basis, processor and transfer questions."}}
  ]
}
</script>
