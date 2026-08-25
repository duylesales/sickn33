---
Title: "Case Study: Implementing Graceful Degradation for an LLM Outage in 5 Days"
Keywords: Graceful Degradation, LLM Outage, AI SaaS Reliability, Fallback Model, OpenAI Outage, LaunchStudio, Manifera, Replit
Buyer Stage: Decision
---

# Case Study: Implementing Graceful Degradation for an LLM Outage in 5 Days

Every AI SaaS product has a single point of failure that most founders don't think about until it fails: the LLM provider itself. When OpenAI or Anthropic has a bad day, any product with no fallback plan goes down with it — not because of a bug in the founder's own code, but because of an architecture that never accounted for the possibility. This is the story of Nadia, a founder whose entire platform went dark during a three-hour OpenAI outage, and how LaunchStudio implemented graceful degradation for her product in five days so the next outage would be a minor inconvenience instead of a company-threatening event.

## The Three Hours That Nearly Cost Nadia Her Best Customer

Nadia built a meeting-notes and action-item platform for remote teams using Replit, with GPT-4 doing the heavy lifting: transcribing meeting audio, summarizing key points, and extracting action items automatically after every call. The product worked well enough that a 200-person company had just signed on as her largest customer yet, with a trial period that would decide whether they rolled it out company-wide.

On the fourth day of that trial, OpenAI had a regional outage lasting just over three hours. Nadia's platform didn't have a fallback of any kind — every API call to OpenAI simply hung until it timed out, and because the frontend had no failure-state handling either, users saw a spinning loader that never resolved. Meeting notes from six calls that morning were silently lost — not saved in a degraded form, not queued for retry, just gone, because the code assumed the API call would eventually succeed and had nothing in place for the case where it didn't.

The trial customer's IT lead noticed immediately and asked a pointed question in the shared Slack channel: "What happens when this happens again, but during a board meeting?" Nadia didn't have a real answer, and she knew that not having one could cost her the deal.

## Why "It Worked in Testing" Doesn't Predict What Happens in an Outage

The uncomfortable truth Nadia had to confront is that her product had never actually failed during development or QA, because OpenAI's API is reliable enough, most of the time, that a founder testing manually rarely triggers a real outage scenario. That reliability creates a dangerous blind spot: teams build and ship products that have never once exercised their failure path, because the failure path was never built in the first place — there was nothing to exercise.

This is a structural gap, not a coding mistake in the traditional sense. Nadia's code wasn't buggy; it simply didn't have an opinion about what should happen when the AI provider was unavailable. Three specific gaps compounded during the outage:

- **No timeout or circuit breaker.** API calls to OpenAI had no timeout configured, so requests hung indefinitely rather than failing fast and triggering any kind of recovery logic.

- **No fallback path.** There was no secondary model, cached response, or degraded-functionality mode — when the primary call failed, there was nothing else for the system to try.

- **No user-facing failure state.** The frontend had no design for "the AI is temporarily unavailable." Users just saw a loader spin forever, with no indication of what was happening or what to do next, which is what turned a backend outage into a visible trust problem.

## The Five-Day Build: Making Failure a Designed Experience

Nadia contacted LaunchStudio the day after the outage, with the trial decision now just over a week away. The engagement focused on one specific, scoped goal: make the next LLM outage survivable, without touching the core product experience customers already liked.

**Day 1-2: Circuit breakers and timeouts.** Engineers added explicit timeouts to every LLM call and wrapped them in a circuit breaker pattern — after a defined number of consecutive failures within a short window, the system stops sending requests to the failing provider entirely for a cooldown period, rather than letting every new request hang and pile up. This alone prevented the kind of resource exhaustion that had made Nadia's outage worse than it needed to be, since queued, hanging requests had been consuming server resources that could have served other users.

**Day 2-3: A secondary model fallback.** The team wired in a fallback to a second provider for the highest-priority function — transcription summarization — so that when the primary model was unavailable, the system automatically routed to the backup instead of failing outright. The fallback model wasn't as strong as GPT-4 for nuanced summarization, but a slightly less polished summary that actually arrives beats a perfect one that never does.

**Day 3-4: Local queuing for non-urgent processing.** For functions where a fallback model wasn't practical — action-item extraction, which needed higher accuracy than the fallback model reliably delivered — the team implemented a local queue. Raw transcripts were saved immediately and reliably, regardless of AI availability, with processing retried automatically once the primary provider recovered. Nothing was ever silently lost again; worst case, a result arrived a few minutes late instead of never.

**Day 4-5: Honest, designed failure states in the UI.** The frontend was updated to detect degraded and failed states explicitly, replacing the infinite loader with a clear message: "We're experiencing a temporary delay with AI processing — your meeting is saved and notes will be ready shortly." Users could see their raw transcript immediately, even before the AI-generated summary caught up, so a call was never fully invisible even during an outage.

## The Result: The Next Outage Was a Non-Event

Three weeks after the fix shipped, OpenAI had another, shorter outage — this time about 40 minutes. Nadia's platform automatically failed over to the secondary model for summarization, queued the action-item extraction for retry, and displayed a clear status message to users the entire time. No meeting notes were lost. No support tickets were filed. The trial customer's IT lead, who had been the one to raise the original concern, noticed nothing at all — which was exactly the point.

Nadia's trial converted to a full company-wide rollout two weeks later. When asked directly what tipped the decision, the IT lead cited two things: the product itself, and the fact that Nadia had come back with a concrete answer to "what happens when this happens again" instead of a promise to look into it.

## The Broader Lesson: Reliability Is a Feature You Have to Design, Not One You Get for Free

Graceful degradation isn't really about the LLM provider at all — it's about accepting that any external dependency will fail eventually, and deciding in advance what "failing well" looks like instead of discovering it live, in front of a customer, during an outage. The pattern Nadia's product needed — timeouts, circuit breakers, fallback paths, and honest UI states — applies just as much to payment processors, email delivery services, and any other third-party API a product depends on to function.

The reason this gets skipped in most AI-builder-generated products isn't negligence; it's that the failure path is invisible until the day it's needed, and nothing in a typical development or demo cycle forces a founder to build for a scenario that, statistically, probably won't happen this week. The cost of skipping it is asymmetric, though: most weeks it costs nothing, and then one week it costs a trial customer, a board meeting's worth of lost notes, or worse.

There's also a monitoring dimension founders tend to underestimate. Before the fix, Nadia had no alerting at all tied to LLM call failures — the first she knew of the outage was the trial customer's Slack message, hours after it started. As part of the same engagement, LaunchStudio wired the circuit breaker's state changes into a monitoring dashboard with a Slack alert, so a future outage triggers a notification to Nadia's team within seconds of the failure threshold being crossed, rather than being discovered secondhand from an unhappy customer. Knowing about a degradation before a customer has to tell you about it is, on its own, often the difference between a minor operational note and a trust-damaging incident.

## Key Takeaways

- Most AI SaaS products have never actually exercised their failure path, because LLM providers are reliable enough that manual testing rarely triggers a real outage — which means the failure path often doesn't exist at all until it's forced into existence during a real incident.

- Circuit breakers and explicit timeouts prevent a single provider outage from cascading into resource exhaustion caused by requests hanging and piling up indefinitely.

- A fallback to a secondary model, even one that produces slightly lower-quality output, is almost always better than a hard failure — a usable result that arrives late beats no result at all.

- Honest, designed failure states in the UI turn an outage from an invisible trust problem into a visible, well-handled one; users tolerate delays far better than they tolerate silence.

- Partnering with reliability specialists like LaunchStudio (backed by Manifera's 11+ years of production engineering, trusted by enterprise clients including Vodafone and TNO) can implement graceful degradation for LLM outages in about a week, turning a company-threatening event into a non-event before it costs you a customer.

## Don't Wait for an Outage to Find Out Your Product Has No Fallback

If your AI SaaS platform has never survived a real LLM provider outage, it's not because it's resilient — it's because it hasn't been tested yet.

LaunchStudio is operated by **Manifera**, an international software engineering company founded in 2014 and led by Founder & Managing Director **Herre Roelevink**. As Roelevink puts it: *"We see a shift in software needs. The challenge is no longer turning good ideas into software. It's now about the architecture and security needed to bring those products to maturity. We have eleven years of experience in exactly that."* Combining "Dutch management with Vietnamese mastery," Manifera maintains headquarters in **Amsterdam, the Netherlands** (Herengracht 420), an Asia hub in **Singapore** (100 Tras Street), and a primary development center in **Ho Chi Minh City, Vietnam** (Pho Quang Street). Through LaunchStudio, senior engineering teams take your existing AI-built frontend and implement production-ready security controls, live payment gateways, secure hosting, and monitoring — transforming your prototype into a secure, compliant MVP in 1 to 3 weeks, without a rebuild. [Get a free quote today](https://launchstudio.eu/en/#contact) or see how Manifera's [custom software development team](https://www.manifera.com/services/custom-software-development/) approaches production-hardening for AI-generated codebases.

## Real example

### An AI-Native Founder in Action: AI Recruiting Screener

Ingrid, a startup founder, used **v0** to build an AI-powered resume-screening platform for recruiting agencies. During a busy hiring season, a 25-minute Anthropic outage caused her platform to silently drop dozens of candidate evaluations mid-process, leaving recruiters unable to tell which candidates had actually been screened and which had simply vanished from the queue.

Ingrid partnered with **LaunchStudio (by Manifera)** to build a graceful degradation layer. The engineering team added persistent job queuing so every screening request survived a provider outage, implemented automatic retries with exponential backoff, and added a clear "processing delayed" status visible to recruiters instead of a silent failure.

**Result:** Ingrid's platform survived its next provider outage with zero lost evaluations and no recruiter-facing confusion, compared to dozens of silently dropped candidates before the fix.

**Cost & Timeline:** €1,400 (Launch Ready Package) — implemented and verified in 5 business days.

---

---

---
## Frequently Asked Questions

### What is graceful degradation in the context of an AI SaaS product?

Graceful degradation is the practice of designing a system so that when a core dependency — like an LLM provider — becomes unavailable or slow, the product continues to function in a reduced but still useful way, instead of failing completely. This includes fallback models, request queuing, circuit breakers, and clear failure messaging in the UI.

### Why didn't testing catch Nadia's lack of a fallback before the outage?

Because LLM providers are reliable enough most of the time that manual testing during development rarely triggers a genuine outage scenario. The failure path had never been built, so there was nothing to test — the gap was structural, not a bug that testing would normally catch.

### How long does it take to implement graceful degradation for LLM outages?

For a focused build like Nadia's — timeouts, circuit breakers, a secondary model fallback, local queuing, and honest UI failure states — five business days is typical, without requiring changes to the product's core user experience.

### Does adding a fallback model hurt output quality?

It can, slightly, for the specific function using the fallback — Nadia's backup model produced marginally less polished summaries than GPT-4. But a usable result that arrives during an outage is almost always preferable to a complete failure, and the fallback is only invoked when the primary provider is actually unavailable.

### What's the difference between a circuit breaker and just adding a timeout?

A timeout stops an individual request from hanging indefinitely, but without a circuit breaker, every new request during an outage still attempts the call and still times out, piling up resource usage. A circuit breaker tracks recent failures and stops sending requests to a failing provider entirely for a cooldown period, preventing that resource exhaustion from compounding the outage's impact.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What is graceful degradation in the context of an AI SaaS product?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Graceful degradation is the practice of designing a system so that when a core dependency — like an LLM provider — becomes unavailable or slow, the product continues to function in a reduced but still useful way, instead of failing completely. This includes fallback models, request queuing, circuit breakers, and clear failure messaging in the UI."
      }
    },
    {
      "@type": "Question",
      "name": "Why didn't testing catch Nadia's lack of a fallback before the outage?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Because LLM providers are reliable enough most of the time that manual testing during development rarely triggers a genuine outage scenario. The failure path had never been built, so there was nothing to test — the gap was structural, not a bug that testing would normally catch."
      }
    },
    {
      "@type": "Question",
      "name": "How long does it take to implement graceful degradation for LLM outages?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "For a focused build like Nadia's — timeouts, circuit breakers, a secondary model fallback, local queuing, and honest UI failure states — five business days is typical, without requiring changes to the product's core user experience."
      }
    },
    {
      "@type": "Question",
      "name": "Does adding a fallback model hurt output quality?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "It can, slightly, for the specific function using the fallback — Nadia's backup model produced marginally less polished summaries than GPT-4. But a usable result that arrives during an outage is almost always preferable to a complete failure, and the fallback is only invoked when the primary provider is actually unavailable."
      }
    },
    {
      "@type": "Question",
      "name": "What's the difference between a circuit breaker and just adding a timeout?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "A timeout stops an individual request from hanging indefinitely, but without a circuit breaker, every new request during an outage still attempts the call and still times out, piling up resource usage. A circuit breaker tracks recent failures and stops sending requests to a failing provider entirely for a cooldown period, preventing that resource exhaustion from compounding the outage's impact."
      }
    }
  ]
}
</script>
