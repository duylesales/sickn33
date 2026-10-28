🚨 Startbewijs van Thijs Damen verwerkt inschrijvingen voor hardloop- en wielerevenementen van elf organisatoren rond Doetinchem en Arnhem. Normaal komen inschrijvingen verspreid over weken binnen. Toen opende een populaire regionale halve marathon de inschrijving met een maximum, om 20:00 op een dinsdag, met zo'n 4.000 wachtenden. Het product hield het elf minuten vol. 😳

Het lag vijftig minuten plat, en de organisator moest de opening verplaatsen. Dit breekt onder een piek op lanceerdag:

❌ Een nieuwe databaseverbinding per verzoek - de limiet bereikt bij zo'n 90 gelijktijdige gebruikers
❌ "Nog beschikbare plaatsen" geteld met een scan over een tabel zonder index, bij elke refresh
❌ De limiet van de e-mailprovider binnen vier minuten bereikt, dus mensen die al ingeschreven waren schreven zich opnieuw in
❌ Een landingspagina die de app opbouwde in plaats van als statisch bestand te serveren

✅ Connection pooling, gemeten op meer dan 2.000 gelijktijdige gebruikers
✅ Een teller bijgehouden door een trigger, en indexen op de kolommen van het inschrijfproces
✅ Statische landingspagina's, e-mails via een wachtrij binnen de limiet van de provider, en een uniciteitsconstraint tegen dubbele inschrijvingen
✅ Uitgavenlimieten, een feature flag voor de live teller, een statuspagina en een loadtest met 5.000 gelijktijdige gebruikers

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring in productie-engineering, testen we uw lancering onder belasting vóórdat uw klanten dat doen. 🏁

💡 Het resultaat: na zeven werkdagen en € 4.400 verwerkte de verplaatste opening 4.100 inschrijvingen in negen minuten, zonder downtime en met een piekresponstijd van 1,2 seconde. De 31 dubbele inschrijvingen werden terugbetaald - en de organisator heeft sindsdien drie extra evenementen ondergebracht. 🚀

👉 Een piek op lanceerdag overleven: https://launchstudio.eu/nl/blog/lovable-hosting-surviving-a-launch-day-spike

#Schaalbaarheid #Lovable #Loadtesting #Evenementen #LaunchStudio #Manifera
