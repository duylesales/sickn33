🩺 Pieter Brink heeft vanuit Enschede een SaaS voor arbodienstverlening, gebouwd met Cursor en Supabase: werkgevers en bedrijfsartsen coördineren verzuimdossiers. Een grote werkgever eiste een onafhankelijke penetratietest voordat hij zou tekenen. Pieter boekte direct een beveiligingsadviesbureau. Het rapport: 32 bevindingen, waarvan zeven met een hoge ernst. 😬

Hij had geen developer, en zijn AI-tool loste een paar bevindingen op maar brak het uploaden van documenten voor artsen. De bevindingen met hoog risico waren onder meer: 🧠

❌ Ontbrekende eigendomscontroles op API-routes
❌ Dossierdocumenten in een openbare bucket
❌ Een blootgestelde servicesleutel
❌ Geen rate limiting op het inloggen, plus verouderde dependencies

✅ Eigendomscontroles op elke route via een gedeelde helper, ondersteund door Row Level Security met tests
✅ Documenten in privéopslag met signed links, en de sleutel geroteerd
✅ Rate limits, security headers en bijgewerkte dependencies
✅ Een korte notitie per fix voor de testers, klaar voor de hertest

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring met software voor klanten zoals Vodafone en TNO, lossen we bevindingen op in uw code en bereiden we u voor op onafhankelijk testen, het liefst vóór de test, niet erna. 🛠️

💡 Het resultaat: €3.300, acht werkdagen. De hertest vond alleen drie problemen met een lage ernst, binnen een dag opgelost, en de werkgever tekende. 🚀

👉 LaunchStudio versus een beveiligingsadviesbureau: https://launchstudio.eu/nl/blog/launchstudio-vs-a-security-consultancy

#Pentest #Beveiliging #Cursor #Supabase #AIFounder #LaunchStudio #Manifera
