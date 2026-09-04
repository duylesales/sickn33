---
Title: "Sharing Your Prototype Safely: NDAs, Repo Access, and What's Reasonable to Ask"
Keywords: NDA for developers, sharing code with a contractor, repo access levels, protecting your prototype, data processing agreement founders, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: AI-Native Founder (Non-Technical)
---

# Sharing Your Prototype Safely: NDAs, Repo Access, and What's Reasonable to Ask

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Sharing Your Prototype Safely: NDAs, Repo Access, and What's Reasonable to Ask",
  "description": "Founders worry about idea theft while handing over live API keys in a chat message, which gets the risk exactly backwards. A staged access ladder, a pre-share checklist, and what an NDA does and does not protect.",
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
  "datePublished": "2027-01-23",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://launchstudio.eu/en/blog/sharing-your-prototype-safely-ndas-and-repo-access"
  }
}
</script>

It's just past one in the morning and the cursor is hovering over "Invite collaborator." Somewhere in that repository is eight months of your life, the entire idea, and — although you don't know this yet — a Stripe key, a Supabase service key and your OpenAI token, all sitting in a committed `.env.local` file that the AI tool helpfully created for you in week two.

The thing you're anxious about is that a stranger will steal your idea. The thing that will actually cost you money is those three keys. Almost every founder in this position worries about the first risk and walks straight into the second, and the fix for both is the same: share in stages, clean before you share, and know which piece of paper protects what.

## The Real Risk Is Not the One You're Worried About

Let's be honest about idea theft, because the fear is real even if the statistics aren't kind to it. A development partner who wanted to compete with you would need your idea *and* your market knowledge, customers, positioning, time and appetite — and they'd be abandoning a business that makes money reliably for one that might. Agencies and freelancers see dozens of products a year; the constraint on them is capacity, not ideas. It happens, but it is rare, and it is not the thing to optimise your process around.

The risks that actually materialise, in rough order of frequency:

- **Credentials leaking** — keys shared over chat, committed to repositories, or left with a contractor after the engagement ended. This is the common one.
- **Real customer data going somewhere it shouldn't** — a production database copied to someone's laptop for debugging. If those records are EU personal data, that's a GDPR issue and an NDA doesn't cover it.
- **Access left switched on** — the contractor from last April is still an admin on your Vercel project and nobody has looked at the member list since.
- **Ownership ambiguity** — no written IP assignment, so the question of who owns what only surfaces when a due-diligence lawyer asks in eighteen months.

Every one of those is preventable with about ninety minutes of preparation.

## The Access Ladder: Four Rungs, In Order

Don't think about "giving access." Think about which rung a conversation has earned.

**Rung 0 — Nothing technical at all.** A ten-minute screen recording of your app working, a written description of what it does, a list of what you know is missing. This is enough for any competent partner to give you a ballpark range and decide whether they want the work. If someone demands repository access before they'll talk to you for fifteen minutes, that's backwards.

**Rung 1 — Read-only, on a cleaned copy.** This is where quoting happens, and where most founders should stop until money changes hands. Read-only means read-only: on GitHub, that's the *Read* role on a private repository, not Write, and absolutely not Admin. On a cleaned copy means you've done the checklist in the next section first.

**Rung 2 — Write access to a branch, still no production.** Once you've signed, the work happens here: they push to a branch, you (or they) merge, and nothing touches your live site or real users. Development and staging environments, test payment keys, seeded fake data.

**Rung 3 — Production.** Deployment, DNS, live payment keys, the real database. This comes last, it's granted per-person rather than shared, it goes through the platform's own team invitations — Vercel team members, Supabase organisation invites, Stripe user accounts with scoped roles — and it never travels through a chat message.

The rule that makes the ladder work: **credentials are invited, never sent.** Every serious platform has a way to add a person by email with a role attached. Using it means access is revocable in one click and auditable afterwards. Pasting a key into Slack means neither.

## The Pre-Share Checklist

Ninety minutes, once, before rung 1. Ask a technical friend to help with the first two if they're unfamiliar — but they are the two that matter most.

1. **Check the git history for secrets.** Deleting a key from a file doesn't remove it from the repository's history. GitHub's secret scanning flags many of these automatically on private repos; `gitleaks` is a free tool that scans locally. AI coding tools commit `.env` files with real values remarkably often.
2. **Rotate anything you find, and anything that's ever been pasted anywhere.** Stripe, Supabase (especially the service role key — it bypasses all your database permissions), OpenAI, SendGrid, Resend. Rotation takes minutes and invalidates every copy in existence, including ones you've forgotten about.
3. **Give them test keys, not live ones.** Stripe and Mollie both have complete test environments. There is no legitimate reason for a developer to hold your live payment keys during a build.
4. **Don't hand over production data.** If they need realistic data to work with, anonymise a subset or generate fake records. Copying a table of real customers to a contractor's machine is a data transfer with legal weight, not a convenience.
5. **Take a backup before anyone else gets access.** A database snapshot and a note of where it's stored. Ninety seconds, and it changes what a bad week looks like.
6. **Write down who has access to what, with the date.** A five-row note in your project doc. You will need this later, and nobody ever reconstructs it accurately from memory.
7. **Put a reminder in your calendar for the day after the project ends,** titled "revoke access." This is the step everyone skips.

## What an NDA Does, and What It Doesn't

An NDA is a promise not to disclose or misuse defined confidential information, enforceable by a lawsuit you probably won't bring. That's not cynicism — it's a description of what you're buying. Its real value is that it establishes that the information was confidential, sets a professional tone, and costs almost nothing.

Reasonable, and what you should expect in a normal mutual NDA:

- **Mutual**, not one-way. They see your product; you see their methods and pricing.
- **A definition of confidential information** that covers your code, data, customer lists, pricing and roadmap.
- **A term of two to five years**, which is standard. Perpetual obligations are unusual outside trade secrets.
- **Ordinary carve-outs**: information already public, information they already had, information developed independently, and disclosure required by law. Refusing these makes an NDA unsignable by any professional firm and doesn't protect you further.
- **A return-or-destroy clause** covering what happens to copies at the end.

What it is *not*: an NDA is not an IP assignment, and this confusion costs founders real money. Without a written assignment clause, work produced by a contractor may not automatically belong to you in every European jurisdiction. The clauses that actually matter live in the development agreement, not the NDA:

- **All work product and IP assigns to you**, on payment or on creation.
- **No reuse of your specific code** in the vendor's other client projects. (Note the word *specific* — no partner will agree not to reuse their general knowledge, and asking for that marks you as difficult without protecting anything.)
- **A named list of accounts** and confirmation they're registered to you.
- **A data processing agreement** if they will touch real EU personal data. This one is a legal requirement under GDPR, not a nice-to-have, and it's the document most founders don't know to ask for.

## What's Reasonable for a Vendor to Ask For

The other half of this, since fairness runs both ways:

**Reasonable:** read access before quoting (nobody can price code they haven't seen); a call with you rather than only written briefs; your test payment keys; a staging environment; production access once contracted; and a deposit.

**Reasonable but negotiable:** holding the repository in their organisation until final payment on a first engagement — acceptable if transfer is contractually automatic and you have read access throughout.

**Worth pushing back on:** admin rights on your domain registrar; live payment keys before launch; a copy of your production database "to work faster"; and anything shared over a personal email address rather than a company one.

One thing that looks like a red flag and usually isn't: **a vendor declining to sign your NDA before an initial conversation.** Firms that review a dozen prototypes a week can't run every one through legal at the enquiry stage, and many will happily sign before receiving code while declining to sign before a first call. Judge them on what they'll commit to at rung 1, not at rung 0.

The genuine red flag is a vendor who can't tell you, in writing, where your code will be stored, who on their side will have access, and what happens to their copies when the project ends. That's a two-paragraph answer for anyone who has thought about it and an uncomfortable silence for anyone who hasn't.

## After the Project: The Revocation Pass

Twenty minutes, on the day the engagement closes. This is the step that turns a clean project into a clean position.

Rotate every credential the vendor touched — payment keys, database keys, third-party API tokens — even with a perfect relationship, because the point is to be able to say honestly that nobody outside your company holds live credentials. Remove their accounts from GitHub, your hosting platform, your database provider, your monitoring and your error tracker; check each service's member list individually rather than assuming one removal cascades. Confirm in writing that local copies have been deleted per the NDA. Then check that everything still works, because occasionally something was quietly running on a key you just rotated — better to find that on a Tuesday afternoon than during a traffic spike.

Update your access note with the date. Next time — and there will be a next time — you'll start from a known position instead of a guess.

## Where to Start

The sequence that keeps founders out of trouble is unremarkable: talk first, share a cleaned read-only copy to get a quote, contract with IP assignment and a data processing agreement if real personal data is involved, grant working access without production, hand over production access at launch, then revoke everything the week after.

[LaunchStudio](https://launchstudio.eu/en/) quotes from rung 1 — a read-only copy is enough — and production credentials aren't needed until deployment, with everything invited through your own accounts rather than passed around. The confidentiality and access practices come from [Manifera](https://www.manifera.com/about-us/), which has run enterprise engagements under NDA and data processing agreements for over eleven years, including for clients where a leaked credential would have been a regulatory event rather than an inconvenience. Ask us for that policy in writing. Ask everyone else for it too.

**Before you share a single file with anyone, ask for their access and confidentiality practice in writing — send us the same request and compare the answers side by side.**

## Real example

### A Founder in Action: The Key That Was Still in the History

Nadia el Amrani, a former recruitment consultant in Rotterdam, built TalentLoop — a Lovable app matching contract researchers to short university projects — and was about to invite three developers to her repository so they could quote.

A friend suggested she run a secret scan first. It found four: a Supabase service role key, a Resend API key, and two versions of an OpenAI token, all committed in week two and all still live, though the files themselves had been deleted months earlier. The service role key was the serious one — it bypasses every database permission rule, and anyone holding it could read or delete every candidate profile in the system.

She rotated all four, generated a fresh set of test credentials, gave the three candidates read-only access, and asked each of them the same question: where will my code be stored, who sees it, and what happens to your copies at the end? Two answered in a paragraph within a day. One never answered.

**Result:** TalentLoop's backend was hardened over nine working days for €2,650, including moving candidate visibility rules into database policies — and Nadia signed a data processing agreement alongside the contract, because real applicant data was involved from day one.

> *"I was worried someone would steal the idea. Meanwhile my master database key had been sitting in a public-ish history for four months. The scan took eleven minutes."*
> — **Nadia el Amrani, Founder, TalentLoop (Rotterdam)**

---

## Frequently Asked Questions

### Should I ask for an NDA before the first call?

You can, but expect some good firms to decline at that stage and offer to sign before receiving any code instead. A first call about what you're building rarely involves anything genuinely confidential, and insisting can cost you conversations with partners who review many prototypes a week.

### Is a free NDA template good enough?

For most prototype-stage sharing, yes — a standard mutual template with a sensible term and normal carve-outs covers it. Spend your legal budget on the development agreement's IP assignment and data clauses instead, since those are the ones that determine what you own.

### Can I give a developer access without letting them see my customer data?

Usually yes. They need the code, the schema and realistic-looking data, not real records — anonymised or generated data works for almost all development, and the exceptions are usually specific bugs that can be investigated with a narrow, time-limited grant.

### What if my prototype is on Lovable or Bolt rather than in a GitHub repository?

Both let you export or connect to a GitHub repository, and doing so before sharing is worth it anyway: it gives you version history, a place to revoke access from, and independence from the tool. Sharing your builder account login instead is the thing to avoid, because it can't be scoped or partially revoked.

### Do I need a data processing agreement even for a small app with fifty users?

If those fifty users are real people in the EU and a contractor can access their data, yes — GDPR doesn't have a small-project exemption. It's usually a short standard annex to the main contract, and any partner who has worked with European clients will have one ready.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Should I ask for an NDA before the first call?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "You can, but some good firms will decline at that stage and offer to sign before receiving code instead. A first call rarely involves genuinely confidential material, and insisting can cost you conversations with partners who review many prototypes weekly."
      }
    },
    {
      "@type": "Question",
      "name": "Is a free NDA template good enough?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "For most prototype-stage sharing, yes. Spend your legal budget on the development agreement's IP assignment and data clauses instead, since those determine what you actually own."
      }
    },
    {
      "@type": "Question",
      "name": "Can I give a developer access without letting them see my customer data?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Usually yes. They need the code, the schema and realistic-looking data rather than real records, and the exceptions are specific bugs that can be handled with a narrow, time-limited grant."
      }
    },
    {
      "@type": "Question",
      "name": "What if my prototype is on Lovable or Bolt rather than in a GitHub repository?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Both can export or connect to a GitHub repository, which also gives you version history, a place to revoke access from, and independence from the tool. Sharing your builder account login instead cannot be scoped or partially revoked."
      }
    },
    {
      "@type": "Question",
      "name": "Do I need a data processing agreement even for a small app with fifty users?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "If those users are real people in the EU and a contractor can access their data, yes, because GDPR has no small-project exemption. It is usually a short standard annex that any partner with European clients will have ready."
      }
    }
  ]
}
</script>
