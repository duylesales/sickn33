---
Title: "AI App Security: Admin Panels and the Access Nobody Audits"
Keywords: ai app security, admin panel, privileged access, impersonation, Lovable, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: Technical Solo Founder / Indie Hacker
---

# AI App Security: Admin Panels and the Access Nobody Audits

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "AI App Security: Admin Panels and the Access Nobody Audits",
  "description": "The admin panel is the one part of a product that can reach every customer's data, and the one part nobody tests. How admin access leaks, why impersonation needs rules, and what a support tool should never be able to do.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-08-15",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/ai-app-security-admin-panels-and-the-access-nobody-audits" }
}
</script>

Every product acquires one eventually. A page where you can look up a customer, fix a stuck record, resend an invoice, or see why somebody's export failed. It starts as a single screen built in twenty minutes because a customer was waiting, and it grows every time support gets hard.

It is also, by design, the one part of your product that ignores every rule you wrote. Tenant isolation does not apply to it. Row level security is bypassed by whatever key it uses. The careful access model that keeps 400 companies apart exists everywhere except here.

And nobody tests it, because it is internal, because it is "just for us", and because testing your own tools feels like distrust of yourself.

## Why This Is the Highest-Value Target in Your Product

Consider what an admin panel typically offers: read any customer's records, change them, reset a password, view a payment, issue a refund, and frequently log in as a user to see what they see.

An attacker reaching that page does not need to find a vulnerability in your application. They have been handed the tool that was built to bypass your application's protections. One compromised admin account is worth more than every ordinary account combined, which is exactly why it deserves defences no ordinary account needs.

## The Five Ways Admin Access Gets Reached

**Security by obscurity.** The page is at a path nobody would guess, and the check is that you have to know the path. Paths are discovered — in browser history, in analytics, in a shared screenshot, by an automated scan trying common names.

**A flag the user controls.** An `is_admin` column on a profile table that users can update. This appears in AI-built applications with genuine regularity, because storing the flag next to the profile is the obvious design and locking that column is a separate decision nobody makes.

**A check that only exists in the interface.** The menu item is hidden for non-admins and the underlying endpoints accept any authenticated request. Hiding a button is not access control; it is decoration over an open door.

**A shared account.** One set of credentials used by you, a contractor and a support colleague. Nothing in your records can attribute any action, and offboarding is impossible.

**A forgotten account.** The developer who helped last year, the test admin created during setup, the founder who left. Each still holds complete access to every customer.

## Impersonation Deserves Its Own Rules

Logging in as a customer is the most useful support feature and the most dangerous one. Three rules make it acceptable.

**It must be recorded.** Every impersonation session: who, which customer, when, for how long. This is the record that answers a customer asking whether anyone from your company looked at their data, and "we don't log that" is an answer with commercial consequences.

**It should be visible.** A banner while active, so nobody forgets which account they are in — and, ideally, a notice to the customer that support accessed their account. Dutch business customers respond well to that transparency and badly to discovering it later.

**It should be limited.** Read-only by default, with a deliberate step to take actions. Most support questions are answered by looking.

There is a fourth consideration worth stating plainly: some data should not be impersonable at all. Health information, private messages, documents a customer marked confidential. A support tool that shows summaries and metadata rather than contents answers most questions without your team reading things they should not.

## What an Admin Tool Should Never Do

**Export everything.** A button producing a file with every customer's data is one click between a bad afternoon and a reportable breach. If bulk export must exist, restrict it, log it, and require a second person's approval.

**Delete without a trace.** Administrative deletion should be reversible and recorded.

**Change money silently.** Refunds, credits and plan changes need an actor, a reason and an audit entry.

**Reveal secrets.** A panel displaying API keys, tokens or password hashes turns one compromise into many.

**Run arbitrary queries.** The "run SQL" box added for convenience is a complete bypass of every control in the product, and it has no business being reachable from a web page.

## The Defences That Actually Fit a Small Team

You do not need an identity platform. Five things are enough.

**Two-factor authentication on every administrative account, without exception.** This is the single highest-value control available, and it is the one that makes a stolen password survivable.

**Separate accounts for separate people,** even in a company of two. Attribution requires it.

**Server-side authorisation on every administrative endpoint,** checked against a role stored where users cannot write it. Not a hidden menu — a check in the code that runs.

**Everything logged,** with the log kept where an administrator cannot edit it.

**A quarterly review of who has access,** which takes ten minutes and consistently finds someone who should not.

Two optional additions are worth the effort once you have business customers: restricting administrative access to known networks, and requiring a fresh authentication step before the most sensitive actions.

## Build Support Features Instead of Admin Access

The strategic move, and the one that reduces risk permanently.

Most administrative access exists to answer recurring questions: why did this email not arrive, why is this record stuck, what happened to this payment. Each of those can be a purpose-built view showing exactly what is needed — a delivery status, a job history, a payment timeline — rather than unrestricted access to everything.

Purpose-built views are safer, faster to use, and can be given to a support colleague without handing over the product. Over time the general-purpose panel shrinks to the handful of genuinely exceptional operations, which is the right size for something this dangerous.

## Testing Your Own Panel

Half an hour, and most teams find something.

Log in as an ordinary user and request an administrative endpoint directly, without going through the interface. Try to set your own role by updating your profile. Open the administrative path while logged out. Ask whether every current administrator still needs access. Check whether administrative actions appear in your audit trail, with an actor. And confirm two-factor authentication is actually enforced rather than merely available.

Anything that succeeds is a finding, and it is a finding somebody else could have made instead.

## The Contractor Who Needs Admin Access Tomorrow

The situation that breaks every policy: a developer is joining for three weeks to fix something, and they need to see real data to do it.

**Ask whether they actually do.** A large proportion of debugging needs the shape of the data rather than the contents. A development environment with anonymised data — real structure, real volume, fictional people — resolves most of these requests and is the single best investment you can make before hiring anyone.

**If real access is genuinely required, make it narrow and temporary.** Their own account, never a shared one. The smallest role that covers the work. A date when it ends, decided before it starts. And tell them it is logged, which is not distrust but the same arrangement any professional expects.

**Never hand over your own credentials.** It is the fastest option and it destroys attribution: every action they take appears as you, including in the records you would rely on if something went wrong. It also means you cannot revoke their access without changing your own.

**Separate the platform from the data.** A contractor frequently needs to change code, not read customer records. Access to the repository, the development environment and deployment can be granted without access to production data, and keeping those separate is the difference between a normal engagement and an anxious one.

**Close it the same day it ends.** Remove the account, rotate anything they could have seen, and note it. The natural moment to do this is when the invoice arrives, which is a useful trigger precisely because it always happens.

This is also what your business customers are asking about when they ask who can access their data. "Two permanent people, plus named contractors with time-limited accounts, all logged" is a professional answer. "Sometimes a freelancer uses my login" is the answer that ends a procurement conversation, and it is the honest answer for a surprising number of small products.

## Locking Down Privileged Access

For an existing product this is a few days of focused work: administrative endpoints moved behind server-side authorisation checked against a role users cannot modify, two-factor authentication enforced, shared accounts split and forgotten ones removed, impersonation made recorded, visible and read-only by default, destructive and bulk operations restricted and logged, any arbitrary-query facility removed, and purpose-built support views built to replace general access.

LaunchStudio does this as part of production readiness, and documents who can do what so you can answer a customer's question about internal access without hesitating. The engineers are Manifera's: eleven years of production systems for clients including Vodafone, TNO and CFLW, from Amsterdam and Ho Chi Minh City.

[Tell us what your admin page can do](https://launchstudio.eu/en/#contact) and you will get a specific assessment, usually within one business day, or see the [packages](https://launchstudio.eu/en/#packages).

## Real example

### An Admin Path in the Browser History of a Shared Laptop

Stijn Groenewoud built Aanmelder with Lovable: event registration used by fourteen organisations around Zwolle — conference organisers, two municipalities and several trade associations. Around 60,000 registrations a year, including dietary requirements, accessibility needs and, for some events, employer details.

The administrative page sat at a path he considered unguessable. Access was granted by an `is_admin` column on the profile table. There was no two-factor authentication, one set of credentials was shared between Stijn and a part-time colleague, and the panel included a button exporting all registrations across all organisations as a spreadsheet, added once for a client who had asked for their own data.

The problem surfaced without malice. A freelance event coordinator borrowed a laptop the part-time colleague had used, typed the first letters of the site into the address bar, and the administrative path appeared from browser history. The session was still valid. She was looking at fourteen organisations' registration lists, recognised competitors' events, and called Stijn immediately.

Eight business days of work: administrative authorisation moved to a role in a table users cannot write, with every administrative endpoint checked server-side rather than by hiding menu items; two-factor authentication enforced on all administrative accounts; the shared login split into three individual accounts and two dormant accounts removed, one belonging to a developer who had finished in the previous year; session lifetime for administrative accounts shortened with re-authentication required for sensitive actions; the global export removed and replaced with a per-organisation export that is logged and attributable; impersonation rebuilt as read-only with a visible banner, a full record of every session and a monthly summary available to each organisation; an audit trail added for every administrative action; and four purpose-built support views created — registration status, email delivery, payment timeline and export history — covering what the panel had actually been used for.

**Result:** the coordinator's report was handled as a near-miss with a written note to the fourteen organisations, all of whom stayed. Two municipalities subsequently asked for the internal-access description during a contract renewal, which Stijn now keeps as a standing document.

> *"My admin page was protected by the fact that nobody knew the address. Then somebody's browser remembered it."*
> — **Stijn Groenewoud, Founder, Aanmelder (Zwolle)**

**Cost & Timeline:** €3,900 (server-side authorisation, two-factor enforcement, account separation, impersonation rebuild with logging, export restriction, purpose-built support views) — completed in 8 business days.

## Frequently Asked Questions

### Is a secret admin URL enough protection?

No. Paths are discovered through browser history, analytics, screenshots and automated scanning. Authorisation must be a server-side check on every administrative endpoint, against a role stored where users cannot modify it.

### Why is an is_admin column on the profile table dangerous?

Because users can usually update their own profile, which means they can promote themselves. Roles belong in a table the user's account cannot write to, and the check must run in code rather than by hiding a menu item.

### What rules should apply to logging in as a customer?

Record every session with actor, customer, time and duration; show a visible banner while active and consider notifying the customer; and make it read-only by default, since most support questions are answered by looking rather than acting.

### What should an admin tool never be able to do?

Export all customers at once without restriction and logging, delete without a trace, change money silently, display secrets, or run arbitrary queries. The last one bypasses every control in the product.

### What is the highest-value control for a small team?

Two-factor authentication on every administrative account, with separate accounts per person. It makes a stolen password survivable and makes every action attributable.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Is a secret admin URL enough protection?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No — paths surface via history, analytics, screenshots and scanners. Authorisation must be a server-side check against a role users cannot modify."
      }
    },
    {
      "@type": "Question",
      "name": "Why is an is_admin column on the profile table dangerous?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Users can usually update their own profile and therefore promote themselves. Roles belong in a table the user's account cannot write."
      }
    },
    {
      "@type": "Question",
      "name": "What rules should apply to logging in as a customer?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Record every session, show a visible banner and consider notifying the customer, and default to read-only since most support questions only require looking."
      }
    },
    {
      "@type": "Question",
      "name": "What should an admin tool never be able to do?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Unrestricted bulk export, untraceable deletion, silent money changes, display of secrets, or arbitrary query execution."
      }
    },
    {
      "@type": "Question",
      "name": "What is the highest-value control for a small team?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Two-factor authentication on every administrative account, with a separate account per person so actions are attributable."
      }
    }
  ]
}
</script>
