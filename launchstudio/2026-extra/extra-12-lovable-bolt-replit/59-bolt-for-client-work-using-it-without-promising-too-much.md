---
Title: "Bolt for Client Work: Using It Without Promising Too Much"
Keywords: bolt for agencies, client work, scoping, prototype expectations, white label, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: Agency / Freelancer (White-Label Partner)
---

# Bolt for Client Work: Using It Without Promising Too Much

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Bolt for Client Work: Using It Without Promising Too Much",
  "description": "Showing a client a working prototype in a day is a genuine advantage and a trap. Framing what they are seeing, quoting the production work honestly, and the contract terms that prevent the argument.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-01-09",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/bolt-for-client-work-using-it-without-promising-too-much" }
}
</script>

For an agency or a freelancer, these tools change the sales conversation completely. Instead of a proposal describing what you would build, you arrive at the second meeting with something the client can use.

Nothing persuades like that. It also creates the specific problem this article is about: the client has now seen a working application, and every subsequent conversation about time and cost is measured against the impression that it already exists.

"You built it in a day, so why is finishing it eight weeks?" is a question with a good answer, and the answer has to be given before the question rather than after.

## Say What It Is, Every Time

The framing matters more than anything else and it must be established before the demonstration, not defensively afterwards.

What works: this is a working model of the product, built to confirm we agree on what it should do. It runs, you can click through it, and it is not the product — it has no security, no reliability, no protection of anyone's data. Those are the next eight weeks.

Say it, put it in writing in the same email as the link, and repeat it at the start of the demonstration. Clients accept this readily when it is said in advance and resist it entirely when it emerges during a discussion about cost.

The framing also helps you. A prototype explicitly labelled as a model can be thrown away without anyone feeling that money was wasted, which preserves your ability to say that a different structure is needed.

## Quote Discovery and Production Separately

The commercial structure that works is two stages with their own prices.

**Discovery**, a small fixed fee, producing a working prototype and a written specification of what the real product must do. The client owns both. If they stop here, they have something valuable and you have been paid.

**Production**, quoted from the specification, delivering the thing customers can use.

Three benefits. The prototype is paid work rather than an elaborate free pitch. The production quote is based on something concrete rather than on a conversation, so it is more accurate and easier to defend. And the client can decline stage two without either party feeling misled.

Never quote production before the prototype exists. The prototype is what tells you what the product actually is, and a number given before that is a guess you will be held to.

## Itemise What Production Buys

A single figure for "productionising the prototype" invites the comparison you do not want. An itemised list of work turns it into a specification.

The items that appear in almost every such quote: authorisation and access control across every endpoint; moving credentials server-side and rotating them; server-side validation; a real data model with constraints and migrations; authentication, sessions and password recovery done properly; file handling with type verification and private storage; payments including the failure paths; error handling, logging and monitoring; backups with a tested restore; three environments and a repeatable deployment; performance work — indexes, caching, pagination; accessibility; and the legal and privacy work if the client is selling in Europe.

A client reading that list stops asking why it takes eight weeks. Most of them have no idea any of it exists, which is not their failing — it is invisible by design.

## Be Careful About What You Warrant

Contractually, three provisions are worth having in any agreement involving AI-generated code.

**Say what the prototype is.** A clause stating that the discovery deliverable is a demonstration model, not fit for production use, not warranted, and not to be deployed to real users. Clients do deploy them otherwise, and you do not want to be the supplier of record when that goes wrong.

**Be honest about intellectual property.** Generated code may resemble other code. You cannot warrant originality in the way you might for handwritten work, and a blanket warranty you cannot support is worse than a clear statement of what you do and do not guarantee.

**Limit liability the way you would anywhere.** Capped at fees, excluding indirect damage, with the exclusions Dutch law does not permit left out. This is ordinary and it matters more here because the work moves fast.

## Tell Them How It Was Built

The question of whether to disclose that you used AI tools has a clear answer: yes, plainly, as a matter of course.

It will come out. A developer the client hires later will see it, and a client who feels it was concealed treats everything else you said as suspect.

Framed properly it is an advantage rather than a confession: we use these tools to get to a working model in days instead of weeks, which is why your discovery costs what it does. The engineering that follows is the same engineering it has always been.

The clients who object to the tools are rare. The clients who object to finding out later are most of them.

## Who Owns What, Precisely

Clients ask, and a vague answer creates a problem at exactly the moment you least want one — usually when they are considering working with someone else.

The position that is fair and easy to state: the client owns the deliverables they paid for, including the source code, the data and anything produced specifically for them. You retain whatever you brought — your own libraries, components and internal tooling — and grant them a licence to use it as part of what you delivered.

Two points specific to this kind of work. Generated code cannot be warranted as original in the way handwritten work sometimes is, and saying so plainly in the agreement is better than a warranty nobody could support. And the tool subscriptions are yours rather than theirs, which matters when a client assumes that paying for the project included an account they can continue using.

The handover deserves the same precision. Agree in advance what it consists of: the repository transferred to their account, the environment variables documented, the services listed with who holds each account, the deployment process written down, and a walkthrough. Clients who have been handed a zip file and a login remember it, and the ones who have been handed a repository with history and a page of documentation recommend you.

## Where the Margin Actually Is

For an agency, the economics of this work are not what the first fast prototype suggests, and getting them right determines whether the practice is sustainable.

Discovery is fast and should be priced as a product rather than by the hour. Two days of work sold at €2,500 is good business and the client gets something genuinely valuable — but it does not scale into a living on its own, and pricing it by time undervalues it badly.

Production is where the hours are, and it is ordinary engineering priced ordinarily. The mistake is to assume the tools compress it the way they compressed discovery. They help — scaffolding, boilerplate, tests — but authorisation, data modelling, payment failure paths and accessibility are thinking rather than typing, and thinking has not become faster.

The third piece, and the one agencies neglect, is what happens afterwards. A product that has launched needs updates, monitoring, incident response and small changes indefinitely. A retainer covering that is predictable revenue on work you are already best placed to do, and it keeps you in the relationship when the client's next project appears.

The shape that works: discovery as a fixed-price product, production quoted from the specification and staffed properly, and a monthly arrangement afterwards. Agencies that price only the middle stage find themselves competing on how fast a prototype can be produced, which is a race with no winner.

## Setting This Up

For an agency or freelancer this is typically a day of preparation that then applies to every engagement: a written framing of what a prototype is, sent with every demonstration link; a two-stage commercial structure with discovery priced and paid; a standard itemised list of production work to accompany every quote; contract clauses covering the prototype's status, intellectual property and liability; a disclosure position on tool use; and a checklist for the production phase so nothing on the list is forgotten when the work is actually done.

LaunchStudio does the production stage as a white-label partner for agencies who prefer to keep the client relationship and hand over the hardening. Behind it is Manifera — eleven years, 160+ projects, 120+ engineers, from Herengracht 420 in Amsterdam.

[Ask us to quote the production stage](https://launchstudio.eu/en/#contact) while you keep the client.

## Real example

### A Prototype the Client Deployed

Joost Meijer runs Studio Meridiaan, a three-person digital agency in Utrecht working mostly with Dutch scale-ups.

He pitched a customer portal to a facilities company by building a prototype in Bolt over two days and demonstrating it in the second meeting. The client was delighted. They asked for the link so they could show their board.

Three weeks later, while Joost was preparing the production quote, the client's operations manager put the prototype link in an email to 40 customers, because it worked and they were impatient. Customer names, contract details and service requests went into a database with no access control, hosted on a preview URL, with the API key in the frontend.

Nothing was breached, as far as anyone could establish. But the client had by then used it for three weeks, considered it live, and was unhappy at being quoted €18,000 for what they experienced as making an existing system slightly better.

The engagement was rescued over four business days: the prototype taken offline with an explanation of exactly what had been exposed and what had not, supported by the access logs; the three weeks of real data migrated into a properly built version rather than discarded, which mattered to the client more than anything else; the production work itemised into 14 named items with the reasoning for each; and the relationship rebuilt around a two-stage structure applied from that point on.

Since then, Studio Meridiaan has used a standard framing: every prototype link expires after 14 days, is password-protected, carries a visible banner reading *demonstratiemodel — niet voor gebruik met echte gegevens*, and is accompanied by a one-page written statement of what it is. Discovery is quoted at €2,500 and paid before the prototype is built.

**Result:** across eleven engagements since, the production quote has been accepted nine times and never questioned on the basis of the prototype's speed. Joost's view is that the banner and the expiry do more work than any conversation.

> *"They deployed it to forty customers because it worked. That was not their mistake — I had shown them something that worked and said nothing about what it was."*
> — **Joost Meijer, Partner, Studio Meridiaan (Utrecht)**

**Cost & Timeline:** €4,300 (incident assessment and client communication, data migration from prototype to production build, itemised production specification, commercial structure and contract clauses, prototype framing standards) — completed in 4 business days.

## Frequently Asked Questions

### How do I stop a client treating a prototype as finished?

Say what it is before demonstrating, in writing; expire the link; password-protect it; and put a visible banner on it stating it is a demonstration model not for real data.

### Should discovery be free?

No. Charge a fixed fee for a prototype plus a written specification, both of which the client owns. It makes the work valuable, and the production quote that follows is based on something concrete.

### How do I justify the production cost?

Itemise it. Authorisation, credentials, validation, data model, authentication, file handling, payments, logging, backups, environments, performance, accessibility, privacy. Clients stop comparing against the prototype once they see the list.

### Should I tell clients I used AI tools?

Yes, as a matter of course. It will emerge later, and a client who feels it was concealed distrusts everything else. Framed as speed in discovery, it is an advantage.

### What contract terms matter for this work?

A clause stating the prototype's status and that it must not be deployed, an honest position on intellectual property given generated code, and an ordinary capped liability limitation.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "How do I stop a client treating a prototype as a finished product?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "State what it is in writing before demonstrating, expire and password-protect the link, and show a visible banner marking it a demonstration model."
      }
    },
    {
      "@type": "Question",
      "name": "Should discovery prototypes be free?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No. Charge a fixed fee for the prototype and a written specification the client owns, then quote production from it."
      }
    },
    {
      "@type": "Question",
      "name": "How do I justify production costs after a fast prototype?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Itemise the work — authorisation, credentials, validation, data model, auth, payments, logging, backups, environments, performance, accessibility, privacy."
      }
    },
    {
      "@type": "Question",
      "name": "Should agencies disclose AI tool use to clients?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. It emerges later regardless, and concealment damages trust. Framed as discovery speed it is an advantage."
      }
    },
    {
      "@type": "Question",
      "name": "Which contract terms matter for AI-assisted client work?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "The prototype's status and a prohibition on deploying it, an honest intellectual property position, and a capped liability limitation."
      }
    }
  ]
}
</script>
