---
Titel: "AI-Prototype naar Productie: 12 Vragen Vóór Je een Offerte Ondertekent"
Trefwoorden: ai-prototype naar productie, ontwikkelofferte, vragen aan developer, fixed-price offerte, lovable, LaunchStudio, Manifera
Koperfase: Decision
Doelgroep: AI-Native Oprichter (Niet-Technisch)
---

# AI-Prototype naar Productie: 12 Vragen Vóór Je een Offerte Ondertekent

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "AI-Prototype naar Productie: 12 Vragen Vóór Je een Offerte Ondertekent",
  "description": "Twaalf kritische vragen die niet-technische oprichters moeten stellen aan elke freelancer, softwarebureau of specialist voordat ze een offerte ondertekenen om een AI-prototype naar productie te brengen — over scope, intellectueel eigendom, verificatie, vaste prijzen en nazorg.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-11-14",
  "inLanguage": "nl-NL",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/ai-prototype-to-production-twelve-questions-before-you-sign-any-quote" }
}
</script>

Een offerte is een belofte op papier, opgesteld in een technisch jargon dat je als niet-technische ondernemer wellicht niet vloeiend spreekt. Wanneer je een externe partij vraagt om jouw met AI gebouwde prototype productierijp te maken, staat het voorstel vaak vol termen als "security hardening", "backend-integratie" en "deployment-infrastructuur". Het is daardoor verdomd lastig in te schatten of een bedrag van € 3.000 een buitenkans is of een financiële valkuil. Je kunt de programmacode zelf niet direct beoordelen. Maar je kunt wél haarfijn beoordelen hoe een leverancier reageert op de juiste vragen.

Deze twaalf vragen werken universeel voor freelancers, traditionele softwarebureaus en gespecialiseerde partijen — inclusief onszelf. Bij elke vraag lees je exact hoe een professioneel antwoord klinkt, en welk antwoord juist alle alarmbellen moet doen rinkelen.

## Over de Scope en Afbakening

**1. "Wat bekijken jullie van mijn app vóórdat jullie een prijs afgeven?"**
- *Goed antwoord:* "We bestuderen eerst de broncode, de database en de hostingconfiguratie — of we inspecteren de repository gezamenlijk tijdens een korte video-call — en geven op basis daarvan een vaste, afgebakende scope."
- *Alarmerend antwoord:* Een vast bedrag noemen puur op basis van jouw mondelinge toelichting, zonder ook maar één blik in de daadwerkelijke code te hebben geworpen.

**2. "Wat is exact inbegrepen — en wat uitdrukkelijk níét?"**
- *Goed antwoord:* Een schriftelijke opsomming van concrete opleverpunten, aangevuld met een expliciete lijst van uitgesloten zaken (zoals nieuwe visuele features of externe licenties).
- *Alarmerend antwoord:* "Alles wat nodig is om live te gaan," zonder enige verdere specificatie.

**3. "Wat gebeurt er met de frontend die ik zelf met AI heb gebouwd?"**
- *Goed antwoord:* "Die behouden we volledig, en we passen hem alleen aan waar iets technisch kapot of aantoonbaar onveilig is."
- *Alarmerend antwoord:* "Die gaan we helemaal opnieuw bouwen op onze eigen framework-stack" — tenzij jij daar zelf om gegronde redenen om hebt gevraagd.

## Over Beveiliging en Kwaliteit

**4. "Hoe waarborgen jullie dat gebruikers uitsluitend hun eigen data kunnen inzien?"**
- *Goed antwoord:* Noemt expliciet afdwinging op server- of databaseniveau (zoals Row-Level Security in PostgreSQL) en geautomatiseerd testen met meerdere accounts.
- *Alarmerend antwoord:* "We voegen een inlogscherm toe," of een antwoord dat zich puur richt op het verbergen van knoppen in de gebruikersinterface.

**5. "Hoe weet de applicatie met 100% zekerheid dat een betaling echt is geslaagd?"**
- *Goed antwoord:* Noemt cryptografisch gevalideerde webhooks rechtstreeks vanuit de betaalprovider (zoals Mollie of Stripe).
- *Alarmerend antwoord:* "Na het afrekenen sturen we de bezoeker door naar een bedankpagina en zetten we de bestelling op betaald."

**6. "Hoe weet ik als klant dat het werk technisch deugdelijk is uitgevoerd?"**
- *Goed antwoord:* Een gedocumenteerde auditlijst bij de start, een hertest-rapport bij oplevering en een begrijpelijke demonstratie — idealiter afgedekt met geautomatiseerde tests die in de code-repository achterblijven.
- *Alarmerend antwoord:* "Vertrouw ons maar, wij doen dit al jaren."

## Over Eigenaarschap en Intellectueel Eigendom

**7. "Op wiens naam en accounts staan de broncode, hosting en database straks geregistreerd?"**
- *Goed antwoord:* "Volledig op jouw naam. We werken direct binnen jouw eigen cloudaccounts of dragen alle eigendomsrechten direct na afronding aan jou over."
- *Alarmerend antwoord:* Hosting of repositories op het eigen bureau-account onderbrengen "omdat dat lekker makkelijk voor je is."

**8. "Kan ik de app na jullie oplevering blijven aanpassen met mijn vertrouwde AI-tool?"**
- *Goed antwoord:* "Jazeker; we documenteren alle wijzigingen helder en houden de code leesbaar en compatibel met tools zoals Lovable, Cursor of Bolt."
- *Alarmerend antwoord:* Aarzeling, of de mededeling dat je voortaan voor elke kleine wijziging van hun uren afhankelijk bent.

## Over Prijs en Doorlooptijd

**9. "Is de geoffreerde prijs een vaste prijs? Wat zou die kunnen verhogen?"**
- *Goed antwoord:* Een vaste aanneemsom voor een nauwkeurig omschreven scope, waarbij eventuele extra wensen altijd als een afzonderlijke, vooraf goedgekeurde meerwerkofferte worden behandeld.
- *Alarmerend antwoord:* Een vage urenschatting voor ongedefinieerd werk, of een vaste prijs met een vage scope die uitnodigt tot onverwachte naheffingen.

**10. "Wanneer starten jullie concreet, en wat is de exacte opleverdatum?"**
- *Goed antwoord:* Harde kalenderdata, gekoppeld aan wat zij concreet van jou nodig hebben om die deadlines te halen.
- *Alarmerend antwoord:* "Zo snel mogelijk," zonder specifieke data of mijlpalen.

## Over de Periode Ná de Livegang

**11. "Wat gebeurt er als er tijdens de eerste dagen na livegang onverhoopt iets omvalt?"**
- *Goed antwoord:* Een contractueel vastgelegde garantieperiode voor nazorg (hypercare), inclusief duidelijke afspraken over bereikbaarheid en escalatie.
- *Alarmerend antwoord:* Nazorg die vanaf de allereerste seconde na de livegang op uurbasis wordt gefactureerd.

**12. "Met welke doorlopende maandelijkse exploitatiekosten moet ik rekening houden?"**
- *Goed antwoord:* Een helder en transparant overzicht — hosting, database, e-mailproviders, transactiekosten per betaling en optioneel beheer — inclusief realistische kostenindicaties.
- *Alarmerend antwoord:* "Dat hangt er helemaal vanaf," zonder ook maar één concreet getal te noemen.

## Hoe Je de Antwoorden Beoordeelt Vóór het Tekenen

Je hoeft van een partij niet op alle twaalf de vragen een perfect geformuleerd schoolvoorbeeld te verwachten. Let vooral op structurele patronen:

- **Specifieke, concrete antwoorden** getuigen van een partij die dit type werk herhaaldelijk heeft uitgevoerd en jouw project echt heeft begrepen.
- **Antwoorden die jou de volledige controle geven** — jouw eigen accounts, jouw code, een vaste prijs — minimaliseren jouw ondernemersrisico.
- **Antwoorden die je zelfstandig kunt verifiëren** — testrapporten, bevindingenlijsten en demonstraties — vervangen blind vertrouwen door tastbaar bewijs.

Als een partij vraag 4 (autorisatie) en vraag 5 (betalingsvalidatie) niet helder en overtuigend kan beantwoorden, zijn zij per definitie niet de juiste partner voor software-hardening, ongeacht wat ze verder beloven.

## Twee Offertes Zij aan Zij Vergelijken

Wanneer je meerdere voorstellen hebt ontvangen, zet je ze naast elkaar in een vergelijkingstabel op basis van deze twaalf vragen. Een praktijkvoorbeeld maakt het onderscheid direct glashelder:

| Vraag | Offerte A (Traditioneel bureau) | Offerte B (Freelancer) | Offerte C (Gespecialiseerd) |
| --- | --- | --- | --- |
| Code vooraf ingezien? | Nee | Vluchtig | Ja, grondig geanalyseerd |
| Scope en uitsluitingen op schrift? | Vage fasering | Losse takenlijst | Concreet plan + uitsluitingen |
| Frontend behouden? | Nee, herbouw | Ja | Ja, 100% behouden |
| Autorisatieverificatie | "Enterprise security" | "Inloggen toevoegen" | RLS-policies + tests |
| Betalingsvalidatie | Niet gespecificeerd | Redirect na betaling | Cryptografische webhooks |
| Bewijs van oplevering | Eindpresentatie | Geen | Hertest-rapport + CI-tests |
| Eigenaarschap accounts | Cloudaccount van bureau | Jouw account | Jouw account |
| Prijsmodel | Vaste prijs per fase | Urenschatting | Vaste projectprijs |
| Doorlooptijd | 4 maanden | "2 tot 4 weken" | 12 werkdagen |
| Nazorg na livegang | Maandelijkse retainer | Uurtarief | 48 uur hypercare inbegrepen |

De goedkoopste offerte leidt zelden tot de laagste totale kosten, en het duurste voorstel is allerminst automatisch het meest zorgvuldig. De tabel toont feitelijk aan wat je voor jouw geld krijgt.

## Hoe Professionele Dienstverleners Horen te Reageren

Goede ontwikkelaars verwelkomen deze kritische vragen van harte. Let niet alleen op wát ze antwoorden, maar ook op hóé ze reageren: stellen ze inhoudelijke vervolgvragen over jouw software en doelgroep? Noemen ze concrete voorbeelden uit vergelijkbare afgeronde trajecten? Durven ze openlijk onzekerheden te benoemen ("pas na de diepere analyse weten we of jouw betaalstroom een aanpassing vereist")? Leggen ze hun toezeggingen direct schriftelijk vast? Een partij die defensief, geïrriteerd of ontwijkend reageert wanneer je vraagt hoe zij de beveiliging gaan valideren, laat precies zien hoe zij zich zullen opstellen zodra er tijdens het project een probleem ontstaat.

## Rode Vlaggen in Offertes

Wees op je hoede bij de volgende verdachte patronen:

- **"Security hardening" als één regeltje** zonder enige specificatie van de werkzaamheden.
- **Geen enkele expliciete uitsluiting**, wat vrijwel altijd leidt tot latere conflicten over meerwerk.
- **Hosting op het cloudaccount van de leverancier** zonder een contractueel vastgelegd overdrachtsprotocol.
- **Een open urenfacturatie** voor een project waarvan de scope niet vooraf is afgebakend.
- **Een vage planning zonder harde kalenderdata** of toetsbare tussenopleveringen.
- **Volledige betaling vooraf (100%)** voor een project van meerdere weken.
- **Geen enkele vermelding van geautomatiseerd testen** buiten "we kijken of het werkt."

Geen van deze punten diskwalificeert een partij automatisch, maar elk punt vereist opheldering vóórdat je ook maar één handtekening zet.

## Mijlpalen en Betalingsvoorwaarden

Bij projecten met een vaste prijs koppelen gezonde betalingsvoorwaarden de termijnen aan tastbare mijlpalen: bijvoorbeeld een aanbetaling bij aanvang, een deelbetaling zodra de architectuurverbeteringen zijn opgeleverd op een staging-omgeving, en het restant pas na formele oplevering en acceptatie. De acceptatie moet gebaseerd zijn op vooraf overeengekomen criteria — zoals het slagen van de hertest en jouw eigen functionele goedkeuring op staging. Dit zorgt voor gelijke belangen en geeft jou houvast.

## Wat Je Vooraf Klaarzet Vóór Je Offertes Opvraagt

Een ontwikkelaar kan een veel scherpere en betrouwbaardere offerte afgeven wanneer je goed voorbereid aan tafel verschijnt. Handige input: een link naar het prototype met leestoegang tot de repository; een korte toelichting op gebruikersrollen en kernstromen; een lijst van gebruikte API-koppelingen; hoe betalingen verlopen; welke persoonsgegevens je verwerkt; je gewenste lanceerdatum; en de resultaten van checks die je zelf al hebt gedaan (zoals de twee-accountstest). Hiermee verandert een intakegesprek direct in een constructieve werksessie en worden offertes echt vergelijkbaar.

## Na de Handtekening

Het ondertekenen is de start van een intensieve samenwerking. Maak direct heldere afspraken over de communicatiecadans (bijvoorbeeld een dagelijkse beknopte statusupdate en een wekelijkse call), wijs aan beide zijden één vast aanspreekpunt aan, leg vast hoe besluiten worden genotuleerd en hoe eventueel gewenst meerwerk wordt aangevraagd en gecalculeerd. Bewaar alle documenten — offerte, auditrapport, wijzigingsverzoeken en testverslagen — overzichtelijk in één gezamenlijke map. Mocht er ooit een meningsverschil ontstaan, dan lost een helder dossier dit binnen enkele minuten op.

## Wanneer Je Moet Bedanken en Weglopen

Soms is de allerbeste zakelijke beslissing simpelweg om niet te tekenen — of een haperend project direct stop te zetten. Redenen om af te zien van samenwerking: het missen van de allereerste deadline zonder plausibele verklaring, weigeren om de scope schriftelijk vast te leggen, vasthouden aan eigenaarschap over jouw code of accounts, of het onvermogen om technische keuzes in begrijpelijke mensentaal uit te leggen. Vroegtijdig afscheid nemen is bijna altijd vele malen goedkoper dan doormodderen in een verkeerde samenwerking.

## Aanvullende Vragen voor Specifieke Situaties

De twaalf hoofdvragen zijn algemeen toepasbaar. Voeg gerust enkele gerichte vragen toe die aansluiten op jouw specifieke product:

- **Bij medische, financiële of kindergegevens:** "Welke aanvullende encryptie passen jullie toe op deze data, en hoe wordt toegang gelogd?"
- **Bij zakelijke (B2B) klanten:** "Leveren jullie technische documentatie op die we direct kunnen overhandigen aan de security- of privacy-officer van onze klant?"
- **Bij AI-features:** "Hoe begrenzen jullie de API-kosten van LLM-tokens en hoe beveiligen jullie de app tegen prompt-injectie?"
- **Bij mobiele apps:** "Wie verzorgt de indiening bij Apple en Google en zorgt voor de verplichte account-verwijderfunctie?"
- **Bij internationale verkoop:** "Hoe richten jullie de btw-berekening (OSS), meertaligheid en lokale betaalmethoden in?"

Dergelijke specifieke vragen tonen direct aan of een partij daadwerkelijke ervaring heeft met jouw type software — of dat zij op jouw kosten moeten gaan pionieren.

## Begrijpen Wat Níét Onder een Vaste Prijs Valt

Een vaste prijs dekt een nauwkeurig gespecificeerde scope; het dekt uiteraard niet alles wat er hypothetisch kan gebeuren. Gebruikelijke uitsluitingen zijn: compleet nieuwe functionele wensen, visuele herontwerpen, licentiekosten van externe diensten (zoals servers of e-mailproviders), vertragingen ontstaan door het niet tijdig aanleveren van inloggegevens door de opdrachtgever, en formeel juridisch advies. Door deze scheidslijn vooraf te begrijpen, voorkom je teleurstellingen en kun je realistisch budgetteren voor de zaken die je zelf verzorgt.

## Referenties Checken Die Écht Inzicht Geven

Vraag een potentiële partij om één of twee referenties van vergelijkbare afgeronde projecten. Stel bij het nabellen praktische en directe vragen: Werd het afgesproken budget gerespecteerd? Werden onvoorziene knelpunten tijdig gecommuniceerd? Was de overgedragen documentatie helder genoeg om zelfstandig verder te kunnen? Zouden ze deze partij direct opnieuw inhuren voor bedrijfskritische productie-afronding? Een kort, openhartig telefoongesprek van vijf minuten met een collega-ondernemer levert oneindig veel meer waardevolle inzichten op dan een gelikte portfoliopagina.

## De Ultieme Toets Vóór Je Tekent

Vraag de ontwikkelaar of het bureau vlak voor ondertekening om in hun eigen woorden samen te vatten: wat doet jouw software precies, wie zijn de gebruikers en wat zijn de drie grootste technische risico's? Als hun samenvatting naadloos aansluit op jouw visie en de benoemde risico's specifiek zijn voor jouw applicatie, weet je dat er echt naar je is geluisterd. Klinkt het als een generiek verkooppraatje, zoek dan rustig verder.

## De Werkelijke Waarde van Deze Vragen

Deze twaalf vragen zijn niet bedoeld om ontwikkelaars klem te zetten. Ze zijn bedoeld om een complexe en onbekende technische aankoop te transformeren naar een rationele en transparante vergelijking. Zodra je scope, verificatiemethoden, eigenaarschap en tarieven objectief naast elkaar kunt leggen, wordt de juiste partnerkeuze voor jouw AI-prototype volkomen vanzelfsprekend — en weet de partij die je selecteert vanaf dag één dat je stuurt op feiten, transparantie en meetbare kwaliteit.

## Hoe LaunchStudio Deze Vragen Beantwoordt

Om de daad bij het woord te voegen, geven we hier direct onze eigen concrete antwoorden. Wij inspecteren jouw broncode altijd tijdens of direct na een vrijblijvende kennismakingscall van 15 minuten alvorens een offerte uit te brengen. De scope en uitsluitingen worden vastgelegd in een transparant fixed-price voorstel tussen € 800 en € 7.500. Jouw zelfgebouwde frontend blijft 100% behouden. Toegangscontrole wordt direct in de database afgedwongen en getest met meerdere gescheiden testaccounts; betalingen worden gevalideerd via cryptografisch geverifieerde webhooks. Je ontvangt een auditrapport vooraf en een hertest-rapport bij oplevering. Alles draait op jouw eigen cloudaccounts, helder gedocumenteerd en direct door te ontwikkelen met jouw favoriete AI-tools. Ons Launch Ready-pakket bevat 48 uur intensieve hypercare na livegang; managed hosting voor € 49 per maand is een optionele keuze. Bekijk alle details op onze [pakkettenpagina](https://launchstudio.eu/nl/#packages).

Achter deze garanties staat Manifera, een gerenommeerd softwareontwikkelingsbedrijf met ruim 11 jaar ervaring, meer dan 160 succesvol opgeleverde maatwerkprojecten en ruim 120 senior engineers verspreid over Amsterdam (Herengracht 420), Singapore en Ho Chi Minh City. Bekijk [het portfolio van Manifera](https://www.manifera.com/portfolio/). Om de registratie van een leverancier te controleren, is het officiële [KVK-handelsregister](https://www.kvk.nl/) een betrouwbare bron.

[Plan direct een gratis kennismakingsgesprek van 15 minuten](https://launchstudio.eu/nl/#contact) — en stel ons gerust alle twaalf de vragen.

## Praktijkvoorbeeld

### Een AI-Native Oprichter in Actie: De Eigenares van een Yogastudio en Twee Totaal Verschillende Offertes

Esther van Leeuwen, eigenares van een yogastudio in Zeist, bouwde Yogarooster in Lovable: een reserveringsplatform waarmee yogi's rittenkaarten aanschaffen, lessen boeken, zich op de wachtlijst plaatsen en geautomatiseerde herinneringen ontvangen. Yogadocenten zien realtime wie er aanwezig is. Twee bevriende studio's in Utrecht wilden het systeem eveneens in gebruik nemen. Esther had eerder al € 2.400 betaald aan een lokale freelancer om de app "productieklaar te maken", maar na die klus verdwenen reserveringen nog steeds af en toe spontaan en werden lessen soms niet van rittenkaarten afgeschreven.

Voordat ze opnieuw geld uitgaf, legde ze deze twaalf vragen voor aan twee partijen. De eerste partij vroeg € 4.000 "om de backend af te maken", kon niet uitleggen hoe betalingen waterdicht werden bevestigd en wilde de applicatie op zijn eigen servers draaien. LaunchStudio bekeek tijdens het eerste intakegesprek direct de repository en bracht binnen 24 uur een vaste offerte met een scherp omschreven scope uit.

De code-analyse van LaunchStudio bracht de eerdere fouten direct aan het licht: de freelancer had weliswaar een login gebouwd, maar het saldo van rittenkaarten werd in de browser van de gebruiker verlaagd. Klanten die na het reserveren direct hun browsertabblad sloten, stonden wél op de deelnemerslijst zonder dat hun tegoed werd verminderd. Mollie-betalingen werden puur bevestigd via een browser-redirect. Studenten konden bovendien via eenvoudige API-aanroepen de volledige boekingsgeschiedenis van andere cursisten inzien. Tot overmaat van ramp bleek de hosting te draaien op het persoonlijke Vercel-account van de freelancer. Binnen acht werkdagen verplaatste het team van LaunchStudio het afschrijven van rittenkaarten naar een ondeelbare databasetransactie gekoppeld aan de boeking, werden betalingen gekoppeld aan geverifieerde webhooks, werd autorisatie afgedwongen op accountniveau, werden de hosting en accounts overgedragen naar Esther's eigen bedrijfsnaam en werden staging, monitoring en documentatie ingericht.

**Het resultaat:** Yogarooster sloot beide externe yogastudio's succesvol aan. Niet-afgeschreven lessen en zoekgeraakte reserveringen behoren definitief tot het verleden. Esther hanteert de twaalf vragen sindsdien standaard bij elke technische offerte die ze beoordeelt.

> *"De eerste keer tekende ik een offerte die ik simpelweg niet kon beoordelen. De tweede keer stelde ik gerichte vragen waarvan ik de antwoorden feilloos kon toetsen. Dat heeft me duizenden euro's en een hoop slapeloze nachten bespaard."*
> — **Esther van Leeuwen, Oprichtster, Yogarooster (Zeist)**

**Kosten & Tijdlijn:** € 2.100 (Launch Ready-pakket: rittenkaartlogica, betalingen, autorisatie en accountoverdracht) — succesvol opgeleverd in 8 werkdagen.

## Veelgestelde Vragen

### Wat is de allerbelangrijkste vraag om te stellen voordat je een AI-prototype naar productie brengt?
"Hoe waarborgen jullie dat gebruikers uitsluitend hun eigen data kunnen inzien?" Het antwoord laat direct zien of de partij de meest voorkomende en gevaarlijke architectuurfout in met AI gegenereerde applicaties begrijpt en kan oplossen.

### Moet een offerte voor software-hardening altijd een vaste prijs (fixed-price) hebben?
Voor een afgebakend project na een initiële code-review: ja. Zodra de broncode is geïnspecteerd, zijn de benodigde verbeteringen voorspelbaar genoeg om met een vaste prijs te offreren. Facturatie op uurbasis bij een open einde schuift alle financiële risico's naar jou als opdrachtgever.

### Is het een alarmsignaal als een partij mijn app op hun eigen cloudaccount wil hosten?
Het vormt een aanzienlijk risico op vendor lock-in. De software-repository, cloudhosting, databases en domeinnamen moeten te allen tijde geregistreerd staan op naam van jouw eigen onderneming. Een externe partner kan deze uitstekend namens jou beheren zonder er eigenaar van te zijn.

### Hoe zorgt Manifera ervoor dat haar offertes betrouwbaar en realistisch zijn?
Door de codebase altijd éérst inhoudelijk te auditen vóór het uitbrengen van een offerte, en door te putten uit ruim 11 jaar aan data van meer dan 160 afgeronde projecten. Die rijke ervaring maakt onze vaste prijzen uiterst solide in plaats van een te optimistische gok.

### Kunnen deze twaalf vragen indirect ook de online reputatie van mijn bedrijf beschermen?
Absoluut. Door te kiezen voor een partner die een robuuste, veilige applicatie oplevert, voorkom je pijnlijke beveiligingsincidenten, datalekken en klachten van gefrustreerde gebruikers. Een vlekkeloze reputatie vormt een krachtig signaal voor zowel zoekmachines als AI-gestuurde antwoordsystemen.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Wat is de allerbelangrijkste vraag om te stellen voordat je een AI-prototype naar productie brengt?",
      "acceptedAnswer": { "@type": "Answer", "text": "Hoe de ontwikkelaar waarborgt dat gebruikers uitsluitend hun eigen data kunnen inzien." }
    },
    {
      "@type": "Question",
      "name": "Moet een offerte voor software-hardening altijd een vaste prijs (fixed-price) hebben?",
      "acceptedAnswer": { "@type": "Answer", "text": "Ja voor een afgebakende scope na code-review; uurbasis bij een open einde schuift alle risico naar jou." }
    },
    {
      "@type": "Question",
      "name": "Is het een alarmsignaal als een partij mijn app op hun eigen cloudaccount wil hosten?",
      "acceptedAnswer": { "@type": "Answer", "text": "Het is een serieus risico; hosting, repositories, databases en domeinen horen op jouw naam te staan." }
    },
    {
      "@type": "Question",
      "name": "Hoe zorgt Manifera ervoor dat haar offertes betrouwbaar en realistisch zijn?",
      "acceptedAnswer": { "@type": "Answer", "text": "Door de code eerst te reviewen en te putten uit 11+ jaar en 160+ projecten aan calculatie-ervaring." }
    },
    {
      "@type": "Question",
      "name": "Kunnen deze twaalf vragen indirect ook de online reputatie van mijn bedrijf beschermen?",
      "acceptedAnswer": { "@type": "Answer", "text": "Zeker, doordat storingen en datalekken worden voorkomen, wat leidt tot positieve signalen in zoek- en AI-systemen." }
    }
  ]
}
</script>
