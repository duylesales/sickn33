🌐 Wouter Claassen zette Zaalplanner live op `app.zaalplanner.nl` voor sportzalen in Tilburg. Een maand later bleek Google een onbeveiligde testomgeving (`staging.zaalplanner.nl`) te hebben geïndexeerd, terwijl sessie-cookies lekten tussen de test- en live-omgeving — waardoor testaccounts actieve productiegegevens overschreven. 😳

Een professionele domeinstructuur vereist strikte subdomein-scheiding, cookie-scoping en canonieke redirects. Waar het misgaat:

❌ Zoekmachines per ongeluk testomgevingen laten indexeren door ontbrekende headers of wachtwoorden
❌ Inlogcookies te breed instellen op het hoofddomein waardoor test- en live-sessies door elkaar lopen
❌ Geen canonieke 301-redirects tussen `www` en root-domeinen, wat SEO-waarde versnippert
❌ Mislukte API-calls door verkeerd geconfigureerde Cross-Origin Resource Sharing (CORS) regels

Wat u wél moet inrichten vóór domeinfouten uw zoekpositie schaden of sessielekken veroorzaken:

✅ Alle staging- en testsubdomeinen afschermen achter verplichte authenticatie of IP-whitelists
✅ Inlogcookies strikt binden aan het exacte subdomein (`app.domein.nl`) tegen dataschade
✅ Strikte 301-redirects en HSTS-headers afdwingen op DNS- en edge-niveau
✅ Een apart subdomein inrichten voor transactionele e-mail gescheiden van de webservers

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring in enterprise engineering, richten we uw complete domein- en routeringsinfrastructuur in volgens de strengste security- en SEO-normen.

💡 Het resultaat: Wouter Claassen liet de domeinstructuur van Zaalplanner binnen 3 werkdagen saneren voor € 1.600 (domeinstructuur, staging-beveiliging, cookie-scoping, redirects). De staging-pagina's verdwenen binnen 3 weken uit Google en sessiefouten zijn definitief verleden tijd. 🚀

👉 Lees hoe u subdomeinen, cookies en redirects foutloos inricht voor uw SaaS: https://launchstudio.eu/nl/blog/lovable-custom-domain-subdomains-and-redirects

#DNS #Domeinen #Beveiliging #DevOps #LaunchStudio #Manifera
