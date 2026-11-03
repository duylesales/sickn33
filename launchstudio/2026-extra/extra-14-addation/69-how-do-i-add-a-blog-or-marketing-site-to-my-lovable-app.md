---
Title: "How Do I Add a Blog or Marketing Site to My Lovable App?"
Keywords: blog for lovable app, marketing site saas, lovable app and website, subdomain app marketing site, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: SaaS Founder Scale-Up
---

# How Do I Add a Blog or Marketing Site to My Lovable App?

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "How Do I Add a Blog or Marketing Site to My Lovable App?",
  "description": "A blog inside a client-rendered Lovable app struggles to rank. This guide compares three setups for adding a blog and marketing pages: inside the app with prerendering, a CMS on the main domain with the app on a subdomain, or a static site generator, with SEO and AI-citation trade-offs.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-03-17",
  "inLanguage": "en",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/how-do-i-add-a-blog-or-marketing-site-to-my-lovable-app" },
  "citation": [
    { "@type": "CreativeWork", "name": "Google: Creating helpful, reliable, people-first content", "url": "https://developers.google.com/search/docs/fundamentals/creating-helpful-content" },
    { "@type": "CreativeWork", "name": "Google SEO Starter Guide", "url": "https://developers.google.com/search/docs/fundamentals/seo-starter-guide" },
    { "@type": "CreativeWork", "name": "Google: Introduction to structured data", "url": "https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data" },
    { "@type": "CreativeWork", "name": "Google: JavaScript SEO basics", "url": "https://developers.google.com/search/docs/crawling-indexing/javascript/javascript-seo-basics" }
  ]
}
</script>

**Short answer:** for most SaaS founders, the most effective setup is a separate, server-rendered marketing site and blog on your main domain (`yourapp.nl`), using a CMS such as WordPress or a framework like Next.js or Astro, with the Lovable app on a subdomain (`app.yourapp.nl`). It gives you fast, crawlable pages that rank and get cited by AI assistants, while the app stays focused on logged-in users. Putting a blog inside the Lovable app is possible with prerendering, but harder to maintain for regular publishing.

## Key Takeaways

- **For most SaaS founders, a separate, server-rendered marketing site and blog on the main domain, with the Lovable app on a subdomain, performs best** for search and AI citation.
- **A blog inside a client-rendered Lovable app can work** with prerendering, but is harder to maintain for regular publishing.
- **Google's guidance rewards helpful, people-first content** with clear expertise; publishing workflow and site structure matter as much as technology.
- **Structured data, internal links and consistent company information** help search engines and AI assistants understand and cite your pages.
- **Keep the handoff between site and app smooth:** consistent design, clear sign-up links and correct authentication redirects for the app subdomain.

## Three Setups Compared

| Setup | SEO and AI citation | Effort to publish | Best for |
| --- | --- | --- | --- |
| Blog inside the Lovable app, prerendered | Good if prerendering is maintained | Each post is a code change or needs a CMS integration | A few landing pages, rare posts |
| CMS (e.g. WordPress) on main domain, app on subdomain | Very good, mature SEO tooling | Write and publish in an editor | Regular publishing, non-technical writers |
| Static site generator or Next.js on main domain | Very good, very fast | Markdown or headless CMS | Founders comfortable with code or a developer |

## Why Not Just Prompt a Blog Into Lovable?

You can, and for a handful of pages it works. For a content strategy with dozens or hundreds of posts, problems appear: client-side rendering that some crawlers do not execute, every post needing a deployment, no editorial workflow, and SEO plugins and structured data you would have to build yourself. Our article on [whether Google can index Lovable apps](https://launchstudio.eu/en/blog/can-google-index-my-lovable-app) explains the rendering issue.

## Making the Split Setup Work

1. **Domains.** Marketing on `yourapp.nl`, app on `app.yourapp.nl`. Update Supabase redirect URLs for the app subdomain.
2. **Navigation.** "Log in" and "Start free" buttons on the marketing site link to the app; the app links back to pricing and help.
3. **Design consistency.** Reuse colours, fonts and logo so the jump feels seamless.
4. **Tracking.** If you use analytics across both, configure it for both domains and respect cookie consent.
5. **Sign-up handoff.** Pass the chosen plan from the marketing site to the app's sign-up via URL parameters.

## SEO and GEO Essentials for the Marketing Site

- Unique titles and descriptions per page
- Structured data: Organization, Product or SoftwareApplication, FAQPage, Article
- Clear pricing and feature pages in plain text
- Internal links from blog posts to the relevant product or service pages
- An about page that names your company, location and people, which helps AI assistants understand who you are

## Why Content Matters for SaaS Growth

For many SaaS companies, content is a durable acquisition channel. Articles that answer real questions attract visitors searching for solutions, build trust before a sales conversation and increasingly get cited by AI assistants. Google's guidance on helpful, reliable, people-first content describes what works: content created for people, demonstrating first-hand expertise, providing substantial value and clearly identifying who is behind it. A blog full of generic articles written only to rank tends to underperform; a smaller set of genuinely useful pages compounds over time.

## Choosing a Platform for Marketing and Blog

| Platform | Strengths | Considerations |
| --- | --- | --- |
| WordPress | Mature editor, SEO plugins, large ecosystem | Needs updates and security maintenance |
| Headless CMS with Next.js or Astro | Fast, flexible, modern | Requires a developer for setup |
| Static site generator with Markdown | Very fast, simple hosting | Writers need to be comfortable with Markdown or a Git-based editor |
| Lovable with prerendering | One tool for everything | Publishing requires prompts or code changes |

The best choice depends on who writes. If non-technical team members publish weekly, a CMS with a friendly editor matters more than technical elegance.

## Site Structure That Helps Search and AI

Organise content around topics your customers care about. A clear structure might include: homepage, product or features pages, use cases by customer type, pricing, a resources section with articles grouped by topic, case studies and an about page. Link related articles to each other and to the relevant product pages. Google's SEO starter guide recommends descriptive URLs, logical site hierarchy and meaningful internal links; the same structure helps AI assistants understand your expertise.

## Structured Data for Marketing Sites

Add Organization structured data with your legal name, logo, contact details and social profiles; Article structured data on blog posts with author and dates; FAQPage on genuine FAQ sections; and BreadcrumbList for navigation. Google's structured data documentation explains requirements. Consistency matters: your company name, address and details should match across your site, Google Business Profile and other listings.

## Writing for AI Assistants as Well as Search

AI assistants answer questions by summarising sources they trust. Pages that state a direct answer early, use clear headings, include specific facts such as prices, steps and locations, and show who is behind the content are more likely to be cited. Avoid hiding key information in images or interactive widgets. Update pages when facts change; outdated prices or steps damage trust with both people and machines.

## Measuring Content Performance

Use Google Search Console for impressions, clicks and queries per page, and your analytics tool, configured with appropriate consent, for engagement and conversions from content to sign-up. Review monthly: which articles bring visitors, which convert, which queries you appear for but do not answer well. Update and expand the articles that perform best rather than only writing new ones.

## Legal and Privacy Considerations

Marketing sites usually use analytics and sometimes advertising pixels. Under e-privacy rules, non-essential cookies and tracking require consent in the EU; implement a consent banner that genuinely blocks trackers until consent is given. Keep your privacy statement accurate for both the marketing site and the app, and show your company details clearly, as Dutch and EU rules expect.

## A Content Plan for the First Three Months

| Month | Focus | Examples |
| --- | --- | --- |
| 1 | Foundation pages | Features, pricing, about, three cornerstone guides for your main customer problem |
| 2 | Questions customers ask | Answers to the ten most common sales or support questions |
| 3 | Comparisons and use cases | Your product versus alternatives; one page per customer segment |

Publish consistently rather than in bursts, and update the best-performing pages as you learn more.

## Technical Setup Checklist

- Marketing site on the main domain, app on a subdomain
- Supabase site URL and redirect list updated for the app subdomain
- Sign-up and login buttons linking to the app, with plan parameters where useful
- Sitemap, robots.txt and canonical URLs on the marketing site
- Structured data for organisation, articles and FAQs
- Consent banner blocking non-essential trackers until accepted
- Consistent branding across site and app
- Analytics events for sign-ups originating from content

## Common Mistakes

- Publishing dozens of thin articles targeting slight keyword variations
- Leaving the app's preview domain indexable
- Hiding pricing behind a contact form when competitors show it
- Forgetting to update old articles when the product changes
- Measuring traffic but not sign-ups from content

## Using AI to Write Content

AI tools can help draft content, but Google's guidance focuses on whether content is helpful, original and demonstrates expertise, regardless of how it was produced. Use AI for outlines and first drafts, then add what only you know: real customer examples, specific numbers, opinions from experience and up-to-date facts. Review every claim. Content that reads like everyone else's earns neither rankings nor citations.

## The Payoff

A well-structured marketing site and blog becomes an asset that compounds: each useful article keeps attracting the right visitors, supports sales conversations and gives AI assistants reasons to recommend you. Separating it from the app lets each do its job well.

## Questions to Answer Before Choosing

Who will write and publish content, and how comfortable are they with technical tools? How often will you publish? Do you need multiple languages, such as Dutch and English? Which pages must rank for which searches? How much design control do you need? The answers usually point clearly to a CMS, a framework or prerendering inside Lovable.

## Related Reading

Our guides on whether Google can index a Lovable app, v0 versus Lovable and Dutch and English versions of your app cover rendering, framework choice and multilingual SEO in more depth.

## Summary

Put content where it can be crawled, published easily and measured, keep the app focused on logged-in users and connect the two with consistent design and clear sign-up paths. That setup serves people, search engines and AI assistants equally well.

## The Role of Your About Page

An about page is easy to neglect and important for trust. Describe who you are, where you are based, why you built the product and who is behind it, with real names and photos where appropriate. Search engines and AI assistants use these signals to judge expertise and trustworthiness, and customers read them before buying. For Dutch businesses, include company details such as KvK number on the site as well.

## Where to Start Today

List the ten questions prospects ask most often. Each one is a candidate for a page that answers it clearly on a crawlable marketing site.

## The Payoff

Content that ranks and gets cited keeps working long after you publish it, bringing qualified visitors to your app every month.

## Getting It Set Up

LaunchStudio sets up the domain split, sign-up handoff and redirects as part of launches, and can connect a marketing site to your app. LaunchStudio is powered by Manifera, which builds websites and web applications for clients from Amsterdam and Ho Chi Minh City, including WordPress, Next.js and React projects; see [Manifera's web app development](https://www.manifera.com/services/web-app-develop/). Google's [SEO starter guide](https://developers.google.com/search/docs/fundamentals/seo-starter-guide) covers the basics for any marketing site.

## Real example

### An AI-Native Founder in Action: The Blog Nobody Could Find

Mila Vermeer built Zzp-Administratie in Lovable: a bookkeeping helper for Dutch freelancers, with expense scanning and quarterly BTW overviews. She wrote 25 helpful articles about freelancer taxes inside the Lovable app, each as a separate route. After five months, Search Console showed three of them indexed, and none ranked.

Every article shared the same title tag, the content was rendered client-side, there was no sitemap, and publishing a new article meant prompting Lovable and redeploying, which sometimes broke unrelated pages.

LaunchStudio moved the marketing pages and blog to a WordPress site on the main domain with an SEO plugin, structured data and a sitemap, migrated the 25 articles with redirects from the old routes, moved the app to `app.` subdomain with updated auth redirects, and connected "Start free" buttons to the app's sign-up with the selected plan.

**Result:** Within three months, all articles were indexed and several ranked on the first page for freelancer BTW questions. Blog-driven sign-ups became the app's largest acquisition channel.

> *"I was writing good articles into a place search engines could barely read."*
> - **Mila Vermeer, Founder, Zzp-Administratie (Rotterdam)**

**Cost & Timeline:** €2,900 (domain split, WordPress setup with SEO, article migration and redirects, app subdomain and sign-up handoff) - completed in 9 business days.

## Frequently Asked Questions

### Should my blog be on a subdomain or the main domain?

Usually the main domain, with the app on a subdomain such as `app.`. Your main domain then accumulates the authority of your content, and the app remains separate.

### Can I build my marketing site in Lovable too?

You can, especially for a few landing pages, ideally with prerendering. For regular publishing and strong SEO, a CMS or server-rendered framework is easier to maintain and more reliably crawled.

### How do users move from the blog to my app?

Through clear links such as "Log in" and "Start free" that point to your app's sign-up or login, optionally passing the chosen plan as a parameter. Consistent design makes the transition feel natural.

### How does Manifera approach marketing sites for SaaS clients?

As a separate product with its own goals: speed, crawlability and easy publishing. Manifera's 11+ years of web projects show that separating marketing and app avoids compromises on both sides.

### Does a blog help my product appear in AI assistant answers?

Yes, if the content is clear, specific and crawlable. AI assistants cite pages that answer questions directly, with facts such as prices, locations and steps. A well-structured blog is one of the best ways to be cited.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Should my blog be on a subdomain or the main domain?",
      "acceptedAnswer": { "@type": "Answer", "text": "Usually the main domain, with the app on a subdomain like app." }
    },
    {
      "@type": "Question",
      "name": "Can I build my marketing site in Lovable too?",
      "acceptedAnswer": { "@type": "Answer", "text": "For a few prerendered pages yes; regular publishing is easier with a CMS or server-rendered framework." }
    },
    {
      "@type": "Question",
      "name": "How do users move from the blog to my app?",
      "acceptedAnswer": { "@type": "Answer", "text": "Via clear Log in and Start free links to the app, optionally passing the plan." }
    },
    {
      "@type": "Question",
      "name": "How does Manifera approach marketing sites for SaaS clients?",
      "acceptedAnswer": { "@type": "Answer", "text": "As a separate product optimised for speed, crawlability and publishing." }
    },
    {
      "@type": "Question",
      "name": "Does a blog help my product appear in AI assistant answers?",
      "acceptedAnswer": { "@type": "Answer", "text": "Yes, when content is clear, specific and crawlable." }
    }
  ]
}
</script>
