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
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/how-do-i-move-my-lovable-app-to-my-own-hosting" },
  "citation": [
    { "@type": "CreativeWork", "name": "Vercel: Vite on Vercel", "url": "https://vercel.com/docs/frameworks/frontend/vite" },
    { "@type": "CreativeWork", "name": "Vite: Env Variables and Modes", "url": "https://vite.dev/guide/env-and-mode" },
    { "@type": "CreativeWork", "name": "DORA 2024 Accelerate State of DevOps Report", "url": "https://dora.dev/research/2024/dora-report/" },
    { "@type": "CreativeWork", "name": "web.dev: Web Vitals", "url": "https://web.dev/articles/vitals" },
    { "@type": "CreativeWork", "name": "OWASP Top 10 2021: A05 Security Misconfiguration", "url": "https://owasp.org/Top10/A05_2021-Security_Misconfiguration/" }
  ]
}
</script>

**Short answer:** sync your Lovable project to GitHub, import that repository into a host such as Vercel, Netlify or Cloudflare Pages, set the build command and environment variables, add a rewrite so all routes serve `index.html`, test on the host's preview URL, then point your domain's DNS to the new host. Your Supabase backend stays where it is. Afterwards, Lovable remains your editor, but your host decides what goes live.

## Key Takeaways

- **Moving a Lovable app to your own host** - Vercel, Netlify, Cloudflare Pages or managed hosting - gives you previews, staging, rollbacks and independence.
- **The steps are straightforward:** sync to GitHub, import into the host, set build settings and environment variables, add an SPA rewrite, update allowed URLs, switch DNS.
- **Your Supabase backend stays where it is;** only redirect URLs and provider settings need the new domain.
- **Lovable remains your editor,** but your host decides what reaches customers.
- **Choose regions and settings with EU users in mind,** and keep one canonical domain for SEO.

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

## Why Control Over Deployment Matters

Publishing directly from a builder is convenient: one click and the change is live. It also means every change goes to customers immediately, without a staging step, a preview for review or a quick way back. Google's DORA research has long associated deployment automation, small changes and fast recovery with better delivery outcomes. Your own hosting gives you those capabilities: every commit can produce a preview, `main` can deploy to staging, production can be promoted deliberately and any release can be rolled back in seconds.

## Comparing Hosts in More Detail

| Consideration | Vercel | Netlify | Cloudflare Pages |
| --- | --- | --- | --- |
| Git integration and previews | Yes | Yes | Yes |
| SPA rewrites | `vercel.json` rewrites | `_redirects` or `netlify.toml` | `_redirects` |
| Serverless or edge functions | Yes, region configurable | Yes | Workers at the edge |
| EU-focused configuration | Function regions selectable | Region options vary | Global edge network |
| Best fit | Next.js and React apps | React and static sites | Globally distributed static apps |

For a standard Lovable app, any of these works well. Choose based on your team's familiarity, pricing for your expected traffic and any data location requirements for functions.

## DNS and Domains Without Downtime

Switching your domain to a new host is the step that worries founders most. A careful sequence avoids downtime: deploy to the new host and test thoroughly on its preview URL; lower your DNS records' time-to-live a day in advance so changes propagate quickly; add the domain in the new host and follow its instructions for records; update DNS and wait for SSL certificates to be issued; then verify login, payments and email links on the live domain. Keep the old publishing active until you are sure the new setup works, then disable or redirect it.

## Environment Variables and Secrets

Frontend variables in a Vite-based Lovable app use the `VITE_` prefix and are embedded at build time, as Vite's documentation explains. Only public values belong there: your Supabase URL and publishable key, analytics IDs and similar. Secret keys for payments, email or AI providers belong in Supabase edge function secrets or your host's server-side environment, never in frontend variables. Set variables separately for preview, staging and production, and rebuild after changing them.

## Performance Settings Worth Checking

Hosts serve your static files from a CDN, which makes a well-built Lovable app fast globally. Check that assets are cached with long cache lifetimes, that HTML is not cached too aggressively so updates appear promptly, that images are compressed and that compression is enabled. Google's Web Vitals measure the loading and responsiveness users experience; a quick check with browser tools after the move confirms everything is working as expected.

## Security Headers

Your own host lets you add HTTP security headers: a Content Security Policy to limit where scripts can load from, `X-Frame-Options` or frame-ancestors to prevent clickjacking, `Strict-Transport-Security` to enforce HTTPS and a referrer policy. Start with a report-only Content Security Policy to avoid breaking third-party scripts, then enforce it. These headers are a meaningful layer of defence that builder publishing often does not let you configure.

## Preview Deployments for Review

Once your app deploys from GitHub, every pull request can get its own preview URL. Use previews to review changes from developers or Lovable before they reach staging or production. Protect previews with passwords or the host's access controls, and point them at your staging backend, never production. Previews make collaboration visible: anyone can click a link and see exactly what a change does.

## Costs of Your Own Hosting

For most founder apps, hosting costs are modest: free or low tiers cover small traffic, with usage-based charges for bandwidth and function invocations as you grow. Compare plans on your expected traffic, team members and features such as password-protected previews. Managed hosting from LaunchStudio bundles hosting with monitoring, backups and updates for €49 per month if you prefer not to manage it yourself.

## Common Mistakes

- Forgetting the SPA rewrite, so deep links return 404
- Putting secret keys in `VITE_` variables
- Not updating Supabase, OAuth and payment redirect URLs for the new domain
- Leaving the old Lovable-published URL indexable alongside the new domain
- Switching DNS before testing on the host's preview URL
- Not documenting the new deployment process for collaborators

## A Checklist for Moving Day

- Repository synced and up to date in your company's GitHub
- Host project created with correct build settings and environment variables
- SPA rewrite configured and deep links tested
- Supabase site URL and redirect list updated
- OAuth providers and payment webhooks updated
- DNS switched, SSL active, old URL redirected
- Monitoring pointed at the new domain
- Team informed about the new release process

## Summary

Moving to your own hosting takes a day or two and gives you previews, staging, rollbacks, security headers and independence from your builder, while Lovable remains the fastest way to keep improving your interface.

## Rolling Back When Something Goes Wrong

The most valuable feature of your own hosting is instant rollback. Practise it once: deploy a harmless change, then use the host's dashboard to restore the previous deployment and confirm the site reverts. During a real incident, rollback first and investigate second; customers care about the app working again far more than about the root cause in the first minutes.

## Working With Lovable After the Move

After the move, keep editing in Lovable as before. Lovable commits to GitHub, the host deploys `main` to staging, and you promote to production when ready. Avoid using Lovable's own publish button for the production domain, which would bypass your process. Tell collaborators about the new flow so nobody publishes around it by accident.

## Related Reading

For the pipeline behind your new hosting, see our guide on automatic deployments for Lovable or Bolt apps; for the staging backend, see our staging environment guide; and for why independence matters, see what happens to your app if Lovable changes pricing or shuts down.

## Questions to Ask Before Moving

Who will promote changes to production after the move? Which domain is canonical? Where will secrets live? Which services reference the current URL? How will you roll back if something goes wrong on moving day? Answering these five questions in advance turns the move into a routine task rather than an anxious evening.

## Where to Start Today

Connect your Lovable project to GitHub if you have not already, import the repository into a host's free tier and deploy it to a preview URL. Seeing your app run outside Lovable, even before switching the domain, makes the rest of the move feel routine.

## The Payoff

Your own hosting turns releases into a controlled, reversible process and removes your production site's dependence on any single builder.

## Summary

Sync to GitHub, deploy from a host you control, keep secrets server-side and promote changes deliberately.

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
