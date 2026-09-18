---
Title: "AI App Security: The Keys You Hand Out to Integrations"
Keywords: ai app security, api keys, third party integrations, oauth scopes, supabase security, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: SaaS Scale-Up
---

# AI App Security: The Keys You Hand Out to Integrations

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "AI App Security: The Keys You Hand Out to Integrations",
  "description": "Every integration is a credential going somewhere you do not control — in both directions. How to issue keys that can be scoped and revoked, what to do about the keys customers give you, and why breadth of access is the real risk.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-08-18",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/ai-app-security-the-keys-you-hand-out-to-integrations" }
}
</script>

Integrations are how a product stops being an island, and every one of them is a credential living somewhere you cannot see.

The traffic runs both ways, and founders think about only one direction. Keys you hold, for the services you call — those get attention, because they appear on your invoices. Keys you issue, so customers and partners can call you — those get much less, because they feel like a feature rather than a risk. And keys customers give you, so you can reach into their systems, get the least attention of all, which is unfortunate because they carry the most consequence.

## Three Directions, Three Different Problems

**Keys you hold.** Your payment provider, email service, mapping API, model provider. The risk is leakage and cost, and the controls are the familiar ones: server-side only, restricted, capped, rotated.

**Keys you issue.** A customer wants their own system to push data into yours, or a partner builds on top of you. Now you are the provider, and the risk is a key of yours in somebody else's codebase, deployed by people you will never meet, possibly committed to a repository you cannot see.

**Keys customers give you.** Access to their accounting system, their calendar, their CRM. The risk is that you are now holding the keys to another company's data, and if you are compromised, they are — which is precisely what their procurement team was worried about.

Each needs a different answer. The dangerous move is treating all three as "an API key in an environment variable".

## When You Issue Keys, Assume They Will Leak

Not through malice — through ordinary practice. Keys get committed to repositories, pasted into chat, written into a low-code tool by a contractor, put in a browser-side script by somebody who did not realise, and left behind when an employee leaves.

Design for that. Five properties make an issued key survivable.

**Scoped.** A key that can read invoices should not be able to delete customers. Offering read-only keys costs you very little and removes most of the possible damage.

**Attributable.** Each key belongs to one integration, so you can see what used it and revoke it without breaking everything else. One key per customer, shared across their three integrations, cannot be revoked without an outage.

**Revocable by the customer, instantly, in your interface.** They will need this before you do.

**Visible.** Show when each key was last used and from where. Customers spot their own anomalies faster than you will, and an unused key is one they can safely remove.

**Rotatable without downtime.** Support two valid keys during a changeover, or every rotation becomes an outage nobody wants to schedule.

Add rate limits per key, and a displayed-once-at-creation policy so you store only a hash. If you can display an existing key back to a user, you are storing it in a form that can be stolen.

## The Keys Customers Give You Are a Liability

When a customer connects their accounting system or calendar to your product, you have accepted custody of access to their business.

**Prefer delegated authorisation over passwords.** Where the other service offers OAuth, use it: the customer authorises specific permissions, you never see their password, and they can revoke you from their side without contacting you.

**Request the narrowest scope that works.** Every extra permission is something a reviewer will ask about and something an attacker gains. "Read calendar availability" is a different conversation from "full access to mailbox and calendar".

**Store these credentials differently.** Encrypted, access-restricted, never in application logs, never visible in your admin panel. A support tool that displays a customer's connected credentials is a breach waiting for one bad afternoon.

**Handle expiry and revocation properly.** Tokens expire; customers disconnect. Both should produce a clear message to the customer, not a silent failure that leaves data un-synchronised for three weeks.

**Disconnect fully.** When a customer removes an integration, revoke the token at the source rather than only deleting your copy. Deleting your record leaves an active grant on their side with your name on it, which they will eventually notice.

## Webhooks in Both Directions

If you send webhooks to customers, sign them, document how to verify the signature, and retry with a sensible schedule. A customer whose endpoint is down for an hour should not lose events permanently.

If you receive them, verify signatures, deduplicate by event identifier, and never let an unauthenticated notification change money or access. This is the same discipline as receiving payment notifications, and the same omission appears whenever an integration is generated quickly.

## What Generated Integration Code Gets Wrong

A consistent pattern, worth knowing before you review any of it.

It requests broad scopes, because broad scopes are what make the example work first time. It stores tokens in ordinary columns alongside business data. It writes the full request and response to logs during development, including the credential, and nobody removes it. It ignores token refresh until the integration mysteriously stops after an hour or a month. And it treats every failure as retryable, hammering a partner's API and occasionally getting your account suspended.

Ask explicitly for the opposite: narrowest scopes, encrypted storage, no credentials in logs, refresh handled, and a bounded retry policy with backoff.

## Third-Party Access Is Part of Your Security Story

Once you have integrations, two questions appear in every customer conversation.

**"What can your integration do inside our system?"** Answerable in one sentence if you requested narrow scopes, and uncomfortable if you asked for everything.

**"What happens to our access if you are breached?"** They want to hear that credentials are encrypted, access is restricted internally, and you can revoke everything quickly. Having a tested revocation path — one operation that invalidates all issued keys or all stored customer tokens — is worth building before you are asked.

Add both to the security document you send to procurement teams, alongside the subprocessor list.

## The Inventory Nobody Has

Half an hour, and almost every product yields a surprise.

List every key you hold, where it lives, what it can do, whether it is capped, and when it was last rotated. List every key you have issued, to whom, with what scope, and when it was last used. List every customer credential you hold, with scope and expiry. Then look for the three usual findings: a credential with far more access than the feature needs, an issued key nobody has used in a year, and a stored token belonging to a customer who left.

## What You Do When a Key Is Compromised

It will happen, usually through somebody else's mistake, and having a sequence written down converts a frightening morning into an hour of work.

**Revoke first, investigate second.** The instinct is to understand the scope before acting, and it is the wrong order. Revoking an issued key affects one integration and that customer will accept a short interruption. Leaving it live while you read logs does not.

**Then establish what it did.** Your integration audit trail answers this: which endpoints, from which origins, at what times, on which records. This is the moment logging either pays for itself or reveals its absence, and the difference between "no unexpected use" and "we cannot say" is entirely determined by work done months earlier.

**Tell the customer plainly.** What was exposed, what it could reach, what you found, what you have done. If the leak was theirs — a key committed to a repository, pasted into a browser — say so without blame and help them move the integration server-side. They already feel bad; what they need is the fix.

**Decide whether it is notifiable.** If the key could reach personal data and there is any indication it was used, this is a potential personal data breach with the obligations that follow, including timescales agreed in your data processing agreement. Assess it deliberately rather than hoping, and document the reasoning either way.

**Then reduce the blast radius for next time.** Almost every compromised key turns out to have had more access than the integration needed. Reissue with narrower scope, add a rate limit if there was none, and check whether other customers hold keys with the same excess.

Write this sequence on one page now, while nothing is wrong. During an actual incident, the useful thing is not knowing what to do; it is not having to decide.

## Putting Integration Access on a Sound Footing

For a product with integrations already running, this is bounded work: a full credential inventory in all three directions, issued keys reworked to be scoped, hashed, attributable, rate-limited and revocable by the customer with last-used visibility, stored customer credentials encrypted and removed from logs and admin views, scopes narrowed to what each feature needs with re-consent where required, token refresh and disconnect handled properly at the source, webhook signing and verification in both directions, and a tested mass-revocation path.

LaunchStudio does this as part of production readiness for products selling to Dutch businesses, and writes the two paragraphs that answer procurement's integration questions. The engineers are Manifera's: eleven years of systems integration for clients including Vodafone, TNO and CFLW, from Amsterdam Herengracht 420 and Ho Chi Minh City.

[Tell us what your product connects to](https://launchstudio.eu/en/#contact) and you will get a specific assessment, usually within one business day, or see the [packages](https://launchstudio.eu/en/#packages).

## Real example

### One Key, Twelve Construction Firms, Full Access

Merel Duijvestein built Bouwdossier with Lovable: construction document exchange used by twelve building firms and four architectural practices around Almere, holding drawings, permits, inspection photographs and contracts for about 300 active projects.

The largest customers wanted their project-management systems to push documents in automatically. She had built an API for that, and issued each customer a key. The key was generated once, stored in plain text in her database so she could show it to customers who lost it, carried full access to everything that customer could do including deletion and user management, had no rate limit, and had never been rotated for anyone.

A building firm's IT manager reported the problem himself. Their key had been committed to a repository by a contractor eighteen months earlier, and the repository had been made public during a reorganisation. He had found it while auditing something else.

Ten business days of work: an issued-key system rebuilt with scopes — read, write and administrative as separate grants — with each key hashed rather than stored, shown once at creation, named per integration, rate-limited, and revocable by the customer in their own settings screen with last-used time and origin displayed; all 16 existing keys revoked and reissued with the narrowest scope each integration actually needed, which for nine of them was read-and-upload only; access logs for the exposed key reviewed against the firm's own records, establishing that it had not been used from an unexpected origin; outgoing webhooks signed with documented verification; the incoming endpoint given signature verification and deduplication; an integration audit trail added so every API action is attributable to a named key; and a single operation built that revokes every key for a customer at once.

The review of the exposed key found no unauthorised use. That conclusion was only possible because the logging was added before the answer was needed — a point Merel now makes to prospects.

**Result:** the firm stayed and expanded its contract, and the per-customer key screen became a feature two later prospects mentioned during evaluation.

> *"A key I issued sat in a public repository for months with permission to delete every drawing on three hundred projects. It could have been read-only and nobody would have noticed the difference."*
> — **Merel Duijvestein, Founder, Bouwdossier (Almere)**

**Cost & Timeline:** €4,700 (scoped key system with hashing and self-service revocation, key reissue, webhook signing and verification, integration audit trail, mass revocation) — completed in 10 business days.

## Frequently Asked Questions

### Should I store the API keys I issue to customers?

Only as a hash. Show the key once at creation and never again. If your system can display an existing key back to a user, it is stored in a form that can be stolen from you.

### What scope should an issued key have?

The narrowest the integration actually needs, offered as separate grants — read, write, administrative. Most customer integrations only need to read and add data, and offering read-only removes most of the possible damage.

### How should I hold credentials a customer gives me?

Encrypted, access-restricted, never in logs and never visible in an admin panel. Prefer delegated authorisation over passwords, request the narrowest scope, and revoke at the source when a customer disconnects rather than only deleting your copy.

### What does generated integration code typically get wrong?

Broad scopes, tokens stored in ordinary columns, credentials written into logs during development, token refresh ignored, and unbounded retries that hammer a partner's API. Ask explicitly for the opposite.

### What will customers ask about our integration?

What your integration can do inside their system, and what happens to that access if you are breached. Narrow scopes and a tested path that revokes everything quickly make both answerable in a sentence.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Should I store the API keys I issue to customers?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Only as a hash, shown once at creation. If you can display an existing key back to a user, it can be stolen from you."
      }
    },
    {
      "@type": "Question",
      "name": "What scope should an issued key have?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "The narrowest the integration needs, as separate read, write and administrative grants — most customer integrations only read and add data."
      }
    },
    {
      "@type": "Question",
      "name": "How should I hold credentials a customer gives me?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Encrypted, access-restricted, never in logs or admin panels, with delegated authorisation, narrow scopes, and revocation at the source on disconnect."
      }
    },
    {
      "@type": "Question",
      "name": "What does generated integration code typically get wrong?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Broad scopes, tokens in ordinary columns, credentials in logs, ignored token refresh, and unbounded retries against a partner's API."
      }
    },
    {
      "@type": "Question",
      "name": "What will customers ask about our integration?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "What it can do inside their system and what happens to that access if you are breached — both answerable with narrow scopes and a tested revocation path."
      }
    }
  ]
}
</script>
