🚨 Routeplanning van Ferdi Aalbersberg plant bezorgroutes voor 24 regionale bakkerijen en voedingsdistributeurs, waarvan de chauffeurs de app vanaf vijf uur 's ochtends gebruiken. Om 06:40 op een woensdag rolde hij een "triviale" wijziging uit: een kolom hernoemen van adres naar address. 😳

Elke chauffeur onderweg draaide de oude versie, die vroeg om een kolom die niet meer bestond. Zo'n 60 chauffeurs bij negen bedrijven kregen foutmeldingen — en terugdraaien mislukte ook, omdat de oude code de verwijderde kolom nodig had. Daarom breekt correcte code toch bij een deploy:

❌ Een kolom hernoemen en de app aanpassen in één deployment
❌ Geen besef dat browsertabbladen het JavaScript van gisteren blijven draaien
❌ Een rollback die na een destructieve schemawijziging niet kon werken
❌ Deployen tijdens het drukste tijdvak van de klanten

✅ Expand-and-contract over drie deployments: toevoegen, naar beide schrijven en aanvullen in batches van 2.000, lezen omzetten, later verwijderen
✅ Een regel: geen deployment mag een kolom verwijderen of hernoemen die de draaiende versie nog gebruikt
✅ Alleen aanvullende API-wijzigingen, met verwijderde endpoints 30 dagen bewaard als lege handeling
✅ Een melding "nieuwe versie beschikbaar" die chauffeurs bij hun volgende stop accepteren, een checklist van vier regels met getimede rollback, en geen deploys tussen 05:00 en 09:00

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring in productie-engineering, zorgen we dat uw volgende migratie omkeerbaar is voordat u haar uitrolt. 🔄

💡 Het resultaat: na één werkdag en € 1.600 — twaalf maanden zonder deploymentincident, inclusief twee verdere schemawijzigingen van vergelijkbare omvang. Door de versiemelding bleek dat chauffeurs zonder het te weten builds van drie dagen oud draaiden. 🚀

👉 Deploys zonder downtime terwijl mensen het gebruiken: https://launchstudio.eu/nl/blog/lovable-hosting-zero-downtime-deploys-while-people-are-using-it

#DevOps #Deployment #Databasemigraties #Lovable #LaunchStudio #Manifera
