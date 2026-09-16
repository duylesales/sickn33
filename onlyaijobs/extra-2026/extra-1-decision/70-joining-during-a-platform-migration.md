---
Title: "The Team Is Halfway Through a Platform Migration. Is This a Good Time to Join?"
Keywords: joining during cloud migration, data platform migratie baan, warehouse migration job, legacy to cloud data team, migration project data engineer, OnlyAIJobs
Buyer Stage: Decision
Target Persona: B (Experienced AI or ML engineer)
Content Format: Decision Guide
---

# The Team Is Halfway Through a Platform Migration. Is This a Good Time to Join?

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "The Team Is Halfway Through a Platform Migration. Is This a Good Time to Join?",
  "description": "Migrations dominate a data team's work for a year or more. What the job really consists of during one, which migrations are healthy, and what to ask before joining mid-flight.",
  "author": {"@type": "Organization", "name": "OnlyAIJobs", "url": "https://onlyaijobs.eu"},
  "publisher": {"@type": "Organization", "name": "OnlyAIJobs", "url": "https://onlyaijobs.eu"},
  "datePublished": "2027-01-04",
  "mainEntityOfPage": {"@type": "WebPage", "@id": "https://onlyaijobs.eu/blog/joining-during-a-platform-migration"},
  "inLanguage": "en",
  "about": [{"@type": "Thing", "name": "Joining a team during a data platform migration"}, {"@type": "Place", "name": "Netherlands"}],
  "mentions": [
    {"@type": "Organization", "name": "OnlyAIJobs"},
    {"@type": "Thing", "name": "Cloud migration"},
    {"@type": "Thing", "name": "Data warehouse"},
    {"@type": "Thing", "name": "Legacy systems"},
    {"@type": "Thing", "name": "Parity testing"},
    {"@type": "Thing", "name": "Technical debt"},
    {"@type": "Thing", "name": "Decommissioning"},
    {"@type": "Thing", "name": "Vendor contracts"},
    {"@type": "Thing", "name": "Data engineering"},
    {"@type": "Thing", "name": "Change freeze"}
  ]
}
</script>

The vacancy mentions it almost in passing: the team is moving to a new data platform, and you would join during the transition. It sounds like a detail and it is the central fact of the job. A migration consumes a data team's attention for a year or more, reshapes what everyone works on, and determines whether your first year consists of building things or of making sure that old things still produce the same numbers in a new place. Some migrations are among the best learning experiences available. Others are a slow institutional grind that people leave rather than finish.

## What "Migration" Actually Covers

**On-premise to cloud.** The classic version, usually accompanied by a rethink of tooling and access.

**Warehouse replacement.** Moving from one data warehouse to another, with all transformation logic rewritten.

**Reporting tool change.** Hundreds of dashboards rebuilt, and an argument about which ones are still needed.

**ML platform consolidation.** Several teams' ad hoc setups replaced by one supported platform.

**Vendor exit.** Leaving a supplier's environment, often driven by cost or by a contract ending.

The technical work differs, but the shape is the same: everything that currently works must keep working somewhere else, and nobody gets credit for that.

## What Your Job Will Actually Be

Candidates hired during migrations are often surprised by the ratio.

**Porting.** Rewriting transformations, pipelines and jobs in a new environment, mostly faithfully rather than creatively.

**Parity testing.** Proving that the new system produces the same results as the old one, and investigating every difference until you can explain it. This is the bulk of the work and the part that consumes the schedule.

**Archaeology.** Understanding logic written years ago by people who left, including the rules nobody documented.

**Negotiating scope.** Deciding what does not move — the reports nobody reads, the models nobody uses — which is politically harder than the engineering.

**Documentation.** Often written for the first time, because the migration forces the question of what things actually do.

Modelling work continues, usually at reduced volume. If you were hired as a data scientist expecting to build models, ask what proportion of your first year is realistically migration work.

## The Two Versions of a Migration

**The healthy one.** A named sponsor, a funded programme, a decommissioning date for the old platform, a scope decision about what does not move, and explicit acceptance that feature work slows during the transition.

**The zombie.** Started two years ago, no end date, both platforms running in parallel indefinitely, teams maintaining two versions of everything, and nobody empowered to switch anything off. This is a specific and miserable way to spend a year, and it is common.

The distinguishing question is simple: when is the old system being switched off, and who has the authority to do it? A migration without a decommissioning date is not a migration; it is an expansion.

## Why Joining Now Can Be Excellent

**You learn platform engineering properly.** Migrations teach infrastructure, orchestration, data modelling and testing at a depth that ordinary project work rarely reaches.

**You see the whole estate.** Within months you understand every data flow in the organisation, which takes years otherwise.

**You arrive without history.** Newcomers can ask why something exists, and can propose retiring it, in a way that colleagues who built it cannot.

**Budget exists.** Migrations are funded, which often means good tooling and training.

**Visible, finite wins.** Systems moved, reports retired, costs reduced. Progress is measurable, which is not always true of data work.

**It is a strong CV item** in a market where most employers either have migrated recently or are about to.

## Why It Can Be Miserable

**Double running.** Maintaining two platforms doubles the operational load while the schedule assumes it did not.

**Feature freeze.** New work stops during the transition, which is frustrating and, for a new joiner, means less of the work you were hired for.

**Everything is blocked.** Access, permissions, approvals, vendor tickets. Momentum is hard to build.

**Deadlines set by contracts.** When the driver is a licence expiry, the date does not move regardless of readiness, and the last months become unpleasant.

**Credit asymmetry.** A successful migration produces no visible change for users; a failed one is extremely visible.

**No end.** The zombie version, where you spend eighteen months and the old system is still there.

## Questions to Ask Before Accepting

- **When is the old platform being decommissioned, and is that date contractual?**
- **Who sponsors the migration, and is the budget secured?**
- **How long has it been running, and how much is done?** Percentages are unreliable; ask which specific systems have moved.
- **What is being left behind?** A migration with no scope reduction is usually in trouble.
- **What proportion of my first year would be migration work?**
- **Is there a feature freeze, and how long has it been in place?**
- **What happens to the team after the migration?** Occasionally the honest answer is that it shrinks.
- **Who does the parity testing, and is it automated?**

## Warning Signs

- Nobody can name a decommissioning date.
- The migration has already taken longer than originally planned, twice.
- Both platforms are being actively developed.
- The original architects have left.
- The scope has never been reduced; everything is moving.
- The word used is "eventually".

## When to Accept

- You want to build platform and data engineering depth, and you are honest that this is the work.
- There is a decommissioning date with authority behind it.
- The scope has been cut deliberately.
- The team is staffed for double running, or the freeze is explicit and accepted.
- There is a clear picture of what the team does afterwards.
- You are joining early or mid-way rather than into the final scramble.

## When to Decline

- You were hired as a data scientist and expect to model; the reality would be twelve months of porting.
- The migration has no end date and both systems are alive.
- The deadline is contractual and the remaining work is clearly larger than the time.
- The team is smaller than when the migration started.
- Nobody can explain what will be retired.
- You are early in your career and would learn migration mechanics rather than modelling practice.

## How to Make It Work If You Join

Own the parity testing. It is the least popular part of the work and the most valuable position to hold, because everything ships through it and you become the person who knows both systems.

Push for scope reduction from the outside view you still have. In your first weeks you can ask why a report exists without anyone taking offence.

Document as you port. The archaeology you do is knowledge the organisation has never had written down.

Insist on decommissioning. Every system switched off is real progress; every one left running is permanent cost.

And agree what your role becomes afterwards. The conversation is much easier before you join than in month fourteen, when the migration is finishing and nobody has thought about what the team does next.

## What to Negotiate Before You Join

If you decide the migration is worth joining, a few things are much easier to agree before you start than to raise in month eight.

**A written description of the role after the migration.** Not a promise of a promotion — simply what the work becomes once the old platform is switched off. This is the single most useful thing to have in writing, because migrations end and nobody plans for the day after.

**A protected share of non-migration work.** Even one day a week on modelling or analysis keeps your skills current and makes the year survivable. Ask for it explicitly; it will not happen by default.

**Training on the new platform.** Migrations are funded, and platform training during one is an easy request that employers rarely refuse.

**Clarity that you are not the sole owner of double running.** If the team is maintaining two systems, make sure the operational load is shared rather than quietly assigned to the newest person, which is the default outcome.

**Realistic expectations about your first quarter.** You will spend it reading undocumented logic. Say so in the interview, so that it is understood as normal rather than slow.

**A say in scope.** Ask whether new joiners can propose retirements. An organisation that welcomes that question will use you well; one that does not has already decided that everything moves.

None of these requests is unusual, and asking them signals that you have done this before — which, for an employer halfway through a difficult migration, is exactly the impression you want to leave.

## Real example

### An engineer in Amersfoort who asked when the old system dies

An engineer interviews at a retailer migrating from an on-premise warehouse to a cloud platform. The role is advertised as data engineering with machine learning responsibilities.

He asks when the old warehouse is being switched off. The answer is specific: eleven months away, driven by a hardware support contract that will not be renewed, with the decision approved at board level.

He asks what is being left behind. About forty percent of existing reports have been reviewed and marked for retirement, which tells him someone has done the unglamorous work of scope reduction.

He asks what proportion of his first year would be migration. The honest answer is nearly all of it, with modelling work resuming afterwards. He decides that is acceptable, because he wants the platform experience.

The year is hard. Parity testing uncovers three cases where the old system had been producing subtly wrong numbers for years, which creates uncomfortable conversations with finance.

The old warehouse is switched off two weeks late. His second year is what was advertised, and the migration work turns out to be what employers ask him about most in later interviews.

## Key Takeaways

- A migration is the central fact of the job, not a detail: expect porting, parity testing, archaeology, scope negotiation and documentation rather than modelling.
- The distinguishing question is when the old platform is decommissioned and who has authority to do it; without a date, the migration is an expansion.
- Joining can be excellent for platform depth, a complete view of the data estate and the freedom a newcomer has to question what exists.
- It can be miserable through double running, feature freezes, blocked access, contract-driven deadlines and credit asymmetry.
- If you join, own the parity testing, push for scope reduction early, document as you port and agree what your role becomes afterwards.

## Where to Start

Ask when the old platform is switched off before you accept — then compare the answer with employers near you whose migration is already finished.

Browse current AI, machine learning and data jobs by category and distance, free and without an account, at [onlyaijobs.eu/jobs](https://onlyaijobs.eu/jobs).

## Frequently Asked Questions

### (Scenario: candidate offered a role mid-migration) Is joining during a migration a bad idea?
Not inherently. Migrations build serious platform and data engineering depth. The risk is joining one with no end date, or being hired as a modeller into a year of porting.

### (Scenario: candidate assessing the project) What is the most important question?
When the old platform is being decommissioned and who has the authority to switch it off. A migration without a decommissioning date tends to run indefinitely.

### (Scenario: candidate expecting modelling work) Will I still do machine learning?
Usually less than advertised during the transition. Ask directly what proportion of the first year is migration work and when normal work resumes.

### (Scenario: candidate spotting trouble) What are the warning signs?
No end date, both platforms under active development, scope never reduced, original architects gone, and a schedule that has already slipped repeatedly.

### (Scenario: new joiner in a migration) How do I get the most out of it?
Own the parity testing, question what should be retired while you are still new, document the logic you uncover and agree in advance what your role becomes afterwards.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {"@type": "Question", "name": "Is joining during a migration a bad idea?", "acceptedAnswer": {"@type": "Answer", "text": "Not inherently — it builds platform depth; the risk is an endless migration or mis-set expectations."}},
    {"@type": "Question", "name": "What is the most important question?", "acceptedAnswer": {"@type": "Answer", "text": "When the old platform is decommissioned, and who has authority to switch it off."}},
    {"@type": "Question", "name": "Will I still do machine learning?", "acceptedAnswer": {"@type": "Answer", "text": "Usually less during the transition; ask what proportion of year one is migration work."}},
    {"@type": "Question", "name": "What are the warning signs?", "acceptedAnswer": {"@type": "Answer", "text": "No end date, both platforms developed in parallel, no scope reduction and repeated slippage."}},
    {"@type": "Question", "name": "How do I get the most out of it?", "acceptedAnswer": {"@type": "Answer", "text": "Own parity testing, question what should be retired, document logic and agree your next role."}}
  ]
}
</script>
