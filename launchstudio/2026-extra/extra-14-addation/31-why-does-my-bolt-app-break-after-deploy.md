---
Title: "Why Does My Bolt App Break After Deploy? Seven Causes and Fixes"
Keywords: bolt app break after deploy, bolt.new deploy error, bolt netlify 404, bolt app not working production, LaunchStudio, Manifera
Buyer Stage: Awareness
Target Persona: Technical Solo Founder / Indie Hacker
---

# Why Does My Bolt App Break After Deploy? Seven Causes and Fixes

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Why Does My Bolt App Break After Deploy? Seven Causes and Fixes",
  "description": "A Bolt app that works in the preview and breaks after deploy almost always has one of seven causes: missing environment variables, SPA routing, case-sensitive imports, Node-only code, auth redirect URLs, CORS or build differences. Each is explained with a fix.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-02-08",
  "inLanguage": "en",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/why-does-my-bolt-app-break-after-deploy" }
}
</script>

**Short answer:** because Bolt's preview runs in a browser-based environment that is more forgiving than a real server. The seven most common causes are missing environment variables, single-page app routing on the host, file name case mismatches, code that relies on Node-only features, authentication redirect URLs still pointing to the preview, cross-origin (CORS) restrictions and differences between the dev server and the production build. Each has a quick diagnosis and a known fix.

## 1. Missing or Misnamed Environment Variables

**Symptom:** blank screen, "undefined" in API URLs, Supabase or Stripe errors right after loading.
**Why:** variables set in Bolt's session or a local `.env` file were never added to the host. With Vite, only variables starting with `VITE_` are exposed to the browser code, and they are inlined at build time.
**Fix:** add every required variable in the host's settings (Netlify, Vercel), with the correct prefix for frontend variables, then rebuild. Never put secret keys in `VITE_` variables.

## 2. Page Not Found When Refreshing a Route

**Symptom:** the home page works, but refreshing `/dashboard` or opening a shared link shows a 404.
**Why:** the host looks for a file at that path. In a single-page app, all routes must be served by `index.html`.
**Fix:** add a rewrite rule. On Netlify, a `_redirects` file with `/* /index.html 200`. On Vercel, a rewrite in `vercel.json`. Frameworks with server rendering handle this differently.

## 3. "Module Not Found" in the Build Log

**Symptom:** the build fails with an import error for a file that clearly exists.
**Why:** the import says `./components/UserCard` but the file is `usercard.tsx`. Some environments forgive case differences; Linux build servers do not.
**Fix:** rename files or imports so the case matches exactly. A lint rule can prevent it from happening again.

## 4. Code That Only Works in Node

**Symptom:** errors like `process is not defined`, `fs` or `Buffer` not available, or server code failing at runtime.
**Why:** code meant for a server ended up in the frontend bundle, or a backend expects a long-running Node server while the host provides static hosting or serverless functions.
**Fix:** move server logic into serverless functions (Netlify Functions, Vercel Functions, Supabase Edge Functions) and keep the frontend free of Node-only APIs. If you need a persistent server, choose a host that runs one.

## 5. Login Works in the Preview but Not in Production

**Symptom:** sign-in redirects back to the preview URL, magic links fail, OAuth shows "redirect URI mismatch".
**Why:** Supabase Auth, Google, GitHub or other providers only allow redirects to URLs you have configured. The production domain was never added.
**Fix:** add the production URL and any preview URLs to the allowed redirect list in Supabase and each OAuth provider. Update the site URL in Supabase.

## 6. API Calls Blocked by CORS

**Symptom:** network errors mentioning CORS, requests to your own API or a third-party API failing only in production.
**Why:** the API allows requests from the preview origin but not from your domain, or a third-party API should not be called from the browser at all.
**Fix:** configure allowed origins on your API or edge functions. For third-party APIs with secret keys, route the call through a server function instead.

## 7. Dev Server vs Production Build Differences

**Symptom:** features behave differently, styles missing, dynamic imports fail.
**Why:** the dev server compiles on demand; the production build optimises, tree-shakes and splits code. Some patterns, such as dynamic import paths built from variables, behave differently.
**Fix:** run the production build locally (`npm run build` then `npm run preview`) before deploying, and fix any warnings.

## Quick Diagnosis Table

| What you see | Look at |
| --- | --- |
| Blank page, console errors about undefined config | Environment variables (1) |
| 404 on refresh or shared links | Rewrites (2) |
| Build fails on an import | File name case (3) |
| `process` / `fs` / `Buffer` errors | Node-only code (4) |
| Login redirects to the wrong place | Auth redirect URLs (5) |
| CORS errors in the console | Allowed origins, server routing (6) |
| Works in dev, odd in build | Production build locally (7) |

## Beyond "It Deploys"

Fixing these gets your Bolt app online. It does not make it production ready: data access rules, secrets on the server, verified payments, staging, backups and monitoring are the next layer. Our [Bolt.new to production service](https://launchstudio.eu/en/blog/bolt-new-app-to-production-fixed-price-launch-service) covers both layers at a fixed price, typically €800-€3,500 for most Bolt apps.

Our engineers have shipped 160+ projects for enterprise clients through Manifera, the software development company behind LaunchStudio, with 11+ years of deployment work on Netlify, Vercel, AWS and Azure. Engineering is based in Ho Chi Minh City, with client contact in Amsterdam and Singapore. See [Manifera's technologies](https://www.manifera.com/about-us/manifera-technologies/). For the Vite details, the official [Vite guide on deploying a static site](https://vite.dev/guide/static-deploy) is a good reference.

## Real example

### An AI-Native Founder in Action: The Museum Tour That Worked Everywhere Except the Museum

Emma Lambrecht, a museum educator in Bruges, built Zaalgids with Bolt: a mobile-friendly audio tour visitors open by scanning a QR code next to each artwork, with text, audio and a small quiz for children. In Bolt's preview it was flawless. On Netlify, it broke in three ways on the first test day.

Every QR code linked directly to a room page, such as `/room/flemish-primitives`, and all of them returned 404, because there was no rewrite rule. After Emma added one by hand, audio files did not load because their storage URL came from an environment variable set only in her Bolt session. And the quiz scores, saved through Supabase, failed because the production domain was missing from Supabase's allowed URLs, which also broke the staff login.

LaunchStudio added Netlify rewrites, configured environment variables per environment, added the production and preview domains to Supabase Auth settings, moved the audio files to a CDN-backed bucket with caching for the museum's weak wifi, and added offline caching for the tour text. A pre-deployment check now runs the production build and tests the QR routes automatically.

**Result:** Zaalgids went live for the museum's summer exhibition. Over twelve weeks, visitors started around 9,600 tours, with audio loading reliably even in the basement galleries.

> *"Every QR code pointed to a page that didn't exist, according to the server. In the preview, it had always existed."*
> - **Emma Lambrecht, Founder, Zaalgids (Bruges)**

**Cost & Timeline:** €1,600 (Launch Ready package: rewrites, environment configuration, auth URLs, CDN audio, offline caching and deploy checks) - completed in 6 business days.

## Frequently Asked Questions

### Why does my Bolt app show a blank page after deployment?

Most often because environment variables are missing on the host, or a JavaScript error occurs at startup. Open the browser console: errors mentioning undefined configuration point to environment variables. Add them in the host's settings with the correct prefix and rebuild.

### How do I fix 404 errors on page refresh in a Bolt app?

Add a rewrite so every route is served by `index.html`. On Netlify, create a `_redirects` file containing `/* /index.html 200`; on Vercel, add a rewrite in `vercel.json`. This applies to single-page apps built with Vite and React Router.

### Should I deploy my Bolt app from Bolt or from GitHub?

For anything beyond a demo, deploy from GitHub through a pipeline. It gives you build logs, previews, environment separation and rollbacks. Bolt's built-in deployment is convenient for quick sharing but offers less control.

### How does Manifera's deployment experience help with Bolt apps?

The seven causes above are standard deployment issues that Manifera's engineers have handled across hosting platforms for 11+ years. LaunchStudio applies that experience to diagnose Bolt deployment failures quickly and set up pipelines that prevent them.

### Do deployment errors affect my search rankings?

Yes. Search engines that crawl 404 pages or blank screens cannot index your content, and broken shared links lose their value. Fixing routing and rendering issues is essential before you invest in content or SEO.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Why does my Bolt app show a blank page after deployment?",
      "acceptedAnswer": { "@type": "Answer", "text": "Usually missing environment variables or a startup JavaScript error. Check the console, add variables on the host with the correct prefix and rebuild." }
    },
    {
      "@type": "Question",
      "name": "How do I fix 404 errors on page refresh in a Bolt app?",
      "acceptedAnswer": { "@type": "Answer", "text": "Add a rewrite serving index.html for all routes: a _redirects file on Netlify or a rewrite in vercel.json on Vercel." }
    },
    {
      "@type": "Question",
      "name": "Should I deploy my Bolt app from Bolt or from GitHub?",
      "acceptedAnswer": { "@type": "Answer", "text": "From GitHub through a pipeline for anything beyond a demo, for build logs, previews, environments and rollbacks." }
    },
    {
      "@type": "Question",
      "name": "How does Manifera's deployment experience help with Bolt apps?",
      "acceptedAnswer": { "@type": "Answer", "text": "These are standard deployment issues Manifera has handled for 11+ years, enabling quick diagnosis and preventive pipelines." }
    },
    {
      "@type": "Question",
      "name": "Do deployment errors affect my search rankings?",
      "acceptedAnswer": { "@type": "Answer", "text": "Yes. 404s and blank screens cannot be indexed and broken links lose value, so fix routing and rendering before investing in SEO." }
    }
  ]
}
</script>
