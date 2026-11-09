🐢 Thijs Kuipers leidt een facilitair bedrijf in Amersfoort en bouwde Roosterpunt met Bolt en Supabase om schoonmaakdiensten op 140 locaties te plannen. In het begin laadde het planningsdashboard direct. Een jaar en tienduizenden diensten later duurde het zo'n elf seconden, en leidinggevenden waren roosters gaan uitprinten. 🖨️

Hij stond klaar om voor een grotere server te betalen. De metingen vertelden een ander verhaal: 🧠

❌ Elke dienst ooit aangemaakt opgehaald, daarna in de browser gefilterd op deze week
❌ Elke locatiekaart deed een eigen verzoek: 100+ verzoeken per keer laden
❌ Een Row Level Security-policy die voor elke rij een subquery uitvoerde
❌ Pdf-exports binnen het verzoek, waardoor het scherm een halve minuut bevroor

✅ Filteren verplaatst naar de database, met indexen op locatie en datum
✅ Eén gekoppelde query in plaats van honderd kleine
✅ De policy herschreven met een geïndexeerde opzoektabel
✅ Pdf-exports op de achtergrond, lichtere afbeeldingen, twee ongebruikte libraries weg en meldingen voor trage query's

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring met systemen voor klanten zoals Vodafone en TNO, meten we eerst, repareren we de grootste oorzaken en bewijzen we het resultaat met cijfers van vóór en na. 🛠️

💡 Het resultaat: €2.300, zes werkdagen. Het dashboard laadt in minder dan een seconde met de volledige geschiedenis, leidinggevenden kwamen binnen een week terug en de database-upgrade was niet nodig. 🚀

👉 Prestatieoptimalisatie voor apps gebouwd met AI: https://launchstudio.eu/nl/blog/ai-app-performance-optimisation-service

#Prestaties #Supabase #Bolt #CoreWebVitals #AIFounder #LaunchStudio #Manifera
