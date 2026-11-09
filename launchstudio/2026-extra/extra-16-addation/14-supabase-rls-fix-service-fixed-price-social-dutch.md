🔐 Joyce Vermeulen heeft een administratiekantoor in Hoorn en bouwde Klantmap met Lovable en Supabase: zo'n 180 klanten uploaden bonnetjes en bankafschriften, en haar team bereidt hun btw-aangiften voor. Tijdens de onboarding vroeg een nieuwe klant die in de IT werkte: "Hoe zorgt u ervoor dat andere klanten mijn documenten niet kunnen zien?" Joyce besefte dat ze het niet wist. 😶

Een test op blootstelling via de API gaf binnen enkele minuten antwoord. Elke klant zat op één query afstand van de bestanden van elke andere klant: 🧠

❌ Een policy waarmee elke ingelogde gebruiker alle documenten kon opvragen
❌ Een openbare storagebucket met bestandspaden op basis van klantnamen
❌ Gebruikers die hun eigen rolkolom konden wijzigen en zichzelf konden promoveren
❌ Een security definer-functie die nooit controleerde wie hem aanriep

✅ Een afgesproken toegangsmodel: klanten, toegewezen medewerkers, eigenaar
✅ Policies herschreven voor alle elf tabellen, apart per bewerking
✅ Een privébucket met mappen per klant en signed URL's
✅ Negatieve autorisatietests per rol en projectinstructies voor Lovable

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring met het beveiligen van enterprisesystemen, testen we Row Level Security zoals een aanvaller dat zou doen en repareren we het tegen een vaste prijs, zonder uw interface aan te raken. 🛠️

💡 Het resultaat: €1.850, vijf werkdagen. Het portaal ziet er hetzelfde uit, en Joyce beantwoordt beveiligingsvragenlijsten nu met een document van één pagina en tests als bewijs. 🚀

👉 Supabase RLS-fixservice, tegen een vaste prijs: https://launchstudio.eu/nl/blog/supabase-rls-fix-service-fixed-price

#Supabase #RLS #Lovable #Beveiliging #AIFounder #LaunchStudio #Manifera
