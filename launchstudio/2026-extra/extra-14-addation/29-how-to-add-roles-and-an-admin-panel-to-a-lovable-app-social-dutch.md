🚨 Roos van Dam coördineert een burenhulpnetwerk in Zaandam en bouwde Buurthulp in Lovable: bewoners plaatsen verzoeken zoals boodschappen of een lift naar de dokter, vrijwilligers nemen ze aan, coördinatoren controleren gevoelige verzoeken. Ongeveer 140 vrijwilligers en 300 bewoners sloten zich aan. Toen ontdekte een vrijwilliger per ongeluk iets. 😳

De beheerpagina was verborgen. Dat was alles: verborgen. Iedereen die wist waar hij moest kijken, kon zichzelf promoveren. Zo werkte het:

❌ Coördinatorstatus opgeslagen als kolom role in de tabel profiles
❌ Een pagina voor het bewerken van het profiel die de hele rij opsloeg - inclusief role
❌ Eén aanpassing in de ontwikkelaarstools van de browser maakte van een vrijwilliger een coördinator
❌ Daarmee werden adressen en medische notities van bewoners zichtbaar; de admincontrole zat alleen in React

✅ Een tabel user_roles zonder schrijfpolicies, bestaande coördinatoren daarnaar gemigreerd
✅ De kolom role uit profiles verwijderd, plus een hulpfunctie has_role voor policies
✅ RLS herschreven: medische notities en adressen alleen zichtbaar voor coördinatoren en de toegewezen vrijwilliger
✅ Vrijwilligers goedkeuren en coördinatoren aanwijzen verplaatst naar edge functions met een auditlog

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar werk aan toegangscontrole voor enterpriseklanten, dwingen we rollen af in de database - waar opnieuw gegenereerde componenten ze niet ongedaan kunnen maken. 🛠️

💡 Het resultaat: €1.750, zes werkdagen. Het verhogen van rechten was binnen vier dagen onmogelijk, Roos bekijkt het auditlog maandelijks, en Buurthulp verwerkte sindsdien ongeveer 2.000 verzoeken. 🚀

👉 Rollen en een beheerpaneel toevoegen aan een Lovable-app? Dit is het veilige patroon stap voor stap: https://launchstudio.eu/nl/blog/how-to-add-roles-and-an-admin-panel-to-a-lovable-app

#Lovable #Supabase #Toegangscontrole #Buurt #LaunchStudio #Manifera
