---
Title: "AI Features: Evaluating Model Output Before Customers Do"
Keywords: AI evaluation, LLM evals, model output quality, hallucination checks, structured outputs, prompt regression testing, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: Technical Solo Founder / Indie Hacker
---

# AI Features: Evaluating Model Output Before Customers Do

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "AI Features: Evaluating Model Output Before Customers Do",
  "description": "An AI feature that worked in the demo can quietly get worse with a new model, a changed prompt or different input. How to build an evaluation set, define what good means, test every change before release, validate output in production, and learn from what customers correct.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-03-25",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/ai-features-evaluating-model-output-before-customers-do" }
}
</script>

Most AI features in AI-built products were tested the same way: the founder tried a few examples, the output looked good, and the feature shipped. A summary of a meeting, a draft reply to a customer, a classification of incoming documents, a suggested plan — each worked convincingly on the examples it was shown.

What nobody tested is what happens next. The model provider releases a new version and the old one is retired. An AI assistant "improves" the prompt during a refactor. Customers start feeding in longer documents, different formats, another language. The output changes — usually not dramatically, but in ways that matter: a detail omitted, a fact invented, a tone that no longer fits. And in most products nothing notices, until a customer does.

Traditional software has tests that fail when behaviour changes. AI features need the equivalent, adapted to output that is never exactly the same twice. This article covers how to define what good output means for your feature, build an evaluation set, score it, gate changes on it, check output in production, and use what customers correct to improve it.

## Why AI Features Drift

Four things change the behaviour of an AI feature without anyone touching the feature itself.

**The model changes.** Providers release new versions, deprecate old ones and sometimes adjust a model behind the same name. A cheaper or faster model that is "as good on benchmarks" may be worse at the one thing your feature needs.

**The prompt changes.** Prompts live in code, and code is edited — increasingly by AI assistants that tidy, shorten and rephrase. A sentence removed because it looked redundant was often the instruction that prevented a specific failure.

**The input changes.** Customers use the feature in ways nobody tested: longer transcripts, scanned documents, mixed Dutch and English, unusual terminology. Output quality on real input can differ widely from quality on the examples used during development.

**The context changes.** Retrieval returns different documents as the knowledge base grows, a template changes, a field that used to be filled is now empty.

None of these produces an error. All of them can produce worse output. The only defence is to measure output quality systematically and repeatedly.

## Define What Good Means for Your Feature

"Is the output good?" cannot be tested. Specific properties can. Before building anything, write down what good output means for this feature, in terms you could check.

For a summary of an intake conversation, that might be:

- Every risk or safety concern mentioned in the conversation appears in the summary.
- No person, date or fact appears that is not in the conversation.
- The summary is under 300 words and uses the organisation's section headings.
- It is written in Dutch, in the formal register the organisation uses.

For a classifier of incoming documents: the correct category, and a confidence below which a human decides. For a draft customer reply: the correct facts from the order, no promises the company does not make, the right tone.

These criteria are the specification of the feature. They are also, almost always, more demanding than what the original demo was checked against.

## Build an Evaluation Set

An evaluation set is a collection of realistic inputs, each with the information needed to judge the output. It is the equivalent of a test suite.

**Start with fifty to a hundred and fifty examples.** Enough to cover the variety of real use; few enough to review by hand.

**Use real input, anonymised.** Synthetic examples written by the founder test what the founder imagined. Anonymised examples from real use — with names, addresses and identifying details replaced — test what customers actually do. Agree this with customers if the data is theirs, and handle it under your processing agreement.

**Cover the hard cases deliberately.** Long inputs, short inputs, poor-quality inputs, edge cases, examples where the right answer is "I cannot determine this", examples in which a previous version failed. Every bug report from a customer becomes a new example.

**Record the expected properties for each example**, not a single expected output. For a summary: the facts that must appear, the facts that must not. For a classification: the correct label. For extraction: the correct fields.

```json
{
  "id": "intake-042",
  "input": "transcripts/intake-042.txt",
  "must_include": ["concern about father's alcohol use", "school absence since October"],
  "must_not_include_names_except": ["Sanne", "mother", "father", "mentor"],
  "max_words": 300,
  "language": "nl"
}
```

Store the set in the repository, version it, and treat changes to it with the same care as changes to tests.

## Score Output in Three Ways

Different properties need different checks. Use the cheapest check that is reliable for each.

**Deterministic checks** — code that verifies a property exactly. Is the output valid JSON matching the schema? Is it under the word limit? Is it in Dutch? Does every name in the output appear in the input? Does the classification match the label? These are fast, cheap and should cover as much as possible.

**Model-graded checks** — a second model judges a property that code cannot check easily: "Does this summary mention every concern listed below?" or "Does this reply promise anything not in the policy?" Model graders are useful and imperfect. Give them a narrow, specific question rather than "is this good?", ask for a yes or no with a quoted justification, and validate the grader itself on examples where you know the answer before trusting it.

**Human review** — for a sample of outputs, especially when introducing a new model or prompt, and for properties no automated check captures well, such as whether a summary would actually be useful to the person who reads it. Keep it structured: the same rubric each time, scored, so results can be compared.

The result of an evaluation run is a set of numbers per property — "risk statements included: 97%; invented names: 0 of 120; under word limit: 100%" — not an impression.

## Gate Every Change on the Evaluation

Once the evaluation set exists, it becomes the release gate for anything that affects the AI feature.

A change to the prompt, the model, the temperature, the retrieval, the input preprocessing or the output parsing runs the evaluation and compares the results with the current version. If a critical property gets worse, the change does not ship.

```ts
// eval runner (simplified)
const results = await Promise.all(evalSet.map(async (ex) => {
  const output = await generateSummary(await load(ex.input), { model: CANDIDATE_MODEL });
  return {
    id: ex.id,
    schemaValid: SummarySchema.safeParse(output).success,
    mustInclude: await judgeIncludes(output.text, ex.must_include),   // model-graded
    inventedNames: findNames(output.text).filter(n => !ex.must_not_include_names_except.includes(n)),
    words: wordCount(output.text),
  };
}));
assert(rate(results, r => r.mustInclude.allPresent) >= 0.95, 'risk statements regressed');
assert(results.every(r => r.inventedNames.length === 0), 'hallucinated names');
```

Run it in CI when prompts or AI code change, and manually before switching models. Pin model versions explicitly in configuration rather than using aliases that the provider may move, so a model change is a deliberate commit that goes through the gate.

This is what turns a provider's announcement that a model will be retired from an emergency into a task: run the evaluation on the candidate replacements, compare, choose.

## Comparing Models and Prompts Fairly

Most evaluation work happens at a decision point: a cheaper model, a new provider, a rewritten prompt. Comparing them well avoids two opposite mistakes — switching to something worse because it looked fine on five examples, and refusing to switch to something better because nobody measured.

**Run every candidate on the same evaluation set, with the same settings.** Fix the temperature, the context and the post-processing, so the only variable is the one being compared.

**Run more than once.** Model output varies between runs. Two or three runs per candidate show whether a two-point difference is real or noise. For small evaluation sets, treat small differences as ties and decide on cost, latency or other properties.

**Compare per property, not on one score.** A candidate that is better on average but worse on the one critical property — omitted risks, wrong amounts, invented facts — is worse. Decide in advance which properties are critical and treat any regression on them as disqualifying.

**Compare cost per acceptable output.** A cheaper model that fails validation more often, and therefore retries or falls back to a human, may cost more per useful result than the expensive one. Divide the total cost by the number of outputs that pass all critical checks.

**Confirm in production gradually.** After a candidate passes the evaluation, release it behind a feature flag to a small share of customers, as the feature flags article in this series describes, and compare edit rates and validation failures between the two groups before switching everyone. The evaluation set tells you what you expected; production tells you what you did not.

Record each comparison — candidates, results, decision and reason — in the decisions log. The next time a provider announces a new model, the previous comparison is the starting point rather than a forgotten conversation.

## Constrain the Output

Many quality problems are prevented more cheaply by constraining what the model can produce than by checking it afterwards.

**Use structured output.** Ask the model to return JSON matching a schema — most providers support this directly — and validate it with a schema library before using it. A summary with required fields such as `concerns`, `agreements` and `follow_up` cannot silently omit the concerns section; it can only leave it empty, which is checkable.

**Require evidence.** For extraction and summarisation, ask for a short quote from the input supporting each important statement. Statements without evidence can be flagged or dropped, and invented facts become much rarer.

**Allow "unknown".** A model forced to fill every field invents values. Make uncertainty an explicit, valid answer.

**Keep the task narrow.** One prompt that summarises, classifies, extracts and drafts at once is harder to evaluate and fails in more ways than four small prompts, each with its own evaluation.

## Check Output in Production

The evaluation set protects against regressions you anticipated. Production checks catch the rest.

**Validate every output** with the deterministic checks before it is shown or stored: schema, length, language, names that do not appear in the input. When a check fails, retry once, then fall back — show a clear message, offer the manual path — rather than presenting broken output.

**Sample for review.** A small percentage of outputs, chosen at random and anonymised, reviewed weekly against the rubric. It catches drift in real input that the evaluation set does not yet contain, and every interesting failure is added to the set.

**Measure what users do with the output.** Thumbs up and down are useful but rare. More informative is what happens next: was the suggestion accepted unchanged, edited heavily, or discarded? The proportion of outputs edited, and how much, is a continuous quality signal that costs nothing to collect. A sudden increase after a release is a regression.

**Watch cost and latency as quality properties.** A change that makes output slightly better and three times slower or more expensive may be the wrong change. Track tokens and response time per request alongside quality, as the AI cost articles in this series describe.

## Human Review Where Stakes Are High

For some features, the right answer is not better evaluation but a human in the loop. Output that affects someone's care, money, legal position or employment should be a draft that a person reviews and confirms, not an action the system takes.

Design the review to be real rather than a click-through: show the evidence alongside each statement, highlight what the model was unsure about, and make editing easy. Record who confirmed the output. The EU AI Act article in this series describes when this becomes an obligation; for many B2B features it is simply what customers expect.

## Logging Without Creating a Privacy Problem

Evaluating and debugging AI features requires seeing inputs and outputs. Inputs often contain exactly the personal data customers trust you to protect.

Log deliberately. Store prompts and outputs only as long as needed — thirty days is common — with access restricted and every access logged. Redact identifiers where you can before logging. Exclude the most sensitive features from logging altogether and rely on the evaluation set and sampled review instead. Record the model, prompt version and settings for every request, so a complaint can be traced to the configuration that produced it. Add the logging to your records of processing and retention register, as the GDPR articles in this series describe — and check that your model provider's data handling matches what you told your customers.

## Dutch-Language Quality

Most models are strongest in English. A feature that works well in English can be noticeably weaker in Dutch: unnatural phrasing, anglicisms, mixed formal and informal address, incorrect domain terms.

Evaluate in the language your customers use. Include properties for language quality in the rubric — correct register, the organisation's terminology, no English fragments — and have a native speaker review a sample when evaluating a new model. Consider instructing the model in Dutch rather than English when output must be Dutch; test both, because the result differs per model.

## Setting This Up

For a product with one or more AI features, this is typically four to six days: the definition of good output written per feature as checkable properties, an evaluation set of fifty to one hundred and fifty anonymised real examples with hard cases and expected properties, deterministic checks for everything code can verify, narrow and validated model-graded checks for the rest, a structured human review rubric, an evaluation runner that gates prompt, model and pipeline changes in CI, pinned model versions, structured output with schemas, evidence and explicit uncertainty, production validation with retry and fallback, sampled weekly review, acceptance and edit tracking, cost and latency tracked with quality, human confirmation for high-stakes output, privacy-conscious logging with retention and redaction, and Dutch-language quality in the rubric.

LaunchStudio sets this up for AI features that customers have started to rely on. Behind it is Manifera — eleven years, 120+ engineers, 160+ projects, from Amsterdam and Ho Chi Minh City.

[Ask us how you would know if your AI feature got worse](https://launchstudio.eu/en/#contact).

## Real example

### A Cheaper Model and the Concerns It Left Out

Linda Smits built Intakeverslag in Lovable: AI summaries of intake conversations for social care teams, used by neighbourhood teams in 19 municipalities. A social worker records or uploads the conversation, the product drafts a structured summary, and the worker edits and confirms it.

To reduce costs, the model was switched to a newer, cheaper version with a one-line configuration change. In the same release, an AI assistant tidying the code shortened the prompt, removing a paragraph that instructed the model to always include every statement about risk or safety.

Three weeks later, a team lead noticed that a summary omitted a child's statement about violence at home that was clearly present in the recording. A review of recent summaries found the same pattern in others, and two summaries that mentioned a sibling who did not exist. The social workers had been editing summaries, but under time pressure, and trusting the draft.

Five business days: an evaluation set of 120 anonymised intake conversations, built with two team leads, each annotated with the risk statements that must appear and the people who exist; deterministic checks for schema, length, language and names not present in the transcript; a model-graded check for each required risk statement, validated against the annotations before use; a CI gate that runs the evaluation on any change to prompts, models or the summarisation pipeline, with model versions pinned; structured output with a required `risk_indicators` field, each item with a supporting quote from the transcript; the omitted prompt paragraph restored and documented with the reason it exists; production validation that blocks summaries containing names not in the transcript; risk indicators highlighted for the social worker to confirm explicitly; edit tracking per summary; and logging limited to 30 days with redaction, documented for the municipalities' privacy officers.

**Result:** on the evaluation set, the cheaper model with the shortened prompt omitted at least one risk statement in 14% of conversations; the restored prompt with structured output brought this below 2% on the original model, and the gate later rejected two candidate models that regressed. Invented names went to zero in production. The municipalities' privacy officers accepted the documentation, and the share of summaries heavily edited by social workers fell by about a third.

> *"We changed one line to save money and a tidy-up removed one paragraph. Nothing errored. The summaries just started leaving out the things that mattered most."*
> — **Linda Smits, Founder, Intakeverslag (Utrecht)**

**Cost & Timeline:** €5,200 (annotated evaluation set of 120 conversations, deterministic and model-graded checks, CI evaluation gate with pinned models, structured output with evidence, production validation, explicit risk confirmation, edit tracking, privacy-conscious logging and documentation) — completed in 5 business days.

## Frequently Asked Questions

### Why does an AI feature get worse without anyone changing it?

Because the model, the prompt, the input or the context changes. New model versions, edited prompts, different customer data and growing knowledge bases all change output without producing errors.

### What is an evaluation set?

A collection of realistic, anonymised inputs, each with the properties a good output must have. It works like a test suite for AI output and is run whenever the feature changes.

### Can I use a model to grade another model's output?

Yes, for narrow and specific questions, with a justification, after validating the grader on examples with known answers. Use deterministic code checks wherever a property can be verified exactly.

### How do I know the feature is still good in production?

Validate every output automatically, review a random sample weekly, and track how often users accept, edit or discard the output. A rise in heavy edits after a release signals a regression.

### Should AI output be reviewed by a person?

For anything affecting someone's care, money, legal position or employment, yes — as a real review with evidence shown, not a click-through confirmation.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Why do AI features degrade over time?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Model versions, prompts, customer input and retrieved context change, altering output without producing errors."
      }
    },
    {
      "@type": "Question",
      "name": "What is an AI evaluation set?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Anonymised realistic inputs annotated with the properties good output must have, run like a test suite on every change."
      }
    },
    {
      "@type": "Question",
      "name": "Is LLM-as-judge reliable for evaluation?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "For narrow, specific questions with justification and after validating the grader; prefer deterministic checks where possible."
      }
    },
    {
      "@type": "Question",
      "name": "How can AI output quality be monitored in production?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Validate every output, review a weekly random sample, and track how often users accept, edit or discard results."
      }
    },
    {
      "@type": "Question",
      "name": "When should a human review AI output?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Whenever output affects care, money, legal position or employment — with evidence shown and real editing, not a click-through."
      }
    }
  ]
}
</script>
