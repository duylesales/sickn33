🚨 Huurbeheer van Pieter Blom beheert zo'n 2.300 huurwoningen voor negen verhuurbemiddelaars rond Dordrecht. De lijst met panden was netjes gefilterd. Maar één cijfer op het dashboard — "totaal aantal eenheden in beheer" — telde de hele tabel. Een bemiddelaar zag een getal dat veel groter was dan de eigen portefeuille en begreep wat dat betekende. 😳

Ook de huurachterstand en de gemiddelde huur waren ongefilterd, waardoor elke bemiddelaar de cijfers van zijn concurrenten kon zien. Hier lekt multi-tenancy werkelijk:

❌ Gegevens in eigendom van de gebruiker die ze aanmaakte, in plaats van de organisatie
❌ Gedeelde logins tussen collega's, omdat dat de enige manier was om elkaars werk te zien
❌ Dashboardtotalen en rapportages zonder tenantfilter
❌ Server-side queries met verhoogde rechten die de tenantcontrole overslaan

✅ Een organisatiemodel met rollen voor medewerker, manager en eigenaar
✅ Een verplichte tenantkolom in elke tabel, met policies per bewerking
✅ Elk cijfer en elke rapportage herschreven met een expliciet tenantfilter — en getest
✅ Goede uitnodigings- en eigendomsflows, zodat gedeelde logins persoonlijke accounts worden

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring in productie-engineering, bouwen we een tenantscheiding die u aan een koper kunt aantonen. 🏢

💡 Het resultaat: in twaalf werkdagen en voor € 6.800 werden de gedeelde logins 31 persoonlijke accounts en drie ongefilterde serverqueries hersteld. Twee bemiddelaars die een alternatief overwogen, bleven — en Pieter stuurt nu bij elk voorstel een beschrijving van één pagina over de scheiding van gegevens. 🚀

👉 Multi-tenancy in Lovable en Supabase zonder datalekken: https://launchstudio.eu/nl/blog/lovable-supabase-multi-tenancy-without-leaking-data

#Lovable #Supabase #MultiTenancy #Vastgoed #LaunchStudio #Manifera
