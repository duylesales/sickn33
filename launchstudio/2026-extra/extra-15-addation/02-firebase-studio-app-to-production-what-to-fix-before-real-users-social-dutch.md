🚨 Ingrid Hoekstra coördineert vrijwilligers voor voedselbanken rond Leeuwarden. In drie weekenden bouwde Firebase Studio Inzetrooster voor haar: vrijwilligers kiezen diensten, coördinatoren zien wie er komt. Twee weken na de start van een pilot met vier locaties waarschuwde een vrijwilliger die in de IT werkte: de gegevens van de app waren leesbaar voor iedereen die het project-ID kende. 😳

De regels waren nog die van het prototype, `if request.auth != null` - dus elke ingelogde vrijwilliger kon het telefoonnummer en adres van elke andere vrijwilliger lezen. Dit moet u repareren voordat echte gebruikers komen: 🧠

❌ Security Rules uit het prototype die persoonsgegevens blootgaven
❌ Een Firestore-database in een Amerikaanse multi-regio
❌ Een AI-herinneringsfunctie zonder limieten aan te roepen
❌ Alle tests op de live database

✅ Een nieuw productieproject met Firestore in europe-west4, pilotdata gemigreerd
✅ Regels die vrijwilligers beperken tot hun eigen profiel en het rooster van hun locatie
✅ App Check afgedwongen, de AI-functie achter authenticatie met een dagquotum, budgetmeldingen
✅ Het oorspronkelijke project omgezet naar staging, met deploys vanuit GitHub

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring in productie-engineering, geven we u het vertrouwen om gegevens van echte mensen in uw app te zetten. 🛠️

💡 Het resultaat: €2.450, 8 werkdagen. Inzetrooster ging opnieuw live op elf voedselbanklocaties, wordt nu gebruikt door zo'n 380 vrijwilligers en de maandelijkse Firebase-kosten blijven onder €25. 🚀

👉 Bouwt u met Firebase Studio? Dit moet u repareren vóór echte gebruikers: https://launchstudio.eu/nl/blog/firebase-studio-app-to-production-what-to-fix-before-real-users

#FirebaseStudio #Firebase #GDPR #NonProfit #AIFounder #LaunchStudio #Manifera
