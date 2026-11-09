📈 Karim Bouzid bouwde Huiswerkplanner met Bolt en Supabase: een huiswerkplanner waarin leerlingen opdrachten zien, docenten taken plaatsen en ouders de voortgang volgen. Toen besloot een schoolbestuur met 14 scholen de app op één maandagochtend uit te rollen naar 20.000 leerlingen. Karim had nooit meer dan 300 mensen tegelijk online gehad. 😬

Een loadtest vertelde de waarheid: bij ongeveer 600 gelijktijdige leerlingen duurde de planner meer dan vijf seconden en begonnen de fouten. De vraag was niet "kan Supabase 20.000 gebruikers aan?" Dit beperkte de capaciteit echt: 🧠

❌ De planner laadde elke opdracht van de school en filterde in de browser
❌ Elke opdrachtkaart deed zijn eigen extra requests
❌ Een policy met een subquery per rij en geen indexen
❌ Realtime op de hele tabel, waardoor elke wijziging naar elke leerling ging

✅ Samengestelde indexen en een snellere, geïndexeerde policy
✅ Eén view die de komende twee weken van een leerling in één query teruggeeft
✅ Realtime beperkt tot privékanalen per klas
✅ Eén computegrootte omhoog, pas nadat optimalisatie liet zien dat dit de laatste grens was

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring met PostgreSQL-systemen met grote gebruikersbases, optimaliseren we eerst en schalen we daarna. 🛠️

💡 Het resultaat: €4.600, elf werkdagen. Op maandag openden 11.000 leerlingen de app in het eerste uur, met een piek van bijna 2.800 tegelijk en nul fouten. 🚀

👉 Hoeveel gebruikers kan uw Supabase-app echt aan? https://launchstudio.eu/nl/blog/how-many-users-can-a-supabase-app-handle

#Supabase #Bolt #Schaalbaarheid #EdTech #AIFounder #LaunchStudio #Manifera
