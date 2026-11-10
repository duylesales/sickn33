🚨 Hugo Verheij built Intakehulp with Lovable and Supabase: it processes new client inquiries for small law firms, extracts the facts, classifies the area of law and drafts a Dutch reply. Every step used the same large model through a US endpoint, called from four edge functions with slightly different code. 😳

Costs were high, responses sometimes took over twenty seconds, and a law firm's privacy officer asked where inquiries were processed. Then the model version was announced for retirement. Here's how to choose an LLM API for an EU SaaS: 🧠

❌ One big model for every task
❌ Four slightly different AI call implementations
❌ No clear answer on processing location, retention or agreements
❌ No way to test whether a newer model behaved the same

✅ An evaluation set of 120 anonymised inquiries with expected results
✅ A smaller model for classification and extraction, a larger one for drafting
✅ One provider abstraction with per-task config, schema validation, retries and cost logging
✅ EU regional processing with no training use, plus a fallback model for drafting

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we make the ability to switch models your real asset. 🛠️

His result: €4,800, 12 business days. AI costs per inquiry fell by about 70%, processing time dropped from around 18 to 5 seconds, and the model retirement was handled in an afternoon. 🚀

👉 OpenAI, Anthropic or Mistral for your EU SaaS? Here's how to choose: https://launchstudio.eu/en/blog/choosing-an-llm-api-for-an-eu-saas-openai-anthropic-or-mistral

#LLM #AIEngineering #GDPR #LegalTech #AIFounder #LaunchStudio #Manifera
