🍽️ Martijn Koster heeft vanuit Den Bosch een SaaS voor cateraars bij evenementen, gebouwd met Bolt en Supabase: cateraars beheren menu's, offertes en personeelsroosters. Vóór een lancering met een landelijke cateringvereniging huurde hij een week een DevOps-contractor in. Het werk was uitstekend: een pipeline in GitHub, gescheiden staging en productie, uptimemonitoring en gestructureerde logs. 👌

Twee weken vóór de lancering filterde een cateraar in de pilot de lijst met offertes en zag hij offertes van een ander bedrijf. De review liet zien dat de applicatie nooit was gecontroleerd: 🧠

❌ Tabellen voor offertes en menu's leesbaar voor elke ingelogde gebruiker
❌ Telefoonnummers van personeel blootgesteld via een view zonder policies
❌ Aanbetalingen via Mollie als betaald gemarkeerd op de redirectpagina
❌ Pdf's van offertes in een openbare bucket, en geen e-mailauthenticatie

✅ Policies herschreven per cateraar en rol, met tests in de pipeline van de contractor
✅ De view beveiligd
✅ Aanbetalingen overgezet op geverifieerde webhooks, met afstemming
✅ Pdf's in privéopslag en e-mailauthenticatie toegevoegd

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring met DevOps- en applicatie-engineering voor klanten zoals Vodafone en TNO, dekken we de applicatie en de oplevering eromheen, en werken we samen met DevOps-specialisten als u eigen infrastructuur nodig heeft. 🛠️

💡 Het resultaat: €2.400, zes werkdagen. De vereniging lanceerde volgens planning met zo'n 60 cateraars, en de pipeline draait nu bij elke wijziging de toegangstests. 🚀

👉 Lanceringspartner versus DevOps-contractor: https://launchstudio.eu/nl/blog/production-launch-partner-vs-devops-contractor

#DevOps #Beveiliging #Bolt #Supabase #AIFounder #LaunchStudio #Manifera
