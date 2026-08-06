---
Title: "Custom Software Development Services: The Due Diligence Framework for CTOs"
Keywords: custom software development services, evaluate software vendor, technical due diligence, offshore development agency, IT vendor audit, Manifera
Buyer Stage: Consideration / Vendor Selection
Target Persona: A (CTO / VP Engineering)
Content Format: Audit Checklist & Framework
---

# Custom Software Development Services: The Due Diligence Framework for CTOs

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Custom Software Development Services: The Due Diligence Framework for CTOs",
  "description": "A ruthless technical due diligence framework for evaluating custom software development services. Teaches CTOs how to ignore marketing claims and audit an agency's Git history, CI/CD pipelines, and SAST tools.",
  "author": {"@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com"},
  "publisher": {"@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com"},
  "datePublished": "2026-09-11",
  "dateModified": "2026-08-06"
}
</script>

Every agency selling **custom software development services** has a beautiful website. They all claim to use "Agile methodologies." They all promise "scalable architecture." They all have logos of impressive past clients.

If you make your vendor selection based on slide decks and sales calls, you are rolling dice with your company's IT budget. 

Marketing collateral is a lagging indicator of engineering quality. The only leading indicator of engineering quality is how the agency actually builds software when the client is not looking. 

This is a ruthless, technical due diligence framework for CTOs evaluating offshore or nearshore engineering partners. Stop asking them what they build. Start auditing *how* they build it.

## The Technical Audit: 4 Areas to Interrogate

When evaluating an agency, demand to see a sanitized repository or schedule a screen-share walkthrough of a current, non-NDA project. If they refuse because "it's confidential," they are hiding a chaotic engineering culture. 

Here is what you look for.

### 1. Audit the Git Commit History (The Reality Check)

Marketing says: *"We have a rigorous peer review process."*
Git history says: The truth.

**What to look for:**
- **Commit frequency:** Are developers committing small, atomic changes daily, or pushing 4,000 lines of code at 11:30 PM on a Friday? Massive, infrequent commits mean there is no CI/CD pipeline and code reviews are superficial.
- **Commit messages:** Are the messages descriptive (`fix(auth): handle JWT expiration edge case`) or useless (`fixed bug`, `update`, `WIP`)?
- **Pull Request (PR) hygiene:** Open a closed PR. Did the reviewer actually leave comments about architecture and edge cases, or did they just type "LGTM" (Looks Good To Me) and hit approve? 

This isn't a subjective preference — it is measurable. SmartBear's landmark 10-month study of 2,500 code reviews covering 3.2 million lines of code at Cisco Systems found that reviews of 200-400 lines of code, conducted over 60-90 minutes, catch 70-90% of existing defects. Push that same review past 400 lines, or rush it faster than roughly 500 LOC per hour, and defect-detection rates drop sharply — reviewers physically cannot hold that much context in working memory. A 4,000-line PR merged with a single "LGTM" is not a code review in any measurable sense; it is a formality.

### 2. Audit the CI/CD Pipeline (The Safety Net)

Marketing says: *"We build enterprise-grade software."*
The pipeline says: Whether that software is actually testable.

**What to look for:**
- **Automated Gates:** Does the pipeline automatically block merges if unit tests fail or if the code coverage drops below 80%? If humans can bypass the tests, the tests do not exist.
- **Static Application Security Testing (SAST):** Are they running tools like SonarQube, Semgrep, or Snyk on every commit to catch hardcoded secrets and SQL injections? This is not a theoretical risk category: GitGuardian's State of Secrets Sprawl 2025 report found that 23.77 million new hardcoded secrets (API keys, credentials, tokens) were pushed to public GitHub repositories in 2024 alone — a 25% year-over-year increase — and a separate finding in the same research line showed that a majority of leaked secrets remain valid and exploitable for years after exposure because nobody rotated them. A repository scanner that only runs manually, or not at all, is relying on developer discipline to catch a mistake that industry-wide data shows developers make millions of times a year.
- **Deployment mechanism:** Do they deploy via automated Docker containers to a staging environment, or are they manually uploading files via FTP?

As Herre Roelevink, Managing Director at Manifera, states regarding offshore due diligence:
> *"The difference between a cheap agency and a professional partner is visible in their deployment pipeline. A cheap agency spends 100% of your budget on typing code. A professional partner spends 20% on the CI/CD pipeline because they know that is the only way to guarantee the code won't break your business in production."*

### 3. Audit the Database Schema Evolution (The Foundation)

Marketing says: *"Our architectures scale."*
The database says: If it will collapse at 10,000 users.

**What to look for:**
- **Migration scripts:** How do they handle database changes? Are they using formal migration tools (Flyway, Prisma, Laravel Migrations) that are version-controlled, or are developers manually executing SQL scripts on the production database?
- **Indexing strategies:** Look at a table with a high read volume. Are there indexes? Are they using foreign keys to enforce referential integrity? 
- **Soft deletes vs. Hard deletes:** Do they actually delete data (destroying historical audit trails), or do they use soft deletes (e.g., `deleted_at` timestamps)?

### 4. Audit the Observability Stack (The "Day 2" Readiness)

Marketing says: *"We provide ongoing support."*
The observability stack says: If they can actually find the bug when the server crashes at 2 AM.

**What to look for:**
- **Structured Logging:** Are they writing flat text logs (`Error: connection failed`), or are they using structured JSON logging with request IDs so you can trace a user's journey across microservices?
- **Error Tracking:** Do they use Sentry, Datadog, or New Relic to capture unhandled exceptions automatically, or do they rely on users emailing them screenshots of error pages?

## The Fifth Audit Area: Documentation and Knowledge Continuity (The Bus Factor)

Marketing says: *"We provide comprehensive documentation."*
Reality says: Whether your project survives if the two engineers who built it both quit next month.

This is the audit area CTOs skip most often, because it's boring, and it's the one that costs them the most eighteen months later when they try to switch vendors or hire an in-house team to take over. The financial scale of this problem is not niche: Stripe's Developer Coefficient report, based on a survey of over 1,000 developers and 1,000 C-level executives across five countries, found that engineers spend roughly 42% of their working week — about 17.3 of a 41.1-hour average — dealing with technical debt and maintaining bad code rather than shipping new functionality. Poor documentation and tribal knowledge are direct contributors to that number: every hour a new engineer spends reverse-engineering undocumented decisions is an hour not spent building.

**What to look for:**
- **The "hit by a bus" test:** Ask the agency directly: "If your lead developer on my project left tomorrow, how long would it take a new engineer to become productive?" A mature agency answers in days, because onboarding runbooks, architecture diagrams, and a living README exist. An immature agency answers in "weeks," because the knowledge only exists in one person's head.
- **Architecture Decision Records (ADRs):** Do they maintain a lightweight, version-controlled log of *why* major technical decisions were made (e.g., "Chose PostgreSQL over MongoDB because of relational reporting needs — decided 2025-11-03")? Without ADRs, every new engineer re-litigates old arguments, and every architectural choice looks arbitrary six months later.
- **API documentation that isn't a lie:** Ask to see their OpenAPI/Swagger spec, then ask when it was last regenerated. A spec that is manually written and hasn't been touched in four months is actively misleading — it documents an API that no longer exists. Elite teams auto-generate API docs directly from the code (via annotations or contract-first tooling), so the documentation and the running system can never drift apart.
- **Runbooks, not tribal knowledge:** For any production incident (database failover, payment gateway timeout, third-party API outage), is there a written runbook a mid-level, on-call engineer can follow at 3 AM, or does the on-call rotation just escalate straight to the CTO's personal phone?
- **Offboarding and IP handover clauses:** What does the contract say happens to source code, infrastructure credentials, and documentation if you terminate the engagement? A professional partner hands over a complete, running repository with CI/CD, environment variables (redacted appropriately), and a transition document. A weak partner treats this as a negotiation.

**The live test that separates real documentation from theater:** during your technical audit call, ask the agency to have a developer who has *never touched this specific project* attempt to run it locally, live, on screen-share, using only their own internal documentation. Time it. If it takes over 30 minutes to get a local environment running from a clean checkout, their onboarding documentation does not actually work — it merely exists.

This audit area matters most for offshore and nearshore engagements specifically, because geographic and time-zone separation means you cannot simply walk over to someone's desk when documentation gaps surface. The written artifact has to do the work that a hallway conversation would do in a co-located team.

## The Code Review Math: Sizing Reviews So They Actually Catch Bugs

Most CTOs treat "we do code review" as a binary — either the agency does it or it doesn't. That framing misses the variable that actually predicts whether reviews catch anything: batch size. The Cisco/SmartBear research referenced above is granular enough to turn into an audit tool of its own. Use it to interrogate an agency's actual review discipline, not just its stated policy.

| PR / Diff Size | Realistic Defect Detection Rate | What It Signals |
|---|---|---|
| Under 200 LOC | Highest — reviewers can hold full context | Disciplined, incremental engineering culture |
| 200–400 LOC, reviewed over 60–90 minutes | 70–90% of existing defects caught | The evidence-based sweet spot; treat this as the benchmark |
| 400–1,000 LOC | Sharp drop-off; reviewers skim rather than read | Review is happening, but is largely theater |
| 1,000+ LOC, or reviewed in under 10 minutes | Close to zero meaningful defect capture | "LGTM" rubber-stamping; functionally no review at all |

**How to apply this in a vendor interview:** ask to see the diff size distribution of the last 20 merged PRs on a real project (most Git hosting platforms expose this directly). If the median PR exceeds 400-500 lines, or if PRs regularly get approved within minutes of being opened regardless of size, the agency's "rigorous peer review process" is a marketing sentence, not an engineering practice — no matter how confidently it was said in the sales call.

## Comparison: Marketing Claims vs. Technical Reality

Use this matrix during your next vendor interview.

| The Agency Claims... | The CTO Should Ask... | The Red Flag Answer |
|---|---|---|
| "We do Agile." | "Show me your automated testing pipeline." | "We rely on our QA team to manually test before releases." |
| "We build scalable microservices." | "Show me your distributed tracing setup (e.g., Jaeger)." | "We just use standard server logs." |
| "Our code is secure." | "What SAST tools run in your CI pipeline?" | "Our senior developers review all code for security." |
| "We have high code quality." | "Show me a PR from last week." | The PR has 500 lines changed, 0 comments, and was merged in 3 minutes. |

## Why Manifera Welcomes the Audit

At Manifera, we built our [custom software development](https://www.manifera.com/services/custom-software-development/) model for CTOs who know how to look under the hood. 

Our Hybrid Offshore model works precisely because our Dutch architects enforce these technical standards on our Vietnamese engineering pods. We don't just promise clean architecture; we enforce it through automated CI/CD gates, mandatory SAST scanning, and strict PR review policies.

We invite technical due diligence. If you are evaluating partners for your next enterprise build, schedule a technical deep-dive with our architecture team. We will show you our pipelines. 

---

## Frequently Asked Questions

### (Scenario: CEO evaluating a surprisingly cheap quote) Why should I care about CI/CD pipelines if the agency delivers the features I asked for?
Because features delivered without a CI/CD pipeline are fragile. Without automated testing and deployment gates, every new feature the agency builds has a high probability of breaking an old feature. You will spend the money you "saved" on the upfront quote paying for emergency bug fixes and downtime in production.

### (Scenario: IT Manager reviewing an offshore team) What does "LGTM" mean in a Pull Request, and why is it a red flag?
"LGTM" stands for "Looks Good To Me." When a reviewer uses this on a massive code change without leaving any architectural feedback or edge-case questions, it indicates "review fatigue." It means the reviewer is not actually reading the code, just rubber-stamping it. This allows technical debt and bugs to slip directly into the `main` branch.

### (Scenario: Founder starting a new SaaS project) Do I need a complex observability stack for a Minimum Viable Product (MVP)?
Yes, but a basic one. You don't need a €1,000/month Datadog setup, but you absolutely must have a tool like Sentry (often free for MVPs) installed. Without it, early users will experience silent errors, close your app, and never return. You won't even know they had a problem because you have no error telemetry.

### (Scenario: CTO planning a database migration) Why are manual database scripts dangerous?
If a developer manually executes a SQL script to change the database structure, that change is not tracked in Git. When another developer tries to run the application locally, or when the CI pipeline tries to run tests, the system crashes because their database schema doesn't match the production schema. All database changes must be version-controlled via automated migration files.

### (Scenario: Procurement Officer comparing vendor SLAs) How does a vendor's Git commit history predict their maintenance costs?
If a vendor's Git history shows massive, infrequent commits (e.g., pushing a week's worth of code at once), it means they are writing highly coupled, procedural code that is hard to untangle. When you need to maintain or update that code in Year 2, it will take 3x longer than if they had written small, atomic, modular commits.

### (Scenario: CTO planning to bring development in-house next year) What is the "bus factor" and why should it affect my vendor choice?
The "bus factor" is the number of team members who would need to disappear before your project becomes unmaintainable. If only one developer understands the codebase, your bus factor is 1, and you are entirely dependent on that individual. Ask any vendor how long it would take a new engineer to become productive on your project; a well-documented codebase with ADRs, runbooks, and auto-generated API docs answers in days, while a codebase with tribal knowledge only answers in weeks — and that gap becomes your problem the moment you try to switch vendors or hire in-house.

### (Scenario: CTO reviewing PR data during a technical audit) What size should a pull request actually be, and how do I check if a vendor follows this?
Based on SmartBear's Cisco Systems code review study — the largest published research on the topic, covering 2,500 reviews and 3.2 million lines of code — the evidence-based sweet spot is 200-400 lines of code reviewed over 60-90 minutes, which catches 70-90% of existing defects. Beyond roughly 400-500 lines, or when reviews move faster than about 500 LOC per hour, defect-detection rates drop sharply because reviewers can no longer hold the full context in working memory. To check a vendor, pull the diff-size distribution of their last 20 merged PRs on a real project. A median well above 400-500 lines, combined with approvals landing within minutes, indicates the "code review" is a formality rather than a functioning safety net.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Why should I care about CI/CD pipelines if the agency delivers the features I asked for?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Features delivered without a CI/CD pipeline are fragile. Without automated testing gates, new features will break old features. The money saved on a cheap quote will be spent on emergency bug fixes and production downtime."
      }
    },
    {
      "@type": "Question",
      "name": "What does 'LGTM' mean in a Pull Request, and why is it a red flag?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "'Looks Good To Me'. When used on large code changes without architectural feedback, it indicates review fatigue. The reviewer is rubber-stamping the code without reading it, allowing technical debt to slip into production."
      }
    },
    {
      "@type": "Question",
      "name": "Do I need a complex observability stack for a Minimum Viable Product (MVP)?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "You need a basic one, like Sentry. Without error telemetry, early users will experience silent errors and abandon your app. You won't even know they had a problem because you have no visibility into unhandled exceptions."
      }
    },
    {
      "@type": "Question",
      "name": "Why are manual database scripts dangerous?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Manual SQL scripts aren't tracked in Git. This causes schema drift, where local environments, test pipelines, and production databases fall out of sync, causing catastrophic deployment failures. All database changes must be version-controlled migrations."
      }
    },
    {
      "@type": "Question",
      "name": "How does a vendor's Git commit history predict their maintenance costs?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Massive, infrequent commits indicate highly coupled, procedural code without proper review. Maintaining or updating this code in Year 2 will take 3x longer than if the team had written small, atomic, modular commits."
      }
    },
    {
      "@type": "Question",
      "name": "What is the 'bus factor' and why should it affect my vendor choice?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "The bus factor is how many team members could disappear before a project becomes unmaintainable. A low bus factor (e.g., 1) means you are entirely dependent on one person. Ask vendors how fast a new engineer becomes productive on your codebase; documented, well-onboarded teams answer in days, tribal-knowledge teams answer in weeks."
      }
    },
    {
      "@type": "Question",
      "name": "What size should a pull request actually be, and how do I check if a vendor follows this?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Based on SmartBear's Cisco Systems code review study covering 2,500 reviews and 3.2 million lines of code, the evidence-based sweet spot is 200-400 lines of code reviewed over 60-90 minutes, catching 70-90% of existing defects. Beyond roughly 400-500 lines, defect-detection rates drop sharply. Check a vendor's diff-size distribution on their last 20 merged PRs; a median well above 400-500 lines with fast approvals indicates review is a formality, not a functioning safety net."
      }
    }
  ]
}
</script>
