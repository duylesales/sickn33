🚨 Niels Brandsma, backendontwikkelaar in Hoofddorp, bouwde SlotPark met Cursor: bedrijven rond Schiphol delen ongebruikte parkeerplaatsen met elkaars werknemers. Bewust met beveiliging bezig draaide hij Dependabot, Semgrep, gitleaks en een wekelijkse OWASP ZAP-scan. Alles groen. Twaalf bedrijven, 400 werknemers. Toen eiste een potentiële klant in luchtvaartdiensten een onafhankelijke review vóór het tekenen. 😳

De review vond niets wat de scanners in hun eigen categorieën hadden gemist - en vier dingen die ze niet konden zien. Elke werknemer kon boekingen van andere bedrijven bekijken en annuleren door een ID te veranderen. De API voor bedrijfsbeheerders controleerde of u beheerder was, maar niet van welk bedrijf. RLS stond aan met een policy die leesacties toestond voor elke ingelogde gebruiker. En factuurbedragen kwamen uit prijzen die de client meestuurde. Dit vinden scanners - en dit vindt alleen een beveiligingsaudit:

❌ Gebroken toegangsbeheer door een ID te veranderen
❌ Beheerderscontroles zonder tenantcontrole
❌ RLS die bestaat maar alles toestaat
❌ Prijzen overgenomen van de client

✅ Eigendoms- en tenantcontroles hersteld op de server
✅ RLS-policy's herschreven om per bedrijf en gebruiker af te bakenen
✅ Prijsberekening verplaatst naar de server
✅ 27 geautomatiseerde autorisatietests voor elke rol en tenantgrens, in dezelfde CI-pipeline als de scanners

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring in productie-engineering, gebruiken we tools als instrumenten - en menselijk oordeel voor wat ze niet kunnen weten: wie eigenaar hoort te zijn van welke data. ⚙️

💡 Het resultaat: € 1.250, vijf werkdagen. Het luchtvaartdienstenbedrijf tekende na het review- en hertestrapport, en het jaar daarna vingen de autorisatietests twee regressies op die de nog steeds groene scanners misten. 🚀

👉 AI-Applicatie Beveiligingsaudit vs. Geautomatiseerde Scanners: Wat Elk Instrument Ontdekt: https://launchstudio.eu/nl/blog/ai-application-security-audit-vs-automated-scanners-what-each-catches

#AppSecurity #SAST #DevSecOps #Cursor #LaunchStudio #Manifera
