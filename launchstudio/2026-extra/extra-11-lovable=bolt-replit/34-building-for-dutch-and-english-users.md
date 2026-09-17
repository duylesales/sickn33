---
Title: "Lovable SEO in Two Languages: Building for Dutch and English Users"
Keywords: Lovable, lovable seo, dutch english app localisation, hreflang setup, date number formatting locale, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: AI-Native Founder (Non-Technical)
---

# Lovable SEO in Two Languages: Building for Dutch and English Users

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Lovable SEO in Two Languages: Building for Dutch and English Users",
  "description": "Translating the interface is the easy quarter. Dates, numbers, emails, search, SEO signals and the strings buried in generated code are where bilingual products actually break.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-07-06",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/building-for-dutch-and-english-users" }
}
</script>

Most products built in the Netherlands face the same question within a few months of launch: the interface is in English because that is how it was prompted, half the customers are Dutch, and somebody has asked whether there is a Dutch version.

The instinct is to treat this as a translation task — export the text, translate it, put it back. That is roughly a quarter of the work, and the remaining three quarters are the parts that produce a product which is technically bilingual and obviously foreign: dates in the wrong format, a confirmation email in English after a Dutch checkout, a search that cannot find Dutch words, and prices displayed in a way no Dutch customer writes them.

## What Generated Code Does With Text

AI builders write text directly into components. There is no separation between the interface and its wording, because nothing in the description of a product suggested there needed to be.

That means the first real task is extraction: pulling every user-visible string into a structure where a translation can exist alongside it. For a small product this is a day's work and it is unavoidable — without it, adding a language means duplicating your entire interface, which is how bilingual products end up permanently out of sync.

Two details make the difference between a clean job and one that is redone later. Strings need to be identified by meaning rather than by their English text, so that changing the English does not orphan the Dutch. And text with variables inside it — "3 bookings remaining" — must be handled as a template rather than assembled from fragments, because word order differs between languages and concatenation produces sentences that are grammatical in neither.

## The Formats Nobody Translates

This is where a bilingual product reveals itself as an afterthought.

**Dates.** A Dutch user reading "03/04/2027" assumes 3 April; an American reads 4 March. Written months remove the ambiguity entirely, and Dutch date conventions differ from English ones in casing as well as order.

**Numbers and currency.** Dutch convention uses a comma as the decimal separator and a point for thousands, the reverse of English. A price displayed with the wrong convention looks like a typing error at best and a different amount at worst.

**Times and weeks.** The Netherlands uses a 24-hour clock in most contexts and weeks starting on Monday. A calendar starting on Sunday marks your product as imported.

**Addresses and postcodes.** Dutch postcodes have a specific format and appear before the city. A form built to an American layout is filled in awkwardly by every Dutch user.

**Names.** Dutch surnames frequently carry prefixes — "de", "van", "van der" — which affects alphabetical sorting and any assumption that a name splits neatly into two fields.

None of these are translation problems. They are formatting decisions that need to follow the user's language rather than the developer's default.

## Emails Are Where It Breaks Most Visibly

A user switches your interface to Dutch, completes a purchase, and receives an English confirmation. This happens in nearly every bilingual product built this way, because the interface language lives in the browser and the email is generated on the server, which has no idea what the user chose.

The fix is to store a language preference on the account and use it for everything sent to that person: confirmations, invoices, password resets, notifications. It also needs a sensible default for people who have not chosen — usually derived from the browser on signup, and always changeable afterwards.

Invoices deserve specific attention. A Dutch business customer generally expects a Dutch invoice with the correct terminology, and the document is read by their accountant rather than by them.

## Search and Content Behave Differently Per Language

If your product has search, language matters more than founders expect. Word stemming rules differ, and Dutch compound words mean a search for one term should find text containing it as part of a longer word — behaviour that English-configured search will not produce.

If your database holds content in both languages, decide whether search covers both or filters to the user's language. Both are defensible; having never decided is what produces results users find confusing.

## The SEO Side, Briefly

For public pages, two things matter and are usually missing.

**Each language needs its own address.** A page whose content changes based on a stored preference cannot be indexed separately for each language, because a crawler sees one version. Distinct paths — a language prefix is the common pattern — give each version an indexable home.

**Language relationships need declaring.** Alternate-language annotations tell search engines these pages are versions of each other, so the right one is offered to the right person rather than the two competing.

This is also the point to decide which language a page exists in at all. Many Dutch products sensibly keep marketing pages in Dutch and the application interface in both, rather than translating everything by default.

## What Not to Translate

Restraint saves a great deal of maintenance.

Product names and brand terms stay as they are. Technical identifiers, reference numbers and codes stay. Legal documents need a professional translation or a clear statement of which version governs — an automatically translated terms page is worse than an English one honestly labelled.

And user-generated content is not yours to translate. A listing written in Dutch stays in Dutch; offering a translation button is a feature, not an obligation.

## A Realistic Sequence

**Extract the strings first,** even before deciding to add a language. It is the step that makes everything else possible and the step that is hardest to retrofit.

**Fix the formats next,** because they affect both languages and are quick.

**Add the language preference to accounts and wire it to emails,** which removes the most visible inconsistency.

**Then translate,** ideally with a native speaker reviewing rather than a machine pass alone — Dutch produced by translation tools reads as translated, and in a small market that is noticed.

**Finally, handle public pages and their language signals** if search traffic matters to you.

## Getting It Built Once

Bilingual support is one of those features that is cheap when designed and expensive when bolted on, mostly because the extraction work has to happen either way and doing it later means doing it while a live product depends on the strings.

LaunchStudio handles it as part of the last-mile work on an AI-built product: strings extracted and structured, formatting made locale-aware, language preference stored and applied to every outgoing message, search configured for Dutch as well as English, and public pages given distinct addresses with the right language signals — without touching the interface you designed in Lovable.

Behind it is Manifera, eleven years of building software for clients across the EU and Southeast Asia, including Vodafone and TNO, from offices in Amsterdam and Ho Chi Minh City where bilingual products are routine rather than exceptional. See the [packages page](https://launchstudio.eu/en/#packages), or [describe your project](https://launchstudio.eu/en/#contact) and we will tell you what your product needs within one business day.

## Which Language Should the Product Default To?

A decision founders make by accident — usually English, because that is the language the tool was prompted in — and one worth making deliberately, because it shapes who takes the product seriously.

**Selling to Dutch consumers:** Dutch, without hesitation. Consumer trust in the Netherlands is closely tied to a product speaking the customer's language, and an English-only consumer product reads as foreign or unfinished regardless of quality.

**Selling to Dutch businesses:** usually Dutch for anything commercial — the marketing pages, the pricing, the invoices, the contracts — with the application interface acceptable in English if the users are technical. Procurement documents and anything a finance department reads should be Dutch.

**Selling to the public sector, healthcare or education:** Dutch, throughout. This is frequently a procurement requirement rather than a preference, and it extends to your privacy statement and support.

**Selling internationally from the Netherlands:** English as the primary, with Dutch as a second language if the domestic market matters to you. Many Dutch founders over-invest in Dutch translation for products whose customers are mostly elsewhere.

**Mixed audiences:** detect on first visit, let the user change it, and remember the choice on the account rather than only in the browser.

The mistake worth avoiding is a half-Dutch product — Dutch marketing pages leading to an English interface, or a Dutch interface sending English emails. That inconsistency does more damage than either language used consistently, because it reads as carelessness rather than as a language choice.

## Testing the Second Language Properly

Bilingual products are usually tested in the language the founder thinks in, which is how the other version reaches customers with obvious problems intact.

**Switch the language and complete every flow.** Signup, the core action, payment, password reset. Not a glance at the interface — the whole path, including the emails each step sends.

**Check the emails in both languages,** in a real inbox. This is where the inconsistency lives, and it is invisible from inside the app.

**Look for text that did not move.** Validation messages, error states, empty states, buttons inside modals, tooltips and anything generated by a third-party component are the places untranslated strings hide, because nobody clicks them during a review.

**Watch the layout.** Dutch text runs longer than English, frequently by a fifth or more. Buttons designed around a short English label break with the Dutch equivalent, and compound words do not wrap where a designer expected.

**Have a native speaker use it for ten minutes.** Not proofread the strings — use it. Awkward phrasing that reads acceptably in a list is immediately obvious in context, and in a small market that awkwardness is what makes a product feel imported.

## Real example

### A Booking Tool That Was Dutch Everywhere Except Where It Mattered

Lotte Verhoeven built Praktijkplanner in Lovable: an appointment tool for independent physiotherapists and dietitians, used by about sixty practices across Noord-Brabant. The interface had been translated into Dutch by a colleague, and practices were broadly happy.

The complaints were oddly specific. Patients were arriving on the wrong day. An accountant had returned an invoice. Several practice owners said the tool "felt foreign" without being able to say why.

The review found the cause in the formats rather than the translation. Dates were rendered in the American order, so 03/04 was read as 3 April by patients and generated as 4 March by the system. Prices used a decimal point rather than a comma. The calendar week started on Sunday. Appointment confirmation emails were sent in English regardless of the interface language, because language lived only in the browser. And invoices used English terminology, which was what the accountant had objected to.

Seven business days of work: strings extracted into a proper structure; all dates, times, numbers and currency made locale-aware; calendar weeks starting on Monday; a language preference stored per practice and per patient and applied to every outgoing message; invoices rebuilt in Dutch with correct terminology; and the Dutch marketing pages given their own addresses with alternate-language annotations.

**Result:** wrong-day arrivals reported by practices dropped to near zero over the following two months, and two practices that had been evaluating a competitor stayed.

> *"Everything was translated. It still felt like a foreign product, and it turned out the reason was that we were showing Dutch physiotherapists American dates."*
> — **Lotte Verhoeven, Founder, Praktijkplanner (Eindhoven)**

**Cost & Timeline:** €3,250 (string extraction, locale-aware formatting, language preference and email routing, Dutch invoicing, language signals) — completed in 7 business days.

## Frequently Asked Questions

### Is adding a second language just a translation job?

No. Translation is roughly a quarter of it. Extracting text from generated components, making dates, numbers and currency follow the user's locale, routing emails in the right language and handling search per language are the rest, and they are what make a product feel native.

### Why do my Dutch users receive English emails?

Because the interface language usually lives in the browser while emails are generated on the server. Store a language preference on the account and use it for every outgoing message, with a sensible default derived at signup.

### Do I need separate URLs for each language?

For public pages you want indexed, yes. A page that changes language based on a stored preference gives a crawler only one version. Use distinct paths and declare the alternate-language relationships.

### Should I machine-translate the interface?

As a starting point it is acceptable, with a native speaker reviewing before release. For legal documents it is not appropriate — use a professional translation or state clearly which language version governs.

### What formatting differences actually matter for Dutch users?

Date order and written months, comma as decimal separator, 24-hour time, weeks starting on Monday, Dutch postcode layout, and surname prefixes that affect sorting and name fields.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Is adding a second language just a translation job?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No — translation is about a quarter of it. String extraction, locale-aware dates, numbers and currency, language-routed emails and per-language search are the rest."
      }
    },
    {
      "@type": "Question",
      "name": "Why do my Dutch users receive English emails?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Interface language usually lives in the browser while emails are generated server-side. Store a language preference per account and use it for every outgoing message."
      }
    },
    {
      "@type": "Question",
      "name": "Do I need separate URLs for each language?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "For public pages you want indexed, yes — distinct paths with alternate-language annotations, since a crawler sees only one version of a preference-driven page."
      }
    },
    {
      "@type": "Question",
      "name": "Should I machine-translate the interface?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "As a starting point with native review, yes. For legal documents use a professional translation or state which language version governs."
      }
    },
    {
      "@type": "Question",
      "name": "What formatting differences actually matter for Dutch users?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Date order and written months, comma decimal separator, 24-hour time, Monday week start, postcode layout and surname prefixes affecting sorting."
      }
    }
  ]
}
</script>
