🚨 Kees Bakkenes runt een rijschool in Emmen met zes instructeurs en bouwde Rijlesrooster in Bolt, met lesherinneringen per sms voor elke leerling. De hele winter werkten de herinneringen perfect. Toen werd in maart de klok verzet - en elke herinnering kwam een uur te laat. Sommige leerlingen misten hun les. 😳

De herinneringen werkten vijf maanden. Toen werd de klok verzet, en de opkomst van zijn leerlingen ook. Dit zat er verstopt in de gegenereerde code:

❌ Lokale tijden opgeslagen als tekst en vergeleken met de UTC-tijd van de server
❌ Een functie die elke minuut draaide en herinneringen opnieuw verstuurde als de sms-provider traag was - sommige leerlingen kregen hetzelfde bericht drie keer
❌ Geen vastlegging van wat al verstuurd was
❌ Geen melding toen de functie na een storing bij de provider faalde - twee dagen lang merkte niemand iets

✅ Een outboxtabel voor herinneringen met tijdstempels in UTC en planningslogica in Europe/Amsterdam
✅ De planning verplaatst naar Supabase Cron, elke vijf minuten
✅ Idempotent versturen met het bijhouden van de status, zodat elke herinnering precies één keer uitgaat
✅ Nieuwe pogingen bij tijdelijke storingen en meldingen bij vastgelopen taken

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar planningssystemen voor enterprise- en logistieke klanten, behandelen we geplande taken als gemonitorde infrastructuur, niet als een timer die op het beste hoopt. 🛠️

💡 Het resultaat: €1.400, vijf werkdagen. Tijdens de wisseling naar wintertijd in oktober en het jaar daarna kwamen herinneringen op tijd en zonder dubbelingen aan, en het aantal gemiste lessen daalde merkbaar. 🚀

👉 Herinneringen bouwen in een Supabase-app? Dit zijn de zes bouwstenen die ze betrouwbaar maken: https://launchstudio.eu/nl/blog/how-do-i-send-automatic-reminders-from-a-supabase-app

#Supabase #Bolt #pgcron #SaaS #LaunchStudio #Manifera
