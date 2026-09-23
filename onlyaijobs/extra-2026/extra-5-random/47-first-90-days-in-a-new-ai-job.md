---
Title: "Your First 90 Days in a New AI Job: How to Build Credibility Before You Build Models"
Keywords: first 90 days in a new ai job, starting a data science role, new job machine learning engineer, onboarding yourself data team, early career credibility, OnlyAIJobs
Buyer Stage: Awareness
Target Persona: B (Experienced AI or ML engineer)
Content Format: Working Practice Guide
---

# Your First 90 Days in a New AI Job: How to Build Credibility Before You Build Models

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Your First 90 Days in a New AI Job: How to Build Credibility Before You Build Models",
  "description": "A working practice guide to the first 90 days in a new AI job: what to do in each month, how to learn the data and the organisation, which early wins matter, and the mistakes that cost credibility.",
  "author": {"@type": "Organization", "name": "OnlyAIJobs", "url": "https://onlyaijobs.eu"},
  "publisher": {"@type": "Organization", "name": "OnlyAIJobs", "url": "https://onlyaijobs.eu"},
  "datePublished": "2027-06-27",
  "mainEntityOfPage": {"@type": "WebPage", "@id": "https://onlyaijobs.eu/blog/first-90-days-in-a-new-ai-job"},
  "inLanguage": "en",
  "about": [
    {"@type": "Thing", "name": "Onboarding"},
    {"@type": "Thing", "name": "Data science career"},
    {"@type": "Place", "name": "Europe"}
  ],
  "mentions": [
    {"@type": "Organization", "name": "OnlyAIJobs"},
    {"@type": "Thing", "name": "Stakeholder management"},
    {"@type": "Thing", "name": "Data quality"},
    {"@type": "Thing", "name": "Machine learning engineer"}
  ]
}
</script>

The first three months in a technical role set expectations that are surprisingly durable. People form a view of whether you are careful, whether you finish things and whether you understand the business, and that view is hard to revise later. The good news is that the first 90 days in a new AI job reward ordinary behaviour rather than heroics: listening, asking, and shipping one modest thing that works.

## First 90 Days in a New AI Job, Month One: Learn the Terrain

Resist the urge to demonstrate value immediately. The instinct is understandable and it produces work that solves the wrong problem.

**Meet people deliberately.** Not only your team: the people who produce the data, the people who use the output, the person who maintains the source system nobody understands. Ask what they do, what annoys them and what they wish existed. Twenty such conversations in a month is realistic and will make you more useful than any model.

**Learn the data physically.** Query the main tables yourself. Count rows, check keys for uniqueness, look at distributions, find the nulls. Ask what one row represents in each table, and write the answers down. This is how you find the things nobody mentions.

**Read what exists.** Previous analyses, documentation however poor, runbooks, incident histories, the code of whatever is in production. The archaeology tells you what has been tried.

**Ask about the failures.** What projects were cancelled and why. This is the single most informative question a new joiner can ask, and people usually answer it honestly.

## Month Two: Ship Something Small

Around week five or six, deliver something visible, useful and finished. Not a model — a fix, a report someone needed, a monitoring check, a query that answers a recurring question, a documented dataset.

The purpose is not the artefact. It is to demonstrate that you finish things, to learn the path from idea to production while the stakes are low, and to give colleagues a reason to trust you with something larger.

Choose something with a real user who will notice, and finish it properly: tested, documented, handed over.

## Month Three: Take Something Real

By the third month you should own a piece of work that matters, with a defined outcome and a stated timeline. This is also the point to start forming and voicing opinions: what you think is fragile, what you would prioritise, what you believe is being measured wrongly.

Do it carefully. Your observations are valuable precisely because you are still new, and they are easy to deliver badly. "I noticed X — is there history behind it?" works. "This is wrong" rarely does.

## The Questions to Ask in Week One

A prepared list makes early conversations far more productive, and people respond well to being asked properly.

To your manager: What does success look like for me at three months and at a year? What is the most important thing the team does? What would you fix if you had capacity? Who should I talk to that I would not think of? How do you prefer to be updated?

To your teammates: What is in production and who maintains it? What breaks most often? Which data sources do you trust and which do you not? What should I be careful about? What took you longest to learn here?

To data producers: What does this system actually record? What changed in the last two years? What do people misunderstand about your data?

To users of your output: What decision do you make with this? What do you do when you disagree with it? What would you like that you do not have?

To anyone who has been there a long time: What has been tried before? Why did it stop?

Write the answers down. In two months you will have forgotten half of them, and the notes become the informal documentation nobody else has.

## Learning the Data Properly

The fastest route to credibility in a data role is knowing the data better than people expect you to after six weeks.

Do this by hand rather than by reading documentation. For each important table: count the rows, check whether the supposed key is unique, look at the date range and find the gaps, examine null rates per column, list the distinct values of categorical fields, and plot the volume over time to find the discontinuities where a system changed.

Then reconcile one number against something the business publishes. If the organisation reports a figure for last quarter, reproduce it. The process of failing to reproduce it teaches you more about the data than any handover document.

Keep a running file of findings: this field means something different before 2024, this identifier is duplicated for historical reasons, this source is refreshed weekly despite appearing daily. Share it with the team after a month. It is genuinely useful to them and it demonstrates exactly the kind of care that people want to see in a new colleague.

Do not be embarrassed to ask what a column means. Every experienced person in the team has asked the same question, and most of them still do not know.

## Choosing a First Project Wisely

If you are given a first project, evaluate it. If you are choosing one, choose carefully. The properties that matter are the same.

**It has a real user who will notice.** Work nobody consumes teaches you nothing about the organisation and gives you no advocate.

**It is finishable in four to six weeks.** Your first delivery should complete while you are still new.

**It does not depend on someone unavailable.** A project blocked on a colleague on leave or a supplier's timeline will stall through no fault of yours and still look like a slow start.

**It touches the systems you need to learn.** The path to production, the data platform, the deployment process.

**Its success is measurable.** So the conversation about whether it worked is short.

Good first projects in data teams: a monitoring check on an existing system, a data quality report, a recurring manual analysis automated, documentation of an important dataset, or a small improvement to something already running.

Poor first projects: a new model in a domain you do not understand, anything requiring approval from three departments, and anything described as strategic.

## Understanding the Organisation, Not Just the Team

Technical people often onboard into the team and never onboard into the company, which limits them for years.

Spend some of the first three months learning how the organisation actually works. How does it make money, or, in the public sector, what is it accountable for? Which department has influence? Who decides budgets, and when in the year? What is the annual rhythm — a retail peak, a reporting cycle, a regulatory deadline — that determines when people have attention for your work?

Attend meetings you are not required to attend, at least once. Read the annual report or the published strategy. Ask a commercial colleague to explain their job.

This matters practically. A proposal that lands in the middle of budget planning is considered; the same proposal three weeks later waits a year. A project framed in terms of a target the organisation is already measured against gets support; the same project framed technically does not.

It also protects you. Knowing which projects are politically contested, and which sponsor is likely to leave, tells you where to invest your effort. New joiners frequently attach themselves enthusiastically to work that everyone experienced knows is about to be cancelled.

## Mistakes That Cost Credibility Early

A short list, all common and all avoidable.

**Rewriting things in the first month.** The existing system is ugly for reasons, some of which are good. Proposing a rewrite before understanding them is the fastest way to be categorised as someone who does not listen.

**Comparing everything to your previous employer.** Occasionally useful, quickly tiresome. Say "somewhere I worked did X, which helped with Y" once, not weekly.

**Over-promising to make a good impression.** A new joiner who commits to an ambitious timeline and misses it has spent credibility they had not yet earned.

**Disappearing into analysis.** Three weeks of silent work followed by a large presentation is high-risk. Short, frequent updates are safer and build trust faster.

**Not asking, to avoid looking inexperienced.** Everyone can tell when a new person is stuck, and struggling silently for two days is what looks inexperienced.

**Ignoring the unglamorous colleagues.** The person who maintains the source system, the operations staff, the analyst who has been there twelve years. They hold the knowledge that determines whether your work is correct.

**Dismissing the existing approach in front of stakeholders.** Someone in the room probably built it.

## Working With a Manager You Do Not Know Yet

The relationship with your manager is formed early and is worth being deliberate about.

Establish how they want to be updated and at what frequency, then do it consistently. A short written update every week — what you did, what is next, what is blocking you — costs ten minutes and prevents the most common early problem, which is a manager who is unsure what you are doing and starts checking.

Ask explicitly what success looks like at three months. If the answer is vague, propose your own version and ask whether it is right. Ambiguous expectations are the most common cause of a disappointing first review, and they are almost always resolvable by asking.

Raise problems early and with a proposal attached. Managers can absorb bad news; they resent discovering it late.

Ask for feedback at thirty days rather than waiting for a formal review. The question "is there anything you would like me to do differently?" is uncomfortable and extremely efficient.

If the relationship is not working — no time, no clarity, no support — say so once, plainly and constructively, before concluding the job is wrong. A surprising proportion of these situations are inattention rather than intent.

## When the Job Is Not What Was Described

Occasionally the reality differs materially from the vacancy: the data does not exist, the team is being restructured, the project you were hired for was cancelled before you started, or the role is analysis when you were promised engineering.

First, wait. Three months is short, and early impressions of organisations are frequently wrong in both directions. Some of what looks like chaos is simply unfamiliarity.

Then, if the gap is real, raise it factually with your manager: this is what I understood the role to be, this is what I am doing, can we talk about the difference. Many such gaps are accidental and fixable, particularly in organisations that were hiring for a plan that changed.

If it cannot be fixed, you have a decision to make, and it is better made deliberately than by drifting. Note that in most European countries a probationary period exists with shorter notice on both sides, and using it is legitimate rather than shameful.

Leaving a job within a year is not the reputational catastrophe people fear, particularly when you can explain it calmly and without criticising the employer. Staying three unhappy years in a role that does not develop you is the more expensive choice.

## How OnlyAIJobs Fits a Career in Motion

OnlyAIJobs is a European job board listing only AI, machine learning and data roles. Vacancies show their exact address and the distance from your home, applications go directly to the employer's own page, browsing is free without an account, and no employer can pay for a higher position.

Even when you have just started somewhere, an occasional look at the market is useful rather than disloyal: it tells you what skills employers are asking for, how your role compares, and what the next step might require. Note that the platform does not send email job alerts, so a short periodic check works better than waiting to be notified.

To be clear about coverage: listings are currently concentrated in the Netherlands, in cities including Amsterdam, Utrecht, Eindhoven, Groningen, Ede and Capelle aan den IJssel. Employers can list a first vacancy free via info@onlyaijobs.eu.

## Real example

### The new hire who asked about the excluded rows

A machine learning engineer joined a European logistics company and spent his first weeks reading the code of the existing delivery prediction system rather than proposing improvements.

He found a filter that excluded about four per cent of shipments from training data, with no comment. He asked the team about it. Nobody knew; the person who wrote it had left two years earlier.

He investigated. The excluded shipments were those handled by one partner network whose data had been unreliable during a migration in 2024. The data had been fixed eighteen months ago, and the exclusion had simply never been removed. Those shipments were also the ones the model predicted worst, because it had never seen them.

Removing the filter and retraining improved accuracy measurably for a segment the operations team had complained about for a year.

He had written no new model. His manager said afterwards that this was the moment the team decided he was worth listening to.

## Key Takeaways

- Spend the first month learning people, data and history rather than proving yourself.
- Ask what was cancelled and why; it is the most informative question available.
- Ship one small, finished thing by week six to learn the path to production.
- Take on something substantial by month three, with a defined outcome.
- Deliver observations as questions, not verdicts.

## Where to Start

In your first week, list ten people to talk to and three tables to query yourself, and book both. Browse current AI, ML and data vacancies at [onlyaijobs.eu/jobs](https://onlyaijobs.eu/jobs), and if you hire AI talent, list your first vacancy free via info@onlyaijobs.eu.

## Frequently Asked Questions

### (Scenario: new joiner feeling unproductive) Is it normal to feel useless for weeks?
Yes. Most experienced people report two to three months before feeling genuinely productive, and longer in complex domains.

### (Scenario: new joiner with no assigned work) What if nobody gives me anything to do?
Find something. Ask what is broken, what nobody has time for, or what question keeps being asked. Then propose it rather than waiting.

### (Scenario: new joiner seeing obvious problems) Should I say what I think is wrong?
Yes, as questions and gradually. Your fresh perspective is valuable for a few months, so use it, but assume there is history you do not know.

### (Scenario: new joiner in a first job) How much should I ask?
More than feels comfortable. Agree a threshold with your manager, such as asking after thirty minutes stuck, and follow it.

### (Scenario: employer) What should we provide in the first 90 days?
Access on day one, a named buddy, a defined first project and a conversation at thirty days about how it is going.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {"@type": "Question", "name": "Is it normal to feel useless for weeks?", "acceptedAnswer": {"@type": "Answer", "text": "Yes; most people report two to three months before feeling genuinely productive."}},
    {"@type": "Question", "name": "What if nobody gives me work?", "acceptedAnswer": {"@type": "Answer", "text": "Find something broken or unowned and propose it rather than waiting."}},
    {"@type": "Question", "name": "Should I say what I think is wrong?", "acceptedAnswer": {"@type": "Answer", "text": "Yes, as questions and gradually, assuming there is history you do not know."}},
    {"@type": "Question", "name": "How much should I ask?", "acceptedAnswer": {"@type": "Answer", "text": "More than feels comfortable; agree a stuck threshold with your manager."}},
    {"@type": "Question", "name": "What should employers provide in the first 90 days?", "acceptedAnswer": {"@type": "Answer", "text": "Day-one access, a named buddy, a defined first project and a thirty-day conversation."}}
  ]
}
</script>
