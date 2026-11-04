🚨 Mirjam Dekkers coördineert een voedselbank in Helmond en bouwde Voedselhulp in Lovable: vrijwilligers melden zich aan voor uitdeeldiensten en krijgen herinneringen. Op de avond van de lancering ontvingen de eerste 30 of zo vrijwilligers hun bevestigingsmail. Daarna - niets. Vrijwilligers probeerden het opnieuw, maakten dubbele accounts aan en gaven het op. 😳

Dertig mensen kwamen binnen en toen ging de deur stilletjes dicht. Niemand zag een foutmelding, zij ook niet. Dit gebeurde er:

❌ De ingebouwde e-maildienst van Supabase had zijn verzendlimiet bereikt
❌ De e-mails die wel werden verstuurd, kwamen van een algemeen adres, en meerdere gingen direct naar de spam
❌ Links voor wachtwoordherstel wezen naar het previewdomein van Lovable
❌ Dubbele accounts stapelden zich op door herhaalde aanmeldpogingen

✅ Eigen SMTP via een provider voor transactionele e-mail in een EU-regio
✅ SPF-, DKIM- en DMARC-records toegevoegd aan het eigen domein van de voedselbank
✅ Productie-redirect-URL's en Nederlandse sjablonen met de naam van de voedselbank
✅ Eenmalige codes in plaats van magic links voor vrijwilligers met een werkadres, en dubbele accounts samengevoegd

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar transactionele e-mail op schaal, behandelen we e-mail als infrastructuur - niet als bijzaak. 🛠️

💡 Het resultaat: €850, drie werkdagen. Elke wachtende vrijwilliger was de volgende ochtend bevestigd, binnen een maand stonden 210 vrijwilligers geregistreerd, en herinneringen komen nu in de inbox aan in plaats van in de spam. 🚀

👉 Komen de registratiemails van uw Supabase-app niet aan? Dit zijn de vier gangbare oorzaken en de oplossing: https://launchstudio.eu/nl/blog/why-are-my-supabase-signup-emails-not-arriving

#Supabase #Lovable #EmailBezorging #Vrijwilligers #LaunchStudio #Manifera
