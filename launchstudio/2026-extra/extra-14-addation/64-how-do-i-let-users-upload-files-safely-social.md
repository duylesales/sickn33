🚨 Bart Smulders built Huurdossier in Bolt: tenants applying for rental homes upload their ID, payslips and employer statements once, then share a dossier link with landlords. About 900 tenants in Eindhoven used it within two months. Then a landlord noticed the file links ended in /public/documents/1234/payslip.pdf - and changing the number opened other tenants' payslips. 😳

The whole point of his app was keeping sensitive documents in one safe place. They were in one place. It just wasn't safe. Here's why: 🧠

❌ All documents in a public bucket
❌ Sequential IDs in the file paths, so links could be guessed
❌ No storage policies at all
❌ Phone photos of ID cards still carrying location data showing where they were taken

✅ All documents moved to a private bucket with random file names, and existing files migrated
✅ Storage policies so tenants can only access their own folder
✅ Dossier sharing through time-limited signed links on a share page for landlords
✅ Metadata stripped from images, size and type limits, and every file deleted when a tenant closes their account

At **LaunchStudio**, backed by Manifera - trusted by Vodafone, TNO and CFLW for secure document handling - we make uploads private by default, owner-only and short-lived. 🛠️

💡 His result: €1,950, five business days. No file was reachable without authorisation after the fix, and a public page explaining dossier protection became a reason landlords accepted Huurdossier links. 🚀

👉 Letting users upload files in your AI-built app? Here are the seven steps to doing it safely: https://launchstudio.eu/en/blog/how-do-i-let-users-upload-files-safely

#Supabase #FileUploads #AppSecurity #GDPR #LaunchStudio #Manifera
