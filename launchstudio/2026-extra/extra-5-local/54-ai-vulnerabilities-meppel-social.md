🚂 Femke Bosman built RailDock, a freight scheduling and carrier-matching platform for transport companies around Meppel, using v0 across three weeks of evenings — and a routine pre-launch review found that its payment webhook never verified requests actually came from Stripe. Anyone who guessed the URL could fake a "payment succeeded" event. 😳

She'd tested her checkout flow fifty times. It always worked. That's exactly the problem. 🧠

❌ Webhook endpoint accepted unsigned requests — a fake "paid" event could book freight for free
❌ Role-based access (carriers vs. shippers) was only enforced in the UI, never on the backend
❌ Both flows worked flawlessly in her own testing, which is why she never suspected them
❌ "Always works for me" and "can't be faked by someone else" turned out to be two different things

✅ Signature verification added to every incoming webhook request
✅ Role-based access enforced server-side, not just hidden in the UI
✅ Full pre-launch review before real bookings and deposits went live

At **LaunchStudio**, this is exactly the class of AI vulnerabilities our engineers audit for before launch, drawing on Manifera's decade-plus building integration-heavy systems. 🛡️

Her result: RailDock launched with verified payment handling and correctly isolated carrier data, closing a hole that would have let anyone book freight for free. 🚀

👉 Processing real payments through an AI-built app? Get the webhook layer audited first: [Link to article]

#AINativeFounder #LaunchStudio #Manifera #AIVulnerabilities #Meppel
