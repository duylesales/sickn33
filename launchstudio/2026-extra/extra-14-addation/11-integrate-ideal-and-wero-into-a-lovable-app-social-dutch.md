🚨 Sanne Mulder heeft een kleine kwekerij in Haarlem en bouwde Stekje in Lovable: een maandabonnement met een stek, verzorgingsinstructies en een pot. Een vermelding op Instagram leverde veel verkeer op - en meer dan de helft van de mensen die de checkout bereikten, vertrok zonder te betalen. 😳

Een snelle peiling onder haar volgers gaf het antwoord: ze wilden iDEAL. De Stripe-checkout van Lovable bood alleen kaarten, en de eerste poging met iDEAL maakte het erger. Dit ging er mis:

❌ Een checkout met alleen kaarten voor Nederlandse kopers
❌ iDEAL toegevoegd als eenmalige betaling per maand, dus verlengingen hingen af van klanten die eraan dachten
❌ Abonnementen geactiveerd op de succespagina - ook voor klanten die in hun bankapp annuleerden
❌ De geheime Stripe-sleutel in frontendcode

✅ Eerste betaling via iDEAL, met een SEPA-incassomachtiging voor automatische verlengingen
✅ Abonnementen alleen geactiveerd door een geverifieerde webhook
✅ Geannuleerde en verlopen betalingen netjes afgehandeld
✅ Geheime sleutel verplaatst naar een edge function, plus een beheeroverzicht van mislukte verlengingen

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar Nederlandse betaalintegraties vanuit Amsterdam, voegen we iDEAL toe onder uw Lovable-schermen - klaar voor de overstap naar Wero. 🛠️

💡 Het resultaat: €2.300, acht werkdagen. Het aandeel afgeronde checkouts steeg van ongeveer 45% naar zo'n 80%, en Stekje groeide tegen het einde van het seizoen naar ongeveer 340 actieve abonnees. 🚀

👉 Verkoopt u vanuit een Lovable-app aan Nederlandse klanten? Zo voegt u iDEAL toe en bereidt u zich voor op Wero: https://launchstudio.eu/nl/blog/integrate-ideal-and-wero-into-a-lovable-app

#iDEAL #Wero #Lovable #Stripe #LaunchStudio #Manifera
