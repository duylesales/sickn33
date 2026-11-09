🏢 Bas Kramer heeft vanuit Amersfoort een SaaS voor facilitair beheer, gebouwd met Lovable en Supabase: vastgoedbeheerders leggen onderhoudsverzoeken vast, aannemers werken de status bij. Vóór een contract met een woningcorporatie draaide hij de security advisor van Supabase en een gratis externe scanner. Beide zeiden groen. ✅

Eén middag testen met echte rollen zei iets anders: 🧠

❌ Elke tabel had Row Level Security, maar meerdere policies lieten elke ingelogde gebruiker elk verzoek lezen
❌ Aannemers konden via de API de status van klussen van andere aannemers wijzigen
❌ Foto-uploads in een openbare bucket
❌ Een servicesleutel in een Edge Function die zonder authenticatie kon worden aangeroepen

✅ Policies per rol herschreven, met geautomatiseerde tests voor elke tabel
✅ Updates door aannemers beperkt tot toegewezen klussen
✅ Foto's in privéopslag met signed links, de functie beveiligd en de sleutel geroteerd
✅ Rate limits, security headers en een getest herstel van back-ups, plus een rapport om te delen

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring met software voor beveiligingsbewuste klanten zoals Vodafone en TNO, vinden en repareren onze reviews de problemen die scanners niet zien. 🛠️

💡 Het resultaat: €2.200, zes werkdagen. De woningcorporatie accepteerde het rapport, en een formele pentest een jaar later vond alleen twee problemen met een lage ernst. 🚀

👉 Wat kost een beveiligingsreview voor een app gebouwd met AI: https://launchstudio.eu/nl/blog/cost-of-a-security-review-for-an-ai-built-app

#Beveiliging #Pentest #Supabase #Lovable #AIFounder #LaunchStudio #Manifera
