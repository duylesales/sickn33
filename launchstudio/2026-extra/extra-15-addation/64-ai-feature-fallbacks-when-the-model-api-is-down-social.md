🚨 Maarten Oosterhuis built Bonnetjesbot with Bolt and Supabase: employees photograph receipts and AI extracts supplier, date, amount and VAT. Usage peaked on Monday mornings. On several Mondays, the provider rate-limited the account - and once, a two-hour partial outage hit. 😳

Each time, uploads failed, employees had to retake photos, and some gave up. Support heard about it from customers. Here's how to build AI feature fallbacks for when the model API is down: 🧠

❌ The model called synchronously during upload, with no timeout
❌ No retries and no alternative provider
❌ Failed extractions discarding the uploaded image
❌ No record of waiting receipts, and no alerts

✅ Receipts saved to private storage immediately, with extraction from a queue
✅ Timeouts, exponential backoff with jitter and respect for rate limit headers
✅ A circuit breaker switching to a secondary EU-processed model, with jobs held until recovery
✅ Schema validation, prefilled manual entry, per-receipt status and monitoring alerts

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we let the queue absorb the peaks and the fallback absorb the outages. 🛠️

His result: €3,500, 9 business days. On the next Monday rate-limit episode, employees noticed nothing beyond a minute's delay. No receipt was lost the following quarter, and upload tickets dropped to zero. 🚀

👉 What happens when your AI provider goes down? Here's how to build fallbacks: https://launchstudio.eu/en/blog/ai-feature-fallbacks-when-the-model-api-is-down

#AIReliability #LLM #Resilience #FinTech #AIFounder #LaunchStudio #Manifera
