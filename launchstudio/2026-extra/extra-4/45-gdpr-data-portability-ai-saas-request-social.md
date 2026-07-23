🚨 A client of Hugo's emailed a routine-sounding request: "send me all the data you have on me." It wasn't routine — it explicitly cited GDPR Article 20, and the 30-day legal clock was already running. Hugo realized KlantPortaal had no export function anywhere. 📋

🧠 GDPR data portability isn't a feature anyone thinks to prompt for — it's a legal obligation that only becomes visible the moment someone invokes it.

❌ Cursor built everything a client needed day to day — documents, meeting notes, timelines — but never a single function to pull a user's data together
❌ Personal data was scattered across half a dozen database tables with no unified query connecting them
❌ The only fallback under deadline pressure was an engineer manually querying the production database by hand — slow and risky with a legal clock attached

✅ Map every table in the schema that holds personal data, ahead of any request
✅ Build a reusable export function compiling a user's full data footprint into structured JSON or CSV
✅ Add an internal tool so future requests take minutes, not a legal fire drill

At **LaunchStudio**, we map data flows and build the export path before the first real request ever arrives — applying Manifera's 11+ years of production engineering discipline to GDPR compliance. 🛡️

His result: Hugo fulfilled the original request three days before the legal deadline, and every request since has taken under ten minutes. 🚀

👉 Never tested what happens if a user asks for their data tomorrow? Talk to an engineer about your schema: [Link to article]

#AINativeFounder #LaunchStudio #Manifera #GDPR #DataPortability
