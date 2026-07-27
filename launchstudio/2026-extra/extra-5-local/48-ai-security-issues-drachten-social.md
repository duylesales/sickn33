🏭 Sietse Postma built ShiftHub — a shift-scheduling app for manufacturing employers around Drachten — in v0, piloting it with his own former employer. What he didn't know: a user's role was read directly from a value sent by the browser instead of verified against the database. Any regular employee could edit a request and grant themselves manager-level access to coworkers' shift and pay data. 😳

If your AI-built app decides who's an "admin" based on what the browser says, that's not a role check — that's an honor system. 🧠

❌ User role read from client-sent data instead of verified server-side
❌ Any employee could modify a request to escalate to manager-level access
❌ Payroll-adjacent shift data exposed to anyone who knew how to edit a form field
❌ The gap was invisible from the founder's own point of view — the app "worked" fine

✅ Rebuilt authorization so every role check happens server-side against verified account data
✅ Removed all reliance on anything the client sends
✅ Added logging to flag any future privilege-escalation attempt

At **LaunchStudio**, this exact pattern — trusting client-sent data — is the single most common issue our 160+-project engineering team finds in founder prototypes. 🛡️

His result: ShiftHub now enforces role-based access entirely server-side, closing the escalation path before it reached any live manufacturing client. 🚀

👉 Run a ten-minute self-check on your own app, then let us verify the rest: [Link to article]

#AINativeFounder #LaunchStudio #Manifera #AISecurityIssues #Drachten
