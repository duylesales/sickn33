---
Title: "On-Call for Machine Learning Systems: What to Expect and What to Ask Before You Accept"
Keywords: on-call for machine learning systems, ml incident response, production model failures, standby duty tech europe, reliability data teams, OnlyAIJobs
Buyer Stage: Consideration
Target Persona: B (Experienced AI or ML engineer)
Content Format: Working Practice Guide
---

# On-Call for Machine Learning Systems: What to Expect and What to Ask Before You Accept

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "On-Call for Machine Learning Systems: What to Expect and What to Ask Before You Accept",
  "description": "A working practice guide to on-call for machine learning systems: how ML incidents differ from software incidents, what a reasonable rotation looks like, European rules on standby time, and the questions to ask in interviews.",
  "author": {"@type": "Organization", "name": "OnlyAIJobs", "url": "https://onlyaijobs.eu"},
  "publisher": {"@type": "Organization", "name": "OnlyAIJobs", "url": "https://onlyaijobs.eu"},
  "datePublished": "2027-06-22",
  "mainEntityOfPage": {"@type": "WebPage", "@id": "https://onlyaijobs.eu/blog/on-call-for-machine-learning-systems"},
  "inLanguage": "en",
  "about": [
    {"@type": "Thing", "name": "On-call rotation"},
    {"@type": "Thing", "name": "Incident response"},
    {"@type": "Place", "name": "Europe"}
  ],
  "mentions": [
    {"@type": "Organization", "name": "OnlyAIJobs"},
    {"@type": "Thing", "name": "Model monitoring"},
    {"@type": "Thing", "name": "Site reliability engineering"},
    {"@type": "Legislation", "name": "Working Time Directive"}
  ]
}
</script>

As machine learning moved into production, the people who build it inherited an obligation software engineers have lived with for decades: being reachable when it breaks. On-call for machine learning systems is now a normal part of many European AI roles, and it is one of the least discussed aspects of the job during interviews. It is also one of the largest determinants of quality of life, which makes it worth understanding properly before you accept an offer.

## Why On-Call for Machine Learning Systems Is Different

Classic software incidents are usually loud: a service is down, errors are thrown, dashboards go red. Machine learning incidents are frequently quiet, which changes how you detect and diagnose them.

**The system stays up and the output degrades.** Predictions continue, latency is fine, nothing errors. The model is simply wrong more often, and nobody knows for hours or weeks.

**Causes lie upstream.** A data provider changes a field, a source system is migrated, a partner sends a file in a new format, a join silently drops rows. The model is a victim, not a culprit.

**Feedback arrives late.** You often cannot verify correctness at the time of the incident, because the outcome is not observable yet.

**Degradation is gradual.** Distribution shift is a slope, not a cliff, which makes threshold-based alerting awkward.

**Fixing it may take days.** Retraining, validation and deployment are not a hotfix, so mitigation usually means falling back rather than correcting.

## What a Reasonable Rotation Looks Like

Practice varies widely, and it is fair to compare offers on this.

A humane arrangement generally has: at least five or six people in the rotation, so your turn comes every five or six weeks; clear scope, so you are responsible for defined systems and not for everything the company runs; documented runbooks for known failure modes; a defined escalation path with someone to call; and compensation, whether in payment, time off in lieu or both.

An arrangement to be cautious about: three people in rotation, no runbooks, alerts that fire frequently without action being possible, responsibility for systems you did not build and cannot access, and no compensation because "it is part of the role".

Alert quality matters more than alert volume. A rotation with two genuine pages a month is sustainable. One with twenty alerts a week, most of them noise, burns people out regardless of how rarely real incidents occur.

## What Actually Breaks

A catalogue of the failures that generate most machine learning pages, roughly in order of frequency.

**Upstream data changes.** Schema changes, renamed fields, new categorical values, changed units, altered encodings, time zone shifts. The most common cause by a wide margin.

**Missing or late data.** A source that does not arrive, or arrives after the pipeline has run. Systems that silently proceed with partial data produce confident wrong answers.

**Pipeline failures.** Orchestration errors, resource exhaustion, dependency changes, expired credentials. These at least fail loudly.

**Serving problems.** Latency spikes under load, memory exhaustion, a model artefact that fails to load after a deployment, version mismatches between training and serving code.

**Distribution shift.** Real change in the world — a new product line, a seasonal transition, a pandemic, a competitor's promotion — which is not a bug but requires a response.

**Feedback loops.** The model's own outputs change behaviour, which changes the data, which changes the model. Recommendation and pricing systems are particularly prone.

**Integration changes.** A downstream consumer starts using outputs differently, or an upstream team changes a definition without telling anyone.

Notice how few of these are about the model itself. On-call for machine learning is mostly data engineering and operations.

## Monitoring That Catches Problems Early

Good monitoring for machine learning systems has four layers, and most teams implement only the first two.

**Infrastructure.** Is it running, responding, within latency and memory budgets? Standard and necessary.

**Pipeline.** Did the job run, did it complete, how many rows were processed compared with expectation, were there nulls where there should not be?

**Inputs.** This is the layer that catches the incidents that matter. Track the distribution of every important feature against a recent baseline: means, quantiles, null rates, category frequencies and the appearance of unseen categories. Alert on meaningful deviation.

**Outputs and outcomes.** Prediction distribution, rate of extreme values, and — where outcomes eventually arrive — realised accuracy by segment over time.

Add business-level checks, which are often the most sensitive of all: total predicted demand, aggregate price change, number of items flagged, share of cases routed to human review. These catch compound errors that no single technical check would notice.

The practical rule: every alert should have a documented action. An alert nobody can act on will be ignored within a fortnight, and it will train people to ignore the one that matters.

## Designing for Graceful Failure

Because machine learning problems rarely have fast fixes, the design question is what the system does when it cannot be trusted.

**Fallbacks.** Serve the previous day's output, a simpler model, a rule-based default or a cached result. Deciding this in advance, and testing it, is the single highest-value reliability investment for an ML system.

**Circuit breakers.** If input validation fails, stop rather than proceed. Producing no answer is frequently better than producing a wrong one, particularly where money or safety is involved.

**Human routing.** Push uncertain or unvalidated cases to a person instead of automating them. Capacity for this must be planned with the operational team, not assumed.

**Staged rollout.** Deploy new models to a small share of traffic first and compare. Most bad deployments are caught here rather than in testing.

**Easy rollback.** Versioned model artefacts, retained previous versions, and a documented procedure that someone can run at three in the morning without understanding the model.

**Kill switches.** A way to disable a feature entirely, with a named person authorised to use it.

Teams that build these find their on-call load drops sharply, because most incidents become automatic mitigations with a ticket rather than pages.

## Your Rights and the European Context

On-call arrangements in Europe are shaped by employment law and collective agreements more than in some other markets, and it is worth knowing the broad position.

The Working Time Directive establishes minimum daily and weekly rest periods and limits on average weekly working time across the EU, implemented through national law. Case law has addressed standby arrangements, with the general principle that standby time constitutes working time where the constraints placed on the worker significantly affect their ability to use that time freely. The details depend on national implementation and on how restrictive the arrangement is.

In practice this means: if being on-call requires you to remain within a certain distance, respond within minutes or stay sober and available, it is materially different from carrying a phone with a rare chance of a call, and it may be treated differently in law.

Many European employers also operate under collective agreements that specify standby allowances, compensation for call-outs and rest entitlements after night work.

The practical advice is not legal: ask how standby is compensated, what the expected response time is, whether rest is guaranteed after a night incident, and whether the arrangement is documented. A company that has thought about it will answer immediately.

## Questions to Ask in an Interview

On-call is rarely raised by employers and is entirely reasonable for you to raise. Useful questions:

- Is there an on-call rotation for this role, and how many people are in it?
- How often was the last person paged outside working hours, in the past three months?
- What systems would I be responsible for, and did the team build them?
- Are there runbooks, and can I see an example?
- What is the escalation path at two in the morning?
- How is standby compensated, and is there time off after a night call-out?
- What happens after an incident — is there a review, and do fixes get prioritised?
- What proportion of alerts require action?

The answers are diagnostic beyond on-call itself. A team that can answer precisely has an operational culture; a team that says "it's fine, nothing ever happens" either has nothing in production or is not measuring.

Asking these questions does not make you look reluctant. Experienced hiring managers read it as a sign that you have operated systems before, which is exactly what they are trying to establish.

## Surviving a Shift

Practical habits that make on-call less unpleasant.

**Prepare before your rotation starts.** Check that your access works, your phone receives alerts, the runbooks are where you think they are, and you know who to escalate to. Discovering an expired credential during an incident is a specific kind of misery.

**Keep a shift log.** Every alert, what you did, how long it took. This becomes the evidence for improving the rotation and the material for post-incident reviews.

**Mitigate first, diagnose later.** Restore service or fall back, then investigate. The instinct to understand before acting is strong in analytically minded people and is usually wrong at three in the morning.

**Write it down as you go.** During an incident, note the timeline in a shared channel. It helps whoever takes over and it makes the review honest.

**Hand over properly.** A five-minute conversation at the end of your rotation about anything unresolved or suspicious prevents the next person starting cold.

**Take the rest you are owed.** If you worked at night, do not also work a full day. Teams that treat this as optional lose people.

**Push for fixes.** If the same alert fires three times, the fix is the work, not the response.

## Post-Incident Reviews Worth Doing

The value of an incident is what you learn from it, and that depends on how the review is run.

Keep it blameless in substance, not just in name. The question is what made the error possible, not who made it. A person who was able to break production with one command is a system design issue, not a discipline issue.

Establish the timeline first: when it began, when it was detected, when it was mitigated, when it was resolved. The gap between began and detected is usually the most informative number, and in machine learning systems it is often measured in days.

Then ask four questions. Why did it happen? Why did detection take as long as it did? What would have limited the impact? What will we change, who owns it and by when?

Record the outcome somewhere findable, because the same incident recurs in every organisation that does not.

Crucially, protect time to implement the actions. Reviews that produce a list nobody works on are a ritual, and teams notice quickly.

Good reviews also feed hiring: a team that can describe a real incident and what it changed afterwards is demonstrating operational maturity to candidates far more convincingly than any claim about engineering culture.

## How OnlyAIJobs Fits a Search Where Conditions Matter

OnlyAIJobs is a European job board listing only AI, machine learning and data roles. Vacancies show their exact address and the distance from your home, applications go directly to the employer's own page, browsing is free without an account, and no employer can pay for a higher position in the results.

For working conditions specifically, vacancy text carries useful signals. Postings that mention monitoring, reliability, incident response or operating systems in production tell you that production responsibility is part of the role, which is worth knowing before the final interview. Postings for research, analytics or early-stage projects usually carry no on-call expectation at all.

Neither is better; they are different working lives, and matching the one you want is easier when you can read a range of vacancies side by side rather than filtering AI roles out of a general feed.

To be clear about coverage: listings are currently concentrated in the Netherlands, in cities including Amsterdam, Utrecht, Eindhoven, Groningen, Ede and Capelle aan den IJssel, with employers such as Sendcloud, Mollie, Boltrics, AMCS, Cegeka and Accenture among those listing AI and data roles. Employers can list a first vacancy free via info@onlyaijobs.eu.

## Real example

### The file that arrived one column wider

A pricing model at a European retailer ran nightly. One Sunday, a supplier's feed arrived with an additional column inserted in the middle of the file, shifting every subsequent field by one position.

The pipeline did not fail. Types were compatible, the load succeeded and the model produced prices from nonsense inputs. The first indication was a store manager questioning a price on Monday afternoon.

The on-call engineer was paged at that point — eighteen hours after the incident began. Prices had to be reverted manually, and the day was spent on assessment rather than diagnosis.

The changes that followed were unglamorous and effective: schema validation on ingestion that rejected unexpected structure, a check comparing the distribution of each input feature against the previous seven days, a rule that flagged when output prices moved more than a set amount in aggregate, and an automatic fallback to the previous day's prices when validation failed.

The engineer's summary, repeated to every new joiner since, was that they had monitored the model and not the data, and the data is what broke.

## Key Takeaways

- Machine learning incidents are usually quiet degradations with upstream causes.
- Monitor inputs, not only predictions and infrastructure.
- A sustainable rotation has five or more people, clear scope, runbooks and compensation.
- Fallback behaviour matters more than fast fixes, because retraining is not a hotfix.
- Ask about on-call in interviews; it varies enormously between employers.

## Where to Start

Before your next deployment, write down what the system should do when its inputs are wrong, and implement that fallback. Browse current AI, ML and data vacancies at [onlyaijobs.eu/jobs](https://onlyaijobs.eu/jobs), and if you hire AI talent, list your first vacancy free via info@onlyaijobs.eu.

## Frequently Asked Questions

### (Scenario: candidate comparing offers) Is on-call standard for AI roles in Europe?
It is common where models run in production with operational consequences, and rare in research, analytics and early-stage projects.

### (Scenario: candidate asking about pay) Should standby time be compensated?
Yes, and in many European countries there are legal or collective agreement requirements around standby arrangements and rest periods. Ask how it is handled.

### (Scenario: engineer new to on-call) What if I cannot fix the problem?
Mitigate, do not fix. Fall back, disable, revert or serve the previous output, then diagnose during working hours.

### (Scenario: candidate with caring responsibilities) Can I decline on-call?
Discuss it openly. Some teams accommodate it, some do not, and knowing before you accept is better than negotiating afterwards.

### (Scenario: employer) How do we make on-call sustainable?
Reduce alert noise, write runbooks, pay for it, keep the rotation large enough, and fix the causes of repeated pages rather than tolerating them.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {"@type": "Question", "name": "Is on-call standard for AI roles in Europe?", "acceptedAnswer": {"@type": "Answer", "text": "Common where models run in production with operational consequences; rare in research and analytics."}},
    {"@type": "Question", "name": "Should standby time be compensated?", "acceptedAnswer": {"@type": "Answer", "text": "Yes; many European countries have legal or collective agreement requirements around standby and rest."}},
    {"@type": "Question", "name": "What if I cannot fix the problem?", "acceptedAnswer": {"@type": "Answer", "text": "Mitigate rather than fix: fall back, disable or revert, then diagnose in working hours."}},
    {"@type": "Question", "name": "Can I decline on-call?", "acceptedAnswer": {"@type": "Answer", "text": "Discuss it openly before accepting; some teams accommodate it and some do not."}},
    {"@type": "Question", "name": "How do employers make on-call sustainable?", "acceptedAnswer": {"@type": "Answer", "text": "Reduce alert noise, write runbooks, compensate it and keep the rotation large enough."}}
  ]
}
</script>
