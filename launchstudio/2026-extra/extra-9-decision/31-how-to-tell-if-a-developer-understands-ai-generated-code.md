---
Title: "How to Tell If a Developer Actually Understands AI-Generated Code"
Keywords: vetting a developer, AI-generated code review, hiring a developer non-technical founder, Lovable code audit, questions to ask a developer, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: AI-Native Founder (Non-Technical)
---

# How to Tell If a Developer Actually Understands AI-Generated Code

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "How to Tell If a Developer Actually Understands AI-Generated Code",
  "description": "A non-technical founder cannot judge code, but they can judge how a developer talks about code they did not write. This article gives the exact questions to ask on a call, what a genuinely competent answer sounds like, and which responses should end the conversation.",
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
  "datePublished": "2027-01-04",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://launchstudio.eu/en/blog/how-to-tell-if-a-developer-understands-ai-generated-code"
  }
}
</script>

"So you built this in Lovable?"

"Yes — the whole thing. It works, I've got twelve people using it."

"Right. Honestly, the fastest thing would be to start clean. I'd rebuild it properly in Next.js, maybe three months, and then you've got something maintainable."

That exchange happens on a lot of first calls, and to a non-technical founder it sounds like expertise. It usually isn't. It's the sound of somebody who hasn't opened the repository and doesn't want to — because reading somebody else's code is harder than writing your own, and reading code an AI wrote is harder still. You can't verify their technical claims. But you can absolutely verify whether they've read your code, and that turns out to be nearly the same test.

## Stop Testing for the Wrong Thing

The instinct is to test for credentials: years of experience, frameworks, GitHub stars, whether they've "worked with Supabase before." All of that is easy to satisfy and tells you almost nothing about the job in front of you. Your job isn't greenfield development. Your job is comprehension — someone has to open a codebase that a machine generated from your prompts, understand what it currently does, work out which parts are load-bearing and which are decorative, and change only what needs changing.

Those are different skills. Plenty of genuinely good developers are weak at the second one. They've spent their careers writing code from scratch inside conventions they chose, and they get visibly uncomfortable in a codebase with no consistent conventions at all — which is what an AI tool produces when you've prompted it forty times over three weeks. Their discomfort comes out as "this needs a rewrite." Sometimes that's true. Most of the time it's a preference dressed as a diagnosis, and it costs you your entire frontend plus three months.

So test for comprehension directly. Here's how.

## The Trace Test: Make Them Follow One Path Out Loud

Give the candidate read access to your repository — a private GitHub repo, read-only, is enough — a day before the call. Then on the call, ask exactly this:

**"Walk me through what happens when a new user signs up. Start at the button and end at the row in the database. Tell me every place the data stops on the way."**

You don't need to understand the answer. You need to notice its *shape*. A developer who has actually read the code answers in specifics and in order: the component that holds the form, the function it calls, whether that call goes to your own server or straight to Supabase or Firebase from the browser, what gets written where, and what happens if it fails halfway. They will name files. They will say things like "there's a `signup` handler in `app/api/auth/`, but the profile row is actually created client-side afterwards, which means if the second call fails you get an account with no profile."

That last sentence is the tell. Specific, slightly awkward, describes a real flaw that a real codebase has, and could only be produced by someone who traced it.

An evasive answer stays at the altitude of category names: "It's a standard auth flow, Supabase handles that, it's all pretty typical." That's a description of software in general, not of your software. If you hear two of these in a row, ask directly: "Which file did you look at to answer that?" A candidate who has read the code answers instantly. A candidate who hasn't will suddenly need to "check on my other screen."

## Ask What They'd Keep, Not What They'd Change

Anyone can list what's wrong. Ask the reverse:

**"Which parts of what I've built would you keep exactly as they are?"**

A developer comfortable with AI-generated code will happily keep most of it. Typical honest answer: "Your frontend is fine — the components are a bit repetitive but they work and your users like the interface, so I wouldn't touch it. The database tables are reasonably shaped. What I'd replace is the part where the browser talks straight to the database, and I'd move your Stripe handling to the server, because right now anyone can call it with any amount."

That answer is doing something specific: it separates *cosmetic mess* from *structural risk*. AI-generated code is usually full of the first and dangerous because of the second. The cosmetic mess — repeated code, odd naming, three slightly different button components — is ugly and cheap to live with. The structural risk — no server-side permission checks, secrets shipped to the browser, payment amounts trusted from the client — is invisible and expensive to ignore.

Someone who can't tell those apart will either want to rebuild everything (they're treating mess as risk) or wave it all through (they're treating risk as mess). Both are expensive in different directions.

## Plant a Question You Already Know the Answer To

This is the single highest-signal move available to a non-technical founder, and it costs nothing.

Before the call, find one thing you already know is broken or missing. You almost certainly have one. Common candidates: there's no password reset; the admin page is only hidden by a menu item, not actually protected; deleting an account doesn't delete the data; the invite email never arrives; the file upload accepts anything of any size. Pick one you can describe in a sentence.

Now don't mention it. Instead ask:

**"If I gave you an hour with this today, what would you look at first, and what would you expect to find?"**

Then see whether they surface your known issue unprompted, or something equally real that you hadn't spotted. Candidates who've read the code find things. Candidates who haven't produce a generic list — "I'd check security, performance, and scalability" — which is the technical equivalent of a horoscope.

If they miss it entirely, give it to them and watch what happens next: "Actually, my admin page is only hidden in the menu. Anyone who guesses the URL gets in. How bad is that, and what does fixing it involve?" A strong answer explains the mechanism in plain terms (the browser decides what to show, the server decides what to allow, and right now only the browser is deciding), gives a rough scale (an afternoon, not a rebuild), and says what else is likely wrong for the same reason. A weak answer is either panic or a shrug.

## Listen to the Questions They Ask You

Reverse the direction. Over a 30-minute call, a developer who understands this kind of work will ask you about the world your app lives in, not just the deadline. Good questions sound like:

- "Who's allowed to see whose data? Can a coach see another coach's clients?"
- "Where does money actually change hands — is Stripe deciding the price, or is your app sending it?"
- "If a user emails you tomorrow asking you to delete their account, what do you currently do?"
- "How many people use this right now, and what's the number where you'd be uncomfortable?"
- "Is anything already live and taking real data, or is this still just you and your testers?"

Every one of those questions is really a scoping question about risk. A candidate who asks them is pricing your actual situation. A candidate whose only questions are "what's your budget" and "when do you need it by" is pricing your patience.

## Five Phrases That Mean They've Done This Before

You don't need to understand the technology to notice specific vocabulary that only appears in people who've cleaned up AI-generated apps repeatedly. Listen for:

**"Row-level security"** — the database's own permission rules. AI tools frequently leave these off, which means the database will hand data to anyone who asks nicely. Someone who checks this early has done this before.

**"Server-side validation"** — checking rules on your server rather than only in the browser. Prototypes almost always validate only in the browser, which is a suggestion, not a rule.

**"The service key is in the client bundle"** — a master password to your database that's been accidentally shipped to every visitor's browser. It's one of the most common single findings in AI-built apps and it is not subtle to fix.

**"Webhook signature verification"** — proving that the message claiming "this customer paid" genuinely came from Stripe or Mollie and not from someone with a text editor.

**"Idempotency"** — making sure that if the same request arrives twice, the customer is only charged once. Nobody mentions this unless they've been burned.

You are not evaluating whether these are the right five things. You're noticing whether the person reaches for concrete mechanisms or for adjectives like "robust" and "enterprise-grade."

## What a Good Answer Sounds Like When the News Is Bad

The best signal of all is how somebody delivers bad news. You want to hear proportion. "There are three real problems and about ten cosmetic ones. Two of the three matter before you take money from strangers; the third can wait until you've got a few hundred users. Here's roughly what each costs to fix."

What you don't want is either extreme. Catastrophising ("this is completely insecure, you can't launch this") is often a negotiating position that ends in a rebuild quote. Blanket reassurance ("looks fine, we'll clean it up as we go") means they haven't looked, because 45% of AI-generated code ships with security vulnerabilities and nobody who has actually read a Lovable export says it looks fine.

The honest middle sounds unglamorous and slightly boring. That's what competence sounds like.

## Applying the Same Test to Us

It would be dishonest to publish this list and exempt ourselves from it, so: run all of it on [LaunchStudio](https://launchstudio.eu/en/) too. Send the repo before the intro call, ask us to trace your signup path, ask what we'd keep, plant your known bug. We keep the frontend you built because rewriting a working interface is usually the most expensive way to solve a backend problem — not because keeping it is always right, and if your prototype genuinely needs replacing we'll say so and it will cost you nothing to hear it. The engineering underneath comes from [Manifera](https://www.manifera.com/about-us/), which has been shipping production software for enterprise clients for over eleven years; the last-mile work — security, auth, payments, hosting — typically lands between €800 and €3,500 fixed, in one to three weeks.

If a different partner answers the trace test better than we do, hire them. The point of the test is that you can now tell.

**Send us your prototype link and we'll walk your signup path back to you in writing — free, no call required, and yours to use as a benchmark against every other quote you're holding.**

## Real example

### A Founder in Action: The Candidate Who Named the File

Sanne Bakkers, a former physiotherapy clinic manager in Utrecht, built RehabTrack — a Bolt-generated app where clinics assign home exercise programmes to patients — and interviewed three developers over two weeks. Two of them opened the call by recommending a full rebuild. Neither had opened the repository she'd sent four days earlier.

The third traced her patient-invite flow out loud, named the route file it lived in, and pointed out that the invite link contained the patient's internal ID in plain text, so changing one digit in the URL loaded a different patient's exercise plan. Sanne had not known this. It was also, as it happened, exactly the kind of thing she'd been afraid of and unable to check.

She used that finding as the benchmark question for every subsequent conversation, including the one with the team she eventually hired: *"There's a broken access check on the invite route — what would you do about it?"*

**Result:** RehabTrack's invite links were moved to signed, expiring tokens and its clinic-level data separation was rebuilt server-side in nine working days, for €2,400 fixed — with the original Bolt frontend untouched.

> *"I stopped trying to work out who was the better developer. I just started asking all of them the same question about my own broken link, and the difference between the answers was immediately obvious."*
> — **Sanne Bakkers, Founder, RehabTrack (Utrecht)**

---

## Frequently Asked Questions

### Do I need to give a stranger access to my code before I've hired them?

Read-only access to a private repository is standard and low-risk, and you can revoke it the moment the call ends. If a candidate refuses to look before quoting, that's information too — nobody can price work they haven't seen, so a quote given without reading the code is a guess you'll pay for later.

### What if a developer genuinely does recommend rebuilding — is that always a bad sign?

No. Sometimes a prototype really is unsalvageable, usually when the data model can't represent what the business actually does. The difference is that an honest rebuild recommendation comes with specifics: which part, why it can't be adapted, and what it would cost to patch instead. A rebuild recommendation given before opening the repo is a preference, not a diagnosis.

### I don't understand any of the technical vocabulary. Can I really run these tests?

Yes, because you're grading the shape of the answer rather than its content. Specific beats general, files-and-functions beats categories, and proportion beats drama. You'll notice the difference within two calls, even if you never learn what row-level security is.

### How long should this evaluation call take?

Thirty minutes is enough for the trace test, the keep-versus-change question, and your planted issue. If a candidate needs an hour to say anything specific about your code, the problem usually isn't time.

### Should I ask candidates to do a paid trial task instead of just talking?

A small paid task is a good tiebreaker between two strong finalists, but it's an expensive filter to run on everyone. Use the questions first to get from five candidates to two, then pay the last two for a few hours of real work if you're still unsure.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Do I need to give a stranger access to my code before I've hired them?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Read-only access to a private repository is standard, low-risk, and revocable the moment the call ends. A candidate who refuses to look before quoting is guessing, and you will pay for that guess later."
      }
    },
    {
      "@type": "Question",
      "name": "What if a developer genuinely does recommend rebuilding — is that always a bad sign?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No. Sometimes a prototype is unsalvageable, usually when the data model cannot represent what the business does. An honest rebuild recommendation names which part, why it cannot be adapted, and what patching would cost instead."
      }
    },
    {
      "@type": "Question",
      "name": "I don't understand any of the technical vocabulary. Can I really run these tests?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes, because you are grading the shape of the answer rather than its content. Specific beats general, files and functions beat categories, and proportion beats drama."
      }
    },
    {
      "@type": "Question",
      "name": "How long should this evaluation call take?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Thirty minutes covers the trace test, the keep-versus-change question, and a planted issue. If a candidate needs an hour to say anything specific about your code, time is not the problem."
      }
    },
    {
      "@type": "Question",
      "name": "Should I ask candidates to do a paid trial task instead of just talking?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "A small paid task is a good tiebreaker between two strong finalists but an expensive filter to run on everyone. Use the questions to get from five candidates to two, then pay the last two for a few hours of real work."
      }
    }
  ]
}
</script>
