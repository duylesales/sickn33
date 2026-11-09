☕ Vera Hofman heeft een kleine koffiebranderij in Deventer en bouwde Bonenpost met Bolt en Supabase: zo'n 900 abonnees krijgen elke twee of vier weken vers gebrande bonen, betaald via Mollie. Toen vormden de klachten een patroon. Sommige klanten werden in één week twee keer belast, overgeslagen leveringen kwamen toch, en mislukte incasso's stopten stilletjes de leveringen. Opzeggen? Alleen per e-mail. 📬

De beoordeling verklaarde alles: 🧠

❌ Eén geplande functie die afschrijving en order aanmaakte en na time-outs opnieuw vanaf het begin begon
❌ De klokwisseling in het voorjaar die het schema verschoof en één cyclus twee keer liet draaien
❌ Overslaan na de export naar de fulfilment genegeerd, en mislukte SEPA-incasso's en latere storneringen nooit verwerkt
❌ Orders elke cyclus als spreadsheet geëxporteerd en met de hand geüpload

✅ Idempotentiesleutels per abonnement en cyclus, met orders alleen aangemaakt op basis van geverifieerde webhooks
✅ Data van cycli opgeslagen met tijdzone-informatie en getest over klokwisselingen heen
✅ Een duidelijke sluitingstijd twee dagen vóór het branden, een stroom met herinneringen, nieuwe pogingen en links om de betaling bij te werken, en storneringen die de status bijwerken
✅ Orders na de sluitingstijd via de API van de fulfilmentpartner, plus online opzeggen met bevestiging

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring met systemen voor betalingen, planning en integraties voor klanten zoals Vodafone en TNO, laten we elke cyclus één betaling en één order opleveren. 🛠️

💡 Het resultaat: €3.200, acht werkdagen. Dubbele afschrijvingen stopten, en de stroom met herinneringen haalde binnen twee maanden een groot deel van de mislukte betalingen terug. 🚀

👉 Productielancering voor abonnementen in e-commerce: https://launchstudio.eu/nl/blog/production-launch-for-subscription-ecommerce

#Abonnementen #Ecommerce #Mollie #Bolt #AIFounder #LaunchStudio #Manifera
