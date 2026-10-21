🚨 Ledenimport van Eva Broekhuizen verzorgt de ledenadministratie voor 88 sport- en hobbyclubs, waarvan de meeste aan het begin van elk seizoen een ledenlijst importeren. 50 leden werkte. 600 werkte soms. De import werd ergens tussen rij 200 en rij 500 afgebroken — nadat de gebruiker al te horen had gekregen dat het klaar was. 😳

Clubs misten leden en importeerden opnieuw. En nog eens. Twee clubs waren een avond kwijt aan met de hand ontdubbelen. Daarom is "afvuren en vergeten" geen achtergrondwerk:

❌ Een trage functie aangeroepen zonder te wachten — afgebroken zodra het serverless antwoord was verstuurd
❌ Geen nieuwe pogingen, geen registratie van wat werd geprobeerd, geen limiet op gelijktijdigheid
❌ Opnieuw importeren voegde duplicaten toe in plaats van bij te werken
❌ Een nachtelijke taak die stilletjes stopte — en niemand die het elf dagen merkte

✅ Een takentabel in Postgres met atomair claimen, in de rij gezet in dezelfde transactie als de upload
✅ Imports opgesplitst in batches van 50, elke rij gesleuteld op het eigen lidnummer van de club, zodat opnieuw draaien veilig is
✅ Oplopende wachttijd bij tijdelijke fouten, fouten per rij bij slechte data, maximaal drie pogingen, daarna een melding
✅ Een voortgangspagina met fouten per rij, een e-mail als lange imports klaar zijn, en gepland werk op dezelfde wachtrij

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring in productie-engineering, vervangen we "gestart en gehoopt" door werk dat echt afkomt. ⚙️

💡 Het resultaat: na drie werkdagen en € 3.200 komen imports van elke omvang af — het bestand van 3.400 leden van de grootste club, dat nooit was gelukt, draaide in vier minuten over 68 taken. Tickets over dubbele leden gingen van de grootste categorie naar nul. 🚀

👉 Achtergrondwerk dat echt afkomt: https://launchstudio.eu/nl/blog/lovable-supabase-background-work-that-actually-finishes

#Supabase #Achtergrondtaken #Betrouwbaarheid #Lovable #LaunchStudio #Manifera
