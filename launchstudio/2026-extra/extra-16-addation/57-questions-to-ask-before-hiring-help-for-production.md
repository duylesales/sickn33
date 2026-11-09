---
Title: "Questions to Ask Before Hiring Help for Production"
Keywords: questions to ask developer before hiring, production readiness questions, interview agency for app launch, what to ask software partner, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: AI-Native Founder (Non-Technical)
---

# Questions to Ask Before Hiring Help for Production

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Questions to Ask Before Hiring Help for Production",
  "description": "A structured list of questions non-technical founders can ask any freelancer, agency or service before hiring them to make an app built with Lovable, Bolt, v0, Cursor or Claude Code production ready. Questions are grouped by experience, security, payments, data, deployment, ownership, process, cost and support, each with what a good answer sounds like and what should worry you.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-09-21",
  "inLanguage": "en",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/questions-to-ask-before-hiring-help-for-production" },
  "citation": [
    { "@type": "CreativeWork", "name": "OWASP Top 10", "url": "https://owasp.org/www-project-top-ten/" },
    { "@type": "CreativeWork", "name": "Supabase: Production checklist", "url": "https://supabase.com/docs/guides/deployment/going-into-prod" },
    { "@type": "CreativeWork", "name": "Stripe: Webhooks", "url": "https://docs.stripe.com/webhooks" },
    { "@type": "CreativeWork", "name": "Google SRE Book: Monitoring Distributed Systems", "url": "https://sre.google/sre-book/monitoring-distributed-systems/" }
  ]
}
</script>

**Short answer:** Before hiring anyone to make your AI-built app production ready, ask how they will test that users cannot see each other's data, how payments will be confirmed, where your code and accounts will live, what you will receive in writing, what is excluded, what happens if they find something unexpected and what support you get after launch. Good answers are specific and concrete; vague answers or jargon you cannot follow are a warning sign. The full list below covers nine areas, with what good answers sound like.

You do not need technical knowledge to evaluate technical help. You need the right questions and a sense of what good answers sound like. Experienced suppliers answer these questions easily, often before you ask. Inexperienced ones struggle or change the subject. Use this list in your first calls and send the most important questions in writing so you can compare answers.

## Key Takeaways

- **Ask the same questions to everyone** so answers can be compared.
- **Specific answers indicate experience;** generic reassurance does not.
- **Ownership and access questions** protect you most if things go wrong.
- **Ask about after launch,** not only about the project itself.
- **Get key answers in writing,** ideally reflected in the quote.

## 1. Experience

**"Have you worked on apps built with Lovable, Bolt, v0, Cursor or Claude Code before?"**
Good answer: examples of similar apps and the typical issues they found. Worrying answer: "Code is code" without any specifics.

**"What problems do you usually find in apps like mine?"**
Good answer: concrete patterns such as loose database policies, keys in the browser, payments on success pages or public storage. Worrying answer: "It depends" with nothing further.

**"Can I speak to two founders you have helped?"**
Good answer: yes, with contacts. Worrying answer: refusal or only anonymous testimonials.

## 2. Security and Data Access

**"How will you test that one user cannot see or change another user's data?"**
Good answer: testing with several accounts in different roles and organisations, reviewing database policies against your business rules and adding automated tests. Worrying answer: "We use secure frameworks" or "Supabase handles that".

**"What will you do with keys or secrets you find in the code?"**
Good answer: move them to server-side environment variables and rotate any that were exposed. Worrying answer: only "remove them from the code".

**"If you hit a permission error, how do you fix it?"**
Good answer: understand why the rule blocks the request and adjust it correctly. Worrying answer: disabling the rule or using a key that bypasses it.

## 3. Payments

**"How will the app know that a customer actually paid?"**
Good answer: verified webhooks from the payment provider, processed only once, with access updated from those events. Worrying answer: "When they reach the success page".

**"What happens when a renewal fails or a refund is issued?"**
Good answer: a description of how access changes and how customers are informed. Worrying answer: uncertainty or "we will look at that later".

**"Will you check past payments for mistakes?"**
Good answer: offering a reconciliation between provider records and your database if issues are found. Worrying answer: no idea what reconciliation means.

## 4. Data and Privacy

**"Where will our data be hosted?"**
Good answer: a specific provider and region, with reasons, and EU hosting options where needed. Worrying answer: "In the cloud".

**"Will you handle personal data, and will you sign a processing agreement?"**
Good answer: yes, with a clear description of access and safeguards. Worrying answer: unfamiliarity with the concept.

**"Can users export or delete their data?"**
Good answer: either it is in scope, or they explain what would be needed. Worrying answer: "Just delete them in the dashboard".

## 5. Deployment and Operations

**"Will there be a staging environment separate from production?"**
Good answer: yes, with its own database and keys. Worrying answer: "We test carefully in production".

**"How are database changes made and tracked?"**
Good answer: migrations stored in the repository and applied through a pipeline. Worrying answer: "We change it in the dashboard".

**"How will we know if the app goes down or errors increase?"**
Good answer: uptime monitoring and error tracking with alerts to you. Worrying answer: "Customers will tell you".

**"Have you tested restoring a backup?"**
Good answer: a restore test is part of the work. Worrying answer: "Backups are automatic".

**"How do we roll back a bad release?"**
Good answer: a documented, quick procedure. Worrying answer: "We fix forward".

## 6. Ownership and Access

**"In whose name will the code, database, hosting and domain be?"**
Good answer: yours, with their access invited to your accounts. Worrying answer: "We will set it up in ours for convenience".

**"What access do you need, and how will it be removed afterwards?"**
Good answer: a list of services and roles, and removal on request at the end. Worrying answer: asking for your personal passwords.

**"Will I be able to continue with my AI tool, or another developer, afterwards?"**
Good answer: yes, with documentation and instructions for the tool. Worrying answer: suggestions that only they can maintain it.

## 7. Process and Communication

**"How often will I get updates, and in what form?"**
Good answer: a regular rhythm of short written updates. Worrying answer: "We will let you know when it is done".

**"Who is my contact, and who does the work?"**
Good answer: named people and what happens if they are unavailable. Worrying answer: unclear.

**"Will the app look different afterwards?"**
Good answer: no, unless agreed. Worrying answer: plans to redesign without asking.

**"What do you need from me, and when?"**
Good answer: a clear list such as access, decisions and testing time. Worrying answer: nothing, which usually means assumptions.

## 8. Cost and Scope

**"Is the price fixed or an estimate?"**
Good answer: clear statement, with how changes are handled. Worrying answer: vague.

**"What exactly is included, and what is excluded?"**
Good answer: a written list of both. Worrying answer: "Everything you need".

**"What happens if you find something unexpected?"**
Good answer: they tell you first, propose options and nothing extra is done without approval. Worrying answer: "We will sort it out".

**"Are hosting and provider costs included or separate?"**
Good answer: separate, billed directly to you. Worrying answer: bundled without explanation.

## 9. After Launch

**"What support is included after launch?"**
Good answer: a defined period, what it covers and how to reach them. Worrying answer: none, or undefined.

**"If something you built breaks a month later, who pays?"**
Good answer: issues caused by their work are fixed. Worrying answer: everything after delivery is new work.

**"What ongoing options do you offer?"**
Good answer: clear options with prices. Worrying answer: only expensive retainers.

**"What will I receive in writing at the end?"**
Good answer: a summary of what was done, an account inventory, documentation and instructions for your AI tool. Worrying answer: "The code".

## How to Use These Questions

You do not need to ask all of them in one call. A practical approach:

1. **First call:** ask the experience, security and ownership questions. They filter out unsuitable suppliers fastest.
2. **After receiving a quote:** ask the cost, scope and after-launch questions in writing.
3. **Before signing:** confirm that the key answers are reflected in the quote or contract.

Keep notes and compare the answers side by side. Patterns appear quickly.

## Listening for the Quality of Answers

Beyond the content, notice how suppliers answer. Do they explain in plain language, or hide behind jargon? Do they admit uncertainty when appropriate? Do they ask you questions back to understand your situation? Do they mention risks you had not considered? The best suppliers often teach you something in the first call, and they are comfortable saying "that is not something we do, but here is who could help".

## Questions Suppliers Should Ask You

A good supplier will also ask you questions. Expect questions about your users and roles, what data the app stores, how you charge, which tools and services you use, your launch date, any customer requirements, problems you have noticed and how you plan to keep building. If a supplier asks none of these and still gives you a price, the price is likely a guess.

## Questions for Specific Situations

Some situations deserve extra questions. If you handle health, financial or children's data, ask how the supplier has handled such data before and which additional measures they would take. If you sell to larger businesses, ask whether they can support security questionnaires and features such as single sign-on. If your app includes AI features, ask how they control costs per user, which data is sent to model providers and how they prevent the AI from accessing data a user is not allowed to see. If you have a hard deadline, ask what they would cut first if time runs short, which reveals how they think about priorities.

## Comparing Answers Across Suppliers

After two or three conversations, put the answers in a simple table with one row per question and one column per supplier. Mark each answer as specific, partial or vague. The pattern is usually clear: one supplier gives specific answers across almost every area, others are strong in a few and vague elsewhere. Combine that with the quotes, the scope and your sense of who understood your app best. Price matters, but the quality of answers tells you more about how the project will go when something unexpected happens.

## Keep the List for Later

These questions remain useful after you hire someone. Revisit them before each new project, when a supplier changes team members or when your app enters a new phase such as payments, enterprise customers or AI features. Answers that were fine for a prototype may not be enough for a product with paying customers.

## What We Need From You

- A 15-minute intro call, where you are welcome to ask all of these questions
- Read access to your code and configuration for the quote

Use the [price calculator](https://launchstudio.eu/en/#calculator) for an indication.

## Price Overview

| Package | Price |
| --- | --- |
| Launch Ready | €800-€3,500 fixed, including 48 hours of post-launch support |
| Launch & Grow | €2,500-€7,500 fixed, plus €49 per month for ongoing care |

## Why Founders Choose LaunchStudio

LaunchStudio is backed by Manifera, a software development company with 11+ years of experience, 160+ delivered projects and 120+ engineers, working for clients such as Vodafone and TNO. Founders meet the team at Herengracht 420 in Amsterdam; engineering happens at Manifera's development centre on Pho Quang Street in Ho Chi Minh City, with a hub on Tras Street in Singapore. We welcome these questions and answer them in writing in every quote.

## Real example

### An AI-Native Founder in Action: Twelve Questions, One Clear Choice

Hidde Sterk runs a SaaS for tutoring agencies from Groningen, built with v0, Cursor and Supabase, where agencies match students with tutors, schedule lessons and invoice parents through Stripe. Before a growth push, he wanted help making the app production ready and spoke to four suppliers. He picked twelve questions from a list like this one and asked each supplier the same questions, noting the answers in a spreadsheet.

Two suppliers could not explain how they would test access between agencies, and one suggested "turning off the strict security" to fix a permission error Hidde mentioned. A third answered most questions well but planned to host everything in its own account. LaunchStudio answered all twelve specifically, described testing with agency, tutor and parent accounts, explained webhook verification and reconciliation and confirmed in the quote that everything would stay in Hidde's accounts.

The project, quoted at €3,100 within Launch Ready, found that parents could see other families' lesson notes through a shared view, that Stripe invoices were marked paid on redirect and that the Supabase project was on a co-founder's personal account. All were fixed, with tests, staging and monitoring added.

**Result:** Hidde onboarded twelve new tutoring agencies over the following quarter. He shared his question spreadsheet with two founder friends, who used it for their own hiring decisions.

> *"I could not judge code, but I could judge answers. The same twelve questions made the differences between suppliers obvious within a week."*
> - **Hidde Sterk, Founder, Bijlesplanner (Groningen)**

**Cost & Timeline:** €3,100 (Launch Ready package: role-based policies with tests, secured view, Stripe webhooks, ownership transfer, staging and monitoring) - completed in 8 business days.

## Frequently Asked Questions

### What is the most important question to ask before hiring production help?

"How will you test that one user cannot see or change another user's data?" It reveals experience with the most common serious issue in AI-built apps. A specific answer about testing with several roles and reviewing database policies is a strong sign.

### How many suppliers should I talk to?

Usually two to four. Fewer gives you little to compare; more takes time without adding much. Ask all of them the same questions and compare the answers in a simple table.

### What if I do not understand the answers?

Ask the supplier to explain in plain language. Good suppliers can. If they cannot or will not, that is a signal in itself. You can also ask a technical friend to listen in or read written answers.

### How does Manifera's experience show in these answers?

Manifera has 11+ years of experience, 160+ delivered projects and 120+ engineers, working for clients such as Vodafone and TNO. LaunchStudio's answers to these questions, about testing, payments, ownership and support, reflect practices used across that work.

### Should I ask about SEO and AI visibility?

Yes, briefly. Ask whether the work includes a custom domain, HTTPS, correct redirects, fast public pages and monitoring. These form the technical base that search engines and AI answer engines rely on when reading and citing your site.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What is the most important question to ask before hiring production help?",
      "acceptedAnswer": { "@type": "Answer", "text": "How they will test that one user cannot see or change another user's data." }
    },
    {
      "@type": "Question",
      "name": "How many suppliers should I talk to?",
      "acceptedAnswer": { "@type": "Answer", "text": "Usually two to four, with the same questions for all." }
    },
    {
      "@type": "Question",
      "name": "What if I do not understand the answers?",
      "acceptedAnswer": { "@type": "Answer", "text": "Ask for plain language; inability to explain is a signal." }
    },
    {
      "@type": "Question",
      "name": "How does Manifera's experience show in these answers?",
      "acceptedAnswer": { "@type": "Answer", "text": "LaunchStudio's answers reflect practices from Manifera's 11+ years and 160+ projects." }
    },
    {
      "@type": "Question",
      "name": "Should I ask about SEO and AI visibility?",
      "acceptedAnswer": { "@type": "Answer", "text": "Yes; ask about domain, HTTPS, redirects, fast pages and monitoring." }
    }
  ]
}
</script>
