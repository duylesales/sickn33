🚨 Wachtkamer van Lotte van Bemmel regelt het inchecken van patiënten voor huisartsenpraktijken, € 59 per maand na een proefperiode van 21 dagen. Het gebruik groeide sneller dan de omzet. Toen ze actieve accounts naast betalende legde, was het verschil 40 praktijken — sommige checkten al vijf maanden dagelijks patiënten in op een verlopen proefperiode. 😳

Op haar scherm was de proefperiode afgelopen. Op de server was niets veranderd. Zo lekken proefperiodes toegang:

❌ Het verlopen van de proefperiode alleen in de frontend geregeld — een upgradescherm, maar elk verzoek werkte nog
❌ 19 van de 34 endpoints zonder enige autorisatiecontrole
❌ Dubbele proefperiodes via e-mailadressen met een plusteken
❌ Geen herinneringen vóór het verlopen

✅ Eén toegangsfunctie op de server, aangeroepen door elk endpoint
✅ De interface aangestuurd door dezelfde functie, zodat weergave en rechten niet uit elkaar lopen
✅ Normalisatie van e-mailadressen, plus herinneringen op dag 14, dag 20 en bij het verlopen
✅ Alleen-lezen toegang en data-export 60 dagen bewaard, plus een beheeractie om een proefperiode te verlengen

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring in productie-engineering, testen we uw verlopen proefperiode zoals uw gebruikers dat doen — met de ontwikkelhulpmiddelen open. 🔍

💡 Het resultaat: na drie werkdagen en € 2.400 stapten 12 van de 40 praktijken binnen een maand over op betaald, daalden de infrastructuurkosten met een derde, en steeg de conversie van proefperiode naar betaald bij nieuwe aanmeldingen van 18% naar 29%. 🚀

👉 Gratis proefperiodes die geen toegang lekken: https://launchstudio.eu/nl/blog/lovable-payments-free-trials-that-do-not-leak-access

#SaaS #Proefperiode #Toegangsbeheer #Lovable #LaunchStudio #Manifera
