---
Title: "Working as the Only Data Person: How to Succeed When There Is Nobody to Ask"
Keywords: working as the only data person, sole data scientist company, first data hire survival, small team analytics europe, building data capability alone, OnlyAIJobs
Buyer Stage: Awareness
Target Persona: B (Experienced AI or ML engineer)
Content Format: Working Practice Guide
---

# Working as the Only Data Person: How to Succeed When There Is Nobody to Ask

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Working as the Only Data Person: How to Succeed When There Is Nobody to Ask",
  "description": "A working practice guide for the sole data professional in an organisation: choosing what to work on, avoiding unmaintainable systems, finding external technical company, managing expectations and knowing when to leave.",
  "author": {"@type": "Organization", "name": "OnlyAIJobs", "url": "https://onlyaijobs.eu"},
  "publisher": {"@type": "Organization", "name": "OnlyAIJobs", "url": "https://onlyaijobs.eu"},
  "datePublished": "2027-08-14",
  "mainEntityOfPage": {"@type": "WebPage", "@id": "https://onlyaijobs.eu/blog/working-as-the-only-data-person"},
  "inLanguage": "en",
  "about": [
    {"@type": "Thing", "name": "Data professional"},
    {"@type": "Thing", "name": "Small organisation"},
    {"@type": "Place", "name": "Europe"}
  ],
  "mentions": [
    {"@type": "Organization", "name": "OnlyAIJobs"},
    {"@type": "Thing", "name": "Technical debt"},
    {"@type": "Thing", "name": "Mentoring"},
    {"@type": "Thing", "name": "Documentation"}
  ]
}
</script>

A large share of data and AI jobs in Europe are not in teams. They are one person inside a manufacturer, a municipality, a wholesaler, a hospital department or a mid-sized software company, expected to be the entire capability. Working as the only data person offers unusual scope and unusual risk, and the difference between thriving and burning out is mostly a set of decisions made early.

## The Specific Difficulties

**Nobody reviews your work.** Errors reach production, and you will not know which of your habits are bad ones.

**You are every role.** Data engineer, analyst, machine learning engineer, platform engineer, product manager and occasionally the person who fixes the reporting tool.

**Expectations are unanchored.** Colleagues have seen demonstrations and read articles, and have no calibration for what is reasonable.

**Everything is urgent.** With no queue management, every request arrives directly and every requester believes theirs is the priority.

**Your skills can stagnate.** No peers, no code review, no technical discussion, and a year passes.

**Single point of failure.** Your holiday is stressful for everyone, including you.

**Nobody can assess you.** Your manager cannot judge whether your work is good, which affects development, progression and advocacy.

None of this makes the role a mistake. Many people describe it as the most formative period of their career. It does mean managing it deliberately rather than hoping.

## Working as the Only Data Person: Choose Fewer Things

The single most important decision is what not to do.

A sole practitioner who accepts every request produces a stream of small outputs, none of which compound, and is exhausted within a year with nothing durable to show.

The alternative is to pick two or three things that matter, deliver them properly, and hold the line. This requires a sponsor — someone senior who agrees with the priorities and will defend them — and an explicit conversation about what you are not doing.

Prefer work that compounds. A reliable data foundation makes every later analysis faster. A documented definition of a core metric ends a recurring argument. An automated report removes a weekly task permanently. A one-off analysis, however good, buys nothing for next month.

And prefer work you can maintain alone. Which leads to the next point.

## Build Boring Things Deliberately

The strongest technical discipline available to a sole practitioner is restraint.

Every system you build, you maintain, forever, alone. This changes the calculation on every choice. A sophisticated architecture that you enjoy building becomes a burden at the third incident, and an unusual technology choice becomes a liability the moment you leave.

Practical rules that experienced solo practitioners converge on.

**Use what the organisation already supports.** If IT runs a particular database, scheduler and cloud platform, use them. Introducing a parallel stack means you are also the administrator of that stack.

**Prefer managed services over self-hosted components**, because operations time is the scarcest resource you have.

**Choose the simplest approach that solves the problem.** A rule that captures most of the value and can be explained in a sentence beats a model that requires monitoring and retraining, particularly for a first system.

**Automate the recurring, leave the occasional manual.** Automation has a maintenance cost, and a task performed twice a year does not justify it.

**Write it so someone else could run it.** This constraint improves your design and is the only thing protecting your holidays.

The aim is a small number of durable systems rather than an impressive portfolio of fragile ones.

## Finding Technical Company

Isolation is the risk that damages careers, and it has to be addressed from outside the organisation.

**A mentor.** Someone more experienced in your field who will talk to you monthly. Former colleagues, people from your studies, or someone you meet through a community. Many are willing when asked directly, and several European professional communities run informal mentoring arrangements.

**A peer group.** Two or three people at a similar stage, meeting regularly to discuss what they are working on. This substitutes for the corridor conversation you no longer have.

**Code review from outside.** Ask someone to look at something you have built, occasionally. It is the only way to find out which of your habits are poor ones.

**Local meetups.** Most European cities of any size have a data or technology community, and regional ones are often more welcoming than those in the largest cities.

**Online communities** in your specialism, chosen for discussion rather than for announcements.

**Conferences.** Ask your employer to fund one a year; it is a small cost and the justification is straightforward.

Ask for a budget for this explicitly during hiring or at your first review. An employer hiring a sole data person should expect to fund their development, and framing it as risk management rather than as a perk makes the case easily.

## Managing Expectations Without a Buffer

In a team, a manager absorbs unrealistic expectations before they reach the engineers. Alone, they arrive directly, and managing them is part of the job.

**Educate early and repeatedly.** Colleagues genuinely do not know what is feasible. A short, honest explanation of what a project requires — data, time, access, someone to act on the output — changes conversations more than any refusal.

**Give ranges and conditions, not dates.** "Between three and six weeks, assuming I can get access to the order system in the first week" is honest and protects you.

**Show the queue.** A visible list of requests with their status turns prioritisation from a personal refusal into an organisational decision.

**Deliver something early and visibly.** Credibility built on a quick, useful delivery buys patience for the longer work.

**Say no through the sponsor.** "I would need to stop X to do that — shall we ask?" moves the conflict away from you.

**Be honest when something will not work.** The sole practitioner who occasionally says a project is not feasible is trusted far more than one who attempts everything and delivers half of it.

And write down what you deliver. Nobody else is tracking it, and at review time you will need the record.

## Documentation Is Not Optional Here

In a team, documentation is a courtesy. Alone, it is the only thing that makes your work an organisational asset rather than a personal dependency.

The minimum, written as you go: what each system does, what it consumes and produces, and who uses it; a data dictionary for the fields that matter; a decision record for every non-obvious choice; and a runbook for each system covering what to do when it fails, with the failures you have actually seen.

The runbook is the one that matters most and is most often missing. It should be written for a competent colleague who is not you: how to tell whether the job ran, how to restart it, what the common failures look like, and who to call.

Store it where someone will find it, which usually means the repository and a location the organisation already uses, not a personal folder.

Two further habits. Train at least one colleague to perform the basic operational checks — two afternoons, and it transforms your ability to take leave. And record a short walkthrough of each important system; a twenty-minute recording is worth more than pages of text and takes twenty minutes.

None of this is for your successor's benefit. It is what allows you to go on holiday, change role internally, or leave without guilt.

## When the Situation Is Not Workable

Some sole roles cannot be made to work, and recognising that early saves a year.

Warning signs: no sponsor, so priorities change weekly with whoever spoke last; no data worth analysing, because the systems do not record what the questions require; no route to production, so everything you build stops at a presentation; no budget for tooling or development; and a manager who cannot assess your work and does not try.

The most serious is the combination of no sponsor and no route to production, because it guarantees that nothing you do will matter regardless of how well you do it.

Try to fix it first, explicitly. Ask for a sponsor. Propose one bounded project with a defined outcome and an agreed owner for the result. Ask what the organisation wants the capability for. Sometimes the answer is that nobody decided, and asking prompts the decision.

If it cannot be fixed after a genuine attempt, leave without treating it as a failure. Organisations hire data people without knowing why more often than anyone admits, and the outcome is not a reflection of your ability.

For a very junior person, a sole role with no supervision is a poor first job regardless of the organisation's intentions, because you cannot learn the craft with nobody to learn it from.

## What You Gain

The advantages are real and worth stating, because the difficulties above are easier to bear when the benefits are visible.

**Breadth.** You will do every part of the work: sourcing data, building pipelines, modelling, deploying, monitoring, presenting and negotiating scope. Few people in large organisations get that range, and it makes you unusually employable afterwards.

**Ownership.** Your work is visibly yours, and the connection between what you build and what changes in the business is direct and immediate.

**Access.** In a small organisation you talk to the people who decide things. A sole data person often has more influence on strategy than a mid-level analyst in a large company.

**Speed.** No committees, no platform team backlog, no six-week approval. Ideas reach production in weeks.

**Domain depth.** You will understand one business thoroughly, which is the knowledge that compounds most over a career.

**Evidence.** A system you built, deployed and operated end to end is the single most persuasive thing you can bring to any future interview.

Many people who have done this describe it as two or three years that taught them more than the surrounding decade. The condition is that the organisation gave them something real to work on.

## Building Toward a Second Person

The best outcome for a sole practitioner is usually that the role stops being sole, and you can influence whether that happens.

Make the value visible. Keep a simple record of what has been delivered and what it changed, in the organisation's own terms: hours saved, stockouts avoided, errors caught, decisions supported. Present it periodically without being asked.

Make the risk visible too. Say plainly, in writing, that several systems depend on one person, and what the consequence would be. Framed as business continuity rather than as a personal request, this lands with management in a way that a request for help does not.

Prepare the ground. Documentation and runbooks are what make a second hire productive quickly rather than spending three months asking you questions.

Be specific about what you need: a data engineer to own pipelines, an analyst to handle recurring reporting, or a second generalist. A precise request is far easier to approve than a general one.

And if a second person arrives, change how you work. The habits that suited solo work — building quickly, documenting minimally, holding knowledge in your head — become obstacles once there are two of you.

## How OnlyAIJobs Fits a Sole Role

OnlyAIJobs is a European job board listing only AI, machine learning and data roles. Vacancies show their exact address and the distance from your home, applications go directly to the employer's own page, browsing is free without an account, and no employer can pay for a higher position.

Many of the roles that appear on a focused board are exactly these positions: a manufacturer, a wholesaler or a municipality hiring its first or second data person. The vacancy text is worth reading carefully for whether a sponsor, a defined problem and existing data are present, because those three factors determine whether such a role is a career-making opportunity or a difficult two years.

To be clear about coverage: listings are currently concentrated in the Netherlands, in cities including Amsterdam, Utrecht, Eindhoven, Groningen, Ede and Capelle aan den IJssel. Employers can list a first vacancy free via info@onlyaijobs.eu.

## Real example

### The system that could not go on holiday

A data scientist joined a European wholesaler as its first and only data hire. Within eighteen months she had built a demand forecasting system, a pricing analysis, a customer segmentation and three automated reports, all running in production.

It was impressive and it was unmaintainable by anyone else. When she took three weeks of leave, two pipelines failed, nobody could diagnose them, and the operations team reverted to spreadsheets they had not used in a year.

On return she changed her approach rather than her workload. She rebuilt on the tooling the IT department already supported rather than her own stack. She wrote runbooks for every failure she had ever encountered. She trained a colleague in operations to restart jobs and check outputs, which took two afternoons. And she stopped building anything she could not explain to that colleague in an hour.

Her next holiday passed without incident.

Her summary was that her first eighteen months had produced capability that depended entirely on her, which is not capability at all — it is a risk the organisation had not agreed to take.

## Key Takeaways

- Choose two or three things that compound rather than servicing every request.
- Build only what someone else could maintain, using tooling your organisation already supports.
- Find technical company outside the organisation; isolation is the main risk.
- Manage expectations explicitly, because nobody else can calibrate them.
- Document as you go; you are the only source of knowledge about everything you build.

## Where to Start

Write down everything you maintain and ask which of it would survive a month of your absence. Browse current AI, ML and data vacancies at [onlyaijobs.eu/jobs](https://onlyaijobs.eu/jobs), and if you hire AI talent, list your first vacancy free via info@onlyaijobs.eu.

## Frequently Asked Questions

### (Scenario: candidate offered a sole role) Should I take it?
It can be excellent early in a career if there is a sponsor, real data and a defined problem. It is risky with none of those, and worse if you are very junior.

### (Scenario: sole practitioner feeling stuck) How do I keep developing?
Deliberately: a community outside work, a mentor, a peer who reviews your code occasionally, and one substantial technical project a year.

### (Scenario: practitioner overwhelmed by requests) How do I say no?
Through your sponsor and with a visible backlog. "Here is what I am doing and what it displaces" moves the decision to the person who should make it.

### (Scenario: practitioner worried about leaving) What do I owe the organisation?
A proper handover: documentation, runbooks, trained colleagues and systems that survive you. Beyond that, nothing more than any employee.

### (Scenario: employer) How do we support a sole data hire?
Give them a sponsor, a defined scope, a budget for external mentoring or community, and a plan to hire a second person within two years.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {"@type": "Question", "name": "Should I take a sole data role?", "acceptedAnswer": {"@type": "Answer", "text": "It can be excellent with a sponsor, real data and a defined problem; risky without them."}},
    {"@type": "Question", "name": "How do I keep developing alone?", "acceptedAnswer": {"@type": "Answer", "text": "A community outside work, a mentor, occasional external code review and one technical project a year."}},
    {"@type": "Question", "name": "How do I say no to requests?", "acceptedAnswer": {"@type": "Answer", "text": "Through a sponsor and a visible backlog showing what each request displaces."}},
    {"@type": "Question", "name": "What do I owe when leaving?", "acceptedAnswer": {"@type": "Answer", "text": "Documentation, runbooks, trained colleagues and systems that survive you."}},
    {"@type": "Question", "name": "How should employers support a sole data hire?", "acceptedAnswer": {"@type": "Answer", "text": "A sponsor, defined scope, budget for external mentoring and a plan to hire a second person."}}
  ]
}
</script>
