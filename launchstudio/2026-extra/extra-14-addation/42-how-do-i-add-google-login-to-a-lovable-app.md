---
Title: "How Do I Add Google Login to a Lovable App?"
Keywords: google login lovable, lovable oauth, supabase google sign in, social login ai app, LaunchStudio, Manifera
Buyer Stage: Consideration
Target Persona: AI-Native Founder (Non-Technical)
---

# How Do I Add Google Login to a Lovable App?

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "How Do I Add Google Login to a Lovable App?",
  "description": "Google login in a Lovable app runs through Supabase Auth and a Google Cloud OAuth client. This guide covers the setup, redirect URLs for preview and production, the consent screen, account linking and the reasons Google login breaks after launch.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-02-19",
  "inLanguage": "en",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/how-do-i-add-google-login-to-a-lovable-app" }
}
</script>

**Short answer:** create an OAuth client in Google Cloud, enable the Google provider in Supabase Auth with that client's ID and secret, add your Supabase callback URL to Google, add your app's domains to Supabase's allowed redirect URLs, and call Supabase's Google sign-in from your Lovable login page. It takes under an hour to work in the preview. Making it work reliably in production takes a few more decisions.

## Setup Overview

| Where | What to configure |
| --- | --- |
| Google Cloud Console | OAuth consent screen, OAuth client (web application), authorised redirect URI |
| Supabase Auth | Enable Google provider, paste client ID and secret, set site URL and redirect URLs |
| Lovable app | "Continue with Google" button calling Supabase sign-in |

The authorised redirect URI in Google points to Supabase's callback endpoint for your project, not to your app. Supabase then redirects back to your app, which is why your app's URLs must be in Supabase's redirect allow list.

## Why It Breaks After Launch

**Redirects to the preview.** Supabase's site URL still points to the Lovable preview, so users land on the wrong domain after login. Set the site URL to production and list preview URLs separately.

**"redirect_uri_mismatch".** The redirect URI configured in Google does not exactly match what Supabase sends, often a different project or a typo.

**Consent screen in testing mode.** While the Google consent screen is in testing, only listed test users can sign in. Publish it before launch. Depending on the scopes you request, Google may require verification, so ask only for basic profile and email.

**Custom domain for Supabase.** If you later move Supabase to a custom domain, the callback URL changes and Google must be updated.

## Decisions to Make Before Launch

- **Account linking.** If someone signs up with email and later uses Google with the same address, should it be the same account? Supabase can link identities with the same verified email; decide and test the behaviour.
- **Profile creation.** Make sure a profile row is created for Google users too, typically with a database trigger on new auth users, not only in the email sign-up flow.
- **Business accounts.** For B2B, you might restrict sign-in to certain company domains or map users to organisations based on their email domain, enforced server-side.
- **Privacy statement.** List Google as a sign-in provider and what data you receive.

## Testing Checklist

1. New user signs in with Google on production: profile created, lands on the right page
2. Existing email user signs in with Google: behaviour matches your linking decision
3. Login works on mobile browsers and in-app browsers
4. Logout and login again works without loops
5. A user outside your allowed domains (if restricted) is refused

## Getting It Done

Google login is usually a small part of a LaunchStudio Launch Ready engagement (€800-€3,500), together with redirect URLs, email confirmation and session handling. Behind LaunchStudio is Manifera's team of 120+ engineers, who have implemented authentication with Supabase Auth, Auth0 and Firebase for 11+ years; see [Manifera's web app development](https://www.manifera.com/services/web-app-develop/). Supabase's [Login with Google guide](https://supabase.com/docs/guides/auth/social-login/auth-google) covers the exact screens. If users are being logged out unexpectedly, our article on [fixing common Lovable problems](https://launchstudio.eu/en/blog/fix-my-lovable-app-the-problems-founders-bring-us-most) covers redirect and session issues.

## Real example

### An AI-Native Founder in Action: The Study Planner That Only Its Founder Could Log Into

Joris Kuijpers, a student counsellor in Nijmegen, built Tentamenplan in Lovable: students plan revision for exams and share schedules with study groups. He added Google login because nearly every student had a Google account. It worked perfectly for him.

On launch day, students reported "access blocked" errors. The Google consent screen was still in testing mode with Joris as the only test user. After he published it, logins succeeded but sent students back to the Lovable preview domain. Google users also had no profile row, so the study group features crashed for them.

LaunchStudio published and simplified the consent screen scopes, set the production site URL and redirect list in Supabase, added a trigger that created profiles for every new auth user, enabled identity linking for students who had registered with email first, and tested on iOS and Android browsers.

**Result:** Login problems disappeared within a day of the fix. Over the exam period, around 1,300 students signed up, three-quarters of them through Google.

> *"It worked every time I tested it. I was the only person in the world it was configured to work for."*
> - **Joris Kuijpers, Founder, Tentamenplan (Nijmegen)**

**Cost & Timeline:** €950 (Launch Ready package: OAuth configuration, redirects, profile trigger, identity linking and testing) - completed in 3 business days.

## Frequently Asked Questions

### Why do users see "access blocked" when logging in with Google?

Usually because the Google OAuth consent screen is still in testing mode, which only allows listed test users. Publish the consent screen and request only basic scopes such as email and profile to avoid extra verification.

### Why does Google login send users back to the Lovable preview?

Supabase's site URL or redirect settings still point to the preview domain. Set the site URL to your production domain and add every legitimate domain to the allowed redirect URLs.

### Can users sign in with Google and email for the same account?

Yes, if you configure identity linking. Supabase can link identities sharing a verified email. Decide on the behaviour and test it, because silently creating duplicate accounts confuses users and splits their data.

### How does Manifera's authentication experience help with social login?

Social login involves several systems agreeing on URLs, scopes and identities. Manifera's 11+ years of authentication work across providers make those configurations routine, which avoids launch-day surprises.

### Does Google login affect SEO?

Not directly. It can improve sign-up conversion, which helps engagement signals. Make sure public pages remain accessible without login so search engines and AI assistants can still read them.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Why do users see access blocked when logging in with Google?",
      "acceptedAnswer": { "@type": "Answer", "text": "The consent screen is usually still in testing mode. Publish it and request only basic scopes." }
    },
    {
      "@type": "Question",
      "name": "Why does Google login send users back to the Lovable preview?",
      "acceptedAnswer": { "@type": "Answer", "text": "Supabase's site URL or redirect list still points to the preview. Set production as site URL and list allowed domains." }
    },
    {
      "@type": "Question",
      "name": "Can users sign in with Google and email for the same account?",
      "acceptedAnswer": { "@type": "Answer", "text": "Yes with identity linking for verified emails; decide and test the behaviour to avoid duplicates." }
    },
    {
      "@type": "Question",
      "name": "How does Manifera's authentication experience help with social login?",
      "acceptedAnswer": { "@type": "Answer", "text": "11+ years of authentication work make URL, scope and identity configuration routine." }
    },
    {
      "@type": "Question",
      "name": "Does Google login affect SEO?",
      "acceptedAnswer": { "@type": "Answer", "text": "Not directly; keep public pages accessible without login so they can be crawled and cited." }
    }
  ]
}
</script>
