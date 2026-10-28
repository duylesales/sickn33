🚨 Laurens Dijkman, oprichter van Vloerwijzer in Heemskerk, bouwde met Cursor een SaaS voor vloerenwinkels: personeel meet ruimtes op met een tablet, maakt offertes met materiaal- en arbeidskosten, en klanten tekenen en betalen online een aanbetaling. Na een beveiligingsaudit door een freelancer het jaar ervoor beschouwde Laurens de beveiliging als "klaar". Veertig winkels gebruikten het. Elf maanden en zo'n 300 wijzigingen met Cursor later vond de IT-adviseur van een winkel iets. 😳

Personeel van de ene winkel kon via een nieuw rapportage-endpoint de offertes en marges van een andere winkel zien. De review van de wijzigingen sinds de audit vond vier regressies: dat endpoint zonder tenantcontroles, een databasepolicy die tijdens het debuggen was versoepeld, een API-sleutel voor kaarten weer in de frontendbundle, en twee afhankelijkheden met gepubliceerde kwetsbaarheden. Niets had ze opgemerkt, omdat niets controleerde. Dit is eenmalige audit versus doorlopende beveiliging voor een groeiende AI-gebouwde SaaS:

❌ Een schoon rapport dat met elke wijziging verouderde
❌ Opnieuw gegenereerde code die ongemerkt toegangscontroles verwijdert
❌ Policy's die "tijdelijk" zijn versoepeld en nooit hersteld
❌ Geheimen en kwetsbare packages die terugsluipen

✅ Alle vier de regressies opgelost
✅ 38 negatieve autorisatietests voor elke rol en elke grens tussen tenants
✅ Scannen op geheimen en afhankelijkheden in CI, plus meldingen bij wijzigingen in databasepolicy's
✅ Een schema voor lichte reviews per kwartaal en managed hosting voor updates, back-ups en monitoring

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring in productie-engineering, laten onze audits vangrails achter - zodat bevindingen opgelost blijven terwijl u blijft uitbrengen. ⚙️

💡 Het resultaat: € 2.400 in acht werkdagen, plus € 49/maand. Het jaar daarna blokkeerde CI zes wijzigingen die toegang tussen tenants of geheimen opnieuw zouden hebben geïntroduceerd, vonden reviews per kwartaal alleen kleine problemen, en groeide Vloerwijzer naar 64 winkels. 🚀

👉 Beveiligingsaudit voor AI-applicaties: Eenmalig versus continue beveiliging voor groeiende SaaS: https://launchstudio.eu/nl/blog/ai-application-security-audit-once-vs-ongoing-security-what-a-growing-saas-needs

#SecurityAudit #DevSecOps #SaaS #Cursor #LaunchStudio #Manifera
