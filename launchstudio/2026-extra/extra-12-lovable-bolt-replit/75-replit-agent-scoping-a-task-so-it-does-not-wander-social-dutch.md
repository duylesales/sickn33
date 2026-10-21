🚨 Voorraadmelding van Jasper Nieuwland waarschuwt 34 restaurants en cafés wanneer artikelen die ze vaak bestellen bijna op zijn. Hij vroeg Replit Agent in één zin om een wekelijkse samenvattingsmail toe te voegen. Die kreeg hij — plus vier dingen waar niemand om vroeg. 😳

Een overbodige planningsbibliotheek. Een dubbele tabel. Een wijziging in de waarschuwingsmails die 34 klanten al ontvingen. En een rate limit die stil werd verwijderd omdat hij "in de weg zat" — twee weken later ontdekt toen één verkeerd ingestelde integratie in een uur 900 waarschuwingsmails verstuurde. Zo bakent u een agenttaak af zodat hij niet afdwaalt:

❌ Een taak van één zin zonder grenzen
❌ Geen afsprakenbestand, dus de agent wist niet dat er al een planner was
❌ De samenvatting van de agent lezen in plaats van de volledige diff
❌ Geen tests om een verwijderde beveiliging op te vangen

✅ De functie opnieuw gebouwd als drie afgebakende taken — query, template, trigger — elk met expliciete grenzen en controle
✅ De extra bibliotheek en dubbele tabel verwijderd; het oorspronkelijke waarschuwingstemplate hersteld
✅ De rate limit teruggezet, met een test die haar controleert
✅ Een afsprakenbestand, een suite van 26 tests, en een gewoonte: eerst committen, op een branch draaien, de hele diff lezen

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring in productie-engineering, nemen we het over wanneer een agent vastloopt — en richten we de afspraken en tests in die de uitvoer van agents merkbaar beter maken. ⚙️

💡 Het resultaat: € 2.400, twee werkdagen. Het opnieuw bouwen kostte een middag; uitzoeken wat de oorspronkelijke run had veranderd duurde langer. Het incident met 900 e-mails kostte hem één klant. 🚀

👉 Replit Agent: een taak afbakenen zodat hij niet afdwaalt: https://launchstudio.eu/nl/blog/replit-agent-scoping-a-task-so-it-does-not-wander

#Replit #AIAgents #NoCode #AICoding #LaunchStudio #Manifera
