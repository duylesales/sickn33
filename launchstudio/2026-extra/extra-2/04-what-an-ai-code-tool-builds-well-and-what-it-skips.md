---
Title: "What an AI Code Tool Builds Well, and What It Quietly Skips"
Keywords: ai code tool, ai coding, build ai, LaunchStudio, Manifera
Buyer Stage: Awareness
Target Persona: Technical Solo Founder / Indie Hacker
---

# What an AI Code Tool Builds Well, and What It Quietly Skips

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "What an AI Code Tool Builds Well, and What It Quietly Skips",
  "description": "Myth-busting five common assumptions about what an AI code tool actually delivers, and a specific look at where an unguarded admin route tends to hide in AI-generated projects.",
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
  "datePublished": "2026-07-22",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://launchstudio.eu/en/blog/what-an-ai-code-tool-builds-well-and-what-it-skips"
  }
}
</script>

Every AI code tool on the market today — v0, Bolt, Lovable, Cursor — is genuinely good at what it's built for: turning a described feature into working, visually correct code, fast. The confusion starts when founders quietly extend that competence to areas the tool was never actually built for, like access control, abuse prevention, or the specific question of what happens when a route gets requested by someone who was never supposed to see it in the first place.

## Myth: An AI Code Tool Builds a Complete Application

**Reality:** it builds the application you specifically described, which is a narrower thing. If a founder describes "an admin dashboard for managing users" without also specifying "and only admins should be able to reach it," there's a reasonable chance the resulting code renders the dashboard correctly for an admin and simply doesn't consider what an unauthenticated or lower-permission visitor typing the same URL directly would see, because that scenario was never part of the description in the first place.

## Myth: If It Wasn't Linked in the Navigation, Nobody Will Find It

**Reality:** hiding a route from the visible UI is not the same as protecting it. A route that exists on the server responds to a request regardless of whether a navigation link points to it, and search engines, browser history, shared URLs, and simple guessing (`/admin`, `/dashboard`, `/internal`) are all realistic ways an unlinked route gets discovered by someone who was never meant to see it.

## Myth: Basic Login Is the Same as Role-Based Access

**Reality:** many AI-generated apps correctly implement "is this person logged in at all" while never separately implementing "and does this specific logged-in person have the specific role required for this specific page." The first check is a much lower bar than the second, and it's entirely possible for an app to pass the first while failing the second completely.

## Myth: A Working Demo of the Admin Panel Proves It's Protected

**Reality:** a demo proves the admin panel works correctly when the person demoing it is, in fact, the admin. It proves nothing about what happens when someone who isn't the admin tries the same URL, because that's simply a different request that a cooperative demo never generates.

## Myth: This Is a Minor Gap Compared to "Real" Security Issues

**Reality:** an unprotected admin route is often the single highest-value target in an entire application, since admin panels typically expose exactly the kind of broad, sensitive controls — user management, data export, billing overrides — that a narrower vulnerability elsewhere wouldn't. Treating it as a footnote tends to be the opposite of the actual risk it represents.

## What Closing This Gap Looks Like in Practice

The fix is a specific, scoped piece of engineering: adding a server-side role check to every sensitive route, not just the ones currently linked in the UI, and verifying that check independently of whatever the frontend displays. [LaunchStudio](https://launchstudio.eu/en/) runs exactly this kind of route-by-route access review as part of its Launch Ready package, backed by Manifera's 11+ years of experience building role-based access systems for enterprise clients.

Manifera's engineering work is coordinated between its Amsterdam headquarters at Herengracht 420 and its main development center on Pho Quang Street in Ho Chi Minh City, with its Singapore hub at 100 Tras Street supporting regional partnerships across Southeast Asia.

[Talk to an engineer who understands AI-generated code](https://launchstudio.eu/en/#contact).

## Real example

### An AI-Native Founder in Action: The Admin Panel Anyone Could Reach

Lotte, a former estate agent turned founder in Groningen, built PandBoard, an AI-assisted real estate listing tool built with v0, including an internal admin panel for managing listings and agent accounts.

A routine search-engine indexing check turned up her admin panel URL sitting in Google's index, fully reachable without any login redirect. LaunchStudio's review confirmed the admin routes had no server-side role check at all — only a login form that, if bypassed by directly requesting the underlying page, granted full access.

**Result:** LaunchStudio added independent server-side role verification to every admin route, closing public reachability entirely regardless of navigation links or search indexing.

> *"I genuinely thought a login page in front of it meant it was protected. I had no idea the page behind the login was reachable directly the whole time."*
> — **Lotte Janssen, Founder, PandBoard (Groningen)**

**Cost & Timeline:** €1,900 (admin route access control audit) — completed in 7 business days.

---

## Frequently Asked Questions

### Would this exact gap show up the same way in a Next.js app as it did in Lotte's v0-generated project?

The specific file structure differs, but the underlying risk is identical — Next.js API routes and server components still need an explicit role check, and a page that "looks protected" by a client-side redirect is just as reachable directly as any other unguarded route.

### Does Manifera's experience serving Vodafone-scale clients mean small founder projects get a lighter version of the same review?

The review scope is matched to what the project actually needs rather than artificially scaled up or down — a real estate listing tool with one admin panel doesn't require the same review as a telecom's internal systems, but the specific technique applied to the admin panel itself doesn't change.

### CEO Herre Roelevink often notes that founders underestimate architecture risk relative to visible bugs — does an indexed admin panel fit that pattern?

Almost exactly — it's invisible until a search engine or a curious visitor stumbles onto it, which is the defining trait of the architecture-level gaps Roelevink has repeatedly pointed to in his commentary on AI-generated software.

### Is there a quick way for a founder to check whether their own admin routes are indexed before reaching out for a full review?

A basic search for the site's known internal URLs, and checking whether a logged-out browser session can load an admin page directly by URL, are reasonable first checks — though a full review also tests routes that were never linked anywhere and wouldn't show up in either of those checks.

### Why would LaunchStudio's Singapore office come up in a review that's really being done by the Vietnam team?

Singapore functions primarily as a regional coordination and partnership hub rather than the location doing hands-on code review — it's mentioned mainly to explain how Manifera's Southeast Asia presence supports LaunchStudio's broader operating footprint, not because it changes who performs the actual engineering work.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Does this admin-route gap show up the same way in Next.js apps?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "The file structure differs but the underlying risk is identical — an explicit server-side role check is still required."
      }
    },
    {
      "@type": "Question",
      "name": "Do small founder projects get a lighter review than enterprise clients?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Review scope matches project needs, but the specific technique applied to a gap like this doesn't change with company size."
      }
    },
    {
      "@type": "Question",
      "name": "Does an indexed admin panel fit the architecture-risk pattern the CEO describes?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Almost exactly — it's invisible until discovered, the defining trait of the architecture-level gaps he's pointed to."
      }
    },
    {
      "@type": "Question",
      "name": "Can a founder check for this themselves before a full review?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Searching for known internal URLs and testing logged-out access are reasonable first checks, though not fully comprehensive."
      }
    },
    {
      "@type": "Question",
      "name": "What role does the Singapore office play if Vietnam does the actual review?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Singapore is primarily a regional coordination hub, not the location performing the hands-on engineering work."
      }
    }
  ]
}
</script>
