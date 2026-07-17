---
Title: "Software Engineering for AI: Why Traditional Agile and TDD Break Down"
Keywords: software engineering for AI, AI software engineering, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: VP of Engineering / CTO
---

# Software Engineering for AI: Why Traditional Agile and TDD Break Down

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Software Engineering for AI: Why Traditional Agile and TDD Break Down",
  "description": "The introduction of non-deterministic AI models shatters traditional Software Development Life Cycles (SDLC). A deep dive into Evaluation-Driven Development (EDD) and AI software engineering.",
  "author": {
    "@type": "Organization",
    "name": "LaunchStudio",
    "url": "https://launchstudio.eu/en/"
  },
  "publisher": {
    "@type": "Organization",
    "name": "Manifera",
    "url": "https://www.manifera.com"
  },
  "datePublished": "2026-12-06",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://launchstudio.eu/en/blog/software-engineering-for-ai"
  }
}
</script>

For the past two decades, software engineering has been governed by a core assumption: determinism. If a software engineer writes a function that adds two numbers, `add(2, 2)` will always equal `4`. Because code was deterministic, the industry built incredibly robust frameworks around it: Test-Driven Development (TDD), Agile two-week sprints, CI/CD pipelines, and binary pass/fail unit tests.

The integration of Large Language Models (LLMs) into the application stack has shattered this assumption. Software engineering for AI introduces a chaotic, non-deterministic variable into the core of your application. If you prompt an LLM to "summarize this contract," the output will be slightly different every single time. It might return 200 words on Tuesday and 150 words on Wednesday. It might format the output as bullet points today and a dense paragraph tomorrow.

When a VP of Engineering attempts to manage an AI project using traditional software engineering paradigms, the project inevitably stalls. Unit tests fail randomly (flaky tests). Agile estimations become impossible because you cannot predict how long it will take to "tune the prompt" to stop hallucinating. 

To build enterprise-grade AI software, engineering leaders must adopt a fundamentally new Software Development Life Cycle (SDLC) designed specifically for stochastic (randomly determined) systems.

## The Collapse of Traditional Paradigms in AI

Before implementing the solution, we must dissect exactly why traditional software engineering methodologies collapse when applied to AI.

### 1. The Death of Binary Unit Testing (TDD Failure)
In traditional TDD, you write an assertion: `assert(result == "expected_string")`. In AI engineering, this is impossible. If your AI generates a marketing email, you cannot assert an exact string match. Engineering teams try to solve this with regex (checking if certain words exist), but this is brittle. A highly creative, excellent AI email might not use the exact keyword your regex is hunting for, causing a false test failure. Conversely, a terrible, hallucinated email might accidentally contain the keyword, causing a false pass. Traditional CI/CD pipelines break down when tests are flaky.

### 2. The Estimation Impossible (Agile Failure)
In Agile, an engineer estimates a ticket (e.g., "3 Story Points") based on past experience building similar CRUD (Create, Read, Update, Delete) features. In AI, building the feature (the API call to OpenAI) takes 10 minutes. Getting the feature to *stop hallucinating edge cases* might take 3 days, or it might take 3 weeks. The distribution of effort is heavily skewed toward prompt tuning and edge-case mitigation, making sprint velocity tracking virtually useless.

### 3. The Silent Degradation (Monitoring Failure)
Traditional software fails loudly. It throws a `NullReferenceException` or a `500 Server Error`, which triggers an immediate PagerDuty alert. AI software fails silently. If the OpenAI model is updated (e.g., from `gpt-4-0613` to a newer version), the model might suddenly decide to prioritize a different part of your system prompt. The code does not crash. The API still returns a `200 OK`. But the quality of the generated text slowly degrades, annoying users and increasing churn without ever triggering a traditional Datadog alert.

## The New Paradigm: Evaluation-Driven Development (EDD)

To solve these architectural crises, elite AI engineering teams have abandoned TDD in favor of Evaluation-Driven Development (EDD). 

In EDD, you do not test for an exact output. Instead, you use LLMs to grade the outputs of other LLMs against a rubric, generating a statistical distribution of quality rather than a binary pass/fail.

### Phase 1: The Golden Dataset
Instead of writing unit tests, AI software engineering requires a "Golden Dataset." This is a curated database of 100 to 500 diverse inputs (user prompts, uploaded PDFs, complex edge cases) paired with human-approved ideal outputs or specific grading criteria. This dataset acts as the anchor of truth for your non-deterministic system.

### Phase 2: The LLM-as-a-Judge Pipeline
When a developer modifies a prompt or changes the RAG (Retrieval-Augmented Generation) search algorithm, they do not just push to staging. The CI/CD pipeline runs the new codebase against the entire Golden Dataset. 

Because evaluating 500 long-form outputs manually is impossible, the pipeline uses a secondary, highly strictly prompted LLM (the "Judge"). The Judge evaluates the application's output based on a scoring rubric (e.g., "Rate accuracy 1-10", "Check for hallucinations", "Verify brand tone"). 

### Phase 3: Statistical Deployment Guardrails
The CI/CD pipeline aggregates the Judge's scores. A deployment is only allowed if the new prompt achieves a statistically significant improvement (e.g., "Average accuracy score increased from 8.2 to 8.7, and hallucination rate dropped below 2%"). If the score drops, the pull request is blocked. This completely eliminates the "flaky test" problem and replaces it with robust, statistical confidence.

## How LaunchStudio Engineers AI Software

Building an EDD pipeline requires specialized MLOps (Machine Learning Operations) infrastructure that standard web developers rarely possess. 

[LaunchStudio](https://launchstudio.eu/en/), powered by the deep enterprise software engineering roots of [Manifera](https://www.manifera.com/), implements these advanced AI engineering frameworks for scaling SaaS companies. 

Under the architectural vision of CEO Herre Roelevink in Amsterdam, and executed by our dedicated platform engineering teams at 10 Pho Quang Street, Ho Chi Minh City, we transition your team from chaotic "prompt tweaking" into rigorous AI software engineering.

Our EDD Implementation includes:
1. **Evaluation Frameworks:** We integrate specialized open-source evaluation frameworks (like Ragas, LangSmith, or TruLens) directly into your GitHub Actions or GitLab CI.
2. **Deterministic Wrappers:** We implement strict JSON Schema enforcement (using tools like Zod or OpenAI Structured Outputs) to force non-deterministic LLMs to output predictable, type-safe data structures that your traditional frontend can consume without crashing.
3. **Shadow Deployments:** Before a major prompt update goes live, we architect a "Shadow Mode." The new prompt runs in parallel with the old prompt in production, grading the differences silently without showing the new output to the user. Once the statistical confidence is high, we flip the feature flag.

## Real example

### An AI-Native Founder in Action: The Fintech CTO Trapped in Prompt Hell

Marcus is the CTO of a London-based fintech startup that automates accounts payable. The core of their product was an AI engine (built rapidly using Bolt) that ingested PDF invoices in various languages, extracted line items, and mapped them to the company's internal accounting codes.

For the first two months, the system was magical. Then, Marcus's team decided to "improve" the core system prompt to handle a specific edge case involving VAT taxes in France. 

A junior developer tweaked the prompt, ran three test invoices locally, saw that it worked perfectly, and pushed the code to production. 

The next morning, the French VAT invoices were processed flawlessly. However, the prompt change had a catastrophic, unintended consequence on German invoices. The AI suddenly started hallucinating supplier names and swapping billing addresses. Because the traditional unit tests only checked if the API returned a `200 OK` and a valid JSON object, the CI/CD pipeline had passed perfectly. The system failed silently. 

By the time customers noticed the corrupted accounting data four days later, Marcus's team had to manually reverse thousands of incorrect ledger entries. The developers became terrified of touching the prompt again. Feature development ground to a complete halt.

Desperate to regain engineering velocity, Marcus engaged LaunchStudio.

The Manifera engineering team conducted an immediate intervention. In 15 business days, they completely replaced Marcus's traditional CI/CD pipeline with an Evaluation-Driven Development (EDD) framework. 

First, they gathered 400 historical invoices (the Golden Dataset) covering every language, edge case, and format the system had ever encountered. 
Second, they implemented an LLM-as-a-Judge evaluation script using LangSmith. 
Now, when a developer tweaked a prompt to fix a French VAT issue, the CI/CD pipeline automatically processed all 400 invoices using the new prompt. The Judge LLM compared the new extractions against the Golden Dataset. If the French accuracy went up, but the German accuracy dropped by even 1%, the pipeline explicitly blocked the merge and highlighted exactly which German invoices failed.

**Result:** Engineering velocity returned instantly. Developers were no longer paralyzed by fear because the EDD pipeline provided a mathematical safety net. The hallucination rate in production dropped to 0.1%, and Marcus's team successfully scaled the system to process 50,000 invoices a month for major European enterprises.

> *"We were trying to manage a neural network using the same tools we used to manage a basic database. It was a disaster waiting to happen. LaunchStudio didn't just fix our code; they re-educated our entire engineering department on how to actually build software in the AI era. The evaluation pipeline they built is the most valuable piece of infrastructure we own."*
> — **Marcus Sterling, CTO, LedgerAI (London)**

**Cost & Timeline:** €12,500 (Launch & Grow Package with Enterprise MLOps & EDD Add-on) — production-ready and deployed in 15 business days.

---

## Frequently Asked Questions

### (Scenario: VP Engineering planning a sprint) How do we estimate time for AI features if prompt engineering is so unpredictable?

You must decouple the "deterministic" work from the "stochastic" work. Estimate the API integration, the database schema, and the UI components using standard Agile points. For the prompt engineering and tuning phase, use Timeboxing (e.g., "We will spend exactly 3 days tuning this prompt against the Golden Dataset. Whatever score it achieves by Friday is what we launch, and we iterate next sprint.").

### (Scenario: Developer writing tests) Can I use traditional testing frameworks like Jest or PyTest for AI applications?

Yes, but only for the deterministic "plumbing." You should absolutely use Jest to test that your database connection works, your API routes require authentication, and your frontend renders correctly. However, you must *not* use Jest to test the actual text output of the LLM. For the LLM output, you must trigger an EDD script that utilizes a Judge model to score the semantic meaning of the response.

### (Scenario: CTO reviewing architecture) What is the biggest risk of silent AI degradation?

The biggest risk is that an underlying foundational model (like GPT-4) receives a silent update from the provider that slightly alters its reasoning patterns. Your prompt, which worked perfectly for six months, suddenly starts missing edge cases. Because no code changed on your end, standard monitoring won't catch it. LaunchStudio mitigates this by running your Golden Dataset against production daily; if the average score drops overnight, you receive an immediate alert.

### (Scenario: Founder managing AI costs) Doesn't running an LLM to judge another LLM in CI/CD get incredibly expensive?

It can, if engineered poorly. However, you do not need to use the most expensive model (like GPT-4o or Claude 3.5 Sonnet) as the Judge for every test. LaunchStudio architects EDD pipelines to use fast, cheap models (like GPT-4o-mini or Llama 3 8B) for 90% of the routine evaluation tasks (checking JSON structure, verifying keyword presence), reserving the expensive models only for complex semantic grading, keeping CI/CD costs highly optimized.

### (Scenario: Engineering Director scaling a team) How do we prevent developers from overriding the EDD pipeline?

The EDD pipeline must be enforced at the repository level via branch protection rules (e.g., in GitHub). A pull request physically cannot be merged into the `main` branch unless the automated Evaluation action returns a "Pass" status based on the statistical threshold you set. LaunchStudio configures these strict Platform Engineering guardrails so that governance is automated and mathematically enforced, removing human bias from the merge process.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "How do we estimate time for AI features if prompt engineering is so unpredictable?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Decouple deterministic work from stochastic work. Estimate API integrations and UI using standard Agile points. For prompt tuning, use Timeboxing (e.g., 'We spend exactly 3 days tuning against the Golden Dataset, then launch the best version and iterate')."
      }
    },
    {
      "@type": "Question",
      "name": "Can I use traditional testing frameworks like Jest or PyTest for AI applications?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes, but only for the deterministic 'plumbing' (DB connections, auth, UI). You must not use Jest to test the text output of the LLM. For that, trigger an EDD script that utilizes a Judge model to score the semantic meaning of the response."
      }
    },
    {
      "@type": "Question",
      "name": "What is the biggest risk of silent AI degradation?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "The risk is that the LLM provider updates the foundational model, altering its reasoning. Your prompt suddenly starts failing without any code changes on your end, so standard monitoring misses it. LaunchStudio runs your Golden Dataset daily to detect silent score drops."
      }
    },
    {
      "@type": "Question",
      "name": "Doesn't running an LLM to judge another LLM in CI/CD get incredibly expensive?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "It can if engineered poorly. LaunchStudio architects pipelines to use fast, cheap models (like GPT-4o-mini) for 90% of routine evaluation tasks, reserving expensive models only for complex semantic grading, keeping CI/CD costs optimized."
      }
    },
    {
      "@type": "Question",
      "name": "How do we prevent developers from overriding the EDD pipeline?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Enforce it at the repository level via branch protection rules. A pull request cannot be merged unless the automated Evaluation action returns a Pass status based on your statistical threshold. LaunchStudio configures these guardrails to automate governance."
      }
    }
  ]
}
</script>
