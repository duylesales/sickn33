😬 Mark Souren built PensioPortal — a tool helping small employers explain employee pension contribution statements — using Lovable over two and a half weeks. During a pilot, an HR staff member testing it changed a numeric ID in the browser address bar and pulled up a different employee's full pension history, name, and salary band. 😳

Lovable built good-looking pages. Nothing checked if you were allowed to view the record. 🧠

❌ No server-side authorization check confirming the logged-in user could view the requested record
❌ Functional, polished pages that looked secure but weren't
❌ The gap was invisible until someone changed one number in a URL
❌ The founder assumed "security" was something Lovable already handled

✅ Implement proper server-side authorization checks on every record-level endpoint
✅ Add structured audit logging so any access attempt is traceable
✅ Run a broader review confirming no other endpoints share the same flaw

At **LaunchStudio**, backed by Manifera — trusted by Vodafone, TNO, and CFLW Cyber Strategies for security-focused engineering — we schedule this exact review as a planned pre-launch step, not a reaction to an incident. 🛡️

PensioPortal's result: it relaunched with verified access controls and has since passed two employer security reviews without a follow-up question. 🚀

👉 Handling sensitive data with an AI-built app? Have the security conversation before launch, not after: [Link to article]

#AINativeFounder #LaunchStudio #Manifera #AISecurityRisk #Heerlen
