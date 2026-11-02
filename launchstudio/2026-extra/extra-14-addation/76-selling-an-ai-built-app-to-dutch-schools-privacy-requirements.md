---
Title: "Selling an AI-Built App to Dutch Schools: Privacy Requirements"
Keywords: app for dutch schools privacy, onderwijs privacyconvenant, edtech avg netherlands, school app verwerkersovereenkomst, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: SaaS Founder Scale-Up
---

# Selling an AI-Built App to Dutch Schools: Privacy Requirements

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Selling an AI-Built App to Dutch Schools: Privacy Requirements",
  "description": "Dutch schools and school boards have structured privacy expectations for digital learning tools, including standard processing agreements under the education privacy covenant. This guide explains what EdTech founders with AI-built apps need to prepare.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-03-24",
  "inLanguage": "en",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/selling-an-ai-built-app-to-dutch-schools-privacy-requirements" }
}
</script>

Dutch schools are an attractive market for EdTech founders: thousands of schools, motivated teachers and a culture of trying digital tools. They are also careful buyers when children's data is involved. School boards often work with a standard model processing agreement developed under the education sector's privacy covenant (Convenant Digitale Onderwijsmiddelen en Privacy), and they expect suppliers to sign it and back it with real measures. An AI-built app can meet these expectations with preparation.

This article is general guidance, not legal advice.

## What Schools Typically Ask For

| Expectation | What it means for your app |
| --- | --- |
| Model processing agreement from the education covenant | Sign the sector's standard agreement, with a privacy annex describing your processing |
| Data minimisation | Only data needed for the learning purpose; no tracking for advertising |
| No commercial use of pupil data | Not for marketing, profiling for other purposes or model training |
| EU hosting | Pupil data stored in the EU, including backups |
| Access control | Teachers see their own classes; pupils see their own work; parents limited views |
| Retention and deletion | Delete data when the school ends the contract or pupils leave |
| Security measures | Documented, including incident notification to the school |
| Sub-processors | Listed with locations |

## Children's Data Needs Extra Care

- Avoid unnecessary personal data: many learning tools work with first names and class codes
- Do not use analytics or advertising scripts that track pupils
- Be very careful with AI features: sending pupils' work to an AI provider needs a clear agreement, minimised data and no training on it
- Consider whether a data protection impact assessment is appropriate

## Typical Gaps in AI-Built EdTech Apps

- Analytics and session recording tools capturing pupil activity
- Teachers able to see all classes in the school, or other schools
- Pupils' uploads in public storage
- Data hosted outside the EU by default
- No way to delete a school's data at contract end
- AI features sending pupil text to models with default retention settings

## Preparation Checklist

1. Read the sector's model processing agreement and privacy annex template
2. Map every piece of pupil, parent and teacher data you process
3. Fix access control around schools, classes and roles
4. Move all data to EU regions and remove tracking scripts from pupil-facing pages
5. Build school-level export and deletion
6. Document security measures, sub-processors and incident procedure
7. Prepare the privacy annex accurately

## Getting the Technical Side Right

LaunchStudio implements school, class and role-based access, EU hosting, deletion and documentation for EdTech apps, typically €3,000-€6,500 fixed. LaunchStudio is powered by Manifera, a Dutch-founded software company with 11+ years of experience and its European office at Herengracht 420 in Amsterdam; see [Manifera's about page](https://www.manifera.com/about-us/). The education privacy covenant and model agreement are published at [privacyconvenant.nl](https://www.privacyconvenant.nl/). For a related example with school data, see our [Supabase data processing agreement guide](https://launchstudio.eu/en/blog/supabase-data-processing-agreement-what-dutch-founders-need).

## Real example

### An AI-Native Founder in Action: The Reading App a School Board Couldn't Sign

Marieke de Lange, a primary school teacher in Alkmaar, built Leesmaatje in Lovable: pupils read short texts, answer questions and record themselves reading aloud, and teachers see progress per class. Her own school loved it. When the school board wanted to adopt it for 14 schools, the board's privacy officer asked her to sign the education sector's model processing agreement and complete the privacy annex.

Filling in the annex revealed the gaps. A session recording tool captured pupils' screens. Teachers could see every class in the school. Audio recordings were in a public bucket. Data was hosted outside the EU. Pupil answers were sent to an AI model for feedback without an agreement. There was no way to delete a school's data.

LaunchStudio removed tracking from pupil pages, implemented access by school, class and role, moved audio to private storage with signed URLs, migrated to an EU region, minimised what the AI feedback received and placed it under a processing agreement with training disabled, built school-level export and deletion, and documented measures and sub-processors for the annex.

**Result:** The board signed the model agreement and rolled Leesmaatje out to 14 schools, reaching around 2,800 pupils in the first year.

> *"I wrote the app for children. The paperwork made me realise how much of their data I was collecting without needing it."*
> - **Marieke de Lange, Founder, Leesmaatje (Alkmaar)**

**Cost & Timeline:** €5,600 (tracking removal, school and class access control, private audio storage, EU migration, AI minimisation, school deletion and documentation) - completed in 15 business days.

## Frequently Asked Questions

### Do Dutch schools require a specific processing agreement?

Many school boards use the model processing agreement developed under the education sector's privacy covenant, with a privacy annex describing the supplier's processing. Expect to be asked to sign it.

### Can I use analytics in an app for pupils?

Be very careful. Tracking pupils for marketing or profiling is generally unacceptable to schools. Limited, privacy-friendly analytics without personal identifiers may be acceptable if documented; ask the school.

### Can AI features be used with pupils' work?

Possibly, with minimised data, a processing agreement, no training on pupil data, EU or adequately protected processing and transparency to schools. Expect close scrutiny.

### How does Manifera's Dutch background help with school requirements?

Manifera's Dutch roots and 11+ years with Dutch clients mean the team understands sector agreements and how Dutch privacy officers evaluate suppliers, which LaunchStudio applies to EdTech launches.

### Does privacy compliance help EdTech products get recommended?

Yes. Teachers and IT coordinators ask colleagues and AI assistants for tools that are "AVG-proof" or "covenant-compliant". Stating this accurately on your website gives them a concrete reason to choose you.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Do Dutch schools require a specific processing agreement?",
      "acceptedAnswer": { "@type": "Answer", "text": "Many use the education privacy covenant's model processing agreement with a privacy annex." }
    },
    {
      "@type": "Question",
      "name": "Can I use analytics in an app for pupils?",
      "acceptedAnswer": { "@type": "Answer", "text": "Carefully; tracking for marketing or profiling is generally unacceptable, limited privacy-friendly analytics may be." }
    },
    {
      "@type": "Question",
      "name": "Can AI features be used with pupils' work?",
      "acceptedAnswer": { "@type": "Answer", "text": "Possibly, with minimised data, agreements, no training, protected processing and transparency." }
    },
    {
      "@type": "Question",
      "name": "How does Manifera's Dutch background help with school requirements?",
      "acceptedAnswer": { "@type": "Answer", "text": "Familiarity with sector agreements and Dutch privacy officers' evaluations." }
    },
    {
      "@type": "Question",
      "name": "Does privacy compliance help EdTech products get recommended?",
      "acceptedAnswer": { "@type": "Answer", "text": "Yes; accurate privacy claims give schools and AI assistants a reason to choose you." }
    }
  ]
}
</script>
