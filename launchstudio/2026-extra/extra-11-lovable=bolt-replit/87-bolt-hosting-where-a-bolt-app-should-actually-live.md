---
Title: "Bolt Hosting: Where a Bolt App Should Actually Live"
Keywords: Bolt, bolt hosting, deployment, environment variables, lovable hosting, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: Technical Solo Founder / Indie Hacker
---

# Bolt Hosting: Where a Bolt App Should Actually Live

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Bolt Hosting: Where a Bolt App Should Actually Live",
  "description": "A Bolt prototype runs in a place designed for building, not for customers. What moving it properly involves: build output, environment variables, the server-side half, and a deploy you can repeat.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-08-28",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/bolt-hosting-where-a-bolt-app-should-actually-live" }
}
</script>

A Bolt project is a remarkable thing to watch appear. You describe a product, it exists, it runs in front of you, and you can send someone a link within the hour.

That link is the problem. The environment producing it was built to let you iterate, not to serve customers — and the distance between those two purposes is where founders lose data, leak keys and discover that their live product is whatever they happened to be editing on Tuesday.

Moving a Bolt app somewhere durable is not difficult. It is a handful of decisions, most of which nobody tells you about because the prototype worked without them.

## What the Prototype Environment Is Actually Doing

Three properties matter.

**It is tied to your session.** The preview address belongs to your working environment, changes, and reflects your current edits. Sending it to a customer means sending a link that will break and may show them unfinished work.

**It has no separation between building and serving.** There is no notion of a released version. Whatever exists is what runs, which means an experiment at eleven at night is live at eleven at night.

**Its storage is not durable.** Anything written beside the application disappears when the environment is rebuilt, and it is rebuilt more often than you expect.

None of that is a flaw in the tool. It is the correct design for a place where you are trying things.

## What a Bolt App Consists Of

Before choosing where it goes, know what you have — because Bolt typically produces two things people treat as one.

**A frontend.** JavaScript that builds into static files: HTML, CSS and bundled scripts. This is most of what you see, and it can be served by anything, cheaply and fast.

**Server-side pieces, if your product needs them.** Anything that must not run in a browser: calls using a privileged key, payment handling, webhook endpoints, scheduled work. Sometimes Bolt generates these; sometimes the prototype does everything client-side and the server half does not exist yet, which is the situation that produces leaked keys.

Separating those two in your mind is the whole of the hosting decision. Static files go somewhere static. The server-side half goes somewhere that runs code and holds secrets.

## Choosing a Destination

For a typical Bolt product there are three sensible shapes.

**Static hosting plus managed backend services.** The frontend deployed to any static host or CDN; the database, authentication and file storage provided by a managed service such as Supabase; small amounts of server-side logic as serverless functions. Cheapest, fastest, and appropriate for the large majority of products.

**A platform that hosts both.** A single provider serving the frontend and running your server-side code, with previews per branch and deployments tied to your repository. Slightly more expensive, considerably less to think about, and the common default.

**Your own infrastructure.** A container or a virtual machine you manage. Justified when a customer's contract requires it or you have unusual needs, and rarely otherwise — it adds operational work a small team should not be spending time on.

Two constraints narrow the choice quickly. If you sell to Dutch or EU businesses, you want an EU region and you want to be able to say which one. And if anything in your product runs on a schedule or receives webhooks, confirm the destination handles those properly rather than assuming.

## Environment Variables and the Key That Leaks

The single most common failure in moving a prototype to production.

Anything included in a frontend build is public. Not obscured, not difficult to find — present in the files any visitor downloads. Build tools generally require a prefix on variables intended for the browser, and that prefix is a declaration that the value is public, not a mechanism that protects it.

So: the anonymous or publishable key belongs in the frontend, protected by your database's access rules. The service key, the payment secret key, the model provider's key and anything else privileged belong only in server-side code, set as environment variables in the hosting platform, never committed to the repository.

If your Bolt prototype currently calls a paid API directly from the browser, that call needs to move behind a server-side endpoint before you deploy anywhere. This is not an optional refinement; it is the difference between a private key and a published one.

## A Deploy You Can Repeat

The property that separates a hosted prototype from a production system.

Your code lives in a repository. A deployment is built from a specific commit. The build command and the environment variables are recorded in configuration rather than in somebody's memory. And the same process produces the same result whether it runs today or in six months.

That gives you three things immediately: a way back to the previous version when a change goes wrong, the ability to have a staging environment that behaves like production, and the ability for someone other than you to deploy. It also means an agent session that breaks something is a revert rather than an afternoon.

## The Things the Prototype Never Had

Moving is the natural moment to add what was never there, because all of it is configuration rather than code.

A custom domain with HTTPS, so what you send to customers is your own address. Error tracking, so failures reach you rather than the browser console of a customer who will not mention it. Uptime monitoring. Security headers, which most static hosts offer as configuration. Caching rules so returning visitors are not re-downloading your bundle. And backups for the database, verified by restoring one.

An afternoon in total, and it converts a prototype into something you can point a business customer at.

## What to Check Before Announcing the New Address

The application loads on the custom domain with a valid certificate on both the www and bare versions. No privileged key appears anywhere in the downloaded files — check by searching the page source. Data written through the live site persists across a redeploy. Uploads survive too. Webhooks reach the deployed address and are verified. Scheduled work runs where it should. An error appears in your error tracker within a minute of being triggered. And you know how to roll back.

## Staging, Previews, and Not Testing on Customers

Once the deploy is repeatable, you get something the prototype never offered: the ability to see a change working before anybody else does.

**A staging environment** is a second deployment of the same code, with its own database, that nobody outside your team uses. It costs little — static hosting is cheap and a small database tier is usually enough — and it is where you check that a change works against realistic data before it reaches the live site.

Give it its own data rather than pointing it at production. A staging environment connected to the live database means a test that deletes something deletes it for a customer, and it means anybody with staging access can read real personal data. Use an anonymised copy: real structure, real volume, fictional people.

**Block it from search engines,** with a robots file and ideally a password. A staging site indexed alongside your real one competes with it, and visitors occasionally land on the wrong version of your product.

**Preview deployments per branch,** which most platforms offer automatically, are the refinement that makes this pleasant. Each change gets its own temporary address you can open, check and share with a colleague — and it disappears when the change is merged. For a founder working with agent sessions this is particularly valuable, because a session's output can be looked at in a browser before it goes anywhere near customers.

**Keep the promotion step deliberate.** Staging is where you decide something is ready; production is where you publish that decision. A pipeline that deploys to production automatically on every commit is appropriate for a mature product with tests, and premature for one without — because at that stage the only test is you looking at it.

The whole arrangement takes an afternoon to set up and removes the category of incident where a customer discovers your change before you do.

## Moving a Bolt Project Properly

For a working prototype this is bounded work rather than a rebuild: the code moved into a repository you own with a reproducible build, the frontend deployed to a static host or platform in an EU region, privileged calls moved server-side with secrets held in the platform rather than the bundle, database and storage moved to a managed service with access rules written and tested, a custom domain with certificates and redirects, error tracking and monitoring configured, deployment made repeatable with a rollback path, and backups verified by a restore.

LaunchStudio does this without touching the interface Bolt generated, and leaves the project conventional so you can keep iterating. The engineers are Manifera's: eleven years of production deployment for clients including Vodafone, TNO and CFLW, from Amsterdam Herengracht 420 and Ho Chi Minh City.

[Send us your Bolt project](https://launchstudio.eu/en/#contact) and you will get a specific plan, usually within one business day, or see what the [Launch Ready package](https://launchstudio.eu/en/#packages) covers.

## Real example

### A Market-Stall Booking System Living in a Preview Tab

Luuk Hendrickx built Standplaats with Bolt: pitch booking for weekly markets, used by two municipalities and three market organisers around Venray and Horst. Traders book a stall, organisers assign pitches, and invoices follow.

Six months after launch it was still running from the Bolt preview environment. The address he gave traders contained the platform's name and a random string. He avoided editing anything on Thursday and Friday because the markets ran at weekends and his changes were immediately live. Twice, a trader had reported that the site "was not there", which corresponded to times when Luuk had closed his laptop.

Two further problems surfaced during the assessment. A mapping API key used to draw pitch layouts was in the frontend bundle, public since launch. And uploaded trader documents — insurance certificates and registration numbers — were written into the project directory, which meant an unknown number of them had disappeared during rebuilds. Three organisers had been re-requesting documents periodically and had assumed traders were failing to upload them.

Eight business days of work: the project moved into a repository owned by his company with a reproducible build; the frontend deployed to a static host in an EU region with deployment tied to the repository, a staging environment, and a one-step rollback; mapping calls moved behind a server-side endpoint that authenticates the caller and rate-limits per organiser, with the exposed key rotated, domain-restricted and capped; the database moved to a managed service in an EU region with access rules per organiser, tested from two accounts; trader documents moved into private object storage with signed links, and the missing ones identified by reconciling records against stored files so organisers could re-request precisely rather than broadly; a custom domain configured with certificates and redirects; error tracking, uptime monitoring and security headers added; and backups verified with a restore timed at 14 minutes.

**Result:** no unplanned outages in the eight months since, the mapping bill returned to a predictable figure after the key rotation, and one municipality's contract renewal cited the move to a proper domain and EU-hosted data as a condition that had now been met.

> *"My live product was a browser tab on my laptop. When I closed it on a Friday evening, market traders in Venray could not book a pitch."*
> — **Luuk Hendrickx, Founder, Standplaats (Venray)**

**Cost & Timeline:** €3,700 (repository and reproducible build, static deployment with staging and rollback, server-side proxy and key rotation, database and storage migration, domain, monitoring, backup verification) — completed in 8 business days.

## Frequently Asked Questions

### Can I keep using the Bolt preview link for customers?

No. That address belongs to your working environment: it changes, it can stop when you do, and it reflects whatever you are currently editing. Deploy a built version to your own domain.

### Where should a Bolt app be hosted?

For most products, the frontend as static files on a static host or platform, with database, authentication and storage from a managed service and any privileged logic as serverless functions. Choose an EU region if you sell to Dutch or EU businesses.

### Why did my API key end up public?

Because anything included in a frontend build is downloadable by any visitor. The prefix build tools require for browser variables declares a value public rather than protecting it. Privileged keys must live only in server-side code.

### What does a repeatable deploy give me?

A way back to the previous version, a staging environment that behaves like production, the ability for someone else to deploy, and a revert rather than an afternoon when an agent session breaks something.

### What should I add while moving?

A custom domain with HTTPS, error tracking, uptime monitoring, security headers, caching rules and verified database backups. All configuration rather than code, and roughly an afternoon in total.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Can I keep using the Bolt preview link for customers?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No — it belongs to your working environment, changes, can stop when you do, and shows whatever you are editing. Deploy a built version to your own domain."
      }
    },
    {
      "@type": "Question",
      "name": "Where should a Bolt app be hosted?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Frontend as static files on a static host or platform, with managed services for database, auth and storage, and serverless functions for privileged logic — in an EU region for EU customers."
      }
    },
    {
      "@type": "Question",
      "name": "Why did my API key end up public?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Anything in a frontend build is downloadable. The browser-variable prefix declares a value public rather than protecting it; privileged keys belong server-side."
      }
    },
    {
      "@type": "Question",
      "name": "What does a repeatable deploy give me?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Rollback, a staging environment that behaves like production, deployment by someone other than you, and recovery from a bad agent session in minutes."
      }
    },
    {
      "@type": "Question",
      "name": "What should I add while moving?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Custom domain with HTTPS, error tracking, uptime monitoring, security headers, caching rules and verified backups — configuration rather than code."
      }
    }
  ]
}
</script>
