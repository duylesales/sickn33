🕵️ Zoey, een onderzoeker, gebruikte **Cursor** om een documentzoektool te bouwen — totdat gebruikers haar veiligheidsregels begonnen te omzeilen met prompt-injecties om vertrouwelijke databasevelden te downloaden. 📄

RAG-pijplijnen zoeken op wiskundige gelijkenis, niet op autorisatie — dus beveiliging moet worden afgedwongen op de retrievallaag, niet in de prompt. 🧠

❌ Een junior medewerker die de chatbot vraagt om "het Q4-ontslagplan samen te vatten" — en dat gewoon krijgt
❌ Instructies in de systeemprompt zoals "onthul geen HR-gegevens" — triviaal te omzeilen met prompt-injectie
❌ Eén ontbrekend `tenant_id`-filter dat 's nachts verandert in een datalek tussen bedrijven

✅ Metadatafiltering op documentniveau — elke vector taggen met `department`, `clearance_level` en `tenant_id`
✅ Backend-JWT-controles die de databasequery dwingen alleen documenten te retourneren waarvoor de gebruiker geautoriseerd is
✅ Structurele tenant-isolatie via aparte namespaces of schema's, zodat een ontbrekend filter juist blokkeert in plaats van doorlaat

Bij **LaunchStudio** bouwen we sinds 2014, via Manifera, exact dit soort tenant-geïsoleerde infrastructuur, met 11+ jaar ervaring over 160+ enterprise-projecten. 🛡️

Zoeys prompt-injectiepogingen werden geblokkeerd, en de documentisolatie van haar gebruikers is nu volledig beveiligd. 🚀

👉 Bereken de beveiliging van uw eigen RAG-systeem: [Link naar artikel]

#AINativeFounder #LaunchStudio #Manifera #RAGSecurity #DataExfiltration
