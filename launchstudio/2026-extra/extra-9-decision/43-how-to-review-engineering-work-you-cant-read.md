---
Title: "How to Review Engineering Work You Can't Read Yourself"
Keywords: reviewing developer work non-technical, acceptance checklist software, staging URL review, how to approve engineering deliverable, founder oversight, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: AI-Native Founder (Non-Technical)
---

# How to Review Engineering Work You Can't Read Yourself

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "How to Review Engineering Work You Can't Read Yourself",
  "description": "A non-technical founder cannot audit a pull request, but can absolutely verify whether the work they paid for was done. This article sets out the four artifacts to insist on, how to write acceptance criteria that can only pass or fail, and the questions that produce useful answers even when you cannot evaluate the code.",
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
    "@id": "https://launchstudio.eu/en/blog/how-to-review-engineering-work-you-cant-read"
  }
}
</script>

Your engineer sends a message on Thursday: "Auth hardening is done, RLS policies are in place on all tables, and I've moved the API keys server-side. Ready for you to review." You cannot read a single line of what they wrote. So what exactly are you reviewing — and how do you say yes or no to it without either rubber-stamping work you don't understand or wasting everyone's week pretending to understand it?

This is the most common quiet anxiety among founders who built their product with AI tools and then hired real engineers to finish it. The good news is that the anxiety is misdirected. Reading code is not the review. The review is verifying that specific, agreed-upon things are now true about your product — and that is a job you are better qualified for than your engineer is, because you are the only person who knows what the product is supposed to do.

## What You're Actually Being Asked to Judge

There are three separate questions hiding inside "please review," and conflating them is what makes the task feel impossible.

The first is *did the agreed work get done?* That is an inventory question, and you can answer it against a written list without technical knowledge. The second is *does the product still behave correctly for a real user?* That is a testing question, answerable by clicking through your own product with intent. The third is *is the code well built?* That is the only one requiring engineering judgement — and it is the one you are paying an engineering partner to hold on your behalf, verified through their own code review process, not yours.

Founders get into trouble when they try to answer question three and give up entirely, skipping one and two in the process. Answer the first two rigorously and you have covered the failure modes that actually bite non-technical founders: work that was quietly descoped, and work that was done correctly but broke something else.

## Artifact One: A Staging URL You Can Click

Insist on a staging environment — a working copy of your product at a URL like `staging.yourproduct.eu`, running the new work, connected to a test database rather than real customer data. This is non-negotiable, and any competent partner will offer it before you ask.

A staging URL changes the nature of the conversation completely. Instead of evaluating a claim ("payments now work"), you evaluate an experience: you go to the staging site, you sign up, you pay with a test card, and you see what happens. Screenshots and screen recordings are not substitutes, because they show you the path the engineer chose to show you. Your job is partly to walk paths nobody planned for.

Two things to confirm about staging before you trust what you see there. Ask whether staging uses the same configuration as production will — a payment integration that works in Stripe test mode does not prove it works in live mode, and an email that sends in staging does not prove your sending domain is verified for the real one. And ask whether staging contains real customer data. It should not; it should contain anonymised or invented data, both because it is safer and because you need to be free to break things in it without consequences.

## Artifact Two: A Written Acceptance Checklist, Agreed Before the Work Starts

The single highest-leverage document in an engineering engagement is a list of statements that will be true when the work is finished, written in your language, agreed at the start.

Written at the start is the crucial part. A checklist produced at the end is a description of what happened; a checklist agreed at the beginning is a contract about what should happen. It also removes the most uncomfortable dynamic in these engagements — the founder who feels vaguely dissatisfied but cannot articulate why, and the engineer who genuinely delivered what they thought was asked.

Ask for it in this form: a numbered list of ten to twenty-five items, each one a claim about your product's behaviour, each one something you personally can check on staging. Not "implement row-level security." Instead: "If I log in as Customer A and try to open Customer B's order by changing the number in the address bar, I see an error rather than Customer B's order." Same underlying work, but the second version is something you can perform and observe, which means it can be genuinely accepted or genuinely rejected.

## How to Word an Item So It Can Only Pass or Fail

Most weak acceptance checklists fail on wording rather than content. Three rules fix nearly all of it.

**Name the actor.** "A logged-out visitor," "a paying subscriber," "an admin." Half of all security problems in AI-generated apps are really questions about who is allowed to do what, and an item without an actor cannot test that.

**Name the observable outcome, not the mechanism.** "I receive the receipt email within two minutes at an address I control" is testable. "Email integration is configured" is not — configured how, and how would you know? The outcome version also survives implementation changes, which matters if the engineer finds a better approach mid-engagement.

**Include the failure case, not just the happy path.** For every "this works" item, add the corresponding "this correctly refuses" item. Payment succeeds with a valid card — and payment fails gracefully with a declined test card, showing a message rather than a blank screen. Password reset works for a real address — and does not reveal whether an unknown address exists in the system. The failure cases are where AI-generated prototypes are weakest, because these tools optimise for the demo path, and they are exactly where a founder's testing adds value the engineer's own testing might not.

A useful benchmark: if you handed an item to a friend who has never seen your product and they could perform it without asking you a question, it is worded correctly.

## Artifact Three: A Change Log in Plain Language

Ask for a running note — updated at least twice a week, ideally as a shared document — with one line per meaningful change, in ordinary English, plus the reason. Something like: "Moved the OpenAI key out of the browser and onto the server, because anyone opening developer tools could previously copy it and run costs against your account."

This gives you three things. It tells you what happened without requiring you to read a diff. It gives you a record you will need later, when you or a future developer asks why something is built the way it is. And it works as a quiet quality signal: an engineer who can explain a change in one plain sentence understands it, and one who cannot explain it in plain language usually cannot explain it at all.

Do not accept a raw list of commit messages as a substitute. "fix: update RLS policy on orders table" is a log entry for engineers, not for you, and the translation work is part of what you are paying for. LaunchStudio brings Manifera's enterprise-grade engineering to the founder economy, and one thing that carries over from enterprise work is the assumption that every change is explainable to the person who owns the product.

## Artifact Four: A Short Walkthrough Recording at the Midpoint

Around the halfway mark, ask for a ten-minute screen recording — not a live meeting, a recording — where the engineer walks through what has been done on staging, showing the actual behaviour rather than the code.

Recordings beat meetings here for a specific reason: you can pause them, rewatch the part you did not follow, and watch it again in three weeks when you have forgotten. In a live call you nod along and lose it by Friday. Recordings also protect your engineer's focus, since a ten-minute async recording costs them fifteen minutes while a scheduled call costs them the hour around it too.

What you are listening for is not vocabulary. It is whether the explanation connects to your product's reality. "I made sure a coach can only see their own athletes' data" is grounded. "I implemented industry-standard security best practices" is not — not because it is untrue, but because it is unfalsifiable, and unfalsifiable statements are the ones worth following up on.

## Four Questions That Work Even When You Don't Understand the Answer

You do not need to evaluate a technical answer to get value from a technical question. These four consistently surface real information.

*"What did you find that we didn't know about when we scoped this?"* Every hardening engagement uncovers something. An engineer who says "nothing" is either not looking or not telling you, given that roughly 45% of AI-generated code carries security vulnerabilities as written. The answer also gives you early warning about scope before it becomes a surprise.

*"What's the riskiest part of the product right now, and what would you do about it with another week?"* This gets you a prioritised risk view in your engineer's own words, which is useful for launch planning and doubly useful later when you decide whether to extend.

*"If I get 500 signups in one day, what breaks first?"* A good answer names something specific — a rate limit, an email sending quota, a database connection pool, a plan tier. A vague answer means nobody has thought about it, which is worth knowing before a Product Hunt feature rather than during one.

*"What did you deliberately not do, and why?"* Good engineers make constant scope decisions and rarely surface them unprompted. This question turns invisible choices into a list you can review — and occasionally you will find something you would have prioritised differently, which is exactly the kind of correction that is cheap in week two and expensive in week four.

## What Not to Review, and the Three Signals That Do Matter

Do not review code style, file structure, or library choices. Do not paste code into an AI chatbot and relay its critique — an out-of-context model will confidently flag things that are fine, and you will spend your engineer's time defending decisions instead of building. Do not treat commit frequency as a productivity metric; a day spent reading your database schema before touching anything is often the most valuable day of the engagement.

Three signals genuinely do warrant escalation. First, evasiveness about specifics: an engineer who repeatedly answers a concrete behavioural question with an abstract reassurance. Second, a checklist item that keeps slipping without a stated reason — one deferral is normal, three is a pattern. Third, a refusal to give you a staging URL, which has no legitimate explanation on a project of this size.

Reviewing work you cannot read comes down to insisting on the right four artifacts and asking questions whose answers you can evaluate on their concreteness rather than their content. It is a skill, and most founders get competent at it within one engagement. If you want to see what a written acceptance checklist looks like for a product like yours before you commit to anything, the [LaunchStudio process](https://launchstudio.eu/en/#process) is built around exactly this handover discipline, inherited from [Manifera's engineering team](https://www.manifera.com/about-us/) and their 11+ years of delivering to clients who audit everything.

Book a 15-minute intro call and bring your product — you'll leave with a draft acceptance list you could hand to any engineer, whether or not it's us.

## Real example

### A Founder in Action: The Checklist Item That Caught the Real Problem

Fleur Janssen, a former florist turned founder in Haarlem, built Bloemroute — a delivery-slot and route planner for independent flower shops — in Bolt. When she hired out the backend hardening, she asked for the acceptance checklist up front and insisted every item be something she could perform herself.

One item she wrote read: "As shop owner A, if I open the delivery list and change the shop ID in the address bar to another shop's ID, I see an error and not their deliveries." She ran it on staging in week two, and it passed. Then she tried the same thing on the *printable route sheet* page, which was not on the list because nobody had thought of it — and it returned another shop's addresses and customer phone numbers.

**Result:** The print view was using a separate query path that had never been covered by the new access rules. It was found in week two by a founder clicking around rather than in week six by a competitor's customer, fixed in under a day, and three similar "secondary view" paths were audited and corrected as a result.

> *"I found it because I know my product, not because I know code. My engineer knew how to fix it in an hour — but he'd never have thought to check the print page, because he's never printed a route sheet at 6 AM."*
> — **Fleur Janssen, Founder, Bloemroute (Haarlem)**

**Cost & Timeline:** €2,750 (Launch Ready package, multi-tenant data isolation and auth hardening) — live in 12 business days.

---

## Frequently Asked Questions

### Who should write the acceptance checklist — me or the engineering team?

Both, in that order. You write the first draft in your own words describing what should be true about your product, then the engineering team adds the items you could not have known to include, such as failure cases and configuration checks. Agreeing it before work begins is what makes it a contract rather than a report.

### What if I don't get a staging environment on my project?

Ask for one, and treat a refusal as a warning sign. Staging is standard practice on projects of this size and cost, and without it you are approving descriptions of work rather than the work itself. The only reasonable substitute is a very short engagement on a product with no live users, where production and staging are effectively the same thing.

### How much time should reviewing actually take me each week?

Around one to two hours: half an hour walking through staging against checklist items, ten minutes reading the change log, and the rest for questions. More than that and you are likely doing the engineering team's job; much less and problems like a broken secondary page will reach your customers rather than your notes.

### Is it reasonable to ask an engineer to explain a change in plain English every time?

Yes, and it is a fair professional expectation rather than a favour. A change that cannot be explained in one plain sentence is usually one that is not fully understood, and the explanation is also the documentation you will need in six months when you or another developer asks why something works the way it does.

### What do I do if a checklist item fails on staging?

Report it factually and without diagnosing: what you did, what you expected, what happened instead, and a screenshot. Resist the urge to suggest a cause — "the button is broken because the database is wrong" sends the engineer down your guess rather than their own investigation. A failed item in week two is a normal part of the process, not a crisis.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Who should write the acceptance checklist — me or the engineering team?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Both, in that order. You draft what should be true about your product in your own words, then the engineering team adds items you could not have known to include, such as failure cases. Agreeing it before work starts makes it a contract rather than a report."
      }
    },
    {
      "@type": "Question",
      "name": "What if I don't get a staging environment on my project?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ask for one and treat a refusal as a warning sign. Staging is standard on projects of this size, and without it you are approving descriptions of work rather than the work itself."
      }
    },
    {
      "@type": "Question",
      "name": "How much time should reviewing actually take me each week?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "About one to two hours: half an hour on staging against checklist items, ten minutes on the change log, and the remainder for questions. Much more suggests you are doing the engineering team's job; much less means problems reach customers instead of your notes."
      }
    },
    {
      "@type": "Question",
      "name": "Is it reasonable to ask an engineer to explain a change in plain English every time?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes, it is a fair professional expectation. A change that cannot be explained in one plain sentence is usually not fully understood, and the explanation doubles as the documentation you will need months later."
      }
    },
    {
      "@type": "Question",
      "name": "What do I do if a checklist item fails on staging?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Report it factually: what you did, what you expected, what happened instead, and a screenshot. Avoid diagnosing the cause, since a guess sends the engineer down your path rather than their own. A failure in week two is normal, not a crisis."
      }
    }
  ]
}
</script>
