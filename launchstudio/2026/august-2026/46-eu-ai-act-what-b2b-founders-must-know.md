---
Title: "The EU AI Act: Actionable Compliance Steps for B2B AI SaaS Founders"
Keywords: ai security risk, ai privacy issues, ai saas, ai native, ai deployment, ai and software development
Buyer Stage: Awareness
---

# The EU AI Act: Actionable Compliance Steps for B2B AI SaaS Founders

If you thought GDPR was a headache, prepare for the European Union Artificial Intelligence Act. As the world's first comprehensive legal framework for AI, entering into force in phases from 2024 through 2027, it does not just dictate how you handle data; it dictates what you are legally allowed to build, and how you must prove it's safe before you ship it. If you have customers in Europe — or your output is used by anyone in Europe, regardless of where your company is incorporated — you must understand the Act's "Risk Tier" classification system, or risk fines that could bankrupt your startup overnight.

## The Risk-Based Approach

The genius, and the burden, of the EU AI Act is that it does not regulate the technology itself; it regulates the *use case*. A Large Language Model is not inherently illegal, but how you deploy it might be — the exact same summarization model can be "Minimal Risk" powering a meeting-notes tool and "High-Risk" powering a resume screener, depending entirely on what decision it's attached to. The Act divides AI into four risk categories, and correctly classifying your product is the first and most consequential compliance decision you'll make.

## 1. Unacceptable Risk (Banned)

You cannot build these systems, period — no compliance pathway exists. This tier includes AI designed for "Social Scoring" (ranking citizens based on behavior or predicted trustworthiness), AI that deploys subliminal or manipulative techniques to distort behavior in ways likely to cause harm, real-time remote biometric identification in public spaces by law enforcement (with narrow carve-outs), and untargeted scraping of facial images from the internet or CCTV footage to build facial recognition databases — a provision that effectively outlawed the core business model of companies like Clearview AI in the EU market. Fines for deploying banned systems reach up to €35 million or 7% of global annual turnover, whichever is higher — the steepest penalty tier in the regulation.

## 2. High-Risk (Heavily Regulated)

This is where most B2B startups get caught, often without realizing it. An AI system is High-Risk if it's used as a safety component of a regulated product, or if it falls into one of the use-case categories listed in Annex III — which includes employment, education, credit and insurance, law enforcement, migration, and access to essential public and private services. Concretely, examples include:

- **HR Tech:** An AI that reads resumes and automatically filters, ranks, or rejects candidates before a human reviews them.

- **Fintech:** An AI that determines whether a user is approved for a business loan, sets their credit limit, or prices their insurance premium.

- **EdTech:** An AI that scores student exams or determines admission to educational institutions.

If you build High-Risk AI, you must comply with substantial obligations before you launch: establish a continuous risk management system spanning the product's lifecycle, ensure your training data is representative and tested for bias, maintain automated logs of every AI decision (technical documentation and record-keeping under Articles 11-12), register the system in the EU database where applicable, and guarantee genuine "Human-in-the-Loop" oversight — meaning a human with real authority and context to override the machine, not a rubber-stamp approval button. Providers of High-Risk systems must also conduct a conformity assessment before placing the system on the market, and in many cases this requires third-party assessment, not just self-certification.

## 3. Limited Risk (Transparency Required)

Most standard B2B generative AI tools fall here. If you build an AI chatbot for customer support, a tool that generates marketing copy, or an AI that produces synthetic audio or video for advertising, the primary requirement under Article 50 is **Transparency**.

You must explicitly inform the user that they are interacting with a machine, not a human, unless it's obvious from context. Furthermore, any AI-generated or AI-manipulated audio, image, or video content that could be mistaken for authentic (deepfakes) must be clearly disclosed and, where technically feasible, machine-readably marked as artificially generated — a requirement that's pushing providers toward content provenance standards like C2PA.

## 4. Minimal Risk (Unregulated)

This covers AI systems like spam filters, inventory-recommendation engines, or AI-powered video game NPCs. The Act leaves these largely unregulated, though the Commission encourages voluntary codes of conduct, and providers can opt in to some High-Risk-style governance practices to build market trust even when not legally required to.

## General Purpose AI (GPAI) Models and Systemic Risk

If you are building on top of, or are yourself, a foundation model provider, the Act includes specific rules for "General Purpose AI" under Chapter V. All GPAI providers must maintain technical documentation and a summary of training content, and cooperate with downstream deployers. Models that cross a compute threshold (currently set around 10^25 FLOPs used in training) are presumed to carry "systemic risk" and face additional obligations: mandatory model evaluations, adversarial testing, systemic risk assessment and mitigation, and a duty to report serious incidents directly to the AI Office at the European Commission. If your startup fine-tunes an open-weight model and redistributes it, you may inherit some of these obligations as a modifier, not just as a user — a nuance many teams miss until a legal review flags it.

## Getting the Classification Right Is an Engineering Problem, Not Just a Legal One

Determining your risk tier requires mapping your actual decision logic — what the AI outputs, what happens to that output next, and who it affects — not just describing your product in marketing language. This is a joint legal-and-architecture exercise, and it's exactly the kind of cross-cutting compliance work Manifera has built its reputation on since its founding in **2014**, delivering 160+ projects, including regulator-adjacent work with TNO, from its Amsterdam HQ at Herengracht 420 and its engineering hub in Ho Chi Minh City, Vietnam. Herre Roelevink, Founder & Managing Director of Manifera, describes the shift plainly: "We see a shift in software needs. The challenge is no longer turning good ideas into software. It's now about the architecture and security needed to bring those products to maturity. We have eleven years of experience in exactly that." See the underlying delivery model at [Manifera's offshore software development services](https://www.manifera.com/services/offshore-software-development/).

## Key Takeaways

- The EU AI Act applies to any startup, worldwide, that provides AI services to users located within the European Union, or whose AI output is used within the EU. Extraterritoriality is enforced strictly, similar to GDPR.

- The Act regulates AI based on the risk of its use case, not the underlying model, dividing systems into Unacceptable, High, Limited, and Minimal risk tiers — the same model can sit in different tiers depending on deployment.

- Building 'High-Risk' systems (like AI for hiring, lending, or education) requires substantial compliance overhead: bias testing, decision logging, conformity assessment, and genuine human oversight before launch.

- Standard generative AI (Limited Risk) requires strict transparency; you must tell users they are talking to a bot, and clearly, machine-readably label deepfakes or synthetic media.

- Fines for non-compliance are severe, reaching up to €35 million or 7% of global annual revenue for deploying 'Unacceptable Risk' systems, with lower but still substantial tiers for other violations.

- Foundation model providers and anyone fine-tuning and redistributing open-weight models may inherit GPAI obligations, including systemic risk reporting, once compute or usage thresholds are crossed.

## Audit Your AI Risk Tier

Are you accidentally building a 'High-Risk' system? **LaunchStudio** provides technical and architectural audits to ensure your B2B SaaS complies with the EU AI Act's transparency and data governance requirements before you launch in Europe. Get a scoped estimate via the [LaunchStudio calculator](https://launchstudio.eu/en/#calculator).

LaunchStudio is an initiative powered by **Manifera**, an international software development company founded in **2014** by **Herre Roelevink**. Recognizing the shortage of experienced developers in Europe, Herre established development hubs in **Singapore** (100 Tras Street #16-01, 100 AM Singapore 079027) and **Ho Chi Minh City, Vietnam** (Floor 11, Block C, 10 Pho Quang Street, Tan Son Hoa Ward), to leverage high-efficiency engineering talent. Guided by the philosophy of combining "Dutch management with Vietnamese mastery," Manifera operates its European HQ in **Amsterdam, the Netherlands** (Herengracht 420, 1017 BZ). Through LaunchStudio, AI-native founders gain direct access to this enterprise-grade global software development expertise to get their prototypes secure, scalable, and launch-ready in just 1 to 3 weeks. [Get a free quote today](https://launchstudio.eu/en/#contact).

## Real example

### An AI-Native Founder in Action: Adding Decision Log Audits for an AI Recruiter

Lincoln, an HR startup founder, used **Lovable** to build a recruiter app. The app required audit trails under the new EU AI Act regulations because it automatically filtered and ranked candidates before a human ever saw the shortlist — squarely inside the High-Risk employment category.

He partnered with **LaunchStudio (by Manifera)** to build automated database loggers tracking AI scoring metrics, model versions, and decision parameters for every candidate evaluated.

**Result:** App met the EU AI Act's documentation requirements, securing European expansion.

**Cost & Timeline:** €2,400 (AI Act Audit Trail) — production-ready and deployed in 6 business days.

---

## Frequently Asked Questions

### What is the EU AI Act?

It is the world's first comprehensive legal framework for AI, regulating systems based on the level of risk they pose to citizens' safety and fundamental rights, with obligations phasing in from 2024 through 2027.

### Does the Act apply to US-based startups?

Yes. If your US startup offers AI services to European citizens, or the output of your AI is used within the EU regardless of where the company or servers are based, you are legally bound by the Act, just as with GDPR.

### What is a 'High-Risk' AI system?

AI that affects employment (resume screening), credit scoring, insurance pricing, education, or critical infrastructure. These require conformity assessment, mandatory documentation, bias mitigation, and human oversight before launch.

### What AI practices are outright banned?

Social scoring systems, AI that manipulates human behavior via subliminal techniques, real-time public biometric surveillance by law enforcement (with narrow exceptions), and mass scraping of facial images to build biometric databases are strictly prohibited.

### How does LaunchStudio, powered by Manifera, help with AI Act compliance?

LaunchStudio, an initiative of Manifera (founded 2014, 160+ delivered projects), audits your actual decision logic to determine your real risk tier, then builds the logging, documentation, and human-oversight features the Act requires — turning a legal classification exercise into shipped code.
