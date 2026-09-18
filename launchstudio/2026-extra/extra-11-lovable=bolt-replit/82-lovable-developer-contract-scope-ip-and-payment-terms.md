---
Title: "Lovable Developer Contract: Scope, IP and Payment Terms"
Keywords: lovable developer, contract, intellectual property, scope, lovable expert, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: AI-Native Founder (non-technical)
---

# Lovable Developer Contract: Scope, IP and Payment Terms

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Lovable Developer Contract: Scope, IP and Payment Terms",
  "description": "Who owns AI-generated code, what a scope must contain to be enforceable, how to structure payment against milestones, and the accounts clause that decides whether you can leave.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-08-23",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/lovable-developer-contract-scope-ip-and-payment-terms" }
}
</script>

Most disputes between founders and the developers they hire are not about competence. They are about two people who agreed enthusiastically in a video call and wrote down four sentences afterwards.

Three months later the product is nearly finished, the invoices total more than expected, and nobody can settle whether the notification system was included, who owns the code, or what happens to the hosting account if the relationship ends. Both parties are acting in good faith and both are right about what they remember.

A contract is not a defence against a bad developer. It is a device for finding disagreement in week one rather than month four, when it is cheap.

## Ownership: The Clause That Actually Matters

Under Dutch law, the default position for work by an independent contractor is not automatically what founders assume. Copyright in software generally sits with its creator unless it has been transferred in writing — an employer-employee relationship is treated differently from a freelance engagement. So a founder who paid for a product and never signed an assignment may find that ownership was never transferred.

The contract therefore needs an explicit written transfer of all intellectual property in the deliverables, effective on payment, covering code, designs, database structures and documentation. Include a clause obliging the developer to sign whatever further paperwork is needed to make the transfer effective.

Two sensible exceptions. A developer's pre-existing general components — their own libraries and utilities — usually remain theirs, licensed to you perpetually. And open-source dependencies keep their own licences, which is normal; what you should ask for is a list of them, since some licences carry obligations that matter if you later sell the company.

The question that increasingly arises is whether AI-generated code can be owned at all. The law is unsettled, jurisdictions differ, and the practical answer for a small company is to contract for everything the developer can transfer, keep the repository and accounts in your own name, and treat possession and control as the protection that actually works. Verify current requirements with a lawyer for anything consequential; this is what to expect, not legal advice.

## Scope Is a List, Not a Vision

"Build a booking platform" is not a scope. It is a hope shared by two people who each imagine a different product.

A workable scope lists the user-facing capabilities in plain language — what a user can do, screen by screen or flow by flow. It states what is explicitly excluded, which is the more valuable half: no mobile app, no accounting integration, Dutch language only, no multi-user organisations. It names the integrations and who provides the accounts. It states what "done" means for each item, in terms you can check without reading code.

And it sets out how changes are handled: a short written note, a price, an effect on the timeline, agreed before work starts. Most disputes are change disputes wearing a scope costume — a feature that grew by three conversations without anyone noticing it had become a different feature.

## Payment Structured Against Milestones

Hourly billing suits open-ended work and gives a non-technical founder no cost ceiling. Fixed price suits defined work and needs a defined scope. A hybrid is common and honest: fixed for the agreed scope, hourly for changes.

Whatever the model, tie payment to milestones you can verify. A deposit to start, payments at stages where something is demonstrable, and a final payment on handover. Avoid paying the entire amount before you hold the accounts and the code.

A note on the Dutch context: payment terms for business-to-business are generally expected to be reasonable — 30 days is customary, and statutory limits apply to how long they can be — and late payment carries statutory interest. Agree the term explicitly, and if you are the one paying, respect it, because reputation in a small market travels quickly.

## The Accounts Clause

This is the one that decides whether you can leave, and it is almost never written down.

The contract should state that all accounts are registered in your company's name from the outset: domain, hosting, database, payment provider, email service, error tracking, analytics, and the repository. The developer receives access; they do not own the account. Access is removed when the engagement ends.

Founders who skip this find that the domain is on a freelancer's personal account, the database is under an agency workspace, and leaving requires eleven days of cooperation from someone who no longer has a reason to cooperate. It costs nothing to prevent and is very expensive to unwind.

## What Handover Must Include

Define it in the contract and the last week becomes a checklist rather than a negotiation.

The code, in a repository you own, with its history. Ownership of every account transferred and access revoked. Credentials rotated so the keys you hold are yours alone. A written description of how the system runs: what is deployed where, what runs on a schedule, which services are involved and what they cost. Instructions for running and deploying it. And an honest list of known limitations and unfinished items.

That last item is worth paying for. A developer who documents what is approximate is giving you the map your next developer needs, and its absence is what makes a second engagement start with two weeks of archaeology.

## Warranty, Liability and Who Fixes What

Agree a period — commonly 30 to 90 days after delivery — during which defects in the agreed scope are corrected without further charge, with a clear definition separating a defect from a new request.

Cap liability at something proportionate, usually the contract value. Unlimited liability is not something a freelancer can carry, and insisting on it produces either a refusal or a price that reflects the risk. Conversely, be sceptical of a contract excluding all liability including for gross negligence.

For AI-built products, one clause is worth adding specifically: a statement that the developer will not knowingly deliver code with known security vulnerabilities, and that dependencies will be current at delivery. It is reasonable, it is checkable, and it shapes behaviour.

## Confidentiality, References and the Small Print

Mutual confidentiality is standard. Two details are worth attention: whether the developer may name you as a client, which most freelancers value and most founders are happy to grant, and a non-solicitation clause if you are worried about staff.

Skip the non-compete. In a specialised market it is largely unenforceable in practice, it signals distrust, and the good developers will simply decline.

## When the Product Already Exists

A specific case, because it is now the common one: you built the product yourself with AI tooling and you are hiring someone to make it production-ready.

Two things change. The scope should be written against findings rather than features — a list from an assessment, each item with a definition of done. And ownership needs a sentence covering the existing code as well as the new work, so the finished product is not half yours and half ambiguous.

## When the Developer Touches Your Customers' Data

A clause founders skip entirely, and the one their own customers will eventually ask about.

If your product holds personal data — names, addresses, health information, employment records — and a freelancer can reach it, then under GDPR that freelancer is processing personal data on your behalf. You are the controller; they are a processor; and the relationship needs a written agreement covering what they may do with it, confidentiality, security measures, and what happens at the end.

This is not bureaucracy for its own sake. It has three practical consequences.

**Your own customers will ask.** A business customer's questionnaire asks who can access their data and what agreements are in place. "A freelancer, no agreement" is a bad answer that costs deals.

**It sets expectations before they matter.** The agreement is where you state that production data is not copied to a personal laptop, not used for testing, and not retained after the engagement. Saying it afterwards is an accusation; saying it in a contract is procedure.

**It makes the alternative visible.** Most of the time the developer does not need production data at all. A development environment with anonymised records — real structure, real volume, fictional people — resolves the question entirely and is worth building before the first engagement rather than during it.

Two further details. Specify that access is granted to a named individual rather than a firm, so you know who actually holds it. And specify that any copy of customer data made during the work is deleted at the end, with confirmation.

Where processing happens matters too, particularly if the developer works outside the EEA. Confirm the arrangement rather than assuming, and have a lawyer review anything consequential — this is what to expect rather than legal advice, and obligations vary with the data involved.

## Getting the Engagement Right From the Start

LaunchStudio works on fixed scope precisely because it removes this entire category of argument: a written list of what will be done with a defined outcome for each item, fixed price in bands from €800 to €7,500, ownership transferred on payment, every account in your name from day one, and a handover pack containing code, documentation, rotated credentials and an honest list of what remains.

Behind it is Manifera: eleven years of contracted delivery for clients including Vodafone, TNO and CFLW, from Amsterdam Herengracht 420, Singapore and Ho Chi Minh City.

[Send us what you have built](https://launchstudio.eu/en/#contact) and you will get a scoped proposal you can compare against any other, or see the [packages](https://launchstudio.eu/en/#packages).

## Real example

### A Domain, a Database and a Developer Who Went Quiet

Marijke Doornbos built the first version of Planbord with Lovable: production planning for small manufacturers, with seven customers around Leeuwarden and Drachten. She hired a freelance developer to make it production-ready, agreeing terms in a video call and confirming them in a four-sentence email.

The work went well for two months. Then the developer took a full-time position, his replies slowed to weekly, and the last third of the work stalled.

What the four sentences had not covered: ownership of the code, which had never been assigned; the domain, which he had registered on his own account because it was quicker; the hosting and database, which sat inside his personal workspace; the repository, which was private to him; and what "finished" meant, which he and Marijke described differently when asked separately.

He was not acting badly. He was busy, and nothing obliged him to prioritise a project he had effectively left.

Recovery took five weeks and two lawyers' letters, and succeeded mainly because he eventually cooperated. Six business days of work after that: the code moved into a repository owned by her company; the domain transferred with automatic renewal and two administrators; a new database created in an EU region and the data migrated; every credential rotated; the remaining scope completed — the parts he had left were access rules and the payment webhook, which were also the parts nobody had verified; a handover document written covering deployment, scheduled jobs, services and costs; and a proper agreement drafted for her next engagement, with the accounts clause first.

**Result:** Planbord went live eleven weeks later than planned. Marijke's estimate of the direct cost of the five-week recovery, excluding the delay, is roughly €7,000 — against a contract that would have taken an afternoon to write.

> *"He had done nothing wrong. He had just registered my domain on his own account because it was faster, and then he got a job."*
> — **Marijke Doornbos, Founder, Planbord (Leeuwarden)**

**Cost & Timeline:** €4,200 (repository and account transfers, database migration, credential rotation, completion of remaining scope, handover documentation) — completed in 6 business days after access was recovered.

## Frequently Asked Questions

### Do I automatically own code I paid a freelancer to write?

Not necessarily. Under Dutch law copyright in software generally stays with its creator unless transferred in writing, and freelance engagements are treated differently from employment. Put an explicit assignment in the contract, effective on payment.

### Who owns AI-generated code?

The law is unsettled and jurisdictions differ. Practically, contract for everything the developer can transfer, keep the repository and every account in your own name, and treat possession and control as the protection that actually works.

### What must a scope contain to be useful?

The capabilities in plain language, an explicit list of exclusions, the integrations and who supplies the accounts, what "done" means for each item in terms you can verify, and a written process for changes with price and timeline impact.

### How should payment be structured?

Against verifiable milestones: a deposit, staged payments where something is demonstrable, and a final payment on handover. Do not pay in full before you hold the accounts and the code. Agree the payment term explicitly.

### What is the clause founders most often forget?

The accounts clause. Every account — domain, hosting, database, payments, email, repository — registered in your company's name from the start, with the developer given access rather than ownership, and access removed at the end.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Do I automatically own code I paid a freelancer to write?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Not necessarily — under Dutch law copyright generally stays with the creator unless assigned in writing, so include an explicit transfer effective on payment."
      }
    },
    {
      "@type": "Question",
      "name": "Who owns AI-generated code?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "The law is unsettled. Contract for everything transferable, keep repository and accounts in your own name, and rely on possession and control."
      }
    },
    {
      "@type": "Question",
      "name": "What must a scope contain to be useful?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Capabilities in plain language, explicit exclusions, integrations and account ownership, a verifiable definition of done, and a written change process."
      }
    },
    {
      "@type": "Question",
      "name": "How should payment be structured?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Against verifiable milestones — deposit, staged payments, final on handover — and never in full before you hold the accounts and code."
      }
    },
    {
      "@type": "Question",
      "name": "What is the clause founders most often forget?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "The accounts clause: every account in your company's name from day one, with the developer granted access rather than ownership."
      }
    }
  ]
}
</script>
