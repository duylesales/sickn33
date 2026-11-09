🧘 Linda Smeets runs an online course platform for yoga teachers from Nijmegen, built with Lovable, Supabase, Vercel, Stripe and an email provider. After a price change, some students paid but never got access or the welcome email. She opened tickets with Lovable, Supabase, Stripe and the email provider, and posted on Vercel's forum. 🎫

Every platform answered helpfully, and every one was right: their part worked. The bug lived between them: 🧠

❌ The webhook looked up courses by an old price ID after the price change
❌ It failed silently and still returned success to Stripe
❌ So Stripe never retried, and access was never granted
❌ No access meant no email, and nobody was watching the whole chain

✅ The handler fixed to use product metadata instead of price IDs
✅ Failures now returning errors so Stripe retries
✅ Alerts added on webhook failures
✅ 23 affected students reconciled and granted access, with an apology email Linda approved

At **LaunchStudio**, backed by Manifera's 11+ years of running production systems across many platforms for clients such as Vodafone and TNO, we look after your app as a whole and work with platform support when their part needs attention. 🛠️

Her result: €2,600 plus €49 per month, six business days. Every affected student got access the same day, and a later Stripe API change was handled two months before its deadline. 🚀

👉 LaunchStudio vs platform support plans: https://launchstudio.eu/en/blog/launchstudio-vs-platform-support-plans

#Support #Stripe #Supabase #Lovable #AIFounder #LaunchStudio #Manifera
