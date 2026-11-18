Unpopular opinion: your database is not an API. Even when it technically works like one. 🔌

Hasan Demir built Wagenpark in Cursor and Supabase: fleet maintenance for small transport companies, tracking vehicles, inspections and repairs. A customer with 60 vans asked for API access to pull data into their planning system. Under time pressure, Hasan sent them his Supabase URL and public key, with instructions.

It worked. Until:
• He renamed a column, and the customer's integration broke overnight
• He realised their integration ran under a normal user account, whose permissions allowed reading other tenants' vehicle registrations through one loosely protected table

Every schema change was now a risk to that customer. And one loose table was a risk to everyone else.

The real API (LaunchStudio, 13 business days, €4,800):
✓ The loose policy fixed
✓ A versioned /v1 API built with edge functions, for vehicles, inspections and repairs
✓ Per-organisation API keys with read and write scopes, stored as hashes
✓ Rate limits per plan, and usage logs
✓ Signed outgoing webhooks for completed inspections
✓ Public documentation

The customer moved to the new API within a week. Hasan can change his schema now without breaking anyone's integration. Three more customers adopted the API, and API access became a feature of his highest plan.

Self-test: if a customer's integration uses your database URL and anon key, they are one column rename away from an outage.

"I gave a customer my database as an API. Every change I made after that was a risk to them, and every table was a risk to everyone else." - Hasan Demir

https://launchstudio.eu/en/blog/how-do-i-offer-an-api-to-my-saas-customers

#API #SaaS #Supabase #APISecurity #LaunchStudio #Manifera
