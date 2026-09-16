---
Title: "You Would Inherit a Model You Believe Is Wrong. Should You Take the Job?"
Keywords: inheriting a flawed model, model in productie klopt niet, raising concerns about a model, data scientist professional responsibility, model validation new job, OnlyAIJobs
Buyer Stage: Decision
Target Persona: B (Experienced AI or ML engineer)
Content Format: Decision Guide
---

# You Would Inherit a Model You Believe Is Wrong. Should You Take the Job?

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "You Would Inherit a Model You Believe Is Wrong. Should You Take the Job?",
  "description": "Sometimes you can tell during the interviews that a production model is flawed. How to check whether you are right, how to raise it as a new joiner, and when the situation is a reason to decline.",
  "author": {"@type": "Organization", "name": "OnlyAIJobs", "url": "https://onlyaijobs.eu"},
  "publisher": {"@type": "Organization", "name": "OnlyAIJobs", "url": "https://onlyaijobs.eu"},
  "datePublished": "2027-01-12",
  "mainEntityOfPage": {"@type": "WebPage", "@id": "https://onlyaijobs.eu/blog/inheriting-a-model-you-think-is-wrong"},
  "inLanguage": "en",
  "about": [{"@type": "Thing", "name": "Inheriting a flawed production model"}, {"@type": "Place", "name": "Netherlands"}],
  "mentions": [
    {"@type": "Organization", "name": "OnlyAIJobs"},
    {"@type": "Thing", "name": "Model validation"},
    {"@type": "Thing", "name": "Data leakage"},
    {"@type": "Thing", "name": "Backtesting"},
    {"@type": "Legislation", "name": "EU Artificial Intelligence Act"},
    {"@type": "Legislation", "name": "General Data Protection Regulation (GDPR)"},
    {"@type": "Thing", "name": "Model documentation"},
    {"@type": "Thing", "name": "Human oversight"},
    {"@type": "Thing", "name": "Professional responsibility"},
    {"@type": "Thing", "name": "Model governance"}
  ]
}
</script>

It emerges in the technical interview, or in the first week. A model is running in production, decisions are being made on its output, and something about the description is wrong: a validation setup that cannot be sound, a target variable that leaks the answer, a population that no longer matches the one it was trained on, or a use that has drifted well beyond what it was built for. Nobody is lying to you. The people describing it believe it works, because it has been running for two years and the numbers look good. You would be the person who arrives, sees it, and has to decide what to do about it while being the newest person in the room.

## The Kinds of Wrong

They are not equivalent, and the response differs.

**Technically flawed.** Leakage, a broken validation split, a metric that rewards the wrong behaviour, training data that includes the future. The model's reported performance is not real.

**Right model, wrong problem.** It works as built and answers a question nobody needed, while the decision it feeds requires something else.

**Outdated.** It was correct when built, and the process, the population or the data has moved. Very common and easily missed.

**Unfair in effect.** Performance differs systematically across groups in ways that matter, or a feature acts as a proxy for something it should not.

**Used beyond its purpose.** Built for triage, now driving decisions about individuals. The model may be fine; the use is not.

## Why Flawed Models Survive

**Nobody owns it.** The builder left, and it runs.

**The results please someone.** A model that confirms what a department already believed is rarely audited.

**There is no baseline.** Without a comparison to the previous process, nobody can say whether it helps.

**Changing it is expensive.** Retraining, re-approval, re-integration and explaining to users why the numbers moved.

**Questioning it implies criticism.** The person who built it may still be there, possibly as your colleague or your manager.

## Before You Conclude You Are Right

New joiners are sometimes wrong about this, and being wrong loudly in month one is expensive. Systems that look indefensible occasionally turn out to encode something real that nobody wrote down.

**Reproduce it.** Run the training and evaluation yourself, on the same data.

**Look for the documented rationale.** Ask whether a design decision you find strange was deliberate. Often there is a reason, sometimes a good one.

**Build the baseline.** What would the previous process, or a simple rule, achieve on the same period? A model can be flawed and still better than what it replaced, which changes the urgency.

**Backtest honestly.** A clean out-of-time evaluation settles most disputes about validation.

**Ask the users.** People who work with the output daily usually know where it is wrong, in specific and useful terms, and have often stopped trusting it in exactly those cases.

Come with evidence, not with an impression.

## How to Raise It as the New Person

**Privately first, to the person responsible.** Not in a group meeting, and not in writing to a wide audience.

**Frame it as a question.** "I reproduced the validation and got something different — can we look at it together?" leaves room for you to be wrong and for them to save face.

**Separate the finding from the person.** The model was built under constraints you did not face, by someone solving a different problem.

**Bring a proportionate proposal.** Not "we must rebuild", but "here is a check we could run, and here is what we would do if it confirms the issue".

**Escalate in writing only when necessary,** and then factually: what you found, what it affects, what you recommend, what you need decided.

Handled this way, finding a serious flaw in your first months is one of the fastest routes to credibility. Handled badly, it is how new joiners become the person who criticised everything before understanding anything.

## When It Is More Than a Technical Matter

The calculation changes when the model affects people rather than processes.

If it influences employment, credit, access to services, benefits, education or similar decisions, the organisation's obligations are heavier — under the **AI Act**, such uses generally fall in the high-risk category, with requirements around documentation, data governance, human oversight and monitoring, while privacy rules impose their own duties around transparency and decisions with significant effects.

In that context, an unresolved known flaw is not merely a quality issue. Raise it formally, involve the people whose job it is — compliance, the data protection officer, model validation where it exists, the works council if employees are affected — and keep a record of what you raised and what was decided. Obligations sit with the organisation, and your professional position rests on having said so clearly and in writing.

## If You Spot It During the Interviews

You have more leverage before accepting than at any point afterwards. Use it carefully.

**Ask neutral questions.** How the model is validated, what it is compared against, how often it is retrained, who monitors it, what happens when it is wrong about a case.

**Listen for whether the concern is new to them.** An employer who says "we know, that is partly why we are hiring" is offering you a defined and reasonable mandate. One who becomes defensive is showing you the reception your first months will receive.

**Ask what would happen if you concluded it needed rebuilding.** The answer tells you whether you would have the authority the role implies.

**Ask who built it and where they are now.** If they are your prospective manager, weigh that carefully — it is workable, and it requires a manager secure enough to be corrected.

## When to Accept

- The employer already suspects the problem and wants it addressed.
- You would have a mandate to validate, and a budget to fix.
- The model affects processes rather than individuals, so the risk is commercial rather than personal.
- There is a sponsor senior enough to absorb the finding.
- You are experienced enough to be sure, and diplomatic enough to be heard.
- Fixing it would be a genuinely strong piece of work to have done.

## When to Decline

- The flaw affects decisions about people and the organisation is not interested.
- Questioning it in the interview produced defensiveness.
- The builder is in charge and considers the matter closed.
- There is no route to compliance, legal or governance expertise.
- You would carry responsibility for the output without authority to change it.
- Documentation does not exist and nobody intends to create any.

## The Opportunity Hidden in It

Inheriting something broken is, oddly, one of the better situations for a new joiner. The bar is low, the improvement is measurable, and the story afterwards is exactly what interviewers want: you found a real problem, established it with evidence, persuaded people, fixed it and showed what changed.

The candidates who do badly are not the ones who inherit flawed models. They are the ones who inherit them, notice, and say nothing for two years because raising it felt awkward — and then have to explain, in a later interview, why the system they owned was producing numbers that were never right.

## If You Have to Live With It for a While

Confirming a problem does not mean you can fix it next week. Retraining may need approval, the business may depend on the output, and the replacement may take a quarter. That interval is manageable, and how you handle it is what separates professional judgement from either panic or silence.

**Write the limitation down.** A short, factual note: what the model does, where it is unreliable, which cases it should not be used for, and what the evidence is. This single document protects users, the organisation and you.

**Restrict the use rather than the model.** Often the fastest safe step is narrowing where the output is applied — excluding the population where it fails, or requiring human review for the affected cases — while the rebuild proceeds.

**Add monitoring immediately.** If nobody was watching, start. Even a weekly check on distribution and outcomes turns an unknown into something observable.

**Tell the users what changed in their terms.** People who rely on the output deserve to know which of their decisions should now carry more caution. They usually respond better than teams expect, because many of them had already noticed.

**Set a date and put it in a plan.** An acknowledged problem with a remediation date is a managed risk. The same problem with no date becomes the thing nobody mentions until it appears in an audit.

**Keep the record.** What you found, when you raised it, what was decided and by whom. Not as self-protection first, but because it is what makes the eventual fix defensible.

## Real example

### An engineer in Almere who rebuilt the validation before saying anything

An engineer joins a service company and inherits a churn model that has been running for three years and is described as highly accurate. In his second week he notices that one feature is updated after the outcome it predicts.

He does not raise it immediately. He reproduces the training pipeline, confirms the leakage, and builds an out-of-time evaluation plus a simple baseline using three obvious variables.

The real performance is far below what is reported, and roughly equal to the baseline. Marketing has been spending on retention campaigns targeted by this model for three years.

He takes it to his manager privately, with the notebook and a one-page summary. The conversation is uncomfortable for ten minutes and then constructive — the person who built it left two years ago, and nobody has looked at it since.

They keep the model running for one more cycle with a corrected feature set, measure properly against the baseline, and rebuild over the following quarter.

The finding becomes the reason he is trusted with the next two projects, and the validation framework he wrote is now applied to every model in the company.

## Key Takeaways

- Distinguish technical flaws, right-model-wrong-problem, outdated models, unfair effects and use beyond the intended purpose — the response differs for each.
- Before concluding you are right, reproduce the work, look for the documented rationale, build a baseline, backtest out of time and ask the users.
- Raise it privately first, framed as a question, separated from the person who built it, with a proportionate proposal.
- When the model affects decisions about people, treat an unresolved flaw as a governance matter: involve compliance or the data protection officer and keep a written record.
- Ask in the interview how the model is validated and what would happen if you concluded it needed rebuilding — defensiveness there predicts your first year.

## Where to Start

Ask how any production model is validated and what it is compared against before you accept — and see which employers near you already have a validation practice rather than a plan for one.

Browse current AI, machine learning and data jobs by category and distance, free and without an account, at [onlyaijobs.eu/jobs](https://onlyaijobs.eu/jobs).

## Frequently Asked Questions

### (Scenario: candidate spotting a flaw in interviews) Should I decline a role because a production model looks flawed?
Not usually. Employers who already suspect the problem offer a clear mandate. Decline when the model affects people and the organisation is not interested, or when you would carry responsibility without authority.

### (Scenario: new joiner in the first weeks) How do I check whether I am right?
Reproduce the training and evaluation, look for a documented rationale, build a simple baseline, run an honest out-of-time backtest and ask the people who use the output.

### (Scenario: new joiner raising a problem) How should I raise it?
Privately first, as a question rather than a verdict, separated from whoever built it, with evidence and a proportionate next step rather than a demand to rebuild.

### (Scenario: model affecting individuals) When is this more than a technical issue?
When the model influences employment, credit, services or similar decisions. Those uses generally carry high-risk obligations, so involve compliance or the data protection officer and record what you raised.

### (Scenario: candidate weighing the opportunity) Is inheriting a broken model bad for my career?
The opposite, if you act. Finding a real problem, proving it and fixing it is among the strongest stories you can tell later. Saying nothing for two years is the damaging option.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {"@type": "Question", "name": "Should I decline a role because a production model looks flawed?", "acceptedAnswer": {"@type": "Answer", "text": "Not usually — decline when it affects people and nobody is interested, or when you lack authority."}},
    {"@type": "Question", "name": "How do I check whether I am right?", "acceptedAnswer": {"@type": "Answer", "text": "Reproduce it, seek the documented rationale, build a baseline, backtest out of time and ask users."}},
    {"@type": "Question", "name": "How should I raise it?", "acceptedAnswer": {"@type": "Answer", "text": "Privately, as a question, with evidence and a proportionate next step."}},
    {"@type": "Question", "name": "When is this more than a technical issue?", "acceptedAnswer": {"@type": "Answer", "text": "When decisions about people are involved — treat it as governance and record what you raised."}},
    {"@type": "Question", "name": "Is inheriting a broken model bad for my career?", "acceptedAnswer": {"@type": "Answer", "text": "The opposite if you act; staying silent for years is the damaging option."}}
  ]
}
</script>
