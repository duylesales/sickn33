🌐 Ines schakelde zelf DNS om, om haar met Bolt gebouwde projectmanagementtool naar een eigen domein te verplaatsen — Google OAuth-login brak voor alle 400 actieve gebruikers binnen 20 minuten.

"Het is gewoon DNS" is de aanname die logins, betalingen en e-mailbezorgbaarheid tegelijk breekt.

❌ OAuth callback-URL's die nog naar het oude domein wijzen op het moment dat DNS omschakelt
❌ Stripe-webhooks te vroeg — of te laat — bijgewerkt, waardoor betalingsbevestigingen stilletjes verloren gaan
❌ SPF/DKIM/DMARC-records nooit geconfigureerd, waardoor wachtwoordresetmails stilletjes bouncen

✅ Een gefaseerde migratie met dual-domain ondersteuning gedurende het volledige DNS-propagatievenster
✅ Webhook- en OAuth-overdracht pas nadat elk geverifieerd werkend is op het nieuwe domein
✅ Oud domein aangehouden als redirect, niet gedeactiveerd, vangt elke resterende bladwijzer en link op

Bij **LaunchStudio** voeren wij precies dit soort zero-downtime migraties al sinds 2014 uit via Manifera, over 160+ opgeleverde projecten. 🛡️

De migratie van Ines werd voltooid zonder inlogfouten, zonder gemiste webhooks, en zonder voor klanten zichtbare downtime. (€ 1.400 — Launch Ready Pakket, gemigreerd en geverifieerd in 5 werkdagen.) 🚀

👉 Bekijk hoe wij het oplosten: [Link naar artikel]

#LaunchStudio #Manifera #AISaaS #ZeroDowntime #Bolt
