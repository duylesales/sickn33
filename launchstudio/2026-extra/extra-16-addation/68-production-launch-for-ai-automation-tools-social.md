🧾 Stijn Kuijpers runs a start-up in Venlo that built Bonbot with Cursor and Supabase: it reads purchase invoices from a customer's inbox, extracts supplier, amounts and VAT, and books them in Moneybird or Exact Online. About 40 bookkeeping firms signed up in the first months. Then volumes grew, and so did the problems. 📈

What went wrong in production: 🧠

❌ Processing inside a web request, so large batches timed out, restarted and booked some invoices twice
❌ Rate limit errors that stopped runs without telling anyone
❌ Expired Gmail tokens that silently stopped automations
❌ Full email threads sent to the AI model, and every customer's tokens stored unencrypted in one table

✅ A job queue with workers, retries with backoff and a dead-letter list
✅ A stable key per invoice and stored booking IDs, so retries never book twice
✅ Throttling per accounting system, encrypted tokens with automatic refresh and reconnect prompts
✅ Only the invoice attachment sent to AI, model routing, a review queue for uncertain results and run history per invoice

At **LaunchStudio**, backed by Manifera's 11+ years of building integrations and background processing for clients such as Vodafone and TNO, we make automations safe to retry, visible to customers and affordable to run. 🛠️

His result: €6,200, sixteen business days. Duplicate bookings stopped completely, AI cost per invoice fell substantially and Bonbot grew to about 120 firms. 🚀

👉 Production launch for AI automation tools: https://launchstudio.eu/en/blog/production-launch-for-ai-automation-tools

#Automation #AI #Moneybird #Supabase #AIFounder #LaunchStudio #Manifera
