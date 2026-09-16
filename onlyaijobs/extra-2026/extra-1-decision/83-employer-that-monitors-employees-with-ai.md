---
Title: "They Want You to Build AI That Monitors Their Own Staff. Should You?"
Keywords: employee monitoring ai job, personeelsvolgsysteem or instemming, workplace surveillance data scientist, ai act emotion recognition work, gdpr employee monitoring, OnlyAIJobs
Buyer Stage: Decision
Target Persona: B (Experienced AI or ML engineer)
Content Format: Decision Guide
---

# They Want You to Build AI That Monitors Their Own Staff. Should You?

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "They Want You to Build AI That Monitors Their Own Staff. Should You?",
  "description": "Productivity scoring, call analysis, driver tracking and access data: building systems that watch colleagues carries legal constraints and professional consequences. What to check before accepting.",
  "author": {"@type": "Organization", "name": "OnlyAIJobs", "url": "https://onlyaijobs.eu"},
  "publisher": {"@type": "Organization", "name": "OnlyAIJobs", "url": "https://onlyaijobs.eu"},
  "datePublished": "2027-01-11",
  "mainEntityOfPage": {"@type": "WebPage", "@id": "https://onlyaijobs.eu/blog/employer-that-monitors-employees-with-ai"},
  "inLanguage": "en",
  "about": [{"@type": "Thing", "name": "Building employee monitoring systems"}, {"@type": "Place", "name": "Netherlands"}],
  "mentions": [
    {"@type": "Organization", "name": "OnlyAIJobs"},
    {"@type": "Legislation", "name": "EU Artificial Intelligence Act"},
    {"@type": "Legislation", "name": "Works Councils Act (Wet op de ondernemingsraden), article 27"},
    {"@type": "Legislation", "name": "General Data Protection Regulation (GDPR)"},
    {"@type": "Thing", "name": "Data protection impact assessment"},
    {"@type": "GovernmentOrganization", "name": "Autoriteit Persoonsgegevens (Dutch Data Protection Authority)"},
    {"@type": "Thing", "name": "Data protection officer"},
    {"@type": "Thing", "name": "Works council consent"},
    {"@type": "Thing", "name": "Employee privacy"},
    {"@type": "Thing", "name": "Proportionality"}
  ]
}
</script>

The role sounds ordinary until the use case appears. Scoring customer service calls for quality. Analysing how long tasks take in a warehouse. Modelling driver behaviour from telematics. Flagging unusual access patterns in internal systems. Predicting which employees are likely to resign. All of these exist in Dutch organisations, all of them are technically interesting, and all of them make your colleagues the subject of the model rather than its user. That changes the questions you should ask before accepting — not because such work is automatically wrong, but because a great deal of it is built without the conditions that would make it defensible.

## What This Work Covers

**Quality and performance analysis.** Call scoring, handling times, output per shift, error rates attributed to individuals.

**Location and behaviour data.** Vehicle telematics, badge and access logs, warehouse scanners, device activity.

**Communication analysis.** Email, chat or ticket content, usually framed as workload analysis or knowledge management.

**Risk and integrity detection.** Identifying internal fraud, data exfiltration or policy breaches.

**Workforce prediction.** Attrition models, absence prediction, capacity planning at individual level.

The technology is unremarkable. The context is what makes it different: the people in the training data cannot meaningfully refuse, and the consequences for them can include dismissal.

## The Legal Frame You Should Know

**Some practices are prohibited outright.** The **AI Act** bans certain practices, including inferring emotions of people in the workplace, subject to narrow exceptions such as medical or safety reasons. If a proposal involves detecting frustration, stress or engagement from voice or video, that is the first thing to check.

**Employment-related AI is largely high-risk.** The Act's Annex III includes AI used in employment and worker management — recruitment, task allocation, monitoring and evaluation of performance and behaviour, and decisions on promotion or termination. That brings obligations around documentation, data governance, human oversight, logging and monitoring, phased over time.

**Privacy law applies in parallel.** Under the **GDPR**, monitoring requires a lawful basis, and consent is generally problematic in an employment relationship because of the power imbalance, so employers typically rely on legitimate interests — which requires a genuine balancing exercise. A **data protection impact assessment** is normally expected for systematic monitoring, and transparency obligations mean employees must be informed. The **Autoriteit Persoonsgegevens** has published guidance on employee monitoring and has acted on it.

**The works council has a consent right.** Under article 27 of the **Works Councils Act**, an employer needs the works council's consent for decisions on, among other things, arrangements for staff monitoring or facilities for observing employees' presence, behaviour or performance. This is not a consultation but a consent requirement, and a decision taken without it can be challenged.

Rules and timelines change, so verify the current position for the specific system rather than relying on any summary.

## Why the Works Council Question Is Your Best Test

Of everything above, one question separates serious employers from careless ones: has the works council given consent, or been asked?

An organisation that has taken its proposal to the works council has necessarily defined the purpose, the data, the retention and the consequences, because that is what the works council will ask. An organisation that has not is usually still at the stage where someone in management thinks this is a good idea and nobody has examined it.

If you would be joining before that process, ask what happens if consent is refused. The honest answer shapes your first year: either the project is redesigned, or you will be asked to build something that may be stopped.

## Three Kinds of Request, Three Different Answers

**Safety and security.** Detecting unsafe driving, unauthorised access to sensitive systems, or genuine integrity risks. Usually defensible, provided it is proportionate and transparent, and this work has real value.

**Aggregate process improvement.** Understanding where a process is slow, where workload is unevenly distributed, where errors cluster — at team or process level rather than individual level. Frequently the most useful version, and the least intrusive.

**Individual measurement and ranking.** Scoring, comparing and predicting individuals. This is where most problems live: it is the version most likely to be disproportionate, most likely to be inaccurate, and most likely to damage trust irreversibly.

Ask which of these the role is, and notice whether the answer changes between the recruiter and the hiring manager.

## Questions to Ask Before Accepting

- **What is the purpose, stated precisely?** "Insight" is not a purpose.
- **Is it aggregate or individual?** And would individual results be visible to managers?
- **Has the works council been asked, and what did they say?**
- **Is there a data protection impact assessment, and may I see its conclusions?**
- **Who is the data protection officer, and are they involved?**
- **Are employees informed, and what are they told?** Covert monitoring is a serious matter and should end the conversation.
- **What decisions would be taken on the output?** Coaching is different from dismissal.
- **What happens if the model is wrong about someone?** Ask for the process, not the intention.
- **Who can stop this?**

## Signals to Walk Away

- Employees are not to know.
- The proposal involves inferring emotional states at work.
- Nobody can name the lawful basis.
- The works council has objected and management is proceeding anyway.
- Individual scores would feed directly into performance or dismissal decisions with no human review.
- The employer describes privacy questions as obstacles.
- You are told the legal side is "being looked at" and the build should start now.

## Your Position If You Have Concerns

You are an employee, not the accountable party, and the obligations under these rules sit with the organisation. Your practical protection is the same as in any regulated work: raise concerns in writing, address them to the people whose job it is — the data protection officer, legal, the works council where appropriate — and keep a record of what you raised and what was decided.

If the answer is that the concerns are noted and the work proceeds unchanged, you have a decision to make, and it is much easier to make it before you have built the thing than afterwards.

## The Career Angle

Two considerations, in opposite directions.

Done well, this work builds genuine expertise in a scarce area: proportionate design, oversight, documentation, working with a works council and a data protection officer. Employers in regulated sectors value exactly that, and the AI Act's employment provisions mean demand for people who understand it is growing.

Done badly, it attaches your name to a system that colleagues resent and that may become a public problem. Dutch organisations have had visible episodes involving automated systems used on people, and the professionals involved are remembered. It is reasonable to think about whether you would be comfortable explaining this project in an interview in five years.

## When to Accept

- The purpose is specific, the design is proportionate and the output is aggregate wherever possible.
- The works council has been engaged and consent obtained or sought properly.
- There is a data protection impact assessment and a data protection officer involved.
- Employees are informed and the organisation can explain the system to them.
- Human review sits between the model and any consequence for an individual.
- You would have influence over the design rather than only implementing it.

## When to Decline

- Any element is covert.
- The system infers emotions or engagement from voice, face or text at work.
- Individual outputs would drive employment consequences automatically.
- Legal and works council questions are unresolved and the build is expected to start.
- Your objections in the interview are treated as naivety.

## The Version Employees Accept

If you do take this work, it is worth knowing what distinguishes systems that colleagues tolerate from systems they resent, because that difference is largely a design choice and it is usually yours to influence.

**Measure the process, not the person.** Where is the queue slow, which step produces the errors, when does workload spike. The same data answers these questions without ranking individuals, and the operational value is almost always in the process answer.

**Show people their own data first.** A system that gives employees insight into their own work before it gives managers a dashboard lands completely differently, and it is often technically identical.

**Aggregate and delay.** Team-level reporting, with individual detail deleted quickly, satisfies most legitimate purposes. Ask what retention period the purpose actually requires rather than what the platform allows.

**Publish what is measured.** If people can read what the system records and what it is used for, in plain language, most of the resentment disappears. Systems people cannot inspect are assumed to be worse than they are.

**Put a human between output and consequence,** with the ability and the mandate to disagree. A flag that triggers a conversation is very different from a score that triggers a process.

**Involve the people being measured in the design.** Operators, agents and drivers know which variations mean something and which are noise, and their input usually improves accuracy as well as acceptance.

These choices tend to survive works council scrutiny, and they also produce better models — because ranking people on noisy individual data is, quite apart from everything else, usually bad measurement.

## Real example

### An engineer in Tilburg who asked what the works council said

An engineer is offered a role at a logistics company, working on operational analytics. In the second interview the flagship project emerges: analysing scanner and telematics data to identify which employees deviate most from expected handling times.

He asks whether the works council has been consulted. The answer is that it is "on the agenda". He asks what happens if consent is refused, and the manager says they would proceed with aggregate reporting instead.

That answer is the useful one. He asks whether the aggregate version could be the project, and the manager admits it would probably deliver most of the operational value, since the real question is where the process is slow rather than who is slow.

He accepts, on the basis that the first phase is aggregate and that the works council decides on anything individual.

The works council later consents to team-level reporting and refuses individual scoring. The project he builds identifies two layout problems and a scanner configuration issue that were costing more than any individual variation.

His conclusion: the constraint improved the work, and he would not have joined without knowing where the boundary was.

## Key Takeaways

- Employee monitoring is technically ordinary and contextually different, because the people in the data cannot meaningfully refuse and the consequences can include dismissal.
- The AI Act prohibits certain practices, including workplace emotion inference with narrow exceptions, and treats employment and worker management as high-risk; privacy law requires a lawful basis, an impact assessment and transparency.
- Under article 27 of the Works Councils Act, staff monitoring arrangements need works council consent — asking whether it has been given is the single best test of the employer.
- Aggregate process analysis usually delivers most of the value with a fraction of the intrusion; individual scoring is where the problems concentrate.
- Decline covert monitoring, emotion inference and automatic employment consequences; raise concerns in writing and keep a record.

## Where to Start

If a role involves data about colleagues rather than customers, establish the works council position before the final interview — and compare with employers near you doing operational analytics without individual measurement.

Browse current AI, machine learning and data jobs by category and distance, free and without an account, at [onlyaijobs.eu/jobs](https://onlyaijobs.eu/jobs).

## Frequently Asked Questions

### (Scenario: candidate offered a monitoring project) Is building employee monitoring systems acceptable work?
It can be, when the purpose is specific, the design proportionate, the output aggregate where possible and the works council has consented. It is not when any part is covert or automatic.

### (Scenario: candidate checking the rules) What does the law require in the Netherlands?
A lawful basis and transparency under the GDPR, usually an impact assessment, works council consent under article 27 of the Works Councils Act, and compliance with AI Act rules that prohibit some practices and treat worker management as high-risk.

### (Scenario: candidate assessing an employer) What is the best single question?
Whether the works council has been asked and what they said. An employer that has been through that process has had to define purpose, data, retention and consequences.

### (Scenario: candidate with objections) What if I have concerns once I am there?
Raise them in writing with the data protection officer, legal or the works council, and keep a record. Obligations sit with the organisation, but your professional record is your own.

### (Scenario: candidate thinking ahead) How does this look on my CV later?
Well, if you can describe proportionate design, oversight and governance — a scarce specialism. Poorly, if the system became something colleagues resented or that attracted public criticism.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {"@type": "Question", "name": "Is building employee monitoring systems acceptable work?", "acceptedAnswer": {"@type": "Answer", "text": "It can be when purpose, proportionality, aggregation and works council consent are in place; never when covert."}},
    {"@type": "Question", "name": "What does the law require in the Netherlands?", "acceptedAnswer": {"@type": "Answer", "text": "A GDPR lawful basis and transparency, usually a DPIA, works council consent under article 27, and AI Act compliance."}},
    {"@type": "Question", "name": "What is the best single question?", "acceptedAnswer": {"@type": "Answer", "text": "Whether the works council has been asked and what they decided."}},
    {"@type": "Question", "name": "What if I have concerns once I am there?", "acceptedAnswer": {"@type": "Answer", "text": "Raise them in writing with the DPO, legal or the works council and keep a record."}},
    {"@type": "Question", "name": "How does this look on my CV later?", "acceptedAnswer": {"@type": "Answer", "text": "Strong if you can show proportionate design and governance; poor if the system became a public problem."}}
  ]
}
</script>
