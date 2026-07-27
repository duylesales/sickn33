---
Title: "Navigating the EU AI Act: What AI SaaS Founders Must Know"
Keywords: AI In Saas, EU AI Act, AI Compliance, High-Risk AI, GPAI, AI Regulation, SaaS Founders, AI Governance
Buyer Stage: Awareness
---

# Navigating the EU AI Act: What AI SaaS Founders Must Know

For the first few years of the AI boom, startups operated in the Wild West. You could launch an AI resume screener, a predictive credit modeling tool, or an automated tenant-scoring platform over a weekend without a second thought about regulatory obligations. That era is definitively over.

The **European Union Artificial Intelligence Act** (Regulation (EU) 2024/1689) — commonly called the **EU AI Act** — entered into force on August 1, 2024. It is the world's first comprehensive, horizontally applicable legal framework governing artificial intelligence. Just as GDPR fundamentally reshaped how every technology company handles personal data, the AI Act is rewriting the rules for how AI systems are designed, developed, deployed, and monitored — not just in Europe, but globally for any company whose AI touches EU residents.

This is not a vague "future regulation." Key provisions are already enforceable, and others become mandatory on fixed dates through 2027. Here is what every AI SaaS founder must understand — in concrete, actionable detail — to avoid fines that can reach tens of millions of euros.

---

## The Enforcement Timeline: What Is Already Law and What Is Coming

The AI Act uses a **phased enforcement model**. Different obligations activate at different dates, giving companies time to prepare — but that preparation window is closing fast.

| **Date** | **What Becomes Enforceable** |
|---|---|
| **February 2, 2025** | Prohibitions on "Unacceptable Risk" AI practices take full effect. AI literacy obligations for providers and deployers begin. |
| **August 2, 2025** | Rules for General-Purpose AI (GPAI) models apply. Governance structures (national competent authorities, the EU AI Office) become operational. Penalties framework fully active. |
| **August 2, 2026** | Most remaining provisions apply, including all obligations for **High-Risk AI systems** listed in Annex III (HR, finance, education, law enforcement, etc.). Transparency obligations for Limited-Risk systems fully enforceable. |
| **August 2, 2027** | Obligations for High-Risk AI systems that are **safety components of products** already regulated under existing EU product-safety legislation (e.g., medical devices, machinery, aviation). |

**The practical implication for SaaS founders:** If your product uses AI in HR, recruitment, creditworthiness assessment, education, or insurance, you have until **August 2, 2026** to achieve full compliance. If you are building on top of foundation models (GPT-4, Claude, Gemini, Llama, Mistral), the GPAI rules your model provider must follow are already active as of **August 2, 2025**. And if your product falls under the "Unacceptable Risk" category, it is **already illegal** as of February 2025.

---

## The Extraterritorial Reach: Why Your Company's Location Is Irrelevant

A common misconception among founders is: *"I'm incorporated in Delaware and my servers are in AWS us-east-1, so European laws don't apply to me."* This is false and potentially very expensive.

Like GDPR, the AI Act has **broad extraterritorial scope** (Article 2). It applies to:

1. **Providers** (companies that develop or commission an AI system) who place their product on the EU market or put it into service in the EU — regardless of whether the provider is established inside or outside the EU.
2. **Deployers** (companies that use an AI system under their authority) established in the EU or in a place where EU law applies.
3. **Any provider or deployer located outside the EU** whose AI system's **output is used within the EU**.

That third point is the catch-all. If a hiring manager in Munich uses your SaaS platform to evaluate a candidate — even if your company has no EU office, no EU entity, and no EU servers — you are subject to the AI Act. If a loan officer in Amsterdam runs a creditworthiness check through your API, you are in scope. If a student in Lisbon receives an AI-generated grade from your EdTech platform, you are in scope.

**The only reliable way to avoid the AI Act is to actively geoblock all 27 EU member states plus the EEA** — a business decision most growth-stage SaaS companies cannot afford to make.

If you are subject to the AI Act but not established in the EU, you are required to designate an **authorized representative** in the EU (Article 22) before placing your system on the market. This is analogous to the GDPR requirement for a Data Protection Representative.

---

## The Risk-Based Classification System: Four Tiers, Radically Different Obligations

The AI Act does not regulate the technology itself — it regulates the **use case**. The same underlying AI model (say, a fine-tuned LLM) could be Minimal Risk in one application, High Risk in another, and Unacceptable Risk in a third. Classification depends entirely on what the system is *used for* and *how* it affects people.

### Tier 1: Unacceptable Risk — Outright Banned (Already Enforceable Since February 2, 2025)

These AI practices are **prohibited entirely** within the EU. There is no compliance path — you cannot build these, deploy these, or make them available to EU users under any circumstances.

The specific prohibitions (Article 5) include:

- **Social credit scoring systems**: AI that evaluates or classifies natural persons based on their social behavior or personal characteristics, leading to detrimental treatment disproportionate to the context. This applies to both government and private-sector implementations.

- **Subliminal, manipulative, or deceptive AI techniques**: Systems that deploy techniques beyond a person's consciousness, or exploit vulnerabilities related to age, disability, or social/economic situation, in a manner that materially distorts behavior and causes significant harm.

- **Biometric categorization based on sensitive attributes**: AI systems that categorize individuals based on biometric data to deduce race, political opinions, trade union membership, religious beliefs, sex life, or sexual orientation. (Exception: lawful labeling or filtering of biometric datasets in law enforcement.)

- **Emotion recognition in workplaces and educational institutions**: AI that infers emotions of employees or students based on biometric data, except for medical or safety purposes.

- **Untargeted scraping for facial recognition databases**: Creating or expanding facial recognition databases through untargeted scraping from the internet or CCTV footage.

- **Predictive policing based solely on profiling**: AI that assesses a person's likelihood to commit a crime based solely on profiling or personality traits, without objective and verifiable facts linked to criminal activity.

- **Real-time remote biometric identification in public spaces for law enforcement**: Subject to very narrow exceptions (e.g., imminent terrorist threat) with prior judicial authorization.

**Practical SaaS implications:** If your product includes any form of emotion detection applied to workplaces (monitoring employee moods during video calls, sentiment analysis in team meetings) or educational settings (monitoring student attentiveness through webcam analysis), it is **already illegal in the EU** since February 2025. Several EdTech and HR-tech tools that launched in 2023-2024 have had to shut down EU operations or fundamentally redesign their feature sets.

---

### Tier 2: High Risk — Strictly Regulated (Enforceable from August 2, 2026)

This is the tier where most B2B SaaS founders will find themselves ensnared. An AI system is classified as "High Risk" if it falls into one of the use cases enumerated in **Annex III** of the Act, or if it is a safety component of a product covered by existing EU product-safety harmonization legislation (Annex I).

#### Annex III High-Risk Use Cases Most Relevant to SaaS Founders

| **Domain** | **Specific Use Cases** | **Common SaaS Examples** |
|---|---|---|
| **Employment, workers management, access to self-employment** | AI for recruiting, screening CVs, evaluating candidates, making decisions on promotion/termination, allocating tasks based on individual behavior, monitoring/evaluating performance | ATS platforms with AI ranking, employee performance prediction tools, AI interview analyzers |
| **Access to essential private/public services** | AI for evaluating creditworthiness, setting insurance premiums, evaluating eligibility for public benefits, credit scoring | Fintech lending platforms, insurance pricing engines, credit scoring APIs |
| **Education and vocational training** | AI for determining access to educational institutions, evaluating learning outcomes, assessing appropriate education level, monitoring prohibited behavior during exams | AI grading tools, adaptive learning platforms with high-stakes assessments, proctoring software |
| **Administration of justice and democratic processes** | AI assisting judicial authorities in researching/interpreting facts and law, AI used to influence election outcomes | Legal AI research tools used by courts, political campaign AI tools |
| **Migration, asylum, and border control** | AI for processing visa/residence applications, assessing security risk of migrants | Immigration processing SaaS |
| **Biometric identification (non-prohibited)** | Remote biometric identification systems not covered by the ban, biometric categorization for non-prohibited purposes | Identity verification platforms for age/identity checks |

#### What "High Risk" Actually Requires: The Technical Compliance Burden

If your AI system is classified as High Risk, you must implement — and continuously maintain — the following **mandatory requirements** before placing it on the EU market (Articles 8-15):

**1. Risk Management System (Article 9)**
A documented, iterative process running throughout the entire lifecycle of the AI system. This is not a one-time risk assessment document — it must:
- Identify and analyze known and reasonably foreseeable risks.
- Estimate and evaluate risks from intended use *and* reasonably foreseeable misuse.
- Adopt risk mitigation measures and test their effectiveness.
- Be reviewed and updated when changes are made or significant new information emerges.

**2. Data Governance (Article 10)**
Training, validation, and testing datasets must meet stringent quality criteria:
- Relevant, sufficiently representative, and as free of errors as possible.
- Appropriate statistical properties, including for the specific geographical, contextual, behavioral, or functional setting in which the system will operate.
- Must address potential biases, particularly those leading to discrimination against protected groups.
- If personal data is used for bias monitoring/correction, specific safeguards apply including data minimization and access controls.

**3. Technical Documentation (Article 11)**
Before placing the system on the market, you must prepare comprehensive technical documentation demonstrating compliance with all requirements. This documentation must be kept up to date throughout the system's lifecycle. The required content is extensive — it includes a general description of the system, detailed information on the development process, design specifications, monitoring/functioning/control procedures, and a description of the risk management system.

**4. Record-Keeping / Automatic Logging (Article 12)**
High-Risk AI systems must be designed to automatically log events ("logs") throughout their lifetime. Logs must enable:
- Traceability of the system's functioning to the extent appropriate to its intended purpose.
- Identification of situations that may result in the system presenting a risk.
- Post-market monitoring.
- Monitoring of the system's operation by deployers.

Logs must be retained for a period appropriate to the intended purpose — at minimum the duration specified in applicable Union or national law, and no less than six months (unless otherwise specified in sectoral regulations).

**5. Transparency and Information to Deployers (Article 13)**
High-Risk AI systems must be designed to be sufficiently transparent to enable deployers to interpret the system's output and use it appropriately. You must provide:
- Clear instructions for use with concise, complete, correct, and understandable information.
- The system's capabilities and limitations, including its level of accuracy, robustness, and cybersecurity.
- Any known or foreseeable circumstances that may lead to risks.
- Technical measures to facilitate interpretation of outputs.
- Where appropriate, the specifications for input data.

**6. Human Oversight (Article 14)**
High-Risk AI systems must be designed so that they can be effectively overseen by natural persons during the period of use:
- The human overseer must be able to fully understand the system's capacities and limitations.
- Must be able to correctly interpret outputs (taking into account the characteristics of the system and available interpretability tools).
- Must be able to decide not to use the system, disregard, override, or reverse the output.
- Must be able to interrupt the system via a "stop" button or similar procedure.

**7. Accuracy, Robustness, and Cybersecurity (Article 15)**
- The system must achieve an appropriate level of accuracy, robustness, and cybersecurity throughout its lifecycle.
- Levels must be declared in accompanying instructions for use.
- Must be resilient against errors, faults, and attempts by unauthorized parties to alter its use or performance (including adversarial attacks such as data poisoning, model manipulation, or adversarial inputs).

#### Conformity Assessment: The Gatekeeping Procedure

Before you can legally place a High-Risk AI system on the EU market, you must undergo a **conformity assessment** (Article 43). For most Annex III High-Risk systems, this can be an internal conformity assessment based on internal control (Annex VI) — meaning you self-certify compliance, but must maintain all documentation and be prepared for audit by market surveillance authorities.

For certain biometric identification systems and a few other specific cases, a third-party conformity assessment (involving a notified body) is required.

After conformity assessment, you must:
- Affix a **CE marking** to the system.
- Register the system in the **EU AI database** (a publicly accessible, non-confidential database).
- Draw up an **EU declaration of conformity**.

---

### Tier 3: Limited Risk — Transparency Obligations (Enforceable from August 2, 2026)

This tier covers most generative AI tools, chatbots, and content-generation systems. The primary obligation is **transparency** (Article 50):

- **AI-generated content**: If your system generates synthetic audio, image, video, or text content, you must ensure the output is machine-readably marked as artificially generated or manipulated. This applies to deepfakes and any AI-generated media.

- **Chatbots and conversational AI**: You must clearly inform users that they are interacting with an AI system, not a human — unless this is obvious from the circumstances.

- **Emotion recognition or biometric categorization**: If your system performs emotion recognition or biometric categorization (in contexts where it is legal), you must inform the persons exposed to it about the system's operation and process their personal data in accordance with GDPR and the Law Enforcement Directive.

**Practical SaaS implications:** If you build a customer support chatbot, a content writing assistant, or an AI image generator, you must implement clear disclosure mechanisms. This means UI labels ("This response was generated by AI"), metadata tags on generated content (C2PA provenance markers or equivalent), and watermarking for generated images/video/audio.

---

### Tier 4: Minimal Risk — No Specific Obligations

AI applications like spam filters, AI-powered video game NPCs, inventory optimization tools, or recommendation engines for non-critical decisions fall here. The vast majority of AI systems belong in this category and face no additional regulatory obligations under the Act beyond existing general legislation (GDPR, consumer protection, product safety, etc.).

However, the Act **encourages** (but does not require) providers of Minimal Risk AI to voluntarily adopt codes of conduct aligned with the High-Risk requirements.

---

## General-Purpose AI (GPAI) Models: Provider vs. Deployer Obligations

The AI Act introduces specific rules for **General-Purpose AI models** (Articles 51-56) — foundation models like GPT-4, Claude, Gemini, Llama, and Mistral that can be adapted for many downstream tasks.

### If You Are a GPAI Model Provider (You Trained the Foundation Model)

You must:
- Maintain and make available technical documentation (including training process, data sources, evaluation results).
- Provide information and documentation to downstream providers who integrate your model into their own AI systems.
- Implement a policy to comply with EU copyright law (including the text and data mining opt-out provisions).
- Publish a sufficiently detailed summary of the training data content.

If your GPAI model poses **systemic risk** (defined as models trained with more than 10²⁵ FLOPs of cumulative compute, or designated by the European Commission), additional obligations apply: adversarial testing, incident reporting, adequate cybersecurity protections, and energy consumption reporting.

### If You Are a SaaS Deployer Building on Top of a GPAI Model

**You are not exempt from the AI Act simply because you use someone else's model.** The provider of the underlying GPAI model (OpenAI, Anthropic, Google, Meta) bears responsibility for the model-level obligations. But you, as the deployer or downstream provider of the *application*, bear responsibility for:

- **Correctly classifying your application's risk tier** based on its intended purpose.
- **Fulfilling all obligations** associated with that risk tier (High Risk, Limited Risk, etc.).
- **Conducting your own risk management** for the specific use case you built.
- **Ensuring the outputs** of the model as deployed in your system are appropriate, not discriminatory, and properly supervised.
- **Providing transparency** to end-users about the role of AI in your product.

In practical terms: if you build an AI-powered resume screener using the OpenAI API, OpenAI must comply with GPAI provider rules for their model — but *you* must comply with the full High-Risk system requirements for your screening application. You cannot delegate this to your model provider.

---

## The Penalties: The EU Is Not Bluffing

The penalty framework (Article 99) is deliberately designed to be painful at every scale of company:

| **Violation** | **Maximum Fine** |
|---|---|
| Deploying a **prohibited AI practice** (Unacceptable Risk) | **€35 million** or **7% of global annual turnover** (whichever is higher) |
| Failing to comply with **High-Risk system requirements** or GPAI obligations | **€15 million** or **3% of global annual turnover** |
| Supplying **incorrect, incomplete, or misleading information** to regulators | **€7.5 million** or **1% of global annual turnover** |

For SMEs and startups, the fines are adjusted to the lower of the two figures (absolute amount vs. percentage of turnover) — but even the "reduced" fines can be existential for a startup. A seed-stage company with €500K in annual revenue facing a €7.5 million fine for providing misleading information to a regulator is effectively shut down.

The penalties are enforced by **national market surveillance authorities** in each EU member state, coordinated by the **European AI Office** (established within the European Commission). The AI Office has direct enforcement power for GPAI model rules.

---

## A Practical Compliance Playbook for SaaS Founders

### Step 1: Classify Your System Honestly

Map every AI feature in your product against Annex III. Be conservative — if there is ambiguity about whether your system is High Risk, treat it as High Risk. Reclassification after launch is far more disruptive than building for compliance from the start.

### Step 2: Implement Logging Infrastructure from Day One

Automatic logging (Article 12) is one of the hardest requirements to retrofit. Design your database schema, API middleware, and model inference pipeline to capture:
- Every input sent to the AI model.
- Every output received.
- The model version used.
- The timestamp and user context.
- Any human override decisions.

Store logs in an immutable, tamper-evident format with appropriate retention policies.

### Step 3: Build the Human-in-the-Loop Mechanism

For High-Risk systems, this cannot be a checkbox. You need:
- A real interface where a qualified human can review AI decisions before they take effect.
- The ability for the human to override, reverse, or discard the AI's output.
- An emergency stop mechanism.
- Training materials and documentation for the human overseers.

### Step 4: Document Your Data Pipeline

Prepare technical documentation covering:
- What data was used for training/fine-tuning (provenance, quality, bias assessment).
- How bias was tested and mitigated.
- Accuracy/performance metrics on representative validation datasets.
- Known limitations and failure modes.

### Step 5: Prepare for Conformity Assessment

For Annex III High-Risk systems, prepare the internal conformity assessment (Annex VI):
- Establish a quality management system.
- Verify your system meets all Chapter III, Section 2 requirements.
- Draw up the EU declaration of conformity.
- Register in the EU database.
- Affix CE marking.

### Step 6: Appoint or Designate Responsible Persons

- Designate an internal AI compliance officer or assign responsibility to an existing legal/compliance role.
- If outside the EU: appoint an authorized representative in the EU before market placement.
- Ensure deployers receive adequate instructions for use.

---

## Build Compliant Infrastructure

Don't risk a €15 million fine. LaunchStudio builds secure, auditable database infrastructure that helps your startup meet the rigorous logging, data governance, human oversight, and risk management requirements of the EU AI Act.

LaunchStudio is operated by **Manifera**, an international software engineering company led by Founder & Director **Herre Roelevink**. Combining "Dutch management with Vietnamese mastery," Manifera maintains headquarters in **Amsterdam, the Netherlands** (Herengracht 420) and development hubs in **Singapore** and **Ho Chi Minh City, Vietnam**. Through LaunchStudio, our senior engineering teams take your AI-built frontend and implement production-ready security controls, automated logging pipelines, human-in-the-loop review interfaces, live payment gateways, secure hosting, and monitoring — transforming your prototype into a secure, EU AI Act-compliant MVP in 1 to 3 weeks. [Get a free quote today](https://launchstudio.eu/en/#contact).

---

## Real Example

### An AI-Native Founder in Action: AI HR Evaluation Tool

Stella, a startup founder, used **Cursor** to build an AI HR evaluation tool prototype that ranked job candidates using a fine-tuned LLM. The tool analyzed CVs, predicted cultural fit scores, and recommended interview shortlists. While the application was functionally impressive, it was blocked from launching in Europe due to multiple EU AI Act compliance gaps:

- **No automatic logging** of AI decisions — no audit trail of why specific candidates were ranked higher or lower.
- **No bias testing** on the training dataset — no evidence that the system didn't discriminate based on gender, ethnicity, or age.
- **No human-in-the-loop mechanism** — hiring managers received final ranked lists with no ability to inspect the AI's reasoning or override individual decisions.
- **No technical documentation** describing the system's accuracy, known limitations, or intended use conditions.

Stella partnered with **LaunchStudio (by Manifera)** to make the product launch-ready. The engineering team:

1. Built an **immutable model activity log system** capturing every input, output, model version, and timestamp in a tamper-evident audit trail.
2. Designed a **human review interface** where HR managers could inspect AI reasoning, override rankings, and document their decisions.
3. Configured **automated bias testing pipelines** running against representative demographic datasets, with alerts when disparate impact metrics exceeded thresholds.
4. Prepared **comprehensive technical documentation** covering data provenance, accuracy benchmarks, known limitations, and deployment guidelines.
5. Established **secure EU data hosting** (Frankfurt, Germany) with GDPR-compliant data processing and appropriate retention policies.

**Result:** Stella launched in full compliance with the EU AI Act High-Risk requirements, securing contracts with French and German corporations that required demonstrable regulatory compliance from their HR technology vendors.

**Cost & Timeline:** €5,200 (EU Compliance Package) — production-ready and deployed in 16 business days.

---

## Frequently Asked Questions

### What is the EU AI Act and when does it take effect?

The EU AI Act (Regulation (EU) 2024/1689) is the world's first comprehensive legal framework regulating artificial intelligence based on its potential to cause harm. It classifies AI systems into four risk tiers — Minimal, Limited, High, and Unacceptable — with progressively stricter obligations. It entered into force on August 1, 2024, with prohibitions on Unacceptable Risk practices already enforceable since February 2, 2025, GPAI model rules active since August 2, 2025, and most High-Risk system obligations becoming enforceable on August 2, 2026.

### Does the EU AI Act apply to my startup if I am based outside the EU?

Yes. The EU AI Act has broad extraterritorial reach, similar to GDPR. If your AI system is placed on the EU market, put into service in the EU, or its output is used within the EU — regardless of where your company is headquartered or where your servers are located — you must comply. A US-based startup whose SaaS is used by a single hiring manager in Germany is in scope. Non-EU providers must also designate an authorized representative in the EU before market placement.

### How do I determine if my SaaS product is classified as 'High Risk'?

Your AI system is High Risk if it falls into one of the use cases listed in Annex III of the Act. The most common SaaS-relevant categories are: employment and worker management (AI for recruiting, CV screening, performance evaluation), access to essential services (credit scoring, insurance pricing, loan decisions), and education (grading, admissions decisions, exam proctoring). If your AI influences decisions about people's access to jobs, credit, insurance, education, or public services, it is almost certainly High Risk. When in doubt, consult legal counsel specializing in EU AI regulation and treat ambiguous cases as High Risk.

### What technical measures must I implement for a High-Risk AI system?

High-Risk AI systems require six categories of technical compliance: (1) a continuously updated risk management system, (2) data governance ensuring training data quality and bias mitigation, (3) comprehensive technical documentation, (4) automatic logging of all AI system events with appropriate retention, (5) transparency provisions including clear instructions for deployers, and (6) human oversight mechanisms allowing qualified humans to understand, interpret, and override AI outputs. Additionally, you must demonstrate appropriate levels of accuracy, robustness, and cybersecurity, complete a conformity assessment, register in the EU AI database, and affix CE marking.

### What are the penalties for violating the EU AI Act?

Penalties are structured in three tiers based on the severity of the violation. Deploying a prohibited AI practice (Unacceptable Risk) carries fines up to €35 million or 7% of global annual turnover, whichever is higher. Failing to comply with High-Risk system requirements or GPAI obligations carries fines up to €15 million or 3% of global annual turnover. Supplying incorrect or misleading information to regulators carries fines up to €7.5 million or 1% of global annual turnover. For SMEs and startups, the lower of the two figures applies — but even reduced fines can be existential for early-stage companies.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What is the EU AI Act and when does it take effect?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "The EU AI Act (Regulation (EU) 2024/1689) is the world's first comprehensive legal framework regulating artificial intelligence based on its potential to cause harm. It classifies AI systems into four risk tiers — Minimal, Limited, High, and Unacceptable — with progressively stricter obligations. It entered into force on August 1, 2024, with prohibitions on Unacceptable Risk practices already enforceable since February 2, 2025, GPAI model rules active since August 2, 2025, and most High-Risk system obligations becoming enforceable on August 2, 2026."
      }
    },
    {
      "@type": "Question",
      "name": "Does the EU AI Act apply to my startup if I am based outside the EU?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. The EU AI Act has broad extraterritorial reach, similar to GDPR. If your AI system is placed on the EU market, put into service in the EU, or its output is used within the EU — regardless of where your company is headquartered or where your servers are located — you must comply. A US-based startup whose SaaS is used by a single hiring manager in Germany is in scope. Non-EU providers must also designate an authorized representative in the EU before market placement."
      }
    },
    {
      "@type": "Question",
      "name": "How do I determine if my SaaS product is classified as 'High Risk'?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Your AI system is High Risk if it falls into one of the use cases listed in Annex III of the Act. The most common SaaS-relevant categories are: employment and worker management (AI for recruiting, CV screening, performance evaluation), access to essential services (credit scoring, insurance pricing, loan decisions), and education (grading, admissions decisions, exam proctoring). If your AI influences decisions about people's access to jobs, credit, insurance, education, or public services, it is almost certainly High Risk."
      }
    },
    {
      "@type": "Question",
      "name": "What technical measures must I implement for a High-Risk AI system?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "High-Risk AI systems require six categories of technical compliance: (1) a continuously updated risk management system, (2) data governance ensuring training data quality and bias mitigation, (3) comprehensive technical documentation, (4) automatic logging of all AI system events with appropriate retention, (5) transparency provisions including clear instructions for deployers, and (6) human oversight mechanisms allowing qualified humans to understand, interpret, and override AI outputs. Additionally, you must demonstrate appropriate levels of accuracy, robustness, and cybersecurity, complete a conformity assessment, register in the EU AI database, and affix CE marking."
      }
    },
    {
      "@type": "Question",
      "name": "What are the penalties for violating the EU AI Act?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Penalties are structured in three tiers based on the severity of the violation. Deploying a prohibited AI practice (Unacceptable Risk) carries fines up to €35 million or 7% of global annual turnover, whichever is higher. Failing to comply with High-Risk system requirements or GPAI obligations carries fines up to €15 million or 3% of global annual turnover. Supplying incorrect or misleading information to regulators carries fines up to €7.5 million or 1% of global annual turnover. For SMEs and startups, the lower of the two figures applies — but even reduced fines can be existential for early-stage companies."
      }
    }
  ]
}
</script>
