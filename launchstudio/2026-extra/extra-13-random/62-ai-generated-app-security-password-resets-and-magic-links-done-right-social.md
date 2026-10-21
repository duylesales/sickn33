🚨 Tijmen Boersma runs a commercial cleaning company in Almelo and built Poetsplan with Cursor: planners assign cleaners to office buildings, and clients see completed rounds and building access notes — including alarm codes. 22 cleaning companies in Twente used it. Then a security-minded client guessed his way into a test account in one afternoon with a simple script. 😳

Tijmen had asked Cursor for "passwordless login with a code by email". He got a six-digit code, valid for 24 hours, with unlimited attempts. The separate reset flow built its link from the request's host header, tokens were stored in plain text, a reset didn't end other sessions, and the login form told non-customers "unknown email". Here's how to get password resets and magic links right in an AI-built app: 🧠

❌ Six-digit codes with unlimited guesses
❌ Reset links built from the request host
❌ Tokens stored in plain text and never invalidated
❌ Sessions that survive a password change

✅ Custom login and reset replaced by Supabase Auth's built-in flows
✅ Ten-minute expiry, single-use hashed tokens and a confirmation step that survives email scanners
✅ Rate limits per email and IP with lockouts, and reset URLs fixed to a configured base URL
✅ All sessions revoked on password change with a notification email, unified messages, an authenticated sending domain — and alarm codes limited to planners

At **LaunchStudio**, backed by Manifera's 11+ years of production engineering and its cybersecurity roots, we check the second door into every account — not just the front one. ⚙️

His result: €1,150, four business days. The client's follow-up test found no way in, Poetsplan passed that client's supplier security check, and it has since grown to 35 cleaning companies. 🚀

👉 AI generated app security: password resets and magic links done right: https://launchstudio.eu/en/blog/ai-generated-app-security-password-resets-and-magic-links-done-right

#Authentication #AppSecurity #Supabase #Cursor #LaunchStudio #Manifera
