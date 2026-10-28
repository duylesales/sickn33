🚨 Eline Rademaker, dierenartsassistente in Apeldoorn, bouwde Huisdierpas in Lovable: een marktplaats die huisdiereigenaren verbindt met gescreende oppassers - inclusief medische notities over allergieën en medicatie. Voordat ze buiten 40 piloteigenaren lanceerde, vroeg ze offertes op: een geautomatiseerde scan van € 450, of een penetratietest van € 14.000. 😳

Ze koos geen van beide. Een gerichte review van € 950 vond 13 problemen - drie kritiek: oppassers konden de medische notities van elk huisdier lezen, berichten gingen open door een ID te veranderen, en een Supabase-servicesleutel stond in de frontend. De geautomatiseerde scan die ze ter vergelijking draaide, vond de sleutel… en geen van de toegangsproblemen. Dit hoort een beveiligingsaudit op te leveren - en te kosten:

❌ Een goedkope scan die logicafouten zoals gebrekkig toegangsbeheer mist
❌ Een penetratietest geprijsd voor een enterprise, niet voor een jonge app
❌ Medische notities leesbaar op het hele platform
❌ Een servicesleutel met volledige toegang in de browserbundel

✅ Een geschreven rapport: scope, gerangschikte bevindingen, bewijs, oplossingen - en wat in orde bleek
✅ Row level security die medische notities koppelt aan actieve boekingen; controles op deelnemers bij berichten
✅ De servicesleutel geroteerd en uit de frontend gehaald; rate limiting en uploadlimieten
✅ Een vastgelegde hertest die laat zien dat elke kritieke bevinding is opgelost

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring in productie-engineering en een oprichter met wortels in cybersecurity, beoordelen we de logica die scanners niet zien - tegen een vaste prijs. ⚙️

💡 Het resultaat: € 2.750 totaal (€ 950 review + € 1.800 fixes en hertest). Huisdierpas bereikte in vier maanden 520 eigenaren en 85 oppassers, en het hertestrapport hielp bij een samenwerking met een regionale huisdierverzekeraar. 🚀

👉 Beveiligingsaudit voor AI-applicaties: wat je ontvangt en wat het kost: https://launchstudio.eu/nl/blog/ai-application-security-audit-what-you-receive-and-what-it-costs

#AppSecurity #Lovable #SecurityAudit #Startups #LaunchStudio #Manifera
