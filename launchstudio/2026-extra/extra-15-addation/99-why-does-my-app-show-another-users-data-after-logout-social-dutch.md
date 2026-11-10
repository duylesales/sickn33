🚨 Daan Peters bouwde Ledenloket met Lovable en Supabase: leden van negen sportscholen checken in op een gedeelde tablet bij de receptie, bekijken hun abonnement en boeken lessen. Toen klaagde een lid: na het inloggen zag ze een paar seconden de naam, het abonnement en de boekingen van het vorige lid. 😳

Eén keer boekte ze, door snel te tikken, zelfs een les op het account van het vorige lid. De database was goed afgeschermd. Het lek zat in alles wat de app onthield. Waarom apps na het uitloggen gegevens van een andere gebruiker tonen: 🧠

❌ Uitloggen dat alleen de sign-out van Supabase aanriep
❌ React Query-resultaten gecachet onder sleutels zonder gebruikers-ID
❌ Profiel en vestiging in local storage, en het lid-ID voor boekingen in een globale store
❌ Een Cloudflare-regel die "lessen van vandaag" cachete met een persoonlijke "geboekt"-markering

✅ CDN-caching verwijderd voor geauthenticeerde routes, met private, no-store-headers
✅ Eén centrale uitlogroutine die caches, stores, local storage en realtime leegt en daarna herlaadt
✅ Querysleutels met het lid-ID, en boekingen die het lid-ID uit de serversessie halen
✅ Automatisch uitloggen op de kiosk na 60 seconden, en het incident vastgelegd als datalek onder de AVG

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring in productie-engineering, ruimen we op wat uw app onthoudt nadat mensen weg zijn. 🛠️

💡 Het resultaat: €1.700, 4 werkdagen. Tests op gedeelde toestellen tonen geen gegevens van vorige leden, er kwamen geen nieuwe klachten, en het automatisch uitloggen op de kiosk werd een functie die sportscholen aanbevelen. 🚀

👉 Lekt uw app data tussen gebruikers op gedeelde toestellen? Zo lost u het op: https://launchstudio.eu/nl/blog/why-does-my-app-show-another-users-data-after-logout

#Privacy #SessionSecurity #GDPR #FitnessTech #AIFounder #LaunchStudio #Manifera
