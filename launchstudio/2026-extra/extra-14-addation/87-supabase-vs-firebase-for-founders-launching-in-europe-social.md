🚨 Mark Peeters built Clubbeheer with FlutterFlow and Firebase: a mobile app for amateur sports clubs. Chat and live match updates worked beautifully. Then club treasurers wanted fee overviews per team and season - which meant reading thousands of documents and stitching them together. Firebase costs spiked every time a report ran, and a permissive Security Rule let any member read every other member's payment status. 😳

Firebase was perfect for the live parts of his app. His treasurers needed a database that could add up numbers. Here's what broke: 🧠

❌ Relational reporting forced onto a document database
❌ Thousands of reads per report, and a monthly bill that spiked with them
❌ Reports taking around a minute to load
❌ A Security Rule exposing every member's payment status

✅ Security Rules fixed: members see their own payments, treasurers see their club's
✅ Firebase kept for the app's real-time features
✅ A nightly sync of financial data into Supabase PostgreSQL in Frankfurt
✅ Treasurer reports as SQL views in a small web dashboard, plus monitoring

At **LaunchStudio**, backed by Manifera's 11+ years with both relational and document databases, we pick backends by data shape, users' locations and team skills - not by whichever default the builder chose. 🛠️

💡 His result: €4,300, twelve business days. Firebase read costs dropped sharply, reports now load in seconds, and treasurers of 22 clubs use the dashboard at season end. 🚀

👉 Supabase or Firebase for a European launch? Here's the practical comparison: https://launchstudio.eu/en/blog/supabase-vs-firebase-for-founders-launching-in-europe

#Supabase #Firebase #PostgreSQL #GDPR #LaunchStudio #Manifera
