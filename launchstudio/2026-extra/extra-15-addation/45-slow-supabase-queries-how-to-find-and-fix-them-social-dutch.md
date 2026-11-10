🚨 Wessel Hofman bouwde Storingsboek met Lovable en Supabase: onderhoudsbedrijven registreren reparatieverzoeken, wijzen monteurs toe en volgen werkorders. Zijn grootste klant kwam op zo'n 180.000 werkorders - en het hoofddashboard deed er negen seconden over om te laden. 😳

Monteurs zeiden dat hun mobiele opdrachtenlijst nauwelijks bruikbaar was. Wessel stond op het punt Supabase de schuld te geven. Zo vindt en repareert u trage Supabase-queries: 🧠

❌ Alle open werkorders met elke kolom geladen, gefilterd in JavaScript
❌ Aparte requests per werkorder voor monteur en object
❌ Een RLS-policy die per rij teamlidmaatschap opvroeg, zonder index
❌ Geen indexen op de belangrijkste filters, en zoeken met ilike '%term%'

✅ Samengestelde indexen voor veelgebruikte filters en sorteringen
✅ Een herschreven policy met (select auth.uid()) en een geïndexeerde lidmaatschapscheck
✅ Een view met alleen de nodige kolommen, gekoppelde namen en keyset-paginering
✅ Tellingen per status uit een door triggers bijgewerkte tabel en trigram-zoeken, getest op productieschaal

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring in productie-engineering, zorgen we dat uw app de database niet honderden keren hetzelfde werk laat doen. 🛠️

💡 Het resultaat: €3.100, 8 werkdagen. Het dashboard laadt in zo'n 400 milliseconden, mobiele lijsten in minder dan een halve seconde, en het CPU-gebruik van de database halveerde ruim. 🚀

👉 Wordt uw Supabase-app trager? Zo vindt en repareert u trage queries: https://launchstudio.eu/nl/blog/slow-supabase-queries-how-to-find-and-fix-them

#Supabase #Postgres #Performance #PropTech #AIFounder #LaunchStudio #Manifera
