---
Title: "Replit Custom Domain: Going Live on Your Own Address"
Keywords: Replit, lovable custom domain, dns records, ssl certificate, domain ownership, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: AI-Native Founder (non-technical)
---

# Replit Custom Domain: Going Live on Your Own Address

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Replit Custom Domain: Going Live on Your Own Address",
  "description": "Moving from a platform address to your own domain: the DNS records, certificates, the www decision, why email is a separate problem, and why the domain must be registered in your own name.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-08-07",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/replit-custom-domain-going-live-on-your-own-address" }
}
</script>

You are on a call with a prospective customer — a Dutch company with forty employees and a procurement process — and they ask where they can see it. You send the link. It contains the name of a development platform and a string that looks like an identifier, and you find yourself explaining what it is before you explain what the product does.

That is the entire argument for a custom domain, and it is enough on its own. But there are three more reasons, and one of them will cost you a great deal if you get it wrong at the start.

## What a Custom Domain Actually Changes

**Credibility, immediately.** A business buyer evaluating an unfamiliar supplier reads the address as a signal of permanence. A platform subdomain says experiment.

**Email that arrives.** Sending from a free mailbox undermines the same impression, and sending from a domain you do not control makes proper authentication impossible. Your own domain is a prerequisite for email that reaches inboxes rather than spam folders.

**Search visibility that accumulates to you.** Reputation earned by a platform subdomain is not portable. Every link, every mention and every ranking earned on your own domain follows you wherever you host next.

**Freedom to move.** This is the one that matters most and is appreciated least. With your own domain, changing platform is a DNS change nobody outside notices. Without it, changing platform means changing the address every customer has bookmarked, every partner has linked, and every document references.

## The Records You Will Touch

DNS sounds technical and is mostly two record types.

**An A record** points a name directly at an address — typically used for your bare domain, such as `yourcompany.nl`.

**A CNAME record** points one name at another name — typically used for `www.yourcompany.nl` or a subdomain like `app.yourcompany.nl`.

The platform tells you which to create and with what values; your registrar is where you create them. Two practical notes. Changes are not instantaneous — allow for propagation, and resist the urge to change things repeatedly while waiting, which is how people create problems they then have to diagnose. And every domain has a TTL setting that determines how long answers are cached; lowering it a day before a planned move makes the cutover faster.

## Certificates and the Padlock

Every site needs HTTPS. Without it browsers mark the page as not secure, which is the single most effective way to lose a visitor who arrived interested.

Platforms generally issue and renew a certificate automatically once your DNS is pointing correctly, which removes what used to be an annoying manual task. Two things still go wrong. A certificate cannot be issued while DNS is misconfigured, so an early failure usually means a record is wrong rather than anything deeper. And a certificate covering `www` but not the bare domain, or the reverse, produces warnings for half your visitors — which is why the next decision matters.

## Pick One Address and Redirect the Other

`yourcompany.nl` and `www.yourcompany.nl` are different addresses. So are the HTTP and HTTPS versions of each.

If all four resolve independently, you have four versions of your site, which splits search signals, breaks analytics, and occasionally produces the certificate warning above. Choose one as canonical — either is fine, be consistent — and make every other version redirect to it permanently. Then use that one form everywhere: in your links, your emails, your printed material and your structured data.

## Email Is a Separate Problem

A frequent and expensive misunderstanding: pointing your domain at your application does nothing for email.

Email needs its own records — SPF declaring who may send on your behalf, DKIM signing your messages, and DMARC telling receiving servers what to do with messages that fail. Without them, transactional email from your product — password resets, confirmations, invoices — lands in spam at a rate you will not measure and customers will not report. They will simply say they never received it.

Set these up when you set up the domain, send a test to several providers, and check where it lands. Also check that your sending address is a real mailbox somebody monitors, because replies to a no-reply address are a category of lost customer nobody counts.

## One Address, One Canonical, for Search

Once traffic matters, three small things save future work.

Set a canonical URL on every page pointing at the chosen form of your domain. Make sure your sitemap and any structured data use that same form. And if you were previously sharing the platform address anywhere public, redirect it if the platform allows, so the attention already earned follows you.

## Register the Domain in Your Own Name

The failure that turns a small problem into a large one.

A domain registered by a freelancer, an agency, a former co-founder or a well-meaning friend belongs to whoever is named on it. When the relationship ends, or that person stops answering email, the recovery process is slow, occasionally impossible, and always worse than the five minutes it would have taken to register it correctly.

Register it under an account your company controls, with billing that will not expire, renewal set to automatic, and ideally more than one person able to reach the account. Then check the registration is actually in your name rather than assuming, which takes one lookup.

## The Checklist Before You Announce It

Both `www` and bare versions resolve and one redirects to the other. HTTPS works on every version, with no mixed-content warnings. Email authentication records are in place and a test message reaches a real inbox. Internal links, canonical tags and sitemap all use the chosen form. The domain is registered to you with automatic renewal. And the platform address is no longer what you send to anybody.

## Subdomains and the Addresses You Will Need Later

Most founders set up one address and then discover, over the following year, that they need four. Planning the shape now costs nothing and prevents a second migration.

**The marketing site and the application.** Two common arrangements: the application on a subdomain such as `app.yourcompany.nl` with the marketing site on the main domain, or both on the main domain with the application under a path. The first is cleaner operationally — the two can be hosted separately, deployed independently, and the marketing pages can be static while the application is not. The second keeps everything in one place, which is simpler until it is not.

**A staging address,** such as `staging.yourcompany.nl`, once anyone depends on you. This is where a change is confirmed working before customers see it. Block it from being indexed, and put it behind a password so it is not accidentally public.

**A blog or documentation.** Keep it on the main domain rather than a separate domain. Reputation earned by content accrues to the domain it lives on, and splitting it across two names halves the benefit for no gain.

**A status page,** hosted somewhere other than your own infrastructure, so that it still works during the event it exists to describe.

Two technical consequences of splitting across subdomains. Cookies and sessions do not automatically work across them, so if visitors move between your marketing site and your application while logged in, that behaviour needs deliberate configuration. And each subdomain needs its own certificate coverage, which is automatic on most platforms but worth verifying rather than assuming.

**If you ever want a subdomain per customer** — `klantnaam.yourcompany.nl` — decide early. Supporting it means wildcard DNS and wildcard certificates, and retrofitting it onto a product whose customers already have bookmarked addresses is considerably more work than building it in.

Write the intended shape down on one page: which name points where, what each is for, where the certificate comes from, what is blocked from indexing. It takes ten minutes, it is the document you will hand to whoever helps you next, and it is the thing nobody has when they ask for help.

## Doing It Once, Properly

For most projects this is an afternoon, and it is worth doing carefully because the cost of doing it twice falls on your customers.

LaunchStudio handles it as part of going live: domain and DNS configured with the canonical form chosen and redirects in place, certificates verified across every variant, email authentication set up and delivery tested against the major providers, canonical tags and sitemap aligned, ownership confirmed in your own name with automatic renewal, and the whole configuration documented so you can change hosting later without help.

Behind it is Manifera: eleven years of production work for clients including Vodafone, TNO and CFLW, from Amsterdam and Ho Chi Minh City. [Tell us your domain and where it points](https://launchstudio.eu/en/#contact), or see what the [Launch Ready package](https://launchstudio.eu/en/#packages) includes.

## Real example

### A Domain Registered by Someone Who Stopped Answering

Ilse Brandsma built Proefles on Replit: a trial-lesson booking tool used by four music schools and two dance studios around Breda. A friend who had helped her at the beginning had registered the domain on his own account, paid for it on his own card, and pointed it at the project.

Eighteen months later the friend had moved abroad and stopped replying. The domain's renewal was approaching, the card on file had expired, and Ilse had no access to the registrar account. She also could not add email authentication records, which meant booking confirmations had been reaching spam folders for a year — something she discovered only when a music school mentioned that confirmations "usually turn up eventually, in the junk".

Recovery took eleven days through the registrar's dispute process, with documentation of her business's use of the name, and it succeeded only because the friend eventually responded to a registrar notification.

Three business days of work once access was restored: domain transferred to an account owned by her company with automatic renewal and two administrators; the canonical form chosen with redirects from every other variant; certificates verified; SPF, DKIM and DMARC configured and delivery tested against four major providers; the sending address changed from no-reply to a monitored mailbox; canonical tags and sitemap aligned; and the DNS configuration documented.

**Result:** confirmation emails now reach inboxes — one dance studio reported that no-shows for trial lessons fell noticeably in the following two months — and a planned hosting change three months later required a single DNS edit.

> *"My domain belonged to someone who had moved to New Zealand and stopped reading his email. It took eleven days and a dispute process to get back a name my customers had been typing for a year."*
> — **Ilse Brandsma, Founder, Proefles (Breda)**

**Cost & Timeline:** €900 (domain transfer and ownership setup, redirects and certificates, email authentication with delivery testing, canonical alignment, documentation) — completed in 3 business days after access was recovered.

## Frequently Asked Questions

### Which DNS records do I need for a custom domain?

Usually an A record for the bare domain and a CNAME for www, with the exact values given by your platform. Create them at your registrar and allow time for propagation rather than changing them repeatedly while you wait.

### Do I need to do anything about the HTTPS certificate?

Generally no — it is issued and renewed automatically once DNS points correctly. A failure early on almost always means a record is wrong. Check that both the www and bare versions are covered.

### Should I use www or the bare domain?

Either, as long as you choose one, redirect everything else to it permanently, and use that form consistently in links, emails, canonical tags and your sitemap.

### Does pointing my domain at my app fix my email?

No. Email needs its own SPF, DKIM and DMARC records. Without them, password resets and confirmations land in spam at a rate you will not measure and customers will not report.

### Why does it matter whose name the domain is registered in?

Because the person named on the registration controls it. If a freelancer, agency or former collaborator registered it, recovery when they become unreachable is slow and sometimes impossible. Register it under an account your company controls, with automatic renewal.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Which DNS records do I need for a custom domain?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Typically an A record for the bare domain and a CNAME for www, using the values your platform specifies, created at your registrar."
      }
    },
    {
      "@type": "Question",
      "name": "Do I need to do anything about the HTTPS certificate?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Generally no — it is issued and renewed automatically once DNS is correct. Early failures usually mean a misconfigured record; check both www and bare versions are covered."
      }
    },
    {
      "@type": "Question",
      "name": "Should I use www or the bare domain?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Either — choose one, redirect all other versions to it permanently, and use that form consistently everywhere."
      }
    },
    {
      "@type": "Question",
      "name": "Does pointing my domain at my app fix my email?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No. Email needs SPF, DKIM and DMARC records of its own, or transactional messages land in spam unmeasured."
      }
    },
    {
      "@type": "Question",
      "name": "Why does it matter whose name the domain is registered in?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Whoever is named controls it. Recovering a domain from an unreachable freelancer or former collaborator is slow and sometimes impossible."
      }
    }
  ]
}
</script>
