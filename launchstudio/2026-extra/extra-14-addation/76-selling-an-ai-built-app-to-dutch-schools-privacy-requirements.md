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
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/selling-an-ai-built-app-to-dutch-schools-privacy-requirements" },
  "citation": [
    { "@type": "CreativeWork", "name": "Privacyconvenant onderwijs", "url": "https://www.privacyconvenant.nl/" },
    { "@type": "CreativeWork", "name": "GDPR Article 8: Conditions applicable to child's consent", "url": "https://gdpr-info.eu/art-8-gdpr/" },
    { "@type": "CreativeWork", "name": "GDPR Article 28: Processor", "url": "https://gdpr-info.eu/art-28-gdpr/" },
    { "@type": "CreativeWork", "name": "EU Artificial Intelligence Act", "url": "https://artificialintelligenceact.eu/" },
    { "@type": "CreativeWork", "name": "Autoriteit Persoonsgegevens", "url": "https://www.autoriteitpersoonsgegevens.nl/en" }
  ]
}
</script>

Dutch schools are an attractive market for EdTech founders: thousands of schools, motivated teachers and a culture of trying digital tools. They are also careful buyers when children's data is involved. School boards often work with a standard model processing agreement developed under the education sector's privacy covenant (Convenant Digitale Onderwijsmiddelen en Privacy), and they expect suppliers to sign it and back it with real measures. An AI-built app can meet these expectations with preparation.

This article is general guidance, not legal advice.

## Key Takeaways

- **Dutch schools and school boards often use the education sector's model processing agreement** under the Convenant Digitale Onderwijsmiddelen en Privacy, with a privacy annex describing your processing.
- **Children's data requires extra care:** minimisation, no tracking for commercial purposes and no use for model training.
- **Technical expectations include EU hosting, access by school, class and role, deletion at contract end and documented security measures.**
- **AI features processing pupils' work need agreements, minimisation and transparency,** and some educational AI uses are considered high-risk under the EU AI Act.
- **Preparation shortens procurement:** schools appreciate suppliers who arrive with an accurate privacy annex and clear answers.

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

## How Dutch Schools Buy Digital Tools

Dutch primary and secondary schools are typically part of school boards, which handle procurement and privacy for multiple schools. Teachers often discover tools first and then involve the board's privacy officer or ICT coordinator. That officer evaluates whether the supplier processes pupil data lawfully and securely. The education sector developed a covenant on digital learning materials and privacy, with a model processing agreement and privacy annex, to make these evaluations consistent. Suppliers who sign the model agreement and fill in the annex accurately make the board's job easier.

## The Privacy Annex in Practice

The privacy annex describes, for your specific product, what data you process, for which purposes, where, by which sub-processors, with which security measures, how long you retain data and how deletion works. It is effectively a structured description of your app's data flows. Founders often discover gaps while filling it in: tracking scripts they forgot, a region outside the EU or no deletion process. Treat the annex as a design checklist, not just paperwork.

## Children's Data Under the GDPR

The GDPR recognises that children merit specific protection, because they may be less aware of risks. Article 8 sets conditions for consent by children for information society services, and recital 38 explains the need for special protection, especially for marketing and profiling. For school tools, the school usually determines the legal basis for processing, and your role is typically that of a processor following the school's instructions. In practice: collect only what is needed for learning, do not use data for marketing or profiling, do not train models on pupils' data and keep everything secure and deletable.

## Access Control for Schools

School data has a natural hierarchy: board, school, class, teacher, pupil and sometimes parent. Model it explicitly:

| Role | Typical access |
| --- | --- |
| Board admin | Configuration across schools, no access to individual pupil work unless needed |
| School admin | Classes, teachers and pupils in their school |
| Teacher | Pupils in their own classes |
| Pupil | Their own work and assignments |
| Parent | Their own child's progress, where offered |

Enforce these rules with Row Level Security and server-side checks. Test that a teacher cannot see another school's classes or another teacher's pupils, and that pupils cannot see each other's work unless the feature explicitly shares it.

## Analytics, Tracking and Third Parties

Many AI-built apps include analytics, session recording or advertising scripts by default. In a school context, these are often unacceptable, especially if they track pupils for purposes beyond the service. Remove trackers from pupil-facing pages, use privacy-friendly analytics without personal identifiers if you need usage statistics and list every remaining third party in your privacy annex. Schools will ask; being able to say "no tracking on pupil pages" is a strong position.

## AI in Education

AI features such as feedback on writing, reading assessments or adaptive exercises are attractive and sensitive. The EU AI Act classifies certain AI systems in education, such as those determining access to education or evaluating learning outcomes in ways that steer a pupil's path, as high-risk, with significant obligations. Many feedback tools fall outside that category, but transparency, human oversight and data protection still matter. Use AI providers under processing agreements with no training on pupils' data, minimise what you send and let teachers review AI output.

## Retention and End of Contract

Schools expect pupil data to be deleted when it is no longer needed: when pupils leave, at the end of the school year where appropriate and when the contract ends. Build school-level and pupil-level deletion and export, define retention periods with your customers and describe them in the privacy annex. Automate deletion where possible so it does not depend on manual effort.

## Preparing for the Board's Privacy Officer

Before your first conversation with a school board, prepare: the signed model processing agreement or your willingness to sign it, a completed privacy annex, a description of security measures, a sub-processor list with locations, your deletion and retention approach, and a short explanation of any AI features. Offer a demo account so the officer can see what teachers and pupils experience. Privacy officers review many tools; clear, honest documentation makes yours easy to approve.

## Accessibility for Pupils

Schools serve pupils with different needs. Accessible design - readable fonts, sufficient contrast, keyboard navigation, alternative text and support for screen readers - is good practice and increasingly expected for public sector purchases. Building it in from the start costs far less than retrofitting.

## Common Mistakes

- Session recording or advertising scripts on pupil pages
- Teachers able to see all classes or schools
- Pupil uploads in public storage
- Hosting outside the EU without clear justification
- No way to delete a school's data at contract end
- Sending pupils' work to AI providers without agreements

## Summary

Sign the sector's model agreement, describe your processing honestly in the privacy annex, minimise pupil data, enforce access by school, class and role, keep data in the EU and make deletion routine. Schools reward suppliers who make privacy easy.

## Where to Start Today

Open your app as a pupil and inspect which third-party scripts load. Remove anything that tracks pupils beyond what the learning service needs. Then sketch your board-school-class-teacher-pupil access model and check that your database policies follow it.

## Related Reading

Our guides on GDPR deletion in Supabase, letting users upload files safely and the Supabase data processing agreement cover the technical pieces school privacy officers examine most often.

## The Payoff

School boards that approve a tool often roll it out across many schools at once, and teachers who trust a tool recommend it to colleagues elsewhere. Getting privacy right is the key that opens that growth path, and it protects the children whose data you hold.

## Questions to Ask Before Selling to Schools

Which data does each feature truly need? Who at the school decides on privacy? Will you sign the sector's model agreement? Where is every piece of data stored and processed? How will a school leave you cleanly? Answering these early shapes a product schools can adopt with confidence.

## A Final Word

Schools are careful because they are responsible for children. Suppliers who share that care - and can show it in their product and paperwork - become long-term partners.

## One Practical Tip

Ask a friendly teacher to introduce you to their board's privacy officer early; a short conversation about expectations saves weeks later.

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
