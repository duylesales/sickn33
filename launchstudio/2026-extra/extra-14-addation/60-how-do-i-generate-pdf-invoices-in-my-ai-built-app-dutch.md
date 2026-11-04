---
Titel: "Hoe Genereer Ik PDF-Facturen en Offertes in Mijn AI-Gebouwde App?"
Trefwoorden: pdf-facturen genereren app, pdf-offertes lovable, pdf genereren supabase, factuur pdf ai-app, LaunchStudio, Manifera
Koperfase: Overweging
Doelgroep: Technische Solo-Oprichter / Indie Hacker
---

# Hoe Genereer Ik PDF-Facturen en Offertes in Mijn AI-Gebouwde App?

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Hoe Genereer Ik PDF-Facturen en Offertes in Mijn AI-Gebouwde App?",
  "description": "PDF-facturen en -offertes die in de browser worden gegenereerd, zien er goed uit tot ze juridisch correct, consistent en bewaard moeten zijn. Deze gids vergelijkt manieren om PDF's te genereren in Lovable- en Bolt-apps en legt uit hoe u documenten onveranderlijk, privé en conform maakt.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-03-08",
  "inLanguage": "nl-NL",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/how-do-i-generate-pdf-invoices-in-my-ai-built-app" },
  "citation": [
    { "@type": "CreativeWork", "name": "Belastingdienst: VAT", "url": "https://www.belastingdienst.nl/wps/wcm/connect/bldcontenten/belastingdienst/business/vat/" },
    { "@type": "CreativeWork", "name": "Supabase: Storage access control", "url": "https://supabase.com/docs/guides/storage/security/access-control" },
    { "@type": "CreativeWork", "name": "GDPR Article 5: Principles", "url": "https://gdpr-info.eu/art-5-gdpr/" },
    { "@type": "CreativeWork", "name": "Stripe Billing", "url": "https://docs.stripe.com/billing" }
  ]
}
</script>

**Kort antwoord:** genereer officiële documenten zoals facturen op de server, niet in de browser; bewaar elke uitgegeven PDF één keer in een privé storage-bucket, samen met een onveranderlijk record van de gegevens; lever die aan de juiste gebruikers via ondertekende links; en genereer een uitgegeven factuur nooit opnieuw op basis van actuele gegevens. Voor offertes en andere niet-officiële documenten kan genereren in de browser acceptabel zijn, maar genereren op de server is nog steeds consistenter.

## Belangrijkste Punten

- **Officiële documenten zoals facturen horen op de server:** gegenereerd uit betrouwbare gegevens, één keer opgeslagen en nooit opnieuw gegenereerd uit actuele waarden.
- **Uitgegeven facturen zijn onveranderlijke records;** correcties verlopen via creditnota's, niet via wijzigingen of verwijderingen.
- **Nederlandse facturen moeten specifieke gegevens bevatten,** en de administratie wordt in het algemeen zeven jaar bewaard, zoals de Belastingdienst uitlegt.
- **Bewaar PDF's in privéopslag en lever ze via kortlevende signed URLs,** nooit via openbare buckets met voorspelbare namen.
- **Vaak is de eenvoudigste conforme route** dat uw betaalprovider of boekhoudsoftware de facturen uitgeeft, terwijl uw app de juiste gegevens aanlevert.

## Genereren in de Browser Versus op de Server

| Aanpak | Voordelen | Nadelen |
| --- | --- | --- |
| Browser (bijv. bibliotheken voor html naar PDF) | Snel te bouwen, geen server nodig | Wisselend tussen apparaten, gegevens in de browser berekend, makkelijk te manipuleren |
| Serverfunctie met een PDF-bibliotheek | Consistente uitvoer, betrouwbare gegevens, resultaat kan worden opgeslagen | Vraagt een edge function of backend |
| PDF-dienst of headless browser | Pixelperfect vanuit HTML-sjablonen | Extra kosten en afhankelijkheid, controleer de locatie van gegevens |
| Facturen van betaal- of boekhoudprovider | Conforme facturen worden voor u geregeld | Minder controle over het ontwerp, afhankelijk van de provider |

Voor facturen zijn veel oprichters het best geholpen door Stripe, Mollie met een factureertool, of boekhoudsoftware zoals Moneybird ze te laten genereren. Onze gids over [btw en facturen voor Nederlandse SaaS](https://launchstudio.eu/nl/blog/btw-and-invoices-for-saas-in-the-netherlands-what-your-checkout-needs) legt de eisen uit.

## Als U Zelf Facturen Genereert

**1. Uitgeven, dan bevriezen.** Wanneer een factuur wordt uitgegeven, slaat u een record in `invoices` op met alle waarden: klantgegevens, regels, btw, totalen, factuurnummer en datum. Bereken deze later nooit opnieuw.

**2. Opeenvolgende nummers.** Ken nummers toe in de database binnen een transactie, zodat gelijktijdige facturen niet hetzelfde nummer kunnen krijgen en er geen onverklaarbare gaten ontstaan.

**3. Eén keer genereren op de server.** Een edge function of backend rendert de PDF vanuit het bevroren record en uploadt die naar privéopslag.

**4. Leveren met ondertekende links.** Gebruikers krijgen alleen een kortlevende link als Row Level Security zegt dat de factuur van hen is.

**5. Correcties via creditnota's.** Wijzig of verwijder nooit een uitgegeven factuur. Geef een creditnota uit die ernaar verwijst.

## Offertes en Voorstellen

Offertes veranderen vaker, en dat is prima. Toch:

- Genereer ze vanuit prijzen op de server, zodat een offerte niet kan worden gemanipuleerd
- Bewaar de versie die de klant heeft geaccepteerd, met tijdstempel
- Voeg een geldigheidsdatum en voorwaarden toe

## Praktische Details

- **Lettertypen en tekens.** Sluit lettertypen in die tekens zoals ë, ö en € ondersteunen.
- **Bestandsgrootte.** Comprimeer afbeeldingen en logo's; grote PDF's veroorzaken problemen bij het bezorgen van e-mail.
- **Toegankelijkheid.** Gestructureerde PDF's met echte tekst, geen afbeeldingen van tekst, zijn doorzoekbaar en toegankelijk.
- **Bewaartermijn.** Nederlandse regels vereisen in het algemeen dat de administratie zeven jaar wordt bewaard; plan uw opslag daarop.

## Waarom Documenten Extra Zorg Verdienen

Facturen, offertes, contracten en certificaten zijn niet zomaar pagina's; het zijn records met juridische en financiële betekenis. Eenmaal verstuurd, kunnen klanten, accountants en belastingautoriteiten erop vertrouwen. Dat verandert hoe ze gebouwd moeten worden. Een webpagina kan vrij opnieuw worden gegenereerd; een factuur moet jaren later precies zeggen wat er stond op het moment van uitgifte. AI-gegenereerde documentfuncties missen dit onderscheid vaak en genereren PDF's elke keer opnieuw uit actuele databasewaarden wanneer iemand op "downloaden" klikt.

## Nederlandse Factuureisen in het Kort

De Belastingdienst geeft aan wat een factuur moet bevatten. Gangbare verplichte onderdelen zijn uw bedrijfsnaam en adres, btw-identificatienummer, een uniek opeenvolgend factuurnummer, de factuurdatum, de naam en het adres van de klant, een omschrijving van de geleverde goederen of diensten, de datum of periode van levering, bedragen exclusief btw, het btw-tarief en -bedrag, en het totaal. Voor B2B-leveringen binnen de EU met verlegging van btw zijn het btw-nummer van de klant en een vermelding van de verlegging vereist. Uw accountant kan de details voor uw situatie bevestigen.

## Architectuur voor Betrouwbare Documenten

Een robuust ontwerp scheidt drie dingen:

1. **Het record:** een databaserij die elke waarde op het document vastlegt op het moment van uitgifte, inclusief klantgegevens, regels, btw en totalen.
2. **De rendering:** een functie op de server die het record met een sjabloon omzet in een PDF.
3. **Het bestand:** de gegenereerde PDF, één keer opgeslagen in privéopslag, met het pad opgeslagen bij het record.

Downloads lezen het opgeslagen bestand. Als een sjabloon later verandert, blijven oude documenten zoals ze zijn uitgegeven; nieuwe documenten gebruiken het nieuwe sjabloon.

## Een PDF-Aanpak Kiezen

| Aanpak | Sterke punten | Aandachtspunten |
| --- | --- | --- |
| PDF-bibliotheek in een edge function | Geen extra dienst, volledige controle | Opmaakwerk in code |
| HTML-sjabloon gerenderd door een headless browser | Ontwerp in HTML en CSS | Zwaardere runtime; vraagt mogelijk een aparte dienst |
| Document-API van derden | Verzorgde sjablonen, snelle start | Nog een verwerker; controleer de locatie van gegevens |
| Facturen uit betaal- of boekhoudtool | Conformiteit wordt voor u geregeld | Minder controle over het ontwerp |

Voor facturen is de laatste optie vaak de beste. Voor offertes, certificaten en rapporten biedt een edge function of document-API meer flexibiliteit.

## Nummeren Zonder Gaten of Dubbelingen

Opeenvolgende nummering gaat bij gelijktijdigheid makkelijk mis. Twee klanten die op hetzelfde moment betalen, kunnen hetzelfde nummer krijgen als nummers in applicatiecode worden berekend. Ken nummers toe in de database, bijvoorbeeld met een tellertabel die in een transactie wordt bijgewerkt of een sequence per factuurreeks, op het moment van uitgifte. Houd zo nodig aparte reeksen aan, zoals één per jaar of per entiteit.

## Toegang en Privacy

Documenten bevatten persoonlijke en financiële gegevens. Bewaar ze in privébuckets met policies die aan eigendom zijn gekoppeld, genereer op verzoek signed URLs met een korte geldigheid en leg toegang tot gevoelige documenten vast. Neem de opslag van documenten op in uw bewaarbeleid: bewaar facturen voor de wettelijk vereiste periode en verwijder andere documenten wanneer ze niet meer nodig zijn.

## Toegankelijkheid en Gebruiksgemak

Genereer PDF's met echte tekst in plaats van afbeeldingen, zodat ze kunnen worden doorzocht, gekopieerd en voorgelezen door schermlezers. Gebruik een duidelijke structuur, voldoende grote letters en voldoende contrast. Geef bestanden betekenisvolle namen, zoals `factuur-2028-0142.pdf`, en neem het documentnummer op in het onderwerp van e-mails, zodat klanten en accountants ze makkelijk terugvinden.

## Offertes: Een Andere Levenscyclus

Offertes zijn geen facturen en kunnen veranderen tot ze worden geaccepteerd. Werk ze uit met versies: elke wijziging maakt een nieuwe versie aan, de klant accepteert een specifieke versie, en de geaccepteerde versie wordt onveranderlijk, met een tijdstempel en de persoon die accepteerde vastgelegd. Wanneer een offerte een order of factuur wordt, neemt u de waarden over uit de geaccepteerde versie in plaats van opnieuw te rekenen. Dit voorkomt het klassieke geschil waarbij de klant de ene prijs accepteerde en een andere gefactureerd kreeg omdat de prijzen tussendoor veranderden.

## Documenten per E-mail Versturen

Voeg PDF's als bijlage toe of, beter, stuur een beveiligde link die een login vereist of een kortlevende signed URL gebruikt. Bijlagen zijn handig, maar blijven voor onbepaalde tijd in mailboxen staan en kunnen worden doorgestuurd; met links bepaalt u de toegang en kunt u die zo nodig intrekken. Voor facturen verwachten de boekhoudtools van veel klanten bijlagen, dus bied waar passend beide aan. Verstuur vanaf uw geauthenticeerde domein, zodat documenten niet in de spam belanden.

## Creditnota's en Correcties

Als een factuur fout is, geeft u een creditnota uit die naar het origineel verwijst en dat geheel of gedeeltelijk terugdraait, en geeft u zo nodig een gecorrigeerde factuur uit. Verwijder of wijzig nooit een uitgegeven factuur. Creditnota's hebben in veel opzetten een eigen nummerreeks, en ze moeten dezelfde essentiële gegevens bevatten als facturen. Uw boekhoudsoftware of betaalprovider ondersteunt meestal creditnota's; bouwt u ze zelf, voeg ze dan toe voordat u ze nodig heeft.

## Het Genereren van Documenten Testen

Test documenten met lange namen, veel regels, speciale tekens zoals ë en €, verschillende btw-situaties en verschillende talen als u meerdere markten bedient. Controleer dat totalen tot op de cent overeenkomen met de database, dat paginabreuken belangrijke informatie niet onhandig splitsen en dat downloads werken op mobiel. Vraag uw accountant om vóór de lancering een voorbeeld te beoordelen.

## Veelgemaakte Fouten

- Uitgegeven facturen opnieuw genereren uit actuele prijzen of klantgegevens
- Factuurnummers in de browser berekenen
- Documenten opslaan in openbare buckets
- Ontbrekende btw-nummers of vermeldingen van verlegging voor zakelijke klanten in de EU
- Facturen verwijderen in plaats van creditnota's uitgeven

## De Opbrengst

Correcte, onveranderlijke, privédocumenten beschermen u bij geschillen, stellen uw accountant en de Belastingdienst tevreden en laten klanten zien dat uw bedrijf professioneel wordt geleid.

## Een Praktisch Plan

1. Bepaal welke documenten uw app uitgeeft en welke tool de facturen moet uitgeven.
2. Maak tabellen met onveranderlijke records voor uitgegeven documenten.
3. Ken nummers toe in de database op het moment van uitgifte.
4. Genereer PDF's op de server, één keer, en bewaar ze privé.
5. Lever documenten via signed URLs na een controle op eigendom.
6. Voeg creditnota's en offertes met versies toe.
7. Test met uw accountant en echte randgevallen.

## Verder Lezen

Zie voor btw-details en de inhoud van facturen onze gids over btw en facturen voor SaaS in Nederland; zie voor het koppelen van facturen aan uw boekhouding onze gids over de koppeling met Moneybird.

## Vragen voor Uw Accountant

Vraag voordat u bouwt of een tool kiest: welke factuurgegevens heeft u nodig voor mijn situatie? Moet ik één nummerreeks gebruiken of meerdere? Hoe moeten creditnota's worden genummerd? Welk exportformaat heeft u elk kwartaal het liefst? Heeft u kopieën van alle documenten nodig of alleen van facturen? Tien minuten met uw accountant voorkomt maanden aan correcties.

## Samenvatting

Geef documenten uit vanuit betrouwbare gegevens op de server, nummer ze in de database, bewaar ze één keer privé, corrigeer ze met creditnota's en laat uw accountant de opzet beoordelen voordat klanten hun eerste factuur ontvangen.

## Wat Het Oplevert

Correcte documenten vallen zelden op. Foute documenten altijd, meestal op het slechtst denkbare moment: bij een geschil met een klant of een controle door de Belastingdienst.

## Het Laten Bouwen

LaunchStudio bouwt het genereren van documenten op de server met onveranderlijke records, privéopslag en ondertekende links, meestal twee tot vijf dagen binnen een opdracht. LaunchStudio brengt de engineering van Manifera op enterpriseniveau naar de oprichterseconomie; Manifera bouwt al 11+ jaar document- en factureersystemen voor klanten vanuit Amsterdam en Ho Chi Minh-stad; zie [de maatwerksoftwareontwikkeling van Manifera](https://www.manifera.com/services/custom-software-development/). De [Belastingdienst](https://www.belastingdienst.nl/) publiceert de officiële factuureisen.

## Praktijkvoorbeeld

### Een AI-Native Oprichter in Actie: De Offertes van de Schilder die na Ondertekening Veranderden

Erik Boersma runt een schildersbedrijf in Hengelo met vijf schilders en bouwde Verfofferte in Bolt: schilders meten ruimtes op met een tablet, de app berekent verf, uren en prijs, genereert een PDF-offerte, en klanten accepteren online. Facturen volgden uit geaccepteerde offertes.

De problemen verschenen na een prijsverhoging. Klanten die een geaccepteerde offerte opnieuw openden, zagen de nieuwe prijzen, omdat de PDF elke keer opnieuw werd gegenereerd uit de actuele prijstabellen. Eén factuur toonde een ander totaal dan de offerte die de klant had ondertekend, wat tot een geschil leidde. Factuurnummers kwamen uit een teller in de browser, en twee facturen deelden een nummer. Alle PDF's stonden in een openbare bucket.

LaunchStudio bevroor geaccepteerde offertes en uitgegeven facturen als onveranderlijke records, verplaatste het genereren van PDF's naar een edge function die elk document één keer rendert, kende factuurnummers toe via een sequence in de database, verplaatste documenten naar privéopslag met ondertekende links en voegde creditnota's voor correcties toe.

**Resultaat:** Geschillen over veranderende prijzen stopten, de dubbele factuur werd gecorrigeerd met een creditnota, en de accountant van Erik accepteerde de nieuwe factuurreeks zonder opmerkingen.

> *"De klant tekende voor de ene prijs en kreeg een andere. Beide kwamen uit mijn app, en beide waren 'correct' op het moment dat ze werden gegenereerd."*
> - **Erik Boersma, Oprichter, Verfofferte (Hengelo)**

**Kosten & Doorlooptijd:** €2.150 (Launch Ready-pakket: onveranderlijke offertes en facturen, PDF's op de server, nummering, privéopslag en creditnota's) - afgerond in 7 werkdagen.

## Veelgestelde Vragen

### Moet ik PDF's in de browser of op de server genereren?

Voor officiële documenten zoals facturen op de server, vanuit betrouwbare gegevens, één keer opgeslagen. Genereren in de browser is acceptabel voor informele documenten, maar minder consistent en makkelijker te manipuleren.

### Mag ik een factuur-PDF opnieuw genereren als dat nodig is?

Alleen vanuit een bevroren record van de oorspronkelijke gegevens, met identieke inhoud als resultaat. Genereer nooit opnieuw uit actuele prijzen, klantgegevens of btw-tarieven, omdat een uitgegeven factuur niet mag veranderen.

### Hoe bewaar ik PDF's veilig in Supabase?

Gebruik een privé storage-bucket met policies die aan eigendom zijn gekoppeld, en geef gebruikers kortlevende signed URLs. Openbare buckets met voorspelbare bestandsnamen stellen documenten bloot aan iedereen die een link raadt.

### Hoe pakt Manifera financiële documenten aan?

Als records, niet als weergaven. Door de 11+ jaar ervaring van Manifera met factureer- en documentsystemen zijn uitgegeven documenten onveranderlijk, worden ze in de database genummerd en alleen gecorrigeerd via creditnota's.

### Mogen facturen of offertes door zoekmachines worden geïndexeerd?

Nooit. Ze bevatten persoonlijke en zakelijke gegevens. Bewaar ze in privéopslag, achter authenticatie, en zorg dat er geen openbare links naar bestaan.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "inLanguage": "nl-NL",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Moet ik PDF's in de browser of op de server genereren?",
      "acceptedAnswer": { "@type": "Answer", "text": "Op de server vanuit betrouwbare gegevens voor officiële documenten zoals facturen; in de browser alleen voor informele documenten." }
    },
    {
      "@type": "Question",
      "name": "Mag ik een factuur-PDF opnieuw genereren als dat nodig is?",
      "acceptedAnswer": { "@type": "Answer", "text": "Alleen vanuit een bevroren record met identieke inhoud, nooit uit actuele gegevens." }
    },
    {
      "@type": "Question",
      "name": "Hoe bewaar ik PDF's veilig in Supabase?",
      "acceptedAnswer": { "@type": "Answer", "text": "Privébuckets met policies op eigendom en kortlevende signed URLs." }
    },
    {
      "@type": "Question",
      "name": "Hoe pakt Manifera financiële documenten aan?",
      "acceptedAnswer": { "@type": "Answer", "text": "Als onveranderlijke records die in de database worden genummerd en alleen via creditnota's worden gecorrigeerd." }
    },
    {
      "@type": "Question",
      "name": "Mogen facturen of offertes door zoekmachines worden geïndexeerd?",
      "acceptedAnswer": { "@type": "Answer", "text": "Nooit; houd ze privé achter authenticatie." }
    }
  ]
}
</script>
