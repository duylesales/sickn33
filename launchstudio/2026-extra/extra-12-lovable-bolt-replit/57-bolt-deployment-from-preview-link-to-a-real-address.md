---
Title: "Bolt Deployment: From Preview Link to a Real Address"
Keywords: bolt deployment, hosting a bolt app, custom domain, environments, CI, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: AI-Native Founder (Non-Technical)
---

# Bolt Deployment: From Preview Link to a Real Address

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Bolt Deployment: From Preview Link to a Real Address",
  "description": "A preview link is fine for showing someone and wrong for running a business. Getting the code out, choosing where it runs, environments, a domain, and a deploy you can repeat and undo.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-01-05",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/bolt-deployment-from-preview-link-to-a-real-address" }
}
</script>

The link Bolt gives you works. You can send it to someone, they can open it, the product runs. For a demonstration this is exactly right and it is the reason the tool is useful.

It is not where a business runs. A preview URL is tied to the tool, it says nothing about your company, it cannot be found in search, and your customers' relationship with your product is mediated by a service they have never heard of and you do not control.

Moving to a real deployment is a day of work and it is the step that turns a prototype into a thing that exists independently.

## Get the Code Into Your Own Repository

Before anything else, own the code.

Export the project and put it in a repository under your own account. This is the single most important step, and it is the one founders postpone — until the afternoon they want to hire someone, change tools, or simply find out what changed last week, and discover that the entire history of their product lives inside somebody else's product.

A repository gives you a history you can read, a place to work from with any tool, a backup that is not a platform's responsibility, and the foundation for everything below. It takes twenty minutes.

While you are there: check what came with it. A repository exported from a prototype frequently contains environment files with live credentials, which should be removed and rotated before the first commit rather than after.

## Choose Where It Runs

For a typical Bolt application — a frontend with serverless functions and a hosted database — the realistic options are the platforms built for exactly that shape: Vercel, Netlify, Cloudflare. All three deploy from a repository, handle SSL and domains, and cost nothing at small scale.

The choice matters less than founders expect. Pick the one whose documentation you find clearest, and be aware of two things: where your functions execute, which should be a region near your database rather than near your visitors, and what your bill does if traffic spikes.

The alternatives — a container on a cloud provider, a virtual server — are more control and more responsibility, and they are rarely the right answer for a product at this stage.

## Three Environments From the Start

Production is what customers use. Staging is a full copy where changes are confirmed working. Development is your machine.

Each needs its own database, its own credentials and its own configuration, with nothing shared. A staging environment pointing at production's database is not a staging environment, and one holding production's email credentials will eventually email your customers.

Set this up at deployment time rather than later. It is fifteen minutes when there is one environment to duplicate and a project once there is history to untangle.

Staging should also be blocked from search engines and, ideally, behind access protection — otherwise you acquire a second copy of your site competing with the first.

## A Domain and What Comes With It

Buy the domain, point it at your deployment, and let the platform issue the certificate.

Three things that are worth doing at the same time and are annoying later. Decide whether you are using the bare domain or the www version, redirect one to the other permanently, and make that decision once. Set up email authentication records — SPF, DKIM and DMARC — before you send your first customer email, because a domain that starts sending without them acquires a reputation that is slow to repair. And keep the domain registration in your own account with the renewal on a card that does not expire quietly.

## Make the Deploy Repeatable and Reversible

The last step, and the one that distinguishes a deployment from a launch.

Deploying should be one action — a push to a branch — that builds and releases without a remembered sequence. Most bad releases at this scale are a forgotten step rather than bad code.

And you should know how to undo it. Find the rollback control on your platform today, while nothing is wrong, deploy something trivial, roll it back, and time it. A rollback you have performed is one you will use; one you have only read about is one you will avoid at the worst moment.

## Keep Using the Tool Afterwards

Deploying properly does not mean abandoning Bolt, and founders sometimes assume it does — as though moving to a repository were a graduation that requires writing everything by hand from then on.

The arrangement that works: the repository is the source of truth, and the tool is one of the ways you change it. Export once, deploy from the repository, and continue using Bolt or any other assistant against that codebase for the things it is good at.

What changes is the direction of authority. Previously the tool held your product and you had a copy; now you hold your product and the tool is something you point at it. That means changes arrive as commits you can read, review and revert, rather than as edits to a workspace with no history.

Two habits make this comfortable. Work on a branch for anything substantial, so a session that goes badly is discarded rather than unpicked. And commit often with messages that say what changed, because the history is the only record of why your product is the way it is — and in a codebase where much of the writing was done by a tool, that record is the difference between a product you can explain and one you can only observe.

The founders who manage this transition well tend to describe the repository as the thing that made them feel the product was theirs. That is not only sentiment; it is the practical difference between an asset and an arrangement.

## What to Check the Day After

A deployment that succeeds is not the same as a deployment that is right, and the differences show up in the first twenty-four hours if anyone looks.

Six checks, each a minute.

Open the product as a customer would, on a phone, from outside your own network. Sign in, do the main thing, and sign out. The number of launches that fail because something worked only on the developer's machine is not small.

Confirm the site is reachable at both the www and bare forms and that one redirects to the other. Confirm the certificate is valid and that there is no mixed-content warning from an asset still loading over HTTP.

Send one real email from the product and check where it lands — inbox or spam — from a Gmail address and an Outlook address, which behave differently.

Check that your error tracking received something, by deliberately triggering an error. A tracker that was configured but is not receiving is the most common silent failure at launch.

Look at what the server returns for a URL that does not exist. It should be a 404, not your application shell returning 200, which quietly tells search engines every mistyped address is a real page.

And confirm your uptime check is actually failing when it should, by pointing it at a deliberately broken path for a minute. A monitor that never alerts is indistinguishable from one that is not running.

Write the six down and repeat them after any significant deployment. They take ten minutes and they catch the class of problem that monitoring does not: things that are broken in a way the system considers normal.

A useful rule to adopt at the same time: do not deploy at a moment when you cannot spend those ten minutes. Most of what goes wrong at launch is found by the person who shipped it, looking — and looking is only possible if you are still there.

## Setting This Up

For a Bolt project going live this is typically one day: the code exported into your own repository with credentials removed and rotated, a hosting platform chosen with functions running near the database, three environments with separate databases and credentials and nothing shared, staging blocked from indexing and behind access protection, a domain with a chosen canonical form and a redirect, SSL issued, email authentication records configured before the first send, deployment automated from a branch push, rollback identified and timed, and basic uptime monitoring pointed at a page that exercises the application.

LaunchStudio does this as part of the Launch Ready package from €800, and operates it afterwards under managed hosting at €49 per month. The engineers are Manifera's — eleven years, 160+ projects, from Herengracht 420 in Amsterdam.

[Send us your Bolt project](https://launchstudio.eu/en/#contact) and we will put it on your own address this week.

## Real example

### A Business Running on a Preview Link

Renske Bouhuijs built Zwemlesplanner with Bolt: lesson scheduling and attendance for swimming schools, which three schools began using within a month because it solved a problem they had.

It ran on the preview URL for five months. Parents received links to that address. The schools bookmarked it. Renske invoiced €45 a month per school and the business, such as it was, existed entirely inside a prototyping tool's preview.

Two things happened in the same week. The preview became unavailable for several hours during a platform incident, with no status page she could point anyone at and no ability to do anything. And a school asked for her company's website before renewing, which did not exist, because the product had no address of its own.

One business day: the project exported into a repository under her own account, with an environment file containing live database credentials removed and those credentials rotated; deployment to a hosting platform from a branch push, with functions pinned to the same region as her Supabase project, which also removed a noticeable delay on every page; three environments created with separate databases and credentials, replacing a single shared one where she had been testing against live data; staging put behind access protection and excluded from indexing; a `.nl` domain bought and pointed at the deployment with SSL, the www form redirecting to the bare domain; SPF, DKIM and DMARC configured before the first lesson reminder went out from the new domain; rollback tested and timed at 35 seconds; and uptime monitoring against a page that exercises a real database query.

**Result:** the three schools renewed and two more joined within a quarter, which Renske attributes partly to having an address that looked like a company. The environment separation also ended a habit she had not recognised as dangerous — testing changes against the live database, which had twice caused visible oddities during a school's lesson hours.

> *"Parents were bookmarking a preview link. When it went down for four hours I had nothing to tell anyone, because the product did not really exist anywhere I controlled."*
> — **Renske Bouhuijs, Founder, Zwemlesplanner (Hoorn)**

**Cost & Timeline:** €1,900 (repository export with credential rotation, hosting deployment with regional function placement, three-environment separation, domain and SSL with canonical redirect, email authentication, automated deploy with tested rollback, uptime monitoring) — completed in 1 business day.

## Frequently Asked Questions

### Can I run a business on a Bolt preview link?

You can, briefly, and it is a poor idea. It is tied to the tool, cannot be found in search, says nothing about your company, and gives you no control during an incident.

### What is the first step?

Export the code into a repository under your own account, removing and rotating any credentials that came with it. Everything else depends on owning the code.

### Which hosting platform should I choose?

Any of the ones built for this shape of application. The choice matters less than running your functions near your database and knowing what your bill does under traffic.

### Do I really need a staging environment?

Once customers depend on the product, yes — with its own database and credentials, blocked from indexing. Testing against live data is the habit it replaces.

### What should I do before sending my first email from a new domain?

Configure SPF, DKIM and DMARC. A domain that starts sending without them acquires a deliverability reputation that takes a long time to repair.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Can I run a business on a Bolt preview link?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Only briefly. It is tied to the tool, invisible to search, carries no brand, and leaves you powerless during an incident."
      }
    },
    {
      "@type": "Question",
      "name": "What is the first step in deploying a Bolt app?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Export the code into your own repository, removing and rotating any credentials included. Everything else depends on owning the code."
      }
    },
    {
      "@type": "Question",
      "name": "Which hosting platform suits a Bolt app?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Any built for frontends with serverless functions. What matters more is running functions near your database and understanding cost under load."
      }
    },
    {
      "@type": "Question",
      "name": "Is a staging environment necessary?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Once customers rely on the product, yes — with its own database and credentials, and blocked from search indexing."
      }
    },
    {
      "@type": "Question",
      "name": "What must be configured before sending email from a new domain?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "SPF, DKIM and DMARC. Sending without them damages deliverability in ways that take a long time to repair."
      }
    }
  ]
}
</script>
