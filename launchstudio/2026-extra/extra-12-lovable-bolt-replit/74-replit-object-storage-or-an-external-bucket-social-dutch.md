🚨 Met Keuringsdossier van Freek Batenburg uploaden keurmeesters van liften en machines foto's en ondertekende rapporten vanaf locatie - zes bedrijven, zo'n 3.200 objecten. Uploads gingen naar een map in het Replit-project. Vier maanden werkte dat. Toen deployde hij op een dinsdagmiddag, en elf dagen aan keuringsdocumenten - zo'n 340 bestanden - waren gewoon weg. 😳

Geen fout, niets in welke log dan ook. De database noemde nog elk document, dus het product toonde 340 bijlagen die een fout gaven bij openen. En er was geen back-up. Hier horen gebruikersbestanden op Replit echt te staan:

❌ Uploads naar het bestandssysteem van de container - dat elke deployment vervangt
❌ Databaseback-ups waar de bestanden nooit in zaten
❌ Geen typecontrole: de upload accepteerde alles
❌ Records die naar bestanden verwijzen zonder dat iets ze gelijk houdt

✅ Object storage achter één opslagmodule, met paden (geen URL's) in de database
✅ Een indeling met de eigenaar voorop - bedrijf, object, gegenereerde bestands-ID - in privé-buckets met kortlevende signed URLs
✅ Type gecontroleerd op bestandsinhoud, limieten van 20 MB, en een register met uploader, tijdstip, pad, grootte en type
✅ Een back-up van de bucket naar een apart account, met een getest herstel

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring in productie-engineering, zijn bestanden op het bestandssysteem een van de meest voorkomende bevindingen wanneer we Replit-producten naar productie brengen. ⚙️

💡 Het resultaat: € 2.800, drie werkdagen. Zo'n 260 van de 340 bestanden werden teruggehaald uit de eigen kopieën van de bedrijven - en uploads kunnen niet meer verdwijnen met een deploy. 🚀

👉 Replit Object Storage of een externe bucket: https://launchstudio.eu/nl/blog/replit-object-storage-or-an-external-bucket

#Replit #ObjectStorage #Bestandsuploads #DevOps #LaunchStudio #Manifera
