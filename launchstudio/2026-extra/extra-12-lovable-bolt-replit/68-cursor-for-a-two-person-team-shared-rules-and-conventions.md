---
Title: "Cursor for a Two-Person Team: Shared Rules and Conventions"
Keywords: cursor rules, team conventions, shared context, code review, small team workflow, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: SaaS Scale-Up
---

# Cursor for a Two-Person Team: Shared Rules and Conventions

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Cursor for a Two-Person Team: Shared Rules and Conventions",
  "description": "Two people with AI editors produce two codebases inside one repository unless something reconciles them. The shared rules file, what belongs in it, and the review habits a small team actually needs.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-01-27",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/cursor-for-a-two-person-team-shared-rules-and-conventions" }
}
</script>

One person with an AI editor produces an inconsistent codebase slowly. Two people with AI editors produce one twice as fast, and in two different directions.

The reason is that each person's assistant follows the code it can see and the instructions it has been given. Two people, two sets of habits, two sets of preferences expressed in conversation — and within a month the invoicing module and the reporting module are written in noticeably different styles, use different libraries for the same job, and handle errors in incompatible ways.

The fix is a written set of rules that both assistants read, and it is the highest-leverage document a small technical team can have.

## Put the Rules Where the Tools Read Them

Every serious AI editor supports a project-level instructions file — a file in the repository describing how this codebase works, which is included in the assistant's context automatically.

That file is the mechanism. Instructions given in a conversation last for that conversation; instructions in the repository apply to everybody, every session, including the ones your colleague runs on a Tuesday while you are elsewhere.

Keep it short enough to be read. A page or two. A five-page document is one the model will partially ignore and the humans will certainly ignore.

## What Belongs In It

Six sections cover what actually matters.

**The stack and structure.** What this project is built with, and where things live. Two sentences and a short directory description.

**Conventions.** Naming for files, components, database tables and columns. The date and money handling rules. The directory a new feature belongs in.

**The chosen library for each job.** One for dates, one for forms, one for components, one for validation. This is the section that prevents the second and third library appearing.

**The patterns to follow.** How data is fetched, where authorisation is checked, how errors are handled, how server work is separated from the interface. Short examples are more effective than descriptions.

**The rules that must never be broken.** Every endpoint checks the caller's organisation. No secrets in client code. All input validated server-side. Money as integer minor units. These are the ones worth stating baldly.

**The vocabulary.** The words your product uses for its concepts, and the synonyms it does not use.

## Write It From the Code That Exists

The temptation is to write the rules you wish you followed. That produces a document contradicted by every file, which the model resolves by imitating the code rather than the instructions.

Write it from what the codebase actually does, where that is deliberate, and mark the exceptions explicitly: "invoicing uses the old pattern; new code uses the one described above". Then converge as you touch things.

Two people should write it together, in an hour, because the process of writing it is where the disagreements surface — and disagreements settled in a document are cheaper than disagreements discovered in a merge.

## Review Each Other's Changes, Briefly

With two people, formal review processes are overhead. Something is still needed, because the failure mode is specific: each person's assistant produces plausible code that the other person has never seen and cannot maintain.

The proportionate arrangement: everything goes through a pull request, and the other person looks at the diff before it merges. Not a line-by-line audit — five minutes, checking that it does what it says, that it follows the conventions, and that the five never-broken rules hold.

Reserve real scrutiny for the categories the review article in this series names: money, permissions, deletion, outbound communication, schema. Everything else gets the five-minute pass.

The secondary benefit matters as much as the first. Two people who read each other's changes both know what is in the product, which is what prevents the situation where one person is the only one who understands half of it.

## Keep the Rules Current

A rules file written once and left becomes wrong, and a wrong rules file is worse than none because it is confidently followed.

Two habits. When a decision is made — a library chosen, a pattern settled, a rule agreed after an incident — it goes into the file in the same commit. And it is read again every few months, which takes ten minutes and usually removes something obsolete.

The signal that it needs attention: the assistant producing code that does not match the file. That means either the file is out of date or the surrounding code contradicts it, and both are worth resolving rather than working around.

## Divide by Layer, Not by Feature

The arrangement that produced two codebases in the example above is the natural one and it is worth naming as a trap: splitting the work by feature, with each person owning their half end to end.

It is efficient for a month and it produces two specialists who cannot cover for each other, two styles, and a product where half the knowledge lives in one head.

Two alternatives work better at this size.

**Rotate.** Each person works across the whole product, taking whatever is next rather than whatever is theirs. Slower at first, and after two months both people know everything.

**Pair on the hard parts.** The schema, the authorisation model, the payment handling, the data model for a major feature. These are the decisions that are expensive to change and that both people need to understand; deciding them together costs an hour and prevents the divergence that matters most.

The general principle for a two-person team: optimise for both people being able to do everything, not for throughput this month. The first time one of you is ill, on holiday, or simply busy with customers, that decision is what determines whether the product keeps moving.

## Two People Multiply the Deployment Risk

A detail that catches small teams: with one person, deployments are serialised by physics. With two, both can deploy at once, and both can be halfway through a migration when the other's change lands.

Three small measures prevent the resulting confusion.

**Announce deployments**, however informally. A message in whatever channel you use, before and after. It takes five seconds and it prevents the situation where one person is debugging a problem the other person just introduced.

**One person owns a migration from start to finish.** Schema changes are the one category where parallel work reliably goes wrong, because the database is shared state that both branches assume.

**Keep main deployable.** If anything on the main branch can be deployed at any time, then the other person deploying is never a problem. This is the practical reason for the branch-per-change workflow rather than an aesthetic one.

Add one shared record of what was deployed and when — a line in a file, or whatever your platform already logs. When something breaks on a Thursday afternoon, the first question is always what changed, and with two people the answer is no longer obvious to either of them.

## What Does Not Need a Process

It is worth being explicit about what a two-person team should not adopt, because the material available on this subject is written for organisations with fifty engineers and applying it will slow you down without making anything better.

No ticket system with workflow states, unless you both genuinely want one. A shared list of what is next is sufficient.

No branching strategy beyond branch-per-change. Release branches, development branches and the rest exist to coordinate many people releasing on different schedules.

No formal code review with approvals, sign-offs and checklists. Five minutes on the diff is the review.

No estimates in points. Two people know how long things take and can say so in hours.

No architecture documents beyond the rules file. The codebase is small enough to read.

What is worth having is the short list this article describes: shared rules, small reviewed changes, deployment awareness, and both people able to work anywhere in the product. That is perhaps two hours of setup and no ongoing ceremony, and it is the whole of what a team this size needs — the rest becomes worth adding somewhere around the fifth or sixth person, and adding it earlier is a cost with no return.

## Setting This Up

For a two-person team this is typically half a day: a project rules file written together from what the codebase actually does, covering stack and structure, naming and formatting conventions, the chosen library for each job, the patterns for data access, authorisation and error handling, the rules that must never be broken, and the product's vocabulary; exceptions marked explicitly with a convergence plan; the file committed so both assistants read it; every change going through a pull request with a five-minute diff review; real scrutiny reserved for money, permissions, deletion, outbound communication and schema; and the file updated in the same commit as any decision it records.

LaunchStudio produces this document when handing a project to a client team, because it is what keeps the work consistent after we leave. The engineers are Manifera's — eleven years, 120+ engineers, from Amsterdam and Ho Chi Minh City.

[Ask us to write your project's rules file](https://launchstudio.eu/en/#contact) from the code you already have.

## Real example

### Two Halves of One Product

Steven Doornekamp and his co-founder built Zorgdeclaratie together in Cursor: declaration handling between allied health practices and insurers, used by 52 practices.

They divided the work — one took declarations and insurer integration, the other took practice administration and reporting — and worked in parallel for four months without a rules file or any review.

The result was two codebases in one repository. Declarations used one date library and one form approach; administration used different ones for both. Errors were thrown in one half and returned as values in the other. Database tables were named in the plural on one side and the singular on the other. Two separate validation libraries were in the dependency list. And neither could work confidently in the other's area, which meant that a week of illness stopped half the product.

The bug that forced the issue: a declaration period calculated with one date library in one half and a different one in the other, disagreeing about week numbers at the end of December, which sent 60 declarations with the wrong period and had them rejected by two insurers.

Three business days: a rules file written together in an afternoon, from the code, choosing one library per job — one date library, one form approach, one validation library, one error handling pattern — and stating the naming conventions, the patterns and five rules that must never be broken; the losing choices removed from the dependency list and converted in the areas both touched, with the rest marked as an exception to converge over time; the date handling unified and the week number disagreement fixed with a test written from the insurer specification; pull requests adopted with a five-minute diff review by the other person; and the vocabulary settled — declaration, practice, insurer, period — replacing three sets of synonyms.

**Result:** the 60 rejected declarations were resubmitted. The more significant change, in Steven's assessment, is that both of them can now work in either half, which he discovered when his co-founder was away for two weeks and the product kept moving.

> *"We had one repository and two products in it. Neither of us could work in the other's half, and a date library disagreement at the end of December got sixty declarations rejected."*
> — **Steven Doornekamp, Founder, Zorgdeclaratie (Arnhem)**

**Cost & Timeline:** €3,100 (rules file from existing code, library consolidation with one choice per job, date handling unification with specification-derived tests, convergence plan for exceptions, pull request and review practice, vocabulary settlement) — completed in 3 business days.

## Frequently Asked Questions

### Why do two people with AI editors diverge so quickly?

Because each assistant follows the code it sees and the instructions it is given in conversation. Without a shared written set, two sets of habits become two styles within weeks.

### Where should the rules live?

In a project instructions file in the repository, which editors read automatically. Instructions given in a conversation apply only to that conversation.

### How long should it be?

A page or two. Longer documents are partially ignored by the model and entirely ignored by the humans.

### Should I write the rules I want or the rules we follow?

The ones you follow, with deliberate exceptions marked. A document contradicted by the code is resolved by the model in favour of the code.

### What review does a two-person team need?

Every change through a pull request with a five-minute diff check, and real scrutiny only for money, permissions, deletion, outbound communication and schema changes.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Why do two developers with AI editors diverge?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Each assistant follows the code it sees and instructions given in conversation, so two sets of habits become two styles within weeks."
      }
    },
    {
      "@type": "Question",
      "name": "Where should shared coding rules live?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "In a project instructions file in the repository, which editors include automatically — conversation instructions do not persist."
      }
    },
    {
      "@type": "Question",
      "name": "How long should a rules file be?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "A page or two. Longer files are partially ignored by models and entirely ignored by people."
      }
    },
    {
      "@type": "Question",
      "name": "Should rules describe current practice or the ideal?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Current practice, with exceptions marked. A file contradicted by the code loses to the code."
      }
    },
    {
      "@type": "Question",
      "name": "What review process suits a two-person team?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Pull requests with a five-minute diff check, and close review only for money, permissions, deletion, outbound communication and schema."
      }
    }
  ]
}
</script>
