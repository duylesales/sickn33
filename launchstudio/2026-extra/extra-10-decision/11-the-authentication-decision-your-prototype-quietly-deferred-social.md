🚨 Tomasz deleted a fired manager from Supabase and told the owner "done." Thirty days later, the manager's browser was still logged in. 😳

Deleting a user feels like revoking access — until you learn what a signed JWT actually promises: 🧠

❌ The token sat in `localStorage` with a 30-day expiry and zero refresh rotation — Bolt picked that, nobody chose it
❌ Deleting the Supabase user record does nothing to a token that's already signed and handed out
❌ "We'll add roles later" usually means rewriting authorization across every route, not extending one central check
❌ A specific "email already registered" error on signup hands attackers a free list of who has an account

✅ Move the token into an httpOnly, Secure cookie so one XSS bug can't leak every logged-in session at once
✅ Cut access tokens to 20 minutes, backed by a genuinely revocable refresh token
✅ Add a `role` column on day one, even with one value — retrofitting later means auditing forty-plus endpoints
✅ Make logout a real server-side revoke, not just clearing a browser's local storage

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we harden the auth model underneath your login screen without touching the UI your AI tool built. 🔐

His result: Rotaflow can now kill any account's access within 20 minutes worst case instead of 30 days, and adding a read-only accountant role next quarter is a one-line addition instead of an audit of every route. 🚀

👉 Find out what your auth model is actually doing: https://launchstudio.eu/en/blog/the-authentication-decision-your-prototype-quietly-deferred

#IndieHacker #AICoding #ProductionReady #SaaS #LaunchStudio #Manifera
