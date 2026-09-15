---
Title: "Should You Hire an ML Engineer or a Data Scientist First? Matching the Role to Your Real Bottleneck"
Keywords: ml engineer vs data scientist hire, which ai role to hire first, building ai team netherlands, mlops engineer hiring, ai engineer role llm, OnlyAIJobs
Buyer Stage: Decision / Employer Acquisition
Target Persona: C (Hiring manager or recruiter for AI/ML/Data roles)
Content Format: Decision-Stage Guide
---

# Should You Hire an ML Engineer or a Data Scientist First? Matching the Role to Your Real Bottleneck

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Should You Hire an ML Engineer or a Data Scientist First? Matching the Role to Your Real Bottleneck",
  "description": "Many employers hire a data scientist when they need an ML engineer, or the other way around. A decision guide to identifying your actual bottleneck, understanding how roles differ, including the newer AI engineer role, and sequencing hires for an effective AI team.",
  "author": {"@type": "Organization", "name": "OnlyAIJobs", "url": "https://onlyaijobs.eu"},
  "publisher": {"@type": "Organization", "name": "OnlyAIJobs", "url": "https://onlyaijobs.eu"},
  "datePublished": "2026-11-24",
  "mainEntityOfPage": {"@type": "WebPage", "@id": "https://onlyaijobs.eu/blog/ml-engineer-or-data-scientist-first"},
  "inLanguage": "en",
  "about": [{"@type": "Thing", "name": "Choosing between machine learning engineer and data scientist roles"}, {"@type": "Thing", "name": "AI team composition"}],
  "mentions": [
    {"@type": "Thing", "name": "MLOps"},
    {"@type": "Thing", "name": "CRISP-DM"},
    {"@type": "CreativeWork", "name": "Hidden Technical Debt in Machine Learning Systems (Sculley et al., 2015)"},
    {"@type": "Thing", "name": "AI engineer role"},
    {"@type": "Thing", "name": "Large language models"},
    {"@type": "Legislation", "name": "EU Artificial Intelligence Act"},
    {"@type": "Legislation", "name": "Digital Operational Resilience Act (EU) 2022/2554"},
    {"@type": "Legislation", "name": "General Data Protection Regulation (GDPR)"},
    {"@type": "Thing", "name": "Analytics engineering"},
    {"@type": "Thing", "name": "Data engineering"}
  ]
}
</script>

A company has an idea for machine learning and opens a vacancy for a data scientist. Six months later, the data scientist has built several promising models in notebooks — none of which run in production. Another company hires a strong ML engineer who builds an impressive platform, but nobody has defined which business problems the platform should solve. Both companies hired talented people. Both hired for the wrong bottleneck. Choosing between a machine learning engineer and a data scientist — and increasingly an AI engineer — is one of the most consequential decisions in building an AI capability.

## How the Roles Differ

| Role | Core question | Typical work | Typical output |
|---|---|---|---|
| Data analyst | What happened and why? | Reporting, analysis, dashboards | Insights and reports |
| Data scientist | What will happen, what works, and what should we do? | Statistical modelling, experimentation, prototyping ML models | Validated models, experiments, recommendations |
| Machine learning engineer | How do we make models work reliably in production? | Deployment, pipelines, monitoring, scaling, MLOps | Production ML systems |
| Data engineer | How does data get where it needs to be, reliably? | Data pipelines, platforms, integration | Reliable data infrastructure |
| Analytics engineer | How do we turn raw data into trusted models and metrics? | Data modelling, testing, documentation | Clean datasets and metrics |
| AI engineer | How do we build products using foundation models? | LLM integration, retrieval, evaluation, application development | AI-powered applications |

In practice, boundaries overlap and titles vary between organisations. That is precisely why defining the bottleneck matters more than choosing a title.

## Identify Your Real Bottleneck

| Symptom | Likely bottleneck | Role to consider |
|---|---|---|
| Data is scattered, unreliable or inaccessible | Data foundation | Data engineer or analytics engineer |
| Leadership wants AI but cannot name concrete problems | Problem definition and value | Data scientist with strong business skills, or analyst |
| Models exist in notebooks but never reach production | Productionisation | ML engineer |
| Models in production degrade without anyone noticing | Monitoring and operations | ML engineer with MLOps experience |
| The company wants to build features using language models | Application development with foundation models | AI engineer |
| Experiments are run without reliable evaluation | Statistical rigour | Data scientist |
| Many teams want models but each builds infrastructure separately | Platform and standardisation | ML platform engineer |

## Why "Models in Notebooks" Is So Common

The machine learning community has long recognised that the model itself is a small part of a production ML system. A well-known 2015 paper, **"Hidden Technical Debt in Machine Learning Systems"**, described how data dependencies, configuration, monitoring, serving infrastructure and feedback loops create complexity far beyond the model code. Organisations that hire only data scientists often underestimate this complexity. Data scientists may be capable engineers, but their training and incentives usually focus on modelling and experimentation rather than reliable operation.

## Why "Platform Without Problems" Happens Too

The reverse mistake is equally common in technically ambitious organisations. An ML engineer builds pipelines, feature stores and deployment workflows before the organisation has validated which use cases deliver value. Methodologies such as **CRISP-DM** have long emphasised that data projects start with business understanding and data understanding before modelling and deployment. Without that foundation, infrastructure investments risk serving problems that do not matter.

## The Rise of the AI Engineer

The availability of powerful foundation models accessible through APIs and open-source releases has created a newer role: the AI engineer. Instead of training models from scratch, AI engineers build applications that use language models — for example, retrieval-augmented question answering on internal documents, automated document processing or assistants embedded in products.

The skills overlap with software engineering, ML engineering and data science: integrating APIs, designing retrieval pipelines, evaluating output quality, managing costs and latency, handling security and privacy and monitoring behaviour. For organisations whose AI ambitions centre on generative AI applications, an AI engineer with strong software engineering and evaluation skills may be a better first hire than a traditional data scientist.

## Sequencing Hires by Organisational Stage

| Stage | Situation | Suggested sequence |
|---|---|---|
| Exploration | Few clear use cases, data foundation uncertain | Analyst or versatile data scientist, supported by data engineering expertise |
| First production use case | Validated use case, need to deploy | Add ML engineer; ensure data engineering capacity |
| Scaling | Multiple use cases and teams | Add ML platform engineering, analytics engineering and more data scientists |
| Generative AI products | Building features on foundation models | AI engineer with software engineering skills, plus evaluation and data governance support |
| Regulated environment | Models affecting customers under regulation | Add model risk, governance and documentation capacity |

## Regulation Changes the Calculation

**EU Artificial Intelligence Act.** Providers of high-risk AI systems must meet requirements such as technical documentation, record-keeping through automatic logging, accuracy, robustness, cybersecurity and post-market monitoring. These are engineering and operational capabilities as much as modelling capabilities. Organisations building high-risk systems need ML engineering and governance capacity early, not as an afterthought.

**Digital Operational Resilience Act.** Financial entities must manage ICT risks, including risks from third-party providers, which affects how ML systems and external AI services are deployed and monitored.

**GDPR.** Data protection by design, data minimisation and security requirements influence data pipelines and model deployment choices.

## Buying Versus Building: How External Services Change the Choice

The decision about which role to hire first is also influenced by what can be bought rather than built.

**Managed ML platforms.** Cloud providers and data platform vendors offer managed services for training, deploying and monitoring models. These reduce the amount of infrastructure an organisation must build, which can lower the initial need for ML platform engineering — although someone still needs to configure, integrate and operate the services responsibly.

**Foundation model APIs.** Organisations building generative AI features can use models through APIs instead of training their own. This shifts the need from model development towards application engineering, evaluation, security and cost management — the core of the AI engineer role.

**Packaged AI products.** Some use cases, such as document processing or demand forecasting for common retail patterns, can be addressed with existing software products. In such cases, the most valuable first hire may be someone who can evaluate vendors, integrate products and measure results rather than build models.

**Consultancies and interim professionals.** External experts can deliver a first production use case or set up infrastructure, while internal hires take over ownership. This works well when knowledge transfer is planned explicitly.

Buying does not remove the need for internal expertise. Organisations still need people who understand data, can judge whether a product or model works well for their context and can take responsibility for outcomes — including obligations under regulations such as the AI Act.

## Writing the Vacancy for the Right Role

**Describe the bottleneck.** "Our demand forecasting models perform well in testing but are updated manually and not monitored" clearly signals an ML engineering role.

**Avoid unicorn job descriptions.** Vacancies that require expert-level statistics, deep learning research, production infrastructure, data engineering and stakeholder management for one position deter strong candidates and attract people who overestimate their breadth.

**State the team context.** Candidates want to know whether they will be the first data hire, whether data engineering support exists and who owns deployment.

**Categorise correctly.** On specialist job boards, choosing the right category — for example machine learning, development or infrastructure — helps the right candidates find the vacancy.

## Assessing the Right Skills

| Role | What to assess |
|---|---|
| Data scientist | Problem framing, statistical reasoning, model evaluation, experiment design, communication |
| ML engineer | Software engineering, deployment, pipelines, monitoring, testing, cloud infrastructure |
| AI engineer | Application development with LLMs, retrieval design, evaluation of generative outputs, security and cost awareness |
| Data engineer | Data modelling, pipeline reliability, data quality, platform knowledge |

Using a data science interview to hire an ML engineer — or the reverse — is a common reason good hires are missed.

## Collaboration Patterns That Work

Choosing the right roles is only part of the picture; how they work together determines results.

**Pairing from the start.** Teams in which data scientists and ML engineers collaborate from the beginning of a project avoid the handover problem, where a model built without production constraints must be rebuilt later. Engineers can advise on data availability at prediction time, latency and monitoring needs while models are still being designed.

**Shared ownership of outcomes.** When data scientists are responsible only for model accuracy and engineers only for uptime, nobody owns business impact. Shared goals — such as adoption by users or measurable improvements — encourage collaboration.

**Embedded versus central teams.** Small organisations often have one central data team serving the whole business. Larger organisations sometimes embed data scientists in business units while ML platform engineers work centrally to provide shared infrastructure. Both can work, but the model should be chosen deliberately.

**Clear interfaces.** Agree on standards for how models are packaged, documented and handed over, how data contracts are defined and who is on call when a production model fails.

**Involving domain experts.** Planners, underwriters, engineers or clinicians should be part of the team rhythm, not only consulted at the start and end.

## A Concrete Scenario: Correcting the Sequence

A logistics company hires two data scientists to improve delivery time predictions. After a year, they have built accurate models, but predictions are generated manually each week and shared through spreadsheets. Planners stop using them when they become outdated.

The company reassesses its bottleneck. It hires an ML engineer who builds an automated pipeline, integrates predictions into the planning system and sets up monitoring. Within three months, predictions are updated daily and used routinely. The data scientists spend less time on manual runs and more on improving models. The company realises its first hire should have been a combination: one data scientist and one ML engineer — or a data scientist with strong engineering support from the start.

## A Common Misconception

A common misconception is that a sufficiently talented data scientist can cover every AI role. Some individuals are genuinely versatile, particularly in small organisations, but expecting one person to handle problem definition, modelling, data engineering, deployment, monitoring and governance leads to burnout and fragile systems. Another misconception is that generative AI has made data scientists unnecessary. Evaluating model outputs, designing experiments and measuring business impact remain core data science skills — even when the underlying model comes from an API.

## Key Takeaways

- Data scientists focus on problem framing, modelling and evaluation; ML engineers focus on reliable production systems; AI engineers build applications on foundation models; data and analytics engineers build the data foundation.
- Identify your real bottleneck before choosing a title: data foundation, problem definition, productionisation, monitoring or generative AI application development.
- "Models in notebooks" and "platform without problems" are both common results of hiring for the wrong bottleneck.
- Sequence hires according to organisational stage, and account for AI Act, DORA and GDPR requirements that demand engineering and governance capacity.
- Write vacancies around the bottleneck, avoid unicorn descriptions and assess role-specific skills.

## Where to Start

Write down the single biggest obstacle between your current situation and AI delivering value — then choose the role whose core job is removing exactly that obstacle.

Post your AI, machine learning or data vacancy in the right category — first listing free — at info@onlyaijobs.eu.

## Frequently Asked Questions

### (Scenario: company starting with AI) Should our first AI hire be a data scientist or an ML engineer?
It depends on the bottleneck: without clear use cases, start with data science or analysis; with validated models that are not in production, hire an ML engineer.

### (Scenario: company with models in notebooks) Why don't our data scientists' models reach production?
Production ML requires deployment, pipelines, monitoring and operations — skills typically associated with ML engineering rather than modelling.

### (Scenario: company building generative AI features) What is an AI engineer?
A role focused on building applications using foundation models, including retrieval, evaluation, integration, security and cost management.

### (Scenario: employer writing a vacancy) Can one person cover data science and ML engineering?
Some versatile professionals can in small settings, but expecting one person to cover all AI roles often leads to fragile systems and burnout.

### (Scenario: regulated company) Does the AI Act influence which roles we need?
Yes — high-risk AI systems require documentation, logging, robustness and monitoring, which call for engineering and governance capacity.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {"@type": "Question", "name": "Should our first AI hire be a data scientist or an ML engineer?", "acceptedAnswer": {"@type": "Answer", "text": "It depends on the bottleneck: use cases first suggests data science; deployment gaps suggest ML engineering."}},
    {"@type": "Question", "name": "Why don't our data scientists' models reach production?", "acceptedAnswer": {"@type": "Answer", "text": "Production ML requires deployment, pipelines and monitoring skills."}},
    {"@type": "Question", "name": "What is an AI engineer?", "acceptedAnswer": {"@type": "Answer", "text": "A role building applications on foundation models, including retrieval and evaluation."}},
    {"@type": "Question", "name": "Can one person cover data science and ML engineering?", "acceptedAnswer": {"@type": "Answer", "text": "Sometimes in small settings, but it often leads to fragile systems."}},
    {"@type": "Question", "name": "Does the AI Act influence which roles we need?", "acceptedAnswer": {"@type": "Answer", "text": "Yes — high-risk systems need engineering and governance capacity."}}
  ]
}
</script>
