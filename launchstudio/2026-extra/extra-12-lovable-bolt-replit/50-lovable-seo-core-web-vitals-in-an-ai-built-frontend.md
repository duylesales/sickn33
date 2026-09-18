---
Title: "Lovable SEO: Core Web Vitals in an AI-Built Frontend"
Keywords: lovable seo, core web vitals, LCP, INP, CLS, page speed, bundle size, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: Technical Solo Founder / Indie Hacker
---

# Lovable SEO: Core Web Vitals in an AI-Built Frontend

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Lovable SEO: Core Web Vitals in an AI-Built Frontend",
  "description": "Generated frontends are heavy in predictable ways. What the three metrics measure, why laboratory scores mislead, and the five changes that fix most AI-built sites.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-12-22",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/lovable-seo-core-web-vitals-in-an-ai-built-frontend" }
}
</script>

Core Web Vitals are three measurements of what using your site feels like: how long until the main content appears, how quickly the page responds when someone interacts, and whether things move around while they are reading.

They are a ranking factor, which is why they appear in SEO discussions. They matter considerably more as a conversion factor, because a page that takes six seconds on a phone loses a substantial share of the people who requested it — and the ranking effect is small compared with that.

AI-built frontends fail them in consistent ways, which is good news: the fixes are the same every time.

## The Three Metrics, Practically

**Largest Contentful Paint** — how long until the biggest visible element appears. Under 2.5 seconds is good. On generated sites this is usually slow because the page is assembled by JavaScript after a large bundle downloads, or because the hero image is enormous.

**Interaction to Next Paint** — how quickly the page responds when someone taps or types. Under 200 milliseconds is good. Failures come from too much JavaScript occupying the main thread, and are far worse on mid-range Android phones than on a developer's laptop.

**Cumulative Layout Shift** — how much content moves while loading. Under 0.1 is good. Caused by images without dimensions, fonts swapping, banners inserted above content, and anything that appears after the page has rendered.

## Measure Real Visitors, Not a Laboratory

A page speed tool gives you a laboratory score from one simulated run. It is useful for diagnosis and misleading as a measure of reality.

What counts is field data — actual measurements from actual visitors on their actual devices and connections. Search consoles report it, and it is the number that reflects your users.

The gap between the two is frequently large, and always in the same direction. Your laboratory score is generated on a fast connection; your Dutch customers include people on a train with a four-year-old phone. Optimising the laboratory number while the field number stays poor is the most common way this work is wasted.

If you have too little traffic for field data, test on a real mid-range phone with the network throttled. It is uncomfortable and it is the truth.

## The Five Changes That Fix Most Sites

**Serve real HTML for public pages.** Covered elsewhere in this series and the single largest factor: if the content is in the server's response, the largest element can paint immediately instead of after a bundle downloads and executes.

**Fix the images.** Correct dimensions in the markup so nothing shifts, modern formats, sizes matched to display, lazy loading for anything below the fold — and specifically *not* lazy loading the hero image, which is a common mistake that directly harms the metric it was meant to help.

**Reduce the JavaScript.** Generated sites routinely ship several hundred kilobytes for a marketing page with no interactivity. Split by route so a visitor downloads what that page needs, remove component libraries used for one element, and question anything imported for a single function.

**Host the fonts yourself, with a fallback.** A font fetched from a third party costs a connection and a round trip before any text appears, and swapping to it later shifts the layout. Self-host, preload the one face you need, and set a fallback stack so text is readable immediately.

**Remove third-party scripts from pages that do not need them.** Chat widgets, analytics, embeds and tag managers each cost main thread time. On a marketing page, most of them are optional.

## Reserve Space for Everything That Arrives Late

Layout shift is the easiest metric to fix and the most visible to users, because it is the reason someone taps the wrong thing.

Every element that appears after initial render needs its space reserved: images and video with explicit dimensions or an aspect ratio, advertisements and embeds with a sized container, notification banners rendered above the fold rather than inserted into it, and dynamically loaded content occupying a placeholder of the right size.

The test is to load your page on a slow connection and watch. Anything that jumps is a defect you can see, and it takes minutes to find.

## Do Not Chase a Perfect Score

A score of 100 is not the goal and pursuing it produces diminishing returns quickly.

The thresholds are what matter: LCP under 2.5 seconds, INP under 200 milliseconds, CLS under 0.1, for the 75th percentile of real visitors. A site meeting all three is fine, and further optimisation buys very little in either ranking or conversion.

Spend the effort saved on content, which is where the actual ranking is.

## Keep It From Coming Back

Performance regresses the same way accessibility does: gradually, through individual changes that each seem harmless.

An AI session adds a charting library for one small visualisation and it lands in the shared bundle. A marketing request adds an embedded video to the home page. An animation library arrives for a single transition. None of these is unreasonable and together they undo a day's work over four months.

Two measures hold the line at small-product scale.

**A budget, enforced in the build.** State a maximum size for the JavaScript served to public pages — 200 KB compressed is a reasonable starting point for a marketing site — and fail the build when it is exceeded. The failure forces a decision rather than allowing an accumulation, and the decision is usually "load this only on the page that needs it".

**A monthly look at field data.** Five minutes in the search console, comparing the three metrics against last month. A step change points at a specific deploy, which is far easier to investigate than a gradual decline discovered a year later.

The habit worth attaching to both: when a library is added, ask which pages need it. In a generated codebase the default is that everything is imported everywhere, and the difference between that and route-based loading is frequently the whole of a site's performance problem.

## The Application Deserves the Same Attention

The metrics are a search consideration for public pages, and a retention consideration for the product behind the login — where the same visitor returns every day rather than once.

The failure modes differ. Public pages are slow because too much is downloaded before anything appears. Applications are slow because too much work happens after the data arrives: a list rendering four hundred rows at once, a component recalculating on every keystroke, a table re-sorting the whole dataset in the browser.

The measurement that matters inside a product is responsiveness — the delay between a user acting and something happening. Typing in a search box that freezes for 300 milliseconds per character is a product people describe as sluggish without being able to say why, and it is invariably work on the main thread that could be deferred, debounced or moved to the server.

Three checks find most of it. Open the busiest screen with a device throttled to a quarter of its speed and use it normally. Type quickly in every search and filter field. And load the account with the most data rather than your own test account, which is the difference between a product that feels fine and one your largest customer complains about.

Fixes are usually small: debounce the input, paginate the list, move the sort to the database, and render only what is visible. None is architectural, and together they change how a daily-use product feels.

It is also the work most likely to be noticed by the people paying you. Nobody writes to say your marketing page loads quickly; customers absolutely notice when the screen they open forty times a day stops making them wait.

## Setting This Up

For an existing site this is typically one to two days: field data reviewed for real visitors rather than laboratory scores, public pages served as real HTML, images given explicit dimensions and modern formats with the hero eagerly loaded and the rest lazy, JavaScript split by route with unnecessary libraries removed, fonts self-hosted with preloading and a fallback stack, third-party scripts removed from pages that do not need them, space reserved for everything that arrives late, and verification on a real mid-range phone with a throttled connection rather than on a laptop.

LaunchStudio does this alongside the architectural work that usually determines it, since the rendering decision sets the ceiling for everything else. Behind it is Manifera — eleven years, 160+ projects, from Amsterdam and Ho Chi Minh City.

[Ask us what your site scores for real visitors](https://launchstudio.eu/en/#contact), not in a test.

## Real example

### Fast on a Laptop, Unusable on a Train

Nienke Brandts built Cursusplein in Lovable: a marketplace listing training courses from 210 providers, where learners search, compare and book.

Her page speed score on a laptop was 88 and she considered performance solved. Her field data told a different story: LCP at the 75th percentile was 5.8 seconds, INP was 410 milliseconds, and CLS was 0.34. Roughly 70 percent of her visitors were on phones.

The specific finding that made it concrete: her booking conversion rate from mobile was a third of desktop, which she had assumed was a behavioural difference rather than a performance one.

Two business days: course listing and detail pages converted to static generation with server-rendered HTML, which alone moved LCP from 5.8 to 2.1 seconds; the hero image on listing pages given explicit dimensions and removed from lazy loading, which had been delaying the largest element deliberately; course thumbnails converted to modern formats at display size, cutting a listing page from 3.8 MB to 340 KB; JavaScript split by route, with a date library, a charting library used on one administrative screen, and a component library used for two buttons removed from the public bundle, reducing it from 780 KB to 190 KB; two fonts self-hosted with one preloaded and a fallback stack set, replacing a third-party import; a chat widget removed from public pages and kept only in the booking flow; explicit space reserved for the provider logo and the availability banner, both of which had been inserted after render and causing most of the layout shift; and everything verified on a four-year-old Android phone on a throttled connection rather than on a laptop.

**Result:** field LCP settled at 1.9 seconds, INP at 140 milliseconds and CLS at 0.02. Mobile booking conversion rose from 1.1 to 2.9 percent over the following two months, which on her volume was worth roughly €4,100 a month in commission. Organic rankings improved modestly; the conversion change was the one that mattered.

> *"My score on a laptop was 88 and I thought I was finished. My actual customers were on phones on trains, and for them the site took six seconds and then moved while they were tapping."*
> — **Nienke Brandts, Founder, Cursusplein (Haarlem)**

**Cost & Timeline:** €2,900 (static generation for public pages, image dimensions formats and loading strategy, bundle splitting and library removal, font self-hosting with preload, third-party script removal, layout shift remediation, real-device verification) — completed in 2 business days.

## Frequently Asked Questions

### Do Core Web Vitals actually affect rankings?

They are a factor and a modest one. The larger effect is on conversion — a six-second page on a phone loses a meaningful share of visitors before anything else matters.

### Why is my laboratory score good but my field data poor?

Because the laboratory runs on a fast connection and a capable machine, while your visitors include mid-range phones on mobile networks. Field data at the 75th percentile is the number that counts.

### What single change helps most in an AI-built site?

Serving real HTML for public pages instead of assembling them with JavaScript. It sets the ceiling for everything else.

### Should I lazy load all images?

No. Lazy loading the hero image delays the largest element and directly harms LCP. Load it eagerly and lazy load what is below the fold.

### Is a perfect score worth pursuing?

No. Meet the thresholds — 2.5 seconds, 200 milliseconds, 0.1 — and spend the remaining effort on content, which is where ranking actually comes from.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Do Core Web Vitals affect search rankings?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "They are a modest ranking factor. The larger effect is conversion — slow pages lose visitors before content quality matters."
      }
    },
    {
      "@type": "Question",
      "name": "Why is my lab score good but field data poor?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Lab tests run on fast connections and capable devices. Field data at the 75th percentile reflects real phones on real networks."
      }
    },
    {
      "@type": "Question",
      "name": "What single change helps AI-built sites most?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Serving real HTML for public pages instead of assembling them in the browser — it sets the ceiling for every other improvement."
      }
    },
    {
      "@type": "Question",
      "name": "Should every image be lazy loaded?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No. Lazy loading the hero image directly harms LCP. Load it eagerly and lazy load only what is below the fold."
      }
    },
    {
      "@type": "Question",
      "name": "Is a perfect performance score worth chasing?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No. Meet the thresholds and spend remaining effort on content, which drives ranking far more."
      }
    }
  ]
}
</script>
