🚨 Sjoerd Wiersma, penningmeester van een korfbalclub in Leeuwarden, bouwde Contributieman met Bolt zodat leden hun jaarcontributie online via Mollie konden betalen. Na de eerste maand zei de app dat 212 leden hadden betaald. Mollie zei 174. 😳

Het verschil had één oorzaak: de app vertrouwde de terugkeerpagina. Iedereen die daarop landde, werd als betaald gemarkeerd - ook leden die in hun bankapp annuleerden. Dit ontbrak:

❌ Helemaal geen Mollie-webhook
❌ Leden als betaald gemarkeerd bij de redirect, ook na geannuleerde of verlopen betalingen
❌ De live sleutel van Mollie in een omgevingsbestand van de frontend
❌ Bedragen verstuurd vanuit de browser

✅ Het aanmaken van betalingen verplaatst naar een Supabase edge function, met bedragen uit de database
✅ Een Mollie-webhook die de echte status ophaalt via de API van Mollie en lidmaatschappen idempotent bijwerkt
✅ Elke status gekoppeld aan een duidelijke melding voor leden
✅ De blootgestelde sleutel vervangen, plus een maandelijks reconciliatierapport

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar betaalintegraties vanuit Amsterdam, bouwen we de onderdelen van een Mollie-integratie die AI-tools overslaan. 🛠️

💡 Het resultaat: €1.700, zeven werkdagen. De volgende reconciliatie klopte tot op de cent, de club inde 96% van de jaarcontributies online, en de 38 leden die onterecht als betaald stonden, betaalden binnen twee weken. 🚀

👉 Gebruikt u Mollie in een Lovable-, Bolt- of Cursor-app? Dit is de volledige integratie stap voor stap: https://launchstudio.eu/nl/blog/mollie-integration-for-ai-built-apps-step-by-step

#Mollie #iDEAL #Supabase #Bolt #LaunchStudio #Manifera
