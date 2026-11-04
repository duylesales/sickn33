🚨 Ilse van Wijk, a legal assistant in Leiden, built Clausewijs in Lovable: small business owners upload supplier contracts and get a plain-language summary of notice periods, liability and price clauses. Within two weeks of a LinkedIn post, 300 people had tried it. Then her AI provider sent a usage alert: €640 in two days. 😳

The feature worked so well that strangers started using it - on her account. Here's what was going on: 🧠

❌ The AI API key sitting in frontend code, copied and used from unknown sources
❌ Any logged-in user could summarise any contract by changing its ID
❌ Full contracts, signatures and personal details sent to the AI API
❌ No usage limits per user or plan

✅ The key revoked and rotated, AI calls moved into an edge function that verifies contract ownership
✅ Daily per-user limits tied to plans
✅ Personal data stripped before text reaches the model, training disabled under a processing agreement
✅ Model output rendered as plain text

At **LaunchStudio**, backed by Manifera's security-minded delivery, every AI call is treated like any other data access: verified, limited and minimised. 🛠️

💡 Her result: €2,300, seven business days. Daily AI costs dropped to a predictable €4-€8, and Clausewijs converted 41 users to paid plans in its first month. 🚀

👉 Adding AI features like ChatGPT to a Lovable app? Here's the safe architecture and five safeguards: https://launchstudio.eu/en/blog/how-do-i-add-ai-features-to-my-lovable-app-safely

#AI #LLM #Lovable #AISecurity #LaunchStudio #Manifera
