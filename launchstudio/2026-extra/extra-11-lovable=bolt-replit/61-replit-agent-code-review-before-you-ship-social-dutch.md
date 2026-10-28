🚨 Freek Wiersma vroeg de Replit-agent om PDF-export toe te voegen aan Werkbriefje, een werkbontool voor vier installatiebedrijven rond Zutphen. Binnen twintig minuten klaar en het werkte meteen. Hij zette het live zonder de lijst met wijzigingen te lezen. Drie weken later startte het project niet meer. 😳

De agent had elf packages geïnstalleerd - waaronder een complete headless browser, alleen om een PDF te maken. Dit raakt een agentsessie werkelijk aan:

❌ Packages waar u nooit om vroeg, sommige zwaar genoeg om het geheugenbudget te overschrijden
❌ Gegenereerde bestanden naast de app, waar de volgende rebuild ze wist
❌ Een licentiesleutel in een bestand dat in het project is vastgelegd
❌ Meerdere losse wijzigingen verpakt in één melding "klaar"

✅ Eén verzoek per agentsessie, zodat elke wijzigingslijst leesbaar blijft
✅ Lees de nieuwe packages, bestanden en instellingen vóórdat u accepteert
✅ Bewaar gegenereerde bestanden in externe opslag, nooit naast de code
✅ Secrets alleen in secret storage - en vervang alles wat ooit in de repository stond

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring in productie-engineering, controleren we wat de agent bouwde vóórdat uw klanten het vinden. 🔍

💡 Het resultaat: in vijf werkdagen en voor € 2.200 werden negen packages verwijderd, de PDF-pipeline lichter opgebouwd, bestanden naar object storage verplaatst en de sleutel vervangen. De opstarttijd is weer normaal - en het lezen van de wijzigingslijst kost Freek nu twee minuten per sessie. 🚀

👉 De reviewroutine voor door agents gegenereerde code: https://launchstudio.eu/nl/blog/replit-agent-code-review-before-you-ship

#Replit #AIAgents #CodeReview #VibeCoding #LaunchStudio #Manifera
