🎟️ Wouter Zijlstra built EilandGo — a ferry ticket booking platform for tourists heading from Harlingen to the Wadden Islands — in Bolt, launching ahead of summer tourist season. Ticket numbers were simple, sequentially generated (1001, 1002, 1003...). Anyone could predict a valid, unused ticket number just by incrementing from a real one — meaning a fraudulent boarding pass could be generated without ever paying. 😳

Security isn't pass/fail. It's dozens of small decisions an AI tool made without asking — and predictable IDs are one of the most common. 🧠

❌ Ticket numbers generated as simple incrementing values, not cryptographically random
❌ Anyone could guess a valid, unused ticket number in seconds
❌ No server-side check against the actual payment record at boarding
❌ The risk looked harmless in every demo — it only mattered once real tickets and real money were involved

✅ Replaced sequential ticket IDs with cryptographically random, unpredictable identifiers
✅ Added server-side verification against the actual payment record at the point of boarding
✅ Closed the gap before the first full tourist season began

At **LaunchStudio**, this is exactly the kind of structured risk assessment Manifera's engineers — 160+ projects delivered for clients like Vodafone and TNO — run on founder prototypes. 🛡️

His result: EilandGo now issues tickets that can't be predicted or forged, verified against real payment records at boarding. 🚀

👉 Check your own app's ticket, order, or booking IDs today — can you guess the next one? Explore LaunchStudio's approach: [Link to article]

#AINativeFounder #LaunchStudio #Manifera #AISecurityRisk #Harlingen
