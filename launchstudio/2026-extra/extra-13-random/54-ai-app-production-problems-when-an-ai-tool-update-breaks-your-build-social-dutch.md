🚨 Lars Nieuwenhuis heeft een zeilschool aan het IJsselmeer bij Hoorn en bouwde Zeilschool in Lovable: cursisten boeken cursussen, betalen met iDEAL, kiezen boottypes en krijgen weersafhankelijke bevestigingen. Een soepel seizoen, zo'n 1.100 boekingen. Toen vroeg hij Lovable in het vroege voorjaar wat tekst op de cursuspagina aan te passen. Twee dagen later belde een cursist: haar bevestiging toonde de verkeerde datum. 😳

Dezelfde bewerking had een gedeelde datumhulpfunctie opnieuw gegenereerd met een andere bibliotheek die datums in UTC las - boekingen in de avond schoven in bevestigingen en het instructeursrooster naar de volgende dag. Het lockfile was niet gecommit, en er glipte een update van de Supabase-client mee, waardoor cursisten midden in het boeken werden uitgelogd. Lovable vragen om terug te draaien leverde een derde variant met eigen problemen op. Dit doet u als een update van uw AI-tool de build breekt:

❌ Een tekstwijziging die ongemerkt gedeelde code herschreef
❌ Datums in UTC in plaats van lokale tijd
❌ Geen lockfile - afhankelijkheden die onder u veranderen
❌ "Terugdraaien" dat weer een nieuwe versie oplevert

✅ De laatst bekende goede versies hersteld uit de GitHub-geschiedenis die Lovable had gesynchroniseerd
✅ Datumafhandeling expliciet op Europe/Amsterdam gezet
✅ Lockfile en Node.js-versie gecommit en vastgezet, Dependabot achter een testpoort
✅ Tests voor boekingsdata, inloggen, betalen en bevestigingen, een stagingomgeving, en Lovable-regels die wijzigingen aan afhankelijkheden of hulpfuncties zonder expliciete opdracht verbieden

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring in productie-engineering, zorgen we dat een wijziging die meer raakt dan u vroeg uw klanten niet kan bereiken. ⚙️

💡 Het resultaat: € 1.450, vijf werkdagen. Zo'n 1.500 zomerboekingen zonder regressies in datums of inloggen - en tests hebben sindsdien twee Lovable-bewerkingen vóór productie tegengehouden. 🚀

👉 Productieproblemen met AI-Apps: Wanneer een Update van je AI-Tool de Build Breekt: https://launchstudio.eu/nl/blog/ai-app-production-problems-when-an-ai-tool-update-breaks-your-build

#Lovable #Regressie #Testen #DevOps #LaunchStudio #Manifera
