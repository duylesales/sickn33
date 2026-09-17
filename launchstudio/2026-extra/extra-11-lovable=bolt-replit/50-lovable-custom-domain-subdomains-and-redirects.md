---
Title: "Lovable Custom Domain: Subdomains, Redirects and Multi-Brand Setups"
Keywords: lovable custom domain, lovable seo, subdomain versus subfolder, redirect configuration, staging subdomain, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: AI-Native Founder (Non-Technical)
---

# Lovable Custom Domain: Subdomains, Redirects and Multi-Brand Setups

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Lovable Custom Domain: Subdomains, Redirects and Multi-Brand Setups",
  "description": "Once one domain works, the questions multiply: app on a subdomain or a path, where staging lives, how redirects should behave, and what changes when you serve several brands. A practical structure for founders.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-07-22",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/lovable-custom-domain-subdomains-and-redirects" }
}
</script>

Connecting one domain to a Lovable app is a solved problem. What arrives next is less obvious and more consequential: should the application live at `app.yourdomain.nl` or at `yourdomain.nl/app`? Where does staging go? What happens to the old address when a page moves? And what changes when a customer asks whether the product can run under their own brand?

These are structural decisions. They are cheap now, moderately annoying in six months, and genuinely expensive after you have search visibility, saved bookmarks and integrations pointing at addresses you chose casually.

## Subdomain or Path: The Decision That Shapes Everything Else

Two arrangements, and the choice affects search, cookies, certificates and deployment.

**Application on a subdomain** — `app.yourdomain.nl` — with marketing pages on the root. This is the common arrangement for products, and it has practical advantages: the two can be hosted separately, deployed independently, and use different technology without interfering. It also keeps the application out of the way of anything you want indexed.

**Application on a path** — `yourdomain.nl/app` — keeps everything on one hostname. Analytics stays unified, cookies are simpler, and search signals accumulate to a single domain. The cost is that both halves must be served from the same place or routed carefully, which for a Lovable frontend plus separate marketing pages is more configuration than it sounds.

For a small product the pragmatic default is: application on `app.`, marketing on the root, and no agonising. Pick one before you have inbound links, because moving an application between the two later means redirects, reconfigured callbacks and re-authenticated sessions for every user.

## What Else Deserves Its Own Subdomain

**Staging.** Something like `staging.yourdomain.nl`, which should be blocked from search indexing and, ideally, behind a password. Staging environments discovered and indexed by a crawler are a recurring embarrassment — and occasionally worse, because they frequently contain a copy of real data.

**Transactional email.** A dedicated sending subdomain isolates your application's sending reputation from your personal and business email, which is why it is worth doing even for a product sending fifty messages a day.

**Documentation or support,** if you have them, though a path on the marketing site works equally well and consolidates your search signals.

**Customer-facing assets,** where you serve files or images at volume, which lets you cache them differently from your application.

What does not deserve a subdomain: a marketing campaign, a single landing page, or a blog. These belong as paths on your main site, where they contribute to the same domain rather than starting from nothing.

## Redirects: Small Rules That Prevent Slow Losses

Four cases cover nearly everything a small product needs.

**Apex to www, or the reverse.** Pick one canonical form and permanently redirect the other. Both work either way; having both serve content splits your search visibility and confuses analytics.

**Insecure to secure.** Every request over an insecure connection should redirect to the secure one, and this should be verified rather than assumed.

**Old paths to new.** When a page moves, redirect permanently from the old address. This preserves accumulated search value and stops the bookmarks and shared links you cannot see from breaking.

**The preview address.** Once your domain is live, the original platform URL should redirect to it or be blocked from indexing. Leaving both live and indexable is how a product ends up with a second, unbranded version of itself in search results.

One caution worth knowing: redirect chains — old address to another old address to the current one — lose value and slow loading. Redirect directly to the final destination each time you move something.

## Cookies, Sessions and the Subdomain Boundary

The detail that surprises founders after they add a second subdomain.

Cookies are scoped to a host by default. A session created on `app.yourdomain.nl` is not automatically available on `yourdomain.nl`, which means a user who logs into the application and then clicks through to your marketing site appears logged out. Whether that matters depends on your product — for many it does not — and if it does, cookies can be scoped to the parent domain so they are shared.

Sharing cookies across subdomains has a security consequence worth stating: a compromise or a careless script on any subdomain then has access to the session. For a small product with a staging subdomain containing test code, that is a real consideration rather than a theoretical one.

Decide deliberately: shared sessions across subdomains, or separate. Both are reasonable; discovering the answer through a confused user is not.

## Certificates Across Several Names

Every hostname you serve needs a valid certificate, and modern hosting issues and renews them automatically — for the names it knows about.

Two failure patterns. A subdomain added in DNS but never configured at the host, which resolves and then presents a certificate error. And a wildcard arrangement where the certificate covers one level of subdomain but not a deeper one.

The check is mechanical: open every hostname you serve, in a private window, on a device that has never visited it, and confirm the padlock. Do it after every change to your domain configuration, because certificate problems are silent until a visitor meets them.

## When a Customer Wants Their Own Brand

The request arrives once you sell to businesses: can this run at `planning.theircompany.nl`?

It is achievable and it is a product decision rather than a configuration one, because it introduces ongoing obligations. Each customer domain needs a certificate issued and renewed, DNS records the customer must add at their own registrar, and support when their IT department changes something. Your application also needs to know which brand it is serving, which affects sessions, emails and any link it generates.

For a small product, the sequence that works: start by offering a subdomain of your own domain per customer — `theircompany.yourdomain.nl` — which gives most of the perceived benefit with a fraction of the operational cost, and reserve genuine custom domains for customers who require them and are large enough to justify the work.

## A Structure That Holds Up

For most Dutch products this arrangement survives growth without rework:

- `yourdomain.nl` — marketing pages, canonical, with `www` redirecting to it or the reverse.
- `app.yourdomain.nl` — the application.
- `staging.yourdomain.nl` — protected and not indexed.
- `mail.yourdomain.nl` — transactional email sending only.
- Everything else as paths, not subdomains.
- One canonical form, permanent redirects for anything moved, and the preview address redirected.

Decide it once, write it down, and configure it before you have traffic. It takes an afternoon and removes a category of problem entirely.

## Getting It Configured Once, Properly

Domain structure is small work with a long tail of silent failures — certificates on a subdomain nobody checked, a staging environment in Google, callbacks pointing at a preview address, sessions that behave unexpectedly across hosts.

LaunchStudio sets it up as part of taking an AI-built product live: canonical form chosen and enforced, application and marketing separated cleanly, staging protected and excluded from indexing, sending subdomain configured with authentication records, certificates verified across every hostname, redirects mapped without chains, and provider callbacks swept — without touching the interface you built in Lovable.

Behind it is Manifera, eleven years of production engineering for clients including Vodafone, TNO and CFLW, from Amsterdam and Ho Chi Minh City. [Describe your project](https://launchstudio.eu/en/#contact) and you will get a domain structure you can grow into, usually within one business day, or see the [packages](https://launchstudio.eu/en/#packages).

## Write Down Your Domain Map

One page, kept with your other operational documents, listing every hostname you control and what it does. It takes fifteen minutes and it prevents a category of problem that otherwise recurs indefinitely.

**For each hostname:** what serves it, where the DNS is managed, whether it has a certificate and how that renews, whether it should be indexed, and who set it up.

**Include the ones you are not using.** Domains bought defensively, an old brand, a campaign address from last year. These are the ones that expire without anyone noticing, and an expired domain that still has DNS records pointing somewhere is occasionally worse than no domain at all.

**Note the registrar and the renewal date,** with the payment method. Domain expiry through a lapsed card is a genuinely common way for small products to go dark, and it happens on a Saturday.

**Record who has access** to the registrar and the DNS provider, which belongs in the same access review as everything else.

The reason to write it down rather than remember it: domain configuration is touched rarely and changed by whoever is nearest at the time. Six months later, nobody can say why a subdomain exists, whether anything depends on it, or whether removing it is safe — and the safe assumption becomes leaving it, which is how an unmaintained subdomain ends up serving an old version of your product to somebody.

## Before You Buy a Second Domain

Founders frequently buy a second domain — a variant spelling, a Dutch and an English version, a shorter one for campaigns — and then have to decide what it does.

The useful default is that a second domain redirects to your primary one and serves nothing of its own. That protects the name, catches typos and misremembered spellings, and keeps every signal consolidated on a single address.

Running genuine content on a second domain is a decision to maintain two of everything — two sets of pages, two certificates, two places search engines index, and two chances to leave one out of date. For a small product it is almost never worth it, and the exception is a genuinely separate brand rather than a variation of the same one.

If you do buy variants, register them at the same registrar as your main domain, on the same renewal cycle, and add them to your domain map.

## Real example

### A Staging Environment That Ranked Better Than the Product

Wouter Claassen ran Zaalplanner, a venue-booking tool built in Lovable for community centres and sports halls around Tilburg. The marketing site and the application both sat on the root domain, and a staging copy had been set up months earlier at an address nobody had thought about since.

Two problems surfaced in the same week. A prospective customer searching for the product found the staging site first, complete with test bookings carrying real-looking names, because nothing prevented it from being indexed. And a venue manager reported that logging into the application signed her out of the booking calendar — a session scope problem introduced when part of the product had been moved to a subdomain without adjusting cookie configuration.

Three business days of work: staging moved behind a password and excluded from indexing, with the indexed pages removed through Search Console; the application separated onto `app.` deliberately, with sessions scoped to the parent domain so both halves shared a login; the canonical form fixed with permanent redirects; certificates verified across all four hostnames on a phone over mobile data; the original preview address redirected; and a sending subdomain configured with authentication records, which incidentally improved email deliverability.

**Result:** the staging pages disappeared from search within three weeks, the session issue ended, and Wouter now has a written structure he applied without thinking when adding a documentation site two months later.

> *"A prospect found my test environment before they found my product, and it was full of fake bookings with real-sounding names. That was a memorable morning."*
> — **Wouter Claassen, Founder, Zaalplanner (Tilburg)**

**Cost & Timeline:** €1,600 (domain structure, staging protection, session scoping, certificates and redirects, sending subdomain) — completed in 3 business days.

## Frequently Asked Questions

### Should my app be on a subdomain or a path?

For most small products, the application on `app.` with marketing on the root is the pragmatic default: the two can be hosted and deployed independently. A path keeps analytics and cookies simpler but requires more routing configuration. Decide before you have inbound links.

### Where should my staging environment live?

On its own subdomain, password-protected and excluded from search indexing. Staging environments that get indexed are a recurring embarrassment, and they frequently contain a copy of real data.

### Do sessions work across subdomains?

Not by default — a session on `app.yourdomain.nl` is not available on the root. Cookies can be scoped to the parent domain to share them, at the cost of any subdomain compromise having access to the session. Decide deliberately.

### Can I let customers use their own domain?

Technically yes, and it brings ongoing obligations: certificates per customer domain, DNS records they must add, and support when their IT changes something. Offering a subdomain of your own domain per customer gives most of the benefit for far less operational cost.

### What should happen to my old preview URL?

Redirect it to your real domain, or block it from indexing if redirection is impossible. Leaving both live and indexable produces a second, unbranded version of your product competing with you in search results.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Should my app be on a subdomain or a path?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "For most small products, the application on app. with marketing on the root is the pragmatic default, since both can be hosted and deployed independently. Decide before you have inbound links."
      }
    },
    {
      "@type": "Question",
      "name": "Where should my staging environment live?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "On its own subdomain, password-protected and excluded from indexing, since staging environments often contain a copy of real data."
      }
    },
    {
      "@type": "Question",
      "name": "Do sessions work across subdomains?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Not by default. Cookies can be scoped to the parent domain to share sessions, at the cost of any subdomain compromise having access to them."
      }
    },
    {
      "@type": "Question",
      "name": "Can I let customers use their own domain?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes, with ongoing obligations for certificates, customer DNS records and support. A subdomain per customer on your own domain gives most of the benefit far more cheaply."
      }
    },
    {
      "@type": "Question",
      "name": "What should happen to my old preview URL?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Redirect it to your real domain, or block indexing if that is impossible, so you do not compete with an unbranded copy of your product."
      }
    }
  ]
}
</script>
