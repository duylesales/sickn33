---
Title: "SAML SSO Implementation for B2B SaaS"
Keywords: saml sso implementation, supabase saml sso, enterprise sso saas, entra id okta sso integration, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: AI-Native Founder (Non-Technical)
---

# SAML SSO Implementation for B2B SaaS

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "SAML SSO Implementation for B2B SaaS",
  "description": "Enterprise customers expect their employees to sign in to SaaS products with their company accounts through single sign-on. This guide explains how to implement SAML SSO in an AI-built SaaS: how SAML works, options with Supabase Auth and identity platforms, domain verification, just-in-time provisioning, role mapping, SCIM deprovisioning, enforcing SSO, testing with Microsoft Entra ID, Okta and Google, and common pitfalls.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-06-09",
  "inLanguage": "en",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/saml-sso-implementation-for-b2b-saas" },
  "citation": [
    { "@type": "CreativeWork", "name": "Supabase: Enterprise SSO with SAML", "url": "https://supabase.com/docs/guides/auth/enterprise-sso/auth-sso-saml" },
    { "@type": "CreativeWork", "name": "OASIS SAML 2.0 specifications", "url": "https://docs.oasis-open.org/security/saml/v2.0/" },
    { "@type": "CreativeWork", "name": "RFC 7644: SCIM Protocol", "url": "https://www.rfc-editor.org/rfc/rfc7644" },
    { "@type": "CreativeWork", "name": "Microsoft Entra ID: SAML-based single sign-on", "url": "https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/what-is-single-sign-on" }
  ]
}
</script>

There is a moment in the life of many B2B SaaS products when a larger customer says: "We would love to roll this out to our 400 employees, but they must log in with their company accounts." In procurement language, that means single sign-on, usually through SAML or OpenID Connect, connected to the customer's identity provider, such as Microsoft Entra ID, Okta or Google Workspace.

For the customer, SSO is about control. Their IT department decides who has access, enforces their own password and MFA policies, and removes access instantly when someone leaves. For the founder, SSO is often the difference between a pilot with one team and a company-wide contract.

AI-built apps usually start with email and password or magic links. Adding SSO properly involves more than a login button. This guide explains how SAML SSO works and how to implement it in a way that enterprise IT teams will approve.

## Key Takeaways

- **SAML SSO lets customers' employees sign in with their company identity provider,** with authentication and MFA handled by the customer's IT.
- **Supabase Auth supports SAML SSO** on paid plans, and identity platforms such as WorkOS, Auth0 or Clerk offer SSO with customer self-service setup.
- **Map users to the right organisation and role,** using verified email domains and attributes from the identity provider.
- **Deprovisioning matters as much as login.** Use SCIM or periodic checks so people who leave the customer's company lose access.
- **Enforce SSO for organisations that require it,** so employees cannot bypass it with a password account.

## How SAML Works, Briefly

SAML 2.0 is an established standard for exchanging authentication information between two parties:

- **The identity provider (IdP):** the customer's system that knows who their employees are, such as Microsoft Entra ID, Okta or Google Workspace.
- **The service provider (SP):** your SaaS product.

A typical login:

1. The user goes to your app and enters their work email, or clicks "Sign in with SSO".
2. Your app recognises the email domain, determines which customer's IdP to use, and redirects the user there.
3. The user signs in at their company's IdP, with the company's password and MFA policies.
4. The IdP sends a signed SAML assertion back to your app, stating who the user is and possibly additional attributes, such as name, department or groups.
5. Your app verifies the signature, creates or updates the user and signs them in.

Configuration happens once per customer: your app provides its metadata, such as the assertion consumer service URL and entity ID, and the customer's IT provides theirs, such as the IdP's sign-in URL and signing certificate.

OpenID Connect is a newer alternative that some identity providers prefer. Many SSO solutions support both.

## Implementation Options

| Option | How it works | Strengths | Considerations |
| --- | --- | --- | --- |
| Supabase Auth SAML SSO | Supabase acts as the service provider; you register each customer's IdP | Integrated with existing Supabase users and RLS | Available on paid plans; configuration per customer through CLI or API |
| Dedicated SSO platform | A service handles SAML and OIDC connections and passes identities to your app | Customer self-service setup portals, many IdPs, SCIM support | Additional cost and processor, integration work |
| Authentication platform with SSO | An auth provider that includes enterprise SSO | One system for all login methods | Migration if you already use another auth system |
| Building it yourself | Implementing SAML with libraries | Full control | Complex and security-sensitive; rarely worth it |

For apps already on Supabase Auth, its built-in SAML support is usually the most straightforward route, keeping users, sessions and Row Level Security consistent. If you expect many enterprise customers who want to configure SSO themselves, a dedicated platform with a self-service portal can save significant support time.

## Domain Verification and Routing

Your app must decide which identity provider to use for a given user, usually by email domain. Before associating a domain with a customer's SSO configuration:

- **Verify domain ownership,** for example by asking the customer to add a DNS TXT record. Otherwise, anyone could claim a domain they do not own.
- **Handle multiple domains** per customer, such as `company.nl` and `company.com`.
- **Handle shared domains carefully.** Public email domains such as gmail.com must never be linked to an SSO configuration.

## User Provisioning and Role Mapping

When a user signs in through SSO for the first time, your app needs to:

1. **Link the user to the customer's organisation** based on the SSO connection.
2. **Create the user account** if it does not exist, known as just-in-time provisioning.
3. **Assign a role,** either a default role or one derived from IdP attributes, such as group memberships.
4. **Update attributes** on subsequent logins, such as name or department.

Role mapping from IdP groups is popular with IT teams: members of the group "Finance" get the finance role in your app. Keep the mapping configurable per customer and decide which side is authoritative. If the IdP says someone is no longer in the admin group, should they lose admin rights in your app at the next login? Usually yes.

Existing users complicate things. If an employee already had a password account before the company enabled SSO, link the accounts carefully, based on verified email addresses, and preserve their data.

## Deprovisioning: The Part IT Cares About Most

Login is only half of SSO. When an employee leaves the customer's company, IT disables them in the identity provider. With SAML alone, the person cannot log in again, but an existing session in your app may still be active, and their account remains.

Options:

- **SCIM provisioning:** the SCIM protocol lets identity providers create, update and deactivate users in your app automatically. Many enterprise customers expect it alongside SSO for larger rollouts.
- **Session limits:** shorter session lifetimes for SSO users, so access ends soon after the IdP disables someone.
- **Periodic reconciliation:** for customers without SCIM, admin tools to deactivate users and reports of inactive accounts.

Security questionnaires frequently ask how quickly access is removed when an employee leaves. Have a clear answer.

## Enforcing SSO

Once a customer enables SSO, they usually want it to be the only way in for their employees:

- **Block password and magic link logins** for users with email addresses on the customer's verified domains.
- **Disable password reset** for those users.
- **Allow a break-glass account** for the customer's admin, protected with strong MFA, in case the IdP has an outage, if the customer wants one.

Without enforcement, an employee who leaves could still sign in with a password account created before SSO was enabled.

## Sessions, Logout and Security

- **Validate SAML assertions strictly:** signatures, audience, recipient, timestamps and replay protection. Use well-maintained libraries or your auth provider's implementation; SAML vulnerabilities usually come from incomplete validation.
- **Keep the IdP's signing certificate current,** and handle certificate rotation, which IdPs perform periodically.
- **Consider session duration** per customer, as some require shorter sessions.
- **Log SSO events:** successful and failed logins, configuration changes and provisioning actions, for your audit log.

## Testing With Real Identity Providers

Set up test configurations with the IdPs your customers use most:

- **Microsoft Entra ID,** very common among Dutch and European enterprises and public sector organisations
- **Okta,** common in international companies
- **Google Workspace,** common in smaller companies and schools

Test first login, repeat login, role changes, users removed from the app in the IdP, certificate changes, IdP-initiated login, if you support it, and logout. Write a setup guide for customers' IT teams with screenshots for each IdP.

## The Onboarding Process for Each SSO Customer

Every new SSO customer goes through a similar process. Making it smooth reduces the time from signed contract to active users:

1. **Kick-off with the customer's IT contact.** Confirm which identity provider they use, which domains are involved, whether they need SCIM and how roles should map.
2. **Domain verification.** The customer adds a DNS record for each domain; your app confirms it.
3. **Exchange metadata.** Provide your service provider metadata or setup values; receive the identity provider's metadata or certificate and sign-in URL.
4. **Configure and test in a staging environment,** with one or two test users from the customer.
5. **Agree on role mapping** and test it with users from different groups.
6. **Enable SCIM,** if used, and verify that creating and disabling a test user works.
7. **Switch on enforcement** for the customer's domains on an agreed date, and inform their employees.
8. **Document the configuration** in your admin tools, including certificate expiry dates.

A one-page checklist and a short setup guide per identity provider let your team repeat this process in an hour or two rather than days of back-and-forth emails. With a dedicated SSO platform, much of this can be done by the customer's IT team through a self-service portal.

## Pricing SSO

SSO adds cost and support effort. Many B2B SaaS products include SSO in business or enterprise plans, which reflects its value to larger customers. Avoid making it so expensive that security-conscious smaller customers are pushed away; some buyers view SSO as a security baseline rather than a premium feature.

## How LaunchStudio Helps

LaunchStudio implements enterprise SSO in AI-built SaaS: choosing between Supabase Auth SAML and dedicated platforms, domain verification, organisation mapping, just-in-time provisioning, role mapping from IdP groups, SSO enforcement, session policies, SCIM provisioning where needed, audit logging and setup guides for customers' IT teams.

SSO implementations typically fall within **Launch & Grow** (€2,500-€7,500 plus €49 per month), which also includes managed hosting, monitoring and priority support. Use the [price calculator](https://launchstudio.eu/en/#calculator) for an estimate. For the commercial context, see our article on [SSO requests from enterprise customers](https://launchstudio.eu/en/blog/ai-app-security-sso-when-an-enterprise-customer-asks).

LaunchStudio is backed by Manifera, a software development company with 11+ years of experience, 160+ delivered projects and 120+ engineers, with experience integrating identity systems for enterprise clients such as Vodafone. CEO Herre Roelevink's cybersecurity background shapes how we approach identity and access. Founders meet the team at Herengracht 420 in Amsterdam; engineering happens at the development centre on Pho Quang Street in Ho Chi Minh City, with a hub on Tras Street in Singapore.

## Real example

### An AI-Native Founder in Action: The Onboarding App a Hospital Group Wanted for 3,000 Staff

Tessa Groen built Inwerkplan with Lovable and Supabase: an onboarding tool where new employees follow personalised checklists, complete training modules and meet their buddies. After successful pilots with smaller companies, a hospital group in Zuid-Holland wanted it for all new staff, around 3,000 employees across several locations, on one condition: login through Microsoft Entra ID, with automatic removal of leavers.

Inwerkplan only supported magic links. Tessa's first attempt, a Microsoft social login button, did not meet the requirement: it allowed any Microsoft account, did not map users to the hospital's organisation, ignored the hospital's groups and did nothing when people left. Some hospital employees had also already created accounts with magic links during the pilot.

LaunchStudio implemented SAML SSO through Supabase Auth with the hospital's Entra ID, after verifying the hospital's two email domains through DNS records. First-time logins provisioned users into the hospital's organisation, with roles mapped from Entra ID groups for HR staff, managers and new employees. Existing pilot accounts were linked by verified email, preserving progress. Magic link and password logins were blocked for the hospital's domains, sessions were limited to working-day durations, and SCIM provisioning through a dedicated service deactivated users automatically when they were disabled in Entra ID. SSO events and provisioning actions were written to an audit log, and the hospital's IT team received a setup guide with screenshots.

**Result:** The hospital group's IT approved the integration after one test session, and Inwerkplan rolled out across all locations. In the first year, around 1,100 new employees onboarded through it, and leavers lost access within minutes of being disabled in Entra ID. Two other healthcare organisations signed after learning about the Entra ID integration.

> *"I thought SSO meant a 'Sign in with Microsoft' button. For the hospital, it meant their IT department staying in control of every account, from the first day to the last."*
> - **Tessa Groen, Founder, Inwerkplan (Delft)**

**Cost & Timeline:** €6,500 (Launch & Grow package: SAML SSO with Entra ID, domain verification, provisioning and role mapping, SSO enforcement, SCIM deprovisioning, audit logging and IT guide) - completed in 16 business days.

## Frequently Asked Questions

### Is "Sign in with Microsoft" the same as enterprise SSO?

Not quite. A social login button lets any Microsoft account sign in, without linking users to their organisation, applying the company's policies or handling leavers. Enterprise SSO connects to a specific customer's identity provider, maps users to their organisation and roles, and is controlled by the customer's IT team.

### Does Supabase support SAML SSO?

Yes, Supabase Auth supports SAML 2.0 single sign-on on paid plans. You register each customer's identity provider and map their domains, and users signing in through SSO become regular Supabase users, so your existing Row Level Security policies continue to work.

### What is SCIM and do I need it?

SCIM is a standard that lets identity providers create, update and deactivate users in your app automatically. Larger enterprise customers often expect it so that leavers lose access immediately. For smaller SSO customers, admin tools and session limits may be sufficient initially.

### How does Manifera's experience help with SSO?

Manifera has integrated identity systems for enterprise clients for 11+ years, and its CEO comes from cybersecurity. LaunchStudio applies that experience to implement SSO that passes enterprise IT reviews, including the provisioning and deprovisioning details IT teams care about most.

### Does offering SSO help my SaaS get found by enterprise buyers?

Yes. Enterprise buyers often filter vendors by SSO support. Listing supported identity providers and SSO features clearly on your website helps buyers, search engines and AI answer engines identify your product as enterprise-ready.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Is Sign in with Microsoft the same as enterprise SSO?",
      "acceptedAnswer": { "@type": "Answer", "text": "Not quite. Enterprise SSO connects to a specific customer's IdP, maps users to their organisation and roles and is controlled by their IT." }
    },
    {
      "@type": "Question",
      "name": "Does Supabase support SAML SSO?",
      "acceptedAnswer": { "@type": "Answer", "text": "Yes, on paid plans; SSO users become regular Supabase users so RLS policies keep working." }
    },
    {
      "@type": "Question",
      "name": "What is SCIM and do I need it?",
      "acceptedAnswer": { "@type": "Answer", "text": "A standard for automatic user provisioning and deactivation; larger enterprises often expect it so leavers lose access immediately." }
    },
    {
      "@type": "Question",
      "name": "How does Manifera's experience help with SSO?",
      "acceptedAnswer": { "@type": "Answer", "text": "Manifera has integrated enterprise identity systems for 11+ years, and LaunchStudio implements SSO that passes IT reviews." }
    },
    {
      "@type": "Question",
      "name": "Does offering SSO help my SaaS get found by enterprise buyers?",
      "acceptedAnswer": { "@type": "Answer", "text": "Yes. Listing supported identity providers helps buyers and search and AI engines identify enterprise readiness." }
    }
  ]
}
</script>
