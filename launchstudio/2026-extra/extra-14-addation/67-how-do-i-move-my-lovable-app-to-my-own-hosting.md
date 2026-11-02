---
Title: "How Do I Move My Lovable App to My Own Hosting?"
Keywords: lovable own hosting, deploy lovable to vercel, lovable netlify, self host lovable app, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: Technical Solo Founder / Indie Hacker
---

# How Do I Move My Lovable App to My Own Hosting?

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "How Do I Move My Lovable App to My Own Hosting?",
  "description": "Moving a Lovable app from Lovable's publishing to your own host gives you control over deployments, regions, previews and rollbacks. This guide covers choosing a host, connecting GitHub, environment variables, SPA routing, the domain switch and what changes in your workflow.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-03-15",
  "inLanguage": "en",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/how-do-i-move-my-lovable-app-to-my-own-hosting" }
}
</script>

**Short answer:** sync your Lovable project to GitHub, import that repository into a host such as Vercel, Netlify or Cloudflare Pages, set the build command and environment variables, add a rewrite so all routes serve `index.html`, test on the host's preview URL, then point your domain's DNS to the new host. Your Supabase backend stays where it is. Afterwards, Lovable remains your editor, but your host decides what goes live.

## Why Founders Move

- **Control over releases:** staging, previews per change and instant rollback
- **Independence** from the builder's publishing (see our article on [what happens if Lovable changes](https://launchstudio.eu/en/blog/what-happens-to-my-app-if-lovable-changes-pricing-or-shuts-down))
- **Regions and performance:** choose where functions run and use a CDN you configure
- **Team workflows:** developers can deploy without access to the builder
- **Contracts:** customers sometimes ask where and how the app is hosted

## Choosing a Host

| Host | Strengths for Lovable apps |
| --- | --- |
| Vercel | Simple Git integration, previews, good DX |
| Netlify | Similar features, straightforward redirects |
| Cloudflare Pages | Global CDN, generous free tier |
| Managed hosting (e.g. LaunchStudio's €49/month) | Hosting, SSL, monitoring, backups handled for you |

For a Vite-based React app, any of these work well.

## Step-by-Step

1. **GitHub.** Make sure the Lovable project is synced to a repository in your company organisation.
2. **Import.** Create a project on the host from that repository.
3. **Build settings.** Build command `npm run build`, output directory `dist` (for typical Vite setups).
4. **Environment variables.** Add your Supabase URL and public key and any other frontend variables, with the `VITE_` prefix your code expects. Never add secret keys to frontend variables.
5. **Routing.** Add a rewrite so every path serves `index.html`, otherwise deep links return 404. Our [Bolt deployment article](https://launchstudio.eu/en/blog/why-does-my-bolt-app-break-after-deploy) explains this in detail; it applies equally to Lovable.
6. **Test the preview URL.** Log in, check main flows, payments in test mode.
7. **Update allowed URLs.** Add the new domain to Supabase Auth redirect URLs, OAuth providers and payment provider settings.
8. **Switch DNS.** Point your domain to the new host and wait for SSL to be issued.
9. **Disconnect old publishing.** Remove or redirect the old published URL so there is one canonical site.

## What Changes in Your Workflow

Lovable keeps syncing with GitHub. Every commit triggers a deploy on your host, ideally to staging first. You promote to production deliberately, as described in our [CI/CD guide](https://launchstudio.eu/en/blog/how-do-i-set-up-automatic-deployments-for-a-lovable-or-bolt-app).

## Getting It Done

Moving a Lovable app to independent hosting usually takes one to three days within a Launch Ready package, or is included when you choose LaunchStudio's managed hosting. LaunchStudio is powered by Manifera, which deploys on Vercel, Netlify, AWS, Azure and DigitalOcean for clients, coordinated from Amsterdam and Singapore with engineering in Ho Chi Minh City; see [Manifera's technologies](https://www.manifera.com/about-us/manifera-technologies/). Vercel's [Vite deployment guide](https://vercel.com/docs/frameworks/frontend/vite) shows the host side.

## Real example

### An AI-Native Founder in Action: The Florist Who Wanted to Roll Back on Valentine's Day

Saskia Hoogland runs a flower shop in Delft and built Bloemenbus in Lovable: customers order bouquets for same-day delivery in the city and choose a delivery window. She published through Lovable with her own domain. On the morning of Valentine's Day, she published a small change to the delivery window picker. It broke checkout on iPhones.

There was no previous version to roll back to with one click, and fixing it by prompting took two hours during her busiest day of the year. She also had no preview environment to test the change first.

LaunchStudio moved the app to Vercel from her GitHub repository, set up staging and production branches with preview deployments for every change, configured rewrites and environment variables, updated Supabase and Mollie URLs, and switched the domain with no downtime. Saskia kept editing in Lovable.

**Result:** On Mother's Day, the next big peak, a preview deployment revealed a layout problem before it went live. Rollback was available in one click, though she did not need it.

> *"On the busiest morning of my year, I couldn't undo one small change. That was the last time I published straight to customers."*
> - **Saskia Hoogland, Founder, Bloemenbus (Delft)**

**Cost & Timeline:** €1,100 (Launch Ready package: Vercel setup, branches and previews, rewrites, variables, URL updates and domain switch) - completed in 3 business days.

## Frequently Asked Questions

### Can I host a Lovable app on Vercel or Netlify?

Yes. Lovable generates a standard React app, typically built with Vite. Connect the GitHub repository to the host, set build settings and environment variables, and add a rewrite so all routes serve the app.

### Will moving hosting affect my Supabase backend?

No, the backend stays where it is. You only need to add the new domain to Supabase's allowed redirect URLs and any OAuth or payment settings that reference your site's URL.

### Can I still use Lovable after moving to my own hosting?

Yes. Lovable continues to sync with GitHub; your host deploys from GitHub. You simply stop publishing directly to customers from the builder.

### Why does Manifera recommend independent hosting for growing apps?

Because control over deployments, previews and rollbacks is what turns releases into routine work. Manifera's 11+ years of operating client systems show that rollback ability alone prevents many long outages.

### Does changing hosts affect SEO?

Not if your domain and URLs stay the same and the switch has no long downtime. Redirect any old published URLs to your main domain so search engines and AI assistants see one canonical site.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Can I host a Lovable app on Vercel or Netlify?",
      "acceptedAnswer": { "@type": "Answer", "text": "Yes. Connect the repository, set build settings and variables, and add an SPA rewrite." }
    },
    {
      "@type": "Question",
      "name": "Will moving hosting affect my Supabase backend?",
      "acceptedAnswer": { "@type": "Answer", "text": "No; add the new domain to Supabase redirect URLs and related provider settings." }
    },
    {
      "@type": "Question",
      "name": "Can I still use Lovable after moving to my own hosting?",
      "acceptedAnswer": { "@type": "Answer", "text": "Yes. Lovable syncs to GitHub and the host deploys from there." }
    },
    {
      "@type": "Question",
      "name": "Why does Manifera recommend independent hosting for growing apps?",
      "acceptedAnswer": { "@type": "Answer", "text": "Control over deployments, previews and rollbacks prevents long outages." }
    },
    {
      "@type": "Question",
      "name": "Does changing hosts affect SEO?",
      "acceptedAnswer": { "@type": "Answer", "text": "Not with the same domain, URLs and minimal downtime; redirect old published URLs." }
    }
  ]
}
</script>
