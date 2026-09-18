---
Title: "Cookie Consent That Would Pass a Dutch Audit"
Keywords: cookie consent, AVG cookies, consent banner, analytics without cookies, ePrivacy, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: AI-Native Founder (Non-Technical)
---

# Cookie Consent That Would Pass a Dutch Audit

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Cookie Consent That Would Pass a Dutch Audit",
  "description": "Most consent banners on AI-built sites do nothing: scripts load before anyone clicks. What consent must actually look like, which cookies need none, and the option of not needing a banner at all.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-12-02",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/cookie-consent-that-would-pass-a-dutch-audit" }
}
</script>

Open your own site with the network tab visible and look at what loads before you touch the banner.

In the large majority of AI-built sites, the analytics script, the marketing pixel and the support chat widget have all loaded and set their cookies before the visitor has made any choice at all. The banner is decoration: it records a preference that changes nothing, because the tracking already happened.

This is the single most common compliance failure on small Dutch websites, and it is also entirely fixable in an afternoon.

## Consent Means Before, Not After

The requirement is straightforward. Non-essential cookies and similar technologies may be placed only after the visitor has given permission. Before means before — not while the banner is shown, not on the second page view, not "we anonymise it so it is fine".

So the technical arrangement that follows is equally straightforward. Scripts that set non-essential cookies must not be in the page at all until consent exists. They are added dynamically once permission is recorded, and on a visitor's return the recorded choice determines what loads.

A tag manager does not solve this by itself. A tag manager that fires everything on page load is the same failure with more configuration.

## What Needs Consent and What Does Not

Necessary cookies need none: the session that keeps a user logged in, a security token, a shopping basket, a load balancer's routing, and the record of the consent choice itself.

Everything else needs it. Analytics of every kind unless it genuinely qualifies for an exemption. Advertising and remarketing pixels. Embedded video that sets cookies. Support chat widgets. Session recording, heatmaps, and A/B testing tools.

Two frequent misunderstandings. "Anonymised" analytics still generally requires consent if it reads or writes on the visitor's device — the question is about the access to the device, not only about identification. And an embedded video or map is a third party you are inviting onto the page, which is why the well-behaved approach is a placeholder that loads the embed only when the visitor asks for it.

## What a Valid Banner Looks Like

Five properties, and most banners fail at least two.

**Refusing is as easy as accepting.** If accepting is one click and refusing requires opening preferences and untoggling categories, the consent is not freely given. An equally prominent reject button on the first screen is the expected standard now, and its absence is the most cited failure in European enforcement.

**Nothing is pre-ticked.** Categories default to off. Silence is not consent, and neither is continued scrolling.

**Granular by purpose.** Analytics, marketing and functional as separate choices, not one switch.

**Specific and clear.** What is set, by whom, for what, and for how long — reachable from the banner, in plain language.

**Withdrawable.** A visible way to change the choice later, on every page, as easy as giving it was.

Record what was consented to and when, because the burden of showing that consent was obtained falls on you.

## Consider Not Needing One

The option founders overlook: a site with no non-essential cookies needs no banner.

Privacy-focused analytics tools exist that measure page views and referrers without cookies and without identifying individuals — enough for the questions a small product actually asks. Support chat can be a link rather than an embedded widget. Video can be self-hosted or loaded on request. Fonts can be served from your own domain rather than fetched from a third party.

The result is a faster site, no banner, nothing to maintain, and no exposure at all. For most small products the analytics detail lost is genuinely negligible, and the conversion gained from removing an interstitial is not.

This is the recommendation for a founder who wants this subject to stop being a subject.

## The Dutch Specifics

Two points worth knowing if you sell here.

The Autoriteit Persoonsgegevens has been explicit about dark patterns: banners that make refusal harder than acceptance, or that use colour and placement to steer. A reject button styled as an afterthought is a documented failure mode rather than a clever design.

And cookie walls — refusing access unless a visitor accepts tracking — are generally not acceptable, because consent conditioned on access is not freely given.

## Inside the Product, Different Rules Apply

Founders conflate the marketing site and the logged-in application, and the considerations are not the same.

Inside a product, the session cookie and security tokens are necessary and need no consent. What does need thought is the analytics and session recording that AI-built applications frequently include by default — because here you are observing identifiable users doing their work, often with their customers' data on screen.

Two things follow. Product analytics on an authenticated user is personal data processing that requires a basis and disclosure, and for a business product it is your customer's data you are observing, which means their processing agreement covers it and they may well object.

Session recording deserves particular care. A tool that captures what a user sees is capturing their clients' records, their patients' notes, their employees' salaries. If you use one, mask input fields and sensitive regions by default, exclude the screens that show customer data entirely, and disclose it plainly. Several products have discovered at an awkward moment that their recording tool holds a searchable archive of other people's confidential information.

The conservative position, and the one worth defaulting to: measure your product with events you emit deliberately — a feature used, a flow completed — rather than by recording what people see. It answers the questions you actually have, and it collects almost nothing you would rather not hold.

## The Conversion Argument Nobody Makes

There is a commercial case for doing this properly that has nothing to do with regulation, and it is worth stating because it changes how founders feel about the work.

A consent banner is an interstitial between a visitor and your product. It delays the first meaningful moment, it looks the same as every other banner they have dismissed today, and on a phone it frequently covers the content they arrived for. Sites that remove the need for one report faster pages and lower bounce rates, and the effect is largest on mobile where the banner occupies the most screen.

Against that, weigh what the analytics actually gives you. For most small products the honest answer is: page views, referrers, and which pages convert. All three are available without cookies.

The detailed behavioural data that requires consent is valuable to a company running experiments at volume. At forty visitors a day it is not a basis for any decision you can make with confidence, and half of it is missing anyway because a large share of visitors refuse.

So the calculation for a small product usually favours the cookie-free route on its own merits: a faster site, no banner, no maintenance, no exposure, and data that is slightly less rich but more complete because nobody opted out of it.

## Check It Twice a Year

Cookie compliance decays, and it decays through ordinary work rather than neglect.

A marketing page gets an embedded video. A support tool is swapped. An AI session adds a font from a third party because that was the shortest way to get the typography right. A campaign adds a pixel for a month and nobody removes it. Each change is small, none goes through a review, and the site that was compliant in March is not in September.

The check is quick enough to schedule. Open the site in a fresh browser profile, refuse everything, and look at what still loads and what cookies exist. Then compare that list against what your policy says. Fifteen minutes, twice a year, and after any campaign that involved adding a tag.

Two supporting habits make the check rarer rather than more frequent. Keep a note of every third party allowed on the site and why, so an addition is a decision rather than an accident. And treat adding a third-party script as a change worth mentioning, the same way you would treat adding a dependency — because that is exactly what it is, with the difference that this one runs in your visitors' browsers and can see what they type.

## Setting This Up

For an existing site this is typically half a day: an audit of what is actually set before consent, non-essential scripts removed from the page and loaded dynamically only after permission, a banner with equally prominent accept and reject, no pre-ticked categories, granular purposes, a clear specific description and a persistent way to withdraw, consent choices recorded with a timestamp, embedded third-party content replaced with click-to-load placeholders, and a verification pass with the network tab to confirm that a visitor who refuses is genuinely untracked.

Or, frequently better: the cookie-free alternative, which is usually less work than doing the above properly.

LaunchStudio does either, and recommends the second for most small products. Behind the work is Manifera — eleven years, clients including Vodafone, TNO and CFLW, with European client contact from Herengracht 420 in Amsterdam.

[Ask us what loads on your site before the banner](https://launchstudio.eu/en/#contact). It takes two minutes to check.

## Real example

### A Banner That Changed Nothing

Priya Ramnath built Webshopstart in Lovable: a platform where 180 small Dutch retailers run simple online shops, with her own marketing site attracting new merchants.

Her consent banner was added by an AI session and looked entirely conventional: accept, and a link to preferences. A complaint reached her after a visitor examined the site and found that analytics, an advertising pixel and a support chat widget all loaded and set cookies on arrival, before any interaction. The banner recorded a preference and nothing acted on it.

Worse, the same banner was embedded in all 180 merchant shops, which meant every retailer using her platform had the same defect on their own storefront — and as merchants, they were the ones responsible for their visitors' data.

Four business days: a full audit of what loaded before consent across the marketing site and the shop template, finding six third parties including a font service and an embedded map nobody had noticed; all non-essential scripts removed from the page and loaded dynamically only after consent; the banner rebuilt with equally prominent accept and reject on the first screen, no pre-ticked categories, three granular purposes and a specific description of each cookie with its duration and provider; consent recorded with a timestamp and a version, so a change to the cookie set re-asks; a persistent footer link to change the choice; the embedded map replaced with a click-to-load placeholder and fonts moved to self-hosting; and the corrected banner rolled out across all 180 shops with a notice to merchants explaining what had changed and why.

**Result:** roughly 41 percent of visitors now refuse analytics, which Priya describes as uncomfortable and honest. Page load improved by 700 milliseconds after removing the third-party font and map. Nine merchants replied to the notice; two said the explanation was the first time anyone had told them they had an obligation of their own.

> *"My banner was a picture of a banner. It asked a question, stored the answer, and then loaded everything regardless of what the visitor had said."*
> — **Priya Ramnath, Founder, Webshopstart (Rotterdam)**

**Cost & Timeline:** €2,800 (consent audit across platform and shop template, script loading rework, banner rebuild with granular purposes and equal prominence, consent recording with versioning, third-party embed replacement, self-hosted fonts, rollout across 180 shops) — completed in 4 business days.

## Frequently Asked Questions

### Does my banner work if scripts load before the visitor clicks?

No. Consent must precede placement. If analytics and pixels load on arrival, the banner records a preference that nothing acts on — the most common failure on small Dutch sites.

### Does anonymised analytics need consent?

Generally yes, if it reads or writes on the visitor's device. The requirement concerns access to the device, not only whether an individual is identified.

### Must the reject button be as prominent as accept?

Yes. If refusing takes more effort than accepting, consent is not freely given, and unequal prominence is a documented enforcement concern in the Netherlands.

### Can I require consent to use my site?

Cookie walls are generally not acceptable, since consent conditioned on access is not freely given.

### Can I avoid a banner altogether?

Yes — use cookie-free analytics, self-host fonts, replace embedded third-party content with click-to-load placeholders. For most small products this is less work than implementing consent properly.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Is my cookie banner valid if scripts load before the click?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No. Consent must precede placement — scripts loading on arrival make the banner decorative."
      }
    },
    {
      "@type": "Question",
      "name": "Does anonymised analytics require consent?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Generally yes if it reads or writes on the visitor's device; the rule concerns device access, not only identification."
      }
    },
    {
      "@type": "Question",
      "name": "Must reject be as prominent as accept?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. Unequal prominence means consent is not freely given and is a documented enforcement concern in the Netherlands."
      }
    },
    {
      "@type": "Question",
      "name": "Are cookie walls allowed?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Generally not — consent conditioned on access to the site is not freely given."
      }
    },
    {
      "@type": "Question",
      "name": "Can a site avoid needing a cookie banner?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes — cookie-free analytics, self-hosted fonts and click-to-load embeds remove the requirement and are usually less work than proper consent."
      }
    }
  ]
}
</script>
