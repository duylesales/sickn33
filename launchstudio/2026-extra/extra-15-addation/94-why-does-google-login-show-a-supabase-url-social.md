Which sign-in screen would you trust? 🔐

A: "continue to xptlqmvhrzke.supabase.co"
B: "Sign in to Verlofzaken", with the company logo

Two IT contacts at prospective customers picked neither, and paused their trials. One wrote that screen A "looked exactly like a phishing test."

Screen A was real. Jasper Mulder built Verlofzaken with Lovable and Supabase: leave and absence management for companies of 20 to 150 employees, where employees request time off and managers approve it. Sign-up ran through Google Workspace accounts. And analytics showed that about a quarter of people who clicked "Sign in with Google" never finished.

What sat behind screen A:
• The consent screen still in testing mode, with a default name
• A privacy policy that was a Google Doc link
• Supabase redirect URLs covering only the preview domain and production, so staging sign-ins landed on the live app

How screen B was built (LaunchStudio, 7 business days including Google's review, €1,600):
✓ Privacy policy and terms moved to Jasper's own domain, and the domain verified in Search Console
✓ The consent screen set up with the Verlofzaken name, logo and authorised domains, then submitted for branding verification, approved in four business days
✓ A Supabase custom domain, auth.verlofzaken.nl, with DNS records and a new Google callback, while the old callback stayed active for two weeks
✓ Redirect URLs set per environment
✓ Authentication emails rebranded, sent from an address on the company domain

Completed Google sign-ups rose from about 75% to 93% of attempts. Both paused prospects came back, and became customers after their IT contacts reviewed the new setup.

"I lost deals because of one screen I'd never really looked at. Now the first thing customers see is my brand, not a random address." - Jasper Mulder

https://launchstudio.eu/en/blog/why-does-google-login-show-a-supabase-url

#GoogleLogin #OAuth #Supabase #B2BSaaS #AIFounder #LaunchStudio #Manifera
