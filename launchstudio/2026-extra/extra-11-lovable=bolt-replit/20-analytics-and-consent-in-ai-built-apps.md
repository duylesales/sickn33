---
Title: "Cookie Consent and Analytics in AI-Built Apps: Doing It Properly"
Keywords: ai app security, cookie consent netherlands, analytics without cookies, autoriteit persoonsgegevens consent, Lovable, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: AI-Native Founder (Non-Technical)
---

# Cookie Consent and Analytics in AI-Built Apps: Doing It Properly

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Cookie Consent and Analytics in AI-Built Apps: Doing It Properly",
  "description": "Why the consent banner on most AI-built apps fails on the two points that matter, what actually requires consent, and how to set up analytics you can rely on without collecting a legal problem.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-06-22",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/analytics-and-consent-in-ai-built-apps" }
}
</script>

Adding analytics to a Lovable app takes about ninety seconds: paste a snippet, deploy, watch the numbers arrive. Adding a cookie banner takes about the same, because there is a component for it and it looks like the ones on every other website.

Both of those ninety-second decisions are usually wrong, and in a specific way. The tracking starts before anyone consents to it, and the banner offers a prominent "accept" with no equally easy way to refuse. That combination is common enough to look normal and is precisely what Dutch and European supervisory authorities have been writing about for years.

This is general information rather than legal advice, and the rules and guidance in this area continue to develop — verify the current position for your product.

## What Actually Requires Consent

Two separate rules apply, which is why the subject confuses people.

**Storing or reading information on someone's device** — cookies, and equivalent techniques like local storage or device fingerprinting — is governed by ePrivacy rules implemented in Dutch telecommunications law. Consent is required unless the storage is strictly necessary to deliver the service the visitor asked for.

**Processing personal data** is governed by the GDPR, which requires a lawful basis and, where consent is that basis, sets standards for what counts as consent: freely given, specific, informed and unambiguous, with refusal as easy as agreement.

The practical upshot for a typical AI-built product: your login session cookie is strictly necessary and needs no consent. Your analytics, your heatmap tool, your advertising pixel and your chat widget generally do need it, before they run.

## The Two Failures in Almost Every Banner

**The scripts load first.** This is the technical failure and it is nearly universal in generated apps. The analytics snippet sits in the page and executes on load; the banner appears afterwards and sets a preference that nothing checks. Clicking "reject" changes a value in storage and stops nothing, because the tracking already happened.

**Refusing is harder than accepting.** A prominent "Accept all" button next to a grey link to "Manage preferences" that takes three clicks to refuse is exactly the pattern regulators have been describing as non-compliant. Guidance from the Dutch Autoriteit Persoonsgegivens and other European authorities has consistently pointed toward equal prominence for accepting and refusing.

There is a third, quieter failure: a banner that says "by continuing to use this site you agree" — which is not consent by any current standard, and has not been for years.

## The Analytics Question Behind the Banner

Before designing consent, ask a more useful question: what do you actually need to know?

Most founders want four numbers — how many people visited, where they came from, which pages they looked at, and how many signed up. That is a genuinely modest requirement, and it does not need a full commercial analytics suite following individuals across the internet.

Three options serve it, with different consequences.

**Privacy-focused analytics tools** that avoid storing identifiers on the device and do not track individuals across sites. Several are built explicitly to run without consent, and their own documentation explains the basis on which they claim that. This is the route most small Dutch products should look at first.

**Server-side counting.** Your own application already knows how many signups happened and which pages were requested. For a product with a few hundred users, a simple internal dashboard answers most questions without any third party at all.

**Full commercial analytics** with consent properly implemented, if you genuinely need funnels, cohorts and cross-device attribution — typically once you are spending on advertising and need to measure it.

Choosing the first or second removes most of the banner problem by removing the tracking that required it.

## Doing Consent Properly When You Need It

If you do need consent-requiring tools, the implementation has to satisfy four things.

**Nothing loads before a choice is made.** Scripts are injected after consent, not merely gated by a flag. This is the part that takes real work in an AI-built app, because the generated code typically hardcodes the snippet into the page.

**Accept and refuse are equally easy.** Same visual weight, same number of clicks, both on the first screen.

**Categories are separable.** Someone can accept analytics and refuse advertising.

**The choice is recorded and revocable.** You can show what a visitor consented to and when, and they can change their mind through a persistent link rather than by clearing their browser.

## What About Data You Already Collected?

An awkward question with a straightforward answer: if it was collected without a valid basis, do not build on it. In practice that means not using historic advertising audiences assembled without consent, and being cautious about analytics data you would have to defend.

For most small products the volume is small and the loss is trivial. Deleting a few months of questionable analytics costs you nothing you were relying on, and it removes a liability you would otherwise carry indefinitely.

## Where This Intersects With Your Customers' Reviews

For business-to-business products this stops being about your own compliance. If your app embeds tracking that loads before consent on a page your customer's users visit, your customer inherits the problem. Procurement teams have started asking about it specifically, alongside the sub-processor list, because a third-party script in your product is a third-party script in their service.

Being able to say that your application loads no third-party trackers at all, or loads them only after explicit consent, is a short and strong answer in a security review.

## A Sensible Setup for a Small Product

For most AI-built products in the Netherlands, this is enough.

Use a privacy-focused analytics tool, or your own server-side counting, so that no consent is required for basic measurement. Load no advertising pixels until you are actually advertising. Keep only strictly necessary cookies, which need no banner at all. Write a short, honest privacy statement that says what you collect and why. And if you later add tools that require consent, implement the banner properly at that point, with scripts injected after the choice.

The result is fewer moving parts, a faster site, one less thing to defend in a review — and, for the vast majority of founders, exactly the same four numbers they were looking at anyway.

## Getting It Set Up Once, Correctly

This is small work with a large downside when skipped, and it is part of what LaunchStudio sorts out when preparing an AI-built product for launch: removing trackers that were never needed, configuring measurement that does not require consent where possible, implementing consent properly where it is, ensuring scripts genuinely do not run before a choice, and writing the privacy statement to match what the app actually does rather than what a template assumed.

The frontend you built in Lovable stays as it is, the code stays yours, and the documentation goes into the same pack your customers' privacy officers will eventually ask for. Behind it is Manifera — eleven years of production engineering for clients including Vodafone and TNO, from Amsterdam and Ho Chi Minh City.

[Describe your project](https://launchstudio.eu/en/#contact) and you will hear within one business day what your app is currently loading and whether it needs a banner at all, or read what [Launch Ready covers](https://launchstudio.eu/en/#packages) first.

## The Privacy Statement Nobody Reads and Everybody Checks

Almost every AI-built product has a privacy statement copied from a generator, describing data handling that does not match what the app does. It is rarely read by users and it is read closely by exactly two audiences: a business customer's privacy officer, and a regulator responding to a complaint.

Getting it right is mostly a matter of describing reality.

**Say what you collect, in categories a person recognises.** Account details, content they create, technical data such as address and browser, payment information handled by your provider. Not a legal taxonomy — a list.

**Say why, for each category,** and on what basis. "To provide the service you signed up for" covers most of it; analytics and marketing need their own lines.

**Name your sub-processors, or link to a list you maintain.** This is the item business customers check first, and the one most templates omit entirely.

**State retention in time periods,** not in the phrase "as long as necessary". If you delete inactive accounts after two years, say two years.

**Describe rights and how to exercise them,** with a real address that reaches a human. An email that bounces is worse than none.

**Say where data is stored.** One sentence naming the region.

Then keep it current. A statement that described your app accurately in March and not in September is a document that actively works against you, because it demonstrates that nobody is minding the subject. Review it whenever you add a third-party service — which, in an AI-assisted workflow, happens more often than you think.

## Embedded Content Counts Too

Trackers are not only the ones you installed deliberately. Several things AI builders add without comment behave the same way.

**Embedded videos** frequently set cookies and contact a third party the moment a page loads, whether or not anyone presses play. Privacy-preserving embed options usually exist and are a configuration choice.

**Web fonts loaded from a third party** send the visitor's address to that provider on every page view. Hosting the font files yourself removes the transfer entirely and usually makes the page faster.

**Maps, chat widgets and social buttons** all load third-party code with its own data handling.

The practical step is the same audit as before: load your page with the browser's network tab open and look at every external domain contacted before you interacted with anything. Each one is either necessary, replaceable with a self-hosted alternative, or something that should wait for consent.

## Real example

### A Job Board That Removed Its Banner Entirely

Rik Doornbos ran Vakwerk, a niche job board for skilled trades in Gelderland, built in Lovable. It carried a copied consent banner, a commercial analytics snippet, a heatmap tool he had installed during a redesign and forgotten, and an advertising pixel from a campaign that ended in March.

A recruitment agency doing due diligence before a partnership asked which third-party scripts ran on pages where their vacancies appeared. Rik did not know, and finding out took an afternoon of reading his own page source.

The cleanup took three business days. The heatmap tool and the dormant advertising pixel were removed entirely. Commercial analytics was replaced with a privacy-focused tool that stores no identifier on the visitor's device, which removed the consent requirement for measurement. The banner was deleted rather than fixed, since only strictly necessary cookies remained. The privacy statement was rewritten to describe the four things the site now collects. Page weight dropped noticeably as a side effect, improving mobile load time.

**Result:** the agency partnership proceeded, the site got faster, and Rik reports that the numbers he actually uses — visits, sources, vacancy views, applications — are unchanged.

> *"I had a consent banner asking permission for three tools I wasn't using and one I'd forgotten about. Deleting them was easier than explaining them."*
> — **Rik Doornbos, Founder, Vakwerk (Arnhem)**

**Cost & Timeline:** €980 (tracker audit, analytics replacement, banner removal, privacy statement) — completed in 3 business days.

## Frequently Asked Questions

### Does every website need a cookie banner?

No. Banners are needed for storage that is not strictly necessary — analytics, advertising, embedded third-party tools. A site with only essential cookies needs a clear privacy statement and no consent banner at all.

### Is my copied banner good enough?

Usually not, on two counts: the tracking scripts typically load before any choice is made, and refusing is rarely as easy as accepting. Both are the specific issues European and Dutch supervisory guidance has focused on.

### Can I run analytics without consent?

Some privacy-focused tools are designed for this, storing no identifier on the device and not tracking individuals across sites. Read the specific tool's documentation about the basis it relies on, and confirm your configuration matches it.

### What should I do about the analytics data I already have?

If it was collected without a valid basis, avoid building on it. For most small products, deleting a few months of questionable data costs nothing of substance and removes an ongoing liability.

### Why do my business customers care about my trackers?

Because a third-party script inside your product runs on their users' devices, which makes it their problem as well as yours. Being able to say you load no trackers, or only post-consent, shortens a security review considerably.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Does every website need a cookie banner?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No. Banners are needed for storage that is not strictly necessary, such as analytics or advertising. A site with only essential cookies needs a clear privacy statement and no banner."
      }
    },
    {
      "@type": "Question",
      "name": "Is my copied banner good enough?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Usually not: tracking scripts typically load before any choice is made, and refusing is rarely as easy as accepting — the two issues supervisory guidance focuses on."
      }
    },
    {
      "@type": "Question",
      "name": "Can I run analytics without consent?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Some privacy-focused tools are designed for it, storing no device identifier and not tracking across sites. Check the tool's documentation and confirm your configuration matches."
      }
    },
    {
      "@type": "Question",
      "name": "What should I do about analytics data I already have?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "If it lacked a valid basis, avoid building on it. For small products, deleting a few months of questionable data costs little and removes an ongoing liability."
      }
    },
    {
      "@type": "Question",
      "name": "Why do my business customers care about my trackers?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "A third-party script in your product runs on their users' devices, making it their problem too. Loading no trackers, or only after consent, shortens their security review."
      }
    }
  ]
}
</script>
