🚨 Evi Janssens, restaurantmanager in Maastricht, bouwde Tafelgarant in Bolt: gasten boeken online, betalen een aanbetaling van € 10 per persoon via iDEAL of kaart, krijgen herinneringen en kunnen tot 24 uur vooraf gratis annuleren. Negen restaurants in Maastricht en Heerlen, zo'n 2.500 couverts per maand. Toen kwam het carnavalsweekend - dubbel geboekte tafels en woedende gasten met betaalbewijzen. 😳

Aanbetalingen werden bevestigd als de browser terugkeerde van Mollie, dus gasten die in hun bankapp betaalden bleven "in afwachting" en verloren hun tafel. De termijn van 24 uur werd in UTC berekend, waardoor annuleringen die nog op tijd waren werden geweigerd. Terugbetalingen gingen met de hand, capaciteit was een vast aantal per half uur, twee gezelschappen pakten tegelijk de laatste grote tafel, en allergienotities waren zichtbaar voor personeel van alle negen restaurants. Dit heeft een horeca-app met AI nodig vóór productie:

❌ Betalingen bevestigd via de redirect in de browser
❌ Annuleringstermijnen in UTC in plaats van lokale tijd
❌ Tellingen per slot die tafelgroottes en wedlopen negeren
❌ Gezondheidsgegevens van gasten gedeeld tussen locaties

✅ Bevestiging van aanbetalingen via geverifieerde Mollie-webhooks, met de carnavalsboekingen verzoend
✅ Annuleringstermijnen in de tijdzone Europe/Amsterdam met automatische terugbetalingen
✅ Een capaciteitsmodel op basis van tafels, afgedwongen in de database, met zittingsduur per gezelschapsgrootte
✅ Data gescheiden per restaurant, allergienotities alleen voor vloer en keuken van die locatie, en herinneringen via een geauthenticeerde e-mail- en sms-aanbieder

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring in productie-engineering, zorgen we dat de tafel er is als uw gast binnenkomt. ⚙️

💡 Het resultaat: € 2.950, tien werkdagen. Nul dubbele boekingen in de twee maanden daarna, no-shows onder de 2% van de couverts, en nog vier restaurants sloten zich aan vóór het terrasseizoen. 🚀

👉 AI-App naar Productie voor Horeca: Reserveringen, Aanbetalingen en No-Shows: https://launchstudio.eu/nl/blog/ai-app-to-production-for-hospitality-reservations-deposits-and-no-shows

#Horeca #Restaurants #iDEAL #Bolt #LaunchStudio #Manifera
