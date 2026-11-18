🏨 Imagine checking out of a hotel, handing in your key card, and the card still opens your room for the next 30 days.

Copies of it too.

That's roughly how logout worked in Zaalvrij.

Sem Evers, a facility coordinator turned founder in IJsselstein, built Zaalvrij with Cursor: companies in shared office buildings book meeting rooms, manage visitors and get monthly usage invoices. Twenty-six companies across four buildings, often using shared reception computers. Then a receptionist reported that after logging out, pressing the browser's back button showed another company's bookings. And clicking around still worked.

The key card, examined:
🔑 JWT tokens stored in localStorage, valid for 30 days
🔑 Logout only removed the token from the browser. It never invalidated it. A copied token kept working.
🔑 "Remember me" cookies without HttpOnly or SameSite flags
🔑 No CSRF protection on the forms that cancel bookings
🔑 Changing your password didn't end your other sessions
🔑 A reflected XSS in the visitor name field, meaning a crafted link could have read the token from localStorage

A front desk that actually deactivates keys (LaunchStudio, 4 business days, €1,100):
✓ Custom JWT handling replaced with Supabase Auth sessions
✓ Refresh tokens in HttpOnly, Secure, SameSite=Lax cookies, with shorter access token lifetimes
✓ Sessions invalidated on the server at logout and on password change
✓ An eight-hour idle timeout for accounts flagged as shared-computer use
✓ CSRF tokens on every state-changing form
✓ The XSS fixed, with output escaping and a Content Security Policy
✓ A "log out everywhere" button

The shared-computer issue disappeared. A later security questionnaire from a larger tenant was answered without follow-up questions. And Zaalvrij has since moved into two more office buildings.

"Our logout button was a polite suggestion. Now it actually ends the session." - Sem Evers

https://launchstudio.eu/en/blog/ai-generated-app-security-before-and-after-sessions-and-cookie-settings

#SessionSecurity #Cookies #CSRF #Cursor #LaunchStudio #Manifera
