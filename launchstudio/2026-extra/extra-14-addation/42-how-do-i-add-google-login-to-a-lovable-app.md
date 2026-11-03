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
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/how-do-i-add-google-login-to-a-lovable-app" },
  "citation": [
    { "@type": "CreativeWork", "name": "Supabase: Login with Google", "url": "https://supabase.com/docs/guides/auth/social-login/auth-google" },
    { "@type": "CreativeWork", "name": "Supabase: Redirect URLs", "url": "https://supabase.com/docs/guides/auth/redirect-urls" },
    { "@type": "CreativeWork", "name": "GDPR Article 5: Principles", "url": "https://gdpr-info.eu/art-5-gdpr/" },
    { "@type": "CreativeWork", "name": "OWASP Top 10 2021: A07 Identification and Authentication Failures", "url": "https://owasp.org/Top10/A07_2021-Identification_and_Authentication_Failures/" }
  ]
}
</script>

**Short answer:** create an OAuth client in Google Cloud, enable the Google provider in Supabase Auth with that client's ID and secret, add your Supabase callback URL to Google, add your app's domains to Supabase's allowed redirect URLs, and call Supabase's Google sign-in from your Lovable login page. It takes under an hour to work in the preview. Making it work reliably in production takes a few more decisions.

## Key Takeaways

- **Google login in a Lovable app runs through Supabase Auth** and an OAuth client you create in Google Cloud.
- **Most production failures are configuration:** a consent screen still in testing, redirect URLs pointing to the preview domain, or a mismatched redirect URI.
- **Decide on account linking before launch,** so users who sign up with email and later use Google do not end up with two accounts.
- **Request only basic scopes** (email and profile) to avoid extra verification and to respect data minimisation under the GDPR.
- **Always offer an email-based fallback;** not every user has or wants to use a Google account.

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

## How OAuth Sign-In Works, Step by Step

Understanding the flow makes troubleshooting straightforward. When a user clicks "Continue with Google":

1. Your app asks Supabase to start a Google sign-in, including where to return afterwards.
2. Supabase redirects the browser to Google's consent screen with your OAuth client ID.
3. The user chooses an account and approves the requested scopes.
4. Google redirects to Supabase's callback URL with an authorisation code.
5. Supabase exchanges the code for the user's identity, creates or finds the user and issues a session.
6. Supabase redirects the browser back to your app at an allowed URL, where the session is picked up.

Problems at step 3 are usually consent screen settings. Problems at step 4 are usually the authorised redirect URI in Google Cloud. Problems at step 6 are usually Supabase's site URL and redirect allow list. Supabase's guide to Google login and its documentation on redirect URLs describe each setting.

## Configuring the Google Cloud Side

In Google Cloud Console, you set up an OAuth consent screen with your app name, support email, logo and links to your privacy policy and terms. You then create an OAuth client of type "web application" and add Supabase's callback URL as an authorised redirect URI. A few practical notes:

- Use a Google Cloud project owned by your company account, not a personal one
- Keep the consent screen branding consistent with your app so users trust it
- Publish the consent screen before launch; in testing mode only listed test users can sign in
- Request the minimal scopes; additional sensitive scopes trigger Google's verification process

## Configuring the Supabase Side

In Supabase Auth settings, enable the Google provider and paste the client ID and secret. Set the site URL to your production domain, and list every legitimate redirect destination: production, staging and preview URLs if you use them. If your app runs on several subdomains, include each. Store the Google client secret only in Supabase; it should never appear in frontend code.

## Profiles, Roles and Organisations for Google Users

Users who sign in with Google skip your sign-up form, so anything that form did - creating a profile row, assigning a default role, joining an organisation - must also happen for them. The robust approach is a database trigger on new users that creates the profile, plus server-side logic that handles organisation membership, for example through invitations. Test the first-login experience for a brand-new Google user; it is the path most often broken.

## Restricting Sign-In for Business Apps

For B2B products, you may want only users from certain companies to sign in, or to place users into an organisation based on their email domain. Implement these rules on the server: check the email domain in a trigger or edge function, and refuse or route accordingly. Do not rely on hiding the Google button in the interface.

## Adding Microsoft and Apple Too

Business users often have Microsoft accounts; iPhone users may prefer Sign in with Apple, which Apple requires in some App Store situations when other social logins are offered. Supabase supports both through similar configuration. Add them based on your audience rather than by default, and keep identity linking consistent across providers.

## Privacy and Transparency

Social login means Google, Microsoft or Apple process data about the sign-in. Mention each provider in your privacy statement, explain what data you receive (usually name, email and profile picture) and store only what you need. Under the GDPR's data minimisation principle, there is no reason to request calendar, contacts or drive access for authentication.

## Testing Before Launch

Test on desktop and mobile browsers, including in-app browsers from apps like Instagram or LinkedIn, which sometimes block or alter OAuth flows. Test a new user, a returning user, a user who previously registered by email, a user from a blocked domain if you restrict access, and logout followed by login. These tests take half an hour and catch nearly every launch-day problem.

## Common Error Messages and What They Mean

| Message or symptom | Likely cause |
| --- | --- |
| "Access blocked: app has not completed verification" | Consent screen in testing or requesting sensitive scopes |
| "redirect_uri_mismatch" | Authorised redirect URI in Google does not match Supabase's callback |
| Returned to the preview domain | Supabase site URL or redirect list not updated |
| Logged in but app shows errors | Missing profile row or role for new Google users |
| Login loop on mobile | Redirect URL or session storage issues in in-app browsers |

## Security Considerations for Social Login

Social login shifts password security to Google, which is a strength: Google accounts commonly have two-factor authentication and strong breach detection. It also creates dependencies worth managing. If a user loses access to their Google account, they lose access to your app unless an alternative exists; offer email-based recovery. If someone's Google account is compromised, your app is exposed too; for sensitive apps, consider requiring your own second factor for administrators. OWASP's guidance on identification and authentication failures applies regardless of provider: protect sessions, handle logout properly and avoid leaking tokens in URLs or logs.

## Conversion Effects

Social login usually reduces sign-up friction, particularly on mobile, where typing passwords is cumbersome. Measure it rather than assuming: compare completion rates for the Google button and the email form over a few weeks. Some B2B audiences prefer Microsoft; some privacy-conscious audiences avoid social login entirely. Your own data will show which options deserve prominence.

## Keeping It Working After Launch

OAuth configurations break silently when domains change. Whenever you add a domain, move to a custom Supabase domain, change hosting or launch a new environment, update both Google's authorised redirect URIs and Supabase's redirect list, then test login on the new URL. A short line in your deployment checklist prevents a surprisingly common outage.

## When Google Login Is Not Enough

Some customers will ask for single sign-on through their own identity provider, such as Microsoft Entra ID or Okta, so their IT department controls access. That is a later-stage requirement for most founders. Supabase supports SAML-based SSO on certain plans; plan for it when your first enterprise customer requests it, not before.

## Summary

Configure Google Cloud and Supabase carefully, publish the consent screen, align redirect URLs, create profiles for every new user, decide on account linking and test on real devices. Done once, Google login is one of the lowest-maintenance features in your app.

## One Last Tip

Keep a short note in your repository listing every place OAuth is configured - Google Cloud project, Supabase settings, redirect URLs - so the next person to change a domain knows exactly what to update.

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
