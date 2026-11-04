🚨 Noor Bakker, fysiotherapeut in Amersfoort, bouwde FysioSlot met Lovable en Supabase: online boeken voor kleine praktijken, met intakeformulieren en behandelnotities. Drie praktijken, elf therapeuten. Toen merkte een patiënt die in de IT werkt vriendelijk op dat hij intakeformulieren van andere patiënten kon ophalen via de ontwikkelaarstools van zijn browser. 😳

Supabase is veilig als het is geconfigureerd. De AI vertelde nooit welke delen hij had overgeslagen. Dit vond Noor:

❌ RLS uitgeschakeld op twee tabellen die Lovable later aanmaakte: intake_forms en treatment_notes
❌ Policies op de andere tabellen waarmee elke ingelogde gebruiker alles kon lezen
❌ De service role key in een omgevingsbestand van de frontend
❌ Uploads van intakeformulieren in een openbare storage bucket

✅ Blootgestelde sleutel vervangen, RLS ingeschakeld op elke tabel
✅ Een lidmaatschapsmodel: patiënten zien hun eigen gegevens, therapeuten alleen hun eigen praktijk
✅ Intakebestanden in een privébucket met ondertekende URL's
✅ Migraties in git, een stagingproject en dagelijkse back-ups met een geteste terugzetting

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar enterprisewerk met PostgreSQL, maakt een Supabase developer de laag af die AI-builders openlaten - op uw eigen account, in uw eigen repository. 🛠️

💡 Het resultaat: €2.900, zes werkdagen. FysioSlot is sindsdien gegroeid naar zeven praktijken zonder verdere toegangsproblemen. 🚀

👉 Op zoek naar een Supabase developer? Dit is de productie-inrichting stap voor stap: https://launchstudio.eu/nl/blog/supabase-developer-for-hire-production-setup-and-rls

#Supabase #RowLevelSecurity #Lovable #Zorgtech #LaunchStudio #Manifera
