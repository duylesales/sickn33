🚨 Tim Schouten bouwde Offertetracker in v0 met Supabase: een tool voor de offertepijplijn van verkoopteams bij installatiebedrijven. Klanten vroegen om uitnodigingen voor teams, rollen en inloggen met Microsoft. De organisatiefuncties van Clerk leken compleet, dus Tim begon het te integreren - en liep vast. Elke RLS-policy gebruikte gebruikers-ID's van Supabase, en de helft van zijn tabellen verwees naar auth.users. 😳

Clerk leek de snelle route. Blijven bij wat zijn database al begreep, bleek sneller. Dit had overstappen betekend:

❌ Elke RLS-policy herschrijven zodat die gebruikers-ID's van Clerk leest
❌ Gebruikers migreren en ID's omzetten in de helft van zijn tabellen
❌ Een tweede gebruikerstabel die gesynchroniseerd moet blijven
❌ Nog een verwerker uit de VS voor Nederlandse klanten die de voorkeur gaven aan minder

✅ Gebleven bij Supabase Auth, met inloggen via Microsoft (Azure) toegevoegd
✅ Organisaties, lidmaatschappen en uitnodigingen met verlopende tokens
✅ De rollen eigenaar, manager en verkoop afgedwongen in RLS
✅ MFA ingeschakeld voor managers

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring met Supabase Auth, Auth0, Firebase Auth en NextAuth, helpen we oprichters voorkomen dat ze van authenticatiesysteem wisselen voor functies die eenvoudig te bouwen zijn. 🛠️

💡 Het resultaat: €3.800, tien werkdagen. Tim leverde de teamfuncties in twee weken op, zonder migratie van gebruikers en zonder nieuwe leverancier, en zijn lijst van verwerkers voor klanten bleef kort. 🚀

👉 Supabase Auth of Clerk voor uw AI-gebouwde app? Dit is de vergelijking die ertoe doet: https://launchstudio.eu/nl/blog/supabase-auth-vs-clerk-for-ai-built-apps

#Supabase #Clerk #Authenticatie #B2B #LaunchStudio #Manifera
