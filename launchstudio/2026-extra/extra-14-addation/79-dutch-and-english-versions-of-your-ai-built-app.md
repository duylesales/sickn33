---
Title: "Dutch and English Versions of Your AI-Built App: Doing i18n Right"
Keywords: dutch english app translation, i18n lovable app, meertalige app, hreflang dutch english, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: SaaS Founder Scale-Up
---

# Dutch and English Versions of Your AI-Built App: Doing i18n Right

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Dutch and English Versions of Your AI-Built App: Doing i18n Right",
  "description": "Many Dutch SaaS products need both Dutch and English. AI builders often hard-code text in one language. This guide covers translation files, language detection, emails, dates and currency, database content, and hreflang for public pages.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-03-27",
  "inLanguage": "en",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/dutch-and-english-versions-of-your-ai-built-app" }
}
</script>

Dutch customers expect Dutch. International employees at Dutch companies expect English. Belgian, German and expat users add more variety. AI builders usually hard-code every label in whichever language you prompted in, which makes adding a second language a search-and-replace nightmare. Doing internationalisation (i18n) properly once makes Dutch and English, and later other languages, manageable.

## What Needs Translating

| Area | Often forgotten? |
| --- | --- |
| Interface labels and buttons | No |
| Error and validation messages | Yes |
| Transactional emails (confirmation, reset, receipts) | Yes |
| Auth emails from Supabase | Yes |
| PDF documents such as invoices | Yes |
| Push notifications and SMS | Yes |
| Public marketing pages | No, but SEO setup often missing |
| User-generated or admin-managed content in the database | Yes |

## Step 1: Move Text Into Translation Files

Use an i18n library for React, such as i18next or similar, and move every visible string into translation files (`nl.json`, `en.json`) with keys. AI tools can help extract strings, but review the result: keys should be meaningful and nothing should be missed.

## Step 2: Choose the Language

- Store each user's preferred language in their profile
- For new visitors, use the browser language as a default, with a visible switcher
- For B2B, consider an organisation default that users can override

## Step 3: Dates, Numbers and Currency

Use locale-aware formatting: `14 maart 2028` versus `14 March 2028`, `€ 1.250,00` versus `€1,250.00`. Store dates in UTC and amounts as integers in cents; format only for display.

## Step 4: Emails and Documents

Send emails in the user's language. Supabase auth email templates can be customised; for multiple languages, many teams send auth emails through their own email function with language-specific templates. Invoices may need to be in the customer's language and include legally required details either way.

## Step 5: Database Content

If admins create content such as product names, categories or help articles, store translations per language, for example a `translations` table or separate columns, with a fallback language.

## Step 6: Public Pages and SEO

For marketing pages, use language-specific URLs (`/nl/` and `/en/`), `hreflang` tags linking the versions, and translated titles and descriptions. This helps search engines and AI assistants show the right language to the right user. LaunchStudio's own site uses this structure.

## Translation Quality

Machine translation is a good start; native review is worth it for key screens, emails and marketing pages. Tone matters: Dutch SaaS products usually address users informally with "je", while some sectors expect "u".

## Getting It Done

LaunchStudio sets up i18n frameworks, translation files, multilingual emails and hreflang for AI-built apps, typically three to seven days depending on the app's size. LaunchStudio is powered by Manifera, which builds multilingual systems for clients across Europe and Asia from Amsterdam, Singapore and Ho Chi Minh City; see [Manifera's web app development](https://www.manifera.com/services/web-app-develop/). Google explains [hreflang and localized versions](https://developers.google.com/search/docs/specialty/international/localized-versions). For Belgian users, see our [Bancontact checkout guide](https://launchstudio.eu/en/blog/bancontact-and-ideal-checkout-for-benelux-ai-apps).

## Real example

### An AI-Native Founder in Action: The Expat HR Portal Half in Dutch

Kim Verhoef built Inwerkplein in Bolt: an onboarding portal for international employees joining Dutch companies, covering BSN registration steps, housing tips and company policies. She had prompted everything in Dutch, then asked Bolt to "add English". The result was a toggle that translated about 70% of the interface; error messages, emails, PDFs and admin-entered content stayed Dutch. New international hires, the core users, were confused.

LaunchStudio extracted all strings into Dutch and English translation files, stored language preference per user with an organisation default, localised dates and numbers, built multilingual transactional and auth emails, added translation fields for company-entered policies with fallback, and set up `/nl/` and `/en/` marketing pages with hreflang.

**Result:** International users received the whole experience in English, Dutch HR staff kept working in Dutch, and Kim added German for a client with many German employees in two days, using the same structure.

> *"My app was for people who didn't speak Dutch yet. Half of it only spoke Dutch."*
> - **Kim Verhoef, Founder, Inwerkplein (Amsterdam)**

**Cost & Timeline:** €2,800 (string extraction, i18n framework, user and organisation language, localisation, multilingual emails, content translations and hreflang) - completed in 8 business days.

## Frequently Asked Questions

### Can Lovable or Bolt translate my app automatically?

They can help generate translations and toggles, but often miss error messages, emails, documents and database content. A proper i18n setup with translation files makes translations complete and maintainable.

### Should my app use "je" or "u" in Dutch?

Most Dutch SaaS products use informal "je". Some sectors, such as legal, financial or care services for older users, may prefer "u". Choose deliberately and use it consistently.

### How do I translate Supabase auth emails?

Supabase auth templates can be customised, but supporting several languages usually means sending auth-related emails through your own email function with language-specific templates, or carefully using template variables.

### How does Manifera handle multilingual projects?

With translation files, locale-aware formatting and content models designed for multiple languages from the start. Manifera's international client base across Europe and Asia makes multilingual delivery routine.

### Does a bilingual site help with AI search?

Yes. Language-specific pages with hreflang let search engines and AI assistants serve Dutch content to Dutch queries and English content to English queries, increasing the chance of being cited in both.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Can Lovable or Bolt translate my app automatically?",
      "acceptedAnswer": { "@type": "Answer", "text": "They help but often miss errors, emails, documents and database content; use proper i18n." }
    },
    {
      "@type": "Question",
      "name": "Should my app use je or u in Dutch?",
      "acceptedAnswer": { "@type": "Answer", "text": "Most SaaS uses je; some sectors prefer u. Choose and stay consistent." }
    },
    {
      "@type": "Question",
      "name": "How do I translate Supabase auth emails?",
      "acceptedAnswer": { "@type": "Answer", "text": "Customise templates or send auth emails via your own function with language-specific templates." }
    },
    {
      "@type": "Question",
      "name": "How does Manifera handle multilingual projects?",
      "acceptedAnswer": { "@type": "Answer", "text": "Translation files, locale-aware formatting and multilingual content models from the start." }
    },
    {
      "@type": "Question",
      "name": "Does a bilingual site help with AI search?",
      "acceptedAnswer": { "@type": "Answer", "text": "Yes; hreflang lets engines and assistants serve the right language." }
    }
  ]
}
</script>
