🚨 Sem Evers, a facility coordinator turned founder in IJsselstein, built Zaalvrij with Cursor: companies in shared office buildings book meeting rooms, manage visitors and get monthly usage invoices. 26 companies across four buildings - often on shared reception computers. Then a receptionist reported that after logging out, the browser's back button showed another company's bookings. And clicking around still worked. 😳

Cursor had built JWT auth with tokens in localStorage, valid for 30 days, and logout just deleted the token from the browser - a copied token kept working. "Remember me" cookies lacked HttpOnly and SameSite, booking-cancellation forms had no CSRF protection, password changes didn't end other sessions, and a reflected XSS in the visitor name field could have read the token. Here's AI-generated app security before and after fixing sessions and cookies: 🧠

❌ Tokens in localStorage, valid for a month
❌ Logout that only hides the token
❌ Cookies without HttpOnly or SameSite, and no CSRF protection
❌ Sessions that survive a password change

✅ Custom JWT handling replaced by Supabase Auth sessions
✅ Refresh tokens in HttpOnly, Secure, SameSite=Lax cookies and shorter access-token lifetimes
✅ Server-side invalidation on logout and password change, plus an eight-hour idle timeout for shared-computer accounts
✅ CSRF tokens on state-changing forms, the XSS fixed with output escaping and a Content Security Policy - and "log out everywhere"

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering and its cybersecurity roots, we make sure your logout button ends the session for real. ⚙️

His result: €1,100, four business days. The shared-computer problem disappeared, a larger tenant's security questionnaire was answered with no follow-up questions, and Zaalvrij was adopted in two more office buildings. 🚀

👉 AI generated app security: before and after sessions and cookie settings: https://launchstudio.eu/en/blog/ai-generated-app-security-before-and-after-sessions-and-cookie-settings

#SessionSecurity #Cookies #CSRF #Cursor #LaunchStudio #Manifera
