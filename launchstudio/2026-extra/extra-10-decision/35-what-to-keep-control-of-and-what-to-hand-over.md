---
Title: "What You Should Keep Control Of — and What to Hand Over"
Keywords: founder owned accounts, domain ownership founder, credentials control startup, who owns the Stripe account, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: AI-Native Founder (Non-Technical)
---

# What You Should Keep Control Of — and What to Hand Over

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "What You Should Keep Control Of — and What to Hand Over",
  "description": "A category-by-category answer to which accounts, domains and credentials should always stay registered in the founder's own name, and which day-to-day technical access is genuinely fine to delegate during a build. Helps founders avoid the ownership mistakes that are hard to reverse later.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-02-10",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/what-to-keep-control-of-and-what-to-hand-over" }
}
</script>

"Whose name is the domain actually registered under?"

"...I'm not sure. My old developer set it up, I think? I've never logged into it."

That exchange, or something close to it, happens on a noticeable share of first calls with founders who built their prototype with help from a freelancer or a technical friend before coming to LaunchStudio. It's rarely malicious — the person who registered the domain two years ago almost certainly meant well and has probably forgotten about it too. But "I think" is not an acceptable answer to "who owns your company's address on the internet," and the fact that so many founders can only offer it points to a decision nobody walked them through: which things must always sit in your own name, and which are fine to let someone else hold the keys to while they work.

## The Rule That Sorts Everything Else

Before the category list, one test does most of the sorting: if this account, domain, or credential disappeared or became inaccessible tomorrow, could you rebuild your business without it, or does its loss threaten the business's existence? Anything in the second group stays in your name, no exceptions, regardless of how technical it sounds or how much easier it would be to let someone else manage it.

This test cuts against a common founder instinct, which is to sort by "how technical does this feel." Domain registration sounds technical, so founders often let it live wherever it was first set up. But domain ownership is closer to owning your company's legal address than it is to a coding decision — it's identity and continuity, not implementation.

## Always in Your Own Name, No Exceptions

**Your domain registration.** Registered through an account you personally control — your own login, your own payment method, your own recovery email. Not a developer's account "for now," not an agency's portfolio of client domains. If you ever need to change providers, add a subdomain, or move hosting, you need to be able to do it without asking anyone's permission or waiting for someone to remember a password. Losing access to your domain registrar is one of the few failures on this entire list with no clean recovery path — you can lose your business's address permanently.

**Your business email and Google Workspace or Microsoft 365 tenant.** The account that owns your company's email domain, calendar, and shared drives should be under your control, with you as the billing owner and primary admin, even if a co-founder or assistant manages day-to-day settings. This is also usually the account tied to password resets for everything else, which makes it a single point of failure worth protecting deliberately.

**Your payment processor account (Stripe, Mollie, PayPal).** The account that actually holds your merchant status, your payout bank details, and your transaction history must be yours — created with your business details, your bank account, your login. An engineer configures products, webhooks, and checkout flows inside it; they should never be the account holder. If a dispute or a compliance question ever arises, you are the legally responsible party regardless of who set up the integration, so you should be the one who can actually see and act on the account.

**Your code repository's organisation account (GitHub, GitLab).** The organisation — not necessarily every individual repository setting — should belong to you, with your engineering partner added as a collaborator with appropriate permissions. This is the single clearest expression of "the founder always owns the code," a principle LaunchStudio treats as non-negotiable: code lives in your repository, on your account, from day one, not transferred to you as a courtesy at the end.

**Your hosting and cloud provider account (Vercel, AWS, Netlify, DigitalOcean).** Same logic as the domain: the account that holds your production infrastructure, your billing, and your ability to redeploy or roll back should be one you can log into directly. An engineer needs access to work inside it; they don't need to be the one whose card is on file or whose login is the only path in.

**Your business registration and legal accounts.** Chamber of Commerce records, your accounting software, your business bank account — obviously yours, but worth listing here because founders sometimes let a co-founder or early hire become the sole admin on tools like this for convenience, which creates the same single-point-of-failure risk as any technical account.

## Genuinely Fine to Delegate During a Build

**Day-to-day repository access and branch permissions.** Once the organisation is yours, who can push code, review pull requests, and merge changes is an operational detail your engineering partner should manage without needing your approval for each change.

**Staging environment configuration.** Environment variables, test data, and settings on the non-production version of your app are working tools, not assets — let your engineering partner set these up and change them freely.

**Which specific engineer or team member has access to what.** Whether your partner uses one engineer or three, and how they divide access internally, is their operational business, not yours to specify, as long as the accounts they're accessing remain under your ownership.

**Technical monitoring and error-tracking tool configuration.** Tools like Sentry or a hosting provider's built-in logging are usually fine to let your engineering partner set up and administer during the build, provided you retain visibility (a viewer login, or the ability to be added as an owner later if you outgrow the relationship).

**Third-party API accounts used purely for development or testing.** A sandbox account for a mapping API used only during the build, or a test-mode payment integration, doesn't need to be in your name from day one — though anything that becomes part of production should transition to your ownership before launch, not after.

## The Grey Area: Email-Sending and Transactional Services

Services like SendGrid, Postmark, or Resend sit in between. The account should ultimately be yours, because it sends mail as your business and affects your domain's sender reputation — but it's common and reasonable for an engineering partner to set it up under your business details during the build and hand over admin access at launch, rather than requiring you to create the account yourself before any work starts. The test: by the time you're live and paying customers are receiving mail, you should be the verified account owner, even if someone else configured the templates and sending logic.

## How to Give Access Without Giving Away Ownership

Keeping ownership doesn't mean doing the technical setup yourself or becoming a bottleneck on every configuration change — it means using the access controls these platforms already provide to separate "who owns this" from "who can work in this," which almost every serious provider supports.

On GitHub and GitLab, this is organisation ownership versus collaborator or team-member roles — you hold the organisation, your engineer gets exactly the repository permissions their work requires. On Google Workspace and Microsoft 365, it's the difference between the primary billing-owner role and an admin or delegated-access role — you can grant broad administrative capability to someone else without ever losing the ability to reclaim it, because the platform tracks a distinct owner separately from admins. On Stripe, it's team member roles with scoped permissions (view-only, developer, administrator) layered under an account that remains registered to your business. On domain registrars, most now support adding a secondary contact or a "trusted account" without transferring the registration itself.

The habit worth building is checking, for any account someone else is setting up on your behalf, whether it was created under your ownership from the start or under theirs with a plan to transfer later. The first is nearly always cleaner. A "we'll transfer it to you at the end" plan depends on someone remembering to do it, correctly, at a moment when the engagement is wrapping up and everyone's attention is already elsewhere — which is precisely when handover steps get skipped.

## Recovery Methods Matter as Much as the Login Itself

Ownership isn't just "whose password is it" — it's also "what happens when the password is lost." Check the recovery email and phone number on each of the accounts above, not just who's logged in as the primary user today. It's common to find a critical account's recovery email pointing at a personal address a co-founder no longer checks, or a phone number tied to a SIM card that's been cancelled. An account you technically own but can't recover into is functionally not yours the moment you need it most — during a lockout, a suspicious-login flag, or a lost device.

Set recovery details to something durable: a role-based email address you control (like owner@yourcompany.com) rather than a personal one, and a phone number on a line the business actually controls if the platform requires SMS-based recovery. This single check — walking through five accounts and confirming the recovery path actually reaches you — is worth doing in the same sitting as the ownership audit below, because it's the same failure mode wearing a different hat.

## Why This Matters More at the Moment You're Not Thinking About It

The risk with all of these isn't really about the build itself — it's about what happens later, when the relationship with whoever set something up changes. A freelancer who registered your domain moves on to other clients and stops responding to emails. A co-founder who was the sole Stripe account holder has a falling-out and leaves. An early technical hire who set up your Google Workspace tenant as the primary admin departs without transferring ownership. None of these are hypothetical — they are the specific, recurring stories behind founders who arrive at a scoping call unable to answer "who owns your domain."

Fixing this after the fact ranges from mildly annoying (a support ticket and an identity verification process) to genuinely difficult (a former collaborator who won't respond, a domain registrar with no clear recovery path for an account you were never the primary contact on). Fixing it before it happens costs the time it takes to check five logins and change five recovery emails — an afternoon, done once, ideally before any engagement starts rather than after something goes wrong.

## A Five-Minute Audit You Can Run Today

Open each of these and check who the account owner and billing contact actually is: your domain registrar, your email/Workspace tenant, your payment processor, your code hosting organisation, your cloud hosting provider. For each one where the answer isn't unambiguously "me," that's the item to fix this week — not during your next engineering engagement, when it will compete for attention with everything else.

This is exactly the kind of housekeeping LaunchStudio walks new clients through before work begins, because Manifera's 11+ years of onboarding founders across very different starting points has shown that ownership confusion, not technical debt, causes the messiest post-engagement disputes. Getting it clean before you start protects both sides. [Describe your project](https://launchstudio.eu/en/#contact) and mention what you're unsure about ownership-wise — it's a normal, expected part of a first conversation, not an awkward one.

## Real example

### The Domain Nobody Could Log Into

Ruben Verhoeven's team had been running Toolwissel, a tool-sharing platform for small construction firms, on a domain registered two years earlier by a freelancer who'd since gone quiet. Nobody on the current team had the registrar login, the recovery email pointed to an address that no longer existed, and the domain's renewal was eleven days away when this surfaced during a pre-engagement ownership check.

Rather than starting the hardening engagement with the domain still exposed, LaunchStudio's engineer flagged it as priority zero — ahead of any code work — because a lapsed domain would have taken the entire product offline regardless of how well the backend was secured. Ruben spent two days working with the registrar's account-recovery process, eventually regaining access through a combination of old invoices and a notarised ownership statement, five days before the renewal deadline.

**Result:** the domain was re-registered under Toolwissel's own business account with Ruben as the verified owner, and the actual hardening engagement started on schedule once that was resolved — but Ruben has since said the domain scare was more stressful than anything in the technical work that followed.

> *"I'd been worried about security bugs the whole time. It turned out the thing that could have actually killed the business was a domain login nobody had, sitting there quietly for two years."*
> — **Ruben Verhoeven, Founder, Toolwissel**

**Cost & Timeline:** €2,600 (Launch Ready Package plus domain-ownership remediation) — live in 11 business days after the domain issue was resolved.

## Frequently Asked Questions

### What if my engineering partner insists on holding one of these accounts themselves "for efficiency"?

Push back specifically on the accounts in the "always yours" category — domain, payment processor, code organisation, hosting, business email. A reputable partner will explain why they need access to work inside these, not why they need to be the owner of them; those are different requests, and only the first one is reasonable.

### I already let a previous freelancer register my domain. How do I fix this safely?

Contact the registrar's support directly and ask about their business transfer or ownership-recovery process — most have one, though it can take days and may require proof of your business's connection to the domain. Do this before any renewal deadline, not after, since a lapsed domain can be re-registered by someone else the moment it expires.

### Does it matter if my co-founder, not an outside engineer, holds some of these accounts?

Yes, in the sense that a single point of failure is a single point of failure regardless of whether it's a co-founder or a contractor — the difference is trust today, not risk tomorrow. Add yourself as a secondary owner or admin on anything currently held by only one person, co-founder included.

### Should I list all of this in the handover document described elsewhere in this series?

Yes — the ownership inventory described here belongs as its own short section in that document, listing each account, who currently holds it, and whether that needs to change. It's one of the fastest sections to write and one of the most valuable to have on record.

### What's the actual risk if I never fix this and everything just happens to keep working?

The risk isn't that anything breaks under normal operation — it's that you have no leverage or recovery path the moment a relationship changes, a person becomes unreachable, or an account needs urgent action (a domain renewal, a payment dispute, a security incident) and you can't act because you were never the one with access.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "What if my engineering partner insists on holding one of these accounts themselves \"for efficiency\"?", "acceptedAnswer": { "@type": "Answer", "text": "Push back specifically on domain, payment processor, code organisation, and hosting accounts. A reputable partner will explain why they need access to work inside these, not why they need to own them." } },
    { "@type": "Question", "name": "I already let a previous freelancer register my domain. How do I fix this safely?", "acceptedAnswer": { "@type": "Answer", "text": "Contact the registrar's support about their business transfer or ownership-recovery process, and do it before any renewal deadline, since a lapsed domain can be re-registered by someone else the moment it expires." } },
    { "@type": "Question", "name": "Does it matter if my co-founder, not an outside engineer, holds some of these accounts?", "acceptedAnswer": { "@type": "Answer", "text": "Yes. A single point of failure is a single point of failure regardless of who holds it — the difference is trust today, not risk tomorrow. Add yourself as a secondary owner on anything held by only one person." } },
    { "@type": "Question", "name": "Should I list all of this in the handover document described elsewhere in this series?", "acceptedAnswer": { "@type": "Answer", "text": "Yes. The ownership inventory belongs as its own short section listing each account, who currently holds it, and whether that needs to change. It's one of the fastest sections to write and most valuable to have on record." } },
    { "@type": "Question", "name": "What's the actual risk if I never fix this and everything just happens to keep working?", "acceptedAnswer": { "@type": "Answer", "text": "The risk isn't that anything breaks under normal operation. It's that you have no leverage or recovery path the moment a relationship changes or a person becomes unreachable and you can't act because you were never the one with access." } }
  ]
}
</script>
