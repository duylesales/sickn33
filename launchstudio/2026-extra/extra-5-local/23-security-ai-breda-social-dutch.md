🚨 Elise van Dongen bouwde TableTuned, een reserverings- en personeelsroostertool voor restaurants rond het Bredase Ginnekenmarkt-district, met Cursor — binnen een maand waren al zes restaurants live. Toen veranderde de manager van een zevend restaurant, die de tool alleen aan het evalueren was, uit nieuwsgierigheid een reservering-ID in de URL en kreeg de volledige gastenlijst van een ander restaurant te zien, telefoonnummers incluis. 😳

Hij meldde het in plaats van het te misbruiken. De blootstelling had de hele maand live gestaan. 🧠

❌ Geen enkel row-level-securitybeleid op de reserveringstabel — een standaard Supabase-configuratie die nooit was afgesloten
❌ Elk restaurant kon de gasten van elk ander restaurant zien door simpelweg een URL te wijzigen
❌ Het openbare boekingseindpunt had geen rate limiting
❌ Stripe-sleutels stonden in client-side code

✅ Correcte tenant-isolatie implementeren voor elke reservering
✅ Rate limiting toevoegen aan het openbare boekingseindpunt
✅ Betaalsleutels uit de frontend halen en onderbrengen in een beveiligde backendfunctie

Bij **LaunchStudio** behandelen de technici van Manifera — vertrouwd door Vodafone, TNO en CFLW Cyber Strategies voor beveiligingsgevoelig werk — row-level security als een standaard controlepunt vóór lancering, niet als bijzaak. 🛡️

Het resultaat voor TableTuned: de tool werd opnieuw gelanceerd met geverifieerde tenant-isolatie, en Elise leidt haar verkoopgesprekken nu met haar beveiligingsaudit in plaats van te hopen dat het onderwerp niet ter sprake komt. 🚀

👉 Werkt u met boekings- of gastgegevens in een door AI gebouwde app? Laat de audit uitvoeren voordat een nieuwsgierige gebruiker het gat vindt: [Link naar artikel]

#AINativeFounder #LaunchStudio #Manifera #SecurityAudit #Breda
