---
Title: "AI Deployment Isn't a Button. Here's What It Actually Requires"
Keywords: ai deployment, deployment of ai, ai coding, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: AI-Native Founder (Non-Technical)
---

# AI Deployment Isn't a Button. Here's What It Actually Requires

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "AI Deployment Isn't a Button. Here's What It Actually Requires",
  "description": "A myth-busting look at what clicking 'deploy' in an AI coding tool actually accomplishes versus what genuine production deployment requires, using missing security headers in a beauty salon booking app as the concrete case.",
  "author": {
    "@type": "Organization",
    "name": "LaunchStudio",
    "url": "https://launchstudio.eu/en/"
  },
  "publisher": {
    "@type": "Organization",
    "name": "Manifera",
    "url": "https://www.manifera.com"
  },
  "datePublished": "2026-07-27",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://launchstudio.eu/en/blog/ai-deployment-isnt-a-button-heres-what-it-actually-requires"
  }
}
</script>

Clicking "deploy" inside an AI coding tool genuinely does put your application on a live, reachable URL — that part isn't an exaggeration. AI deployment, in that narrow sense, works exactly as advertised. What it doesn't automatically configure is the layer of protective headers and settings that tell browsers how to treat your site safely, which is a separate, specific set of decisions a deploy button has no reason to make on your behalf.

## Myth: A Live URL Means Your Deployment Is Complete

**Reality:** having a reachable URL means the deployment succeeded in the narrowest technical sense — code is running somewhere, and requests get a response. It says nothing about whether that response includes security headers instructing browsers to enforce HTTPS strictly, prevent your site from being embedded in a malicious frame elsewhere, or restrict what kinds of content can execute on your pages.

## Myth: If the Site Loads Over HTTPS, You're Already Protected

**Reality:** loading over HTTPS protects the specific connection in progress, but without an HSTS (HTTP Strict Transport Security) header, a browser has no instruction to always insist on HTTPS for your domain going forward — meaning a user who happens to type or follow a plain HTTP link could be silently downgraded to an unencrypted connection, an increasingly rare but real risk this specific header exists to close. This matters most in the exact moment a user is most vulnerable — connecting from an untrusted public Wi-Fi network, where a downgraded connection is precisely the opening a nearby attacker on the same network needs to intercept traffic that should have stayed encrypted the entire time.

## Myth: Security Headers Are an Advanced, Enterprise-Only Concern

**Reality:** security headers are a standardized, well-documented part of basic web security practice applicable to any live website regardless of size or industry — a beauty salon booking site handling customer names, phone numbers, and appointment details faces essentially the same baseline exposure as any other product collecting personal information over the web.

## Myth: An AI Coding Tool Would Add These by Default If They Mattered

**Reality:** deployment platforms and coding tools focus their defaults on getting your specific described application running correctly, not on applying a comprehensive security header policy that wasn't part of what was asked for — the tool isn't making a judgment that headers don't matter, it simply isn't the layer where that decision gets made unless someone specifically configures it. It's worth being precise about where responsibility actually sits here: the hosting platform typically provides the mechanism for setting headers, the AI coding tool builds the application that runs on top of it, and neither one owns the decision of which specific headers your particular product needs — that decision requires someone looking at the finished, deployed product and deliberately configuring it.

## Myth: This Is a One-Time Setting You Configure Once and Forget

**Reality:** header configuration typically lives in deployment or server configuration files that can be inadvertently reset or overwritten during a platform migration, a redeploy from a fresh template, or a significant infrastructure change — meaning it's worth periodically reconfirming rather than assuming a setting made once necessarily persists forever.

## Closing the Gap Between "Deployed" and "Properly Configured"

A proper review confirms HSTS, content-security-policy, and related headers are correctly set for your specific hosting environment, tested against your live domain rather than assumed from a generic template. [LaunchStudio](https://launchstudio.eu/en/) verifies exactly this kind of deployment configuration as part of its standard review, backed by Manifera's 11+ years of production deployment experience across Vercel, AWS, Azure, and DigitalOcean environments.

Manifera's deployment configuration reviews are performed by the engineering team at the Ho Chi Minh City development center on Pho Quang Street, coordinated with the Amsterdam headquarters at Herengracht 420.

[Drop us your prototype link — we'll review it for free](https://launchstudio.eu/en/#contact).

## The Six Headers Worth Actually Knowing About

Security headers aren't one single setting — they're a small family of related but distinct protections, each closing a different, specific gap. Knowing roughly what each one does makes a scanner report considerably less mysterious.

**A quick reference for the headers that matter most:**

1. **HSTS (Strict-Transport-Security)** — tells the browser to always use HTTPS for your domain going forward, preventing a downgrade to an unencrypted connection even if a user follows a plain HTTP link.
2. **Content-Security-Policy** — restricts what sources of scripts, styles, and other content your pages are allowed to load from, meaningfully limiting the damage a successful script-injection attempt (like a stored XSS bug) could actually do.
3. **X-Frame-Options** — prevents your site from being loaded inside a frame on someone else's page, closing off a class of attack called clickjacking, where a malicious site overlays your page invisibly to trick users into clicking something they didn't mean to.
4. **X-Content-Type-Options** — stops browsers from trying to guess a file's type based on its content rather than trusting its declared type, closing a narrow but real avenue for tricking a browser into executing something as a different, more dangerous file type than intended.
5. **Referrer-Policy** — controls how much information about the page a user came from gets sent along when they click a link to another site, limiting accidental leakage of sensitive URLs (like a password reset link) into a third party's server logs.
6. **Permissions-Policy** — explicitly restricts which browser features (camera, microphone, location) your pages are allowed to request at all, reducing the risk if a script-injection vulnerability elsewhere is ever exploited to try requesting one of them.

None of these require a founder to configure them manually with deep technical understanding of each one — the value of a professional review is confirming all six are set correctly and consistently for your specific hosting setup, rather than a founder needing to become fluent in each header's exact syntax themselves.

## Real example

### An AI-Native Founder in Action: The Booking Site With No Headers At All

Sara, a former salon manager turned founder in Maastricht, built KapselKalender, an AI-assisted beauty salon booking app built with v0 for the interface and a connected backend, deployed and running smoothly for several partner salons within weeks of building.

A partner salon's IT-savvy relative, checking the site's configuration out of curiosity using a free online security-header scanner, found KapselKalender had none of the standard protective headers configured at all — no HSTS, no content-security-policy, nothing beyond the platform's bare default. LaunchStudio's review confirmed the deployment had never included any explicit header configuration.

**Result:** LaunchStudio configured the full set of standard security headers appropriate to KapselKalender's hosting setup and verified them against the live domain, closing the gap without requiring any redeployment disruption or change to the booking experience itself.

> *"The site worked perfectly the entire time from a booking perspective, which is exactly why I never thought to check anything underneath that. It took someone running a free online scanner to even show me headers were a thing to check."*
> — **Sara Jansen, Founder, KapselKalender (Maastricht)**

**Cost & Timeline:** €1,400 (deployment security header configuration) — completed in 5 business days.

---

## Frequently Asked Questions

### Would a hosting or infrastructure specialist consider missing security headers a serious gap, or a minor best-practice suggestion?

Serious enough that it's routinely included in standard production-readiness checklists across the industry — it's not the single most severe category of gap a review typically finds, but it's a well-established, low-effort protection that most professional deployment processes apply as a matter of course.

### Can a founder check their own site's header configuration without technical help?

Yes, reasonably easily — free online security-header scanning tools exist specifically for this purpose, requiring only a website's URL to produce a report; understanding and correctly fixing what the report flags is where technical help typically becomes necessary.

### Does the specific hosting platform (Vercel versus AWS versus DigitalOcean) change how these headers get configured?

Yes, meaningfully — each platform has its own specific configuration mechanism for setting response headers, which is exactly why Manifera's cross-platform experience across Vercel, AWS, Azure, and DigitalOcean matters for correctly implementing this regardless of which platform a founder's AI tool happened to deploy to.

### Herre Roelevink has spoken about the architecture layer being where most gaps hide — do deployment headers fit that description?

Yes, precisely — headers are a configuration-level, infrastructure decision rather than a visible application feature, exactly the kind of layer Roelevink's public commentary consistently identifies as the part AI-native founders don't naturally think to check.

### Does fixing missing security headers require any downtime or risk breaking the live site?

Properly implemented, header configuration changes typically don't require downtime and shouldn't affect how the site functions for users, though testing the change against the live domain afterward is a standard, necessary step to confirm nothing was inadvertently affected before considering the fix complete.

### Can a Content-Security-Policy header actually break parts of a site if it's configured too strictly?

Yes, and this is precisely why it's the header most worth having a professional configure rather than copying a generic template — an overly strict policy can accidentally block a legitimate third-party script, font, or embedded widget your site actually relies on, while an overly loose one fails to meaningfully restrict anything. Getting the policy right requires understanding exactly what your specific site legitimately loads and from where.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Are missing security headers a serious gap or a minor suggestion?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Serious enough to be routinely included in standard production-readiness checklists across the industry."
      }
    },
    {
      "@type": "Question",
      "name": "Can a founder check their own site's headers without technical help?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes, free online scanning tools can produce a report; fixing what's flagged typically needs technical help."
      }
    },
    {
      "@type": "Question",
      "name": "Does the hosting platform change how headers are configured?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes, each platform has its own configuration mechanism, requiring cross-platform experience to implement correctly."
      }
    },
    {
      "@type": "Question",
      "name": "Do deployment headers fit the architecture-layer-hides-gaps framing?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes, headers are a configuration-level decision exactly the kind of layer founders don't naturally think to check."
      }
    },
    {
      "@type": "Question",
      "name": "Does fixing missing headers risk downtime or breaking the site?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Properly implemented, it typically requires no downtime, though testing afterward is a standard necessary step."
      }
    },
    {
      "@type": "Question",
      "name": "Can a Content-Security-Policy header break parts of a site if configured too strictly?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes, an overly strict policy can block a legitimate third-party script or widget, which is why it needs careful configuration."
      }
    }
  ]
}
</script>
