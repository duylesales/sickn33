🚨 Pauline Smeets runs a network of second-hand bookshops in Limburg and built Boekenspoor in Lovable: shops list their stock, readers search across all of them. With 38,000 books listed, search took several seconds and froze older phones. That was the problem she noticed. The one she didn't: every shop's purchase prices were visible to any visitor. 😳

Search was slow, which she saw. It was also leaking private data, which she didn't. Here's why: 🧠

❌ Search loaded every book record into the browser and filtered locally
❌ Private fields - purchase prices and supplier notes - came along with every record
❌ The books table policy returned all columns to everyone
❌ No search index, no pagination, no tolerance for typos

✅ Public and private fields split into separate tables with distinct policies
✅ Full-text search with the Dutch configuration across title, author and description
✅ Trigram matching for author names, plus paginated results
✅ Search moved into a database function that returns only public fields

At **LaunchStudio**, backed by Manifera's 11+ years of building search for enterprise data systems, we move search into the database - inside the same access rules as everything else. 🛠️

💡 Her result: €1,850, six business days. Search responses fell to well under half a second, private prices disappeared from public responses, and zero-result searches dropped sharply. 🚀

👉 Is your app's search filtering everything in the browser? Here's how to do it properly in Supabase: https://launchstudio.eu/en/blog/how-do-i-add-search-to-my-supabase-app

#Supabase #Postgres #Search #Lovable #LaunchStudio #Manifera
