🚨 Kim Verheul verhuurt kleine elektrische bootjes in Vlaardingen en bouwde Bootje in Lovable als "maar een MVP": klanten kiezen een boot en een tijdslot, betalen een borg en krijgen een digitale code voor het bootslot. Ze wilde het één zomer testen. Binnen drie weken kwamen er zo'n 400 boekingen binnen. Toen werd een boot meegenomen door iemand die hem niet had geboekt - met een slotcode uit de boeking van een andere klant. 😳

Elke boeking - naam, telefoonnummer en slotcode - was via de API leesbaar voor elke ingelogde gebruiker. Borgsommen werden bevestigd via de redirect in de browser, dus sommige klanten kregen codes zonder te betalen. De Mollie-sleutel stond in de frontend, er waren geen back-ups, en de database stond in een Amerikaanse regio. Dit verbergt het etiket "het is maar een MVP":

❌ Slotcodes leesbaar voor elke gebruiker
❌ Codes uitgegeven voordat de betaling was bevestigd
❌ Een betaalsleutel in de browser
❌ Geen back-ups en data buiten de EU

✅ Toegang tot boeking en slotcode beperkt tot de boeker - en alleen geldig tijdens het geboekte slot
✅ Borgsommen bevestigd via Mollie-webhooks voordat er een code wordt uitgegeven
✅ Sleutelrotatie, migratie naar de EU met back-ups en een geteste restore
✅ Accounts samengebracht en meldingen ingericht - met de functies precies zo klein als voorheen

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring in productie-engineering, houden we uw MVP klein - maar nooit de veiligheid ervan. ⚙️

💡 Het resultaat: € 2.200, acht werkdagen. Bootje sloot de zomer af met zo'n 1.900 boekingen zonder nieuw onbevoegd gebruik van boten, en breidde het voorjaar daarna uit naar een tweede jachthaven - met dezelfde minimale functies. 🚀

👉 AI-App Productieproblemen Vermomd als 'Het Is Maar een MVP': https://launchstudio.eu/nl/blog/ai-app-production-problems-hidden-behind-its-just-an-mvp

#MVP #StartupLancering #Lovable #Verhuur #LaunchStudio #Manifera
