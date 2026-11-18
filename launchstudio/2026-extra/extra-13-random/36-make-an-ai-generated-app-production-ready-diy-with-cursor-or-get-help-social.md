DIY production readiness: ████████████████░░░░ 80%

Stijn Vermeulen, a frontend developer in Voorburg, built Paadje with Cursor: a subscription app with curated hiking routes across the Netherlands, offline maps, GPX downloads and a community section for trail reports. He planned to do it all himself, and did most of it well. 🥾

THE 80% STIJN DID HIMSELF
✓ Custom domain and SSL
✓ Email with DKIM and DMARC
✓ Sentry
✓ Uptime checks
✓ GitHub Actions CI
✓ A staging environment

THE 20% HE WAS QUIETLY WORRIED ABOUT
Before launching paid subscriptions, he booked a focused review of three areas. All three were worth worrying about.

1. The paywall
Premium GPX files were served from a public bucket. The paywall only hid the download button.

2. Cancellations
Stripe subscription cancellations weren't handled, so cancelled subscribers kept premium access forever.

3. Trail reports
Cursor had written the update policy as "using (auth.uid() is not null)," so any logged-in user could edit any report. Stijn's own tests passed, because they only tested users editing their own reports.

The remaining 20% (LaunchStudio, 6 business days, €1,600):
✓ Storage access fixed
✓ The full Stripe lifecycle handled: cancellations, failed renewals and refunds
✓ RLS policies corrected
✓ Negative tests added to his CI, with a walkthrough, so he could extend them himself

Paadje launched subscriptions in spring and reached 1,900 paying hikers by autumn. Stijn has maintained it alone since, adding negative tests with every new feature. They've already caught one policy regression from a Cursor refactor.

"I didn't need someone to build my app. I needed someone to look at the three things I was quietly worried about. All three were worth worrying about." - Stijn Vermeulen

https://launchstudio.eu/en/blog/make-an-ai-generated-app-production-ready-diy-with-cursor-or-get-help

#IndieHacker #Cursor #Supabase #SoloFounder #LaunchStudio #Manifera
