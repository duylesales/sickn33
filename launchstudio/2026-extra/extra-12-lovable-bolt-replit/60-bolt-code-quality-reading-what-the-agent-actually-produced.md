---
Title: "Bolt Code Quality: Reading What the Agent Actually Produced"
Keywords: bolt code quality, reading generated code, duplication, dead code, maintainability, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: Technical Solo Founder / Indie Hacker
---

# Bolt Code Quality: Reading What the Agent Actually Produced

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Bolt Code Quality: Reading What the Agent Actually Produced",
  "description": "You do not need to be a developer to assess an AI-built codebase. The specific patterns that predict trouble, how to find them without reading every line, and which are worth fixing.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-01-11",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/bolt-code-quality-reading-what-the-agent-actually-produced" }
}
</script>

Generated code is rarely incompetent. It is usually competent and repetitive, written one request at a time by something with no memory of the previous requests and no view of the whole.

That produces a specific signature: the same logic implemented four times in four components, two ways of doing the same thing living side by side, and features that were abandoned still present and still running.

None of it stops the product working. All of it makes every subsequent change slower, more expensive and more likely to break something — which is the cost that eventually becomes visible as "this codebase is hard to work with".

You do not need to read every line to assess it. Half a dozen checks tell you most of what matters.

## Duplication Is the Main Symptom

Search for a distinctive phrase — the format of a date you display, the way you calculate VAT, the shape of a database query — and count how many places it appears.

Four copies of a VAT calculation means four places to change when a rate changes, and three of them will be missed. Four copies of a database query means the scoping to the current organisation exists in four places and is absent from one. This is not an aesthetic concern; it is where correctness bugs come from.

The fix is mechanical: one function, called everywhere, with the copies removed. Do it for the things that matter — money, dates, permissions, data access — and leave cosmetic duplication alone.

## Dead Code Is Everywhere

Abandoned features are not removed by the tool that built them. It adds; it does not tidy.

Look for components nothing renders, endpoints nothing calls, database tables nothing queries, and dependencies nothing imports. In a project with six months of history, expect a meaningful proportion.

Two reasons to delete rather than ignore. Dead code is still context sent on every request, which costs money and dilutes the model's attention. And an unused endpoint or table is still reachable — an abandoned feature with no authorisation is a live vulnerability nobody is watching.

## Look for Two Ways of Doing One Thing

The most reliable predictor of a difficult codebase is inconsistency: two state management approaches, two ways of fetching data, two styling systems, two date libraries.

It happens because each session solves its problem with whatever it reached for, and nothing reconciles them. The cost is that every future change begins with working out which convention applies here, and every AI session sees two patterns and picks one at random — which is how a third appears.

Choose one of each and converge. It does not have to happen at once; the rule that works is that anything you touch gets converted, and nothing new uses the losing pattern.

## The Files That Have Grown Too Large

A component of 900 lines doing data fetching, business logic and presentation is the shape that generated code tends towards, because each request added to the file that was already open.

The practical problem is not length. It is that such a file cannot be changed safely — any modification risks the parts you were not thinking about — and it cannot be sent to a model without carrying everything with it.

Sort your files by size. The largest three or four are where your bugs live and where your costs concentrate. Splitting them by responsibility — data access, logic, presentation — is usually a contained afternoon with a disproportionate effect.

## Check What Happens When Things Go Wrong

Generated code handles the successful path thoroughly and the failure paths rarely.

Look for what happens when a request fails, when a list is empty, when a field is missing, when a user has no permission. Common findings: errors caught and silently discarded, so a failure looks like an empty page; no loading state, so the interface appears broken while waiting; no empty state, so a new user sees a blank screen with no explanation; and an error message that shows the raw technical failure to the customer.

These are small fixes individually and they are most of what people mean when they say a product feels unfinished.

## What Not to Worry About

Three things founders fixate on that do not matter much.

Formatting and naming style, provided it is consistent enough to read. A formatter applied once settles it.

Whether it uses the newest approach. Working, understandable code in an older idiom is better than a rewrite to the current fashion.

Whether a developer would have written it that way. Some of it they would not, and much of that is taste. What matters is whether it is correct, consistent and changeable.

## Tests, Proportionately

The question that always follows a discussion of code quality is whether an AI-built product needs a test suite, and the honest answer is: a small one, covering specific things, written after the product has stopped changing shape.

Writing comprehensive tests against a prototype that is still being redesigned weekly is wasted work — the tests encode decisions that are about to change. But launching with none means every deployment is verified by clicking, and clicking does not scale past about a dozen screens.

The proportionate set for a small product, in order of value.

**Authorisation tests.** The cross-account check described throughout this series, automated: a second-organisation user requesting every endpoint, failing the build on any data returned. This is the highest-value test an AI-built product can have.

**Money.** Every calculation involving prices, VAT, discounts, proration and totals. These are the bugs that cost real amounts and the ones duplication produces.

**The main flow, end to end.** One test that signs up, does the central thing your product exists for, and checks the result. It catches the deployment that broke everything.

**Any bug you have fixed twice.** A test at the moment of the second fix guarantees there is no third.

That is perhaps thirty tests for a typical product, they run in under a minute, and they cover the failures that actually happen. Asking a coding assistant to write them is a reasonable use of it, provided you read what they assert — a test that passes regardless of behaviour is worse than none, and generated suites contain them.

## The Half-Hour Review Worth Doing Monthly

None of this needs to be a project. A recurring half-hour, once a month, keeps a generated codebase from reaching the state where it needs one.

Open the repository and look at what changed since last time. Not line by line — just the list of files touched and the shape of the additions. Three questions.

**Did anything get duplicated?** A new component that reimplements something that exists is the most common addition, and catching it the same month is a ten-minute fix rather than a search-and-replace across seven files next year.

**Did anything become dead?** A feature replaced last month left its predecessor behind. Deleting it now is trivial; deleting it in a year requires establishing whether anything still uses it.

**Did a new convention appear?** A second date library, a different way of fetching data, a styling approach that does not match. This is the moment to decide whether it replaces the old one everywhere or is reverted — before a third arrives.

Thirty minutes a month, on a codebase that mostly writes itself, is the difference between a product that stays cheap to change and one that becomes the thing founders describe as needing a rewrite. And the rewrite is almost never necessary; it is simply what accumulated neglect feels like from the inside.

It works because the unit of neglect in these codebases is small and regular. Each session adds a little, and nothing removes anything; a monthly pass that removes is all the counterweight required.

It is also the review that keeps the assessment honest. A codebase looks fine when you only ever see the part you are changing; the monthly look at the whole is how the pattern becomes visible while it is still small.

## Setting This Up

For an AI-built codebase this is typically one to two days: duplication found by searching for distinctive logic and consolidated for money, dates, permissions and data access; dead components, endpoints, tables and dependencies removed, with unused endpoints checked for exposure before deletion; competing conventions identified and one of each chosen with a convergence rule; the largest files split by responsibility; failure, loading and empty states added where missing; error messages made human; a formatter and linter applied; and the conventions written into the repository so the next session follows them.

LaunchStudio does this when taking over an AI-built product, and it is what makes every subsequent piece of work cheaper. The engineers are Manifera's — eleven years, 120+ engineers, 160+ projects, from Amsterdam and Ho Chi Minh City.

[Send us your repository](https://launchstudio.eu/en/#contact) and we will tell you where the duplication is.

## Real example

### Seven Copies of the Same Calculation

Rogier Slagter built Verhuurbeheer with Bolt: rental administration for holiday home owners and small property managers, 62 users managing 380 properties.

The Dutch tourist tax rate in one municipality changed. Rogier updated it, deployed, and three days later a property manager reported that their invoices still showed the old amount.

The rate appeared in seven places: two components, an invoice generator, a quote preview, a PDF template, a summary calculation and a database default. He had found and changed four of them.

Two business days: the seven copies consolidated into one configuration with a single calculation function, which also surfaced that two of the copies had been slightly different for months — a rounding difference producing invoices that disagreed with their own line items by a cent; the same treatment applied to date formatting, which had five implementations with three different behaviours around midnight; 14 dead components, 6 unused endpoints and 3 abandoned tables removed, one of the endpoints being an unauthenticated export of all bookings left over from an early experiment; two competing data-fetching approaches reconciled to one; the four largest files, all above 600 lines, split into data access, logic and presentation; loading and empty states added to eleven screens that had shown blank pages; error messages rewritten from raw technical text to sentences; a formatter applied; and a conventions file committed describing the chosen patterns.

**Result:** the tourist tax change now takes one edit. The unauthenticated export endpoint had been reachable for eight months and was the most serious finding, discovered only because dead code was being removed. Rogier reports that subsequent AI sessions produce noticeably more consistent work since the conventions file was added, which he had not expected.

> *"I changed the tax rate in four places and thought I was done. It was in seven, and two of them had been quietly disagreeing with each other since spring."*
> — **Rogier Slagter, Founder, Verhuurbeheer (Zandvoort)**

**Cost & Timeline:** €2,700 (duplication consolidation for tax and date logic, dead code removal with exposure check, convention reconciliation, large file splitting, failure and empty state handling, error message rewriting, formatting, conventions documentation) — completed in 2 business days.

## Frequently Asked Questions

### How do I assess code quality without being a developer?

Search for distinctive logic and count the copies, look for unused components and endpoints, check whether two approaches to the same thing coexist, sort files by size, and see what happens on failure.

### Why does duplication matter so much?

Because a change made in three of four places leaves one wrong, and when the duplicated logic is money, permissions or data scoping, that is a correctness or security bug rather than untidiness.

### Is dead code actually harmful?

Yes. It is context sent to the model on every request, and an abandoned endpoint or table is still reachable — frequently without any authorisation, since it was never finished.

### Should I rewrite generated code to look hand-written?

No. Correct, consistent and changeable is the standard. Rewriting for style or for the newest idiom spends time without improving anything a customer experiences.

### What single change makes future AI sessions better?

A conventions file in the repository describing the patterns you chose. Assistants read it, and the consistency of what they produce improves immediately.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "How can a non-developer assess AI-generated code?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Count copies of distinctive logic, look for unused components and endpoints, check for competing approaches, sort files by size, and test failure paths."
      }
    },
    {
      "@type": "Question",
      "name": "Why does duplicated logic matter?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "A change applied to three of four copies leaves one wrong — and when the logic is money, permissions or data scoping, that is a real bug."
      }
    },
    {
      "@type": "Question",
      "name": "Is dead code harmful in an AI-built project?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes — it is paid context on every request, and abandoned endpoints or tables are often reachable without authorisation."
      }
    },
    {
      "@type": "Question",
      "name": "Should generated code be rewritten by hand?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No. Correct, consistent and changeable is the standard; rewriting for style or fashion improves nothing a customer sees."
      }
    },
    {
      "@type": "Question",
      "name": "What improves future AI sessions most?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "A conventions file in the repository describing your chosen patterns — assistants read it and produce noticeably more consistent work."
      }
    }
  ]
}
</script>
