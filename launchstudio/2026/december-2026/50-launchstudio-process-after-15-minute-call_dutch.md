---
Titel: "Het LaunchStudio-proces: Wat Gebeurt er Nadat Je Je Gesprek van 15 Minuten Boekt"
Trefwoorden: AI-ontwikkeling, AI-deployment, app bouwen met AI, AI-app-ontwikkeling, LaunchStudio, Manifera
Koperfase: Beslissing
Doelgroep: AI-Native Founder (niet-technisch)
---

# Het LaunchStudio-proces: Wat Gebeurt er Nadat Je Je Gesprek van 15 Minuten Boekt

De onzekerheid van "wat gebeurt er precies als ik dit boek?" houdt meer founders tegen dan de prijs zelf. Onzekerheid over proces, niet prijs, is vaak het echte dat een aarzelende founder ervan weerhoudt dat eerste gesprek te boeken. Dit is een concrete, stap-voor-stap-doorloop van precies wat er gebeurt nadat je dat doet.

## Stap 1: Het Introductiegesprek van 15 Minuten

Je beschrijft je product, wat je al hebt gebouwd (doorgaans met Lovable, Bolt, Cursor of v0), en wat je hoopt te bereiken — een lanceringsdeadline, een specifieke zorg zoals beveiliging, of algemene "maak dit productieklaar"-begeleiding. Geen technische achtergrond vereist; het gesprek is gestructureerd zodat founders hun situatie in gewone taal beschrijven, en het LaunchStudio-team vertaalt dat naar technische scope aan hun kant.

## Stap 2: Codebase-beoordeling en Scoping

Na het gesprek beoordeelt het team de codebase van je daadwerkelijke prototype om te beoordelen wat er bestaat, wat er ontbreekt tegen de zeven-lagen-productiestack (frontend, AI/model-laag, authenticatie, database, betalingen, hosting, monitoring), en welk specifiek werk nodig is om de gaten voor jouw specifieke product en doelen te dichten.

## Stap 3: Vastgeprijsde Offerte en Tijdlijn

Je ontvangt een specifieke, gespecificeerde offerte — geen vage range — samen met een toegezegde tijdlijn, doorgaans één tot drie weken afhankelijk van scope. Dit is het punt waarop je beslist of je doorgaat; er is geen verplichting gecreëerd door het eerste gesprek of de scopingbeoordeling.

## Stap 4: Kickoff en Ontwikkeling

Zodra je de offerte goedkeurt, begint Manifera's engineeringteam met werken. Je frontend-ontwerp wordt behouden als het vaste startpunt (zoals behandeld in eerdere frontendbehoudsrichtlijnen), waarbij het team de ontbrekende infrastructuurlagen eromheen bouwt — authenticatie, databasebeveiliging, betalingen, hostingconfiguratie.

## Stap 5: Voortgangscommunicatie

Gedurende de ontwikkeling ontvang je regelmatige updates over voortgang — geen stilte tot een plotseling "het is klaar"-bericht. Voor founders met harde externe deadlines (een lanceringsevenement, een klantverplichting) wordt voortgangscommunicatie gekalibreerd naar die urgentie.

## Stap 6: Testen en Beoordeling

Vóór de definitieve levering test het team kritieke flows (aanmelding, kerngebruik van functies, betalingsverwerking) en, voor beveiligingsgevoelige projecten, voert het soort cross-account-isolatietests uit behandeld in eerdere multi-tenant-architectuurrichtlijnen. Je wordt uitgenodigd om het live, gedeployde product zelf te beoordelen voordat de opdracht als voltooid wordt beschouwd.

## Stap 7: Lancering en Ondersteuning na Lancering

Je product gaat live op je eigen domein, onder je eigen accounts, met je code-eigendom volledig intact. Afhankelijk van je pakket gaat 48-uurs ondersteuning na lancering (Launch Ready) of doorlopende prioriteitsondersteuning met managed hosting (Launch & Grow, €49/maand) daarna door.

## Wat Er Niet Gebeurt

Geen herontwerp van je interface zonder expliciete bespreking. Geen open-einde uurtarief-verrassingen, zoals behandeld in eerdere vastprijsrichtlijnen. Geen druk om diensten te kopen buiten wat jouw specifieke project daadwerkelijk nodig heeft — het doel is een afgebakende, eerlijke opdracht, geen maximalisering van factureerbare scope.

[Boek je gesprek van 15 minuten](https://launchstudio.eu/en/#contact) — de eerste, vrijblijvende stap in precies dit proces.

## Achter Stap 2: Hoe de Zeven-Lagen-Analyse Daadwerkelijk Werkt

Founders willen begrijpelijkerwijs weten wat er precies gebeurt tijdens de codebase-beoordeling, aangezien dit de stap is die zowel de offerte als de daaropvolgende tijdlijn bepaalt. De beoordeling is geen enkele technische check-in-één-keer — het zijn zeven vrij nauw omschreven inspecties, elk corresponderend met één productiegereedheidslaag, die elk een specifiek geslaagd, gezakt, of gedeeltelijk verdict opleveren in plaats van een vage algemene indruk.

**Wat wordt gecontroleerd, laag voor laag:**
1. **Frontend** — is de interface stabiel, of breekt hij onder toestanden waar de oorspronkelijke build nooit op getest is (lege data, foutresponses, trage verbindingen)? Deze laag slaagt meestal grotendeels zoals hij is, aangezien dit is waar founders de meeste iteratietijd in hun AI-tool aan besteedden.
2. **AI/model-laag** — wordt de model-aanroep veilig gedaan vanaf een serverroute, of blootgesteld aan de clientzijde? Is er een fallback als de AI-provider een time-out krijgt of misvormde output teruggeeft?
3. **Authenticatie** — bestaat er een echt sessie- en wachtwoordhashingsysteem, of is "inloggen" cosmetisch, met een naam opgeslagen in local storage zonder daadwerkelijke verificatie?
4. **Database** — is er oprechte rij-niveau-isolatie tussen gebruikers, of staat het schema technisch toe dat elke geauthenticeerde gebruiker de data van iemand anders kan opvragen?
5. **Betalingen** — bestaat er een betalingsverwerkerintegratie, en handelt die correct mislukte betalingen, terugbetalingen, en abonnementsstatuswijzigingen af?
6. **Hosting** — is de huidige deployment stabiel onder gelijktijdige belasting, of is die alleen ooit getest door de founder in zijn eentje?
7. **Monitoring** — waarschuwt er iets het team als het product plat gaat of fouten begint te geven, of zou een founder het alleen ontdekken via een boze klant-e-mail?

Elke laag krijgt een specifieke notitie in het scopingdocument — niet "heeft werk nodig" maar het precieze gat, zoals "geen rij-niveau-beveiligingsbeleid geconfigureerd op de boekingentabel" — omdat vage bevindingen vage offertes opleveren, en vage offertes zijn precies wat founders die deze stap overwegen, proberen te vermijden.

**Waarom dit een vaste offerte oplevert in plaats van een range:** omdat de bevinding van elke laag specifiek is in plaats van bij benadering, kunnen de engineeringuren die nodig zijn om elk gat te dichten met echt vertrouwen worden geschat, in plaats van opgevuld om onzekerheid af te dekken. Een founder wiens authenticatie al correct Supabase Auth gebruikt, krijgt een kleiner offertecomponent voor die laag dan een founder wiens "authenticatie" decoratief blijkt te zijn — de beoordeling stuurt direct het cijfer, in plaats van dat het cijfer eerst wordt vastgesteld en achteraf gerechtvaardigd.

Dit is ook waarom de codebase-beoordeling vóór de offerte plaatsvindt, niet andersom: een vaste prijs offreren zonder eerst de daadwerkelijke zeven lagen te inspecteren zou gokken vereisen, en gokken is precies het open-einde-facturatierisico dat vastgeprijsde offertes juist zijn ontworpen om te elimineren. Dit is de mechanische reden waarom de offerte van Stap 3 gespecificeerd kan zijn in plaats van bij benadering, en de reden waarom twee founders die vergelijkbaar klinkende producten beschrijven tijdens hun eerste gesprek toch betekenisvol verschillende offertes kunnen ontvangen zodra hun daadwerkelijke codebases zijn beoordeeld.

**Wat founders vooraf kunnen doen om deze stap sneller te maken:** de live URL van je prototype klaar hebben, en indien mogelijk een manier om leestoegang tot de codebase te verlenen (een GitHub-link, of een export vanuit Lovable, Bolt, Cursor, of v0), vóór de codebase-beoordeling betekent dat de zeven-lagen-inspectie direct kan beginnen in plaats van te wachten op toegangslogistiek. Founders hoeven zelf geen technische samenvatting voor te bereiden — gaten accuraat beschrijven is precies waarvoor de beoordeling bestaat — maar de daadwerkelijke code toegankelijk hebben, in plaats van alleen een beschrijving van wat het hoort te doen, is wat Stap 2 verandert van een gesprek in een oprechte inspectie met een specifiek, verdedigbaar verdict per laag.

## Echt voorbeeld

### Een AI-native founder in actie: elke stap doorlopen, van begin tot eind

Puck, een activiteitencoördinator voor kinderen in Culemborg, bouwde SpeelAgenda, een AI-tool die leeftijdsgeschikte lokale activiteiten en evenementen suggereerde aan ouders op basis van de leeftijden en interesses van hun kinderen, met v0. Ze had weken geaarzeld voordat ze LaunchStudio's introductiegesprek boekte, specifiek omdat ze niet begreep wat er daadwerkelijk zou gebeuren — zou ze onder druk gezet worden voor een grote aankoop, zou haar ontwerp veranderd worden zonder haar input, zou de tijdlijn betrouwbaar zijn?

Pucks gesprek van 15 minuten behandelde haar prototype, haar doel om te lanceren voor het nieuwe schooljaar, en haar specifieke zorg over het wijzigen van haar ontwerp. De daaropvolgende codebase-beoordeling identificeerde de concrete gaten: geen echte authenticatie, geen manier om de kleine maandelijkse vergoeding te rekenen die ze had gepland, en een database zonder correcte dataisolatie voor ouderaccounts. Ze ontving een vaste offerte van €2.250 met een tijdlijn van 11 werkdagen — geen druk, geen upsell buiten wat haar project daadwerkelijk nodig had.

Puck keurde de offerte goed, en de ontwikkeling verliep met wekelijkse voortgangsupdates gezien haar schooljaardeadline. Testen vóór levering omvatte dat Puck persoonlijk verifieerde dat twee aparte ouder-testaccounts niet bij elkaars kinderdata konden komen. SpeelAgenda lanceerde op haar eigen domein, in haar eigen accounts, met haar originele ontwerp volledig ongewijzigd.

**Resultaat:** SpeelAgenda lanceerde drie dagen voor Pucks zelfopgelegde schooljaardeadline, waarbij het hele proces exact verliep zoals beschreven tijdens het eerste gesprek — wat de onzekerheid wegnam die Puck weken had weerhouden van boeken.

> *"Ik had het boeken van het gesprek een maand uitgesteld omdat ik niet wist waar ik me precies voor aanmeldde. Elke stap gebeurde exact zoals ze het vooraf beschreven — geen verrassingen, geen druk, geen wijzigingen aan mijn ontwerp waar ik niet eerst mee instemde."*
> — **Puck Willems, Founder, SpeelAgenda (Culemborg)**

**Kosten & tijdlijn:** €2.250 (Launch Ready Pakket) — live in 11 werkdagen.

---

## Veelgestelde vragen

### Is er een verplichting of kosten verbonden aan het eerste gesprek van 15 minuten?

Nee. Het gesprek is gratis en creëert geen verplichting om door te gaan — het bestaat specifiek om je te helpen je opties te begrijpen en een accuraat gevoel voor scope te krijgen voordat je beslist of je doorgaat met een betaalde opdracht.

### Hoe lang duurt het codebase-beoordelings- en offerteproces doorgaans na het eerste gesprek?

Dit varieert per projectcomplexiteit, maar founders ontvangen doorgaans een vaste offerte binnen een paar werkdagen na het eerste gesprek, zodra het team de tijd heeft gehad om de codebase van het bestaande prototype correct te beoordelen.

### Wat als ik het ergens niet mee eens ben tijdens het ontwikkelingsproces, zoals een voorgestelde technische aanpak?

Directe communicatie gedurende de opdracht betekent dat zorgen kunnen worden geuit en aangepakt zodra ze opkomen, in plaats van pas ontdekt te worden bij de definitieve levering — dit is deel van waarom regelmatige voortgangscommunicatie (Stap 5) een bewust onderdeel van het proces is, geen bijzaak.

### Kan ik wijzigingen in de scope aanvragen nadat de vaste offerte is goedgekeurd?

Ja, hoewel zoals behandeld in vastprijsrichtlijnen, scopewijzigingen expliciet worden besproken en overeengekomen in plaats van stilletjes geabsorbeerd of stilletjes genegeerd — een oprechte uitbreiding van scope kan de prijs en tijdlijn aanpassen, transparant gecommuniceerd voordat er wordt doorgegaan.

### Verschilt het proces voor de Launch Ready- versus Launch & Grow-pakketten?

Het kernproces (gesprek, scoping, offerte, ontwikkeling, testen, lancering) is hetzelfde voor beide. Het verschil zit voornamelijk in wat er in de scope zelf is inbegrepen — Launch & Grow voegt betalingsintegratie, managed hosting, en doorlopende ondersteuning toe bovenop Launch Ready's kern-productiegereedheidsscope.
