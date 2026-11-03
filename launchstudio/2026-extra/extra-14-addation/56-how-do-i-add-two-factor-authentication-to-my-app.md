---
Title: "How Do I Add Two-Factor Authentication to My AI-Built App?"
Keywords: two-factor authentication supabase, mfa lovable app, 2fa ai-built app, totp supabase, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: SaaS Founder Scale-Up
---

# How Do I Add Two-Factor Authentication to My AI-Built App?

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "How Do I Add Two-Factor Authentication to My AI-Built App?",
  "description": "Business customers increasingly ask for two-factor authentication. This guide explains how to add MFA to a Supabase-backed Lovable or Bolt app with authenticator apps, enforce it in policies, handle recovery and decide who must use it.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-03-04",
  "inLanguage": "en",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/how-do-i-add-two-factor-authentication-to-my-app" },
  "citation": [
    { "@type": "CreativeWork", "name": "Supabase: Multi-Factor Authentication", "url": "https://supabase.com/docs/guides/auth/auth-mfa" },
    { "@type": "CreativeWork", "name": "Verizon Data Breach Investigations Report", "url": "https://www.verizon.com/business/resources/reports/dbir/" },
    { "@type": "CreativeWork", "name": "OWASP Top 10 2021: A07 Identification and Authentication Failures", "url": "https://owasp.org/Top10/A07_2021-Identification_and_Authentication_Failures/" },
    { "@type": "CreativeWork", "name": "GDPR Article 32: Security of processing", "url": "https://gdpr-info.eu/art-32-gdpr/" }
  ]
}
</script>

**Short answer:** Supabase Auth supports multi-factor authentication with authenticator apps (TOTP). Add an enrolment screen where users scan a QR code, a challenge step after login, and, importantly, enforce MFA in your Row Level Security policies by checking the session's assurance level for sensitive data. Plan recovery before you launch, because users will lose phones.

## Key Takeaways

- **Supabase Auth supports multi-factor authentication with authenticator apps (TOTP)** and exposes session assurance levels you can check in Row Level Security policies.
- **MFA is one of the most effective controls against credential theft,** which the Verizon Data Breach Investigations Report consistently ranks among the leading causes of breaches.
- **Enforcement must happen on the server:** require assurance level 2 (aal2) in policies and functions for sensitive data and actions.
- **Require MFA for administrators and staff;** offer it to all users; let business customers require it for their members.
- **Plan recovery before launch:** multiple factors, a verified support process and an audit trail for resets.

## Why Customers Ask for It

Security questionnaires from business customers almost always ask whether MFA is available, and sometimes whether it can be required for their users. For apps holding financial, health or business-critical data, MFA is one of the most effective protections against stolen passwords.

## How MFA Works in Supabase

| Step | What happens |
| --- | --- |
| Enrol | User adds a TOTP factor, scans a QR code in an authenticator app, confirms with a code |
| Login | User signs in with password or another method; session is at assurance level 1 (aal1) |
| Challenge | User enters a code from the app; session is upgraded to aal2 |
| Enforce | Policies and functions check for aal2 where required |

## Step 1: Enrolment Screen

In your Lovable settings page, add "Enable two-factor authentication". Show the QR code and the secret for manual entry, then ask for a code to confirm. Show clear instructions and name common authenticator apps.

## Step 2: Challenge After Login

After sign-in, check whether the user has a verified factor and whether the session is still aal1. If so, show a code prompt before letting them into the app.

## Step 3: Enforce It Where It Matters

Hiding pages from users without MFA is not enforcement. Use the `aal` claim in the user's token inside Row Level Security policies for sensitive tables, for example requiring aal2 for admins or for financial data. Supabase documents this pattern in its MFA guides.

## Step 4: Decide Who Must Use It

- **Optional for all users:** easiest start, answers most questionnaires
- **Required for admins and staff:** strongly recommended
- **Required per organisation:** let business customers require MFA for all their members, enforced server-side

## Step 5: Recovery

- Allow more than one factor where possible, such as two devices
- Define an identity verification process for support-led resets
- Log every MFA reset in an audit trail
- Never let support reset MFA based only on an email request

## Step 6: Communicate

Announce MFA to existing users, explain why it helps, and link to setup instructions. Mention it on your security page; it is a fact business buyers look for.

## Why MFA Matters

Passwords fail in predictable ways: reuse across sites, phishing, guessing and leaks. Attackers routinely test leaked email and password combinations against other services, a practice known as credential stuffing. The Verizon Data Breach Investigations Report has repeatedly found stolen or misused credentials among the most common ways breaches begin. A second factor stops most of these attacks, because a stolen password alone is no longer enough. For apps holding financial, health or business-critical data, MFA is now an expectation rather than a premium feature.

## Factor Types Compared

| Factor | Security | User experience | Notes |
| --- | --- | --- | --- |
| Authenticator app (TOTP) | Strong | Good, widely familiar | Supported by Supabase Auth |
| SMS codes | Moderate | Familiar | Vulnerable to SIM swapping and interception |
| Email codes | Moderate | Easy | Only as strong as the email account |
| Passkeys and security keys | Very strong, phishing-resistant | Excellent once set up | Check current support in your auth provider |

Start with authenticator apps, which Supabase supports directly, and consider passkeys as support matures.

## Assurance Levels Explained

Supabase sessions carry an authenticator assurance level. After a password or social login, the session is at aal1. After the user completes an MFA challenge, it is upgraded to aal2. The level is included in the user's token, so Row Level Security policies and edge functions can check it. For example, a policy on a salaries table can require aal2, so even a user with the right role cannot read salary data without completing MFA in that session. That is real enforcement, independent of what the interface shows.

## Rolling Out MFA to Existing Users

Introducing MFA to an existing user base works best in stages:

1. **Announce it** with a short explanation of why it protects users.
2. **Make it optional** for all users, with clear setup instructions.
3. **Require it for staff and administrators** immediately.
4. **Offer organisation-level enforcement** to business customers who want it.
5. **Measure adoption** and consider requiring it for sensitive roles after a transition period.

Forcing MFA on everyone overnight tends to generate support requests and frustration; a staged rollout builds adoption with goodwill.

## Recovery Without Weakening Security

Every MFA system needs a recovery path, and recovery is where attackers look for weaknesses. Good practices:

- Encourage users to register more than one factor
- Provide recovery codes at enrolment and ask users to store them safely
- Require identity verification for support-led resets, never based solely on an email request
- Log every reset with who requested it and who approved it
- Notify the user by email when MFA is reset on their account

## MFA in Security Questionnaires and Contracts

Business customers often ask whether MFA is available, whether it can be enforced for all their users and whether your own staff use it to access production systems. Answer all three: yes, yes and yes. Then include MFA in your security summary and, where relevant, your processing agreement's description of technical measures, in line with the GDPR's Article 32 requirement for appropriate security.

## Usability Details That Matter

Small details reduce friction: show the QR code and a manual setup key, name common authenticator apps, allow users to remember trusted devices for a limited period where appropriate, and give clear error messages for expired codes. Test the flow on a phone, since many users will set it up on the same device they use to log in.

## Implementing MFA in a Lovable App, Step by Step

1. **Enable MFA** in your Supabase Auth settings.
2. **Build an enrolment page** in Lovable that calls Supabase's MFA enrol method, displays the QR code and manual key, and verifies the first code.
3. **Add a challenge step after login** that checks whether the user has a verified factor and whether the session is still aal1, and asks for a code if so.
4. **Update Row Level Security policies** for sensitive tables to require aal2, using the assurance level claim in the user's token.
5. **Protect edge functions** for sensitive actions with the same check.
6. **Add organisation settings** that let business admins require MFA for all members, enforced server-side.
7. **Build recovery** with recovery codes and a verified support process.
8. **Test** with users who have and do not have MFA, across devices.

## Common Mistakes

- Showing an MFA screen in the interface but not enforcing aal2 in policies
- Requiring MFA for customers while staff accounts with broader access have none
- Allowing MFA resets through a simple email request to support
- Not testing enrolment on mobile devices
- Forgetting that API calls with an aal1 session can still reach unprotected tables

## The Payoff

MFA turns stolen passwords from a breach into a failed login attempt. For a few days of work, it removes one of the most common attack paths, satisfies a standard questionnaire item and gives business customers a reason to trust you with their data.

## MFA for Your Own Team and Tools

MFA inside your app protects users; MFA on your own accounts protects everything. Require it on GitHub, Supabase, your hosting provider, payment provider, email provider, domain registrar and any AI or analytics tools with access to customer data. An attacker who takes over your Supabase or GitHub account bypasses every policy in your app. This takes an afternoon to set up and is one of the most valuable security steps a founder can take.

## Monitoring Authentication Events

Watch for signs of attacks: spikes in failed logins, many MFA challenges failing for one account, logins from unusual locations for admin accounts and MFA resets. Supabase Auth logs these events; send alerts for the most suspicious patterns, especially for staff and administrator accounts.

## Related Reading

MFA works best alongside the other controls covered in our guides on bot protection, roles and admin panels, and our 25-point launch checklist.

## What Customers Experience

For most users, MFA adds a few seconds at login and a one-time setup of two minutes. Explain it in plain language: "We ask for a code from your phone so that nobody else can log in with your password." Users who understand why accept it readily, and many business customers will see it as a sign of maturity rather than a hurdle. Measure login completion before and after introducing MFA; with a clear flow, the impact is usually small.

## Summary

Offer MFA to all users, require it for staff and admins, enforce it in policies and functions, plan recovery carefully and turn it on for every account that runs your business.

## Related Reading

See our guides on roles and admin panels and on protecting apps from bots for the controls that work alongside MFA.

## Getting It Built

MFA with enforcement and recovery is a typical two-to-four-day addition in a LaunchStudio engagement. LaunchStudio is backed by Manifera, whose founder Herre Roelevink built his career in cybersecurity at CFLW, and whose engineers implement authentication for enterprise clients; see [Manifera's about page](https://www.manifera.com/about-us/). Supabase's [MFA documentation](https://supabase.com/docs/guides/auth/auth-mfa) covers enrolment, challenges and policy enforcement. For broader context, see our [GDPR checklist for SaaS founders](https://launchstudio.eu/en/blog/gdpr-checklist-for-saas-founders-in-the-netherlands).

## Real example

### An AI-Native Founder in Action: The Payroll Tool That Failed a Questionnaire on One Line

Stefan Huisman built Loonvoorbereider with Cursor and Supabase: a payroll preparation tool for small hospitality businesses, where owners enter hours and the tool prepares data for their payroll provider. A restaurant group with 14 locations wanted to sign, but its security questionnaire included "Is multi-factor authentication enforced for all users with access to salary data?" The answer was no.

The app had password login only. Admin accounts at Stefan's company could see every customer's salary data, also without MFA. Password resets could be triggered by anyone who knew an email address, with no rate limit.

LaunchStudio added TOTP enrolment and challenge screens, enforced aal2 in RLS policies on salary tables, required MFA for all of Stefan's internal admin accounts, allowed customers to require MFA for all their members, added rate limits to password resets and logged MFA resets with a verified support procedure.

**Result:** The restaurant group signed after its security officer reviewed the change. Within three months, 70% of all users had enabled MFA, and three other customers switched on the organisation-wide requirement.

> *"One line in a questionnaire was worth more than any feature on my roadmap that month."*
> - **Stefan Huisman, Founder, Loonvoorbereider (Apeldoorn)**

**Cost & Timeline:** €2,050 (Launch Ready package: MFA enrolment and challenge, RLS enforcement, organisation requirement, reset rate limits and recovery process) - completed in 6 business days.

## Frequently Asked Questions

### Does Supabase support two-factor authentication?

Yes. Supabase Auth supports multi-factor authentication with time-based one-time passwords from authenticator apps, and session assurance levels you can check in policies. Check the documentation for currently supported factor types.

### Is hiding pages enough to enforce MFA?

No. Users without MFA could still call your API. Enforce MFA in Row Level Security policies and server functions by checking the session's assurance level for sensitive data and actions.

### Should SMS be used for two-factor authentication?

Authenticator apps are generally more secure than SMS, which is vulnerable to SIM swapping. SMS can be better than nothing for some audiences, but start with authenticator apps for business users.

### Why does Manifera recommend requiring MFA for internal admins?

Because admin accounts can see every customer's data. Manifera's security background through Herre Roelevink's CFLW work shows that compromised admin credentials cause the most damaging incidents, so MFA there is non-negotiable.

### Does offering MFA help when buyers research my product?

Yes. Security pages that list MFA, data location and other measures give business buyers and AI assistants concrete facts. Tools with clearly documented security are easier to shortlist.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Does Supabase support two-factor authentication?",
      "acceptedAnswer": { "@type": "Answer", "text": "Yes, with TOTP authenticator apps and assurance levels usable in policies." }
    },
    {
      "@type": "Question",
      "name": "Is hiding pages enough to enforce MFA?",
      "acceptedAnswer": { "@type": "Answer", "text": "No. Enforce assurance levels in RLS policies and server functions for sensitive data." }
    },
    {
      "@type": "Question",
      "name": "Should SMS be used for two-factor authentication?",
      "acceptedAnswer": { "@type": "Answer", "text": "Authenticator apps are more secure than SMS, which is vulnerable to SIM swapping." }
    },
    {
      "@type": "Question",
      "name": "Why does Manifera recommend requiring MFA for internal admins?",
      "acceptedAnswer": { "@type": "Answer", "text": "Admin accounts access all customer data; compromised admin credentials cause the most damaging incidents." }
    },
    {
      "@type": "Question",
      "name": "Does offering MFA help when buyers research my product?",
      "acceptedAnswer": { "@type": "Answer", "text": "Yes. Documented security measures give buyers and AI assistants concrete facts." }
    }
  ]
}
</script>
