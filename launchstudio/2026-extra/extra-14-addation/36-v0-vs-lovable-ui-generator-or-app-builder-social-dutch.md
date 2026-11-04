🚨 Merel Kok heeft een kleine architectenstudio in Schiedam en wilde Ontwerpkluis: een openbaar portfolio dat scoort op "renovatiearchitect" rond Rotterdam, plus een privéportaal waar klanten tekeningen bekijken en ontwerpfasen goedkeuren. Ze bouwde eerst alles in Lovable. 😳

Het portaal werkte. Het portfolio werd in twee maanden nauwelijks geïndexeerd. Ze bouwde het portfolio opnieuw in v0 - dat werd snel geïndexeerd - en begon daarna ook het portaal daar opnieuw te bouwen, en liep vast. Dit was er aan de hand:

❌ Portfoliopagina's van Lovable die in de browser renderden, nauwelijks zichtbaar voor zoekmachines
❌ De herbouw in v0 liep vast op authenticatie en rechten op bestanden voor het portaal
❌ Twee halve versies en geen gedeelde backend
❌ Tekeningen van klanten zonder goede toegangscontrole

✅ Beide behouden: de Next.js-site uit v0 voor openbare pagina's op het hoofddomein, het portaal uit Lovable op een subdomein
✅ Eén gedeeld Supabase-project in Frankfurt, met Row Level Security zodat klanten alleen hun eigen projecten zien
✅ Tekeningen in privéopslag met ondertekende URL's, plus flows voor opmerkingen en goedkeuringen met e-mailmeldingen
✅ Omgevingsvariabelen per Vercel-omgeving en gestructureerde data op projectpagina's

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar werk met React en Next.js, laten we elke tool doen waar hij goed in is - en verbinden we ze goed. 🛠️

💡 Het resultaat: €4.600, dertien werkdagen. Het portfolio werd binnen enkele weken geïndexeerd en leverde aanvragen voor renovaties uit Rotterdam en Delft op, en veertien klanten gebruikten het portaal in het eerste kwartaal. 🚀

👉 v0 of Lovable - UI-generator of appbuilder? Zo kiest u, of gebruikt u beide: https://launchstudio.eu/nl/blog/v0-vs-lovable-ui-generator-or-app-builder

#v0 #Lovable #NextJS #SEO #LaunchStudio #Manifera
