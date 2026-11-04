🚨 Joost Hermsen bouwde Montagebon in Lovable: digitale werkbonnen voor installatiebedrijven. Na een audit was zijn Row Level Security hersteld, waren sleutels naar de server verplaatst en liepen betalingen via webhooks. Een week later meldde een klant dat hij de werkbonnen van een ander bedrijf zag. 😳

De audit had zijn app hersteld. Eén onschuldige prompt brak hem weer. Dit gebeurde er:

❌ Hij vroeg Lovable om "ervoor te zorgen dat monteurs werkbonnen kunnen zien die door elke planner zijn toegewezen"
❌ Lovable voegde een nieuwe policy toe die elke ingelogde gebruiker leestoegang gaf tot de tabel met werkbonnen
❌ Postgres combineert permissive policies met OR - dus die ene policy hief alle correcte policies op
❌ Geen regels, geen review van migraties en geen test die het opving voordat klanten het deden

✅ De ruime policy verwijderd, en projectregels toegevoegd die het wijzigen van policies verbieden
✅ De logica voor het toewijzen van monteurs verplaatst naar een databasefunctie, buiten bereik van gegenereerde componenten
✅ Een Playwright-test die bij elke deployment de zichtbaarheid tussen bedrijven controleert
✅ Een GitHub-melding bij elke wijziging in supabase/migrations

Bij **LaunchStudio**, ondersteund door Manifera - waarvan oprichter Herre Roelevink uit de cybersecurity komt - richten we vangrails in zodat u kunt blijven prompten zonder uw beveiliging ongedaan te maken. 🛠️

💡 Het resultaat: €1.300, vier werkdagen. Joost bleef bouwen in Lovable; de geautomatiseerde test hield één vergelijkbare regressie tegen vóór de deployment, en meldingen over migraties signaleerden nog twee riskante voorstellen voordat hij ze accepteerde. 🚀

👉 Bang dat de volgende prompt uw beveiligingsoplossingen ongedaan maakt? Dit zijn de vijf vangrails die ze laten standhouden: https://launchstudio.eu/nl/blog/how-do-i-stop-lovable-prompts-from-breaking-security

#Lovable #Supabase #RLS #AppSecurity #LaunchStudio #Manifera
