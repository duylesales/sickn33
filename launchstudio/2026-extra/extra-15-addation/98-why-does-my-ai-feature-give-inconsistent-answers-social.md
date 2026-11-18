🧾 The same kind of receipt, three different answers (illustrative)

Monday: Fuel ➜ Car costs
Wednesday: Fuel ➜ Travel
Friday: Fuel ➜ (nothing saved)

Iris Dekker's users saw exactly this pattern. She built Bonnetjesbak with Lovable and Supabase: freelancers and small businesses photograph receipts, an AI model extracts supplier, date, amount and VAT, and assigns a bookkeeping category. Around 1,300 users relied on it for their quarterly VAT returns. Then the complaints started: inconsistent categories, VAT that didn't add up, and sometimes a receipt saved with no data at all.

Why the answers changed:
• One loose prompt, "read this receipt and return the details," with the code splitting the text answer line by line. If the model added an introduction, every field shifted.
• The model calculated VAT and totals itself, and got it wrong on about one in fifteen receipts with mixed VAT rates
• Categories came from the model's own judgement, with no list of allowed values
• A general model alias had been updated a month earlier, right when the complaints began

Making the answers consistent (LaunchStudio, 9 business days, €3,100):
✓ A structured-output request with a strict schema
✓ A fixed list of categories matching Dutch bookkeeping practice, with examples for tricky cases like fuel, mixed-rate supermarket receipts and foreign suppliers
✓ Every response validated, retried once, then flagged for the user to review instead of saved blank
✓ VAT and totals calculated in code from the extracted line amounts and rates, with a flag when they differ from the printed total
✓ The model version pinned
✓ An evaluation set of 220 anonymised receipts, run before every prompt or model change
✓ One-tap category corrections that feed new examples into the set

Category accuracy on the evaluation set rose from about 81% to 96%. VAT errors went to zero, blank records disappeared, and support messages about wrong receipts fell by over 70% around the busy VAT deadline.

"I thought the AI was the clever part. The reliable part turned out to be everything around it." - Iris Dekker

https://launchstudio.eu/en/blog/why-does-my-ai-feature-give-inconsistent-answers

#LLM #AIEngineering #StructuredOutput #FinTech #AIFounder #LaunchStudio #Manifera
