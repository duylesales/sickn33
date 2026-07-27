🚨 Sanne de Wit besteedde zes weken aan het bouwen van Ledgerly — een gedeelde onkostentracker voor freelancers — bijna volledig in Cursor. Het zag er af. Tot een bètatester terloops opmerkte dat ze de boodschappenbonnetjes van een vreemde kon zien. 😳

AI-coderingstools optimaliseren voor "werkt het", niet voor "is het veilig" — en row-level security is het eerste dat stilletjes wordt overgeslagen. 🧠

❌ De onkostenrecords van elke gebruiker waren bereikbaar voor elke andere ingelogde gebruiker door simpelweg een ID in de URL te wijzigen
❌ De AI had de databasequery's gebouwd zonder ze te beperken tot de geauthenticeerde gebruiker
❌ Niemand merkte het op in zes weken testen — omdat de demo hier nooit op testte
❌ Haar geheime Stripe-sleutel stond ook in een client-blootgesteld omgevingsbestand

✅ Voeg row-level security toe zodat query's beperkt zijn tot de geauthenticeerde gebruiker, niet alleen "ingelogd"
✅ Voeg rate limiting toe aan de API voordat echt verkeer de gaten vindt
✅ Roteer en verplaats geheime sleutels weg uit alles wat de browser kan lezen

Bij **LaunchStudio** bouwen we voort op de meer dan 11 jaar ervaring van Manifera met productiesystemen voor klanten zoals Vodafone en TNO — dezelfde nauwkeurigheid die we toepassen op prototypes van solo-oprichters. 🛡️

Ledgerly werd negen dagen later opnieuw gelanceerd met correcte gegevensisolatie en doorstond een vervolg-penetratietest zonder kritieke bevindingen. 🚀

👉 Bouwt u momenteel met AI in Amsterdam? Laat vóór de lancering een gratis beveiligingscheck uitvoeren: [Link naar artikel]

#AINativeFounder #LaunchStudio #Manifera #AICoding #Amsterdam
