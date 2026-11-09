🚨 Dennis Vos runt vanuit Zoetermeer een SaaS voor autogarages, gebouwd met Lovable en Supabase en gebruikt door zo'n 70 garages voor afspraken en facturen. Op zondagavond vroeg hij zijn AI-tool om "een kolom toe te voegen voor de naam van de monteur" en accepteerde hij meerdere vervolgsuggesties. Op maandagochtend zagen garages lege planningen. Vier extra prompts maakten het erger. Om 08:40 belde hij LaunchStudio. ☎️

De diagnose liet zien: 🧠

❌ Een suggestie van zondag had de policy van de afspraken vervangen door een policy die verkeerd naar de nieuwe kolom verwees, waardoor elke query niets teruggaf
❌ Een latere prompt hernoemde een kolom waarvan de factuurfunctie afhankelijk was
❌ Geen staging, dus elke wijziging ging direct naar de garages
❌ Geen tests om de kapotte policy vóór de release op te vangen

Zo werd het gestabiliseerd: ✅

✅ Een vaste prijs van €950 afgesproken vóór enige wijziging
✅ De policy hersteld vanuit de migratiegeschiedenis en het hernoemen van de kolom teruggedraaid
✅ De deployment teruggezet naar de versie van zaterdag, met planningen en facturen om 10:15 bevestigd door twee garages
✅ De kolom voor de monteur die middag correct toegevoegd via een migratie op een nieuwe staging, plus een incidentrapport met aanbevelingen

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring met het beheren van productiesystemen voor klanten zoals Vodafone en TNO, stabiliseren we eerst, leggen we helder uit wat er speelt en helpen we het volgende incident te voorkomen. 🛠️

💡 Het resultaat: zo'n anderhalf uur uitval, een eerlijke verontschuldiging en geen enkele garage die opzegde. Een vervolgproject binnen Launch Ready voegde tests toe die sindsdien een vergelijkbare promptfout hebben opgevangen. 🚀

👉 Spoedreparatie wanneer uw app gebouwd met AI plat ligt: https://launchstudio.eu/nl/blog/emergency-fix-service-when-your-ai-built-app-is-down

#AppPlat #Incident #Lovable #Supabase #AIFounder #LaunchStudio #Manifera
