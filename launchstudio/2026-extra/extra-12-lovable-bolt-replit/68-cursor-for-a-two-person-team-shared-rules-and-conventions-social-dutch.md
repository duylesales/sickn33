🚨 Steven Doornekamp en zijn medeoprichter bouwden Zorgdeclaratie in Cursor — declaratieverwerking tussen 52 paramedische praktijken en verzekeraars. Ze verdeelden het werk per functie en bouwden vier maanden parallel. Geen regelbestand, geen review. Eind december gingen er 60 declaraties met de verkeerde periode uit en wezen twee verzekeraars ze af. 😳

De oorzaak: elke helft berekende weeknummers met een andere datumbibliotheek — en die waren het oneens. Eén repository, twee producten erin. Zo houdt een team van twee AI-editors aan één codebase bouwen:

❌ Twee datumbibliotheken, twee aanpakken voor formulieren, twee validatiebibliotheken in één repo
❌ Fouten in de ene helft gegooid en in de andere als waarde teruggegeven
❌ Tabelnamen in meervoud aan de ene kant, enkelvoud aan de andere
❌ Geen van beide oprichters kon in de helft van de ander werken — een week ziekte legde half het product stil

✅ Een regelbestand samen geschreven in een middag, op basis van de echte code: één bibliotheek per taak, vijf nooit te breken regels
✅ De verliezende bibliotheken verwijderd; datumafhandeling geüniformeerd met een test vanuit de specificatie van de verzekeraar
✅ Elke wijziging via een pull request met een diffreview van vijf minuten door de ander
✅ Eén gedeelde woordenschat — declaratie, praktijk, verzekeraar, periode — in plaats van drie sets synoniemen

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring in productie-engineering, schrijven we dit regelbestand wanneer we een project aan een klantteam overdragen — het houdt het werk consistent als wij weg zijn. ⚙️

💡 Het resultaat: € 3.100, drie werkdagen. De 60 declaraties werden opnieuw ingediend — en toen zijn medeoprichter twee weken weg was, ging het product gewoon door. 🚀

👉 Cursor voor een team van twee: gedeelde regels en afspraken: https://launchstudio.eu/nl/blog/cursor-for-a-two-person-team-shared-rules-and-conventions

#Cursor #KleineTeams #CodeReview #AICoding #LaunchStudio #Manifera
