🕵️ Pim's AI tool read every uploaded CV — including one with white-on-white text nobody could see, telling the model to shortlist a candidate it hadn't actually screened. 😳

Assuming only your users are "talking" to your model is the mistake that let this through. Here's the real story: 🧠

❌ Hidden white-on-white text in a PDF instructed the model to ignore assessment criteria and mark the candidate "exceptionally qualified"
❌ The model could update candidate status directly — a hidden instruction became a real hiring action
❌ Nobody could see the injected text; a recruiter only caught it three weeks later from an inconsistent summary
❌ A review found 4 more submissions with similar hidden instructions, from 2 candidates

✅ Removed the model's ability to change status — it now drafts an assessment a recruiter confirms
✅ Uploaded document text extracted and clearly marked as untrusted data, never as instructions
✅ Model access limited strictly to the specific vacancy and candidate under review
✅ Output validated against an expected structure, with scores constrained to a fixed range

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we contain prompt injection by architecture, not by asking the model nicely to ignore it. 🔒

His result: the injection risk was contained rather than filtered away, model calls logged for review, and the rebuild delivered in 4 business days. 🚀

👉 See if your AI feature can be manipulated by what it reads: [Link to article]

#PromptInjection #AISecurity #SaaS #IndieHacker #LaunchStudio #Manifera
