🚨 Wouter Nagelkerke bouwde Vaarschool Online met Lovable - theoriecursussen voor het vaarbewijs, € 79 per cursus. Hij koos Stripe omdat de tutorials dat deden, en lanceerde met alleen kaartbetalingen. De checkoutconversie bleef op 31% steken, wat hij normaal vond. 😳

Hij stelde één vraag in de mail voor afgebroken bestellingen. Van de 46 antwoorden zeiden er 38: "ik gebruik geen creditcard." Dit heeft een Nederlandse checkout nodig:

❌ Een checkout met alleen kaarten voor Nederlandse consumenten die met iDEAL betalen
❌ De geheime Stripe-sleutel sinds de lancering in de frontend
❌ Prijzen vanuit de browser verstuurd en door de server vertrouwd
❌ Niet-geverifieerde webhooks - een herhaald event leverde een tweede cursusinschrijving op

✅ iDEAL ingeschakeld en als standaard betaalmethode geplaatst
✅ Checkout op de server aangemaakt, met de prijs uit de database
✅ Verificatie van webhookhandtekeningen plus een idempotentiesleutel
✅ Een betalingstabel in zijn eigen database, en afgebroken iDEAL-betalingen die netjes verlopen

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring in productie-engineering, kiezen we de betaalprovider die past bij uw echte klanten - en sluiten we hem zo aan dat hij niet te misbruiken is. 💳

💡 Het resultaat: na vier werkdagen en € 2.150 ging de checkoutconversie in de eerste maand van 31% naar 68% bij hetzelfde verkeer - en de wekelijkse mails over dubbele inschrijvingen hielden volledig op. 🚀

👉 Mollie of Stripe voor een Nederlands product: https://launchstudio.eu/nl/blog/lovable-payments-mollie-or-stripe-for-a-dutch-product

#iDEAL #Mollie #Stripe #Lovable #LaunchStudio #Manifera
