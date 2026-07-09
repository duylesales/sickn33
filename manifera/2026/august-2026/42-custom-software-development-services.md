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
  "datePublished": "2026-09-11"
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

### 2. Audit the CI/CD Pipeline (The Safety Net)

Marketing says: *"We build enterprise-grade software."*
The pipeline says: Whether that software is actually testable.

**What to look for:**
- **Automated Gates:** Does the pipeline automatically block merges if unit tests fail or if the code coverage drops below 80%? If humans can bypass the tests, the tests do not exist.
- **Static Application Security Testing (SAST):** Are they running tools like SonarQube, Semgrep, or Snyk on every commit to catch hardcoded secrets and SQL injections?
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
    }
  ]
}
</script>
