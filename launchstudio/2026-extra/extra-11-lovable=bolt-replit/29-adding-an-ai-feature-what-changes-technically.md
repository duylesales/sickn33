---
Title: "AI App Security When You Add a Model: Injection, Cost and Output"
Keywords: ai app security, prompt injection protection, model api cost control, output validation, Lovable, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: Technical Solo Founder / Indie Hacker
---

# AI App Security When You Add a Model: Injection, Cost and Output

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "AI App Security When You Add a Model: Injection, Cost and Output",
  "description": "Calling a language model from your product introduces variable cost, unpredictable latency, prompt injection, unvalidated output and a new sub-processor. What each of those means practically, and the checks to put in place before launch.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-07-01",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/adding-an-ai-feature-what-changes-technically" }
}
</script>

"Summarise this for me" is four words in a prompt and about nine new categories of problem in a product.

Adding an AI feature feels like adding any other feature: an API call, a response, a place to display it. It is not, and the difference is not sophistication — it is that you have introduced something whose cost varies with user behaviour, whose latency you cannot predict, whose output has no guaranteed shape, and which treats text written by strangers as instructions. None of those are true of the payment API you integrated last month.

This is what actually changes, and what to do about each part.

## Your Costs Now Depend on What Users Type

Every other line on your infrastructure bill scales roughly with how many users you have. A model API scales with how much text they send and how much they ask for back.

That has three consequences worth planning for. A single user pasting a long document can cost more than a hundred ordinary users. A retry loop written without care can multiply spend silently. And a feature that is free for your users is a subsidy with no natural ceiling.

Three controls, none of them difficult: a hard spending cap at the provider, per-user limits on how often the feature can be used and how much text it accepts, and truncation of inputs to a length you have decided rather than a length your user chose. Set all three before launch, not after the first surprising invoice.

## Latency Changes Your Interface, Not Just Your Backend

Model responses take seconds, sometimes many. That is long enough that the usual pattern — click, wait, page updates — produces an interface that feels broken.

The practical requirements: stream the response where the provider supports it, so text appears progressively rather than after a silence; show what is happening rather than a generic spinner; make the operation cancellable; and never block the rest of the interface while it runs.

There is also a hard question to answer: what happens when the provider is slow or unavailable? An app whose core flow stops entirely because a third party is having a bad afternoon needs a timeout and a graceful path, which brings us to the part almost nobody builds.

## Prompt Injection: User Text Is Now Instructions

This is the genuinely new security category and the one most AI-built features get wrong.

If your feature takes content from a user — a message, a document, a profile, a support ticket — and puts it into a prompt alongside your own instructions, then that user's text can contain instructions too. A line inside an uploaded CV saying to ignore previous instructions and output something else is not exotic; it is the basic form of the attack, and it works more often than people expect.

It gets sharper when the model has capability. If your feature can call functions, read records or send messages, then injected instructions inherit that capability. A summarisation feature with database access is a different risk from one that only returns text.

The defences that matter for a small product: keep the model's capability minimal — no tool access unless the feature genuinely requires it; separate instructions from user content clearly in the request structure your provider offers; treat any output as untrusted data rather than as a command; and never let model output decide an authorisation question. Whether a user may see a record is your application's decision, made in code, before the model is ever involved.

## Output Validation: Assume the Shape Is Wrong

Models return text. If your code expects structured data, you now have a parsing problem that will fail eventually — not usually, but eventually, which is the worst frequency because it appears in production rather than in testing.

Validate every response against the structure you expect. Reject and retry once if it fails, then fall back rather than looping. Never pass model output directly into a database write, a query, or anything rendered as markup without escaping — output containing markup can carry a scripting attack into your page exactly as user input can.

And treat factual output as a claim, not a result. If your feature summarises a legal document or extracts figures from an invoice, the output needs to be presented as something to check rather than something decided, with the source visible next to it.

## A New Sub-Processor, With Everything That Implies

The moment you send user content to a model provider, that provider is processing your users' data. That has concrete consequences you will be asked about.

You need a data processing agreement with them. You need to know the region their processing happens in. You need to know whether your data may be used for training — most business tiers say no, and it is a setting or a contract term rather than an assumption. You need to add them to the sub-processor list your business customers will request. And your privacy statement needs to say that content is sent to a third party for processing.

Founders frequently add a model API in an afternoon and remember none of this. It is the single most common gap in a privacy review of an AI-built product that itself uses AI.

## Moderation, Logging and What You Keep

**Moderation** matters if your feature generates content users see. Providers offer filtering; use it, and decide what happens when it triggers.

**Logging** is necessary for debugging and dangerous by default. Storing every prompt and response means storing whatever users pasted in — which may include personal data you never intended to hold. The workable compromise: log metadata always (who, when, how long, how much it cost, whether it failed), log content only when something failed, and delete those on a short schedule.

## The Fallback Nobody Builds

Write down what your product does when the model call fails. Not as an error page — as a designed experience.

For most features the answer is straightforward: show the underlying data without the AI layer, offer a retry, and be explicit that the enhanced version is temporarily unavailable. A search that falls back to keyword matching when the semantic layer is down is still a working search. A product whose entire interface is a chat box has no fallback at all, which is worth knowing before you build it that way.

## Before You Launch the Feature

- A hard spending cap at the provider and a per-user rate limit in your app.
- Input length truncation you chose.
- The model call behind your own server-side endpoint, never called directly from the browser.
- Minimal capability: no tool or data access the feature does not need.
- Output validated against an expected structure, escaped before rendering.
- A timeout and a designed fallback.
- The provider in your sub-processor list, with an agreement and a known region.
- Logging that captures metadata rather than content by default.
- A test where you paste adversarial instructions into the user input and confirm nothing interesting happens.

That last one takes five minutes and is the check almost nobody runs.

## Getting the Layer Underneath Right

AI features are the clearest example of something that is quick to prototype and genuinely different to operate. LaunchStudio builds the surrounding layer on products that already have the feature working: the call moved server-side with authentication and limits, spending caps and usage alerts, input and output validation, injection-resistant structuring, a designed fallback, privacy-appropriate logging, and the documentation your customers' reviewers will ask for.

The interface you built in Lovable, Bolt or Cursor stays as it is, and the code remains documented and AI-readable so you can keep iterating. It sits inside the [Launch Ready package](https://launchstudio.eu/en/#packages), delivered by Manifera's engineers from Amsterdam and Ho Chi Minh City, with eleven years of production work behind them for clients including Vodafone, TNO and CFLW.

If your product calls a model and you are not certain what a user could make it do, [talk to an engineer who understands AI-generated code](https://launchstudio.eu/en/#contact).

## Choosing a Model, and Changing It Later

Founders agonise over which model to use and then hardcode the choice in a way that makes changing it painful. The second mistake costs more than the first.

**Start with the cheapest model that passes your own test set.** Build twenty realistic examples with expected outputs before choosing anything, then try two or three models against them. This takes an afternoon and replaces opinion with evidence.

**Assume you will change.** Providers release new versions, prices move, and a model that suits you today may be superseded in months. Keep the provider call behind a single function in your code so swapping means changing one place rather than eleven.

**Pin the version explicitly** rather than accepting whatever "latest" resolves to. Silent model updates change your outputs without any deployment on your side, which is a debugging experience worth avoiding.

**Keep the test set as a regression check.** When you change model or prompt, run the twenty examples first. It is the closest thing to a unit test that this kind of feature allows, and it catches the quality drop that a casual try-it-once comparison misses.

## Real example

### A Recruitment Tool Whose CV Screener Could Be Talked Into Anything

Sanne Koopmans built Sollicitatiescan in Lovable: a tool letting small employers upload applicant CVs and receive a structured summary with a suitability score. Around forty employers in and around Amersfoort used it.

Two problems surfaced in review. The model call was made from the browser with the API key included, so anyone could use her provider account directly — and someone had, accounting for a noticeable share of the previous month's cost. And because CV text was inserted directly into the prompt, a test CV containing a line instructing the model to report the candidate as exceptionally qualified produced exactly that, with a high score and confident reasoning.

The second issue was the serious one. Employers were making shortlisting decisions on output that any applicant could influence by typing a sentence into their own document.

Six business days of work: the model call moved into a server-side function with authentication, per-account rate limits and input truncation; a hard spending cap and usage alerting at the provider; CV content separated from instructions in the request structure; output validated against a strict schema with the score constrained to a range and the extracted evidence required to quote source text; a visible caution in the interface that output is a summary to check rather than an assessment; a data processing agreement put in place and the provider added to the sub-processor list; and logging reduced to metadata with content retained only on failures for seven days.

**Result:** provider costs fell to roughly a fifth of the peak month, the injection test now fails safely, and two employers who had asked where CV data was processed received a documented answer.

> *"An applicant could write one sentence in white text at the bottom of their CV and my product would recommend them. I had built a screening tool that screened for whoever knew that trick."*
> — **Sanne Koopmans, Founder, Sollicitatiescan (Amersfoort)**

**Cost & Timeline:** €2,900 (server-side endpoint, limits and caps, injection hardening, output validation, privacy documentation) — completed in 6 business days.

## Frequently Asked Questions

### Can I call a model API directly from my frontend?

No. The key would be published to every visitor and your account would be usable by anyone. The call belongs in a server-side function that authenticates the user, applies your rate limit and then calls the provider.

### What is prompt injection, in practical terms?

Text supplied by a user containing instructions that the model follows. If your feature processes documents, messages or profiles, assume that content can attempt to redirect the model — and never let model output decide an authorisation question.

### How do I stop an AI feature becoming unpredictably expensive?

A hard spending cap at the provider, per-user rate limits, and truncation of input length to a value you chose. Cost scales with what users paste, not with how many users you have.

### Do I need to tell customers that content goes to a model provider?

Yes. They are a sub-processor: you need an agreement, a known processing region, clarity on whether data may be used for training, an entry in your sub-processor list and a line in your privacy statement.

### Should I log the prompts and responses?

Log metadata by default — who, when, cost, duration, success — and content only on failures, deleted on a short schedule. Storing every prompt means storing whatever users pasted, which is frequently personal data you did not intend to hold.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Can I call a model API directly from my frontend?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No — the key would be published to every visitor. The call belongs in a server-side function that authenticates the user and applies rate limits before calling the provider."
      }
    },
    {
      "@type": "Question",
      "name": "What is prompt injection, in practical terms?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "User-supplied text containing instructions the model follows. Assume documents, messages and profiles can redirect the model, and never let output decide authorisation."
      }
    },
    {
      "@type": "Question",
      "name": "How do I stop an AI feature becoming unpredictably expensive?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "A hard provider spending cap, per-user rate limits and input truncation you chose, because cost scales with what users paste rather than user count."
      }
    },
    {
      "@type": "Question",
      "name": "Do I need to tell customers that content goes to a model provider?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes — they are a sub-processor requiring an agreement, a known region, clarity on training use, a sub-processor list entry and a privacy statement line."
      }
    },
    {
      "@type": "Question",
      "name": "Should I log the prompts and responses?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Log metadata by default and content only on failures with short retention, since prompts often contain personal data you did not intend to store."
      }
    }
  ]
}
</script>
