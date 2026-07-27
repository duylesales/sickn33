🏝️ Sophie Lammers bouwde TideStay, een boekingsplatform voor vakantieverhuur en B&B's in Zierikzee en Schouwen-Duiveland, met Bolt vóór het zomerseizoen — ze nam aan dat omdat Bolt veilig was, haar app die beveiliging erfde. Een beoordeling vóór lancering ontdekte dat elk ingelogd hostaccount de boekingsgegevens van elke gast in het systeem kon opvragen. 😳

"Het platform is veilig" en "mijn app is veilig" zijn twee compleet verschillende zinnen. 🧠

❌ Geen row-level security — elke host kon de namen, aankomstdata en betaalgegevens van elke andere host zien
❌ Stripe was nog niet verder dan een gedeeltelijke, ongeteste configuratie
❌ Geen AVG-conform bewaarbeleid voor persoonsgegevens van gasten
❌ Ze kwam er pas drie weken vóór het begin van het piekboekingsseizoen achter

✅ Row-level security gebonden aan de eigen panden van elke host
✅ Stripe gemigreerd naar een volledig geteste live configuratie met webhookverificatie
✅ AVG-conform bewaarbeleid dat gastgegevens automatisch archiveert na de wettelijke periode

Bij **LaunchStudio** verifiëren we precies deze vier punten voordat een prototype live gaat — dezelfde standaard die Manifera toepast voor zakelijke klanten zoals Vodafone en TNO. 🛡️

Haar resultaat: TideStay lanceerde zijn volledige zomerseizoen met correct geïsoleerde gastgegevens over meer dan een dozijn hostpanden en nul gemelde data-incidenten. 🚀

👉 Lanceert u een seizoensgebonden boekingsapp? Laat het verifiëren vóór het seizoen begint, niet erin: [Link naar artikel]

#AINativeFounder #LaunchStudio #Manifera #DataSecurityAI #Zierikzee
