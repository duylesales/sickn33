---
Title: "Who Actually Has 'AI Access' to Your Codebase and Customer Data"
Keywords: ai access, third party ai data access, revoking integration keys, ai model provider data access
Buyer Stage: Consideration
Target Persona: AI-Native Founder (Non-Technical)
---

# Who Actually Has 'AI Access' to Your Codebase and Customer Data

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Who Actually Has 'AI Access' to Your Codebase and Customer Data",
  "description": "Founders rarely audit which AI model providers and integrations have standing access to their codebase and customer data after launch. Here's how to find out, and why old test keys are the usual culprit.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2026-07-27",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/ai-access-who-has-it" }
}
</script>

Ask most founders who has "AI access" to their app and you'll get a shrug, not because they don't care, but because nobody ever showed them where to look. AI access isn't one thing — it's a scattering of integration keys, model provider connections, and test credentials created at different points while the app was being built, most of which quietly outlive the reason they were created. Nobody audits this list because nothing about running the app day to day ever forces you to look at it.

## What "AI access" actually refers to

Every AI coding tool connects your project to at least one underlying model provider to generate code, and often to additional providers for features like chat, search, or content generation once the app is live. Each of those connections is granted through an access key or token, created at some point during development — sometimes for testing, sometimes for a feature that shipped, sometimes for a feature that got abandoned halfway through. The key doesn't get deleted just because its original purpose ended. It keeps working, silently, until someone specifically goes and revokes it.

## Why nobody checks this after launch

There's no natural moment where a founder is prompted to review this list. The app works, customers sign up, everything looks fine from the outside — and a working app gives no visible signal that an old test integration is still sitting there with standing access to production data that didn't exist when the key was created. The key was scoped for a test environment with no real customers in it. Nobody went back and asked whether it should still have that access once real customer files started flowing through the same system.

## How to actually find out who has access

- List every integration and API key connected to your project, including ones created early in development that you may have forgotten about.
- For each one, ask: what is this currently used for, and is that still true?
- Check whether any key created for testing was ever scoped down or revoked once the feature it supported went live.
- Confirm whether your AI model provider's access extends to customer-uploaded content, or only to the application code itself.

This is rarely a five-minute task, because most AI coding tools don't surface this list in one place — it has to be reconstructed by going through the project's integration settings one at a time.

LaunchStudio is powered by Manifera, a software development company with 11+ years of experience auditing exactly this kind of accumulated access across AI-generated codebases. Our Amsterdam team runs this audit as a standard part of taking over a founder's project. If you want to know what your own app's access list actually looks like, you can [calculate what a full access audit would cost](https://launchstudio.eu/en/#calculator), and Manifera's [web application development](https://www.manifera.com/services/web-app-develop/) practice covers the broader engineering context behind that work.

## A 20-Minute Access Audit You Can Actually Run Today

The list-and-ask approach above is the right shape for a proper audit, but it can feel abstract without a concrete starting point. Here's a version scoped tightly enough to actually finish in about twenty minutes, using places most founders already have access to rather than anything requiring a technical background to check.

**Minutes 0–5: pull your environment variables file.** Whether it's called `.env`, a secrets panel in your hosting dashboard, or a configuration tab inside your AI coding tool, this is the single most concentrated list of active keys most apps have. Every entry is something with standing access to your project right now. Copy the list of variable names (not the values) into a document — you're building an inventory, not reviewing each one yet.

**Minutes 5–10: check your billing pages, not your code.** Log into the billing dashboard for every AI model provider, hosting service, or third-party API you can remember signing up for during development. An active subscription or usage-based charge is proof of a live, currently-billed connection — and it's a faster way to surface a forgotten integration than searching code, because a provider you're still being charged for is, by definition, still connected to something.

**Minutes 10–15: check the "connected apps" or "authorized applications" list on any account your project touches.** If your app connects to email, calendar, payment, or storage providers through OAuth, most of those services have a settings page listing every third-party application currently authorized — often with a "revoke" button right next to each one. This surfaces connections that don't show up in your own codebase at all, because the authorization lives on the third-party service's side, not yours.

**Minutes 15–20: match your three lists against each other, and flag anything on only one.** A key in your environment file with no matching active billing charge might be dead and safe to remove. A billing charge with no corresponding key in your environment file might mean the key lives somewhere else you haven't checked yet — worth a follow-up, not something to wave off. An authorized app you don't recognize at all is the highest-priority item on the whole list.

This twenty-minute version won't catch everything a full audit would — subprocessors, scoped permissions within a single key, or access granted through code you haven't personally reviewed all require deeper work. What it reliably catches is the most common version of this problem: a key or connection that's still active, still billed, and long past the point where anyone remembers why it exists. Given how often that turns out to be exactly what's sitting there, twenty minutes spent finding out is a reasonable trade against finding out the hard way instead.

## Real example

### An AI-Native Founder in Action: The Test Key Nobody Remembered to Revoke

Lieve Prinsen, a founder based in Wijchen, built "DataToegang" — a shared document tool for small nonprofits — using Lovable. During development, she connected a third-party AI model provider through an integration key to test a document-summarization feature. The feature shipped in a different form later, using a separate connection, but the original test key was never revoked — it simply stayed active, unnoticed, in the project's settings.

Nobody flagged this because nothing about running DataToegang day to day surfaced it. The test key had been scoped during a phase when the app held only sample documents. By the time real nonprofits were uploading real donor records and internal files, that same key — created for a testing phase that no longer existed — still had standing access to whatever passed through the system, and no one had gone back to ask whether it should.

The gap surfaced during a security review Lieve requested after a partner nonprofit asked, reasonably, exactly which third parties had access to their uploaded files. LaunchStudio's audit turned up the forgotten test key within the first pass through her project's integrations. Our engineers revoked it, mapped every remaining active connection against its actual current purpose, and gave Lieve a documented list she could hand to future partners asking the same question.

**Result:** DataToegang now has a fully documented, current list of every integration with access to customer data, with the unused test key permanently revoked.

> *"I had no idea that key even still existed. Nothing about the app running normally would have ever told me."*
> — **Lieve Prinsen, Founder, DataToegang (Wijchen)**

**Cost & Timeline:** €650 (integration access audit and key revocation) — completed in 3 business days.

---

## Frequently Asked Questions

### How do I find out which AI providers have access to my app right now?

Go through your project's integration and API key settings one at a time and ask what each one is currently used for — most AI coding tools don't summarize this in one place automatically.

### Why do old test keys keep working after the feature they supported is gone?

Because nothing automatically revokes a key just because its original purpose ended. It stays active until someone specifically goes back and removes it.

### Does my AI model provider automatically have access to customer-uploaded content?

It depends on the specific integration and its scope — which is exactly why checking each connection individually matters rather than assuming a single blanket answer.

### How often does Manifera's team find forgotten access like this?

Often enough that it's now a standard step in Amsterdam-based reviews Manifera runs when taking over an AI-generated project — accumulated, unrevoked access is one of the more common findings.

### Is this something I can check myself without a full audit?

You can start by listing every integration in your project's settings and asking what each is for, but a full audit — checking scope, not just existence — is the more reliable route for anything holding real customer data.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "How do I find out which AI providers have access to my app right now?", "acceptedAnswer": { "@type": "Answer", "text": "Go through your project's integration and API key settings one at a time and ask what each one is currently used for, since most AI coding tools don't summarize this in one place automatically." } },
    { "@type": "Question", "name": "Why do old test keys keep working after the feature they supported is gone?", "acceptedAnswer": { "@type": "Answer", "text": "Because nothing automatically revokes a key just because its original purpose ended. It stays active until someone specifically goes back and removes it." } },
    { "@type": "Question", "name": "Does my AI model provider automatically have access to customer-uploaded content?", "acceptedAnswer": { "@type": "Answer", "text": "It depends on the specific integration and its scope, which is why checking each connection individually matters rather than assuming a single blanket answer." } },
    { "@type": "Question", "name": "How often does Manifera's team find forgotten access like this?", "acceptedAnswer": { "@type": "Answer", "text": "Often enough that it's now a standard step in Amsterdam-based reviews Manifera runs when taking over an AI-generated project." } },
    { "@type": "Question", "name": "Is this something I can check myself without a full audit?", "acceptedAnswer": { "@type": "Answer", "text": "You can start by listing every integration in your project's settings and asking what each is for, but a full audit checking scope, not just existence, is more reliable for anything holding real customer data." } }
  ]
}
</script>
