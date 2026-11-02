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
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/how-do-i-add-two-factor-authentication-to-my-app" }
}
</script>

**Short answer:** Supabase Auth supports multi-factor authentication with authenticator apps (TOTP). Add an enrolment screen where users scan a QR code, a challenge step after login, and, importantly, enforce MFA in your Row Level Security policies by checking the session's assurance level for sensitive data. Plan recovery before you launch, because users will lose phones.

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
