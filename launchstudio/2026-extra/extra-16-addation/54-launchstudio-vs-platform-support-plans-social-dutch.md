🧘 Linda Smeets heeft vanuit Nijmegen een online cursusplatform voor yogadocenten, gebouwd met Lovable, Supabase, Vercel, Stripe en een e-mailprovider. Na een prijswijziging betaalden sommige studenten, maar kregen ze nooit toegang of de welkomstmail. Ze opende tickets bij Lovable, Supabase, Stripe en de e-mailprovider, en stelde een vraag op het forum van Vercel. 🎫

Elk platform antwoordde behulpzaam, en elk had gelijk: hun deel werkte. De bug zat ertussen: 🧠

❌ De webhook zocht cursussen na de prijswijziging op met een oud prijs-ID
❌ Die faalde stilletjes en gaf toch succes terug aan Stripe
❌ Dus probeerde Stripe het nooit opnieuw, en werd de toegang nooit gegeven
❌ Geen toegang betekende geen e-mail, en niemand keek naar de hele keten

✅ De handler gerepareerd zodat die productmetadata gebruikt in plaats van prijs-ID's
✅ Fouten geven nu een foutmelding terug, zodat Stripe het opnieuw probeert
✅ Meldingen toegevoegd bij mislukte webhooks
✅ 23 getroffen studenten afgestemd en toegang gegeven, met een excuusmail die Linda goedkeurde

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring met productiesystemen op veel platforms voor klanten zoals Vodafone en TNO, zorgen we voor uw app als geheel en werken we samen met platformsupport als hun deel aandacht nodig heeft. 🛠️

💡 Het resultaat: €2.600 plus €49 per maand, zes werkdagen. Elke getroffen student kreeg dezelfde dag toegang, en een latere wijziging van de Stripe-API werd twee maanden vóór de deadline afgehandeld. 🚀

👉 LaunchStudio versus de supportplannen van platforms: https://launchstudio.eu/nl/blog/launchstudio-vs-platform-support-plans

#Support #Stripe #Supabase #Lovable #AIFounder #LaunchStudio #Manifera
