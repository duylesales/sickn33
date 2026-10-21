🚨 Hypotheekmap van Bram Nieuwenhuijs verzamelt loonstroken, arbeidscontracten, bankafschriften en identiteitsbewijzen voor 26 hypotheekadviseurs en zo'n 400 klanten. Een klant kopieerde de URL van zijn eigen loonstrook, verving de achternaam door die van een vriend — en het arbeidscontract van de vriend werd geladen. 😳

Er kwam geen hacken aan te pas. De bestandsnaamgeving was de kwetsbaarheid. Zo lekken storage buckets in door AI gebouwde apps:

❌ Een publieke bucket — leesbaar voor iedereen met de URL, zonder login, zonder verloopdatum
❌ Bestanden genoemd naar achternaam en documenttype, dus de bucket was af te lopen
❌ Permanente links in al verstuurde e-mails
❌ Het verwijderen van een account verwijderde nooit de opgeslagen bestanden

✅ Een privébucket met policies op het organisatiesegment van het pad
✅ 1.247 bestanden gemigreerd naar paden adviseur/klant/document met gegenereerde ID's, plus een documententabel
✅ Ondertekende URL's op de server: 15 minuten om te bekijken, een uur om te downloaden
✅ Uploadvalidatie op het echte contenttype (limiet 25 MB), 180 oude links ongeldig gemaakt, en verwijderen dat ook de bestanden wist

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring in productie-engineering, controleren we eerst uw bucketinstellingen — dat kost tien minuten en daar zit meestal het lek. 🔒

💡 Het resultaat: na drie werkdagen en € 3.300 was het lek binnen de week gedicht. Bram meldde het bij de Autoriteit Persoonsgegevens en informeerde elke betrokken adviseur en klant — twee adviseurs zeiden dat die transparantie de reden was dat ze bleven. 🚀

👉 Storage buckets en wie wat mag lezen: https://launchstudio.eu/nl/blog/lovable-supabase-storage-buckets-and-who-can-read-what

#Supabase #Databeveiliging #AVG #Lovable #LaunchStudio #Manifera
