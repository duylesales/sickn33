---
Titel: "Lovable i18n: Een Nederlands en Engels Product in Eén Codebase"
Trefwoorden: lovable i18n, internationalisering, Nederlandse en Engelse app, vertalingen, meertalige SaaS, LaunchStudio, Manifera
Koperfase: Overweging
Doelgroep: AI-Native Oprichter (Niet-technisch)
---

# Lovable i18n: Een Nederlands en Engels Product in Eén Codebase

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Lovable i18n: Een Nederlands en Engels Product in Eén Codebase",
  "description": "De meeste Nederlandse B2B-producten hebben eerder dan gepland een tweede taal nodig. Hoe u Engels toevoegt aan een AI-gebouwde app zonder schermen te dupliceren: de architectuur, waar de taal vandaan komt, opmaak, tekst van de server, de vertaalworkflow en de controles die twee talen gelijk houden.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-03-03",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/lovable-i18n-a-dutch-and-english-product-in-one-codebase" }
}
</script>

Een Nederlands product dat aan Nederlandse klanten wordt verkocht, begint in het Nederlands, en een tijdlang is dat het hele verhaal. Dan neemt een klant een internationaal team aan, vraagt een Belgische prospect om Engels, of wil een bedrijf met expats het proberen, en vraagt de oprichter de bouwtool om "Engels toe te voegen".

Wat er meestal terugkomt, is een van drie dingen: een tweede kopie van elk scherm, Engelse teksten naast Nederlandse geplakt met een conditie om elk, of een vertaaltabel in de database die elk component bevraagt. Elk werkt in een demonstratie. Zes maanden later moet elke wijziging twee keer worden gedaan, zijn de talen uit elkaar gegroeid, en weet niemand meer welke versie juist is.

Internationalisering - i18n, naar de achttien letters tussen de i en de n - is niet moeilijk. Het is een structurele beslissing met een handvol regels, goedkoop bij twintig schermen en duur bij tachtig. Dit artikel behandelt het geheel: de architectuur, waar de taal vandaan komt, de opmaak die niet over woorden gaat, de tekst die uw server maakt, de workflow voor vertalingen, en de controles die twee talen gelijk houden.

## Drie Manieren Waarop Het Misgaat

Het is goed de patronen te benoemen die AI-tools opleveren wanneer ze een taal moeten toevoegen, omdat elk redelijk oogt en elk op een kenmerkende manier faalt.

**Gedupliceerde schermen.** Een `InvoiceList` en een `InvoiceListEn`. Elke bug die in de ene wordt opgelost, moet ook in de andere worden opgelost, en binnen enkele weken verschillen ze in gedrag, niet alleen in woorden. Dit is het duurste patroon, omdat het naast tekst ook logica dupliceert.

**Inline condities.** `{lang === 'nl' ? 'Opslaan' : 'Save'}` verspreid door elk component. Het gedrag blijft gedeeld, maar de tekst van elke taal staat op honderden plekken, niemand kan een taal als geheel nakijken, en een derde taal betekent elke conditie bewerken.

**Vertalingen in de database.** Een tabel `translations` die tijdens het draaien wordt bevraagd. Het voelt flexibel en levert een trage interface op, een netwerkverzoek voor elk label, een leeg scherm wanneer de query faalt, en vertalingen die onzichtbaar zijn in de codereview en ontbreken in versiebeheer.

De werkende aanpak is geen van deze, en ze is al tientallen jaren de standaard in software.

## De Architectuur: Sleutels, Berichtbestanden, Eén Bibliotheek

De interface verwijst naar een sleutel. De woorden staan in één bestand per taal. Een bibliotheek verbindt de twee.

```json
// locales/nl/invoices.json
{
  "list": {
    "title": "Facturen",
    "empty": "Er zijn nog geen facturen.",
    "count": "{count, plural, one {# factuur} other {# facturen}}"
  },
  "actions": { "send": "Versturen", "markPaid": "Markeren als betaald" }
}
```

```json
// locales/en/invoices.json
{
  "list": {
    "title": "Invoices",
    "empty": "There are no invoices yet.",
    "count": "{count, plural, one {# invoice} other {# invoices}}"
  },
  "actions": { "send": "Send", "markPaid": "Mark as paid" }
}
```

```tsx
const { t } = useTranslation('invoices');
<h1>{t('list.title')}</h1>
<p>{t('list.count', { count: invoices.length })}</p>
```

Voor een React-applicatie die door Lovable of Bolt is gegenereerd, zijn de twee volwassen keuzes i18next met react-i18next, en FormatJS met react-intl. Beide ondersteunen het ICU-berichtformaat hierboven - de syntaxis die meervouden, variabelen en keuzes binnen een vertaling afhandelt in plaats van in code. Beide zijn prima; kies er een en leg de keuze vast in het afsprakenbestand, zodat de volgende AI-sessie niet de andere introduceert.

Drie structurele beslissingen houden de bestanden beheersbaar naarmate het product groeit.

**Namespaces per onderdeel.** Eén bestand per deel van het product - `invoices`, `clients`, `settings`, `common` - in plaats van één enorm bestand. Vertalers werken onderdeel voor onderdeel, mergeconflicten worden zeldzaam, en de bibliotheek kan alleen de namespaces laden die een scherm nodig heeft.

**Sleutels die de plek beschrijven, niet de inhoud.** `invoices.list.empty`, niet `noInvoicesText`. Een sleutel die naar de inhoud is genoemd, wordt onjuist zodra de inhoud verandert; een sleutel die naar de plek is genoemd, blijft juist en vertelt de vertaler waar de tekst verschijnt.

**Een namespace `common` voor echt gedeelde woorden** - opslaan, annuleren, verwijderen, de dagen van de week - en verder niets. Een `common`-bestand dat uitgroeit tot de helft van het product, maakt het doel van namespaces ongedaan.

## Bouw Nooit Zinnen uit Fragmenten

Het meest voorkomende defect in vertaalde producten, en het defect dat AI-gegenereerde code het betrouwbaarst oplevert:

```tsx
// Fout: de zin wordt in code samengesteld
{t('youHave')} {count} {t('openInvoices')}
```

De woordvolgorde verschilt per taal, dus een zin die uit stukken wordt samengesteld, is niet correct te vertalen. In dit voorbeeld lopen Nederlands en Engels toevallig gelijk op; in de volgende zin niet, en een derde taal breekt het volledig.

De regel: één sleutel per volledige zin, met de variabelen erin.

```json
"openSummary": "U heeft {count, plural, one {# openstaande factuur} other {# openstaande facturen}} met een totaal van {total}."
```

Hetzelfde geldt voor zinnen met links of nadruk. "Lees onze *voorwaarden* voordat u verdergaat" opsplitsen in drie sleutels rond de link, levert fragmenten op die een vertaler niet kan ordenen. Beide grote bibliotheken ondersteunen rich-text-placeholders - `"Lees onze <link>voorwaarden</link> voordat u verdergaat"` - zodat de zin heel blijft en het component de link levert.

## Waar de Taal Vandaan Komt

Een product heeft één heldere regel nodig voor welke taal iemand ziet, op dezelfde manier toegepast in de browser en op de server. De volgorde die werkt voor een B2B-product:

1. **De opgeslagen voorkeur van de gebruiker**, als die is ingelogd en er een heeft gekozen.
2. **De taal in de URL**, voor openbare pagina's zoals `/nl/` en `/en/`.
3. **Een cookie** die wordt gezet wanneer een anonieme bezoeker van taal wisselt.
4. **De header `Accept-Language` van de browser**, als eerste gok voor nieuwe bezoekers.
5. **Nederlands**, als standaard.

De opgeslagen voorkeur hoort in de database, bij de gebruiker en niet bij de organisatie:

```sql
alter table profiles
  add column locale text not null default 'nl'
  check (locale in ('nl', 'en'));
```

Per gebruiker opslaan doet ertoe omdat de reden dat de meeste Nederlandse producten Engels toevoegen, is dat Nederlandse organisaties mensen in dienst hebben die het liever gebruiken. Een voorkeur per organisatie dwingt het hele bedrijf in één taal en levert precies de klacht op die het werk in gang zette.

In de database opslaan in plaats van alleen in de browser doet ertoe omdat de server haar nodig heeft: e-mails, pdf's, geplande meldingen en alles wat wordt gemaakt terwijl de gebruiker niet naar een scherm kijkt.

## Opmaak Is Geen Vertaling

Tekst is het zichtbare deel. Vier andere dingen verschillen tussen Nederlandse en Engelse gebruikers, en ze verkeerd doen laat een vertaald product in beide talen vreemd aanvoelen.

| | Nederlands (`nl-NL`) | Brits Engels (`en-GB`) | Amerikaans Engels (`en-US`) |
|---|---|---|---|
| Bedrag | € 1.250,50 | €1,250.50 | €1,250.50 |
| Datum, kort | 03-04-2028 | 03/04/2028 | 4/3/2028 |
| Datum, lang | 3 april 2028 | 3 April 2028 | April 3, 2028 |
| Tijd | 14:30 | 14:30 | 2:30 PM |
| Eerste dag van de week | maandag | maandag | zondag |

Daaruit volgen twee conclusies. Ten eerste: maak getallen, geld of datums nooit met de hand op; gebruik de `Intl`-formatters van het platform met de locale van de gebruiker:

```ts
new Intl.NumberFormat(locale, { style: 'currency', currency: 'EUR' }).format(1250.5);
new Intl.DateTimeFormat(locale, { dateStyle: 'long', timeZone: 'Europe/Amsterdam' }).format(date);
```

Ten tweede: voor een Europees product betekent Engels bijna altijd `en-GB` in plaats van `en-US`. Uw Engelssprekende gebruikers zitten in Europa, werken van maandag tot vrijdag met weken die op maandag beginnen, gebruiken op het werk de 24-uursklok en lezen datums als dag-maand. Standaard Amerikaanse conventies aanhouden is een van de duidelijkste signalen dat een product is vertaald in plaats van gebouwd voor zijn gebruikers.

Let op de tijdzone in het voorbeeld. Een datum die zonder tijdzone wordt opgemaakt, wordt opgemaakt in de tijdzone van de machine waarop de code draait - de laptop van de gebruiker, of een server in een andere regio - en het tijdzone-artikel in deze reeks beschrijft wat dat met afspraaktijden doet. De locale bepaalt hoe een datum eruitziet; de tijdzone bepaalt welke datum het is. Beide moeten expliciet zijn.

Geef voor alles waarbij een verkeerd gelezen datum gevolgen heeft - afspraken, deadlines, vervaldata - de voorkeur aan het lange formaat met de maand uitgeschreven. "3 april 2028" kan niet verkeerd worden gelezen; "03/04/2028" wel, door iemand.

## Meervouden, Aanspreekvorm en Toon

**Meervouden** worden afgehandeld door de ICU-syntaxis in plaats van door er een "s" aan te plakken. Nederlands en Engels hebben allebei twee vormen, wat het probleem verbergt totdat een taal met meer vormen wordt toegevoegd - nog een reden om vanaf het begin de meervoudsregels van de bibliotheek te gebruiken.

**Formele en informele aanspreekvorm** is een Nederlandse beslissing zonder Engelse tegenhanger. Het product moet één keer kiezen tussen "u" en "je", het opschrijven, en het overal toepassen, zoals het artikel over design systems in deze reeks betoogt. Voor B2B-producten in gereguleerde sectoren - zorg, financiën, overheid - is "u" de veilige standaard; voor producten gericht op een jonger of creatief publiek is "je" gebruikelijk. De fout is geen van beide keuzes; het is ze mengen, en dat is wat machinevertaling vanuit het Engels oplevert, omdat het Engels er geen aanwijzing voor geeft.

**Toon** verdient een korte geschreven richtlijn voor beide talen: hoe foutmeldingen worden geformuleerd, of het product gebruikers direct aanspreekt, hoe formeel bevestigingen zijn. Een halve pagina, en het is wat een vertaler - mens of model - in staat stelt consistente beslissingen te nemen over zinnen die niemand had voorzien.

## Tekst Die de Server Maakt

De interface is de makkelijke helft. De moeilijkere helft is tekst die buiten de browser wordt gemaakt, en daar hebben AI-gebouwde producten het vaakst Nederlands diep in de backend vastgecodeerd.

**Validatie- en foutmeldingen.** Een edge function die `"Het e-mailadres is ongeldig"` teruggeeft, heeft de server verantwoordelijk gemaakt voor taal. Het betere contract is een code: de server geeft `{ "error": "email_invalid" }` terug en de interface vertaalt `errors.email_invalid`. De server blijft taalneutraal, en dezelfde API bedient elke client.

**Statussen en categorieën in de database.** Sla codes op - `paid`, `overdue`, `draft` - nooit weergavetekst. Een kolom `status` met "Betaald" maakt elk rapport, elk filter en elke integratie afhankelijk van het Nederlands, en Engels toevoegen betekent een datamigratie. Vertaal de code bij het tonen: `t('invoice.status.paid')`.

**E-mails en meldingen.** Op de server gerenderd met de opgeslagen locale van de ontvanger. Templates staan naast de interfacevertalingen - of in dezelfde berichtbestanden - zodat een tekstwijziging niet in twee systemen hoeft.

**Pdf's en documenten.** Gerenderd met een expliciete locale, die voor facturen bewust kan afwijken van de interfacetaal van de gebruiker, zoals hieronder besproken.

**Geplande taken.** Een herinnering die 's nachts wordt verstuurd, heeft geen browser en geen verzoek. Ze moet de locale uit het profiel van de ontvanger lezen, en de taak is waar vastgecodeerd Nederlands het langst overleeft, omdat niemand het tijdens het testen ziet.

## Beslis Wat Wordt Vertaald

Niet alles heeft twee talen nodig, en de beslissingen moeten worden opgeschreven in plaats van per scherm genomen.

| Content | Vertalen? | Regel |
|---|---|---|
| Interface | Ja | Volgt de locale van de gebruiker |
| Transactionele e-mails | Ja | Volgt de opgeslagen locale van de ontvanger |
| Facturen | Bewust | Meestal de zakelijke taal van de klant, niet de interfacetaal van de gebruiker |
| Contracten, voorwaarden, privacybeleid | Ja, zorgvuldig | De Nederlandse versie is vaak juridisch leidend; vermeld dat in de Engelse versie |
| Eigen data van klanten | Nee | Blijft in de taal waarin ze is geschreven |
| Marketingpagina's | Ja, apart | Eigen URL's per taal, met hreflang |
| Help en documentatie | Geleidelijk | Begin met de pagina's waarnaar support het vaakst verwijst |

De factuurregel verdient een toelichting. De Engelssprekende officemanager van een Nederlands bedrijf kan de interface in het Engels gebruiken, terwijl de accountant van het bedrijf facturen in het Nederlands verwacht. Maak de factuurtaal een instelling van de organisatie van de klant, niet een gevolg van wie op de knop drukte.

De marketingregel doet ertoe voor vindbaarheid. Een taalschakelaar die de tekst op één URL wisselt, is in de tweede taal onzichtbaar voor zoekmachines. Elke taal heeft een eigen URL nodig - `/nl/prijzen` en `/en/pricing` - met `hreflang`-tags die naar elkaar verwijzen, zoals de SEO-artikelen in deze reeks uitgebreid beschrijven.

## De Vertaalworkflow

De verleiding is het model alles te laten vertalen en het live te zetten. Voor een eerste concept is dat redelijk; als definitieve versie van iets wat een klant leest, niet.

Machinevertaling van interfacetekst faalt op voorspelbare manieren. Korte teksten missen context - "Post" als zelfstandig naamwoord of werkwoord, "Open" als toestand of actie. Termen lopen uiteen - hetzelfde Nederlandse begrip wordt in drie sessies drie Engelse woorden. De aanspreekvorm raakt gemengd, zoals hierboven beschreven. En lengte wordt genegeerd, zodat een vertaling die de betekenis treft de layout breekt.

De workflow die werkt:

1. **Leg eerst een woordenlijst vast.** De twintig tot veertig begrippen waarop uw product is gebouwd - cliënt, praktijk, afspraak, factuur, locatie - met de ene afgesproken vertaling van elk. Dit is het waardevolste document in het proces.
2. **Schrijf in de taal waarin u denkt.** Voor de meeste Nederlandse oprichters is dat Nederlands; het Nederlandse bestand is de bron.
3. **Laat een model de andere taal opstellen, met context.** Geef de woordenlijst, de toonrichtlijn, de sleutelnaam en waar nuttig een beschrijving van waar de tekst verschijnt. Vertalen zonder context is waar de meeste fouten vandaan komen.
4. **Laat een moedertaalspreker het nakijken.** Een middag voor een product van gemiddelde omvang. Die vangt de problemen met aanspreekvorm op en de termen die juist zijn maar niet idiomatisch.
5. **Houd de bestanden in de repository.** Voor twee talen en een klein team volstaan JSON-bestanden die in pull requests worden gereviewd. Een platform voor vertaalbeheer begint zich terug te betalen bij drie of meer talen of externe vertalers.

## Layout en Tekstuitzetting

Nederlandse tekst is voor dezelfde betekenis merkbaar langer dan Engelse - samenstellingen als "factuurinstellingen" en "betalingsherinnering" zijn lang en kunnen niet afbreken waar het Engels dat wel kan. Een knop ontworpen rond "Save" past misschien niet bij "Opslaan en versturen".

Drie voorzorgsmaatregelen. Ontwerp componenten zo dat ze afbreken of meegroeien in plaats van af te kappen, vooral knoppen, tabelkoppen en navigatie. Gebruik CSS `hyphens: auto` met het juiste `lang`-attribuut op de pagina, zodat lange Nederlandse samenstellingen kunnen afbreken. En test met **pseudo-lokalisatie**: een nep-locale die elke tekst veertig procent langer maakt en tussen markeringen zet - `[!! Ïñvöîçéš !!]` - zodat u binnen minuten ziet welke schermen breken en welke teksten nooit zijn uitgelicht.

## Controles Die Twee Talen Gelijk Houden

Vertaalbestanden lopen uit de pas. Een functie wordt in het Nederlands toegevoegd, de Engelse sleutels worden vergeten, en een Engelse gebruiker ziet `invoices.export.button` op zijn scherm. Vier controles voorkomen het.

**Sleutelpariteit in CI.** Een kort script dat beide locales laadt en de build laat falen wanneer de ene sleutels heeft die de andere mist:

```ts
const missing = flattenKeys(nl).filter(k => !flattenKeys(en).includes(k));
if (missing.length) { console.error('Ontbreekt in en:', missing); process.exit(1); }
```

**Ongebruikte sleutels.** Hetzelfde script, omgekeerd tegen de broncode, toont sleutels die geen component gebruikt. Geen buildfout - een maandelijkse opschoning.

**Zichtbare gaten tijdens ontwikkeling.** Stel de bibliotheek zo in dat ontbrekende sleutels tijdens ontwikkeling opvallend worden getoond, zodat een gat duidelijk is tijdens het bouwen in plaats van in productie.

**Een verstandige terugval in productie.** Ontbreekt een sleutel in het Engels, toon dan de Nederlandse tekst in plaats van de kale sleutel. Een gat dat erdoor glipt, wordt een ongemak in plaats van een kapot scherm.

Voeg één regel toe aan het afsprakenbestand: elke nieuwe tekst wordt in dezelfde wijziging aan beide locale-bestanden toegevoegd. Assistenten lezen het, en het meeste uit de pas lopen stopt bij de bron.

## Een Bestaand Product Achteraf Aanpassen

Voor een product dat al tachtig schermen met vastgecodeerd Nederlands heeft, valt het werk uiteen in een mechanisch deel en een deel dat oordeel vraagt.

Het mechanische deel - elke tekst vinden, vervangen door een sleutel, de sleutel toevoegen aan het Nederlandse bestand - is precies het soort grote, uniforme wijziging dat een AI-agent goed doet, zoals het agentartikel in deze reeks opmerkt. Doe het namespace voor namespace, één onderdeel per wijziging, en review van elk een steekproef.

Het deel dat oordeel vraagt, is alles wat het uitlichten blootlegt: zinnen uit fragmenten, met de hand opgemaakte datums, bedragen aan "€" geplakt, statussen als Nederlandse tekst opgeslagen, foutmeldingen die op de server worden gemaakt, e-mails met vastgecodeerde templates. Elk daarvan vraagt afzonderlijke aandacht, en samen zijn ze het grootste deel van de moeite.

Een realistische schatting voor een product van gemiddelde omvang is twee tot vier dagen, waarvan ongeveer een derde aan uitlichten en twee derde aan de details.

## Dit Inrichten

Voor een Lovable- of Bolt-product dat een tweede taal toevoegt, is dit doorgaans twee tot vier dagen: één i18n-bibliotheek overgenomen en vastgelegd in het afsprakenbestand, elke interfacetekst uitgelicht naar berichtbestanden per namespace met sleutels op basis van plek, zinnen uit fragmenten herschreven als hele berichten met ICU-placeholders, een locale per gebruiker opgeslagen en in een vaste volgorde bepaald op zowel client als server, getallen, geld en datums opgemaakt via `Intl` met een expliciete tijdzone en `en-GB` als Engelse standaard, serverfouten als codes teruggegeven en statussen als codes opgeslagen, e-mails, pdf's en geplande taken gerenderd met de locale van de ontvanger, een geschreven regel voor de taal van facturen en juridische documenten, een woordenlijst en toonrichtlijn in beide talen, een controle door een moedertaalspreker van de conceptvertalingen, pseudo-lokalisatie om layouts te testen, en een CI-controle op sleutelpariteit.

LaunchStudio doet dit als onderdeel van het klaarmaken van een Nederlands product voor de eerste internationale klanten. Daarachter staat Manifera - elf jaar, 160+ projecten, met teams die in het Nederlands, Engels en Vietnamees werken vanuit Amsterdam en Ho Chi Minh-stad.

[Vraag ons hoeveel van uw interface is vastgecodeerd](https://launchstudio.eu/nl/#contact). Het antwoord is meestal: alles.

## Echt voorbeeld

### Twee Codebases in Eén Map

Thijs Wolterink bouwde Kinderopvangplanner in Lovable: roosters en oudercommunicatie voor kinderopvangorganisaties, gebruikt door 21 locaties met zo'n 1.600 kinderen.

Toen twee locaties in Amsterdam om Engels vroegen voor hun expatouders, vroeg hij de tool het toe te voegen. Het resultaat was een taalschakelaar en daarachter condities op 140 stukken tekst verspreid over 38 schermen, die elk inline Nederlands of Engels toonden.

Binnen vier maanden waren de twee talen uit elkaar gegroeid. Negen schermen die sindsdien waren toegevoegd, hadden helemaal geen Engels. Datums in de Engelse versie stonden in de Nederlandse volgorde, waardoor een ouder 4 maart las als 3 april en een maand te vroeg kwam voor een wenmoment. Notificatiemails gingen uit in de taal van de organisatie in plaats van die van de ouder, en de Engelse tekst gebruikte drie verschillende woorden voor "groep" - group, class en unit.

Drie werkdagen: een vertaalbibliotheek overgenomen en alle 140 teksten plus de 61 onvertaalde op de nieuwere schermen uitgelicht naar Nederlandse en Engelse bestanden met sleutels; elf zinnen die uit fragmenten waren opgebouwd herschreven als hele zinnen met placeholders; elke datum, tijd en elk bedrag opgemaakt via de locale van de gebruiker, met uitgeschreven maanden op het rooster voor ouders; een taalvoorkeur per ouder opgeslagen en gebruikt voor notificatiemails; een woordenlijst van veertien begrippen in beide talen afgesproken - onder meer groep, locatie, mentor en wenperiode; het Engels als concept gemaakt door het model en in een middag nagekeken door een moedertaalspreker; en een CI-controle die de sleutelsets vergelijkt en een deployment blokkeert wanneer ze verschillen.

**Resultaat:** de Engelse versie werd volledig en bleef dat; de CI-controle blokkeerde in het kwartaal daarna vier deployments die onvertaalde schermen zouden hebben opgeleverd. Binnen twee maanden tekenden nog drie Amsterdamse locaties, waarvan twee de Engelse oudercommunicatie als reden noemden.

> *"Eén ouder kwam een maand te vroeg omdat we de datum op het Engelse scherm op de Nederlandse manier schreven. Dat was het moment waarop ik ophield vertalen als woorden te zien."*
> - **Thijs Wolterink, Oprichter, Kinderopvangplanner (Amstelveen)**

**Kosten & Doorlooptijd:** €2.900 (vertaalbibliotheek en uitlichten van teksten over 38 schermen, herschreven zinnen, datums en getallen via de locale, taalvoorkeur per gebruiker voor e-mails, tweetalige woordenlijst, controle door moedertaalspreker, CI-vergelijking van sleutels) - afgerond in 3 werkdagen.

## Veelgestelde vragen

### Hoe voeg ik Engels toe aan een Lovable-app?

Neem één vertaalbibliotheek over, vervang elke interfacetekst door een sleutel, en bewaar de woorden in één bestand per taal en onderdeel. Vermijd gedupliceerde schermen, inline condities en vertalingen in de database.

### Moet ik Brits of Amerikaans Engels gebruiken?

Voor een Europees product Brits Engels (`en-GB`): dag-maanddatums, de 24-uursklok en weken die op maandag beginnen, passen bij hoe uw Engelssprekende gebruikers echt werken.

### Wat verschilt er naast tekst tussen Nederlandse en Engelse gebruikers?

Opmaak van getallen en valuta, volgorde van datums, meervoudsregels, en in het Nederlands de keuze tussen formele en informele aanspreekvorm. Maak op via `Intl` met de locale van de gebruiker en een expliciete tijdzone, nooit met de hand.

### En tekst die op de server wordt gemaakt?

Geef foutcodes terug in plaats van meldingen, sla statussen op als codes in plaats van Nederlandse woorden, en render e-mails, pdf's en geplande meldingen met de opgeslagen locale van de ontvanger.

### Hoe voorkom ik dat vertalingen ontbreken?

Met een CI-controle die de sleutelsets van elk taalbestand vergelijkt en faalt wanneer ze verschillen, opvallende ontbrekende sleutels tijdens ontwikkeling, een Nederlandse terugval in productie, en een afspraak dat elke nieuwe tekst in dezelfde wijziging aan beide bestanden wordt toegevoegd.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Hoe voeg ik een tweede taal toe aan een Lovable-app?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Neem één vertaalbibliotheek over, vervang interfacetekst door sleutels, en bewaar de woorden in één bestand per taal en onderdeel - geen gedupliceerde schermen, inline condities of databasetabellen."
      }
    },
    {
      "@type": "Question",
      "name": "Moet een Europees product Brits of Amerikaans Engels gebruiken?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Brits Engels (en-GB): dag-maanddatums, de 24-uursklok en maandag als eerste dag van de week passen bij Europese gebruikers."
      }
    },
    {
      "@type": "Question",
      "name": "Wat verschilt er naast woorden tussen Nederlandse en Engelse gebruikers?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Notatie van getallen en valuta, volgorde van datums, meervoudsregels en formele of informele aanspreekvorm - afgehandeld via Intl-formatters met de locale van de gebruiker en een expliciete tijdzone."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe moet tekst van de server worden vertaald?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Geef foutcodes terug in plaats van meldingen, sla statussen op als codes, en render e-mails, pdf's en geplande meldingen met de opgeslagen locale van de ontvanger."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe voorkom ik ontbrekende vertalingen in productie?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Een CI-controle die sleutelsets vergelijkt, zichtbare ontbrekende sleutels tijdens ontwikkeling, een Nederlandse terugval in productie, en een regel dat nieuwe teksten in dezelfde wijziging in beide bestanden komen."
      }
    }
  ]
}
</script>
