🔬 Anatomy of one link

/storage/v1/object/public/documents/1234/payslip.pdf

public ➜ the bucket was open to anyone
1234 ➜ sequential IDs: try 1235, then 1236
payslip.pdf ➜ exactly what it sounds like

A landlord noticed that pattern in a Huurdossier link. Changing the number opened other tenants' payslips. 📄

Bart Smulders built Huurdossier in Bolt: people applying for rental homes upload ID, payslips and employer statements once, then share one dossier link with landlords. Around 900 tenants in Eindhoven used it within two months.

What else the review found:
• No storage policies at all
• Phone photos of ID cards containing location data showing where they were taken

What LaunchStudio did (5 business days, €1,950):
✓ All documents moved to a private bucket, with random file names, and existing files and references migrated
✓ Storage policies so tenants can only access their own folder
✓ Dossier sharing through time-limited signed links, sent to landlords via a share page
✓ Metadata stripped from images
✓ Size and type limits on uploads
✓ Every file deleted when a tenant closes their account

Bart documented the incident and informed the affected users.

The anatomy of a link today: private, random, and expiring. No file is reachable without authorisation. Bart also added a public page explaining how dossiers are protected, which several landlords mention as a reason to accept Huurdossier links.

"The whole point of my app was keeping sensitive documents in one safe place. They were in one place. It just wasn't safe." - Bart Smulders

https://launchstudio.eu/en/blog/how-do-i-let-users-upload-files-safely

#Supabase #FileUploads #AppSecurity #GDPR #LaunchStudio #Manifera
