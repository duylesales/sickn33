🚨 Hasan Demir bouwde Wagenpark met Cursor en Supabase: onderhoud van wagenparken voor kleine transportbedrijven. Een klant met 60 bestelbussen vroeg om API-toegang. Onder tijdsdruk stuurde Hasan zijn Supabase-URL en publieke sleutel. Dat werkte - tot hij een kolom hernoemde en hun integratie 's nachts brak. 😳

Toen werd het erger: de integratie van de klant kon de kentekens van voertuigen van andere klanten lezen. Hij had een klant zijn database als API gegeven. Dit betekende dat:

❌ Klanten direct gekoppeld aan zijn interne databaseschema
❌ Elke schemawijziging een brekende wijziging voor hun systemen
❌ Eén slecht beschermde tabel die gegevens van andere klanten blootstelde
❌ Geen manier om af te bakenen, te beperken of te meten wat de klant deed

✅ De te ruime policy hersteld
✅ Een API met versie /v1 in edge functions voor voertuigen, keuringen en reparaties
✅ API-sleutels per organisatie met scopes voor lezen en schrijven, opgeslagen als hash, plus rate limits per abonnement en logs van gebruik
✅ Ondertekende uitgaande webhooks voor afgeronde keuringen, en openbare documentatie

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring met het ontwerpen van integratie-API's voor enterpriseklanten, bouwen we kleine, strikt geautoriseerde API's met versiebeheer - nooit uw database met een sleutel eraan. 🛠️

💡 Het resultaat: €4.800, dertien werkdagen. Hasan kan zijn schema nu wijzigen zonder iemand te breken, nog drie klanten gingen de API gebruiken, en API-toegang werd een functie van zijn hoogste abonnement. 🚀

👉 Vragen zakelijke klanten om een API? Zo biedt u die veilig aan vanuit een AI-gebouwde SaaS: https://launchstudio.eu/nl/blog/how-do-i-offer-an-api-to-my-saas-customers

#API #SaaS #Supabase #APISecurity #LaunchStudio #Manifera
