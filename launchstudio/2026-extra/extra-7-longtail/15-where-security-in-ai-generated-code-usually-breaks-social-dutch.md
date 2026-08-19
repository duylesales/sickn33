🚨 Het bureau van Lukas Reindl in Wenen stond op het punt om de fysiotherapie-planningsapp "PatientPing" van een klant onder eigen naam live te zetten — totdat een pre-launch review ontdekte dat de plannings-API volledige patiëntendossiers, inclusief telefoonnummers en notities van therapeuten, overhandigde aan elke geauthenticeerde gebruiker, en niet alleen aan de toegewezen therapeut. 😳

Een eenvoudige functionele test vond niets vreemds. Er was een echte beveiligingsreview voor nodig om het daadwerkelijke risico te ontdekken. 🧠

❌ De plannings-API retourneerde complete patiëntendossiers aan elke geauthenticeerde gebruiker, niet alleen aan de therapeut die aan die patiënt was toegewezen
❌ Geen rate limiting op het afspraakboekingseindpunt, waardoor het openstond voor spam met valse boekingen
❌ Een overgebleven intern debugging-eindpunt uit het bouwproces van Bolt was nog steeds bereikbaar in productie en dumpte de ruwe afsprakentabel op verzoek

✅ Rolgebaseerde autorisatie toegevoegd zodat therapeuten alleen hun eigen toegewezen patiënten kunnen opvragen
✅ Interne notities verwijderd uit elke API-respons die de frontend bereikt
✅ Rate limiting toegevoegd aan de boekingsstroom en het blootgestelde debugging-eindpunt gesloten

Bij **LaunchStudio** zijn white-label beveiligingsbeoordelingen voor bureaus die door AI gebouwd klantwerk overnemen vaste praktijk — Manifera's technici, vertrouwd door organisaties als Vodafone, TNO en CFLW, coördineren de levering via het team in Singapore aan Tras Street. 🛡️

Lukas' resultaat: de fix werd opgeleverd onder de eigen branding van zijn bureau — zijn klant heeft nooit geweten dat er een gespecialiseerde partner bij betrokken was. 🚀

👉 Neemt u AI-prototypes van klanten aan onder de naam van uw eigen bureau? Ken deze checklist vooraf: [Link naar artikel]

#AINativeFounder #LaunchStudio #Manifera #WhiteLabel #AppSecurity
