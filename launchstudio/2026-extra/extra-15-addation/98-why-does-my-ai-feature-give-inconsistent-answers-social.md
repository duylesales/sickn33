🚨 Iris Dekker built Bonnetjesbak with Lovable and Supabase: freelancers photograph receipts, and AI extracts supplier, date, amount and VAT and assigns a bookkeeping category. Around 1,300 users relied on it for their quarterly VAT returns. Then complaints started. 😳

The same kind of receipt landed in different categories, VAT didn't add up, and some receipts were saved with no data at all. Here's why AI features give inconsistent answers: 🧠

❌ One loose prompt, with the text answer split by line
❌ VAT and totals calculated by the model - wrong on about one in fifteen mixed-rate receipts
❌ Categories from the model's own judgement, no allowed list
❌ A general model alias updated a month before the complaints began

✅ Structured output with a strict schema, a fixed Dutch bookkeeping category list and examples
✅ Validation with one retry, then user review instead of blank records
✅ VAT calculated in code with a mismatch flag, and the model version pinned
✅ An evaluation set of 220 anonymised receipts and one-tap category correction

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we build the reliable part around your AI. 🛠️

The result: €3,100, 9 business days. Category accuracy rose from about 81% to 96%, VAT errors dropped to zero, and support messages about wrong receipts fell by more than 70%. 🚀

👉 Is your AI feature unpredictable? Here's how to make LLM output reliable: https://launchstudio.eu/en/blog/why-does-my-ai-feature-give-inconsistent-answers

#LLM #AIEngineering #StructuredOutput #FinTech #AIFounder #LaunchStudio #Manifera
