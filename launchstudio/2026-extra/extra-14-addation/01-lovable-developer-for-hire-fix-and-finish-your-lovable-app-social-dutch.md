🚨 Lotte van Rijn, oud-docent uit Groningen, bouwde Bijlespunt in Lovable: ouders boeken bijles voor wiskunde en talen, chatten met de docent en betalen per les. Twaalf docenten, veertig proeflessen geboekt. Toen mailde een ouder: ze kon de berichten van een ander gezin met hun docent lezen. 😳

Lotte vroeg Lovable het drie keer te repareren. Elke fix veranderde wat er op het scherm stond, maar de query eronder haalde nog steeds elk gesprek op. Dit is wat een Lovable developer echt repareert:

❌ Row Level Security waardoor iedereen elke chat kon lezen
❌ Een geheime Stripe-sleutel in een frontendbestand
❌ Dubbele klikken die ouders twee keer lieten betalen
❌ Geen staging, dus elke prompt ging direct live

✅ RLS-policies zodat gebruikers alleen hun eigen gesprekken zien
✅ De Stripe-sleutel verplaatst naar een Supabase edge function
✅ Een idempotency key op boekingen: één klik, één betaling
✅ Een stagingproject plus uptime- en foutmeldingen op Lottes telefoon

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring in productie-engineering, behouden we uw Lovable-frontend en repareren we alleen wat eronder zit. 🛠️

💡 Het resultaat: €2.600, elf werkdagen. Bijlespunt verwerkte het schooljaar daarna zo'n 1.400 lessen zonder één melding van gelekte gegevens - en Lotte bouwde gewoon verder in Lovable. 🚀

👉 Een Lovable developer nodig die uw app niet opnieuw bouwt? Dit kunt u verwachten: https://launchstudio.eu/nl/blog/lovable-developer-for-hire-fix-and-finish-your-lovable-app

#Lovable #Supabase #EdTech #AIFounder #LaunchStudio #Manifera
