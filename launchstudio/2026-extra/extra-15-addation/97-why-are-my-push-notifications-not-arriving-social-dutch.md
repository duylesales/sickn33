🚨 Lars Visser bouwde Afhaalklaar met Lovable en Supabase: een PWA voor bakkers en delicatessenzaken waarmee klanten vooraf bestellen en een melding krijgen als het klaarligt. Elf winkels gebruikten het, met als belofte "geen rijen meer". Maar klanten stonden nog steeds aan de toonbank te wachten en zeiden dat ze nooit een melding kregen. 😳

Op Lars' Android-telefoon werkte het perfect. Voor de meeste klanten van zijn klanten bestond het niet. Waarom pushmeldingen niet aankomen: 🧠

❌ iPhone-gebruikers (zo'n 60%) die in Safari bestelden zonder de app op het beginscherm te zetten
❌ Eén subscriptionveld per gebruiker, dus alleen het laatst gebruikte toestel kreeg een melding
❌ VAPID-sleutels opnieuw gegenereerd door een prompt, waardoor oudere subscriptions stil stopten
❌ Een latere prompt die de service worker verving door een versie zonder pushhandler

✅ Stabiele VAPID-sleutels in server-secrets en een pushhandler in een Workbox-service worker
✅ Eén subscriptionrij per toestel, ververst bij openen en verwijderd bij 404/410
✅ Elke verzending gelogd met het resultaat
✅ Push of sms gekozen bij het afrekenen, met een installatiegids en standaard sms voor iPhone-gebruikers

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring in productie-engineering, maken we meldingen betrouwbaar - en meetbaar. 🛠️

💡 Het resultaat: €2.000, 6 werkdagen. Meer dan 95% van de "bestelling klaar"-berichten komt nu aan via push of sms, en het aandeel bestellingen dat binnen 15 minuten werd opgehaald, steeg van ongeveer de helft naar meer dan 80%. 🚀

👉 Komen uw pushmeldingen nergens aan? Zo verschillen web, iOS en Android: https://launchstudio.eu/nl/blog/why-are-my-push-notifications-not-arriving

#PushNotifications #PWA #iOS #FoodTech #AIFounder #LaunchStudio #Manifera
