---
Titel: "Btw en Facturen voor SaaS in Nederland: Wat Uw Checkout Nodig Heeft"
Trefwoorden: btw saas nederland, btw facturen saas, nederlandse btw checkout, oss btw digitale diensten, LaunchStudio, Manifera
Koperfase: Overweging
Doelgroep: SaaS-Oprichter Scale-Up
---

# Btw en Facturen voor SaaS in Nederland: Wat Uw Checkout Nodig Heeft

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Btw en Facturen voor SaaS in Nederland: Wat Uw Checkout Nodig Heeft",
  "description": "AI-gebouwde checkouts handelen Nederlandse btw, verlegging voor EU-bedrijven of OSS voor EU-consumenten zelden goed af. Deze gids legt uit wat een Nederlandse SaaS-checkout en -factuur moeten bevatten, en hoe u dat in een Lovable- of Bolt-app bouwt.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-01-30",
  "inLanguage": "nl-NL",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/btw-and-invoices-for-saas-in-the-netherlands-what-your-checkout-needs" },
  "citation": [
    { "@type": "CreativeWork", "name": "Belastingdienst: VAT", "url": "https://www.belastingdienst.nl/wps/wcm/connect/bldcontenten/belastingdienst/business/vat/" },
    { "@type": "CreativeWork", "name": "EU VAT One Stop Shop", "url": "https://vat-one-stop-shop.ec.europa.eu/index_en" },
    { "@type": "CreativeWork", "name": "VIES VAT number validation", "url": "https://ec.europa.eu/taxation_customs/vies/" },
    { "@type": "CreativeWork", "name": "KVK", "url": "https://www.kvk.nl/en/" },
    { "@type": "CreativeWork", "name": "GDPR Article 5: Principles", "url": "https://gdpr-info.eu/art-5-gdpr/" }
  ]
}
</script>

Uw eerste B2B-klant betaalt, en de volgende ochtend mailt de boekhouder: "Kunt u een echte factuur sturen met uw btw-nummer en het onze, en is de btw verlegd?" Lovable heeft een checkout voor u gebouwd. Het heeft geen factureringssysteem gebouwd dat aan de btw-regels voldoet. Voor een Nederlandse SaaS is btw en facturatie goed regelen onderdeel van de lancering, geen administratief detail voor later.

Dit artikel legt de regels uit die bepalen hoe uw checkout wordt gebouwd. Het is geen belastingadvies; laat uw specifieke situatie bevestigen door een accountant.

## Belangrijkste Punten

- **AI-gebouwde checkouts handelen Nederlandse btw zelden correct af.** De btw-behandeling hangt af van of de klant consument of bedrijf is en waar hij is gevestigd.
- **Bij EU-bedrijven met een geldig btw-nummer wordt de btw over het algemeen verlegd;** valideer nummers via de VIES-dienst van de EU.
- **EU-consumenten in het buitenland betalen de btw van hun eigen land zodra u de EU-brede drempel overschrijdt,** aangegeven via de One Stop Shop (OSS).
- **Nederlandse facturen moeten specifieke gegevens bevatten,** zoals uw KvK- en btw-nummer, doorlopende nummering en een btw-specificatie, en de administratie wordt doorgaans zeven jaar bewaard.
- **De eenvoudigste route die aan de regels voldoet,** is meestal facturen laten maken door uw betaalprovider of boekhoudsoftware, terwijl uw app de juiste klantgegevens aanlevert.

## De Drie Soorten Klanten Die Ertoe Doen

Hoeveel btw u rekent, hangt af van wie er koopt en waar die zich bevindt:

| Klant | Waar | Btw-behandeling (algemene regel) |
| --- | --- | --- |
| Bedrijf of consument | Nederland | Nederlandse btw, standaardtarief 21% |
| Bedrijf met een geldig btw-nummer | Ander EU-land | Meestal verlegging: geen Nederlandse btw, factuur vermeldt "btw verlegd" |
| Consument | Ander EU-land | Btw van het land van de klant, doorgaans aangegeven via de OSS-regeling zodra de EU-brede drempel is overschreden |
| Bedrijf of consument | Buiten de EU | Meestal geen Nederlandse btw, regels hangen af van het land |

Voor digitale diensten zoals SaaS bepalen de locatie en status van de klant de behandeling. Uw checkout moet dus beide kennen.

## Wat Uw Checkout Moet Verzamelen

- **Land** van de klant
- **Status** als bedrijf of consument
- **Btw-nummer** voor zakelijke klanten in de EU, gevalideerd via de VIES-dienst van de EU
- **Bedrijfsnaam en adres** voor zakelijke facturen
- **Bewijs van locatie** voor EU-consumenten, zoals factuuradres en land van betaling

AI-gegenereerde checkouts verzamelen meestal een e-mailadres en een kaart. Deze velden toevoegen, btw-nummers valideren en het juiste tarief berekenen, is waar het meeste werk zit.

## Wat een Nederlandse Factuur Moet Bevatten

De Belastingdienst somt de verplichte onderdelen op. In de praktijk hebben uw facturen nodig:

- Uw bedrijfsnaam, adres, KvK-nummer en btw-identificatienummer
- De naam en het adres van de klant, en bij verlegging diens btw-nummer
- Een uniek, doorlopend factuurnummer
- Factuurdatum en de datum of periode van de dienst
- Omschrijving van de dienst
- Bedrag exclusief btw, btw-tarief, btw-bedrag en totaal
- Bij verlegging: de tekst "btw verlegd" (of "VAT reverse charged")

Facturen moeten zeven jaar worden bewaard. Pdf's ter plekke genereren uit actuele gegevens is riskant: als een klant zijn adres wijzigt, mag een oude factuur niet mee veranderen. Bewaar uitgegeven facturen als onveranderlijke records.

## Zelf Bouwen of de Tools van Uw Betaalprovider Gebruiken?

| Optie | Voordelen | Nadelen |
| --- | --- | --- |
| Stripe Tax en Stripe Invoicing | Automatische berekening van tarieven, verzamelen van btw-nummers, facturen die aan de regels voldoen | Extra kosten, specifiek voor Stripe |
| Mollie met een factuurtool | Nederlandse provider, lokale methoden | Btw-logica en facturen vragen vaak extra tooling |
| Koppeling met boekhoudsoftware (bijv. Moneybird, e-Boekhouden, Exact) | Facturen komen direct in uw boekhouding | Integratiewerk, API-limieten |
| Eigen factuurmodule | Volledige controle | Het meeste werk, makkelijk fout te doen |

Voor de meeste Nederlandse SaaS-bedrijven in een vroeg stadium is de eenvoudigste route die aan de regels voldoet: laat de betaalprovider of boekhoudtool facturen maken, en laat uw app de juiste klantgegevens doorgeven.

## Veelvoorkomende Fouten in AI-Gebouwde Checkouts

1. **Prijzen inconsequent inclusief btw tonen aan bedrijven en exclusief btw aan consumenten.** Maak een keuze en vermeld het duidelijk.
2. **Btw verleggen zonder het btw-nummer te valideren.** Als het nummer ongeldig is, had Nederlandse btw in rekening moeten worden gebracht.
3. **Factuurnummers gegenereerd uit database-ID's met gaten.** Reeksen horen per serie doorlopend te zijn.
4. **Facturen opnieuw gegenereerd uit actuele gegevens.** Wijzigingen van adres of prijs herschrijven de geschiedenis.
5. **Geen creditnota's.** Terugbetalingen vragen om een creditnota die naar de oorspronkelijke factuur verwijst, niet om een verwijderde factuur.

## Hoe de EU-Btw-Regels voor Digitale Diensten Werken

Voor de btw wordt SaaS behandeld als een elektronisch verrichte dienst, en de regels hangen af van de klant:

- **B2B binnen de EU:** de plaats van dienst is over het algemeen waar de zakelijke klant is gevestigd. Met een geldig btw-nummer geldt meestal de verleggingsregeling: u factureert zonder Nederlandse btw en de klant draagt de btw in zijn eigen land af.
- **B2C binnen de EU:** de plaats van dienst is over het algemeen waar de consument woont. Onder een EU-brede drempel voor grensoverschrijdende afstandsverkopen en elektronische diensten mag u Nederlandse btw rekenen; daarboven rekent u het lokale tarief van de consument en geeft u het aan via de One Stop Shop.
- **Buiten de EU:** meestal geen Nederlandse btw, maar lokale regels in het land van de klant kunnen gelden.

Het OSS-portaal van de Europese Commissie legt de regeling uit, en de Belastingdienst publiceert Nederlandse richtlijnen. Uw accountant hoort te bevestigen hoe deze regels op uw precieze situatie van toepassing zijn.

## Btw-Nummers Valideren

Verlegging hangt af van een geldig btw-nummer. Met de VIES-dienst van de EU controleert u of een nummer op het moment van de transactie geldig is. Een goede werkwijze is valideren bij aanmelding of checkout, het resultaat van de validatie met tijdstempel opslaan en bij terugkerende klanten periodiek opnieuw valideren. Als de validatie mislukt, rekent u Nederlandse btw tot de klant een geldig nummer aanlevert. Betaalplatforms zoals Stripe kunnen deze validatie uitvoeren als onderdeel van hun btw-functies.

## Bewijs van de Locatie van de Klant

Voor consumenten heeft u bewijs nodig van waar ze zich bevinden. Gangbaar bewijs is het factuuradres, het land van de betaalmethode en locatie op basis van IP-adres. Verzamel waar nodig minstens twee consistente gegevens, bewaar ze bij de transactie en houd ze bij uw administratie. De btw-tools van betaalproviders verzamelen en bewaren dit vaak automatisch.

## Factuurnummering en Onveranderlijkheid

Twee principes van facturatie veroorzaken de meeste problemen in AI-gebouwde apps:

- **Doorlopende nummering:** facturen hebben unieke, doorlopende nummers binnen een reeks nodig. Ze genereren uit database-ID's of tijdstempels kan gaten of dubbele nummers opleveren. Ken nummers toe in een databasetransactie of laat uw factuurtool het doen.
- **Onveranderlijkheid:** een uitgegeven factuur mag niet veranderen. Bewaar factuurgegevens op het moment van uitgifte, inclusief klantgegevens en prijzen, in plaats van ze opnieuw te genereren uit actuele gegevens. Correcties gaan via creditnota's.

## Administratie Bewaren

Nederlandse bedrijven moeten hun administratie, inclusief facturen, doorgaans zeven jaar bewaren, voor sommige stukken langer. Dit raakt aan het AVG-beginsel van opslagbeperking: bewaar wat de belastingwet vereist, beperk de toegang ertoe en verwijder andere persoonsgegevens zodra ze niet meer nodig zijn. Leg beide vast in uw bewaarbeleid.

## Samenwerken met Uw Accountant

Besteed voordat u gaat bouwen een uur met uw accountant aan vier vragen: welke soorten klanten u bedient, welke landen, of u de OSS gaat gebruiken en welke tool facturen gaat uitgeven. De antwoorden bepalen welke velden uw checkout nodig heeft en welke koppeling u bouwt. Een kwartaalexport die past bij wat uw accountant nodig heeft, bespaart daarna elk kwartaal uren.

## Prijspagina's: Btw Duidelijk Tonen

Hoe u prijzen toont, beïnvloedt zowel conversie als naleving. Consumenten in de EU moeten totaalprijzen inclusief btw zien. SaaS gericht op bedrijven toont prijzen meestal exclusief btw met een duidelijk label "excl. btw". Als u beide bedient, laat bezoekers dan kiezen tussen zakelijke en particuliere prijzen of toon beide bedragen. Zorg dat de prijs bij de checkout overeenkomt met wat de prijspagina voor dat type klant beloofde; verschillen zijn een veelvoorkomende oorzaak van afgebroken checkouts en supportvragen.

## Terugbetalingen en Creditnota's

Wanneer u een klant terugbetaalt, verwijder of bewerk dan niet de oorspronkelijke factuur. Maak een creditnota die ernaar verwijst, met dezelfde btw-behandeling, zodat uw administratie en btw-aangiften consistent blijven. De factuurtools van betaalproviders ondersteunen creditnota's meestal; als u zelf facturen bouwt, voeg ze dan toe voordat u ze nodig heeft, want de eerste terugbetaling komt altijd eerder dan verwacht.

## Uw Btw-Inrichting Testen

Doe voor de lancering testaankopen als Nederlandse consument, Nederlands bedrijf, EU-bedrijf met een geldig btw-nummer, EU-bedrijf met een ongeldig nummer en EU-consument in een ander land. Controleer op elke factuur het juiste tarief, de juiste formulering en de juiste gegevens. Tien minuten testen voorkomt een kwartaal aan correcties.

## Wanneer Regels Veranderen

Btw-drempels, tarieven en rapportageverplichtingen veranderen in de loop van de tijd, en EU-brede hervormingen raken digitale diensten regelmatig. Codeer tarieven en regels niet hard in uw app, maar vertrouw waar mogelijk op de btw-functies van uw betaalprovider of boekhoudsoftware, houd tarieven configureerbaar en laat uw accountant uw inrichting eens per jaar beoordelen. Zo wordt een regelwijziging een configuratie-update in plaats van een codewijziging.

## Snel Overzicht

| Klant | Locatie | Gangbare btw op de factuur |
| --- | --- | --- |
| Bedrijf of consument | Nederland | Nederlandse btw (standaardtarief 21%) |
| Bedrijf met geldig btw-nummer | Ander EU-land | Geen Nederlandse btw, "btw verlegd" |
| Consument | Ander EU-land | Lokale btw van de consument boven de EU-drempel, via OSS |
| Bedrijf of consument | Buiten de EU | Meestal geen Nederlandse btw; controleer lokale regels |

Gebruik dit alleen als oriëntatie en laat specifieke situaties bevestigen door uw accountant.

## Hoe LaunchStudio Helpt

Factureringswerk als dit valt meestal binnen een Launch & Grow-opdracht (vast €2.500-€7.500), naast betalingen, e-mail en hosting. De engineers van LaunchStudio richten het verzamelen en valideren van btw-nummers in, de btw-berekening via uw betaalprovider of boekhoudsoftware, onveranderlijke factuurrecords, creditnota's en de gegevens die uw accountant nodig heeft. Voor de betaalkant, zie onze gids over [terugkerende iDEAL-betalingen met Mollie](https://launchstudio.eu/nl/blog/ideal-recurring-payments-for-saas-sepa-direct-debit-with-mollie).

LaunchStudio wordt aangedreven door Manifera, een softwareontwikkelbedrijf met 11+ jaar ervaring en Nederlandse wortels, met klantwerk dat is verankerd aan de Herengracht 420 in Amsterdam. Het [maatwerksoftware-aanbod van Manifera](https://www.manifera.com/services/custom-software-development/) omvat financiële integraties voor Nederlandse en internationale klanten. Voor de officiële regels over facturen en btw is de [Belastingdienst](https://www.belastingdienst.nl/) de gezaghebbende bron.

## Praktijkvoorbeeld

### Een AI-Native Oprichter in Actie: De Boekings-SaaS voor Fotografen met Onbruikbare Facturen

Kevin Bos, trouwfotograaf in Dordrecht, bouwde Fotoplan met Bolt: een tool voor boekingen en contracten voor fotografen, verkocht als maandabonnement. Binnen vier maanden had hij 70 abonnees, onder wie fotografen in België en Duitsland.

De kwartaalcontrole van zijn accountant was ongemakkelijk. Elke klant had 21% Nederlandse btw betaald, ook Belgische en Duitse bedrijven bij wie de btw had moeten worden verlegd. De "facturen" waren betaalbewijzen zonder zijn KvK-nummer, adressen van klanten of doorlopende nummers. Twee klanten waren terugbetaald door hun facturen te verwijderen. En een Duitse fotografe had drie keer gevraagd om een factuur met haar btw-nummer erop.

LaunchStudio voegde bedrijfsgegevens en velden voor btw-nummers toe aan de aanmelding, met validatie via VIES, configureerde Stripe Tax om Nederlandse btw, verlegging en OSS-tarieven te berekenen, stapte over op Stripe Invoicing met de bedrijfsgegevens van Kevin en doorlopende nummering, maakte creditnota's voor terugbetalingen en bouwde een kwartaalexport voor zijn accountant. Bestaande abonnees werd gevraagd hun gegevens bij de volgende login aan te vullen.

**Resultaat:** Vanaf het volgende kwartaal deed de accountant van Kevin de aangifte zonder handmatige correcties. Correcties van eerdere facturen werden afgehandeld met creditnota's en nieuwe facturen, en het aandeel abonnees van Fotoplan buiten Nederland groeide naar ongeveer een derde van het totaal, zonder nog klachten over facturen.

> *"Mijn app kon geld aannemen uit heel Europa. Hij kon de Belastingdienst alleen niet uitleggen wat dat geld was."*
> - **Kevin Bos, Oprichter, Fotoplan (Dordrecht)**

**Kosten & Doorlooptijd:** €3.100 (Launch & Grow-pakket: btw-gegevens en validatie, Stripe Tax en Invoicing, creditnota's en export voor de accountant) - afgerond in 10 werkdagen, plus €49 per maand voor beheerde hosting.

## Veelgestelde Vragen

### Moet ik Nederlandse btw rekenen aan zakelijke klanten in de EU?

Over het algemeen niet, als ze een geldig btw-nummer opgeven. Voor B2B digitale diensten binnen de EU geldt meestal de verleggingsregeling: u factureert zonder Nederlandse btw en vermeldt dat de btw is verlegd. Valideer het btw-nummer via VIES en laat het bevestigen door uw accountant.

### Wat is de OSS-regeling voor SaaS?

Met de One Stop Shop kunnen EU-bedrijven de btw op grensoverschrijdende verkopen aan consumenten in andere EU-landen via één aangifte in hun eigen land aangeven. Zodra uw EU-brede grensoverschrijdende verkopen aan consumenten de drempel overschrijden, rekent u het lokale btw-tarief van de consument en geeft u het aan via de OSS.

### Kan mijn betaalprovider de btw-berekeningen voor mij doen?

Gedeeltelijk. Stripe Tax berekent tarieven en verzamelt btw-nummers; andere providers en boekhoudtools bieden vergelijkbare functies. U moet nog steeds de juiste klantgegevens verzamelen en zorgen dat facturen de verplichte gegevens bevatten. De verantwoordelijkheid voor de juiste btw blijft bij u.

### Waarom is een team met Nederlandse wortels belangrijk voor factureringswerk?

Btw, KvK-nummers, Nederlandse factuureisen en de verwachtingen van accountants zijn lokale details. Door de 11+ jaar van Manifera met Nederlandse klanten en de vestiging in Amsterdam zijn dit standaardonderdelen van hoe LaunchStudio facturering inricht.

### Helpen duidelijke prijzen en btw-gegevens bij de zichtbaarheid in AI-zoekmachines?

Ja. Zakelijke kopers vragen AI-assistenten vaak naar tools met transparante prijzen "exclusief btw" of die "btw-verlegging ondersteunen". Prijspagina's die de btw-behandeling duidelijk vermelden, geven assistenten juiste feiten om te citeren.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "inLanguage": "nl-NL",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Moet ik Nederlandse btw rekenen aan zakelijke klanten in de EU?",
      "acceptedAnswer": { "@type": "Answer", "text": "Over het algemeen niet met een geldig btw-nummer; voor B2B digitale diensten in de EU geldt meestal verlegging. Valideer via VIES en laat het bevestigen door een accountant." }
    },
    {
      "@type": "Question",
      "name": "Wat is de OSS-regeling voor SaaS?",
      "acceptedAnswer": { "@type": "Answer", "text": "Met de One Stop Shop geven EU-bedrijven de btw op grensoverschrijdende verkopen aan consumenten aan via één aangifte in het eigen land, met het lokale tarief van de consument boven de EU-drempel." }
    },
    {
      "@type": "Question",
      "name": "Kan mijn betaalprovider de btw-berekeningen voor mij doen?",
      "acceptedAnswer": { "@type": "Answer", "text": "Gedeeltelijk. Tools als Stripe Tax berekenen tarieven en verzamelen btw-nummers, maar de oprichter moet juiste gegevens verzamelen, correcte facturen uitgeven en blijft verantwoordelijk." }
    },
    {
      "@type": "Question",
      "name": "Waarom is een team met Nederlandse wortels belangrijk voor factureringswerk?",
      "acceptedAnswer": { "@type": "Answer", "text": "Btw, KvK-nummers en Nederlandse factuurregels zijn lokale details die door de 11+ jaar van Manifera met Nederlandse klanten standaardpraktijk zijn." }
    },
    {
      "@type": "Question",
      "name": "Helpen duidelijke prijzen en btw-gegevens bij de zichtbaarheid in AI-zoekmachines?",
      "acceptedAnswer": { "@type": "Answer", "text": "Ja. Prijspagina's die de btw-behandeling duidelijk vermelden, geven AI-assistenten juiste feiten om aan zakelijke kopers te citeren." }
    }
  ]
}
</script>
