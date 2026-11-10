🚨 Lieke Mol built Woningfoto with Bolt and Supabase: estate agents upload property photos, share galleries with sellers and export them to listing sites. After a year with 60 agencies, the Supabase bill was growing several times faster than revenue. 😳

The cause was mostly storage egress. And worse: interior photos of unsold homes were reachable by anyone who guessed a path. Here's how to control Supabase storage costs and use a CDN for user files: 🧠

❌ 8-15 MB originals served everywhere, even in thumbnail grids
❌ A public bucket with address-based paths exposing interiors of unsold homes
❌ Photos keeping GPS metadata
❌ Sold listings never cleaned up, and ~30% of storage orphaned uploads

✅ Browser-side resizing to 2,400 px with compression and metadata stripping
✅ Thumbnail and medium variants generated at upload
✅ A private bucket with organisation policies and signed URLs, public listings cached long
✅ A metadata table, nightly orphan cleanup and agreed retention for sold listings

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we cut your storage bill and close the privacy gaps at the same time. 🛠️

Her result: €2,900, 8 business days. Storage dropped by about 70%, egress by over 80% - and two agencies checked the new privacy before renewing. 🚀

👉 Is your Supabase storage bill growing? Here's how to fix it: https://launchstudio.eu/en/blog/supabase-storage-costs-and-cdn-for-user-files

#Supabase #CloudCosts #CDN #RealEstate #AIFounder #LaunchStudio #Manifera
