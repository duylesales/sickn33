---
Titel: "Hoe een Echte Security Audit Er Uitziet — en Hoe een Nep-Rapport Er Uitziet"
Trefwoorden: security audit rapport, penetratietest rapport, AI code beveiligingsaudit, kwetsbaarheden overzicht, vulnerability scanner vs pentest, LaunchStudio, Manifera
Koperfase: Beslissing
Doelgroep: Technische Solo-Oprichter / Indie Hacker
---

# Hoe Een Echte Security Audit Er Uitziet — en Hoe Een Nep-Rapport Er Uitziet

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Hoe een Echte Security Audit Er Uitziet — en Hoe een Nep-Rapport Er Uitziet",
  "description": "Een echt security audit rapport bevat concrete bevindingen met bestandslocaties, reproductiestappen, bewijslast en gerichte oplossingen. Een nep-rapport is een ruwe scanner-dump in een PDF-jasje. Hoe u ze onderscheidt vóórdat u betaalt of het rapport aan een klant overhandigt.",
  "author": {
    "@type": "Organization",
    "name": "LaunchStudio",
    "url": "https://launchstudio.eu/nl/"
  },
  "publisher": {
    "@type": "Organization",
    "name": "Manifera",
    "url": "https://www.manifera.com"
  },
  "datePublished": "2027-01-12",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://launchstudio.eu/nl/blog/hoe-een-echte-security-audit-er-uitziet-en-hoe-een-nep-rapport-er-uitziet"
  }
}
</script>

Het PDF-document arriveert op donderdagmiddag in uw inbox. Eenendertig pagina's dik, voorzien van uw eigen bedrijfslogo op het voorblad, een geruststellende groene banner met de tekst **SECURITY ASSESSMENT — PASSED**, en daaronder pagina na pagina gevuld met tabellen die u vaag herkent: pakketnamen, geïnstalleerde versies, gepatchete versies, CVE-nummers en een risicoscore. Veertien 'High'-meldingen, waarvan het merendeel betrekking heeft op indirecte afhankelijkheden van een build-tool die in productie nooit draait. Het rapport sluit af met twee pagina's algemene adviezen over het inschakelen van HTTPS, het gebruik van sterke wachtwoorden en een digitale handtekening.

Dat document heeft u € 1.900 gekost en is in werkelijkheid vrijwel waardeloos. Het is immers niets anders dan de uitvoer van `npm audit` en een geautomatiseerde dependency-scanner, gegoten in een Word-sjabloon. Het bevat geen enkel bewijs dat een mens uw broncode daadwerkelijk heeft geopend. En hier zit het wrange punt: het zal bij sommige zakelijke inkoopafdelingen nog steeds volstaan om een checklist af te vinken — en dat is exact de reden waarom deze schijnmarkt floreert.

Als u een audit inkoopt — of een rapport van een partner accepteert als bewijs van hun vakbekwaamheid — moet u het opgeleverde document zelfstandig op waarde kunnen beoordelen.

## Geautomatiseerde Tools Zijn een Ingang, Geen Eindproduct

Geen enkele serieuze security engineer werkt zonder scanners. Tools zoals `npm audit`, Dependabot, Snyk, Trivy, Semgrep, `gitleaks`, OWASP ZAP en `nuclei` horen thuis in elke professionele ontwikkelstraat. Een auditrapport dat bekende CVE's in externe bibliotheken volledig negeert, zou eveneens tekortschieten. Het onderscheid zit dan ook niet in het wel of niet inzetten van tools; het onderscheid zit in de vraag of een mens de uitvoer van die tools heeft geanalyseerd en gekwalificeerd.

De cruciale taak van een security expert is **triage op bereikbaarheid (reachability)**. Een kritieke CVE in `lodash` is pas een reëel risico wanneer de kwetsbare functie via gebruikersinvoer kan worden aangeroepen op een actieve API-route; het is volkomen irrelevant als het pakket uitsluitend tijdens het compileren op de ontwikkelmachine wordt gebruikt en nooit in de productie-bundel belandt. Een rapport dat veertien ernstige kwetsbaarheden opsomt zonder aan te geven welke daarvan daadwerkelijk bereikbaar zijn vanuit de publieke toegangspunten van uw applicatie, slaat het eigenlijke werk over en verkoopt u ruwe data als een volwaardige analyse.

Het tweede wat uitsluitend een mens kan doen, is het opsporen van fouten die scanners per definitie missen. Voor door AI gegenereerde software is dit doorslaggevend. De typische kwetsbaarheden die tools zoals Lovable, Bolt, v0 en Cursor produceren, betreffen vrijwel altijd **autorisatiefouten in de bedrijfslogica (business-logic authorisation failures)**. Een scanner begrijpt immers niet dat het endpoint `/api/invoices/:id` uitsluitend facturen mag retourneren van het bedrijf waartoe de ingelogde gebruiker behoort. De scanner ziet een HTTP 200-respons en concludeert dat alles naar behoren functioneert. Aangezien circa 45% van de door AI gegenereerde code kwetsbaarheden bevat, en de lekken die in beveiligingsincidenten eindigen vrijwel altijd betrekking hebben op object-autorisatie, multi-tenant scheiding, mass assignment en ongevalideerde webhooks — en zelden op een verouderde `axios`-versie — is menselijke code review onvervangbaar.

## De Anatomie van een Echte Bevinding

Een authentiek auditrapport is een verzameling concrete bevindingen. Elke volwaardige bevinding bevat stelselmatig acht vaste onderdelen. Dit is de structuur waarop u toetst:

1. **Identificatie en titel** — een eenduidige referentie (`FIND-004`) met één heldere beschrijvende zin
2. **Ernst met motivering** — een CVSS v3.1-vectorstring of een expliciete matrix waarin impact en waarschijnlijkheid specifiek voor *uw* implementatie zijn gewogen, geen generieke score uit een database
3. **Getroffen asset** — het exacte bestand en de regelnummers, de API-route, de HTTP-methode en de databasetabel. Expliciet benoemd.
4. **Randvoorwaarden (preconditions)** — wie kan dit misbruiken: een anonieme bezoeker, elke willekeurige ingelogde gebruiker, een gebruiker van een andere organisatie, of een beheerder
5. **Reproductiestappen** — het exacte verzoek (request), direct te kopiëren en te plakken
6. **Bewijslast (evidence)** — de geanonimiseerde serverrespons die aantoont dat de aanval slaagt
7. **Impact** — wat de aanvaller concreet in handen krijgt, geformuleerd in reële bedrijfsschade
8. **Hersteladvies (remediation)** — de concrete codewijziging of configuratieaanpassing, geen algemene link naar een OWASP-pagina

Zo ziet een vakkundig gedocumenteerde bevinding er in de praktijk uit:

```
FIND-004 — Gebrekkige autorisatie op objectniveau bij opvragen facturen
Ernst: Hoog (CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N — Score 7.7)
Getroffen component: app/api/invoices/[id]/route.ts: regels 14–29 (GET)
Randvoorwaarden: elke geauthenticeerde gebruiker met een actief account

De API-handler laadt de factuur direct op basis van de primaire sleutel (ID)
en retourneert deze zonder te controleren of invoice.organisation_id overeenkomt
met de organisatie van de aanvrager. De organisatiefilter is uitsluitend
geïmplementeerd in de frontend React-hook (lib/hooks/useInvoices.ts:22),
een controle die de client eenvoudig kan omzeilen.

Reproductie:
  1. Authenticeer als gebruiker@tenant-b.nl (org_id 88)
  2. Verstuur: GET /api/invoices/4193
     Authorization: Bearer <token van tenant B>
  3. Respons: HTTP 200 met de factuurgegevens van org_id 41

Bewijs: HTTP 200 OK, JSON-body bevat:
{"id":4193,"organisation_id":41,"customer_name":"[AFGESCHERMD]","total_cents":184500,...}

Impact: elke geregistreerde gebruiker kan sequentiële ID's aflopen en alle
facturen in het systeem uitlezen, inclusief klantnamen, factuurbedragen en
adressen van alle 60 aangesloten organisaties. Door de opeenvolgende integer-ID's
is een volledige data-extractie triviaal (ongeveer 4.200 aanroepen).

Hersteladvies: voeg het organisatiefilter toe aan de serverside query
(.eq('organisation_id', session.org_id)) en activeer row-level security op
de tabel public.invoices, zodat het autorisatiebeleid op databaseniveau wordt
afgedwongen in plaats van in één losse route. Hercontroleer met het token van
tenant B; de verwachte respons is HTTP 404.

Hertest 22-01-2027: VOLDAAN — retourneert HTTP 404 Not Found.
```

Deze omschrijving kunt u aan elke competente softwareontwikkelaar geven, waarna het probleem binnen twintig minuten is opgelost. Dat is de ultieme toets: **een bevinding is pas echt wanneer een ontwikkelaar ermee aan de slag kan zonder nadere vragen aan de auditor te hoeven stellen.**

## Vergelijking: Echte Audit versus Geautomatiseerde Scanner-Dump

| Onderdeel | Echte Beveiligingsaudit | Scanner-Dump in PDF-Vorm |
|---|---|---|
| Referentie in bevindingen | Bestandspaden, regelnummers, routes, tabellen | Uitsluitend pakketnamen uit `package.json` |
| Reproductie | Exacte verzoeken, rollen, verwachte versus werkelijke respons | Ontbreekt, of verwijst naar "zie tool-uitvoer" |
| Bewijslast | Geanonimiseerde serverantwoorden, gerichte schermafbeeldingen | Schermafbeelding van het dashboard van de scanner |
| Ernstbepaling | Toegesneden op uw architectuur, met onderbouwing | Rechtstreeks overgenomen uit de CVE-database |
| Bedrijfslogica | Autorisatie, dataleidende rollen en betalingen handmatig getest | Volledig buiten beschouwing gelaten |
| Scope-omschrijving | Geteste omgevingen, rollen, commits en beperkingen genoemd | Vage kreet zoals "volledige applicatiescan" |
| Valse positieven | Expliciet verworpen met motivering | Alles opgenomen om het aantal pagina's op te blazen |
| Oplossing | Concrete code-aanpassing of configuratiewijziging | Generiek advies ("update software"), vaak gekopieerd |
| Hertest | Aparte paragraaf met data en status per bevinding | Ontbreekt volledig |

## De Scope-Verklaring: Waar Eerlijke Rapporten Zich Onderscheiden

Sla het rapport open bij de methodologieparagraaf. Een betrouwbare auditor legt daar nauwkeurig vast wat er *niet* is onderzocht. Dat is geen zwaktebod, maar het fundament onder de geloofwaardigheid van het onderzoek:

> **Onderzochte scope:** de webapplicatie op staging.voorbeeld.nl tussen 6 en 9 januari 2027, geauthenticeerd onder drie specifieke rollen (anoniem, lid, organisatiebeheerder) met testaccounts die door de opdrachtgever ter beschikking zijn gesteld; de RLS-policies en bucket-permissies binnen het Supabase-project; de webhook-afhandeling van Stripe; en de git-repository op commit `a3f19c2`.
>
> **Niet onderzocht:** DoS-aanvallen en stresstests onder zware belasting; de publieke marketingwebsite; externe SaaS-integraties buiten het bereik van onze directe API-aanroepen; social engineering en fysieke beveiliging; mobiele apps. Voor de microservice `pdf-render` was geen broncode beschikbaar; deze is uitsluitend als black-box getoetst.

Elk rapport dat "honderd procent dekkende beveiliging" belooft zonder een tijdsbestek, een git-commit, een specifieke testomgeving en de geteste gebruikersrollen te specificeren, claimt iets wat in software engineering onmogelijk is. Beveiligingsonderzoek is altijd begrensd door tijd en scope; wie doet alsof dat niet zo is, verkoopt u een fabel.

Evenzo is een uitkomst zonder ernstige kwetsbaarheden heel goed mogelijk, maar die formuleert men dan als volgt: *"Binnen de afgebakende scope en het tijdsbestek van acht uur hebben wij drie bevindingen met een laag risico aangetroffen en geen bevindingen van hoog of kritiek niveau. Let op: de isolatie tussen tenants kon slechts gedeeltelijk worden getoetst omdat wij uitsluitend toegang hadden tot accounts binnen één enkele organisatie."* Dat leest heel anders dan een nietszeggende groene 'PASSED'-stempel.

## Vijf Snelle Controles Binnen Negentig Seconden

Voordat u ook maar één pagina tot in detail leest:

1. **Zoek in de PDF naar een `/` in een monospace-codelettertype.** Als er nergens in het document bestands- of routepaden voorkomen, heeft niemand uw broncode gelezen.
2. **Zoek naar de termen "curl", "POST" of "Authorization".** Geen concrete HTTP-requests betekent geen reproductie, en dus geen geverifieerde audit.
3. **Controleer of er bevindingen zijn gemarkeerd als 'vals positief' of 'puur informatief'.** Een echte expert filtert altijd ruis weg. Een rapport waarin elke scan-hit integraal is overgenomen, is niet handmatig beoordeeld.
4. **Zoek naar een hertest-paragraaf (retest).** Het ontbreken ervan is niet direct fataal (hertests worden vaak apart afgesproken), maar de aanwezigheid ervan is een uitstekend signaal: de auditor wil afgerekend worden op de effectiviteit van de reparaties.
5. **Lees de managementsamenvatting en vraag uzelf af of deze uw belangrijkste risico's in gewone mensentaal benoemt.** "Het meest kritieke risico is dat elke ingelogde gebruiker de facturen van alle andere bedrijven kan inzien" is een bruikbare samenvatting. "De applicatie vertoont een gematigd beveiligingsniveau met ruimte voor optimalisaties" is inhoudsloze opvulling.

## Reproduceer Zelf Één Bevinding op Uw Staging-Omgeving

Dit is de meest overtuigende verificatie die u kunt uitvoeren, en het kost u hooguit een uurtje. Kies één bevinding uit het rapport — bij voorkeur eentje met een gemiddeld risico ('Medium'), aangezien kritieke lekken wellicht al provisorisch zijn gedicht — en doorloop de beschreven stappen op uw eigen staging-omgeving. U ziet exact wat het rapport beschrijft, of u ziet het niet.

Werken de stappen niet, dan wijst dat niet direct op bedrog; een codebase evolueert en een bevinding van drie weken geleden kan per toeval zijn verholpen door een recente commit. Vraag de auditor om opheldering en beoordeel de reactie. Een deskundige auditor antwoordt: *"Die specifieke route is gewijzigd in commit 9d2; exact hetzelfde kwetsbaarheidspatroon zit echter nog steeds op `/api/exports`."* Een partij die een scanner-dump heeft geleverd, zal daarentegen direct ontwijkend reageren.

U kunt deze toets overigens exact zo toepassen op een geanonimiseerd auditrapport dat een potentiële ontwikkelpartner u tijdens het selectieproces toont als bewijs van bekwaamheid. Vraag hen om één bevinding toe te lichten en te beargumenteren waarom die specifieke CVSS-score is toegekend. Een engineer die het onderzoek zelf heeft uitgevoerd, discussieert met plezier over de CVSS-parameters. Iemand die louter sjablonen verkoopt, weet niet eens wat een vectorstring inhoudt.

## Audit, Penetratietest, Code Review, Verklaring: Vier Verschillende Zaken

Hanteer de juiste termen, want leveranciers gebruiken ze regelmatig door elkaar terwijl zakelijke inkopers dat beslist niet doen:

- **Secure code review** — een software engineer leest uw broncode handmatig, veelal ondersteund door tools zoals Semgrep of CodeQL. Biedt met afstand de meeste waarde voor door AI gebouwde software, omdat logicafouten direct in de broncode zichtbaar en goedkoop op te sporen zijn.
- **Penetratietest (pentest)** — black-box of grey-box testen van de actieve, draaiende applicatie. Toont aan wat daadwerkelijk misbruikt kan worden via internet, inclusief configuratiefouten op de server. Reken bij gespecialiseerde bureaus doorgaans op € 4.000 tot € 15.000 voor een compacte applicatie.
- **Vulnerability scan** — een geautomatiseerde, periodieke toolscan. Uitstekend als doorlopende nulmeting, maar hoort enkele tientjes per maand te kosten, geen duizenden euro's per rapport.
- **Attestation / Letter of Assurance** — een beknopte formele verklaring van één A4 die de inkoopafdeling van een zakelijke klant in haar archief kan opnemen. Het is een *samenvatting van* een audit, en volstrekt waardeloos zonder het onderliggende technische rapport.

Een zakelijke prospect die vraagt om "uw meest recente security-rapport", heeft doorgaans genoeg aan de formele verklaring (Letter of Assurance) plus een geanonimiseerde managementsamenvatting van de bevindingen. Deel nooit uw volledige rapport met bestandspaden en reproductiestappen met een prospect; dat is onnodig riskant.

## De Realistische Middenweg voor Startups

Voor een solo-oprichter met een AI-gebouwd SaaS-product en een eerste serieuze zakelijke prospect is een complete pentest van tienduizend euro vaak een te zware investering, terwijl een simpel scanner-abonnement simpelweg onvoldoende zekerheid biedt. De pragmatische middenweg is een gerichte menselijke code review die focust op de kwetsbaarheden die AI-tools typisch produceren: permissies op objectniveau, RLS-beleid in Supabase, tenant-isolatie, webhook-handtekeningen, API-sleutels in client-code en mass assignment — opgeleverd als concrete, direct oplosbare bevindingen, gevolgd door een professionele reparatie.

Dat is exact de opzet van de security-audits binnen het [Launch Ready traject van LaunchStudio](https://launchstudio.eu/nl/), geprijsd tussen € 800 en € 3.500 met een doorlooptijd van één tot drie weken. De onderzoeken worden uitgevoerd door dezelfde senior engineers die de security-trajecten leiden bij moederbedrijf [Manifera](https://www.manifera.com/about-us/manifera-technologies/). Onze rapporten bevatten concrete reproductiestappen in plaats van nietszeggende certificaat-stempels. Geeft u de voorkeur aan een onafhankelijk gespecialiseerd auditbureau voor de inspectie en een andere partij voor het herstelwerk? Ook dat is een uitstekende en zuivere structuur.

**Heeft u een auditrapport ontvangen en twijfelt u over de kwaliteit? Stuur het ons toe en wij vertellen u kosteloos of het een serieuze analyse betreft of een veredelde scanner-dump — of deel uw repository met ons voor een open gesprek met engineers die dagelijks AI-code auditen.**

## Praktijkvoorbeeld

### Een Indie Hacker in Actie: Het Rapport Dat Zijn Eigen Reproductietest Niet Doorstond

Ruben Hoekstra, een solo-ontwikkelaar in Groningen, bouwde ShiftLedger: een in Cursor ontwikkelde planningsapplicatie voor horecagroepen. Om te voldoen aan de vendor questionnaire van een grote hotelketen kocht hij voor € 1.600 een "security assessment". Het rapport somde negentien kwetsbaarheden op, waarvan zeventien betrekking hadden op npm-afhankelijkheden, en kende de app het eindoordeel "Low Risk" toe.

Toen Ruben probeerde twee van de bevindingen zelf te verifiëren, liep hij vast: het document bevatte geen enkele reproductiestap. Wat hem echter écht zorgen baarde, was dat het rapport met geen woord repte over autorisatie — terwijl hij drommels goed wist dat zijn route `/api/shifts` de vestigingen enkel filterde in de frontend React Query-hook en niet op de server. Hij voerde zelf een test uit met een tweede account: de API leverde zonder morren de complete dienstroosters en bijbehorende bruto uurlonen van álle hotels uit.

Een second opinion via LaunchStudio leverde binnen twee dagen elf concrete bevindingen op inclusief bestandsverwijzingen: het ontbreken van serverside autorisatie op de dienstenroute, een publiek toegankelijke storage-bucket met arbeidscontracten, een Mollie-webhook die gemanipuleerde betalingsstatussen accepteerde en uitgeschakelde RLS op vier kerntabellen.

**Resultaat:** De autorisatie van ShiftLedger werd verplaatst naar de server met hard afgedwongen RLS in PostgreSQL, de webhook werd voorzien van cryptografische handtekeningverificatie, en Ruben doorstond de audit van de hotelketen glansrijk met een reproduceerbaar rapport inclusief hertest-verklaring — voor € 2.700 vast binnen acht werkdagen.

> *"Het eerste rapport gaf mij het stempel 'Laag Risico' voor een app waarin elke ingelogde gebruiker de salarisadministratie van concurrerende hotels kon downloaden. Het tweede rapport leverde mij elf serieuze problemen en een flinke kater op — maar dat was precies de waarheid waarvoor ik had betaald."*
> — **Ruben Hoekstra, Oprichter, ShiftLedger (Groningen)**

---

## Veelgestelde Vragen

### Is een CVSS-score verplicht voor een legitiem auditrapport?

Niet verplicht, maar een expliciete methodiek voor risicoclassificatie is dat wél. Sommige auditoren gebruiken een heldere matrix van impact maal waarschijnlijkheid, wat prima volstaat. Onacceptabel is een willekeurig risicocijfer zonder toelichting, of een CVSS-score zónder de bijbehorende vectorstring — want juist in die string zit de technische onderbouwing van de score.

### Wat kost een serieuze security review van een AI-gebouwd prototype?

Een gerichte menselijke code review van een afgebakende applicatie ligt doorgaans tussen de € 1.000 en € 3.500; een volwaardige black-box penetratietest door een gespecialiseerd bureau begint meestal rond de € 4.000 en loopt op naarmate de scope groeit. Wie een "complete audit" aanbiedt voor enkele honderden euro's, levert uitsluitend geautomatiseerde scanner-output.

### Mag hetzelfde bureau ook de geconstateerde beveiligingslekken repareren?

Het is gebruikelijk en efficiënt, al is er sprake van een lichte belangenverstrengeling. De remedie is een rapport dat zo specifiek en gedetailleerd is dat elke willekeurige externe ontwikkelaar de fixes kan doorvoeren. Dat is precies waarom u moet vasthouden aan bestandspaden en concrete reproductiestappen: het maakt de bevindingen direct overdraagbaar.

### Wat stuur ik daadwerkelijk naar een zakelijke klant die om security-documentatie vraagt?

Stuur een beknopte formele verklaring (Letter of Assurance) met de scope, data en het eindresultaat, vergezeld van een managementsamenvatting waarin de aantallen bevindingen per risicoklasse en de status van de oplossingen staan vermeld. Het versturen van het integrale technische rapport met exacte bestandspaden en aanvalsinstructies naar een prospect is overbodig en kan zelfs veiligheidsrisico's opleveren.

### Mijn database draait op Supabase en het dashboard staat volledig op groen. Is dat niet voldoende?

Het dashboard toont aan dat de cloudinfrastructuur operationeel gezond is, niet dat uw autorisatieregels waterdicht zijn. De meest voorkomende ernstige kwetsbaarheid in prototypes met Supabase is dat Row Level Security (RLS) is uitgeschakeld of te permissief staat geconfigureerd op tabellen die de frontend rechtstreeks bevraagt. Een groen dashboard is perfect verenigbaar met een database waarvan alle klantdata wagenwijd openstaat voor iedereen met een login.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Is een CVSS-score verplicht voor een legitiem auditrapport?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Niet verplicht, maar een heldere risicomethodiek wel. Een transparante matrix van impact maal waarschijnlijkheid volstaat, maar een los cijfer zonder methode of een CVSS-score zonder vectorstring is onvoldoende onderbouwd."
      }
    },
    {
      "@type": "Question",
      "name": "Wat kost een serieuze security review van een AI-gebouwd prototype?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Een gerichte menselijke code review van een compacte app ligt meestal tussen de 1.000 en 3.500 euro, terwijl een complete black-box penetratietest begint rond 4.000 euro. Aanbiedingen van enkele honderden euro's betreffen louter geautomatiseerde scanner-output."
      }
    },
    {
      "@type": "Question",
      "name": "Mag hetzelfde bureau ook de geconstateerde beveiligingslekken repareren?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Dat is gangbaar en praktisch, mits het rapport zo gedetailleerd is dat ook een externe ontwikkelaar de reparaties kan uitvoeren. Duidelijke bestandspaden en reproductiestappen maken de bevindingen overdraagbaar."
      }
    },
    {
      "@type": "Question",
      "name": "Wat stuur ik daadwerkelijk naar een zakelijke klant die om security-documentatie vraagt?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Een formele verklaring van één pagina met de scope, data en managementsamenvatting van de bevindingen en mitigaties. Deel niet het volledige technische rapport met kwetsbare paden en exploit-instructies."
      }
    },
    {
      "@type": "Question",
      "name": "Mijn database draait op Supabase en het dashboard staat volledig op groen. Is dat niet voldoende?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Nee. Het dashboard bevestigt dat de clouddienst draait, niet dat uw autorisatieregels deugen. Uitgeschakelde of te open RLS-regels op direct bevraagde tabellen zijn een veelvoorkomend lek bij een ogenschijnlijk groen dashboard."
      }
    }
  ]
}
</script>
