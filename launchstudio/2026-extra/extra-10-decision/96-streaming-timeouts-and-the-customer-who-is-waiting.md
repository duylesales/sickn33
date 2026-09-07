---
Title: "Streaming, Timeouts, and the Customer Who Is Waiting"
Keywords: streaming llm response ux, serverless timeout ai request, long running ai job queue, cancel ai generation, perceived latency ai feature, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: Technical Solo Founder / Indie Hacker
---

# Streaming, Timeouts, and the Customer Who Is Waiting

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Streaming, Timeouts, and the Customer Who Is Waiting",
  "description": "AI calls take seconds rather than milliseconds, which breaks assumptions built into hosting platforms and interfaces alike. Why long requests time out, when streaming is the right answer and when a background job is, and how to handle a customer who closes the tab.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-05-25",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/streaming-timeouts-and-the-customer-who-is-waiting" }
}
</script>

Every other request in your product completes in well under a second. An AI call takes three seconds for something short and considerably longer for anything substantial, and that single fact breaks assumptions in three places at once: the hosting platform that terminates long-running requests, the browser that gives up on a connection, and the customer looking at a screen that appears to have stopped.

The result in most prototypes is a feature that works during development, when the developer is patient and the test input is small, and fails intermittently in production in a way that looks like a bug in the model rather than in the request handling.

## The Timeout Is Not Where You Think

There is rarely one timeout. There are several, and the shortest one wins.

**The hosting platform** terminates requests after a fixed period — commonly 10 to 60 seconds on serverless platforms, sometimes configurable, sometimes not. This is the one that catches people, because it is invisible until exceeded.

**Any proxy or load balancer** in front of your application has its own limit.

**The browser** will abandon a request that produces nothing for long enough, and a customer on a mobile connection may lose it sooner.

**The customer** gives up before any of these. Ten seconds of a spinner with no change is where people start clicking again, navigating away, or concluding the feature is broken.

Two consequences follow. Anything that might take longer than your platform's limit cannot run inside a normal request, regardless of how you feel about it. And the customer's patience, not the technical limit, is the constraint that should shape the design.

## Streaming Solves Perception, Not Duration

Streaming — showing the response as it is produced, token by token — is the standard answer for text a person reads, and it works for a specific reason: perceived wait is dominated by time to *first* output, not total time. A response that begins appearing in 800 milliseconds and completes in twelve seconds feels faster than one that appears all at once at six.

It also keeps the connection active, which prevents some timeouts, and it lets the customer start reading and decide early whether the answer is going the right way.

Streaming is right when a person is reading the output as prose. It is not right for everything, and three cases argue against it. **Structured output** you need to validate before use is not meaningful in fragments, so streaming adds complexity for no benefit. **Very long operations** — anything measured in minutes — should not hold a connection open even while streaming. And **anything the customer is not watching** obviously gains nothing.

Implementing it also has real requirements: the platform must support streaming responses, which not all do; partial output must be handled when the connection drops mid-stream; and the customer needs a way to stop generation, which should also stop the work rather than merely hiding it.

## When It Should Be a Background Job

The rule is simple: if it might exceed the platform's request limit, or if the customer might reasonably do something else while waiting, it belongs in a background job.

That shape is familiar from imports and exports. Accept the request, return immediately with an identifier, do the work in a worker, notify when finished. The customer sees a queued state, then progress, then a result — and can close the tab without losing anything, which is the property that matters most for anything that takes more than a few seconds.

This applies to a whole class of AI features: processing a long document, generating something for every row in a dataset, anything involving several sequential model calls, and anything where the output is a file rather than a screen.

Two details make the difference between a background job that helps and one that frustrates. **Show meaningful progress** — "processing page 12 of 40" rather than an indefinite spinner — because an unbounded wait with no information is worse than a longer wait with a number. And **make the result durable**, so a customer who returns an hour later finds it waiting rather than discovering the work was discarded when they navigated away.

Building AI features that respect platform limits, stream where it helps, and move to background work where it is necessary is ordinary production engineering, and it is a common failure point in AI-built products where the model call sits directly inside a request handler. LaunchStudio, backed by Manifera's 11+ years of production engineering, structures these paths so they work under real conditions. [Describe your project](https://launchstudio.eu/en/#contact) for a review within one business day.

## Failing and Cancelling Without Losing Work

Two states that prototypes handle badly.

**The customer cancels or leaves.** They should be able to stop generation, and stopping should actually terminate the work rather than leaving it running and billing you. Equally, a customer who closes a tab during a background job should find the result when they return — the work was paid for and there is no reason to discard it.

**The call fails partway.** Model APIs return errors, rate limits, and occasional timeouts of their own. Retry once for transient failures, with a short delay; distinguish a rate limit, which should wait and retry, from an invalid request, which will fail identically forever. And never leave the customer with a spinner that continues indefinitely because the failure path was not implemented — an honest error with a retry option is far better.

Timeouts on your side deserve a specific decision: set your own limit on how long you will wait for a model, shorter than the platform's, so that you control the failure rather than being terminated mid-call with nothing recorded.

## Design the Wait Itself

Beyond the mechanics, the interface during the wait determines how long it feels.

**Say what is happening**, specifically. "Reading your document", then "Writing the summary" is materially better than a spinner, because it demonstrates progress rather than asserting it.

**Give an honest expectation.** "This usually takes about 20 seconds" prevents the customer from concluding at second eight that something is wrong.

**Let them do something else.** A background job with a notification is better than a modal that blocks the product.

**Never lose their input.** If generation fails, whatever they typed must still be there. Losing a customer's carefully written prompt because the model call errored is a small failure that produces disproportionate annoyance.

And where a fast, lower-quality result is available, consider showing it first and refining — an extractive summary in half a second while the model produces a better one, for instance. Whether that suits depends on the feature, and when it does, it removes the wait entirely.

## Real example

### The Feature That Worked for Short Documents Only

Nora Bakkali ran Contractlens, a contract-review tool for small legal practices, built in Lovable. Uploaded contracts were analysed by a model and returned as a summary with flagged clauses, inside a normal request on a serverless platform with a 30-second limit.

For short contracts it worked. For anything over about fifteen pages the call exceeded 30 seconds and the platform terminated the request, returning a generic error. The model call continued and completed on the provider's side, so she paid for every failed analysis. Customers, seeing an error, uploaded again — often three or four times — multiplying the cost of a document that never succeeded.

Roughly a fifth of uploads were failing this way, and because the error message was generic, customers had reported it as "the product doesn't work with big contracts", which she had interpreted as a model limitation rather than a timeout.

**Result:** analysis moved to a background job with per-section progress, results stored durably so customers could close the tab, a shorter internal timeout with one retry on transient failures, cancellation that actually terminates the work, and a clear expectation shown before starting. Long-contract failures went to zero and the duplicate-upload spend disappeared.

> "I thought the model could not handle long contracts. The model handled them fine every single time — my hosting platform hung up before the answer came back."
> — **Nora Bakkali, Founder, Contractlens**

**Cost & Timeline:** background processing and progress reporting delivered in 3 business days.

## Frequently Asked Questions

### Why do AI features fail on larger inputs but work on small ones?

Because the request exceeds a timeout — usually the hosting platform's, often 10 to 60 seconds on serverless platforms. The model call frequently completes anyway, so you pay for work the customer never receives.

### Does streaming fix timeout problems?

Partly. It keeps the connection active and greatly improves perceived speed by showing output early, but it does not suit structured output that must be validated, and anything measured in minutes still belongs in a background job.

### When should an AI feature be a background job?

Whenever it might exceed the platform's request limit, involves several sequential model calls, processes a long document, or produces a file. The customer should be able to close the tab and find the result later.

### What should happen if the customer cancels?

Generation should actually stop rather than continuing to run and bill you. Conversely, a background job should not be discarded because the customer navigated away, since the work has already been paid for.

### How do I make the wait feel shorter?

Show what is happening specifically rather than a spinner, give an honest time expectation, let the customer do something else while it runs, and never lose their input if it fails.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "Why do AI features fail on larger inputs but work on small ones?", "acceptedAnswer": { "@type": "Answer", "text": "The request exceeds a timeout, usually the hosting platform's. The model call often completes anyway, so you pay for work the customer never receives." } },
    { "@type": "Question", "name": "Does streaming fix timeout problems?", "acceptedAnswer": { "@type": "Answer", "text": "Partly. It keeps the connection active and improves perceived speed, but it does not suit structured output needing validation, and long operations still belong in background jobs." } },
    { "@type": "Question", "name": "When should an AI feature be a background job?", "acceptedAnswer": { "@type": "Answer", "text": "Whenever it might exceed the request limit, involves several sequential calls, processes a long document, or produces a file, so the customer can close the tab and return." } },
    { "@type": "Question", "name": "What should happen if the customer cancels?", "acceptedAnswer": { "@type": "Answer", "text": "Generation should actually stop rather than continue billing you, while a background job should not be discarded merely because the customer navigated away." } },
    { "@type": "Question", "name": "How do I make the wait feel shorter?", "acceptedAnswer": { "@type": "Answer", "text": "Show specifically what is happening, give an honest time expectation, let the customer do something else, and never lose their input on failure." } }
  ]
}
</script>
