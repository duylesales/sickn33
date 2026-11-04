🚨 Hasan Demir built Wagenpark with Cursor and Supabase: fleet maintenance for small transport companies. A customer with 60 vans asked for API access. Under time pressure, Hasan sent them his Supabase URL and public key. It worked - until he renamed a column and broke their integration overnight. 😳

Then it got worse: the customer's integration could read other tenants' vehicle registrations. He'd given a customer his database as an API. Here's what that meant: 🧠

❌ Customers coupled directly to his internal database schema
❌ Every schema change a breaking change for their systems
❌ One loosely protected table exposing other tenants' data
❌ No way to scope, limit or measure what the customer did

✅ The loose policy fixed
✅ A versioned /v1 API in edge functions for vehicles, inspections and repairs
✅ Per-organisation API keys with read and write scopes, stored as hashes, plus rate limits per plan and usage logs
✅ Signed outgoing webhooks for completed inspections, and public documentation

At **LaunchStudio**, backed by Manifera's 11+ years of designing enterprise integration APIs, we build small, versioned, strictly authorised APIs - never your database with a key attached. 🛠️

💡 His result: €4,800, thirteen business days. Hasan can now change his schema without breaking anyone, three more customers adopted the API, and API access became a feature of his top plan. 🚀

👉 Business customers asking for an API? Here's how to offer one safely from an AI-built SaaS: https://launchstudio.eu/en/blog/how-do-i-offer-an-api-to-my-saas-customers

#API #SaaS #Supabase #APISecurity #LaunchStudio #Manifera
