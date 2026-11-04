🚨 Olivier Maes coördineert de vrijwilligers van een muziekfestival bij Leuven en bouwde Shiftwissel met Bolt en Supabase: vrijwilligers kiezen diensten, ruilen ze en krijgen de gegevens van hun polsbandje. Binnen twee weken meldden zich ongeveer 600 aan. Toen stuurde een vrijwilliger met een achtergrond in ontwikkeling hem een bericht. 😳

Het JavaScript van de app bevatte een sleutel waarvan de gedecodeerde rol service_role was. Bolt had die als shortcut gebruikt om dienstruilen te laten werken. Dit betekende dat:

❌ Een loper die Row Level Security omzeilt, meegestuurd naar de browser van elke bezoeker
❌ Iedereen kon het telefoonnummer en adres van elke vrijwilliger lezen
❌ Iedereen kon het volledige dienstrooster verwijderen
❌ De policies van de anon key stonden ruilen nooit toe - dus nam de AI een shortcut

✅ De service role key binnen het uur vervangen, logs gecontroleerd - geen toegang buiten de eigen test van de vrijwilliger
✅ Ruillogica verplaatst naar een edge function die controleert of beide vrijwilligers akkoord zijn
✅ RLS op elke tabel: vrijwilligers lezen alleen hun eigen gegevens en het openbare rooster
✅ Een stagingproject voor verdere wijzigingen

Bij **LaunchStudio**, ondersteund door Manifera en de cybersecurity-achtergrond van de oprichter, komt het beheer van geheimen in elke review als eerste - nog voor enig functiewerk. 🛠️

💡 Het resultaat: €1.350, vier werkdagen. Shiftwissel verwerkte tijdens het festival ongeveer 1.100 dienstruilen zonder incidenten, en de organisatoren namen het over voor het jaar daarop. 🚀

👉 Is de anon key van Supabase veilig in uw frontend? Ja - maar alleen als uw RLS klopt. Zo controleert u het: https://launchstudio.eu/nl/blog/is-the-supabase-anon-key-safe

#Supabase #AppSecurity #Bolt #Evenementen #LaunchStudio #Manifera
