🚨 Wagenparkbeheer van Bram Terlouw regelt onderhoud, keuringen en brandstof voor 34 bedrijven en 1.900 voertuigen. Na achttien maanden waren wijzigingen pijnlijk traag geworden - dus maakte hij een week vrij en vroeg Cursor het hele project te herstructureren. Woensdag werkte er niets meer. 😳

Vier gigantische commits, geen tests, en drie dagen aan wijzigingen die hij niet uit elkaar kon halen. De dinsdag erna ging hij live met drie defecten - waarvan één onderhoudsrecords aan het verkeerde voertuig koppelde. Zo schoont u een AI-gebouwde codebase op zonder hem te breken:

❌ "Refactor het hele project" als één verzoek
❌ Geen testvangnet dat liet zien wat er kapot was
❌ Structuur en gedrag in dezelfde commits gewijzigd
❌ Terugdraaien betekende twee echte fixes kwijtraken samen met de schade

✅ Productie hersteld, dan eerst een vangnet: autorisatie over 26 endpoints, kernberekeningen, één end-to-end-flow
✅ Verwijderen als eigen ronde: 19 ongebruikte componenten, 7 dode endpoints (twee zonder authenticatie), 4 verlaten tabellen
✅ Duplicatie alleen opgelost waar het ertoe deed - een berekening van de keuringsdatum op vijf plekken, in twee varianten
✅ Een vaste regel: ruim op waar u werkt, in een eigen commit - nooit een opschoonweek

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring in productie-engineering, doen we de eerste opschoonronde bij het overnemen van een AI-gebouwd product - en die maakt alles daarna goedkoper. ⚙️

💡 Het resultaat: € 3.600, vier werkdagen herstel. Dezelfde opschoning werd daarna in drie maanden afgerond naast normaal functiewerk - zonder één incident dat klanten zagen. 🚀

👉 Refactoren in Cursor: een AI-gebouwde codebase veilig opschonen: https://launchstudio.eu/nl/blog/cursor-refactoring-cleaning-an-ai-built-codebase-safely

#Refactoring #Cursor #TechnischeSchuld #AICoding #LaunchStudio #Manifera
