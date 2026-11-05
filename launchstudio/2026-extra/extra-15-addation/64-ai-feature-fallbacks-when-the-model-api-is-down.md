---
Title: "AI Feature Fallbacks: When the Model API Is Down"
Keywords: ai api outage fallback, llm fallback strategy, circuit breaker ai api, resilient ai features saas, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: AI-Native Founder (Non-Technical)
---

# AI Feature Fallbacks: When the Model API Is Down

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "AI Feature Fallbacks: When the Model API Is Down",
  "description": "Every AI provider has outages, rate limits and slow periods, and AI-built apps often fail completely when they happen. This guide explains the failure types, retries with backoff, timeouts, circuit breakers, secondary models and providers, queues, caching and graceful degradation, how to communicate with users, and how to test fallbacks before customers depend on them.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-06-20",
  "inLanguage": "en",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/ai-feature-fallbacks-when-the-model-api-is-down" },
  "citation": [
    { "@type": "CreativeWork", "name": "Google SRE Book: Handling overload", "url": "https://sre.google/sre-book/handling-overload/" },
    { "@type": "CreativeWork", "name": "AWS Architecture Blog: Exponential backoff and jitter", "url": "https://aws.amazon.com/blogs/architecture/exponential-backoff-and-jitter/" },
    { "@type": "CreativeWork", "name": "Martin Fowler: Circuit Breaker", "url": "https://martinfowler.com/bliki/CircuitBreaker.html" },
    { "@type": "CreativeWork", "name": "OpenAI status page", "url": "https://status.openai.com/" }
  ]
}
</script>

When your AI features work, they can be the reason customers choose your product. When the model provider has an outage, they can be the reason customers lose a morning of work. Every major AI provider publishes a status page, and every status page shows incidents: elevated error rates, degraded performance, rate limiting during peaks, occasional full outages. These events are normal for any large online service. What is not inevitable is your product failing along with them.

AI-built apps usually have a single path for AI features: call the model, wait for the answer, show it. If the call fails, the user sees an error, or worse, a spinner that never stops. If the call takes forty seconds instead of four, the page appears frozen. If the provider rate-limits your account during a busy hour, every customer is affected at once.

This guide explains how to design AI features that degrade gracefully instead of failing completely.

## Key Takeaways

- **AI calls fail in several ways:** outages, rate limits, timeouts, slow responses, refusals and model retirements. Each needs a defined response.
- **Retry transient errors with exponential backoff and jitter,** and set strict timeouts.
- **Use circuit breakers** to stop sending requests to a failing provider and switch to alternatives quickly.
- **Fallback options include secondary models, other providers, queues for later processing, cached results and manual alternatives.**
- **Tell users what is happening** and never lose their input when an AI step fails.

## How AI Calls Fail

| Failure | What it looks like | Typical response |
| --- | --- | --- |
| Transient error | Occasional 5xx responses or connection resets | Retry with backoff |
| Rate limiting | 429 responses, often during peaks | Back off, queue, spread load, use alternative capacity |
| Timeout or slowness | Responses taking far longer than usual | Timeout, fallback model, or queue |
| Partial outage | High error rates for a specific model or region | Circuit breaker, switch model or region |
| Full outage | Provider unavailable | Switch provider, queue, or degrade |
| Refusal or filtered output | Model declines or returns unusable content | Retry with adjusted prompt, alternative model, or manual path |
| Invalid output | Output does not match the expected format | Validate, retry, repair or fall back |
| Model retirement | Model version no longer available | Planned migration, configuration switch |

Treat each as an expected condition, not an exception.

## Timeouts First

The most common resilience problem is no timeout at all. A request that hangs ties up the user's screen, your server function and sometimes a database connection.

- **Set timeouts per feature,** based on what users will tolerate. A suggestion widget may tolerate a few seconds; a background document analysis may tolerate a minute.
- **For streaming,** set a timeout for the first token and for overall duration.
- **When a timeout occurs,** move to the next step in your fallback plan rather than simply showing an error.

## Retries With Backoff and Jitter

Transient errors often succeed on a second attempt. Retry them, carefully:

- **Retry only retryable errors,** such as timeouts, connection errors, 5xx responses and rate limits. Do not retry invalid requests.
- **Use exponential backoff,** for example waiting one, two and four seconds, with random jitter so many clients do not retry at exactly the same moment.
- **Respect retry headers** from providers when rate limited.
- **Limit total attempts and total time,** so retries do not make a slow situation worse.
- **Make retries idempotent** on your side, for example not deducting credits twice or creating two records.

## Circuit Breakers

When a provider is clearly failing, continuing to send every request to it wastes time and capacity. A circuit breaker tracks recent failures and, after a threshold, "opens" to stop requests for a short period, sending them to a fallback instead. After a cooldown, it lets a few test requests through and closes again if they succeed.

For a small SaaS, a simple implementation with failure counts and time windows per provider and model is enough. Store state in memory or a shared store, depending on how your functions run.

## Fallback Options

**1. Secondary model from the same provider.** If a large model is slow or unavailable, a smaller one may handle the task acceptably. Useful for classification, extraction and short responses.

**2. Another provider.** With a provider abstraction, a feature can switch to a comparable model from another provider. This requires prompts and output handling that work with both, verified on your evaluation set. Consider data terms: the fallback provider must meet the same data location and processing commitments you made to customers.

**3. Queue for later.** For non-interactive tasks, such as summarising uploaded documents or generating reports, put the job in a queue and process it when the provider recovers. Tell the user it will be ready later and notify them when it is.

**4. Cached results.** If the same input was processed recently, return the cached result. Effective for repeated questions, standard summaries or classification of identical items.

**5. Rule-based or template fallback.** For some features, a simpler non-AI method provides a basic result, such as keyword-based categorisation or a template reply the user can edit.

**6. Manual path.** Let the user complete the task without AI: write the reply themselves, choose a category manually, fill in fields by hand. The key is that the rest of the product keeps working.

## Choosing Fallbacks Per Feature

| Feature | Primary | Fallback 1 | Fallback 2 | Last resort |
| --- | --- | --- | --- | --- |
| Chat assistant | Main model | Secondary model | Alternative provider | Message that assistant is temporarily unavailable |
| Document extraction | Main model | Retry later via queue | Alternative provider | Manual entry form, prefilled where possible |
| Reply drafting | Main model | Smaller model | Template reply | User writes manually |
| Classification | Small model | Alternative provider | Rule-based classifier | Manual selection |
| Report generation | Batch job | Retry later | Alternative provider | Notify user of delay |

Document these choices so the team, and AI coding tools working on the codebase, apply them consistently.

## Never Lose User Input

The worst experience is losing what the user did before the AI step failed. Protect it:

- **Save input before calling the model,** such as the uploaded document, the typed question or the form contents.
- **Keep the request in a retryable state** with clear status.
- **Allow the user to retry** with one click, without re-entering anything.
- **For background jobs,** show status in the interface and notify when complete.

## Communicating With Users

Honest, specific messages maintain trust:

- "Our AI assistant is temporarily slower than usual. Your summary will appear in a moment."
- "AI suggestions are temporarily unavailable. You can continue writing manually; we will try again automatically."
- "Your document has been received and will be processed within a few minutes. We will notify you when it is ready."

Avoid generic "Something went wrong" messages. If an outage lasts longer, mention it on your status page. Our guide on [adding a status page to your SaaS](https://launchstudio.eu/en/blog/how-do-i-add-a-status-page-to-my-saas) explains how.

## Validating Output

Not every failure is an error code. Models sometimes return output that is malformed, incomplete or off-task. For structured outputs:

- **Validate against a schema** before using the result.
- **Retry with a repair prompt** or a different model if validation fails.
- **Fall back to manual review** for repeated failures.
- **Log invalid outputs** to improve prompts and detect provider regressions.

## Cost and Quality Trade-offs of Fallbacks

Fallbacks are not free. Each option has consequences you should understand before an incident forces the decision:

- **Secondary models** may be cheaper but less accurate. If a fallback model handles a quarter of traffic for a day, some customers receive lower-quality results. Decide whether to label fallback results or to queue instead for quality-sensitive tasks.
- **Alternative providers** may cost more per request, and maintaining prompts for two providers takes ongoing effort. Rerun your evaluation set on both whenever prompts change.
- **Queues** preserve quality but delay results. For interactive features, a delay of seconds is acceptable; a delay of hours may not be.
- **Caching** saves money and improves resilience, but cached answers can become stale. Set sensible expiry times, and never cache results that depend on data the user may have changed.
- **Manual paths** cost users time. They are a last resort, and the interface should make them as quick as possible, for example with prefilled fields.

Write down, per feature, which trade-off you accept. During an incident, there is no time to debate whether a slightly worse summary is better than no summary.

## Planning for Provider Changes

Some "outages" are planned: a model version is retired, a price changes or a region is added or removed. Treat provider announcements as part of your operations. Subscribe to provider changelogs, keep model identifiers in configuration rather than code, and schedule migrations well before retirement dates, verified against your evaluation set.

## Monitoring

Track per provider and model:

- Error rate and error types
- Latency percentiles, including time to first token for streaming
- Rate limit responses
- Fallback usage
- Queue length for deferred tasks

Alert when error rates or latency exceed thresholds, and subscribe to provider status pages. Fallback usage is especially informative: if the secondary model handles a large share of traffic, users may be getting lower quality without anyone noticing.

## Testing Fallbacks

Fallbacks that have never run probably do not work. Test them deliberately:

- **Fault injection in staging:** configure the AI layer to return errors, timeouts or rate limits for a percentage of requests.
- **Provider switch tests:** force the secondary provider and run your evaluation set.
- **Queue recovery tests:** simulate an outage, queue jobs, then restore and confirm they complete.
- **User experience checks:** verify messages, retry buttons and preserved input.

Run these tests before launch and after significant changes to AI features.

## How LaunchStudio Helps

LaunchStudio makes AI features resilient in AI-built apps: adding timeouts and retries with backoff, circuit breakers per provider and model, secondary models and providers behind a provider abstraction, queues for deferred processing, caching, output validation, user-facing status and retry flows, monitoring and fault injection tests.

The **Launch Ready** package (€800-€3,500) covers resilience fixes for existing AI features along with security hardening; **Launch & Grow** (€2,500-€7,500 plus €49 per month) adds managed hosting, monitoring and priority support. Use the [price calculator](https://launchstudio.eu/en/#calculator) for an estimate. For provider choice, see our guide on [choosing an LLM API for an EU SaaS](https://launchstudio.eu/en/blog/choosing-an-llm-api-for-an-eu-saas-openai-anthropic-or-mistral).

LaunchStudio is backed by Manifera, a software development company with 11+ years of experience, 160+ delivered projects and 120+ engineers, building resilient integrations for enterprise clients. Founders meet the team at Herengracht 420 in Amsterdam; engineering happens at the development centre on Pho Quang Street in Ho Chi Minh City, with a hub on Tras Street in Singapore.

## Real example

### An AI-Native Founder in Action: The Expense Scanner That Stopped Every Monday Morning

Maarten Oosterhuis built Bonnetjesbot with Bolt and Supabase: an app where employees photograph receipts and an AI model extracts supplier, date, amount and VAT for expense claims. Usage peaked on Monday mornings, when employees submitted the previous week's receipts. On several Mondays, the provider rate-limited the account, and once there was a two-hour partial outage. Each time, uploads failed with an error, employees had to retake photos later and some gave up.

The app called the model synchronously during upload, with no timeout, no retries and no alternative. Failed extractions discarded the uploaded image. There was no record of which receipts were waiting, and support learned about problems from customers.

LaunchStudio separated upload from extraction: receipts were saved to private storage immediately with a pending status, and extraction ran from a queue. Calls had a timeout, retried with exponential backoff and jitter while respecting rate limit headers, and a circuit breaker switched to a secondary model from another provider, processed in the EU under the same data commitments, after repeated failures. If both were unavailable, jobs stayed queued and processed automatically on recovery. Output was validated against a schema, with failed validations retried once and otherwise sent to manual entry with prefilled fields. Employees saw a clear status per receipt and received a notification when extraction completed, and monitoring alerted Maarten when error rates or queue length rose.

**Result:** On the next provider incident, a Monday morning rate-limit episode, employees noticed nothing beyond receipts taking a minute longer to process. Over the following quarter, no receipt was lost, and support tickets about failed uploads dropped to zero.

> *"I used to dread Monday mornings. Now the queue absorbs the peak and the fallback absorbs the outages."*
> - **Maarten Oosterhuis, Founder, Bonnetjesbot (Groningen)**

**Cost & Timeline:** €3,500 (Launch Ready package: queue-based processing, timeouts and retries, circuit breaker, secondary provider fallback, validation, status and monitoring) - completed in 9 business days.

## Frequently Asked Questions

### What should my app do when the AI provider is down?

It should keep working as much as possible: retry briefly, switch to a secondary model or provider if available, queue non-urgent work for later, and let users complete tasks manually. Users should see clear status messages and never lose their input.

### Should I use multiple AI providers?

For important features, having a fallback provider reduces dependence on a single service. It requires a provider abstraction, prompts that work with both and fallback providers that meet the same data commitments you made to customers. For less critical features, a secondary model or a queue may be enough.

### How do I handle rate limits from AI providers?

Retry with exponential backoff and jitter, respect retry headers, spread work through queues, cache repeated requests and request higher limits for your expected volume. Avoid retrying aggressively, which makes rate limiting worse.

### How does Manifera's experience help with resilient AI features?

Manifera has built integrations with external services for enterprise clients for 11+ years, where outages are expected and must not stop the business. LaunchStudio applies those resilience patterns to AI features, which depend on external providers more than most product functionality.

### Does AI reliability affect my product's reputation?

Yes. Customers judge your product, not your provider, when an AI feature fails. Resilient features and honest status communication protect reviews and retention, which shape how buyers, search engines and AI answer engines perceive your product.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What should my app do when the AI provider is down?",
      "acceptedAnswer": { "@type": "Answer", "text": "Retry briefly, switch to secondary models or providers, queue non-urgent work, allow manual completion and never lose input." }
    },
    {
      "@type": "Question",
      "name": "Should I use multiple AI providers?",
      "acceptedAnswer": { "@type": "Answer", "text": "For important features yes, with a provider abstraction and fallbacks meeting the same data commitments." }
    },
    {
      "@type": "Question",
      "name": "How do I handle rate limits from AI providers?",
      "acceptedAnswer": { "@type": "Answer", "text": "Exponential backoff with jitter, respect retry headers, queues, caching and higher limits; avoid aggressive retries." }
    },
    {
      "@type": "Question",
      "name": "How does Manifera's experience help with resilient AI features?",
      "acceptedAnswer": { "@type": "Answer", "text": "Manifera has built resilient enterprise integrations for 11+ years and LaunchStudio applies those patterns to AI features." }
    },
    {
      "@type": "Question",
      "name": "Does AI reliability affect my product's reputation?",
      "acceptedAnswer": { "@type": "Answer", "text": "Yes; customers blame your product, so resilience and honest status communication protect reviews and retention." }
    }
  ]
}
</script>
