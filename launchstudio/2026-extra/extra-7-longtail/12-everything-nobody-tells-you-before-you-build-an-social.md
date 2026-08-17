🚨 Nina Callens built "RouteMate," a route optimization tool for delivery businesses, using Cursor — solid working logic, but no rate limiting on the API, session tokens that never expired, and a Stripe integration she'd stubbed out but never finished. 😬

Two freelancer quotes later, neither one could actually explain what was wrong. 🧠

❌ No rate limiting on the route-calculation API
❌ Session tokens that never expired, no matter how long a user stayed idle
❌ A payment flow wired halfway to Stripe and left unfinished
❌ Her optimization algorithm called a third-party mapping API using a key exposed right in the frontend bundle — anyone could copy it and run up her bill

✅ Fixed the session expiry logic and added rate limiting to the route-calculation API
✅ Completed the Stripe integration without touching the routing logic Nina had written herself
✅ Rotated the exposed mapping-API key behind a server-side proxy

At **LaunchStudio**, this is exactly the kind of scoped fix we specialize in on top of code you already trust — Manifera's engineers, coordinated through the Singapore team on Tras Street, review AI-generated projects from Cursor, Bolt, Lovable, and v0 regularly, so diagnosis is fast. 🛡️

Nina's result: a specific, written list of exactly what had actually been wrong — something neither of her two freelancer quotes had been able to produce upfront. 🚀

👉 Comparing DIY, freelancer, agency, or a specialist for your AI-built app? Read the honest breakdown: [Link to article]

#AINativeFounder #LaunchStudio #Manifera #CursorAI #IndieHacker
