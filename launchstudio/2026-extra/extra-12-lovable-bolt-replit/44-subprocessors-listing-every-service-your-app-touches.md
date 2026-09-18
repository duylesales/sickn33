---
Title: "Subprocessors: Listing Every Service Your App Touches"
Keywords: subprocessors, subverwerkers, vendor list, data flows, third party services, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: SaaS Scale-Up
---

# Subprocessors: Listing Every Service Your App Touches

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Subprocessors: Listing Every Service Your App Touches",
  "description": "Every external service your product sends data to is a subprocessor your customers are entitled to know about. Finding the ones you forgot, publishing the list, and notifying customers before you add one.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-12-10",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/subprocessors-listing-every-service-your-app-touches" }
}
</script>

Your customer signed an agreement with you. Their data is then handled by your hosting platform, your database provider, your email service, your error tracker, your analytics tool and possibly a model API — none of whom your customer has ever heard of.

Those are subprocessors. Your customer is entitled to know who they are, what each receives and where it goes, and to be told before you add another one.

Most founders can name three or four. The actual number in a typical AI-built product is eight to twelve, and the gap between those two figures is where the uncomfortable conversations start.

## Find All of Them

The list is not a memory exercise. Build it from evidence.

**The obvious four:** hosting, database, email, payments.

**The ones added for convenience:** error tracking, analytics, support chat, session recording, uptime monitoring, feature flags, a scheduling widget.

**The AI ones:** every model API, including the one behind a feature you shipped in an afternoon.

**The infrastructure ones:** a CDN, DNS, object storage, a search service, a queue.

**The business ones that touch customer data:** your CRM if it holds their contacts, your invoicing tool, a document signing service, a mailing list containing their staff.

Then verify against the code rather than the memory. Search for external URLs, review your environment variables — every credential implies a service — and open the network tab on your own product to see what the browser contacts. Products routinely find a font service, an embedded map or an analytics tool nobody remembers adding.

## Record What Each Actually Receives

The list of names is the easy half. What matters for a customer's review is what each service gets.

Be specific. "Error tracking" is not an answer; "error tracking receives stack traces and, currently, full request bodies including customer names" is. That level of specificity is also how you discover what to fix — the second version of that sentence is one nobody wants to publish, which is exactly why writing it produces a change.

For each: what data, for what purpose, where it is processed and stored, and under what contractual basis if outside the EEA.

## Every One Needs an Agreement

You are obliged to have a processing agreement with each subprocessor, imposing the same obligations you accepted from your customer.

For large providers this is a standard document you accept during signup, frequently as part of the terms. Find it, confirm it applies to your account tier, and keep a copy or a link.

Two places founders find a gap. Model APIs, where the data processing terms sometimes require explicit acceptance or a particular plan, and where behaviour around training on submitted data differs by tier. And small tools added on a free plan, which occasionally offer no processing agreement at all — which makes them unusable for customer data regardless of how convenient they are.

## Publish the List

A public page listing your subprocessors, what each receives and where, with a last-updated date.

It shortens procurement considerably, because a reviewer reads it instead of asking. It signals a level of operational maturity most small competitors do not reach. And it is the artefact your processing agreement's annex refers to, so maintaining one keeps several documents true at once.

Offer a way to subscribe to changes, even if that is an email address people can ask to be added to. The notification obligation is easier to meet when there is a mechanism for it.

## Adding One Is a Decision, Not a Configuration

The obligation is to notify customers before adding a subprocessor, with an opportunity to object. That turns "install this tool and see if it helps" into a small process.

The process worth adopting: before any new service receives customer data, confirm it has a processing agreement, confirm where it processes and stores, add it to the list, and notify customers with a notice period — 30 days is common.

This sounds heavy until you notice the alternative. A founder who adds a service casually and mentions it later has breached a contractual commitment, and the discovery usually happens during a review with a customer who is already asking careful questions.

It also imposes a useful discipline. Each new subprocessor is a permanent obligation, another entry in the register, another dependency, another thing to review annually. A moment's friction before adding one is proportionate.

## Review Them Annually, Because They Change

A subprocessor list is a snapshot of relationships that move underneath you, and three kinds of change are worth catching.

**The service changes what it does.** A provider adds a feature that processes data differently, moves a region, or updates its terms — including, increasingly, its position on using submitted data for model training. Providers notify these changes by email to whoever registered the account, which is frequently an address nobody reads.

**The service is acquired.** New owner, potentially new jurisdiction, new terms. This is the change most likely to matter to a customer and least likely to be noticed by a founder.

**You stop using it and the data remains.** The abandoned-tool problem described elsewhere in this series. Removing a service from your code does not remove your data from theirs — that requires a deletion request, which should be part of decommissioning.

So an annual pass: confirm each service is still used, still has a current agreement, still processes where you said, and still holds only what you expect. For anything you stopped using, request deletion and get confirmation.

Put the renewal dates and the account email in the same document. A subprocessor list that also records who holds the account and where the invoices go is the document that makes handing the product to someone else possible — and that, rather than compliance, is usually the reason founders are grateful it exists.

## The Ones Hiding in the Browser

Services your server calls are findable in your code. Services the visitor's browser calls are a separate category, and they are the ones founders miss entirely because nothing in the backend mentions them.

Every third-party script, stylesheet, font, image or embed on your pages means the visitor's browser makes a request to that company — carrying their IP address, the page they are on, and frequently a cookie. That is a data flow you are responsible for even though your server was never involved.

The usual inhabitants of this category in an AI-built product: a font service imported by a generated stylesheet, an embedded map, a video player, a support chat widget, a social media embed, an analytics script, and an icon library loaded from a CDN.

Two of those deserve particular attention in a product with logged-in users. A chat widget on an authenticated page can typically read the page, which means it can see whatever your customer's data is on screen. And any script on that page runs with your application's origin, so it is a security dependency as much as a privacy one.

The remedy is mostly the same in both directions: self-host what you can — fonts and icons are trivial — replace embeds with click-to-load placeholders, and keep third-party scripts off authenticated pages entirely. What remains after that is a short list you have chosen deliberately, which is the state you want before anyone asks.

A content security policy is what makes this durable rather than a one-time cleanup: declare which sources your pages may load from, and anything added later that is not on the list simply does not load. It is a header, it takes an afternoon to get right, and it converts "we removed the third parties" into "a third party cannot be added without a deliberate change".

## Setting This Up

For an existing product this is typically half a day: every external service identified from code, environment variables and network traffic rather than memory, what each receives recorded specifically, processing and storage locations confirmed, a processing agreement located for each with gaps closed or the service replaced, unused services removed and their data deleted, a published subprocessor page with a last-updated date and a way to subscribe, the same list wired into your processing agreement annex and register, and a written process requiring notification before a new service receives customer data.

LaunchStudio produces this alongside the register and the processing agreement, since they are three views of one inventory. Behind it is Manifera — eleven years, 160+ projects, clients including Vodafone, TNO and CFLW, from Herengracht 420 in Amsterdam.

[Ask us to find your subprocessors from your code](https://launchstudio.eu/en/#contact). The count is usually higher than expected.

## Real example

### Eleven, Not Four

Manon Duyvesteyn built Tolkplanner in Lovable: interpreter booking and assignment for translation agencies and public bodies, 24 agencies with around 1,100 interpreters.

A customer's privacy officer asked for her subprocessor list before renewing. She wrote down four: hosting, database, email and payments.

The audit against her code found eleven. In addition to the four: error tracking receiving full request bodies including interpreter names and assignment details; a support chat widget loading on the logged-in application with access to the page; an analytics service capturing URLs that contained assignment identifiers; a model API summarising assignment briefs, added six months earlier, sending the full brief text; a font service contacted by every page load, which meant visitor IP addresses were going to a third party; an SMS provider for interpreter notifications, which she had genuinely forgotten because it was configured once; and a document signing service holding signed assignment contracts including interpreters' personal details.

Of the eleven, four had no processing agreement in place: the analytics service, the font service, the model API on the tier she was using, and the chat widget.

Four business days: the full inventory built from code, environment variables and network traffic; what each service receives documented specifically; the font service removed and fonts self-hosted; the analytics service replaced with a cookie-free tool that receives no identifiers, and URLs changed to stop carrying assignment identifiers; error tracking configured to scrub request bodies; the model API moved to a tier with data processing terms and an EU region, with the payload reduced to the brief text alone rather than the full assignment record; the chat widget removed from authenticated pages and replaced with a support link; processing agreements located and filed for the remaining services; a published subprocessor page with locations and a last-updated date; and a written process requiring agreement, location check, list update and 30-day customer notification before any new service.

**Result:** the renewal proceeded and the privacy officer specifically noted the published page. Manon sends the link with every proposal now. Two of the eleven services no longer exist in her product at all, which she describes as the most satisfying part.

> *"I would have sworn there were four. The one that bothered me most was the font — every visitor's IP address going to a company I had never thought about, because a generated stylesheet imported it."*
> — **Manon Duyvesteyn, Founder, Tolkplanner (Den Haag)**

**Cost & Timeline:** €2,800 (code and traffic audit, per-service documentation, font self-hosting, analytics replacement, error scrubbing, model API tier and region change with payload reduction, chat widget removal, agreement collection, published page, notification process) — completed in 4 business days.

## Frequently Asked Questions

### What counts as a subprocessor?

Any external service that processes your customers' personal data on your behalf — hosting, database, email, error tracking, analytics, model APIs, storage, SMS, document signing, and anything else that receives it.

### How do I find the ones I have forgotten?

From evidence rather than memory: search the code for external URLs, review every credential in your environment configuration, and open the network tab on your own product.

### Does every subprocessor need an agreement?

Yes, imposing the obligations you accepted from your customer. Large providers include one in their terms; small free-tier tools sometimes offer none, which makes them unusable for customer data.

### Do I have to publish the list?

It is not strictly required, but it shortens procurement, demonstrates maturity and keeps your processing agreement annex accurate. Most customers who ask would rather read a page than exchange emails.

### What do I do before adding a new service?

Confirm it has a processing agreement, check where it processes and stores, add it to the list, and notify customers with a notice period — typically 30 days — before it receives any data.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What counts as a subprocessor?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Any external service processing your customers' personal data on your behalf — hosting, database, email, error tracking, analytics, model APIs, storage and more."
      }
    },
    {
      "@type": "Question",
      "name": "How do I find subprocessors I have forgotten?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Audit from evidence — external URLs in code, every credential in environment configuration, and the network tab on your own product."
      }
    },
    {
      "@type": "Question",
      "name": "Does each subprocessor need a processing agreement?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes, imposing the obligations you accepted. Large providers include one in their terms; some free-tier tools offer none and cannot be used for customer data."
      }
    },
    {
      "@type": "Question",
      "name": "Should the subprocessor list be published?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "It shortens procurement, signals maturity and keeps your processing annex accurate — most reviewers prefer a page to an email exchange."
      }
    },
    {
      "@type": "Question",
      "name": "What is the process before adding a new service?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Confirm a processing agreement, check processing and storage location, update the list, and notify customers with around 30 days' notice."
      }
    }
  ]
}
</script>
