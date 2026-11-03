🚨 Jelle Terpstra organiseert kleine concerten in Nijmegen en bouwde Zaalvol in v0: ticketverkoop, check-in aan de deur en uitbetalingen voor zalen tot 300 plaatsen. Zaaleigenaren wilden meteen beginnen. Maar wie beter keek, zag het: elk cijfer in het dashboard kwam uit voorbeelddata. 😳

v0 laat interfaces er echt uitzien. Wat het openlaat, is alles eronder. Dit miste Zaalvol:

❌ Geen echt schema - verkochte tickets kwamen nooit op de gastenlijst
❌ Een handmatige Stripe-betaallink zonder koppeling naar de app
❌ Mapbox- en geheime Stripe-sleutels in clientcomponenten
❌ Scannen aan de deur dat de rij blokkeerde bij zwakke wifi

✅ Een Supabase-schema in Frankfurt voor zalen, shows, tickettypes en bestellingen
✅ Supabase Auth met rollen voor zaaleigenaren en deurpersoneel
✅ Stripe Checkout met een ondertekende webhook die bij betaling tickets aanmaakt
✅ Geheimen naar server actions en offline-tolerant scannen met achtergrondsynchronisatie

Bij **LaunchStudio**, aangedreven door Manifera's 11+ jaar webengineering, behouden we elk v0-component en bouwen we de app eronder. 🧩

💡 Het resultaat: €5.900, vijftien werkdagen. Zaalvol verkocht in de eerste twee maanden zo'n 2.300 tickets voor 41 shows, met check-ins onder de twee seconden per scan. 🚀

👉 Wat uw v0-interface nog nodig heeft voordat echte klanten komen: https://launchstudio.eu/nl/blog/v0-app-to-production-backend-auth-and-deployment

#v0 #Vercel #NextJS #Ticketing #LaunchStudio #Manifera
