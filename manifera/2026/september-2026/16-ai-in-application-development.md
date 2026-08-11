---
Title: "AI in Application Development: The Threat of 'Dead Code'"
Keywords: ai in application development, custom software development, GitHub Copilot, technical debt, software architecture, dead code, Manifera
Buyer Stage: Consideration / Code Quality
Target Persona: A (CTO / Lead Architect)
Content Format: Technical Analysis & Risk Mitigation
---

# AI in Application Development: The Threat of 'Dead Code'

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "AI in Application Development: The Threat of 'Dead Code'",
  "description": "An architectural analysis of AI in application development. Explains how AI code generators flood codebases with verbose 'Dead Code' and why strict architectural governance is required to prevent immediate technical debt.",
  "author": {"@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com"},
  "publisher": {"@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com"},
  "datePublished": "2026-09-16"
}
</script>

A startup gives their engineering team full access to GitHub Copilot and other generative AI tools. The team is thrilled. Their "velocity" skyrockets. They are merging 40% more Pull Requests per week. 

However, the Lead Architect notices a deeply concerning trend. The repository size has doubled in just three months. Functions that used to take 10 lines of concise, elegant logic are now 50 lines of verbose, highly repetitive code. 

Worse, when the Architect runs a code coverage tool, they discover that 30% of the newly generated code is "Dead Code" (code that is written and compiled, but never actually executed by the application). 

The use of **AI in application development** did not make the team 40% more productive. It made them 40% more prolific at generating unmaintainable technical debt. 

## The Verbosity Problem of Generative AI

To understand why this happens, you must understand how Large Language Models (LLMs) operate. LLMs are statistical prediction engines, not systems architects. 

When a developer asks an LLM to write a function, the AI favors verbosity. It generates highly repetitive, explicitly written blocks of code because that is the safest statistical path. 

### 1. The Loss of Abstraction
Elite software engineers use abstraction (like creating a reusable helper function) to keep code DRY (Don't Repeat Yourself). 
An AI code generator rarely refactors existing code to create an abstraction. If you ask it to build three similar UI components, the AI will simply write the same 100 lines of code three separate times. If a bug is found in that component later, a human engineer now has to manually find and fix that bug in three different places.

### 2. The Proliferation of Dead Code
Because AI models try to be "helpful," they often generate defensive boilerplate code (e.g., error handling for extreme edge cases that physically cannot occur in your specific application). 
Junior developers, trusting the AI, leave this code in. This "Dead Code" bloats the application size, slows down the CI/CD pipeline, and drastically increases the cognitive load for any human engineer trying to read the file six months later.

AI does not write elegant code; it writes statistically average code, the most probable next token given everything it has seen before, not the most abstracted or maintainable solution to your specific problem. Without a senior architect ruthlessly deleting the AI's verbosity, a codebase built this way turns into a bloated legacy system in a matter of months, not years.

This is no longer just an architect's hunch. GitClear's 2025 AI Copilot Code Quality research, which analyzed 211 million lines of code changes, found that the share of "copy/pasted" (cloned) code in commits rose from 8.3% in 2021 to 12.3% in 2024, and that 2024 was the first year on record where copy-pasted code in commits exceeded genuinely refactored ("moved") code. GitClear's researchers also cite prior research linking cloned code blocks to 15-50% more defects than equivalent code that was properly abstracted. The abstraction problem described above is not a theoretical risk; it is showing up as a measurable, industry-wide trend in the same repositories generative AI tools are being used to write.

## Mitigating AI-Driven Technical Debt

The use of **AI in application development** is inevitable. You cannot ban the tools. But you must radically increase your architectural governance to survive them.

If you are outsourcing [custom software development](https://www.manifera.com/services/custom-software-development/), you must demand strict guardrails from your agency.

### 1. Shift from "Writing" to "Refactoring"
Developers must be trained that AI output is merely a first draft. The developer's primary job is to ruthlessly refactor the AI's verbose output. If the AI generates 50 lines of code, the human engineer must spend 10 minutes figuring out how to abstract it down to 15 lines before opening a Pull Request.

### 2. Automated Cyclomatic Complexity Checks
You must upgrade your CI/CD pipeline. Implement automated tools (like SonarQube) that measure "Cyclomatic Complexity" (how many different logical paths exist in a function). If an AI generates a massive, convoluted function, the CI/CD pipeline must mathematically reject the Pull Request until a human simplifies it.

### 3. The Power of the Deletion PR
The best Tech Leads celebrate "Deletion PRs" (Pull Requests where more code is deleted than added). They force the team to constantly prune the dead code generated by AI to keep the architecture lean and maintainable.

## The Security Risk: AI-Generated Vulnerabilities and Hallucinated Dependencies

Beyond bloat, **AI in application development** introduces a subtler risk: security vulnerabilities baked into code that looks syntactically correct and sails through a cursory review. LLMs learn from public repositories that include outdated and insecure patterns (string concatenation for SQL queries, weak cryptographic defaults, placeholder API keys that a junior developer forgets to remove). Because the code compiles and the tests pass, these vulnerabilities frequently slip through code review undetected until a penetration test, or worse, a breach.

### 1. Slopsquatting: The Hallucinated Package Attack
A specific and rapidly growing threat is "package hallucination." When an LLM is asked to import a library, it will sometimes invent a plausible-sounding package name that does not actually exist (for example, suggesting `flask-auth-utils` instead of the real `flask-login`). Attackers have started monitoring these predictable hallucinations and registering the exact fabricated package names on public registries like npm and PyPI, filling them with malicious payloads. Security researchers call this technique "slopsquatting," a term coined by Python Software Foundation Developer-in-Residence Seth Larson. A developer who copy-pastes the AI's suggested `pip install` or `npm install` command without verifying the package's provenance can unknowingly pull malware directly into the build pipeline.

This is not a fringe edge case. A large-scale academic study by researchers at the University of Texas at San Antonio, Virginia Tech, and the University of Oklahoma, "We Have a Package for You! A Comprehensive Analysis of Package Hallucinations by Code Generating LLMs," analyzed 576,000 code samples generated by 16 different LLMs and found that 19.7% of the recommended packages did not exist, over 205,000 unique hallucinated package names in total. The rate was worse for open-source models (21.7%) than commercial ones (5.2%), but no model tested was immune, and even a well-regarded commercial model in the study still hallucinated packages several percent of the time. At that rate, a team merging a handful of AI-suggested dependencies every sprint is not facing a hypothetical risk; they are facing a statistical certainty over a long enough timeline, unless a provenance gate is in place.

### 2. The Fix: Provenance Gates, Not Trust
You cannot solve this by asking developers to "be more careful." You need mechanical gates in the pipeline itself:
- **Dependency allow-listing:** New packages must be manually approved and added to an internal registry mirror before they can be installed, closing the door on typosquatted or hallucinated names entirely.
- **Software Composition Analysis (SCA):** Tools like Snyk or Dependabot scan every new dependency for known vulnerabilities and suspiciously low download or reputation scores before a build is permitted to proceed.
- **SAST on every AI-assisted Pull Request:** Static Application Security Testing must run on every PR, not just the ones flagged as "AI-generated," because most teams cannot reliably self-report which PRs used AI assistance in the first place.

At Manifera, this is treated as a governance function, not a suggestion. Our Dutch Architects require an approved dependency manifest for every project, and our CI/CD pipelines block any Pull Request that introduces an unverified package, regardless of whether a human or an AI wrote the import statement.

### 3. Maintaining an AI Bill of Materials
Forward-thinking engineering teams now maintain an "AI Bill of Materials" alongside their standard Software Bill of Materials (SBOM): a running log of which parts of the codebase were AI-assisted, which model generated them, and which senior engineer approved the final refactor. This is not bureaucratic overhead. When a critical vulnerability is disclosed in a widely used package six months from now, the team needs to answer one question in minutes, not days: which of our services actually import that hallucinated or vulnerable dependency, and who signed off on it? Without that audit trail, a security incident becomes an archaeology project.

## What Ungoverned AI Velocity Actually Costs, in Numbers

The "40% more Pull Requests" scenario in the introduction is not exaggerated for effect. It is worth walking through what that velocity gain actually costs a team over two release cycles, once the GitClear-documented pattern of rising clone rates and falling refactor rates plays out inside a real codebase. The following is an illustrative planning scenario for a mid-sized SaaS backend, not a specific client's audited numbers.

**Quarter 1: Ungoverned AI adoption**
- Pull requests merged per week rise from roughly 25 to 35, a genuine short-term velocity gain.
- Following the pattern GitClear documented industry-wide, the share of copy-pasted code in new commits climbs from a healthy single-digit baseline toward the 12%+ range, while genuinely refactored code shrinks.
- CI pipeline time increases 20-30% as the codebase grows without a corresponding grow in test efficiency, since AI-generated tests often mirror the verbosity of the code they cover.
- Defect rate on the newly duplicated code sits in the 15-50% higher range GitClear's cited research associates with cloned code blocks, compared to properly abstracted equivalents.

**Quarter 2: The bill arrives**
- New feature velocity slows, not because the team got worse, but because every change to a duplicated piece of logic now has to be found and applied in three or four places instead of one.
- On-call load rises as the elevated defect rate from Quarter 1's duplicated code surfaces in production.
- A senior engineer, or an outside architect brought in specifically for this, has to spend several weeks on a deduplication and refactor pass before feature work can resume at a sustainable pace, effectively clawing back a meaningful share of the Quarter 1 velocity gain.

**The governed alternative**
A team running Cyclomatic Complexity gates, mandatory Deletion PR culture, and a senior architect reviewing for abstraction from week one typically sees a smaller initial velocity spike (closer to 15-20% more PRs merged, not 40%) but does not incur the Quarter 2 clawback. Over two quarters, the governed team's net throughput is usually higher than the ungoverned team's, because it never has to spend a sprint paying down debt it didn't need to create. The lesson is not that AI-assisted velocity is fake. It is that ungoverned velocity is frequently borrowed from a future sprint at a poor exchange rate.

## The Manifera Governance Standard

Many [offshore software development](https://www.manifera.com/services/offshore-software-development/) agencies use AI to artificially inflate their output, billing you for thousands of lines of bloated, unmaintainable code. 

At Manifera, we use AI to move fast, but we govern it with extreme European rigor. 

Our Hybrid Offshore model places a senior Dutch Architect as the gatekeeper for every line of code produced by our Vietnamese engineering pods. The Dutch Architect reviews the AI-assisted code not just for functionality, but for elegance, abstraction, and the absence of Dead Code. 

We ensure that the speed of AI does not compromise the structural integrity of your enterprise architecture. 

Stop paying for bloated, AI-generated technical debt. Contact our Amsterdam team to deploy a highly governed engineering pod.

---

## Frequently Asked Questions

### (Scenario: CTO auditing codebase health) What is 'Dead Code' and why does AI generate so much of it?
Dead Code is code that exists in the application but is never actually executed. AI models generate it because they favor verbosity and 'defensive programming' (adding error handling for theoretical edge cases that don't apply to your specific business logic). Junior developers often leave this extra code in, bloating the system.

### (Scenario: Lead Developer reviewing PRs) Why does AI code generation often violate the DRY (Don't Repeat Yourself) principle?
AI models are statistical prediction engines, not software architects. Instead of analyzing your existing codebase to find and reuse a helper function (Abstraction), the AI will usually just write the full logic again from scratch. This leads to massive code duplication, making future maintenance exponentially harder.

### (Scenario: VP Engineering planning CI/CD upgrades) How can we automatically prevent developers from merging bloated AI code?
You must integrate Static Code Analysis tools (like SonarQube) into your CI/CD pipeline. You can set strict thresholds for 'Cyclomatic Complexity' or 'Code Duplication'. If a developer uses AI to generate a highly convoluted or repetitive function, the CI pipeline will automatically block the Pull Request until a human refactors it.

### (Scenario: Founder worried about offshore agency quality) Why do some offshore agencies love using AI to write verbose code?
Some agencies measure 'productivity' by Lines of Code (LOC) or use it to justify their billable hours. AI allows them to generate thousands of lines of code instantly. If they are not governed by strict European architects, they will deliver a massive, bloated codebase that is technically functional but structurally unmaintainable.

### (Scenario: IT Procurement evaluating Manifera) How does Manifera's Hybrid Model ensure AI tools don't ruin the architecture?
Our Dutch Architects act as the ultimate firewall. While our Vietnamese pods use AI to increase their initial coding speed, the Dutch Architect manually reviews every Pull Request. They ruthlessly enforce abstraction, demand the deletion of Dead Code, and ensure the final merged code is elegant, lean, and strictly adheres to European architectural standards.

### (Scenario: Security Engineer reviewing AI-assisted commits) What is 'slopsquatting' and how does it relate to AI code generation?
AI models sometimes hallucinate plausible but non-existent package names when generating import statements. Attackers monitor these predictable hallucinations and publish real, malicious packages under those exact names on registries like npm or PyPI, a supply-chain attack known as slopsquatting. A developer who blindly installs the AI-suggested dependency can pull malware straight into the build pipeline.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What is 'Dead Code' and why does AI generate so much of it?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Dead code is written code that is never executed. AI generates it because it writes highly defensive, verbose boilerplate for edge cases that don't apply to your specific app. Junior developers blindly accept it, bloating the codebase."
      }
    },
    {
      "@type": "Question",
      "name": "Why does AI code generation often violate the DRY (Don't Repeat Yourself) principle?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "AI lacks macro-level architectural awareness. Instead of finding and reusing an existing abstracted function, the AI simply writes the logic again from scratch, leading to massive code duplication and maintenance nightmares."
      }
    },
    {
      "@type": "Question",
      "name": "How can we automatically prevent developers from merging bloated AI code?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Integrate Static Code Analysis (e.g., SonarQube) into your CI/CD pipeline. Set strict limits on Cyclomatic Complexity and duplication. The pipeline will automatically block any bloated AI-generated Pull Requests until a human simplifies them."
      }
    },
    {
      "@type": "Question",
      "name": "Why do some offshore agencies love using AI to write verbose code?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "It artificially inflates their perceived productivity (Lines of Code) and justifies billable hours. Without strict architectural governance, they will deliver a massive, unmaintainable codebase built entirely of AI spaghetti code."
      }
    },
    {
      "@type": "Question",
      "name": "How does Manifera's Hybrid Model ensure AI tools don't ruin the architecture?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Our Dutch Architects review every PR generated by our Vietnamese pods. We enforce abstraction, mandate the deletion of dead code, and ensure the final merged code is elegant, lean, and strictly adheres to European standards."
      }
    },
    {
      "@type": "Question",
      "name": "What is 'slopsquatting' and how does it relate to AI code generation?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "AI models sometimes invent plausible but non-existent package names when suggesting imports. Attackers register those exact hallucinated names on registries like npm or PyPI with malicious code inside, so a developer who blindly installs the AI's suggested dependency can pull malware directly into the build pipeline."
      }
    }
  ]
}
</script>
