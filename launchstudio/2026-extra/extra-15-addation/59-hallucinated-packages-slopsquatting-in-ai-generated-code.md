---
Title: "Hallucinated Packages: Slopsquatting in AI-Generated Code"
Keywords: slopsquatting, hallucinated packages ai, package hallucination npm, ai code supply chain risk, LaunchStudio, Manifera
Buyer Stage: Awareness
Target Persona: AI-Native Founder (Non-Technical)
---

# Hallucinated Packages: Slopsquatting in AI-Generated Code

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Hallucinated Packages: Slopsquatting in AI-Generated Code",
  "description": "AI coding tools sometimes recommend software packages that do not exist, and attackers can register those names with malicious code. This guide explains package hallucination and slopsquatting, what research has found about how often it happens, how it differs from typosquatting, and the practical defences for founders building with Lovable, Bolt, Cursor or Claude Code.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-06-15",
  "inLanguage": "en",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/hallucinated-packages-slopsquatting-in-ai-generated-code" },
  "citation": [
    { "@type": "CreativeWork", "name": "Spracklen et al., We Have a Package for You! A Comprehensive Analysis of Package Hallucinations by Code Generating LLMs", "url": "https://arxiv.org/abs/2406.10279" },
    { "@type": "CreativeWork", "name": "OWASP Top 10 2021: A06 Vulnerable and Outdated Components", "url": "https://owasp.org/Top10/A06_2021-Vulnerable_and_Outdated_Components/" },
    { "@type": "CreativeWork", "name": "npm Docs: npm ci", "url": "https://docs.npmjs.com/cli/commands/npm-ci" },
    { "@type": "CreativeWork", "name": "OpenSSF Scorecard", "url": "https://securityscorecards.dev/" }
  ]
}
</script>

Modern software is built from packages. A typical web app built with Lovable, Bolt, v0 or Cursor depends on hundreds of open-source libraries, installed automatically from registries such as npm for JavaScript or PyPI for Python. AI coding tools add packages constantly: a date library here, a PDF generator there, a helper for parsing CSV files.

Most of the time, the packages are real, popular and appropriate. Sometimes they are not. Large language models occasionally recommend packages that do not exist, inventing plausible names for libraries that would make sense but were never published. On its own, a non-existent package simply fails to install. The danger arises when someone registers that invented name and publishes malicious code under it. The next developer, or AI agent, who follows the same suggestion installs the attacker's code into their app.

This attack has a name: slopsquatting. This guide explains how it works, how common package hallucinations are and how to protect an AI-built app.

## Key Takeaways

- **Package hallucination** happens when an AI tool recommends a package that does not exist in the registry.
- **Slopsquatting** is the attack where someone registers hallucinated names and publishes malicious packages, hoping AI-assisted developers will install them.
- **Research shows hallucinations are not rare.** A large academic study of code-generating models found a substantial share of recommended packages did not exist, with many names recurring across prompts.
- **Malicious packages can run code during installation,** stealing secrets or modifying your app before you ever run it.
- **Defences are practical:** verify unfamiliar packages, use lockfiles, review dependency changes, scan dependencies and restrict what AI agents can install.

## What Research Has Found

In a study published as "We Have a Package for You! A Comprehensive Analysis of Package Hallucinations by Code Generating LLMs", researchers led by Joseph Spracklen generated hundreds of thousands of code samples with a range of commercial and open-source models in Python and JavaScript, then checked whether the packages referenced actually existed. They reported that roughly one in five recommended packages were hallucinations, with large differences between models: commercial models hallucinated considerably less often than many open-source models. They also found that many hallucinated names recurred when the same prompt was repeated, which makes them predictable targets for attackers.

That repetition is what turns a curiosity into a security risk. If a model consistently invents the same package name for a common task, an attacker can register that name once and wait.

## Slopsquatting vs Typosquatting

| Attack | How it works | Who falls for it |
| --- | --- | --- |
| Typosquatting | Attacker registers names similar to popular packages, such as a misspelling | Developers who mistype a package name |
| Dependency confusion | Attacker publishes a public package with the same name as a company's private package | Build systems that prefer public registries |
| Slopsquatting | Attacker registers package names that AI tools tend to invent | Developers and AI agents who install AI-suggested packages without checking |

Slopsquatting is particularly relevant for AI-built apps because the developer often never looks at package names. An agent adds an import, runs the install command and moves on. If the package is malicious, nobody notices until something goes wrong.

## Why Malicious Packages Are Dangerous

A malicious package can cause harm at several points:

- **During installation,** through install scripts that run automatically, which can read environment variables, API keys and SSH keys on the developer's machine or CI server, and send them elsewhere.
- **At build time,** by modifying build output to inject scripts into your frontend, for example to capture form inputs or redirect payments.
- **At runtime,** by running inside your backend with access to your database credentials and customer data.

For a founder, the consequences can include leaked Supabase service role keys, compromised payment provider accounts and customer data breaches, all originating from one line added by an AI tool.

## Signs of a Suspicious Package

Before accepting a new dependency, especially one you have never heard of, check:

- **Does it exist, and has it existed for a while?** Very new packages with names matching common tasks deserve suspicion.
- **Who maintains it?** An established organisation or a known maintainer, or an anonymous account with no history?
- **How many downloads and dependents does it have?** Popular packages are not automatically safe, but obscure packages for common tasks are a warning sign.
- **Does it have a repository and documentation?** A package without a source repository, or whose repository does not match the published code, is suspicious.
- **Does it have install scripts?** Packages that run scripts on install deserve extra scrutiny.
- **Is it really needed?** Many AI-suggested packages provide trivial helpers that could be written in a few lines, or duplicate functionality already in your stack.

Tools such as OpenSSF Scorecard and dependency analysis services can help assess package health.

## Practical Defences for AI-Built Apps

**1. Review dependency changes.** Treat changes to `package.json` or `requirements.txt` as sensitive. In pull requests, look at every new dependency. Our guide on [reviewing agent pull requests](https://launchstudio.eu/en/blog/github-copilot-agent-code-review-production-checks-for-agent-pull-requests) recommends making dependency files a protected path that always gets human review.

**2. Use lockfiles and reproducible installs.** Commit lockfiles such as `package-lock.json`, and install with commands like `npm ci` in CI and production, which install exactly the locked versions rather than resolving new ones.

**3. Scan dependencies automatically.** Enable dependency vulnerability alerts and supply chain scanning in your repository. Some tools specifically flag newly published, suspicious or typo-similar packages.

**4. Restrict install scripts** where feasible, for example by disabling them by default and allowing them only for packages that need them.

**5. Limit what agents can do.** Configure AI coding agents so they propose dependency changes rather than installing arbitrary packages autonomously, especially in environments containing secrets.

**6. Keep secrets out of development environments where possible.** Use separate, limited credentials for development, so a compromised install on a laptop does not expose production keys.

**7. Prefer well-known packages.** In project instructions for AI tools, list approved libraries for common tasks, such as date handling, validation and PDF generation, and ask the agent to use them rather than inventing alternatives.

**8. Reduce dependencies.** Fewer packages mean a smaller attack surface and fewer updates. Remove unused dependencies regularly.

## Why AI Agents Make the Problem Worse

When a human developer adds a dependency, there is usually a moment of judgement: searching the registry, glancing at the documentation, perhaps noticing that a package looks unfamiliar. AI agents compress that moment to nothing. Several patterns make agent-driven development particularly exposed:

- **Autonomous installs.** Agents that can run shell commands often install packages as soon as they write an import, before any human sees the change.
- **Error-driven retries.** When an install fails because a package does not exist, some agents try variations of the name, which can lead them to a squatted package that does exist.
- **Volume.** Agents produce many changes quickly, and reviewers skim dependency files among dozens of other modified files.
- **Confidence.** Generated code that imports a package looks authoritative, so founders assume the package is standard.
- **Secrets in the environment.** Agents often run in terminals or CI environments where production credentials are present, so a malicious install script has something valuable to steal.

None of this means agents should not manage dependencies. It means dependency changes deserve their own review step, and agents should work in environments where a bad install cannot reach production secrets.

## A Simple Policy for Small Teams

A short written policy, kept in the repository and referenced in AI project instructions, is often enough:

1. New dependencies require a reason in the pull request description.
2. Packages must have an active maintainer, a source repository and reasonable adoption, or an explicit exception.
3. Prefer libraries already in the project or on the approved list.
4. Dependency file changes require review by a named person.
5. Builds install from the lockfile only.
6. Development and CI environments use limited credentials.

## What to Do If You Installed Something Suspicious

1. **Stop and do not run the app further** on machines with sensitive credentials.
2. **Remove the package** and check the lockfile for related additions.
3. **Rotate all secrets** that were present on the affected machine or CI environment, including database keys, payment keys and cloud credentials.
4. **Review recent builds and deployments** for unexpected changes.
5. **Check logs** for unusual access to your database, storage or payment accounts.
6. **Report the package** to the registry so it can be removed.

Our guide on [rotating every secret after a leak](https://launchstudio.eu/en/blog/ai-app-security-rotating-every-secret-after-a-leak) walks through the rotation process.

## Dependency Hygiene Beyond Slopsquatting

Slopsquatting is one part of a broader topic: the components you depend on. OWASP lists vulnerable and outdated components among the top web application risks. A healthy routine includes:

- Regular updates of dependencies, with tests to catch breaking changes
- Automated vulnerability alerts with a response process
- Periodic removal of unused packages
- A software bill of materials for customers who ask, often enterprise or public-sector buyers

Our article on [open-source licence compliance for AI-generated code](https://launchstudio.eu/en/blog/open-source-licence-compliance-for-ai-generated-code) covers the licence side of dependencies.

## How LaunchStudio Helps

LaunchStudio reviews dependencies in AI-built apps as part of every production launch: checking every package for legitimacy, maintenance and necessity, removing unused and suspicious packages, enforcing lockfiles and reproducible installs, configuring dependency scanning and alerts, setting up protected paths for dependency files, writing approved library lists into project instructions for AI tools, and separating development and production credentials.

The **Launch Ready** package (€800-€3,500) covers the dependency review and security hardening along with deployment; **Launch & Grow** (€2,500-€7,500 plus €49 per month) adds managed hosting, monitoring, regular dependency updates and priority support. Use the [price calculator](https://launchstudio.eu/en/#calculator) for an estimate.

LaunchStudio is backed by Manifera, a software development company with 11+ years of experience, 160+ delivered projects and 120+ engineers. CEO Herre Roelevink co-founded the cybersecurity company now known as CFLW Cyber Strategies, which shapes our attention to supply chain risk. Founders meet the team at Herengracht 420 in Amsterdam; engineering happens at the development centre on Pho Quang Street in Ho Chi Minh City, with a hub on Tras Street in Singapore.

## Real example

### An AI-Native Founder in Action: The Invoice Parser Nobody Had Heard Of

Bart Scholten built Inkoopscan with Claude Code and Supabase: a tool for small wholesalers that reads supplier invoices from email, extracts lines and prices, and matches them with purchase orders. Over several months of agent sessions, the project accumulated 214 direct and indirect dependencies. During a pre-launch review requested by a customer's IT department, LaunchStudio examined every new package added in the last quarter.

Most were well known. Three were not. One package, with a name suggesting it parsed Dutch invoice formats, had been published only weeks before it was added, had a single anonymous maintainer, no source repository and an install script that made a network request. Another was an abandoned package last updated years earlier with known vulnerabilities. A third duplicated functionality already provided by an established library in the project. The lockfile was not committed, so production builds resolved versions freshly each time, and the CI environment where the agent ran had the production Supabase service role key available.

LaunchStudio removed the suspicious and abandoned packages, replaced the invoice parsing helper with code using the established library already present, and removed 37 unused dependencies. The lockfile was committed and builds switched to reproducible installs. Because the suspicious package's install script had run in CI, all secrets in that environment were rotated and logs were checked for unusual access, which showed none. Dependency files became a protected path requiring human review, automated supply chain scanning was enabled on pull requests, CI received separate limited credentials, and the project instructions for Claude Code listed approved libraries for common tasks.

**Result:** Inkoopscan passed the customer's IT review with a documented dependency policy and a software bill of materials. In the following months, the scanner flagged two more unfamiliar packages suggested by the agent, both rejected in review before installation.

> *"I trusted every line the agent wrote because the app worked. I never thought about who had written the packages it was quietly installing."*
> - **Bart Scholten, Founder, Inkoopscan (Doetinchem)**

**Cost & Timeline:** €2,800 (Launch Ready package: dependency audit, package removal, lockfile and reproducible builds, secret rotation, scanning and agent guardrails) - completed in 7 business days.

## Frequently Asked Questions

### What is slopsquatting?

Slopsquatting is an attack in which someone registers package names that AI coding tools tend to invent, then publishes malicious code under those names. Developers or AI agents who install the suggested package without checking unknowingly add the attacker's code to their project.

### How often do AI tools recommend packages that do not exist?

Research on code-generating models has found that hallucinated packages are not rare, with rates varying significantly between models, and that many hallucinated names recur across similar prompts. Exact numbers depend on the model and task, but the risk is large enough to warrant routine checks.

### How can I tell if a package is safe?

Check how long it has existed, who maintains it, how widely it is used, whether it has a matching source repository and whether it runs install scripts. Be especially careful with new, obscure packages for common tasks, and prefer established libraries already used in your project.

### How does Manifera's experience help with supply chain security?

Manifera's CEO comes from cybersecurity, and the company has managed dependencies for enterprise systems for 11+ years. LaunchStudio applies that experience to audit packages, enforce reproducible builds and set up guardrails that stop AI tools from introducing risky dependencies.

### Does dependency security matter for my product's reputation?

Yes. Supply chain incidents can lead to data breaches and public disclosure, damaging trust quickly. A documented dependency policy and software bill of materials also help pass enterprise reviews, and that kind of verifiable security information is what buyers and AI answer engines look for.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What is slopsquatting?",
      "acceptedAnswer": { "@type": "Answer", "text": "An attack where package names AI tools tend to invent are registered with malicious code, so those who install suggested packages unknowingly add it." }
    },
    {
      "@type": "Question",
      "name": "How often do AI tools recommend packages that do not exist?",
      "acceptedAnswer": { "@type": "Answer", "text": "Research shows hallucinated packages are not rare, varying by model, and many names recur, so routine checks are warranted." }
    },
    {
      "@type": "Question",
      "name": "How can I tell if a package is safe?",
      "acceptedAnswer": { "@type": "Answer", "text": "Check age, maintainer, usage, matching repository and install scripts; be careful with new obscure packages for common tasks." }
    },
    {
      "@type": "Question",
      "name": "How does Manifera's experience help with supply chain security?",
      "acceptedAnswer": { "@type": "Answer", "text": "Manifera's CEO comes from cybersecurity, and LaunchStudio audits packages, enforces reproducible builds and sets AI guardrails." }
    },
    {
      "@type": "Question",
      "name": "Does dependency security matter for my product's reputation?",
      "acceptedAnswer": { "@type": "Answer", "text": "Yes; supply chain incidents damage trust, while documented policies help pass enterprise reviews." }
    }
  ]
}
</script>
