---
Title: Securing Third-Party API Keys in Next.js AI Applications
Keywords: Api In AI, Securing, Third, Party, API, Keys, Next, AI, Applications
Buyer Stage: Awareness
---

# Securing Third-Party API Keys in Next.js AI Applications
If a hacker steals your Supabase URL, they can annoy you. If a hacker steals your OpenAI API key, they can bankrupt your startup in 48 hours. Malicious scripts actively scrape the internet searching for exposed `sk-proj-` strings, using stolen keys to run massive crypto mining operations or generate spam at your expense. If you are building with Next.js, you must architect your security flawlessly.

## The Client-Side Vulnerability

The most devastating mistake a junior developer can make is importing the OpenAI SDK directly into a React Client Component. If your code looks like this:

You have already been hacked. The `NEXT_PUBLIC_` prefix explicitly tells Next.js to compile this secret key into the public JavaScript bundle. Any user can open Chrome DevTools, check the Network tab, copy your API key, and begin using it globally.

**The Fix**: OpenAI API keys must never touch the browser. Remove the `NEXT_PUBLIC_` prefix from your `.env` file. API calls must be orchestrated entirely on the backend.

## Architecting Secure API Routes

In Next.js App Router, the secure pattern involves Server Actions or Route Handlers.

1. The user clicks "Generate" on the frontend (Client Component).

2. The frontend makes an HTTP POST request to your backend (e.g., `/api/generate`).

3. Your backend Route Handler (which runs securely on Vercel's servers) reads the `process.env.OPENAI_API_KEY`.

4. The backend calls OpenAI, retrieves the data, and securely streams it back to the frontend.

Because the Node.js environment variables are never exposed to the client, the key remains completely secure.

## The 'Bring Your Own Key' (BYOK) Model

Many bootstrapped AI startups utilize a BYOK model. Instead of paying OpenAI and charging users a markup, they ask the user to input their own personal OpenAI API key. The software acts as an interface, but the user pays the raw compute cost directly.

This introduces massive liability. If your Supabase database is breached and you have been storing your users' API keys in plain text, you are responsible for the resulting financial damage.

**Encryption at Rest is Mandatory.**

If you ask users for their API key:

- When the user submits the key, your Next.js server must immediately encrypt it using a strong algorithm (like AES-256-GCM) with a master server secret.

- Save the *encrypted cipher* to Supabase, not the raw key.

- When the user runs a prompt, your server retrieves the cipher from Supabase, decrypts it in memory, makes the OpenAI call, and then the decrypted key is cleared from memory.

## Setting Hard Limits in OpenAI

Code is written by humans, and humans make mistakes. You might accidentally push your `.env` file to a public GitHub repository. To protect yourself from a catastrophic financial event, you must rely on provider-level safeguards.

Log into your OpenAI API dashboard and set a **Hard Billing Limit**. If you expect your startup to use $50 of credits a month, set a hard limit of $100. If your key is stolen and a hacker tries to generate $10,000 of data, OpenAI will automatically disable your API access at $100. Your application will go offline, but your bank account will survive.

## Key Takeaways

- Never expose AI API keys on the frontend. A secret key prefixed with `NEXT_PUBLIC_` in Next.js is publicly visible to anyone who opens Chrome DevTools.

- Always orchestrate AI API calls through secure backend Server Actions or Route Handlers, where environment variables remain hidden.

- If implementing a 'Bring Your Own Key' (BYOK) model, you must encrypt user API keys before storing them in your database to prevent massive liability in a breach.

- Never commit your `.env` file to GitHub; ensure it is strictly listed in your `.gitignore` file.

- Always set a Hard Billing Limit inside your OpenAI (or Anthropic) dashboard to ensure a stolen key or a runaway code loop cannot bankrupt your company.

## Audit Your AI Security

A single exposed key can destroy your business. **LaunchStudio** performs rigorous security audits on Next.js AI applications, implementing robust encryption and backend orchestration to keep your infrastructure safe.

LaunchStudio is an initiative powered by **Manifera**, an international software development company founded by **Herre Roelevink**. Recognizing the shortage of experienced developers in Europe, Herre established development hubs in **Singapore** and **Ho Chi Minh City, Vietnam**, to leverage high-efficiency engineering talent. Guided by the philosophy of combining "Dutch management with Vietnamese mastery," Manifera operates its European HQ in **Amsterdam, the Netherlands** (at Herengracht 420). Through LaunchStudio, AI-native founders gain direct access to this enterprise-grade global software development expertise to get their prototypes secure, scalable, and launch-ready in just 1 to 3 weeks. [Get a free quote today](https://launchstudio.eu/en/#contact).

## Real example

### An AI-Native Founder in Action: Securing Exposed Anthropic Keys in an AI Copywriter

Evelyn, a content marketer, used **Bolt** to build a copywriting assistant. A user found her private Anthropic API key exposed in the browser's JavaScript bundle.

She worked with **LaunchStudio (by Manifera)**. The team moved all API operations to serverless Route Handlers and secured keys in Vercel environment variables.

**Result:** Private API keys were hidden from the client, securing her billing from unauthorized access.

**Cost & Timeline:** €850 (Secrets Protection Package) — production-ready and deployed in 2 business days.

---

## FAQ

## Frequently Asked Questions

### How does an API key get stolen?

The most common ways are pushing the key to a public GitHub repository, or executing the OpenAI call on the client-side React code, allowing anyone to find the key in their browser.

### What is the NEXT_PUBLIC_ prefix?

In Next.js, any environment variable starting with 'NEXT_PUBLIC_' is bundled into the public JavaScript. Never use this prefix for secret API keys.

### How do I secure an OpenAI call in Next.js?

Use Server Actions or Route Handlers. The frontend sends the prompt to your backend. The backend reads the secure environment variable, calls OpenAI, and returns the result to the frontend.

### How do I securely store a user's API key?

Never store it in plain text in your database. Encrypt the API key on your server before writing it to Supabase, and decrypt it only in memory when making the API call on their behalf.