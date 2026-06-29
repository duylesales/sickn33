---
Title: Optimizing Vercel Edge Functions for Low-Latency LLM Responses
Keywords: Vercel, Edge Functions, LLM, Latency, Streaming
Buyer Stage: Consideration
---

# Optimizing Vercel Edge Functions for Low-Latency LLM Responses

User experience in AI products is entirely dependent on perceived speed. If a user waits more than 2 seconds for the first token, they assume your app is broken.

## Why Edge Functions?
Traditional Serverless functions (like AWS Lambda or Vercel Node.js runtimes) suffer from cold starts and geographical latency. Edge functions execute globally, close to the user, with virtually zero cold boot time.

## Implementation
When implementing the Vercel AI SDK, force the runtime to the Edge:
```javascript
export const runtime = 'edge';
```
Combined with React Server Components and `streamText`, this architecture guarantees sub-500ms Time-to-First-Byte (TTFB) globally.
