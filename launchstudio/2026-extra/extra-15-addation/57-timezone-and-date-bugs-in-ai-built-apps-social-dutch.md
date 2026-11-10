🚨 Ricardo Fernandes bouwde Rijlesplanner met Lovable en Supabase: rijscholen publiceren beschikbaarheid, leerlingen boeken lessen en krijgen herinneringen. Op de maandag na de start van de zomertijd kwamen tientallen leerlingen een uur te laat - of stonden instructeurs een uur te vroeg te wachten. 😳

Iedereen die de app gebruikte, zat in Nederland. Maar Nederland heeft twee tijdzones per jaar. Dit zijn de tijdzone- en datumbugs die door AI gebouwde apps verkeerd doen: 🧠

❌ Wekelijkse beschikbaarheid opgeslagen als vaste UTC-tijden
❌ timestamp without time zone, lokaal gelezen in de browser en als UTC in herinneringen
❌ Een cron op vaste UTC-tijd die herinneringen om 06:00 of 07:00 stuurde in plaats van 08:00
❌ toISOString() die facturen in de verkeerde maand dateerde, en rapporten op UTC-dagen

✅ Lestijden gemigreerd naar timestamptz, met de tijdzone van elke rijschool opgeslagen
✅ Terugkerende beschikbaarheid als lokale regels in Europe/Amsterdam
✅ Herinneringen bij het boeken berekend als UTC-moment, verstuurd door een taak elke vijf minuten
✅ Lokale factuurdatums en maandgrenzen, expliciete tijdzones in e-mails en tests voor de zomertijd

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring in productie-engineering, zorgen we dat uw planning de klokwisseling overleeft. 🛠️

💡 Het resultaat: €2.900, 8 werkdagen. Oktober en de maart daarna verliepen zonder één verschoven les, en tickets over verkeerde tijden daalden van een paar dozijn per maand naar bijna nul. 🚀

👉 Gaat uw app goed om met tijdzones? Dit zijn de bugs om te controleren: https://launchstudio.eu/nl/blog/timezone-and-date-bugs-in-ai-built-apps

#Timezones #Scheduling #Supabase #EdTech #AIFounder #LaunchStudio #Manifera
