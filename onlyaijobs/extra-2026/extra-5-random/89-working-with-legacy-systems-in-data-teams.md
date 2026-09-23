---
Title: "Working With Legacy Systems in Data Teams: The Reality Behind Most European AI Projects"
Keywords: working with legacy systems in data teams, legacy data integration, mainframe erp data extraction, modernising analytics europe, technical debt data platform, OnlyAIJobs
Buyer Stage: Awareness
Target Persona: B (Experienced AI or ML engineer)
Content Format: Working Practice Guide
---

# Working With Legacy Systems in Data Teams: The Reality Behind Most European AI Projects

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Working With Legacy Systems in Data Teams: The Reality Behind Most European AI Projects",
  "description": "A working practice guide to legacy systems in data work: why they persist, how to extract data safely, the archaeology of undocumented logic, modernisation without disruption, and why this experience is valuable.",
  "author": {"@type": "Organization", "name": "OnlyAIJobs", "url": "https://onlyaijobs.eu"},
  "publisher": {"@type": "Organization", "name": "OnlyAIJobs", "url": "https://onlyaijobs.eu"},
  "datePublished": "2027-08-08",
  "mainEntityOfPage": {"@type": "WebPage", "@id": "https://onlyaijobs.eu/blog/working-with-legacy-systems-in-data-teams"},
  "inLanguage": "en",
  "about": [
    {"@type": "Thing", "name": "Legacy system"},
    {"@type": "Thing", "name": "Data integration"},
    {"@type": "Place", "name": "Europe"}
  ],
  "mentions": [
    {"@type": "Organization", "name": "OnlyAIJobs"},
    {"@type": "Thing", "name": "Enterprise resource planning"},
    {"@type": "Thing", "name": "Data migration"},
    {"@type": "Thing", "name": "Change data capture"}
  ]
}
</script>

Conference talks describe data platforms built from nothing. Most European organisations have a manufacturing system installed in 2003, an enterprise resource planning implementation customised beyond recognition, a mainframe running the core business process, and four departmental databases that nobody has authority to change. Working with legacy systems in data teams is not an unfortunate exception to modern AI work; for most practitioners on the continent it is the majority of the job.

## Working With Legacy Systems in Data Teams: Why They Persist

Newcomers often assume legacy systems survive through inertia. Usually they survive for reasons.

**They work.** A system that has processed transactions correctly for twenty years has been debugged by two decades of use, and its replacements have not.

**They encode business rules nobody has written down.** The logic accumulated in that system is the organisation's actual operating procedure, and much of it exists nowhere else.

**Replacement is expensive and risky.** Large system migrations in European enterprises routinely take years, and a meaningful share fail or deliver less than promised.

**Regulatory certification.** In pharmaceutical, aviation, medical and financial contexts, systems are validated, and revalidation is a serious undertaking.

**Nobody owns the decision.** Replacement crosses departments, budgets and political boundaries.

Understanding this matters because it sets your posture. An engineer who treats the old system as an embarrassment to be bypassed will not be trusted with access to it. One who treats it as a constraint to work within will.

## Getting Data Out Safely

The first practical problem is extraction, and the first rule is that you must not affect the operating system.

These systems frequently run the business in real time. A query that locks a table or consumes resources during a production run can stop a factory, delay payments or block order entry. Consequences of this kind end data projects permanently.

Approaches in rough order of preference: read from an existing replica or reporting database if one exists; use change data capture from transaction logs, which imposes minimal load; schedule batch extracts during quiet windows agreed with the system owner; and query directly only with the owner's agreement, with limits, and never during peak processing.

Whatever the method, talk to whoever administers the system before touching it. They know which tables are dangerous, when the nightly jobs run and what broke the last time someone tried this. That conversation is the single most valuable thirty minutes available.

## The Archaeology of Undocumented Logic

A large part of this work is reconstructing what a system does and why, and it has recognisable methods.

**Read the code, including what is commented out.** Disabled sections, old branches and dead functions record decisions. Comments, where they exist, frequently contain a name and a date that lead somewhere.

**Look at the data for evidence.** Distributions change when meanings change. Plot every important field over the full history and investigate each discontinuity. Gaps, spikes, sudden shifts in null rates and changes in value ranges all mark events.

**Find the version history.** Even old systems often have change records, release notes or a ticketing archive. These are tedious and they answer questions nothing else can.

**Talk to long-serving staff.** The most valuable source and the most perishable. People who have worked with a system for fifteen years hold the explanations, and they retire. Ask early, write down what they say, and credit them.

**Check the reports people trust.** Someone built a spreadsheet years ago that the business believes. Reverse-engineering it reveals the definitions actually in use, which frequently differ from the official ones.

Record everything you establish. You are producing documentation that does not exist, and it is among the most durable contributions a data person can make.

## Common Technical Obstacles

A catalogue of what you will actually encounter, and how teams handle it.

**No usable interface.** Some systems offer only screens, reports or file exports. Options include scheduled exports to a shared location, database-level access with the owner's agreement, or reading transaction logs.

**Character encodings and dates.** Older European systems carry a legacy of encodings that mangle accented characters, and date formats that vary by locale and module. Both cause silent corruption.

**Flat files with fixed-width fields.** Still common, still parseable, and unforgiving when a field width changes without notice.

**Codes without a lookup table.** Status fields containing values whose meaning exists only in someone's memory or a printed manual.

**Denormalised history.** Records overwritten in place, so past states are unrecoverable. This is the reason point-in-time analysis is impossible in some systems, and it is a fact to establish before promising anything.

**Batch windows.** Data only available after a nightly process, which constrains any requirement for fresher information.

**Multiple sources of the same fact**, disagreeing, each used by a different department.

None of these are exotic. They are the ordinary texture of enterprise data in Europe, and competence with them is what distinguishes someone who can deliver in a real organisation.

## Building an Abstraction Layer

The strategic response to legacy constraint is to insulate your work from it rather than to fight it.

The pattern is straightforward: extract raw data from source systems with minimal transformation and store it, then build a modelled layer on top that presents clean, documented, stable definitions to everything downstream. Analyses, models and reports consume the modelled layer, never the source directly.

The benefits compound. When a source system changes or is replaced, you adjust the extraction and the mapping rather than every downstream consumer. When two systems disagree, you resolve the conflict once in the model rather than in each analysis. And the modelled layer becomes the place where definitions live, which is where documentation becomes useful rather than ornamental.

Keeping the raw extract matters. When you discover in eighteen months that a transformation was wrong, being able to rebuild from raw history is the difference between a correction and a reconstruction.

Version everything and keep the extraction code in the same repository as the models, so the lineage from source to answer is traceable. In regulated contexts this traceability is required; everywhere else it is what lets you answer the question "where does this number come from" without a three-day investigation.

## Surviving a System Migration

Sooner or later the organisation replaces something, and data teams are frequently informed late and affected severely.

Ask to be involved early. Migration projects focus on transactional continuity and routinely overlook analytics, which means historical data and reporting break at cutover. Being in the room when field mappings are decided is worth more than any amount of remediation afterwards.

Insist on field-level mapping documentation. What becomes what, what is not migrated, what changes meaning, and what history is retained. This document is the difference between a manageable transition and two years of confusion.

Establish what happens to history. Frequently only a limited period is migrated, and the rest remains in an archive or is lost. If you need ten years for forecasting, say so before the decision is made, not afterwards.

Run parallel and reconcile. For at least one full business cycle, produce key figures from both systems and investigate every difference. The differences are where the surprises are.

Expect definitions to shift. New systems impose their own structures, and a metric that meant one thing will mean something slightly different. Document the break explicitly so that future analysts do not misread a discontinuity as a business change.

And protect a period of reduced delivery. Migration consumes data teams, and pretending otherwise leads to commitments nobody can meet.

## Working With the People Who Own Them

The relationships matter as much as the technology, and they are frequently mishandled.

System administrators and long-serving developers have often watched a series of enthusiastic projects arrive, disrupt their systems and depart. Their caution is earned, and treating it as obstruction guarantees a difficult relationship.

What works: ask before you touch anything; explain what you want to do and why; accept constraints about timing and load; report back when something you did caused a problem rather than waiting for them to find out; and credit them when their knowledge made your work possible.

They also hold information that exists nowhere else. The reason a field is populated inconsistently, the workaround introduced during a crisis in 2021, the report that everybody uses and nobody maintains. This is the organisation's institutional memory, and it is available to anyone who asks respectfully.

Be careful about how you describe their systems. Publicly calling something legacy, outdated or a mess in front of the people who maintain it is both discourteous and self-defeating.

In many European organisations these colleagues are approaching retirement, which makes capturing what they know a genuine priority rather than a nicety. Teams that arrange this deliberately — sessions, recordings, written notes — preserve something that cannot be rebuilt.

## Making the Case for Change

Eventually you will want something modernised, and the argument has to be made in terms the organisation accepts.

Arguments that fail: the technology is old; other companies use something better; this is not how modern data teams work. None of these describe a business consequence.

Arguments that work: quantified cost of the current situation, in hours spent, errors made, decisions delayed or opportunities missed; risk, particularly where a system depends on one person, an unsupported platform or a manual process that could fail; regulatory exposure, where data cannot be traced, retained or deleted as required; and a specific, bounded proposal rather than a replacement programme.

Incrementalism is usually the practical route. Extract and model one domain properly, demonstrate the benefit, and use that as the argument for the next. A proposal to replace everything invites a two-year project that will be cancelled; a proposal to fix one painful thing gets approved.

Timing matters. Proposals land during budget planning and die between cycles. Find out when your organisation decides, and be ready.

And be honest about what modernisation will not fix. New tooling over the same undocumented definitions and the same organisational disagreements produces the same problems in a more expensive environment.

## Why This Experience Is Worth Having

Engineers sometimes regard legacy work as a career risk. The evidence across European hiring suggests the opposite.

Almost every organisation of any age has these systems. A candidate who can describe extracting data from an unfamiliar enterprise system without disrupting it, reconstructing undocumented logic, and building a stable modelled layer over an unstable source is describing exactly what most employers need and few candidates have.

It also builds skills that generalise: reading unfamiliar code, investigating data forensically, working with people who are wary of you, and delivering within constraints you cannot remove. These are the abilities that distinguish senior practitioners from strong juniors.

There is a limit worth respecting. Several years working exclusively on extraction from one old system, with no exposure to current tooling or practice, does narrow your options. The balance most people find is legacy integration alongside modern modelling, deployment and evaluation practice, which is anyway how these projects run.

## How OnlyAIJobs Fits This Reality

OnlyAIJobs is a European job board listing only AI, machine learning and data roles. Vacancies show their exact address and the distance from your home, applications go directly to the employer's own page, browsing is free without an account, and no employer can pay for a higher position.

Vacancy text usually reveals what you would actually face. Mentions of integration, migration, enterprise systems or data foundations indicate that the first year involves this work. Postings describing only model development at an organisation with no data platform are describing the same work without acknowledging it, which is worth knowing before you accept.

Neither is bad; they are simply different jobs, and reading several vacancies side by side is the fastest way to tell them apart.

To be clear about coverage: listings are currently concentrated in the Netherlands, in cities including Amsterdam, Utrecht, Eindhoven, Groningen, Ede and Capelle aan den IJssel, with employers such as Boltrics, AMCS, Heijmans, Rexel, Cegeka and Accenture among those listing AI and data roles. Employers can list a first vacancy free via info@onlyaijobs.eu.

## Real example

### The field that meant something else after 2019

An analyst at a European distributor built a margin analysis from the order system, going back ten years. The results showed a sharp and unexplained improvement in 2019 that nobody in the commercial team recognised.

Investigation found no change in pricing or costs. The change was in the data. In 2019 the company had implemented a new discount structure, and rather than adding fields, the implementation had reused an existing column that previously held a surcharge, now storing a discount percentage with the opposite sign convention.

No documentation recorded this. The two people involved had left. The evidence was a commented-out section in a stored procedure and a colleague who remembered the project.

The analysis was rebuilt with a correction for the period, and the finding was written into the data dictionary with the date and the evidence.

The analyst's conclusion was that every long time series in an old system contains at least one of these, and that finding them is the actual work rather than an obstacle to it.

## Key Takeaways

- Legacy systems persist for reasons, and respecting that is the precondition for getting access.
- Never affect the operating system; agree extraction methods with whoever administers it.
- Long time series in old systems contain undocumented changes of meaning; assume this and look for them.
- The people who remember are as important as the documentation, and they are leaving.
- This experience is valuable and transfers to almost every European employer.

## Where to Start

Before your next analysis on historical data, plot volumes and distributions over the full period and investigate every discontinuity. Browse current AI, ML and data vacancies at [onlyaijobs.eu/jobs](https://onlyaijobs.eu/jobs), and if you hire AI talent, list your first vacancy free via info@onlyaijobs.eu.

## Frequently Asked Questions

### (Scenario: engineer frustrated by old systems) Should I push for replacement?
Rarely as your first move. Understand why it exists, deliver something useful within the constraint, and earn the standing to make the argument later with evidence.

### (Scenario: candidate evaluating a role) Is legacy work bad for my career?
No. Integration, migration and archaeology skills are in demand across Europe, because almost every organisation has this problem.

### (Scenario: engineer facing no documentation) How do I understand undocumented logic?
Read the code, examine the data for patterns, and talk to long-serving staff. The last of these is usually the fastest and the most perishable.

### (Scenario: team planning a migration) How do we avoid breaking analytics during a system replacement?
Run both in parallel, reconcile outputs for a full cycle, and map every field explicitly before cutover.

### (Scenario: employer) How do we make this work attractive?
Acknowledge it in the vacancy, resource it properly, and recognise the people who do it rather than treating it as lesser work.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {"@type": "Question", "name": "Should I push for replacing a legacy system?", "acceptedAnswer": {"@type": "Answer", "text": "Rarely first; understand why it exists and deliver within the constraint before arguing."}},
    {"@type": "Question", "name": "Is legacy work bad for my career?", "acceptedAnswer": {"@type": "Answer", "text": "No; integration and migration skills are in demand across Europe."}},
    {"@type": "Question", "name": "How do I understand undocumented logic?", "acceptedAnswer": {"@type": "Answer", "text": "Read the code, examine the data, and talk to long-serving staff."}},
    {"@type": "Question", "name": "How do we protect analytics during a migration?", "acceptedAnswer": {"@type": "Answer", "text": "Run both systems in parallel, reconcile for a full cycle and map every field."}},
    {"@type": "Question", "name": "How do employers make this work attractive?", "acceptedAnswer": {"@type": "Answer", "text": "Acknowledge it honestly, resource it and recognise the people doing it."}}
  ]
}
</script>
