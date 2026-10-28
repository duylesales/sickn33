🚨 Yara Ouali, eigenaar van een klein reisbureau voor reizen op maat in Leidschendam, bouwde Reisdossier in Bolt: reizigers vullen passagiersgegevens in, uploaden paspoortscans, bekijken reisschema's, betalen termijnen en chatten met hun adviseur. Zo'n 1.100 reizigers. Toen vroeg een partner-touroperator om een privacyreview - en vond elf scripts van derden op elke pagina. 😳

Analytics, twee advertentiepixels, een heatmap met sessie-opname, een chatwidget, een reviewwidget, een lettertypedienst, een kaartbibliotheek en drie scripts van tools die Yara niet meer gebruikte. De sessie-opname legde namen, geboortedata en paspoortnummers vast terwijl reizigers typten. Alles laadde vóór de cookiebanner, kaartgegevens liepen via de eigen velden van het portaal, en er was geen Content Security Policy. Dit betekenen scripts van derden voor de beveiliging van AI-gegenereerde code:

❌ Scripts die niemand zich herinnerde, op elke pagina
❌ Sessie-opname die paspoortnummers vastlegt
❌ Trackers die afgaan vóór toestemming
❌ Kaartgegevens ingetypt in de eigen formulieren van de app

✅ Zes ongebruikte of overbodige scripts verwijderd, chat- en reviewwidgets beperkt tot pagina's zonder persoonlijke formulieren
✅ Privacyvriendelijke analytics met hosting in de EU, advertentiepixels alleen na toestemming en nooit op portaalpagina's
✅ Sessie-opname uit het portaal gehaald en opgenomen sessies bij de leverancier verwijderd
✅ Termijnbetalingen naar de gehoste checkout van Mollie, en een Content Security Policy ingevoerd - eerst report-only, daarna afgedwongen

Bij **LaunchStudio**, ondersteund door Manifera's 11+ jaar ervaring in productie-engineering en zijn wortels in cybersecurity, zorgen we dat de code die u niet zelf schreef niet langer het zwakste deel van uw app is. ⚙️

💡 Het resultaat: € 1.500, zes werkdagen. De touroperator keurde het portaal goed, het passagiersformulier laadt twee keer zo snel, en Yara keurt elk nieuw script nu goed aan de hand van een inventaris van één pagina. 🚀

👉 Beveiliging van AI-gegenereerde code: Externe scripts, widgets en de gegevens van uw klanten: https://launchstudio.eu/nl/blog/ai-generated-code-security-third-party-scripts-widgets-and-your-customers-data

#ScriptsVanDerden #CSP #Privacy #Bolt #LaunchStudio #Manifera
