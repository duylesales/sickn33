---
Title: "Records of Processing: The Register Nobody Builds Until Asked"
Keywords: records of processing, verwerkingsregister, AVG article 30, data mapping, compliance documentation, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: SaaS Scale-Up
---

# Records of Processing: The Register Nobody Builds Until Asked

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Records of Processing: The Register Nobody Builds Until Asked",
  "description": "A two-page document that answers most privacy questions a customer or regulator asks. What belongs in a verwerkingsregister for a small product, how to build one from the codebase, and keeping it true.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-12-06",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/records-of-processing-the-register-nobody-builds-until-asked" }
}
</script>

Of all the compliance artefacts a small product is asked for, the register of processing activities has the best ratio of effort to usefulness — and it is the one almost nobody has.

It is a document listing what personal data you process, why, on what basis, who else sees it, where it goes, and how long you keep it. Two pages for a typical product. And once it exists, it answers the majority of questions that arrive in a customer's privacy review, supplies the annex to every processing agreement you sign, and forms the basis of your privacy policy.

The reason it is worth building before anyone asks is that building it under deadline is how founders discover that their product collects three things nobody knew about.

## What the Register Contains

For each processing activity, seven things.

**The activity**, named the way your business would describe it: customer account administration, appointment scheduling, invoicing, support, product analytics.

**Categories of data subjects.** Whose data — your customers' staff, their clients, your own users, website visitors.

**Categories of personal data.** Names, contact details, appointment times, notes, payment references. Flag anything in a special category — health, biometric, anything about a person's circumstances — because stricter rules apply.

**Purpose**, in a sentence.

**Lawful basis**, where you are the controller.

**Recipients.** Every subprocessor receiving this data, named, with what they receive.

**Retention.** How long, and what happens afterwards — deleted, or anonymised.

Add transfers outside the EEA with their basis, and a line on security measures. That is the document.

## Build It From the Product, Not From a Template

The temptation is to download a spreadsheet and fill it in. The result is a register describing a generic company.

The reliable method takes a morning and is mechanical.

Open your database and list every table containing anything about a person. For each, note what the columns actually hold — including free-text fields, which contain whatever users typed and are usually the most sensitive thing you have.

Then list every external service data flows to. Payment provider, email provider, error tracking, analytics, storage, model APIs, support tooling. Check what each actually receives rather than what you assume: error tracking capturing full request bodies is the classic discovery.

Then list every export and integration — reports, CSV downloads, webhooks to customers' systems, anything that sends data somewhere.

Group those findings into activities and write the seven fields for each. The work is the inventory; the document is the easy part.

## The Questions It Forces You to Answer

The value of the register is not the artefact. It is that writing it makes three things impossible to avoid.

**Why do we have this?** Every field without a purpose is a field to delete. Most founders find several.

**How long do we keep it?** "Forever, because nobody decided" is the default answer in every AI-built product, and it is not an answer you can write in a document you will hand to a customer.

**Who else has it?** The subprocessor list is always longer than remembered, and the exercise frequently turns up a service that was tried once and still receives data.

Each of those leads to a change in the product rather than in the paperwork, which is the point.

## Keep It True

A register that describes last year's product is worse than none, because it is a statement you have made.

Two habits keep it current at almost no cost. Attach it to change: adding a table with personal data, a new subprocessor, or a new export is a one-line update at the time, not a review later. And revisit it annually, alongside your subprocessor list and your security annex, which are the same information in different shapes.

Keep it in the repository, in a plain text format, so it is versioned alongside the code it describes. A register in a document on somebody's laptop is a register that will not be updated.

## Free-Text Fields Are the Hard Part

Every structured column in your database has a known meaning. Free-text fields have whatever meaning your users gave them, and in practice that is always more than intended.

A "notes" field on a customer record accumulates whatever the person typing needed to remember. In a care product it becomes clinical information. In a recruitment product it becomes opinions about candidates. In a financial product it becomes details of someone's circumstances. None of that was designed; it emerged, because a text box is the path of least resistance for anything the form does not have a field for.

This matters for the register because the category of data you hold is determined by what is in it, not by what it was for. A product that would otherwise process ordinary contact details may in fact be processing special category data in one column.

Three practical responses. Sample the field — read fifty rows, with appropriate care and access controls, and find out what is actually there. Label it honestly in the register, based on the sample rather than the intention. And reduce the pressure that fills it: if practitioners keep putting clinical notes in a practical-remarks box, either give them a proper field with appropriate handling or state clearly in the interface what the box is not for.

The unhelpful response is to assume the intended purpose is the actual one, which is how a product ends up holding a category of data its own documentation does not mention.

## One Document, Four Uses

The reason to treat the register as foundational rather than as one more item on a compliance list is that almost everything else in this area is a view of the same information.

**The processing agreement annex** is the register's content, reformatted, for one customer.

**Your privacy policy** is the register written for the people whose data it describes, in plainer language and with their rights added.

**The subprocessor page** is one column of the register, published.

**The answers to a privacy questionnaire** are the register, rearranged into whatever order the customer asked.

So the sequence that avoids repeated work is to build the register first and derive the rest, rather than writing four documents separately and discovering that they disagree — which is the usual state of affairs, and the specific thing a careful reviewer looks for.

It also changes maintenance from four tasks to one. When a subprocessor changes, the register is updated and the other three are regenerated from it. When a founder tells us they have compliance documentation but cannot remember which version of what is current, this is invariably the missing piece.

## When the Register Says You Need Advice

Two findings, if they appear, mean the exercise has outgrown a founder working alone, and recognising them is part of the value.

**Special category data at any scale.** Health, biometric, ethnicity, political or religious information, trade union membership, or anything about a person's sex life or orientation. The rules are stricter, the lawful bases are narrower, and a mistake is consequential. A product that discovers it holds this — often through free-text fields, as above — should take advice rather than reason its way to a position.

**Processing that is systematic and large-scale, or that evaluates people.** Monitoring, profiling, scoring, automated decisions with a real effect on someone. This is the territory where a data protection impact assessment is required, and where the AI Act questions arrive alongside the privacy ones.

Neither means a large project. Both mean a conversation with someone qualified, using the register you have just built as the input — which is precisely why it is worth building first. An adviser handed a completed register can give a useful answer in an hour; one handed a vague description of a product spends that hour asking questions you could have answered yourself.

For everything outside those two findings, a small product can reasonably handle this work in-house, revisit it annually, and be in a better position than most of its competitors.

## Setting This Up

For an existing product this is typically half a day to a day: every table and free-text field holding personal data inventoried, every external service checked for what it actually receives, exports and integrations listed, findings grouped into activities with the seven fields completed, special categories flagged, transfers outside the EEA identified with their basis, retention decided per activity and then implemented rather than merely written, unnecessary fields removed, and the register committed to the repository with a note to update it when data flows change.

LaunchStudio produces this as part of preparing a product for business customers, and it doubles as the processing annex and the basis for an accurate privacy policy. Behind the work is Manifera — eleven years, clients including Vodafone, TNO and CFLW, from Herengracht 420 in Amsterdam.

[Ask us to build your register from your schema](https://launchstudio.eu/en/#contact). The findings are usually more interesting than the document.

## Real example

### Three Discoveries in One Morning

Jorinde Talsma built Kliniekplanner in Lovable: appointment scheduling and patient communication for physiotherapy and podiatry clinics, 37 clinics with around 22,000 patients.

A clinic's own auditor requested her register. She did not have one, and building it took a morning and produced three findings she had not expected.

The first: a free-text "notes" field on appointments, intended for practical remarks like parking instructions, contained clinical information in a substantial share of records — practitioners had used it for what was convenient. That made it health data, a special category, with stricter requirements than anything else in her product.

The second: error tracking was capturing full request bodies, which meant patient names, appointment reasons and those same notes were being transmitted to a service outside the EU with no data processing agreement and no scrubbing.

The third: an analytics service she had trialled for two weeks eleven months earlier was still receiving page events including URLs that contained patient identifiers.

Four business days: the register built from the schema covering nine processing activities; the notes field acknowledged as potentially clinical, with access restricted, a warning shown to practitioners, and the field brought under the stricter handling that special category data requires; error tracking replaced with an EU-hosted provider and configured to scrub request bodies entirely; the abandoned analytics service removed and its retained data deleted on request; URLs changed to stop carrying patient identifiers; retention set per activity — appointments retained per clinic instruction, communication logs 24 months, technical logs 30 days — and implemented with a scheduled job rather than only documented; two unused fields removed from the patient record; the register committed to the repository; and the same content reused as the processing annex and to rewrite the privacy policy.

**Result:** the auditor's questions were answered from the register. Jorinde reports the eleven-month analytics leak as the finding that justified the exercise — nothing in her product referenced that service, nobody had thought about it since, and it had been receiving patient identifiers the entire time.

> *"I expected to spend a morning writing a document. I spent a morning finding out that a tool I stopped using last year had been collecting patient data every day since."*
> — **Jorinde Talsma, Founder, Kliniekplanner (Leeuwarden)**

**Cost & Timeline:** €2,900 (schema and data flow inventory, register across nine activities, special category handling for clinical notes, error tracking migration with scrubbing, abandoned service removal and deletion, identifier removal from URLs, retention implementation, field minimisation, policy and annex derivation) — completed in 4 business days.

## Frequently Asked Questions

### Does a small company need a register of processing?

The obligation has thresholds, but the practical answer is yes: it is requested in most business privacy reviews, supplies the annex to every processing agreement, and takes half a day to produce.

### What goes in it?

Per activity: the activity name, categories of data subjects and data, purpose, lawful basis, recipients, retention, transfers outside the EEA and their basis, and a line on security measures.

### How do I build one accurately?

From your database and your outbound data flows rather than from a template — every table with personal data, every external service and what it actually receives, every export and integration.

### What does the exercise usually find?

Fields nobody uses, no retention decision anywhere, and more subprocessors than remembered — frequently including a service that was trialled once and still receives data.

### Where should it live?

In your repository as plain text, versioned with the code it describes and updated when data flows change. A document on a laptop does not get updated.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Does a small company need a processing register?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Practically yes — it is requested in business privacy reviews, provides the processing agreement annex, and takes about half a day to produce."
      }
    },
    {
      "@type": "Question",
      "name": "What does a register of processing contain?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Per activity: name, data subject and data categories, purpose, lawful basis, recipients, retention, non-EEA transfers with basis, and security measures."
      }
    },
    {
      "@type": "Question",
      "name": "How should the register be built?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "From the database and outbound data flows — every table holding personal data, every external service and what it actually receives, every export."
      }
    },
    {
      "@type": "Question",
      "name": "What does building a register usually reveal?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Unused fields, no retention decisions, and more subprocessors than remembered — often including an abandoned service still receiving data."
      }
    },
    {
      "@type": "Question",
      "name": "Where should a processing register be kept?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "In the repository as plain text, versioned with the code and updated whenever data flows change."
      }
    }
  ]
}
</script>
