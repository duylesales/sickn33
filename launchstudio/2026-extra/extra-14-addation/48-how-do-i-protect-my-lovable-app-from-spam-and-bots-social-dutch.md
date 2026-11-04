🚨 Sevda Arslan bouwde Buurtruil in Lovable: een gratis ruilmarktplaats voor haar wijk in Arnhem. Een lokale krant schreef er op een donderdag over. Op maandag had Buurtruil 4.300 nieuwe accounts - waarvan ongeveer 3.900 nep - en honderden advertenties voor dubieuze cryptoconstructies. 😳

Het krantenartikel bracht haar buren en bots. De bots waren veel sneller. Dit is waarom:

❌ Geen CAPTCHA op het registratieformulier
❌ E-mailbevestiging uitgeschakeld
❌ Advertenties die elke link konden bevatten
❌ De ingebouwde e-mailverzending uitgeput door nepregistraties, waardoor echte buurtbewoners hun bevestigingsmail nooit kregen

✅ Cloudflare Turnstile ingeschakeld bij Supabase Auth
✅ E-mailbevestiging aangezet, met eigen SMTP
✅ Rate limits op registraties en advertenties per IP-adres en per account, en links geblokkeerd in advertenties van nieuwe accounts
✅ Nepaccounts en -advertenties verwijderd met een script op de server, plus een dagelijkse grafiek van registraties met meldingen

Bij **LaunchStudio**, ondersteund door Manifera en de cybersecurity-achtergrond van de oprichter bij CFLW, is bescherming tegen bots gelaagd en gemonitord - niet alleen één CAPTCHA die één keer wordt toegevoegd. 🛠️

💡 Het resultaat: €1.050, drie werkdagen. Het aantal nepregistraties daalde naar een handvol per week, het echte ledental groeide naar ongeveer 900 huishoudens, en de marktplaats was binnen twee dagen weer bruikbaar. 🚀

👉 Uw Lovable-app beschermen tegen spamregistraties en bots? Dit is de gelaagde verdediging: https://launchstudio.eu/nl/blog/how-do-i-protect-my-lovable-app-from-spam-and-bots

#Lovable #Supabase #Botbescherming #AppSecurity #LaunchStudio #Manifera
