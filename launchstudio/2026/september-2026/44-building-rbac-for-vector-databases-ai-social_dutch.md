🔓 Penelope, een CRM-consultant, gebruikte **Bolt** om een AI-verkoopadviseur te bouwen — maar de app had geen scheiding op rijniveau, wat datalekken tussen klantorganisaties riskeerde. 📊

Een vectordatabase heeft geen intrinsiek begrip van "vertrouwelijk" — ze weet alleen wat wiskundig dichtbij ligt, waardoor de vraag van een stagiair net zo makkelijk het geheime memo van de CEO naar boven kan halen als een openbare FAQ. 🧠

❌ Een monolithische vectorindex waarin HR-, sales- en fusiedocumenten allemaal in dezelfde onbeperkte zoekruimte staan
❌ Het LLM zelf vragen om gevoelige documenten "niet te onthullen" — een regel die prompt-injectie moeiteloos omzeilt
❌ Resultaten pas filteren na retrieval, waardoor een gevoelig document alsnog even in geheugen en logs staat

✅ Metadatatags zoals `allowed_roles`, `department` en `sensitivity`, gekoppeld aan elke vector bij het inladen
✅ Backend-handhaving die JWT-rolclaims uitleest en filtert binnen dezelfde query als de gelijkenis-zoekopdracht
✅ Lichte metadata-updates (geen herembedding) telkens wanneer de rol of afdeling van een medewerker verandert

Bij **LaunchStudio** ontwerpen we sinds 2014, via Manifera, exact dit soort granulaire toegangsarchitectuur, over 160+ enterprise-projecten. 🛡️

Penelopes klantgegevens werden volledig geïsoleerd en voldeden aan enterprise-beveiligingsnormen. 🚀

👉 Bekijk onze vaste-scope hardeningspakketten: [Link naar artikel]

#AINativeFounder #LaunchStudio #Manifera #RBAC #VectorDatabaseSecurity
