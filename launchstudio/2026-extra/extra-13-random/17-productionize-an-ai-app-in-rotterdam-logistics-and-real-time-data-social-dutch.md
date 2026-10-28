🚨 Samira El Amrani was acht jaar operationeel manager van een magazijn in het Rotterdamse havengebied en bouwde daarna DockSlot in Lovable: vervoerders boeken losslots, poortpersoneel meldt vrachtwagens aan op een tablet, planners volgen een live bord van elk dock. Drie magazijnen in de Waalhaven en op de Maasvlakte gebruikten het. Toen betwistte een vervoerder een rekening voor overliggeld - en niemand kon zeggen wie hun slot had verschoven. 😳

Op drukke ochtenden stapelde alles zich op: twee of drie dubbele boekingen per week, een live bord dat de database elke twee seconden vanaf elk scherm pollde, aanmeldingen die verdwenen als tablets bij de stalen deuren de wifi verloren, en een TMS-integratie van een verlader die de app vertraagde zodra die zelf trager werd. Dit heeft operationele logistieke software nodig vóór productie:

❌ Beschikbaarheid controleren en boeking opslaan in twee aparte stappen
❌ Polling vanaf elk open scherm tijdens de piek van 05:30
❌ Aanmeldingen die verloren gaan als het signaal wegvalt
❌ Synchrone integraties en geen audittrail

✅ Een exclusion constraint in de database die overlappende dockboekingen onmogelijk maakt
✅ Gefilterde realtime abonnementen per magazijn van de gebruiker
✅ Een offline wachtrij voor aanmeldingen bij de poort, met duidelijke indicatoren
✅ De TMS-integratie achter een wachtrij met retries en idempotentie, plus een append-only auditlog

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring in productie-engineering, maken we AI-gebouwde tools net zo betrouwbaar als de mensen die ermee werken - en blijft de Lovable-interface intact. ⚙️

💡 Het resultaat: € 5.600, achttien werkdagen. Dubbele boekingen daalden naar nul, de databasebelasting in de ochtendpiek nam met zo'n 70% af, en DockSlot tekende met nog twee magazijnen - één eiste de auditlog en een beschikbaarheidsafspraak van 99,5%. 🚀

👉 Een AI-app productierijp maken in Rotterdam: logistieke ondernemers en realtime data: https://launchstudio.eu/nl/blog/productionize-an-ai-app-in-rotterdam-logistics-and-real-time-data

#Logistiek #Rotterdam #SupplyChain #Lovable #LaunchStudio #Manifera
