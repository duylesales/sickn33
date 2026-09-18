---
Title: "AVG Compliance for AI-Built Apps: What Dutch Customers Verify"
Keywords: AVG compliance, GDPR, AI-built apps, verwerkersovereenkomst, data minimisation, Dutch privacy, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: AI-Native Founder (Non-Technical)
---

# AVG Compliance for AI-Built Apps: What Dutch Customers Verify

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "AVG Compliance for AI-Built Apps: What Dutch Customers Verify",
  "description": "What a Dutch business customer actually checks before signing: the processing agreement, where data sits, who can see it, deletion, and whether your app can do what your privacy policy claims.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-11-26",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/avg-compliance-for-ai-built-apps-what-dutch-customers-verify" }
}
</script>

There is a version of privacy compliance that consists of a generated policy page nobody reads, and there is the version a Dutch business customer applies before they sign. They are not the same exercise, and founders usually meet the second one unprepared.

The good news is that the second version is narrower and more practical than the reputation suggests. A procurement officer at a Dutch company is not testing your knowledge of the regulation. They are asking a handful of concrete questions, and what they are really assessing is whether your answers are specific.

## You Are the Processor, They Are the Controller

The vocabulary matters because everything else follows from it.

Your customer — the accountancy firm, the clinic, the municipality — decides why and how personal data is processed. They are the *verwerkingsverantwoordelijke*, the controller. You process it on their instructions, which makes you the *verwerker*, the processor.

That relationship requires a written processing agreement, a *verwerkersovereenkomst*, and this is the first thing a serious customer asks for. Having one ready, in Dutch, that you wrote rather than downloaded, moves you ahead of most competitors at your size.

Note the exception: data about your own customers as your customers — their contact details, their billing — is data you control. Your privacy policy covers that. The processing agreement covers their data, which sits inside your product.

## The Five Questions That Actually Get Asked

Almost every Dutch business review reduces to these.

**What personal data does your product hold, and why?** They want a list of categories and purposes, not a philosophy. Names, addresses, appointment times, notes — each with a reason.

**Where is it stored and processed?** Including backups, error tracking, email and any AI feature. This is the question most AI-built products fail, because nobody checked.

**Who can see it on your side?** Meaning how many people at your company can read their data, under what controls, and whether that access is recorded.

**What happens when we leave?** Export format, deletion timeline, and confirmation that backups age out under a stated retention rule.

**Who else is involved?** Your subprocessors, by name, with what each receives.

Five answers, written once. A founder who can produce them in one email is a founder whose contract moves forward.

## Data Minimisation Is Where AI-Built Products Fail

The principle is that you collect what you need and no more. AI tools do the opposite by default, because a generated form asks for everything that might be relevant and a generated table stores it forever.

Go through your forms and ask, field by field, what breaks if you remove it. Date of birth on a scheduling tool. A phone number nobody calls. An address for a service delivered entirely online. Each unnecessary field is data you must secure, disclose, export and delete, in exchange for nothing.

The same applies to duration. Records kept indefinitely because nothing was decided are a liability that grows. Set a retention period per category, enforce it with a scheduled job, and state it.

This is the part of compliance that is genuinely also engineering, and it is where the largest reduction in risk comes from — data you do not hold cannot be breached, requested, or mishandled.

## Your Policy Must Describe the Product You Have

The common failure is a privacy policy generated from a template describing an application that does not exist.

It says data is retained for 12 months while your database has everything since launch. It lists no subprocessors while you use four. It promises deletion within 30 days while your product has no deletion function at all. It omits the AI feature entirely.

This matters because a policy is a statement you can be held to. An inaccurate one is worse than a brief accurate one, and a customer who finds a discrepancy between your policy and your product will ask what else is untrue.

The fix is to write the policy from the product rather than from a template: walk through what you actually collect, where it goes, how long you keep it, and who else touches it — which is the same inventory the five questions require.

## Rights Must Be Operable, Not Just Promised

People have rights over their data, and the ones that matter operationally are access, correction, deletion, and export in a portable format.

Your customer, as controller, receives these requests and will pass them to you. So the question is practical: if a clinic asks you to delete one patient's data today, what happens?

In most AI-built products the honest answer is a manual database operation performed carefully by the founder, which works at ten requests a year and is a genuine problem at a hundred. Building an export and a deletion function that a customer can run themselves is usually a day, and it converts a recurring obligation into a feature you can point at during a sales conversation.

Deletion needs thought rather than a DELETE statement: what must be kept for legal reasons, such as invoices; what should be anonymised rather than removed, such as historical statistics; and what genuinely goes.

## Write Down the Basics Before Anyone Asks

Three documents, each short, cover most of what a review requests: a register of processing activities describing what you process and why, a processing agreement ready to sign, and a subprocessor list with locations.

None needs to be long. A register for a small product fits on two pages. What matters is that it exists, is current, and was written about your product rather than adapted from someone else's.

## The Lawful Basis Question, Briefly

Every processing activity needs a reason the law recognises, and for a business product the answer is usually simpler than the discourse around it suggests.

For your customer's use of your product, the basis is normally the contract between them and the people whose data they hold, or their own legitimate interest, or a legal obligation — and that determination is theirs to make, not yours. You process on their instructions.

For your own processing — your customer's contact details, billing, service emails — the basis is typically the contract with them or your legitimate interest in running the service.

Consent is the basis founders reach for first and it is usually the wrong one. It must be freely given, specific and withdrawable, which makes it a poor foundation for anything your product needs to function: a customer who withdraws consent for data your service cannot operate without creates a problem that a contractual basis would not have.

Where consent genuinely applies is the optional extras — marketing email, non-essential cookies and analytics, anything the person could reasonably decline while still using the product. Keep those separate, record when and how consent was given, and make withdrawal as easy as giving it.

The practical output is one line per processing activity in your register naming its basis. Writing that down is an hour, and it is the question a well-prepared reviewer asks after the five above.

## When You Need Help, and When You Do Not

Compliance advice for small products divides cleanly, and knowing which side a question falls on saves both money and delay.

Do it yourself: the data inventory, field minimisation, retention periods, export and deletion functions, the subprocessor list, access restriction, and rewriting the privacy policy from the product. These are engineering and honesty, and nobody understands your application well enough to do them for you.

Get help: the processing agreement itself, reviewed once by someone qualified so you are not signing a template you have not understood; any product handling special categories of data — health, biometric, anything about a person's circumstances — where the rules are stricter and the consequences larger; a data protection impact assessment, which is required for higher-risk processing and is a structured exercise rather than a document to invent; and the question of whether you need a data protection officer, which most small products do not but which depends on what you process rather than on your size.

One practical note on cost: a Dutch privacy lawyer reviewing a processing agreement for a small SaaS is typically a few hours of work, not a project. Founders often avoid the conversation expecting an engagement and discover it is an afternoon. The expensive version is the one that happens after a customer's legal team has found something.

## Setting This Up

For an existing product this is typically two to three days: an inventory of personal data by category and purpose, a processing agreement in Dutch ready to sign, a documented subprocessor list with processing locations, unnecessary fields removed from forms and schema, retention periods set per category and enforced by a scheduled job, export and deletion functions a customer can operate, access to production data restricted and recorded, a privacy policy rewritten from the actual product, and a register of processing activities.

LaunchStudio does this as part of preparing a product to sell to Dutch businesses, which is where most of our customers' revenue comes from. Behind the work is Manifera — eleven years, clients including Vodafone, TNO and CFLW, and European operations from Herengracht 420 in Amsterdam.

[Send us the privacy questions you were asked](https://launchstudio.eu/en/#contact) and we will tell you which ones your product can currently answer.

## Real example

### Twelve Questions From an Accountancy Group

Steven Nijhuis built Urenregistratie in Lovable: time registration for accountancy and bookkeeping offices, 41 offices with around 600 staff.

An accountancy group of nine offices ran a privacy review before onboarding. Their questionnaire had twelve questions and Steven could answer four.

He had no processing agreement. His privacy policy was a template that mentioned a retention period of 12 months, while his database held every record since launch two years earlier. He had never listed his subprocessors and, on counting, there were six. His deletion process was him running a query. Error tracking was capturing full request bodies including staff names and client references, processed outside the EU with no scrubbing. And his registration form collected date of birth, home address and a private phone number, none of which the product used for anything.

Three business days: a data inventory by category and purpose, which identified three fields collected and never used; those fields removed from the form and dropped from the schema, with existing values deleted; retention set per category — time entries kept seven years for tax reasons, account data 24 months after the office leaves, logs 30 days — and enforced by a monthly job; export and deletion functions built into the office administrator view, so an office can act on a staff member's request without contacting him; a processing agreement drafted in Dutch with legal review; a subprocessor list published with processing locations, after moving error tracking to an EU provider and configuring field scrubbing; the privacy policy rewritten from the actual product; production data access restricted to one account with access recorded; and a two-page register of processing activities.

**Result:** the twelve questions were answered from the prepared documents and the group signed for nine offices. Steven now sends the processing agreement and subprocessor list with every proposal, and reports that three later customers said it was the reason they chose him over a larger competitor whose answers took six weeks.

> *"My privacy policy promised things my product could not do. That was the part I found genuinely alarming — I had written a commitment to strangers that my own software could not keep."*
> — **Steven Nijhuis, Founder, Urenregistratie (Deventer)**

**Cost & Timeline:** €4,100 (data inventory, field and schema minimisation, retention policy with enforcement, customer-operated export and deletion, processing agreement, subprocessor documentation and error tracking migration, privacy policy rewrite, access restriction, processing register) — completed in 3 business days.

## Frequently Asked Questions

### Am I a controller or a processor?

For data your customers put into your product, you are the processor and they are the controller — which requires a written processing agreement. For your own customer and billing data, you are the controller.

### Do I need a Dutch-language processing agreement?

If you sell to Dutch businesses, yes in practice. A ready-to-sign *verwerkersovereenkomst* in Dutch removes a step that otherwise adds weeks to a procurement process.

### What is the most common failure in AI-built products?

Collecting data nobody uses and keeping it indefinitely. Generated forms ask for everything and generated schemas keep it forever, which creates obligations in exchange for nothing.

### Does my privacy policy have to match what the product does?

Yes. It is a statement you can be held to. A policy promising 12-month retention and deletion within 30 days, on a product that does neither, is worse than a shorter accurate one.

### What do I do when a customer asks me to delete one person's data?

Build export and deletion as functions your customer can run themselves. Decide in advance what must be retained for legal reasons and what should be anonymised rather than removed.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Am I a controller or a processor under the AVG?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "For data customers put into your product you are the processor and they are the controller, which requires a written processing agreement. Your own billing data you control."
      }
    },
    {
      "@type": "Question",
      "name": "Do I need a Dutch verwerkersovereenkomst?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "If you sell to Dutch businesses, in practice yes — a ready-to-sign agreement in Dutch removes weeks from procurement."
      }
    },
    {
      "@type": "Question",
      "name": "Where do AI-built products fail on privacy?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Data minimisation. Generated forms collect fields nobody uses and generated schemas retain them indefinitely."
      }
    },
    {
      "@type": "Question",
      "name": "Must my privacy policy match the product?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes — it is a commitment you can be held to. A template promising retention and deletion the product cannot perform is worse than a short accurate policy."
      }
    },
    {
      "@type": "Question",
      "name": "How should deletion requests be handled?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Build export and deletion as functions the customer can run, deciding in advance what must be legally retained and what should be anonymised."
      }
    }
  ]
}
</script>
