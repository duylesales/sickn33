🚨 Taxatierapport van Vincent Bogaers maakt taxatierapporten voor negentien makelaars en vier taxatiebureaus rond Bergen op Zoom en Roosendaal. Op een donderdagmiddag verhuisde hij de hosting en bracht hij de DNS onder bij dezelfde provider. Binnen twintig minuten stond de site op de nieuwe host. Hij dacht dat hij klaar was. 😳

Drie dagen lang werd elke e-mail aan zijn domein geweigerd — ook op het adres dat op elk taxatierapport stond. Dit kan een domeinverhuizing ongemerkt kapotmaken:

❌ MX-records nooit opnieuw aangemaakt
❌ Login-callbacks die nog naar het oude hostingadres verwezen — niemand kon inloggen
❌ Een betaalwebhook die naar het oude adres wees: elf dagen aan abonnementsgebeurtenissen kwijt
❌ Hostingverhuizing en registrar-overdracht tegelijk gepland

✅ MX, SPF, DKIM en DMARC hersteld en de aflevering getest bij vier grote providers
✅ Beide adressen geregistreerd voor de login-callbacks tijdens de overgang
✅ De webhook omgezet met handtekeningcontrole en ontdubbeling, en de elf dagen afgestemd
✅ Lagere TTL's, een zone-export, een volledige inventaris van alles wat het domein gebruikt — en de registrar-overdracht apart uitgevoerd

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring in productie-engineering, verhuizen we live domeinen zonder één e-mail te verliezen. 🌐

💡 Het resultaat: na vijf werkdagen en € 2.800 verliep de registrar-overdracht drie weken later zonder problemen, en de inventaris is nu het uitgangspunt voor elke DNS-wijziging. De geweigerde mail was niet terug te halen — hij schat dat het hem het vertrouwen van één taxatiebureau kostte, het grootste deel van een jaar. 🚀

👉 Een live domein veilig verhuizen: https://launchstudio.eu/nl/blog/lovable-custom-domain-migrating-a-live-domain-safely

#DNS #Lovable #EigenDomein #EmailDeliverability #LaunchStudio #Manifera
