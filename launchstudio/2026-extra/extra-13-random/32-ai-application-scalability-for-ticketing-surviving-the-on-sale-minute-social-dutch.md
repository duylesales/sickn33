🚨 Kevin Oosterhuis, geluidstechnicus en promotor in Amsterdam-Noord, bouwde Zaalkaart op Replit: ticketing voor kleine muziekzalen en theaters, met Mollie-betalingen en QR-kaarten. Achttien zalen, evenementen van 150–600 mensen. Toen kondigde een bekende Nederlandse band een intieme show aan in een zaal met 450 stoelen — en om 10:00 probeerden 6.000 mensen te kopen. 😳

De evenementpagina bevroeg de database voor elke bezoeker en werd tergend traag. Beschikbaarheid werd in aparte stappen gecontroleerd en verlaagd, dus 38 stoelen werden twee keer verkocht. Kopers die in hun bankapp betaalden maar nooit terugkeerden, kregen geen kaarten. Er waren geen reserveringen tijdens de checkout, en een handvol accounts kocht elk 40 kaarten. Dit betekent schaalbaarheid van AI-applicaties voor ticketing:

❌ Voorraad gecontroleerd in code, niet afgedwongen in de database
❌ Geen reserveringen terwijl kopers betalen
❌ Betalingen bevestigd door de browser
❌ Niet-gecachete evenementpagina's en geen botlimieten

✅ Elke stoel een rij met een unique constraint op reservering/bestelling
✅ Reserveringen van 10 minuten met automatische vrijgave en een regel voor late betalingen
✅ Mollie-webhooks via een geverifieerde, idempotente wachtrij
✅ Gecachete evenementpagina's, een wachtkamer voor veelgevraagde evenementen, limieten per account en per kaart — en een loadtest met 10.000 gesimuleerde kopers

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring in productie-engineering, bouwen we voor de ene minuut waarin uw beste en slechtste dag samenvallen. ⚙️

💡 Het resultaat: € 4.800, veertien werkdagen. De volgende show van de zaal — 450 stoelen, zo'n 7.500 kopers in de eerste minuut — was in vier minuten uitverkocht, zonder overboeking, zonder ontbrekende kaarten en zonder account dat meer dan vier kocht. Sindsdien sloten nog negen zalen aan. 🚀

👉 Schaalbaarheid van AI-Applicaties voor Ticketing: Overleven Tijdens de Verkoopminuut: https://launchstudio.eu/nl/blog/ai-application-scalability-for-ticketing-surviving-the-on-sale-minute

#Ticketing #Schaalbaarheid #Replit #LiveMuziek #LaunchStudio #Manifera
