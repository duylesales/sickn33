🚨 Leveranciersportaal van Bart Engelen regelt leverancierskwalificatie voor 14 inkoopteams. Een regionaal nutsbedrijf met 2.000 medewerkers wilde kopen - als inloggen via hun Entra ID liep, afgedwongen, met automatisch verlies van toegang voor vertrekkers. Hij zette Supabase SAML aan, liet organisaties hun eigen IdP-metadata plakken, en koppelde gebruikers op e-mailadres aan bestaande accounts. 😳

Een review een week voor livegang ontdekte dat elk proefaccount een eigen test-identity provider kon registreren, het e-mailadres van elke klant kon opgeven - en zo rechtstreeks in het account van die persoon kwam. Dit vraagt SSO voor een enterpriseklant echt:

❌ Geen domeinverificatie, dus elke koppeling kon elk e-maildomein opgeven
❌ Accounts onvoorwaardelijk gekoppeld op e-mailadres
❌ Sessies van 30 dagen, dus een uitgeschakelde Entra-gebruiker hield tot een maand toegang
❌ Geen bewaking van het verlopen van SAML-certificaten

✅ Domeinverificatie via DNS TXT; elke koppeling beperkt tot geverifieerde domeinen, gratis e-mailaanbieders geweigerd
✅ Koppelen alleen voor geverifieerde domeinen, met inloggen via wachtwoord uitgeschakeld op afgedwongen domeinen
✅ Just-in-time aanmaken met de rol Lid, Entra-groepen gekoppeld aan rollen, afdwingen in de API met één gelogd noodaccount
✅ SSO-sessies van 10 uur, SCIM-deprovisioning, waarschuwingen bij verlopende certificaten en een configuratiegids voor het IT-team van de klant

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring in productie-engineering, implementeren we SSO wanneer de eerste enterprisedeal van een product ervan afhangt. ⚙️

💡 Het resultaat: € 5.600, vijf werkdagen. Logs bevestigden dat niemand het gat had misbruikt. Het nutsbedrijf tekende voor € 38.000 per jaar - en elf maanden later ging de waarschuwing af, zodat het certificaat werd vervangen zonder één buitengesloten gebruiker. 🚀

👉 AI-appbeveiliging: SSO wanneer een enterpriseklant erom vraagt: https://launchstudio.eu/nl/blog/ai-app-security-sso-when-an-enterprise-customer-asks

#SSO #EnterpriseSaaS #AppSecurity #Supabase #LaunchStudio #Manifera
