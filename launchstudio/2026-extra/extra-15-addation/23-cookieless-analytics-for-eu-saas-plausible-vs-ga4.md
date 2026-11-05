---
Title: "Cookieless Analytics for EU SaaS: Plausible vs GA4"
Keywords: cookieless analytics eu, plausible vs google analytics 4, analytics zonder cookies, gdpr compliant analytics saas, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: AI-Native Founder (Non-Technical)
---

# Cookieless Analytics for EU SaaS: Plausible vs GA4

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Cookieless Analytics for EU SaaS: Plausible vs GA4",
  "description": "European SaaS founders must balance useful analytics with GDPR and cookie rules. This guide compares privacy-focused cookieless tools such as Plausible with Google Analytics 4 and Consent Mode, explains what Dutch rules say about analytics cookies, and shows how to set up a compliant analytics stack for an AI-built marketing site and app.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-05-10",
  "inLanguage": "en",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/cookieless-analytics-for-eu-saas-plausible-vs-ga4" },
  "citation": [
    { "@type": "CreativeWork", "name": "Autoriteit Persoonsgegevens: Cookies", "url": "https://www.autoriteitpersoonsgegevens.nl/en/themes/internet-and-smart-devices/cookies" },
    { "@type": "CreativeWork", "name": "Plausible Analytics data policy", "url": "https://plausible.io/data-policy" },
    { "@type": "CreativeWork", "name": "Google: Consent mode overview", "url": "https://support.google.com/analytics/answer/9976101" },
    { "@type": "CreativeWork", "name": "EDPB Guidelines 2/2023 on technical scope of Art. 5(3) ePrivacy Directive", "url": "https://www.edpb.europa.eu/our-work-tools/documents/public-consultations/2023/guidelines-22023-technical-scope-art-53-eprivacy_en" }
  ]
}
</script>

Every founder wants to know where visitors come from, which pages convince them and where they drop out of the sign-up flow. Every European founder also has to deal with the rules that govern how that data is collected. The result is a familiar compromise: a consent banner that most visitors click away, analytics that miss a large share of traffic, and a nagging uncertainty about whether the setup is compliant at all.

Privacy-focused analytics tools such as Plausible promise a way out: no cookies, no personal data, no banner. Google Analytics 4, with Consent Mode, promises richer data and integration with Google Ads, within a consent framework. Which is right for an AI-built SaaS depends on what you need to know, who you advertise to and how much complexity you want to manage.

This guide explains the trade-offs. It is general information, not legal advice; consult a privacy specialist for your specific setup.

## Key Takeaways

- **Cookie rules apply to storing or reading information on a visitor's device,** not only to cookies. In the Netherlands, these rules sit in the Telecommunicatiewet, alongside GDPR for personal data.
- **Dutch guidance allows some analytics without consent** if it has little impact on privacy, but Google Analytics in its common configuration generally requires consent.
- **Privacy-focused tools such as Plausible are designed to work without cookies or personal data,** which in many setups allows analytics without a consent banner. Check your configuration and get advice.
- **GA4 with Consent Mode is often needed if you run Google Ads,** because conversion measurement and audiences depend on it.
- **Many SaaS companies use both:** a privacy-focused tool for site analytics and product events, plus consent-based Google tags for advertising.

## The Rules in Plain Terms

Two sets of rules apply to analytics in the EU.

**ePrivacy rules,** implemented in the Netherlands in Article 11.7a of the Telecommunicatiewet, cover storing or accessing information on a user's device, whether through cookies, local storage, pixels or similar techniques. Consent is required unless the storage or access is strictly necessary for the service, or falls under a specific exception. The European Data Protection Board's guidelines on the technical scope of these rules make clear that techniques other than cookies, such as tracking pixels and some forms of fingerprinting, can also be covered.

**GDPR** applies when you process personal data, including online identifiers such as IP addresses in many contexts. You need a legal basis, transparency, data minimisation, appropriate security and, for transfers outside the EU, an appropriate transfer mechanism.

The Autoriteit Persoonsgegevens has published guidance that analytics cookies with little or no impact on privacy can be placed without consent, under conditions such as limiting data, masking IP addresses, not sharing data with third parties for their own purposes and informing users. In practice, Google Analytics in its standard configuration, where Google uses data for its own purposes and links data across services, does not meet those conditions, so consent is generally needed.

## Option 1: Privacy-Focused Analytics (Plausible and Similar)

Plausible is an EU-based analytics service designed around privacy. According to its data policy, it does not use cookies, does not collect personal data and does not track visitors across sites. To count unique visitors, it uses a daily rotating hash of the IP address, user agent and website domain, which it does not store and which cannot be reversed to identify a person. Data is hosted in the EU.

Other tools take similar approaches, including Fathom, Simple Analytics and Matomo in a cookieless configuration, and some product analytics tools offer cookieless modes.

**What you get:**

- Page views, unique visitors, referrers, UTM campaigns, devices, countries and entry and exit pages
- Custom events, such as "Sign-up started" and "Sign-up completed", and goal conversions
- A simple dashboard that non-technical team members actually read
- Typically no consent banner needed for the analytics itself, depending on your configuration and legal assessment

**What you give up:**

- Individual user journeys across sessions and devices
- Detailed audience demographics and interests
- Native integration with Google Ads audiences and bidding
- Some precision in unique visitor counts

## Option 2: Google Analytics 4 With Consent Mode

GA4 is free and powerful, with deep integration into Google Ads, Search Console and BigQuery exports. For SaaS companies running paid search, it is often part of the measurement stack.

Consent Mode lets Google tags adjust their behaviour based on the visitor's consent choice. When a visitor declines, tags send limited, cookieless signals, and Google uses modelling to estimate conversions. Since March 2024, Google requires advertisers who use its services for users in the European Economic Area to implement Consent Mode with a consent management platform for features such as audience building and measurement.

**What you get:**

- Detailed event analytics, funnels and user journeys for consenting visitors
- Conversion tracking and modelling for Google Ads
- Audiences for remarketing, where consent allows
- Integration with BigQuery for deeper analysis

**What you give up:**

- Simplicity: GA4's interface and configuration are complex
- Complete data: visitors who decline consent are only partially visible
- A banner-free experience: you need a consent management platform
- Some control: data is processed by Google, with transfer considerations

## Comparison

| Factor | Plausible (privacy-focused) | GA4 with Consent Mode |
| --- | --- | --- |
| Cookies | None | Yes, after consent |
| Personal data | Designed to avoid it | Yes, for consenting visitors |
| Consent banner for analytics | Often not needed | Required |
| Data location | EU | Google infrastructure, with transfer mechanisms |
| Ease of use | Very simple | Complex |
| Google Ads integration | Limited, via offline imports | Native |
| User journeys | Aggregate only | Detailed for consenting users |
| Cost | Paid subscription | Free tier |
| Coverage of visitors | Near complete | Depends on consent rate, plus modelling |

## A Practical Stack for an AI-Built SaaS

Many European SaaS companies settle on a layered approach:

**1. Site analytics with a privacy-focused tool.** Install Plausible or similar on the marketing site and app, tracking page views and key events: sign-up started, sign-up completed, trial activated, plan purchased. This gives near-complete, privacy-friendly visibility into the funnel.

**2. Product events in your own database.** Record meaningful product events, such as "first project created" or "invited a teammate", in your own backend, linked to accounts. This is first-party operational data for understanding activation and retention, covered by your privacy policy, and often more useful than any third-party analytics.

**3. Google tags only where needed, behind consent.** If you run Google Ads, load the Google tag with Consent Mode, show a clear consent banner and send conversion events, such as a completed sign-up or purchase. Consider server-side or offline conversion imports for better accuracy within the consent framework.

**4. One consent banner across domains.** If your marketing site and app are on different subdomains, share the consent state so visitors decide once. Our guide on [connecting a Webflow or Framer site to an AI-built app](https://launchstudio.eu/en/blog/webflow-or-framer-site-with-an-ai-built-app-domains-auth-and-seo) covers the cross-domain setup.

## Measuring Google Ads Without Over-Tracking

Founders running Google Ads often worry that respecting consent will leave them blind. In practice, a careful setup recovers most of the signal while staying within the rules.

**Measure the conversion that matters.** Send a conversion only when something valuable happens, such as a confirmed sign-up, a booked demo or a paid plan, rather than on button clicks. Fewer, meaningful conversions give Google's bidding better signals than many noisy ones.

**Use Consent Mode properly.** When visitors decline, Consent Mode sends limited, cookieless pings, and Google models conversions from them. Modelling is only as good as the consenting sample, so a banner that offers a fair choice, explained clearly, tends to produce better data than one that frustrates people.

**Consider offline conversion imports.** For B2B SaaS, the most valuable conversion may happen days later, when a trial becomes a paying customer. Recording the advertising click identifier at sign-up, where consent allows, and importing paid conversions later connects ad spend to revenue rather than to form fills.

**Check your numbers against your own database.** Compare conversions reported in Google Ads with sign-ups and payments recorded in your backend each month. Large gaps usually point to a tracking problem, such as a tag firing on the wrong page, rather than to real performance changes.

## Common Mistakes in AI-Built Apps

**Loading Google Analytics before consent.** AI builders often add the GA snippet to the page head because a prompt asked for "analytics". It runs before the banner appears, which defeats the purpose of the banner.

**A banner without real choices.** "Accept" with no equivalent "Reject" option, or pre-ticked boxes, do not produce valid consent under Dutch and EU guidance.

**Assuming "cookieless" means "no rules".** Techniques that read device information can still fall under ePrivacy rules. Use tools designed for privacy, check their documentation and get advice on your configuration.

**Tracking personal data in event properties.** Sending email addresses or names as event properties to any analytics tool creates unnecessary personal data processing.

**Forgetting the privacy policy.** Every analytics tool belongs in your privacy policy, with what it collects and why.

**Measuring everything, using nothing.** Dozens of events with no defined questions produce dashboards nobody reads. Start with five to ten events that map to your funnel.

## Defining the Events That Matter

Before configuring any tool, write down the questions you want answered:

1. Which channels bring visitors who sign up?
2. Where in the sign-up flow do people abandon?
3. How many sign-ups reach the first meaningful action?
4. Which plans do converting customers choose?
5. Which features do retained customers use in their first week?

Each question maps to a small number of events. For a typical SaaS: `signup_started`, `signup_completed`, `email_verified`, `first_key_action`, `trial_started`, `plan_purchased`, `teammate_invited`. Name events consistently, document them and send the same names to every tool that needs them.

## What It Costs

Setting up a compliant analytics stack is usually part of a production launch. LaunchStudio's **Launch Ready** package (€800-€3,500) covers removing pre-consent tracking, installing privacy-focused analytics, defining and implementing funnel events, configuring a consent banner where Google tags are needed and updating privacy policy inputs, along with security hardening and deployment. **Launch & Grow** (€2,500-€7,500 plus €49 per month) adds payments, managed hosting, monitoring and priority support. Analytics tools charge their own subscriptions. Use the [price calculator](https://launchstudio.eu/en/#calculator) for an estimate.

## Who Does the Work

LaunchStudio is powered by Manifera, a software development company with 11+ years of experience, 160+ delivered projects and 120+ engineers, used to building systems under European privacy requirements. Founders meet the team at Herengracht 420 in Amsterdam; engineering happens at the development centre on Pho Quang Street in Ho Chi Minh City, with a hub on Tras Street in Singapore.

## Real example

### An AI-Native Founder in Action: The Tutoring Platform That Tracked Before Asking

Laura Hermans built Studiemaatje in Lovable: a platform where secondary school students in the Netherlands book online study coaching, with a marketing site in Framer. She had asked Lovable to "add Google Analytics", installed a free consent banner from a template on the Framer site and was running Google Ads for terms related to study help.

A parent who worked in privacy compliance emailed to point out that Google Analytics loaded on the app before any consent choice, the banner on the marketing site had only an "OK" button, and the app had no banner at all. Because many users were minors, the concern was serious. Meanwhile, Laura's analytics showed only around 40% of the visits her hosting logs recorded, and she could not see where students dropped out of the booking flow.

LaunchStudio removed the hard-coded Google Analytics snippet and installed Plausible on both the Framer site and the app, with custom events for the booking funnel from landing page to confirmed first session. Product events were recorded in Supabase per account without personal data in event properties. For Google Ads, the Google tag now loaded through a consent management platform with Consent Mode, a genuine reject option and consent shared across both domains, and conversions were sent only for completed bookings. Engineers listed every tool and its purpose for the privacy policy update.

**Result:** Laura now sees close to complete funnel data, which revealed that half of the drop-off happened at a timezone selection step that was quickly simplified. Booking completion rose by about 15% over the next two months, and Google Ads conversion reporting, with modelling, stabilised within weeks.

> *"I thought analytics meant pasting a Google snippet. Doing it properly gave me better data and a reply I could send to that parent with confidence."*
> - **Laura Hermans, Founder, Studiemaatje (Leiden)**

**Cost & Timeline:** €1,750 (Launch Ready package: analytics redesign, funnel events, consent management, Consent Mode setup and privacy policy inputs) - completed in 6 business days.

## Frequently Asked Questions

### Do I need a cookie banner if I use Plausible?

Often not for the analytics itself, because Plausible is designed to work without cookies or personal data. Whether you need a banner overall depends on everything else your site loads, such as advertising pixels, embedded videos or chat widgets. Review all scripts and get advice on your full configuration.

### Can I use Google Analytics 4 in the Netherlands?

Yes, with a proper setup. In common configurations, GA4 requires consent under Dutch guidance, so you need a consent banner with genuine choices, Consent Mode if you use Google Ads and attention to data transfer and privacy policy requirements.

### Which analytics tool is best for an early-stage SaaS?

For most early-stage SaaS companies, a privacy-focused tool for site and funnel analytics plus product events in their own database gives the most useful, compliant insight. Add GA4 with Consent Mode when you invest meaningfully in Google Ads.

### How does Manifera's experience help with analytics compliance?

Manifera has built systems for European clients under privacy requirements for 11+ years. LaunchStudio uses that experience to remove hidden tracking, implement consent correctly and design events that answer business questions without collecting unnecessary personal data.

### Does privacy-friendly analytics affect SEO or AI visibility?

Not negatively. Lightweight analytics scripts load faster than heavy tag setups, which can help page speed, and fewer intrusive banners improve user experience. Search engines and AI answer engines do not reward the choice of analytics tool itself, but they do reward fast, usable pages.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Do I need a cookie banner if I use Plausible?",
      "acceptedAnswer": { "@type": "Answer", "text": "Often not for the analytics itself, since Plausible avoids cookies and personal data, but other scripts such as ad pixels may still require consent. Review your full setup." }
    },
    {
      "@type": "Question",
      "name": "Can I use Google Analytics 4 in the Netherlands?",
      "acceptedAnswer": { "@type": "Answer", "text": "Yes, with a consent banner offering genuine choices, Consent Mode for Google Ads and attention to transfers and the privacy policy." }
    },
    {
      "@type": "Question",
      "name": "Which analytics tool is best for an early-stage SaaS?",
      "acceptedAnswer": { "@type": "Answer", "text": "A privacy-focused tool for funnel analytics plus product events in your own database, adding GA4 with Consent Mode when investing in Google Ads." }
    },
    {
      "@type": "Question",
      "name": "How does Manifera's experience help with analytics compliance?",
      "acceptedAnswer": { "@type": "Answer", "text": "Manifera has built systems under European privacy requirements for 11+ years, and LaunchStudio removes hidden tracking, implements consent and designs useful events." }
    },
    {
      "@type": "Question",
      "name": "Does privacy-friendly analytics affect SEO or AI visibility?",
      "acceptedAnswer": { "@type": "Answer", "text": "Not negatively. Lightweight scripts can help page speed and user experience, which search and AI engines reward." }
    }
  ]
}
</script>
