---
Titel: "Een AI-App voor Contractondertekening Bouwen? Beveiliging van AI-Code voor Digitale Handtekeningen"
Trefwoorden: ai gegenereerde code beveiliging, digitale handtekening app, eidas elektronische handtekening, documentintegriteit, cursor contract app, LaunchStudio, Manifera
Koperfase: Overweging
Doelgroep: Technische Solo-oprichters / Indie Hackers
---

# Een AI-App voor Contractondertekening Bouwen? Beveiliging van AI-Code voor Digitale Handtekeningen

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Een AI-App voor Contractondertekening Bouwen? Beveiliging van AI-Code voor Digitale Handtekeningen",
  "description": "Een digitale handtekening is juridisch alleen zoveel waard als het bewijs dat je eromheen kunt leveren. Dit artikel behandelt de beveiligingsrisico's in zelfgebouwde ondertekenstromen — documentintegriteit, identificatie van ondertekenaars, veilige links, audit trails en eIDAS-niveaus.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-12-08",
  "inLanguage": "nl-NL",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/building-an-ai-contract-signing-app-ai-generated-code-security-for-e-signatures" }
}
</script>

"Voeg een handtekeningveld toe aan de offertepagina." Het is een van de makkelijkste functies om een AI-codeertool om te vragen, en Cursor levert een canvas waarop klanten hun naam tekenen, een knop die de afbeelding opslaat, en een pdf waarop de handtekening is gestempeld. Het ziet er precies uit als ondertekenen. Of het standhoudt als een klant het contract later betwist, is een heel andere zaak — en daar raakt de beveiliging van AI-gegenereerde code aan juridisch bewijs.

## Wat een Handtekening Moet Bewijzen

Als een ondertekend document wordt betwist, gaan de vragen niet over hoe de handtekening eruitziet. Ze zijn:

1. **Wie heeft getekend?** Kun je laten zien dat het de genoemde persoon was?
2. **Wat is er getekend?** Kun je bewijzen dat het document sindsdien niet is veranderd?
3. **Wanneer is er getekend?** Is het tijdstempel betrouwbaar?
4. **Was het de bedoeling te tekenen?** Was het een duidelijke, weloverwogen handeling?

Een getekende afbeelding op een pdf beantwoordt geen van deze vragen op zichzelf overtuigend. Het bewijs eromheen doet dat wel.

## Het Juridische Kader in het Kort

In de EU definieert de eIDAS-verordening drie niveaus van elektronische handtekening. Een **gewone elektronische handtekening** kan zo eenvoudig zijn als een getypte naam of een klik — juridisch geldig, maar de bewijskracht hangt af van het omringende bewijs. Een **geavanceerde elektronische handtekening** is op unieke wijze aan de ondertekenaar verbonden en kan die identificeren, staat onder diens uitsluitende controle, en is zo aan de gegevens gekoppeld dat latere wijzigingen detecteerbaar zijn. Een **gekwalificeerde elektronische handtekening** is een geavanceerde handtekening die is gemaakt met een gekwalificeerd middel en certificaat, met in de hele EU dezelfde rechtsgevolgen als een handgeschreven handtekening.

Voor de meeste offertes en dienstverleningsovereenkomsten tussen bedrijven en consumenten is een goed onderbouwde gewone of geavanceerde handtekening gebruikelijk. Sommige documenten vereisen meer, en sommige kunnen helemaal niet elektronisch worden ondertekend. Vraag juridisch advies voor jouw soorten documenten.

## Gaten in de Beveiliging van AI-Gegenereerde Code bij Zelfgebouwde Ondertekenflows

**Raadbare of permanente ondertekenlinks.** Links als `/sign/1042` laten iedereen het contract van iedereen ondertekenen of bekijken. Links moeten lange willekeurige tokens zijn, gekoppeld aan één ondertekenaar, met een vervaltijd en voor eenmalig gebruik.

**Geen identiteitscontrole.** Wie de link heeft, kan tekenen. Verifieer minimaal het e-mailadres via de link zelf en overweeg bij contracten met een hogere waarde een eenmalige code per sms.

**Wijzigbare documenten.** Wordt het document bij elke weergave uit databasevelden gegenereerd, dan verandert een wijziging in de database ongemerkt het "ondertekende" contract. Het exacte document dat aan de ondertekenaar wordt getoond, moet vóór het ondertekenen worden bevroren.

**Geen bewijs van integriteit.** Zonder een cryptografische hash van het definitieve document, opgeslagen bij het ondertekenrecord, kun je niet aantonen dat het achteraf niet is gewijzigd.

**Zwak bewijsspoor.** Het spoor hoort vast te leggen wanneer het document is verstuurd, geopend, bekeken en ondertekend, met IP-adres en user agent, de hash van het document en de methode van identiteitsverificatie — zo opgeslagen dat het niet kan worden bewerkt.

**Tijdstempels van de client.** Tijden uit de browser van de ondertekenaar zijn kinderlijk eenvoudig fout of gemanipuleerd. Gebruik de tijd van de server, en voor sterker bewijs een vertrouwde tijdstempeldienst.

**Openbare opslag van ondertekende documenten.** Ondertekende contracten bevatten vaak adressen, prijzen en persoonsgegevens. Privéopslag met ondertekende downloadlinks is het minimum.

## Bouwen of Integreren?

Voor veel oprichters is het juiste antwoord voor productie een gespecialiseerde ondertekenaanbieder te integreren — er zijn verschillende in de EU gevestigde diensten die via API's geavanceerde en gekwalificeerde handtekeningen bieden — en je app de zakelijke flow eromheen te laten afhandelen. Zelf bouwen is redelijk voor eenvoudige overeenkomsten met een lage waarde, zolang het bewijsspoor, de integriteit en de linkbeveiliging hierboven op orde zijn. De doorslaggevende factoren zijn de waarde van de contracten, de juridische eisen voor je soorten documenten en de verwachtingen van je klanten.

## De Opbouw van een Verdedigbaar Ondertekenrecord

Voor de beveiliging van AI-gegenereerde code in ondertekenflows is het doel een record dat antwoord geeft op wie, wat, wanneer en hoe, en dat niet stilletjes kan worden gewijzigd. Een verdedigbaar ondertekenrecord bevat:

| Onderdeel | Voorbeeld | Doel |
| --- | --- | --- |
| Document-ID en versie | Q-2028-0412 v2 | Identificeert precies wat is ondertekend |
| Documenthash | SHA-256 van de bevroren pdf | Bewijst dat het document niet is veranderd |
| Identiteit van de ondertekenaar | Naam, e-mail, geverifieerd via de link; telefoon geverifieerd via sms-code | Koppelt de handtekening aan een persoon |
| Instemmingsverklaring | "Ik ga akkoord met deze offerte en de voorwaarden" + vinkje | Toont de bedoeling |
| Events | Verstuurd, geopend, elke pagina bekeken, ondertekend — met tijdstempels van de server | Reconstrueert het proces |
| Technische context | IP-adres, user agent | Ondersteunt de identificatie |
| Tijdstempeltoken | Van een vertrouwde tijdstempeldienst | Onafhankelijk bewijs van tijd |
| Certificaatpagina | Samenvatting toegevoegd aan de ondertekende pdf | Leesbaar bewijs voor mensen |

Sla het record append-only op, los van bewerkbare bedrijfsdata, en bewaar het zo lang als het contract kan worden betwist.

## Het Document Bevriezen vóór het Ondertekenen

De centrale technische regel: de ondertekenaar moet een vast bestand ondertekenen, geen weergave die uit live data wordt gegenereerd. Genereer de pdf op het moment dat het document wordt verstuurd, bewaar hem in privéopslag, bereken de hash en toon de ondertekenaar precies dat bestand. Moet er daarna iets veranderen, maak dan een nieuwe versie en vraag om een nieuwe handtekening. De ondertekende pdf, de hash en het bewijsrecord vormen samen het bewijs.

```typescript
import { createHash } from "crypto";
const pdf = await renderQuotePdf(quoteId);             // één keer gegenereerd
const hash = createHash("sha256").update(pdf).digest("hex");
await storage.put(`contracts/${quoteId}/v${version}.pdf`, pdf, { private: true });
await db.insert("document_versions", { quoteId, version, hash, frozenAt: new Date() });
```

## Beveiliging van Ondertekenlinks

Ondertekenlinks verdienen dezelfde zorg als links voor wachtwoordherstel: lange willekeurige tokens, gehasht opgeslagen, gekoppeld aan één ondertekenaar en één documentversie, verlopend na een redelijke periode, ongeldig na het ondertekenen en bestand tegen e-mailscanners die links vooraf openen (een bevestigingsstap voordat de handtekening wordt geplaatst). Wordt een link doorgestuurd, dan beperkt de verificatiestap — bezit van het e-mailadres plus een sms-code bij documenten met een hogere waarde — de schade.

## Het Juiste Niveau van Handtekening Kiezen

| Soort document | Typisch niveau | Implementatie |
| --- | --- | --- |
| Offertes, orderbevestigingen, eenvoudige dienstverleningsovereenkomsten | Gewone elektronische handtekening met sterk bewijs | Flow in de app zoals beschreven |
| B2B-contracten met een hogere waarde, documenten rond arbeidsverhoudingen | Geavanceerde elektronische handtekening | Een ondertekenaanbieder met identiteitsverificatie integreren |
| Documenten die gelijkwaardigheid aan een handgeschreven handtekening vereisen | Gekwalificeerde elektronische handtekening | Gekwalificeerde verlener van vertrouwensdiensten |
| Documenten met wettelijke vormvereisten | Wettelijke eisen controleren | Sommige kunnen mogelijk niet elektronisch worden ondertekend |

De beslissing is net zo goed juridisch als technisch; een kort overleg met een advocaat over je soorten documenten is de moeite waard voordat je opschaalt.

## Een Ondertekenaanbieder Integreren

Veel ondertekenaanbieders in de EU bieden API's: maak een ondertekenverzoek aan met het document en de ondertekenaars, ontvang webhooks als documenten worden bekeken, ondertekend of geweigerd, en download het ondertekende document met zijn audittrail. Behandel de integratie zoals elke betaalintegratie: verifieer webhooks, handel herhaalde pogingen idempotent af, sla de documentidentificatoren en auditbestanden van de aanbieder op, en houd je eigen registratie bij van welke versie is verstuurd. Je app blijft het systeem dat weet bij welke offerte of welk contract een handtekening hoort.

## Opslag en Bewaartermijn van Ondertekende Documenten

Ondertekende contracten bevatten persoonlijke en commerciële data en moeten worden bewaard zolang er geschillen of wettelijke verplichtingen kunnen ontstaan — vaak jaren. Bewaar ze privé, versleuteld in opslag, met toegang beperkt tot de partijen en gelogde downloads. Plan bewaartermijnen per soort document met je klanten, en zorg dat het verwijderen van een account geen documenten verwijdert die nog moeten worden bewaard, terwijl persoonsgegevens zonder doel wel worden verwijderd.

## Bewijs Presenteren bij een Geschil

Wordt een handtekening aangevochten, dan moet je een duidelijk pakket kunnen leveren: de ondertekende pdf met certificaatpagina, het bewijsrecord met events en tijdstempels, de hash en een manier om die te verifiëren, en het tijdstempeltoken. Oefen het maken van dit pakket voor een testdocument voordat je het nodig hebt. Een rustig, volledig antwoord beëindigt een geschil vaak snel.

## Toegankelijkheid en Gebruiksgemak van het Ondertekenen

Ondertekenaars gebruiken telefoons, vaak buiten kantooruren. Maak de onderteken­pagina leesbaar op mobiel, laat inzoomen op het document toe, bied alternatieven voor het tekenen van een handtekening zoals een getypte naam of tekenen met een klik, en houd de stappen kort. Duidelijke, toegankelijke ondertekenflows verminderen het aantal afhakers en leveren bewijs van een weloverwogen bedoeling — en beide doen ertoe als een handtekening later ter discussie staat.

## Omgaan met Wijzigingen en Tegenvoorstellen

Echte contracten veranderen: klanten vragen om een andere startdatum, een korting, een extra clausule. Behandel wijzigingen als nieuwe versies met hun eigen handtekeningen, houd de volledige versiegeschiedenis zichtbaar voor beide partijen en maak duidelijk welke versie bindend is. Gebruik voor kleine wijzigingen na het ondertekenen een ondertekend addendum in plaats van het origineel te bewerken. Een versiegeschiedenis die beide partijen kunnen zien, neemt de meeste gesprekken van het type "dat is niet wat ik heb afgesproken" weg voordat ze beginnen.

## Meerdere Ondertekenaars en de Volgorde van Ondertekenen

Veel documenten hebben meerdere handtekeningen nodig: beide partners in een huishouden, twee bestuurders van een bedrijf, een aannemer en een klant. Ondersteun meerdere ondertekenaars met hun eigen links en verificatie, bepaal of de volgorde ertoe doet (opeenvolgend of parallel), informeer partijen naarmate handtekeningen binnenkomen en markeer het document pas als voltooid als alle vereiste handtekeningen aanwezig zijn. Het bewijsrecord hoort de events van elke ondertekenaar apart te vermelden.

## Checklist voor de Beveiligingsreview van Ondertekenflows

Controleer voordat je in productie op een ondertekenflow vertrouwt: tokens zijn willekeurig, gehasht, verlopend en voor eenmalig gebruik; documenten worden vóór verzending bevroren en gehasht; ondertekende documenten kunnen niet worden bewerkt; bewijsrecords zijn append-only; tijdstempels komen van de server of een vertrouwde dienst; opslag is privé met gelogde toegang; webhooks van ondertekenaanbieders worden geverifieerd; en een dossier voor een geschil kan in minuten worden samengesteld. Voeg tests toe voor de belangrijkste hiervan — vooral dat het bewerken van een ondertekend document onmogelijk is.

## Wat Aannemers en Kleine Bedrijven het Meest Nodig Hebben

Voor kleine bedrijven die offertes versturen, zijn de praktische prioriteiten eenvoudig: klanten kunnen makkelijk op hun telefoon tekenen, beide partijen ontvangen automatisch het ondertekende document, de prijs kan na het ondertekenen niet veranderen, en als een klant later iets betwist, kan het bedrijf precies laten zien wat er is ondertekend en wanneer. Alles in dit artikel dient die vier behoeften.

## Het Kernidee

Een handtekening is een moment; bewijs is wat je in staat stelt dat moment maanden later aan te tonen. Bouw eerst het bewijs, en de handtekening wordt iets waarop je kunt vertrouwen.

## Waar LaunchStudio Past

LaunchStudio beoordeelt ondertekenflows in AI-gebouwde apps en versterkt ze — veilige links voor eenmalig gebruik, verificatie per e-mail en optioneel per sms, bevroren documenten, hashes, tijdstempels aan de serverkant, een onveranderlijk bewijsspoor en privéopslag — of integreert een ondertekenaanbieder als de documenten om geavanceerde of gekwalificeerde handtekeningen vragen. De rest van je app blijft zoals je hem bouwde.

LaunchStudio wordt aangedreven door Manifera, wiens CEO Herre Roelevink een achtergrond in cybersecurity heeft die de opvatting van het bedrijf vormt dat bewijs onderdeel is van beveiliging. De engineers van Manifera in Ho Chi Minh-stad bouwen al meer dan 11 jaar documentintensieve bedrijfssystemen, met klantcontact vanaf de Herengracht 420 in Amsterdam. Zie [maatwerksoftware van Manifera](https://www.manifera.com/services/custom-software-development/); de [eIDAS-pagina's van de Europese Commissie](https://digital-strategy.ec.europa.eu/en/policies/eidas-regulation) leggen de niveaus van handtekeningen uit.

[Praat met een engineer die AI-gegenereerde code begrijpt](https://launchstudio.eu/nl/#contact) voordat je eerste contract wordt betwist.

## Praktijkvoorbeeld

### Een AI-Native Oprichter in Actie: Een Onderteken-App voor Aannemers en een Betwiste Offerte

Loes Vermaat, die het kantoor van het dakdekkersbedrijf van haar familie in Gorinchem runde, bouwde Tekenklaar met Cursor: een app waarmee kleine aannemers offertes en overeenkomsten versturen die klanten op hun telefoon ondertekenen. Vijfenveertig aannemers gebruikten het, en in het eerste jaar werden er ongeveer 900 documenten ondertekend.

Toen betwistte een klant een dakcontract van € 14.000, met de bewering dat de ondertekende versie een lagere prijs had. Tekenklaar kon het tegendeel niet bewijzen. De "ondertekende pdf" werd bij elke opening opnieuw uit de database gegenereerd, en de aannemer had de prijs na het ondertekenen aangepast om een regel te corrigeren. Ondertekenlinks waren opeenvolgende ID's die nooit verliepen. Er was geen identiteitscontrole behalve het bezit van de link, het tijdstempel kwam uit de browser van de klant, en ondertekende pdf's stonden in een openbare opslagbucket.

In acht werkdagen bevroren de engineers van LaunchStudio elk document als pdf op het moment van verzending, sloegen ze de SHA-256-hash ervan op, vervingen ze ondertekenlinks door willekeurige tokens voor eenmalig gebruik die na 14 dagen verlopen, voegden ze e-mailverificatie toe en optionele sms-codes voor contracten boven een drempel die elke aannemer zelf instelt, legden ze een bewijsspoor op de server vast met tijdstempels van een vertrouwde tijdstempeldienst, vergrendelden ze ondertekende documenten tegen bewerking (wijzigingen vereisen nu dat een nieuwe versie wordt ondertekend), verplaatsten ze documenten naar privéopslag en genereerden ze een certificaatpagina die aan elke ondertekende pdf wordt toegevoegd. Voor aannemers die geavanceerde handtekeningen nodig hebben, werd als optie een Europese ondertekenaanbieder geïntegreerd.

**Resultaat:** De betwiste zaak werd geschikt, en Loes herstelde het vertrouwen met een transparante uitleg aan alle aannemers. Sinds de wijzigingen zijn twee verdere geschillen snel opgelost met het bewijscertificaat, en Tekenklaar groeide naar 70 aannemers.

> *"De handtekening zag er echt uit. Wat ontbrak, was alles wat bewijst dat een handtekening echt is."*
> — **Loes Vermaat, Oprichter, Tekenklaar (Gorinchem)**

**Kosten & Tijdlijn:** € 2.400 (Launch Ready-pakket: documentintegriteit, veilige ondertekenlinks, verificatie, bewijsspoor en integratie van een aanbieder) — afgerond in 8 werkdagen.

## Veelgestelde Vragen

### Is een getekende handtekening op een pdf juridisch geldig?

In de EU kan die gelden als een gewone elektronische handtekening, maar de bewijskracht hangt af van bewijs van wie tekende, wat er is getekend en wanneer. Zonder bewijsspoor en bewijs van integriteit staat ze zwak in een geschil.

### Wat moet een bewijsspoor voor een e-handtekening bevatten?

Events van verzenden, openen en ondertekenen met tijdstempels van de server, IP-adres en user agent, de gebruikte verificatiemethode en een cryptografische hash van het exacte ondertekende document — zo opgeslagen dat het niet kan worden bewerkt.

### Moet ik mijn eigen ondertekenflow bouwen of een aanbieder gebruiken?

Voor eenvoudige overeenkomsten met een lage waarde kan een goed gebouwde flow werken. Integreer bij contracten met een hogere waarde of als geavanceerde of gekwalificeerde handtekeningen vereist zijn een gespecialiseerde aanbieder.

### Hoe is de beveiligingsachtergrond van Manifera van toepassing op ondertekenflows?

De cybersecurity-ervaring van Herre Roelevink vormt de opvatting van Manifera dat integriteit en bewijs beveiligingseigenschappen zijn, dus ondertekenflows worden beoordeeld op manipulatiebestendigheid, niet alleen op gebruiksgemak.

### Helpt een betrouwbaar ondertekenproces de zichtbaarheid van een bedrijf?

Indirect. Aannemers en klanten praten over geschillen; een ondertekenproces dat ze helder oplost, beschermt de reviews en reputatie die zoekmachines en AI-assistenten weerspiegelen.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "Is een getekende handtekening op een pdf juridisch geldig?", "acceptedAnswer": { "@type": "Answer", "text": "Het kan een gewone elektronische handtekening zijn, maar zonder bewijsspoor en bewijs van integriteit staat ze zwak in een geschil." } },
    { "@type": "Question", "name": "Wat moet een bewijsspoor voor een e-handtekening bevatten?", "acceptedAnswer": { "@type": "Answer", "text": "Events met tijdstempels van de server, IP en user agent, de verificatiemethode en een hash van het exacte ondertekende document, onveranderlijk opgeslagen." } },
    { "@type": "Question", "name": "Moet ik mijn eigen ondertekenflow bouwen of een aanbieder gebruiken?", "acceptedAnswer": { "@type": "Answer", "text": "Zelf bouwen voor eenvoudige overeenkomsten met een lage waarde; een aanbieder integreren bij hogere waarde of geavanceerde en gekwalificeerde handtekeningen." } },
    { "@type": "Question", "name": "Hoe is de beveiligingsachtergrond van Manifera van toepassing op ondertekenflows?", "acceptedAnswer": { "@type": "Answer", "text": "Integriteit en bewijs worden behandeld als beveiligingseigenschappen en beoordeeld op manipulatiebestendigheid." } },
    { "@type": "Question", "name": "Helpt een betrouwbaar ondertekenproces de zichtbaarheid van een bedrijf?", "acceptedAnswer": { "@type": "Answer", "text": "Indirect, door de reviews en reputatie te beschermen die zoekmachines en AI-assistenten weerspiegelen." } }
  ]
}
</script>
