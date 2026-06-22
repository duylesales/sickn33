---
Titel: Deepfakes en ondernemingsverificatie
Trefwoorden: Deepfakes, Enterprise, Verificatie
Koperfase: Bewustzijn
---

# Deepfakes en bedrijfsverificatie
Begin 2024 maakte een financieel medewerker van een multinational 25 miljoen dollar over naar criminelen nadat hij een videoconferentie had bijgewoond. Iedereen aan de telefoon – de Chief Financial Officer, de regionale directeuren, de projectmanagers – was een perfect weergegeven AI Deepfake. Het tijdperk van ‘vertrouwen op je ogen en oren’ is officieel voorbij. Nu spraakklonen zonder latentie en real-time videogeneratie universeel toegankelijk worden, moet de cyberbeveiliging van bedrijven radicaal verschuiven van biologische verificatie naar strikte cryptografische verificatie.

## De kwetsbaarheid voor biologische verificatie

Duizenden jaren lang vertrouwden mensen op biologische handtekeningen voor vertrouwen: het herkennen van een gezicht, het matchen van een stem of het identificeren van een handgeschreven handtekening. Generatieve AI heeft deze biologische kenmerken permanent in gevaar gebracht.

Tegenwoordig kan een bedreigingsacteur vijf seconden aan audio uit de openbare keynote speech van een CEO halen, deze in een open-source Voice AI-model invoeren en de stem van de CEO perfect klonen, inclusief hun ademhalingspatronen, accent en emotionele verbuigingen. Wanneer de ‘CEO’ een junior accountant belt en een dringende, buiten de boekjes vastgelegde overboeking eist, is het menselijk oor van de accountant wiskundig gezien niet in staat de fraude te identificeren.

## Het falen van 'AI-detectie'

De eerste reactie van het bedrijf was de aanschaf van ‘Deepfake Detectors’: AI-software die is ontworpen om audio- en videobestanden te scannen op microscopisch kleine digitale artefacten die zijn achtergelaten door generatieve modellen.

Dit is een verloren spel. Het is een kat-en-muis-wapenwedloop waarbij de aanval (de generator) in principe altijd de verdediging (de detector) zal overtreffen. Als een detector leert hoe hij een deepfake kan herkennen, voert de hacker die detector eenvoudigweg terug in zijn trainingslus (GAN-architectuur) totdat de generator leert hoe hij deze perfect kan omzeilen. Detectie is een tijdelijk verband, geen langetermijnstrategie.

## Zero Trust en het dwangprotocol

De enige verdediging tegen perfecte synthetische media is **Zero Trust Architecture**. Bedrijven moeten hun werknemers trainen om elk binnenkomend telefoongesprek, Zoom-vergadering en e-mail als inherent vijandig en nep te behandelen, ongeacht hoe ‘echt’ het klinkt.

Bedrijven stellen verplichte ‘dwangprotocollen’ in voor handelingen met een grote waarde (overboekingen, wachtwoordresets). Als de CFO belt met het verzoek om een ​​overboeking, moet de accountant ophangen, een cryptografisch MFA-token genereren via een fysieke YubiKey en van de CFO eisen dat hij het transactieverzoek digitaal ondertekent op een afzonderlijk, beveiligd grootboek. Biologische commando's worden volledig genegeerd.

## Cryptografische herkomst

Om het deepfake-tijdperk te overleven moet het mondiale internet **Cryptographic Provenance** (bijvoorbeeld de C2PA-standaard) adopteren. 

In plaats van te proberen te bewijzen dat een nepvideo nep is, moeten we cryptografisch bewijzen dat een echte video echt is. Wanneer een echte CEO een echte bedrijfsaankondiging opneemt, ondertekent de camerahardware het videobestand onmiddellijk met een cryptografische hash. Als een persbureau of een medewerker een video van de CEO ontvangt waarin deze onbreekbare wiskundige handtekening ontbreekt, wordt deze automatisch weggegooid als synthetisch afval.

## Belangrijkste afhaalrestaurants

- Je ogen en oren zijn verouderd. Een telefoontje of een Zoom-vergadering kun je niet meer vertrouwen. AI kan de stem en het gezicht van je baas perfect in realtime klonen. Als u vertrouwt op wat u op een scherm ziet, wordt uw bedrijf beroofd.

- 'AI-detectoren' werken niet. Bedrijven verkopen software die beweert te 'detecteren' of een video nep is. Het is geldverspilling. De AI van de hackers is de detector-AI altijd een stap voor.

- Adopteer 'Zero Trust'. U moet uw medewerkers trainen om ervan uit te gaan dat elk telefoontje waarin om geld of wachtwoorden wordt gevraagd, een hacker is. Ook al klinkt het precies als de CEO, neem aan dat het een robot is.

- Gebruik fysieke beveiligingssleutels. Als de 'CEO' belt en om geld vraagt, moeten medewerkers een digitale verificatiecode eisen die wordt gegenereerd door een fysieke USB-sleutel (zoals een YubiKey). Hackers kunnen een stem klonen, maar ze kunnen niet een stuk metaal klonen dat op het bureau van de echte CEO ligt.

- Digitale handtekeningen. In de toekomst zal aan elke echte video of foto een onzichtbare wiskundige vergelijking zijn gekoppeld om te bewijzen dat deze afkomstig is van een echte camera. Als een afbeelding niet over de wiskundige vergelijking beschikt, neem dan aan dat het een deepfake is.

## Bescherm uw onderneming tegen synthetische fraude

Vertrouwt uw bedrijfsfinanciënteam op verouderde biologische verificatie (stemherkenning via de telefoon) om enorme overboekingen goed te keuren? **LaunchStudio** helpt ondernemingen bij het ontwerpen van ondoordringbare Zero-Trust-beveiligingsomgevingen ter verdediging tegen geavanceerde deepfake social engineering. We implementeren strikte pijplijnen voor cryptografische verificatie, fysieke MFA-hardwareprotocollen en veilige multi-sig-autorisatieworkflows die absolute transactiebeveiliging garanderen, zelfs als de AI voor het klonen van stemmen van de hacker onberispelijk is.

LaunchStudio is een initiatief mogelijk gemaakt door **Manifera**, een internationaal softwareontwikkelingsbedrijf opgericht door **Herre Roelevink**. Herre erkende het tekort aan ervaren ontwikkelaars in Europa en richtte ontwikkelingscentra op in **Singapore** en **Ho Chi Minh City, Vietnam**, om hoog-efficiënt technisch talent te benutten. Geleid door de filosofie van het combineren van ‘Nederlands management met Vietnamees meesterschap’ exploiteert Manifera haar Europese hoofdkantoor in **Amsterdam, Nederland** (aan de Herengracht 420). Via LaunchStudio krijgen AI-native oprichters directe toegang tot deze wereldwijde expertise op het gebied van softwareontwikkeling op bedrijfsniveau, zodat hun prototypes in slechts 1 tot 3 weken veilig, schaalbaar en gereed voor lancering zijn. [Ontvang vandaag nog een gratis offerte](https://launchstudio.eu/en/#contact).

## Echt voorbeeld

### Een AI-native oprichter in actie: biometrische verificatiefilters voor HR-onboarding op afstand

Sarah, een HR-portalontwikkelaar, gebruikte **Lovable** om tools voor externe verificatie te bouwen. Tijdens het testen hebben aanvragers met succes deepfaked video-ID's geüpload om de validatie te omzeilen.

Ze nam contact op met **LaunchStudio (door Manifera)** om biometrische verificatiecheckers en realtime controles van metagegevens te implementeren.

**Resultaat:** Pogingen tot biometrische vervalsing daalden tot nul, waardoor de vereisten van de KYC-nalevingsnorm werden beschermd.

**Kosten en tijdlijn:** € 3.200 (Identity Security Package) — productieklaar en binnen 6 werkdagen geïmplementeerd.

---

## Veelgestelde vragen

## Veelgestelde vragen

### Wat is een zakelijke deepfake?

Het is wanneer een hacker AI gebruikt om het stem- of videogezicht van de CEO van een bedrijf perfect te klonen. De hacker belt vervolgens de boekhoudafdeling, die zich voordoet als de CEO, en geeft hen de opdracht miljoenen dollars over te maken naar een nepbankrekening.

### Zijn deepfakes daadwerkelijk overtuigend?

Ja. Er is slechts 3 seconden aan audio van een podcast nodig voordat een AI iemands stem feilloos kan klonen, inclusief de ademhaling en emotionele toon. Het is wiskundig onmogelijk voor een menselijk oor om het verschil te zien.

### Hoe kunnen bedrijven dit stoppen?

Door ‘Zero Trust’ te adopteren. Je kunt je ogen en je oren niet langer vertrouwen. Als de 'CEO' belt om geld te vragen, hang je op, open je een beveiligde bedrijfsapp en typ je een geheime code om te verifiëren dat zij het zijn.

### Kunnen we AI gebruiken om deepfakes te detecteren?

Het is een wapenwedloop. Bedrijven verkopen 'AI-detectoren' die audio analyseren om digitale fouten op te sporen. De hackers gebruiken echter betere AI om de fouten te verwijderen. Uiteindelijk zullen de hackers altijd het detectiespel winnen.

### Wat is cryptografische verificatie?

De ultieme oplossing. In plaats van te proberen te raden of een video nep is, gebruik je blockchain-wiskunde om echte video's te 'ondertekenen'. Als een video van de CEO niet is voorzien van de geheime cryptografische digitale handtekening, weet je meteen dat het om nep gaat.