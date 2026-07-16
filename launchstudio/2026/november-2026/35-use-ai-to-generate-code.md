---
Title: "Use AI to Generate Code, Use Humans to Govern It: The Rise of the Internal Developer Portal"
Keywords: use ai to generate code, ai can code, ai code governance, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: VP of Engineering / CTO
---

# Use AI to Generate Code, Use Humans to Govern It: The Rise of the Internal Developer Portal

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Use AI to Generate Code, Use Humans to Govern It: The Rise of the Internal Developer Portal",
  "description": "When everyone in your company can use AI to generate code, technical debt scales exponentially. A deep dive into how engineering teams use Internal Developer Portals (IDPs) to govern AI-generated shadow IT.",
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
  "datePublished": "2026-12-05",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://launchstudio.eu/en/blog/use-ai-to-generate-code"
  }
}
</script>

The fact that AI can code is no longer a debate; it is a baseline reality. In 2026, junior developers, product managers, and even marketing executives use AI to generate code daily. They build internal dashboards, data parsing scripts, and marketing automation workflows at blistering speed. 

For a VP of Engineering, this democratization of code generation is a double-edged sword. Productivity is at an all-time high, but governance has collapsed. 

When you use AI to generate code outside of a structured engineering pipeline, you create "Shadow IT." An operations manager might use Lovable to build a tracking app that connects directly to the production database using a hardcoded, unrotated credential. A junior developer might use Cursor to generate a 2,000-line React component that violates every accessibility and security standard the company holds. 

You cannot stop your team from using AI to code. If you try, they will simply do it on their personal laptops. The only solution is to embrace the speed of AI generation while enforcing strict, automated human governance. This is achieved through the implementation of an Internal Developer Portal (IDP).

## The AI Governance Crisis

Before exploring the solution, we must understand the specific engineering crises caused by unmanaged AI code generation in mid-to-large organizations.

### 1. The Secrets Sprawl
AI models do not understand the concept of a `.env` file unless explicitly prompted. When non-engineers use AI to generate scripts, the AI often hardcodes API keys (Stripe, AWS, OpenAI) directly into the Python or JavaScript files. These files are then uploaded to shared Slack channels, internal wikis, or public GitHub repositories, resulting in immediate, catastrophic security breaches.

### 2. The Dependency Nightmare
AI models frequently hallucinate npm or pip packages, or import severely outdated, vulnerable versions of libraries. If a marketing team deploys an AI-generated Node.js script using a package with a known Remote Code Execution (RCE) vulnerability, the entire corporate network is compromised.

### 3. The Architecture Bypass
Enterprise architecture relies on strict boundaries: frontends talk to API gateways, which talk to microservices, which talk to databases. AI code generators naturally prefer the path of least resistance. They will happily write a React frontend that executes a raw SQL query directly against the production PostgreSQL instance, completely bypassing the API gateway, rate limiters, and audit logs.

## The Solution: Internal Developer Portals (IDPs)

To govern AI code generation, engineering leaders are deploying Internal Developer Portals (like Backstage by Spotify, or Port). An IDP acts as a structural funnel. It says: "You can use AI to generate whatever code you want, but to get it onto a server, it must pass through this portal."

### 1. Automated CI/CD Guardrails
When an employee submits AI-generated code to the IDP, the portal triggers a rigorous CI/CD pipeline. Static Application Security Testing (SAST) tools scan the code for hardcoded secrets. Software Composition Analysis (SCA) tools scan the `package.json` for vulnerable dependencies. If the AI code fails, it is automatically rejected, and the pipeline provides a prompt the employee can feed back to the AI to fix the issue.

### 2. Scaffolded Environments
Instead of letting an employee ask an AI to "build a Node.js app from scratch," the IDP provides "Golden Paths." The employee clicks a button in the IDP to provision a secure, pre-configured repository. This repository already contains the correct Dockerfiles, authentication middleware, and database ORMs. The employee then uses AI to generate the *business logic* inside this secure scaffold, rather than generating the infrastructure itself.

### 3. The API Gateway Enforcement
The IDP provisions environments that physically cannot reach the production database directly. The AI-generated code is forced to route all data requests through the company's secure API Gateway. This enforces Row Level Security (RLS) and audit logging natively, regardless of how sloppy the AI-generated frontend code might be.

## How LaunchStudio Engineers AI Governance

Building an IDP and configuring aggressive CI/CD pipelines requires specialized DevOps and Platform Engineering expertise. 

[LaunchStudio](https://launchstudio.eu/en/), leveraging the deep enterprise capabilities of [Manifera](https://www.manifera.com/), implements these governance structures for scaling software companies.

Directed by Herre Roelevink in Amsterdam, with platform engineering executed in Ho Chi Minh City, the LaunchStudio team establishes the guardrails that allow your team to code with AI safely.

We build the Platform Engineering layer:
1. **Repository Scaffolding:** We create the "Golden Path" templates (Next.js, Node.js, Python) equipped with enterprise security defaults.
2. **Pipeline Automation:** We configure the GitHub Actions or GitLab CI pipelines that automatically reject AI hallucinations, hardcoded secrets, and vulnerable dependencies.
3. **Infrastructure as Code (IaC):** We ensure that all deployments triggered by the IDP are managed via Terraform, keeping your cloud environment secure and predictable.

## Real example

### An AI-Native Founder in Action: The Engineering Director Fighting Shadow IT

Mark is a VP of Engineering at a logistics software company in Rotterdam. His team of 40 developers was highly productive, but he noticed a terrifying trend. The operations and customer success teams had discovered AI coding tools. 

They were using Cursor to write their own internal dashboards to track shipments and manage client onboarding. At first, Mark was impressed by their initiative. Then, the company's AWS bill spiked by €4,000. 

Mark investigated and found a "Shadow IT" disaster. A customer success manager had used AI to write a Python script that queried the production database every 5 seconds to check for updates. The script contained a hardcoded master database password. It was running on an unpatched AWS EC2 instance that the manager had provisioned using a corporate credit card. 

Mark couldn't ban AI—the business velocity it provided was too valuable. But he needed control. He hired LaunchStudio to build an AI governance framework.

In 20 business days, the Manifera team deployed an Internal Developer Portal based on Backstage. They locked down AWS IAM permissions, ensuring nobody could manually provision servers. If the operations team wanted a new AI-generated dashboard, they had to click "Create Dashboard" in the IDP. 

The IDP automatically spun up a secure Vercel environment and a GitHub repository with pre-configured API endpoints that could only read (not write) from a read-replica database. When the operations team pasted their AI-generated code into the repository, LaunchStudio's automated CI/CD pipeline immediately blocked it, flagging the hardcoded database password and forcing them to use a secure environment variable instead.

**Result:** The shadow IT crisis was neutralized. The operations team continued building internal tools with AI, but they did so within a mathematically secure sandbox. Mark regained total visibility over his cloud architecture, and the AWS bill dropped back to normal levels. The company avoided a massive potential data breach.

> *"AI coding tools turned my non-technical staff into developers overnight, which was amazing for business but terrifying for security. LaunchStudio built the platform engineering guardrails we needed. Now, my team can use AI to build whatever they want, and I can sleep at night knowing the infrastructure won't collapse."*
> — **Mark van Dijk, VP of Engineering, LogiTech Solutions (Rotterdam)**

**Cost & Timeline:** €9,500 (Launch & Grow Package with Platform Engineering & IDP Add-on) — production-ready and deployed in 20 business days.

---

## Frequently Asked Questions

### (Scenario: CTO managing junior developers) How do I stop junior developers from committing vulnerable AI-generated code?

You cannot rely on manual code reviews; the volume of AI code is too high. You must implement automated CI/CD guardrails. LaunchStudio configures pipelines with tools like SonarQube (for code quality), Snyk (for dependency vulnerabilities), and TruffleHog (for hardcoded secrets). If the AI code fails any of these automated checks, the pull request is physically blocked from being merged.

### (Scenario: VP Engineering evaluating AI tools) Should I force my team to use a specific AI coding tool (like GitHub Copilot) for security reasons?

While Enterprise tools (like Copilot Enterprise) offer IP indemnification and zero-data-retention policies, developers will inevitably copy-paste code from ChatGPT or Claude. The most secure approach is tool-agnostic: assume all code is untrusted, regardless of which AI generated it. Enforce security at the repository level (via an IDP and CI/CD pipelines) rather than trying to police which chat window the developer uses.

### (Scenario: Operations Manager building internal tools) I am not an engineer, but I want to build a tool for my team. How do I do it safely?

Request an IDP (Internal Developer Portal) scaffold from your engineering team or LaunchStudio. This scaffold will give you a pre-configured environment where you can safely paste your AI-generated code. It ensures you don't accidentally expose the company database to the internet or leak API keys, allowing you to focus purely on the business logic of your tool.

### (Scenario: Technical founder scaling a team) At what size does a startup need an Internal Developer Portal (IDP)?

In the pre-AI era, IDPs were for 100+ engineer enterprise teams. Today, because AI allows a team of 5 people to generate the code volume of 50 people, the governance breaking point happens much earlier. We recommend implementing basic IDP scaffolding and strict CI/CD guardrails as soon as you hire your first non-founding engineer or allow non-technical staff to contribute code.

### (Scenario: Security Engineer auditing AI code) Does AI-generated code have unique security vulnerabilities compared to human code?

Yes. AI models frequently suffer from "hallucinated dependencies" (inventing a library name that doesn't exist). Malicious actors actively monitor for these hallucinations and register the fake package names on npm or PyPI with malware. When your developer's AI code installs the hallucinated package, your system is compromised. LaunchStudio's automated SCA pipelines specifically scan for and block these supply-chain attacks.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "How do I stop junior developers from committing vulnerable AI-generated code?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Manual code reviews cannot scale with AI volume. You must implement automated CI/CD guardrails. LaunchStudio configures pipelines with SAST, SCA, and secret scanning tools. If the AI code fails these checks, the pull request is automatically blocked."
      }
    },
    {
      "@type": "Question",
      "name": "Should I force my team to use a specific AI coding tool for security reasons?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "While enterprise tools offer better IP protection, the most secure approach is tool-agnostic: assume all code is untrusted. Enforce security at the repository level via an IDP and CI/CD pipelines, rather than policing which AI tool the developer uses."
      }
    },
    {
      "@type": "Question",
      "name": "I am not an engineer, but I want to build a tool for my team. How do I do it safely?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Request an IDP scaffold from your engineering team or LaunchStudio. This provides a pre-configured, sandboxed environment where you can safely paste AI code without accidentally exposing databases or leaking API keys."
      }
    },
    {
      "@type": "Question",
      "name": "At what size does a startup need an Internal Developer Portal (IDP)?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Because AI allows a 5-person team to generate the code volume of 50 people, governance breaks early. We recommend implementing basic IDP scaffolding and strict CI/CD guardrails as soon as you allow non-technical staff to contribute code."
      }
    },
    {
      "@type": "Question",
      "name": "Does AI-generated code have unique security vulnerabilities compared to human code?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. AI models frequently hallucinate dependencies. Attackers register these fake package names with malware. When the AI code installs the package, the system is compromised. LaunchStudio's automated SCA pipelines scan for and block these supply-chain attacks."
      }
    }
  ]
}
</script>
