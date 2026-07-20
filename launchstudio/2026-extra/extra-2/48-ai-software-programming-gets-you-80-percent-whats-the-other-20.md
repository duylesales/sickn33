---
Title: "AI Software Programming Gets You 80%. What's the Other 20%?"
Keywords: ai software programming, ai software app, ai coding, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: AI-Native Founder (Non-Technical)
---

# AI Software Programming Gets You 80%. What's the Other 20%?

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "AI Software Programming Gets You 80%. What's the Other 20%?",
  "description": "A production-readiness checklist explaining the specific 20% AI software programming tends to leave unfinished, using a permission bug exposing edit access on a shared career-coaching document as the concrete case.",
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
  "datePublished": "2026-08-01",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://launchstudio.eu/en/blog/ai-software-programming-gets-you-80-percent-whats-the-other-20"
  }
}
</script>

Cursor got you 80% of the way there, and that's a genuinely accurate, common founder observation about AI software programming today — it does the bulk of the visible work remarkably well. The remaining 20% tends to concentrate in a specific, checkable list of permission edge cases, and a shared document that's supposed to be view-only, but isn't quite, is a clean illustration of exactly what that list contains.

## Checklist Item One: Does "Read-Only" Actually Mean Read-Only on the Server?

A shared document feature offering both "can view" and "can edit" sharing permissions needs the server, not just the interface, to enforce that distinction — if a "view-only" recipient's edit requests are still processed and saved by the backend regardless of their permission level, the interface hiding the edit controls provides no actual protection at all.

## Checklist Item Two: Is Permission Checked on Every Modifying Request, or Just at Page Load?

Some AI-generated permission systems check a user's access level only once, when a page initially loads, to decide what to display — but if the actual save or update action doesn't separately re-verify that same permission level before processing the request, a view-only user whose interface simply doesn't show edit buttons can still potentially submit an edit request directly.

## Checklist Item Three: Would a Founder's Normal Testing Reveal This?

Testing sharing permissions by inviting a real second account, viewing as intended, and confirming the interface correctly hides edit controls looks completely correct — because it is correct from the interface's perspective. The gap only reveals itself if someone specifically tries to submit an edit request despite the interface not offering one, which cooperative testing has no reason to attempt.

## Checklist Item Four: Does This Matter More for Coaching-Adjacent Content Specifically?

A career coaching platform's shared documents often contain genuinely personal content — a client's career goals, salary expectations, personal reflections shared with a specific coach — meaning unauthorized modification isn't just a technical inconvenience, it's a real breach of the kind of trust a coaching relationship specifically depends on.

## Checklist Item Five: How Does a Founder Know Whether Their Own Product Has This Gap?

Without specifically testing an edit request from a view-only account's perspective, a founder generally can't know one way or the other from ordinary use alone — this specific check requires either technical comfort with directly crafting such a request, or a dedicated review that tests exactly this scenario as a matter of routine.

## Closing This Gap Without Overcomplicating Sharing

A proper fix re-verifies permission level on every modifying request server-side, independent of what the interface happens to display, applied consistently across every shared or collaborative feature in a product. [LaunchStudio](https://launchstudio.eu/en/) tests exactly this pattern as part of its access-control review, backed by Manifera's 11+ years of experience building permission systems for collaborative software.

Manifera's permission and access-control audits are performed by the engineering team at the Ho Chi Minh City development center on Pho Quang Street, coordinated with the Amsterdam headquarters at Herengracht 420.

[Walk us through what you built — we'll respond within a business day](https://launchstudio.eu/en/#contact).

## Real example

### An AI-Native Founder in Action: The View-Only Document a Client Could Still Edit

Luuk, a former HR career transition consultant turned founder in Harderwijk, built LoopbaanPad, an AI-assisted career coaching platform built with Lovable, letting coaches share planning documents with clients using either view-only or edit permissions depending on the specific document.

A coach noticed a client's shared, supposedly view-only career plan had been modified, with the client insisting they'd only ever clicked around the document without realizing edits were even possible. LaunchStudio's review confirmed the document-update endpoint accepted and saved edit requests regardless of the sharing permission recorded for that specific user, meaning the "view-only" restriction existed only in which buttons the interface displayed, not in what the server actually allowed.

**Result:** LaunchStudio added server-side permission verification to every document-update request, ensuring a view-only share genuinely cannot modify content regardless of how the request is made, closing the gap without changing how coaches configured sharing permissions.

> *"The client wasn't even trying to do anything wrong, near as we can tell — some UI action just happened to trigger a save that should never have been allowed to go through in the first place. It really could have been a much less innocent situation."*
> — **Luuk Timmermans, Founder, LoopbaanPad (Harderwijk)**

**Cost & Timeline:** €2,000 (permission verification audit across shared documents) — completed in 6 business days.

---

## Frequently Asked Questions

### Would an access-control specialist consider interface-only permission enforcement a common shortcut in quickly built features?

Yes, quite common — it's genuinely faster to build a sharing feature that only adjusts what the interface displays based on permission level, and the shortcut works perfectly well for every test that interacts with the product exactly as the interface presents it, which is exactly what makes it easy to overlook.

### Is this kind of gap specific to document-sharing features, or does it show up in other collaborative features too?

It generalizes to any feature with more than one permission level sharing access to the same resource — shared calendars, shared project boards, and comment permissions on shared content all face the same underlying question of whether the server, not just the interface, actually enforces the distinction.

### Manifera has built permission systems for collaborative software across various industries — does that experience transfer specifically to a career coaching context like LoopbaanPad's?

Yes, directly — the underlying permission-verification pattern is identical regardless of the collaborative software's specific purpose, and having implemented and reviewed this pattern across many different collaborative contexts makes catching and correctly closing the gap considerably faster for any new client, coaching-specific or otherwise.

### CEO Herre Roelevink has spoken about the last 20% being where architecture, not raw features, determines whether a product is genuinely trustworthy — does this permission gap illustrate that well?

Very well — LoopbaanPad's sharing feature worked exactly as described from a feature-list perspective, with the missing piece being a specific architectural decision about where permission gets actually enforced, precisely the last-20% distinction Roelevink's commentary on AI-native founders' remaining gap consistently emphasizes.

### If a founder specifically prompts their AI tool to "enforce view-only permissions properly," does that reliably solve this?

It can help direct the tool's attention to the requirement, but reliably confirming the resulting implementation actually enforces permission server-side, on every relevant request rather than just at initial page load, still benefits from an independent technical verification rather than trusting the prompt's intention was fully and correctly translated into the generated code.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Is interface-only permission enforcement a common shortcut?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes, quite common, since it's faster to build and works fine for any test that follows the interface as presented."
      }
    },
    {
      "@type": "Question",
      "name": "Is this gap specific to document-sharing features?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No, it generalizes to any feature with multiple permission levels sharing access to the same resource."
      }
    },
    {
      "@type": "Question",
      "name": "Does permission-system experience transfer to a career coaching context specifically?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes, the underlying pattern is identical regardless of the collaborative software's specific purpose."
      }
    },
    {
      "@type": "Question",
      "name": "Does this gap illustrate the last-20%-is-architecture point the CEO makes?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Very well — the feature worked as described; the missing piece was where permission gets actually enforced."
      }
    },
    {
      "@type": "Question",
      "name": "Does prompting an AI tool to enforce permissions properly reliably solve this?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "It can help, but independent technical verification is still needed to confirm the actual implementation."
      }
    }
  ]
}
</script>
