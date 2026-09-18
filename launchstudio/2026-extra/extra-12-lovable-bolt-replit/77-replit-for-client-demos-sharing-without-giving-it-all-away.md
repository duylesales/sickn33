---
Title: "Replit for Client Demos: Sharing Without Giving It All Away"
Keywords: replit demos, sharing a prototype, access control, demo data, client presentations, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: Agency / Freelancer (White-Label Partner)
---

# Replit for Client Demos: Sharing Without Giving It All Away

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Replit for Client Demos: Sharing Without Giving It All Away",
  "description": "Sending a link is the fastest way to show a client what you built and the easiest way to leak your code, your keys and somebody else's data. How to share a demonstration safely and deliberately.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-02-14",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/replit-for-client-demos-sharing-without-giving-it-all-away" }
}
</script>

Showing somebody a working application is the most persuasive thing you can do, and a link takes ten seconds to produce. That combination is why so many demonstrations leak something.

Three things travel with a carelessly shared project: the code, which for an agency is the work the client has not yet paid for; the credentials, which are whatever the project runs with; and the data, which in a demonstration built from a previous engagement may belong to a different customer entirely.

None of this requires the recipient to be malicious. It requires only that they forward the link, which is what people do with things they find interesting.

## Decide What You Are Sharing

Three different things get called "sharing a demo", and they have different risks.

**A running application at a URL.** The recipient uses the product and cannot see the code. This is usually what you want.

**Access to the project.** The recipient can read the code, see the configuration, and fork it. This is what you do not want, and it is the default for several sharing mechanisms.

**A recording.** Nothing runs, nothing leaks, and you control exactly what is seen. Underrated, and for many first demonstrations the correct answer.

Know which one the link you are about to send provides. The most common mistake is sending a project link when a deployment link was intended.

## Never Demonstrate With Real Data

The rule that prevents the worst outcome: a demonstration runs on invented data, always.

Using a previous client's data to demonstrate to a prospect is a disclosure of that client's information to a third party. It happens because it is convenient — the product is populated, the screens look real — and it is a breach of the agreement you signed with the first client.

Build a demonstration dataset instead: plausible names, realistic volumes, the awkward cases that make the product look capable. It takes an afternoon once, it is reusable across every demonstration, and it lets you construct the scenario that shows your product at its best rather than whatever happens to be in a real account.

There is a commercial benefit too. Real data is messy and shows what one customer happens to do; invented data can be arranged to tell the story you want to tell.

## Put a Door on It

A demonstration URL that anyone can open is a demonstration URL that will be found, indexed and shared.

Three levels, in increasing order of protection.

**A password**, shared with the client. Adequate for most demonstrations and takes a minute.

**Individual accounts** for the people who should see it, so you know who looked and can revoke one person's access.

**A time limit.** The link stops working after a fortnight, which as the client work article in this series describes, also prevents the demonstration from being quietly adopted as a live system.

Add a noindex directive regardless, so it does not appear in search results — which is how a client discovers that their unannounced product is publicly visible.

## Make It Obvious What It Is

A visible banner on every screen: *demonstration — not for use with real data*.

This is not decoration. It is what prevents the client's operations manager from putting the link in front of forty customers, which is the incident the Bolt client work article in this series describes in detail.

It also protects you. A demonstration that is clearly labelled cannot later be characterised as something you delivered, and the label is the cheapest contractual protection available.

## Separate the Demonstration From Everything Else

The demonstration should run with its own everything: its own database, its own credentials, its own storage, its own email configuration that cannot send.

The reason is not elegance. A prospect clicking through a demonstration that shares a database with a live client is one confused screen away from seeing real records, and a demonstration that can send email is one form submission away from emailing somebody real.

For an agency running several demonstrations, a template project with a fresh copy of the dataset per prospect is worth the hour it takes to set up. Each prospect gets their own copy, nothing is shared, and a demonstration can be wrecked without consequence — which is what you want a prospect to feel free to do.

## Build the Dataset Deliberately

A demonstration dataset is a sales asset rather than test data, and treating it as one changes what goes into it.

Four properties make a demonstration persuasive.

**Enough volume to look real.** Three records look like a prototype. Three hundred look like a working system, and the difference in how a prospect responds is considerable.

**Names and details that fit the market.** Dutch names, Dutch cities, Dutch company forms, amounts in euros, dates in the right format. A demonstration full of American placeholder names quietly signals that the product was not built for here.

**The awkward cases the prospect will ask about.** The cancelled appointment, the partial payment, the customer with two addresses, the record with a long name that tests the layout. Prospects probe exactly these, and having them present and handled well is more convincing than any feature list.

**A scenario you can walk through.** Not a random assortment but a story: this practice, this week, this problem, this is how the product handles it. The dataset should support the demonstration you intend to give.

Regenerate it rather than accumulating in it. A demonstration account that has been clicked through by forty prospects is full of half-finished records and test entries called "aaa", and resetting it to a clean state before each demonstration takes one command if it was built as a script.

## After the Demonstration

Two things happen next, and both deserve a decision made in advance rather than in the moment.

**The prospect asks to keep using it.** This is a good sign and the answer is not yes. A demonstration environment has no security, no backups and no reliability, and the incidents throughout this series begin with exactly this. The answer that works: yes, and that starts the production stage — here is what that involves and what it costs.

**The prospect goes quiet.** The link keeps working, the data sits there, and in six months it is still there with credentials nobody has rotated. Expire demonstrations automatically and delete their data on a schedule, so that a dormant opportunity does not become a liability with your name on it.

For an agency, both of these argue for treating the demonstration as a deliverable with a lifecycle rather than as an artefact left lying around. Created for a prospect, protected, labelled, expiring, and deleted when the opportunity closes either way.

One further habit worth adopting: record what you showed. Which version, which dataset, which scenario. When the same prospect returns three months later saying "it did X when you showed us", you want to be able to check rather than to contradict them — and a product that changes weekly will have moved since.

A line in a file per demonstration — date, prospect, version, dataset — takes seconds and settles that conversation in one look rather than one guess.

It is also useful internally: three months of those lines tells you which scenarios you actually demonstrate, which is usually a shorter list than the product's feature set and a good guide to what the marketing pages should emphasise.

## Setting This Up

For an agency or founder demonstrating regularly this is typically half a day, once: a reusable demonstration dataset of invented but realistic data, a template project cloned per prospect with its own database, credentials and storage, outbound email disabled by the absence of credentials rather than by configuration, a deployment link rather than project access, protected by a password or individual accounts with a time limit, a noindex directive, a visible banner on every screen, and a written statement of what the demonstration is sent alongside the link.

LaunchStudio does the production build after the demonstration has done its work, as a white-label partner for agencies who keep the client relationship. Behind it is Manifera — eleven years, 120+ engineers, 160+ projects, from Herengracht 420 in Amsterdam.

[Ask us to quote the production stage](https://launchstudio.eu/en/#contact) from a demonstration you have already shown.

## Real example

### A Demonstration With Another Client's Patients

Fabienne Schuurmans runs a two-person studio in Utrecht building scheduling software for healthcare practices.

Pitching to a dental group, she demonstrated using the project she had built for an existing physiotherapy client, because it was populated and looked convincing. She shared the project link rather than a deployment link, so the prospect could "have a proper look".

The prospect forwarded it to two colleagues. One of them opened the project files, found the configuration, and mentioned to Fabienne that the database connection string was visible. The database contained around 900 real patients of the physiotherapy practice: names, dates of birth, appointment histories and treatment notes.

She had also, in the same link, disclosed the entire codebase of a product the physiotherapy client had paid for.

Three business days: the project made private immediately and the database credentials rotated; the extent of access established from the platform and from the three recipients, all of whom confirmed in writing what they had opened; the physiotherapy client informed within a day, with a written account and the credential rotation evidence, and the incident assessed as a personal data breach and reported to the Autoriteit Persoonsgegevens given the health data involved; a demonstration dataset built with 300 invented patients across two invented practices, including the awkward cases that show the product well; a template project created that is cloned per prospect with its own database, credentials and storage, and with no email credentials at all; deployment links replacing project links, password-protected, expiring after 14 days, with a noindex directive and a banner on every screen; and a one-page statement of what a demonstration is, sent with every link.

**Result:** the physiotherapy practice remained a client, which Fabienne attributes entirely to telling them within a day and in full. The dental group did not proceed. Her assessment is that the demonstration dataset has made her demonstrations better as well as safer, because she can arrange the scenario rather than working with whatever a real practice happens to have.

> *"I shared a project link so they could have a proper look, and what they could look at was nine hundred real patients and a codebase somebody else had paid for."*
> — **Fabienne Schuurmans, Partner, studio in Utrecht**

**Cost & Timeline:** €3,400 (credential rotation and access assessment, client notification and regulatory report, demonstration dataset, per-prospect template with isolated resources, protected expiring deployment links with banner and noindex, written demonstration statement) — completed in 3 business days.

## Frequently Asked Questions

### What is the difference between sharing a project and a deployment?

A deployment link lets someone use the application. A project link lets them read the code, see the configuration and fork it. Sending the second when you meant the first is the most common mistake.

### Can I demonstrate with a real customer's data?

No. It discloses their information to a third party and breaches the agreement you signed. Build an invented dataset, which is also better for demonstrating because you control the scenario.

### How should a demonstration link be protected?

A password at minimum, individual accounts where you want to know who looked, and a time limit so it cannot quietly become a live system. Add a noindex directive so it does not appear in search.

### Why put a banner on a demonstration?

Because clients deploy demonstrations. A visible label prevents it, and it is the cheapest protection against a demonstration later being characterised as something you delivered.

### What should a demonstration environment share with production?

Nothing. Its own database, credentials and storage, and no email credentials at all, so it cannot reach anyone real.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What is the difference between a project link and a deployment link?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "A deployment lets someone use the app; a project link exposes the code, configuration and the ability to fork it."
      }
    },
    {
      "@type": "Question",
      "name": "Can I demonstrate using a real client's data?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No — it discloses their data to a third party and breaches your agreement. Use an invented dataset you control."
      }
    },
    {
      "@type": "Question",
      "name": "How should demo links be protected?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "A password or individual accounts, a time limit, and a noindex directive so it never appears in search results."
      }
    },
    {
      "@type": "Question",
      "name": "Why label a demonstration with a banner?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Clients deploy demonstrations. A visible label prevents it and protects you from it being treated as a delivered product."
      }
    },
    {
      "@type": "Question",
      "name": "What should a demo environment share with production?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Nothing — its own database, credentials and storage, and no email credentials so it cannot reach real people."
      }
    }
  ]
}
</script>
