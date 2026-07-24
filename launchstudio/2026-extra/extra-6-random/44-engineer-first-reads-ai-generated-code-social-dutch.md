🔑 Kevin de Ruiter bouwde MonteurApp, een tool voor de buitendienst van monteurs, met Bolt — en voegde in de loop van meerdere maanden een kaartdienst, pushmeldingen en een onderdelenzoekintegratie toe. De eerste keer dat een engineer van LaunchStudio de codebase doorlas, sprong het patroon meteen eruit: hardgecodeerde API-sleutels, rechtstreeks vastgelegd in zes verschillende bestanden. 😳

Niet één onoplettendheid — zes, één voor elke integratie die Bolt ooit had toegevoegd. 🧠

❌ Elke integratie op dezelfde manier opgelost: de API-sleutel rechtstreeks in het bestand geplakt
❌ Zes afzonderlijke inloggegevens in platte tekst, klaar om live toegang tot elke verbonden dienst tegelijk weg te geven
❌ Er ging nooit iets stuk in de demo, dus niets signaleerde ooit het patroon
❌ Niemand — niet Kevin, niet de tool — merkte dat het meer dan één keer gebeurde

✅ Haal elke inloggegeven naar een goede setup voor geheimenbeheer
✅ Roteer elke blootgestelde sleutel, want alles dat in een repository is vastgelegd moet als gecompromitteerd worden behandeld
✅ Voeg een geautomatiseerde controle toe om het patroon op te sporen voordat het terugkeert

Bij **LaunchStudio** doen onze technici in Amsterdam dit soort eerste-leesreviews regelmatig — gesteund door Manifera, vertrouwd door klanten als Vodafone, TNO en CFLW. 🛡️

Zijn resultaat: MonteurApp beheert nu alle integratie-inloggegevens via één beveiligde configuratie, met een herhaalbare controle zodat de kortere weg niet stilletjes kan terugkeren. 🚀

👉 Klaar om een engineer daadwerkelijk uw codebase te laten lezen: [Link naar artikel]

#AINativeFounder #LaunchStudio #Manifera #CodeReview #AICodeSecurity
