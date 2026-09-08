🚨 A DNS change quietly broke Youssef's certificate renewal. On a Saturday morning, every browser hitting his check-in system threw a full-page security warning. 😳

"Renewal is automated" feels like a solved problem — until it fails silently for weeks first. Here's what the outage uncovered: 🧠

❌ Renewal failed silently at 60 days and again at 75 days after a DNS record was removed — nobody was watching
❌ Practices couldn't check patients in on a Saturday; the fix took an hour once he found out, two hours later
❌ The audit found the payment provider's secret key sitting in his repository history for 14 months, never rotated
❌ A storage key with full read-and-write access was embedded in the frontend bundle, and an OAuth secret was 22 months into a two-year expiry

✅ Monitor certificate expiry with an alert at two weeks out — don't just trust that renewal worked
✅ Rotate first, investigate second, whenever a credential may have leaked — the window it's valid is the risk
✅ Keep an inventory of every credential, where it's used, and its expiry date, reviewed quarterly
✅ Replace embedded keys with short-lived, server-issued credentials, and enable automated secret scanning on your repo

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we audit credential handling — including what's quietly sitting in repository history — as part of launch preparation. 🔐

His result: every credential rotated, a full inventory built, expiry monitoring added, uploads reworked off the embedded key, and secret scanning enabled — delivered in 2 business days. 🚀

👉 Find out what's hiding in your repository history: https://launchstudio.eu/en/blog/secrets-keys-and-certificates-that-expire

#SaaS #IndieHacker #DevOps #CyberSecurity #LaunchStudio #Manifera
