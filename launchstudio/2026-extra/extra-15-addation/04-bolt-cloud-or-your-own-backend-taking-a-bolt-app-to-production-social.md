💍 Something old, something new, something borrowed, something blue

Ruben Smits is a wedding photographer in 's-Hertogenbosch. He built Fotodeel in Bolt: guests scan a QR code at an event, upload photos to a shared gallery and download the best ones afterwards. It ran on Bolt's built-in hosting and database at a dozen weddings.

Then a Brabant venue chain wanted to offer it to every couple. Their contract asked for EU storage, a processing agreement, deletion of all photos 90 days after each event, and a monthly usage export for invoicing.

SOMETHING OLD
Gallery access protected only by an unguessable-looking link in the frontend. The underlying file listing could be queried for any event.

SOMETHING BORROWED
A Stripe key for premium galleries, sitting in a frontend file.

SOMETHING NEW (LaunchStudio, 12 business days, €4,900)
• The Bolt frontend connected to a new Supabase project in Frankfurt
• Around 41,000 photos migrated into private storage buckets
• Row Level Security, so each gallery is limited to its event's guests and the couple, with signed URLs for downloads
• A scheduled function that deletes photos 90 days after each event
• The Stripe key moved into an edge function and rotated
• A monthly usage export for the venue chain

SOMETHING BLUE
Nothing to feel blue about: Fotodeel went live with the venue chain 12 business days after the first call and was used at around 140 events in its first season. The automatic deletion job became a selling point with other venues. Ruben still edits the interface in Bolt.

"Bolt Cloud was perfect for my first weddings. The moment a company asked where photos were stored, I needed my own answer." - Ruben Smits

Bolt Cloud or your own backend? https://launchstudio.eu/en/blog/bolt-cloud-or-your-own-backend-taking-a-bolt-app-to-production

#BoltNew #Supabase #GDPR #EventTech #AIFounder #LaunchStudio #Manifera
