🚨 Ivo Ramaker runt Fietsabonnement, een abonnementsdienst voor fietsen in Amsterdam met ongeveer 2.000 abonnees. Voor zijn supportteam van vijf mensen bouwde hij een intern paneel in Lovable - snel, met de service role key zodat het paneel "alles kon zien". Elke medewerker kon elke abonnee bekijken en wijzigen, alle gegevens exporteren en terugbetalingen doen, zonder dat werd vastgelegd wie wat deed. 😳

Hij bouwde het supportpaneel voor snelheid. Hij had niet gemerkt dat hij ook het gevaarlijkste scherm van zijn bedrijf had gebouwd. Dit maakte dat paneel mogelijk:

❌ De service role key in het paneel, waarmee alle toegangsregels werden omzeild
❌ Elke medewerker kon de gegevens en betaalstatus van elke abonnee bekijken en wijzigen
❌ Onbeperkte exports van gegevens en terugbetalingen
❌ Geen audittrail van wie wat deed

✅ De service role key verwijderd, met rollen voor medewerkers (medewerker, senior medewerker, beheerder) in een tabel met rollen
✅ RLS-policies geschreven voor de toegang van medewerkers
✅ Terugbetalingen en exports verplaatst naar edge functions die beperkt zijn tot senior rollen
✅ Een auditlog van gevoelige acties met een controlescherm, plus MFA voor alle medewerkers

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring met backofficesystemen voor grote bedrijven, behandelen we interne tools als hoog risico: minimale rechten, logging en MFA - of u nu in Lovable of Retool bouwt. 🛠️

💡 Het resultaat: €2.600, zeven werkdagen. Het team hield een snel paneel op maat, Ivo ziet wie elke terugbetaling en export heeft gedaan, en twee maanden later loste het auditlog een geschil met een klant binnen enkele minuten op. 🚀

👉 Lovable of Retool voor uw interne tools? Zo kiest u - en houdt u ze veilig: https://launchstudio.eu/nl/blog/lovable-vs-retool-for-internal-tools

#Lovable #Retool #InterneTools #Supabase #LaunchStudio #Manifera
