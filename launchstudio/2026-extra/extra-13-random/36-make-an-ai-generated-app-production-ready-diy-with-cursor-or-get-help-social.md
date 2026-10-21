🚨 Stijn Vermeulen, a frontend developer in Voorburg, built Paadje with Cursor: a subscription app with curated Dutch hiking routes, offline maps, GPX downloads and trail reports. He did almost everything himself — domain, SSL, DKIM/DMARC, Sentry, uptime checks, CI and staging. Before launching paid subscriptions, he booked a review of just the three things he was quietly worried about. All three were worth worrying about. 😳

Premium GPX files were served from a public bucket, so the paywall only hid a button. Stripe cancellations weren't handled, so cancelled subscribers kept premium access forever. And the RLS policy on trail reports let any logged-in user update any report — Cursor had written `using (auth.uid() is not null)`, and Stijn's tests only checked people editing their own. Here's how to split DIY and help when making an AI-generated app production ready: 🧠

❌ A paywall in the interface, not in storage
❌ Subscription lifecycle with only the happy path
❌ An AI-written policy that passed happy-path tests
❌ Reviewing your own code for what you forgot

✅ Premium files moved behind proper storage access
✅ Stripe cancellations, failed renewals and refunds handled
✅ RLS policies corrected
✅ Negative tests added to CI — and walked through so Stijn could extend them himself

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we're happy to review just the risky 20% while you do the other 80%. ⚙️

His result: €1,600, six business days. Paadje reached 1,900 paying hikers by autumn; Stijn maintains it alone, and his negative tests have already caught one policy regression from a Cursor refactor. 🚀

👉 Make an AI generated app production ready: DIY with Cursor or get help?: https://launchstudio.eu/en/blog/make-an-ai-generated-app-production-ready-diy-with-cursor-or-get-help

#IndieHacker #Cursor #Supabase #SoloFounder #LaunchStudio #Manifera
