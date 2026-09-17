🚨 Hanneke ran Buurtkracht in Zwolle. Two members requested GDPR deletion. She set `is_deleted = true` in the database. A month later, their names and phone numbers resurfaced in automated group emails and community search. 😳

A 'soft delete' flag does not satisfy GDPR Article 17. True erasure requires cascading database engineering: 🧠

❌ Using soft-delete boolean flags while background jobs, search indexes, and exports continue reading 'deleted' rows
❌ Leaving personal data orphaned in related relational tables (comments, invoices, audit logs)
❌ Retaining uploaded avatars, identity photos, and attachments in storage buckets after account deletion
❌ No documented data retention policy explaining what must legally be kept (tax invoices) vs erased

✅ Implement cascading database deletion workflows or cryptographically anonymize historical records
✅ Purge associated files, photos, and cached avatars from cloud storage buckets immediately
✅ Reconcile tax retention obligations (keeping anonymized financial records for 7 years) with GDPR erasure
✅ Provide users with a verifiable written confirmation detailing exactly what data was removed

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we build compliant, automated data lifecycle and GDPR erasure pipelines into your Supabase backend. ⚖️

Her result: Buurtkracht resolved the deletion requests legally, documented their data retention policy, and passed a regional municipality privacy audit. 🚀

👉 Learn how to handle GDPR data deletion and erasure properly in Supabase: https://launchstudio.eu/en/blog/data-deletion-and-erasure-in-practice

#GDPR #AVG #Supabase #DataPrivacy #LaunchStudio #Manifera
