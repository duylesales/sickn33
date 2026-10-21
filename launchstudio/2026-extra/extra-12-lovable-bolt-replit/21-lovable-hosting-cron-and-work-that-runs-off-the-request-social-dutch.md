🚨 Afspraakherinnering van Casper IJsselstein verstuurt herinneringen de avond vóór de afspraak voor 38 tandarts- en orthodontiepraktijken — zo'n 1.900 afspraken per week. In maart veranderde een deploy een afhankelijkheid en begon de nachtelijke taak op haar eerste regel te falen. Het product zag er volkomen gezond uit. 😳

Elf dagen later belde een praktijk in Bergen op Zoom: hun no-showpercentage was ongeveer verdubbeld. Zo'n 3.000 herinneringen nooit verstuurd, en meer dan 200 gemiste afspraken. Daarom faalt gepland werk stil:

❌ Eén nachtelijke cronrun die al het werk deed voor elke praktijk
❌ Een cron-endpoint dat iedereen kon aanroepen die het pad kende
❌ Eén UTC-schema — sinds de klokwissel een uur te laat
❌ Mislukkingen gelogd waar niemand keek, en geen melding als de taak gewoon niet draaide

✅ De crontaak zet nu één taak per praktijk in de rij — een mislukking raakt één praktijk, niet alle
✅ Het endpoint beschermd met een gedeeld geheim, plus een advisory lock tegen overlap
✅ Runs elk uur die de tijdzone van elke ontvanger en de openingstijden van de praktijk controleren
✅ Een runregistratie per taak, een melding als er 26 uur geen geslaagde run was, en een externe heartbeat

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring in productie-engineering, maken we de stilte hoorbaar wanneer gepland werk stopt. 🔔

💡 Het resultaat: na twee werkdagen en € 2.100 worden mislukkingen binnen uren opgemerkt, niet weken. De afwezigheidsmelding ging het jaar daarop drie keer af — en geen enkele praktijk ontdekte een gat voordat Casper dat deed. 🚀

👉 Cron en werk dat buiten het verzoek draait: https://launchstudio.eu/nl/blog/lovable-hosting-cron-and-work-that-runs-off-the-request

#Cron #Monitoring #Betrouwbaarheid #Lovable #LaunchStudio #Manifera
