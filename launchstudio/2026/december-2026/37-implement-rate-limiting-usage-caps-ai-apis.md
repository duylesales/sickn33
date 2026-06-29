---
Title: How to Implement Rate Limiting and Usage Caps for AI APIs
Keywords: Rate, Limiting, Usage, Caps, AI, APIs, Upstash, Redis
Buyer Stage: Consideration
---

# How to Implement Rate Limiting and Usage Caps for AI APIs

An unprotected AI API endpoint is a blank check signed with your corporate credit card. If a malicious user discovers your `/api/generate-report` endpoint and hits it with a simple `while(true)` loop, they can rack up $10,000 in OpenAI fees over a single weekend. Even non-malicious users can accidentally bankrupt you by getting stuck in an infinite retry loop on the frontend. The defense mechanism against this is **Rate Limiting and Usage Caps**. For Next.js AI applications, implementing this at the edge using Upstash Redis is the industry standard for preventing API abuse.

## Rate Limiting vs. Usage Caps

It is critical to understand that these are two different defense mechanisms, and your AI SaaS needs both:

**1. Rate Limiting (The Throttle):** 
Prevents abuse in the short term. "User A can only make 5 AI requests per minute." If they make 6, the API returns a `429 Too Many Requests` error. This stops botnets and accidental `useEffect` infinite loops from hammering your server.

**2. Usage Caps (The Budget):**
Prevents abuse in the long term. "User A can only consume 100,000 tokens per month on their current billing plan." If they hit the limit on day 5, they are locked out until they upgrade or the month resets.

## Implementing Edge Rate Limiting with Upstash

You do not want a blocked request to even reach your Next.js API route, let alone your database. The check must happen at the "Edge" (the Vercel CDN node closest to the user) to be fast and cheap.

**Upstash Redis** is a serverless Redis database that pairs perfectly with Vercel Edge Middleware. They provide a library specifically for this: `@upstash/ratelimit`.

### The Middleware Implementation

```typescript
import { Ratelimit } from '@upstash/ratelimit';
import { Redis } from '@upstash/redis';
import { NextResponse } from 'next/server';

// Create a new ratelimiter, allowing 5 requests per 1 minute
const ratelimit = new Ratelimit({
  redis: Redis.fromEnv(),
  limiter: Ratelimit.slidingWindow(5, '1 m'),
});

export async function middleware(request) {
  // Only apply rate limiting to the AI endpoint
  if (request.nextUrl.pathname.startsWith('/api/ai/')) {
    // Extract the user ID from the JWT or use IP address for public endpoints
    const identifier = request.cookies.get('userId')?.value || request.ip;
    
    const { success } = await ratelimit.limit(identifier);
    
    if (!success) {
      return new NextResponse('Rate limit exceeded', { status: 429 });
    }
  }
  return NextResponse.next();
}
```

This simple middleware executes in single-digit milliseconds. If the user is blocked, the request never reaches your expensive Node.js backend.

## Implementing Token-Aware Usage Caps

Rate limiting counts *requests*. But in AI, 1 request generating a 10-word summary costs a fraction of a cent, while 1 request summarizing a 50-page PDF costs 10 cents. You must also cap by *tokens*.

You cannot do this at the Edge because you do not know how many tokens a prompt will consume until you actually parse it.

**The Backend Implementation:**
1. User clicks "Generate".
2. The request passes the Edge Rate Limit (they haven't made 5 requests this minute).
3. The request hits your API Route.
4. **The Check:** You query Supabase: `SELECT tokens_used, token_limit FROM users WHERE id = X`.
5. If `tokens_used > token_limit`, return `402 Payment Required`.
6. If allowed, execute the OpenAI call.
7. **The Deduction:** After OpenAI returns the response, extract the `total_tokens` from the response payload and update Supabase: `UPDATE users SET tokens_used = tokens_used + X WHERE id = Y`.

*Crucial Architecture Note:* Always use Postgres RPC functions or transactions to update the token count. Do not read the value in Node.js, add the tokens, and write it back. This creates race conditions where simultaneous requests will overwrite each other's token counts.

## Dynamic Limits Based on Billing Tiers

Hardcoding "5 requests per minute" is fine for a free tier, but your Enterprise customers paying $1,000/month will be furious if they hit that limit. 

Your Edge Middleware should dynamically adjust the rate limit based on the user's tier. You can store a mapping of `userId -> tier` in Upstash Redis, allowing the middleware to instantly look up the user's tier and apply a `slidingWindow(100, '1 m')` limit for Enterprise accounts.

## The LaunchStudio Approach

At LaunchStudio, we treat API security as an existential requirement, not an afterthought. For every AI SaaS we deploy, we implement a dual-layer defense system: Upstash Redis rate limiting at the Vercel Edge to block DoS attacks, combined with strict token-aware usage caps enforced by Supabase Postgres transactions. We ensure your AI product generates revenue, not run-away API bills.

---

*Worried about API abuse bankrupting your startup? LaunchStudio implements robust rate limiting and usage cap architectures for Next.js AI applications. [Secure your APIs today](https://launchstudio.eu/en/).*
