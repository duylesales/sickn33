🚨 Joris Kramer runs a renovation business in Amersfoort and built KlusKompas in Bolt: homeowners describe a job, upload photos and get an indicative quote. He had a stand at a home-improvement fair in sixteen days — and 300 flyers already printed with the app's QR code. 😳

The two-day review found photo uploads with no limits in a publicly listable bucket, deposits marked "paid" by the browser instead of Mollie's webhook, and an admin screen anyone could reach by guessing the URL. Here's what a realistic 14-day path to production looks like: 🧠

❌ Uploads with no size or type limits, stored publicly
❌ Payment status trusted from the browser
❌ An unprotected admin route for editing quotes
❌ No staging — every Bolt change went straight to live

✅ Day 3: storage locked down and upload limits added
✅ Day 4: admin route behind server-side role checks
✅ Day 5: deposits confirmed only by verified Mollie webhooks
✅ Days 6–12: backups, staging, monitoring and testing — which caught silently failing iPhone HEIC photos

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we take AI-built apps live on a fixed schedule — as long as you stop adding features. ⚙️

His result: €2,900, live on day 13 — two days before the fair. Over the fair weekend: 74 quote requests, 19 paid deposits, zero failed payments. 🚀

👉 AI app to production in 14 days: a realistic schedule: https://launchstudio.eu/en/blog/ai-app-to-production-in-14-days-a-realistic-schedule

#Bolt #AIApp #Startups #Mollie #LaunchStudio #Manifera
