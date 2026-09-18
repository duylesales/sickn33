---
Title: "Lovable SEO: Architecture for an App With a Marketing Front"
Keywords: lovable seo, site architecture, rendering, indexable pages, app subdomain, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: AI-Native Founder (Non-Technical)
---

# Lovable SEO: Architecture for an App With a Marketing Front

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Lovable SEO: Architecture for an App With a Marketing Front",
  "description": "An AI-built product is one application serving two audiences with opposite needs. How to structure marketing pages and the logged-in app so search engines can read one and never see the other.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-12-16",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/lovable-seo-architecture-for-an-app-with-a-marketing-front" }
}
</script>

A product built with Lovable is usually one application doing two jobs. It shows marketing pages to strangers who must be able to find them, and it runs a logged-in application for customers which no search engine should ever see.

Those two jobs have opposite requirements, and the default output serves neither well: the marketing pages are rendered by JavaScript in a way that makes them slow and sometimes invisible to search engines, while the application's routes are technically crawlable and occasionally appear in results as empty pages titled "Loading".

The fix is architectural and it is easier before you have traffic than after.

## Why Generated Pages Struggle

The output of these tools is typically a single-page application. The server sends a near-empty HTML document and JavaScript builds the page in the browser.

Search engines can execute JavaScript, so this is not fatal. It is, however, a handicap: rendering is queued and delayed rather than immediate, any failure in your script means the page has no content at all, and the same page is slower for every visitor on a mid-range phone.

The alternative is that the server sends real HTML — either generated at build time for pages that rarely change, or rendered per request. Marketing pages, blog articles and public listings all belong in that category, and for a small product static generation at build time is both the fastest and the simplest option.

This is the decision that determines everything else, and it is the one most likely to require restructuring later if it is left alone.

## Separate the Two Halves

Draw a clear line between what is public and what is behind a login.

Everything public — home, product pages, pricing, blog, documentation, public listings — is statically generated, cached at the edge, and indexable.

Everything private — dashboards, settings, customer data, anything after a sign-in — is excluded from indexing entirely, and there is no reason for it to be fast to a crawler because no crawler should be there.

Two ways to draw the line. A path prefix, with the application under something like `/app`, which keeps one domain and is simplest. Or a subdomain, with `app.yourproduct.nl` separate from the marketing site, which allows the two to be built and deployed independently.

Path prefixes suit most small products. Subdomains earn their complexity when the marketing site is managed separately, for instance in a CMS your marketing person edits without touching the application.

## Exclude the Application Properly

Founders rely on robots.txt for this, and it does the wrong thing.

Disallowing a path in robots.txt asks crawlers not to visit. It does not prevent a page from being indexed if it is linked from elsewhere — which produces the worst outcome: a result in search with your URL, no description, and no way for the crawler to see that it should not be there, because you told it not to look.

The reliable mechanism is a noindex directive on the pages themselves, served in the HTML or as a header, which crawlers must fetch the page to see. So: allow crawling of the application's routes, and tell them clearly not to index. Combine with authentication, which means most of the content is not reachable anyway.

Where this matters more than founders expect is preview deployments, which are frequently public URLs containing a complete copy of your site and, without a directive, are indexable duplicates of everything.

## One URL Per Page

Duplicate content in AI-built sites comes from a small set of causes, and each is a one-line fix.

The same page reachable with and without a trailing slash, with and without `www`, over both HTTP and HTTPS, with query parameters from campaigns appended, and at both `/blog/post` and `/blog/post/`. Each variation is a separate URL that a crawler may treat as a separate page.

Pick one form, redirect the others to it permanently, and put a canonical link on every page naming its preferred URL. It is fifteen minutes and it removes an entire category of problem that otherwise dilutes every page you publish.

## The Pages Worth Having

Architecture is only useful if there is something to index. A product's public surface should at minimum include a home page that says plainly what the product does and for whom, a page per significant feature or use case, a pricing page with actual prices, an about page identifying the company and the people, and contact details.

Then the pages that earn traffic over time: articles answering the questions your customers asked before they bought, comparisons against the alternatives they considered, and documentation if your product has any depth.

For a Dutch product there is a further consideration covered elsewhere in this series: whether those pages exist in Dutch, English, or both, and how they are related to each other.

## Check What the Server Actually Sends

The single most useful diagnostic in this area takes ten seconds and almost nobody runs it: fetch your own page the way a crawler does, without a browser, and read what comes back.

From a terminal, request the URL and look at the HTML. If your headline, your body copy and your links are in that response, search engines can read the page immediately. If what comes back is a container div and a script tag, everything depends on rendering that may be delayed or may fail.

Do the same for three or four page types — home, an article, a feature page, a pricing page — because in a partially migrated site they frequently differ.

Two related checks worth the same ten seconds. Confirm that your internal links are real anchors with href attributes rather than click handlers on divs, because a crawler follows the former and cannot see the latter. And confirm the response status is what you expect: a page that returns 200 for a URL that does not exist means every mistyped link becomes an indexed empty page, which is a surprisingly common configuration in single-page applications where the server returns the same document for everything.

These three checks tell you more about whether a site can rank than any audit tool, and they are the first things to verify after any change to how pages are built.

## The Titles and Descriptions Generated Sites Share

A single-page application typically has one title, defined once in the document, and it stays the same on every route. Every page in search results then carries the same text, which is both unhelpful to a reader choosing between results and a wasted opportunity on every page you publish.

Each page needs its own title and description, written for that page. A title is roughly sixty characters and should name the specific thing plus, where it fits, the product or company. A description is roughly a hundred and sixty characters and is an advertisement rather than a summary — its job is to make someone click, not to restate the heading.

Three habits make this manageable rather than tedious. Set them where the page's content is defined, so writing a new article means writing its title and description at the same time. Generate them from the content for pages that are produced from data, with a pattern that produces something specific rather than a template with a variable slotted in. And check them in bulk occasionally — a list of every page's title and description, read in one sitting, makes duplicates and omissions obvious in a way that reviewing pages individually never does.

The same applies to the preview shown when a link is shared in a message or a social post. A generated site usually has one image and one description for the entire domain, so every article shared looks identical.

## Setting This Up

For an existing product this is typically two to three days: public pages moved to static generation or server rendering with real HTML in the response, the public and private halves separated by path prefix or subdomain, the application excluded from indexing with a noindex directive rather than robots.txt alone, preview deployments protected and excluded, one canonical URL per page with permanent redirects from every variation, a sitemap generated from actual routes and submitted, structured data on the pages where it applies, and the public surface reviewed for the pages a buyer would look for and cannot currently find.

LaunchStudio does this as part of making an AI-built product findable, which is frequently the first growth work a launched product needs. Behind it is Manifera — eleven years, 160+ projects, with European client contact from Herengracht 420 in Amsterdam.

[Ask us what a search engine currently sees on your home page](https://launchstudio.eu/en/#contact). It is sometimes nothing.

## Real example

### A Product Nobody Could Find

Jasmijn Kolthof built Voorraadslim in Lovable: stock management for independent retailers and webshops, 130 customers acquired almost entirely through a Facebook group and word of mouth.

She had written eleven articles about stock management over a year and none of them appeared in search results for anything. Her home page did not rank for her own product name.

The site was a single-page application. The HTML served for every URL was identical — an empty container and a script — with the content assembled in the browser. Search engines had indexed the home page with the title "Voorraadslim" and no description, and had indexed nothing else because the internal links were handled entirely in JavaScript with no real href attributes. Additionally, 40 application routes were indexable and four had been indexed as empty pages, one of them titled "Loading...". The same content was reachable at four URL variations, and three preview deployments were fully indexed as duplicates of the whole site.

Four business days: public pages converted to static generation so the server returns complete HTML, with the articles, feature pages and pricing built at deploy time; internal links rewritten as real anchors with href attributes; the application moved under an `/app` prefix and excluded with a noindex directive, with robots.txt adjusted to permit crawling so the directive can be seen; preview deployments put behind access protection and excluded; a single canonical URL form chosen with permanent redirects from the www, trailing slash and HTTP variations, and a canonical link on every page; a sitemap generated from the actual route list and submitted; article structured data added; the four indexed application pages removed from the index through the search console; and two missing pages written — a pricing page with real prices, which had never existed, and an about page identifying the company.

**Result:** within eight weeks, nine of the eleven articles were indexed and ranking, and organic visits went from 40 a month to 610. Two of the articles now bring more trial signups than the Facebook group. Jasmijn's note is that she had written the content a year earlier and nothing had been wrong with it — it simply could not be read.

> *"I thought my articles were not good enough. They had never been seen. The server was sending an empty page to everyone, and only browsers were putting the words in."*
> — **Jasmijn Kolthof, Founder, Voorraadslim (Zutphen)**

**Cost & Timeline:** €3,500 (static generation for public pages, real internal links, application separation and noindex, preview protection, canonical URLs and redirects, sitemap, structured data, index cleanup, missing pages) — completed in 4 business days.

## Frequently Asked Questions

### Can search engines read JavaScript-rendered pages?

They can execute JavaScript, but rendering is delayed and fragile, and a script failure means no content at all. Public pages should be served as real HTML, generated at build time where possible.

### Should my app be on a subdomain or a path?

A path prefix such as `/app` is simplest and suits most small products. A subdomain earns its complexity when the marketing site is built or managed separately.

### Is robots.txt enough to keep my app out of search?

No. It asks crawlers not to visit but does not prevent indexing of linked URLs, which produces results with no description. Use a noindex directive on the pages themselves.

### Why do the same pages appear at several URLs?

Trailing slashes, www, HTTP, and campaign parameters each create a variation. Choose one form, redirect the others permanently, and add a canonical link to every page.

### What public pages should exist at minimum?

A home page saying plainly what the product does, a page per significant use case, real prices, an about page identifying the company, and contact details — then articles answering pre-purchase questions.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Can search engines read JavaScript-rendered pages?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "They can, but rendering is delayed and fragile. Public pages should return real HTML, statically generated where possible."
      }
    },
    {
      "@type": "Question",
      "name": "Should the app live on a subdomain or a path?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "A path prefix like /app suits most small products; a subdomain is worthwhile when the marketing site is managed separately."
      }
    },
    {
      "@type": "Question",
      "name": "Does robots.txt keep an app out of search results?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No — it prevents crawling, not indexing of linked URLs. Use a noindex directive the crawler can actually fetch."
      }
    },
    {
      "@type": "Question",
      "name": "Why does one page appear at several URLs?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Trailing slashes, www, HTTP and campaign parameters each create variants. Redirect to one canonical form and declare it on every page."
      }
    },
    {
      "@type": "Question",
      "name": "What public pages does a product need at minimum?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "A clear home page, a page per use case, real prices, an about page identifying the company, and contact details."
      }
    }
  ]
}
</script>
