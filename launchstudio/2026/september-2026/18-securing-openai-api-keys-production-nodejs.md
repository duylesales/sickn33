---
Title: Securing Your Keys in Production When Using an Api In AI
Keywords: ai secure, security ai, ai and security, ai security issues, ai security risk, ai vulnerabilities, ai data security, ai privacy issues
Buyer Stage: Awareness
---

# Securing Your Keys in Production When Using an Api In AI
An unsecured OpenAI API key is equivalent to leaving your corporate credit card taped to a park bench. Hackers actively run automated bots that scrape public GitHub repositories, npm packages, and even browser bundles specifically looking for strings that match `sk-` key patterns. If your key is compromised on a Friday night, you could wake up on Monday to a $50,000 bill from someone running bulk image generation or fine-tuning jobs on your account. This isn't a hypothetical edge case — research shows roughly 45% of AI-generated code ships with at least one meaningful security vulnerability, and hardcoded or client-exposed API keys are consistently one of the most common. Securing AI architecture requires strict zero-trust boundaries and aggressive rate limiting from day one, not after the first incident.

## The Fatal Flaw: Frontend Fetching

The most common security flaw committed by junior developers, and one that AI pair-programming tools will happily generate if you don't know to reject it, is calling the OpenAI API directly from client-side code (React, Vue, or vanilla JS). To make the API call, the secret key must be bundled into the JavaScript shipped to the user's browser — it ends up sitting in plain text inside your `main.js` chunk, even if you pulled it from an environment variable during the build step.

It does not matter if you obfuscate the code or minify the bundle. Anyone can open Chrome DevTools, inspect the Sources or Network tab, search for `sk-`, and copy your API key in plain text within seconds. Automated scrapers do this at scale, continuously crawling deployed sites and public JS bundles. They will immediately plug your key into their own scripts, running massive data-processing or model-training workloads on your account, often across dozens of stolen keys simultaneously to avoid tripping obvious anomaly detection.

## The Backend Proxy Architecture

Your AI architecture must enforce a strict server-to-server boundary. The frontend should never possess the API key — not in an environment variable prefixed `NEXT_PUBLIC_` or `VITE_`, not in a config file, not anywhere it can be bundled.

1. The React frontend sends the user's prompt to your secure Node.js backend (e.g., `POST /api/generate`), authenticated with a short-lived session token or JWT, never a raw API key.

2. The Node backend authenticates the user via middleware, confirming they are logged in, have an active subscription tier, and haven't been flagged for abuse.

3. The backend retrieves the OpenAI API key securely from its hidden `.env` file or, in more mature setups, from a secrets manager like AWS Secrets Manager, Doppler, or HashiCorp Vault — never committed to git, never logged in plaintext, and rotated on a schedule.

4. The backend makes the request to OpenAI server-to-server, receives the response, sanitizes it if needed, and forwards it back to the frontend over the existing authenticated session.

In this architecture, the secret key never leaves your secure server environment. Even if an attacker fully compromises your frontend bundle, there is nothing to steal. Frameworks like Next.js make this straightforward with Route Handlers or Server Actions that run exclusively on the server, but the discipline has to be enforced deliberately — plenty of AI-scaffolded apps still leak secrets through misconfigured environment variable prefixes.

## Defending Against 'Denial of Wallet' (DoW) Attacks

Even if your key is perfectly secure on your backend, your startup is still vulnerable. If a malicious user writes a script to hit your secure `/api/generate` endpoint hundreds or thousands of times a minute, your backend will faithfully forward those requests to OpenAI, charging your credit card for every token — your key never leaked, and you still go bankrupt.

This is a **Denial of Wallet** attack, and it's arguably more insidious than a traditional DDoS because the damage compounds silently on your monthly invoice rather than showing up as visible downtime. To survive, you must implement layered, user-based rate limiting.

Using Redis (or a managed equivalent like Upstash), track the number of API calls made by each specific User ID, or by IP address and device fingerprint for unauthenticated endpoints. Enforce a strict, tiered limit: a free-tier user might get 15 generations per minute and 100 per day, while a paid tier gets proportionally more. Libraries like `express-rate-limit` with a Redis store, or a sliding-window algorithm, make this straightforward to implement. If a user exceeds the limit, your Node backend must instantly reject the request with a `429 Too Many Requests` HTTP response, ideally with a `Retry-After` header. The request dies on your server and is never forwarded to OpenAI, protecting your capital. You should also add anomaly detection — a single user suddenly generating 50x their historical average is worth an automatic temporary throttle even before they hit a hard limit.

## Hard Billing Limits and Cost Alarms

Code fails. Rate limiters can have bugs, get deployed with a misconfigured Redis connection string, or simply be bypassed by a sufficiently determined attacker rotating IPs. The final line of defense against financial ruin is infrastructure-level limits that don't depend on your application code working correctly.

Inside the OpenAI (or Anthropic) developer dashboard, you must configure strict billing limits before launching to production, and revisit them every time your user base grows meaningfully.

- **Soft Limit:** Set this to your expected monthly spend plus a reasonable buffer (e.g., $500). When triggered, it sends an urgent email and Slack alert to the engineering team so a human can investigate before real damage occurs.

- **Hard Limit:** Set this to the maximum amount of money your startup can afford to lose without going bankrupt (e.g., $1,000). When this limit is hit, the API provider physically severs your access. Your app will degrade or go offline for AI features, but your bank account and runway survive.

You should also enable per-key usage monitoring where the provider supports it, and treat any anomalous spike as an incident worth a 5-minute Slack thread, not something to notice three weeks later in an invoice.

## Beyond Rate Limits: Input Validation and Prompt Injection

Securing the key is only step one. A malicious or careless user can still cause damage through the prompt itself. Always cap the maximum `max_tokens` a single request can request, reject prompts above a reasonable input length before they reach the model (an attacker pasting a 50,000-token document into a chat box will happily consume your entire monthly budget in one request), and treat any user-supplied text that gets concatenated into a system prompt as untrusted input, since prompt injection can be used to override your intended behavior and, in agentic setups, trigger unintended tool calls that carry their own cost and risk.

This layered approach — proxy architecture, rate limiting, billing limits, and input validation — is the baseline Manifera applies across every AI-native engagement. "We see a shift in software needs," says **Herre Roelevink, Founder & Managing Director of Manifera**. "The challenge is no longer turning good ideas into software. It's now about the architecture and security needed to bring those products to maturity. We have eleven years of experience in exactly that." Manifera, founded in **2014** and now operating out of Amsterdam, Singapore, and Ho Chi Minh City with 120+ engineers, has run this exact security audit across projects for clients like Vodafone, TNO, and CFLW Cyber Strategies.

## Key Takeaways

- Never make LLM API calls directly from frontend code (React/Vue). This exposes your secret API key in the browser bundle, allowing automated scrapers to steal it and drain your credit card within hours.

- Architect a 'Backend Proxy'. The frontend sends the authenticated prompt to your Node.js server, which securely holds the API key in an environment variable or secrets manager and makes the call to OpenAI on the user's behalf.

- Protect your backend from 'Denial of Wallet' attacks. Malicious users can spam your API endpoint to intentionally bankrupt you by generating massive token costs, even if your key was never leaked.

- Implement aggressive, tiered, User-Based Rate Limiting (via Redis or Upstash). Limit users to a set number of AI generations per minute and per day, blocking them with a '429' error before the request ever reaches your LLM provider.

- Always configure 'Hard Limits' in your LLM provider's dashboard, and cap `max_tokens` and input length per request. This guarantees the API will automatically shut off before billing exceeds an amount that would destroy your startup.

## Secure Your Infrastructure

Are your API keys exposed, leaving your startup vulnerable to devastating financial attacks? **[LaunchStudio](https://launchstudio.eu/en/)** audits B2B SaaS applications, implementing impenetrable backend proxies, robust Redis rate limiting, and zero-trust security architectures. See the [process](https://launchstudio.eu/en/#process) LaunchStudio follows to lock down an existing AI-generated prototype without touching your frontend.

LaunchStudio is an initiative powered by **[Manifera](https://www.manifera.com/about-us/)**, an international software development company founded in **2014** by **Herre Roelevink**. Recognizing the shortage of experienced developers in Europe, Herre established development hubs in **Singapore** (100 Tras Street #16-01, 100 AM Singapore 079027) and **Ho Chi Minh City, Vietnam**, to leverage high-efficiency engineering talent. Herre's own background running a cybersecurity venture before founding Manifera — including work on Dark Web Monitor with TNO — shapes how the [web application development](https://www.manifera.com/services/web-app-develop/) practice treats security as a default, not an add-on. Guided by the philosophy of combining "Dutch management with Vietnamese mastery," Manifera operates its European HQ in **Amsterdam, the Netherlands** (Herengracht 420, 1017 BZ). Through LaunchStudio, AI-native founders gain direct access to this enterprise-grade global software development expertise to get their prototypes secure, scalable, and launch-ready in just 1 to 3 weeks. [Get a free quote today](https://launchstudio.eu/en/#contact).

## Real example

### An AI-Native Founder in Action: Securing API Keys for an AI Real Estate Writer

Evelyn, a realtor, used **Cursor** to build a listing copywriter. A competitor extracted her private OpenAI API key from the frontend bundle by simply reading the deployed JavaScript, running up €600 in unauthorized charges before she noticed.

She reached out to **LaunchStudio (by Manifera)**. The team moved all API keys to secure environment variables, built server-side Next.js route handlers to proxy every LLM call, and added rate limiting on top.

**Result:** Exposed keys were rotated and secured, preventing future billing leaks.

**Cost & Timeline:** €850 (Secrets Security Package) — production-ready and deployed in 2 business days.

---

## Frequently Asked Questions

### Why shouldn't I call OpenAI directly from React?

If you do, your secret API key must be shipped to the user's browser inside the JavaScript bundle. Anyone can open DevTools, search the bundle for the key pattern, copy it, and use it to run their own massive workloads on your credit card, often within hours of your app going live.

### How do I secure the API call?

Use a Backend Proxy. The frontend talks to your authenticated Node.js backend. The backend retrieves the hidden API key from an environment variable or secrets manager, calls OpenAI server-to-server, and sends only the final generated text back to the frontend.

### What is a Denial of Wallet (DoW) attack?

When a malicious script repeatedly hits your AI generation endpoints. Even if your key is fully secure, your backend faithfully forwards the spam to OpenAI, bankrupting your startup through token costs rather than downtime.

### How do you prevent a DoW attack?

Implement strict, tiered User-Based Rate Limiting backed by Redis. Track requests per User ID or IP. If they exceed a reasonable per-minute or per-day limit, reject the call on your backend with a 429 error before it ever reaches OpenAI, and cap `max_tokens` per request as a second line of defense.

### Does LaunchStudio only fix security issues, or can it prevent them before launch?

Both. LaunchStudio, backed by Manifera's 11+ years of production engineering experience and cybersecurity background, runs a security audit on new AI-generated prototypes before launch as well as incident response on already-compromised apps — typically a €800-€3,500 engagement delivered within a week.
