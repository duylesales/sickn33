🚨 Cursor suggereerde een functie voor routeoptimalisatie, Vince Aarts accepteerde de suggestie omdat hij werkte, en ging verder. Wat hij niet wist: de code sloot nauw aan bij code onder een copyleft-licentie — en dat werd pas een probleem toen hij informele overnamegesprekken begon te voeren. ⚖️

🧠 AI-coderingstools suggereren code zonder er een licentie aan te koppelen. Meestal is dat onschuldig. Soms is het een sluimerende due-diligence-mijn in een codebase die u als "eigen" presenteert.

❌ Niets in de interface van Cursor gaf de herkomst van de suggestie aan, laat staan welke licentie erop van toepassing was
❌ Het product werkte prima, gebruikers merkten niets — het probleem komt pas boven water zodra het juridisch team van een overnemende partij een licentiescan uitvoert
❌ Een gemarkeerde copyleft-afhankelijkheid is in dat stadium geen snelle oplossing — het kan een deal vertragen of doden terwijl code onder tijdsdruk wordt herschreven, met advocaten die toekijken
❌ `npm audit` vangt gedeclareerde afhankelijkheden op, maar mist gekopieerde of nauw gespiegelde code die nooit via een pakketbeheerder is gegaan

✅ Scan de daadwerkelijke codebase op patronen die overeenkomen met bekende open-sourceprojecten, niet alleen package.json
✅ Controleer de licentie van elke afhankelijkheid, inclusief transitieve afhankelijkheden meerdere lagen diep
✅ Schrijf bij echte copyleft-conflicten een clean-room-vervanging, gebouwd vanuit de onderliggende logica, niet vanuit de gemarkeerde code

Bij **LaunchStudio** zijn beoordelingen van licentienaleving een standaardonderdeel van het voorbereiden van een codebase op financiering of overname, ondersteund door de 160+ opgeleverde projecten van Manifera voor klanten als Vodafone en TNO. 🛡️

Zijn resultaat: de codebase van RouteBoard doorstond een daaropvolgende informele licentiebeoordeling zonder vlaggen — een schone basis voor elk toekomstig overnamegesprek. 🚀

👉 Van plan om kapitaal op te halen of te verkopen? Laat eerst de licentiestatus van uw codebase checken: [Link naar artikel]

#AINativeFounder #LaunchStudio #Manifera #IndieHacker #DueDiligence
