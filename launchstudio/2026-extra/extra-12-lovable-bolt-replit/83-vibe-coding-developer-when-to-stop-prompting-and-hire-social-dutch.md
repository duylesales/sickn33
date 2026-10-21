🚨 Lidmaatschapbeheer van Wouter Klumpenaar verzorgt de ledenadministratie voor zeven beroepsverenigingen — zo'n 9.000 leden. In elke verlengingsperiode werden een paar leden twee keer afgeschreven. Hij besteedde er vijf maanden en zo'n veertig AI-sessies aan. Elke fix leek te werken — tot de volgende verlenging. 😳

Een ervaren lezer vond de oorzaak in negentig minuten: de verlengingstaak kon via twee paden in verschillende delen van de codebase worden gestart, en geen enkel gesprek had ze ooit allebei gezien. Zo weet u wanneer u stopt met prompten en iemand inschakelt:

❌ Dezelfde bug die veertig sessies in vijf maanden overleeft
❌ Geld dat door het product gaat zonder idempotentie op afschrijvingen
❌ Logica gedupliceerd over twee paden — en hetzelfde patroon elders, dat dubbele welkomstmails verstuurde
❌ Vier endpoints zonder autorisatiecontrole die niemand had opgemerkt

✅ De verlengingstaak idempotent gemaakt op lid en periode, met een test die bewijst dat een tweede run niets afschrijft
✅ Beide aanroeppaden samengevoegd tot één taak in de wachtrij
✅ Een afstemmingsquery die 31 historische dubbele afschrijvingen over drie jaar vond — allemaal terugbetaald
✅ Autorisatie getest over 22 endpoints, vier gaten gedicht, en een overdracht zodat Wouter alles kan onderhouden

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring in productie-engineering, nemen we het werk over waar fouten duur zijn — terwijl het product van u blijft om verder aan te bouwen. ⚙️

💡 Het resultaat: € 3.400, drie werkdagen. De dubbele afschrijvingen stopten, € 2.840 werd proactief terugbetaald — en twee verenigingen zeiden dat die terugbetaling de reden was dat ze verlengden. 🚀

👉 Vibe coding-developer: wanneer u stopt met prompten en iemand inhuurt: https://launchstudio.eu/nl/blog/vibe-coding-developer-when-to-stop-prompting-and-hire

#VibeCoding #Lovable #NoCode #Startups #LaunchStudio #Manifera
