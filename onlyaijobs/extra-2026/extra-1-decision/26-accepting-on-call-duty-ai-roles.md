---
Title: "The Role Includes On-Call Duty. Should You Take It?"
Keywords: on call duty data engineer, consignatiedienst voorwaarden, standby compensation netherlands, mlops on call, production support ai roles, OnlyAIJobs
Buyer Stage: Decision
Target Persona: B (Experienced AI or ML engineer)
Content Format: Decision Guide
---

# The Role Includes On-Call Duty. Should You Take It?

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "The Role Includes On-Call Duty. Should You Take It?",
  "description": "Production machine learning increasingly comes with standby duty. What Dutch working time rules say about on-call, how compensation usually works and which questions reveal whether a rotation is sustainable.",
  "author": {"@type": "Organization", "name": "OnlyAIJobs", "url": "https://onlyaijobs.eu"},
  "publisher": {"@type": "Organization", "name": "OnlyAIJobs", "url": "https://onlyaijobs.eu"},
  "datePublished": "2026-12-13",
  "mainEntityOfPage": {"@type": "WebPage", "@id": "https://onlyaijobs.eu/blog/accepting-on-call-duty-ai-roles"},
  "inLanguage": "en",
  "about": [{"@type": "Thing", "name": "On-call duty in data and ML roles"}, {"@type": "Place", "name": "Netherlands"}],
  "mentions": [
    {"@type": "Legislation", "name": "Working Hours Act (Arbeidstijdenwet)"},
    {"@type": "Thing", "name": "Standby duty (consignatiedienst)"},
    {"@type": "Thing", "name": "Collective labour agreements (cao)"},
    {"@type": "Thing", "name": "MLOps"},
    {"@type": "Thing", "name": "Service level agreements"},
    {"@type": "Legislation", "name": "Digital Operational Resilience Act (EU) 2022/2554"},
    {"@type": "Legislation", "name": "NIS2 Directive (EU) 2022/2555"},
    {"@type": "Thing", "name": "Works council (ondernemingsraad)"},
    {"@type": "Thing", "name": "Occupational physician (bedrijfsarts)"},
    {"@type": "Organization", "name": "OnlyAIJobs"}
  ]
}
</script>

For a long time, data science was an office-hours profession. Models were built, results were presented, and nothing woke anyone at three in the morning. That has changed as machine learning moved into production: fraud scoring that must run before a payment clears, forecasts that feed tomorrow's planning, inspection models on a production line, recommendation systems on a live platform. With that shift comes a line in the job description that candidates often skim past — participation in an on-call rotation. It is worth reading carefully, because a rotation that is well organised is a minor inconvenience and a badly organised one is the most common reason people leave otherwise good engineering jobs.

## What On-Call Usually Means Here

In Dutch employment vocabulary, the relevant concept is standby duty (consignatiedienst): a period outside normal working hours during which you must be reachable and able to respond to a call-out, without being at the workplace.

For data and ML roles it typically means carrying a phone for a week at a time, on a rotation with colleagues, with an escalation path and an agreement about response times. What you are expected to respond to varies enormously: everything from a failed nightly pipeline to a genuine production incident affecting customers.

Related but different arrangements exist. Being genuinely on the premises and available is on-call duty of a different kind with stricter rules; a voluntary "we might call you" culture with no formal rotation is, in practice, the worst version — the obligation without the structure or the compensation.

## What Dutch Rules Say

The **Working Hours Act (Arbeidstijdenwet)** regulates working and rest times, including standby duty. It sets limits on how standby periods can be scheduled, on required rest, and on how call-outs interact with the hours you may work. Collective labour agreements frequently add more detailed rules for a sector — how often you can be scheduled, what compensation applies and what rest follows a night call-out.

Three points matter most in practice.

**Rest after a call-out.** If you are called out at night, rules and agreements exist about the rest you must receive afterwards; being expected to start the next working day as normal after a three-hour incident is a signal that the arrangement is not being managed properly.

**Frequency limits.** There are constraints on how many standby periods can be scheduled in a given timeframe. A rotation with three people rather than six is not just tiring; it may be outside what the rules and the collective agreement contemplate.

**Compensation must be agreed.** Dutch law does not set a single universal standby rate; the compensation usually comes from the collective agreement or the individual contract. What is not acceptable is an expectation with no arrangement at all.

Where a works council exists, arrangements on working time and standby schedules are typically matters it is involved in — which is one reason larger employers usually have clearer rules than small ones.

## Why More AI Roles Now Include It

**Models in production are systems.** Once a model informs a live decision, it needs the same operational treatment as any other production service: monitoring, alerting, incident response.

**The boundary between data and platform has blurred.** MLOps roles sit squarely in operations, and data engineers increasingly own pipelines whose failure has business consequences before the office opens.

**Regulated sectors require resilience.** Financial entities face obligations under the Digital Operational Resilience Act, and organisations in energy, transport, health and digital infrastructure face requirements under the NIS2 Directive. Both push towards documented incident response with people available.

**Batch windows are unforgiving.** A pipeline that must finish before a planning run at six in the morning creates a de facto night shift whether anyone calls it that or not.

## The Questions That Separate Sustainable From Not

Ask these before accepting. The answers vary far more than candidates expect.

- **How many people are in the rotation?** Six or more is comfortable; three is a treadmill.
- **How often did the on-call person actually get called in the last three months?** Ask for the number, not an impression.
- **What happens after a night call-out?** A stated rest arrangement is the clearest sign of a managed rotation.
- **What is the compensation, and where is it written?** Collective agreement, contract or nothing at all.
- **What is the response time expectation?** Fifteen minutes and one hour are different lives.
- **Who else can be escalated to?** A rotation with no second line means every problem is yours.
- **What fraction of alerts are actionable?** High alert volume with low actionability is the definition of an exhausting rotation.
- **Is there time allocated to reduce the alerts?** Teams that treat incident reduction as work improve; teams that treat it as heroism do not.
- **Can I see the runbooks?** Their existence and quality predict your first month on call better than anything else.

## Signals of a Well-Run Rotation

Documented runbooks that a new joiner can follow. A monitoring setup where alerts correspond to real problems rather than noise. A rotation large enough that your turn comes around at a reasonable interval. An explicit onboarding period where you shadow before carrying the phone alone. A blameless review process after incidents, with actions that actually get scheduled. And a manager who has been on the rotation themselves.

## Signals to Be Careful About

A rotation that exists because one person built everything and nobody else understands it. Alerts that fire nightly and are routinely ignored. No compensation arrangement, or one that is "discussed informally". An expectation to be reachable with no formal standby at all. A team that describes on-call with pride in how much they suffer. And systems where the only fix for a failure is to call the person who wrote the code.

## What to Negotiate

On-call is one of the more negotiable parts of an offer, because the constraints are organisational rather than budgetary.

You can ask for a delayed start — joining the rotation after three months rather than immediately, which is reasonable and common. You can ask for the compensation arrangement to be confirmed in writing. You can ask for the rest arrangement after night call-outs to be explicit. You can ask about swaps and cover for holidays, and about what happens during illness or family emergencies.

Where a rotation is genuinely not compatible with your situation — a caring responsibility, a health condition, a partner working nights — say so early. Some roles cannot accommodate it, but many can, and an employer who dismisses the question entirely has told you how flexible they are on everything else.

## Health, Sleep and the Long View

Repeated broken sleep is not a minor inconvenience; it affects health, judgement and mood, and its effects accumulate. If a rotation is affecting your health, the **occupational physician (bedrijfsarts)** is the route to a formal conversation rather than an informal complaint, and Dutch employers have obligations around working conditions.

Take the long view when deciding. A demanding rotation is manageable at some life stages and unsustainable at others. It is entirely legitimate to accept on-call now and to renegotiate it in three years — provided you know that renegotiating is possible, which is itself a question worth asking before you sign.

## What On-Call Gives You

The honest counterweight: operational experience is valuable and rare. Engineers who have carried a pager understand failure modes, monitoring and system design in a way that people who have only built models do not. It teaches you to design for the night you will be woken, which makes you a better engineer during the day.

For a career in production machine learning, some on-call exposure is close to essential. The question is not whether to do it ever, but whether this rotation, at this employer, with these people and this compensation, is one you can sustain.

## On-Call, Hybrid Work and Being Abroad

Two practical questions come up constantly and are rarely covered in the job description.

**Where can you be while on call?** Some employers only require you to be reachable and able to connect within an agreed response time; others expect you to be within a certain travel distance of a site, which matters if physical access is ever needed. That single distinction decides whether a standby week means staying near home or merely keeping your laptop with you.

**Can you be abroad?** A week of standby while visiting family in another country sounds harmless and often is not: connectivity, time zones, access to systems and sometimes security policies about connecting from outside the country all come into play. Some organisations prohibit it outright; others allow it with notice. Ask rather than assume, because doing it unannounced and being unavailable during an incident damages trust quickly.

Related questions worth settling early: whether swaps with colleagues are allowed and how far in advance, what happens if you fall ill during your week, and how holidays are handled in the rotation planning. Teams with clear answers have thought about sustainability; teams that improvise these arrangements tend to improvise the rest of the rotation too.

## Real example

### An MLOps engineer in Rotterdam who asked for the numbers

An MLOps engineer receives an offer that includes a weekly on-call rotation. The role is otherwise excellent: production systems, a good team, twenty minutes from home.

He asks the questions. The rotation has five people. In the last quarter there were eleven call-outs, of which four were at night. Compensation follows the collective agreement, and there is a stated rest arrangement after night incidents. Runbooks exist and he is shown two. The team has a standing agreement that a quarter of engineering time goes to reducing alerts, and the alert count has fallen over the last year.

He accepts, with one addition agreed in writing: he joins the rotation after two months rather than immediately, to learn the systems first.

Eighteen months later he is the person who wrote half the runbooks. The rotation is still there and is still occasionally inconvenient, and he describes it as the reason he learned more in that period than in the three years before it.

## Key Takeaways

- Standby duty is regulated under the Working Hours Act, with collective agreements usually setting compensation, frequency and rest arrangements.
- More AI roles include on-call because production models are systems, MLOps sits in operations, and DORA and NIS2 push regulated sectors towards documented incident response.
- The decisive questions are rotation size, actual call-out frequency, alert actionability, compensation in writing, rest after night call-outs and whether runbooks exist.
- Negotiate a delayed start, written compensation and explicit rest arrangements; raise incompatible personal circumstances early.
- Operational experience is genuinely valuable for a production ML career — the question is whether this specific rotation is sustainable for you.

## Where to Start

Before accepting a role with on-call duty, ask for the call-out numbers from the last quarter — and compare the role with others near you where the operational load is different.

Browse current AI, machine learning and data jobs by category and distance, free and without an account, at [onlyaijobs.eu/jobs](https://onlyaijobs.eu/jobs).

## Frequently Asked Questions

### (Scenario: candidate offered a role with on-call) Is on-call duty normal for data and ML roles in the Netherlands?
Increasingly, yes — particularly for MLOps, data engineering and production machine learning in regulated sectors where incident response is required.

### (Scenario: candidate asking about pay) Is standby duty compensated?
Compensation normally comes from the collective labour agreement or your contract rather than a single statutory rate; what matters is that it is agreed in writing.

### (Scenario: candidate called out at night) Do I have to work normally the next day?
Rules under the Working Hours Act and collective agreements govern rest after call-outs; a team that expects a normal start after a night incident is managing the rotation poorly.

### (Scenario: candidate assessing a rotation) How can I tell whether a rotation is sustainable?
Ask for rotation size, actual call-outs in the last quarter, the share of actionable alerts, whether runbooks exist and whether time is allocated to reducing alerts.

### (Scenario: candidate with care responsibilities) Can I decline on-call duty?
Sometimes. Raise it early: some roles genuinely require it, but many employers can adjust, and their reaction tells you a lot about their flexibility generally.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {"@type": "Question", "name": "Is on-call duty normal for data and ML roles in the Netherlands?", "acceptedAnswer": {"@type": "Answer", "text": "Increasingly yes, especially for MLOps and production ML in regulated sectors."}},
    {"@type": "Question", "name": "Is standby duty compensated?", "acceptedAnswer": {"@type": "Answer", "text": "Usually via the collective agreement or contract; ensure it is agreed in writing."}},
    {"@type": "Question", "name": "Do I have to work normally the next day?", "acceptedAnswer": {"@type": "Answer", "text": "Rest rules apply under the Working Hours Act and collective agreements."}},
    {"@type": "Question", "name": "How can I tell whether a rotation is sustainable?", "acceptedAnswer": {"@type": "Answer", "text": "Ask about rotation size, call-out numbers, alert quality and runbooks."}},
    {"@type": "Question", "name": "Can I decline on-call duty?", "acceptedAnswer": {"@type": "Answer", "text": "Sometimes — raise it early; the employer's reaction reveals their flexibility."}}
  ]
}
</script>
