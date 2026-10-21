---
Title: "AI App Security: SSO When an Enterprise Customer Asks"
Keywords: ai app security, single sign-on, SAML, Microsoft Entra ID, SCIM, enterprise SaaS, Supabase SSO, LaunchStudio, Manifera
Buyer Stage: Decision
Target Persona: SaaS Scale-Up
---

# AI App Security: SSO When an Enterprise Customer Asks

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "AI App Security: SSO When an Enterprise Customer Asks",
  "description": "The first enterprise prospect asks for single sign-on, and what they mean is more than a login button. SAML or OIDC, Entra ID in practice, domain verification, account linking, enforcement, deprovisioning with SCIM, and the security mistakes that turn SSO into a way in.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-03-09",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/ai-app-security-sso-when-an-enterprise-customer-asks" }
}
</script>

The first larger organisation that wants to buy your product will send a security questionnaire, and somewhere on it is a question that small products have never had to answer: "Does the application support single sign-on with our identity provider?"

For a Dutch company of a few hundred people or more, the identity provider is almost always Microsoft Entra ID — what used to be called Azure Active Directory — and occasionally Google Workspace or Okta. Their IT department wants employees to sign in to your product with their company account, wants access to end when someone leaves, and does not want another set of passwords to manage.

Founders tend to hear "add a Microsoft login button". The request is larger than that, and implemented carelessly, SSO becomes the easiest way into someone else's account. This article covers what the customer actually wants, the choice of protocol and provider, the implementation details that matter, and the security mistakes to avoid.

## What the Customer Is Actually Asking For

"SSO" on a questionnaire usually bundles five separate requirements. Ask which ones apply before quoting, because the effort differs considerably.

**Sign-in through their identity provider.** Employees click "Sign in with your company account", authenticate at Microsoft, and arrive in your product. This is the core.

**Enforced SSO.** Employees of that company cannot sign in any other way — no password, no magic link. Without enforcement, SSO is a convenience; with it, the company's own controls apply to every login.

**Their multi-factor authentication and conditional access.** Their policies — MFA, compliant devices, blocked countries — apply because authentication happens at their provider. This comes for free with enforced SSO and is often the real reason they ask.

**Automatic provisioning and deprovisioning.** New employees get access without an invitation; leavers lose access the day they leave. This is SCIM, and it is a separate piece of work.

**Role mapping.** Membership of a group in their directory determines the role in your product — "Finance" becomes Accountant, "Procurement leads" becomes Administrator.

A first enterprise customer typically needs the first three and asks for the fourth. The fifth can usually wait.

## SAML or OIDC

Two protocols do this job.

**SAML 2.0** is older, XML-based and universal in enterprise. Every identity provider supports it, and procurement checklists name it explicitly. Configuration is an exchange of metadata — URLs, an entity ID and a signing certificate — between you and the customer's IT department.

**OpenID Connect (OIDC)** is newer, JSON-based and simpler to implement. Entra ID, Google and Okta all support it well. It is what "Sign in with Microsoft" buttons usually use.

For a B2B product the practical answer is: support SAML, because that is what enterprise IT departments expect to configure, and add OIDC where it simplifies things for particular providers. A product that only offers a generic "Sign in with Microsoft" button — multi-tenant OIDC for any Microsoft account — has not delivered what the questionnaire asked, because it neither binds the login to the customer's tenant nor allows enforcement.

## Build It, Use Supabase, or Buy It

Writing a SAML implementation yourself is the one option to rule out. XML signature validation is notoriously easy to get wrong, and several of the most serious authentication vulnerabilities of the last decade were exactly that. Use a maintained implementation.

That leaves two realistic paths for a Lovable or Supabase product.

**Supabase Auth's SAML SSO**, available on paid plans. You register each customer's identity provider with its metadata and the email domains it is responsible for, and users from those domains sign in through it. It keeps authentication in one place and costs nothing extra beyond the plan. It handles sign-in; enforcement, role mapping and SCIM are yours to build.

**A dedicated identity layer** — WorkOS, Auth0, Clerk or similar — which provides an admin portal where the customer's IT department configures SSO themselves, plus SCIM directory sync, for a per-connection fee. You trade money for the parts that consume support time: configuration, certificate rotation, directory sync and provider quirks.

The decision usually follows the number of enterprise customers you expect. For one or two, Supabase SAML plus a small amount of your own code is proportionate. If enterprise is the direction of the business, a dedicated layer pays for itself in support hours, mainly because the customer's IT department can configure and troubleshoot it without you.

## Domain Verification Comes First

This is the security property that matters most, and the one most often skipped.

An SSO connection asserts identities for email addresses. If a connection configured by Customer A is allowed to assert addresses at `@customer-b.nl`, then anyone who controls Customer A's identity provider can sign in as anyone at Customer B. In a self-service setup — where customers configure their own SSO during a trial — that means any trial account can take over any user whose email domain it claims.

The rule: a connection may only assert identities for domains the organisation has proven it owns. The standard proof is a DNS TXT record:

```
_launchstudio-verify.customer.nl.  TXT  "ls-verify=8f3c1e9a2b7d4f60"
```

Generate the token, ask the customer to publish it, check it before activating the connection, and re-check it periodically. Store the verified domains on the organisation, and reject any assertion from a connection for an email outside them.

```ts
const domain = assertion.email.split('@')[1].toLowerCase();
if (!connection.verifiedDomains.includes(domain)) {
  throw new AuthError('sso_domain_not_verified');
}
```

Never verify domains for free email providers — gmail.com, outlook.com, hotmail.com — however the request is phrased.

## Linking Existing Accounts

Most enterprise customers already have a few users in your product with passwords, created during the trial. When SSO is switched on, those people sign in through their identity provider and should arrive in their existing account, not a new empty one.

Linking by email address is the obvious approach and it is safe only under one condition: the email domain is verified for that connection. Then the identity provider is authoritative for that address, and linking is correct.

Without verification, linking by email is an account takeover mechanism. Anyone who can make any identity provider assert `ceo@customer.nl` gets the existing account of that address, with its data and its role. AI-generated SSO flows link by email unconditionally with some regularity, because it makes the demonstration work.

After linking, decide what happens to the password. For an enforced domain, disable password sign-in for those accounts so the old password cannot be used to bypass the company's controls.

## Just-in-Time Provisioning and Role Mapping

When an employee signs in through SSO for the first time and has no account, the product can create one on the spot and add them to the organisation — just-in-time provisioning. It removes the need to invite people one by one, which is what the customer's IT department wants.

Three rules keep it safe:

- JIT applies only to verified domains of the organisation that owns the connection.
- New users get the lowest role by default — Member or Read-only — never Administrator.
- Role elevation comes from explicit group mapping or from an administrator in your product, not from anything the user controls.

Role mapping uses the group claims the identity provider sends. Map them to roles in your product, as defined in the roles and permissions article in this series:

```ts
const groupToRole = { 'LS-Admins': 'administrator', 'LS-Finance': 'accountant' };
const role = assertion.groups.map(g => groupToRole[g]).find(Boolean) ?? 'member';
```

Re-evaluate mapped roles at every sign-in, so that removing someone from a group in Entra ID reduces their role in your product the next time they arrive.

## Enforcement and the Break-Glass Account

Enforced SSO means the sign-in page, given an email at an enforced domain, sends the user to their identity provider and offers nothing else. Password sign-in, magic links and password reset are all refused for that domain — including through the API, not only in the interface.

Enforcement creates one risk: if the customer's SSO configuration breaks — an expired certificate, a changed tenant, a misconfigured policy — nobody at that company can sign in. Keep one break-glass account: a named owner at the customer, exempt from enforcement, with strong MFA, whose use is logged and alerted. Agree in writing who holds it.

## Deprovisioning: The Part SSO Alone Does Not Solve

A common misunderstanding, shared by customers and founders alike: when an employee leaves and their Entra account is disabled, they lose access to your product.

They lose the ability to sign in again. They do not lose a session that is already open. If your sessions last thirty days, a leaver who was signed in on their last day keeps access for up to a month — on a laptop they may still have.

Two measures close the gap.

**Shorter sessions for SSO users**, with re-authentication against the identity provider every eight to twelve hours. Since sign-in is a single click for someone still employed, the cost is negligible; the session article in this series covers refresh and revocation.

**SCIM provisioning.** The identity provider calls your SCIM endpoint when a user is created, changed or deactivated. On deactivation you remove the membership and revoke sessions immediately, as the team invitations article describes. SCIM is a defined protocol with a handful of endpoints; implementing it yourself is a few days, and a dedicated identity layer provides it as directory sync.

If you cannot offer SCIM yet, say so honestly on the questionnaire and describe the compensating control: short sessions, an administrator in the customer's organisation who can remove users instantly, and an audit log of sign-ins.

## Security Mistakes That Turn SSO Into a Way In

Beyond domain verification and account linking, five mistakes recur.

**Not validating the assertion properly.** Signature, audience, recipient, expiry and the expected issuer must all be checked. A maintained library does this; a hand-written parser frequently does not.

**Accepting IdP-initiated sign-in without care.** Logins that start at the identity provider rather than at your site are convenient and lack the request binding that protects against forged responses. Support them only if a customer requires it, with short assertion lifetimes and replay protection.

**Trusting the email claim from a multi-tenant OIDC app.** "Sign in with Microsoft" for any tenant returns email claims that are not always verified. Bind each connection to the customer's specific tenant ID.

**Letting one organisation's connection affect another.** Each connection belongs to exactly one organisation; a user signing in through it lands in that organisation and nowhere else.

**Ignoring certificate expiry.** SAML signing certificates typically rotate yearly. When the customer's certificate expires and nobody updated the configuration, every user at that company is locked out on a Monday morning. Store the expiry date and alert sixty days before it.

## Sign-In Logs the Customer Will Ask For

Once SSO is live, the customer's security team becomes a regular reader of your product, and the first thing they ask for is evidence.

Record every SSO sign-in with the organisation, the connection, the user, the result and the reason for any failure — signature invalid, domain not verified, user not provisioned, certificate expired. Failed attempts matter more than successful ones: a burst of failures for one connection is either a misconfiguration you can fix before the customer calls, or something worse.

Expose the organisation's own sign-in history to its administrators, filterable by user and date. It answers "did this person still log in after they left" without a support ticket, and it is the kind of capability that moves a questionnaire answer from "on request" to "available in the product".

Two retention decisions belong in the data retention register described elsewhere in this series: how long sign-in logs are kept — twelve months is common for security purposes — and whether IP addresses are stored, since they are personal data under GDPR. Decide deliberately and write the reason down; the customer's privacy officer will ask.

Finally, make SSO failures visible to you. An alert when one connection produces more than a handful of failures in an hour catches the expired certificate, the tenant migration and the misconfigured policy before an entire company finds itself locked out on a Monday morning.

## The Commercial Side

SSO is often sold on a higher plan, and enterprise buyers expect that. Two points make the conversation easier.

Price it to reflect the real cost — per-connection fees if you use a provider, support time for configuration, and the enforcement and SCIM work — rather than as a penalty. Customers resent an "SSO tax" that looks arbitrary and accept a price that is clearly tied to an enterprise plan with other enterprise features.

And document it. A short page for the customer's IT department — which identity providers are supported, the metadata they need, how domain verification works, what enforcement does, how SCIM behaves — turns a week of email into an afternoon of configuration, and is the page their security reviewer reads.

## Testing Before the Customer Does

Test against a real identity provider, not a mock. A free Entra ID developer tenant or a test Okta organisation lets you run the actual flows: first sign-in with JIT, linking of an existing password account, group-based role changes, enforcement refusing passwords, a disabled user losing access, a certificate rollover.

Add two negative tests that matter most: a connection attempting to assert an email at an unverified domain must fail, and a user from one organisation's connection must never appear in another organisation.

## Setting This Up

For a Lovable or Supabase product preparing for its first enterprise customer, this is typically four to six days: the customer's actual requirements established — sign-in, enforcement, provisioning, role mapping — SAML through Supabase Auth or a dedicated identity layer rather than a hand-written implementation, DNS-based domain verification with assertions limited to verified domains, account linking only for verified domains with password sign-in disabled afterwards, just-in-time provisioning at the lowest role, group-to-role mapping re-evaluated at every sign-in, enforcement applied in the API as well as the interface, a logged break-glass account, shorter sessions for SSO users, SCIM deprovisioning or a documented compensating control, certificate expiry monitoring, a configuration guide for the customer's IT department, and tests against a real identity provider.

LaunchStudio implements this when a product's first enterprise deal depends on it. Behind it is Manifera — eleven years, 120+ engineers, 160+ projects, delivering for enterprise clients including Vodafone, TNO and CFLW.

[Send us the security questionnaire](https://launchstudio.eu/en/#contact) and we will tell you what the SSO line actually requires.

## Real example

### A Trial Account That Could Sign In as Anyone

Bart Engelen built Leveranciersportaal in Lovable: supplier qualification and certificate management for procurement teams, used by 14 companies.

A regional utility with around 2,000 employees wanted to buy it on one condition: sign-in through their Entra ID, enforced, with leavers losing access automatically. Bart enabled Supabase SAML, added a settings screen where an organisation's administrator could paste their identity provider's metadata, and linked incoming users to existing accounts by email address so trial users would keep their data.

A review before go-live found the problem. Any organisation — including a free trial — could register an identity provider, and nothing restricted which email domains that provider could assert. A trial account with its own test identity provider could assert the address of any user at any customer and be linked straight into their account. Separately, sessions lasted thirty days, so a utility employee disabled in Entra ID would keep access for up to a month.

Five business days: domain verification through DNS TXT records, with every connection restricted to the organisation's verified domains and free email providers refused; account linking limited to verified domains, with password sign-in disabled for linked accounts on enforced domains; the self-service metadata screen restricted to organisations on the enterprise plan after verification; just-in-time provisioning at the Member role, with three Entra groups mapped to roles and re-evaluated at each sign-in; enforcement applied in the API as well as the sign-in page, with one logged break-glass owner at the utility; SSO sessions shortened to ten hours; SCIM directory sync through a dedicated identity layer so deactivated employees lost access within minutes; certificate expiry stored with an alert at sixty days; and a configuration guide for the utility's IT department.

**Result:** no SSO connections had been registered by other organisations before the fix, confirmed from the logs. The utility signed a contract worth €38,000 a year, and their IT department configured the connection in an afternoon from the guide. Eleven months later the expiry alert fired; the certificate was rotated without a single locked-out user.

> *"I had built SSO that let any trial account sign in as anyone at any customer, as long as it typed their email address into its own test identity provider. The review found it a week before the utility went live."*
> — **Bart Engelen, Founder, Leveranciersportaal (Arnhem)**

**Cost & Timeline:** €5,600 (domain verification, verified-domain account linking, plan-restricted SSO configuration, JIT provisioning with group role mapping, API-level enforcement with break-glass account, shortened SSO sessions, SCIM deprovisioning, certificate expiry monitoring, IT configuration guide) — completed in 5 business days.

## Frequently Asked Questions

### What does an enterprise customer mean by SSO?

Usually sign-in through their identity provider, enforcement so no other login is possible, their MFA and conditional access applying, automatic deprovisioning through SCIM, and sometimes group-based roles. Ask which apply before quoting.

### Should I support SAML or OIDC?

SAML, because enterprise IT departments expect to configure it, with OIDC where it simplifies particular providers. A generic "Sign in with Microsoft" button for any tenant is not enterprise SSO.

### Why is domain verification so important?

Because an SSO connection asserts identities for email addresses. Without proof that the organisation owns the domain, any connection could assert any address and take over existing accounts.

### Does disabling someone in Entra ID remove their access?

It stops new sign-ins, not existing sessions. Use short sessions for SSO users and SCIM deprovisioning to revoke access immediately.

### Should I build SAML myself?

No. Use Supabase Auth's SAML support or a dedicated identity provider. Hand-written XML signature validation is a classic source of serious authentication vulnerabilities.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What does an enterprise customer mean when asking for SSO?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Sign-in through their identity provider, enforcement, their MFA and conditional access, SCIM deprovisioning, and sometimes group-based roles."
      }
    },
    {
      "@type": "Question",
      "name": "Should a B2B SaaS support SAML or OIDC?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "SAML first, because enterprise IT expects it, with OIDC where helpful — a generic multi-tenant Microsoft login button is not enterprise SSO."
      }
    },
    {
      "@type": "Question",
      "name": "Why does SSO need domain verification?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Without proof of domain ownership, any SSO connection could assert any email address and take over existing accounts."
      }
    },
    {
      "@type": "Question",
      "name": "Does disabling a user in Entra ID end their access?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "It blocks new sign-ins but not open sessions — use short SSO sessions and SCIM deprovisioning for immediate revocation."
      }
    },
    {
      "@type": "Question",
      "name": "Should I implement SAML myself?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No — use Supabase Auth SAML or a dedicated identity layer; hand-written signature validation is a classic source of vulnerabilities."
      }
    }
  ]
}
</script>
