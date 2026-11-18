🔻 THE FUNNEL THAT LEAKED

Clicks on "Probeer gratis": hundreds a month
⬇
Confirmed accounts: a few dozen
⬇
Conversion: about 11%

Charlotte Verbeek, a former HR consultant in Utrecht, launched Verlofwijzer, a leave planning tool for small companies. Her Framer marketing site was beautiful and ranked well for several Dutch HR terms. The product, built in Lovable, ran on a preview URL behind the site's sign-up button.

She tested it herself on a phone and found the leaks:
💧 Confirmation emails linked to an old preview address that no longer worked
💧 Google sign-in showed an unfamiliar app name and a warning
💧 The login page appeared in Google above her pricing page
💧 Analytics stopped at the button click
💧 The app used a different font and colour scheme from the site

Each tool worked fine on its own. The leaks were in the gaps between them.

The fix (LaunchStudio, 5 business days, €1,650):
🔧 The app moved to app.verlofwijzer.nl on Vercel, with the DNS record added next to Framer's and email settings left untouched
🔧 Supabase Auth redirect URLs and site URL updated, preview entries removed
🔧 The Google OAuth consent screen set up with the right name and logo
🔧 noindex on app routes, analytics unified across both domains with sign-up and activation events, consent shared across subdomains
🔧 The app restyled with the Framer site's design tokens

THE FUNNEL AFTER, first full month:
Sign-up clicks to confirmed accounts: about 46%
The login page dropped out of search results within weeks, and Charlotte can finally see which LinkedIn posts bring in paying customers.

"Each tool worked perfectly on its own. The leak was in the space between them, and I would never have found it myself." - Charlotte Verbeek

https://launchstudio.eu/en/blog/webflow-or-framer-site-with-an-ai-built-app-domains-auth-and-seo

#Framer #Webflow #Lovable #SEO #AIFounder #LaunchStudio #Manifera
