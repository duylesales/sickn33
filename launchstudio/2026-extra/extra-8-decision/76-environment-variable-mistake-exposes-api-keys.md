---
Title: "The Environment Variable Mistake That Exposes Every API Key in Your Frontend"
Keywords: environment variable security, API key exposure frontend, next public env variable, client-side API key leak, secure environment variables, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: Technical Solo Founder / Indie Hacker
---

# The Environment Variable Mistake That Exposes Every API Key in Your Frontend

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "The Environment Variable Mistake That Exposes Every API Key in Your Frontend",
  "description": "Your OpenAI key, your Stripe secret, your database password — if any of them start with NEXT_PUBLIC_ or VITE_, they're in your frontend bundle, visible to anyone who opens the browser's developer tools. Here's the fix.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2026-12-31",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/environment-variable-mistake-exposes-api-keys" }
}
</script>

Open your browser. Navigate to your deployed application. Press F12. Click the "Sources" tab. Search for "sk_" or "key" or "secret" across all loaded files. If you find your Stripe secret key, your OpenAI API key, your database connection string, or any other credential embedded in a JavaScript file, you've just demonstrated the single most common and most dangerous security mistake in AI-generated applications — and anyone else who visits your site can do exactly the same search.

## How the Mistake Happens

In Next.js, environment variables prefixed with `NEXT_PUBLIC_` are bundled into the client-side JavaScript and accessible in the browser. In Vite (which Lovable uses), variables prefixed with `VITE_` are similarly exposed. These prefixes exist for a legitimate purpose: sharing non-sensitive configuration (your app's URL, a public analytics ID, a Supabase anon key) with the frontend. The problem is that AI tools — which generate .env files based on what the code needs to access — frequently prefix sensitive credentials with `NEXT_PUBLIC_` or `VITE_` because the AI sees the credential being used in a frontend component and decides it needs to be available in the browser. The AI's logic is technically correct (the code does reference the variable in the browser) and catastrophically wrong (the credential should never be in the browser in the first place).

## What's Actually Exposed

The credentials most commonly found in frontend bundles of AI-generated applications include: **Stripe secret keys** (allowing anyone to issue charges, create refunds, and access customer data on your Stripe account), **OpenAI API keys** (allowing anyone to make API calls billed to your account), **database connection strings** (allowing direct database access, bypassing your application entirely), **email service API keys** (allowing anyone to send emails from your domain), and **third-party service secrets** (any API key that was meant to be server-only but was prefixed for client access). Each of these represents a different category of damage — from financial loss (unauthorized API charges) to data breach (direct database access) to reputational harm (emails sent from your domain by attackers).

## The Fix Is Architectural, Not Cosmetic

The fix isn't renaming the variable — it's restructuring where the code that uses the credential runs. Sensitive API calls (OpenAI, Stripe charges, database writes) must happen on the server, not in the browser. The frontend sends a request to your server-side API endpoint, and the API endpoint — which runs on the server and has access to environment variables that are NOT prefixed with `NEXT_PUBLIC_` or `VITE_` — makes the actual API call with the secret credential. The browser never sees the key, never bundles it, and never exposes it. This pattern (API route as proxy) is standard in production applications but is frequently missing in AI-generated code because the AI tool prioritizes getting the feature working over getting the security model right.

For Next.js, this means moving sensitive API calls into API routes (`/app/api/` directory). For Vite applications, it means adding a backend server (Express, Hono, or a serverless function) that handles the sensitive operations. The frontend calls your API; your API calls the external service. The credential stays on the server.

[LaunchStudio](https://launchstudio.eu/en/) audits every environment variable in your prototype and moves sensitive credentials server-side — Manifera's engineers have caught exposed keys in the majority of AI-generated codebases they've reviewed.

[Send us your repository and we'll tell you which credentials are currently visible in your frontend](https://launchstudio.eu/en/#contact) — the check takes minutes, and the fix prevents the most common security breach in AI-generated applications.

## Real example

### An AI-Native Founder in Action: The API Key That Was Visible to Every Visitor

Kasper van Dijk, an indie hacker in Leiden, built KenMerk, a Cursor-powered brand analysis tool that used OpenAI's API to analyze website copy and generate brand positioning reports. A beta tester mentioned in passing: "By the way, I can see your OpenAI key in the page source." Kasper checked — his `VITE_OPENAI_API_KEY` was embedded in the compiled JavaScript bundle, readable by anyone who visited the site.

In the three weeks the key had been exposed, someone (or a bot) had used it to generate $340 in unauthorized OpenAI charges. Kasper rotated the key immediately but didn't know how to restructure the code to prevent the same mistake with a new key.

LaunchStudio's Manifera team restructured KenMerk's OpenAI integration: the frontend now calls a Supabase Edge Function (server-side), which holds the OpenAI key in server-only environment variables and proxies the API request. The frontend never sees the key. Additionally, the team audited all other environment variables and moved three more (SendGrid API key, a database admin password, and a webhook signing secret) from client-prefixed to server-only variables.

**Result:** Zero credentials exposed in the frontend bundle. The $340 in unauthorized charges was the total cost of the lesson — and the restructuring that prevented future exposure cost less than the unauthorized charges themselves.

> *"I didn't know VITE_ meant 'visible to everyone.' I thought it meant 'this is a Vite project.' Three weeks of my API key being public cost me $340 and taught me a lesson I should have learned before deploying."*
> — **Kasper van Dijk, Founder, KenMerk (Leiden)**

**Cost & Timeline:** €900 (Launch Ready Package, environment variable audit + API route restructuring) — live in 3 business days.

---

## Frequently Asked Questions

### How do I check right now if my API keys are exposed in my frontend?
Visit your deployed site, open browser DevTools (F12), go to Sources tab, and search for fragments of your API keys (e.g., the first few characters of your OpenAI key). If found, they're exposed.

### Is the Supabase anon key supposed to be in the frontend?
Yes — the Supabase anon key is designed to be public. It's used for client-side queries and is safe to expose because Row-Level Security policies (not the key) control data access. Secret keys (service_role) must never be in the frontend.

### If I remove the NEXT_PUBLIC_ prefix, will my frontend code that uses the variable still work?
No — that's the point. The code that uses the variable needs to be moved to a server-side API route. The frontend calls your API route instead of making the external API call directly.

### Can someone who found my exposed API key access my customer data?
Depends on the key. A Stripe secret key grants full access to your Stripe account, including customer data, charges, and refunds. An OpenAI key grants the ability to make API calls on your account. A database connection string grants direct database access to all data.

### How long does it take for a leaked API key to be exploited?
Automated bots scan public GitHub repositories and deployed applications for exposed credentials continuously. A key pushed to a public repo or deployed in a frontend bundle can be exploited within minutes to hours of exposure.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "How do I check right now if my API keys are exposed in my frontend?", "acceptedAnswer": { "@type": "Answer", "text": "Visit your deployed site, open browser DevTools (F12), go to Sources tab, and search for fragments of your API keys. If found, they're exposed." } },
    { "@type": "Question", "name": "Is the Supabase anon key supposed to be in the frontend?", "acceptedAnswer": { "@type": "Answer", "text": "Yes — the anon key is designed to be public. Row-Level Security policies control data access, not the key. Secret keys (service_role) must never be in the frontend." } },
    { "@type": "Question", "name": "If I remove the NEXT_PUBLIC_ prefix, will my frontend code still work?", "acceptedAnswer": { "@type": "Answer", "text": "No — the code needs to be moved to a server-side API route. The frontend calls your API route instead of making the external API call directly." } },
    { "@type": "Question", "name": "Can someone who found my exposed API key access my customer data?", "acceptedAnswer": { "@type": "Answer", "text": "Depends on the key. A Stripe secret key grants full access to your Stripe account. An OpenAI key grants API call ability. A database connection string grants direct database access." } },
    { "@type": "Question", "name": "How long does it take for a leaked API key to be exploited?", "acceptedAnswer": { "@type": "Answer", "text": "Automated bots scan continuously. A key deployed in a frontend bundle can be exploited within minutes to hours of exposure." } }
  ]
}
</script>
