---
Title: "Cursor and Git: Commits, Branches and an Undo History"
Keywords: cursor git, version control, branches, commit messages, reverting AI changes, LaunchStudio, Manifera
Buyer Stage: Awareness
Target Persona: AI-Native Founder (Non-Technical)
---

# Cursor and Git: Commits, Branches and an Undo History

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Cursor and Git: Commits, Branches and an Undo History",
  "description": "Version control matters more when a machine writes the code, because you need to see what changed and be able to undo it. The minimum workflow for a solo founder, explained without jargon.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-01-25",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/cursor-and-git-commits-branches-and-an-undo-history" }
}
</script>

Version control is usually presented as something professional teams need for collaboration. For a founder working alone with an AI editor, it is something else entirely: the only mechanism by which you can see what a machine changed in your product and undo it if it was wrong.

That makes it more important here than in traditional development, not less. A person writing code remembers what they did. A tool that modified eleven files in response to a request about one of them has left you with no other way to find out.

## The Three Things It Gives You

**A record of what changed.** Every modification, when, and ideally why. In a codebase written largely by a tool, this is the only explanation of why the product is the way it is.

**The ability to undo.** Not one keystroke, but any change, any time, including one made three weeks ago that turns out to have broken something you only noticed today.

**A place to experiment.** A branch is a copy you can wreck freely. Given one, a session that goes badly is discarded in a second rather than unpicked over an afternoon — which, as the cost article in this series describes, is also where most of the money goes.

## The Minimum Workflow

Ignore most of what is written about branching strategies. For one person, this is enough.

**One main branch** that is always in a working state and is what gets deployed.

**A branch for each piece of work**, created before starting, named for what it is. When it works, merge it into main and delete it. If it goes wrong, delete it and start again — this is the moment the whole practice justifies itself.

**Commit whenever something works**, not when a feature is finished. Small commits, frequently, each a point you can return to. A day with twelve commits is a day with twelve checkpoints.

**Push to a remote** — a hosted repository — at least daily. Locally committed work lives on one laptop.

That is the whole workflow. It takes a few days to become automatic and it removes an entire class of anxiety about accepting changes.

## Write Messages That Explain Why

A commit message is the one place where intention is recorded, and in an AI-built codebase it is frequently the only place.

"Update" says nothing. "Fix the VAT calculation so the discount is applied before tax rather than after, which was producing invoices one to two euros too high for discounted line items" is a sentence that answers the question a future reader will have.

The habit that makes this easy: write the message first, before the change. It clarifies what you are about to do, it keeps the change to one thing, and it means the message describes the intention rather than being reconstructed afterwards.

Two conventions worth adopting. A short first line saying what changed, and, where it is not obvious, a paragraph explaining why. And one commit per logical change, so history can be read as a sequence of decisions rather than as a pile.

## Commit Before Every Session, Without Exception

The single most useful rule when working with an AI editor: never start a session with uncommitted changes.

The reason is simple. If the working state is committed, anything the tool does can be undone completely with one command. If it is not, the tool's changes and yours are mixed together and separating them is manual work at exactly the moment you are frustrated.

Make it a reflex. Commit, then prompt. The cost is five seconds and the benefit is that every session becomes reversible.

## What Not to Commit

Three categories, and the first is serious.

**Secrets.** Environment files, keys, credentials. Once committed they remain in the history after deletion, which is why the correct response to finding one is to rotate it. An ignore file covering environment files is the first thing to add to any project.

**Generated output.** Build artefacts, dependency folders. They are large, they change constantly, and they are reproducible.

**Personal data.** Database exports, customer samples, screenshots containing real records. These end up in repositories more often than anyone would like, and a repository that later becomes public takes them with it.

Everything else — including your configuration example file, your conventions file and your migrations — belongs in there.

## When Something Breaks and You Do Not Know When

The situation that justifies the whole practice: a customer reports something that used to work, and you have no idea when it stopped.

With a history, this is answerable rather than mysterious. Find a commit from before the problem existed, check it out into a temporary state, and see whether the behaviour is correct there. Then work forwards — or, faster, use the bisect facility, which finds the exact commit that introduced a problem by testing points in the history in the way you would guess at, but systematically.

For a product with a year of small commits, this typically identifies the responsible change in a handful of checks. For a product with a year of enormous commits, it identifies a commit containing forty files, which is less useful — which is the practical argument for small commits, made concrete.

Two habits make this work when you need it. Commits that each do one thing, so the answer is specific. And a working state at every commit, so a commit you check out actually runs; commits that do not run are holes in the history that break the search.

None of this is advanced. It is the routine use of a record you already have, and it is the difference between "it broke sometime this spring" and "it broke in this change, for this reason, and here is the fix".

## The Repository Is the Asset

There is a reason to do this that has nothing to do with undo, and founders tend to encounter it suddenly.

At some point somebody will want to know what you have built. An investor conducting diligence. A developer you are hiring. An acquirer. A customer's technical reviewer. A partner considering an integration.

What you hand them is the repository, and what it contains says a great deal beyond the code. A history of small, described changes over eighteen months reads as a product someone has been running. A single commit called "initial commit" dated last Tuesday reads as a product with no history at all — which, if the work was done over eighteen months, is a story that has been lost rather than one that never existed.

The same applies to handover. A developer joining a project with a readable history can see how it evolved and why decisions were made. One joining a project with no history has only the current state and must infer everything.

And there is a practical dimension: a repository under your own account, with the history, is the thing that makes your product portable between tools, platforms and people. Without it, what you own is whatever is currently deployed, and everything else is somebody else's arrangement.

That is the strongest argument for setting it up on day one rather than month five, and it costs an hour.

It is also, for most founders, the moment the product starts feeling like a company rather than a project — which is not a technical benefit, and is reported often enough by the people who do it to be worth mentioning.

There is one more small benefit worth having: a repository makes it possible to work from a different machine, which matters the first time a laptop fails and the product turns out to exist only on it.

And it makes the eventual first hire straightforward rather than an archaeology exercise: what you hand a new person is a repository they can clone, with a history they can read.

## Setting This Up

For a founder working with an AI editor this is typically an hour to set up and a week to internalise: a repository with everything committed and pushed to a hosted remote, an ignore file covering environment files, keys, build output and any data, a branch for each piece of work with a habit of deleting rather than salvaging the ones that go wrong, a commit before every session without exception, small frequent commits with messages explaining intention, a daily push, and a check that no secret is already in the history — with rotation if one is.

LaunchStudio sets this up when taking over a project, and it is the first thing we do, because nothing else is safe without it. The engineers are Manifera's — eleven years, 120+ engineers, from Amsterdam and Ho Chi Minh City.

[Ask us to check whether your repository has a secret in its history](https://launchstudio.eu/en/#contact). Many do.

## Real example

### Three Days Rebuilt by Hand

Karin Zoetelief built Praktijkfacturatie in Cursor: invoicing for allied health practices — physiotherapy, dietetics, speech therapy — handling insurer and patient billing for 41 practices.

She worked without version control for the first five months. The project lived in a folder, backed up by a cloud sync that kept a few versions of individual files.

Asked to change how insurer declaration codes were handled, a session made changes across the project. The result did not work and the errors were not obviously related to what she had requested. She tried to undo it by prompting, which made it worse, and then by restoring individual files from her sync history, which produced a mixture of old and new code that was internally inconsistent.

She rebuilt three days of work by hand over the following week, and remained uncertain for months afterwards whether something from the incident remained.

Two business days, then a changed practice: the project put into a repository with an initial commit and pushed to a hosted remote; an ignore file added covering environment files, build output and a folder of test exports containing real patient data, which had been syncing to a cloud account for five months; two credentials found in the folder rotated; a branch-per-change workflow adopted with deletion as the response to a bad session; a rule of committing before every session; the declaration code change redone on a branch, taking an afternoon rather than a week; and a short written note of the workflow kept in the repository for her own reference.

**Result:** in the following year Karin discarded 23 sessions that went wrong, each in a few seconds, having previously lost a week to one. She describes the commit-before-session rule as the change that made using the tools comfortable rather than nerve-racking.

> *"I rebuilt three days by hand because I had no way to go back. The fix was a repository, which took an hour, and I had spent five months not doing it because it sounded like something teams needed."*
> — **Karin Zoetelief, Founder, Praktijkfacturatie (Nijmegen)**

**Cost & Timeline:** €1,300 (repository setup with remote, ignore rules, credential rotation after finding secrets and patient data in the project folder, branch workflow, session discipline, workflow documentation) — completed in 2 business days.

## Frequently Asked Questions

### Do I need version control working alone?

More than a team does, when a tool writes the code. It is the only way to see what changed and the only reliable way to undo it.

### What is the minimum workflow?

A main branch that always works, a branch per piece of work, a commit whenever something works, a commit before every session, and a daily push to a hosted remote.

### Why commit before starting an AI session?

So that everything the tool does can be undone in one command. Uncommitted changes mix your work with the tool's, and separating them afterwards is manual.

### What should not go into a repository?

Secrets, build output and any real data. A committed secret stays in the history after deletion, so finding one means rotating it rather than removing the file.

### What makes a good commit message?

One line saying what changed and, where it is not obvious, why. Write it before making the change — it clarifies the work and keeps the commit to one thing.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Is version control necessary when working alone?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "More so than in a team when a tool writes the code — it is the only way to see what changed and to undo it reliably."
      }
    },
    {
      "@type": "Question",
      "name": "What is the minimum git workflow for a solo founder?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "A working main branch, a branch per task, frequent commits, a commit before every AI session, and a daily push to a hosted remote."
      }
    },
    {
      "@type": "Question",
      "name": "Why commit before starting an AI session?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "So the session's changes can be discarded entirely. Uncommitted work mixes with the tool's edits and must be separated by hand."
      }
    },
    {
      "@type": "Question",
      "name": "What should never be committed?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Secrets, build artefacts and real data. A committed secret persists in history after deletion and must be rotated."
      }
    },
    {
      "@type": "Question",
      "name": "What makes a useful commit message?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "A short line on what changed plus why when not obvious — written before the change, which also keeps the commit focused."
      }
    }
  ]
}
</script>
