🚨 Quinten built FactuurFlow, an invoicing tool for freelancers, on Lovable — then found out it was invoicing its own subscribers wrong. Every customer, no matter which EU country they signed up from, got charged Dutch VAT. His own bookkeeper caught it during a routine review. 🧾

🧠 "It calculates tax" and "it calculates tax correctly" are two very different claims — and EU VAT doesn't run on one number.

❌ The AI-generated billing logic had only ever been given one rate: the founder's own country
❌ EU digital services VAT is charged at the buyer's country rate, not the seller's — this stayed invisible while customers were mostly Dutch
❌ It surfaced only once Belgian and German freelancers signed up and their invoices didn't match what their own accountants expected
❌ A full quarter of cross-border invoices had to be reissued once the bug was found

✅ Determine customer location from two independent signals — IP address and billing address
✅ Pull the correct rate automatically from an auto-updating EU rate table, and validate VAT numbers via VIES for B2B reverse charge
✅ Regenerate every affected historical invoice with the correct line items and legal basis

At **LaunchStudio**, we treat VAT determination as a structured checklist, not guesswork — built on Manifera's 11+ years shipping billing and compliance systems for clients like Vodafone. 🛡️

His result: FactuurFlow now bills correctly across every EU country it operates in, with an audit trail an accountant can actually sign off on. 🚀

👉 Selling across EU borders? Get your billing logic reviewed before the next quarterly filing: [Link to article]

#AINativeFounder #LaunchStudio #Manifera #EUVAT #SaaSFounder
