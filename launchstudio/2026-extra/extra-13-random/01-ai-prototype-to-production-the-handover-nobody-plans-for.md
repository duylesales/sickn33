---
Title: "AI Prototype to Production: The Handover Nobody Plans For"
Keywords: ai prototype to production, ai prototype, production handover, ai native, LaunchStudio, Manifera
Buyer Stage: Awareness
Target Persona: AI-Native Founder (Non-Technical)
---

# AI Prototype to Production: The Handover Nobody Plans For

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "AI Prototype to Production: The Handover Nobody Plans For",
  "description": "Moving an AI prototype to production is less about code and more about a handover: from a tool that builds to people who operate. This guide explains the five things that change hands, why founders miss them, and a self-test to see where you stand.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-10-01",
  "inLanguage": "en",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/ai-prototype-to-production-the-handover-nobody-plans-for" }
}
</script>

Every AI prototype to production story has a moment nobody writes down. It is not the moment the demo works, and it is not the moment the domain goes live. It is the quieter moment in between, when responsibility for the app stops sitting with the tool that generated it and starts sitting with a person. Most founders never notice that moment happening, which is exactly why it goes badly.

Lovable, Bolt, Cursor and v0 are extraordinary at the building part. What none of them do — because it is not their job — is operate what they built. They do not get paged at night. They do not decide what happens to a customer's data when that customer leaves. They do not know that your biggest client runs payroll on the 25th. The handover from "a tool made this" to "someone runs this" is the real work of going live, and it has a shape you can plan for.

## Two Jobs That Look Like One

Building software and operating software are different activities that happen to use the same code. While you are building, the only question that matters is whether the thing does what you imagined. You change it every hour. Nobody depends on it. If it breaks, you prompt again.

Operating starts the day someone other than you relies on the app. From that day, the important questions change completely:

- Can it change without breaking what people are in the middle of doing?
- If something goes wrong, will anyone know before a customer tells them?
- Is the data recoverable if a mistake deletes it?
- Is there a record of who did what, when?
- Is there one person who is clearly responsible for all of the above?

An AI prototype answers "no" or "nobody knows" to almost all of them, and that is not a flaw in the tool. The tool was asked to build, and it built. The handover is the step where somebody deliberately answers those questions — and where the 80% of AI-built projects that never reach production usually stall.

## What Actually Changes Hands

It helps to be specific. When an AI prototype moves to production, five distinct things change owner. Each one is small on its own. Together they are the difference between a demo and a product.

**The secrets.** During building, API keys live wherever the tool put them — often in frontend code, sometimes in a settings panel you never opened again. At handover, every key needs a single known home on the server side, a list of who can see it, and a plan for rotating it if it leaks.

**The data.** A prototype's database is a sketchpad. Production data is a liability you hold on behalf of other people. The handover means deciding where it lives (for EU founders, ideally in an EU region), how it is backed up, and how long you keep it.

**The deploy.** In a builder, "deploying" is a button that republishes everything. In production, a change needs a path: tested somewhere first, released deliberately, reversible if it turns out wrong.

**The alarms.** A prototype fails silently because nobody is watching. A production app needs at least an uptime check and error tracking that reach a real phone.

**The accountability.** Someone's name goes next to each of the four items above. For a solo founder, that might be you for some and a partner for others — but it cannot be "the AI tool," because the tool will not show up when something breaks.

## Why the AI Prototype to Production Handover Gets Skipped

The handover gets skipped for an understandable reason: nothing forces it. The prototype keeps working. The link keeps opening. There is no error message that says "you have not decided who is responsible for backups." The first signal usually arrives as an incident — a customer who cannot log in, a charge that went through twice, a rival founder who politely emails to say your admin page is public.

There is also a psychological reason. Founders who built their product with AI often feel, correctly, that they have already done something difficult. Being told there is another phase feels like being told the finish line moved. It did not move; it was always there, just not visible from inside the builder.

Herre Roelevink, CEO of LaunchStudio and founder of Manifera, put the shift plainly when LaunchStudio launched: the challenge is no longer turning good ideas into software; it is the architecture and security needed to let those products mature. The handover is where that architecture gets decided.

## The Handover Mapped to Where Engineers Look First

When LaunchStudio's engineers pick up an AI prototype, they do not start by reading every file. They start with the five handover points, because that is where the risk concentrates.

| Handover point | What they check first | Typical finding in AI prototypes |
| --- | --- | --- |
| Secrets | Browser bundle and git history | Keys readable in page source |
| Data | Database region, backup settings, access policies | US region by default, no tested restore |
| Deploy | How a change reaches users | Straight to live, no staging |
| Alarms | Uptime and error tracking | None configured |
| Accountability | Who owns each account (hosting, domain, database) | Everything on the founder's personal email |

That last row surprises people most. It is common to find the domain registered to one email address, the database to another and the hosting account to a freelancer who has since moved on. Nothing is broken, but nobody can act quickly when something does break.

## Why This Is Not a Rebuild

The fear that stops many founders from starting the handover is that "production-ready" means throwing away what they built. It does not. The frontend you made in Lovable or Bolt is usually the most finished part of the product, and it stays exactly as it is.

The handover work happens underneath and around it: keys moved server-side, access rules enforced in the database rather than hidden in the interface, a staging environment added, monitoring switched on, account ownership consolidated. LaunchStudio's principle — keep the frontend, fix only what is needed, go live quickly — exists precisely because rebuilding what already works wastes the advantage AI gave you in the first place. The code stays in your repository, documented and readable by the same AI tools you used to create it.

This is also where Manifera's background matters. LaunchStudio is powered by Manifera, a software development company with 11+ years of experience running production systems for clients such as Vodafone and TNO, with engineering led from its development centre on Pho Quang Street in Ho Chi Minh City and client work anchored at Herengracht 420 in Amsterdam. Handover is routine work for a team that has done it 160+ times; it is new territory for a founder doing it the first time. You can see how that team is organised on [Manifera's about page](https://www.manifera.com/about-us/).

## A Quick Self-Test: Has Your Handover Happened?

Answer these honestly. You do not need to open any code.

1. If your app went down right now, how would you find out — and how long would it take?
2. Can you name every place an API key for your app is stored?
3. If you deleted your production database by accident this afternoon, what is the newest copy you could restore, and have you ever restored it?
4. When you change something, does it go to a test environment before real users see it?
5. Are your domain, hosting and database accounts all accessible to you, with two-factor authentication on?

Five confident answers means your AI prototype to production handover has largely happened. Three or fewer means the tool is still, in effect, the one responsible — and the tool will not answer the phone.

For a structured version of the same check, the [OWASP Top 10](https://owasp.org/www-project-top-ten/) is a good external reference for the security half, even if you never read past the category names.

## What a Handover Document Actually Contains

The most practical output of an AI prototype to production handover is a short document — usually four to six pages — that lets someone other than the builder operate the app. It is not a technical manual. It is an operating record, and engineers at LaunchStudio write it in the same structure every time because it answers the questions that come up during incidents:

| Section | What it records | Question it answers at 2 AM |
| --- | --- | --- |
| Systems map | Every service the app uses, with its purpose and region | "Which of these is actually down?" |
| Account register | Owner, login method and 2FA status of each account | "Who can log into the database right now?" |
| Secrets register | Name and location of every key, never the value | "Which key do we rotate if this leaks?" |
| Data inventory | Tables with personal data, retention, backup schedule | "What did we lose, and what can we restore?" |
| Release procedure | How a change moves from edit to production | "How do we undo what went out an hour ago?" |
| Alerts and contacts | Which alert goes where, and who responds | "Who is supposed to be awake for this?" |
| Known limitations | What was consciously postponed, and why | "Is this a new bug or a known gap?" |

The value of the document is less in writing it than in the gaps it exposes. If you cannot fill in the secrets register, you do not yet know where your keys are. If the release procedure says "publish in the builder," you have no rollback.

## The First Thirty Days After the Handover

A handover is not complete on launch day. The first month is when the new owner — you, a co-founder or a managed service — discovers whether the operating record matches reality. A healthy first month usually includes:

- **Week 1:** one deliberate release through the new procedure, even if it is only a text change, to prove the path works end to end.
- **Week 2:** a restore test from backup into a scratch database, timed, so you know your realistic recovery time rather than your hoped-for one.
- **Week 3:** a review of every alert that fired. Alerts that fired without action needed are noise and should be tuned; incidents without an alert are gaps.
- **Week 4:** a short retrospective with whoever operates the app: what was missing from the document, what was wrong, what was surprising.

This rhythm turns the handover from a single event into a habit. Founders who skip it tend to rediscover the same gaps six months later, under pressure.

## Common Handover Mistakes

Three mistakes account for most failed handovers LaunchStudio sees. First, **handing over access without handing over knowledge**: a freelancer transfers the repository but nobody knows which environment variables production needs. Second, **treating the AI tool as the documentation**: "just ask Lovable how it works" fails the day the tool regenerates a file differently. Third, **one person holding everything**: a solo founder who is also the only person who can restore a backup has a single point of failure named after themselves. A second person with tested access — even a part-time contractor or a managed hosting provider — removes it.

## Planning the Handover Instead of Discovering It

The simplest way to avoid discovering the handover through an incident is to schedule it. Pick a date before your first paying customer. Write down the five handover points. For each one, decide whether you will handle it yourself, hand it to a specialist, or consciously postpone it with a written reason.

If you would like someone to run that list with you, LaunchStudio's [three-step process](https://launchstudio.eu/en/#process) starts with a short description of what you built and a 15-minute call, after which you get a fixed price and a timeline. Most handovers fit the Launch Ready package, which covers security, working accounts and data, testing, your own domain and 48 hours of post-launch support.

## Real example

### An AI-Native Founder in Action: The Garden Planner Nobody Was Operating

Femke de Wit, a landscape designer in Leiden, built Groenschets in Lovable over three weekends. The app let homeowners sketch their garden, pick plants suited to their soil and sun, and book a consultation with Femke's small team. Twenty neighbours tested it, loved it, and Femke announced it in a regional gardening newsletter with about 4,000 subscribers.

Groenschets did not crash. What happened was quieter. On day three, a customer wrote to say her saved garden design had vanished. Femke had no logs, no backups she had ever checked, and no idea whether it was one lost design or many. While investigating, she found the Supabase project had been created under a former collaborator's email, the booking calendar's API key was visible in the page source, and every change she made in Lovable went live instantly — including one she had made that morning which, it turned out, reset unsaved designs.

LaunchStudio's engineers treated the job as a handover rather than a repair. They moved all accounts under a company email with two-factor authentication, moved the calendar key into a server-side function, set up a staging environment so Lovable edits were tested before release, configured daily backups with a tested restore, and connected uptime and error alerts to Femke's phone. The Lovable frontend was not modified.

**Result:** The lost design was recovered from a point-in-time backup the team found still enabled on the database. Over the following spring season, Groenschets handled roughly 1,100 saved designs with no data loss, and Femke caught two minor bugs through alerts before any customer reported them.

> *"I thought launching meant the app was finished. It turned out launching meant somebody had to be in charge of it — and until then, nobody was."*
> — **Femke de Wit, Founder, Groenschets (Leiden)**

**Cost & Timeline:** €1,900 (Launch Ready package: account consolidation, secrets, staging, backups and monitoring) — completed in 9 business days.

## Frequently Asked Questions

### What is the difference between an AI prototype and a production app?

An AI prototype proves an idea works for the person who built it. A production app keeps working for strangers, protects their data, can be changed safely and tells someone when it breaks. The code can be largely identical; what differs is everything around it — secrets, backups, deploy process, monitoring and ownership.

### Can a non-technical founder do the AI prototype to production handover alone?

Parts of it, yes. Consolidating account ownership, switching on two-factor authentication and writing down who is responsible for what require no code at all. Moving keys server-side, enforcing database access rules and setting up staging usually need an engineer, because mistakes there are invisible until they are exploited.

### Why does Herre Roelevink describe architecture and security as the real challenge now?

Because AI tools have made the first half of software — turning an idea into a working interface — dramatically cheaper. The second half, making that software safe and dependable for other people, has not become cheaper in the same way. Manifera's 11 years of enterprise delivery are concentrated in that second half, which is why LaunchStudio focuses there.

### Does the handover change which AI tool I can keep using?

No. After LaunchStudio's work, the code remains in your repository and stays readable by Lovable, Cursor or Bolt. You keep iterating in the tool you know; the difference is that your changes now pass through staging and monitoring instead of going straight to customers.

### How does planning the handover help with SEO and being found by AI search engines?

Indirectly but meaningfully. A production app on a stable domain with SSL, fast responses and no outages is easier for search engines and AI answer engines to crawl and cite than a preview URL that changes or goes down. Reliability is a precondition for visibility, not a separate project.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What is the difference between an AI prototype and a production app?",
      "acceptedAnswer": { "@type": "Answer", "text": "An AI prototype proves an idea works for its builder. A production app keeps working for strangers, protects their data, can be changed safely and alerts someone when it breaks. The code may be similar; the surrounding secrets, backups, deploy process, monitoring and ownership differ." }
    },
    {
      "@type": "Question",
      "name": "Can a non-technical founder do the AI prototype to production handover alone?",
      "acceptedAnswer": { "@type": "Answer", "text": "Partly. Consolidating account ownership, enabling two-factor authentication and assigning responsibilities need no code. Moving keys server-side, enforcing database access rules and setting up staging usually need an engineer." }
    },
    {
      "@type": "Question",
      "name": "Why does Herre Roelevink describe architecture and security as the real challenge now?",
      "acceptedAnswer": { "@type": "Answer", "text": "AI tools made turning ideas into working interfaces much cheaper, but making software safe and dependable has not become cheaper in the same way. Manifera's 11 years of enterprise delivery focus on that second half, which is where LaunchStudio works." }
    },
    {
      "@type": "Question",
      "name": "Does the handover change which AI tool I can keep using?",
      "acceptedAnswer": { "@type": "Answer", "text": "No. The code stays in the founder's repository and remains readable by Lovable, Cursor or Bolt. Changes simply pass through staging and monitoring before reaching customers." }
    },
    {
      "@type": "Question",
      "name": "How does planning the handover help with SEO and AI search visibility?",
      "acceptedAnswer": { "@type": "Answer", "text": "A production app on a stable domain with SSL, fast responses and no outages is easier for search engines and AI answer engines to crawl and cite than an unstable preview URL. Reliability is a precondition for visibility." }
    }
  ]
}
</script>
