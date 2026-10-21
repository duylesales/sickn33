🚨 Inschrijfpunt van Joost Berkhout verzorgt inschrijving en betaling voor 22 organisatoren van hardloop- en fietsevenementen. Op een zaterdagochtend in mei was zijn webhookhandler elf minuten onbereikbaar tijdens een deploy — precies toen de inschrijving opende voor het grootste evenement van zijn jaar. 😳

Zeventien mensen betaalden. Het geld kwam binnen. Zijn app wist het nooit. De organisator ontdekte het op de wedstrijddag, toen zeventien lopers kwamen opdagen met een betaalbevestiging en zonder startnummer. Daarom drijft uw database af van Stripe:

❌ Webhooks behandeld als gegarandeerd — ze worden opnieuw geprobeerd, en dan opgegeven
❌ Geen referentie van de provider opgeslagen bij betaalrijen
❌ Handlers die verwerken vóórdat het event is vastgelegd, zonder transactie om de schrijfacties
❌ Niemand die ooit provider, database en bank vergeleek

✅ Een maandelijkse afstemmingsquery (en na elke deploy) met drie verschillenlijsten
✅ Uitbetalingsrecords gekoppeld aan hun transacties, zodat elke bankstorting zichzelf verklaart
✅ Events vastgelegd vóór verwerking, in een transactie, idempotent op het event-ID
✅ Een lijst met onafgehandelde events en een gedocumenteerde procedure om opnieuw af te spelen — geen met de hand aangepaste rijen

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring in productie-engineering, houden we uw omzetcijfers, rechten en bankafschriften met elkaar in lijn. 🔄

💡 Het resultaat: na twee werkdagen en € 1.850 werden de zeventien lopers via het normale codepad hersteld in plaats van met de hand ingetypt. Het jaar daarop ving afstemming nog vier kleine verschillen op, elk binnen een maand — en de organisator verlengde. 🚀

👉 Stripe afstemmen met uw eigen database: https://launchstudio.eu/nl/blog/lovable-payments-reconciling-stripe-with-your-own-database

#Stripe #Webhooks #Afstemming #Lovable #LaunchStudio #Manifera
