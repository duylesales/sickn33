---
Title: "Reading a Scope Document When You're Not Technical"
Keywords: reading a scope document, software statement of work, acceptance criteria, what a scope document should include, non-technical founder contracts, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: AI-Native Founder (Non-Technical)
---

# Reading a Scope Document When You're Not Technical

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Reading a Scope Document When You're Not Technical",
  "description": "A scope document decides what you actually receive, and most disputes come from what it left undefined rather than what it got wrong. This is a line-by-line method for reading one without technical knowledge, including the four zones that are almost always left blank.",
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
    "@id": "https://launchstudio.eu/en/blog/reading-a-scope-document-when-youre-not-technical"
  }
}
</script>

Everyone tells founders to have a lawyer look at the contract. Very few mention that the contract is rarely where things go wrong. The contract covers payment terms, liability caps and what happens if someone walks away — all important, all fairly standard, and all largely irrelevant to the argument you'll actually end up having.

The argument you'll actually have is about whether hosting was included. Or whether "user management" meant password resets. Or who was supposed to move your 200 existing test users across, and why nobody did. Those live in the scope document — the two-to-six-page annex that describes the work — and it's usually the document nobody reads properly, because it's full of words that look technical and therefore feel unreviewable.

They're not unreviewable. You don't need to know what any of the technology does to find the holes. You need to know where holes hide.

## What a Scope Document Is Actually For

A scope document exists to answer one question in advance: **when is this finished?** Everything else in it is supporting material. If you read a scope and can't tell what state the world will be in on the last day of the project, the document has failed regardless of how professional it looks.

That's the frame to hold while reading. Not "is this technically correct" — you can't assess that — but "does this let two people who later disagree settle the disagreement by pointing at a page." A good scope is boring, specific and slightly over-explained. A weak scope is smooth, confident and full of nouns.

## The Margin Method: Three Questions Per Line

Print it. Actually print it, or open it in something you can annotate. For every deliverable line, write three things in the margin:

- **Who does it?** (them, you, or a third party)
- **What proves it's done?** (something you could see or click)
- **What happens if it isn't?** (does the project stop, or does it silently become your problem?)

Most lines will fail on the second question. Take a line like "Implement user authentication." Who does it — them, fine. What proves it's done? You genuinely cannot answer that. Can you reset a forgotten password? Does a new user get a verification email? Can you log in on your phone? Can someone still get into an account after you've deleted it? All of those are "user authentication," and a scope line that doesn't say which ones are included is not a commitment, it's a topic.

Now compare it to a line that survives the method: *"Signup, login, logout, password reset by email, and email verification, all working on production for a new user created from scratch — demonstrated on a call before invoicing."* You can grade that. A twelve-year-old could grade that. That's the standard.

## The Four Zones That Are Almost Always Blank

Across hundreds of scope documents written for prototype-to-production work, the same four areas go undefined. Search your document for each. If it's not there, it's not included, regardless of what anyone said on a call.

**1. Hosting and whose account it lives in.** The question isn't "will it be deployed" — everybody says yes. It's: *on which platform, in an account registered to whom, paid for with whose card, and what is the monthly cost?* A prototype deployed into a vendor's own account is a prototype you can't take with you. This is the single most common source of the awkward conversation eighteen months later.

**2. Data migration.** If anything already exists — test users, real users, uploaded files, a spreadsheet of early signups — someone has to move it, and moving it is real work with real failure modes. Scope documents habitually say "migrate existing data" without saying how much data, from where, or what happens to records that don't fit the new structure. Ask for a number: *"200 existing user records and their 1,400 uploaded files will be migrated; records missing a valid email will be listed in a report rather than imported."*

**3. Environments.** Is there a separate staging copy where changes are tested, or does every change go straight to the site your customers use? This is a €200–€500 decision that determines whether your first post-launch bug fix is nerve-racking or routine. It's almost never mentioned.

**4. What happens after handover.** Not "support" as a word, but: how long, covering what, at what response time, and what specifically is excluded. "Thirty days of bug fixes, where a bug means the software doesn't do what this document says it does, response within one business day, excluding new features and third-party outages" is a real commitment. "Post-launch support included" is a mood.

## Weasel Verbs and What to Replace Them With

Certain verbs do a lot of quiet work in scope documents. When you hit one, don't argue — just ask for the replacement.

| If it says | Ask | Because |
|---|---|---|
| "Integrate payments" | "Which provider, which payment types, and what happens when a card fails?" | Integration can mean a checkout button or a full subscription lifecycle |
| "Assist with deployment" | "Who presses the button, and who fixes it if it fails?" | "Assist" means you're the one responsible |
| "Standard security practices" | "Name three things you will check and how I'll know you did" | Unfalsifiable as written |
| "As needed" / "where applicable" | "Who decides what's needed — you or me?" | This phrase transfers the decision to them |
| "Best effort" | "What's the outcome if best effort doesn't get there?" | It's an explicit disclaimer of the result |
| "Up to 5 pages" | "What's the minimum?" | Ranges anchored only at the top are ceilings, not commitments |
| "Support the frontend" | "Are you changing my UI or leaving it alone?" | Decides whether you keep what you built |

None of these are dishonest phrasings. They're normal professional shorthand, and most vendors will replace them with something specific the moment you ask. The ones who won't have told you something important.

## Turn Every Deliverable Into a Sentence Starting "I Will Be Able To"

This is the highest-leverage request you can make, and it takes a vendor about twenty minutes. Ask them to add an acceptance criteria section: each deliverable rewritten as something you personally can verify, phrased from your side.

- *I will be able to sign up with a new email address and receive a verification email within one minute.*
- *I will be able to log into my own admin account and see all bookings; a normal user account visiting the same address will be refused by the server, not just hidden in the menu.*
- *I will be able to subscribe with a test card, cancel, and see the subscription end date reflected in my account.*
- *I will be able to point my own domain at the site, and it will load over HTTPS.*
- *I will be able to hand this repository to another developer along with a written architecture note, without needing you.*

Two things happen when you ask for this. First, you get a document you can actually enforce without technical knowledge — go down the list, click each one, done or not done. Second, and often more valuable, the vendor discovers items they hadn't thought about while writing the list, and the scope gets better before the work starts. Some things that were "obviously included" turn out to be extra; better to learn that now, in writing, than in week three.

## Watch for the Sentence That Ends Too Early

A quick structural scan you can do in five minutes: read every deliverable and check that it names an *object* and a *finish state*, not just an activity.

- "Database optimisation" — activity only. Optimised to what? Measured how?
- "Improve security" — activity only.
- "Code cleanup and refactoring" — activity only, and often a large open-ended cost bucket.
- "Set up automated backups of the production database, retained 30 days, with one restore tested before handover" — object, finish state, and proof. Good.

Anything in the first category is billable time without a defined endpoint. It might be legitimate work; it just can't be part of a fixed-price agreement in that form, because neither of you can say when it's over.

## What Should Also Be In There, and Usually Isn't

Four smaller items worth adding by request. They're cheap to include and expensive to add later:

**A list of accounts and who owns them.** GitHub, hosting, database, payment provider, email sending, domain registrar. One table, name against each. Everything should say you.

**Third-party costs you'll carry after launch.** Roughly €20–€80/month is normal for a small production app once hosting, database, email and monitoring are counted. It's not the vendor's fee, but a scope that never mentions it leaves you surprised in month two.

**An explicit exclusions list.** Good vendors write these voluntarily: *"Not included: iOS/Android apps, GDPR legal review, content and copy, SEO, load testing beyond 500 concurrent users."* An exclusions list is a sign of someone who has been burned into clarity, which is exactly who you want.

**What happens to scope changes.** Not whether they'll happen — they will. Whether a change is quoted separately before work starts, or absorbed, or billed after the fact.

## Where This Leaves You

You'll never be able to audit the code inside a scope document, and you don't need to. You can check whether every line has an owner, a proof and a consequence; whether hosting, migration, environments and post-launch ownership are named rather than implied; and whether the vendor was willing to rewrite vague verbs into things you can click. Vendors who write scopes this way tend to deliver projects that finish, because writing it forces the thinking that makes finishing possible.

For reference, [LaunchStudio](https://launchstudio.eu/en/) quotes prototype-hardening work as a fixed scope with named acceptance criteria before anyone touches the code — €800–€3,500 for the Launch Ready package, one to three weeks, with every account in your name from day one — because the engineers doing it come out of [Manifera's custom software practice](https://www.manifera.com/services/custom-software-development/), where eleven years of enterprise delivery makes ambiguous scopes an expensive habit to keep. Use our scope as a template even if you hire elsewhere; a good scope document is not a competitive secret.

**Send us what you've built and what you think you need — you'll get a written scope with acceptance criteria back within one business day, and you're free to hand it to any developer you like.**

## Real example

### A Founder in Action: The Line That Said "Deployment Support"

Fenna Duijvestein, a former restaurant group operations lead in Haarlem, built MenuPilot in Lovable — a tool letting small restaurant chains push menu changes to all their locations at once — and received a nine-page scope from a small development studio. It looked thorough. It listed sixteen deliverables, a timeline, and a fixed price of €6,800.

Applying the margin method surfaced three problems in an hour. "Deployment support" put her in charge of a process she couldn't perform. The word "migration" appeared once with no quantity, though she had 340 menu items and eleven locations already loaded. And nothing anywhere named which account the hosting would live in. When she asked, the studio confirmed it would sit under their own agency account at €140/month, billed through them.

She didn't walk away — she asked for a revision. The rewritten scope moved hosting into her own accounts, quantified the migration, and added eleven acceptance-criteria sentences. The price went up by €600 and the ambiguity went to zero.

**Result:** MenuPilot launched three weeks later against a scope Fenna could grade line by line, with all accounts in her name and a documented €46/month running cost instead of €140.

> *"I couldn't tell you whether their architecture was good. I could tell you that four lines didn't say who was doing the work, and that turned out to be enough."*
> — **Fenna Duijvestein, Founder, MenuPilot (Haarlem)**

---

## Frequently Asked Questions

### Is a scope document the same thing as a contract?

No. The contract governs payment, liability and termination; the scope document defines what gets built and when it's finished. They're usually signed together, and the scope is the one that determines whether you're satisfied at the end.

### Won't asking for acceptance criteria make me look difficult?

It'll make you look like someone who has done this before, which changes how you're treated for the rest of the engagement. Vendors who write good scopes are usually relieved to be asked, because clear acceptance criteria protect them from endless "just one more thing" requests as much as they protect you.

### What if the vendor says the scope has to stay flexible because the work is unpredictable?

That can be genuinely true for exploratory work, but it means you're buying time rather than an outcome — so the pricing model should match. If they want flexibility, ask for a capped budget with weekly written updates, not a fixed price attached to a vague scope.

### How long should a scope document be for a small prototype-hardening project?

Two to five pages is typical, and longer isn't better. What matters is whether every deliverable has an owner, a definition of done, and a consequence — a tight three-page scope beats a padded twelve-page one every time.

### Should I add my own items to a scope they wrote?

Yes, and expect a price adjustment if you're adding real work. Send additions as a numbered list with a note that you'd like each either included, quoted separately, or explicitly excluded — that framing makes it easy for the vendor to answer quickly and hard for anything to stay ambiguous.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Is a scope document the same thing as a contract?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No. The contract governs payment, liability and termination, while the scope document defines what gets built and when it is finished. The scope is the one that determines whether you are satisfied at the end."
      }
    },
    {
      "@type": "Question",
      "name": "Won't asking for acceptance criteria make me look difficult?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "It makes you look like someone who has done this before. Vendors who write good scopes are usually relieved to be asked, because clear acceptance criteria protect them from endless extra requests as much as they protect you."
      }
    },
    {
      "@type": "Question",
      "name": "What if the vendor says the scope has to stay flexible because the work is unpredictable?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "That can be true for exploratory work, but it means you are buying time rather than an outcome, so the pricing model should match. Ask for a capped budget with weekly written updates rather than a fixed price on a vague scope."
      }
    },
    {
      "@type": "Question",
      "name": "How long should a scope document be for a small prototype-hardening project?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Two to five pages is typical and longer is not better. What matters is whether every deliverable has an owner, a definition of done, and a consequence."
      }
    },
    {
      "@type": "Question",
      "name": "Should I add my own items to a scope they wrote?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes, and expect a price adjustment for real additions. Send them as a numbered list asking for each to be included, quoted separately, or explicitly excluded, which makes it easy to answer and hard for anything to stay ambiguous."
      }
    }
  ]
}
</script>
