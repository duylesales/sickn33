🔓 Penelope, een CRM-consultant, bouwde een AI-verkoopadviseur met **Bolt** — maar de app miste scheiding op rijniveau, wat direct risico gaf op datalekken tussen verschillende klantorganisaties. 📊

Een vectordatabase kent geen geheimhoudingsniveaus — het zoekt puur op wiskundige tekstovereenkomst, waardoor de vraag van een stagiair net zo makkelijk de geheime directienotitie oplevert als een openbare FAQ. 🧠

❌ Een monolithische vectorindex waarin HR-, marketing- en overnamestukken in één onbeveiligde ruimte staan
❌ Het taalmodel vragen om vertrouwelijke documenten "niet te delen" — wat prompt-injecties direct omzeilen
❌ Resultaten pas ná het ophalen filteren, waardoor vertrouwelijke data tijdelijk in het geheugen en de logs belandt

✅ Metadata-tags zoals `allowed_roles`, `department` en `sensitivity` gekoppeld aan elke vector bij inname
✅ Backend-handhaving die JWT-claims leest en filtert binnen dezelfde databasequery als de similarity search
✅ Lichte metadata-updates (zonder kostbare re-embeddings) zodra de rol van een medewerker wijzigt

Bij **LaunchStudio** bouwen we sinds 2014 fijnmazige autorisatie-architecturen via Manifera, met meer dan 160 gerealiseerde enterprise-projecten. 🛡️

LaunchStudio implementeerde Supabase RLS en pgvector metadata-filtering voor Penelope — klantdata werd 100% geïsoleerd en voldeed aan enterprise-beveiligingsnormen. (€2.100 (Database Tenancy Tuning Pakket) — productieklaar en binnen 5 werkdagen gedeployed). 🚀

👉 Ontdek hoe u RBAC inricht op uw vectordatabase: [Link naar artikel]

#AINativeFounder #LaunchStudio #Manifera #RBAC #VectorDatabaseSecurity #DataIsolation #Supabase #pgvector #AISaaS #StartupOpschalen
