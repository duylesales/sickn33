🦷 Ilse Jansen runs a scheduling SaaS for physiotherapy practices from Arnhem, built with Lovable and Supabase and already production ready after an earlier LaunchStudio project. Then dental practices asked for something similar, with different appointment types, reminders and integrations. Her first instinct: copy the Lovable project and its database. ✂️

Copying everything usually leads to: 🧠

❌ Two diverging codebases to maintain
❌ Patient data from different products mixed in one database
❌ Shared secrets, so one leak affects both products
❌ Revenue that cannot be reported per product

What LaunchStudio set up instead: ✅

✅ Two apps in one repository, sharing a design system, components and authentication
✅ A separate Supabase project per product, so patient data never mixes, with one login for practices using both
✅ Separate Stripe products for clear revenue per app
✅ The pipeline, monitoring, backups, tests and project instructions reused and extended, plus separate privacy documentation for the dental app

At **LaunchStudio**, backed by Manifera's 11+ years of building product families and platforms for clients such as Vodafone and TNO, we help you reuse what works and separate what matters. 🛠️

Her result: €3,400 within Launch Ready, eight business days, because most of the foundation already existed. The dental product launched with 12 practices in its first month, with no incidents. 🚀

👉 Production readiness for a second product or spin-off: https://launchstudio.eu/en/blog/production-readiness-for-a-second-product-or-spin-off

#SecondProduct #SpinOff #Lovable #SaaS #AIFounder #LaunchStudio #Manifera
