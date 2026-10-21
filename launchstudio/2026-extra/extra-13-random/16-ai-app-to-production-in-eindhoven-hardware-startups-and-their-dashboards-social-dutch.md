🚨 Pieter Hofstede verliet een groot Eindhovens techbedrijf om SensaGrow te starten: draadloze sensoren die temperatuur, luchtvochtigheid en CO₂ meten in commerciële kassen. De hardware was zorgvuldig ontworpen. Het klantdashboard werd in ongeveer drie weken in Cursor gebouwd. Vijf Westlandse telers testten 340 sensoren — toen wilde een coöperatie er 2.000 uitrollen. 😳

De IT-adviseur vroeg om een beveiligingsoverzicht. Elke sensor deelde één API-sleutel in de firmware, het endpoint voor binnenkomende data vertrouwde elke device_id, telers konden via de API elkaars data lezen, en het commando om de ventilatie te overrulen had geen rolcontrole of auditlog. Dit moeten hardware-startups oplossen voordat het dashboard productie in gaat:

❌ Eén gedeelde apparaatsleutel — één keer uitlezen, elke sensor nadoen
❌ Eén databaserij per meting: 40 miljoen rijen en grafieken van 20 seconden
❌ Scheiding tussen klanten alleen in de interface
❌ Apparaatcommando's zonder rollen, limieten of audittrail

✅ Tokens per apparaat met een intrekkingslijst, uitgerold via de volgende firmware-update
✅ Een wachtrij met gebundelde, idempotente verwerking van binnenkomende data
✅ TimescaleDB met samenvattingen per uur en per dag
✅ Row level security per teler, en ventilatie overrulen alleen voor beheerders, met bevestiging, waardelimieten en een audittrail

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring in productie-engineering — inclusief klanten met industriële en energiehardware — bouwen we het dashboard met dezelfde zorg als het apparaat. ⚙️

💡 Het resultaat: € 4.200, vijftien werkdagen. SensaGrow doorstond de beveiligingsbeoordeling van de coöperatie en begon aan de uitrol van 2.000 sensoren. Grafieken laden binnen een seconde, en de verwerking haalt 60+ metingen per seconde zonder dataverlies. 🚀

👉 Van AI-app naar productie in Eindhoven: hardware-startups en hun dashboards: https://launchstudio.eu/nl/blog/ai-app-to-production-in-eindhoven-hardware-startups-and-their-dashboards

#IoT #Eindhoven #Brainport #AppSecurity #LaunchStudio #Manifera
