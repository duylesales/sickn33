🚨 Gijs Kramer built Evenementenhub with Bolt and Supabase: event organisers sell tickets, publish programmes and share photos. Revenue grew steadily - but the Supabase bill grew faster, becoming one of his largest costs. He'd upgraded compute twice and was considering another provider. 😳

Only part of the bill came from production. Here's why a Supabase bill keeps growing: 🧠

❌ Four other paid projects: two old prototypes, staging and a demo, one with PITR
❌ Full-size event photos driving most of the egress
❌ A request log table on every page view, grown to tens of gigabytes
❌ A reconnecting realtime subscription, a failing webhook retried thousands of times a day, and bot sign-ups

✅ Old prototypes deleted, the demo paused and staging downsized without add-ons
✅ Photos resized with variants and served through a CDN
✅ The log table archived and dropped in favour of platform logs
✅ Realtime and webhook fixed, Turnstile on sign-up, and queries indexed so production could downsize

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we find what you're really paying for before you switch providers. 🛠️

His result: €2,400, 6 business days. The monthly Supabase bill fell by roughly 60% while usage grew, pages got faster - and Gijs stayed with Supabase. 🚀

👉 Is your Supabase bill growing faster than your revenue? Here's why: https://launchstudio.eu/en/blog/why-does-my-supabase-bill-keep-growing

#Supabase #CloudCosts #EventTech #FinOps #AIFounder #LaunchStudio #Manifera
