🚨 Offerteroute van Marnix Oosterveld beheert offertes voor 61 keuken- en badkamerinstallateurs — zo'n 900 per maand. Klanten begonnen twee exemplaren van elke offerte te ontvangen, sommige om drie uur 's nachts. Twee antwoordden op beide, en één discussieerde over een prijs die tussen de versies was veranderd. 😳

Niets in zijn code verstuurde een tweede e-mail. Een databasetrigger deed dat — acht maanden eerder geschreven door een AI-sessie, in een chat die hij zich niet herinnerde. Dit verstopt zich in een door AI gebouwd Supabase-schema:

❌ Elf triggers die niemand kon uitleggen — twee dupliceerden applicatielogica
❌ Een trigger die een externe webhook aanriep binnen een transactie, met time-outs als gevolg
❌ Drie triggers die vuurden op tabellen die al waren vervangen
❌ Een security definer-functie die de offertes van elk bedrijf teruggaf aan elke ingelogde gebruiker

✅ Elke functie en trigger geïnventariseerd en in één zin beschreven
✅ E-mail- en webhookwerk verplaatst naar applicatiecode, waar het opnieuw kan worden geprobeerd en gelogd
✅ De security definer-functie herschreven met een expliciete lidmaatschapscontrole en een vast zoekpad
✅ Triggers voor tijdstempels en tellers behouden en gedekt door SQL-tests — en het hele schema gecommit als basismigratie

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring in productie-engineering, vinden we wat uw database doet dat uw code nooit noemt. 🗄️

💡 Het resultaat: na drie werkdagen en € 2.700 hielden de dubbele e-mails en de wisselende time-outs op, en werd de blootgestelde functie gedicht voordat iemand haar gebruikte. Marnix heeft nu een document van twee pagina's dat uitlegt wat zijn database uit zichzelf doet. 🚀

👉 Databasefuncties en triggers die het bewaren waard zijn: https://launchstudio.eu/nl/blog/lovable-supabase-database-functions-and-triggers-worth-keeping

#Supabase #PostgreSQL #Databaseontwerp #Lovable #LaunchStudio #Manifera
