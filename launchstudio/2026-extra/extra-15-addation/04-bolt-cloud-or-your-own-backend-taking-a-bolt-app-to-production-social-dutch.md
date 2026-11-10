🚨 Ruben Smits, trouwfotograaf in 's-Hertogenbosch, bouwde Fotodeel in Bolt: gasten scannen een QR-code, uploaden foto's naar een gedeelde galerij en downloaden de mooiste. Het draaide op een tiental bruiloften op Bolts ingebouwde hosting. Toen wilde een Brabantse keten van trouwlocaties het voor elk bruidspaar - met opslag in de EU, een verwerkersovereenkomst en verwijdering van alle foto's 90 dagen na elk evenement. 😳

Ruben ontdekte ook dat galerijen alleen beschermd waren door een link in de frontend, terwijl de bestandslijst voor elk evenement op te vragen was. Wanneer Bolt Cloud volstaat, en wanneer u een eigen backend nodig heeft: 🧠

❌ Galerijtoegang alleen geregeld via een moeilijk te raden link
❌ Bestandslijsten voor elk evenement op te vragen
❌ Een Stripe-sleutel in een frontendbestand
❌ Geen bewaarbeleid of gebruiksexport voor het contract met de locaties

✅ Een Supabase-project in Frankfurt met zo'n 41.000 foto's in privé-buckets
✅ Row Level Security per evenement, met signed URLs voor downloads
✅ Een geplande taak die foto's 90 dagen na elk evenement verwijdert
✅ De Stripe-sleutel naar een edge function verplaatst en geroteerd, plus een maandelijkse gebruiksexport

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring in productie-engineering, behouden we uw Bolt-frontend en geven we die een backend waar klanten mee akkoord kunnen gaan. 🛠️

💡 Het resultaat: €4.900, 12 werkdagen. Fotodeel ging live bij de keten en draaide in het eerste seizoen op zo'n 140 evenementen. De automatische verwijdering werd een verkoopargument. 🚀

👉 Bolt Cloud of een eigen backend? Zo beslist u: https://launchstudio.eu/nl/blog/bolt-cloud-or-your-own-backend-taking-a-bolt-app-to-production

#BoltNew #Supabase #GDPR #EventTech #AIFounder #LaunchStudio #Manifera
