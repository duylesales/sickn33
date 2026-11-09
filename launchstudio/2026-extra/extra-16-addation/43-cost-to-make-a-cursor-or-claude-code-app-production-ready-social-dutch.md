🍽️ Floor Bakker heeft vanuit Utrecht een SaaS voor werving in de horeca, in acht maanden gebouwd met Cursor en later Claude Code op Next.js, Supabase en Stripe. Zo'n 300 bedrijven en 4.000 werkers gebruikten het. Maar het aantal bugs nam toe, en Floor durfde bepaalde bestanden niet meer aan te raken. 😰

De review liet zien hoe acht maanden aan sessies uit elkaar waren gegroeid: 🧠

❌ Drie manieren om in te loggen: Supabase Auth, een eigen sessiesysteem en een oude route met magic links
❌ API-routes die het inloggen controleerden, maar niet of een dienst bij het bedrijf van de gebruiker hoorde
❌ Twee Stripe-sleutels in een gecommit script, en 140 dependencies waarvan zo'n 30 ongebruikt
❌ Geen tests, en deployments vanaf de laptop van Floor

✅ Authenticatie geconsolideerd op Supabase Auth, de oude route verwijderd en eigendomscontroles op elke API-route
✅ Sleutels geroteerd, naar omgevingsvariabelen verplaatst en de geschiedenis van de repository opgeschoond
✅ Ongebruikte dependencies verwijderd, en tests voor inloggen, toegang tussen bedrijven, reacties en Stripe-webhooks
✅ Een pipeline in GitHub naar Vercel met migraties, plus projectregels voor zowel Cursor als Claude Code

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring met het onderhouden van grote codebases voor klanten zoals Vodafone en TNO, consolideren we door AI gegenereerde code in plaats van die te herschrijven. 🛠️

💡 Het resultaat: €3.400, negen werkdagen. Minder bugmeldingen, builds ongeveer een derde sneller en tests die twee wijzigingen blokkeerden die de toegang zouden breken. 🚀

👉 Wat kost het om een app uit Cursor of Claude Code productierijp te maken: https://launchstudio.eu/nl/blog/cost-to-make-a-cursor-or-claude-code-app-production-ready

#Cursor #ClaudeCode #NextJS #Supabase #AIFounder #LaunchStudio #Manifera
