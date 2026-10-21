🚨 Leerlingvervoer van Ruben Hooghiemstra plant het vervoer van zo'n 600 leerlingen in het speciaal onderwijs, voor zeven vervoerders. Het project begon als een openbaar Replit-template waarvan hij leerde. In die vier openbare maanden plakte hij een database-connection string in een configuratiebestand — en vergat het. Achttien maanden later vond een routinereview hem nog steeds. Het project was elf keer geforkt. 😳

De database bevatte namen, adressen, scholen en vervoersbehoeften van leerlingen. Zo verspreiden inloggegevens zich in een gedeeld Replit-project — en zo roteert u ze zonder iets te breken:

❌ Een project dat openbaar bleef zonder dat iemand dat besloot
❌ Een connection string in een bestand in plaats van in het secrets-mechanisme — bestanden reizen mee met elke fork
❌ Vier oud-medewerkers die nog steeds toegang hadden
❌ Eén gedeelde beheerderssleutel voor alles

✅ Database-inloggegevens als eerste geroteerd; de projectgeschiedenis doorzocht op waarde, wat ook een e-mailsleutel opleverde
✅ De elf forks geïdentificeerd en het platform benaderd over de twee openbare
✅ Beperkte inloggegevens per integratie, ontwikkeling en productie echt gescheiden, een inventaris van zeven inloggegevens
✅ Een gedocumenteerde beoordeling van het datalek — en melding aan de vervoerders en de Autoriteit Persoonsgegevens

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring in productie-engineering, is de hygiëne van inloggegevens consequent onze eerste bevinding bij het naar productie brengen van een Replit-project. ⚙️

💡 Het resultaat: € 2.900, twee werkdagen. Logs toonden geen bewijs van toegang — en omdat de vervoerders het eerst rechtstreeks van Ruben hoorden, bleven alle zeven. 🚀

👉 Replit Secrets: sleutels roteren in een gedeeld project: https://launchstudio.eu/nl/blog/replit-secrets-rotating-keys-on-a-shared-project

#Replit #AppSecurity #AVG #SecretsManagement #LaunchStudio #Manifera
