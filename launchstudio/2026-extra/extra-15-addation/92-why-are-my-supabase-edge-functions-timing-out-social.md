🚨 Joost van Leeuwen built Huurcheck with Lovable and Supabase: property managers upload commercial leases, and an AI model flags unusual clauses, indexation terms and notice periods. Pilots went well with short contracts. Then one firm uploaded 60 long leases for an annual review. Nearly every analysis timed out. 😳

One function was trying to do a day's work in one breath. Here's why Supabase Edge Functions time out: 🧠

❌ Whole contracts sent to the AI in one request, plus a second summary call, while the user waited
❌ Long contracts exceeding the wall-clock limit
❌ Scanned PDFs pushing text extraction over the CPU limit
❌ All 60 files looped in one function call, so one failure stopped the rest

✅ A job per contract, with uploads responding immediately
✅ A queue running extraction as its own step
✅ Contracts split into sections analysed in parallel with timeouts and retries, then combined
✅ A dedicated OCR service, progress per contract, email on completion and manual review after two retries

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we give heavy work the right shape - so it becomes boring and reliable. 🛠️

The result: €3,200, 9 business days. The 60-lease batch completed in about 25 minutes without a single timeout, batches of up to 300 run reliably, and two pilot firms became paying annual customers. 🚀

👉 Are your Edge Functions timing out? Here are the limits and fixes: https://launchstudio.eu/en/blog/why-are-my-supabase-edge-functions-timing-out

#Supabase #EdgeFunctions #AIEngineering #PropTech #AIFounder #LaunchStudio #Manifera
