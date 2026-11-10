---
Title: "Why Does Google Login Show a Supabase URL? Branding Your Sign-In"
Keywords: google login shows supabase url, supabase oauth custom domain, continue to supabase.co, google consent screen app name, LaunchStudio, Manifera
Buyer Stage: Awareness
Target Persona: AI-Native Founder (Non-Technical)
---

# Why Does Google Login Show a Supabase URL? Branding Your Sign-In

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Why Does Google Login Show a Supabase URL? Branding Your Sign-In",
  "description": "When users sign in with Google on a Supabase app, the screen often says 'continue to xyz.supabase.co' instead of your brand. This guide explains why, what it does to trust and conversion, and how to fix it with a verified Google consent screen, a custom domain for Supabase Auth and correct redirect settings, plus the verification steps Google requires.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-07-20",
  "inLanguage": "en",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/why-does-google-login-show-a-supabase-url" },
  "citation": [
    { "@type": "CreativeWork", "name": "Supabase: Login with Google", "url": "https://supabase.com/docs/guides/auth/social-login/auth-google" },
    { "@type": "CreativeWork", "name": "Supabase: Custom domains", "url": "https://supabase.com/docs/guides/platform/custom-domains" },
    { "@type": "CreativeWork", "name": "Google: OAuth consent screen and app verification", "url": "https://support.google.com/cloud/answer/13463073" },
    { "@type": "CreativeWork", "name": "Supabase: Redirect URLs", "url": "https://supabase.com/docs/guides/auth/redirect-urls" }
  ]
}
</script>

**Short answer:** Google shows a Supabase address such as "continue to abcdefgh.supabase.co" because, in a standard setup, Google sends the user back to Supabase's authentication server, and that is the domain Google displays. Users see an unfamiliar, random-looking address at the most sensitive moment of signing up, and some abandon. To fix it, configure the Google consent screen with your app name, logo and domains, and get it verified by Google; then use a custom domain for your Supabase project, such as `auth.yourdomain.nl`, so the redirect goes through your own domain. Update the redirect settings in both Google and Supabase, test thoroughly, and the sign-in screen will show your brand.

## Key Takeaways

- **Google displays the domain of the redirect URL,** which defaults to your Supabase project address.
- **An unbranded sign-in screen costs conversions** and looks like phishing to cautious users.
- **Two fixes work together:** a configured, verified consent screen and a custom domain for Supabase Auth.
- **Google verification** for branding requires a privacy policy, homepage and domain ownership.
- **Redirect URLs must match exactly** in Google Cloud and Supabase, or sign-in fails.

## Why the Supabase Address Appears

Signing in with Google uses OAuth. Your app sends the user to Google; after they choose an account, Google sends them back to a "redirect URL" with proof of who they are. In Supabase's standard setup, that redirect URL is `https://yourprojectref.supabase.co/auth/v1/callback`, because Supabase's server handles the exchange before sending users on to your app.

Google's account chooser tells users where they are signing in to. Without a configured and verified consent screen, it shows the domain of that redirect: your Supabase project reference. To a user who expected "Sign in to Plannerly", "continue to qwkxjrtplmzv.supabase.co" looks odd at best and suspicious at worst.

## Why It Matters

- **Trust:** users have learned to check where they sign in. An unknown domain at the sign-in step looks like a phishing page.
- **Conversion:** every hesitation at sign-up loses some users, and sign-up is the step you paid most to get people to.
- **B2B sales:** IT-aware customers notice and ask questions about data handling.
- **Professionalism:** it signals that the product is not finished.

## Fix 1: Configure the Google Consent Screen

In Google Cloud Console, under the OAuth consent screen (in newer versions called Google Auth Platform branding), set:

- **App name** as users know it
- **Logo**
- **Support email**
- **Homepage URL, privacy policy URL and terms URL** on your own domain
- **Authorised domains,** including your app's domain

Set the publishing status to "In production" rather than "Testing", because test mode limits sign-ins to listed test users and shows warnings.

## Fix 2: Get Branding Verified

Google shows your app name and logo only after it verifies your branding. For apps that request only basic scopes, such as email, profile and openid, this is usually a light review. Google checks that:

- You own the domains you listed, verified through Google Search Console.
- Your homepage describes the app and links to the privacy policy.
- The privacy policy explains how you handle Google user data.
- The app name and logo do not imitate other brands.

Verification typically takes a few days. If you request sensitive scopes, such as access to Gmail or Drive, the review is far more extensive; avoid those scopes unless your product truly needs them.

## Fix 3: A Custom Domain for Supabase Auth

Even with a verified consent screen, the redirect still goes to `supabase.co`, which some users notice in the address bar and which may appear in the account chooser. Supabase offers custom domains on paid plans as an add-on, letting you serve your project from a subdomain such as `auth.yourdomain.nl` or `api.yourdomain.nl`.

Steps in outline:

1. **Add a CNAME record** for the subdomain in your DNS, pointing to your Supabase project, and the verification record Supabase asks for.
2. **Activate the custom domain** in Supabase once verification succeeds.
3. **Add the new callback URL** (`https://auth.yourdomain.nl/auth/v1/callback`) to the authorised redirect URIs in Google Cloud.
4. **Update your app** to use the custom domain as the Supabase URL.
5. **Keep the old callback** in Google during the transition, then remove it.

A custom domain also keeps authentication cookies and requests on your own domain, which helps with Safari's stricter privacy rules. See [why apps break on iPhone and Safari](https://launchstudio.eu/en/blog/why-does-my-app-break-on-iphone-and-safari).

## Fix 4: Redirect URLs in Supabase

After Google returns to Supabase, Supabase sends the user on to your app. Supabase only allows redirects to URLs you have listed. If your production domain, staging domain or local development address is missing, sign-in may end on the wrong site, such as the default site URL, or fail.

**Check:** the Site URL is your production app, and the allowed redirect URLs include every environment you use. Avoid overly broad wildcards on production.

## Common Mistakes

| Mistake | Effect |
| --- | --- |
| Consent screen left in "Testing" | Only test users can sign in; others see errors |
| Redirect URI in Google does not match exactly | "redirect_uri_mismatch" error |
| Privacy policy on a different domain than the app | Verification rejected |
| Custom domain added but app still uses old URL | Supabase address still shown |
| Old callback removed too early | Sign-ins fail for users mid-flow |
| Sensitive scopes requested unnecessarily | Long verification, scary warnings |

Our guide on [adding Google login to a Lovable app](https://launchstudio.eu/en/blog/how-do-i-add-google-login-to-a-lovable-app) covers the initial setup; this article picks up where branding is concerned.

## Other Sign-In Methods Have the Same Issue

Sign in with Apple, Microsoft and other OAuth providers also display or validate redirect domains, and email templates for magic links and confirmations come from Supabase defaults unless you customise them. Branding the whole sign-in experience means:

- Custom domain for Auth
- Branded consent screens for each provider
- Custom email templates and a sending address on your own domain, see [DNS setup for launch](https://launchstudio.eu/en/blog/dns-setup-for-launch-domain-email-and-ssl)
- Consistent app name and logo everywhere

## Testing the Change

Before switching production:

- Test sign-up and sign-in with Google on staging with the custom domain.
- Test with a Google account that has never used the app, a returning account and a Google Workspace account.
- Test on iPhone Safari, Android Chrome and desktop browsers.
- Test from an in-app browser, where Google sign-in may be blocked anyway, and offer alternatives.
- Check that sessions persist after the change, and that existing users can still sign in.

## How LaunchStudio Helps

LaunchStudio sets up professional authentication for AI-built apps: Google and other OAuth consent screens, branding verification, Supabase custom domains, redirect configuration for all environments, branded authentication emails and testing across browsers and devices, with a careful switchover for existing users.

The **Launch Ready** package (€800-€3,500) covers authentication setup, security hardening and deployment; **Launch & Grow** (€2,500-€7,500 plus €49 per month) adds managed hosting, monitoring and priority support. Use the [price calculator](https://launchstudio.eu/en/#calculator) for an estimate.

LaunchStudio is backed by Manifera, a software development company with 11+ years of experience, 160+ delivered projects and 120+ engineers. Founders meet the team at Herengracht 420 in Amsterdam; engineering happens at the development centre on Pho Quang Street in Ho Chi Minh City, with a hub on Tras Street in Singapore.

## Real example

### An AI-Native Founder in Action: The HR Tool That Looked Like a Phishing Page

Jasper Mulder built Verlofzaken with Lovable and Supabase: a leave and absence tool for small companies, where employees request time off and managers approve it. He sold it to HR managers at companies of 20 to 150 employees, and sign-up worked through Google Workspace accounts.

Two prospective customers paused their trial after their IT contact flagged the sign-in screen. Google showed "continue to xptlqmvhrzke.supabase.co", and one IT manager wrote that it "looked exactly like a phishing test". Jasper also saw in analytics that about a quarter of people who clicked "Sign in with Google" never completed sign-up. The consent screen was still in testing mode with a default name, the privacy policy was a Google Doc link, and the Supabase redirect URLs included only the preview domain and production, so staging sign-ins landed on the live app.

LaunchStudio moved the privacy policy and terms to Jasper's own domain, verified the domain in Search Console and configured the consent screen with the Verlofzaken name, logo and authorised domains, then submitted it for branding verification, approved within four business days. A Supabase custom domain, `auth.verlofzaken.nl`, was set up with DNS records, the new callback added in Google and the app switched over while the old callback stayed active for two weeks. Redirect URLs were set per environment, and authentication emails were rebranded with a sending address on the company domain.

**Result:** The Google screen now shows "Sign in to Verlofzaken" with the logo. Completed Google sign-ups rose from about 75% to 93% of attempts, and both paused prospects resumed and became customers after their IT contacts reviewed the new setup.

> *"I lost deals because of one screen I'd never really looked at. Now the first thing customers see is my brand, not a random address."*
> - **Jasper Mulder, Founder, Verlofzaken (Arnhem)**

**Cost & Timeline:** €1,600 (Launch Ready package: consent screen and verification, Supabase custom domain, redirect configuration, branded auth emails and testing) - completed in 7 business days, including Google's review time.

## Frequently Asked Questions

### Why does Google sign-in say "continue to supabase.co"?

Because Google sends users back to your Supabase project's authentication address, and without verified branding Google shows that domain. A verified consent screen and a custom domain for Supabase Auth replace it with your brand.

### Do I need a paid Supabase plan for a custom domain?

Custom domains are a paid add-on on Supabase's paid plans. Check current pricing; for a product with paying customers, the cost is usually small compared with the trust it adds. See [do I need a paid Supabase plan](https://launchstudio.eu/en/blog/do-i-need-a-paid-supabase-plan-for-production).

### How long does Google verification take?

For apps with only basic scopes, branding verification usually takes a few business days once your domain, homepage and privacy policy are in order. Sensitive or restricted scopes take much longer.

### How does Manifera's experience help with authentication?

Manifera has implemented authentication and single sign-on for business applications for 11+ years. LaunchStudio applies that experience to give AI-built apps a secure, professional sign-in that customers' IT teams accept.

### Does branded sign-in affect SEO or AI visibility?

Indirectly. Domain verification in Search Console, a clear homepage and a public privacy policy are good foundations for search, and a trustworthy sign-up improves conversion from the traffic you earn.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Why does Google sign-in say \"continue to supabase.co\"?",
      "acceptedAnswer": { "@type": "Answer", "text": "Google shows the redirect domain of your Supabase project unless branding is verified and Auth uses a custom domain." }
    },
    {
      "@type": "Question",
      "name": "Do I need a paid Supabase plan for a custom domain?",
      "acceptedAnswer": { "@type": "Answer", "text": "Yes, custom domains are a paid add-on on Supabase paid plans." }
    },
    {
      "@type": "Question",
      "name": "How long does Google verification take?",
      "acceptedAnswer": { "@type": "Answer", "text": "Usually a few business days for basic scopes once domain, homepage and privacy policy are ready." }
    },
    {
      "@type": "Question",
      "name": "How does Manifera's experience help with authentication?",
      "acceptedAnswer": { "@type": "Answer", "text": "Manifera has implemented business authentication and SSO for 11+ years." }
    },
    {
      "@type": "Question",
      "name": "Does branded sign-in affect SEO or AI visibility?",
      "acceptedAnswer": { "@type": "Answer", "text": "Indirectly, through domain verification, public policies and better sign-up conversion." }
    }
  ]
}
</script>
