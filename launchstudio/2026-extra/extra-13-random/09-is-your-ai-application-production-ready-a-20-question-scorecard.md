---
Title: "Is Your AI Application Production Ready? A 20-Question Scorecard"
Keywords: ai application production ready, production readiness scorecard, ai prototype checklist, ai websites, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: AI-Native Founder (Non-Technical)
---

# Is Your AI Application Production Ready? A 20-Question Scorecard

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Is Your AI Application Production Ready? A 20-Question Scorecard",
  "description": "A 20-question scorecard, in plain language, to test whether an AI application is production ready across five areas: access, data, money, operations and trust. Includes scoring bands and what to do with a low score.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-10-09",
  "inLanguage": "en",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/is-your-ai-application-production-ready-a-20-question-scorecard" }
}
</script>

Eighty percent of AI-built projects never reach production. Some of those stop for good reasons — the idea did not work, the market was not there. Many stop because the founder could not tell whether their AI application was production ready, and either launched too early and got burned or waited forever for a certainty that never came — all because they could not answer one question: is my AI application production ready?

A scorecard does not replace an engineer's review, but it replaces guessing. The twenty questions below are grouped into five areas. Each "yes" scores one point. Be strict: "I think so" counts as no.

## Area 1: Access (Who Can See and Do What)

1. Have you tested with two separate accounts that one user cannot see the other's data, including by changing numbers or codes in the URL?
2. If your app has admin or staff features, are they blocked for normal users even when someone types the admin page address directly?
3. Do password reset links expire after use or after a short time?
4. Is there a limit on how many times someone can try a wrong password?

**Why this area matters most:** access failures are the most common serious finding in AI-generated apps, and the one users forgive least. An app that leaks one customer's data to another rarely gets a second chance.

## Area 2: Data (What Survives)

5. Do you know which country or region your database is hosted in?
6. Are automatic backups switched on?
7. Has anyone ever restored a backup to prove it works?
8. Can you delete a user's data completely if they ask you to?

**Why it matters:** backups that have never been restored are hopes, not backups. And under GDPR, a deletion request is not optional — you need to be able to honour it within a month.

## Area 3: Money (What Gets Counted)

9. Is a payment marked as successful only when Stripe, Mollie or your provider confirms it on the server — not when the customer's browser returns to your site?
10. When a subscription is cancelled or a payment fails, does the customer lose access automatically?
11. Are test payments completely separate from live payments, with different keys?
12. Can you see, for any customer, what they paid and when, without opening the database?

**Why it matters:** payment bugs are expensive in both directions. Either you give away what you should charge for, or you charge people for things they did not receive — and payment providers take the second one very seriously.

## Area 4: Operations (What Happens When Things Go Wrong)

13. Would you be alerted within minutes if the app went down?
14. When an error happens, is it recorded somewhere you can look at later?
15. Do changes go to a test environment before real users see them?
16. Can you undo a bad change within minutes?

**Why it matters:** every app has bad days. The difference between a production app and a prototype is whether you know about them and can recover before customers do the finding for you.

## Area 5: Trust (What Others Need to See)

17. Is the app on your own domain with a valid SSL certificate?
18. Do you have a privacy notice that accurately lists the services that process user data?
19. Are all accounts (domain, hosting, database, payments) owned by a company email you control, with two-factor authentication?
20. Could you explain to a customer, in two sentences, how their data is protected — and would it be true?

**Why it matters:** B2B customers, payment providers, investors and increasingly your end users will ask. The honest answers need to exist before the questions arrive.

## Scoring: Is Your AI Application Production Ready?

| Score | What it means | Suggested next step |
| --- | --- | --- |
| 18–20 | Production ready in most practical senses | Launch, keep monitoring, review again after major changes |
| 14–17 | Close, with specific gaps | Fix the "no" answers in Areas 1 and 3 first, then launch |
| 9–13 | Prototype with some production features | Plan a hardening project before inviting paying customers |
| 0–8 | Working demo | Treat launch as a project, not a button |

Two rules override the total. First, any "no" on questions 1, 2 or 9 means you should not launch to paying customers yet, regardless of score — those are the failures with the highest damage. Second, if you answered "I don't know" to several questions, your real score is lower than you think; uncertainty is itself a finding.

## Why the Scorecard Is Not the Whole Story

A founder can answer all twenty questions and still miss problems an engineer would catch in an hour: an API key visible in the page source, a file upload with no type checking, a database rule that looks correct but has an exception nobody intended. The scorecard tells you where to look and how worried to be. It does not tell you what is actually in the code.

That is the role of a review. LaunchStudio's review follows the same five areas, with the addition of a code and configuration pass, and produces a written list of findings ranked by risk, each explained in plain language. It is the starting point of every engagement and the basis of a fixed-price quote.

## How to Run the Scorecard as a Team

The scorecard works best when it is not filled in alone. If you have a co-founder, a freelancer or even a technically curious friend, run it together in a single session of about an hour:

1. **Prepare:** two test accounts, access to your database and payment dashboards, and your app open on a phone and a laptop.
2. **Answer each question by doing, not by remembering.** Question 1 is answered by performing the two-account test right now, not by recalling that you "think it was fine."
3. **Record evidence:** a screenshot, a note of what you tried, the date. This turns the scorecard into a small audit trail.
4. **Mark "I don't know" explicitly.** Uncertainty is a finding. It usually means nobody owns that area.
5. **Agree on owners** for each "no" and "don't know": who will fix it, or who will find someone who can.

Repeating the session every quarter, or before a major launch, gives you a trend line. A score moving from 11 to 16 to 19 is a story investors and customers understand immediately.

## What Each Area Usually Reveals in AI-Built Apps

Across the AI-built applications LaunchStudio reviews, the scorecard's areas fail in predictable ways:

| Area | Most common "no" | Typical root cause |
| --- | --- | --- |
| Access | Question 1 (cross-user data) | Access filtered in the interface, not the database |
| Data | Question 7 (restore never tested) | Backups assumed, never verified |
| Money | Question 9 (browser-confirmed payments) | Checkout generated from a redirect-based example |
| Operations | Question 13 (no alerts) | Nobody decided who should be woken up |
| Trust | Question 19 (account ownership) | Accounts created under personal or freelancer emails |

Knowing the common failure points helps you check them first — and helps you judge whether an engineer's findings are thorough. If a review of your AI application comes back without mentioning any of these five areas, ask why.

## From Score to Action Plan

A score is only useful if it becomes a plan. Convert your "no" answers into a short, prioritised list using three columns: **harm** (could a customer be hurt by this?), **effort** (hours, days or weeks), and **dependency** (does something else need to be fixed first?). Items with high harm go first regardless of effort. Items with low harm and high effort can be scheduled after launch, in writing.

For many founders, the resulting list maps naturally onto a small production project: access and money in the first week, data and operations in the second, trust items handled by the founder in parallel. That structure is also what a fixed-price quote should reflect — if it doesn't, ask the provider to explain the difference.

## Adapting the Scorecard to Your Product

The twenty questions are general. A few product types should add questions of their own. Apps with teams should ask whether a removed member loses access immediately. Apps that call AI models should ask whether there is a per-user limit on model usage. Apps used by children or holding health data should ask whether that data is separated and access-logged. Mobile apps should ask whether account deletion works inside the app. Adding three or four product-specific questions keeps the scorecard honest as your product evolves.

## Why Self-Assessment Is Worth Doing Before Paying Anyone

Some founders skip the scorecard and go straight to hiring an engineer. Doing it first has three advantages. It makes the conversation with any provider concrete: instead of "please make it secure," you can say "questions 1, 9 and 13 failed, and I don't know the answer to 7." It gives you a baseline to measure the provider's work against — after the project, the same questions should pass. And it protects you from over-scoping: if your score is already 17, you do not need a large project, and a provider proposing one should explain why.

## Keeping the Score High After Launch

Scores decay. Every new feature, AI-regenerated file or added integration can turn a "yes" back into a "no." The most effective protection is to convert the riskiest questions into automated checks: a test that performs the two-account check, a test that simulates a closed-tab payment, an alert that fires if backups fail. Once those exist, questions 1, 9 and 13 answer themselves every day, and your quarterly scorecard session becomes a quick confirmation rather than an anxious discovery. Treat the scorecard as a habit, not an event, and it will keep telling you the truth about your AI application.

## One Last Rule

When in doubt between two answers, choose the stricter one. A scorecard that flatters you is worse than none, because it replaces a vague worry with false confidence. The goal is not a high number on paper; it is an AI application that stays production ready when real users do unexpected things.

## How Manifera's Standards Shape the Questions

The twenty questions are a founder-sized version of the checks Manifera applies to enterprise systems. Our engineers have shipped 160+ projects for enterprise clients — now they are here to launch yours. What changes between an enterprise audit and a founder scorecard is depth and paperwork, not the underlying questions: who can access what, what survives, what gets counted, what happens when it breaks, and what you can prove. Manifera's team works from its development centre in Ho Chi Minh City, with its Singapore hub on Tras Street and its European base at Herengracht 420, Amsterdam. More on the team is on [Manifera's about page](https://www.manifera.com/about-us/).

If your score came out lower than you hoped, [calculate what your project would cost](https://launchstudio.eu/en/#calculator) — the calculator takes about a minute and uses the same categories. For an external benchmark on the security side, the [OWASP Top 10](https://owasp.org/www-project-top-ten/) lists the most critical web application risks in order.

## Real example

### An AI-Native Founder in Action: A Curtain Configurator That Scored 9 Out of 20

Iris Jansen runs a curtain and upholstery studio in Den Bosch and built Stoffenstudio in Lovable: customers choose a fabric, enter window measurements, see a price, pay a 30% deposit and book a fitting appointment. Friends and early customers loved it. Before announcing it to her 6,000 Instagram followers, Iris found an earlier version of this scorecard and filled it in. She scored 9.

Her "no" answers clustered exactly where the rules say to worry. Customers could see each other's orders, including home addresses, by changing an order number in the URL (question 1). The deposit was marked paid when the browser returned from Mollie (question 9). The admin page where she adjusted prices was reachable by anyone who knew the address (question 2). There were no alerts, no staging environment and no tested backups.

LaunchStudio's engineers confirmed the findings in a one-day review and found two more: an unrestricted file upload for window photos and the Mollie API key visible in the page source. Over seven business days they added row-level security to orders and customers, moved deposit confirmation to verified webhooks, locked the admin area behind server-side role checks, restricted uploads, rotated and moved the key, and set up EU backups with a tested restore, staging and alerts.

**Result:** Iris retook the scorecard and scored 19 — the missing point was a privacy notice she wrote herself that weekend. The Instagram launch brought in 212 configured orders and 58 paid deposits in the first fortnight, with no payment mismatches and no data complaints.

> *"The scorecard didn't fix anything, but it told me I wasn't ready in a way I couldn't argue with. That was worth more than reassurance."*
> — **Iris Jansen, Founder, Stoffenstudio (Den Bosch)**

**Cost & Timeline:** €1,750 (Launch Ready package: access control, payments, admin protection, uploads and monitoring) — completed in 7 business days.

## Frequently Asked Questions

### Is a high scorecard result enough to call my AI application production ready?

It is a strong signal, not a guarantee. The scorecard checks behaviour you can observe; a code review can find problems — exposed keys, unsafe uploads, flawed rules — that do not show up from the outside.

### Why do questions 1, 2 and 9 override the total score?

Because they cover the failures with the most severe consequences: exposing customer data, giving strangers admin powers and mishandling money. A single failure there can outweigh everything else that works.

### How often should I retake the scorecard?

After any significant change — a new feature, a new user role, a change in payment setup — and at least every few months. AI tools regenerate code readily, and a fix made once can be undone by a later prompt.

### Does Manifera use a similar scorecard for enterprise clients?

The underlying areas are the same, but enterprise reviews go deeper with formal documentation, penetration testing and compliance mapping. The founder scorecard distils those checks into questions a non-technical person can answer honestly.

### Can a production readiness scorecard help with visibility in AI search results?

Indirectly. Questions 17 and 18 — a proper domain with SSL and an accurate privacy notice — are also trust signals that search engines and AI answer engines consider when deciding which sites to show and cite.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Is a high scorecard result enough to call my AI application production ready?",
      "acceptedAnswer": { "@type": "Answer", "text": "It is a strong signal but not a guarantee. A code review can find exposed keys, unsafe uploads or flawed rules that are not visible from outside." }
    },
    {
      "@type": "Question",
      "name": "Why do questions 1, 2 and 9 override the total score?",
      "acceptedAnswer": { "@type": "Answer", "text": "They cover the most severe failures: exposing customer data, giving strangers admin powers and mishandling money." }
    },
    {
      "@type": "Question",
      "name": "How often should I retake the scorecard?",
      "acceptedAnswer": { "@type": "Answer", "text": "After any significant change and at least every few months, since AI tools can regenerate code and undo earlier fixes." }
    },
    {
      "@type": "Question",
      "name": "Does Manifera use a similar scorecard for enterprise clients?",
      "acceptedAnswer": { "@type": "Answer", "text": "The areas are the same, but enterprise reviews add formal documentation, penetration testing and compliance mapping." }
    },
    {
      "@type": "Question",
      "name": "Can a production readiness scorecard help with visibility in AI search results?",
      "acceptedAnswer": { "@type": "Answer", "text": "Indirectly. A proper HTTPS domain and accurate privacy notice are trust signals search engines and AI answer engines consider." }
    }
  ]
}
</script>
