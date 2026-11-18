🧊 A bookshop search, above and below the waterline

ABOVE THE WATERLINE (what readers noticed)
Search across 38,000 second-hand books took several seconds and froze older phones.

BELOW THE WATERLINE (what nobody noticed)
Every search loaded every book record into the browser and filtered there, private fields included. The books table policy returned all columns to everyone. So every shop owner's purchase prices and supplier notes were sitting in the network responses of any visitor.

Pauline Smeets runs a network of second-hand bookshops in Limburg and built Boekenspoor in Lovable: shops list their stock, readers search across all shops, and shop owners have a private dashboard with purchase prices and supplier notes.

"Search was slow, which I noticed. It was also leaking every shop's purchase prices, which I didn't." - Pauline Smeets

What LaunchStudio changed (6 business days, €1,850):
✓ Public and private fields split into separate tables, each with its own policies
✓ A full-text search column with Dutch configuration, across title, author and description
✓ Trigram matching for author names
✓ Paginated results
✓ Search moved into a database function that returns public fields only

ABOVE THE WATERLINE NOW
Search responses well under half a second. Fewer searches with zero results, thanks to stemming and typo tolerance.

BELOW THE WATERLINE NOW
Private prices gone from public responses.

https://launchstudio.eu/en/blog/how-do-i-add-search-to-my-supabase-app

#Supabase #Postgres #Search #Lovable #LaunchStudio #Manifera
