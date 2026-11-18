🏡 FOR VIEWING: one photo storage setup (before renovation)

Features include:
• Spacious originals of 8 to 15 MB each, served everywhere, even in thumbnail grids
• An open-plan public bucket, with paths based on listing addresses
• Interior photos of unsold homes, viewable by anyone who guesses a path
• Original GPS metadata, preserved in every photo
• Photos of sold and withdrawn listings, kept forever
• About 30% of storage taken up by orphaned uploads from abandoned forms
• A Supabase bill growing several times faster than revenue, mostly storage egress

This was Woningfoto. Lieke Mol built it with Bolt and Supabase so estate agents can upload property photos, organise them per listing, share galleries with sellers and export them to listing websites. After a year: 60 agencies, and that bill.

THE RENOVATION (LaunchStudio, 8 business days, €2,900)
🔨 Browser-side resizing to 2,400 pixels, with compression and metadata stripping before upload
🔨 Thumbnail and medium variants generated at upload
🔨 Gallery and seller photos in a private bucket, with organisation-based storage policies and signed URLs valid for a few hours
🔨 Photos for public listings copied to a public bucket with long cache durations
🔨 A metadata table linking every file to a listing
🔨 A nightly job removing orphaned uploads, and sold listings' photos deleted after an agreed retention period

AFTER RENOVATION
Storage down about 70%. Egress down over 80%. The bill back to a sensible share of revenue. And interior photos of unsold homes no longer public, which two agencies checked before renewing.

"I was paying to send fifteen-megabyte photos to thumbnails the size of a stamp, and anyone could see inside my clients' homes. Fixing it saved money and my reputation." - Lieke Mol

https://launchstudio.eu/en/blog/supabase-storage-costs-and-cdn-for-user-files

#Supabase #CloudCosts #CDN #RealEstate #AIFounder #LaunchStudio #Manifera
