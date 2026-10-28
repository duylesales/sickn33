🚨 Stijn Vermeulen, frontendontwikkelaar in Voorburg, bouwde Paadje met Cursor: een abonnementsapp met geselecteerde Nederlandse wandelroutes, offline kaarten, GPX-downloads en routeverslagen. Hij deed bijna alles zelf - domein, SSL, DKIM/DMARC, Sentry, uptimecontroles, CI en staging. Vóór de lancering van betaalde abonnementen boekte hij een review van alleen de drie dingen waar hij zich stilletjes zorgen over maakte. Alle drie terecht. 😳

Premium GPX-bestanden kwamen uit een openbare bucket, dus de betaalmuur verborg alleen een knop. Opzeggingen bij Stripe werden niet afgehandeld, dus opgezegde abonnees hielden voor altijd premiumtoegang. En de RLS-policy op routeverslagen liet elke ingelogde gebruiker elk verslag bijwerken - Cursor had `using (auth.uid() is not null)` geschreven, en Stijns tests controleerden alleen mensen die hun eigen verslag bewerkten. Zo verdeelt u zelf doen en hulp bij het productierijp maken van een AI-gegenereerde app:

❌ Een betaalmuur in de interface, niet in de opslag
❌ Een abonnementslevenscyclus met alleen het ideale pad
❌ Een door AI geschreven policy die tests op het ideale pad doorstond
❌ Uw eigen code reviewen op wat u vergat

✅ Premiumbestanden achter goede opslagtoegang
✅ Opzeggingen, mislukte verlengingen en terugbetalingen bij Stripe afgehandeld
✅ RLS-policy's gecorrigeerd
✅ Negatieve tests toegevoegd aan CI - en samen doorgelopen zodat Stijn ze zelf kon uitbreiden

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring in productie-engineering, reviewen we graag alleen de riskante 20% terwijl u de andere 80% doet. ⚙️

💡 Het resultaat: € 1.600, zes werkdagen. Paadje bereikte in de herfst 1.900 betalende wandelaars; Stijn onderhoudt het alleen, en zijn negatieve tests hebben al één policyregressie uit een Cursor-refactor opgevangen. 🚀

👉 Een AI-Gegenereerde App Productierijp Maken: Zelf Doen met Cursor of Hulp Inschakelen?: https://launchstudio.eu/nl/blog/make-an-ai-generated-app-production-ready-diy-with-cursor-or-get-help

#IndieHacker #Cursor #Supabase #SoloOprichter #LaunchStudio #Manifera
