---
Title: "Data Processing Agreements: The Paperwork Your SaaS Stack Requires"
Keywords: data processing agreement SaaS, DPA sub-processor list, GDPR vendor agreements, processor vs controller, DPA checklist startup, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: SaaS Founder Scale-Up
---

# Data Processing Agreements: The Paperwork Your SaaS Stack Requires

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Data Processing Agreements: The Paperwork Your SaaS Stack Requires",
  "description": "A practical inventory of which vendors in a typical SaaS stack require a signed Data Processing Agreement, how to find and verify each one, and the decision framework for building a sub-processor list that survives an enterprise procurement review.",
  "author": {
    "@type": "Organization",
    "name": "LaunchStudio",
    "url": "https://launchstudio.eu/en/"
  },
  "publisher": {
    "@type": "Organization",
    "name": "Manifera",
    "url": "https://www.manifera.com"
  },
  "datePublished": "2027-01-09",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://launchstudio.eu/en/blog/data-processing-agreements-your-saas-stack-requires"
  }
}
</script>

Rutger, three months into growing his invoicing SaaS, gets an email from a prospective customer's legal team: "Please send us your Data Processing Agreement and a list of your sub-processors." He's never heard the term. He calls his co-founder. Neither of them signed anything with Stripe, Resend, or Supabase that they remember — did they need to? Is this something they're supposed to have written themselves? The honest answer is both: most of your vendors already have a DPA ready for you to accept, usually buried in their terms of service or available as a one-click acceptance in their dashboard, and you also need your own DPA — the one you offer your customers, since from their perspective, you're the processor now.

This confusion is almost universal among first-time SaaS founders, because "Data Processing Agreement" sounds like a document you'd need a lawyer to draft from scratch, when for the vendor side it's usually a document you just need to know exists and go find. Here's the actual inventory: which categories of tools in a typical stack need one, where to find each vendor's version, and what your own DPA — the one flowing the other direction, to your customers — actually needs to say.

## Controller, Processor, and Why the Direction of the Agreement Matters

A DPA is a contract between a controller (the entity deciding why and how personal data is processed) and a processor (the entity processing it on the controller's instructions). For your relationship with your infrastructure vendors, you're the controller and they're the processor — you decide to store user emails in Supabase; Supabase processes that data on your behalf and instructions. For your relationship with your own customers, if you're B2B SaaS, the direction usually flips: your customer is the controller of their end-users' data, and you're their processor. This means you need DPAs in two directions simultaneously — accepting them from every vendor that processes data for you, and offering one to every customer who asks (and eventually, every customer will ask, because their own compliance obligations require it). Getting this backwards — treating your vendor DPAs as sufficient without ever producing your own — is the single most common gap LaunchStudio finds when a scale-up founder gets their first serious procurement questionnaire.

## The Inventory: Which Vendors in a Typical Stack Actually Need One

Not every tool in your stack touches personal data, and not every tool that does requires the same level of scrutiny. Walk through the categories that matter for a typical SaaS product built on AI-generated code and modern infrastructure. **Hosting and database** (Supabase, AWS, Vercel, Railway, Render) — always needs a DPA, since your entire user database lives here; every major provider publishes one, usually accepted automatically as part of their standard terms or available as a downloadable PDF in account settings. **Email delivery** (Resend, Postmark, SendGrid, Mailgun) — needs one, since every transactional and marketing email contains a recipient's email address and often their name; check specifically because some providers' free tiers exclude the DPA or require an upgrade to access it. **Analytics** (Google Analytics, PostHog, Plausible, Mixpanel) — needs one if you're tracking any user-identifiable behavior, though privacy-first tools like Plausible minimize this by design since they don't collect personal identifiers in the first place. **Payment processing** (Stripe, Mollie, PayPal) — needs one, though payment processors typically carry additional certifications (PCI-DSS) on top of their standard DPA, since payment data has its own regulatory layer beyond GDPR. **AI API providers** (OpenAI, Anthropic, any hosted model) — needs one if any personal data is included in prompts sent to the model, which is a decision worth making deliberately rather than discovering after the fact, since AI providers' data retention and training-use policies vary meaningfully between consumer and business/API tiers. **Customer support and CRM tools** (Intercom, HubSpot, Zendesk) — needs one, since these tools store the full history of customer conversations, often including sensitive troubleshooting details. **Error tracking and logging** (Sentry, LogRocket, Datadog) — frequently overlooked, but needs one, since stack traces and session replays can inadvertently capture personal data typed into forms or visible in application state.

## Finding a Vendor's DPA When It Isn't Advertised

Most established SaaS vendors publish their DPA somewhere findable, but "findable" varies wildly — some put a direct link in the footer, some bury it inside a broader "Trust Center" or "Legal" page, and some require you to explicitly request and countersign it via account settings or a support ticket. The practical search pattern: check the vendor's footer for "DPA," "Trust," "Legal," "Privacy," or "GDPR" links first; if nothing surfaces, search "[vendor name] DPA" directly, since most vendors that have one make it indexable specifically because customers search for it this way; if neither works, email their support or sales contact and ask directly — a vendor processing EU personal data without a ready DPA is a legitimate reason to reconsider using them for anything beyond a low-risk internal tool. For vendors on paid enterprise tiers specifically, the DPA is sometimes gated behind that tier, which is worth checking before committing to a cheaper plan if you know you'll need enterprise customers who will ask for it. Keep a copy of every accepted DPA, or a link to its current version, somewhere organized — a shared drive folder or a section of your sub-processor list document — rather than trusting you'll be able to re-find six vendors' agreements under deadline pressure during a real procurement review.

## Building Your Own DPA: What Your Customers Will Actually Ask to See

Once you're processing data on behalf of B2B customers, you need your own DPA to offer them, and while the specific legal drafting genuinely benefits from a lawyer's review, the structural content you need to think through yourself first: what categories of your customer's end-user data you process and why, where it's hosted and by which sub-processors (this is where your own vendor inventory becomes essential — you can't write an honest DPA without first knowing your own sub-processor list), what security measures you have in place, your data breach notification commitment (typically within 72 hours of becoming aware, mirroring GDPR's own requirement to regulators), and your data deletion or return process at contract termination. Many SaaS companies at this stage use a template DPA — several reputable ones exist as a starting point, often modeled on the EU Commission's Standard Contractual Clauses structure — and have a lawyer review and adapt it rather than drafting from a blank page, which is both faster and more defensible than either extreme of "no DPA at all" or "fully custom legal drafting for a two-person company's first enterprise deal."

## The Sub-Processor List: One Document That Answers Most Future Questions

Every DPA you offer customers should reference, and ideally link to, a maintained sub-processor list — the same inventory built while working through the vendor categories above, formatted as a customer-facing document rather than an internal spreadsheet. This list needs to name each sub-processor, what it does, where it's hosted, and ideally a mechanism for notifying customers before adding a new one (many enterprise DPAs require 30 days' notice before a new sub-processor is added, giving the customer a window to object). Building this list once and keeping it current is meaningfully cheaper than reconstructing it under time pressure for every new enterprise deal, and it's a document sophisticated customers increasingly expect to find publicly linked from a pricing or security page, not something they have to request via email and wait a week for.

## The Decision Points Where a Lawyer Genuinely Earns Their Fee

Founders can competently handle vendor DPA discovery and acceptance, and can draft a reasonable first version of their own sub-processor list, without legal help. Where a lawyer's review is worth the cost: adapting a DPA template with liability and indemnification language specific to your actual risk profile, negotiating DPA terms with an enterprise customer's legal team who pushes back on your standard version, and any situation involving special category data or cross-border enforcement exposure. A one-time paid review of a DPA template, run once and reused for every subsequent customer, is a far more efficient use of legal spend than negotiating from scratch with every new enterprise prospect — get the template right once, with professional help, and the marginal cost of each future deal drops close to zero.

## Timing the Inventory Against Your Growth Stage

The right moment to build a full sub-processor inventory isn't your first day of coding, and it isn't the day an enterprise prospect emails asking for one either — both extremes waste effort or create risk. Building it too early means documenting a stack that's still changing weekly, producing a document that's out of date before it's finished. Building it only in reaction to a request means doing rushed, high-stakes work under a deal deadline, with a prospect watching the clock. The practical trigger point is somewhere in between: once your product has real paying customers and the core of your stack — hosting, auth, payments, email — has stabilized, even if features are still shipping fast, that's the moment to spend an afternoon on the inventory. A useful forcing function is to treat "first paying B2B customer" as the deadline, regardless of whether that customer has asked for anything yet, because the second one almost always will, and having it ready removes an entire category of deal risk from every subsequent sales conversation. Revisiting the list quarterly, or whenever a new vendor is added to the stack, keeps it accurate without turning it into a maintenance burden.

## Why This Pays Off Before You're Asked, Not After

The founders who handle this well aren't the ones with the most sophisticated legal setup — they're the ones who did the vendor inventory before the first enterprise prospect asked for it, so the response to "send us your DPA and sub-processor list" is a same-day email with an existing document attached, rather than a two-week scramble that stalls the deal. Enterprise sales cycles are long enough already; being visibly unprepared on paperwork a competitor already has ready is a self-inflicted reason to lose a deal that had nothing to do with product fit.

Assembling an accurate sub-processor inventory across a real production stack, and getting the resulting DPA into shape a procurement team will actually accept, is exactly the kind of last-mile groundwork [LaunchStudio](https://launchstudio.eu/en/) does alongside security hardening — informed by Manifera's 11+ years of experience closing enterprise deals that hinge on exactly this kind of paperwork being ready.

[Talk to an engineer who can walk your actual stack](https://launchstudio.eu/en/#contact) and tell you, tool by tool, which DPAs you already have and which ones you're missing.

## Real example

### A SaaS Founder in Action: The Procurement Email That Stalled a Deal

Rutger Hofstra's invoicing SaaS, Boekly, had grown to twelve paying customers on Bolt-generated code before a mid-sized accounting firm's legal team requested a DPA and sub-processor list as a condition of signing. Rutger had never produced either document, and his own vendor relationships — Supabase, Resend, Stripe, and an OpenAI-powered invoice categorization feature — had DPAs available but unaccepted, sitting unread in each dashboard's legal settings.

The deal stalled for eleven days while Rutger tracked down each agreement manually and attempted to draft a customer-facing DPA from an online template he wasn't confident matched his actual data flows, particularly around what the OpenAI integration did with invoice line-item data. Manifera's review confirmed the AI integration sent line-item descriptions but not customer names or account numbers, which meaningfully simplified the DPA language, and helped assemble a proper sub-processor list Rutger could now reuse for every future enterprise prospect.

**Result:** Boekly closed the accounting firm deal and, three months later, reused the same sub-processor list and DPA template to close two more enterprise customers in under a week each, rather than eleven days.

> *"The actual paperwork took an afternoon once someone told me what I was even looking for. What cost me eleven days was not knowing the words 'sub-processor list' were a real, findable thing."*
> — **Rutger Hofstra, Founder, Boekly (Groningen)**

## Frequently Asked Questions

### Do I need to sign a DPA with every single vendor, even small ones like a form builder?

Only vendors that process personal data on your behalf need one — a form builder collecting names and emails does, a font-hosting service or a code-formatting tool doesn't. Focus the inventory on tools that actually touch customer or user personal data rather than every tool in your stack indiscriminately.

### Can I use a free DPA template instead of paying a lawyer to draft one?

A reputable template, often modeled on the EU Commission's Standard Contractual Clauses, is a reasonable starting point for most early-stage SaaS companies, and a one-time paid legal review to adapt it to your specific data flows is more cost-effective than either skipping legal review entirely or paying for a fully custom draft.

### What happens if a vendor I use doesn't offer a DPA at all?

Treat that as a real red flag, not a minor gap — a vendor processing personal data on your behalf without a ready DPA either hasn't thought seriously about EU compliance or is deliberately avoiding the commitment, and either reason is grounds to ask directly or consider a different vendor for anything touching personal data.

### How is a sub-processor list different from the DPA itself?

The DPA is the legal agreement establishing the processing relationship and its terms; the sub-processor list is the specific, maintained inventory of which vendors you use, referenced by the DPA and typically required to be kept current with an advance-notice mechanism for changes. You need both, and the list needs updating every time your stack changes.

### At what company size do enterprise customers actually start asking for this paperwork?

It varies, but the trigger is usually the customer's own compliance maturity rather than your company size — a single mid-sized customer with a real legal or procurement team can ask for a DPA and sub-processor list even when you're a two-person startup with a handful of total customers, so it's worth having ready before you assume you're "too small" to need it.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "Do I need to sign a DPA with every single vendor, even small ones like a form builder?", "acceptedAnswer": { "@type": "Answer", "text": "Only vendors that process personal data on your behalf need one. Focus the inventory on tools that actually touch customer or user personal data rather than every tool in your stack indiscriminately." } },
    { "@type": "Question", "name": "Can I use a free DPA template instead of paying a lawyer to draft one?", "acceptedAnswer": { "@type": "Answer", "text": "A reputable template modeled on the EU Commission's Standard Contractual Clauses is a reasonable starting point, and a one-time paid legal review to adapt it to your data flows is more cost-effective than skipping review entirely or paying for a fully custom draft." } },
    { "@type": "Question", "name": "What happens if a vendor I use doesn't offer a DPA at all?", "acceptedAnswer": { "@type": "Answer", "text": "Treat that as a real red flag. A vendor processing personal data on your behalf without a ready DPA either hasn't thought seriously about EU compliance or is avoiding the commitment, and either reason is grounds to ask directly or reconsider the vendor." } },
    { "@type": "Question", "name": "How is a sub-processor list different from the DPA itself?", "acceptedAnswer": { "@type": "Answer", "text": "The DPA is the legal agreement establishing the processing relationship; the sub-processor list is the specific, maintained inventory of vendors used, referenced by the DPA and typically requiring an advance-notice mechanism for changes." } },
    { "@type": "Question", "name": "At what company size do enterprise customers actually start asking for this paperwork?", "acceptedAnswer": { "@type": "Answer", "text": "It depends on the customer's compliance maturity rather than your size. A single mid-sized customer with a real legal team can ask for a DPA and sub-processor list even from a two-person startup with a handful of customers." } }
  ]
}
</script>
