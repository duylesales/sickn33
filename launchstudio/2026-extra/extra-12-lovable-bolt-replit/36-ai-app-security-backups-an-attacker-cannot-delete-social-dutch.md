🚨 Praktijkdossier van Youri Landman bevat cliëntdossiers en sessienotities voor 64 psychologen en coaches - zo'n 3.200 cliënten. Een behandelaar hergebruikte een gelekt wachtwoord. De aanvaller logde in, gebruikte een brede exportfunctie om data mee te nemen, en verwijderde daarna records in de hele praktijk. 😳

Zijn enige extra back-up stond in hetzelfde cloudaccount, met dezelfde sleutels. Het herstel duurde elf uur - en van 340 sessiebijlagen was nooit een back-up gemaakt. Ze waren weg. Dit heeft een back-up tegen een aanval echt nodig:

❌ Back-ups die te verwijderen zijn met dezelfde inloggegevens waarmee de app draait
❌ Alleen een back-up van de database - nooit van geüploade bestanden
❌ Alleen nachtelijke exports, dus tot 24 uur werk op het spel
❌ Nooit één back-up teruggezet om te zien of het werkte

✅ Een onafhankelijke back-up bij een andere provider, met een schrijfsleutel zonder verwijderrecht die de app niet heeft
✅ Object lock voor 35 dagen, met dagelijkse, wekelijkse en maandelijkse bewaring - en bijlagen meegenomen
✅ Point-in-time recovery, waardoor het mogelijke verlies daalde van 24 uur naar vijf minuten
✅ Een geschreven herstelplan, een herstel getimed op 47 minuten, meldingen bij ontbrekende of gekrompen back-ups, een ingeperkte export en 2FA voor beheerders

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring in productie-engineering, vragen we wanneer u voor het laatst een back-up hebt teruggezet - het antwoord is meestal nooit, en dat is de bevinding. 💾

💡 Het resultaat: na drie werkdagen en € 3.300 werd een reconstructie van elf uur een herstel van 47 minuten, en staan de back-ups nu waar zijn eigen inloggegevens niet bij kunnen. De 340 verloren bijlagen - en de gesprekken met betrokken cliënten - zijn waarom hij zegt dat het ertoe doet. 🚀

👉 Back-ups die een aanvaller niet kan verwijderen: https://launchstudio.eu/nl/blog/ai-app-security-backups-an-attacker-cannot-delete

#Backups #Ransomware #Gegevensbescherming #Lovable #LaunchStudio #Manifera
