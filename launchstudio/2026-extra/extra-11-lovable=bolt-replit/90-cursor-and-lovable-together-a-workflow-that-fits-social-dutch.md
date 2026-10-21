🚨 Ivo Schaminée bouwde Servicecontract met Lovable — administratie van onderhoudscontracten voor elf installatiebedrijven rond Oss en Uden — en gebruikte Cursor voor de onderdelen die de builder slecht deed. Op een donderdag bracht hij de verlengingsberekening lokaal samen. Op vrijdag vroeg een klant om een tekstwijziging van twee woorden. 😳

Hij deed die in de builder, die het bestand met de verlengingslogica opnieuw genereerde — en zijn hele donderdag was weg. Zo botsen twee tools op één codebase:

❌ Bedrijfslogica in een scherm dat de builder zonder aarzelen herschrijft
❌ Lokaal werk dat nog niet gepusht is terwijl de builder zijn eigen versie pusht
❌ Geen tests die een kapotte datumregel opvangen
❌ Twee tools die hetzelfde deel bewerken, zonder afspraak over wie wat beheert

✅ De verlengingsberekening in een eigen module, met de regel voor halverwege de maand bevestigd door drie bedrijven
✅ Tests rond de grensgevallen
✅ De repository als bron van waarheid, één gedeelde formatter, een gecommitte lockfile en regelbestanden voor beide tools
✅ Een eenvoudige werkafspraak: pullen voor u begint, pushen als u klaar bent, één tool per onderdeel tegelijk

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring in productie-engineering, richten we Lovable en Cursor zo in dat ze samenwerken in plaats van elkaar tegenwerken. 🔀

💡 Het resultaat: er waren al 34 herinneringen met verkeerde datums verstuurd voordat iemand het merkte. Na zeven werkdagen en € 3.300 waren die gecorrigeerd — en in de negen maanden daarna zijn er geen botsingen meer geweest. 🚀

👉 Cursor en Lovable samen — een werkwijze die past: https://launchstudio.eu/nl/blog/cursor-and-lovable-together-a-workflow-that-fits

#Cursor #Lovable #Werkwijze #GitHub #LaunchStudio #Manifera
