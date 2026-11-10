🚨 Tim Hoogland bouwde Vrijwilligersrooster met Bolt en Supabase: festivalorganisatoren publiceren vrijwilligersdiensten, vrijwilligers claimen ze in ruil voor gratis tickets. Een groot zomerfestival bij Nijmegen wilde 4.000 diensten openzetten om precies 10:00 op een zaterdag - aangekondigd aan zo'n 9.000 vrijwilligers. Tim had nooit meer dan ongeveer 40 mensen tegelijk in de app gezien. 😳

Een piektest op staging vertelde het verhaal: bij zo'n 600 gelijktijdige gebruikers duurde de dienstenlijst meer dan 12 seconden en begonnen claims te falen. Daarom doet u een loadtest vóór de lancering van een door AI gebouwde app: 🧠

❌ Elke gebruiker laadde alle 4.000 diensten met hun claims
❌ Een RLS-policy die per rij teams opvroeg, zonder indexen
❌ Claims gecontroleerd in de browser, zodat twee vrijwilligers de laatste plek konden pakken
❌ Bevestigingsmails synchroon verstuurd bij elke claim

✅ De dienstenlijst gepagineerd per dag en team, met alleen de nodige kolommen
✅ Samengestelde indexen en een geïndexeerde lidmaatschapscheck in de policy
✅ Claims via een databasefunctie met rijvergrendeling - overboeking onmogelijk
✅ E-mails in een achtergrondwachtrij, connection pooling en een hertest bij 1.500 gebruikers onder 800 ms

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring in productie-engineering, vinden we het breekpunt voordat uw klanten het vinden. 🛠️

💡 Het resultaat: €4.300, 10 werkdagen. Op de dag zelf openden zo'n 5.200 vrijwilligers de app in tien minuten, en alle 4.000 diensten waren binnen 47 minuten geclaimd - zonder overboeking of storing. 🚀

👉 Verwacht u een piek in bezoekers? Zo doet u een loadtest op uw door AI gebouwde app: https://launchstudio.eu/nl/blog/load-testing-an-ai-built-app-before-launch

#LoadTesting #Supabase #Performance #EventTech #AIFounder #LaunchStudio #Manifera
