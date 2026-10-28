🚨 Transportplanner van Ruud Schipper beheert transportorders voor 26 regionale transportbedrijven, en hun grootste verladers sturen orders automatisch vanuit hun eigen systemen. Er was geen echte API - verladers riepen de REST-endpoints van Supabase rechtstreeks aan, elk met de service role key. Toen hernoemde een AI-assistent tijdens een refactor twee kolommen. 😳

De systemen van negen verladers maakten geen orders meer aan. Twee dagen lang kwamen zo'n 1.100 transportorders stil nooit binnen - en de service keys bleken elke verlader volledige toegang te geven tot de data van elk transportbedrijf. Zo geeft u versies aan een API waarvan uw klanten afhankelijk zijn:

❌ Het databaseschema blootgesteld als "API", dus een hernoemde kolom brak klanten
❌ De service role key uitgedeeld aan integratoren
❌ Geen specificatie, geen controle op brekende wijzigingen, geen gebruikslogs
❌ Geen idempotentie, geen beleid voor uitfaseren, geen changelog

✅ Service key direct geroteerd; afgebakende, gehashte API-sleutels per organisatie
✅ Een eigen /v1-API met een OpenAPI-specificatie, envelopes, cursorpaginering, UTC-tijden, vaste foutcodes en idempotency keys
✅ Een compatibiliteitslaag voor oude veldnamen gedurende zes maanden, met Deprecation- en Sunset-headers en een migratiegids
✅ Vergelijking van de specificatie en contracttests in CI die falen bij brekende wijzigingen, plus ondertekende webhooks met versies en gebruikslogs per sleutel

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring in productie-engineering, bouwen we de API-laag voordat uw eerste integratieklant ervan afhankelijk wordt. ⚙️

💡 Het resultaat: € 6.200, vijf werkdagen. De orders werden binnen een dag opnieuw aangemaakt. Sindsdien: veertien API-releases zonder één brekend incident, drie riskante pull requests tegengehouden door CI, en twee grote verladers in elk een week gekoppeld zonder één telefoontje. 🚀

👉 AI-app-architectuur: versies geven aan een API waarvan klanten afhankelijk zijn: https://launchstudio.eu/nl/blog/ai-app-architecture-versioning-an-api-customers-depend-on

#API #Softwarearchitectuur #SaaS #Supabase #LaunchStudio #Manifera
