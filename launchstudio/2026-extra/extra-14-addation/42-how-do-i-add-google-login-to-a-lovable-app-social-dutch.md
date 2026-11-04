🚨 Joris Kuijpers, studentendecaan in Nijmegen, bouwde Tentamenplan in Lovable: studenten plannen hun voorbereiding op tentamens en delen schema's met studiegroepen. Hij voegde inloggen met Google toe, omdat bijna elke student een Google-account heeft. Het werkte perfect - voor hem. Op de lanceringsdag zagen studenten "access blocked". 😳

Het werkte elke keer als hij het testte. Hij was de enige persoon ter wereld voor wie het was ingericht. Dit was er mis:

❌ Het toestemmingsscherm van Google stond nog in testmodus, met Joris als enige testgebruiker
❌ Na publicatie kwamen studenten na het inloggen terug op het previewdomein van Lovable
❌ Geen profielrij voor Google-gebruikers, waardoor functies voor studiegroepen crashten
❌ Geen plan voor studenten die zich al met e-mail hadden geregistreerd

✅ Toestemmingsscherm gepubliceerd met vereenvoudigde, basale scopes
✅ Productie-site-URL en redirectlijst ingesteld in Supabase
✅ Een trigger die voor elke nieuwe authenticatiegebruiker een profiel aanmaakt
✅ Koppelen van identiteiten voor studenten die zich eerst met e-mail registreerden, getest in browsers op iOS en Android

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar authenticatiewerk, laten we social login werken voor elke gebruiker - niet alleen voor de oprichter. 🛠️

💡 Het resultaat: €950, drie werkdagen. De inlogproblemen verdwenen binnen een dag, en tijdens de tentamenperiode meldden zich ongeveer 1.300 studenten aan - driekwart via Google. 🚀

👉 Inloggen met Google toevoegen aan een Lovable-app? Dit is de inrichting en waarom het na de lancering kapotgaat: https://launchstudio.eu/nl/blog/how-do-i-add-google-login-to-a-lovable-app

#Lovable #Supabase #GoogleLogin #EdTech #LaunchStudio #Manifera
