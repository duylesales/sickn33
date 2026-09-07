---
Title: "Evaluating an AI Feature Without a Data Team"
Keywords: llm evaluation small team, golden test set prompts, regression testing ai output, measuring ai quality saas, prompt change testing, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: Technical Solo Founder / Indie Hacker
---

# Evaluating an AI Feature Without a Data Team

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Evaluating an AI Feature Without a Data Team",
  "description": "Without evaluation, changing a prompt is guesswork and every change is a coin flip. How a founder can build a useful test set of thirty examples in an afternoon, what to measure, and when automated scoring is worth the complexity.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-05-31",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/evaluating-an-ai-feature-without-a-data-team" }
}
</script>

Ordinary code has tests: the function returns the expected value or it does not. AI features have no such property, which leaves most founders improving them by changing the instructions, trying two or three inputs, forming an impression, and shipping. That process cannot detect a change that improved the case you tested and broke four others, and over several iterations it produces a feature that is different rather than better.

The remedy is not an evaluation framework or a data team. It is thirty examples and a spreadsheet, and it takes an afternoon to assemble. What it buys is the ability to answer "did that change help" with evidence rather than impression, which compounds over every subsequent change.

## Build a Test Set From Real Inputs

Thirty to fifty examples is enough to be useful and small enough to remain manageable. What matters is composition, not size.

Include **ordinary cases** that represent the bulk of real use — perhaps twenty. Include **awkward cases**: the longest input you have seen, the shortest, one in another language, one with unusual formatting, one that is nearly empty. Include **the cases that failed**, every time a customer reports a bad output, which is what makes the set improve continuously. And include **cases where the correct answer is to refuse** — an input that does not contain what the feature is looking for, where the right behaviour is to say so rather than fabricate.

Draw them from real customer inputs, anonymised. Invented examples miss the shapes that actually occur, which are messier than anything you would think to write.

For each, record what a good output looks like. Not necessarily an exact expected text — for generative tasks that is not meaningful — but the properties: which facts must appear, what must not appear, what format is required, and roughly what length is acceptable.

## What to Measure

The measurement depends on the task, and matching them correctly is what keeps this cheap.

**For extraction and classification**, where there is a right answer, measure accuracy directly. Does the extracted total match, is the category correct? These can be checked automatically and comparing two prompt versions takes a script and a minute.

**For generation**, where there is no single right answer, check properties rather than text. Does the summary mention the required facts, avoid claims absent from the source, stay within a length range, and keep the requested format? Each of those is checkable, and together they catch most regressions.

**For refusal cases**, check that the feature declined rather than inventing something, which is the failure mode most likely to reach a customer as confident nonsense.

Alongside the test set, two production measurements are worth more than any offline metric. **The correction rate**: how often customers edit the output, per feature, tracked over time. And **the retry rate**: how often they run the same thing again, which usually indicates the first result was unusable.

## The Workflow That Makes Changes Safe

With a test set in place, changing anything follows the same short loop.

Run the set against the current configuration and record the results. Make the change — a prompt adjustment, a different model, a change in what context is sent. Run the set again. Compare, and look specifically at what got worse rather than at the overall impression, because prompt changes routinely improve one class of input while damaging another.

Then, when the offline comparison is favourable, roll it out behind a flag to a small share of accounts and watch the correction rate before applying it to everyone. Offline evaluation catches regressions; production measurement catches the things your thirty examples did not represent.

The discipline that makes this work is running the set every time, including for changes that seem obviously safe. The changes that break things are precisely the ones that seemed too small to test.

Establishing an evaluation set, automating the comparison, and connecting it to a staged rollout is a modest piece of engineering that turns prompt iteration from guesswork into a process. LaunchStudio, backed by Manifera's 11+ years of production engineering, sets this up alongside the AI features themselves. [Describe your project](https://launchstudio.eu/en/#contact) for a review within one business day.

## When Automated Scoring Earns Its Complexity

Reviewing thirty outputs by hand takes perhaps twenty minutes, which is entirely acceptable for a change made monthly and tedious for one made daily.

The common escalation is to have a model judge the outputs — asking a second model whether a summary is accurate and complete against its source. This works better than most people expect and has two limitations worth knowing. It agrees with human judgement most of the time but not always, and it has systematic biases, notably toward longer and more confident-sounding answers. It is a useful screen and a poor final authority.

A practical arrangement: automated checks for the properties that can be checked mechanically, model-assisted scoring for the subjective dimension, and human review of the cases where the two disagree or the score is borderline. That keeps the human effort proportionate while retaining judgement where it matters.

What is rarely worth it at this stage is an evaluation platform. The tooling is real and it is built for teams running many experiments across many features. A spreadsheet, a script, and a discipline covers a product with two or three AI features, and it has the advantage that you will actually use it.

## Real example

### The Prompt Improvement That Broke Half the Cases

Daria Ivanova ran Klachtclassificatie, a complaint-triage tool for utility companies, built in Lovable. It categorised incoming complaints into eight types, routing them to the appropriate team.

A customer complained that billing disputes were being miscategorised, so she adjusted the instructions to describe the billing category more precisely. Testing on four billing complaints showed the fix working, and it went live.

Over the following fortnight, mis-routing complaints rose sharply across other categories. The added emphasis on billing had made the model classify anything mentioning an amount as a billing issue — including service complaints, meter disputes, and connection requests where a figure was mentioned in passing. Accuracy on the largest category had fallen from around 91% to 63%, while billing accuracy improved by a few points.

Nobody detected it for two weeks, because there was no measurement: the only signal was complaint volume from the teams receiving wrongly routed work.

**Result:** a test set of 45 real complaints across all eight categories, including 12 previously misclassified, with automated accuracy scoring; a required workflow of running the set before and after any prompt change; and rollout behind a flag to 10% of volume with routing accuracy monitored. The billing problem was subsequently fixed properly with no loss elsewhere, verified against the set before deployment.

> "I tested my fix on the four cases it was meant to fix. It worked on all four and quietly ruined the category that carried most of the volume."
> — **Daria Ivanova, Founder, Klachtclassificatie**

**Cost & Timeline:** evaluation set and comparison workflow delivered in 2 business days.

## Frequently Asked Questions

### How many examples does a useful test set need?

Thirty to fifty, drawn from real anonymised inputs. Composition matters more than size: ordinary cases, awkward ones, previously failed ones, and cases where the correct behaviour is to refuse.

### How do I test outputs that have no single right answer?

Check properties rather than exact text: whether required facts appear, whether anything absent from the source is asserted, whether the format and length are within range. Each is checkable and together they catch most regressions.

### Can a model be used to score another model's output?

As a screen, yes, and it agrees with human judgement much of the time. It carries biases toward longer and more confident answers, so it works best combined with mechanical checks and human review of borderline cases.

### What should I measure in production?

The correction rate — how often customers edit the output — and the retry rate. Both are stronger signals of real quality than any offline metric, and both require only that edits and repeats are recorded.

### Do I need an evaluation platform?

Not for a product with a few AI features. A test set, a script, and the discipline of running it before and after every change covers it, with the advantage that you will actually use it.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "How many examples does a useful test set need?", "acceptedAnswer": { "@type": "Answer", "text": "Thirty to fifty real anonymised inputs. Composition matters more than size: ordinary cases, awkward ones, previously failed ones, and cases where refusal is correct." } },
    { "@type": "Question", "name": "How do I test outputs that have no single right answer?", "acceptedAnswer": { "@type": "Answer", "text": "Check properties rather than exact text: required facts present, nothing asserted that is absent from the source, format and length within range." } },
    { "@type": "Question", "name": "Can a model be used to score another model's output?", "acceptedAnswer": { "@type": "Answer", "text": "As a screen, yes. It agrees with human judgement much of the time but is biased toward longer, more confident answers, so combine it with mechanical checks and human review." } },
    { "@type": "Question", "name": "What should I measure in production?", "acceptedAnswer": { "@type": "Answer", "text": "The correction rate and the retry rate. Both are stronger signals of real quality than offline metrics and require only that edits and repeats are recorded." } },
    { "@type": "Question", "name": "Do I need an evaluation platform?", "acceptedAnswer": { "@type": "Answer", "text": "Not for a few AI features. A test set, a script, and the discipline of running it before and after every change is sufficient and more likely to be used." } }
  ]
}
</script>
