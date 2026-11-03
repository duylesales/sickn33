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
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/dutch-and-english-versions-of-your-ai-built-app" },
  "citation": [
    { "@type": "CreativeWork", "name": "Google: Tell Google about localized versions of your page", "url": "https://developers.google.com/search/docs/specialty/international/localized-versions" },
    { "@type": "CreativeWork", "name": "Supabase: Custom SMTP", "url": "https://supabase.com/docs/guides/auth/auth-smtp" },
    { "@type": "CreativeWork", "name": "web.dev: Web Vitals", "url": "https://web.dev/articles/vitals" }
  ]
}
</script>

Dutch customers expect Dutch. International employees at Dutch companies expect English. Belgian, German and expat users add more variety. AI builders usually hard-code every label in whichever language you prompted in, which makes adding a second language a search-and-replace nightmare. Doing internationalisation (i18n) properly once makes Dutch and English, and later other languages, manageable.

## Key Takeaways

- **Many Dutch SaaS products need both Dutch and English;** AI builders often hard-code text in one language, which makes adding a second painful.
- **Proper internationalisation covers more than buttons:** errors, emails, auth emails, PDFs, notifications and database content.
- **Store user language preferences, format dates and numbers by locale and keep timestamps in UTC.**
- **For public pages, use language-specific URLs with `hreflang`,** as Google recommends for localised versions.
- **Choose "je" or "u" deliberately in Dutch** and stay consistent across the product.

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

## Internationalisation Versus Localisation

Internationalisation (i18n) is preparing your app so it can support multiple languages and regions: text in translation files, locale-aware formatting, layouts that handle longer words. Localisation (l10n) is the work of adapting content for a specific language and market: translation, tone, examples, currency and legal references. Doing i18n once makes each new localisation much cheaper. AI-built apps usually skip i18n, so the first translation project often includes a one-time refactor.

## Extracting Strings Safely

Moving hard-coded text into translation files is mechanical but error-prone. A good approach: introduce an i18n library, extract strings screen by screen with meaningful keys such as `checkout.payButton`, run the app in a "pseudo-locale" that wraps every translated string in brackets to spot anything missed and add a check in CI that flags hard-coded text in components. AI tools can help with extraction; review their output, as they sometimes miss strings in error handling or conditional branches.

## Handling Plurals, Gender and Word Order

Languages differ in how they handle plurals ("1 item" versus "2 items"), word order and formality. Use your i18n library's pluralisation features rather than concatenating strings, and avoid building sentences from fragments. Dutch and English are relatively close, but adding German or French later will expose fragmentation, so design translation keys as complete sentences from the start.

## Formatting Dates, Numbers and Currency

Use locale-aware formatting from the browser's internationalisation APIs or your library: dates such as "14 maart 2028" versus "14 March 2028", numbers such as "1.250,00" versus "1,250.00", and currency formatting appropriate to the locale. Store values in neutral formats - UTC timestamps, amounts in cents - and format only for display. Time zones matter as well: show times in the user's time zone, and be careful around daylight saving changes.

## SEO for Multilingual Sites

Google's documentation on localised versions recommends separate URLs for each language, such as `/nl/` and `/en/`, with `hreflang` annotations linking the versions so the right page appears for each language and region. Translate titles, meta descriptions and structured data as well as body text. Avoid automatically redirecting users based on IP address without letting them choose, since crawlers and travellers may be redirected incorrectly. For AI assistants, clear language-specific pages make it easier to cite the right version for Dutch or English questions.

## Machine Translation and Human Review

Machine translation has become very good and is a sensible starting point for interface text. Key pages, legal texts, onboarding flows and marketing content deserve native review: tone, idioms and domain terms matter. In Dutch, choose between informal "je" and formal "u" based on your audience and apply it consistently; mixing them looks careless. For Belgian audiences, a Flemish reviewer can catch Netherlands-specific phrasing.

## Translating User-Generated and Admin Content

If administrators create content such as product names, help articles or email templates, decide whether it should be translated and how. Common approaches include separate fields per language, a translations table keyed by content ID and language, or translation on demand with an AI service whose output is reviewed. Always define a fallback language so missing translations never show empty text.

## Accessibility and Language

Set the `lang` attribute on your HTML so screen readers pronounce text correctly, and update it when users switch languages. Make sure translated text still fits layouts on mobile; Dutch words can be long and break designs created with English text.

## Multilingual Emails and Documents

Emails and documents often stay in one language long after the interface is translated. Store each user's preferred language and pass it to every email and document function. Maintain templates per language for confirmations, password resets, receipts, notifications and reminders. Supabase's built-in auth templates can be customised, but supporting several languages usually means sending auth-related emails through your own function with language-specific templates. Invoices may need a fixed language for your bookkeeping while customer-facing text follows the user's preference; ask your accountant.

## A Practical Rollout Plan

1. Introduce an i18n library and extract strings from the most-used screens first.
2. Add a language switcher and store preferences in the profile.
3. Translate interface, errors and validation messages.
4. Translate transactional and auth emails.
5. Localise dates, numbers and currency.
6. Add language-specific public pages with `hreflang`.
7. Review key flows with native speakers.
8. Add a CI check that blocks new hard-coded strings.

## Testing Multilingual Apps

Test each language on key flows: sign-up, onboarding, the core action, payments and emails. Look for untranslated strings, truncated text, wrong date formats and mixed languages in a single screen. Test switching languages mid-session and with users whose browser language differs from their profile preference.

## Common Mistakes

- Translating the interface but not emails, errors or PDFs
- Building sentences from fragments that cannot be translated naturally
- Mixing "je" and "u" in Dutch
- Redirecting visitors by IP without letting them choose
- Forgetting the `lang` attribute and `hreflang` tags
- No fallback when a translation is missing

## The Payoff

A properly multilingual product serves Dutch customers in their own language, welcomes international employees and opens new markets with modest extra effort. Each additional language becomes a translation project rather than an engineering one.

## Summary

Separate text from code, format by locale, translate every channel, structure public pages for multilingual SEO and choose your Dutch tone deliberately. Do it once, and languages stop being a barrier to growth.

## Choosing an i18n Library

For React apps built with Lovable or Bolt, established libraries such as i18next with its React bindings, or FormatJS-based solutions, handle translation files, plurals, interpolation and formatting. Choose one that supports lazy loading of language files, so users download only the language they need, and that integrates with your build tooling. Avoid inventing a homemade system; translation edge cases are well solved in mature libraries.

## Managing Translations as the Product Grows

As features multiply, translation files grow and drift. Keep them organised by feature, use a translation management tool or a simple review process for new keys, and include translation updates in the same change that adds a feature. A CI check that flags missing keys in any language prevents half-translated releases.

## Where to Start Today

Pick your most important screen - often sign-up or checkout - and move its text into translation files. Seeing one screen work in two languages makes the rest of the project concrete and shows how much work remains.

## Questions to Answer Before Translating

Which languages do your current and target customers need? Will the whole product be translated, or only customer-facing parts? Who reviews translations? Should Dutch use "je" or "u"? How will you handle content created by administrators? Answering these before starting keeps the project focused and avoids rework.

## Related Reading

For Belgian audiences and payments, see our Bancontact and iDEAL checkout guide; for multilingual SEO on a separate marketing site, see our guide on adding a blog or marketing site to a Lovable app.

## The Bottom Line

Treat language as infrastructure rather than decoration: set it up once, properly, and every new market becomes much easier to serve.

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
