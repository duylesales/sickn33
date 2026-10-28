🚨 Quinten Aardema bouwde Leveranciersportaal in een weekend met Bolt - een portaal waar de 90 leveranciers van een voedingsgroothandel prijslijsten, certificaten en leverschema's indienen. De groothandel vond de demo geweldig en vroeg wanneer het live kon. "Volgende week," zei hij. Het werkte. 😳

De review vóór de lancering vond de service role-sleutel in de frontend, 23 endpoints zonder controle op leverancier - dus elke leverancier kon de prijzen van elke concurrent lezen door één nummer te veranderen - en certificaten in een publieke bucket. Dit lost u op voordat een Bolt-app echte gebruikers ontmoet:

❌ Onbeperkte databasesleutels meegestuurd naar de browser
❌ Geen autorisatie: elke ingelogde gebruiker kon elk record zien
❌ Validatie alleen in de browser - negatieve prijzen en leverdatums in 1970 geaccepteerd
❌ Publieke opslag, routes zonder authenticatie, geen rate limits, en een oude preview met nog de oude sleutels

✅ De service role-sleutel vervangen, met alle datatoegang achter serverfuncties met een anonieme sleutel en policies
✅ Row-level security op alle negen tabellen en autorisatie op alle 23 endpoints
✅ Schemavalidatie op de server voor elke invoer, een privébucket voor certificaten met ondertekende URL's
✅ Rate- en groottelimieten, time-outs, de oude preview opgeheven, en een vastlegging van één pagina van wat is gecontroleerd

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring in productie-engineering, vertellen we u wat een vreemde nu met uw Bolt-project kan doen - en sluiten we het af. 🔒

💡 Het resultaat: na twee werkdagen en € 2.900 ging het portaal een week later live met 90 leveranciers en draait het inmiddels twee jaar. Die week vertraging, zegt hij, was de beste beslissing in het project. 🚀

👉 Wat u oplost voordat een Bolt-app echte gebruikers ontmoet: https://launchstudio.eu/nl/blog/bolt-security-what-to-fix-before-a-bolt-app-meets-real-users

#Bolt #Appbeveiliging #Prototyping #Supabase #LaunchStudio #Manifera
