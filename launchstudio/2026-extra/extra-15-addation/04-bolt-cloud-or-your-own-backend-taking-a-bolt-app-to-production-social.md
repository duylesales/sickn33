🚨 Ruben Smits, a wedding photographer in 's-Hertogenbosch, built Fotodeel in Bolt: guests scan a QR code, upload photos to a shared gallery and download the best ones. It ran at a dozen weddings on Bolt's built-in hosting. Then a venue chain in Brabant wanted it for every couple - with EU storage, a processing agreement and deletion of all photos 90 days after each event. 😳

Ruben also found that galleries were protected only by a link in the frontend, while the file listing could be queried for any event. Here's when Bolt Cloud is enough, and when you need your own backend: 🧠

❌ Gallery access controlled only by a hard-to-guess link
❌ File listings queryable for any event
❌ A Stripe key sitting in a frontend file
❌ No retention policy or usage export for the venue contract

✅ A Supabase project in Frankfurt with ~41,000 photos in private buckets
✅ Row Level Security per event, with signed download URLs
✅ A scheduled job deleting photos 90 days after each event
✅ The Stripe key moved to an edge function and rotated, plus a monthly usage export

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we keep your Bolt frontend and give it a backend customers can sign off on. 🛠️

His result: €4,900, 12 business days. Fotodeel went live with the venue chain and ran at around 140 events in its first season. The auto-deletion job became a selling point. 🚀

👉 Bolt Cloud or your own backend? Here's how to decide: https://launchstudio.eu/en/blog/bolt-cloud-or-your-own-backend-taking-a-bolt-app-to-production

#BoltNew #Supabase #GDPR #EventTech #AIFounder #LaunchStudio #Manifera
