🍽️ Karin Wouters leidt een familiebedrijf in Roosendaal dat groothandel is in horecabenodigdheden en bouwde Bestelportaal met Lovable en Supabase: zo'n 300 restaurants en hotels bestellen na, zien hun eigen prijzen en downloaden facturen die vanuit Exact Online worden gesynchroniseerd. Telefonische bestellingen daalden binnen weken. Toen vertelde een hotelmanager dat hij, door een filter aan te passen, kon zien wat een andere hotelketen betaalde. 😬

De beoordeling vond dat het fundament van het portaal klanten helemaal niet scheidde: 🧠

❌ Prijzen en facturen alleen in de interface op klant gefilterd
❌ Pdf's van facturen in een openbare bucket met voorspelbare namen
❌ Het token voor de synchronisatie met Exact Online leesbaar in een functie aan de clientkant
❌ Elke gebruiker bij een klant zag alles, ook keukenmedewerkers die alleen nabestellen

✅ Scheiding van bedrijven afgedwongen met Row Level Security op prijzen, bestellingen en facturen, met tests op scheiding
✅ Facturen in privéopslag met kortgeldige signed links, en downloads gelogd
✅ De synchronisatie met Exact Online verplaatst naar een geplande serverfunctie met een geroteerd, afgebakend token en meldingen bij fouten
✅ Rollen voor klanten voor beheerders, inkopers en financiën, en idempotente bestellingen zodat een dubbele klik geen twee bestellingen meer oplevert

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring met portalen en integraties voor klanten zoals Vodafone en TNO, scheiden we uw klanten goed en koppelen we uw backoffice veilig. 🛠️

💡 Het resultaat: €3.200, acht werkdagen. Geen enkele klant kan nog de prijzen van een andere zien, en klantbeheerders beheren nu hun eigen medewerkers. 🚀

👉 Productielancering voor B2B-klantportalen: https://launchstudio.eu/nl/blog/production-launch-for-b2b-customer-portals

#Klantportaal #B2B #ExactOnline #Lovable #AIFounder #LaunchStudio #Manifera
