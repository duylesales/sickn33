🚨 Tessa Oomen draaide Wachtlijst op Replit — een intake- en wachtlijsttool voor drie fysiotherapiepraktijken rond Tiel. Aanmeldingen werden opgeslagen in een bestand binnen het project. Elke redeploy wiste stilletjes alles sinds de vorige. Zo'n 40 mensen die op zorg wachtten raakten in zes weken zoek. 😳

Een bestand in uw project gedraagt zich als een database, tot het moment dat het dat niet meer doet. Hier breekt de datalaag:

❌ Gegevens opslaan binnen het project, waar elke redeploy ze wist
❌ Geen toegangsregels, waardoor de ene praktijk in principe patiënten van een andere kon zien
❌ Directe verbindingen die bij zo'n veertig gelijktijdige aanmeldingen falen
❌ Back-ups die nooit iemand heeft teruggezet

✅ Een echte database (Supabase, EU-regio) met één tabel per onderwerp
✅ Toegangsregels getest door in te loggen als twee verschillende klanten
✅ Pooled connections, met een loadtest vóór het drukke seizoen
✅ Het schema vastgelegd in migraties — en een restore gemeten, niet aangenomen

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring in productie-engineering, koppelen we Replit-apps aan een database die een deploy overleeft. 🗄️

💡 Het resultaat: in zes werkdagen en voor € 3.200 werd de datalaag opnieuw opgezet, gingen uploads naar object storage en werd een restore gemeten op 17 minuten. In de elf maanden daarna ging er niets meer verloren — ook niet in een september met meer aanmeldingen per week dan het oude systeem in zes weken kwijtraakte. 🚀

👉 Zo koppelt u Replit aan een database die blijft staan: https://launchstudio.eu/nl/blog/replit-and-supabase-wiring-a-database-that-survives

#Replit #Supabase #Dataverlies #Zorgtech #LaunchStudio #Manifera
