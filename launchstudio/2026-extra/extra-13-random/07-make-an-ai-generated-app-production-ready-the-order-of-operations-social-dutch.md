🚨 Thijs Groen, sommelier in Nijmegen, bouwde WijnWijzer: een webshop voor wijnabonnementen met een v0-etalage en een Supabase-backend. Omdat hij graag wilde verdienen, besteedde hij zijn eerste twee weken aan Stripe-abonnementen - en bij een zachte lancering meldden 70 klanten zich aan. Toen werd het volgordeprobleem zichtbaar. 😳

Abonnementen hingen aan een klant-ID dat in de browser werd aangemaakt, waardoor terugkerende klanten op een nieuw apparaat dubbele accounts en dubbele afschrijvingen kregen. Leeftijdsverificatie - wettelijk verplicht bij alcohol - was een vinkje in de frontend, geheime Stripe-sleutels stonden in clientcode, en de database draaide in de VS. Dit is de volgorde die voorkomt dat u alles twee keer doet:

❌ Betalingen eerst gebouwd, op een zwak gebruikersmodel
❌ Leeftijdsverificatie alleen afgedwongen in de interface
❌ Geheime Stripe-sleutels in een configuratiebestand aan de clientkant
❌ Een database in een Amerikaanse regio

✅ Accounts samengebracht, Stripe-sleutels geroteerd en naar de server verplaatst
✅ Een degelijk gebruikersmodel op de server met opgeslagen en afgedwongen leeftijdsbevestiging
✅ Database gemigreerd naar een EU-regio met een getest herstel
✅ Stripe opnieuw gebouwd rond geverifieerde webhooks - 11 dubbele records samengevoegd en 4 dubbele afschrijvingen terugbetaald - daarna staging, hosting en monitoring

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring in productie-engineering, volgen we elke keer dezelfde volgorde: eigenaarschap, geheimen, toegang, data, geld, levering, zichtbaarheid. ⚙️

💡 Het resultaat: € 3.200, twaalf werkdagen. WijnWijzer groeide in vijf maanden naar 410 actieve abonnees zonder dubbele accounts of afschrijvingen, en doorstond de beoordeling van de betaalprovider voor alcoholverkoop. 🚀

👉 Een AI-gegenereerde app productierijp maken: de juiste volgorde van stappen: https://launchstudio.eu/nl/blog/make-an-ai-generated-app-production-ready-the-order-of-operations

#Stripe #Supabase #AIApp #Startups #LaunchStudio #Manifera
