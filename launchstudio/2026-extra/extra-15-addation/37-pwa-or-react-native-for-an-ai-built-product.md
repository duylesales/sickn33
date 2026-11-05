---
Title: "PWA or React Native for an AI-Built Product?"
Keywords: pwa vs react native, mobile app for lovable app, expo react native startup, capacitor vs react native, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: AI-Native Founder (Non-Technical)
---

# PWA or React Native for an AI-Built Product?

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "PWA or React Native for an AI-Built Product?",
  "description": "Founders with a web app built in Lovable, Bolt or v0 often want a mobile app next. This guide compares three routes: a progressive web app, wrapping the web app with Capacitor, and building a native app with React Native and Expo. It covers capabilities, app store requirements, push notifications, offline support, cost, maintenance and how to choose.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-05-24",
  "inLanguage": "en",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/pwa-or-react-native-for-an-ai-built-product" },
  "citation": [
    { "@type": "CreativeWork", "name": "MDN: Progressive web apps", "url": "https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps" },
    { "@type": "CreativeWork", "name": "Capacitor documentation", "url": "https://capacitorjs.com/docs" },
    { "@type": "CreativeWork", "name": "Expo documentation", "url": "https://docs.expo.dev/" },
    { "@type": "CreativeWork", "name": "Apple App Store Review Guidelines", "url": "https://developer.apple.com/app-store/review/guidelines/" }
  ]
}
</script>

Once a web app built with AI tools starts working, the next question arrives quickly: "Can we have it in the App Store?" Customers ask for an app icon on their phone. Field users want camera access, offline mode and push notifications. A competitor has an app, so investors ask whether you need one too.

There are three realistic routes for an AI-built product: improve the web app into a progressive web app (PWA), wrap the existing web app in a native shell with a tool like Capacitor, or build a native app with React Native, usually through Expo. Each route has different costs, capabilities and long-term consequences. The right choice depends less on technology and more on what your users actually need on their phones.

This guide compares the three and helps you choose.

## Key Takeaways

- **A PWA is the cheapest route** and often sufficient: installable, works offline, supports push notifications on modern browsers including iOS for installed PWAs, no app store review.
- **Capacitor wraps your existing web app** in a native container, enabling app store distribution and native plugins with little rewriting, but apps that are only a website in a wrapper risk App Store rejection.
- **React Native with Expo produces a genuinely native app,** best for demanding mobile experiences, but it is a separate codebase for the interface.
- **Decide based on required device capabilities, distribution needs and budget,** not on the feeling that "real products have apps".
- **The backend stays the same in all three routes.** A production-ready Supabase backend with proper security serves web and mobile alike.

## The Three Routes at a Glance

| Factor | PWA | Capacitor wrapper | React Native with Expo |
| --- | --- | --- | --- |
| Reuses existing web code | Fully | Almost fully | Logic partly, interface rebuilt |
| App store presence | No (installable from browser) | Yes | Yes |
| App store review | Not applicable | Required | Required |
| Push notifications | Yes, with platform limits | Yes, native | Yes, native |
| Offline support | Yes, via service worker and IndexedDB | Yes | Yes |
| Device features | Camera, location, some sensors | Broad via plugins | Broadest |
| Performance and feel | Web-like | Web-like | Native |
| Typical extra cost | Low | Low to moderate | Moderate to high |
| Maintenance | One codebase | One codebase plus native projects | Separate mobile codebase |

## Route 1: Progressive Web App

A PWA is a website that can be installed on a phone's home screen, opens without browser chrome, works offline through a service worker and can send push notifications. For apps built with Vite, which most Lovable and Bolt projects use, adding PWA support involves a web app manifest, icons, a service worker and some offline design.

**Strengths:**

- One codebase for desktop and mobile
- Updates instantly, without store review
- No app store fees or developer account requirements
- Shareable links work naturally

**Limitations:**

- Not listed in app stores, which matters if customers expect to search there
- On iOS, installation requires users to add the app to the home screen from Safari, which many users do not know how to do
- Push notifications on iOS work for PWAs installed to the home screen on supported iOS versions, with some limitations compared to native apps
- Background processing and some device integrations are restricted

PWAs suit business tools used by known users, such as employees, clients or members, who can be guided to install the app, and products where the web experience is already good on mobile. Our guide on [offline mode for PWAs](https://launchstudio.eu/en/blog/offline-mode-for-pwas-built-with-ai-tools) explains the offline side in detail.

## Route 2: Capacitor Wrapper

Capacitor, maintained by the Ionic team, packages a web app into native iOS and Android projects. The app runs in a native web view, and Capacitor plugins give it access to native features such as the camera, push notifications, file system, biometrics and secure storage.

**Strengths:**

- Reuses nearly all existing web code
- Distribution through the App Store and Google Play
- Native push notifications and broader device access than a PWA
- One team can maintain web and mobile

**Limitations:**

- Performance and feel remain web-like, which is fine for forms and lists but less suitable for animation-heavy interfaces
- Requires Apple and Google developer accounts, native build tooling and store review
- Apple's App Store Review Guidelines expect apps to offer more than a repackaged website. An app that is simply your web app in a wrapper, without native features or app-like experience, risks rejection under the minimum functionality guideline
- Updates to native parts require new store releases

Capacitor is often the best route for AI-built products that need app store presence and a few native capabilities, without the cost of a separate mobile codebase. Our article on [publishing a Lovable app to the App Store](https://launchstudio.eu/en/blog/can-i-publish-my-lovable-app-to-the-app-store) covers the store process.

## Route 3: React Native With Expo

React Native lets you build native mobile apps using React and JavaScript or TypeScript. The interface is rendered with native components, not a web view. Expo is a framework and set of services around React Native that simplifies development, builds and updates considerably, and it is now the most common way to start a React Native project.

**Strengths:**

- Native performance and platform-appropriate interface
- Full access to device features
- Strong ecosystem, including libraries for Supabase, payments and analytics
- Expo's services handle builds, store submissions and over-the-air updates for JavaScript changes within store rules

**Limitations:**

- The interface must be rebuilt; web components from Lovable or v0 do not run directly in React Native
- A second codebase to maintain alongside the web app, unless you also move the web app to a shared approach
- Requires more mobile-specific expertise
- Higher upfront cost

React Native suits products where the mobile experience is central: consumer apps, apps used for long sessions on phones, apps relying heavily on device features or apps where native feel is a competitive factor. Some AI tools can now generate React Native code, which reduces but does not remove the extra work.

## Questions That Decide the Route

**1. Do your users need to find you in an app store?** For consumer products discovered through app stores, yes. For business tools where users are invited by their employer or provider, often not.

**2. Which device features are essential?** List them. Camera and location work in PWAs. Background location tracking, Bluetooth peripherals, advanced biometrics or deep integration with other apps point towards native.

**3. How important are push notifications?** If notifications drive your product's value, such as booking reminders or delivery updates, check platform support carefully. Capacitor and React Native offer the most reliable notifications across platforms.

**4. How much time will users spend in the app on their phones?** Occasional use favours a PWA or wrapper. Hours of daily use favours native.

**5. What is your budget and team?** A PWA can often be delivered in days. A Capacitor app in one to three weeks. A React Native app takes longer, depending on scope.

## A Common Path for AI-Built Products

Many founders take a staged approach:

1. **Make the web app production-ready and mobile-friendly,** with a responsive interface and secure backend.
2. **Add PWA support** so users can install it and use key features offline.
3. **Wrap with Capacitor** when app store presence or native notifications become necessary, adding a few native features to meet store expectations.
4. **Build a React Native app** only when mobile usage and requirements clearly justify a dedicated mobile experience.

This path keeps costs low while the product finds its market, and each stage builds on the previous one rather than replacing it.

## The Backend Matters More Than the Frontend Choice

Whichever route you choose, the mobile app talks to the same backend. That backend must be ready:

- **Row Level Security and server-side authorisation,** because mobile apps can be decompiled and their API calls replayed
- **No secrets in the app bundle,** since anything shipped in a mobile app is extractable
- **Secure token storage** on the device, using platform secure storage rather than plain local storage in native apps
- **API versioning,** because users do not update mobile apps immediately and old versions must keep working for a while
- **Push notification infrastructure** with device token management and opt-in handling
- **Deep links** that open the right screen and respect authentication

Mobile apps make backend weaknesses more visible, not less.

## App Store Practicalities

If you choose Capacitor or React Native, plan for:

- Apple Developer Program and Google Play Console accounts
- Privacy details in both stores, describing data collection accurately
- Review times and occasional rejections, often for missing account deletion, unclear purpose strings for permissions or minimal functionality
- In-app account deletion, which Apple requires for apps that support account creation
- Rules on in-app purchases for digital goods, which may affect how you sell subscriptions inside the app

## Cost of Ownership Over Three Years

The upfront build is only part of the cost. Over three years, maintenance often matters more:

| Cost item | PWA | Capacitor | React Native |
| --- | --- | --- | --- |
| Initial build | Low | Low to moderate | Moderate to high |
| Developer accounts | None | Apple and Google annual and one-time fees | Same |
| Operating system updates | Rarely affect the app | Occasional native project updates | Regular dependency and SDK upgrades |
| Store reviews and releases | None | For native changes | For native changes, plus over-the-air updates for JavaScript |
| Feature development | Once, for all platforms | Once, plus occasional native plugin work | Twice if the web app is maintained separately |
| Testing | Browsers and devices | Browsers, devices and store builds | Devices and store builds, plus web separately |

The biggest hidden cost of a separate native codebase is duplicated feature work. Every new feature has to be designed, built and tested for web and mobile, unless the product moves entirely to mobile. For an early-stage team, that can halve development speed. Choose native when the mobile experience genuinely justifies it, not by default.

## How LaunchStudio Helps

LaunchStudio helps founders choose and execute the right mobile route: making web apps production-ready and mobile-friendly, adding PWA support, wrapping with Capacitor including native features and store submission, and preparing the backend for mobile clients with secure authentication, push infrastructure and API versioning. For full React Native builds, Manifera's mobile teams can take on larger projects.

PWA support usually fits within **Launch Ready** (€800-€3,500). Capacitor apps with store submission typically fit within **Launch & Grow** (€2,500-€7,500 plus €49 per month). Use the [price calculator](https://launchstudio.eu/en/#calculator) for an estimate.

LaunchStudio is backed by Manifera, a software development company with 11+ years of experience, 160+ delivered projects and 120+ engineers, including mobile apps for enterprise clients. Founders meet the team at Herengracht 420 in Amsterdam; engineering happens at the development centre on Pho Quang Street in Ho Chi Minh City, with a hub on Tras Street in Singapore.

## Real example

### An AI-Native Founder in Action: The Dog Walking Service That Did Not Need Native Yet

Sophie Kramer runs a dog walking business in Utrecht and built Uitlaatplanner with Lovable and Supabase: dog owners book walks, walkers check in at pick-up and drop-off with a photo, and owners receive updates. Several customers asked for "a real app", and Sophie received a quote of over €40,000 for native iOS and Android apps.

Before deciding, she asked LaunchStudio for a second opinion. The analysis showed that her needs were check-ins with photos, location at check-in, push notifications for owners and offline resilience for walkers in parks with poor reception. Owners were all existing customers, invited by email, so app store discovery did not matter yet. Meanwhile, the web app itself had problems: the mobile layout was cramped, check-ins failed without signal and photo uploads had no compression.

LaunchStudio improved the mobile interface and added PWA support with a manifest, icons, offline check-ins queued in IndexedDB and compressed photo uploads. Push notifications were implemented for installed PWAs and by email as a fallback, with an install guide sent to customers. For walkers, who needed reliable background notifications for new bookings, the PWA was wrapped with Capacitor, adding native push notifications and camera access and distributed through TestFlight and Google Play internal testing to the walkers only. The backend gained secure token handling, API versioning and push token management.

**Result:** Owners adopted the installed PWA quickly, and walkers used the Capacitor app daily. Missed check-ins dropped to near zero. Sophie spent a fraction of the native quote and postponed a decision on full native apps until a planned expansion to other cities.

> *"I almost spent forty thousand euros on an app my customers didn't need. What they needed was the web app working properly on their phones."*
> - **Sophie Kramer, Founder, Uitlaatplanner (Utrecht)**

**Cost & Timeline:** €4,600 (Launch & Grow package: mobile interface fixes, PWA with offline check-ins, push notifications, Capacitor app for walkers and backend preparation) - completed in 13 business days.

## Frequently Asked Questions

### Is a PWA good enough instead of a native app?

Often, yes, for business tools and services with known users. PWAs can be installed, work offline and send push notifications on modern platforms. Choose native or a wrapper when app store discovery, advanced device features or reliable background notifications are essential.

### Will Apple accept my Lovable app wrapped with Capacitor?

It can, but Apple expects apps to provide more than a repackaged website. Adding native features such as push notifications, camera integration, offline support and an app-like interface improves the chances of approval under the App Store Review Guidelines.

### Can I convert my Lovable app to React Native automatically?

Not directly. Lovable generates web React components that do not run in React Native. Business logic and API calls can often be reused, but the interface needs to be rebuilt with native components, sometimes with help from AI tools that generate React Native code.

### How does Manifera's experience help with mobile decisions?

Manifera has built web and mobile applications for enterprise clients for 11+ years. LaunchStudio uses that experience to match the route to real user needs, often saving founders from expensive native builds that are not yet necessary.

### Does having an app store listing help visibility?

It can, particularly for consumer products, because app stores are search engines in their own right. For business tools, a strong website with clear product information usually matters more for search engines and AI answer engines than an app store listing.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Is a PWA good enough instead of a native app?",
      "acceptedAnswer": { "@type": "Answer", "text": "Often yes for business tools with known users. Choose native or a wrapper when store discovery, advanced device features or reliable background notifications are essential." }
    },
    {
      "@type": "Question",
      "name": "Will Apple accept my Lovable app wrapped with Capacitor?",
      "acceptedAnswer": { "@type": "Answer", "text": "It can, but Apple expects more than a repackaged website; native features and app-like experience improve approval chances." }
    },
    {
      "@type": "Question",
      "name": "Can I convert my Lovable app to React Native automatically?",
      "acceptedAnswer": { "@type": "Answer", "text": "Not directly. Logic and API calls can be reused, but the interface must be rebuilt with native components." }
    },
    {
      "@type": "Question",
      "name": "How does Manifera's experience help with mobile decisions?",
      "acceptedAnswer": { "@type": "Answer", "text": "Manifera has built web and mobile apps for 11+ years, and LaunchStudio matches the route to real user needs." }
    },
    {
      "@type": "Question",
      "name": "Does having an app store listing help visibility?",
      "acceptedAnswer": { "@type": "Answer", "text": "It can for consumer products; for business tools, a strong website matters more for search and AI engines." }
    }
  ]
}
</script>
