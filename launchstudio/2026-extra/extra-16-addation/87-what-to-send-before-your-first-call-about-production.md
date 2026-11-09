---
Title: "What to Send Before Your First Call About Production"
Keywords: prepare for developer call, what to send agency before quote, production readiness intro call, app brief for quote, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: AI-Native Founder (Non-Technical)
---

# What to Send Before Your First Call About Production

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "What to Send Before Your First Call About Production",
  "description": "A preparation guide for founders before an intro call about making an app built with Lovable, Bolt, v0, Cursor or Claude Code production ready: the one-page app summary, list of tools and services, user types and permissions, payments, data, known problems, deadlines and customer requirements, how to share access safely, what not to send and how preparation leads to a faster, more accurate fixed quote.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-10-21",
  "inLanguage": "en",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/what-to-send-before-your-first-call-about-production" },
  "citation": [
    { "@type": "CreativeWork", "name": "GitHub: Inviting collaborators to a personal repository", "url": "https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-personal-account-on-github/managing-access-to-your-personal-repositories/inviting-collaborators-to-a-personal-repository" },
    { "@type": "CreativeWork", "name": "Supabase: Access control for organisations", "url": "https://supabase.com/docs/guides/platform/access-control" },
    { "@type": "CreativeWork", "name": "Vercel: Team members and roles", "url": "https://vercel.com/docs/rbac/access-roles" },
    { "@type": "CreativeWork", "name": "OWASP: Secrets Management Cheat Sheet", "url": "https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html" }
  ]
}
</script>

**Short answer:** Before your first call about making your app production ready, send a one-page summary of what the app does, a list of the tools and services it uses, the types of users and what each may see, whether it takes payments or stores sensitive data, any problems you have noticed, your deadline and any requirements from customers. If you can, also share read access to the code. Do not send passwords or secret keys by email. With this information, the intro call takes 15 minutes and the fixed quote follows quickly and accurately.

Founders sometimes postpone contacting a development partner because they feel they need to "prepare properly" or understand the technical details first. You do not. What helps most is simple information about your app and your business, which only you have. This page lists what to send, why it matters and what to leave out.

## Key Takeaways

- **A one-page summary** in your own words is the most useful thing you can send.
- **A list of tools and services** shows where the app lives and who owns what.
- **User types and permissions** reveal the biggest security questions.
- **Known problems and deadlines** shape priorities and the timeline.
- **Never send passwords or secret keys;** invite people to accounts instead.

## 1. A One-Page Summary of Your App

Write a few paragraphs, as if explaining your app to a smart friend:

- What does the app do, and for whom?
- How long has it been live, and how many users or customers does it have?
- What is the main journey a user goes through?
- What is coming next: new customers, a launch, an investor demo?

You do not need technical terms. "Gyms use it to schedule classes, members book and pay, trainers see their own classes" tells us more than a list of frameworks.

## 2. Tools and Services

List everything the app uses, as far as you know:

| Category | Examples |
| --- | --- |
| AI building tools | Lovable, Bolt, v0, Cursor, Claude Code |
| Code | GitHub repository, or code only inside the builder |
| Database and authentication | Supabase, Firebase, Neon, Clerk |
| Hosting | Vercel, Netlify, the builder's own hosting |
| Payments | Stripe, Mollie |
| Email | Resend, Postmark, Brevo, the database provider's default email |
| AI providers | OpenAI, Anthropic, Google, Mistral |
| Integrations | Exact Online, HubSpot, Google Calendar, Shopify |
| Domain | Registrar and who registered it |
| Other | Analytics, error tracking, file storage, SMS |

For each, note whose account it is in: yours, your company's, a co-founder's, a freelancer's. Ownership questions are among the most important things we check, and knowing them early saves days.

## 3. User Types and What Each May See

Describe the types of users and their permissions in plain language, for example:

- "Customers see only their own orders and invoices."
- "Staff at a customer company see their company's orders; only finance sees invoices."
- "Our support team sees all customers but cannot change payments."
- "Admins can do everything."

This description is what we test against when we review database access. The most serious problems in AI-built apps are usually differences between what founders think users can see and what the app actually allows.

## 4. Payments

If the app takes money, describe how: one-time payments, subscriptions, deposits, marketplaces with payouts. Which provider, which payment methods, which plans? Have customers ever paid without getting access, or received access without paying? Any such story is valuable.

## 5. Data

What kind of data does the app store? Names and emails only, or also addresses, documents, health information, financial data, children's data, employee data? Where do you think it is hosted? Have customers asked about data location or sent a processing agreement? Sensitive data changes the scope and is better known early.

## 6. Known Problems

List anything that worries you or has gone wrong: slow pages, emails in spam, a test account that saw someone else's data, payments that went wrong, errors after a certain change, features you are afraid to touch. Even vague feelings help, such as "I am not sure the admin page is protected". Nothing you mention will surprise us; these are the problems we fix every week.

## 7. Deadlines and Constraints

Is there a date that matters: a launch, a trade fair, a customer pilot, an investor demo, the start of a school year? Is there a budget range you need to stay within? Are there periods when the app must not change, such as a busy season? Deadlines shape how we plan and what we prioritise.

## 8. Customer or Investor Requirements

If a customer has sent a security questionnaire, a processing agreement, accessibility requirements or a request for SSO, include it. If an investor asked technical due diligence questions, include those. These documents often define the scope more precisely than anything else.

## 9. Access, Shared Safely

If you are comfortable, give us read access before the call, so we can take a short look and quote accurately:

- **GitHub:** invite us as a collaborator with read access to the repository
- **Builder:** some builders allow inviting collaborators or sharing a project link
- **Supabase, Vercel and others:** invite us with a read-only or developer role if available

If you are not ready to share access yet, that is fine. We can start with a screen share during the call and a description of your setup.

## What Not to Send

- **Passwords** for any account
- **Secret keys** such as Supabase service role keys, Stripe secret keys or API tokens
- **Exports of customer data** or database dumps
- **Screenshots containing personal data** of your customers

If you have already shared a secret somewhere, such as in a chat or email, mention it; we will help rotate it as one of the first steps.

## A Simple Template

You can copy this and fill it in:

1. App name and one-sentence description
2. Users and customers today, and expected in six months
3. Tools and services used, and whose account each is in
4. User types and what each may see and do
5. Payments: provider, model and any problems
6. Data: types of personal or sensitive data
7. Known problems or worries
8. Deadline and why it matters
9. Customer or investor requirements, attached if available
10. Access you can share before the call

Sending this usually takes 20 to 30 minutes and makes the call much more useful.

## What Happens in the Call

The intro call takes about 15 minutes. We confirm what you sent, ask a few follow-up questions, explain what we would look at and whether Launch Ready or Launch & Grow is likely to fit and agree the next step: usually a short look at the project with read access, followed by a written fixed quote within one or two business days. If your app does not need us, or needs something we do not do, we say so.

## Why Preparation Leads to Better Quotes

Fixed prices depend on accurate assumptions. When we know your tools, users, payments, data and problems in advance, the quote can name specific scope items, such as "rewrite policies for the eleven tables holding customer data, tested with customer, staff and admin accounts", rather than general statements. That makes the price more reliable, reduces surprises during the project and makes the quote easier to compare with others.

## If You Do Not Know the Answers

Many founders do not know where their database is hosted, whether policies exist or who registered the domain. That is normal, especially if a freelancer helped at the start or the AI tool set things up. Write "not sure" and move on. Finding out is part of our work, and the account inventory we create will answer these questions for good.

## Sharing With Other Suppliers

The same preparation works for any supplier. If you are comparing several, send each the same summary and access, so their quotes are based on the same information. That makes quotes far easier to compare and reveals which suppliers actually looked at your app.

## Questions You Might Want to Ask Us

The intro call is also your chance to evaluate us. Useful questions include: how will you test that users cannot see each other's data, who will work on the project, where will the accounts live, what will I receive at the end, what happens if you find something unexpected and what support do I get after launch? We are happy to answer these, and the answers will appear in writing in the quote.

## After the Call

Within one or two business days of the call and the short look at your project, you receive a written quote with scope, assumptions, exclusions, timeline and fixed price. There is no obligation. If you decide to go ahead, we agree a start date and send a short list of accounts to invite us to. If you decide not to, you still have a clearer picture of your app's risks than before.

## Price Reference

| Package | Price |
| --- | --- |
| Launch Ready | €800-€3,500 fixed, including 48 hours of post-launch support |
| Launch & Grow | €2,500-€7,500 fixed, plus €49 per month for ongoing care |

Use the [price calculator](https://launchstudio.eu/en/#calculator) for an indication before the call.

## Screenshots and Short Recordings

If something is easier to show than to describe, a few screenshots or a two-minute screen recording of the main journey help a lot: how a new user signs up, what an admin sees, where a problem appears. Make sure no customer personal data is visible, or use a test account. A short walkthrough recorded on your phone is often more useful than a long written explanation.

## Language and Format

Send the information in English or Dutch, whichever is easier for you. A document, an email or even a voice memo transcript works. Completeness matters more than polish.

## Why Founders Choose LaunchStudio

LaunchStudio is backed by Manifera, a software development company with 11+ years of experience, 160+ delivered projects and 120+ engineers, working for clients such as Vodafone and TNO. Founders meet the team at Herengracht 420 in Amsterdam; engineering happens at Manifera's development centre on Pho Quang Street in Ho Chi Minh City, with a hub on Tras Street in Singapore. A short, honest description of your app is all we need to start.

## Real example

### An AI-Native Founder in Action: Twenty Minutes of Preparation, a Quote Next Day

Nadia Bouzid runs a SaaS for interpreters and translation agencies from Rotterdam, built with Bolt and Supabase, where agencies assign interpreting jobs, interpreters accept them and invoices are generated monthly. Before her first call with LaunchStudio, she filled in the template in about twenty minutes. She listed Bolt, Supabase, Netlify, Mollie and Postmark, noted that the Supabase project had been created by a freelancer who helped her early on and wrote that interpreters should see only their own jobs and rates, while agencies should see their own interpreters and invoices.

Under known problems, she wrote: "Once an interpreter told me she could see another interpreter's hourly rate. I think I fixed it with a prompt but I am not sure." She attached a security questionnaire from a hospital interpreting service and mentioned a pilot starting in five weeks. She invited LaunchStudio to the GitHub repository with read access.

The intro call took fifteen minutes. The short look confirmed that the earlier fix had hidden the rate in the interface but left it readable through the API, and that the Supabase project was still in the freelancer's account. The written quote, €3,100 within Launch Ready, arrived the next morning with eighteen specific scope items, including the ownership transfer, policies for agencies and interpreters with tests and support for the hospital's questionnaire.

**Result:** The project started three days later and finished a week before the pilot. The hospital accepted the questionnaire answers, and Nadia said the preparation made her feel in control from the first conversation.

> *"I thought I needed to understand my app technically before calling anyone. I only needed to describe it honestly. The technical part was their job."*
> - **Nadia Bouzid, Founder, Tolkplanner (Rotterdam)**

**Cost & Timeline:** €3,100 (Launch Ready package: ownership transfer, role-based policies with tests, payment and email checks, questionnaire support and production setup) - quote within one business day, project completed in 8 business days.

## Frequently Asked Questions

### What should I prepare before a call about making my app production ready?

A short summary of the app, a list of tools and services with account ownership, user types and permissions, payment details, types of data, known problems, deadlines and any customer or investor requirements. Read access to the code helps but is optional.

### Should I share passwords or keys before the call?

No. Never send passwords or secret keys by email or chat. Invite us to accounts with our own logins and appropriate roles. If a secret was shared before, mention it and we will help rotate it.

### What if I do not know which services my app uses?

Write down what you know and mark the rest as unsure. Finding out is part of our work, and the account inventory we create during the project will answer these questions permanently.

### How does Manifera's experience make the first call efficient?

Manifera has scoped and delivered 160+ projects over 11+ years with 120+ engineers, for clients such as Vodafone and TNO. LaunchStudio knows which questions matter for AI-built apps, so a short, well-prepared call is enough for an accurate quote.

### Should I mention SEO or visibility goals?

Yes, briefly. If public pages, search rankings or how AI answer engines describe your product matter to you, mention it. The production setup covers the technical basics, and knowing your goals helps us prioritise public page performance and metadata.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What should I prepare before a call about making my app production ready?",
      "acceptedAnswer": { "@type": "Answer", "text": "A summary, tools and ownership, user types, payments, data, problems, deadlines and requirements." }
    },
    {
      "@type": "Question",
      "name": "Should I share passwords or keys before the call?",
      "acceptedAnswer": { "@type": "Answer", "text": "No; invite us to accounts and rotate any previously shared secrets." }
    },
    {
      "@type": "Question",
      "name": "What if I do not know which services my app uses?",
      "acceptedAnswer": { "@type": "Answer", "text": "Mark it as unsure; finding out is part of the work." }
    },
    {
      "@type": "Question",
      "name": "How does Manifera's experience make the first call efficient?",
      "acceptedAnswer": { "@type": "Answer", "text": "Experience from 160+ projects means a short prepared call is enough for an accurate quote." }
    },
    {
      "@type": "Question",
      "name": "Should I mention SEO or visibility goals?",
      "acceptedAnswer": { "@type": "Answer", "text": "Yes briefly, so public page priorities can be set." }
    }
  ]
}
</script>
