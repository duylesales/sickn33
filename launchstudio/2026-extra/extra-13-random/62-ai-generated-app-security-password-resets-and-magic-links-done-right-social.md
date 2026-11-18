🧮 The math of a six-digit login code

1,000,000 possible codes
× valid for 24 hours
× no limit on attempts
+ one simple script
= into a test account within an afternoon

That's what a security-minded client of Poetsplan found. 🧹

Tijmen Boersma runs a commercial cleaning company in Almelo and built Poetsplan with Cursor: a scheduling SaaS where planners assign cleaners to office buildings, and clients see completed rounds and building access notes, alarm codes included. Twenty-two cleaning companies in Twente used it. Tijmen had asked Cursor for "passwordless login with a code by email." He got convenience, and a lock with six digits and unlimited guesses.

The review found more in the reset flow:
• Reset links built from the request's host header
• Tokens stored in plain text
• A password reset that didn't end other sessions
• A login form that said "unknown email" for non-customers

The new math (LaunchStudio, 4 business days, €1,150):

Supabase Auth's built-in flows, instead of custom code
× 10-minute expiry
× single-use, hashed tokens, with a confirmation step that survives email scanners
× rate limits per email and per IP, with attempt lockouts
+ reset URLs from a configured base URL
+ every session revoked on a password change, with a notification email
+ unified error messages
+ sending from an authenticated domain
+ alarm codes restricted to the planner role
= no way in

The client's follow-up test found exactly that, and Poetsplan passed that client's supplier security check. It has since grown to 35 cleaning companies.

"I asked for convenience and got a lock with six digits and unlimited guesses. The fix was mostly using what my auth provider already did properly." - Tijmen Boersma

https://launchstudio.eu/en/blog/ai-generated-app-security-password-resets-and-magic-links-done-right

#Authentication #AppSecurity #Supabase #Cursor #LaunchStudio #Manifera
