🚨 Ilse Vermeer bouwde Groothandelportaal met Cursor en Supabase: restaurants en winkels bestellen online bij voedselgroothandels. Groothandels wilden bestellingen automatisch naar hun magazijnsystemen, dus voegde Cursor een databasetrigger toe die rechtstreeks de URL van elke groothandel aanriep. 😳

Was een magazijnsysteem traag, dan werd bestellen traag. Lag het eruit, dan faalden bestellingen. En het URL-veld accepteerde interne adressen - een SSRF-risico richting private netwerken. Zo bouwt u uitgaande webhooks voor uw SaaS-klanten: 🧠

❌ Bestellen geblokkeerd door trage systemen van klanten
❌ Geen handtekeningen en geen retries, dus bestellingen raakten zoek in magazijnen
❌ Payloads met interne margevelden
❌ URLs die interne netwerken konden bereiken

✅ Een eventstabel geschreven in dezelfde transactie, afgeleverd door een wachtrijworker
✅ Korte timeouts en exponential backoff over 24 uur
✅ HMAC-SHA256-handtekeningen, compatibel met Standard Webhooks
✅ Alleen HTTPS-URLs, gecontroleerd op private ranges, klantgerichte payloads, en logs met replay

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring in productie-engineering, behandelen we webhooks als het kleine product dat ze echt zijn. 🛠️

💡 Het resultaat: €5.100, 13 werkdagen. Bestellen werd onafhankelijk van de systemen van groothandels, er is sindsdien geen event meer verloren gegaan en het SSRF-risico was gedicht voordat het ooit werd misbruikt. 🚀

👉 Voegt u webhooks toe aan uw SaaS? Zo maakt u ze betrouwbaar en veilig: https://launchstudio.eu/nl/blog/outgoing-webhooks-for-your-saas-customers

#Webhooks #APIs #B2BSaaS #AppSecurity #AIFounder #LaunchStudio #Manifera
