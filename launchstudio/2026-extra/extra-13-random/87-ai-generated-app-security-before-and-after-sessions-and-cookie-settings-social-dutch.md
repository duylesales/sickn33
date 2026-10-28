🚨 Sem Evers, facilitair coördinator en oprichter in IJsselstein, bouwde Zaalvrij met Cursor: bedrijven in gedeelde kantoorgebouwen boeken vergaderruimtes, beheren bezoekers en krijgen maandelijkse facturen voor het gebruik. 26 bedrijven in vier gebouwen - vaak op gedeelde receptiecomputers. Toen meldde een receptioniste dat de terugknop van de browser na het uitloggen de boekingen van een ander bedrijf liet zien. En doorklikken werkte nog steeds. 😳

Cursor had JWT-authenticatie gebouwd met tokens in localStorage, 30 dagen geldig, en uitloggen verwijderde het token alleen uit de browser - een gekopieerd token bleef werken. Cookies voor "ingelogd blijven" misten HttpOnly en SameSite, formulieren om boekingen te annuleren hadden geen CSRF-bescherming, wachtwoordwijzigingen beëindigden geen andere sessies, en een reflected XSS in het veld voor de naam van een bezoeker had het token kunnen lezen. Dit is de beveiliging van AI-gegenereerde apps vóór en na het repareren van sessies en cookies:

❌ Tokens in localStorage, een maand geldig
❌ Uitloggen dat alleen het token verbergt
❌ Cookies zonder HttpOnly of SameSite, en geen CSRF-bescherming
❌ Sessies die een wachtwoordwijziging overleven

✅ Eigen JWT-afhandeling vervangen door sessies van Supabase Auth
✅ Refresh tokens in HttpOnly-, Secure- en SameSite=Lax-cookies en kortere levensduur van access tokens
✅ Ongeldig maken op de server bij uitloggen en wachtwoordwijziging, plus een inactiviteitstime-out van acht uur voor accounts op gedeelde computers
✅ CSRF-tokens op formulieren die de staat wijzigen, de XSS opgelost met output-escaping en een Content Security Policy - en "overal uitloggen"

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring in productie-engineering en zijn wortels in cybersecurity, zorgen we dat uw uitlogknop de sessie echt beëindigt. ⚙️

💡 Het resultaat: € 1.100, vier werkdagen. Het probleem met de gedeelde computer verdween, de beveiligingsvragenlijst van een grotere huurder werd zonder vervolgvragen beantwoord, en Zaalvrij werd in gebruik genomen in nog twee kantoorgebouwen. 🚀

👉 Beveiliging van AI-gegenereerde apps: Voor en na sessies en cookie-instellingen: https://launchstudio.eu/nl/blog/ai-generated-app-security-before-and-after-sessions-and-cookie-settings

#Sessiebeveiliging #Cookies #CSRF #Cursor #LaunchStudio #Manifera
