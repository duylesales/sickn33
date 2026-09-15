---
Title: "Who Owns Your Side Project? IP, Open Source and AI Models for Engineers Employed in the Netherlands"
Keywords: side project ownership netherlands, intellectual property employee software, open source contribution employer, ai model ownership employee, ip clause data scientist, OnlyAIJobs
Buyer Stage: Consideration / Career Planning
Target Persona: B (Experienced AI or ML engineer)
Content Format: Career Guide
---

# Who Owns Your Side Project? IP, Open Source and AI Models for Engineers Employed in the Netherlands

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Who Owns Your Side Project? IP, Open Source and AI Models for Engineers Employed in the Netherlands",
  "description": "Many AI engineers build tools, models and open-source projects outside their job. A guide to how Dutch copyright, patent and trade secret rules, employment contracts and open-source licences determine who owns that work.",
  "author": {"@type": "Organization", "name": "OnlyAIJobs", "url": "https://onlyaijobs.eu"},
  "publisher": {"@type": "Organization", "name": "OnlyAIJobs", "url": "https://onlyaijobs.eu"},
  "datePublished": "2026-11-16",
  "mainEntityOfPage": {"@type": "WebPage", "@id": "https://onlyaijobs.eu/blog/ip-clauses-side-projects-ai-engineers"},
  "inLanguage": "en",
  "about": [{"@type": "Thing", "name": "Intellectual property of employee side projects"}, {"@type": "Place", "name": "Netherlands"}],
  "mentions": [
    {"@type": "Legislation", "name": "Dutch Copyright Act (Auteurswet), Article 7"},
    {"@type": "Legislation", "name": "Dutch Patents Act 1995 (Rijksoctrooiwet 1995), Article 12"},
    {"@type": "Legislation", "name": "Dutch Trade Secrets Protection Act (Wet bescherming bedrijfsgeheimen)"},
    {"@type": "Legislation", "name": "Dutch Databases Act (Databankenwet)"},
    {"@type": "Legislation", "name": "Directive (EU) 2019/790 on Copyright in the Digital Single Market"},
    {"@type": "Legislation", "name": "Dutch Civil Code, Article 7:653a (side activities)"},
    {"@type": "Thing", "name": "Apache License 2.0"},
    {"@type": "Thing", "name": "GNU General Public License"},
    {"@type": "Thing", "name": "MIT License"},
    {"@type": "Legislation", "name": "EU Artificial Intelligence Act"}
  ]
}
</script>

Machine learning engineers and data scientists are builders by nature. Many maintain open-source libraries, publish notebooks, train small models over the weekend, build tools that later become startups or contribute to community projects. At some point, a question arises that few think about in advance: does this work belong to me or to my employer? The answer in the Netherlands depends on a combination of copyright law, patent law, trade secret protection, the employment contract and — for open-source work — licences. Understanding these rules protects both your projects and your relationship with your employer.

This article provides general information, not legal advice. For specific situations, consult an intellectual property or employment lawyer.

## The Default Rule for Copyright: Work Created in Performing Your Duties

Software, documentation, notebooks and many other outputs of AI work can be protected by copyright if they are original creations. Under **Article 7 of the Dutch Copyright Act**, when an employee creates a work in the performance of their duties, the employer is considered the maker of that work, unless otherwise agreed.

The key phrase is "in the performance of their duties". Work that clearly falls within your job — code written for your employer's product, models trained for your team's project — belongs to the employer. Work created outside your job, unrelated to your duties and without using employer resources, generally remains yours under the default rule.

The difficult cases lie in between. A tool built in the evening that solves a problem you face at work, a library that generalises code you wrote for your employer or a model trained on your own time but using techniques developed at work can raise genuine questions.

## Patents: When the Nature of the Job Involves Inventing

Most AI software is protected by copyright rather than patents, but some AI-related inventions — particularly technical applications in hardware, medical devices or industrial processes — can be patented. Under **Article 12 of the Dutch Patents Act 1995**, an employer is entitled to a patent for an invention made by an employee if the nature of the employee's position requires using special knowledge to make inventions of that kind. In some circumstances, the employee may be entitled to fair remuneration if the invention's value exceeds what can reasonably be considered covered by salary.

For researchers and engineers at companies that file patents, this means inventions related to the job generally belong to the employer, while inventions unrelated to the role may remain with the employee.

## Contract Clauses Often Go Further

Employment contracts frequently include intellectual property clauses that extend beyond the statutory defaults. Common examples include clauses that:

- Transfer all intellectual property created during employment to the employer, regardless of when or where it was created.
- Require employees to disclose all inventions.
- Cover work "related to the employer's business", which can be broad for companies active in AI.
- Require employees to cooperate in registering rights.

Whether such clauses are fully enforceable depends on their wording, the circumstances and general principles of reasonableness. Very broad clauses covering unrelated personal projects may be challenged, but litigation is costly and uncertain. The practical lesson is to read these clauses before signing and to negotiate exclusions for existing and unrelated projects.

## Trade Secrets and Confidential Information

The **Dutch Trade Secrets Protection Act**, implementing the EU Trade Secrets Directive, protects information that is secret, has commercial value because it is secret and is subject to reasonable secrecy measures. In AI work, this can include training data, model architectures, hyperparameters, evaluation results, feature engineering methods and customer insights.

Even if a side project is legally yours, using your employer's confidential information to build it can violate trade secret rules and your contract. Common risks include reusing proprietary data, replicating internal model designs or using insights from confidential customer projects.

## Databases and Training Data

The **Dutch Databases Act** protects databases where there has been substantial investment in obtaining, verifying or presenting the contents. Datasets compiled at work may be protected, and extracting substantial parts for a personal project can infringe the employer's rights.

For training data from external sources, copyright and licensing rules also matter. The **EU Directive on Copyright in the Digital Single Market** introduced exceptions for text and data mining, including a general exception that rights holders can opt out of by reserving their rights, for example in machine-readable form. The **EU AI Act** requires providers of general-purpose AI models to put in place a policy to comply with EU copyright law, including respecting such reservations. Engineers training models on scraped data in side projects should be aware of these rules.

## Side Activities and Conflicts of Interest

Under **Article 7:653a of the Dutch Civil Code**, an employer may only prohibit or restrict an employee's side activities if there is an objective justification, such as preventing conflicts of interest or protecting confidential business information. This means a blanket ban on side projects is not automatically valid.

However, a side project that competes with your employer, targets the same customers or uses similar confidential knowledge can create a genuine conflict of interest. Transparency is usually the best approach: informing your manager about significant side projects reduces misunderstandings.

## Open-Source Contributions

Open-source work adds another layer.

**Contributions made as part of your job.** If your employer encourages or requires contributions to open-source projects, the employer typically owns the copyright in those contributions and decides under which licence they are released. Many companies have open-source policies that specify approval processes.

**Contributions made in your own time.** Personal contributions to open-source projects generally belong to you, unless your contract assigns them to the employer. Many projects require contributors to sign a contributor licence agreement, in which you confirm you have the right to contribute — something you should only do if you are sure your employer does not claim the rights.

**Licences.** Permissive licences such as the **MIT License** and the **Apache License 2.0** allow broad reuse, while copyleft licences such as the **GNU General Public License** require derivative works to be distributed under the same licence. Using copyleft code in employer products without approval can create compliance problems.

## AI-Generated Code and Model Outputs

Increasingly, engineers use AI coding assistants to write parts of their code. Under EU copyright principles, protection generally requires originality reflecting the author's own intellectual creation. The extent to which code or content generated mainly by AI is protected by copyright remains uncertain and is the subject of legal debate. Employers also often have policies on the use of AI assistants for work code, particularly regarding confidential information entered into external tools.

For side projects, this uncertainty can matter if you later commercialise the project: investors and acquirers may ask how code was created and whether rights are clear.

## When You Change Jobs: Taking Knowledge, Not Code

Changing employers raises a related question: what can you take with you? The general principle is that your skills, experience and general professional knowledge belong to you. You can use what you learned about forecasting methods, model evaluation or data architecture in your next job. What you cannot take is the former employer's property and confidential information: source code, trained models, datasets, internal documents, customer information or specific confidential methods.

In practice, the boundary can be subtle. Rewriting a former employer's proprietary pipeline from memory in detail may cross the line, while applying the general approach to a new problem is normal professional practice. Downloading files or copying repositories before leaving is a clear risk and can lead to legal action under trade secret rules and contractual obligations.

Good practices when leaving include returning or deleting all company data and equipment, not forwarding work documents to personal accounts and being cautious about recreating specific internal tools. New employers also have an interest here: most will explicitly ask new hires not to bring confidential information from previous jobs, to avoid legal exposure.

For open-source projects you maintained as part of your job, check whether you can continue contributing personally after leaving — many projects welcome this, but the previous employer may control the project's governance.

## A Concrete Scenario: The Weekend Library That Became a Product

A machine learning engineer at a logistics company builds an open-source library in the evenings for time series forecasting of intermittent demand — a problem she encountered at work. The library becomes popular, and a startup offers to hire her to build a commercial product on top of it.

Her employer's legal department raises concerns: the library solves a problem closely related to her job, and some ideas resemble internal work. Her contract contains a broad IP clause covering inventions "related to the business". After review, it becomes clear that she wrote the library on her own equipment, outside working hours, without using internal code or data, and that she informed her manager when she started. The employer agrees to confirm in writing that it does not claim rights to the library. The situation is resolved because she kept clear boundaries — and documented them.

## A Common Misconception

A widespread misconception is that anything created outside working hours automatically belongs to the employee. In reality, the connection to the job, the use of employer resources and information and the contract terms all matter. The reverse misconception — that employers own everything an employee ever creates — is also incorrect. The truth lies in the details, which is why clarity at the start of employment and transparency during it are so valuable.

## Practical Steps to Protect Your Side Projects

- **List existing projects** in your employment contract or an annex before starting a job.
- **Read and negotiate IP clauses** so they focus on work related to your duties.
- **Keep clear boundaries:** use your own equipment, accounts and time, and never use employer data or confidential information.
- **Inform your employer** about significant side projects, particularly if they are related to your field.
- **Check the employer's open-source policy** before contributing to projects related to your work.
- **Get written confirmation** if your employer agrees that a project is yours.
- **Be careful with training data licences** and text and data mining opt-outs.
- **Seek advice** before commercialising a project that is related to your job.

## Questions to Ask Before Signing a Contract

- **Does the IP clause cover work outside working hours and unrelated to my role?**
- **Can existing personal and open-source projects be excluded explicitly?**
- **What is the company's policy on open-source contributions?**
- **Are side activities allowed, and under which conditions?**
- **Is there a policy on using AI coding assistants for work and personal projects?**

## Key Takeaways

- Under the Dutch Copyright Act, employers own works employees create in the performance of their duties; unrelated work created independently generally remains with the employee.
- The Patents Act gives employers rights to inventions when the nature of the job involves making such inventions, sometimes with fair remuneration for the employee.
- Contract IP clauses often go further than the law; read and negotiate them before signing.
- Trade secret, database and copyright rules — including text and data mining opt-outs — limit what employer information and external data can be used in side projects.
- Side activity restrictions require objective justification, and transparency with your employer is the best protection for your projects.

## Where to Start

Before your next job change, list your personal and open-source projects, read the IP clauses carefully and agree on clear boundaries — it is far easier than resolving disputes later.

Browse current AI, machine learning and data jobs at [onlyaijobs.eu/jobs](https://onlyaijobs.eu/jobs).

## Frequently Asked Questions

### (Scenario: engineer building a tool in the evening) Does my employer own code I write outside working hours?
Not automatically — it depends on whether the work relates to your duties, whether you used employer resources or information, and what your contract says.

### (Scenario: engineer contributing to open source) Can I contribute to open-source projects while employed?
Generally yes for personal contributions, but check your contract and the employer's open-source policy, especially for projects related to your work.

### (Scenario: researcher who made an invention) Who owns a patentable invention I made at work?
The employer is entitled if your position requires making such inventions; you may be entitled to fair remuneration in some cases.

### (Scenario: engineer planning a startup) Can I turn my side project into a company?
Possibly, if it was built independently, without employer information or resources, and your contract does not assign the rights; seek advice before commercialising.

### (Scenario: engineer using AI coding tools) Is code generated by AI protected by copyright?
This remains legally uncertain, because copyright generally requires original human creativity; check employer policies and keep track of how code was created.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {"@type": "Question", "name": "Does my employer own code I write outside working hours?", "acceptedAnswer": {"@type": "Answer", "text": "Not automatically — it depends on the link to your duties, use of resources and your contract."}},
    {"@type": "Question", "name": "Can I contribute to open-source projects while employed?", "acceptedAnswer": {"@type": "Answer", "text": "Generally yes for personal contributions; check your contract and open-source policy."}},
    {"@type": "Question", "name": "Who owns a patentable invention I made at work?", "acceptedAnswer": {"@type": "Answer", "text": "The employer if your role requires such inventions, sometimes with fair remuneration for you."}},
    {"@type": "Question", "name": "Can I turn my side project into a company?", "acceptedAnswer": {"@type": "Answer", "text": "Possibly, if built independently and not assigned by contract; seek advice first."}},
    {"@type": "Question", "name": "Is code generated by AI protected by copyright?", "acceptedAnswer": {"@type": "Answer", "text": "Legally uncertain, since copyright generally requires original human creativity."}}
  ]
}
</script>
