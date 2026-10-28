🚨 Ledenadmin van Koen Vermeulen verzorgt de ledenadministratie voor vijf sportclubs rond Helmond - zo'n 4.000 leden met adressen, geboortedata, bankgegevens en soms medische notities. Row level security stond aan. De policy liet elke ingelogde gebruiker de hele tabel lezen. 😳

Elk lid kon de bankgegevens van elk ander lid inzien, over alle vijf clubs heen. Daarom is "RLS staat aan" niet hetzelfde als beschermd:

❌ Een policy uit de ontwikkelfase die een lege lijst moest oplossen - en alles teruggaf
❌ De rolkolom in een profiel dat gebruikers zelf kunnen aanpassen
❌ Gevoelige gegevens zoals bankgegevens in dezelfde tabel als al het andere
❌ Vergeten tabellen, zoals een oude importkopie, nog leesbaar met de publieke sleutel

✅ Een organisatie- en lidmaatschapsmodel: elke club een tenant, met echte rollen
✅ Policies per tabel en per bewerking, met de identiteit uit de sessie
✅ Bankgegevens in een aparte tabel, alleen leesbaar voor clubbeheerders
✅ Testen door aan te vallen: meerdere accounts, een niet-ingelogde client en elke tabel rechtstreeks opvragen

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring in productie-engineering, schrijven we Supabase-policies die standhouden als iemand het echt probeert. 🛡️

💡 Het resultaat: in negen werkdagen en voor € 4.600 vond de aanvalstest ook nog twee vergeten leesbare tabellen, die beide zijn verwijderd. De vijf clubs tekenden een gezamenlijke verwerkersovereenkomst die vastzat - en Koen heeft nu een document voor elk bestuur dat vraagt wie wat kan zien. 🚀

👉 Row level security-policies die echt standhouden: https://launchstudio.eu/nl/blog/supabase-security-row-level-security-policies-that-hold

#Supabase #RowLevelSecurity #Lovable #AVG #LaunchStudio #Manifera
