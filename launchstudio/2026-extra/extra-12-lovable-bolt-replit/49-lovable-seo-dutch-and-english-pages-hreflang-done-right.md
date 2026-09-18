---
Title: "Lovable SEO: Dutch and English Pages, hreflang Done Right"
Keywords: lovable seo, hreflang, bilingual site, nl-NL, en, language targeting, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: AI-Native Founder (Non-Technical)
---

# Lovable SEO: Dutch and English Pages, hreflang Done Right

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Lovable SEO: Dutch and English Pages, hreflang Done Right",
  "description": "A Dutch product with English pages needs search engines to serve the right one. URL structure, hreflang that actually validates, why automatic redirection hurts, and whether you need both languages at all.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-12-20",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/lovable-seo-dutch-and-english-pages-hreflang-done-right" }
}
</script>

Dutch founders reach this question early, because the Netherlands is a country where everyone reads English and almost everyone prefers Dutch when buying something that matters.

The technical part — telling search engines which version to show whom — is a solved problem with a specific implementation that is easy to get subtly wrong. The strategic part, which comes first, is whether you should have two languages at all.

## Answer the Strategic Question First

Two languages is roughly twice the content work, forever. Every article, every feature page, every change.

The cases where it is clearly right: you sell to both Dutch and international customers, or your product serves an industry where the working language genuinely differs, or you are targeting Belgium and Germany as well.

The cases where it is not: you sell only in the Netherlands. Your buyers are Dutch, they search in Dutch, and an English version competes with your own Dutch pages for the same audience while doubling your workload. One language done well beats two done at half depth, and the depth is what ranks.

The middle case, which is common: Dutch for everything that sells, English for documentation and technical content where the terminology is English anyway and where an international audience may find you. That is an asymmetric split, deliberately chosen, rather than a mirrored site.

## URL Structure

Three options, and for a small Dutch product one is clearly best.

**Subdirectories** — `yourproduct.nl/nl/` and `yourproduct.nl/en/` — keep everything on one domain, share whatever authority the domain has, and are simplest to host and maintain. This is the right default.

**Subdomains** — `nl.yourproduct.nl` — are more separated than most small products need.

**Separate domains** — a `.nl` and a `.com` — make sense when you genuinely operate as two businesses in two markets, and they mean building authority twice.

Whichever you choose, make the language explicit in the URL. A site that serves different content at the same URL depending on the visitor's browser settings cannot be indexed properly, because a crawler sees one version and has no way to reach the other.

## hreflang, Correctly

The mechanism that tells search engines these pages are translations of each other, so the right one is shown to the right person.

Four rules, and breaking any of them makes the whole thing inert.

**Every page lists every version, including itself.** The Dutch page names both the Dutch and the English URL; so does the English page. A page that omits itself is the most common error.

**It must be reciprocal.** If A points to B, B must point to A. One-directional declarations are ignored.

**Use correct codes.** `nl` for Dutch, `en` for English, `nl-BE` for Dutch in Belgium. The language comes first; a region alone is not valid.

**Include an x-default** naming the version to show when nothing matches — usually your English page, or a language selector.

Put them in the HTML head, pointing at absolute canonical URLs. And make sure the canonical link on each page points at itself rather than at the other language, which is an error that quietly removes one version from the index entirely.

## Do Not Redirect Automatically

The instinct is to detect the visitor's language or country and send them to the matching version. It causes more problems than it solves.

A crawler arriving from a US address is redirected to English and never sees the Dutch pages, so half your site goes unindexed. A Dutch speaker travelling abroad gets English. Someone who deliberately chose English is redirected back to Dutch on their next visit.

The approach that works: serve the URL that was requested, and offer the other version prominently — a clear language switcher, and a dismissible notice suggesting the alternative. Remember the choice, and let the user's explicit selection override any detection.

## Translate Properly, Including the Keywords

A translated page is not a translation of your keywords.

Dutch buyers search using Dutch terms, and the direct translation of your English keyword is frequently not the term people use. Sometimes the English word is what Dutch professionals actually search for; sometimes there is a Dutch term with far more volume. This has to be researched per market rather than assumed.

The same applies to the whole page. Titles, descriptions, headings, image alternatives and structured data all need their own language version — a Dutch page with an English title in search results is a page nobody clicks.

And translate the content rather than generating it: machine translation has improved enormously and still produces Dutch that reads as translated, which for a product selling trust to Dutch businesses is a cost that does not appear in any analytics.

## The Product Has a Language Too

Everything above concerns public pages. The application behind the login has a parallel set of decisions, and they are frequently made by accident in AI-built products.

The interface language should follow the user's own setting, stored on their account, not the browser's guess and not the marketing site's current path. A Dutch user who happens to open your product on an English-configured machine should still see Dutch.

Three things travel with that setting and are usually missed. Emails your product sends — confirmations, reminders, invoices — should be in the recipient's language, which means the template is selected per recipient rather than per application. Dates, numbers and currency formatting, where Dutch conventions differ from English ones in ways that look wrong immediately to a native reader. And exported documents, which are frequently generated from a template that was never translated at all.

Two implementation notes. Keep translations as data rather than as conditionals in your code, so adding a language is a file rather than a rewrite — and so an AI session adding a feature has an obvious place to put its strings rather than hard-coding English. And ensure the fallback is defined: a missing translation should show the default language, not an empty string or a raw key, which is how a product ends up displaying `dashboard.header.title` to a customer.

## Belgium Is Not the Netherlands

Founders who add Dutch pages often assume Flanders comes free. It mostly does, with three caveats worth knowing before you promise a Belgian customer anything.

The language differs in ways that are noticeable to a Belgian reader — vocabulary, some terminology, and a register that reads as distinctly Dutch-from-the-Netherlands. For marketing copy this is usually tolerable; for a product that positions itself as local, less so.

The practical differences matter more. Belgian business buyers frequently expect Bancontact at checkout. VAT numbers, company registration formats and invoicing conventions differ. And a Belgian customer searching will often be served results from Belgian domains preferentially, which is the one thing hreflang genuinely helps with: a `nl-BE` declaration, pointing at pages written for that market, tells search engines which version belongs there.

The question to answer before doing any of it is whether you have Belgian customers or merely Belgian traffic. Adding a `nl-BE` variant of every page to serve four visitors a month is the same trap as adding English for an audience you do not sell to.

The pragmatic sequence: sell to Belgium with your Dutch pages first, find out whether it works, and add market-specific pages once the revenue justifies maintaining them.

One more thing that costs nothing and helps disproportionately in both markets: state where your company is, on the page, in text. A Dutch address in the footer and an about page naming the city is a signal to search engines and a reassurance to buyers, and a surprising number of AI-built sites identify their company nowhere at all.

It also removes an ambiguity that hreflang cannot resolve on its own. A `.nl` domain carries some signal about where a business operates; a `.com` carries none, and for a Dutch company on a `.com` the address in the footer is doing work that nothing else does.

## Setting This Up

For an existing product this is typically two to three days: a decision about which languages and which content in each, language-explicit URLs with a subdirectory structure, complete reciprocal hreflang including self-references and an x-default, self-referencing canonical links per language, automatic redirection removed in favour of a clear switcher with a remembered preference, per-language titles, descriptions, headings, alternatives and structured data, keyword research per language rather than translated keywords, separate sitemaps per language, and validation in the search console to confirm the declarations are being read.

LaunchStudio does this for Dutch products selling into more than one market — and advises against a second language where the audience does not justify it. Behind the work is Manifera — eleven years, bilingual operations from Amsterdam, Singapore and Ho Chi Minh City.

[Ask us whether your second language is earning its keep](https://launchstudio.eu/en/#contact). Sometimes the answer is no.

## Real example

### Two Languages, One Audience

Sjoerd Waanders built Magazijnmaat in Lovable: warehouse and picking software for wholesalers and distributors, 48 customers, all Dutch.

He had built the site in English first because that is what his tools produced, then added Dutch pages a year later. Both versions existed at the same URLs, with the language chosen by browser detection and a redirect.

Nothing ranked. The search console showed the English pages indexed and the Dutch pages almost entirely absent, because crawlers arriving with non-Dutch settings were redirected to English every time and never saw them. The English pages, meanwhile, were competing for terms his actual buyers never searched — his customers were Dutch wholesalers searching for Dutch terms.

Three business days: language-explicit URLs introduced with `/nl/` and `/en/` subdirectories and permanent redirects from the old shared URLs; automatic redirection removed, replaced with a visible switcher and a dismissible notice that remembers the choice; complete reciprocal hreflang added including self-references and an x-default; canonical links corrected, since every Dutch page had been pointing at its English equivalent, which had been actively removing them from the index; per-language titles, descriptions and structured data; Dutch keyword research, which found that his customers searched for "magazijnsoftware" and "orderpicken software" with meaningful volume while the English terms he had optimised for had essentially none in the Netherlands; the Dutch pages rewritten around the actual terms rather than translated from English; separate sitemaps per language; and the English version reduced from a full mirror to six pages covering the product for an international audience, since maintaining two complete sites for one Dutch customer base was the underlying problem.

**Result:** the Dutch pages were indexed within three weeks and organic traffic went from 90 to 740 visits a month within four months, with 11 trial signups attributable to organic search in the fourth month against zero before. Sjoerd's assessment is that reducing the English site was as valuable as fixing the technical errors, because it halved the work of keeping the Dutch pages good.

> *"Every crawler that arrived was sent to the English site, so Google had never seen my Dutch pages at all. I had been writing them for a year for nobody."*
> — **Sjoerd Waanders, Founder, Magazijnmaat (Ede)**

**Cost & Timeline:** €3,200 (language-explicit URL structure with redirects, redirection removal and switcher, reciprocal hreflang, canonical correction, per-language metadata and structured data, Dutch keyword research and page rewriting, sitemaps, English site reduction) — completed in 3 business days.

## Frequently Asked Questions

### Do I need an English version if I only sell in the Netherlands?

Usually not. It doubles the work, competes with your own Dutch pages, and serves an audience you do not sell to. One language done thoroughly outranks two done at half depth.

### Should I redirect visitors based on their language or country?

No. It prevents crawlers from seeing one version entirely and overrides deliberate choices. Serve the requested URL and offer a clear switcher that remembers the preference.

### What is the most common hreflang mistake?

Omitting the self-reference, or making the declarations non-reciprocal. Either makes the whole set inert. A close second is canonical links pointing at the other language.

### Can I translate my keywords directly?

No. Dutch buyers frequently use different terms, and sometimes the English word is what they search for. Research each market rather than translating.

### Is machine translation good enough?

For understanding, yes. For pages selling to Dutch businesses, it reads as translated, and that cost does not appear in any analytics while affecting whether people trust you.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Do I need English pages if I only sell in the Netherlands?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Usually not — it doubles the work and competes with your Dutch pages. One language done thoroughly outperforms two done shallowly."
      }
    },
    {
      "@type": "Question",
      "name": "Should visitors be redirected by language or country?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No. It stops crawlers seeing one version and overrides deliberate choices. Serve the requested URL with a clear switcher."
      }
    },
    {
      "@type": "Question",
      "name": "What is the most common hreflang error?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Omitting the self-reference or non-reciprocal declarations, either of which makes the set ignored — followed by canonicals pointing at the other language."
      }
    },
    {
      "@type": "Question",
      "name": "Can keywords be translated directly?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No. Dutch buyers often use different terms, and sometimes the English word is the one searched. Research each language separately."
      }
    },
    {
      "@type": "Question",
      "name": "Is machine translation sufficient for marketing pages?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "It reads as translated to Dutch business buyers, and the cost to trust does not show up in analytics."
      }
    }
  ]
}
</script>
