---
Title: How to Build a White-Label AI Product with Next.js
Keywords: White-Label, AI, Product, Next.js, B2B, Custom, Domains
Buyer Stage: Awareness
---

# How to Build a White-Label AI Product with Next.js

Many B2B software companies want to offer "AI features" to their customers, but they lack the in-house machine learning expertise to build them from scratch. Instead of building, they want to buy. They want to take your perfectly tuned RAG application, slap their own logo on it, put it on their own domain, and sell it to their clients as if they built it themselves. This is the **White-Label** SaaS model. It is incredibly lucrative because you can charge a massive premium for the brand customization. But architecturally, transforming a single Next.js application into a multi-tenant, white-labeled platform requires a specific infrastructure strategy involving Custom Domains, Edge Middleware, and Dynamic Theming.

## The Architectural Challenge

If MegaCorp wants your AI product hosted at `ai.megacorp.com`, you cannot afford to duplicate your entire GitHub repository, spin up a new Vercel project, and manually change the CSS colors. Managing 50 separate codebases for 50 white-label clients will destroy your engineering velocity.

You must serve all 50 clients from **one single Next.js codebase** deployed to a single Vercel project. The application must dynamically change its behavior, logo, and theme based entirely on the URL the user visits.

## 1. Custom Domains and Vercel

The foundation of a white-label product is the Custom Domain API. 

When MegaCorp signs the contract, they point a CNAME record in their DNS settings (`ai.megacorp.com`) to `cname.vercel-dns.com`. 

Your application must programmatically tell Vercel to accept traffic for that domain. You do this using the Vercel REST API:

```typescript
// Add a domain to your Vercel Project programmatically
await fetch(`https://api.vercel.com/v9/projects/${PROJECT_ID}/domains`, {
  method: 'POST',
  headers: { 'Authorization': `Bearer ${VERCEL_API_TOKEN}` },
  body: JSON.stringify({ name: 'ai.megacorp.com' })
});
```
Vercel automatically provisions the SSL certificate and begins routing traffic to your single Next.js app.

## 2. Next.js Edge Middleware (The Traffic Router)

Now that `ai.megacorp.com` hits your app, how does Next.js know to show MegaCorp's logo instead of your default logo? You use Next.js Middleware.

Middleware runs at the edge *before* a request hits your page. It inspects the `Host` header of the incoming request.

```typescript
import { NextResponse } from 'next/server';

export default function middleware(req) {
  const url = req.nextUrl.clone();
  
  // Extract the hostname (e.g., 'ai.megacorp.com')
  const hostname = req.headers.get('host');
  
  // Rewrite the URL to a dynamic route that handles the specific tenant
  // User sees: ai.megacorp.com/dashboard
  // Next.js serves: /_sites/ai.megacorp.com/dashboard
  url.pathname = `/_sites/${hostname}${url.pathname}`;
  
  return NextResponse.rewrite(url);
}
```

This single block of code is the secret to Next.js multi-tenancy. 

## 3. Dynamic Theming and Supabase

Inside your Next.js page component (`app/_sites/[domain]/page.tsx`), you read the domain from the URL parameters. You then query your Supabase database to fetch that specific organization's configuration.

```sql
-- Supabase table: organization_settings
id | domain            | logo_url         | primary_color | ai_model
1  | ai.megacorp.com   | s3://logo_m.png  | #FF0000       | gpt-4
2  | chat.otherco.com  | s3://logo_o.png  | #00FF00       | claude-3
```

You inject the `primary_color` into your Tailwind configuration dynamically using CSS variables (`style={{ '--brand-primary': data.primary_color }}`). Suddenly, the buttons are red for MegaCorp and green for OtherCo.

## 4. White-Labeling the AI Prompts

White-labeling is not just visual; it applies to the AI's behavior. MegaCorp might want the AI agent to refer to itself as "MegaAssist" and adopt a highly formal tone. OtherCo might want a casual tone.

Your database must store a `system_prompt_override` for each domain. When the user executes a query, your backend fetches the specific system prompt linked to their custom domain before calling the LLM API. 

## The LaunchStudio Approach

At LaunchStudio, we help successful AI startups unlock new B2B revenue streams by architecting flawless white-label infrastructure. We implement the Vercel Domains API, the Next.js Edge Middleware routing, and the Supabase dynamic configuration schemas. We transform your single AI application into an engine capable of powering hundreds of custom-branded enterprise platforms from a single codebase.

---

*Ready to sell your AI product as a white-label solution to enterprise clients? LaunchStudio architects multi-tenant, custom-domain infrastructure for Next.js AI SaaS. [Contact us](https://launchstudio.eu/en/).*
