---
Title: "Lovable Supabase and GDPR: Seven Questions Dutch Customers Ask"
Keywords: lovable supabase, ai app security, GDPR questionnaire startup, sub-processor list, data retention deletion, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: AI-Native Founder (Non-Technical)
---

# Lovable Supabase and GDPR: Seven Questions Dutch Customers Ask

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Lovable Supabase and GDPR: Seven Questions Dutch Customers Ask",
  "description": "The questions that arrive when a Dutch business, clinic or school evaluates your AI-built product, why each one is asked, and how to prepare answers you can defend before the questionnaire lands.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-06-21",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/privacy-questions-dutch-customers-ask-ai-apps" }
}
</script>

The email is polite and it changes everything. "Before we can proceed, our privacy officer has a few questions about how you handle data." Attached is a document with between seven and forty items, and somewhere around question three you realise that your app has been running for eight months without anyone ever asking where the data lives.

This is the moment AI-built products most often stall — not at the demo, not at the price, but at the security review of the first real business customer. What follows is the seven questions that appear in nearly every Dutch questionnaire, what each one is actually checking, and how to be able to answer it.

This is general information rather than legal advice. Several of these answers eventually need a lawyer's eye, and the point of preparing them is to make that conversation short.

## One: Where Is the Data Stored?

They are asking for a country or region, not a provider name. "Supabase" is not an answer; "Frankfurt, in the European Union" is.

The reason this comes first is that it is the easiest question for them to verify and the one that most often produces a surprise. Lovable projects backed by Supabase are frequently created in a default region outside the EU, and nothing in the running app reveals it. Dutch clinics, schools, municipalities and employers frequently require EU hosting as a procurement condition, regardless of whether the law strictly demands it, because it is simpler for their own compliance story.

Check your project's region today. Changing it later means a data migration; deciding it before launch is one dropdown.

## Two: Who Can Access It?

Not "is it secure" — who, specifically. The expected answer names categories: the customer's own users according to defined roles, your engineering team under stated conditions, and your sub-processors for their specific purposes.

The uncomfortable follow-up is usually "and can one of your customers see another's data?" For multi-tenant products this is the question that fails reviews, and the honest answer requires having tested it: two accounts in two organisations, each trying to read the other's records.

## Three: Can We See Your Sub-Processor List?

A sub-processor is any third party that touches the data on your behalf. For a typical AI-built app, the list is longer than founders expect: your database provider, your hosting platform, your transactional email service, your payment provider, your error tracking tool, your analytics, and any AI model API your product calls.

Prepare this as a one-page table before anyone asks: the service, what it is used for, what data it touches, and where it is hosted. It takes an afternoon while you control the timing, and it is a scramble when a procurement team has given you five working days.

## Four: Do You Have a Data Processing Agreement With Each of Them?

When your customer's data is involved, you are typically acting as a processor for them and your suppliers are processors for you. That chain needs agreements at each link.

Most major providers publish a standard data processing agreement that you accept in their dashboard. The work is not negotiating them — it is knowing which ones you have accepted, storing copies, and being able to produce them. Founders routinely discover during a review that a tool they added in an afternoon has been receiving customer data with nothing signed at all.

## Five: How Long Do You Keep Data, and How Is It Deleted?

Two different questions in one.

**Retention** means having a stated period after which data is removed — and actually removing it. AI-built apps almost never delete anything, because nobody asked them to. "We keep it indefinitely" is an answer; it is just a poor one, and it conflicts with the principle that personal data should not be kept longer than necessary.

**Deletion** means what happens when someone exercises their rights or a customer ends the contract. Can you delete one individual's data without breaking referential integrity? Does deletion reach your backups, your error tracker, your email provider? Can you produce evidence it happened?

The answer most products need is a documented retention period per data type, a working deletion path, and an honest statement about backup rotation — that deleted data persists in backups until they expire, which is normal and should be stated rather than hidden.

## Six: What Happens if There Is a Breach?

They are checking whether you could detect one and whether you know your obligations.

Under the GDPR, a personal data breach must generally be reported to the supervisory authority — in the Netherlands, the Autoriteit Persoonsgegevens — without undue delay and where feasible within 72 hours of becoming aware of it, unless it is unlikely to result in a risk to individuals. As a processor for your customer, you typically have to notify *them* without undue delay so they can meet their own obligation.

The part that catches AI-built products is "becoming aware". Without logging, monitoring and access records, you have no mechanism for becoming aware of anything, and you cannot tell a customer what was accessed. Being able to say "we log access to sensitive tables and retain those logs" turns a frightening question into a short answer.

## Seven: Can We Get Our Data Out?

Export, in a usable format, on request and at the end of the relationship. This is partly a rights question and largely a commercial one: no serious organisation wants to be unable to leave.

For most products this means a working export of a customer's records in a standard format. Building it takes a day. Explaining that you do not have one costs you the deal.

## Prepare the Answers Before the Questionnaire

Write a single document — two pages is plenty — covering: hosting region and provider, access model in plain language, the sub-processor table, where your data processing agreements are stored, retention periods per data type, the deletion procedure, your logging and monitoring setup, your breach notification process with names attached, and your export capability.

Keep it current. Send it with your proposal rather than waiting to be asked. Founders who do this report that reviews shrink from weeks to days, because the reviewer's job becomes verification rather than interrogation.

## What You Genuinely Cannot Do Yourself

Deciding whether you are a controller or a processor for a given flow, drafting the agreement you sign with your customers, assessing whether a particular use needs a data protection impact assessment, and judging cross-border transfer mechanisms — these belong with a data protection lawyer. The mistake is not hiring one; it is hiring one before the technical facts exist, so the conversation becomes hypothetical and expensive.

Get the technical answers straight first. Then the legal conversation is short.

## Getting to Answers You Can Defend

Most of the seven questions are engineering work with a compliance shape: region set deliberately, access model enforced and tested, logging and monitoring in place, retention and deletion implemented, export built, sub-processors documented. LaunchStudio does exactly that as part of making an AI-built product production-ready — without touching the interface you built in Lovable — and hands over the documentation alongside the code, which is what turns the questionnaire into an afternoon rather than a crisis.

Behind it is Manifera: eleven years of production engineering for clients including Vodafone, TNO and CFLW, from Amsterdam and Ho Chi Minh City, where enterprise security reviews are an ordinary part of the week. See what the [Launch Ready package](https://launchstudio.eu/en/#packages) covers, or [describe your project](https://launchstudio.eu/en/#contact) and get a straight assessment of where you stand within one business day.

## When the Honest Answer Is Uncomfortable

At some point in a questionnaire you will reach a question where the true answer is "we do not do that". Founders panic at this moment and reach for vagueness, which is the worst available option.

Privacy officers assess questionnaires professionally. They can recognise evasion instantly, and vagueness reads as either incompetence or concealment — both of which end a review faster than an honest gap would.

The formulation that works has three parts: what is true now, what you are doing about it, and by when. "We do not currently log read access to patient records. We are implementing it this month and can demonstrate it before go-live." That is an answer a reviewer can work with, and it is frequently accepted with a condition attached rather than a rejection.

Two things make this credible. A date, which means you have thought about the work rather than the sentence. And consistency — the same gap described the same way to everyone who asks, because reviewers at different organisations occasionally compare notes, and Dutch sector networks are smaller than founders assume.

The one answer to avoid entirely is claiming a control you do not have. It is discoverable during the review itself, it converts a fixable gap into a trust problem, and a privacy officer who catches it will remember your product for the wrong reason.

## Keep the Pack Somewhere You Can Find It

A small operational note that saves more time than it should. The two-page document described above has a habit of existing in a founder's downloads folder, six months out of date, in a version nobody can locate when the next questionnaire arrives.

Keep it in one place, dated, with a note of what changed. Review it whenever you add a third-party service — which in an AI-assisted workflow happens more often than you expect — and whenever your hosting or database arrangements change.

Then attach it to proposals rather than waiting to be asked. Founders who do this consistently report the same thing: the review stops being an interrogation and becomes a verification, and the questions that come back are specific and answerable rather than open-ended.

## Real example

### A Scheduling Tool That Failed a Review and Passed Six Weeks Later

Tessa Blom's app, Planbaar, scheduled home-care visits for small care organisations around Deventer. Two organisations used it informally. The third was larger and sent a nineteen-question privacy assessment before signing.

Planbaar failed on five of the seven questions above. The Supabase project was in a US region. No sub-processor list existed, and the review surfaced that client notes were being passed to an error-tracking service and a marketing email tool, neither with an agreement in place. Nothing was ever deleted. There was no access logging, so the question about detecting a breach had no answer. And there was no export.

The work took twelve business days: migration to an EU region with a tested restore, the marketing tool removed from the data path and replaced with a transactional provider covered by an agreement, error tracking configured to scrub personal data before transmission, retention periods defined per data type with automatic deletion, read-access logging on care-note tables, a customer-level export, and the two-page documentation pack.

**Result:** Planbaar passed the reassessment six weeks later and now sends the documentation pack with every proposal. The two smaller organisations, who had never asked, received it too — and one of them upgraded their contract.

> *"I kept thinking privacy was a document I needed to write. It turned out to be six things my app didn't do."*
> — **Tessa Blom, Founder, Planbaar (Deventer)**

**Cost & Timeline:** €4,200 (Launch Ready Package: region migration, data path cleanup, retention and deletion, access logging, export) — completed in 12 business days.

## Frequently Asked Questions

### Do I need all of this before my first customer?

Before your first *business* customer, largely yes, because their procurement process will ask. For consumer products the questions arrive later and the same answers apply, so the work is rarely wasted.

### Is EU hosting legally required for a Dutch customer?

Not automatically — transfers outside the EU are possible under the right safeguards. In practice many Dutch organisations require it contractually because it simplifies their own compliance, so the commercial answer is often stricter than the legal one.

### What counts as a sub-processor?

Any third-party service that processes personal data on your behalf: hosting, database, email, payments, error tracking, analytics, AI model APIs. If customer data reaches it, it belongs on the list.

### How do I handle deletion when data is in backups?

State it plainly: deleted data is removed from live systems immediately and persists in backups until those expire on a stated schedule. This is standard practice, and attempting to claim instant deletion everywhere is both false and unnecessary.

### Who writes the data processing agreement with my customers?

A lawyer, working from the technical facts you supply. Get the region, access model, sub-processor list and retention periods established first — that turns a vague, expensive engagement into a short one.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Do I need all of this before my first customer?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Before your first business customer, largely yes, because procurement will ask. For consumer products the questions arrive later and the same answers apply."
      }
    },
    {
      "@type": "Question",
      "name": "Is EU hosting legally required for a Dutch customer?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Not automatically, since transfers are possible under the right safeguards. In practice many Dutch organisations require it contractually, so the commercial answer is stricter than the legal one."
      }
    },
    {
      "@type": "Question",
      "name": "What counts as a sub-processor?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Any third-party service processing personal data on your behalf — hosting, database, email, payments, error tracking, analytics and AI model APIs."
      }
    },
    {
      "@type": "Question",
      "name": "How do I handle deletion when data is in backups?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "State it plainly: removed from live systems immediately and persisting in backups until they expire on a stated schedule. That is standard practice."
      }
    },
    {
      "@type": "Question",
      "name": "Who writes the data processing agreement with my customers?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "A lawyer, working from technical facts you supply. Establishing region, access model, sub-processors and retention first keeps that engagement short."
      }
    }
  ]
}
</script>
