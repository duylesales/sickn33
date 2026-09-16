---
Title: "The Codebase Is a Mess. Should You Take the Job Anyway?"
Keywords: technical debt data team, legacy pipelines job, notebooks in production, opruimen datateam, joining a messy codebase, OnlyAIJobs
Buyer Stage: Decision
Target Persona: B (Experienced AI or ML engineer)
Content Format: Decision Guide
---

# The Codebase Is a Mess. Should You Take the Job Anyway?

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "The Codebase Is a Mess. Should You Take the Job Anyway?",
  "description": "Manual steps, undocumented pipelines, notebooks in production and no monitoring. Repairing a data team's technical debt can be a career-making role or unpaid heroics — how to tell which.",
  "author": {"@type": "Organization", "name": "OnlyAIJobs", "url": "https://onlyaijobs.eu"},
  "publisher": {"@type": "Organization", "name": "OnlyAIJobs", "url": "https://onlyaijobs.eu"},
  "datePublished": "2027-01-08",
  "mainEntityOfPage": {"@type": "WebPage", "@id": "https://onlyaijobs.eu/blog/joining-a-team-with-heavy-technical-debt"},
  "inLanguage": "en",
  "about": [{"@type": "Thing", "name": "Joining a data team with significant technical debt"}, {"@type": "Place", "name": "Netherlands"}],
  "mentions": [
    {"@type": "Organization", "name": "OnlyAIJobs"},
    {"@type": "Thing", "name": "Technical debt"},
    {"@type": "Thing", "name": "Data pipelines"},
    {"@type": "Thing", "name": "Model monitoring"},
    {"@type": "Thing", "name": "Testing and version control"},
    {"@type": "Thing", "name": "Key person risk"},
    {"@type": "Thing", "name": "Incident response"},
    {"@type": "Thing", "name": "Documentation"},
    {"@type": "Thing", "name": "Engineering standards"},
    {"@type": "Thing", "name": "Production machine learning"}
  ]
}
</script>

The interview goes well until the technical conversation, when the picture emerges. Pipelines run on a schedule nobody fully understands. A model retrains when someone remembers to press the button. There is a notebook in production, a spreadsheet that feeds a dashboard the board reads, and a critical step that only works on one colleague's machine. Nobody is hiding it — they are telling you, because that is why the role exists. The question is whether repairing it is the best year of your career or twelve months of invisible work that nobody thanks you for, and the difference is almost entirely about how the organisation has decided to pay for it.

## What Data Technical Debt Actually Looks Like

**Manual steps in automated processes.** Someone downloads a file each Monday, and everything downstream depends on them remembering.

**No tests, anywhere.** Changes are validated by running things and looking at the output.

**Notebooks in production,** often copied and modified, with three near-identical versions and no way to tell which is authoritative.

**Duplicated logic.** The same business rule implemented differently in four places, producing four slightly different answers.

**Undocumented dependencies.** Nobody knows what breaks if a table is renamed.

**No monitoring.** Failures are discovered when a stakeholder asks why a number looks strange.

**Single points of failure,** where one person's knowledge or one person's laptop is load-bearing.

## Why It Accumulates

Rarely incompetence. Usually speed under pressure: a first data hire building fast to prove value, a consultancy delivering to a deadline, a migration that was abandoned halfway, or years of small changes made by people who left. In Dutch organisations the most common cause is simply that the data function grew faster than anyone's engineering practice, and nobody was ever given time to consolidate.

Knowing the cause matters, because it predicts whether the organisation now understands what it costs.

## The Two Situations

**Acknowledged debt.** The organisation knows, has counted the cost in incidents and delays, and is hiring you to fix it. Budget and time are allocated, and management expects a period where new features slow down. This is a genuinely attractive role.

**Denied debt.** Everyone complains about the mess informally and nobody has agreed to spend anything on it. The expectation is that you will repair the foundations in evenings and weekends while delivering the same roadmap. This is the version that burns people out.

The question that separates them: what has been taken off the roadmap to make room for this work?

## What the Job Will Actually Be

**Archaeology.** Reading undocumented code and reconstructing intent.

**Stabilisation before improvement.** Monitoring first, so you know when things break, then tests, then refactoring.

**Firefighting, initially.** In a fragile system, incidents consume your first months, and you cannot refuse them because the business depends on the output.

**Negotiating what dies.** Retiring the dashboard nobody reads and the model nobody uses is usually the highest-value work available and the hardest to get agreement on.

**Writing things down** for the first time, which is what turns a fragile system into a maintainable one.

Modelling work continues, at reduced volume. If you are hired as a data scientist into a role that is genuinely ninety percent repair, you should know that before accepting.

## Why This Can Be an Excellent Role

**Visible, fast wins.** Going from silent failures to monitored pipelines changes how the whole organisation experiences the data team, within months.

**Authority to set standards.** You are being invited to define how things are done, which is rare and satisfying.

**Cheap credibility.** In a fragile environment, making things stop breaking earns more goodwill than any model.

**Deep learning.** You will understand the entire data estate faster than in any tidy environment, and you will develop engineering judgement you cannot get from greenfield work.

**A strong interview story.** "I inherited a fragile system, here is what I measured, here is what I changed and here is what it did" is one of the most convincing narratives an engineer can offer.

## Why It Can Be a Trap

**Invisible work.** Nobody notices the incidents that did not happen, and in organisations that measure delivered features, a year of repair can look like a year of nothing.

**Unchanged expectations.** Feature pressure continues at the same rate while you also rebuild the foundations.

**No budget.** Tooling, infrastructure and time all cost money, and repair without them is just careful effort against an unchanged system.

**Blame arriving late.** Fragile systems fail. If the culture blames whoever touched it last, that will be you, permanently.

**Skill narrowing.** Two years of repair with no new building can leave you with a CV of remediation and no recent modelling work.

## Questions to Ask Before Accepting

- **What has been removed from the roadmap to make room for this work?**
- **Is there budget for tooling and infrastructure, and how much?**
- **How many incidents were there last quarter, and who handled them?**
- **Who decides what gets retired?**
- **What proportion of my first year is repair versus new work?**
- **Has anyone attempted this before, and what happened?**
- **Does management understand that delivery slows first?** Ask how that was communicated internally.
- **Who else would work on this with me?** Repairing a large estate alone rarely succeeds.

## Warning Signs

- "We'd like you to improve things alongside the normal work."
- Nobody can say how often things break.
- The person who built it is still there and defensive about it.
- There is no budget and the answer is that the platform team will help "when they can".
- The previous person in this role left within a year.
- Every stakeholder describes the data as unreliable and no one treats that as urgent.

## How to Do It Well

**Measure first.** Count incidents, failures, manual steps and time lost. Without numbers, repair is a matter of taste and the first budget cut removes it. With numbers, it is a business case.

**Fix what breaks most, not what offends you most.** The ugliest code is often stable; the elegant pipeline may be the one failing weekly.

**Add monitoring before refactoring.** You cannot safely change what you cannot observe.

**Tie repair to delivery.** Rebuild the pipeline as part of the feature that needs it, rather than asking for a separate cleanup project that will never be prioritised.

**Retire aggressively.** Every system switched off is permanent savings, and identifying the unused ones is easiest in your first months, when asking naive questions is expected.

**Report progress in business terms.** Not "refactored the ingestion layer", but "the Monday report has not failed in eleven weeks, and nobody downloads a file by hand anymore".

## When to Accept

- The debt is acknowledged, quantified and funded.
- Something has been taken off the roadmap.
- You would have authority to retire things.
- There is at least one colleague working on it with you.
- You enjoy this kind of work, which not everyone does.
- The role includes some new building, so your skills stay current.

## When to Decline

- Repair is expected on top of an unchanged workload.
- There is no budget and no tooling.
- The author of the mess is still in charge of decisions about it.
- Nobody can quantify how bad it is.
- You are early in your career and would learn remediation rather than practice.
- You want to build models; this role is engineering, whatever the title says.

## Explaining Debt to People Who Do Not Write Code

Much of the difficulty in these roles is not technical. It is persuading a director who has never seen a pipeline that spending three months on plumbing is a good use of money. Candidates who can do this get budget; those who cannot spend a year asking.

**Translate into consequences, not causes.** Not "the ingestion layer has no error handling", but "when the supplier's file arrives late, the Monday report shows last week's numbers and nobody is told".

**Attach a number to the pain.** Hours lost per week, reports delayed per quarter, decisions made on stale data. Even rough numbers change the conversation, because they convert a technical complaint into a cost.

**Use the near-miss.** Every fragile estate has an incident that almost caused real damage. Describing it once, factually, does more than any architecture diagram.

**Offer a choice rather than a demand.** "We can keep delivering at this pace and accept roughly one failure a week, or pause one project and reduce that substantially" gives management a decision to make rather than a problem to refuse.

**Report the absence of failure.** The hardest part of repair work is that success is silence. Send a short monthly note — what broke, what did not, what changed — so the improvement is visible while it is happening rather than forgotten afterwards.

**Never frame it as blame.** The people who built the system were solving a different problem under different pressure, and some of them are still there. Repair described as criticism gets resisted; repair described as maturation gets funded.

## Real example

### An engineer in Breda who counted the failures first

An engineer joins a wholesaler whose data team of four maintains a fragile estate: nightly jobs that fail two or three times a week, a pricing model retrained manually, and reporting that depends on a file someone copies each morning.

He asks the budget question in the interview. The answer is honest: there is money for tooling and a commitment that one of the two quarterly projects will be dropped, because the finance director has grown tired of unreliable numbers.

His first month is measurement rather than repair. He counts failures, the hours spent recovering from them and the number of manual steps in each process. The total is roughly a day and a half per week across the team.

That number is what secures everything afterwards. Monitoring goes in first, then tests around the three processes that break most, then automation of the two manual steps. Nine dashboards are retired after he asks who opens them and finds that nobody has in a year.

Six months in, failures are down to roughly one a fortnight, and the team has recovered more than a day a week. The pricing model retrains on a schedule.

He then spends his second year building the demand forecasting work that had been impossible while everything was on fire — which is, he says, the part he was hired for and the part that would never have happened without the first year.

## Key Takeaways

- Data technical debt usually reflects speed under pressure rather than incompetence; what matters is whether the organisation now understands its cost.
- Acknowledged, funded debt makes an excellent role; denied debt means repairing foundations in your own time against an unchanged roadmap.
- Ask what has been removed from the roadmap, what the tooling budget is, how many incidents occurred last quarter and who decides what gets retired.
- Measure before repairing, add monitoring before refactoring, tie repair to delivery and retire aggressively while you are still new enough to ask naive questions.
- Report progress in business terms, because invisible work is the main reason good repair years go unrewarded.

## Where to Start

Ask in the first interview how often things break and what was taken off the roadmap — then compare with employers near you whose platforms are already stable.

Browse current AI, machine learning and data jobs by category and distance, free and without an account, at [onlyaijobs.eu/jobs](https://onlyaijobs.eu/jobs).

## Frequently Asked Questions

### (Scenario: candidate offered a cleanup role) Is fixing technical debt good for my career?
It can be excellent, because it builds engineering judgement fast and produces a convincing interview story. It goes wrong when the work is unfunded and expected alongside an unchanged roadmap.

### (Scenario: candidate assessing the offer) What is the single best question?
What has been taken off the roadmap to make room for this work. If the answer is nothing, the organisation has not actually decided to pay for it.

### (Scenario: candidate planning the first months) Where should I start?
With measurement: incidents, failures, manual steps and hours lost. Numbers turn repair from a preference into a business case that survives budget pressure.

### (Scenario: candidate worried about recognition) How do I make the work visible?
Report in business terms — failures avoided, hours recovered, reports that no longer break — rather than in technical descriptions of what you refactored.

### (Scenario: candidate who wants to model) Will I still do machine learning?
Less than the title suggests during the repair period. Ask for the honest proportion of year one, and for some new building to keep your modelling current.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {"@type": "Question", "name": "Is fixing technical debt good for my career?", "acceptedAnswer": {"@type": "Answer", "text": "It can be excellent when funded and acknowledged; poor when expected alongside an unchanged roadmap."}},
    {"@type": "Question", "name": "What is the single best question?", "acceptedAnswer": {"@type": "Answer", "text": "What has been removed from the roadmap to make room for the repair work."}},
    {"@type": "Question", "name": "Where should I start?", "acceptedAnswer": {"@type": "Answer", "text": "Measurement — incidents, manual steps and hours lost — to turn repair into a business case."}},
    {"@type": "Question", "name": "How do I make the work visible?", "acceptedAnswer": {"@type": "Answer", "text": "Report failures avoided and hours recovered rather than technical refactoring details."}},
    {"@type": "Question", "name": "Will I still do machine learning?", "acceptedAnswer": {"@type": "Answer", "text": "Less during repair; ask for an honest proportion and some new building."}}
  ]
}
</script>
