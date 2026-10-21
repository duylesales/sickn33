🚨 Zorgdossier van Gerlof Tichelaar beheert zorgplannen voor 26 kleinschalige woonzorgaanbieders — zo'n 1.400 bewoners. Toen bood een regionale zorggroep een contract aan voor negen locaties, meer waard dan zijn bestaande omzet. Hun inkoop eiste een specifieke regio, certificering en contractvoorwaarden die zijn Supabase-plan niet bood. 😳

Hij vroeg het eerst aan Supabase — de stap die de meeste oprichters overslaan. Een deel was op te lossen; de regio en certificering niet, niet op tijd. Dit houdt het verlaten van Supabase werkelijk in:

❌ "Het is duur", "het is traag", "lock-in" — meestal geen echte redenen om te vertrekken
❌ Aannemen dat de database het moeilijke deel is (dat is het niet — het is standaard Postgres)
❌ Auth onderschatten: elke sessie eindigt en elke RLS-policy moet worden herschreven
❌ De generale repetitie overslaan en gokken hoe lang de overstap duurt

✅ Een volledige repetitie op een kopie — die twee ontbrekende extensies vond en de overstap op 40 minuten mat, niet twee uur
✅ Wachtwoordhashes geïmporteerd, zodat geen zorgverlener iets hoefde te resetten, en 31 RLS-policies herschreven
✅ 94.000 documenten gekopieerd tijdens twee weken lezen uit beide locaties, met oude links omgeleid
✅ Realtime vervangen door polling waar het klinisch niet nodig was, en een geteste herstelactie vóór het opheffen van het oude project

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring in productie-engineering, vertellen we u ook als u níet moet migreren — en dat is vaker het antwoord. 🧭

💡 Het resultaat: na zestien werkdagen en € 11.800 werd het contract getekend. De overstap van 40 minuten vond plaats om zes uur op een zondagochtend, en niemand merkte het. De infrastructuur ging van € 85 naar € 310 per maand — het minst interessante getal van het project. 🚀

👉 Supabase verlaten voor gewone Postgres: https://launchstudio.eu/nl/blog/lovable-supabase-leaving-supabase-for-plain-postgres

#Supabase #PostgreSQL #Migratie #Zorg #LaunchStudio #Manifera
