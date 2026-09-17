---
Title: "Lovable Hosting: Where Your App Really Runs After Launch"
Keywords: lovable hosting, Lovable, lovable app deployment, preview URL vs production, managed hosting AI app, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: AI-Native Founder (Non-Technical)
---

# Lovable Hosting: Where Your App Really Runs After Launch

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Lovable Hosting: Where Your App Really Runs After Launch",
  "description": "A plain-English explanation of what Lovable hosting gives you, what a preview URL really is, and the four things that behave differently once real users arrive. Helps non-technical founders decide where their app should live before they point a domain at it.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-06-03",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/where-lovable-apps-run-hosting-explained" }
}
</script>

Bram had a link. That was the thing he kept coming back to: he had built a booking tool for padel courts in Rotterdam in about nine days inside Lovable, and he had a link he could send to anyone, and it worked. Two club owners opened it on their phones and filled in a test booking. So when his accountant asked him where the app was hosted, the question genuinely puzzled him. It was on the internet. Someone could open it. Wasn't that hosting?

It is, in the same way a demo apartment is housing. Everything you need to see the idea is there, and almost nothing you need to actually live in it. The gap between a Lovable preview URL and a production deployment is not a technical detail that engineers care about for aesthetic reasons — it is the difference between an app that survives its first busy Monday and one that doesn't.

## What That Preview URL Actually Is

When Lovable builds your app, it also gives you somewhere to see it. That environment is optimised for one job: letting you and a handful of people look at the thing while you iterate. It is generous, it is fast to update, and it assumes a very small number of concurrent visitors who are broadly on your side.

Production hosting is optimised for a different job: staying up, staying fast, and staying predictable when the people arriving are strangers who did not read your instructions. Those two goals pull in opposite directions in ways that matter. A preview environment is happy to rebuild the whole app when you change a line. A production environment needs to not change at all while someone is halfway through a payment.

The practical translation for a founder: your preview link is proof the product exists. It is not yet the place you send a paying customer, and treating it as one is the most common reason a launch weekend goes badly.

## The Four Things That Behave Differently With Real Users

**Concurrency stops being theoretical.** Two friends clicking around is not the same load pattern as forty people arriving from a LinkedIn post at 09:00. Preview environments frequently have limits on simultaneous requests that nobody notices until they are exceeded — and when they are, the failure looks to your users like a blank page rather than an error you can explain.

**Secrets become a real problem.** In the build phase, an API key sitting in your frontend code is invisible to you because everything works. In production, that same key is visible to anyone who opens the browser's developer tools. Anyone. This is the single most common security finding when an AI-built app comes in for review, and the fix is architectural — the key has to move to a server-side function — not a setting you toggle.

**Database connections run out.** Your app talks to a database, and every visitor session opens a connection. Development traffic never exhausts the pool. Real traffic can, and when it does, the symptom is a site that works perfectly for the first thirty people and throws errors for everyone after — which is exactly the moment you least want it to happen.

**File uploads stop being free.** If your app lets users upload anything — a profile photo, a document, a court-booking screenshot — that data has to live somewhere with rules about size, type and access. AI-generated apps typically accept whatever they are given, which means your storage bill and your security exposure both scale with your least careful user.

## Your Database Lives Somewhere Else Entirely

This is the part that surprises non-technical founders most, and it is worth stating bluntly: hosting your app and hosting your data are two separate arrangements with two separate lifecycles.

Most Lovable projects store their data in Supabase. That Supabase project has its own region, its own backup settings, its own security rules and its own bill. You can change where your frontend is hosted without touching it, and you can lose your entire database while your frontend sits there looking perfectly healthy.

Two consequences follow. First, when you ask "where is my app hosted," you are actually asking two questions, and the data one matters more, because a frontend can be rebuilt in a day and a customer database cannot. Second, the region your Supabase project runs in was chosen at creation, often by default, and for EU founders that default is frequently not in Europe. Moving it later is a migration, not a setting — export, restore, verify, cut over — so it is worth checking now while the answer costs you one dropdown.

## "Deployed" and "Launched" Are Not the Same Word

An app is deployed when the code is running somewhere stable. An app is launched when the code is running somewhere stable **and** someone is responsible for it.

That second half is the part AI tools cannot give you, and it breaks down into questions with concrete answers:

- If the app goes down at 22:00 on a Saturday, who finds out, and how?
- If a customer says "my booking disappeared," who can look at the logs and confirm what happened?
- If you need to fix a bug, does deploying the fix take fifteen seconds or does it require redeploying everything and hoping?
- If the database is corrupted on a Tuesday, what is the most recent copy you can restore, and has anyone ever tested restoring it?

None of these require an in-house engineering team. They do require deciding, once, before your first real customer, rather than discovering the answer during an incident.

## Monitoring: The Thing You Only Miss Once

A production app should tell you when it is unhappy. In practice, for a small product, that means three modest things: an uptime check that pings your app every few minutes and messages you if it stops responding, error tracking that records what broke and on which page, and visibility into your database's health.

Founders often skip this because it feels like enterprise ceremony for a product with eleven users. The reason to do it anyway is simpler than it sounds: without monitoring, you find out about outages from customers, and finding out from customers is what makes small technical problems into trust problems.

## Backups, Stated Plainly

Ask yourself one question: if your database were wiped right now, what would you lose?

For most early Lovable apps, the honest answer is "everything, and I'm not sure there's a copy." Managed database providers usually offer backups, sometimes only on paid plans, often with a retention window shorter than founders assume. The important detail is not whether backups exist but whether anyone has ever restored one — an untested backup is a hypothesis, not a safety net.

## Your Three Realistic Hosting Options

**Stay on Lovable's hosting.** Simplest, fastest, and appropriate for genuinely small products. You accept the platform's limits and defaults, and you keep iterating inside the tool that built the app. For a landing page with a form, this can be enough for a long time.

**Move the frontend to a dedicated host.** Vercel, Netlify, or similar. This gives you proper build pipelines, environment variable handling, preview deployments per change, custom caching, and infrastructure that expects production traffic. The code remains yours and remains AI-readable, so you can keep editing in Lovable or Cursor afterwards.

**Have it managed.** Someone else owns the hosting, SSL, monitoring, backups and security updates, and you own the product. This is what LaunchStudio's Launch & Grow package covers at €49 per month on top of the build, and it exists because most founders do not want to become their own infrastructure department at the exact moment they should be selling.

There is no universally correct answer. There is an answer that fits how much downtime your customers would tolerate and how much of your week you want to spend on this.

## Decide These Before You Point a Domain At It

- Which region your database is in, and whether that is where you need it.
- Whether any API key is currently sitting in frontend code.
- Where backups go, how far back they reach, and whether a restore has been tested once.
- Who receives an alert if the app stops responding.
- What your deploy process is: how a fix reaches production, and how long that takes.
- What happens to in-progress user sessions when you deploy.

If you can answer six out of six, your app is genuinely ready for a domain. Four out of six means you are close. Two means the preview link is doing more work than it should be.

## Getting From Link to Launch

The good news is that this is a bounded piece of work, not a rebuild. LaunchStudio's engineers take the frontend you already built — untouched — and put the production layer underneath it: environment secrets moved server-side, database connections pooled properly, hosting configured with SSL and a real deploy pipeline, monitoring wired up, and backups tested rather than assumed. That is the [Launch Ready package](https://launchstudio.eu/en/#packages), typically inside a couple of weeks rather than a couple of months, and it is the same engineering discipline Manifera has applied to enterprise systems for more than eleven years from its Amsterdam and Ho Chi Minh City offices.

If you would rather find out where you stand before committing to anything, [send us your prototype link](https://launchstudio.eu/en/#contact) and you will get a straight answer about what is already solid and what needs attention first.

## Real example

### A Padel Booking Tool Meets Its First Busy Monday

Bram Verhoeven's app, CourtSlot, served three padel clubs around Rotterdam. He launched by sending the Lovable preview link to the clubs' member mailing lists on a Sunday evening — roughly 900 people in total. By Monday morning, about sixty of them tried to book a court in the same twenty-minute window.

The frontend held. The database did not: connections were opened per session and never pooled, so members thirty-one onwards saw a blank screen with no explanation. Two of them called the club, the club called Bram, and Bram had no logs to look at because error tracking had never been set up. He also discovered, while investigating, that the Supabase project was running in a US region and that his booking API key was readable in the page source.

The work took eight business days: connection pooling and query fixes, the API key moved into a server-side function, the database migrated to an EU region with a tested restore, hosting moved to a proper deploy pipeline with a staging environment, and uptime plus error monitoring wired to his phone. The frontend he had built in Lovable was not modified at all.

**Result:** CourtSlot handled a 400-member release from a fourth club six weeks later without incident, and Bram found out about the one outage that did occur — a provider issue lasting four minutes — from his phone rather than from a club manager.

> *"I thought hosting was a box you tick. It turned out to be the difference between people booking a court and people phoning the club to complain about me."*
> — **Bram Verhoeven, Founder, CourtSlot (Rotterdam)**

**Cost & Timeline:** €2,400 (Launch Ready Package: hosting, database migration, secrets and monitoring) — live in 8 business days, plus managed hosting at €49/month.

## Frequently Asked Questions

### Can I just keep using the Lovable preview link as my real app?

For a small internal tool or an early pilot with a handful of friendly users, sometimes yes. It becomes a problem the moment you have paying customers, real personal data, or traffic arriving in bursts — because preview environments are built for iteration, not for concurrency, uptime guarantees or incident recovery.

### Does moving hosting mean rebuilding my app?

No. The frontend you built stays as it is. Moving hosting means changing where that code is served from and how it is built and deployed, plus wiring up the production concerns around it. Your code stays yours and stays editable in Lovable or Cursor afterwards.

### Is my Supabase database affected if I change frontend hosting?

Not automatically — they are separate services with separate settings. That independence cuts both ways: you can move hosting without touching data, and you can also have a perfectly healthy frontend pointing at a database with no backups and the wrong region.

### How much traffic can a default Lovable setup actually handle?

There is no single number, because it depends on what each page does and how your database queries are written. The more useful question is what happens at your realistic peak — a product launch email, a press mention — and whether anything in the chain has a hard limit you would hit there.

### What does managed hosting actually include?

In LaunchStudio's case: hosting, SSL certificates and renewal, uptime monitoring, automatic backups and security updates, for €49 per month alongside the Launch & Grow package. The value is less the infrastructure than the fact that someone other than you notices when something breaks.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Can I just keep using the Lovable preview link as my real app?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "For a small internal tool or an early pilot with friendly users, sometimes. It becomes a problem once you have paying customers, real personal data or bursty traffic, because preview environments are built for iteration rather than concurrency, uptime or incident recovery."
      }
    },
    {
      "@type": "Question",
      "name": "Does moving hosting mean rebuilding my app?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No. The frontend stays as it is. Moving hosting changes where the code is served from and how it is built and deployed, and wires up production concerns around it. The code remains yours and remains editable in Lovable or Cursor."
      }
    },
    {
      "@type": "Question",
      "name": "Is my Supabase database affected if I change frontend hosting?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Not automatically, because they are separate services with separate settings. That independence also means a healthy frontend can be pointing at a database with no backups and the wrong region."
      }
    },
    {
      "@type": "Question",
      "name": "How much traffic can a default Lovable setup actually handle?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "There is no single number; it depends on what each page does and how queries are written. The useful question is what happens at your realistic peak, such as a launch email, and whether anything in the chain has a hard limit you would hit there."
      }
    },
    {
      "@type": "Question",
      "name": "What does managed hosting actually include?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "For LaunchStudio: hosting, SSL and renewal, uptime monitoring, automatic backups and security updates at €49 per month alongside the Launch & Grow package. The main value is that someone other than the founder notices when something breaks."
      }
    }
  ]
}
</script>
