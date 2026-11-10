🚨 Joris Peters bouwde Leskaart met Bolt en Supabase: dans- en yogastudio's verkopen strippenkaarten en abonnementen via Mollie. Een studio-eigenaar merkte dat leden die een tienrittenkaart hadden betaald nog steeds nul lessen zagen. 😳

Het onderzoek kostte twee dagen. De logs stonden vol namen, e-mailadressen en telefoonnummers - maar zeiden niets over of de verwerking was gelukt. Een schemawijziging had elf dagen eerder het bijschrijven van kaarten gebroken, met 63 betalingen bij vijf studio's als gevolg. Daarom heeft een kleine SaaS gestructureerde logging nodig: 🧠

❌ console.log dat volledige requests en ledengegevens dumpte
❌ Geen request-ID's om te volgen wat er gebeurde
❌ Een webhook die 200 teruggaf, ook als de database-update faalde
❌ Standaard bewaartermijnen en geen reconciliatie

✅ Een gestructureerde logger die ontvangst, verificatie, resultaat en duur vastlegt met alleen interne ID's
✅ Request-ID's bij elk request, teruggegeven in foutmeldingen
✅ Webhookfouten met een foutstatus zodat Mollie opnieuw probeert, met meldingen
✅ 30 dagen bewaartermijn en een dagelijkse taak die Mollie-betalingen vergelijkt met bijgeschreven kaarten

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring in productie-engineering, laten we uw logs vertellen wat er gebeurde - en niets over iemands privéleven. 🛠️

💡 Het resultaat: €2.400, 7 werkdagen. Alle 63 betalingen bijgeschreven. Twee maanden later ging er binnen minuten een melding af bij een timeout van een provider, en Joris had het hele verhaal in minder dan vijf minuten. 🚀

👉 Kunnen uw logs uitleggen wat er misging? Zo zet u gestructureerde logging op: https://launchstudio.eu/nl/blog/structured-logging-for-small-saas

#Logging #Observability #Mollie #SaaS #AIFounder #LaunchStudio #Manifera
