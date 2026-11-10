🚨 Jeroen Bos bouwde Sporthal Online met Lovable en Supabase: boekingen voor sporthallen en velden van gemeenten en stichtingen. Wachtwoordresets liepen via de standaard e-maildienst van Supabase, en een maandelijkse nieuwsbrief ging vanaf hetzelfde domein - zonder authenticatie voor beide. 😳

Na één grote nieuwsbrief konden gebruikers hun wachtwoord niet resetten, kregen nieuwe aanmelders geen bevestiging en verdwenen boekingsbevestigingen. Zo kiest u tussen Resend, Postmark en Brevo voor transactionele e-mail: 🧠

❌ Rate limits op de standaard e-maildienst van Supabase
❌ Geen SPF, DKIM of DMARC op het domein
❌ Een als spam gemarkeerde nieuwsbrief die inlogmails meetrok
❌ Gebouncede adressen uit oude imports die nog steeds mail kregen

✅ Postmark voor transactionele e-mail op een eigen, geauthenticeerd subdomein
✅ Supabase Auth via custom SMTP met gebrande Nederlandse en Engelse sjablonen
✅ De nieuwsbrief naar Brevo op een apart subdomein, met toestemming en afmeldlink
✅ Bounce- en klachtwebhooks die een suppressietabel vullen, met een vraag om het adres te corrigeren

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring in productie-engineering, halen we het brandalarm uit de keuken - zodat marketing nooit uw inlog breekt. 🛠️

💡 Het resultaat: €1.900, 6 werkdagen. Resets en bevestigingen kwamen binnen enkele dagen betrouwbaar aan, tickets over ontbrekende mails daalden met meer dan 90% en de volgende nieuwsbrief had geen invloed op transactionele mail. 🚀

👉 Belanden de mails van uw app in spam? Zo kiest u een transactionele provider: https://launchstudio.eu/nl/blog/transactional-email-providers-resend-vs-postmark-vs-brevo

#EmailDeliverability #Postmark #Brevo #Resend #AIFounder #LaunchStudio #Manifera
