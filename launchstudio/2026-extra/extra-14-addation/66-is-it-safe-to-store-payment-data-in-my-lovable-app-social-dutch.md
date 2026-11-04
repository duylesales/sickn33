🚨 Dennis Groot organiseert regionale bordspelbeurzen en bouwde Spelbeurs in Bolt voor tickets en toernooitafels. Hij vroeg Bolt om "sneller afrekenen voor terugkerende bezoekers". Bolt bouwde een formulier dat kaartnummers, vervaldatums en CVC-codes opsloeg in een tabel saved_cards. Een bevriende ontwikkelaar vond die tijdens het oplossen van een andere bug: 312 kaarten. 😳

Hij vroeg om sneller afrekenen. Hij kreeg een database vol kaartnummers die nooit had mogen bestaan. Zo erg was het:

❌ Volledige kaartnummers en CVC-codes opgeslagen in zijn eigen database
❌ Kaartgegevens die bij elke aankoop vanuit zijn app naar de betaal-API werden gestuurd
❌ De service key in de frontend, waardoor iedereen de tabel ondanks RLS had kunnen lezen
❌ Betaalvelden die in de logs verschenen

✅ Het eigen formulier en de tabel verwijderd, en de opgeslagen kaartgegevens veilig gewist
✅ Alle sleutels geroteerd
✅ De gehoste checkout van de provider, met opgeslagen betaalmethoden die de provider zelf beheert
✅ Geverifieerde webhooks gekoppeld en betaalvelden uit de logs verwijderd

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar integraties met Stripe, Mollie en PayPal, is "nooit kaartgegevens aanraken" een vaste regel - alleen verwijzingen, nooit kaartnummers. 🛠️

💡 Het resultaat: €1.700, vier werkdagen. Terugkerende bezoekers rekenen nog steeds met één klik af via de opgeslagen betaalmethoden van de provider, en de app slaat helemaal geen kaartgegevens meer op. 🚀

👉 Slaat uw AI-gebouwde app betaalgegevens op die er niet horen? Dit mag u wel en niet bewaren: https://launchstudio.eu/nl/blog/is-it-safe-to-store-payment-data-in-my-lovable-app

#PCIDSS #Betalingen #Stripe #AppSecurity #LaunchStudio #Manifera
