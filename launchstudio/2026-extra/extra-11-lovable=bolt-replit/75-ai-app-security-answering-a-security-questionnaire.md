---
Title: "AI App Security: Answering a Security Questionnaire"
Keywords: ai app security, security questionnaire, vendor assessment, gdpr, supabase security, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: SaaS Scale-Up
---

# AI App Security: Answering a Security Questionnaire

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "AI App Security: Answering a Security Questionnaire",
  "description": "A spreadsheet of forty questions arrives from a customer's procurement team. What they are actually asking, which answers are fine without certifications, what you must never claim, and how to prepare once rather than every time.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-08-16",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/ai-app-security-answering-a-security-questionnaire" }
}
</script>

The deal is going well. The demo landed, the price is accepted, the champion inside the company wants it. Then an email arrives from someone you have not spoken to, with a spreadsheet attached and forty questions in it, and a note saying procurement needs this before contracting.

This is the moment where a large number of promising deals quietly die — not because the answers are bad, but because the founder does not answer for three weeks, answers vaguely, or panics and claims something that is not true.

The questionnaire is survivable. It is not a test you pass by having a compliance department; it is a test you pass by knowing how your own product works and saying so plainly.

## What They Are Actually Trying to Establish

Behind forty questions are four concerns.

**Will our data leak?** Who can reach it, how customers are separated, what happens if an employee of yours goes wrong.

**Will you still exist, and will we still have our data?** Backups, recovery, and getting data out if the relationship ends.

**Will you tell us when something goes wrong?** Detection, and notification obligations.

**Are you a route into us?** If you integrate with their systems, your weaknesses become theirs.

Answers that address the concern behind the question land far better than answers that address the wording. A reviewer reading "we do not have ISO 27001, and here is how access to your data is actually controlled" has learned something useful. A reviewer reading "N/A" has learned that you did not engage.

## The Questions That Actually Come Up

Prepare these and you have covered most of any questionnaire.

**Where is data stored, and in which region?** Name the providers and the region. For Dutch customers, an EU region is frequently a requirement rather than a preference.

**Who on your side can access customer data?** A number and a list of roles. "Two people, both with two-factor authentication, every access logged" is a strong answer from a company of two.

**How are customers separated from each other?** The tenancy answer: a tenant on every record, enforced in the database rather than remembered by application code, verified by testing from a second account.

**Is data encrypted in transit and at rest?** With managed providers, yes on both counts — confirm it rather than assuming, and name the mechanism.

**How do you handle authentication?** Password requirements, whether two-factor is available, session handling, and what happens on repeated failed attempts.

**What third parties process the data?** Every service that touches it, with purpose and region. Write this list once; it is also a GDPR requirement and most founders have never compiled it.

**What are your backup and recovery arrangements?** Frequency, retention, and whether you have actually restored. The honest "backups are automated daily, retained thirty days, last restore rehearsed in June and took 34 minutes" is a better answer than most enterprises give.

**How would you detect and report an incident?** Monitoring, logging, and who decides. Under GDPR a notifiable personal data breach must be reported to the supervisory authority — in the Netherlands, the Autoriteit Persoonsgegevens — without undue delay and where feasible within 72 hours, and customers will want to know how quickly you would tell them. Obligations vary with circumstances, so confirm current requirements for your case.

**Can we export our data, and what happens at termination?** Format, timescale, and deletion afterwards.

**Do you run a secure development process?** For a small team this means code review, dependency management, secrets handling and testing before release. Describe what you do; do not invent a framework.

## What You Can Honestly Say Without Certifications

Most small suppliers have no certification, and most procurement teams know that and buy anyway. What they need is evidence of deliberate practice.

You can say your infrastructure runs on providers that hold relevant certifications, and name them — that is your suppliers' compliance, not yours, and stating the distinction clearly builds credibility rather than costing it. You can describe your access controls concretely. You can point to a written access model, a retention policy, an incident procedure, and a tested restore. You can offer to sign a data processing agreement, which for a GDPR-relevant service you should have ready in any case.

What you cannot do is imply a certification you do not hold. Beyond the contractual risk, procurement teams verify, and a supplier caught overstating is finished — not just for this deal.

## The Three Answers That Kill Deals

**"I'm not sure."** Repeatedly. It reads as a product nobody has examined.

**Silence.** Three weeks of delay tells them what support will be like.

**Over-claiming.** "Fully GDPR compliant and enterprise-grade secure" is not an answer, and a reviewer reads it as someone who does not know what the words mean.

The answer that works is specific, short, and honest about gaps — with a date attached. "Two-factor authentication is not currently enforced for customer accounts; it is available for administrators and we are extending it to all users this quarter" is a perfectly acceptable answer. Procurement teams accept known gaps with plans. They reject unknown gaps.

## Prepare Once, Reuse Every Time

Build a security page — an internal document, four to six pages — covering: architecture and hosting with regions; the access model, internal and customer-facing; authentication; the subprocessor list; encryption; backup, recovery and retention; logging and monitoring; the incident process with roles and timelines; development practices; data export and deletion; and a short, honest roadmap of what you are improving.

Written once, it answers most questionnaires by copying. It shortens the sales cycle noticeably. And the act of writing it is itself the most efficient security review a small product can have, because every section you cannot complete is a gap you have just found before a customer did.

## If the Questionnaire Finds Something Real

It often does, and that is not a disaster if you handle it correctly.

Tell the customer what you found, what you are doing, and by when. Then do it. A supplier who responds to a questionnaire by fixing something within a fortnight has demonstrated exactly the behaviour procurement is trying to predict, and that impression outlasts the deal.

## The Data Processing Agreement Arrives With It

Alongside the questionnaire there is usually a contract, and founders treat it as paperwork when it is in fact a description of how the product must behave.

**You are almost certainly the processor.** Your customer decides what happens to the data and why; you process it on their instructions. That distinction determines most of the obligations, and stating it correctly in your first reply signals that you know what you are looking at.

**Subprocessors must be listed, and changes notified.** This is the same list the questionnaire asked for, and the agreement usually adds a duty to inform customers before you add a new one. That has a practical consequence: casually adding an analytics tool or a new AI provider becomes a contractual event. Knowing this in advance prevents an awkward conversation later.

**Where processing happens matters.** For personal data of EU residents, transfers outside the EEA need a valid mechanism, and the agreement will ask you to name it. If every provider you use offers an EU region, the honest and simple answer is that data stays in the EU — which is one more reason to choose regions deliberately at the start.

**Breach notification will carry a timescale.** Frequently shorter than the regulatory one, sometimes 24 hours, and it obliges you to tell the customer rather than a supervisory authority. You cannot meet a 24-hour commitment without monitoring and an error tracker somebody watches.

**Deletion and return are specified.** What happens at the end of the contract, in what format, within how many days, and when backups holding their data expire. Answer this from what your system actually does, not from what sounds reassuring.

**Audit rights are normal.** Usually satisfied by documentation rather than a visit, which is another argument for having the security document written.

Read it rather than signing it, mark anything your product cannot currently do, and negotiate those clauses instead of promising them — a supplier who asks to change a deadline from 24 to 48 hours reads as competent, while one who agrees to everything and then misses it reads as neither. Have a lawyer review the final version; the details here depend on your data and your situation, and this is a description of what to expect rather than legal advice.

## Getting Ready Before the Spreadsheet Arrives

LaunchStudio does this as a defined engagement for founders selling into Dutch businesses: the product assessed against the questions that actually get asked, the genuine gaps fixed — access model, tenant isolation, two-factor authentication, logging, backup verification, subprocessor inventory, retention and erasure — and a security document written in the language procurement teams expect, ready to send.

The engineers are Manifera's: eleven years supplying enterprise clients including Vodafone, TNO and CFLW, from Amsterdam Herengracht 420, Singapore and Ho Chi Minh City — which means the questions on that spreadsheet are ones we have answered from both sides.

[Send us the questionnaire](https://launchstudio.eu/en/#contact) and you will get an honest assessment of what you can answer today and what needs work, usually within one business day, or see the [packages](https://launchstudio.eu/en/#packages).

## Real example

### Forty-One Questions From a Hospital's Procurement Team

Femke Ravensbergen built Keuringsrapport with Lovable: inspection reporting used by technical inspection firms for lifting equipment, fire systems and electrical installations, with eleven customers around Middelburg and Vlissingen.

A regional hospital wanted to use it for internal equipment inspections — a contract worth roughly four times her largest existing customer. The demo went well. Then the questionnaire arrived: 41 questions, a data processing agreement to review, and a two-week deadline.

She could answer eleven of them.

The honest assessment took a day and found five real gaps. Customer separation relied on application-level filtering rather than database policies. There was no audit trail on inspection reports, which for equipment certification is close to a fatal objection. Backups existed and had never been restored. There was no subprocessor list, and compiling it revealed a translation service and an analytics tool she had forgotten were receiving data. And two-factor authentication was available for nobody.

Eleven business days of work: tenant isolation moved into database policies and tested from accounts at three inspection firms; an append-only audit trail added to reports, capturing every change with actor and timestamp, which the hospital later cited as the feature that decided it; two-factor authentication implemented for all users and enforced for administrators; a restore performed and timed at 22 minutes, then scheduled quarterly; the analytics tool removed and the translation service replaced with one offering an EU region and a data processing agreement; retention and erasure implemented; and a six-page security document written covering all 41 questions, with three gaps stated openly alongside dates.

**Result:** the contract was signed six weeks later. The hospital's reviewer commented that the audit trail and the willingness to name unfinished items were what moved the file forward. Femke has since sent the same document to four prospects without changes and reports that two of them skipped the questionnaire entirely.

> *"Forty-one questions arrived and I could answer eleven. The document I wrote to fix that has since won me two contracts I never had to fill in a spreadsheet for."*
> — **Femke Ravensbergen, Founder, Keuringsrapport (Middelburg)**

**Cost & Timeline:** €5,200 (tenant isolation in policies, audit trail, two-factor authentication, restore verification, subprocessor cleanup, retention and erasure, security documentation) — completed in 11 business days.

## Frequently Asked Questions

### Can I win enterprise deals without a security certification?

Frequently, yes. Procurement teams know small suppliers rarely hold certifications; what they need is evidence of deliberate practice — a documented access model, tested backups, a subprocessor list, an incident process, and honest answers.

### What should I never write in a questionnaire?

Anything implying a certification you do not hold, blanket claims such as "fully compliant", or repeated "not sure" answers. Reviewers verify, and an overstatement discovered ends more than the current deal.

### How do I answer a question where the answer is bad?

State the gap, state the plan, state the date. Known gaps with plans are routinely accepted; unknown gaps are not, because they suggest nobody has examined the product.

### What is the subprocessor list and why do I need one?

Every third party that processes customer data — hosting, database, email, analytics, any AI provider — with purpose and region. Customers ask for it, GDPR expects it, and compiling it usually surfaces services founders had forgotten were receiving data.

### Is there a way to avoid answering a questionnaire every time?

Write a four-to-six page security document once, covering architecture, access, authentication, subprocessors, backups, logging, incidents, development practice and data export. Most questionnaires can then be answered by copying, and some customers accept it instead.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Can I win enterprise deals without a security certification?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Often yes. Reviewers expect small suppliers to lack certifications and look instead for a documented access model, tested backups, a subprocessor list and honest answers."
      }
    },
    {
      "@type": "Question",
      "name": "What should I never write in a questionnaire?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Anything implying a certification you do not hold, blanket claims like 'fully compliant', or repeated 'not sure' answers."
      }
    },
    {
      "@type": "Question",
      "name": "How do I answer a question where the answer is bad?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "State the gap, the plan and the date. Known gaps with plans are accepted; unknown gaps suggest nobody has examined the product."
      }
    },
    {
      "@type": "Question",
      "name": "What is the subprocessor list and why do I need one?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Every third party processing customer data, with purpose and region. Customers ask for it, GDPR expects it, and compiling it surfaces forgotten services."
      }
    },
    {
      "@type": "Question",
      "name": "Is there a way to avoid answering a questionnaire every time?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Write a four-to-six page security document once; most questionnaires can then be answered by copying, and some customers accept it instead."
      }
    }
  ]
}
</script>
