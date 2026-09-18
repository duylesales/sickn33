---
Title: "Lovable Hosting: EU Data Residency and Where Your App Actually Runs"
Keywords: lovable hosting, EU data residency, GDPR transfers, regions, subprocessors, data location, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: AI-Native Founder (Non-Technical)
---

# Lovable Hosting: EU Data Residency and Where Your App Actually Runs

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Lovable Hosting: EU Data Residency and Where Your App Actually Runs",
  "description": "Dutch business customers ask where their data is stored, and most AI-built apps cannot answer. How to find out, why the database region is only part of it, and what to do when the honest answer is the wrong one.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-10-27",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/lovable-hosting-eu-data-residency-and-where-your-app-runs" }
}
</script>

The question arrives in an email from a customer's IT or privacy officer, usually while a contract is being reviewed, and it is phrased simply: where is our data stored?

For most founders who built with Lovable, the honest first answer is that they do not know. The database was created by accepting a default. The hosting platform deploys to wherever it deploys. Email goes through a provider whose infrastructure was never considered. And the AI feature added in spring sends customer text to a model API that could be running anywhere.

This is answerable, and answering it well is frequently the difference between winning a Dutch business customer and not. It is also, once you have looked, occasionally a reason to change something.

## Start With the List, Not the Answer

Before deciding anything, write down every service that touches customer data. In a typical AI-built product this is longer than expected.

The database and its backups. Object storage for uploaded files. The application hosting itself, including serverless functions, which may run in a different region from your database. The email provider. Error tracking, which captures request data and sometimes personal details in stack traces. Analytics. The payment provider. Any AI model API. Support tooling. Session recording, if you added it and forgot.

For each, three facts: where the data is processed, where it is stored, and where backups live. All three are published by every reputable provider and none takes long to find.

This list is useful beyond the residency question — it is the register of subprocessors your business customers will ask for anyway, and it is required by the GDPR in substance regardless of who asks.

## The Database Region Is Not the Whole Answer

Founders who look into this usually check the database, find it is in Frankfurt or Amsterdam, and stop.

Three things are commonly missed. Backups may be replicated to a different region than the primary, which is a deliberate resilience feature and a residency question. Serverless functions frequently execute in whichever region is nearest the visitor unless pinned, so your European database is being queried by code running in Virginia. And CDN edge nodes hold cached content worldwide by design — which is fine for public pages and not fine if a personalised response was ever cached.

The functions point causes real latency problems as well: an application deployed globally with a database in one region means every request makes a slow round trip. Pinning functions to the database's region is usually both the compliant answer and the faster one.

## Transfers Outside the EU Are Not Forbidden

It is worth being precise, because founders often believe the rules are stricter than they are.

Personal data may leave the European Economic Area, provided there is a lawful basis for the transfer — an adequacy decision covering the destination country, standard contractual clauses with supplementary measures where needed, or one of the narrow derogations. Most large providers offer the relevant contractual terms as a matter of course.

So "our error tracking is processed in the United States under standard contractual clauses, with personal data scrubbed before transmission" is a legitimate answer. What is not legitimate is not knowing, and what loses contracts is not the transfer but the inability to describe it.

Two practical positions worth distinguishing. A legal requirement to keep data in the EU is rare outside specific sectors. A contractual requirement from a customer — a hospital, a municipality, a bank — is common, and it is negotiated rather than legislated. Knowing which one you face changes what you should do about it.

## Reduce What You Send Before Moving Where You Send It

The cheapest improvement is usually not relocating a service. It is sending it less.

Error tracking configured to scrub personal data before transmission removes most of the concern without changing provider. Analytics configured without personal identifiers becomes a much smaller question. An AI feature that sends only the text needed for the task, rather than a whole record including names and addresses, transfers less and costs less.

This is good practice independent of geography, and it makes the subprocessor conversation shorter, because the honest description becomes "pseudonymised technical data" rather than "customer records".

## When You Do Need to Change Something

Sometimes the answer is genuinely insufficient for the customer in front of you, and something has to move.

Order of difficulty, cheapest first. Pinning serverless functions to a region is usually a configuration line. Changing an email or error tracking provider to an EU-hosted equivalent is a day. Moving object storage is a copy plus a rewrite of how URLs are produced. Moving the database is a migration with a maintenance window. Changing the AI model provider to an EU-region deployment is usually a configuration change with a different endpoint, though it may affect which models are available.

Do them in that order, and check after each one whether the customer's requirement is now satisfied. Frequently it is, two steps in, and the expensive migration is unnecessary.

## Write the Answer Down Before You Are Asked

Prepare a page — a real page on your website, not a paragraph in an email — describing where data is stored, which subprocessors you use, what each receives, and what contractual basis covers any transfer outside the EU.

Three benefits. The sales conversation shortens dramatically, because the procurement officer can read it rather than ask. It signals a level of seriousness that most small competitors do not reach. And writing it forces the inventory to be accurate, which is the part that matters.

Keep it current. A subprocessor page that lists a provider you stopped using two years ago and omits the AI API you added in spring is worse than none, because it is a statement you have made and can be held to.

## The Questions Behind the Question

Residency is rarely the only thing a procurement review wants, and the other items arrive in the same email. Knowing them lets you prepare once rather than three times.

**Who can access the data on your side?** Meaning: how many people at your company can read a customer's records, under what controls, and is that access logged. For a one-person business the honest answer is short, and being able to say "one person, with access recorded, and here is the log" is stronger than a vague reassurance.

**What happens when the contract ends?** Export format, deletion timeline, and confirmation that backups eventually age out. Customers ask because they have been trapped before.

**What is your availability commitment and your incident process?** Not necessarily a formal SLA for a small product, but a stated target and a written description of how you respond and notify.

**Do you use customer data to train models?** Increasingly the first question rather than the last, and the expected answer is no, stated plainly, with the vendor terms to support it — some model APIs behave differently on different tiers, so check rather than assume.

None of these requires a large company to answer well. They require having thought about it before being asked, which is the entire difference between a procurement process that takes two weeks and one that takes two months.

The practical move is to write all five answers into one internal document and keep the customer-facing half of it on your website. Procurement officers are not adversaries; they are people with a checklist who would rather tick it quickly. Give them something to tick.

## Setting This Up

For an existing product this is typically one to two days: an inventory of every service touching customer data with processing, storage and backup locations for each; serverless functions pinned to the database's region; cached content checked so nothing personalised is held at edge nodes; error tracking and analytics configured to scrub or omit personal data; AI features reviewed for what they actually transmit; contractual bases confirmed for transfers outside the EEA; a published subprocessor and data location page; and a note in the repository so the list is updated when a service is added.

LaunchStudio does this as part of preparing a product for business customers, and it is usually the piece that unblocks an enterprise or public sector contract. Behind it is Manifera — eleven years, clients including Vodafone, TNO and CFLW, with European operations from Herengracht 420 in Amsterdam and development in Singapore and Ho Chi Minh City.

[Send us the questionnaire you were sent](https://launchstudio.eu/en/#contact) and we will tell you which answers you already have.

## Real example

### The Municipality's Questionnaire

Hidde Vermaas built Meldpunt in Lovable: a system municipalities use to receive and track public reports about street furniture, lighting and green space maintenance. Eleven smaller municipalities were using it when a larger one began a procurement.

Their questionnaire asked where personal data — reporters' names, addresses, email addresses and free-text descriptions — was stored and processed. Hidde's honest answer required a fortnight of investigation and was less comfortable than he expected.

The Supabase database was in Frankfurt, which was fine. But his serverless functions ran in whichever region was closest to the visitor, so queries were arriving from three continents. His error tracking captured full request bodies including reporters' names and addresses, processed in the United States, with no scrubbing. Uploaded photographs of reported problems were in a storage bucket in a US region, chosen by a default nobody had looked at. And a description-summarising feature added in spring sent the full report text — names included — to a model API with no data processing agreement in place at all.

Six business days: the complete service inventory with processing, storage and backup locations documented; functions pinned to the Frankfurt region, which also cut average response time by 240 milliseconds; error tracking moved to an EU-hosted provider with request body scrubbing configured so personal data is never transmitted; 34,000 photographs migrated to an EU storage region with URL generation rewritten and existing links redirected; the summarisation feature switched to an EU-region model endpoint with a data processing agreement in place, and changed to send only the description text rather than the whole record; a published subprocessor and data location page; and a documented process requiring a residency check before any new service is added.

**Result:** the questionnaire was answered from the published page with two clarifying sentences, and the contract was awarded. Three of the eleven existing municipalities asked for the same document within a month, and Hidde now sends the link before it is requested.

> *"Every one of those defaults was chosen by clicking through a setup screen in an afternoon. None of them was a decision, and all four of them were on the questionnaire."*
> — **Hidde Vermaas, Founder, Meldpunt (Deventer)**

**Cost & Timeline:** €4,200 (service inventory, function region pinning, error tracking migration with scrubbing, storage migration with link redirection, AI endpoint and agreement change with payload reduction, published documentation, process definition) — completed in 6 business days.

## Frequently Asked Questions

### Is it illegal to store EU personal data outside the EU?

No. Transfers are permitted with a lawful basis — an adequacy decision, standard contractual clauses with appropriate measures, or a derogation. What causes problems is not knowing what you do or being unable to describe it.

### Is checking my database region enough?

No. Backups may replicate elsewhere, serverless functions often run near the visitor rather than near the database, and CDN nodes cache worldwide. All three need checking.

### What usually gets missed in the inventory?

Error tracking capturing request bodies, analytics carrying identifiers, AI model APIs added later, and object storage created with a default region nobody chose deliberately.

### Do I need to move everything into the EU?

Usually not. Reduce what you transmit first — scrub personal data from error tracking, send AI features only what they need — then move services in order of cost, checking after each whether the requirement is met.

### Should I publish a subprocessor list?

Yes. It shortens sales conversations with business customers, signals seriousness, and forces your own inventory to be accurate. Keep it current or it becomes a liability.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Is it illegal to store EU personal data outside the EU?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No — transfers are lawful with an adequacy decision, standard contractual clauses or a derogation. The problem is being unable to describe what you do."
      }
    },
    {
      "@type": "Question",
      "name": "Is checking the database region sufficient?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No. Backups may replicate to another region, serverless functions often run near the visitor, and CDN nodes cache worldwide."
      }
    },
    {
      "@type": "Question",
      "name": "What is usually missed when listing where data goes?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Error tracking capturing request bodies, analytics identifiers, AI model APIs added later, and storage buckets created with a default region."
      }
    },
    {
      "@type": "Question",
      "name": "Do I have to move every service into the EU?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Usually not. Reduce what you transmit first, then relocate services in order of cost, checking after each whether the requirement is satisfied."
      }
    },
    {
      "@type": "Question",
      "name": "Should a small product publish a subprocessor list?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. It shortens procurement conversations and forces your own inventory to stay accurate — provided you keep it current."
      }
    }
  ]
}
</script>
