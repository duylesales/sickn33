🚨 Bram de Vries bouwde Ambachtsavond met Bolt en Supabase: keramisten, houtbewerkers en bakkers verkopen plekken in avondworkshops, vooraf betaald met iDEAL of kaart via Mollie. Zo'n 45 hosts boden workshops aan. Toen klaagden hosts: klanten zeiden dat ze hadden betaald, maar stonden niet op de deelnemerslijst. 😳

Ongeveer 20% van de gestarte betalingen werd nooit afgerond. Het Mollie-dashboard liet zien waarom. Waarom de betaling van sommige klanten mislukt bij het afrekenen: 🧠

❌ iDEAL-betalingen "betaald" bij Mollie, boekingen "in behandeling" - alleen bevestigd op de terugkeerpagina
❌ Een eigen kaartformulier dat 3D Secure niet afhandelde
❌ Een succes-URL die boekingen bevestigde zonder enige betaling
❌ Prijzen met korting zoals €42,499 die Mollie afwees

✅ De gehoste checkout van Mollie, die 3D Secure en alle methoden afhandelt
✅ Boekingen alleen bevestigd door een geverifieerde Mollie-webhook, met een terugkeerpagina die de status opvraagt
✅ Bedragen in centen berekend op de server, plus idempotentie
✅ Meldingen bij mislukte webhooks, en 37 klanten die hadden betaald alsnog aan hun workshop toegevoegd

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring in productie-engineering, laten we uw app geloven dat klanten die echt betaald hebben, betaald hebben. 🛠️

💡 Het resultaat: €2.400, 6 werkdagen. Het aandeel afgeronde betalingen steeg van ongeveer 80% naar 94%, en de maandelijkse boekingsomzet steeg in twee maanden met zo'n 17% - zonder extra verkeer. 🚀

👉 Verliest u klanten bij het afrekenen? Dit zijn de oorzaken en oplossingen: https://launchstudio.eu/nl/blog/why-do-some-customers-payments-fail-at-checkout

#Payments #Mollie #iDEAL #3DSecure #AIFounder #LaunchStudio #Manifera
