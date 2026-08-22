---
Title: "Securing API Keys in Next.js: Essential AI Security Guidelines for Production"
Keywords: ai security, ai secure, ai security risk, ai vulnerabilities, ai security vulnerabilities, ai data security, ai deployment, ai native
Buyer Stage: Awareness
---

# Securing API Keys in Next.js: Essential AI Security Guidelines for Production

If a hacker steals your Supabase anon key, they can annoy you within the limits of your row-level security policies. If a hacker steals your OpenAI or Anthropic API key, they can bankrupt your startup in under 48 hours. Malicious scripts actively scrape GitHub, npm packages, and public JavaScript bundles searching for exposed `sk-proj-` or `sk-ant-` strings, using stolen keys to run massive automated generation loops, resell access on gray-market Discord servers, or simply burn your credit limit for spite. If you are building an AI product with Next.js, key security is not optional hardening — it is the first thing that must be right.

## The Client-Side Vulnerability

The most devastating mistake a junior developer, or an AI coding assistant left unsupervised, can make is importing the OpenAI SDK directly into a React Client Component and referencing an API key that was set with the `NEXT_PUBLIC_` prefix. The `NEXT_PUBLIC_` prefix explicitly tells Next.js's build process to compile that value directly into the public JavaScript bundle shipped to every visitor's browser.

If your `.env` file contains `NEXT_PUBLIC_OPENAI_API_KEY=sk-proj-...` and a Client Component reads it, you have already been hacked the moment you deploy. Any user can open Chrome DevTools, check the Sources or Network tab, search the bundle for `sk-`, copy your API key, and begin using it globally — often within minutes of your app going live, since automated scanners crawl newly deployed sites specifically looking for this pattern.

**The Fix**: AI provider API keys must never touch the browser, under any circumstance. Remove the `NEXT_PUBLIC_` prefix from your `.env` file entirely for any secret value. API calls must be orchestrated exclusively on the backend, where `process.env` variables without that prefix remain server-only and are never included in the client bundle.

## Architecting Secure API Routes

In Next.js App Router, the secure pattern involves Server Actions or Route Handlers, both of which execute exclusively on the server.

1. The user clicks "Generate" on the frontend (Client Component).
2. The frontend makes an HTTP POST request to your backend (e.g., `/api/generate`), sending only the prompt and any necessary user context — never a credential.
3. Your backend Route Handler (which runs securely on Vercel's or your hosting provider's servers, never in the browser) reads `process.env.OPENAI_API_KEY`.
4. The backend authenticates the request (verifying the user's session), checks their usage quota, calls the AI provider, and securely streams the response back to the frontend.

Because the Node.js environment variables are never exposed to the client bundle, the key remains completely secure regardless of how thoroughly a user inspects your frontend code. This same pattern applies to every third-party secret your app holds — Stripe secret keys, database service-role keys, internal signing secrets — not just AI provider keys specifically.

## The 'Bring Your Own Key' (BYOK) Model

Many bootstrapped AI startups utilize a BYOK model. Instead of paying the AI provider directly and charging users a markup, they ask the user to input their own personal OpenAI or Anthropic API key. The software acts purely as an interface, but the user pays the raw compute cost directly through their own account.

This introduces a different, but equally serious, category of liability. If your Supabase database is breached and you have been storing your users' API keys in plain text, you are directly responsible for the resulting financial damage to every affected user — and depending on your jurisdiction and terms of service, that responsibility can extend well beyond just refunding a subscription fee.

**Encryption at Rest is Mandatory.**

If you ask users for their API key:

- When the user submits the key, your Next.js server must immediately encrypt it using a strong, authenticated algorithm (like AES-256-GCM) with a master server-side secret that is itself never exposed to the application layer beyond the encryption function.
- Save the *encrypted ciphertext* to Supabase, not the raw key, and ideally store the encryption key itself in a dedicated secrets manager (like Vercel's environment variable encryption, AWS KMS, or Supabase Vault) rather than a plain environment variable your whole codebase can read.
- When the user runs a prompt, your server retrieves the ciphertext from Supabase, decrypts it in memory for the duration of the single API call, makes the request to the AI provider, and ensures the decrypted plaintext key is not logged, cached, or retained anywhere after the call completes.

## Rotation, Least Privilege, and Scoped Keys

Beyond encryption, mature key management includes rotation and scoping. Most AI providers now support creating multiple, separately-named API keys per account or project — use a distinct key per environment (development, staging, production) so a leaked development key doesn't compromise production, and rotate production keys on a schedule or immediately after any team member with access leaves. Where the provider supports it, scope keys to the minimum required permission (for example, a key that can only call chat completions but not fine-tuning or account management endpoints), following the same least-privilege principle that governs database roles and cloud IAM policies.

## Setting Hard Limits in OpenAI or Anthropic

Code is written by humans — and increasingly by AI coding assistants — and both make mistakes. You might accidentally push your `.env` file to a public GitHub repository, or an AI pair-programming tool might generate a code sample that echoes a key into a log statement. To protect yourself from a catastrophic financial event regardless of how a leak happens, you must rely on provider-level safeguards as a last line of defense.

Log into your OpenAI or Anthropic API dashboard and set a **Hard Billing Limit**. If you expect your startup to use $50 of credits a month, set a hard limit of $100–150. If your key is stolen and a hacker tries to generate $10,000 of usage, the provider will automatically disable your API access once the limit is hit. Your application will go offline, but your bank account — and your ability to keep operating the business at all — will survive.

This exact category of gap is why security review is a standard part of taking an AI-generated prototype to production. Industry data suggests roughly 45% of AI-generated code ships with at least one exploitable security vulnerability, and an exposed API key from a `NEXT_PUBLIC_`-prefixed environment variable is one of the single most common findings when a prototype built quickly in Lovable, Bolt, Cursor, or v0 gets its first real security audit. Manifera, the company behind LaunchStudio, has been performing exactly this kind of production security hardening since **2014**, with 11+ years of engineering experience across 160+ delivered projects for enterprise clients including Vodafone and TNO (the Netherlands Organisation for Applied Scientific Research). "We see a shift in software needs. The challenge is no longer turning good ideas into software. It's now about the architecture and security needed to bring those products to maturity. We have eleven years of experience in exactly that," says Herre Roelevink, Founder & Managing Director of Manifera. Given that roughly 80% of AI-built projects never make it to a stable production release, an exposed API key discovered post-launch — rather than caught in review — is a disproportionately common reason a promising product's costs spiral before it ever finds product-market fit.

## Key Takeaways

- Never expose AI API keys on the frontend. A secret key prefixed with `NEXT_PUBLIC_` in Next.js is compiled directly into the public JavaScript bundle, visible to anyone who opens Chrome DevTools.
- Always orchestrate AI API calls through secure backend Server Actions or Route Handlers, where environment variables remain server-only and hidden from the client.
- If implementing a 'Bring Your Own Key' (BYOK) model, you must encrypt user API keys with AES-256-GCM before storing them, and keep the master encryption key in a proper secrets manager, not a plain env variable.
- Use separate, scoped API keys per environment (dev/staging/production) and rotate them on a schedule or immediately after team changes, following least-privilege principles.
- Always set a Hard Billing Limit inside your OpenAI or Anthropic dashboard to ensure a stolen key or a runaway code loop cannot bankrupt your company, even if every other safeguard fails.

## Audit Your AI Security

A single exposed key can destroy your business. **LaunchStudio** performs rigorous security audits on Next.js AI applications, implementing robust encryption, key rotation, and backend orchestration to keep your infrastructure safe — typically at around 20% of the cost of a traditional agency audit. [Get a free quote today](https://launchstudio.eu/en/#contact).

LaunchStudio is an initiative powered by **Manifera**, an international software development company founded in **2014** by **Herre Roelevink**. Recognizing the shortage of experienced developers in Europe, Herre established development hubs in **Singapore** and **Ho Chi Minh City, Vietnam**, to leverage high-efficiency engineering talent. Guided by the philosophy of combining "Dutch management with Vietnamese mastery," Manifera operates its European HQ in **Amsterdam, the Netherlands** (Herengracht 420, 1017 BZ). Through LaunchStudio, AI-native founders gain direct access to this enterprise-grade global software development expertise to get their prototypes secure, scalable, and launch-ready in just 1 to 3 weeks. Learn more about Manifera's approach on its [about page](https://www.manifera.com/about-us/).

## Real example

### An AI-Native Founder in Action: Securing Exposed Anthropic Keys in an AI Copywriter

Evelyn, a content marketer, used **Bolt** to build a copywriting assistant. A user found her private Anthropic API key exposed in the browser's JavaScript bundle.

She worked with **LaunchStudio (by Manifera)**. The team moved all API operations to serverless Route Handlers and secured keys in Vercel environment variables.

**Result:** Private API keys were hidden from the client, securing her billing from unauthorized access.

**Cost & Timeline:** €850 (Secrets Protection Package) — production-ready and deployed in 2 business days.

---

## Frequently Asked Questions

### How does an API key get stolen?

The most common ways are pushing the key to a public GitHub repository, or executing the AI provider call on the client-side React code with a `NEXT_PUBLIC_` prefix, allowing anyone to find the key in their browser's JavaScript bundle.

### What is the NEXT_PUBLIC_ prefix?

In Next.js, any environment variable starting with `NEXT_PUBLIC_` is bundled directly into the public JavaScript sent to every visitor's browser. Never use this prefix for secret API keys or any other credential.

### How do I secure an OpenAI or Anthropic call in Next.js?

Use Server Actions or Route Handlers. The frontend sends only the prompt to your backend. The backend reads the secure, non-prefixed environment variable, calls the AI provider, and returns the result to the frontend — the key itself never leaves the server.

### How do I securely store a user's API key in a BYOK model?

Never store it in plain text in your database. Encrypt the API key with AES-256-GCM on your server before writing it to Supabase, keep the encryption key in a dedicated secrets manager, and decrypt it only in memory for the duration of the API call.

### Is a Next.js security audit something LaunchStudio does on its own, or is that a Manifera service?

LaunchStudio is Manifera's productized offering specifically for AI-native founders — a security audit and hardening pass on an existing Lovable, Bolt, Cursor, or v0 prototype is exactly the kind of fixed-scope engagement LaunchStudio runs. It draws directly on Manifera's 11+ years of production security experience, the same expertise the company applies to its enterprise [custom software development](https://www.manifera.com/services/custom-software-development/) work.
