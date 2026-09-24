---
Title: "AI Application Security Audit After a Freelancer Leaves: Taking Back Access"
Keywords: ai application security audit, freelancer offboarding, revoke access, code ownership, account ownership, LaunchStudio, Manifera
Buyer Stage: Awareness
Target Persona: AI-Native Founder (Non-Technical)
---

# AI Application Security Audit After a Freelancer Leaves: Taking Back Access

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "AI Application Security Audit After a Freelancer Leaves: Taking Back Access",
  "description": "When a freelancer or co-founder leaves, the access they held often stays. This article explains the access audit every founder should run — repositories, hosting, databases, keys, domains, payment and email accounts — plus the contractual side of ownership.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-12-02",
  "inLanguage": "en",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/ai-application-security-audit-after-a-freelancer-leaves-taking-back-access" }
}
</script>

The freelancer who helped you finish your Lovable app was friendly, fast and has now moved on to another client. Nothing went wrong. But somewhere, a GitHub account you don't control can still push code to your repository, a Supabase key they copied during debugging still works, and your domain renews on their credit card next March. An AI application security audit after a contributor leaves is not about suspicion. It is about making sure the only people who can change your product are the people who should.

## Why Access Outlives the Relationship

Building an AI app quickly means handing out access quickly. A freelancer needs the repository, the database, the hosting dashboard, sometimes the payment provider to test webhooks. A co-founder sets up the domain and the email provider under their own account because it is faster. Nobody writes this down, and when the collaboration ends, nobody reverses it.

This matters for three reasons. Former contributors' accounts can be compromised even if they themselves are trustworthy. You cannot act quickly in an incident if an account you need is controlled by someone who no longer answers. And investors and customers increasingly ask exactly this question: who has access to your production systems?

## The AI Application Security Audit for Access, Area by Area

**Code repository.** List every collaborator and deploy key on GitHub, GitLab or Bitbucket. Remove anyone who no longer needs access. Check whether the repository itself is owned by your company account or by someone's personal account; transfer it if needed.

**AI builder projects.** Lovable, Bolt, Replit and similar tools have their own project sharing. Former contributors may still be able to edit and publish.

**Hosting and deployment.** Vercel, Netlify, Replit Deployments, AWS or DigitalOcean — check team members, API tokens and connected Git integrations.

**Database and backend.** Supabase or Firebase project members, plus keys. Service role keys and admin credentials a freelancer used should be rotated, not just their user removed.

**Secrets and API keys.** Payment providers, email providers, AI model APIs, maps and analytics. Anyone who saw a secret key may still have it. Rotate every key a departed contributor could have seen.

**Domain and DNS.** Who owns the registrar account? Whose card pays for renewal? Losing a domain is one of the few truly unrecoverable incidents.

**Email, analytics and support tools.** Google Workspace, transactional email, analytics dashboards, helpdesk and error tracking.

**App stores.** Apple and Google developer accounts, if you have a mobile app.

## The Rotation Order

Rotating keys can break production if done carelessly. A safe order: first list every place a key is used, then create the new key, update all environments, deploy, confirm everything works, and only then revoke the old key. Do payment and database keys during quiet hours, and keep a written log of what was rotated when.

## The Contractual Side

Access is technical; ownership is legal. Check that you have written agreements with former contributors assigning intellectual property in the code to your company, and that any confidentiality obligations continue after the collaboration ended. If code was written without an agreement, ask for a simple IP assignment now, while relations are good. This is the kind of document that becomes very expensive to obtain during a funding round or acquisition.

## Make Offboarding Routine

For the future, a short offboarding checklist turns a stressful audit into a ten-minute routine:

- Give contributors personal accounts, never shared logins
- Use team features on every platform, owned by the company account
- Record which secrets each person can see
- On departure: remove accounts, rotate secrets, confirm ownership of everything, file the IP assignment

## An Access Register Template

The central output of an AI application security audit focused on access is an access register — a living document listing every system and who can reach it:

| System | Purpose | Owner account | People with access | Access level | 2FA | Last reviewed |
| --- | --- | --- | --- | --- | --- | --- |
| GitHub repository | Source code | Company org | Founder, developer | Admin, write | Yes | Date |
| Supabase project | Database, auth, storage | Company email | Founder | Owner | Yes | Date |
| Vercel | Hosting | Company team | Founder, developer | Owner, member | Yes | Date |
| Mollie | Payments | Company | Founder, bookkeeper | Owner, read-only | Yes | Date |
| Domain registrar | Domain, DNS | Company | Founder | Owner | Yes | Date |
| Email provider | Transactional email | Company | Founder | Owner | Yes | Date |
| Error tracking | Monitoring | Company org | Founder, developer | Admin, member | Yes | Date |

Alongside it, keep a secrets register listing each key's name, the service it belongs to, where it is stored and when it was last rotated — never the value itself. Review both monthly and after anyone joins or leaves.

## Rotating Keys Without Downtime

Rotation is where access clean-ups most often cause outages. A safe procedure per key:

1. **Find every usage:** environment variables in each environment, CI secrets, automation tools, mobile apps, partner integrations.
2. **Create the new key** in the provider's dashboard while the old one still works.
3. **Update all usages** with the new key and deploy.
4. **Verify** in logs or the provider's dashboard that requests now use the new key.
5. **Revoke the old key.**
6. **Record** the rotation in the secrets register.

For database passwords and service-role keys, schedule rotation during quiet hours and have a rollback plan. For webhook signing secrets, some providers allow two active secrets during a transition period.

## Checking for Leftover Access in Unexpected Places

Former contributors often retain access in places nobody checks:

- **Personal access tokens** on GitHub or hosting platforms, created for local deployments.
- **Deploy keys and CI secrets** in forks or old repositories.
- **OAuth apps** authorised to act on your accounts.
- **Automation tools** (n8n, Make, Zapier) connected with their credentials.
- **Shared password managers or chat messages** containing keys.
- **Local `.env` files** on their machines — which is why rotation, not just removal, matters.
- **Backup copies or exports** of your database they may have downloaded.

Ask departing contributors, politely and in writing, to delete local copies of code, data and credentials, and to confirm they have done so.

## Offboarding Checklist

For every departure, run through:

- Remove from repository, AI builder, hosting, database, payment, email, analytics, monitoring and support tools.
- Revoke personal tokens and OAuth authorisations they created.
- Rotate every secret they could have seen.
- Transfer ownership of any account registered in their name.
- Update the access and secrets registers.
- Collect signed IP assignment and confirmation of deleted local copies.
- Review recent activity logs for anything unusual.

Keep the checklist in your company documents and run it the same day the collaboration ends.

## Onboarding With Offboarding in Mind

Most offboarding pain is created at onboarding. When someone joins, give them personal accounts through team features owned by the company, the minimum access needed, dev-only secrets where possible and a written agreement covering IP and confidentiality. Record what they received in the access register. When they leave, reversing it is quick.

## Legal Agreements Worth Having

For freelancers and contractors, a simple agreement should cover: scope of work, payment, assignment of intellectual property to your company upon creation or payment, confidentiality, data protection obligations if they handle personal data, return or deletion of materials at the end, and no retention of access. Templates exist from chambers of commerce and legal services; a lawyer can adapt one in an hour. For code already written without an agreement, a short retroactive IP assignment is usually easy to obtain while the relationship is friendly.

## Signs of Misuse to Look For

After someone leaves, review logs for the preceding weeks and following days: unusual logins, large data exports, changes to payment settings, new admin users, deleted backups or new API keys. Most departures are entirely benign, but a quick review provides peace of mind and, in rare cases, early warning.

## Making It Routine

Access hygiene works best as a monthly habit: ten minutes to compare the register with reality, remove stale access and note any rotations due. Founders who make this routine rarely face stressful clean-ups — and can answer an investor's or customer's access question in seconds.

## Special Cases: Co-Founders and Agencies

Co-founder departures are more complex than freelancer departures, because co-founders often created the accounts in the first place and may hold shares. Handle access and ownership in the same shareholder or separation agreement: which accounts transfer, by when, and how credentials are handed over. For agencies that built your app, ask for a formal handover — repository transfer, credentials, documentation, a list of third-party accounts they created on your behalf — before the final invoice is paid. Both situations are much easier to resolve while relationships are good.

## Least Privilege for Everyday Work

Access audits often reveal that everyone has owner or admin rights, simply because it was easiest. Reduce privileges to what each person needs: developers rarely need to change billing, bookkeepers need read-only payment access, support staff need a support view rather than database access. Fewer privileged accounts means fewer ways for a compromised account to cause serious damage — and a smaller list to review each month.

## What Investors and Customers Ask

Due-diligence questionnaires and enterprise security reviews commonly ask: Who has administrative access to production? How is access granted and revoked? Is MFA enforced? How are secrets managed and rotated? When was access last reviewed? An up-to-date access register and offboarding checklist answer all five. Founders who can share these documents immediately stand out — and avoid the scramble that turns a routine question into a week of detective work.

## Tooling That Helps

Several tools make access management easier for small teams: a team password manager for shared credentials, SSO for workforce tools where affordable, secret managers for application keys, and GitHub organisation settings that enforce 2FA for members. None are strictly required, but each reduces the chance that access quietly accumulates in personal accounts.

## The Principle

Access should always belong to the company and be granted to people — never the other way round. When that principle holds, contributors can come and go without leaving doors open behind them.

## Start Today

Open your repository's collaborator list and your database project's member list now. Anyone there who should not be is your first finding.

## Where LaunchStudio Fits

LaunchStudio runs access audits as part of its security reviews: every account, key and integration listed, ownership consolidated under your company with two-factor authentication, secrets rotated safely and a written access register handed over. The code stays in your repository, documented, and nobody at LaunchStudio keeps access after the project unless you ask for managed hosting.

LaunchStudio is powered by Manifera, a software development company with 11+ years of experience and a founder, Herre Roelevink, whose background lies in cybersecurity. Manifera works from Amsterdam (Herengracht 420), Singapore (Tras Street) and Ho Chi Minh City. See [Manifera's about page](https://www.manifera.com/about-us/); GitHub's [guide to reviewing repository access](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/managing-repository-settings/managing-teams-and-people-with-access-to-your-repository) is a practical starting point.

[Plan a free 15-minute intro call](https://launchstudio.eu/en/#contact) if you are not sure who can still reach your production systems.

## Real example

### An AI-Native Founder in Action: A Moving-Help Marketplace and Four Forgotten Accounts

Nadia Bakkali, a former logistics planner in Alphen aan den Rijn, built Verhuisvriend in Lovable with help from two freelancers: a marketplace where people moving house book local helpers and vans by the hour, with Mollie payments and chat. After launch, both freelancers moved on, and Nadia ran the platform alone for eight months, growing to 1,700 completed jobs.

When a larger removals company proposed a partnership, its IT manager asked who had access to Verhuisvriend's production systems. Nadia could not answer. LaunchStudio's audit found that one freelancer was still an owner of the GitHub repository and the Supabase project; the other still had a Vercel team seat and a personal access token that could deploy; the Mollie live API key had been pasted into a shared chat during testing and never rotated; the domain was registered under the first freelancer's name; and neither freelancer had signed an IP assignment.

LaunchStudio's engineers transferred the repository and Supabase project to Nadia's company account, removed both freelancers from all platforms, revoked the Vercel token, rotated the Mollie, Supabase service role, email and maps keys in a planned sequence without downtime, enabled two-factor authentication everywhere and produced an access register. Nadia contacted the freelancers, who transferred the domain and signed IP assignments within a week.

**Result:** Nadia sent the access register to the removals company, and the partnership went ahead. Verhuisvriend now runs a ten-minute offboarding checklist whenever a contractor finishes.

> *"Nobody had done anything wrong. But if one of them had lost their laptop, they'd have lost my business along with it."*
> — **Nadia Bakkali, Founder, Verhuisvriend (Alphen aan den Rijn)**

**Cost & Timeline:** €1,300 (access audit, ownership transfer, key rotation and access register) — completed in 5 business days.

## Frequently Asked Questions

### What should an AI application security audit check after a freelancer leaves?

Every account and key the freelancer could reach: repository, AI builder projects, hosting, database, payment, email and analytics providers, domain registrar and app stores — plus whether IP was formally assigned to your company.

### Is removing a freelancer's user account enough?

No. Keys and tokens they saw or created keep working after their account is removed. Rotate secrets and revoke personal access tokens and deploy keys as well.

### Can rotating API keys break my live app?

It can if done out of order. Create the new key, update every environment, deploy and verify, then revoke the old key — ideally at a quiet time.

### Why does Manifera treat access control as part of security, not administration?

Because many real incidents begin with forgotten access rather than clever exploits. Herre Roelevink's cybersecurity background shaped Manifera's view that knowing who can change production is a security fundamental.

### Can clear ownership help with partnerships and AI-driven due diligence?

Yes. Partners, investors and increasingly automated vendor assessments ask who controls your systems. A documented access register answers the question immediately and signals maturity.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "What should an AI application security audit check after a freelancer leaves?", "acceptedAnswer": { "@type": "Answer", "text": "Every account and key the freelancer could reach, plus whether IP was formally assigned to the company." } },
    { "@type": "Question", "name": "Is removing a freelancer's user account enough?", "acceptedAnswer": { "@type": "Answer", "text": "No. Rotate secrets and revoke personal tokens and deploy keys too." } },
    { "@type": "Question", "name": "Can rotating API keys break my live app?", "acceptedAnswer": { "@type": "Answer", "text": "Only if done out of order: create, update, deploy, verify, then revoke." } },
    { "@type": "Question", "name": "Why does Manifera treat access control as part of security, not administration?", "acceptedAnswer": { "@type": "Answer", "text": "Many incidents begin with forgotten access; knowing who can change production is a security fundamental." } },
    { "@type": "Question", "name": "Can clear ownership help with partnerships and AI-driven due diligence?", "acceptedAnswer": { "@type": "Answer", "text": "Yes. A documented access register answers vendor and investor questions immediately." } }
  ]
}
</script>
