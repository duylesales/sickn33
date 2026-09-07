---
Title: "Embedding Your Product Somewhere Else: Widgets and Iframes"
Keywords: embeddable widget SaaS, iframe embed security, third party cookies embed, booking widget on customer site, embed script versioning, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: Technical Solo Founder / Indie Hacker
---

# Embedding Your Product Somewhere Else: Widgets and Iframes

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Embedding Your Product Somewhere Else: Widgets and Iframes",
  "description": "A booking form or widget running on your customer's website is code you own executing on a page you do not control. The decisions behind it: iframe versus script, browser restrictions on third-party cookies, styling, and versioning something you can never take back.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-04-19",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/embedding-your-product-somewhere-else-widgets-and-iframes" }
}
</script>

For a whole category of products — booking, scheduling, forms, reviews, chat, calculators — the natural distribution is not customers logging into your product but a piece of it running on their own website. It is a strong position to be in: your product becomes part of their site, and removing it is a change they have to plan rather than a subscription they can quietly cancel.

It also means your code runs inside pages built by strangers, on unknown platforms, next to conflicting scripts, under browser rules designed to restrict exactly this kind of cross-site behaviour. The failure modes are unfamiliar to anyone whose product has only ever run at its own address, and the reports you get — "it doesn't work on my site" — carry almost no diagnostic information.

## Iframe or Script: The Decision That Determines Everything After

**An iframe** loads your page inside a frame on theirs. Your styles and code are isolated: nothing on their page can break yours, and nothing of yours leaks into theirs. Predictable, secure, and it looks like a box on their page — sizing is awkward, styling to match their site is limited, and it cannot overlay content.

**A script embed** loads your JavaScript, which inserts elements directly into their page. Visually seamless, fully stylable, capable of modals and overlays — and now sharing an environment with whatever else that page runs. Their CSS can break your layout, their library versions can conflict with yours, and your script has access to their page in a way their security team may reasonably object to.

There is a third option that resolves most of the tension: **a script that creates an iframe**, giving a single-line installation, dynamic sizing through messages between the frame and the page, and the ability to position an overlay — while the content itself stays isolated. For most products this is the right answer, and it is what mature embeddable products converge on.

Whichever you choose, keep the installation to one line the customer pastes. Anything longer will be pasted incorrectly by someone using a website builder they only half understand.

## Browser Restrictions Are the Part That Breaks Silently

Your embed runs in a third-party context, and browsers have spent several years restricting what that context may do. This is where embeds fail in ways that never appear in your own testing.

**Cookies set by your embed are third-party cookies** in that page, and Safari and Firefox block them outright while Chrome restricts them heavily. Anything relying on a cookie to remember a visitor between page loads will work in your development environment — where it is first-party — and fail on a customer's site. The workaround is to avoid depending on cookies at all: keep state in the URL, in the frame's own storage where available, or on your server keyed by something passed in explicitly.

**Storage inside an iframe may be partitioned or unavailable**, particularly in private browsing. Every read must handle the case where it is empty or throws, and the embed must still work correctly with no stored state.

**Content Security Policy on their site can block you entirely.** A customer with a strict policy will find your script refused, with an error only visible in the browser console. Document precisely what needs to be permitted so their developer can add it in one step.

**Ad blockers and privacy extensions block third-party scripts**, sometimes by pattern. If your script path contains words like `track`, `analytics`, or `widget`, a share of visitors will never load it.

Building an embed that works under third-party restrictions, degrades sensibly when storage is unavailable, and can be diagnosed remotely is a specific engineering skill, and it is a common gap in AI-generated products where an embed is developed and tested only on the developer's own page. LaunchStudio, backed by Manifera's 11+ years of production engineering, builds embeds that behave on real customer websites. [Describe your project](https://launchstudio.eu/en/#contact) for a review within one business day.

## Security Runs Both Ways

Your embed must protect the host page, and your product must protect itself from the host page.

Protecting them: your script should not read their page's data, should not interfere with their analytics, and should be defensive about the global environment rather than assuming ownership of it. Their security team may ask for a subresource integrity hash so the browser refuses your script if it changes unexpectedly — a reasonable request that requires immutable, versioned script URLs.

Protecting you: the embed identifies itself with a public key, which is visible to anyone viewing the page source. That key must therefore be restricted, not powerful. Two controls matter. **Domain restrictions**: the customer registers the domains their embed may run on, and requests from elsewhere are refused — which prevents someone copying your customer's embed onto their own site and consuming their quota. And **narrow permissions**: the public key should permit only the specific operations the embed needs, never anything that could read other customers' data or perform administrative actions.

The other risk is what the embed collects. A widget on a customer's website processes their visitors' data, which makes you a processor in that relationship, and it means their cookie consent obligations may cover your embed. Products that set cookies or store identifiers without the host site's knowledge create a compliance problem for their own customer, which is a poor way to be discovered.

## Versioning Something You Cannot Take Back

Once your snippet is pasted into a thousand websites, you cannot change it. Some of those sites will never be touched again by anyone.

Two rules follow. **Version the loader in the URL** and treat it as permanent: `v1` continues to work forever, incompatible changes go to `v2`, and customers upgrade by changing one line when they choose. **Keep the loader tiny and stable** — a small script whose only job is to fetch the current implementation — so improvements can be deployed without customers changing anything, while the entry point stays fixed.

Then the operational consequence people underestimate: this file becomes one of your most availability-critical assets. If it fails to load, your customer's booking form is missing from their website, and they will discover it from their own customers. Serve it from a CDN, keep it small, and make sure a failure degrades to something explicable rather than to an empty space where the form should be.

Finally, give yourself a way to diagnose problems you cannot reproduce. Errors occurring inside an embed on someone else's site are invisible unless you deliberately report them, tagged with the account and the host page. "It doesn't work on my site" is otherwise an unsolvable ticket.

## Real example

### The Booking Widget That Worked Everywhere Except Safari

Milan Novak ran Boekmoment, a booking tool for salons and small clinics, built in Lovable. The booking widget was a script embed that inserted a form into the customer's page and used a cookie to remember partially completed bookings across page loads.

It was tested on his own site and on two customer sites, both on WordPress in Chrome. After launch, salons reported that some customers complained the form "forgot everything" when they navigated away and came back. The cookie was a third-party cookie in that context and was blocked outright in Safari and Firefox — roughly a third of visitors on mobile in his market.

Two further problems surfaced. The script inserted elements directly into the page, and on four customer sites the salon's own CSS made the form nearly unusable — one rendered the submit button invisible for six weeks before anyone reported it. And the public key had no domain restriction: a copy of one salon's snippet had been pasted on an unrelated site and was creating bookings in their account.

**Result:** the embed was rebuilt as a small versioned loader creating a sandboxed iframe with dynamic sizing, removing the CSS conflicts entirely; state moved out of cookies into the URL and server-side sessions keyed by a token; domain restrictions applied to public keys; and error reporting added, tagged by account and host page.

> "It worked on every site I tested and failed for a third of real visitors. I had no way to know, because the failure happened on someone else's website in a browser I was not using."
> — **Milan Novak, Founder, Boekmoment**

**Cost & Timeline:** embed rebuild with versioned loader and domain restrictions delivered in 4 business days.

## Frequently Asked Questions

### Should an embed use an iframe or a script?

A small script that creates an iframe usually gives the best of both: one-line installation, dynamic sizing, and overlay capability, while keeping your content isolated from the host page's styles and scripts.

### Why does my embed lose state on some browsers?

Because cookies set inside an embed are third-party cookies, blocked by Safari and Firefox and restricted in Chrome. Embeds should avoid depending on cookies and handle storage being unavailable.

### How do I stop someone copying my customer's embed code?

Restrict each public key to the domains the customer registers, and refuse requests from anywhere else. The key is visible in page source, so it must be narrow in permission as well as domain-restricted.

### How should an embed be versioned?

Version the loader URL and treat each version as permanent, keeping the loader small and stable so improvements deploy without customers changing anything. Snippets on sites nobody maintains must keep working indefinitely.

### How do I debug an embed on a site I cannot access?

Report errors from inside the embed to your own service, tagged with the account and host page. Without that, failures on customer websites are invisible and the reports you receive carry no diagnostic detail.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "Should an embed use an iframe or a script?", "acceptedAnswer": { "@type": "Answer", "text": "A small script that creates an iframe usually gives one-line installation, dynamic sizing, and overlay capability while keeping content isolated from the host page's styles and scripts." } },
    { "@type": "Question", "name": "Why does my embed lose state on some browsers?", "acceptedAnswer": { "@type": "Answer", "text": "Cookies set inside an embed are third-party cookies, blocked by Safari and Firefox and restricted in Chrome. Embeds should avoid depending on cookies and tolerate storage being unavailable." } },
    { "@type": "Question", "name": "How do I stop someone copying my customer's embed code?", "acceptedAnswer": { "@type": "Answer", "text": "Restrict each public key to registered domains and refuse requests from elsewhere. The key is visible in page source, so it must also be narrow in permission." } },
    { "@type": "Question", "name": "How should an embed be versioned?", "acceptedAnswer": { "@type": "Answer", "text": "Version the loader URL and treat each version as permanent, keeping the loader small and stable so improvements deploy without customers changing anything." } },
    { "@type": "Question", "name": "How do I debug an embed on a site I cannot access?", "acceptedAnswer": { "@type": "Answer", "text": "Report errors from inside the embed to your own service, tagged with account and host page. Otherwise failures on customer websites are invisible." } }
  ]
}
</script>
