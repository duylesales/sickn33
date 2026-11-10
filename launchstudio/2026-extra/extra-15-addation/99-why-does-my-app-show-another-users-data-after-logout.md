---
Title: "Why Does My App Show Another User's Data After Logout? Fixing Session Leaks"
Keywords: app shows previous user data after logout, react query cache logout, supabase logout data still visible, shared device data leak, LaunchStudio, Manifera
Buyer Stage: Awareness
Target Persona: AI-Native Founder (Non-Technical)
---

# Why Does My App Show Another User's Data After Logout? Fixing Session Leaks

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Why Does My App Show Another User's Data After Logout? Fixing Session Leaks",
  "description": "When one person logs out and another logs in on the same device, AI-built apps sometimes still show the first person's data. This guide explains why it happens, through client-side caches, local storage, service workers and shared CDN caches, why it is a privacy issue even when the database is secure, and how to clear state properly on logout and account switch.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-07-25",
  "inLanguage": "en",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/why-does-my-app-show-another-users-data-after-logout" },
  "citation": [
    { "@type": "CreativeWork", "name": "OWASP Session Management Cheat Sheet", "url": "https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html" },
    { "@type": "CreativeWork", "name": "MDN: Clear-Site-Data header", "url": "https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Clear-Site-Data" },
    { "@type": "CreativeWork", "name": "TanStack Query: QueryClient clear", "url": "https://tanstack.com/query/latest/docs/reference/QueryClient" },
    { "@type": "CreativeWork", "name": "GDPR Article 32: Security of processing", "url": "https://gdpr-info.eu/art-32-gdpr/" }
  ]
}
</script>

**Short answer:** if a new user briefly or permanently sees the previous user's data after logging in on the same device, the data is coming from the browser, not from a fresh database query. AI-built apps typically cache data in memory with tools like React Query, store profiles or settings in local storage, keep state in global stores and sometimes cache responses in a service worker. Logout signs the user out of Supabase but leaves all of that behind. In rarer, more serious cases, a CDN caches a personalised response and serves it to others. The fix is to clear every client-side cache and store on logout and on account change, key cached data by user, and make sure personalised responses are never cached publicly.

## Key Takeaways

- **Logging out of Supabase does not clear your app's caches.** The app has to do that itself.
- **Shared devices make this a real privacy issue:** family tablets, shop counters, reception desks and shared office laptops.
- **Row Level Security does not help here,** because the data was legitimately fetched by the previous user and is shown from the cache.
- **CDN caching of personalised pages** is the dangerous variant, because it can affect users on different devices.
- **A single, central logout routine** that clears everything is the reliable fix.

## Why It Happens

When a user logs in, the app fetches their data: profile, orders, messages, settings. To keep things fast, it stores that data in several places:

- **Query caches** such as React Query or SWR keep results in memory, keyed by query name.
- **Global state stores** such as Zustand, Redux or React context hold the current user, team and selections.
- **Local storage and session storage** keep settings, drafts, the selected organisation or even whole records between visits.
- **IndexedDB** may hold offline data in PWAs.
- **Service workers** may cache API responses.

On logout, the generated code calls `supabase.auth.signOut()` and navigates to the login page. The session ends, but the caches remain. When the next person logs in, screens render immediately from cached data, sometimes until a refetch replaces it, sometimes indefinitely if the cache key does not change.

## Why It Matters Even Though the Database Is Secure

Founders sometimes dismiss this because Row Level Security protects the database. But the exposure has already happened: the next person sees names, messages, invoices or health information that belongs to someone else. Under the GDPR, showing personal data to an unauthorised person is a personal data breach, regardless of where the data came from. Our guide on [GDPR data breach response](https://launchstudio.eu/en/blog/gdpr-data-breach-response-the-72-hours-for-a-small-saas) explains what to do if it has already happened.

It is especially serious in apps used on shared devices: a tablet at a clinic reception, a till at a shop, a family iPad, a shared laptop in a workshop or a school computer.

## Cause 1: Query Cache Not Cleared

React Query and similar tools cache data under keys such as `['orders']`. After a new login, the same key returns the previous user's orders from memory until the cache decides to refresh.

**Fix:** on logout, call the cache's clear method, for example `queryClient.clear()`, and include the user ID or organisation ID in query keys, such as `['orders', userId]`, so data for different users can never share an entry.

## Cause 2: Local Storage That Outlives the Session

Generated code often saves things in local storage for convenience: the user's profile, the selected team, recent searches, form drafts or a cached dashboard. Local storage persists until explicitly removed.

**Fix:** keep a list of every key the app writes, remove all of them on logout, and avoid storing personal data in local storage at all where possible. If drafts must survive, key them by user ID and delete them for other users.

## Cause 3: Global State Not Reset

A global store holds the "current organisation" or "current customer". After logout and a new login, the store still holds the previous values, and the new user's first queries may even run against the old organisation, returning nothing or, if access rules are weak, the wrong data.

**Fix:** reset all stores to their initial state on logout, and on login, derive the current organisation from the new user's memberships rather than from what was stored before.

## Cause 4: The Page Is Not Reloaded

Single-page apps keep running between logout and the next login. Every in-memory variable, subscription and open connection, such as realtime channels, persists.

**Fix:** besides clearing caches, unsubscribe realtime channels on logout and consider a full page reload after logout, which is the simplest way to guarantee that in-memory state is gone.

## Cause 5: Service Worker and Offline Data

PWAs that cache API responses or keep offline copies in IndexedDB can serve the previous user's data, even after a reload. Our guide on [offline mode for PWAs](https://launchstudio.eu/en/blog/offline-mode-for-pwas-built-with-ai-tools) covers what to store offline.

**Fix:** never cache authenticated API responses in the service worker's shared cache, clear IndexedDB stores on logout and, where appropriate, send a `Clear-Site-Data` header from a logout endpoint.

## Cause 6: CDN or Server Caching of Personal Data

The most dangerous variant: a CDN, proxy or server-side cache stores a personalised response, such as a dashboard rendered on the server or an API response, and serves it to other users. This can affect people on entirely different devices.

It happens when a "cache everything" rule is added for speed, or when server-rendered pages with user data are sent with public cache headers.

**Fix:** personalised responses must have `Cache-Control: private, no-store`, CDN rules must bypass caching for authenticated requests and API routes, and cache keys must never ignore the authorisation. See [Cloudflare in front of your AI-built app](https://launchstudio.eu/en/blog/cloudflare-in-front-of-your-ai-built-app).

## A Logout Routine That Works

Put all of this in one function that every logout path calls, including session expiry and "switch account":

1. Sign out from Supabase.
2. Clear the query cache.
3. Reset all global stores.
4. Remove the app's local and session storage keys.
5. Clear IndexedDB stores with user data.
6. Unsubscribe realtime channels.
7. Reload the app or navigate with a full page load.

Also handle the reverse case: when a different user logs in, check whether any cached data belongs to another user ID and clear it before rendering.

## A Diagnosis Table

| Symptom | Likely cause | First check |
| --- | --- | --- |
| Previous user's data visible briefly after login | Query cache | Logout code, query keys |
| Previous user's data until a reload | Global state or memory | Store reset on logout |
| Previous user's data even after reload | Local storage or IndexedDB | Application tab in DevTools |
| Previous user's data offline | Service worker cache | Cached API responses |
| Other users on other devices see someone's data | CDN or server caching | Cache headers and CDN rules |
| New user sees the old organisation | Stored selection | Organisation derived at login |

## How to Test It

- Log in as user A on a device, browse key screens, log out.
- Log in as user B on the same device without reloading.
- Check every key screen, including dashboards, search history, drafts and settings.
- Repeat after a reload and with the app installed as a PWA.
- Check API response headers for `private` or `no-store` on personalised data.

Add this to your release checklist; it takes ten minutes. Our guide on [testing before launch](https://launchstudio.eu/en/blog/how-do-i-test-my-ai-built-app-before-launch) includes a broader plan.

## How LaunchStudio Helps

LaunchStudio fixes session and cache leaks in AI-built apps: central logout routines, user-scoped cache keys, storage and state cleanup, realtime and offline data handling, cache headers and CDN rules for personalised responses, shared-device testing and GDPR incident support where data has already been exposed.

The **Launch Ready** package (€800-€3,500) covers session and cache fixes along with security hardening and deployment; **Launch & Grow** (€2,500-€7,500 plus €49 per month) adds managed hosting, monitoring and priority support. Use the [price calculator](https://launchstudio.eu/en/#calculator) for an estimate.

LaunchStudio is backed by Manifera, a software development company with 11+ years of experience, 160+ delivered projects and 120+ engineers. Founders meet the team at Herengracht 420 in Amsterdam; engineering happens at the development centre on Pho Quang Street in Ho Chi Minh City, with a hub on Tras Street in Singapore.

## Real example

### An AI-Native Founder in Action: The Kiosk Tablet That Remembered the Last Member

Daan Peters built Ledenloket with Lovable and Supabase: a check-in and account app for fitness studios, where members log in on a tablet at the entrance to check in, view their membership and book classes. Nine studios used it, each with a shared tablet at reception, and members also used the app on their own phones.

A member complained that after logging in at the tablet, she saw the previous member's name, membership type and upcoming bookings for several seconds, and once, after tapping quickly, booked a class on the previous member's account. Daan found that logout only called Supabase's sign-out. React Query kept every result under keys without a user ID, the profile and selected studio were stored in local storage, and a global store held the member ID used for bookings until the new profile loaded. On top of that, a Cloudflare rule cached the API route for "today's classes" including a personalised "booked" flag, so members on their phones occasionally saw another member's bookings marked as theirs.

LaunchStudio removed the CDN caching for authenticated routes and set private, no-store headers on all personalised responses. A central logout routine now clears the query cache, resets all stores, removes local storage keys, closes realtime channels and reloads the app. Query keys include the member ID, and the booking action takes the member ID from the server session, not from client state. On the kiosk tablets, the app logs members out automatically after 60 seconds of inactivity. Daan assessed the incident with LaunchStudio's help, documented it as a data breach under the GDPR and informed the affected members.

**Result:** Shared-device tests across all key screens now show no previous-member data. No further complaints were received, and the automatic kiosk logout became a feature studios mention when recommending Ledenloket to others.

> *"My database was locked down properly. The leak was in everything my app remembered after people left."*
> - **Daan Peters, Founder, Ledenloket (Eindhoven)**

**Cost & Timeline:** €1,700 (Launch Ready package: logout routine, cache and state cleanup, CDN and header fixes, kiosk timeout, incident documentation) - completed in 4 business days.

## Frequently Asked Questions

### Why does my app show the previous user's data after logging in?

Because the app shows data from caches in the browser, such as a query cache, local storage or global state, that were not cleared at logout. Supabase's sign-out ends the session but does not clear your app's caches.

### Is it a data breach if the previous user's data is shown?

Showing personal data to someone not authorised to see it is a personal data breach under the GDPR, even if the database itself is secure. Document it and assess whether notification is required.

### Does Row Level Security prevent this?

No. RLS controls what the database returns. Here, the data was fetched legitimately by the previous user and displayed from a cache. Clearing caches on logout and keying them by user prevents it.

### How does Manifera's experience help with session security?

Manifera has built secure business applications for 11+ years, including systems used on shared devices. LaunchStudio applies those session management practices to AI-built apps.

### Can caching personal data affect SEO or AI visibility?

If personalised pages are cached publicly, crawlers may also receive them, exposing data in search indexes. Correct cache headers keep personal data private and public content crawlable.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Why does my app show the previous user's data after logging in?",
      "acceptedAnswer": { "@type": "Answer", "text": "Browser caches such as query caches, local storage or global state were not cleared on logout." }
    },
    {
      "@type": "Question",
      "name": "Is it a data breach if the previous user's data is shown?",
      "acceptedAnswer": { "@type": "Answer", "text": "Yes, showing personal data to an unauthorised person is a personal data breach under the GDPR." }
    },
    {
      "@type": "Question",
      "name": "Does Row Level Security prevent this?",
      "acceptedAnswer": { "@type": "Answer", "text": "No; the data comes from a cache. Clear caches on logout and key them by user." }
    },
    {
      "@type": "Question",
      "name": "How does Manifera's experience help with session security?",
      "acceptedAnswer": { "@type": "Answer", "text": "Manifera has built secure business apps, including shared-device systems, for 11+ years." }
    },
    {
      "@type": "Question",
      "name": "Can caching personal data affect SEO or AI visibility?",
      "acceptedAnswer": { "@type": "Answer", "text": "Publicly cached personal pages can reach crawlers; correct headers keep data private." }
    }
  ]
}
</script>
