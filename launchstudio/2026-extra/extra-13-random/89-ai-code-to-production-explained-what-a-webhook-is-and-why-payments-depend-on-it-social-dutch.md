🚨 Rick Jonker, kok die kookworkshops geeft in Hattem, bouwde Pannenklaar in Lovable: gasten boeken een plek, betalen via Mollie en krijgen een bevestiging met het menu en de ingrediëntenlijst. De workshops verkochten goed — soms te goed. En elke week bracht een paar raadsels. 😳

Gasten kwamen aan met bankafschriften waarop de betaling stond, maar zonder boeking in het systeem. Andere boekingen stonden als betaald gemarkeerd zonder bijbehorende Mollie-betaling — sommige van gasten die het tabblad hadden gesloten en via de bedanklink in hun geschiedenis waren teruggekomen. Terugbetalingen in het Mollie-dashboard gaven de plek nooit vrij, waardoor workshops vol leken terwijl ze dat niet waren. Rick wist niet wat een webhook was; de app bevestigde boekingen zodra gasten de bedankpagina bereikten. Dit is een webhook — en waarom betalingen ervan afhangen:

❌ De bedankpagina behandeld als bewijs van betaling
❌ Betaalde boekingen die ontbreken, onbetaalde die zijn bevestigd
❌ Terugbetalingen die de app nooit bereikten
❌ Geen meldingen en geen afstemming

✅ Mollie-webhooks die bij elke melding de echte betaalstatus opzoeken
✅ Bevestiging van boekingen alleen afhankelijk van die status, met herhalingen en meldingen in de verkeerde volgorde afgehandeld
✅ Plekken automatisch vrijgegeven bij terugbetalingen en verlopen betalingen, bevestigingsmails verstuurd door een achtergrondtaak
✅ Meldingen bij mislukte verwerking van webhooks — en twee maanden boekingen afgestemd met de gegevens van Mollie

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring in productie-engineering, zorgen we dat alleen de betaalaanbieder — niet de bedankpagina — bepaalt wat er is betaald. ⚙️

💡 Het resultaat: € 1.350, vijf werkdagen. Niet-gekoppelde betalingen en spookboekingen stopten volledig, vrijgekomen plekken worden opnieuw verkocht voor naar schatting € 600 extra per maand, en Rick besteedt zijn maandagochtenden aan koken in plaats van afstemmen. 🚀

👉 Van AI-code naar productie uitgelegd: Wat een webhook is en waarom betalingen ervan afhangen: https://launchstudio.eu/nl/blog/ai-code-to-production-explained-what-a-webhook-is-and-why-payments-depend-on-it

#Webhooks #Betalingen #Mollie #Lovable #LaunchStudio #Manifera
