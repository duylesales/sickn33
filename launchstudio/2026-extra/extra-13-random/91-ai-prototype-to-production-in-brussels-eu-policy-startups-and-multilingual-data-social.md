🚨 Camille Lenaerts spent eight years at a Brussels environmental NGO, then built Dossierwatch with Cursor: organisations follow legislative files, get AI summaries of new amendments in English and French, map stakeholder positions and share internal notes. 22 NGOs and three trade associations subscribed. Then a trade association's IT lead asked: could NGOs campaigning against them see their stakeholder notes? 😳

The honest answer: it depended on the page. A search endpoint returned matching notes from every organisation. Private notes were sent to an AI model to "improve summaries" without clients knowing. Summaries weren't linked to amendment versions — one misattributed an amendment after an update. French accented terms weren't found, and the last plenary week crawled because summaries were generated on page load. Here's what taking a Brussels policy tool from AI prototype to production requires: 🧠

❌ Client notes leaking through search
❌ Private notes sent to an AI model without consent
❌ Summaries not traceable to source versions
❌ No multilingual search or peak-week capacity

✅ Organisation-level separation with row level security and negative tests
✅ Private notes sent to the model only if an organisation opts in
✅ Every summary linked to source versions and regenerated when sources change, with AI labels and a review status
✅ Accent-insensitive multilingual search, background generation and ingestion with monitoring, cached dossier pages — and a procurement-ready data description listing the AI provider as processor

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we build every feature around one boundary: public data can be shared, client insight never. ⚙️

Her result: €3,700 over twelve business days, plus €49/month. The trade association signed, the next plenary week stayed fast, and Dossierwatch added eleven organisations — several citing the data description in procurement. 🚀

👉 AI prototype to production in Brussels: EU policy startups and multilingual data: https://launchstudio.eu/en/blog/ai-prototype-to-production-in-brussels-eu-policy-startups-and-multilingual-data

#Brussels #PolicyTech #EUAffairs #Multilingual #LaunchStudio #Manifera
