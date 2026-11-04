🚨 Mark de Graaf, a coach in Arnhem, built Rustpunt with Lovable: a guided journaling app for people recovering from burnout, with an AI-generated weekly reflection. Two occupational health services wanted to offer it to employees. Both sent a privacy questionnaire. Mark couldn't answer most of it. 😳

The questions were simple. He just didn't know what his own app was doing with people's diaries. Here's what the AI had built without a word about the AVG: 🧠

❌ The Supabase project running in a US region
❌ Every journal entry sent to an AI API - no processor agreement, default data settings
❌ Analytics capturing full URLs, including entry IDs
❌ Account deletion that removed the login but kept every journal entry

✅ Database and storage migrated to Frankfurt
✅ Minimal data sent to the AI provider, under a processor agreement with training excluded
✅ Identifiers stripped from analytics, plus full account deletion and data export
✅ A retention job for inactive accounts and a data map for his privacy consultant

At **LaunchStudio**, backed by Manifera's 11+ years of building for Dutch organisations like TNO, we handle the technical half of an AVG-proof app - your privacy lawyer handles the wording. 🛠️

💡 His result: €4,800, fourteen business days. Both occupational health services approved Rustpunt, about 420 employees used it within six months, and every later questionnaire took under an hour. 🚀

👉 Is your AI-built app ready for a Dutch privacy questionnaire? Here's what AVG-proof really means: https://launchstudio.eu/en/blog/gdpr-proof-app-netherlands-avg-for-ai-built-products

#GDPR #AVG #Privacy #Lovable #LaunchStudio #Manifera
