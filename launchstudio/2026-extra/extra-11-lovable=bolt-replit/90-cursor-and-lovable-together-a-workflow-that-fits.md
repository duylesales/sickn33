---
Title: "Cursor and Lovable Together: A Workflow That Fits"
Keywords: Cursor, Lovable, vibe coding developer, github sync, workflow, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: Technical Solo Founder / Indie Hacker
---

# Cursor and Lovable Together: A Workflow That Fits

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Cursor and Lovable Together: A Workflow That Fits",
  "description": "Using a visual builder and a code editor on the same project works well until they disagree about what the project is. How to divide the work, keep version control as the source of truth, and avoid overwriting yourself.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-08-31",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/cursor-and-lovable-together-a-workflow-that-fits" }
}
</script>

Once a product has both an interface people use and logic people depend on, most founders end up wanting both kinds of tool. The builder is faster for screens. The editor is better for everything that is not a screen.

Running both is a good idea and it introduces one genuinely new problem: two systems that can each change your project, with different ideas about what belongs in it. Handled carelessly, that produces the worst afternoon in this entire field — work you did, overwritten by work you also did.

## Why Each Tool Wins Where It Wins

**The builder is better at surfaces.** A new screen, a form, a layout, a flow between pages. You see the result as you describe it, which is a genuinely faster feedback loop than reading code and refreshing a browser.

**The editor is better at everything structural.** Consolidating a rule implemented in three places, extracting configuration, applying a change across many files, writing tests, understanding what depends on what. The unit of work is the project rather than the page.

Trying to force one to do the other's job is where the frustration comes from. Asking a builder to refactor produces a parallel implementation; asking an editor to design a screen produces a slow version of something you could have seen immediately.

## Version Control Is the Contract Between Them

The one rule that makes this work: the repository is the truth, and both tools are ways of changing it.

Builders that sync to a repository make this straightforward — changes you make visually appear as commits, and changes you push arrive in the builder. Once that connection exists, three habits keep it healthy.

**Work in one place at a time.** Not both simultaneously on the same area. This sounds obvious and is the rule people break, because the builder is open in a tab and it is quicker to fix a label there while a refactor is half-finished locally.

**Pull before you start and push when you finish.** Every session, in both directions. Most conflicts come from a session that began against a stale copy.

**Commit in small units with a message saying why.** When the two tools do disagree, small commits are what make the disagreement solvable.

If your builder does not sync to a repository, that is the first thing to set up. Without it there is no shared definition of the project and the two tools are simply two copies drifting apart.

## Where They Actually Collide

Four places, worth knowing in advance.

**Regenerated files.** Ask the builder to change a screen and it may rewrite the whole file, discarding hand-written logic you added there. The remedy is separation: keep the logic somewhere the builder has no reason to touch — a separate module, a service file — and let the screen call it. Generated files stay generated; your code lives elsewhere.

**Formatting churn.** The two tools format code differently, producing commits full of whitespace changes that hide the real ones. Agree one formatter, configure both, and commit the configuration.

**Dependencies.** Both can install packages. Keep the lockfile committed and read what changed, or you will get version drift nobody chose.

**Configuration and environment variables.** The builder's notion of settings and your deployment's notion can diverge. Decide that the repository holds the definition and the platform holds the values, and keep it that way.

## A Division That Holds Up

**Builder:** new screens, layout, visual flow, anything where seeing it is faster than reading it, and quick copy changes.

**Editor:** business logic, anything used in more than one place, data access, integrations, tests, refactoring, and reading what the builder produced.

**Neither, without a person deciding:** the access model, payment behaviour, what happens when things fail, and what your product promises customers.

A practical refinement: once a feature graduates from "being designed" to "being relied upon", move its logic out of the generated screen and into code. The screen stays visual and disposable; the rule becomes stable and testable. That single habit prevents most of the pain described in this article.

## Rules Files Are Worth the Ten Minutes

An editor that supports project rules lets you tell the assistant what your project is: the conventions, the structure, which directories are generated and must not be hand-edited, which files must never be modified without discussion — access rules, payment logic, migrations.

Write them once. The difference in suggestion quality is immediate, and the protection against a well-meaning assistant editing something dangerous is worth more than the file takes to write.

Do the same for the builder where it supports project-level instructions: state that a particular module is hand-written and should be called rather than reimplemented.

## When Both Tools Have Touched the Same Thing

It will happen. The recovery is ordinary.

Do not panic-commit. Look at what each side changed, keep the version that has the logic you need, and re-apply the other change deliberately. Small commits make this five minutes; a week of uncommitted work in two places makes it a bad day.

Then ask why it happened. Almost always it is because a piece of logic was living inside a generated file, which is a structural problem rather than a tooling one, and moving it out prevents the recurrence.

## Working This Way With Someone Else

If a developer joins — a freelancer, a partner, a colleague — the workflow needs one addition: agree who works where and when. The builder's changes are immediate and shared; the editor's are branched and reviewed. Without an agreement, the developer's careful refactor and the founder's quick fix collide on a Friday.

The arrangement that works in practice: the founder keeps the builder for screens, on their own branch, merged like any other change; the developer works in code; and anything touching access, money or data is reviewed regardless of who wrote it.

## Screens Graduate, and You Should Notice When

The habit worth naming explicitly, because it is what keeps this workflow healthy over years rather than months.

Every screen in your product starts disposable. It was generated to try an idea, it will be regenerated three times this month, and nothing about it deserves protection. That is exactly the right posture — and it stops being right at a specific, identifiable moment.

**A screen graduates when someone depends on it.** A customer's process runs through it. It calculates something that appears on an invoice. A colleague at a client company has learned where the button is. From that point the cost of an accidental regeneration is no longer zero.

**Graduation means moving the logic out, not freezing the screen.** The layout can keep being regenerated freely; what moves is the rule underneath — the calculation, the eligibility check, the state transition — into a module with a name, called by the screen. The visual half stays fast to change, and the part that matters stops being at risk.

**Write down which is which.** A short list in your repository: these modules are hand-written, these directories are generated. It is what your rules files reference, it is what a developer joining reads first, and it is what stops you making the wrong assumption six months later about your own project.

**Test what graduated.** A rule that someone depends on deserves a test, and this is the point at which writing one is cheap because you have just moved the code and understand it completely.

The failure this prevents is gradual rather than dramatic. Products that never graduate anything accumulate business rules inside regenerable screens until a routine layout change silently alters an invoice — and the founder, reasonably, concludes that the two tools cannot be used together. They can. What cannot coexist is a regenerable surface and an irreplaceable rule occupying the same file.

## Getting the Structure That Makes This Possible

This workflow depends on a project where generated surfaces and hand-written logic are actually separated — which is not how an AI-built product starts out.

LaunchStudio does that separation as bounded work: business logic extracted from generated screens into modules the builder will not overwrite, duplicated rules consolidated into one definition, configuration made explicit, the repository connected as the single source of truth with formatting and lockfiles settled, tests added around the rules that matter, and rules files written for both tools so each stays in its lane — with the interface you built left untouched.

The engineers are Manifera's: eleven years and 160+ production projects for clients including Vodafone, TNO and CFLW, from Amsterdam Herengracht 420 and Ho Chi Minh City.

[Tell us how you are working today](https://launchstudio.eu/en/#contact), or see the [packages](https://launchstudio.eu/en/#packages).

## Real example

### A Refactor Overwritten by a Label Change

Ivo Schaminée built Servicecontract with Lovable: maintenance contract administration for installation companies, used by eleven firms around Oss and Uden. Contracts, planned service visits, invoicing intervals, renewal reminders.

He had started using Cursor for the parts the builder handled badly, and for two months the arrangement worked. Then he spent a Thursday consolidating the renewal calculation, which had been implemented in three places with three different treatments of contracts that started mid-month. The work was done locally and not yet pushed.

On Friday morning a customer asked for a wording change on the contract screen. He made it in the builder, which regenerated the file — and the file was where two of the three renewal calculations lived. The builder's version was pushed. His Thursday was gone, along with the consolidation, and because the third implementation had also been touched, renewal dates for mid-month contracts were now wrong in a fourth new way.

Nobody noticed for eleven days, by which time 34 renewal reminders had gone out with incorrect dates, two of them to customers who had already renewed.

Seven business days of work: the renewal calculation extracted into a single module the builder has no reason to touch, with the mid-month rule defined explicitly and confirmed with three installation firms; tests written around it covering the boundary cases; the 34 incorrect reminders identified and corrected with an apology sent by Ivo; the repository established as the source of truth with the builder connected, one formatter configured in both tools, and the lockfile committed; rules files written for both tools naming the logic modules as hand-written and the access and invoicing files as not to be modified without review; and a short working agreement written for himself — pull before starting, push when finishing, one tool at a time per area.

**Result:** no further collisions in the nine months since. Ivo reports that the habit which actually fixed it was not the tooling configuration but moving logic out of generated screens as soon as a feature stops changing.

> *"A two-word label change on a Friday morning deleted a full day of careful work, because the thing I had carefully fixed was living inside a screen the builder felt free to rewrite."*
> — **Ivo Schaminée, Founder, Servicecontract (Oss)**

**Cost & Timeline:** €3,300 (logic extraction into modules, tests around renewal rules, data correction, repository and tooling configuration, rules files, working agreement) — completed in 7 business days.

## Frequently Asked Questions

### Can I use a visual builder and a code editor on the same project?

Yes, provided the repository is the single source of truth and both tools sync to it. Without that connection there is no shared definition of the project and the two simply drift apart.

### Why did the builder overwrite my code?

Because logic was living inside a generated file. Ask the builder to change that screen and it may rewrite the whole file. Keep hand-written logic in separate modules the builder has no reason to touch, and have the screen call it.

### How do I avoid conflicts between the two?

Work in one place at a time per area, pull before starting and push when finishing every session, and commit in small units. Most conflicts come from a session started against a stale copy.

### What belongs in each tool?

The builder for screens, layout, visual flow and quick copy changes; the editor for business logic, anything used in more than one place, data access, integrations, tests and refactoring. Access rules, payments and failure behaviour need a person deciding, not a tool.

### Are rules files worth writing?

Yes — ten minutes. They tell the assistant your conventions, which directories are generated, and which files must never be modified without discussion, which noticeably improves suggestions and prevents dangerous edits.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Can I use a visual builder and a code editor on the same project?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes, provided the repository is the single source of truth and both tools sync to it; without that, the two copies drift apart."
      }
    },
    {
      "@type": "Question",
      "name": "Why did the builder overwrite my code?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Because logic lived inside a generated file. Keep hand-written logic in separate modules the builder will not touch, and have screens call it."
      }
    },
    {
      "@type": "Question",
      "name": "How do I avoid conflicts between the two?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "One tool at a time per area, pull before starting and push when finishing, and commit in small units."
      }
    },
    {
      "@type": "Question",
      "name": "What belongs in each tool?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Builder for screens and layout; editor for logic, shared code, data access, integrations, tests and refactoring; a person for access, payments and failure behaviour."
      }
    },
    {
      "@type": "Question",
      "name": "Are rules files worth writing?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes — they state conventions, mark generated directories and name files that must not be modified, improving suggestions and preventing dangerous edits."
      }
    }
  ]
}
</script>
