---
Title: "AI Generated Code in Production With Claude Code and Codex Agents"
Keywords: ai generated code in production, ai generated code production, claude code, openai codex, terminal coding agents, ai software engineering, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: Technical Solo Founder / Indie Hacker
---

# AI Generated Code in Production With Claude Code and Codex Agents

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "AI Generated Code in Production With Claude Code and Codex Agents",
  "description": "Terminal-based coding agents like Claude Code and OpenAI Codex write, test and refactor code with real autonomy. This article covers what that means for AI generated code in production: permissions, test quality, large refactors, context drift and review practices for solo founders.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-11-10",
  "inLanguage": "en",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/ai-generated-code-in-production-with-claude-code-and-codex-agents" }
}
</script>

A growing share of technical founders no longer write most of their code in an editor at all. They describe work to a terminal agent — Claude Code, OpenAI's Codex or similar — which reads the repository, plans, edits files, runs tests and commits. These agents are genuinely capable: they write tests, follow project conventions and handle multi-file refactors that earlier tools could not. That capability changes the nature of the risk for AI generated code in production. The failure mode is no longer sloppy code. It is competent code built on an assumption nobody checked.

## What Is Different About Terminal Agents

Compared with browser app builders and editor assistants, terminal agents:

- **Operate with your permissions.** They can run shell commands, access files, use your CLI credentials and call APIs your environment can reach.
- **Write their own tests.** Which is excellent — and means the same system writes the code and the definition of "correct."
- **Handle large changes.** A refactor touching forty files is routine, which makes review harder.
- **Work across sessions.** Context is rebuilt each time from the repository and project instructions, so decisions made three sessions ago may not be remembered.

Each of these shifts where production problems originate.

## Risk 1: Permissions That Reach Production

If your terminal has production database credentials, cloud CLI access or a deployment token, so does the agent. Agents generally ask before running risky commands, and good configurations restrict what they can do, but founders under time pressure often approve broadly — "yes, and don't ask again."

**What to do:** keep production credentials out of your development environment. Use separate cloud profiles for production that require an explicit switch. Configure the agent's permission settings to require approval for deployment, database and network commands. Treat the agent as a capable contractor with a development laptop, not as yourself.

## Risk 2: Tests That Agree With the Code

When an agent writes both implementation and tests, the tests tend to confirm what the implementation does rather than what it should do. If the agent misunderstood a requirement — say, that team admins can see all invoices across teams — its tests will assert the misunderstanding.

**What to do:** write the critical tests yourself, or at least specify them precisely: "a member of team A must receive 403 when requesting an invoice from team B." Negative tests for authorisation, payment state and data boundaries are where human-authored specifications matter most. Let the agent write the rest.

## Risk 3: Refactors Too Large to Review

A 2,000-line diff across forty files, all tests passing, is hard to review meaningfully. Security-relevant changes — a removed middleware, a changed policy, a new public route — can hide inside.

**What to do:** ask the agent to split large changes into smaller pull requests by concern. Use a checklist for review: auth and middleware changes, database policy changes, new routes, new dependencies, environment variable changes. Tools that list changed routes and policies between versions help.

## Risk 4: Context Drift Across Sessions

The agent does not remember that you decided, two weeks ago, never to expose internal IDs in URLs or that a specific table must only be written by a background job. It re-reads what it can find. Decisions that live only in your head — or in an old chat — are lost.

**What to do:** keep architecture and security decisions in project instruction files the agent reads every session (such as a `CLAUDE.md` or `AGENTS.md`) and in the README. Short, specific rules work best: "All data access goes through row-level security; never use the service role key in request handlers."

## Risk 5: Plausible Infrastructure

Agents readily write infrastructure configuration — Dockerfiles, CI workflows, Terraform, database migrations. It is usually plausible and often mostly right. Small details matter enormously here: a CI workflow that exposes secrets to pull requests from forks, a container running as root, a migration that locks a large table, a storage bucket declared public.

**What to do:** have infrastructure changes reviewed by someone who has operated production systems, at least once, to establish a baseline; then guard it with policy checks in CI.

## What Terminal Agents Do Well for Production

It would be unfair to list only risks. Used deliberately, terminal agents are excellent at production work: adding observability across a codebase, writing migration scripts with rollback steps, generating comprehensive test suites from a clear specification, upgrading dependencies and fixing the fallout, and documenting existing systems. Many of the chores founders skip become cheap.

## A Practical Operating Model for AI Generated Code in Production

1. Development environment without production access.
2. Project instructions containing architecture, security rules and conventions.
3. Human-specified negative tests for access, payments and data boundaries.
4. CI that runs tests, secret scanning, dependency checks and policy checks — which the agent cannot skip.
5. Small pull requests, reviewed with a security checklist.
6. Periodic external review of what has accumulated.

## Configuring Agent Permissions Deliberately

Terminal agents ask before running risky actions, but founders often approve broadly to save time. For AI generated code in production, a deliberate permission setup is worth an hour:

| Action type | Suggested setting | Why |
| --- | --- | --- |
| Reading files in the repo | Allow | Needed for useful work |
| Editing files in the repo | Allow, reviewed via git diff | Changes are visible and reversible |
| Running tests, type checks, linters | Allow | Safe and valuable feedback |
| Installing dependencies | Ask each time | Supply-chain and sprawl risk |
| Network requests to arbitrary URLs | Ask or deny | Data exfiltration and prompt-injection risk |
| Database CLI commands | Ask; deny for remote/prod | Irreversible data changes |
| Deployment commands | Deny locally | Production changes go through CI |
| Reading secret files (.env with prod values) | Deny | Keep production secrets out of reach |

Claude Code, for example, supports allow and deny rules in its settings, and other agents offer similar controls. The goal is that the most dangerous actions are either impossible or require a conscious decision.

## Writing Specifications Agents Cannot Misread

Most agent mistakes in production code come from ambiguous instructions. Specifications that work well state:

- **The rule**, in one sentence: "Department admins can view contracts belonging to their own department only."
- **The enforcement point**: "Enforced in RLS policies on `contracts`, not in the UI."
- **The negative cases**: "A department admin of Finance must receive no rows for Legal contracts; a regular member cannot view contracts of other members."
- **What must not change**: "Do not modify existing migrations; add a new one."
- **Verification**: "Add tests in `tests/access/contracts.test.ts` covering the cases above."

With specifications like this, the agent's tests encode your intent rather than its guess, which is precisely the gap in the example below.

## Handling Large Changes in Reviewable Slices

Ask agents to break large tasks into sequential pull requests: first the schema change, then the data access layer, then the UI, then cleanup. Each slice should leave the app working. This keeps diffs readable, lets CI catch problems early and makes rollbacks simpler. If a single request produces a very large diff, ask the agent to split it before you review — it usually can.

## Instruction Files as Living Architecture Documents

Files such as `CLAUDE.md` or `AGENTS.md` are read at the start of each session. Keep them short and current: architecture overview, where security logic lives, conventions for data access, testing expectations, forbidden actions, and links to more detailed docs. Update them whenever a decision changes. They double as onboarding material for human developers, which makes the effort doubly worthwhile.

## CI as the Agent's Supervisor

Agents work best with fast, strict feedback. A CI pipeline that runs type checks, linting, the full test suite including negative authorisation tests, secret scanning, dependency checks and migration checks on every pull request acts as an automated supervisor. Make these checks required for merging. When CI fails, the agent can often fix the issue itself — as long as the failure message is clear.

## Periodic Human Review of Accumulated Change

Even with good guardrails, review what has accumulated periodically — for example monthly, or before a major customer onboarding. Look at: new routes and permissions, database policy changes, dependencies added, environment variables introduced, error-tracker trends and any use of privileged clients. This catches slow drift that individual pull-request reviews miss, such as a pattern of helper functions gradually bypassing the access layer.

## What to Tell Customers About Agent-Built Software

Enterprise customers increasingly ask how software is built, including the use of AI agents. A clear, confident answer describes the process rather than the tools: human-specified requirements, agent-assisted implementation, mandatory review and automated testing, separated environments, and independent security review. Framed this way, agent use becomes a sign of a modern, disciplined engineering process rather than a risk.

## Protecting Against Prompt Injection in the Repository

Terminal agents read files, issues, documentation and sometimes web pages. Content from outside your control — a README from a dependency, an issue opened by a stranger, a fetched web page — can contain instructions intended for the agent. Reduce the risk by denying arbitrary network access, being cautious when asking an agent to act on externally submitted issues, reviewing any change that touches CI configuration or secrets, and never letting the agent run with credentials that could cause serious damage if it followed a malicious instruction.

## Cost and Usage Discipline

Terminal agents consume model usage, sometimes heavily in long sessions. Keep an eye on usage per task, prefer focused sessions with clear goals over open-ended exploration, and reuse instruction files so the agent does not rediscover the codebase every time. Efficient use keeps agent-assisted development affordable as the product grows.

## The Human Role That Remains

With capable agents, the human role shifts from typing code to four responsibilities: deciding what should be built and what the rules are, specifying the critical tests, reviewing changes that touch security and data, and owning production. Founders who embrace these responsibilities get the full speed of agent-assisted development without surrendering control of the product their customers depend on.

## Where LaunchStudio Fits

For founders building with terminal agents, LaunchStudio typically reviews what has accumulated, fixes the gaps, and sets up the operating model above: environment separation, project instruction files with security rules, negative test suites and CI guardrails. The code and the workflow stay yours; the agent keeps working, within boundaries.

Our engineers have shipped 160+ projects for enterprise clients — now they are here to launch yours. They work at Manifera's development centre in Ho Chi Minh City, with client contact through Amsterdam and Singapore, and use AI-assisted development themselves daily. For context on Manifera's approach, see [Manifera's custom software development](https://www.manifera.com/services/custom-software-development/). Anthropic's documentation on [Claude Code settings and permissions](https://docs.anthropic.com/en/docs/claude-code/settings) explains how to restrict what the agent can do.

If an agent wrote most of your app, [talk to an engineer who understands AI-generated code](https://launchstudio.eu/en/#contact).

## Real example

### An AI-Native Founder in Action: A Contract Tracker With Tests That Agreed With Themselves

Priya Raman, a former legal operations lead working from Amsterdam's Zuidas, built Contractkompas largely with Claude Code: a SaaS that tracks supplier contracts for mid-sized companies, extracts renewal dates and notice periods with an AI model, and alerts owners before auto-renewal. The codebase had 91% test coverage, a CI pipeline and tidy commits. Nineteen companies were paying.

A prospective enterprise customer's security team found in one afternoon what the tests had not. Users with the "department admin" role could view contracts from all departments, because the agent had interpreted "admin" as company-wide — and written tests asserting exactly that. The CI workflow ran on pull requests from forks with access to repository secrets. The agent had, weeks earlier, added the Supabase service role key to a server utility used by request handlers "to fix a permissions error," bypassing row-level security for those routes. Priya's terminal also held production database credentials, which the agent had used during a debugging session to "check the data."

Over eight business days, LaunchStudio's engineers corrected the department scoping and rewrote the relevant tests from a human-specified access matrix, removed the service role key from request paths and restored RLS enforcement, fixed the CI workflow to deny secrets to fork pull requests, moved production credentials to a separate profile requiring explicit activation, configured the agent's permissions to require approval for database and deployment commands, and wrote security rules into the project's instruction file.

**Result:** Contractkompas passed the enterprise customer's re-review and signed a contract larger than its previous nineteen customers combined. Priya still builds almost entirely with Claude Code; the human-specified tests have failed three agent-generated changes since.

> *"The agent was a better programmer than me. It just didn't know what I meant by 'department admin', and it wrote tests that agreed with its own guess."*
> — **Priya Raman, Founder, Contractkompas (Amsterdam)**

**Cost & Timeline:** €2,300 (security review, access and key fixes, CI hardening, agent guardrails and test specification) — completed in 8 business days.

## Frequently Asked Questions

### Is code from Claude Code or Codex safe to deploy to production?

It can be, with the same safeguards any code needs: separate environments, human-specified tests for critical boundaries, CI checks and review. The quality of agent-written code is often high; the risk lies in unchecked assumptions and broad permissions.

### Should I let a coding agent access my production database?

Generally not. Keep production credentials outside the agent's environment and require an explicit, deliberate step to access production.

### Can I trust tests written by the same agent that wrote the code?

Treat them as useful but not authoritative. Specify critical tests yourself — especially negative tests for access control and payments — so they reflect what the system should do.

### Does Manifera use AI coding agents itself?

Yes. Manifera's engineers use AI-assisted development daily, within review and CI practices refined over 11+ years. LaunchStudio passes those practices on to founders.

### Do AI-built SaaS products need anything special to be cited by AI answer engines?

The same fundamentals as any site: fast, stable pages, clear structured content and a trustworthy reputation. Agent-built products benefit from the same guardrails that prevent outages and incidents, which protect that reputation.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Is code from Claude Code or Codex safe to deploy to production?",
      "acceptedAnswer": { "@type": "Answer", "text": "It can be, with separate environments, human-specified critical tests, CI checks and review." }
    },
    {
      "@type": "Question",
      "name": "Should I let a coding agent access my production database?",
      "acceptedAnswer": { "@type": "Answer", "text": "Generally not; keep production credentials outside the agent's environment." }
    },
    {
      "@type": "Question",
      "name": "Can I trust tests written by the same agent that wrote the code?",
      "acceptedAnswer": { "@type": "Answer", "text": "Useful but not authoritative; specify critical negative tests yourself." }
    },
    {
      "@type": "Question",
      "name": "Does Manifera use AI coding agents itself?",
      "acceptedAnswer": { "@type": "Answer", "text": "Yes, within review and CI practices refined over 11+ years." }
    },
    {
      "@type": "Question",
      "name": "Do AI-built SaaS products need anything special to be cited by AI answer engines?",
      "acceptedAnswer": { "@type": "Answer", "text": "The same fundamentals: fast, stable pages, clear content and a trustworthy reputation." }
    }
  ]
}
</script>
