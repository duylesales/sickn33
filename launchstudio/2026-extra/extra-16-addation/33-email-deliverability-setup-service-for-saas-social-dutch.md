📧 Daan Willems heeft vanuit Delft een SaaS voor projectmanagement voor architectenbureaus, gebouwd met v0, Cursor en Supabase. Bureaus meldden zich aan, nodigden collega's uit en mailden daarna support: niemand had de uitnodigingen ontvangen. Wachtwoordherstel duurde soms een uur, en de IT-afdeling van een groot bureau zette elk bericht van de app in quarantaine. 📭

Hij heeft weken de code voor uitnodigingen gedebugd. De code was prima. De opzet niet: 🧠

❌ Authenticatiemails via de ingebouwde ontwikkelmaildienst van Supabase
❌ Uitnodigingen via een tweede provider op een niet-geverifieerd domein
❌ Twee SPF-records, dus SPF faalde voor elke verzender, en geen DKIM of DMARC
❌ De nieuwsbrief vanaf het hoofddomein, waardoor marketing en transactionele mail door elkaar liepen

✅ Postmark voor transactionele mail op een eigen subdomein, gekoppeld aan Supabase Auth
✅ De nieuwsbrief naar een apart marketingsubdomein met afmelden met één klik
✅ SPF samengevoegd binnen de limieten, DKIM voor elke verzender en DMARC met rapportage, daarna quarantaine
✅ Webhooks voor bounces en klachten, een blokkadelijst en schone sjablonen met platte tekst

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring met productiesystemen die e-mail versturen voor klanten zoals Vodafone en TNO, zorgen we ervoor dat de e-mails van uw app de inbox bereiken. 🛠️

💡 Het resultaat: €1.450, vier werkdagen. Uitnodigingen en herstelmails komen binnen seconden aan, en tickets over ontbrekende e-mails daalden tot bijna nul. 🚀

👉 Inrichtingsservice voor e-mailbezorging in SaaS: https://launchstudio.eu/nl/blog/email-deliverability-setup-service-for-saas

#Email #Bezorging #DMARC #Supabase #AIFounder #LaunchStudio #Manifera
