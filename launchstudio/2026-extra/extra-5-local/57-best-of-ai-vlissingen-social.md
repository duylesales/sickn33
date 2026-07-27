⚓ Joost Dekker built PortWatch, a berth-scheduling and vessel-tracking tool for shipping agents in Vlissingen's port, and picked Cursor after reading several "best of AI" comparisons ranking it high for code quality. Good choice — except his own database left vessel schedules and agent contact details readable by any logged-in user, regardless of which agency they belonged to. 😳

Ranking articles measure which tool is fun to try, not which output is safe to launch. 🧠

❌ Missing row-level security let any shipping agency see every other agency's data
❌ No rate limiting — one agent's system could overwhelm shared scheduling endpoints for everyone
❌ Schedule updates were trusted from the frontend instead of validated server-side
❌ None of this was about Cursor being the wrong tool — it was what happened after

✅ Row-level security fixed so each agency sees only its own data
✅ Rate limiting added to protect shared scheduling endpoints
✅ Server-side validation added on every schedule update

At **LaunchStudio**, we pick up exactly where the "best of AI" rankings stop — agnostic to which tool built the frontend, backed by Manifera's 120+ engineers across Amsterdam, Singapore, and Ho Chi Minh City. 🛡️

His result: PortWatch now serves multiple shipping agents with properly isolated data and stable performance under real port-scheduling load. 🚀

👉 Picked your AI tool already? Now let's check what actually shipped: [Link to article]

#AINativeFounder #LaunchStudio #Manifera #BestOfAI #Vlissingen
