---
Title: "Mobile App or Responsive Web: The Decision That Sets Your Budget"
Keywords: mobile app or responsive web, app store review costs, push notification infrastructure, PWA versus native app, mobile app development budget, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: AI-Native Founder (Non-Technical)
---

# Mobile App or Responsive Web: The Decision That Sets Your Budget

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Mobile App or Responsive Web: The Decision That Sets Your Budget",
  "description": "Choosing between an app store release and a responsive web product changes your budget, your release cycle, your commission on every sale and your ongoing maintenance load. This article gives non-technical founders the three questions that actually settle the decision.",
  "author": {
    "@type": "Organization",
    "name": "LaunchStudio",
    "url": "https://launchstudio.eu/en/"
  },
  "publisher": {
    "@type": "Organization",
    "name": "Manifera",
    "url": "https://www.manifera.com"
  },
  "datePublished": "2027-01-15",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://launchstudio.eu/en/blog/mobile-app-or-responsive-web-the-budget-decision"
  }
}
</script>

"So it's an app, right?"

"It's a web app. It works on your phone."

"Yes, but is it in the App Store?"

That exchange happens in some form in nearly every early customer conversation, and a lot of founders resolve it by deciding they need an App Store presence because a customer asked. It's an expensive way to answer a question, because the store isn't a distribution choice with a bit of extra work attached. It's a different budget, a different release cycle, a commission on certain kinds of revenue, and a maintenance commitment that renews every autumn whether your product is growing or not.

Here is what actually changes when you cross that line, and the three questions that settle the decision without guessing.

## The Store Takes a Cut of Some Things and Not Others

If you sell digital goods or subscriptions that are consumed inside an iOS app, Apple's rules generally require you to sell them through in-app purchase, with a commission — 30% standard, 15% under the small-business threshold that most early founders qualify for. Google's Play Store works similarly. If you sell physical goods, services delivered in the real world, or business-to-business software billed outside the app, those rules mostly don't apply and you can keep using your own payment provider.

That distinction is worth real money and founders discover it late. A €19/month consumer subscription sold through the App Store nets you around €16 instead of about €18.40 after normal card fees. On a thousand subscribers that's roughly €2,400 a year, indefinitely, on top of the higher build cost. There is also the developer account overhead — €99 per year for Apple, a one-off $25 for Google — and the review process itself: submissions are typically reviewed within a day or two, but a rejection over metadata, account deletion requirements, sign-in options or payment rules turns a release into a week-long conversation with a reviewer. Nobody plans for the rejection loop, and almost everybody experiences it on their first submission.

## Releasing Stops Being Something You Do Whenever You Like

On the web, you fix a bug and it's fixed for everyone in three minutes. In an app store, you fix a bug, submit, wait for review, release, and then wait for users to update — and some of them never will. This is the change that surprises non-technical founders most, because it reshapes how the product has to be built.

Once old versions exist in the wild, your backend has to keep working for them. That means API changes must stay backwards-compatible, or you need a version check that can politely force an upgrade. It means staged rollouts, so a bad release reaches 5% of users rather than all of them. It means crash reporting, because you can't reproduce a problem on a device you don't own. None of this is exotic, but it is real engineering that a responsive web product simply doesn't need, and it is a permanent part of your operating cost rather than a one-time build item.

## Push Notifications Are Infrastructure, Not a Checkbox

Push is the most common reason founders say they need an app, and it's a legitimate one — but it's worth knowing what it involves. Notifications travel through Apple's and Google's delivery services, which means server credentials for both, a device token stored per installation, handling for tokens that silently become invalid when a user reinstalls or changes device, and a backend that decides what to send, to whom, at what local time, without duplicating. It also means an opt-in prompt that a substantial share of users decline, which is why serious products earn the permission with an explanatory screen before asking rather than firing the system dialog on first launch.

Web push exists and works well on Android and desktop. On iOS it works only when the user has added your site to their home screen first, which is a real friction step for a consumer product and often a non-issue for a business tool your customers use daily. If push is the whole reason for the app, be honest about whether your notifications are ones people would genuinely miss — a reminder that a shift starts in 30 minutes, yes; a weekly engagement nudge, probably not worth a €3,000–€7,500 build.

## What the Web Genuinely Cannot Do

Setting push aside, the honest list of things that still need a real app is shorter than it was but not empty: reliable background location tracking, Bluetooth accessory connections, deep offline use with large local data, biometric unlock tied to the device's secure storage, home-screen widgets, health and fitness data from the phone's own store, and access to certain camera capabilities beyond a simple photo capture. If your core loop depends on one of those, the decision is made, and pretending otherwise wastes a quarter.

There is one more genuine advantage that isn't technical: discovery and trust. Some audiences — older consumers, certain regulated sectors, anything used in the field by people who don't like typing URLs — treat "it's in the App Store" as a legitimacy signal. That's not irrational, and it's a valid reason to choose an app. It's just a marketing reason, and it should be weighed against a marketing budget rather than assumed into a technical requirement.

## The Numbers, Side by Side

On the [LaunchStudio price calculator](https://launchstudio.eu/en/#calculator), a website sits at €800–€2,000 and a mobile app at €3,000–€7,500. The gap isn't arbitrary. An app means a build pipeline for two platforms, store assets and metadata, review submissions, device testing across screen sizes and OS versions, push infrastructure, crash reporting, and a backend that supports old versions. Beyond the build, budget for the maintenance treadmill: Apple and Google both ship major OS versions annually, deprecate APIs, and periodically raise the minimum SDK your app must target to stay listed. An app that receives no feature work at all still needs attention roughly twice a year to remain in the store.

Testing is the line item founders forget entirely. A website is tested in a handful of browsers, and if something looks wrong you fix it that afternoon. An app has to behave on a three-year-old Android phone with a small screen and an older OS version, on the newest iPhone, and on a tablet somebody will inevitably install it on — and the bug that only appears on one of those is the bug you'll hear about in a one-star review rather than an email. Budget for either a device testing service or a small set of real phones, and for the time to actually use them before each release.

A cross-platform framework such as React Native or Flutter genuinely reduces the difference — one codebase covering both platforms, with the store and release overhead still fully present. That is usually the right answer for founders who need an app but don't need platform-specific behaviour, and it's why the app band on the calculator is a range rather than a single number.

## The Middle Path Most Founders Should Take First

There is a sequence that works better than the binary: ship the responsive web product, make it installable to the home screen, and let real usage tell you whether the app is needed. A well-built responsive web app on a modern phone is fast, works offline for cached content, can send push on Android and desktop, updates instantly, costs a fraction to maintain, and can be found through Google — which no app can.

If demand for an app then proves real, you have something valuable: a working backend, a validated interface and actual users to test with. Building the app second is cheaper than building it first, because most of what makes an app work is the API underneath it, and you'll have that. The reverse order — app first, web later — means paying the higher build cost against unvalidated demand and then discovering you also need the web version for SEO and desktop.

## Three Questions That Settle It

**One: does your revenue come from digital goods consumed in the app?** If yes, model the commission before you decide; if no, the store's payment rules mostly don't touch you and one objection disappears.

**Two: does your core loop need something only a real app can do** — background location, Bluetooth, deep offline, biometrics, widgets? If yes, build the app and stop deliberating. If the only answer is push notifications, ask whether your notifications are ones a user would miss if they didn't arrive.

**Three: does your customer expect to find you in a store?** Not "would they like it" — expect it, to the point where its absence costs you the sale. If two of these three are yes, budget for the app. If none are, you are looking at a €800–€2,000 build instead of a €3,000–€7,500 one, and you can revisit the question in six months with real data instead of a hunch.

LaunchStudio takes the prototype you built in Lovable or Bolt and makes it production-ready either way — hardened, deployed and live on your own domain — and where an app genuinely is the answer, that work goes to engineers who have shipped to the stores before rather than a freelancer learning on your budget.

If you're still unsure, price both routes before you commit to either: [run the numbers for a web build and an app build side by side](https://launchstudio.eu/en/#calculator) and see how much the store presence is actually costing you. And if the app wins on the three questions, LaunchStudio's mobile work is delivered by [Manifera](https://www.manifera.com/services/mobile-app-development/), which has been building and maintaining store-listed apps for eleven-plus years.

## Real example

### A Founder in Action: The App That Turned Out to Be a Web Product

Sofie Neefjes built Kwiek in Lovable — a coaching product that helps people rebuild an exercise habit after injury, with daily check-ins and a weekly plan. Every early user asked the same question about the App Store, so Sofie assumed the app was the launch, requested quotes, and was looking at €14,000 from an agency for iOS and Android before she'd validated that anyone would pay for the coaching itself.

The scoping call took the decision apart in twenty minutes. Kwiek's revenue was a €14/month subscription for a digital service, so an iOS release would have routed it through in-app purchase and its commission. The core loop was a form, a plan and a reminder — no Bluetooth, no background location, no offline requirement. The only real app-shaped need was the daily reminder, which on Android and desktop works through web push, and on iOS works once a user adds Kwiek to their home screen, something her onboarding could ask for directly. The build went ahead as a responsive web product with proper authentication, subscription billing through her own payment provider, an installable home-screen setup and a reminder system with authenticated email as the fallback channel.

**Result:** Kwiek launched for a fraction of the app quote and roughly seven weeks earlier, kept the full subscription price instead of the store's share, and — the part Sofie hadn't priced in — began acquiring users through Google searches for injury-recovery routines, a channel an app store listing would not have given her.

> *"I was about to spend fourteen thousand euros to answer a question my customers were asking out of habit. What they wanted was a reminder at 07:30. That's not an App Store problem."*
> — **Sofie Neefjes, Founder, Kwiek (Haarlem)**

**Cost & Timeline:** €1,900 fixed price — authentication, subscription billing, installable setup and reminder delivery — live in 7 business days.

---

## Frequently Asked Questions

### Will Apple really take a commission on my subscription?

Only for digital goods and services consumed inside the app, where in-app purchase is generally required, at 30% or 15% under the small-business threshold most early founders qualify for. Physical products, real-world services and business software billed outside the app typically fall outside those rules, so the answer depends entirely on what you are selling.

### Can a responsive web app send push notifications?

On Android and desktop browsers, yes, directly. On iPhone it works only after the user adds your site to their home screen, which is realistic for a tool people use daily and a real drop-off point for casual consumer products. If a notification is the only reason you want an app, test whether home-screen installation is acceptable to your users first.

### Is a cross-platform framework as good as a native app?

For the large majority of founder products, yes — React Native and Flutter cover both platforms from one codebase and are indistinguishable to users for typical interfaces. They reduce build cost but not store overhead, so review submissions, staged releases, device testing and annual OS updates still apply.

### What ongoing costs does an app have that a website doesn't?

An Apple developer account at €99 per year, a one-off Google registration fee, and roughly twice-yearly maintenance to keep pace with new OS versions and rising minimum SDK requirements, plus crash reporting and support for older versions still installed on users' phones. Budget for the app being alive rather than only for building it.

### Can I start with web and add an app later without wasting the first build?

Yes, and it is usually the cheaper sequence, because most of what an app needs is the API and backend underneath it. Building web first gives you a validated interface, real users to test with and search visibility, and turns the app into an additional client on an existing system rather than a project from zero.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Will Apple really take a commission on my subscription?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Only for digital goods and services consumed inside the app, where in-app purchase is generally required at 30% or 15% under the small-business threshold. Physical goods, real-world services and business software billed outside the app typically fall outside those rules."
      }
    },
    {
      "@type": "Question",
      "name": "Can a responsive web app send push notifications?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "On Android and desktop browsers yes, directly. On iPhone it works only after the user adds the site to their home screen, which suits daily-use tools but is a real drop-off point for casual consumer products."
      }
    },
    {
      "@type": "Question",
      "name": "Is a cross-platform framework as good as a native app?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "For most founder products yes: React Native and Flutter cover both platforms from one codebase and are indistinguishable to users for typical interfaces. They reduce build cost but not store overhead such as reviews, staged releases and annual OS updates."
      }
    },
    {
      "@type": "Question",
      "name": "What ongoing costs does an app have that a website doesn't?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "An Apple developer account at €99 per year, a one-off Google registration fee, roughly twice-yearly maintenance for new OS versions and rising minimum SDK requirements, plus crash reporting and support for older installed versions."
      }
    },
    {
      "@type": "Question",
      "name": "Can I start with web and add an app later without wasting the first build?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes, and it is usually cheaper, because most of what an app needs is the API and backend beneath it. Web first gives you a validated interface, real users and search visibility, making the app an extra client on an existing system."
      }
    }
  ]
}
</script>
