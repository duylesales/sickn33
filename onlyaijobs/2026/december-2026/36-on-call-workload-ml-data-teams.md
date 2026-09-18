---
Title: "On-Call, Night Batches and Burnout in ML and Data Teams: Questions to Ask Before You Accept"
Keywords: on call data engineer netherlands, standby compensation cao, burnout data teams, production ml operations, workload machine learning jobs, OnlyAIJobs
Buyer Stage: Consideration / Job Search
Target Persona: B (Experienced AI or ML engineer)
Content Format: Career Guide
---

# On-Call, Night Batches and Burnout in ML and Data Teams: Questions to Ask Before You Accept

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "On-Call, Night Batches and Burnout in ML and Data Teams: Questions to Ask Before You Accept",
  "description": "As models move into production, data teams inherit operational duty without always inheriting the practices that make it sustainable — and Dutch rules on standby, working time and workload apply.",
  "author": {"@type": "Organization", "name": "OnlyAIJobs", "url": "https://onlyaijobs.eu"},
  "publisher": {"@type": "Organization", "name": "OnlyAIJobs", "url": "https://onlyaijobs.eu"},
  "datePublished": "2026-12-18",
  "mainEntityOfPage": {"@type": "WebPage", "@id": "https://onlyaijobs.eu/blog/on-call-workload-ml-data-teams"},
  "inLanguage": "en",
  "about": [{"@type": "Thing", "name": "On-call duty"}, {"@type": "Thing", "name": "Workload and wellbeing at work"}],
  "mentions": [
    {"@type": "Thing", "name": "Standby duty (consignatiedienst)"},
    {"@type": "Thing", "name": "Incident response and runbooks"},
    {"@type": "Thing", "name": "Service level objectives"},
    {"@type": "Organization", "name": "Works council (ondernemingsraad)"},
    {"@type": "Thing", "name": "Psychosocial workload (PSA)"},
    {"@type": "Legislation", "name": "Dutch Working Hours Act (Arbeidstijdenwet)"},
    {"@type": "Legislation", "name": "Dutch Working Conditions Act (Arbowet)"},
    {"@type": "Legislation", "name": "Collective labour agreement (CAO) standby provisions"},
    {"@type": "Thing", "name": "Data pipeline monitoring"},
    {"@type": "Thing", "name": "Team capacity planning"}
  ]
}
</script>

For most of the field's short history, data work was office-hours work. If a model was late, someone fixed it in the morning. That has changed: pipelines feed ordering systems, models price products overnight, dashboards drive Monday decisions, and increasingly a data team's output is something the business cannot start the day without. Operational duty has followed, and many teams inherited it without the practices, the agreements or the compensation that operations professionals have insisted on for decades.

## Why Data Teams Became Operational

The shift has three causes, and recognising them helps you evaluate an employer honestly.

**Models entered production.** A recommendation engine, a pricing model or a replenishment forecast is no longer an analysis; it is a service with a deadline.

**Pipelines became dependencies.** Once a warehouse feeds finance reporting, customer communication and regulatory submissions, a failed load is an incident rather than an inconvenience.

**Teams stayed small.** The people who built the systems are the only ones who understand them, so the on-call rotation is drawn from a group of five rather than fifty.

None of this is inherently a problem. Operating something people depend on is satisfying work. The problem is when operational responsibility arrives without reducing project work, without a rotation large enough to be humane, and without anyone asking whether the system is actually reliable enough to be operated.

## What Dutch Rules Say

The Netherlands regulates working time and standby duty more explicitly than many countries, and candidates should know the outline.

**Working time.** The Working Hours Act sets limits on working hours and minimum rest periods. Being called out at night affects the rest period that must follow, which has practical consequences for the next working day.

**Standby duty.** The Act contains specific provisions for standby arrangements — how often they may be scheduled, and how call-outs interact with rest. Many collective agreements add compensation: an allowance for being available, plus payment or time off for actual call-outs.

**Workload as a health and safety matter.** Under the Working Conditions Act, employers must assess and address risks including psychosocial workload — work pressure is a formal occupational risk, not a personal failing. A structurally overloaded team is a health and safety issue with a legal dimension.

**Works council involvement.** Arrangements concerning working times and standby schedules typically fall within the works council's remit, which means employees have a collective route to change them.

The practical upshot: if you are asked to carry a pager, ask what the agreement says. In a covered employer, there is often an entitlement you were not told about.

## The Warning Signs Before You Accept

Certain answers in an interview reliably predict an unsustainable situation.

**"We're a small team so everyone pitches in."** Translation: there is no rotation, and you are always available.

**"It rarely triggers."** Ask for numbers. How many alerts last month, how many outside office hours, how many required action? Teams that cannot answer are not measuring, which usually means the burden is worse than they believe.

**"We don't really have on-call, but..."** Informal availability is the worst arrangement: the obligation without the compensation, the schedule or the right to be unavailable.

**"We're catching up on tech debt."** This can be honest and healthy, or it can mean firefighting is the job. Ask what proportion of the last quarter went on unplanned work.

**No runbooks.** If incident response depends on knowing who to call rather than on documentation, the load falls permanently on whoever knows most.

**One person who knows the system.** If that person is on holiday, what happens? If the honest answer is "we hope nothing breaks", you are being hired into a risk, not a role.

## A Concrete Scenario: The Night Batch That Ate a Team

A retail data team owns a nightly pipeline feeding ordering. It runs at two in the morning and must complete before six. Failures happen perhaps twice a month.

Initially two people handle it informally. Then the pipeline grows, upstream systems change more often, and failures rise to weekly. Nobody has agreed a rotation, so the same two people wake up. One of them starts declining holidays because the other cannot cover alone.

Six months later, one leaves. The remaining person now carries it alone, and the team's project work stops entirely because all capacity goes to keeping the pipeline alive. Recruitment to replace the leaver takes four months, and the new person cannot be put on call for another three.

The failure was not technical; it was structural. A rotation of two is not a rotation. What would have prevented it is exactly what the team never did: measure the load, state a maximum, and make the business trade off between new features and the reliability work that would reduce failures.

## What a Healthy Arrangement Looks Like

Good practice is not exotic, and you should expect to see most of these.

**A rotation of at least five or six people**, so that duty comes around every few weeks rather than constantly and holiday cover exists.

**Compensation.** An allowance for standby, payment or time off in lieu for call-outs, and explicit permission to start late after a bad night.

**A defined scope.** What is on call actually for? A clear list of systems and severity levels, with an agreement that everything else waits until morning.

**Runbooks.** Documented steps for the failures that actually occur, written by the people who fixed them last.

**Alert hygiene.** Someone owns the alert set and removes ones that fire without requiring action. Alert fatigue is the leading cause of missed real incidents.

**Time for reliability work.** A share of capacity explicitly reserved for reducing the causes of incidents, protected from feature pressure.

**Post-incident review without blame.** The question is what in the system allowed this, not who made a mistake.

**The option to opt out.** People with caring responsibilities, health conditions or other constraints should have a route out of the rotation that does not damage their career.

## Workload Beyond On-Call

On-call is the visible part; chronic overload in data teams is usually quieter.

The typical pattern is demand without prioritisation. Every department wants a dashboard, an extract, an analysis, and a small team says yes to all of it because saying no feels unhelpful. Six months later the team is entirely reactive, nothing is documented, and the individuals are exhausted by the sheer number of context switches rather than by any single task.

The organisational fix is an intake process with an owner who decides priority, and a visible backlog so stakeholders can see the queue. The individual fix is narrower but real: making your workload visible rather than absorbing it silently, because a manager who cannot see the load cannot defend it.

In the Dutch context this is also formally supported. Work pressure is an occupational health topic, occupational health services exist, and both the works council and the employer's own risk assessment obligations provide legitimate channels. Using them is not escalation; it is how the system is designed to work.

## If You Are Already in It

For people reading this from inside an unsustainable situation, a few practical steps in order.

Measure first: a simple log of alerts, hours outside working time and what triggered them. Data changes the conversation from a complaint into a problem statement.

Then raise it as a team rather than individually, because a structural problem presented by one person reads as a personal capacity issue.

Then propose the specific change — rotation size, alert reduction, reserved reliability capacity — rather than only describing the pain. Managers respond better to proposals than to symptoms.

If nothing changes after a genuine attempt, treat it as information about the organisation rather than about yourself. Burnout recovery in the Netherlands is a long process with real protections, but the far better outcome is not needing them.

## Which Roles Carry Operational Duty, and Which Do Not

Candidates often assume on-call is universal in data work. It is not, and choosing deliberately is easier than renegotiating later.

**Usually operational.** Data platform and data engineering roles at companies whose business depends on daily pipelines. Machine learning engineering where models serve live traffic. Analytics engineering in organisations with early-morning reporting deadlines. Anything with the word "platform" in the title at a company operating around the clock.

**Sometimes operational.** Data science roles in product teams, where the team owns what it ships. Whether that includes nights depends entirely on the company's culture and the criticality of the service.

**Rarely operational.** Research and applied research positions, consultancy and project work, policy and governance roles, most public sector analysis, academic and institute positions, and the majority of business analytics roles.

There is an honest trade-off here that is worth naming. Operational roles typically pay better and offer the deep satisfaction of running something real; non-operational roles offer predictability, which for people with caring responsibilities or health considerations may be worth more than the difference in salary.

Neither choice is more serious than the other, and treating on-call as a badge of commitment is a cultural failure rather than a professional standard. Ask early, choose deliberately, and be sceptical of any employer that treats the question itself as a lack of dedication.

## Key Takeaways

- Data teams have inherited operational duty as models and pipelines became business-critical, often without the accompanying practices.
- Dutch law regulates working time, standby and rest, and treats work pressure as an occupational health risk.
- Collective agreements frequently entitle you to standby compensation that employers do not always mention.
- A rotation of two is not a rotation; healthy arrangements have five or six people, runbooks, alert hygiene and protected reliability time.
- Measure the load before raising it, and raise it as a team — a structural problem framed individually reads as personal capacity.

## What Good Employers Do Differently

Across the Dutch market, the teams that run production data systems sustainably tend to share a handful of habits that cost little and change everything.

They treat reliability as a product requirement rather than an engineering preference, which means the business agrees explicitly how reliable a pipeline needs to be and accepts the cost. They allocate a fixed share of capacity to reducing incident causes and defend it during busy periods, on the grounds that firefighting is more expensive than prevention. They rotate on-call widely enough that it is a mild inconvenience rather than a defining feature of the job, and they pay for it properly.

They also make failure discussable. Post-incident reviews look at the system rather than the person, alerts that fire without action are deleted rather than tolerated, and someone senior says out loud that a 3 a.m. page is a design failure, not a normal cost of doing business.

Candidates can detect most of this in one interview question: "Tell me about the last incident and what changed afterwards." An employer with healthy practice will describe a concrete change to the system. One without will describe how quickly someone fixed it — which tells you exactly what your nights will look like.

## Where to Start

Ask three numbers in your next interview: how many out-of-hours alerts last month, how many people are in the rotation, and what proportion of last quarter was unplanned work. The answers describe the job better than the vacancy text does.

Browse current AI, machine learning and data vacancies at [onlyaijobs.eu/jobs](https://onlyaijobs.eu/jobs).

## Frequently Asked Questions

### (Scenario: candidate offered a role with on-call) What should I ask before accepting?
Rotation size, number of out-of-hours alerts last month, compensation arrangements, and whether runbooks exist.

### (Scenario: employee doing informal standby) Am I entitled to compensation?
Many collective agreements provide standby allowances and compensation for call-outs; check the applicable agreement and raise it if it is not being applied.

### (Scenario: employee after a night call-out) Can I be expected to work a normal day?
Working time rules set minimum rest periods, and a call-out affects them; employers should adjust the following day accordingly.

### (Scenario: overloaded team member) Is work pressure a formal issue in the Netherlands?
Yes — psychosocial workload is part of the employer's occupational risk assessment obligations, and the works council has a role.

### (Scenario: candidate who wants no on-call) Are there data roles without it?
Yes — analysis, research, consultancy and many project-based roles have no operational duty; ask explicitly rather than assuming.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {"@type": "Question", "name": "What should I ask before accepting a role with on-call?", "acceptedAnswer": {"@type": "Answer", "text": "Rotation size, out-of-hours alert counts, compensation arrangements and whether runbooks exist."}},
    {"@type": "Question", "name": "Am I entitled to standby compensation in the Netherlands?", "acceptedAnswer": {"@type": "Answer", "text": "Many collective agreements provide standby allowances and call-out compensation; check the applicable agreement."}},
    {"@type": "Question", "name": "Can I be expected to work normally after a night call-out?", "acceptedAnswer": {"@type": "Answer", "text": "Working time rules set minimum rest periods that a call-out affects, so the following day should be adjusted."}},
    {"@type": "Question", "name": "Is work pressure treated as a formal issue in Dutch workplaces?", "acceptedAnswer": {"@type": "Answer", "text": "Yes — psychosocial workload falls under the employer's occupational risk assessment obligations."}},
    {"@type": "Question", "name": "Are there data roles without on-call duty?", "acceptedAnswer": {"@type": "Answer", "text": "Yes — analysis, research, consultancy and many project-based roles carry no operational duty."}}
  ]
}
</script>
