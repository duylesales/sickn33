🚨 Mees van Rijn, voormalig officemanager in Amsterdam, bouwde Lunchlijst op Replit: bedrijven laten medewerkers lunch bestellen bij lokale cateraars, met één maandfactuur per bedrijf. In een jaar groeide het van 1.200 naar zo'n 14.000 gebruikers bij 90 bedrijven. De omzet groeide ongeveer tienvoudig. De infrastructuurkosten groeiden zo'n vijfentwintigvoudig — tot € 2.300 per maand. 😳

De kostenreview herleidde het tot vijf gewoonten: de menupagina pollde elke vijf seconden voor elk open tabblad; foto's van cateraars werden in volle cameraresolutie geleverd; een AI-"lunchsuggestie" riep bij elke paginaweergave een taalmodel aan; de query voor de bestelgeschiedenis had geen index en dwong een groter databaseniveau af; en logs legden elke verzoekbody vast, menu's inbegrepen. Dit kost de schaalbaarheid van AI-applicaties werkelijk bij 1.000, 10.000 en 100.000 gebruikers:

❌ Polling vanuit elk open tabblad
❌ Afbeeldingen in volle resolutie op elke pagina
❌ Een LLM-aanroep bij elke paginaweergave
❌ Ontbrekende indexen en opgeblazen logs

✅ Polling vervangen door gefilterde realtime updates
✅ Afbeeldingen verkleind en gecachet via een CDN
✅ AI-suggesties op aanvraag, dagelijks gecachet per bedrijf
✅ Indexen en paginering, beperkte logging, maandfacturatie in achtergrondtaken — en een dashboard met kosten per actieve gebruiker

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring in productie-engineering, zorgen we dat elke nieuwe klant u winstgevender maakt, niet minder. ⚙️

💡 Het resultaat: € 3.600 in twaalf werkdagen, plus € 49/maand. De maandelijkse infrastructuurkosten daalden naar zo'n € 520 terwijl het aantal gebruikers bleef groeien, de kosten per actieve gebruiker daalden met ongeveer 80%, en Lunchlijst ging voorbij de 20.000 gebruikers met infrastructuur onder 5% van de omzet. 🚀

👉 Schaalbaarheidskosten van AI-Applicaties bij 1.000, 10.000 en 100.000 Gebruikers: https://launchstudio.eu/nl/blog/ai-application-scalability-costs-at-1000-10000-and-100000-users

#Schaalbaarheid #Cloudkosten #Replit #SaaS #LaunchStudio #Manifera
