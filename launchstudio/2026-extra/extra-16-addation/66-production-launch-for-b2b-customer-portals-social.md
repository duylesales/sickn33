🍽️ Karin Wouters runs a family-owned hospitality supplies wholesaler in Roosendaal and built Bestelportaal with Lovable and Supabase: around 300 restaurants and hotels reorder, see their own prices and download invoices synced from Exact Online. Phone orders dropped within weeks. Then a hotel manager mentioned that, by changing a filter, he could see what another hotel chain paid. 😬

The assessment found the portal's foundation wasn't separating customers at all: 🧠

❌ Prices and invoices filtered by customer only in the interface
❌ Invoice PDFs in a public bucket with predictable names
❌ The Exact Online sync token readable in a client-side function
❌ Every user at a customer seeing everything, including kitchen staff who only reorder

✅ Company separation enforced with Row Level Security on prices, orders and invoices, with isolation tests
✅ Invoices in private storage with short-lived signed links, and downloads logged
✅ The Exact Online sync moved to a scheduled server function with a rotated, scoped token and failure alerts
✅ Customer roles for admins, buyers and finance, and idempotent orders so a double click no longer creates two

At **LaunchStudio**, backed by Manifera's 11+ years of building portals and integrations for clients such as Vodafone and TNO, we separate your customers properly and connect your back office safely. 🛠️

Her result: €3,200, eight business days. No customer can see another's prices anymore, and customer admins now manage their own staff. 🚀

👉 Production launch for B2B customer portals: https://launchstudio.eu/en/blog/production-launch-for-b2b-customer-portals

#CustomerPortal #B2B #ExactOnline #Lovable #AIFounder #LaunchStudio #Manifera
