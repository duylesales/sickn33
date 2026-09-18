---
Title: "Vibe Coding Developer: Clients Who Built It Themselves"
Keywords: vibe coding developer, lovable developer, client handover, code assessment, lovable expert, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: Agency / Freelancer (white-label partner)
---

# Vibe Coding Developer: Clients Who Built It Themselves

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Vibe Coding Developer: Clients Who Built It Themselves",
  "description": "A founder who built their own product is a different client from one who commissioned it. What they are actually afraid of, how to assess the work without insulting them, and how to scope a first engagement that succeeds.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-08-26",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/vibe-coding-developer-clients-who-built-it-themselves" }
}
</script>

A client who commissioned a product hands you a system somebody else made. A client who built it themselves hands you something they made, at night, over four months, while running a business — and that difference changes everything about the engagement.

They are proud of it, which is reasonable. They are slightly embarrassed about it, which is also reasonable. They have heard that what they built is probably insecure, and they do not know whether that is true or a story developers tell. And they are worried that hiring you means being told to throw it away.

Handle that badly and you lose the work in the first conversation. Handle it well and you acquire the most loyal category of client available, because you are the person who took what they made seriously.

## What They Are Actually Afraid Of

Four fears, rarely stated.

**That you will condescend.** They have already been told by someone that "vibe-coded apps are all broken". They are braced for it.

**That you will want to rebuild.** In their experience, developers respond to unfamiliar code by proposing to replace it, which means their four months were wasted and the price is enormous.

**That they will lose control of their own product.** They can currently change things themselves, which is the whole reason they built it this way. A professional engagement that ends with them unable to touch it is a downgrade they will resist even when it is technically better.

**That the price is unbounded.** They have no way to judge whether a quote is fair, so they fear an open-ended commitment more than a large fixed one.

Every one of these is addressable in the first conversation, and addressing them is most of the sale.

## The First Conversation

**Start with what works.** Something in the product functions and customers use it. Say so, specifically. "The booking flow is clean and your customers clearly understand it" costs nothing and changes the entire tone.

**Separate the interface from the infrastructure.** This is the single most useful framing available. What they built — the screens, the flow, the product decisions — is usually good, because they know their customers. What is missing is the invisible half: access rules, secrets, backups, monitoring, deployment. Telling them the visible part stays and the invisible part gets fixed removes the rebuild fear immediately, and it happens to be true.

**Be specific rather than general.** "It's insecure" is an insult. "Any logged-in customer can read every other customer's invoices by changing a number in the address, and I can show you in two minutes" is information. Show them. The demonstration converts more reliably than any argument, and it is the moment the conversation stops being about whether to hire you.

**Never disparage the tool.** They chose it, it worked, and criticising it criticises them. The tools are genuinely good at what they do; the gap is in what nobody asked for.

## Assess Before You Quote, and Charge For It

A paid assessment — two to four hours, a few hundred euros, credited against the engagement if they proceed — solves several problems at once.

It gives you the information to quote a fixed price accurately, which is impossible from a demo. It filters people who are shopping for free advice. It gives them something of value even if they go no further, which protects your reputation. And it converts the relationship from a sales conversation into work, which is where you are more convincing anyway.

What the assessment covers: access rules tested from a second account, credentials and where they live, data durability and backups, the deployment and whether it is reproducible, dependencies, error handling and logging, and anything touching money. Deliver it as a short written document with findings ranked by severity, each with what it means in plain language and what fixing it involves.

Write that document for the founder, not for a developer. They will read it, and they may forward it to an investor or a customer.

## Scoping the First Engagement

Keep it small and definite. A first engagement that succeeds is worth more than a large one that drifts.

Take the top findings, define each as a deliverable with a verifiable outcome, put a fixed price and a delivery date on the set, and exclude everything else explicitly — no new features, no redesign, one integration named.

Then deliver in a way that keeps them able to work. Conventional structure, no unnecessary abstraction, comments where a decision was non-obvious, and a short written note of what changed and why. If they can still open the project and add a field afterwards, you have kept the thing they valued most about building it themselves — and you will be called again.

## The Work Is Usually the Same

After a dozen of these you will stop being surprised. The findings repeat: access rules absent or permissive, a privileged key in the frontend, data written somewhere that does not survive a redeploy, no backups or none ever restored, secrets in files, no error tracking, a webhook with no signature verification, uploads in a public bucket with guessable names, and a schema that exists only in a dashboard.

That repetition is an asset. It lets you productise — a named package with a fixed price and a known duration — and it makes your estimates accurate, because you have seen this project before under a different name.

## What Not to Do

**Do not rewrite silently.** Replacing their code with something you prefer, without agreement, destroys trust even when the result is better.

**Do not introduce tooling they cannot use.** A sophisticated setup they cannot operate makes them dependent, which they will eventually resent.

**Do not fix everything you find.** Report it all; fix what was agreed. Unrequested work is either unbilled or a surprise invoice, and both are bad.

**Do not take over their accounts.** Everything stays in their name, with your access removable. Say this early; it answers the control fear directly.

## Where the Work Comes From

These clients are not searching for "developer". They search for their problem — how to make a Lovable app secure, what happens when a customer's procurement team asks about data, why their app slowed down at 300 users.

Which means the way to reach them is to answer those questions publicly, in plain language, in Dutch as well as English. One useful page about a specific problem outperforms a portfolio, because it demonstrates the thing they are actually buying: that you understand what is wrong and can explain it without making them feel foolish.

## The Second Engagement Is Where the Business Is

A first engagement pays for itself. A second one makes the client relationship an asset, and with this particular type of client the second one is unusually likely — if you set it up.

**Finish by telling them what is next.** The assessment found more than you fixed. Hand over the remaining items, ordered, with what each would cost and what triggers it: "the multi-tenancy work matters when you sign a customer with more than one employee", "the reporting queries will need attention around a thousand records per customer". This is not upselling; it is the roadmap they cannot write themselves, and founders keep it.

**Offer maintenance, priced modestly.** Monitoring, updates, backups verified, small fixes, a monthly note. It is the arrangement that keeps you in contact, and contact is what produces the next project — because you will notice what needs doing before they do.

**Stay reachable for small things.** A founder who can ask you a two-minute question without opening a negotiation will bring you the two-week project when it arrives. Build that into the maintenance fee rather than billing it, and the goodwill compounds.

**Check in when their business changes.** A new customer segment, a first enterprise contract, a growth spurt — each has technical consequences you can predict and they cannot. A message that says "you mentioned you were pitching a housing association; that will bring questions about data separation, and here is what that costs to prepare" is worth more than any marketing you could do.

**Ask for the introduction.** Founders who built their own products know other founders who built their own products. This is the most reliable source of this kind of work, and almost nobody asks, because asking feels awkward at exactly the moment the client is most pleased with you.

The economics are straightforward. Acquiring one of these clients takes an assessment and a conversation; keeping one takes a monthly email. Practices that grow are almost always the ones that noticed the difference.

## When the Work Is Bigger Than You

Some engagements exceed what one freelancer should take on alone — multi-tenancy across a live product, a migration with real data, a security programme for a customer with a procurement process.

LaunchStudio takes that work on a white-label basis, delivered under your brand on fixed scope and fixed price, so you keep the client relationship and quote with confidence. The engineers are Manifera's: eleven years, 160+ projects, clients including Vodafone, TNO and CFLW, working from Amsterdam Herengracht 420, Singapore and Ho Chi Minh City.

[Tell us what your client built](https://launchstudio.eu/en/#contact), or see how the [packages](https://launchstudio.eu/en/#packages) are scoped.

## Real example

### The Assessment That Sold Itself

Yara Postma works as a freelance vibe coding developer in Delft, taking on Lovable and Bolt projects for founders who built them personally. Her first year was frustrating: prospects arrived interested, she explained what was wrong, and roughly two in ten proceeded.

The pattern in the losses was consistent. She had been describing problems in general terms — the app was insecure, it needed proper architecture, the data layer was not production-ready — and founders heard a developer preparing to charge them for a rebuild of something that worked fine.

She changed two things. She introduced a paid assessment at €300, credited against any engagement. And in the first call she stopped describing and started demonstrating: two browser windows, two accounts, one customer's records opened from the other account by changing a number.

The demonstration takes four minutes. Every founder she has shown it to has understood immediately, and none has argued.

Her assessment document changed too. Findings ranked by severity, each written in plain language with what it means for the business — "a customer's competitor could read their prices", not "missing row level security" — and each with a fixed price to fix. The last page lists what is already good about the product, which she reports is the page founders mention.

**Result:** over the following year, 23 of 31 assessments converted into engagements averaging €2,700. Four founders who did not proceed immediately came back within six months, three of them after a customer asked them a security question they could not answer. Two now send her their own referrals.

> *"I was telling founders their product was insecure and watching them stop listening. Now I show them one screen for four minutes and they ask me what it costs to fix."*
> — **Yara Postma, Freelance vibe coding developer (Delft)**

**Cost & Timeline:** Assessment restructured to €300 fixed, credited against engagements averaging €2,700 — change implemented in one week.

## Frequently Asked Questions

### How is a founder who built it themselves different from other clients?

They made the thing, so criticism of the product reads as criticism of them. They also fear being told to rebuild, losing the ability to change it themselves, and an unbounded price. Addressing those three fears is most of the sale.

### How do I explain the problems without insulting them?

Separate the interface from the infrastructure: what they built is usually good because they know their customers, and what is missing is the invisible half nobody asked for. Then demonstrate one concrete flaw rather than describing many in general terms.

### Should I charge for an assessment?

Yes. Two to four hours at a few hundred euros, credited against the engagement, gives you what you need to quote a fixed price, filters unserious prospects, and starts the relationship as work rather than sales.

### What should the first engagement look like?

Small and definite: the top findings as deliverables with verifiable outcomes, a fixed price, a delivery date, and explicit exclusions. A small engagement that succeeds leads to more; a large one that drifts does not.

### How do these clients find a developer?

Not by searching for one. They search for their problem — making an app secure, answering a customer's data questions, why it slowed down. Answering those questions publicly in plain language reaches them better than a portfolio.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "How is a founder who built it themselves different from other clients?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "They made it, so product criticism lands personally. They fear a rebuild, losing the ability to change it themselves, and an unbounded price."
      }
    },
    {
      "@type": "Question",
      "name": "How do I explain the problems without insulting them?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Separate interface from infrastructure — what they built stays, the invisible half gets fixed — and demonstrate one concrete flaw rather than describing many."
      }
    },
    {
      "@type": "Question",
      "name": "Should I charge for an assessment?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes — a few hundred euros credited against the engagement gives you quoting information, filters prospects and starts the relationship as work."
      }
    },
    {
      "@type": "Question",
      "name": "What should the first engagement look like?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Small and definite: top findings as deliverables with verifiable outcomes, fixed price, delivery date and explicit exclusions."
      }
    },
    {
      "@type": "Question",
      "name": "How do these clients find a developer?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "By searching their problem rather than for a developer, so publicly answering those problems in plain language works better than a portfolio."
      }
    }
  ]
}
</script>
