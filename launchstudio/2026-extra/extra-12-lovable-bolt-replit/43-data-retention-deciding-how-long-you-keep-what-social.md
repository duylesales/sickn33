🚨 Xander Lubbers's Bezorgdienst handles delivery planning and proof of delivery for 19 couriers and meal suppliers - about 40,000 deliveries a month. In four years, nothing had ever been deleted: 1.6 million records with names, addresses, phone numbers, notes and signatures, plus 900 GB of photos. 😳

Then, in one month: an access request that took two days across three systems, and a courier invoking their deletion clause - which he couldn't meet for one company without touching everyone. Here's how to decide how long you keep what: 🧠

❌ "Keep everything" by default, because deletion was never built
❌ No retention period for any category of data
❌ Deletion that only thinks about database rows
❌ Backups kept indefinitely

✅ Retention per category with reasons: deliveries 24 months (adjustable per customer), signatures and photos 12, finance 7 years, logs 60 days
✅ Anonymisation that keeps date, postcode area, category and duration - so route analytics survive
✅ A weekly batched job with dry-run mode, legal-hold exclusion, run records and an alert if it stops
✅ Deletion covering storage, thumbnails, search index and old exports, 60-day backups, per-customer deletion certificates and a fast access-request tool

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we help you hold less data - a smaller problem in every direction. 🗑️

His result: five business days and €3,700 later, the first run anonymised 1.1 million records and removed 640 GB of files (€190/month saved). Access requests now take four minutes instead of two days - and customers' analytics were untouched. 🚀

👉 Data retention: deciding how long you keep what: https://launchstudio.eu/en/blog/data-retention-deciding-how-long-you-keep-what

#DataRetention #GDPR #Privacy #Lovable #LaunchStudio #Manifera
