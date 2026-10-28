🚨 Tandartsplanner van Evelien Hartman regelt de agenda en online afspraken voor 58 tandartspraktijken. Een nieuwe boekingswidget ging op een maandagochtend live bij alle praktijken tegelijk. Voor praktijken die één stoel delen tussen tandarts en mondhygiënist werd de beschikbaarheid verkeerd berekend. Om tien uur hadden elf praktijken dubbel geboekte stoelen. 😳

Uitzetten betekende terugdraaien, wat ook een migratie en twee fixes ongedaan maakte - dus online boeken lag die ochtend overal plat. Dezelfde maand schoten de kosten van een AI-functie voor terugroepen omhoog, en die was niet te stoppen zonder deploy. Zo laten feature flags u eerst aan een deel van de klanten releasen:

❌ Deployen en releasen als hetzelfde moment, voor alle 58 praktijken
❌ Geen manier om één functie uit te zetten zonder alles terug te draaien
❌ Geen noodschakelaar voor een AI-functie die per aanroep geld kost
❌ De grootste en meest complexe praktijken die nieuwe functies tegelijk met iedereen kregen

✅ Een flagtabel met eigenaars en vervaldata, uitzonderingen per praktijk en stabiele uitrol per percentage
✅ Flags beoordeeld op de server, met alleen resultaten naar de browser - nooit gebruikt als beveiligingsgrens
✅ Noodschakelaars voor AI-suggesties, sms-herinneringen en de boekingswidget, elk met een nette melding "tijdelijk niet beschikbaar"
✅ Een bètagroep van zes praktijken, fouten gelabeld per actieve flag, een audit van flagwijzigingen en tests met flags aan en uit

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring in productie-engineering, maken we releases routine voor producten waarop klanten elke dag rekenen. ⚙️

💡 Het resultaat: € 2.800, drie werkdagen. De gerepareerde widget ging via de bètagroep, dan 25%, dan iedereen - geen enkele dubbele boeking. Negen functies volgden op dezelfde manier; één bug werd bij drie praktijken opgemerkt en binnen een minuut uitgezet. 🚀

👉 Lovable hosting: feature flags en eerst aan een deel van de klanten releasen: https://launchstudio.eu/nl/blog/lovable-hosting-feature-flags-and-releasing-to-some-customers-first

#FeatureFlags #DevOps #SaaS #Lovable #LaunchStudio #Manifera
