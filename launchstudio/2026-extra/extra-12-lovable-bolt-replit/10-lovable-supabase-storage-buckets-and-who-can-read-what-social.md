🔬 Anatomy of one link (illustrative)

.../public/client-documents/jansen-payslip.pdf

public ➜ the bucket was open to the internet
jansen ➜ the client's surname
payslip ➜ the document type

One client copied the URL of his own payslip, changed the surname to that of a friend who used the same adviser, and his friend's employment contract opened. He emailed the founder about it, politely, on a Sunday. 🏠

Bram Nieuwenhuijs built Hypotheekmap with Lovable: mortgage advisers collect documents from clients, like payslips, employment contracts, bank statements and identity documents, and pass a complete file to the lender. 26 advisers, around 400 clients. Uploads went into a public bucket, named by surname and document type, because it made the admin screen easier to read.

There was no hacking. The file naming was the vulnerability.

What LaunchStudio changed (3 business days, €3,300):
✓ A private bucket, with policies matching the organisation segment of the path
✓ All 1,247 objects migrated to an adviser-id/client-id/document-id layout, with generated identifiers instead of names
✓ A documents table recording uploader, path, size, type and timestamp
✓ Signed URLs generated server-side: fifteen minutes to view, one hour to download
✓ Uploads validated by actual content type, with a 25 MB limit
✓ The old bucket blocked, then deleted
✓ 180 previously issued document links from sent emails invalidated, with advisers asked to re-share from inside the product
✓ Account deletion extended to remove stored files, which it had never done

🔬 Anatomy of a link, now
Private. Unguessable. Expiring.

The exposure closed within the week. Bram reported the incident to the Autoriteit Persoonsgegevens with a description of the fix, and informed the 26 advisers and the clients whose documents had been reachable. Two advisers said the transparency was why they stayed.

"He guessed one URL. There was no hacking involved - my file naming was the vulnerability, and I had chosen it because it made the admin screen easier to read." - Bram Nieuwenhuijs

https://launchstudio.eu/en/blog/lovable-supabase-storage-buckets-and-who-can-read-what

#Supabase #DataSecurity #GDPR #Lovable #LaunchStudio #Manifera
