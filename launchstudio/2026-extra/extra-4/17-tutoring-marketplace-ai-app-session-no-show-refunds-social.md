🚨 A tutor simply didn't join a scheduled video session. The student had already been charged at booking. The app marked the session "completed" once the scheduled time passed and released payment to the tutor as normal — because a refund path for this exact scenario didn't exist. Not a missing button. A missing code path. 😳

Everyone tests what happens when the paying customer doesn't show up. Almost nobody tests the opposite — what happens when the person getting paid is the no-show. 🧠

❌ Lovable built the student no-show policy exactly as described — charge the student, no refund inside the cancellation window — and nothing else
❌ The tutor no-show path routed through the same logic as a normal completed session, releasing payment as if the lesson happened
❌ A complete no-show policy needs four distinct outcomes; most AI-generated builds cleanly handle exactly one
❌ In a tutoring marketplace, trust is the entire product — parents booking for kids, students on exam deadlines — and a full charge with no recourse is the fastest way to turn a customer into a public complaint

✅ Treat no-show handling as a state machine with a defined outcome for each of the four scenarios, not one flag applied uniformly
✅ Give the tutor no-show path its own trigger — a student or admin-confirmable report — that routes to an automatic refund hold
✅ Adjust payment-release timing so funds aren't released until session completion is actually confirmed or a timeout passes

At **LaunchStudio**, we build this as an explicit rules layer on top of your existing Stripe integration, so payment logic reflects what actually happened in the session — not a default assumption it went fine. 🛡️

Sanne's result: tutor no-shows now trigger an automatic refund path instead of silently completing as a paid session, closing the exact gap that had gone untested. 🚀

👉 Running a two-sided booking marketplace? Describe your project and we'll respond within one business day: [Link to article]

#AINativeFounder #LaunchStudio #Manifera #EdTech #Marketplace
