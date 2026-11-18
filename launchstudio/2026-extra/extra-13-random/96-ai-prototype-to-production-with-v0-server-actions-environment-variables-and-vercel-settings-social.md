⚙️ ONE LINE IN A CONFIG FILE (illustrative)

NEXT_PUBLIC_STRIPE_SECRET_KEY=sk_live_...

The NEXT_PUBLIC_ prefix means: ship this to every visitor's browser. During a debugging session, the Stripe secret key had been renamed exactly like that. ⚽

Olaf Terlouw, a football club treasurer in Maarssen with a background in web development, built Sportveldhuur with v0: clubs rent unused pitches and training slots to other teams and companies, with online booking and payment. Nine clubs in the Utrecht region used it. Then a renter, who was also a developer, noticed the booking cancellation action accepted any booking ID. He could cancel other teams' bookings.

v0 made the app feel like a set of forms. Under the hood, every form was a public door. The review found:
• Four Server Actions checking only for a logged-in session, not ownership or role
• The Stripe secret key in the browser bundle, via that prefix
• Preview deployments using production environment variables, and reachable by anyone
• A cached club dashboard with revenue figures, briefly shown to another club's treasurer after a deploy

What LaunchStudio changed (8 business days, €2,300):
✓ Ownership and role checks, with Zod validation, in every Server Action
✓ The Stripe key rotated and moved to server-only code
✓ Vercel environment variables split per environment, previews on a staging database, and deployment protection on
✓ Personalised dashboards marked as dynamic, never cached
✓ Pooled EU database connections with Row Level Security
✓ Security headers and monitoring

THE CONFIG FILE, NOW (illustrative)
STRIPE_SECRET_KEY=... (server only, production only)

No more unauthorised cancellations, and no more cross-club data exposure. Sportveldhuur expanded to 16 clubs, and Olaf keeps building new screens in v0, now checked against a checklist before every deploy.

"v0 made the app feel like a set of forms. Under the hood, every form was a public door." - Olaf Terlouw

https://launchstudio.eu/en/blog/ai-prototype-to-production-with-v0-server-actions-environment-variables-and-vercel-settings

#v0 #Vercel #NextJS #ServerActions #LaunchStudio #Manifera
