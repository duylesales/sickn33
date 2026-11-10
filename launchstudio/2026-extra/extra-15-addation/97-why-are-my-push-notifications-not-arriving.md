---
Title: "Why Are My Push Notifications Not Arriving? Web, iOS and Android Explained"
Keywords: push notifications not arriving, web push not working iphone, pwa notifications ios, firebase cloud messaging not delivered, LaunchStudio, Manifera
Buyer Stage: Awareness
Target Persona: AI-Native Founder (Non-Technical)
---

# Why Are My Push Notifications Not Arriving? Web, iOS and Android Explained

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Why Are My Push Notifications Not Arriving? Web, iOS and Android Explained",
  "description": "Push notifications in AI-built apps often work in testing and fail for real users. This guide explains the common causes, from missing permission and iOS home-screen requirements to expired subscriptions, wrong keys, service worker problems, battery savers and Focus modes, and how to build reliable notifications with fallbacks such as email.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-07-23",
  "inLanguage": "en",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/why-are-my-push-notifications-not-arriving" },
  "citation": [
    { "@type": "CreativeWork", "name": "MDN: Push API", "url": "https://developer.mozilla.org/en-US/docs/Web/API/Push_API" },
    { "@type": "CreativeWork", "name": "WebKit: Web Push for Web Apps on iOS and iPadOS", "url": "https://webkit.org/blog/13878/web-push-for-web-apps-on-ios-and-ipados/" },
    { "@type": "CreativeWork", "name": "Firebase Cloud Messaging documentation", "url": "https://firebase.google.com/docs/cloud-messaging" },
    { "@type": "CreativeWork", "name": "web.dev: Push notifications overview", "url": "https://web.dev/articles/push-notifications-overview" }
  ]
}
</script>

**Short answer:** push notifications fail for a handful of reasons. The user never granted permission, or revoked it. On iPhone, web push only works for a web app added to the home screen, on a recent iOS version. Subscriptions expire or change, and the app keeps sending to old ones. The server uses the wrong keys or credentials, or ignores the error responses that say a subscription is gone. The service worker that should display the notification is missing or broken. And the phone's battery saver, Focus mode or notification settings hide what does arrive. Diagnose by checking each step, from permission to delivery, store subscriptions properly, handle errors, and never rely on push alone for anything important.

## Key Takeaways

- **Push is a chain:** permission, subscription, storage, sending, delivery and display. Any broken link stops it.
- **iOS web push** requires the app to be added to the home screen and permission requested after a user action.
- **Subscriptions are not permanent;** the push service tells you when one is gone, and you must remove it.
- **Testing on your own device proves little:** real users have different settings, devices and OS versions.
- **Important messages need a fallback,** such as email or SMS.

## How Push Notifications Work

For web apps and PWAs:

1. The app asks the user for permission.
2. If granted, the browser creates a **subscription** with a unique endpoint at a push service run by Google, Apple or Mozilla.
3. Your app sends that subscription to your server, which stores it for the user.
4. To notify, your server sends a message to the endpoint, signed with your **VAPID keys**.
5. The push service delivers it to the device, where your **service worker** receives it and shows the notification.

Native and React Native apps follow a similar chain with Apple Push Notification service (APNs) and Firebase Cloud Messaging (FCM) tokens instead of web subscriptions.

## Cause 1: No Permission

Many users never see the permission prompt, dismiss it or deny it. Some browsers hide prompts that appear immediately on page load without a user action. Once denied, the site cannot ask again; users must change it in settings.

**Fix:** ask at a meaningful moment, after explaining the benefit ("Get a message when your order is ready"), triggered by a button the user taps. Track how many users grant permission and show a hint in settings for those who denied it.

## Cause 2: iOS Requirements

On iPhone and iPad, web push works only when:

- The device runs iOS 16.4 or later.
- The user has **added the web app to the home screen** and opens it from there.
- Permission is requested in response to a user action inside that home-screen app.
- The web app has a valid manifest.

Users who visit your app in Safari, or in an in-app browser, cannot receive web push at all. Many founders test on Android or desktop, see notifications work and assume iPhone users get them too.

**Fix:** explain to iPhone users how to add the app to the home screen, show the notification option only where it can work, and offer email or SMS as an alternative. If push is central to your product, consider whether a native app is needed; see [PWA or React Native](https://launchstudio.eu/en/blog/pwa-or-react-native-for-an-ai-built-product).

## Cause 3: Stale or Lost Subscriptions

Subscriptions change when users clear browser data, reinstall the app, switch devices or when the browser rotates them. AI-generated code often saves the subscription once at signup, overwrites it with the latest device, or never saves it to the server at all.

**Fix:**

- Store subscriptions in a table linked to the user, **one row per device**.
- Re-check and update the subscription each time the app opens.
- When the push service responds with "gone" or "not found" (HTTP 404 or 410), delete that subscription.
- Remove subscriptions when users log out on a device.

## Cause 4: Server-Side Errors

The server sends messages, but they never leave or are rejected:

- **VAPID keys** were regenerated, so old subscriptions no longer match.
- **APNs or FCM credentials** expired or belong to a different app or environment.
- **The sending code ignores errors,** so failures are invisible.
- **The payload is too large** or incorrectly encrypted.
- **Sending happens in a function that times out** when sending to many users at once. See [why Edge Functions time out](https://launchstudio.eu/en/blog/why-are-my-supabase-edge-functions-timing-out).

**Fix:** keep keys stable and in server secrets, log every send with its response status, retry temporary failures and send in batches through a queue for larger audiences.

## Cause 5: The Service Worker

For web push, the service worker must be registered, active and contain a handler that shows the notification. Problems include a service worker removed or replaced by a later prompt, a handler that receives the message but does not call `showNotification`, or an old service worker still active. Our article on [why users still see the old version](https://launchstudio.eu/en/blog/why-do-users-still-see-the-old-version-after-a-deploy) covers service worker updates.

**Fix:** check registration and the push handler in the browser's Application tab, test with a push sent from DevTools, and use a tested library for service worker management.

## Cause 6: The Device Hides It

Even delivered notifications can be invisible:

- **Focus modes and Do Not Disturb** on iOS and Android.
- **Battery optimisation** on Android, which delays or blocks background activity for some apps.
- **Notification settings** per app or per site turned off.
- **Notification summaries** on iOS bundling messages for later.

**Fix:** these are user settings, but you can help: explain how to allow notifications, use appropriate urgency settings, and avoid sending so many notifications that users switch them off.

## A Diagnosis Table

| Symptom | Likely cause | First check |
| --- | --- | --- |
| No iPhone users receive push | Not added to home screen | How iPhone users open the app |
| Works on your device only | Subscription storage per user | Subscriptions table |
| Stopped for everyone after a change | Keys or credentials changed | Server send logs |
| Stopped for some users over time | Stale subscriptions | 404/410 responses |
| Delivered but not shown | Service worker handler | Application tab, test push |
| Arrives late on Android | Battery optimisation | Device settings |
| Bulk sends fail partway | Function timeout | Batching and queue |

## Build Notifications That Can Be Trusted

- **Log every notification** with recipient, channel and result.
- **Measure delivery:** sent, accepted by push service, clicked.
- **Let users choose channels** per notification type in settings.
- **Fall back to email** for important messages when push is unavailable or not clicked.
- **Never send anything critical by push only,** such as appointment changes, payment issues or security alerts.

Our guide on [automatic reminders from a Supabase app](https://launchstudio.eu/en/blog/how-do-i-send-automatic-reminders-from-a-supabase-app) shows how scheduled notifications fit with email.

## How LaunchStudio Helps

LaunchStudio builds reliable notifications for AI-built apps: permission flows, iOS home-screen guidance, per-device subscription storage, server-side sending with stable keys and error handling, cleanup of expired subscriptions, queued bulk sends, service worker fixes, delivery logging and fallback to email or SMS.

The **Launch Ready** package (€800-€3,500) covers notification fixes, security hardening and deployment; **Launch & Grow** (€2,500-€7,500 plus €49 per month) adds managed hosting, monitoring and priority support. Use the [price calculator](https://launchstudio.eu/en/#calculator) for an estimate.

LaunchStudio is backed by Manifera, a software development company with 11+ years of experience, 160+ delivered projects and 120+ engineers. Founders meet the team at Herengracht 420 in Amsterdam; engineering happens at the development centre on Pho Quang Street in Ho Chi Minh City, with a hub on Tras Street in Singapore.

## Real example

### An AI-Native Founder in Action: The Pick-Up Alerts Only Android Users Got

Lars Visser built Afhaalklaar with Lovable and Supabase: a PWA for bakeries and delis where customers order ahead and receive a notification when their order is ready to collect. Eleven shops used it, and the shop owners' main selling point was "no more queues".

Shop owners noticed that many customers still waited at the counter or came far too late, saying they never got the notification. Lars could not reproduce it on his Android phone. The investigation found that iPhone users, about 60% of customers, mostly ordered from Safari without adding the app to the home screen, so web push could never reach them. The subscription was saved in the user's profile as a single field, so customers using both a laptop and a phone received notifications only on whichever device they had used last. After a prompt regenerated the VAPID keys, all older subscriptions silently stopped working, and the sending function ignored the error responses. Finally, a later prompt had replaced the service worker with a caching-only version without a push handler.

LaunchStudio restored stable VAPID keys in server secrets and added a push handler to a Workbox-based service worker. Subscriptions moved to a table with one row per device, refreshed on each app open and removed on 404 or 410 responses. Every send is logged with its result. Customers now choose at checkout between push and SMS; iPhone users who have not installed the app see a short guide and default to SMS, sent through a Dutch SMS provider. Delivery rates per channel are visible to Lars in a simple dashboard.

**Result:** More than 95% of "order ready" messages now reach customers, by push or SMS. Shop owners reported shorter queues within weeks, and the share of orders collected within 15 minutes of being ready rose from about half to over 80%.

> *"My notification feature worked perfectly, on my phone. For most of my customers' customers, it didn't exist."*
> - **Lars Visser, Founder, Afhaalklaar (Groningen)**

**Cost & Timeline:** €2,000 (Launch Ready package: push fixes, subscription storage, service worker, delivery logging and SMS fallback) - completed in 6 business days.

## Frequently Asked Questions

### Why are my web push notifications not arriving on iPhone?

On iOS, web push only works for web apps added to the home screen on iOS 16.4 or later, with permission requested after a user action. Users who use your app in Safari or in an in-app browser cannot receive web push.

### Why did notifications stop working for users who used to get them?

Subscriptions expire or change, for example after clearing browser data or reinstalling. If keys were changed or the server ignores "gone" responses, notifications silently fail. Refresh subscriptions on app open and remove invalid ones.

### Should I use push notifications or email?

Use both for different purposes. Push is good for timely, short messages to engaged users; email is more reliable and reaches everyone. Important messages should never rely on push alone.

### How does Manifera's experience help with notifications?

Manifera has built messaging and notification systems for web and mobile apps for 11+ years. LaunchStudio applies that experience to make notifications in AI-built apps reliable and measurable.

### Do push notifications affect SEO or AI visibility?

Not directly. They affect engagement and retention, which influence reviews and recommendations, and a well-configured web app manifest also supports a better mobile experience.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Why are my web push notifications not arriving on iPhone?",
      "acceptedAnswer": { "@type": "Answer", "text": "iOS web push requires the web app on the home screen, iOS 16.4+, and permission requested after a user action." }
    },
    {
      "@type": "Question",
      "name": "Why did notifications stop working for users who used to get them?",
      "acceptedAnswer": { "@type": "Answer", "text": "Subscriptions expire or keys change; refresh subscriptions and remove invalid ones." }
    },
    {
      "@type": "Question",
      "name": "Should I use push notifications or email?",
      "acceptedAnswer": { "@type": "Answer", "text": "Use both; never rely on push alone for important messages." }
    },
    {
      "@type": "Question",
      "name": "How does Manifera's experience help with notifications?",
      "acceptedAnswer": { "@type": "Answer", "text": "Manifera has built messaging systems for web and mobile apps for 11+ years." }
    },
    {
      "@type": "Question",
      "name": "Do push notifications affect SEO or AI visibility?",
      "acceptedAnswer": { "@type": "Answer", "text": "Not directly; they affect engagement, reviews and recommendations." }
    }
  ]
}
</script>
