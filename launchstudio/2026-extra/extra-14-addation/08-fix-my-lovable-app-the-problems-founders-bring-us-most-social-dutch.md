🚨 Tim Verbeek heeft een bakfietsverhuur in Delft en bouwde Fietsdeel in Lovable. Twee maanden werkte het. Toen was het medewerkersdashboard elke vrijdagmiddag leeg - terwijl klanten gewoon reserveringsbevestigingen bleven ontvangen. 😳

Tim promptte Lovable een dozijn keer. Elke "oplossing" veranderde de dashboardquery, en twee keer stelde Lovable voor de reserveringspolicy openbaar te maken. De bug zat helemaal niet in het dashboard. Dit was er echt aan de hand:

❌ Een geplande opschoonfunctie die reserveringen archiveerde op UTC in plaats van Nederlandse tijd
❌ Boekingen voor de volgende ochtend op vrijdagmiddag gearchiveerd, voordat medewerkers ze zagen
❌ Een reserveringspolicy waarmee elke klant alle boekingen kon opvragen, inclusief namen en telefoonnummers
❌ Geen staging, dus elke prompt ging direct live

✅ Opschoonfunctie aangepast naar Europe/Amsterdam-tijd, alleen verstreken ophaalmomenten worden gearchiveerd
✅ Gearchiveerde reserveringen teruggezet
✅ RLS herschreven: klanten zien hun eigen boekingen, medewerkers alle boekingen
✅ Een stagingproject om prompts veilig te testen - en de Lovable-frontend onaangeroerd

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar productiewerk, stellen we eerst een diagnose en repareren we daarna alleen wat er onder de motorkap kapot is. 🛠️

💡 Het resultaat: €1.150, vijf werkdagen. Het verdwijnen op vrijdag stopte nog dezelfde week, en Fietsdeel verwerkte in het voorjaarsseizoen ongeveer 900 reserveringen. 🚀

👉 Lovable zegt "opgelost", maar er verandert niets? Dit zijn de acht problemen die oprichters het vaakst bij ons brengen: https://launchstudio.eu/nl/blog/fix-my-lovable-app-the-problems-founders-bring-us-most

#Lovable #Supabase #NoCode #AIFounder #LaunchStudio #Manifera
