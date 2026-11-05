---
Title: "Streaming AI Responses in a Supabase App"
Keywords: stream ai responses supabase, server sent events edge function, streaming llm react, ai chat streaming security, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: AI-Native Founder (Non-Technical)
---

# Streaming AI Responses in a Supabase App

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Streaming AI Responses in a Supabase App",
  "description": "Streaming makes AI features feel fast by showing text as it is generated. This guide explains how to stream model responses through Supabase edge functions or a server route to a React frontend: authentication, server-sent events, cancellation to save costs, timeouts, saving the final result, safe rendering of Markdown, rate limits, cost tracking and the failure modes that AI-generated streaming code usually misses.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-06-19",
  "inLanguage": "en",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/streaming-ai-responses-in-a-supabase-app" },
  "citation": [
    { "@type": "CreativeWork", "name": "Supabase Edge Functions documentation", "url": "https://supabase.com/docs/guides/functions" },
    { "@type": "CreativeWork", "name": "MDN: Server-sent events", "url": "https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events" },
    { "@type": "CreativeWork", "name": "MDN: AbortController", "url": "https://developer.mozilla.org/en-US/docs/Web/API/AbortController" },
    { "@type": "CreativeWork", "name": "OWASP Cross Site Scripting Prevention Cheat Sheet", "url": "https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html" }
  ]
}
</script>

Waiting fifteen seconds for an AI answer feels broken. Watching the answer appear word by word within half a second feels fast, even if the full response still takes fifteen seconds. That is why almost every AI chat, writing assistant and summary feature streams its output: the model sends text in small pieces as it generates them, and the interface shows each piece immediately.

AI builders often add streaming quickly, sometimes by calling the model provider directly from the browser with an API key in the frontend, sometimes through a server function that works in the preview but breaks behind proxies, ignores cancelled requests or never saves the final answer. Streaming touches authentication, cost control, error handling and security at once, so the details matter.

This guide explains how to stream AI responses properly in a Supabase-based app.

## Key Takeaways

- **Never call model providers directly from the browser** with your API key. Stream through a server-side function that authenticates the user.
- **Server-sent events or streamed HTTP responses** are the simplest way to deliver tokens to the browser.
- **Cancel the upstream request when the user stops or leaves,** or you keep paying for tokens nobody reads.
- **Save the final result server-side** once the stream completes, with clear handling of partial or failed streams.
- **Render streamed Markdown safely,** sanitising output to prevent cross-site scripting.

## The Architecture

A safe streaming setup has three parts:

1. **Frontend:** sends the user's request with their session token and renders tokens as they arrive.
2. **Server function:** a Supabase edge function or a server route in Next.js, which authenticates the user, checks permissions and limits, builds the prompt, calls the model provider with streaming enabled and forwards chunks to the client.
3. **Model provider:** streams tokens back to the server function.

The API key for the model provider lives only in the server function's secrets. The server decides what the prompt contains, which data is included and which model is used, so users cannot manipulate those choices directly.

## Streaming Formats

Two common approaches:

**Server-sent events (SSE).** The response uses the `text/event-stream` content type and sends events as lines of text. Browsers support SSE natively through `EventSource` for GET requests, and many libraries handle SSE over POST using `fetch` and stream readers. Model providers commonly use SSE in their own streaming APIs.

**Streamed HTTP body.** The server writes chunks to a response body, and the client reads them with `fetch` and a `ReadableStream` reader. This is flexible and works well with POST requests carrying the prompt.

WebSockets are rarely needed for one-directional AI streaming and add complexity.

Supabase edge functions can return streaming responses, and frameworks such as the Vercel AI SDK provide helpers for streaming on both server and client.

## Authentication and Authorisation

Every streaming request must be authenticated:

- **Verify the user's session token** in the function before calling the model.
- **Check that the user may access the data** you include in the prompt. If the feature summarises a document, confirm the user can read that document, ideally by querying with the user's identity so Row Level Security applies.
- **Apply plan entitlements and limits,** such as monthly AI credits, before starting the stream.

A common failure in AI-generated code is a function that accepts a document ID from the client and loads it with the service role key, letting any logged-in user summarise any document.

## Cancellation: Do Not Pay for Unread Tokens

Users close tabs, navigate away or click "Stop" while a response is still generating. If your server function keeps the upstream request open, the model keeps generating and you keep paying.

- **On the client,** use an `AbortController` to cancel the fetch when the user stops or the component unmounts.
- **On the server,** detect that the client disconnected, typically through the request's abort signal, and abort the upstream request to the model provider.
- **Provide a "Stop generating" button** for long responses.

For long outputs, cancellation can noticeably reduce AI costs.

## Timeouts and Limits

Serverless functions have execution limits, and long generations can approach them. Plan for it:

- **Know your platform's limits** for function duration and response streaming, and choose plans or runtimes accordingly.
- **Cap output length** with the model's maximum tokens parameter.
- **Set a server-side timeout** and end the stream gracefully with an explanatory message if it is exceeded.
- **For very long tasks,** such as analysing large document sets, use a background job and show progress instead of a single long stream.

## Saving the Result

Streaming is about display; persistence is about the database. Decide when and how the result is stored:

- **Save after completion** in the server function, once the full response has been received, along with metadata such as model, tokens used and duration.
- **Mark incomplete results** if the stream was cancelled or failed, so the interface can show "Response interrupted" and offer a retry.
- **Avoid saving from the client,** where the full text could be manipulated or lost if the user closes the tab.

For chat features, store each message with its role, content, status and token usage, linked to a conversation protected by Row Level Security.

## Errors Mid-Stream

Streams can fail halfway: the provider times out, a rate limit is hit or the network drops. Handle it explicitly:

- **Send an error event** that the client can recognise, rather than silently ending the stream.
- **Keep the partial text visible** with a clear indication that it is incomplete.
- **Offer retry,** ideally without charging the user's credits twice for the failed attempt.
- **Log the failure** with request ID, model and stage for debugging.

## Safe Rendering of Streamed Markdown

Models often produce Markdown, and interfaces render it as formatted text. If you convert Markdown to HTML and insert it into the page without sanitisation, a response containing HTML or script content, possibly triggered by injected instructions in a document, can execute in the user's browser. That is cross-site scripting.

- **Use a Markdown renderer that does not allow raw HTML** by default, or sanitise the generated HTML with a well-maintained sanitiser.
- **Never use `dangerouslySetInnerHTML`** with unsanitised model output.
- **Be careful with links and images,** which can leak data to external servers when rendered. Consider restricting or proxying them.
- **Render incrementally without flicker,** by re-rendering the accumulated text efficiently rather than appending raw fragments.

## Proxies, Buffering and Mobile Networks

Streaming that works locally sometimes arrives all at once in production, because a proxy, CDN or framework buffers the response. Check:

- **Response headers,** such as appropriate cache control and, where relevant, headers that disable buffering at proxies
- **Compression settings,** which can buffer chunks
- **CDN or edge configuration** for the streaming route
- **Behaviour on mobile networks,** where connections may drop and need reconnection or retry

Test streaming through your real production setup, not only in local development.

## Designing the Streaming Experience

Good streaming is also a design question. A few patterns make AI features feel trustworthy rather than chaotic:

- **Show progress immediately.** Display a subtle indicator the moment the request is sent, before the first token arrives, so users know something is happening.
- **Keep the layout stable.** Reserve space for the response and avoid content jumping as text grows, which is particularly noticeable on mobile.
- **Let users stop and edit.** A visible stop button, and the ability to edit the prompt and regenerate, give users control.
- **Distinguish draft from final.** For features that produce documents, such as letters or policies, show the streamed text as a draft until the user accepts it, then save it as part of the record.
- **Indicate sources where relevant.** If the response is based on customer documents, show which documents were used once streaming finishes.
- **Handle long outputs gracefully.** For very long responses, consider streaming section by section with headings, so users can start reading meaningful parts early.

Test these behaviours with real users. Small details, such as whether the page scrolls automatically with new text or lets users scroll back without being pulled down, strongly affect how usable a streaming feature feels.

## Rate Limits and Cost Tracking

- **Rate limit per user and per organisation** on streaming endpoints, to prevent abuse and runaway costs.
- **Record token usage** from the provider's final usage information, available in many streaming APIs at the end of the stream, and store it for billing and analysis.
- **Track cost per feature,** so you know which features drive spending.

Our guide on [usage-based billing for AI features](https://launchstudio.eu/en/blog/usage-based-billing-for-ai-features-with-stripe-meters) explains how token usage can feed into pricing.

## Common Mistakes in AI-Built Apps

**API key in the frontend** to stream directly from the provider.

**No authorisation check** on the data included in prompts.

**No cancellation,** paying for responses nobody sees.

**Saving results from the client.**

**Unsanitised Markdown rendering.**

**Silent failures mid-stream,** leaving users with half an answer and no explanation.

**Buffered responses in production** because of proxy or compression settings.

## How LaunchStudio Helps

LaunchStudio implements and hardens streaming AI features in AI-built apps: server-side streaming functions with authentication and permission checks, cancellation end to end, timeouts and output limits, persistence of complete and partial results, error events and retries, safe Markdown rendering, production proxy and CDN configuration, rate limits and token usage tracking.

The **Launch Ready** package (€800-€3,500) covers review and fixes of existing AI features along with security hardening and deployment; **Launch & Grow** (€2,500-€7,500 plus €49 per month) adds managed hosting, monitoring and priority support. Use the [price calculator](https://launchstudio.eu/en/#calculator) for an estimate.

LaunchStudio is backed by Manifera, a software development company with 11+ years of experience, 160+ delivered projects and 120+ engineers. Founders meet the team at Herengracht 420 in Amsterdam; engineering happens at the development centre on Pho Quang Street in Ho Chi Minh City, with a hub on Tras Street in Singapore. For provider selection, see our guide on [choosing an LLM API for an EU SaaS](https://launchstudio.eu/en/blog/choosing-an-llm-api-for-an-eu-saas-openai-anthropic-or-mistral).

## Real example

### An AI-Native Founder in Action: The Policy Assistant That Kept Writing After Users Left

Sarah Lindeman built Beleidsassistent with Lovable and Supabase: an assistant that helps HR managers at small and medium companies draft and explain workplace policies, such as leave, remote work and expenses, based on Dutch employment rules and the company's own handbook. Responses streamed nicely in the browser, and customers liked the feel.

Then the AI bill arrived. A review found the reasons. The frontend called the model provider directly with an API key embedded in the bundle, which was rotated immediately. Streams continued to completion even when users navigated away, and long policy drafts were often abandoned halfway. The prompt included the company handbook loaded by ID from a client parameter using a privileged key, so any user could reference another company's handbook. Responses were saved from the browser after streaming, so closed tabs left conversations without answers. The Markdown renderer allowed raw HTML, and in production behind the CDN, streams sometimes arrived all at once after twenty seconds.

LaunchStudio moved all AI calls into a Supabase edge function that verified the session, loaded the handbook with the user's identity so Row Level Security applied, and checked monthly usage limits. The function streamed server-sent events to the client, propagated cancellation from the client's abort signal to the provider request and capped output length. Final responses, token usage and status were saved server-side, interrupted responses were marked and could be retried without consuming extra credits, and error events were sent explicitly. Markdown rendering moved to a renderer without raw HTML, the streaming route's CDN and compression settings were adjusted, and rate limits applied per user and per company.

**Result:** AI costs fell by roughly 45% in the first month, mainly through cancellation and output caps, while usage continued to grow. First tokens now appear in under a second in production, and the cross-company handbook exposure was closed before any customer noticed.

> *"Streaming made the assistant feel magical. It also made it very easy to pay for answers nobody was reading, and to show the wrong company's handbook."*
> - **Sarah Lindeman, Founder, Beleidsassistent (Utrecht)**

**Cost & Timeline:** €3,100 (Launch Ready package: server-side streaming, authorisation, cancellation, persistence, safe rendering, CDN configuration and rate limits) - completed in 8 business days.

## Frequently Asked Questions

### Can I stream AI responses directly from the browser to the model provider?

You should not with your own API key, because anyone can extract it from the frontend. Stream through a server-side function that authenticates users, controls prompts and data, and holds the key securely.

### Do Supabase edge functions support streaming?

Yes. Edge functions can return streaming responses, which lets you forward tokens from a model provider to the browser as they arrive. Check platform limits on execution time and plan for long generations with output caps or background jobs.

### How do I stop paying for AI responses users abandon?

Cancel end to end: abort the client request when users stop or leave, detect the disconnection in your server function and abort the upstream request to the model provider. Combine with output length limits.

### How does Manifera's experience help with AI streaming features?

Manifera has built real-time and streaming systems for enterprise clients for 11+ years. LaunchStudio applies that experience to AI streaming, covering the security, cost and reliability details that generated code typically misses.

### Does streaming affect SEO or AI visibility?

Not directly, since streaming features usually live behind logins. They improve perceived speed and user satisfaction, which supports reviews and retention. Keep public content server-rendered and independent of streaming for search engines and AI crawlers.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Can I stream AI responses directly from the browser to the model provider?",
      "acceptedAnswer": { "@type": "Answer", "text": "Not with your own API key; stream through an authenticated server function that holds the key." }
    },
    {
      "@type": "Question",
      "name": "Do Supabase edge functions support streaming?",
      "acceptedAnswer": { "@type": "Answer", "text": "Yes; plan for execution limits with output caps or background jobs." }
    },
    {
      "@type": "Question",
      "name": "How do I stop paying for AI responses users abandon?",
      "acceptedAnswer": { "@type": "Answer", "text": "Cancel end to end from client to provider and cap output length." }
    },
    {
      "@type": "Question",
      "name": "How does Manifera's experience help with AI streaming features?",
      "acceptedAnswer": { "@type": "Answer", "text": "Manifera has built enterprise streaming systems for 11+ years, covering security, cost and reliability details." }
    },
    {
      "@type": "Question",
      "name": "Does streaming affect SEO or AI visibility?",
      "acceptedAnswer": { "@type": "Answer", "text": "Not directly; it improves satisfaction, while public content should stay server-rendered." }
    }
  ]
}
</script>
