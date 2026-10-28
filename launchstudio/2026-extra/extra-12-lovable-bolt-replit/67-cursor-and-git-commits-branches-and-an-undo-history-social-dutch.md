🚨 Praktijkfacturatie van Karin Zoetelief verzorgt de facturatie aan verzekeraars en patiënten voor 41 paramedische praktijken. Vijf maanden bouwde ze in Cursor zonder versiebeheer. Toen brak één sessie over declaratiecodes van verzekeraars dingen in het hele project - en ze kon niet terug. 😳

Prompten maakte het erger. Bestanden terugzetten uit de cloudsynchronisatie gaf een mengeling van oude en nieuwe code. Ze herbouwde drie dagen werk met de hand. Dit is het minimale versiebeheer dat een solo-oprichter met AI nodig heeft:

❌ Geen repository - alleen een map met cloudsynchronisatie van losse bestanden
❌ Een AI-sessie ongedaan proberen te maken door de AI te prompten
❌ Testexports met echte patiëntgegevens die vijf maanden naar een cloudaccount synchroniseerden
❌ Inloggegevens in de projectmap

✅ Een repository met een eerste commit, gepusht naar een gehoste remote
✅ Een ignore-bestand voor env-bestanden, builduitvoer en data - en de twee blootgestelde inloggegevens geroteerd
✅ Een branch per wijziging, verwijderd in plaats van gered als een sessie misgaat
✅ Een absolute regel: commit vóór elke AI-sessie

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring in productie-engineering, is versiebeheer het eerste wat we inrichten bij het overnemen van een project - niets anders is veilig zonder. ⚙️

💡 Het resultaat: € 1.300, twee werkdagen. De wijziging van de declaratiecodes kostte een middag op een branch - en in het jaar daarna gooide ze 23 mislukte sessies weg, elk in een paar seconden. 🚀

👉 Cursor en Git: commits, branches en een ongedaan-maakgeschiedenis: https://launchstudio.eu/nl/blog/cursor-and-git-commits-branches-and-an-undo-history

#Git #Cursor #Versiebeheer #AICoding #LaunchStudio #Manifera
