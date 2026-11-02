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
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/how-do-i-add-a-blog-or-marketing-site-to-my-lovable-app" }
}
</script>

**Short answer:** for most SaaS founders, the most effective setup is a separate, server-rendered marketing site and blog on your main domain (`yourapp.nl`), using a CMS such as WordPress or a framework like Next.js or Astro, with the Lovable app on a subdomain (`app.yourapp.nl`). It gives you fast, crawlable pages that rank and get cited by AI assistants, while the app stays focused on logged-in users. Putting a blog inside the Lovable app is possible with prerendering, but harder to maintain for regular publishing.

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
