🚨 Contributiebeheer van Jeroen Wijnstra int zo'n € 2 miljoen per jaar aan contributie voor 63 verenigingen en clubs. Hij liet Cursor zijn testsuite schrijven: 412 tests, 91% dekking, alles groen. Daarna schreef een incassorun 140 leden twee keer af. 😳

De functie erachter had elf tests. Alle elf slaagden - omdat ze op basis van de code waren gegenereerd en meeveranderden met de code, waardoor de bug als verwacht resultaat werd vastgelegd. Zo bouwt u een testsuite die u echt kunt vertrouwen:

❌ Tests die niets controleren dat kan falen: "rendert", "geeft een waarde terug", "mock werd aangeroepen"
❌ Assertions afgeleid van de implementatie in plaats van de bedrijfsregel
❌ Dekking als doel in plaats van gecontroleerd gedrag
❌ Een suite van vier minuten die genoeg vertrouwen gaf om op vrijdag een contributiewijziging te deployen

✅ 280 decoratieve tests verwijderd; 40 herschreven tegen de echte regels van de verenigingen
✅ Een autorisatietest per endpoint - die er drie van de 31 vond zonder enige controle
✅ Geldtests voor instromen halverwege het jaar, uitstromen, afronding, nul en het maximum, met lastige bedragen
✅ Een falende regressietest geschreven vóór de fix; 94 tests in 50 seconden, gekoppeld aan deployment

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring in productie-engineering, bouwen we de proportionele suite waardoor deployen niet langer zenuwslopend is. ⚙️

💡 Het resultaat: € 3.300, drie werkdagen. De 140 dubbele afschrijvingen werden terugbetaald, en de suite vangt nu op wat de 412 tests doorlieten. 🚀

👉 Cursor en tests: een testsuite genereren die u kunt vertrouwen: https://launchstudio.eu/nl/blog/cursor-and-tests-generating-a-suite-you-can-trust

#Testen #Cursor #AICoding #Softwarekwaliteit #LaunchStudio #Manifera
