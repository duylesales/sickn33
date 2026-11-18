🧾 AI PROVIDER USAGE ALERT
Account: Clausewijs
Spend in the last two days: €640
Requests from: sources you don't recognise

Ilse van Wijk, a legal assistant in Leiden, built Clausewijs in Lovable: small business owners upload supplier contracts and get a plain-language summary of notice periods, liability and price clauses. A LinkedIn post brought 300 people in two weeks. The feature worked so well that strangers started using it. On her account.

The API key was in the frontend code, and someone had copied it.

The investigation found two more problems:
• Any logged-in user could request a summary of any uploaded contract, just by changing its ID
• Full contracts, signatures and personal details included, were sent to the API

What LaunchStudio changed (7 business days, €2,300):
✓ The key revoked and rotated
✓ AI calls moved into an edge function that checks contract ownership
✓ Per-user daily limits tied to plans
✓ Personal data stripped before text goes to the model
✓ Training on submitted data disabled, under a processing agreement
✓ Output rendered as plain text

🧾 AI PROVIDER USAGE, AFTER
Daily spend: a predictable €4 to €8
First month: 41 users converted to paid plans, each with a clear usage limit

"The feature worked so well that strangers started using it. On my account." - Ilse van Wijk

https://launchstudio.eu/en/blog/how-do-i-add-ai-features-to-my-lovable-app-safely

#AI #LLM #Lovable #AISecurity #LaunchStudio #Manifera
