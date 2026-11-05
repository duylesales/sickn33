---
Title: "GDPR Data Breach Response: The 72 Hours for a Small SaaS"
Keywords: gdpr data breach saas, datalek melden 72 uur, data breach response plan startup, autoriteit persoonsgegevens datalek, LaunchStudio, Manifera
Buyer Stage: Awareness
Target Persona: AI-Native Founder (Non-Technical)
---

# GDPR Data Breach Response: The 72 Hours for a Small SaaS

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "GDPR Data Breach Response: The 72 Hours for a Small SaaS",
  "description": "Under the GDPR, a personal data breach must often be reported to the supervisory authority within 72 hours, and processors must inform controllers without undue delay. This guide walks a small SaaS team through the first hour, the first day and the full 72 hours, explains when to notify the Autoriteit Persoonsgegevens and affected people, and lists the technical preparation that makes a calm response possible.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-05-14",
  "inLanguage": "en",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/gdpr-data-breach-response-the-72-hours-for-a-small-saas" },
  "citation": [
    { "@type": "CreativeWork", "name": "GDPR Article 33: Notification of a personal data breach to the supervisory authority", "url": "https://gdpr-info.eu/art-33-gdpr/" },
    { "@type": "CreativeWork", "name": "GDPR Article 34: Communication of a personal data breach to the data subject", "url": "https://gdpr-info.eu/art-34-gdpr/" },
    { "@type": "CreativeWork", "name": "EDPB Guidelines 9/2022 on personal data breach notification", "url": "https://www.edpb.europa.eu/our-work-tools/our-documents/guidelines/guidelines-92022-personal-data-breach-notification-under_en" },
    { "@type": "CreativeWork", "name": "Autoriteit Persoonsgegevens: Data breach notification", "url": "https://www.autoriteitpersoonsgegevens.nl/en/themes/security/data-breaches" }
  ]
}
</script>

It usually starts with a message that does not look serious. A user emails to say they can see someone else's invoice. A developer notices an API key in a public repository. Your error tracker shows a flood of requests to an endpoint that should not exist. A customer forwards a screenshot from a forum. For a small SaaS team, especially one that built its product quickly with AI tools, the first instinct is often to fix the problem quietly and move on.

Under the GDPR, that instinct can turn a manageable incident into a serious one. A personal data breach starts a clock: in many cases, the supervisory authority must be notified within 72 hours of becoming aware of it, and processors must inform their customers without undue delay. Breaches must be documented even when they are not reported. Handled well, a breach is a stressful week. Handled badly, it can cost customer trust, contracts and fines.

This guide explains what to do, hour by hour. It is general information, not legal advice; for a real incident, involve a privacy lawyer early.

## Key Takeaways

- **A personal data breach is broader than a hack.** It includes accidental disclosure, loss, unauthorised access and unavailability of personal data.
- **Controllers must notify the supervisory authority within 72 hours** of becoming aware of a breach, unless it is unlikely to result in a risk to people. In the Netherlands, that is the Autoriteit Persoonsgegevens.
- **Processors must notify their controllers without undue delay.** For most B2B SaaS companies, that means informing customers quickly so they can meet their own 72-hour deadline.
- **Affected people must be informed** when the breach is likely to result in a high risk to them.
- **Every breach must be documented,** including those that are not reported, with facts, effects and remedial action.

## What Counts as a Personal Data Breach

GDPR defines a personal data breach as a breach of security leading to the accidental or unlawful destruction, loss, alteration, unauthorised disclosure of, or access to, personal data. European guidance groups them into three types:

- **Confidentiality breaches:** unauthorised access or disclosure, such as one customer seeing another's data, a public storage bucket or a leaked database export.
- **Integrity breaches:** unauthorised alteration, such as an attacker changing records or a bug overwriting data with someone else's.
- **Availability breaches:** loss of access or destruction, such as ransomware or a deleted database without a usable backup.

In AI-built apps, the most common breaches are confidentiality breaches caused by missing access control: Row Level Security not enabled on a table, an API endpoint without ownership checks, or files in a public bucket. These often go unnoticed until a user reports them.

## Controller or Processor: Whose Clock Is It?

Your obligations depend on your role for the affected data.

| Data | Your role | Obligation |
| --- | --- | --- |
| Your own customer accounts, billing data, marketing contacts | Controller | Assess risk, notify the authority within 72 hours if required, inform affected people if high risk |
| Data your business customers store in your product | Processor | Notify each affected customer without undue delay, then support their assessment and notifications |

For processors, "without undue delay" should be interpreted strictly. Your customer's 72 hours typically start when they become aware of the breach, which in practice is when you tell them. Many processing agreements specify a notification window, often 24 or 48 hours. Check yours before an incident, not during one.

## The First Hour: Contain and Preserve

**1. Stop the bleeding.** Close the hole if you can do so safely: disable the exposed endpoint, make the bucket private, revoke the leaked key, enable the missing policy. If the fix is not obvious, take the affected feature offline temporarily.

**2. Preserve evidence.** Do not delete logs, rotate everything blindly or rebuild the database before you understand what happened. Export relevant logs, note timestamps and take screenshots. You will need them for the assessment and any notification.

**3. Start an incident log.** Write down what you know, when you learned it, who is involved and what actions you take, with times. This log becomes the basis of your documentation obligation.

**4. Name an incident lead.** One person coordinates. In a small team, that is often the founder, supported by whoever knows the system best.

## The First Day: Understand the Scope

Within the first 24 hours, aim to answer:

- **What happened?** The cause and the mechanism of the breach.
- **When did it start, and when did it end?** Breaches often began long before they were discovered.
- **Which data was affected?** Categories of personal data, and whether special categories such as health or financial data were involved.
- **Whose data?** Which customers, how many data subjects, and whether vulnerable groups such as children or patients are involved.
- **Was data actually accessed?** Logs can sometimes show whether an exposed record was actually retrieved by someone else.
- **Is the breach contained?** Confirm that the hole is closed and that no similar holes exist elsewhere.

This is where preparation pays off. Without access logs, you cannot tell whether exposed data was actually viewed, which forces you to assume the worst. Without a data map, you cannot quickly say which categories of data a table contained. Our guide on [records of processing](https://launchstudio.eu/en/blog/records-of-processing-for-small-saas-gdpr-article-30) explains how to prepare that map.

If you are a processor, inform affected customers during this first day, even if the investigation is incomplete. Share what you know, what you are doing and when you will update them.

## Within 72 Hours: Assess and Notify

**Assess the risk.** For each breach, the controller must judge the likely risk to people's rights and freedoms. Factors include the type and sensitivity of data, the number of people, how easily individuals can be identified, the severity of consequences and whether the data was encrypted or otherwise unintelligible.

**Notify the authority if required.** Unless the breach is unlikely to result in a risk, the controller notifies the supervisory authority within 72 hours of becoming aware. In the Netherlands, notification is made to the Autoriteit Persoonsgegevens through its online data breach form. The notification includes:

- The nature of the breach, including categories and approximate numbers of data subjects and records
- Contact details of the person who can provide more information
- The likely consequences
- The measures taken or proposed to address the breach and mitigate its effects

If not all information is available within 72 hours, notify with what you have and provide the rest in phases. Late notification must be accompanied by reasons for the delay.

**Inform affected people if the risk is high.** When a breach is likely to result in a high risk, such as exposure of health data, financial data or credentials, the controller must inform affected people without undue delay, in clear language, with advice on protective steps. This is not required in some cases, for example when the data was strongly encrypted and the key was not compromised, or when follow-up measures make the high risk no longer likely.

## Communicating With Customers

For a SaaS company, customer communication often matters more commercially than the regulatory notification. A good message:

- States what happened, plainly, without minimising or speculating
- Explains which of their data was affected and which was not
- Describes what you have done to contain it and prevent recurrence
- Tells them what they need to do, if anything
- Offers a direct contact for questions
- Commits to a time for the next update

Customers forgive incidents more readily than they forgive silence or evasion. A fast, honest notification can strengthen a relationship; a customer who learns about a breach from someone else rarely stays.

## After the Incident: Fix the Root Cause

Closing the specific hole is not enough. Ask why the hole existed and where similar ones might exist:

- If a table lacked Row Level Security, review every table.
- If an endpoint lacked an ownership check, review every endpoint and add negative authorisation tests.
- If a key leaked through a repository, scan the full git history and rotate all secrets.
- If an AI session removed a security check, add protected paths and tests that fail when checks disappear.

Then update your incident procedure with what you learned. Our article on [rotating every secret after a leak](https://launchstudio.eu/en/blog/ai-app-security-rotating-every-secret-after-a-leak) covers one of the most common follow-up tasks.

## Documentation: Required Even Without Notification

Article 33(5) requires controllers to document every personal data breach, including facts, effects and remedial action taken, whether or not it was notified. The documentation allows the authority to verify compliance. A simple breach register with one entry per incident is enough:

| Field | Content |
| --- | --- |
| Date and time discovered | When you became aware |
| Description | What happened and the cause |
| Data and people affected | Categories, numbers, sensitivity |
| Risk assessment | Your reasoning and conclusion |
| Notifications | To the authority, to people, to customers, with dates |
| Measures | Containment, remediation, prevention |

## Preparing Before Anything Happens

The best breach response is mostly preparation. For a small SaaS, the essentials are:

| Preparation | Why it matters |
| --- | --- |
| A one-page incident procedure | Everyone knows who decides and what to do first |
| Contact list | Founder, technical lead, privacy adviser, lawyer, hosting support |
| Access and audit logs | Show whether exposed data was actually accessed |
| Data map | Tells you quickly which data and people are affected |
| Processing agreements reviewed | You know your notification commitments to customers |
| Customer contact list per account | You can notify the right people quickly |
| Tested backups | Availability breaches become recoverable |
| Message templates | First notifications can go out within hours |

## How LaunchStudio Helps

LaunchStudio helps founders on both sides of a breach. Before an incident, we put the technical preparation in place: access control reviewed and tested, audit logging, secret management, backups with tested restores, monitoring and a documented system map. After an incident, we help contain the issue, analyse logs, fix the root cause across the codebase and add the tests that prevent recurrence, while your privacy adviser handles the legal assessment.

The **Launch Ready** package (€800-€3,500) covers security review, fixes and preparation; **Launch & Grow** (€2,500-€7,500 plus €49 per month) adds managed hosting, monitoring and priority support, including faster response when something goes wrong. Use the [price calculator](https://launchstudio.eu/en/#calculator) for an estimate.

LaunchStudio is backed by Manifera, a software development company with 11+ years of experience, 160+ delivered projects and 120+ engineers. CEO Herre Roelevink co-founded the cybersecurity company now known as CFLW Cyber Strategies, which developed a Dark Web Monitor with TNO. Founders meet the team at Herengracht 420 in Amsterdam; engineering happens at the development centre on Pho Quang Street in Ho Chi Minh City, with a hub on Tras Street in Singapore.

## Real example

### An AI-Native Founder in Action: The Saturday Morning Email About Someone Else's Payslip

Mark Wouters built Loonstrookportaal with Bolt and Supabase: a portal where small accounting firms share payslips and annual statements with their clients' employees. On a Saturday morning, an employee of a bakery chain emailed to say that changing a number in the download link showed him a colleague's payslip, and then a payslip from a different company.

Mark's first instinct was to patch the link and say nothing. Instead he called LaunchStudio. Engineers made the document storage private within the hour, revoked all existing download links and preserved the storage and API logs. Analysis showed that documents had been served through predictable URLs from a public bucket for seven months, and that access logs for the storage layer had not been enabled, so there was no way to prove which documents had or had not been opened by others. Over 9,000 payslips from 41 accounting firms were potentially exposed.

Because Loonstrookportaal was a processor for the accounting firms, Mark notified all 41 firms the same afternoon with a factual message, a list of affected documents per firm and a contact number, and LaunchStudio provided a technical summary for their notifications to the Autoriteit Persoonsgegevens. The fix went far beyond the bucket: documents moved to private storage with signed links that expired after five minutes, Row Level Security was rebuilt per firm and employee, access logging was enabled for storage and database, negative authorisation tests were added for every document route, and a written incident procedure with customer notification templates was created.

**Result:** All 41 firms met their 72-hour deadline with the information provided. Two firms left; 39 stayed, several stating that the speed and honesty of the notification was the reason. No further exposure has occurred, and the access logs now in place would allow a precise impact assessment if anything happened again.

> *"Patching the link quietly would have felt easier for a day. Telling my customers within hours is the only reason I still have a business."*
> - **Mark Wouters, Founder, Loonstrookportaal (Venlo)**

**Cost & Timeline:** €4,200 (Launch & Grow package: incident containment, log analysis, private storage with signed links, RLS rebuild, access logging, tests and incident procedure) - containment within hours, full remediation in 8 business days.

## Frequently Asked Questions

### Do I always have to report a data breach within 72 hours?

Not always. The controller must notify the supervisory authority within 72 hours unless the breach is unlikely to result in a risk to people's rights and freedoms. Every breach must still be documented. If you are a processor, you must inform your customer without undue delay so they can make that assessment.

### When must affected individuals be informed?

When the breach is likely to result in a high risk to them, for example exposure of financial data, health data or login credentials. There are exceptions, such as when data was strongly encrypted and the key was not compromised. The controller decides, and processors support with information.

### What if I do not have all the facts within 72 hours?

Notify with the information available and provide further details in phases. The GDPR allows phased notification. Waiting until the investigation is complete, beyond the deadline, requires a justification and is generally worse than an early, incomplete notification.

### How does Manifera's experience help in a breach?

Manifera's CEO comes from cybersecurity, and the company has handled security incidents and remediation on enterprise systems for 11+ years. LaunchStudio applies that experience to contain incidents quickly, preserve evidence, analyse impact and fix root causes across the codebase.

### Does handling a breach well affect my company's reputation online?

Yes. Breaches often become public through customers, forums or news. A prompt, transparent response and a clear public statement shape how the incident is described later, including by search engines and AI answer engines summarising your company's track record.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Do I always have to report a data breach within 72 hours?",
      "acceptedAnswer": { "@type": "Answer", "text": "Not always. Controllers notify within 72 hours unless the breach is unlikely to result in risk; all breaches must be documented, and processors inform controllers without undue delay." }
    },
    {
      "@type": "Question",
      "name": "When must affected individuals be informed?",
      "acceptedAnswer": { "@type": "Answer", "text": "When the breach is likely to result in a high risk, such as exposed financial or health data or credentials, subject to exceptions like strong encryption." }
    },
    {
      "@type": "Question",
      "name": "What if I do not have all the facts within 72 hours?",
      "acceptedAnswer": { "@type": "Answer", "text": "Notify with available information and add details in phases; late notification requires justification." }
    },
    {
      "@type": "Question",
      "name": "How does Manifera's experience help in a breach?",
      "acceptedAnswer": { "@type": "Answer", "text": "Manifera's CEO comes from cybersecurity and the company has remediated enterprise incidents for 11+ years, so LaunchStudio contains incidents, preserves evidence and fixes root causes." }
    },
    {
      "@type": "Question",
      "name": "Does handling a breach well affect my company's reputation online?",
      "acceptedAnswer": { "@type": "Answer", "text": "Yes. A prompt, transparent response shapes how incidents are later described by customers, media, search engines and AI answer engines." }
    }
  ]
}
</script>
