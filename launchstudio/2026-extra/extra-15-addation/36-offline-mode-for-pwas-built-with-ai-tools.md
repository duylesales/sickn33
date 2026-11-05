---
Title: "Offline Mode for PWAs Built With AI Tools"
Keywords: offline pwa lovable, offline first web app, service worker caching strategy, indexeddb sync conflicts, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: AI-Native Founder (Non-Technical)
---

# Offline Mode for PWAs Built With AI Tools

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Offline Mode for PWAs Built With AI Tools",
  "description": "Field workers, inspectors, drivers and event staff often lose connection exactly when they need an app most. This guide explains how to add offline support to a progressive web app built with Lovable, Bolt or v0: service workers, caching strategies, local storage in IndexedDB, sync queues, conflict handling, iOS limitations, security of offline data and testing.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-05-23",
  "inLanguage": "en",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/offline-mode-for-pwas-built-with-ai-tools" },
  "citation": [
    { "@type": "CreativeWork", "name": "MDN: Progressive web apps", "url": "https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps" },
    { "@type": "CreativeWork", "name": "MDN: Service Worker API", "url": "https://developer.mozilla.org/en-US/docs/Web/API/Service_Worker_API" },
    { "@type": "CreativeWork", "name": "web.dev: Storage for the web", "url": "https://web.dev/articles/storage-for-the-web" },
    { "@type": "CreativeWork", "name": "Workbox documentation", "url": "https://developer.chrome.com/docs/workbox" }
  ]
}
</script>

Many of the most useful business apps are used in places with bad connectivity. Inspectors walk through basements and parking garages. Installers work in new buildings without Wi-Fi. Delivery drivers pass through rural areas. Event staff scan tickets in crowded venues where the mobile network collapses. Farmers record data in fields and barns. For these users, an app that shows a spinner whenever the signal drops is not a minor inconvenience; it is unusable.

AI builders produce web apps that assume a constant connection. Every screen fetches data from Supabase or an API on load, every save is sent immediately, and the first time the network disappears, work is lost. Turning such an app into a progressive web app with reliable offline support is very achievable, but it requires deliberate design decisions that no prompt makes automatically.

This guide explains those decisions and how to implement them.

## Key Takeaways

- **Offline support has levels:** from simply loading the app shell offline, to reading cached data, to creating and editing data offline with later synchronisation.
- **Service workers cache the app itself; IndexedDB stores data.** Both are needed for real offline use.
- **A sync queue sends offline changes when the connection returns,** with retries and clear status for users.
- **Conflicts are inevitable** when several people edit the same data offline. Decide how to resolve them before building.
- **Offline data is data on a device.** Protect it, limit it and clear it on logout.

## Decide Which Level of Offline You Need

| Level | What works offline | Effort | Example use |
| --- | --- | --- | --- |
| 1. App shell | The app opens and shows a friendly offline message | Low | Any PWA, minimum standard |
| 2. Read-only cache | Recently viewed data is available to read | Moderate | Reference information, schedules, contact lists |
| 3. Offline capture | New records can be created and are synced later | Significant | Inspection reports, delivery confirmations, timesheets |
| 4. Full offline editing | Existing records can be edited offline with sync and conflict handling | High | Collaborative field work, complex forms |

Most field apps need level 3 for a few key workflows and level 2 for reference data. Level 4 everywhere is rarely necessary and adds considerable complexity. Be specific: "inspectors must be able to complete and photograph an inspection checklist without connection" is a buildable requirement; "the app should work offline" is not.

## Service Workers and Caching Strategies

A service worker is a script the browser runs in the background, between your app and the network. It can intercept requests and serve responses from a cache. For PWAs built with Vite, which most Lovable and Bolt projects use, plugins such as `vite-plugin-pwa`, built on Google's Workbox library, generate a service worker and manifest with sensible defaults.

Different resources need different strategies:

| Resource | Strategy | Why |
| --- | --- | --- |
| App shell: HTML, JavaScript, CSS, icons | Precache at install, update in background | The app must open instantly, even offline |
| Images and static assets | Cache first | Rarely change, expensive to download |
| API reads for reference data | Stale while revalidate | Show cached data instantly, refresh when possible |
| API reads for critical live data | Network first, fall back to cache | Prefer fresh data, but show something offline |
| Writes | Never cached; queued in IndexedDB | Writes must reach the server eventually, not be replayed from a cache |
| Authentication endpoints | Network only | Never cache tokens or sign-in responses |

Updates need care. When you release a new version, users with the old service worker should receive the update without breaking their session. A common pattern is to show "A new version is available, refresh" and activate the new worker on confirmation, especially if there is unsynced offline data.

## Storing Data Locally With IndexedDB

The browser's IndexedDB is the right place for offline data: it handles structured records and large amounts of data, unlike localStorage, which is small and synchronous. Libraries such as Dexie make it far easier to use.

A typical design keeps three kinds of local data:

1. **Reference data** downloaded for offline use, such as the inspector's assigned locations and checklist templates for the next few days
2. **Local records** created or edited offline, each with a local ID, status and timestamps
3. **A sync queue** of pending operations to send to the server

Download only what the user needs. An inspector needs today's and tomorrow's assignments, not every inspection in the company's history.

## The Sync Queue

When the user saves something offline, the app:

1. Writes the record to IndexedDB with a client-generated ID, for example a UUID
2. Adds an operation to the sync queue, such as "create inspection with this ID and data"
3. Shows the record in the interface immediately, marked as "waiting to sync"

When the connection returns, the app processes the queue in order:

- Sends each operation to the server, including the client-generated ID
- On success, marks the operation complete and updates the record's status
- On temporary failure, retries later with increasing delays
- On permanent failure, such as a validation error, keeps the operation and shows the user what needs fixing

The client-generated ID is what makes this safe. If the app sends the same create operation twice, because a response was lost, the server can recognise the ID and avoid creating a duplicate. That is idempotency, and without it offline sync produces duplicate records.

Background Sync, a browser feature that lets the service worker send queued requests even after the app is closed, is supported in some browsers but not in Safari on iOS. Do not depend on it; process the queue whenever the app is open and online, and use background sync as an enhancement where available.

## Photos and Files Offline

Field apps often capture photos. Store them as blobs in IndexedDB, compress them before storage to save space, and upload them through the queue to private storage. Upload photos separately from the record data, so a large photo does not block the rest of the sync, and link them to the record by ID once uploaded.

Watch storage limits. Browsers allocate storage based on device space and may evict data from sites under storage pressure, unless persistent storage is granted. You can request persistent storage through the Storage API, and you should show users when data is waiting to sync so they do not uninstall or clear the app.

## Conflicts

A conflict occurs when the same record is changed on two devices, or on a device and the server, before syncing. Common strategies:

| Strategy | How it works | Good for |
| --- | --- | --- |
| Avoid conflicts by design | Each record is owned by one person or device at a time | Assigned inspections, personal timesheets |
| Last write wins | The most recent change replaces older ones | Low-value fields, where losing an edit is acceptable |
| Field-level merge | Changes to different fields are combined | Forms where different people edit different sections |
| Manual resolution | The user is shown both versions and chooses | High-value records where data loss is unacceptable |

Avoiding conflicts by design is the most effective approach. If an inspection is assigned to one inspector and locked for others while assigned, most conflicts never happen. Use server-side timestamps or version numbers to detect the remaining ones.

## Authentication Offline

Users must be able to open the app offline, which means you cannot require a fresh sign-in every time. At the same time, offline access should not become a security hole:

- Keep the user signed in with a session that refreshes when online.
- Allow offline use for a limited period after the last successful online authentication, for example several days, then require going online.
- When a user signs out, clear local data, the sync queue and caches after warning about unsynced changes.
- When an account is deactivated on the server, the next sync should fail and the app should clear local data.

## Security of Offline Data

Offline data lives on a phone or tablet that can be lost or stolen. Reduce the risk:

- **Store only what is needed,** for the shortest time needed.
- **Avoid sensitive data offline** where possible, such as full customer histories or health information.
- **Rely on device security,** such as screen locks and encryption, and recommend or require them in company device policies.
- **Clear data on logout** and after successful sync for data that does not need to remain.
- **Keep server-side authorisation strict.** Every synced operation must be checked by Row Level Security or server logic, exactly like online requests. The sync endpoint must never trust that a client "only has data it should".

## Designing the Offline Experience

Technical correctness is only half of offline support. Users need to understand what is happening, or they will lose trust and keep paper backups. Good offline interfaces share a few traits:

- **A clear connection indicator** that is visible but not alarming, for example a small "Offline, changes will sync later" banner.
- **Per-record sync status,** such as "Saved on this device", "Syncing" and "Synced", so users know which work has reached the office.
- **An outbox screen** listing everything waiting to sync, with the option to retry and an explanation of any failures.
- **Warnings before risky actions,** such as signing out or clearing data while items are unsynced.
- **Honest limits,** for example disabling features that genuinely require a connection, like searching the full archive, with a short explanation rather than an error.

Test these screens with the people who will use them, in the places they work. Field staff often have specific needs, such as large touch targets for gloved hands or high contrast for bright sunlight, that matter as much as the sync logic.

## Testing Offline Behaviour

Test with real conditions, not only the browser's offline toggle:

1. Airplane mode during a form submission
2. Weak connection that drops intermittently, using network throttling
3. Closing and reopening the app with unsynced data
4. Two devices editing the same record offline
5. An app update released while unsynced data exists
6. Storage nearly full on a device
7. iOS Safari and Android Chrome, both installed as PWAs

## How LaunchStudio Helps

LaunchStudio adds offline capabilities to AI-built PWAs: defining the offline level per workflow, service worker setup with appropriate caching strategies, IndexedDB storage, idempotent sync queues with retries, photo handling, conflict strategies, offline authentication rules, data clearing and server-side authorisation for synced operations. If a PWA is not the right fit, our comparison of [PWA and React Native for AI-built products](https://launchstudio.eu/en/blog/pwa-or-react-native-for-an-ai-built-product) helps decide.

Offline work typically falls within **Launch & Grow** (€2,500-€7,500 plus €49 per month), which also includes managed hosting, monitoring and priority support. Simpler offline improvements, such as app shell caching and read-only reference data, can fit within **Launch Ready** (€800-€3,500). Use the [price calculator](https://launchstudio.eu/en/#calculator) for an estimate.

LaunchStudio is backed by Manifera, a software development company with 11+ years of experience, 160+ delivered projects and 120+ engineers, including mobile and field applications for enterprise clients. Founders meet the team at Herengracht 420 in Amsterdam; engineering happens at the development centre on Pho Quang Street in Ho Chi Minh City, with a hub on Tras Street in Singapore.

## Real example

### An AI-Native Founder in Action: The Roof Inspection App That Lost Reports in Basements

Hendrik Bos, a former roofer turned building inspector, built Dakcontrole with Lovable and Supabase: an app where inspectors complete roof and facade inspection checklists, take photos and generate reports for housing associations. Inspectors loved the interface, but complaints started within weeks: reports disappeared when the connection dropped on rooftops and in stairwells, and some inspectors kept paper notes as backup.

The app saved each checklist item directly to Supabase as it was ticked. When the connection dropped, saves failed silently, and photos taken offline were lost when the app reloaded. There was no service worker, so opening the app without signal showed a browser error. When an inspector retried after reconnecting, duplicate inspections sometimes appeared.

LaunchStudio turned Dakcontrole into a PWA with a precached app shell and stale-while-revalidate caching for checklist templates. Each inspector's assignments for the next three days, with addresses and previous findings, were downloaded to IndexedDB. Inspections were created locally with client-generated UUIDs, photos were compressed and stored as blobs, and a sync queue sent records and photos when online, with retries and a visible status per inspection. Inspections were locked to the assigned inspector to avoid conflicts, the server used the UUIDs to prevent duplicates, Row Level Security checked every synced record, and logout cleared local data after confirming everything had synced.

**Result:** Lost reports stopped entirely. Inspectors completed around 2,800 inspections in the following quarter, many in locations without signal, and the paper backup notes disappeared. Two housing associations cited the reliability when extending their contracts.

> *"On a roof you don't have time to wait for a connection. Now the app waits for the connection instead of my inspectors."*
> - **Hendrik Bos, Founder, Dakcontrole (Deventer)**

**Cost & Timeline:** €5,700 (Launch & Grow package: PWA setup, offline storage and sync queue, photo handling, conflict prevention, offline auth rules and testing) - completed in 15 business days.

## Frequently Asked Questions

### Can a Lovable or Bolt app work offline?

Yes, with additional work. AI builders generate apps that assume a constant connection, but they can be turned into progressive web apps with service workers for the app shell, IndexedDB for local data and a sync queue for changes made offline.

### Does offline mode work on iPhones?

Yes, PWAs installed from Safari support service workers and IndexedDB, but there are limitations. Background Sync is not supported, and storage may be cleared under some conditions. Design the sync queue to run whenever the app is open and online, and show users when data is waiting to sync.

### How do I prevent duplicate records when syncing?

Generate a unique ID on the device when a record is created, send it with the sync request and make the server treat a repeated ID as the same record. This idempotency ensures that retries after lost responses do not create duplicates.

### How does Manifera's experience help with offline apps?

Manifera has built mobile and field applications for enterprise clients for 11+ years, where unreliable connectivity is a normal working condition. LaunchStudio applies that experience to sync design, conflict handling and data security on devices.

### Does a PWA help with search and AI visibility?

A PWA is still a website, so its public pages can be indexed like any other. Offline support itself does not improve rankings, but faster loading through caching and a reliable experience help user satisfaction, and public pages should remain server-rendered for crawlers.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Can a Lovable or Bolt app work offline?",
      "acceptedAnswer": { "@type": "Answer", "text": "Yes, with service workers for the app shell, IndexedDB for local data and a sync queue for offline changes." }
    },
    {
      "@type": "Question",
      "name": "Does offline mode work on iPhones?",
      "acceptedAnswer": { "@type": "Answer", "text": "Yes, installed PWAs support service workers and IndexedDB, but Background Sync is unavailable and storage may be cleared, so sync whenever the app is open and online." }
    },
    {
      "@type": "Question",
      "name": "How do I prevent duplicate records when syncing?",
      "acceptedAnswer": { "@type": "Answer", "text": "Generate a unique ID on the device and have the server treat repeated IDs as the same record, making sync idempotent." }
    },
    {
      "@type": "Question",
      "name": "How does Manifera's experience help with offline apps?",
      "acceptedAnswer": { "@type": "Answer", "text": "Manifera has built field and mobile applications for 11+ years, and LaunchStudio applies that to sync design, conflict handling and on-device data security." }
    },
    {
      "@type": "Question",
      "name": "Does a PWA help with search and AI visibility?",
      "acceptedAnswer": { "@type": "Answer", "text": "Public pages remain indexable; caching improves speed and experience, and public pages should stay server-rendered." }
    }
  ]
}
</script>
