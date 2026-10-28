🚨 Bram Nieuwenhuijs's Hypotheekmap collects payslips, employment contracts, bank statements and ID documents for 26 mortgage advisers and about 400 clients. One client copied the URL of his own payslip, swapped in a friend's surname - and the friend's employment contract loaded. 😳

No hacking involved. The file naming was the vulnerability. Here's how storage buckets leak in AI-built apps: 🧠

❌ A public bucket - readable by anyone with the URL, no login, no expiry
❌ Files named by surname and document type, so the bucket could be walked
❌ Permanent links embedded in emails already sent
❌ Deleting an account never removed the stored files

✅ A private bucket with policies matched on the organisation segment of the path
✅ 1,247 files migrated to adviser/client/document paths with generated IDs, plus a documents table
✅ Server-side signed URLs: 15 minutes to view, one hour to download
✅ Upload validation by real content type (25 MB limit), 180 old links invalidated, and deletion that removes files too

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we check your bucket settings first - it takes ten minutes and it's usually where the exposure is. 🔒

His result: three business days and €3,300 later, the exposure was closed within the week. Bram reported it to the Dutch Data Protection Authority and told every affected adviser and client - two advisers said that transparency is why they stayed. 🚀

👉 Storage buckets and who can read what: https://launchstudio.eu/en/blog/lovable-supabase-storage-buckets-and-who-can-read-what

#Supabase #DataSecurity #GDPR #Lovable #LaunchStudio #Manifera
