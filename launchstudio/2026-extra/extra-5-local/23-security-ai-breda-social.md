🚨 Elise van Dongen built TableTuned, a reservation and staff-scheduling tool for restaurants around Breda's Ginnekenmarkt, with Cursor — six restaurants were live within a month. Then a seventh restaurant's manager, just evaluating the tool, changed a reservation ID in the URL out of curiosity and pulled up another restaurant's full guest list, phone numbers included. 😳

He reported it instead of exploiting it. The exposure had been live the entire month. 🧠

❌ No row-level security policy on the reservations table at all — a default Supabase setup never locked down
❌ Any restaurant could see any other restaurant's guests just by changing a URL
❌ The public booking endpoint had no rate limiting
❌ Stripe keys were sitting in client-side code

✅ Implement proper tenant isolation on every reservation record
✅ Add rate limiting to the public booking endpoint
✅ Move payment keys out of the frontend into a secured backend function

At **LaunchStudio**, Manifera's engineers — trusted by Vodafone, TNO, and CFLW Cyber Strategies for security-sensitive work — treat row-level security as a standard pre-launch audit item, not an afterthought. 🛡️

TableTuned's result: it relaunched with verified tenant isolation, and Elise now leads sales conversations with her security audit instead of hoping the topic doesn't come up. 🚀

👉 Handling booking or guest data with an AI-built app? Get the audit before a curious user finds the gap: [Link to article]

#AINativeFounder #LaunchStudio #Manifera #SecurityAudit #Breda
