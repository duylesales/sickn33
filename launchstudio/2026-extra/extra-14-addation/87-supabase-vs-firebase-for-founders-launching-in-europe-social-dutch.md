🚨 Mark Peeters bouwde Clubbeheer met FlutterFlow en Firebase: een mobiele app voor amateursportclubs. Chat en live wedstrijdupdates werkten prachtig. Toen wilden penningmeesters overzichten van de contributie per team en seizoen - waarvoor duizenden documenten moesten worden gelezen en aan elkaar gezet. De kosten van Firebase schoten omhoog bij elk rapport, en een te ruime Security Rule liet elk lid de betaalstatus van elk ander lid lezen. 😳

Firebase was perfect voor de live onderdelen van zijn app. Zijn penningmeesters hadden een database nodig die kon optellen. Dit ging er mis:

❌ Relationele rapportages in een documentdatabase geperst
❌ Duizenden leesacties per rapport, en een maandrekening die daarmee omhoogschoot
❌ Rapporten die ongeveer een minuut nodig hadden om te laden
❌ Een Security Rule die de betaalstatus van elk lid blootstelde

✅ Security Rules hersteld: leden zien hun eigen betalingen, penningmeesters die van hun club
✅ Firebase behouden voor de realtime functies van de app
✅ Een nachtelijke synchronisatie van financiële gegevens naar PostgreSQL in Supabase in Frankfurt
✅ Rapporten voor penningmeesters als SQL-views in een klein webdashboard, plus monitoring

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring met relationele en documentdatabases, kiezen we backends op basis van de vorm van de gegevens, de locaties van gebruikers en de vaardigheden van het team - niet op basis van wat de builder standaard koos. 🛠️

💡 Het resultaat: €4.300, twaalf werkdagen. De kosten voor leesacties in Firebase daalden sterk, rapporten laden nu in seconden, en penningmeesters van 22 clubs gebruiken het dashboard aan het einde van het seizoen. 🚀

👉 Supabase of Firebase voor een lancering in Europa? Dit is de praktische vergelijking: https://launchstudio.eu/nl/blog/supabase-vs-firebase-for-founders-launching-in-europe

#Supabase #Firebase #PostgreSQL #AVG #LaunchStudio #Manifera
