---
Title: "Lovable SEO: Recovering Rankings After a Rebuild"
Keywords: lovable seo, site migration, redirects, lost rankings, technical seo, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: SaaS Scale-Up
---

# Lovable SEO: Recovering Rankings After a Rebuild

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Lovable SEO: Recovering Rankings After a Rebuild",
  "description": "Rebuilding a site that already ranked is the fastest way to lose traffic you spent years earning. What actually causes the drop, how to diagnose it in an afternoon, and the order in which to recover.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-08-21",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/lovable-seo-recovering-rankings-after-a-rebuild" }
}
</script>

The new site is better in every way you can see. It looks current, it loads in the browser instantly, the forms work, the old clutter is gone. You launched it on a Thursday.

By the following Thursday, enquiries are down by half. Three weeks later the pattern is unmistakable: the pages that used to bring people no longer bring anyone, and the phrases you used to appear for return competitors you had comfortably outranked for years.

This is the most avoidable disaster in this entire field, and it happens constantly — particularly when an established site is rebuilt quickly with AI tooling, because the rebuild reproduces what the site looks like and not what the site *was* to a search engine.

## What a Search Engine Thought Your Old Site Was

Understanding the loss requires understanding what was there.

A site that has ranked for years has accumulated four things. **Addresses** that are known, indexed and linked from elsewhere. **Reputation** attached to those specific addresses, earned by other sites linking to them. **Content** that matched what people searched. And **signals** — structured data, sitemaps, internal links, page titles — telling the engine what each page was about.

A rebuild that keeps the appearance and changes the addresses discards the first two, which are the ones that took years and cannot be recreated by writing more.

## The Five Causes, in Order of Frequency

**Addresses changed without redirects.** The single biggest cause. `/diensten/dakisolatie` becomes `/services/roof-insulation`, or a page that was at a path is now behind a search filter. Every link pointing at the old address now leads nowhere, and the reputation it carried evaporates.

**Content that no longer exists in the initial response.** The rebuild is a browser-rendered application, so where the old pages served text to a crawler, the new ones serve an empty shell. The content is there for humans and absent on the first pass.

**Pages dropped in the rebuild.** The old site had 60 pages; the new one has 12, because nobody listed what existed. Those 48 pages included the long, specific ones nobody thought mattered, which were frequently the ones bringing steady visitors.

**Titles and descriptions flattened.** Every page now shares one title, so pages that matched specific searches no longer distinguish themselves.

**Indexing accidentally blocked.** A development setting carried into production — a robots file disallowing everything, or a directive telling engines not to index. Rarer, catastrophic, and mercifully quick to fix.

## Diagnosing It in an Afternoon

Work in this order; each step either explains the drop or eliminates a cause.

**Check indexing first.** Look at your robots file and at the page source for a no-index directive. If either is blocking, stop and fix it — everything else is secondary.

**Get the list of old addresses.** From your search console, your analytics of the previous year, and a crawl of an archived copy of the old site. This list is the whole recovery: without it you are guessing which pages existed.

**Test a sample of old addresses.** Do they redirect to a sensible new page, redirect to the home page, or return an error? Redirecting everything to the home page is barely better than an error — the engine treats it as the page being gone.

**View the source of your key new pages** with JavaScript disabled. If the content is not there, that is your second cause.

**Compare titles** across the new pages. Identical titles mean the pages no longer differentiate.

**Check which pages are now indexed** against the old list, and note what is missing.

## Recovering, in the Right Order

**One: unblock indexing** if that is the problem.

**Two: map and redirect every old address.** Each old page to its closest new equivalent, using permanent redirects, one hop, never a chain. Where no equivalent exists, redirect to the most relevant section rather than the home page — and where a page genuinely has no successor, consider bringing it back, because a page that earned links for four years is worth more than the tidiness of removing it.

**Three: restore content to the initial response** for the public pages, so a crawler receives text rather than an empty shell.

**Four: give every page its own title, description and single heading.**

**Five: resubmit a sitemap** built from the new addresses, and use your search console to request re-crawling of the most important pages.

**Six: fix internal links** to point at final addresses rather than through redirects. Missing this leaves the site working and the signals muddled.

Then wait. Recovery is not instant — engines re-crawl on their own schedule — and most of it typically comes back within one to two months when the redirects are right. Resist the urge to change things repeatedly while waiting, which makes it impossible to tell what worked.

## What You Cannot Fully Recover

Honesty matters here, because it changes the decision next time.

Redirects pass most, not all, of a page's accumulated reputation. Content genuinely deleted and not restored takes its rankings with it. And time spent out of the index is traffic you do not get back.

A rebuild done properly loses almost nothing. A rebuild done carelessly and repaired three months later typically recovers most of it and not all — which is why the cheapest version of this article is the checklist below, applied before launch rather than after.

## When the Rebuild Also Changes the Domain or the Language

Two variations that multiply the risk, and the rule for both is the same: change one thing at a time.

**A new domain.** Moving from one name to another — a rebrand, a shortened name, a `.nl` replacing a `.com` — is survivable and needs care. Redirect every old address to its exact counterpart on the new domain, one hop, permanently. Keep the old domain registered and the redirects live for years rather than months, because links on other people's sites do not update and neither do bookmarks. Tell your search console about the move using its change-of-address facility. And expect a dip of a few weeks even when everything is correct.

The mistake that makes this expensive is combining it with the rebuild. A new domain and new addresses and new page structure launched together produces a failure nobody can diagnose, because there is no way to tell which change caused what. Move the domain first with identical paths, confirm traffic is stable, then rebuild.

**Adding or splitting a language.** A Dutch site that gains an English version, or a bilingual site being reorganised, changes which address serves which visitor. Each language needs its own address, and the pages must declare the relationship between them so the engine understands they are alternatives rather than duplicates. Get this wrong and the two versions compete, and the one that wins is frequently the wrong one for the visitor.

A related trap: automatically redirecting visitors to a language based on their browser settings. It prevents a crawler from seeing all versions and it irritates the substantial number of Dutch professionals who prefer English documentation. Offer the choice, remember it, and let every version be reachable at its own address.

**Staging both.** Whichever you are doing, rehearse it. A copy of the redirect map tested against the real list of old addresses, run before launch, catches the missing entries that no amount of care catches by eye.

## Doing a Rebuild Without Losing Anything

Before you launch: export the complete list of current addresses with their traffic and their inbound links. Decide, for every one, where it goes. Build the redirect map first, as a file, and test it against the real list rather than a sample. Confirm every public page serves content in the initial response. Preserve titles, descriptions and structured data, improving rather than replacing them. Keep the pages that bring traffic even if they no longer fit the design — a page earning visitors is not clutter. Launch, then check the top fifty addresses within the hour, and watch indexing daily for two weeks.

An afternoon of preparation, against a quarter of lost enquiries.

## Getting It Repaired or Done Right

Whether you are planning a rebuild or three weeks into a bad one, this is bounded work: the full old-address list reconstructed from search console, analytics and archives; a complete redirect map built and tested; public pages restored to server-rendered HTML with per-page metadata; missing pages recovered; structured data and sitemap rebuilt; internal links pointed at final addresses; and re-indexing requested and monitored until traffic stabilises.

LaunchStudio does this regularly for Dutch companies whose new site arrived faster than their traffic recovered. Behind it is Manifera: eleven years of web work from Amsterdam Herengracht 420, with clients including Vodafone, TNO and CFLW.

[Send us the old and new addresses](https://launchstudio.eu/en/#contact) and you will get a diagnosis, usually within one business day, or see the [packages](https://launchstudio.eu/en/#packages).

## Real example

### Sixty-One Pages Became Nine

Annelies ter Horst runs Klusofferte in Ede: a quote-comparison service connecting homeowners with renovation contractors, earning its income from qualified leads. The site had been running for six years and brought roughly 4,800 visitors a month from search, almost entirely to long, specific pages — what a dormer costs in 2026, whether a permit is needed for a particular extension, how to check a contractor's registration.

She rebuilt it with Lovable in a fortnight. The new site was faster, looked far better, and the quote form converted noticeably higher.

It had nine pages. The 61 old ones had not been listed before the rebuild, and nobody had decided what happened to them. The new addresses used a different structure entirely, with no redirects. All public content rendered in the browser. Every page carried the same title.

Six weeks later, monthly visitors from search had fallen to about 600, and lead revenue with them.

Twelve business days of work: the old address list reconstructed from search console, four years of analytics and an archived crawl, producing 61 addresses of which 44 had received meaningful traffic; a redirect map built for every one, tested against the full list rather than a sample, with 9 addresses redirected to the closest new section and 35 pages restored outright because they had accumulated links and had no successor; those restored pages rewritten and updated where their figures or rules had gone out of date; all public pages moved to server-rendered HTML with distinct titles, descriptions and headings; structured data restored and extended to the FAQ sections; sitemap rebuilt and submitted; internal links pointed at final addresses; and re-crawling requested for the 20 highest-value pages.

**Result:** search traffic returned to roughly 3,900 a month by the end of the second month and passed the old level in the fourth, helped by the higher-converting form the rebuild had introduced. Two of the 35 restored pages never fully recovered their position.

> *"The new site was better in every way except the one that paid for it. I had deleted six years of pages without ever seeing a list of them."*
> — **Annelies ter Horst, Founder, Klusofferte (Ede)**

**Cost & Timeline:** €5,400 (address reconstruction, redirect mapping, restoration of 35 pages, server-rendered public pages, metadata and structured data, sitemap and re-indexing) — completed in 12 business days.

## Frequently Asked Questions

### Why did my traffic drop after a rebuild?

Most often because addresses changed without redirects, so every link and every indexed page now leads nowhere. Other common causes are content that only renders in the browser, pages silently dropped, identical titles, and a development no-index setting carried into production.

### Is redirecting everything to the home page acceptable?

No. A search engine treats a redirect to an unrelated page much as it treats a missing page. Each old address should go to its closest equivalent, with a permanent redirect and no chains.

### What if a page has no equivalent on the new site?

Consider restoring it. A page that earned links and visitors for years is worth more than design consistency, and pages with no successor are usually the long specific ones that brought the steadiest traffic.

### How long does recovery take?

Typically one to two months once redirects are correct, since engines re-crawl on their own schedule. Avoid changing things repeatedly while waiting, or you will not be able to tell what worked.

### How do I rebuild without losing rankings at all?

Export every current address with its traffic and inbound links before you start, decide where each one goes, build and test the redirect map as a file, keep pages that bring traffic, preserve metadata and structured data, and verify the top addresses within an hour of launch.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Why did my traffic drop after a rebuild?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Usually addresses changed without redirects, plus browser-only rendering, dropped pages, identical titles, or a no-index setting carried into production."
      }
    },
    {
      "@type": "Question",
      "name": "Is redirecting everything to the home page acceptable?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No — that is treated much like a missing page. Each old address should redirect to its closest equivalent, permanently and without chains."
      }
    },
    {
      "@type": "Question",
      "name": "What if a page has no equivalent on the new site?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Consider restoring it. Pages that earned links for years are worth more than design consistency, and they are often the steadiest traffic sources."
      }
    },
    {
      "@type": "Question",
      "name": "How long does recovery take?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Typically one to two months after redirects are correct, since re-crawling happens on the engine's schedule."
      }
    },
    {
      "@type": "Question",
      "name": "How do I rebuild without losing rankings at all?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Export every address with traffic and links first, map each to a destination, test the redirect map against the full list, keep traffic-earning pages, and verify after launch."
      }
    }
  ]
}
</script>
