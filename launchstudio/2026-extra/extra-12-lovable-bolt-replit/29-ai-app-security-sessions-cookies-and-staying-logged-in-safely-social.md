🚨 Roos Verhagen's Zorgplanning schedules shifts and client visits for 18 home care organisations — about 900 carers. A planner left after a disagreement, and her manager deleted her account on her last day. Matter closed. 😳

Three weeks later, shifts were being reassigned overnight and client visits removed. Her tablet was still signed in: a 90-day refresh token that deleting the account never invalidated. Here's how sessions outlive the people who own them: 🧠

❌ Session tokens in local storage, readable by any script on the page
❌ 90-day refresh tokens, with no server-side record of active sessions
❌ Deleting an account didn't end its sessions
❌ Sign-out that briefly showed the previous user's client list

✅ Tokens moved to httpOnly, secure, sameSite cookies with CSRF tokens on changes
✅ A sessions table — and deactivation or password change now ends every session immediately
✅ Sign-out-everywhere for users, force sign-out for organisation admins, and an active-sessions screen
✅ 30-minute access tokens, a 14-day refresh agreed with customers, a 12-hour idle timeout for shared tablets, and session rotation at login

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering, we check where your app keeps its token — two minutes that decide what a future bug costs you. 🔐

Her result: two business days and €2,700 later, the unauthorised changes were reconstructed from the audit trail and corrected. Since then, three organisations have used the active-sessions screen to find tablets left signed in at client locations. 🚀

👉 Sessions, cookies and staying logged in safely: https://launchstudio.eu/en/blog/ai-app-security-sessions-cookies-and-staying-logged-in-safely

#AppSecurity #Authentication #HealthTech #Lovable #LaunchStudio #Manifera
