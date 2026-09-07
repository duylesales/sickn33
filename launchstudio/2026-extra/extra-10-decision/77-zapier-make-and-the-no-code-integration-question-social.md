🚨 Guusje van Dam had 11 customers naming 11 different systems, and thought scoping a Zapier connector would solve it. She ended up rebuilding her API instead. 😳

"Just add Zapier support" sounds like a weekend add-on — most of the real work is a prerequisite nobody budgeted for: 🧠

❌ Registrations came from one endpoint with no ordering or cursor, so a polling trigger would have silently missed records under load
❌ Field names for the same object differed depending on which endpoint returned it
❌ Errors came back as generic 500s with no message, which Zapier would have shown users as an unexplained failure
❌ There was no authentication a non-technical person could complete — access relied on a session cookie

✅ Build cursor-based listing endpoints with stable ordering before touching the connector definition
✅ Standardise field names across every endpoint returning the same object
✅ Return meaningful validation errors, since those messages get shown directly to non-technical users
✅ Add API key authentication and outgoing webhooks for the events actually worth triggering on

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we build the API and event delivery that integration platforms actually require. 🔌

Her result: 10 of 11 integration requests satisfied by the finished listing, with the eleventh handled directly by that customer's own developer using the same webhooks. 🚀

👉 Find out what your Zapier request is really asking for: [Link to article]

#Zapier #API #SaaS #NoCode #LaunchStudio #Manifera
