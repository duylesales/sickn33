---
Title: "Connecting to a Customer's Other Tools: The OAuth Decisions"
Keywords: OAuth integration SaaS, storing refresh tokens securely, google workspace verification, integration scopes minimum, token expiry handling, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: Technical Solo Founder / Indie Hacker
---

# Connecting to a Customer's Other Tools: The OAuth Decisions

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Connecting to a Customer's Other Tools: The OAuth Decisions",
  "description": "Connecting to Google, Microsoft, or a payment platform on a customer's behalf means holding credentials to someone else's account. What scopes to request, how tokens must be stored and refreshed, the verification processes nobody plans for, and what happens when access is revoked.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-04-11",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/connecting-to-a-customers-other-tools-the-oauth-decisions" }
}
</script>

The moment your product connects to a customer's Google account, their accounting software, or their payment platform, you are holding a credential that acts on their behalf in a system that is not yours. That credential typically does not expire in any useful sense, is stored in your database, and grants whatever you asked for at the moment the customer clicked Allow — which, in most prototype implementations, is considerably more than the feature actually needs.

Integrations are also among the strongest reasons customers choose one product over another, so this is not an argument against building them. It is an argument for understanding what you are taking custody of, because a breach involving stored integration tokens is not a breach of your data. It is a breach of your customers' other systems, through you.

## Ask for the Least, Because You Cannot Un-Ask

The consent screen the customer sees lists what you are requesting, and it is the moment your product is judged. "Read your emails" and "read and delete your files" cause people to abandon the connection, sometimes permanently, even when the underlying feature is innocuous.

Two rules. **Request the narrowest scope that does the job** — read-only where you only read, a restricted scope where the provider offers one. Google, for instance, offers a scope granting access only to files your own application created, which is dramatically less alarming and less risky than access to the customer's whole drive.

**Request incrementally.** Ask for calendar reading when the customer sets up calendar sync, not everything at signup. A customer who has already seen value from one connection consents far more readily to the next, and you avoid asking for permissions that half your customers will never use.

There is a practical consequence to over-asking that founders often discover late: broad scopes push you into stricter verification and, for some providers, an annual third-party security assessment with a real cost attached. Narrow scopes can avoid that entirely.

## Tokens Are Credentials, and Most Prototypes Store Them Badly

An OAuth connection typically leaves you with two things: an access token that expires in an hour, and a refresh token that does not expire in practice and can mint new access tokens indefinitely. That refresh token is the valuable one, and it deserves treatment closer to a password than to ordinary data.

**Encrypt tokens at rest**, with a key held outside the database, so that a database dump does not hand over working access to every connected customer account. This is the single most important measure and the one most commonly missing.

**Never log them.** Tokens appearing in error logs is a routine way for credentials to end up in a third-party logging service with different access controls than your database.

**Handle refresh correctly and in one place.** Access tokens expire constantly, so every call needs to handle the expired case by refreshing and retrying. Implemented ad hoc, this produces a specific bug: two simultaneous requests both refresh, and some providers invalidate the previous refresh token when a new one is issued, so one of the two saves a token that is already dead. The connection then breaks intermittently in a way that is hard to diagnose.

**Delete tokens when the connection is removed**, and revoke them with the provider rather than only deleting your copy. A customer who disconnects expects access to end, and leaving a valid token behind in your database is exactly the kind of detail that turns an ordinary incident into a serious one.

## Connections Break, and Silence Is the Worst Outcome

Every integration will eventually stop working, for reasons that have nothing to do with your product: the customer changed their password, an administrator revoked third-party access, the employee whose account authorised the connection left the company, or the provider expired the grant after a period of inactivity.

What matters is what happens next. The failure mode to avoid is silent: sync stops, nobody is told, and the customer discovers weeks later that their data has been stale since March. This is common because the code path handling a failed refresh usually just logs an error.

The right behaviour is explicit. Mark the connection as broken. Show it prominently in the product, not on a settings page nobody visits. Email the account owner with a one-click reconnect. And distinguish between a temporary failure, which should be retried, and a revoked grant, which will never succeed and needs the customer to act.

There is also an organisational trap worth designing around: a connection authorised by one employee's personal account dies when that person leaves, taking a team's integration with it. Where a provider offers organisation-level or service-account connections, prefer them, and where it does not, at least record and show which person's account a connection depends on.

## Verification, Review, and the Timeline Nobody Plans For

Connecting to a major platform is not purely technical. Google, Microsoft, and Meta all operate review processes, and sensitive scopes trigger the strict versions.

For Google, requesting sensitive or restricted scopes means a verification process involving a demonstration video, a privacy policy meeting specific requirements, domain ownership verification, and — for restricted scopes such as full Gmail or Drive access — an annual security assessment by an approved third party, which carries a substantial cost. Until verification completes, unverified applications face a hard cap on how many accounts may connect and show an alarming warning screen.

The timeline runs from days to several weeks. Founders regularly discover this a fortnight before a launch that depends on the integration, which is the wrong moment. If your product needs a reviewed scope, start the process early, and check first whether a narrower scope avoids the requirement — that single decision has saved more launches than any amount of expediting.

Getting scopes, encrypted token storage, refresh handling, and reconnection flows right is a well-defined piece of production work, and it is a common gap in AI-generated products where an integration is implemented as a happy-path connection that works once. LaunchStudio, backed by Manifera's 11+ years of production engineering, builds integrations that survive expiry, revocation, and the provider's review process. [Describe your project](https://launchstudio.eu/en/#contact) for a review within one business day.

## What to Show the Customer

Three things, and they are quick to build.

**Which connections exist, and what each can do**, in plain language: "Connected to Google Calendar as anna@company.nl — can read and create events." Customers, and particularly their IT administrators, want to see this without inspecting the provider's settings.

**When it last worked**, so a broken connection is visible before it causes a problem.

**How to disconnect**, prominently, with a clear statement of what stops working. A disconnect that leaves the customer unsure whether access was really revoked undermines trust in the whole integration.

For business customers, add one more: a note in your documentation about which scopes you request and why. It is the first thing an IT department asks, and having a written answer converts a multi-day back-and-forth into a link.

## Real example

### The Sync That Had Been Broken Since March

Nienke Bakker ran Afsprakenlijn, an appointment-coordination tool for physiotherapy practices, built in Cursor, which synchronised appointments into practitioners' Google Calendars.

In June, a practice reported double-bookings. Their sync had stopped in March, when the practice manager who originally authorised the connection changed her Google password. The refresh failed, the error was logged, and nothing else happened: no flag in the product, no email, and the connection page still displayed "Connected". Eleven practices were in the same state, three of them for over two months.

The review found two further issues. Refresh tokens were stored unencrypted, meaning a database copy would have granted calendar access to 40 practices. And the original integration had requested full calendar read-write scope across all calendars, where the narrower scope covering only events the application itself created would have been sufficient — a difference that had also put the application into a stricter verification tier.

**Result:** tokens encrypted at rest with a key held outside the database, centralised refresh handling with protection against concurrent refresh, connection health shown in the product with email alerts on failure and one-click reconnect, and scopes narrowed at the next re-authorisation, which removed the stricter verification requirement.

> "Eleven practices thought their calendars were syncing. The product said Connected on every one of them, and it had been wrong since March."
> — **Nienke Bakker, Founder, Afsprakenlijn**

**Cost & Timeline:** integration hardening and connection monitoring delivered in 3 business days.

## Frequently Asked Questions

### How much access should an integration request?

The narrowest scope that performs the feature, requested at the moment the customer enables that feature rather than at signup. Narrow scopes also frequently avoid stricter provider verification requirements.

### How should OAuth refresh tokens be stored?

Encrypted at rest with a key held outside the database, never written to logs, and revoked with the provider when a customer disconnects rather than merely deleted locally.

### Why do integrations break without anyone noticing?

Because a failed token refresh is usually only logged. Connections should be marked broken, shown prominently in the product, and the account owner emailed with a reconnect link.

### How long does Google or Microsoft verification take?

From days to several weeks, depending on the scopes requested. Restricted scopes can also require an annual third-party security assessment, so checking whether a narrower scope avoids review is worth doing before building.

### What happens when the employee who authorised a connection leaves?

The connection typically dies with their account. Prefer organisation-level or service-account connections where the provider offers them, and always show which person's account a connection depends on.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "How much access should an integration request?", "acceptedAnswer": { "@type": "Answer", "text": "The narrowest scope that performs the feature, requested when the customer enables that feature rather than at signup. Narrow scopes also often avoid stricter provider verification." } },
    { "@type": "Question", "name": "How should OAuth refresh tokens be stored?", "acceptedAnswer": { "@type": "Answer", "text": "Encrypted at rest with a key held outside the database, never written to logs, and revoked with the provider when a customer disconnects rather than only deleted locally." } },
    { "@type": "Question", "name": "Why do integrations break without anyone noticing?", "acceptedAnswer": { "@type": "Answer", "text": "A failed token refresh is usually only logged. Connections should be marked broken, shown prominently in the product, and the owner emailed with a reconnect link." } },
    { "@type": "Question", "name": "How long does Google or Microsoft verification take?", "acceptedAnswer": { "@type": "Answer", "text": "Days to several weeks depending on scopes, and restricted scopes can require an annual third-party security assessment. Checking whether a narrower scope avoids review is worth doing first." } },
    { "@type": "Question", "name": "What happens when the employee who authorised a connection leaves?", "acceptedAnswer": { "@type": "Answer", "text": "The connection typically dies with their account. Prefer organisation-level or service-account connections where available, and always show which account a connection depends on." } }
  ]
}
</script>
