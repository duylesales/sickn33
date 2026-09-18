---
Title: "Data Processing Agreements: What a Lovable App Owner Signs"
Keywords: data processing agreement, verwerkersovereenkomst, subprocessors, audit rights, liability caps, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: SaaS Scale-Up
---

# Data Processing Agreements: What a Lovable App Owner Signs

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Data Processing Agreements: What a Lovable App Owner Signs",
  "description": "The verwerkersovereenkomst is where a founder promises things their product may not do. Which clauses commit you to engineering work, which to negotiate, and how to have your own version ready.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-11-28",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/data-processing-agreements-what-a-lovable-app-owner-signs" }
}
</script>

A processing agreement is not a formality. It is a list of operational commitments, and every clause in it describes something your software must actually be able to do.

Founders sign them quickly, because the contract is the last obstacle before revenue and because the document looks like boilerplate. Then, eighteen months later, a customer invokes a clause and the founder discovers they promised a deletion timeline their product cannot meet, an audit right they cannot support, or a breach notification window they have no way of detecting within.

This article is about reading the document as a specification.

## The Clauses That Are Engineering Work

Six, and each one is a feature request wearing legal clothing.

**Deletion on termination.** Typically 30 to 90 days after the contract ends, covering backups. If your product has no deletion function and your backups have no retention rule, you have committed to work you have not done.

**Data export.** Usually in a structured, commonly used format. A customer entitled to their data in a machine-readable form needs an export you have built, not a database dump you produce by hand.

**Breach notification.** Often "without undue delay" and frequently a specific number of hours — 24 or 48 is common, tighter than the regulator's own 72. To meet it you must be able to detect a breach, which means logging and alerting rather than good intentions.

**Assistance with data subject rights.** You must help the controller answer access, correction and deletion requests, within their timeline. In practice this means the customer-operable functions described elsewhere in this series.

**Security measures.** Frequently an annex listing encryption, access control, logging, backups and testing. Read it and confirm each item is true, because it is the part most easily checked and the part founders sign without looking.

**Subprocessor notification.** You must tell the customer before adding a new one, and they may object. That is a process obligation: a list, a way to notify, and the discipline to do it before rather than after.

## The Clauses Worth Negotiating

A small supplier can negotiate more than founders expect, particularly with a mid-sized Dutch customer who wants the product.

**On-site audit rights.** Many templates allow the customer to audit your premises at any time. For a one-person company this is impractical. A reasonable counter: audits satisfied by documentation and a summary report of your annual security test, with on-site visits limited to once a year with notice and at the customer's cost.

**Unlimited liability.** Uncapped exposure is not something a company of your size can carry, and insurers price it accordingly. A cap tied to fees paid — twelve months' worth is a common landing point — is normal commercial practice.

**Notification windows shorter than you can meet.** If the clause says 24 hours and your detection would realistically take longer, either build the detection or negotiate the window. Signing it and hoping is the worst option.

**Blanket subprocessor veto.** A customer who may object to any new subprocessor can, in effect, freeze your infrastructure. The usual compromise is objection on reasonable grounds, with a route to exit if the objection cannot be resolved.

## Have Your Own Version Ready

The single most useful move is to stop reacting to customers' documents.

Prepare your own processing agreement — in Dutch if you sell to Dutch businesses — reviewed once by a qualified lawyer, reflecting what your product genuinely does. Send it with your proposal, before anyone asks.

Three benefits. It sets the starting position, so negotiation begins from terms you can meet. It shortens the process considerably, since many mid-sized customers will accept a reasonable supplier agreement rather than insist on their own. And it signals maturity that most competitors at your size do not project.

When a customer does insist on their template, read it against your own and negotiate the differences, rather than reading forty clauses cold.

## The Annex Everyone Skips

Most agreements have an annex describing the processing: categories of data subjects, categories of personal data, purposes, retention, and the list of subprocessors with locations.

It is the most useful part of the document and the part most often filled in with a vague sentence. Completing it properly is the same inventory work that everything else in this area requires, and once written it is reusable across every customer.

Keep it current. An annex listing five subprocessors when you use seven is a factual inaccuracy in a signed contract, which is a different category of problem from an out-of-date web page.

## Signing for Multiple Customers at Once

A product with forty customers has forty processing agreements, potentially forty variants, and no realistic way to track who agreed to what.

Two practices keep this manageable. Standardise: one agreement, minimal variation, with any negotiated changes recorded against that customer. And keep a register — customer, version signed, date, deviations, renewal — so that when you change a subprocessor you know who must be notified and under what terms.

The alternative, discovered at scale, is that a change to your infrastructure requires reading forty contracts to find out what you promised.

## The Agreement Is Not the Only Contract

A processing agreement covers personal data. It does not cover several things customers assume it does, and the gaps surface at exactly the wrong moment.

**Availability.** Uptime commitments, planned maintenance and what happens when you miss them belong in the service agreement, not here. A processing agreement can be impeccable while your product is down every Tuesday.

**Support.** Response times, channels, and what counts as an emergency.

**Intellectual property and data ownership.** Who owns the customer's data — them — and who owns the software — you. Stating it plainly prevents an argument that otherwise happens at termination.

**Exit assistance beyond data.** Some customers need help migrating, not just an export file. Whether that is included or billed should be written down before it is requested.

**Price and notice.** Including how much notice you give before a price change, which is the term most often missing from small suppliers' contracts and most often disputed later.

For a product selling to businesses, the sensible package is three short documents sent together: terms of service, a processing agreement, and a one-page service description covering availability and support. Together they are shorter than most single enterprise contracts, and having all three ready converts a legal review from a project into a reading task.

## What the Security Annex Should Say

The annex listing your technical and organisational measures is the clause a customer's IT reviewer reads most carefully, and the one founders most often copy from a template describing a company with a security team.

Write it about what you have. For a small product that genuinely means something like: data encrypted in transit and at rest; access to production restricted to named individuals with multi-factor authentication and recorded access; row-level authorisation enforced in the database; backups encrypted, held under separate credentials, with restores tested twice a year; dependencies scanned automatically with security updates applied within a stated period; structured logging with a stated retention; an annual external security assessment; and a documented incident procedure with named responsibilities.

Every one of those is achievable by a one-person company and every one is checkable. That is the point — an annex a reviewer can verify is worth more than an impressive list they suspect is aspirational.

Two rules. Do not list a measure you do not have, because the annex becomes a contractual promise and the gap between it and reality is exactly what an incident investigation examines. And revisit it annually, because it will drift as your product changes — usually in the direction of being more true, which is a pleasant kind of update to make.

## Setting This Up

For a product selling to businesses this is typically two to four days, most of it inventory rather than drafting: a completed processing annex covering data categories, purposes, retention and subprocessors; your own agreement drafted against what the product actually does and reviewed once by a qualified lawyer; each operational clause checked against real capability — deletion, export, breach detection, rights assistance, security measures; negotiation positions prepared for audits, liability, notification windows and subprocessor objections; a register of signed agreements with versions and deviations; and a notification process for subprocessor changes.

LaunchStudio builds the capabilities the agreement commits you to, which is the half that lawyers do not cover. Behind the work is Manifera — eleven years, 160+ projects, contracting with European enterprises including Vodafone, TNO and CFLW from Herengracht 420 in Amsterdam.

[Send us the agreement you were asked to sign](https://launchstudio.eu/en/#contact) and we will tell you which clauses your product cannot currently honour.

## Real example

### A Clause Invoked Two Years Later

Annemieke Vervoort built Leerlingdossier in Lovable: pupil administration and progress tracking for private tutoring organisations, 28 organisations covering about 4,000 pupils.

She had signed each customer's own processing agreement without much scrutiny, because each arrived at the end of a sales process she did not want to delay. Twenty-eight agreements, at least nine variants, none tracked.

Two years in, a tutoring group terminated and invoked their clause: all personal data deleted within 30 days including backups, with written confirmation of completion.

Her product had no deletion function. Data for that group was interleaved with everyone else's across fourteen tables. Her backups had no retention limit and went back to launch. And the clause she had signed — which she read properly for the first time that week — also specified an independent audit right and notification of any breach within 24 hours.

Six business days: a deletion function operating per organisation across all tables, with a documented distinction between records deleted, records anonymised for statistical continuity, and invoices retained under tax obligations; backup retention set to 90 days with an automated rule, and a documented procedure ensuring deleted data is not reintroduced by a restore; a completion certificate generated automatically; an export function producing a structured archive, since two other agreements required one; all 28 agreements read and their obligations tabulated, which found four different deletion windows, three notification periods and two audit rights she could not have supported; her own processing agreement drafted in Dutch and reviewed by a privacy lawyer; a register of signed agreements with versions and deviations; and breach detection improved to make a 24-hour notification realistic rather than aspirational.

**Result:** the deletion was completed within the window with a certificate the customer accepted. Of the 28 customers, 19 have since moved to her standard agreement at renewal. Annemieke's estimate is that reading the contracts before signing would have taken four hours across two years, against six days of remediation under a deadline.

> *"Every one of those agreements was a list of things my software had to be able to do. I signed twenty-eight of them without checking whether it could do any of them."*
> — **Annemieke Vervoort, Founder, Leerlingdossier (Tilburg)**

**Cost & Timeline:** €4,600 (per-organisation deletion with anonymisation and retention rules, backup retention and restore procedure, completion certificates, structured export, contract obligation review across 28 agreements, own agreement drafting and legal review, agreement register, breach detection) — completed in 6 business days.

## Frequently Asked Questions

### Can a small supplier negotiate a processing agreement?

Yes, more than founders expect. On-site audit rights, uncapped liability, notification windows you cannot meet and blanket subprocessor vetoes are all routinely adjusted for suppliers the customer wants.

### Should I use my own agreement or the customer's?

Your own, sent with the proposal. It starts from terms you can meet, shortens the process, and many mid-sized customers accept a reasonable supplier version.

### Which clauses require actual engineering?

Deletion on termination including backups, structured export, breach notification within a fixed window, assistance with data subject rights, the security measures annex, and subprocessor notification.

### What if I have already signed agreements I cannot meet?

Tabulate the obligations across every signed contract, identify the strictest of each, and build to that. Then move customers to your own standard version at renewal.

### How do I handle subprocessor changes across many customers?

Keep a register of who signed which version with what deviations, and a notification process. Without it, changing a provider means reading every contract to find out what you promised.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Can a small supplier negotiate processing agreement terms?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. On-site audits, uncapped liability, unmeetable notification windows and blanket subprocessor vetoes are commonly adjusted."
      }
    },
    {
      "@type": "Question",
      "name": "Should I supply my own processing agreement?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes — sent with the proposal, in Dutch for Dutch customers. It starts from terms you can meet and shortens procurement."
      }
    },
    {
      "@type": "Question",
      "name": "Which processing agreement clauses require engineering?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Deletion on termination including backups, structured export, breach notification windows, data subject rights assistance, the security annex and subprocessor notification."
      }
    },
    {
      "@type": "Question",
      "name": "What if I signed agreements my product cannot honour?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Tabulate obligations across all contracts, build to the strictest of each, then migrate customers to your standard version at renewal."
      }
    },
    {
      "@type": "Question",
      "name": "How do I manage subprocessor changes across many customers?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Keep a register of versions, dates and deviations plus a notification process, so a provider change does not mean re-reading every contract."
      }
    }
  ]
}
</script>
