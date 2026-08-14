🕵️ Zoey, een onderzoeker, bouwde een document-zoekapplicatie met **Cursor** — totdat gebruikers haar veiligheidsregels omzeilden met prompt-injecties om vertrouwelijke databasevelden van anderen te downloaden. 📄

RAG-pipelines zoeken op wiskundige overeenkomst, niet op gebruikersrechten. Beveiliging moet daarom worden afgedwongen op de ophaallaag, nooit in de prompt. 🧠

❌ Een junior medewerker die de chatbot vraagt "vat het ontslagplan voor Q4 samen" en direct antwoord krijgt
❌ Systeemprompts zoals "deel geen HR-data" — die binnen enkele seconden worden omzeild via prompt-injectie
❌ Eén ontbrekend `tenant_id` filter dat leidt tot een fataal datalek tussen verschillende zakelijke klanten

✅ Document-niveau metadata-filtering: elke vector taggen met afdeling, autorisatieniveau en tenant-ID
✅ Backend JWT-controles die afdwingen dat de database uitsluitend geautoriseerde documenten retourneert
✅ Structurele scheiding per klant via aparte namespaces of databaseschema's

Bij **LaunchStudio** bouwen we sinds 2014 enterprise data-isolatie via Manifera, met meer dan 160 gerealiseerde projecten voor opdrachtgevers zoals Vodafone en TNO. 🛡️

LaunchStudio implementeerde metadata-filtering en invoervalidaties voor Zoey — prompt-injecties werden geneutraliseerd en document-isolatie is nu 100% gegarandeerd. (€1.950 (Vector Security Pakket) — productieklaar en binnen 5 werkdagen gedeployed). 🚀

👉 Ontdek hoe u uw RAG-architectuur beveiligt: [Link naar artikel]

#AINativeFounder #LaunchStudio #Manifera #RAGSecurity #DataExfiltration #VectorDatabase #PromptInjection #CyberSecurity #AISaaS #StartupOpschalen
