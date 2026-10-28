---
Titel: "Lovable Hosting: Feature Flags en Eerst aan een Deel van de Klanten Releasen"
Trefwoorden: lovable feature flags, gefaseerde uitrol, noodschakelaar, bètaprogramma, releasebeheer, Supabase, LaunchStudio, Manifera
Koperfase: Overweging
Doelgroep: Technische solo-oprichter / Indie hacker
---

# Lovable Hosting: Feature Flags en Eerst aan een Deel van de Klanten Releasen

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Lovable Hosting: Feature Flags en Eerst aan een Deel van de Klanten Releasen",
  "description": "Code deployen en een functie releasen hoeven niet hetzelfde moment te zijn. Hoe feature flags u eerst aan een paar klanten laten leveren, een kapotte of dure functie in seconden laten uitzetten en een bètaprogramma laten draaien - en hoe u voorkomt dat flags een rommel worden.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-03-21",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/lovable-hosting-feature-flags-and-releasing-to-some-customers-first" }
}
</script>

In de meeste AI-gebouwde producten zijn deployen en releasen dezelfde gebeurtenis. De code gaat live, en elke klant ziet de nieuwe functie op hetzelfde moment. Werkt het, dan merkt niemand het risico dat werd genomen. Werkt het niet - een berekening die voor één soort klant fout is, een scherm dat faalt op de data van het grootste account, een koppeling die een leverancier overspoelt - dan loopt elke klant tegelijk tegen het probleem aan, en is het enige middel een terugdraaiactie die al het andere in de release meeneemt.

Feature flags scheiden de twee. Code wordt gedeployd zodra ze klaar is, uitgeschakeld. De functie wordt daarna bewust gereleased: eerst aan uzelf, dan aan een paar welwillende klanten, dan aan een percentage, dan aan iedereen - met de mogelijkheid haar in seconden weer uit te zetten, zonder deployment, als er iets misgaat.

Voor een klein product klinkt dit als machinerie voor grote bedrijven. Dat is het niet. Een tabel, een functie en een paar gewoonten leveren het grootste deel van het voordeel op, en ze veranderen hoe comfortabel releasen voelt meer dan bijna elke andere praktijk. Dit artikel behandelt de soorten flags, een eenvoudige implementatie op Supabase, gefaseerde uitrol, noodschakelaars, het verschil tussen flags en abonnementen, en de discipline die voorkomt dat flags permanente rommel worden.

## Vier Soorten Flags

Het woord dekt verschillende hulpmiddelen, en ze als één behandelen is hoe flagsystemen verwarrend worden.

**Releaseflags** verbergen een functie totdat ze klaar is en sturen de uitrol. Ze zijn tijdelijk: zodra de functie voor iedereen is gereleased, worden de flag en het oude codepad verwijderd. De meeste flags horen van deze soort te zijn.

**Noodschakelaars** zetten iets uit wat al werkt - een AI-functie, een uitgaande koppeling, een duur rapport, sms-herinneringen - wanneer het zich misdraagt, te veel kost, of afhangt van een leverancier die een storing heeft. Ze zijn permanent en moeten regelmatig worden getest, zoals een brandalarm.

**Klantflags** zetten iets aan voor specifieke organisaties: een functie gebouwd voor één grote klant, een programma voor vroege toegang, een configuratie die maar sommige klanten nodig hebben. Ze kunnen lang bestaan, en ze lopen over in de volgende categorie.

**Rechten op functies (entitlements)** bepalen waarvoor een klant heeft betaald - abonnementslimieten, premiummodules. Ze lijken op flags maar zijn het niet; ze horen bij facturatie, zoals hieronder besproken.

Geef elke flag een naam met haar soort - `release.online_booking`, `kill.ai_recall_suggestions`, `customer.bulk_import_v2` - zodat iedereen die de code leest weet hoe lang ze bedoeld is te bestaan.

## Een Minimale Implementatie

Voor een Supabase-product dekken twee tabellen en één functie de meeste behoeften.

```sql
create table feature_flags (
  key text primary key,
  description text not null,
  kind text not null check (kind in ('release', 'kill', 'customer')),
  enabled boolean not null default false,       -- globale standaard
  rollout_percent int not null default 0 check (rollout_percent between 0 and 100),
  owner text not null,
  expires_on date,                              -- verplicht voor releaseflags
  updated_at timestamptz not null default now()
);

create table feature_flag_overrides (
  flag_key text references feature_flags(key) on delete cascade,
  organisation_id uuid references organisations(id) on delete cascade,
  enabled boolean not null,
  primary key (flag_key, organisation_id)
);
```

De beoordeling volgt een vaste volgorde: een expliciete uitzondering voor de organisatie wint; anders doet de organisatie mee als ze binnen het uitrolpercentage valt; anders geldt de globale standaard.

```ts
function isEnabled(flag: Flag, orgId: string, overrides: Map<string, boolean>): boolean {
  const override = overrides.get(orgId);
  if (override !== undefined) return override;
  if (flag.rollout_percent > 0 && bucket(flag.key, orgId) < flag.rollout_percent) return true;
  return flag.enabled;
}

// Stabiele bucket 0–99: dezelfde organisatie valt voor een flag altijd in dezelfde bucket.
function bucket(flagKey: string, orgId: string): number {
  return parseInt(sha256(flagKey + ':' + orgId).slice(0, 8), 16) % 100;
}
```

Twee details doen ertoe. Rol uit per organisatie in plaats van per gebruiker, zodat collega's bij hetzelfde bedrijf hetzelfde product zien - niets levert sneller verwarde supporttickets op dan twee mensen bij één klant die verschillende schermen zien. En gebruik een stabiele hash, zodat het verhogen van het percentage van 10 naar 25 organisaties toevoegt zonder er een te verwijderen die de functie al had.

Laad de flags één keer per verzoek of cache ze kort - dertig tot zestig seconden - in plaats van bij elke controle een query te doen. Een noodschakelaar die een minuut nodig heeft om effect te hebben, is prima; een die een deployment vereist, niet.

## Beoordeel op de Server

Flags kunnen in de browser of op de server worden beoordeeld, en het verschil doet ertoe.

Een flag die alleen in de frontend wordt beoordeeld, verbergt een knop. Ze voorkomt niet dat het endpoint achter de knop werkt, en iedereen kan dat endpoint rechtstreeks aanroepen, zoals de artikelen over beheerpanelen en IDOR in deze reeks beschrijven. Elke flag die gedrag bewaakt - niet alleen uiterlijk - moet ook op de server worden gecontroleerd: in de edge function, in de RPC, of in een row level security policy als ze toegang tot data regelt.

In de browser beoordeeld verraden flags ook wat er aankomt. Een lijst met elke flag en haar status, naar elke client gestuurd, vertelt concurrenten en nieuwsgierige klanten over functies die nog niet zijn gereleased. Stuur de client alleen de beoordeelde resultaten die hij voor de huidige organisatie nodig heeft, niet de volledige configuratie.

De regel: een flag is nooit een beveiligingsgrens. Ze bepaalt wanneer iets wordt gereleased, niet wie het mag doen. Wie het mag, is de taak van rechten.

## Gefaseerde Uitrol in de Praktijk

Een release met flags volgt doorgaans dezelfde volgorde.

1. **Donker deployen.** De code staat in productie, de flag staat voor iedereen uit. Voor klanten verandert er niets.
2. **Intern.** Zet haar aan voor uw eigen organisatie en gebruik haar op echte infrastructuur.
3. **Bètaklanten.** Zet haar aan voor een handvol organisaties die hebben afgesproken nieuwe functies vroeg te zien en te vertellen wat er kapot is - bij voorkeur inclusief een van uw grootste accounts, omdat grote accounts de problemen vinden die kleine nooit veroorzaken.
4. **Percentage.** 10%, dan 25%, dan 50%, over dagen in plaats van minuten, waarbij u bij elke stap foutpercentages, prestaties en supportberichten in de gaten houdt.
5. **Iedereen.** De flag staat globaal aan.
6. **Opruimen.** Verwijder binnen een paar weken de flag en het oude codepad.

Het bewaken bij stap vier is wat de percentages betekenis geeft. Label fouten en trage verzoeken met de flags die actief waren, zodat "de fouten namen toe nadat de uitrol naar 25% ging" zichtbaar is in de tooling uit het logartikel in plaats van te worden afgeleid uit een gevoel.

Niet elke wijziging heeft elke stap nodig. Een tekstwijziging heeft er geen nodig. Een nieuwe berekening, een nieuwe koppeling, een opnieuw ontworpen werkproces of alles wat met geld te maken heeft, verdient de volledige volgorde.

## Noodschakelaars voor de Dingen Die U Pijn Kunnen Doen

Sommige functies zijn waardevol en riskant: ze kosten geld per gebruik, hangen af van een externe leverancier, of raken mensen buiten uw product. Elk daarvan hoort vanaf de dag dat het wordt gebouwd een noodschakelaar te hebben.

**AI-functies** - wanneer de modelaanbieder een storing heeft, wanneer de kosten pieken door een lus of misbruik, of wanneer de kwaliteit van de uitvoer daalt. De artikelen over AI-kosten en evaluatie in deze reeks beschrijven de faalwijzen.

**Uitgaande berichten** - sms, e-mailcampagnes, WhatsApp-meldingen - wanneer een bug er te veel verstuurt of naar de verkeerde mensen.

**Koppelingen** - boekhoudsynchronisatie, aanroepen naar de betaalprovider, de webhook van een klant - wanneer de andere kant faalt en uw nieuwe pogingen het erger maken.

**Zwaar achtergrondwerk** - grote rapporten, herberekeningen in bulk - wanneer het de database op een druk moment bedreigt.

Een noodschakelaar moet de functie netjes uitzetten: de interface legt uit dat de functie tijdelijk niet beschikbaar is, werk in de wachtrij wacht in plaats van te falen, en niets wordt half gedaan. Test elke noodschakelaar periodiek - zet hem op een rustig uur uit en weer aan - omdat van een schakelaar die niemand heeft gebruikt, niemand weet of hij werkt.

## Flags Zijn Geen Abonnementen

De meest voorkomende ontwerpfout is prijzen implementeren met feature flags: een flag per premiumfunctie, met de hand aangezet voor betalende klanten.

Het werkt voor drie klanten en faalt bij dertig. Niemand kan zien welke klant waarvoor heeft betaald, upgrades en downgrades vereisen handmatige flagwijzigingen die worden vergeten, en de flagtabel wordt een tweede, onbetrouwbaar factureringssysteem.

Houd ze gescheiden. Rechten op functies worden afgeleid uit het abonnement van de klant - pakket, add-ons, limieten - zoals de artikelen over abonnementen en proefperiodes in deze reeks beschrijven, en gecontroleerd door een functie voor die rechten. Feature flags regelen de release van functies, los van wat iemand heeft betaald. Een nieuwe premiumfunctie heeft doorgaans beide nodig: de flag bepaalt of de functie al is gereleased, het recht bepaalt of deze klant haar heeft gekocht.

## Flags en Databasewijzigingen

Flags maken de applicatie schakelbaar; ze maken de database niet schakelbaar. Een functie die een nieuwe kolom of tabel vereist, heeft die wijziging nodig voordat de flag voor wie dan ook aangaat, en ze moet blijven werken of de flag nu aan of uit staat.

Dit is het expand-and-contract-patroon uit het artikel over deployen zonder downtime in deze reeks: voeg de nieuwe structuur toe naast de oude, laat de code naar beide schrijven terwijl de flag wordt uitgerold, schakel het lezen om achter de flag, en verwijder de oude structuur pas nadat de flag is opgeheven. Een flag uitzetten mag nooit data achterlaten die de oude code niet kan lezen.

## Voorkom Dat Flags Schuld Worden

Elke flag verdubbelt het aantal paden door een stuk code. Tien flags in één onderdeel betekent dat dat onderdeel zich op meer manieren kan gedragen dan iemand heeft getest. Flagsystemen falen niet door het mechanisme, maar omdat flags nooit worden verwijderd.

Vier gewoonten voorkomen het.

**Elke releaseflag heeft een eigenaar en een vervaldatum**, afgedwongen door de tabel. Een controle in CI of een wekelijks rapport toont flags waarvan de vervaldatum is verstreken.

**De flag verwijderen hoort bij de functie.** De taak is pas af wanneer de flag en het oude pad zijn verwijderd. Zet het op de lijst wanneer de flag wordt aangemaakt.

**Beperk het aantal actieve releaseflags.** Zijn het er meer dan een handvol, dan begint het team meer dan het afmaakt.

**Leg elke wijziging vast** - wie welke flag voor wie omzette, en wanneer - in het auditlog, en toon recente wijzigingen naast foutgrafieken. "De fouten begonnen toen iemand dit voor 50% aanzette" hoort in seconden zichtbaar te zijn.

## Beide Paden Testen

Zolang een flag bestaat, zijn beide paden productiecode en hebben beide tests nodig. Draai de relevante tests met de flag aan en uit, in elk geval voor releaseflags die geld, rechten of data raken.

Test bij noodschakelaars specifiek de uit-toestand: de functie is niet beschikbaar, de interface zegt dat, werk in de wachtrij blijft bewaard, en er ontstaan geen fouten.

En verwijder de tests voor het oude pad samen met de flag, zodat de suite niet blijft testen op gedrag dat niet meer bestaat.

## Klanten Vertellen Wat Er Veranderde

Een gefaseerde uitrol schept een communicatievraag die een release voor iedereen tegelijk niet kent: op elk moment hebben sommige klanten een functie en andere niet.

Drie praktijken voorkomen dat dat verwarrend wordt.

**Kondig aan op het moment dat een klant de functie krijgt, niet wanneer ze wordt gedeployd.** Een melding in het product die door dezelfde flag wordt gestuurd - "Nieuw: online boeken vanaf uw website" - verschijnt alleen voor organisaties waar de flag aanstaat. Releasenotes op uw site beschrijven functies die voor iedereen beschikbaar zijn, met bètafuncties als zodanig gemarkeerd.

**Bereid support voor vóór het eerste percentage.** De mensen die vragen van klanten beantwoorden - vaak de oprichter - moeten weten welke organisaties welke functies hebben. Een klein paneel in uw beheeromgeving dat de actieve flags van een organisatie toont, beantwoordt "waarom ziet mijn collega bij de andere vestiging iets wat ik niet zie?" in seconden.

**Geef beheerders een keuze bij ingrijpende wijzigingen.** Een opnieuw ontworpen werkproces dat verandert hoe medewerkers elke dag werken, is makkelijker te accepteren als de beheerder van de klant er op een geschikt moment naar kan overstappen - binnen een venster, waarna het de standaard wordt. Geïmplementeerd als uitzondering op de releaseflag die de klant zelf beheert, kost het weinig en maakt het van weerstand een planning.

Zo gedaan is een gefaseerde uitrol niet alleen veiliger; ze wordt merkbaar beter ontvangen, omdat klanten nieuwe functies ervaren als iets wat bewust aankomt in plaats van iets wat hun 's nachts overkwam.

## Bouwen of Inkopen

De minimale implementatie hierboven is genoeg voor de meeste kleine producten, en heeft het voordeel dat ze in uw eigen database leeft, dicht bij uw organisaties en rechten.

Gespecialiseerde tools - Unleash en Flagsmith, beide zelf te hosten of beschikbaar in EU-regio's, de feature flags van PostHog als u dat al voor analyse gebruikt, LaunchDarkly aan de enterprisekant - voegen een interface toe voor niet-developers, rijkere targeting, analyse van experimenten en SDK's. Ze worden de moeite waard wanneer meerdere mensen releases beheren, wanneer u experimenten draait die statistiek nodig hebben, of wanneer het aantal flags groter wordt dan een tabel en een korte beheerpagina comfortabel aankunnen. Gebruikt u er een, dan ontvangt die identificatoren van organisaties en mogelijk kenmerken van gebruikers, wat haar een subverwerker maakt om op te nemen, zoals het artikel over subverwerkers in deze reeks beschrijft.

## Een Bètaprogramma Dat Klanten Waarderen

Flags maken een bètaprogramma eenvoudig te draaien, en een bètaprogramma is meer waard dan alleen de risicovermindering.

Nodig klanten uit die graag vroeg zijn - meestal een mix van enthousiaste kleine accounts en één of twee grotere - en geef ze een expliciete afspraak: ze zien functies eerder dan anderen, ze vertellen u wat er niet klopt, en ze accepteren dat dingen kunnen veranderen. Markeer bètafuncties zichtbaar in de interface. Vraag op een specifiek moment om feedback in plaats van in het algemeen.

Klanten in een bètaprogramma worden vaak de sterkste referenties van het product, omdat ze hebben geholpen het vorm te geven. En functies die eerst aan hen worden gereleased, komen bij alle anderen aan met de ruwe kanten al gevonden.

## Dit Inrichten

Voor een Lovable- of Supabase-product is dit doorgaans twee tot drie dagen: een flagtabel met soorten, eigenaars en vervaldata, uitzonderingen per organisatie, beoordeling op de server met stabiele verdeling per percentage en korte caching, alleen beoordeelde resultaten naar de client, flags nooit als beveiligingsgrens, een releasevolgorde van donker deployen via intern, bèta en percentages naar iedereen, fouten en prestaties gelabeld met actieve flags, noodschakelaars voor AI-functies, uitgaande berichten, koppelingen en zware taken met nette uit-toestanden die periodiek worden getest, rechten op functies gescheiden van flags, expand-and-contract voor databasewijzigingen achter flags, een auditlog van flagwijzigingen, een rapport van verlopen flags, tests voor beide paden, meldingen in het product gestuurd door flags, en een klein bètaprogramma met zichtbare bètalabels.

LaunchStudio richt dit in als onderdeel van het routinematig maken van releases voor producten waarop klanten elke dag rekenen. De engineers zijn van Manifera - elf jaar, 120+ engineers, 160+ projecten, vanuit Amsterdam en Ho Chi Minh-stad.

[Vraag ons hoe u uw volgende functie eerst aan drie klanten released](https://launchstudio.eu/nl/#contact).

## Echt voorbeeld

### Dubbel Geboekte Tandartsstoelen op een Maandagochtend

Evelien Hartman bouwde Tandartsplanner in Lovable: afsprakenplanning, terugroepherinneringen en online boeken voor tandartspraktijken, gebruikt door 58 praktijken.

Een nieuwe widget voor online boeken - patiënten die rechtstreeks vanaf de website van een praktijk boeken - werd op een maandagochtend aan alle praktijken tegelijk gereleased. Voor praktijken met gedeelde stoelen, waar één behandelstoel in hetzelfde uur wordt gedeeld door een tandarts en een mondhygiënist, was de beschikbaarheidsberekening van de widget fout. Binnen drie uur hadden elf praktijken dubbel geboekte stoelen, en belden baliemedewerkers patiënten om afspraken te verzetten.

De widget uitzetten betekende terugdraaien. De release bevatte ook een migratie en twee ongerelateerde fixes, dus het terugdraaien kostte de ochtend, waarin online boeken overal onbeschikbaar was. Dezelfde maand had een AI-functie die voorstelde welke patiënten moesten worden teruggeroepen een kostenpiek toen een lus het model herhaaldelijk aanriep, en er was geen manier om die te stoppen zonder te deployen.

Drie werkdagen: een flagtabel met soorten, eigenaars en vervaldata, met uitzonderingen per praktijk en stabiele uitrol per percentage; flags beoordeeld op de server in de boekings- en terugroepfuncties, met alleen beoordeelde resultaten naar de browser; noodschakelaars voor de AI-suggesties voor terugroepen, sms-herinneringen en de boekingswidget, elk met een nette onbeschikbare toestand; een bètagroep van zes praktijken - inclusief de twee grootste en twee met gedeelde stoelen - die afspraken functies eerst te ontvangen; fouten en trage verzoeken gelabeld met actieve flags in de logs; een audit van flagwijzigingen zichtbaar op de beheerpagina; een wekelijks rapport van releaseflags waarvan de vervaldatum was verstreken; en tests voor de boekingsberekening met de flag van de nieuwe widget aan en uit.

**Resultaat:** de gecorrigeerde widget werd in twee weken via de bètagroep, dan 25%, dan iedereen gereleased, zonder één dubbele boeking. In de zes maanden daarna gingen negen functies op dezelfde manier uit; één probleem in een nieuw factuurscherm werd bij drie praktijken opgemerkt en binnen een minuut uitgezet. Toen de modelaanbieder een storing van twee uur had, werd de AI-noodschakelaar aangezet en zagen praktijken een duidelijke melding in plaats van fouten.

> *"Releasen aan alle achtenvijftig praktijken tegelijk betekende dat elf van hen de bug voor ons vonden vóór tien uur. Nu vinden zes praktijken hem, en zet ik hem uit voordat de anderen hem zelfs zien."*
> - **Evelien Hartman, Oprichter, Tandartsplanner (Leiden)**

**Kosten & Doorlooptijd:** €2.800 (flagtabel met uitzonderingen en uitrol per percentage, beoordeling op de server, noodschakelaars voor AI, sms en boeken met nette uit-toestanden, opzet van het bètaprogramma, foutlogging gelabeld per flag, audit van flagwijzigingen, rapportage van verlopen flags, tests voor beide paden) - afgerond in 3 werkdagen.

## Veelgestelde vragen

### Wat is een feature flag?

Een schakelaar die bepaalt of een functie actief is, voor iedereen of voor specifieke klanten, zonder nieuwe code te deployen. Ze scheidt het deployen van code van het releasen van een functie.

### Hebben kleine producten feature flags nodig?

De meeste hebben baat bij een minimale versie: een tabel, uitzonderingen per organisatie, controles op de server en noodschakelaars voor riskante functies. Het kost een paar dagen en maakt releases veel minder riskant.

### Kan een feature flag een functie beschermen tegen onbevoegd gebruik?

Nee. Flags regelen de release, niet de autorisatie. Alles wat een flag in de interface verbergt, moet ook op de server worden gecontroleerd, en wie het mag gebruiken, wordt bepaald door rechten.

### Moet ik flags gebruiken voor betaalde functies?

Niet als factureringsmechanisme. Rechten op functies komen uit het abonnement; flags bepalen of een functie al is gereleased. Een premiumfunctie controleert doorgaans beide.

### Hoe voorkom ik dat flags zich opstapelen?

Geef elke releaseflag een eigenaar en een vervaldatum, maak het verwijderen van de flag deel van het afronden van de functie, beperk het aantal actieve releaseflags, en rapporteer verlopen flags automatisch.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Wat is een feature flag?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Een schakelaar die een functie voor iedereen of voor specifieke klanten aan- of uitzet zonder deployment, en zo deployen en releasen scheidt."
      }
    },
    {
      "@type": "Question",
      "name": "Hebben kleine SaaS-producten feature flags nodig?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Een minimale versie - een tabel, uitzonderingen per organisatie, controles op de server en noodschakelaars - maakt releases voor een paar dagen werk veel veiliger."
      }
    },
    {
      "@type": "Question",
      "name": "Is een feature flag een beveiligingsmaatregel?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Nee - flags regelen de release, niet de autorisatie. Controleer gedrag achter flags op de server en gebruik rechten voor toegang."
      }
    },
    {
      "@type": "Question",
      "name": "Mogen feature flags abonnementen implementeren?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Nee - rechten op functies komen uit het abonnement; flags bepalen alleen of een functie is gereleased. Premiumfuncties controleren beide."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe voorkom ik schuld door feature flags?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Geef releaseflags eigenaars en vervaldata, verwijder ze als onderdeel van de functie, beperk het aantal actieve flags, en rapporteer verlopen flags."
      }
    }
  ]
}
</script>
