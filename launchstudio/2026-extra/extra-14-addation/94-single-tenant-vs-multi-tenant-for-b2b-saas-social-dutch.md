🚨 Victor Hamers bouwde Inspectieloket in Bolt en Supabase: een tool voor inspecties en compliance voor onderhoudsbedrijven in vastgoed, multi-tenant, met 25 klanten. Toen wilde een landelijke woningcorporatie tekenen - maar die eiste een eigen database in een EU-regio naar keuze, met een eigen schema voor back-ups. Zijn eerste ingeving: het hele project met de hand kopiëren. 😳

Hij had bijna een tweede product gemaakt door het eerste te kopiëren. Eén codebase die twee keer wordt gedeployd, was het antwoord. Dit had kopiëren veroorzaakt:

❌ Twee codebases die bij elke wijziging verder uit elkaar lopen
❌ Migraties die met de hand op aparte databases worden uitgevoerd
❌ De klant met een eigen instantie die achterloopt op functies en oplossingen
❌ Een deal met een grote klant geprijsd zonder de werkelijke kosten van een tweede instantie

✅ Eerst de multi-tenant opzet verstevigd, met RLS op basis van organisaties en geautomatiseerde tests voor scheiding
✅ Een eigen Supabase-project voor de woningcorporatie, gedeployd vanuit dezelfde codebase
✅ Een workflow in GitHub Actions die migraties en edge functions na elkaar op beide projecten toepast
✅ Een prijs voor grote klanten die de extra instantie dekt, plus documentatie

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring met zowel multi-tenant als eigen B2B-systemen, houden we multi-tenant als standaard en automatiseren we eigen instanties alleen wanneer een contract dat echt vereist. 🛠️

💡 Het resultaat: €5.200, veertien werkdagen. De woningcorporatie tekende tegen een prijs voor grote klanten, en elke functie die sindsdien is uitgebracht, bereikte beide omgevingen op dezelfde dag. 🚀

👉 Single-tenant of multi-tenant voor uw B2B-SaaS? Zo beslist u: https://launchstudio.eu/nl/blog/single-tenant-vs-multi-tenant-for-b2b-saas

#SaaS #MultiTenant #Supabase #B2B #LaunchStudio #Manifera
