---
Title: "Why Do Users Still See the Old Version After a Deploy? Caching Explained"
Keywords: users see old version after deploy, app not updating after deploy, clear cache react app, service worker old version, LaunchStudio, Manifera
Buyer Stage: Awareness
Target Persona: AI-Native Founder (Non-Technical)
---

# Why Do Users Still See the Old Version After a Deploy? Caching Explained

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Why Do Users Still See the Old Version After a Deploy? Caching Explained",
  "description": "You deployed a fix, but customers still see the old app. This guide explains the caches between your deploy and your users, from browser and CDN caches to service workers in PWAs and open tabs, the cache settings that work for AI-built React apps and how to roll out updates reliably without asking customers to clear their cache.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-07-16",
  "inLanguage": "en",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/why-do-users-still-see-the-old-version-after-a-deploy" },
  "citation": [
    { "@type": "CreativeWork", "name": "MDN: HTTP caching", "url": "https://developer.mozilla.org/en-US/docs/Web/HTTP/Caching" },
    { "@type": "CreativeWork", "name": "web.dev: Service worker lifecycle", "url": "https://web.dev/articles/service-worker-lifecycle" },
    { "@type": "CreativeWork", "name": "Vite: Building for production", "url": "https://vite.dev/guide/build" },
    { "@type": "CreativeWork", "name": "Cloudflare: Purge cache", "url": "https://developers.cloudflare.com/cache/how-to/purge-cache/" }
  ]
}
</script>

**Short answer:** users see an old version after a deploy because a copy of the old files is stored somewhere between your server and their screen: in their browser cache, in a CDN, in a service worker if your app is a PWA, or simply in a tab that has been open since yesterday. The reliable setup is to never cache `index.html` for long, cache versioned JavaScript and CSS files for a long time, update service workers deliberately, and have the app detect a new version and offer a reload. Then a deploy reaches everyone within minutes, without asking anyone to clear their cache.

## Key Takeaways

- **The HTML page is the key:** if `index.html` is cached, the browser keeps loading old JavaScript.
- **Versioned assets can be cached forever** because each build gives them new file names.
- **Service workers in PWAs** are the most stubborn cache and need an explicit update strategy.
- **Open tabs never update by themselves** in a single-page app; the app has to check for new versions.
- **"Clear your cache" is not a deployment strategy.** Fix the headers instead.

## The Caches Between You and Your Users

When you deploy, the new files land on your host. Before a user sees them, the request can be answered by several layers:

1. **The browser's memory:** an open tab keeps running the JavaScript it loaded earlier.
2. **The browser's HTTP cache:** files saved on disk according to the cache headers your host sent.
3. **A service worker:** in PWAs, a script that intercepts requests and can serve a stored copy of the whole app.
4. **A CDN or proxy:** Cloudflare, Vercel's edge network or a company proxy may serve cached copies.

Each layer needs the right rules. Problems arise when one layer holds on to the old HTML.

## How a Modern Build Is Supposed to Work

Vite and similar tools give JavaScript and CSS files names with a content hash, such as `index-a8f3c2.js`. A new build produces new names. The HTML page references the current names.

That leads to a simple rule:

| File | Cache rule | Why |
| --- | --- | --- |
| `index.html` | No long caching; revalidate every time | It must always point to the latest files |
| Hashed JS and CSS | Cache for a year, immutable | Names change when content changes |
| Images with fixed names | Moderate caching, or version them | Avoid serving stale images forever |
| Service worker file | No caching | Browsers must see updates quickly |

If your host caches `index.html` for hours, users keep loading the old hashed files for hours. That is the most common cause of "the fix isn't live yet".

## Cause 1: The HTML Is Cached

Some hosts and many custom server setups apply one long cache rule to everything. Cloudflare in front of your app may also cache HTML if a "cache everything" rule was added for speed.

**Fix:** set `Cache-Control: no-cache` (which means "check with the server before using a stored copy") for HTML, and long immutable caching for hashed assets. If a CDN caches HTML, purge it on each deploy or exclude HTML from the rule. Our guide on [Cloudflare in front of your AI-built app](https://launchstudio.eu/en/blog/cloudflare-in-front-of-your-ai-built-app) covers the rules.

## Cause 2: The Service Worker Serves the Old App

If your app was turned into a PWA, a service worker probably caches the app shell so it loads offline. By default, a new service worker installs in the background but waits until all tabs of the app are closed before taking over. On phones, where apps stay "open" for days, that can mean users run the old version for a long time.

Worse, some AI-generated service workers cache `index.html` with a "cache first" strategy and never check for updates.

**Fix:** use a well-tested library such as Workbox rather than a hand-written worker, check for updates when the app opens, show a "New version available, reload" message and activate the new worker when the user accepts. Never cache the service worker file itself. Our guide on [offline mode for PWAs](https://launchstudio.eu/en/blog/offline-mode-for-pwas-built-with-ai-tools) explains the trade-offs.

## Cause 3: Tabs That Stay Open

A single-page app loads once and then runs. A user who keeps your app open all week never fetches the new HTML. They see the old interface until they reload, and they may call new backend functions with old code.

**Fix:** have the app check a small version file or endpoint periodically, or when the tab regains focus. When the version differs, show a gentle prompt to reload, or reload automatically at a safe moment such as navigation. Handle failed chunk loads, which happen when an old tab requests files from a deleted build, by reloading once. See [why apps show a blank white screen](https://launchstudio.eu/en/blog/why-does-my-app-show-a-blank-white-screen) for that failure.

## Cause 4: The Deploy Did Not Happen Where You Think

Sometimes it is not caching at all:

- The deploy went to a preview URL, not production.
- The build failed and the host kept serving the previous version.
- Environment variables changed but the app was not rebuilt.
- DNS still points to an old host after a migration.

**Fix:** check the host's deployment log, confirm which deployment is assigned to your domain and expose a version number in the app, for example in the footer or settings page, so you can see exactly what a user is running.

## Backend Compatibility

When old frontends keep running, backend changes must tolerate them for a while. If you rename a column or change a function's parameters in the same release, old tabs break.

**Fix:** make backend changes backwards compatible: add before you remove, support old and new parameters for a transition period and remove old paths only after clients have updated. Our guide on [zero-downtime database migrations](https://launchstudio.eu/en/blog/zero-downtime-database-migrations-in-supabase) explains the expand-and-contract pattern.

## A Diagnosis Table

| Symptom | Likely cause | First check |
| --- | --- | --- |
| Old version until a hard refresh | HTML cached | Response headers on `index.html` |
| Old version even after a hard refresh | CDN or service worker | CDN cache rules; Application tab in DevTools |
| Phone app (PWA) stays old for days | Waiting service worker | Service worker update strategy |
| Users with long-open tabs report old bugs | No version check | Version check in the app |
| Nobody sees the change, including you | Deploy did not go live | Host deployment log |
| Errors right after deploy for some users | Old frontend, new backend | Backwards compatibility |

## How to Check What Users Get

- **Open DevTools, Network tab,** reload and look at the `Cache-Control` header on the HTML and JS files.
- **In the Application tab,** look at registered service workers and cache storage.
- **Show the build version** in the app and ask affected users what it says.
- **Use a private window** to see what a first-time visitor receives.

## A Release Routine That Works

1. Deploy to staging and test.
2. Deploy to production; the host serves new HTML immediately.
3. Purge CDN HTML caches if a CDN caches HTML.
4. Open tabs detect the new version and prompt a reload.
5. PWAs show "update available" and activate on acceptance.
6. Keep old asset files available briefly, so old tabs do not crash mid-session.
7. Remove old backend paths only after the transition period.

## How LaunchStudio Helps

LaunchStudio sets up reliable releases for AI-built apps: correct cache headers per file type, CDN rules and purges, service worker update flows for PWAs, in-app version checks, chunk-failure handling, backwards-compatible backend changes and visible version numbers for support.

The **Launch Ready** package (€800-€3,500) covers deployment configuration and release fixes; **Launch & Grow** (€2,500-€7,500 plus €49 per month) adds managed hosting with releases handled for you, monitoring and priority support. Use the [price calculator](https://launchstudio.eu/en/#calculator) for an estimate.

LaunchStudio is backed by Manifera, a software development company with 11+ years of experience, 160+ delivered projects and 120+ engineers. Founders meet the team at Herengracht 420 in Amsterdam; engineering happens at the development centre on Pho Quang Street in Ho Chi Minh City, with a hub on Tras Street in Singapore.

## Real example

### An AI-Native Founder in Action: The Price Fix That Took a Week to Arrive

Noor El Amrani built Marktkraam with Lovable and Supabase: a PWA that market traders use on their phones to record sales, track stock and see daily takings. About 180 traders across several weekly markets used it, most with the app installed on their home screen.

A bug calculated the VAT on some items incorrectly. Noor fixed it with a prompt, deployed within the hour and announced the fix. Five days later, traders were still reporting wrong totals. The investigation found three layers of caching. The PWA's service worker, generated during an earlier prompt, cached `index.html` with a cache-first strategy and never checked for updates, so installed apps kept running the old code. Cloudflare had a "cache everything" rule that also cached HTML for four hours. And the server sent the same one-week cache header for all files.

Because some traders now ran the new version and others the old one, the VAT figures in shared reports were inconsistent, and an older version kept writing the incorrect values into the database.

LaunchStudio replaced the hand-written service worker with a Workbox setup that checks for updates on launch and shows "New version available" with a reload button. HTML now revalidates on every request while hashed assets are cached for a year, and the Cloudflare rule excludes HTML. The app checks a version endpoint when it regains focus. The backend was changed to calculate VAT on the server, so even an outdated client can no longer write wrong totals, and the affected records were recalculated. The current version number now appears in the app's settings.

**Result:** The next release reached over 95% of active traders within a day, without anyone clearing a cache. Totals in shared reports have been consistent since, and Noor now ships fixes knowing when they arrive.

> *"I kept telling traders the fix was live. On their phones, it wasn't. Now I can see exactly which version everyone runs."*
> - **Noor El Amrani, Founder, Marktkraam (Rotterdam)**

**Cost & Timeline:** €1,800 (Launch Ready package: cache headers, service worker update flow, CDN rules, version checks and server-side VAT calculation) - completed in 5 business days.

## Frequently Asked Questions

### Why do my users still see the old version of my app after I deploy?

Because a cached copy of the old files is being served by their browser, a CDN, a service worker or a tab that has been open since before the deploy. Usually the HTML page is cached too long, so it keeps pointing to old JavaScript.

### Should I tell users to clear their cache?

Only as an emergency measure. The lasting fix is correct cache headers, a service worker update strategy and an in-app version check, so updates arrive without user action.

### Why are PWAs harder to update?

A service worker can store the whole app and, by default, waits for all tabs to close before activating a new version. Without an update prompt, installed apps on phones can run old code for days.

### How does Manifera's experience help with releases?

Manifera has run release processes for enterprise web and mobile apps for 11+ years. LaunchStudio applies the same practices to AI-built apps: predictable caching, versioning and backwards-compatible changes.

### Does caching affect SEO or AI visibility?

Yes. Good caching of static assets makes pages faster, which helps search performance, while HTML that revalidates ensures crawlers see current content rather than outdated pages.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Why do my users still see the old version of my app after I deploy?",
      "acceptedAnswer": { "@type": "Answer", "text": "A browser, CDN, service worker or open tab serves cached old files, usually because the HTML is cached too long." }
    },
    {
      "@type": "Question",
      "name": "Should I tell users to clear their cache?",
      "acceptedAnswer": { "@type": "Answer", "text": "Only in emergencies; fix cache headers, service worker updates and add a version check instead." }
    },
    {
      "@type": "Question",
      "name": "Why are PWAs harder to update?",
      "acceptedAnswer": { "@type": "Answer", "text": "Service workers store the app and wait for all tabs to close before activating a new version." }
    },
    {
      "@type": "Question",
      "name": "How does Manifera's experience help with releases?",
      "acceptedAnswer": { "@type": "Answer", "text": "Manifera has run enterprise release processes for 11+ years, with predictable caching and versioning." }
    },
    {
      "@type": "Question",
      "name": "Does caching affect SEO or AI visibility?",
      "acceptedAnswer": { "@type": "Answer", "text": "Yes; cached assets speed up pages and revalidated HTML keeps crawled content current." }
    }
  ]
}
</script>
