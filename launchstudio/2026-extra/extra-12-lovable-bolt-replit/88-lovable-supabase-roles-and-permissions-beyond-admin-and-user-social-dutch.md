🚨 Horecarooster van Marloes Teunissen roostert zo'n 3.800 medewerkers op 140 locaties voor 27 horecagroepen. Er waren drie rollen: eigenaar, beheerder, lid. Locatiemanagers moesten uren goedkeuren - wat alleen beheerders konden - dus werd elke manager beheerder. Toen zag een financieel directeur dat een manager zijn eigen overuren goedkeurde. 😳

Als beheerder konden managers ook de lonen van elke locatie zien. Diezelfde week haakte een groep met 34 locaties precies om die reden af. Zo bouwt u rollen en rechten voorbij "beheerder en gebruiker":

❌ Eén rolveld dat "alleen mijn locatie" niet kon uitdrukken
❌ Managers tot beheerder gemaakt alleen om uren goed te keuren
❌ Uurlonen zichtbaar voor iedereen met de beheerdersrol
❌ Niets dat mensen tegenhield hun eigen uren goed te keuren

✅ 24 rechtencodes afgeleid van de controles die al door de code verspreid stonden, gebundeld in zes systeemrollen
✅ Roltoewijzingen per locatie; row level security herschreven over 19 tabellen rond één geïndexeerde has_permission-functie
✅ Lonen naar een aparte tabel die alleen met wages.read leesbaar is, en zelfgoedkeuring geblokkeerd in de database
✅ Regels tegen rechtenescalatie, een audit van rolwijzigingen, en een matrix van 24×6 rechten die 288 tests genereert in CI

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring in productie-engineering, bouwen we dit wanneer een product begint te verkopen aan organisaties met meerdere locaties. ⚙️

💡 Het resultaat: € 4.800, vier werkdagen. Een historische controle vond drie managers die samen € 4.100 aan eigen overuren hadden goedgekeurd. De groep met 34 locaties tekende binnen de maand, en een tweede groep volgde - 61 nieuwe locaties. 🚀

👉 Lovable Supabase: rollen en rechten voorbij beheerder en gebruiker: https://launchstudio.eu/nl/blog/lovable-supabase-roles-and-permissions-beyond-admin-and-user

#Supabase #Toegangsbeheer #SaaS #AppSecurity #LaunchStudio #Manifera
