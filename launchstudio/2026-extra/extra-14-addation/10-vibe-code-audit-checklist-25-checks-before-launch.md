---
Title: "Vibe Code Audit Checklist: 25 Checks Before You Launch"
Keywords: vibe code audit checklist, ai code audit checklist, launch checklist ai app, vibe code audit, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: AI-Native Founder (Non-Technical)
---

# Vibe Code Audit Checklist: 25 Checks Before You Launch

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Vibe Code Audit Checklist: 25 Checks Before You Launch",
  "description": "A practical vibe code audit checklist for founders who built with Lovable, Bolt, Cursor, v0 or Replit. Twenty-five checks across accounts, data, keys, payments, privacy and operations, most of which need no coding knowledge.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-01-18",
  "inLanguage": "en",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/vibe-code-audit-checklist-25-checks-before-launch" },
  "citation": [
    { "@type": "CreativeWork", "name": "OWASP Top 10 2021: A01 Broken Access Control", "url": "https://owasp.org/Top10/A01_2021-Broken_Access_Control/" },
    { "@type": "CreativeWork", "name": "OWASP Secrets Management Cheat Sheet", "url": "https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html" },
    { "@type": "CreativeWork", "name": "Verizon Data Breach Investigations Report", "url": "https://www.verizon.com/business/resources/reports/dbir/" },
    { "@type": "CreativeWork", "name": "Google SRE Book: Monitoring Distributed Systems", "url": "https://sre.google/sre-book/monitoring-distributed-systems/" },
    { "@type": "CreativeWork", "name": "GDPR Article 32", "url": "https://gdpr-info.eu/art-32-gdpr/" }
  ]
}
</script>

Eighty percent of AI-built projects never reach production. Many of the ones that do launch with avoidable problems, simply because nobody went through a list. This vibe code audit checklist is that list: 25 checks you can run before launch, most of them without reading code. Where a check needs technical help, we say so.

Print it, open your app in a second window and go through it in one sitting. It takes about two hours.

## Key Takeaways

- **Twenty-five checks, about two hours, mostly without code.** The checklist covers accounts, data access, keys, payments, privacy and operations.
- **Checks 5-10 and 13-16 are launch blockers.** Failures there can expose other people's data or let users get paid features for free.
- **Access control deserves the most attention.** It has been the top web application risk in the OWASP Top 10 since 2021, and it is where AI-generated apps fail most often.
- **Operations count as security.** The Verizon Data Breach Investigations Report repeatedly links most breaches to human elements such as errors and misused credentials, which is why account hygiene and two-factor authentication open the list.
- **Repeat the checklist** before launch, after large AI-generated features and at least quarterly.

## Accounts and Ownership

1. **Every account is yours.** Domain, hosting, database, payment provider, email provider and GitHub are registered to a company email address you control, not a freelancer's or a personal one you might lose.
2. **Two-factor authentication is on** for every account in check 1.
3. **At least two people can log in** to the critical accounts, or you have a documented recovery route if you are unavailable.
4. **Your code is in a repository you own.** If your AI tool disappeared tomorrow, you would still have the code.

## Data and Access

5. **Two test users, two different results.** Create two accounts. Log in as each. Neither should see the other's data anywhere, including search, exports and notifications.
6. **Changing an ID in the address bar does nothing bad.** Open a record, change the number or code in the URL to another one. You should see an error, not someone else's record.
7. **Row Level Security is enabled on every table** (Supabase users). In the dashboard, every table should show RLS as enabled. *Technical help recommended to verify the policies themselves.*
8. **Admin pages are protected on the server.** Log in as a normal user and type the admin URL directly. You should be refused, not shown an empty admin page.
9. **Uploaded files are private.** Upload a file, copy its link, open it in a private browser window. It should not open without login, or the link should expire.

## Keys and Secrets

10. **No secret keys in the browser.** In your browser, view the page source and search for `sk_live`, `service_role`, `secret` and the names of your providers. Publishable keys are fine; secret keys are not. *Technical help recommended if anything appears.*
11. **No secrets in your repository history.** Ask your AI tool or a developer to scan git history for keys. A key deleted from a file still exists in old commits.
12. **Any exposed key has been rotated.** If a secret was ever visible, generate a new one and revoke the old one.

## Payments

13. **A live payment upgrades the account without the success page.** Pay, then close the browser before the redirect finishes. The account should still upgrade, because the webhook does the work.
14. **Paying twice by double clicking charges once.**
15. **A failed or cancelled payment does not grant access.**
16. **Prices come from the server.** A user should not be able to change the amount by editing the request. *Technical help recommended to verify.*

## Privacy and the EU

17. **You know where your data lives.** Database, file storage, email provider and analytics, each with a country or region. For EU users, EU regions are strongly preferred.
18. **You have processor agreements** with the services that handle your users' personal data.
19. **A user can delete their account,** and you know what happens to their data when they do.
20. **Your privacy statement matches reality.** It lists the services you actually use.

## Operations

21. **You would know within ten minutes if the app went down,** through an uptime monitor that alerts your phone.
22. **Errors are tracked.** A tool such as Sentry or your host's logs captures errors with enough detail to fix them.
23. **Backups exist and you have restored one** into a test environment at least once.
24. **Changes go to staging before production,** so a bad prompt does not reach customers.
25. **You have written down how to roll back** the last release.

## Scoring Your Result

| Checks passed | What it means |
| --- | --- |
| 23-25 | Ready to launch, with normal caution |
| 18-22 | Launch possible after fixing the failed items, especially in Data and Keys |
| 12-17 | Not ready. Prioritise Data and Access, Keys and Payments |
| Under 12 | The app is still a prototype. Plan a production phase before inviting customers |

Any failure in checks 5-10 or 13-16 should be treated as a launch blocker regardless of your total.

## Why a Checklist Works for AI-Built Apps

Checklists are a proven tool in fields where experts are fallible under time pressure, from aviation to surgery. Software launches share that profile: many small steps, each easy to forget, any one of which can cause an incident. AI-built apps add a further reason. The builder generates working features quickly, but it does not remind you of what it did not do. A checklist is that reminder.

The list is ordered deliberately. Accounts come first because they determine whether you can act at all during an incident. Data access and keys come next because they carry the highest impact. Payments follow because they combine money and trust. Privacy and operations close the list because they determine how bad an incident becomes and how fast you recover.

## How the Checks Map to Recognised Standards

Each section of the checklist corresponds to established guidance, so passing it is not an arbitrary exercise:

| Checklist section | Related standard or guidance |
| --- | --- |
| Accounts and ownership | Verizon DBIR findings on credential misuse; MFA best practice |
| Data and access | OWASP Top 10 A01 Broken Access Control; OWASP Authorization Cheat Sheet |
| Keys and secrets | OWASP Secrets Management Cheat Sheet |
| Payments | Payment provider guidance on webhooks and idempotency |
| Privacy and the EU | GDPR Articles 5, 17, 28 and 32 |
| Operations | Google SRE guidance on monitoring; tested backups |

For a founder, the practical point is that passing the checklist gives you language and evidence for customer questionnaires, investor questions and your own peace of mind.

## Common Ways Founders Misread the Results

- **"I passed check 7, so RLS is fine."** Check 7 only confirms RLS is enabled. The policies themselves can still allow too much; checks 5 and 6 test that in practice.
- **"My keys are in environment variables, so they are secret."** Variables prefixed for the frontend, such as `VITE_` or `NEXT_PUBLIC_`, are bundled into browser code. Only server-side variables are secret.
- **"Backups are on, so check 23 passes."** The check requires a restore you have actually performed. Untested backups regularly fail when needed.
- **"Nobody would try that."** Most automated attacks are not personal; bots try common paths and IDs on every site they find.

## Turning Results Into a Plan

Score yourself, then sort failures into three groups: launch blockers (data, keys, payments), first-week items (monitoring, backups, staging) and first-month items (documentation, retention, processor agreements). Fix the first group before inviting customers, schedule the second immediately after, and put the third on a calendar. If the first group is long or you cannot verify your fixes, that is the moment to bring in a reviewer rather than continuing to prompt.

## Making the Checklist a Habit

The most valuable use of this list is not a single pass before launch. It is a short routine after each significant change. Many founders keep a copy in their repository and tick it in the pull request that ships a large feature. Over time, the routine becomes quicker, the findings become rarer, and the app becomes easier to defend in front of customers, investors and regulators.

## What This Checklist Does Not Cover

No founder checklist replaces a technical review, and it is worth being explicit about the limits. The list does not verify the logic inside every database policy, test for injection vulnerabilities in custom queries, review third-party dependencies for known vulnerabilities, assess performance under load, or evaluate whether your AI features could be manipulated through prompt injection. It also cannot tell you whether your privacy statement is legally sufficient. Those questions belong to an engineer and, for legal texts, a privacy lawyer.

What the checklist does well is catch the most common and most damaging gaps quickly, and give you a clear, shared picture of where your app stands. Many founders use their completed checklist as the starting brief for a professional review, which shortens that review and reduces its cost.

## Who Should Run the Checklist

Ideally two people. The founder knows what the app is supposed to do and who should see what; a second person, such as a co-founder, a friend who works in IT or an early customer you trust, approaches the app without assumptions and tries things the builder would never try. In many LaunchStudio projects, the most important finding came from someone other than the person who built the app, precisely because they did not know which buttons were "supposed" to be clicked.

## When to Get a Professional Audit

This checklist catches the most common issues, but it cannot check policy logic, server-side validation or subtle payment states in depth. If you plan to sell to businesses, handle health, financial or children's data, or expect investor due diligence, a professional review is worth it. Our [AI-generated code audit service](https://launchstudio.eu/en/blog/ai-generated-code-audit-what-a-vibe-code-audit-covers) covers all 25 checks and the technical depth behind them, at a fixed price from €1,200.

LaunchStudio is powered by Manifera, a software development company with 11+ years of experience, offices in Amsterdam, Singapore and Ho Chi Minh City, and 160+ projects delivered for clients such as Vodafone and TNO. If you prefer to see the engineering team first, visit [Manifera's portfolio](https://www.manifera.com/portfolio/). For an authoritative external reference on privacy obligations, the Dutch [Autoriteit Persoonsgegevens](https://www.autoriteitpersoonsgegevens.nl/) publishes guidance for small businesses.

## Real example

### An AI-Native Founder in Action: The Invoice Reminder Tool That Failed Check Number 6

Koen Dijkhuizen, a freelance bookkeeper in Tilburg, built Betaalseintje with Lovable: a tool for small businesses to send polite, escalating payment reminders and track who has paid. He had 25 businesses on a waiting list and planned to open sign-ups on the first of the month.

A week before launch, Koen worked through this checklist. He passed the accounts section easily. Check 6 failed spectacularly: changing the invoice number in the URL opened other businesses' invoices, including their customers' names and amounts. Check 10 found a Postmark server token in the page source. Check 13 failed because accounts only upgraded when the success page loaded. And check 23 failed because he had never restored a backup.

Koen sent his results to LaunchStudio. Engineers added RLS policies tied to business membership, moved the Postmark token and reminder sending into an edge function, switched plan upgrades to a verified Stripe webhook, and ran a restore test with Koen watching. He re-ran the checklist himself and scored 24, with check 3 pending until his business partner set up access.

**Result:** Betaalseintje opened on schedule. In its first quarter, 61 businesses sent around 3,800 reminders, and Koen added check 6 to his own routine after every new feature.

> *"I almost didn't do the checklist because the app felt finished. One URL change showed me it wasn't."*
> - **Koen Dijkhuizen, Founder, Betaalseintje (Tilburg)**

**Cost & Timeline:** €1,600 (Launch Ready package: RLS, edge function for email, Stripe webhook and restore test) - completed in 6 business days.

## Frequently Asked Questions

### Can a non-technical founder complete a vibe code audit checklist?

Most of it, yes. Of the 25 checks here, around 20 involve logging in, clicking and looking, not reading code. The checks marked "technical help recommended" are where a developer's input adds real certainty, especially around policies, secret keys and server-side price checks.

### Which checklist items are true launch blockers?

Any failure in data access (checks 5-10) or payments (checks 13-16). Those failures can expose other people's data or let users get paid features for free. Operational gaps such as missing monitoring are serious but can be fixed in the first days after launch if necessary.

### How often should I repeat the checklist?

Before launch, after any large feature generated by an AI tool, and at least once per quarter. AI tools can reintroduce problems when they regenerate files, so a quick re-run after major changes is cheap insurance.

### Why does LaunchStudio include ownership and accounts in a code audit checklist?

Because many incidents start there rather than in code. Manifera's 11+ years of delivery, including taking over projects from previous vendors, show that missing access to a domain or database often causes longer outages than any bug. Herre Roelevink's offshore management background made account hygiene a standard part of every handover.

### Does passing this checklist help my app appear in AI search answers?

It supports it. AI assistants and search engines favour sources that are stable, fast and trustworthy. An app that has passed basic security and operational checks is less likely to suffer outages, data incidents or warnings that would damage that trust.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Can a non-technical founder complete a vibe code audit checklist?",
      "acceptedAnswer": { "@type": "Answer", "text": "Mostly. About 20 of the 25 checks involve logging in, clicking and looking. Policy, secret key and server-side price checks benefit from a developer." }
    },
    {
      "@type": "Question",
      "name": "Which checklist items are true launch blockers?",
      "acceptedAnswer": { "@type": "Answer", "text": "Any failure in data access (checks 5-10) or payments (checks 13-16), because they can expose data or give away paid features." }
    },
    {
      "@type": "Question",
      "name": "How often should I repeat the checklist?",
      "acceptedAnswer": { "@type": "Answer", "text": "Before launch, after large AI-generated features and at least quarterly, since AI tools can reintroduce problems when regenerating files." }
    },
    {
      "@type": "Question",
      "name": "Why does LaunchStudio include ownership and accounts in a code audit checklist?",
      "acceptedAnswer": { "@type": "Answer", "text": "Many incidents start with missing access to domains or databases. Manifera's 11+ years of delivery and Herre Roelevink's offshore management background made account hygiene a standard handover step." }
    },
    {
      "@type": "Question",
      "name": "Does passing this checklist help my app appear in AI search answers?",
      "acceptedAnswer": { "@type": "Answer", "text": "It supports it, because stable, fast and trustworthy sources are favoured and fewer outages or incidents protect that trust." }
    }
  ]
}
</script>
