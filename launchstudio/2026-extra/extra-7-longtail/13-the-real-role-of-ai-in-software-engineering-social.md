🚨 Thijs Overkamp built "Uurlijst," a time-tracking tool for freelancers, in Lovable over one rainy weekend in Nijmegen — and it worked exactly as he'd asked. What he never thought to ask: what happens when a freelancer edits a logged hour after that week's invoice has already gone out. 😳

An AI tool builds what you describe. Not the edge case you never knew to describe. 🧠

❌ Editing an hour after invoicing left the invoice total silently unchanged, creating a mismatch between what the app showed and what was actually billed
❌ It wasn't a crash — just a quiet, compounding accuracy bug no demo would ever have caught
❌ Freelancers could also log hours with a future timestamp, letting a week's summary include time that hadn't happened yet

✅ Rebuilt the invoicing logic so edits after generation trigger a recalculation flag instead of silently going stale
✅ Added a locking mechanism so a finalized invoice can't be edited without an explicit override
✅ Added a server-side check rejecting future-timestamped hours, plus automated tests for the exact edit-after-invoice sequence

At **LaunchStudio**, catching the business logic an AI tool was never explicitly told to enforce is standard practice — the same rigor Manifera's engineers, including the team on Pho Quang Street in Ho Chi Minh City, bring to every review. 🛡️

Thijs's result: an invoicing flow that now catches the exact scenario he "hadn't even thought about" testing — because why would he have tested it on himself? 🚀

👉 Curious what part of "software engineering" your AI tool actually skipped? Read the five-step breakdown: [Link to article]

#AINativeFounder #LaunchStudio #Manifera #LovableAI #SoftwareEngineering
