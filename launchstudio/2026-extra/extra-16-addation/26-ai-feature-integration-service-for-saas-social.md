📑 Sven de Boer runs a procurement consultancy in Eindhoven and built Contractwijzer with v0, Cursor and Supabase: a SaaS that stores supplier contracts for manufacturers. He added an AI assistant: "Which contracts renew automatically next quarter?" Customers loved it in demos. Two months later, the AI bill was higher than the revenue from the feature. 💸

Worse, answers sometimes mentioned another customer's contracts. The review showed why: 🧠

❌ The API key in the frontend and no limits per user
❌ The full text of every contract sent with each question
❌ Retrieval searching all customers' embeddings without filtering by organisation
❌ Requests hanging for half a minute with no timeout

✅ The assistant moved server-side with a rotated key
✅ Retrieval rebuilt with pgvector, filtered by organisation, returning only relevant clauses
✅ Model routing, plus renewal dates extracted into fields so many questions became plain queries
✅ Plan limits, caching, timeouts, usage alerts and a 60-question evaluation set

At **LaunchStudio**, backed by Manifera's 11+ years of building software and integrations for clients such as Vodafone and TNO, we make AI features useful, affordable and safe for real customers. 🛠️

His result: €5,600, fourteen business days. AI cost per customer fell to a fraction, the leak was closed and correct answers rose from 41 to 55 of 60. 🚀

👉 AI feature integration service for SaaS: https://launchstudio.eu/en/blog/ai-feature-integration-service-for-saas

#AI #LLM #SaaS #Supabase #AIFounder #LaunchStudio #Manifera
