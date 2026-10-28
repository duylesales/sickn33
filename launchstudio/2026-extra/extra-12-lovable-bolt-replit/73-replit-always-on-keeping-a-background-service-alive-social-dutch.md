🚨 Innametool van Annemarie Poortvliet herinnert zo'n 4.000 patiënten in zes apotheken eraan wanneer een herhaalrecept eraan komt. De herinneringslogica draaide in een lus binnen haar Replit-webapp. Op drukke dagen werkte het. Op rustige nachten ging de app slapen - en herinneringen tussen 2 en 7 uur 's ochtends werden nooit verstuurd. Toen niet, en later ook niet. 😳

Ze ontdekte het pas toen een apotheek haar eigen receptgegevens vergeleek met de verstuurde herinneringen en een consequent gat zag. Zo houdt u achtergrondwerk op Replit in leven:

❌ Een planningslus binnen een autoscale-webapp - die stopt zodra de app slaapt
❌ Een taak die alleen vroeg "wat is nu aan de beurt?", waardoor gemiste vensters voorgoed verloren gingen
❌ Tellers in het geheugen die stil werden gereset en haar verzendstatistieken vertekenden
❌ Op het punt een reserved instance te kopen om het probleem af te dekken

✅ Herinneringen verplaatst naar een geplande deployment die elke 15 minuten draait
✅ De taak herschreven om alles te verwerken sinds de laatste geslaagde run - gemiste vensters worden automatisch ingehaald
✅ De wachtrij in de database, idempotent op patiënt en recept, zodat herhaalde runs nooit dupliceren
✅ Runregistraties, een waarschuwing als de taak binnen een uur niet is geslaagd, en externe uptimemonitoring

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring in productie-engineering, brengen we Replit-producten naar productie - en verlagen we vaak de rekening door altijd-aan-instances te vervangen door gepland werk. ⚙️

💡 Het resultaat: € 2.200, twee werkdagen. Binnen twee weken legde een platformincident de taak drie uur stil - de volgende run haalde alles in en geen patiënt miste een herinnering. De kosten gingen licht omlaag in plaats van omhoog. 🚀

👉 Replit Always-On: een achtergronddienst in leven houden: https://launchstudio.eu/nl/blog/replit-always-on-keeping-a-background-service-alive

#Replit #Achtergrondtaken #DevOps #Zorgtech #LaunchStudio #Manifera
