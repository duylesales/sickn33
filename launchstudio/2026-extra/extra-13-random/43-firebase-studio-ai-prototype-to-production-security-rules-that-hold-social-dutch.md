🚨 Chiara Rossi, muziekdocent en koordirigent in Dordrecht, bouwde Koorplanner in Firebase Studio: amateurkoren plannen repetities, delen bladmuziek en opnames, houden aanwezigheid bij en innen contributie. Binnen een seizoen 140 koren en zo'n 4.000 zangers. Toen verdrievoudigde in één week haar Firebase-rekening — en liet een koorlid uit de IT zien dat hij de ledenlijst van elk koor kon lezen. 😳

Na het verlopen van de testmodus waren de regels ingesteld op "ingelogde gebruikers mogen alles lezen en schrijven". Namen, telefoonnummers en adressen lagen open tussen koren, gelicentieerde bladmuziek was door iedereen te downloaden, leden konden hun eigen contributie als betaald markeren, en het aanwezigheidsscherm luisterde realtime naar de hele collectie. Zo brengt u een Firebase Studio-prototype naar productie met regels die standhouden:

❌ "Ingelogd" behandeld als "gemachtigd voor alles"
❌ Open opslag voor gelicentieerde bestanden
❌ Betaalstatus geschreven door de client
❌ Listeners op hele collecties die de rekening opdrijven

✅ Firestore- en Storage-regels herschreven op basis van standaard weigeren, afgebakend op koorlidmaatschap en rollen — met 48 emulatortests in CI
✅ Contributiestatus alleen bijgewerkt door een Cloud Function na geverifieerde betaalwebhooks
✅ App Check aangezet en de listener vervangen door een afgebakende, gepagineerde query
✅ Budgetmeldingen en geplande back-ups met een geteste restore

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring in productie-engineering, zorgen we dat de regels achter uw openbare config echt een slot op de deur zijn. ⚙️

💡 Het resultaat: € 1.500, zes werkdagen. Toegang tussen koren was dicht op de dag dat de regels live gingen, de Firebase-rekening daalde zo'n 70% ten opzichte van de piek, en Koorplanner groeide het seizoen daarna naar 230 koren. 🚀

👉 Firebase Studio AI-Prototype naar Productie: Beveiligingsregels Die Standhouden: https://launchstudio.eu/nl/blog/firebase-studio-ai-prototype-to-production-security-rules-that-hold

#Firebase #SecurityRules #Firestore #AppSecurity #LaunchStudio #Manifera
