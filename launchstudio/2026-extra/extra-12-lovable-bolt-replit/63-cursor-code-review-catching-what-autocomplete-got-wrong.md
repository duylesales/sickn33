---
Title: "Cursor Code Review: Catching What Autocomplete Got Wrong"
Keywords: cursor code review, reviewing AI code, diffs, plausible errors, self review, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: Technical Solo Founder / Indie Hacker
---

# Cursor Code Review: Catching What Autocomplete Got Wrong

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Cursor Code Review: Catching What Autocomplete Got Wrong",
  "description": "AI-written code is wrong in a distinctive way: plausible rather than obviously broken. What to look for, how to review your own work when there is nobody else, and the five categories worth checking every time.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-01-17",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/cursor-code-review-catching-what-autocomplete-got-wrong" }
}
</script>

Reviewing code written by a person means looking for mistakes made by someone who understood the problem and got something wrong. Reviewing code written by a model is a different exercise, because it produces work that is fluent, idiomatic and confident, and wrong in ways that do not look like errors.

A human writing a function they do not understand produces something visibly uncertain. A model produces something that looks exactly like code written by someone who knew. That is the whole difficulty, and it is why reviewing AI-written code takes a different kind of attention rather than more of the same.

## The Characteristic Failures

Five categories account for most of what gets through.

**Subtly wrong logic.** An off-by-one, a boundary excluded that should be included, a condition inverted in a branch nobody exercises. The code reads correctly; it computes something slightly different from what you wanted.

**Invented interfaces.** A method that does not exist on that object, a parameter the library does not accept, a field the API does not return. Usually caught immediately by a compiler or a test, and not always — a field read from a response that is simply undefined produces a page displaying nothing rather than an error.

**Correct for the happy path only.** No handling of the empty case, the failure, the missing permission or the timeout. This is the most common category by volume.

**Ignoring the codebase.** A new way of doing something that already had a way, because the model imitated a general pattern rather than yours.

**Security omissions.** The ones this series keeps returning to: missing authorisation, absent validation, unbounded queries. Not present because nobody asked for them.

## Read the Diff, Not the Result

The most important habit is to look at what changed rather than at the finished file.

An assistant asked to add a feature frequently touches more than it needed to: a reformatted block, a renamed variable, a changed default, an import removed. Reading the resulting file makes all of it invisible, because it all looks like reasonable code. Reading the diff makes it obvious.

So: make one change at a time, look at the diff before accepting, and be suspicious of any change larger than the request warranted. A request to add a button that modifies eleven files is a request that did something else as well.

## Ask What Happens When It Is Empty

If you have time for exactly one question per change, ask this one: what happens when there is nothing?

An empty list, a missing record, a null field, a user with no organisation, a first-time account. Generated code is written against the case where data exists, and the failure when it does not ranges from a blank screen to an exception on a customer's first visit — which is the worst possible moment.

The second question, if there is time: what happens when it fails? The request errors, the service is slow, the permission is denied. Generated code catches errors and frequently does nothing useful with them.

## Review the Things That Cannot Be Undone

Not every change deserves the same attention, and the honest allocation for a founder working alone is to look hard at a small set.

Anything touching money. Anything touching permissions or authorisation. Anything that deletes or overwrites. Anything that sends something to a customer. Anything that changes the database schema.

Those five categories are where a mistake is expensive or irreversible. Everything else — a layout change, a new display field, a copy edit — can be verified by looking at the product.

This is also the allocation to give an assistant when you ask it to review: point it at the change and ask specifically about authorisation, about the failure paths, about whether this matches how the rest of the codebase does it. Open questions produce generic answers; specific questions produce useful ones.

## Use the Tool to Review the Tool, Carefully

Asking a model to review code is genuinely useful and has a specific limitation: it is good at finding what is present and wrong, and poor at noticing what is absent.

So it will tell you that a variable is unused or a condition is redundant. It will less reliably tell you that no endpoint in this file checks who is asking, because nothing about the code looks incorrect — the absence is only visible against an expectation the model was not given.

The productive pattern is to supply the expectation. "Does this endpoint verify that the requesting user belongs to the organisation that owns this record?" is a question with a checkable answer. "Review this file" is a request for an opinion.

Keep your own checklist of the five categories above, and walk it. The tool is fast at answering; the list is what makes the questions the right ones.

## Reviewing When You Cannot Read the Code

A significant share of founders using these tools cannot read the code with confidence, and the advice above assumes they can. There is a version for everyone else, and it is more effective than it sounds.

**Review the behaviour instead, systematically.** After a change, work through a written list: the thing that changed, the thing next to it, and the main flow of the product end to end. Written down, done the same way each time, this catches most functional regressions.

**Ask the assistant to explain the change in plain language**, then check whether the explanation matches what you asked for. A description that mentions files or behaviour you did not expect is the signal — you do not need to read the code to notice that the answer includes something you never requested.

**Ask specifically about the five categories.** Did this change touch anything to do with permissions? Does anything here handle money? Did this modify the database structure? These are questions with yes or no answers, and a yes means getting a second opinion before deploying.

**Use the tests as your reading.** A test suite covering authorisation, money and the main flow is a reviewer that works whether or not you can read the diff, which is the strongest argument for writing the thirty tests described elsewhere in this series.

And use branches. Work that can be discarded is work you do not have to be certain about, which lowers the cost of being wrong more than any review practice.

## Keep the Changes Small Enough to Review

Everything above becomes easier or impossible depending on one variable: how much changed at once.

A change touching two files can be read in a minute. A change touching twenty cannot be read meaningfully by anybody, and what happens in practice is that it is skimmed and accepted — which is the same as not reviewing it, with the added cost of believing you did.

Three habits keep changes reviewable.

**Ask for one thing.** Not "improve the invoice page" but "add a confirmation dialog to the delete button on the invoice row". The narrower request produces a smaller diff and, separately, a better result.

**Commit at every working point.** A commit is a checkpoint you can return to, and a sequence of small commits is a story you can read later. In a codebase where much of the writing was done by a tool, that history is the only explanation of why things are the way they are.

**Separate refactoring from behaviour change.** A commit that moves code and a commit that changes what it does are both reviewable; one commit that does both is not, because every difference could be either.

This is ordinary engineering discipline, and it matters more here than usual for a specific reason: the tool will happily produce a large change, quickly, and the cost of accepting it is deferred. The discipline is what converts speed into progress rather than into a codebase nobody has read.

## Setting This Up

For a founder working alone this is a habit rather than a project: one change at a time with the diff read before accepting, changes larger than the request treated as suspicious, the empty case and the failure case asked of every change, hard review reserved for money, permissions, deletion, outbound communication and schema, a written checklist of the five failure categories, specific rather than open questions when asking an assistant to review, and version control so anything unclear can be reverted rather than reasoned about.

LaunchStudio does this as a service for founders who want a second reader on the changes that matter. The engineers are Manifera's — eleven years, 120+ engineers, 160+ projects, from Amsterdam and Ho Chi Minh City.

[Send us a week of changes](https://launchstudio.eu/en/#contact) and we will tell you which ones we would have stopped.

## Real example

### A Condition Inverted in a Branch Nobody Ran

Dennis Vermaat built Sleutelbeheer in Cursor: key and access management for property managers and housing associations, tracking who holds which key to which building, used by 17 organisations.

He asked for a change to how expired key assignments were handled. The resulting code was clean, well-named and read correctly. He accepted it without looking at the diff carefully, because the feature worked when he tested it.

The change had also modified an unrelated condition in the same file, inverting the check that determined whether a key holder had permission to view a building's key list. In the path he tested — an administrator viewing their own organisation — the result was identical. In the path he did not test, a contractor with limited access could now see every key holder for every building the organisation managed, including private addresses.

It was found seven weeks later during a routine review, with no evidence anyone had used it.

Two business days: the condition corrected and a test written asserting the permission for both roles; a review of every change made in that period, which found two further unrequested modifications — a default retention value changed and an import removed that had silently disabled a validation; a working practice adopted of one change at a time with the diff read before accepting; a written checklist covering the five failure categories; automated tests added for authorisation across the twelve endpoints that expose key data, since the incident was a permission change that nothing checked; and version control discipline tightened so each session's work is a separate branch that can be discarded.

**Result:** no evidence of access by the affected contractor accounts, confirmed from logs. Dennis's assessment is that the practice change mattered more than the fix: in the following year, reading diffs caught four further unrequested modifications, two of which would have been consequential.

> *"I asked it to change how expiry worked. It also inverted a permission check in the same file, and the version I tested behaved identically. The diff would have taken me thirty seconds."*
> — **Dennis Vermaat, Founder, Sleutelbeheer (Dordrecht)**

**Cost & Timeline:** €2,300 (condition correction with tests, retrospective review of seven weeks of changes, authorisation test suite across twelve endpoints, review practice and checklist, branch discipline) — completed in 2 business days.

## Frequently Asked Questions

### How is reviewing AI code different from reviewing a person's?

A person who does not understand something produces visibly uncertain code. A model produces fluent, idiomatic code that is confidently wrong, so you are checking correctness rather than looking for signs of doubt.

### What is the single most useful habit?

Read the diff rather than the finished file, one change at a time. Unrequested modifications are invisible in the result and obvious in the diff.

### What should I check on every change?

What happens when there is nothing — an empty list, a missing record, a first-time user — and what happens when it fails. Generated code is written for the case where data exists and requests succeed.

### Which changes deserve real scrutiny?

Money, permissions, deletion, anything sent to a customer, and schema changes. Everything else can be verified by using the product.

### Can I ask the assistant to review its own code?

Usefully, if you ask specific questions. It finds what is present and wrong, and misses what is absent — so ask "does this check authorisation" rather than "review this".

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "How does reviewing AI code differ from reviewing human code?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Models produce fluent, confident code that is subtly wrong, with none of the visible uncertainty a person shows when out of their depth."
      }
    },
    {
      "@type": "Question",
      "name": "What is the most useful review habit?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Read the diff, one change at a time. Unrequested modifications are invisible in the finished file and obvious in the diff."
      }
    },
    {
      "@type": "Question",
      "name": "What should be checked on every AI-written change?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "The empty case and the failure case — generated code is written for data that exists and requests that succeed."
      }
    },
    {
      "@type": "Question",
      "name": "Which changes deserve close review?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Money, permissions, deletion, outbound communication and schema changes — where mistakes are expensive or irreversible."
      }
    },
    {
      "@type": "Question",
      "name": "Can an assistant review its own output?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Usefully with specific questions. It finds present errors and misses absences, so ask about authorisation explicitly rather than requesting a general review."
      }
    }
  ]
}
</script>
