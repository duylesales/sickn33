---
Titel: "Case Study: Een PropTech-Oprichter Lanceert Huurderverificatie Zonder Gevoelige Data Op Te Slaan"
Trefwoorden: huurderverificatie app, PropTech MVP lancering, gevoelige data verwerken startup, identiteitsverificatie SaaS, dataminimalisatie compliance, LaunchStudio, Manifera
Koperfase: Beslissing
Doelgroep: SaaS Oprichter Scale-Up
---

# Case Study: Een PropTech-Oprichter Lanceert Huurderverificatie Zonder Gevoelige Data Op Te Slaan

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Case Study: Een PropTech-Oprichter Lanceert Huurderverificatie Zonder Gevoelige Data Op Te Slaan",
  "description": "Een PropTech-oprichter moest de identiteit en het inkomen van huurders verifiëren voor verhuurders. De uitdaging: gevoelige data verzamelen zonder deze op eigen servers op te slaan. Dit is hoe LaunchStudio een verificatieflow implementeerde die persoonsgegevens verwerkt zonder ze ooit te bewaren.",
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
  "datePublished": "2026-12-31",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://launchstudio.eu/nl/blog/proptech-tenant-verification-case-study"
  }
}
</script>

Tom Bakker had een product waar verhuurders om stonden te springen — een huurderscreeningtool die identiteit en inkomen verifieerde vóór het tekenen van een huurcontract, ter vervanging van het onbetrouwbare proces waarbij huurders loonstroken en ID-kopieën moesten mailen. Het probleem was niet de vraag. Het was de data. Op het moment dat HuurCheck een paspoortscan of een salarisstrook op zijn eigen servers opsloeg, werd Toms door Lovable gebouwde prototype een verwerkingsverantwoordelijke onder de AVG met verplichtingen waar hij niet aan kon voldoen: verplichte gegevensbeschermingseffectbeoordelingen, meldplicht bij datalekken binnen 72 uur, afhandeling van verzoeken van betrokkenen, en de aansprakelijkheid die komt kijken bij het beheren van gevoelige persoonsgegevens van duizenden huurders door heel Nederland. Hij had verificatie zonder bewaring nodig — een systeem dat de identiteit en het inkomen van een huurder bevestigde en een resultaat aan de verhuurder leverde zonder dat zijn applicatie ooit de onderliggende documenten vasthield.

## De Oprichter

Tom Bakker, voormalig vastgoedbeheerder in Eindhoven die acht jaar lang handmatig huurders screende. Hij kende elk pijnpunt: verhuurders die huurders om documenten vroegen via e-mail (onveilig), huurders die terughoudend waren om loonstroken te delen met vreemden (begrijpelijk), en het hele proces dat een onversleuteld spoor van gevoelige PDF's achterliet die voor onbepaalde tijd in inboxen bleven staan. HuurCheck was ontworpen om verificatie snel, betrouwbaar en compliant te maken — maar compliance was het deel dat zijn AI-tool niet kon genereren.

## Het Prototype

Gebouwd in Lovable, had HuurCheck een schone, functionele frontend: verhuurders maakten verificatieverzoeken aan, huurders ontvingen een link om documenten te uploaden, en de verhuurder zag een verificatiestatus op zijn dashboard. De UX was gepolijst. Het probleem was de backend: het prototype sloeg geüploade documenten (paspoortscans, loonstroken, arbeidscontracten) rechtstreeks op in Supabase Storage — een platte file-bucket zonder versleuteling in rust, geen automatisch verwijderbeleid, geen toegangsaudittrail, en geen mechanisme om ervoor te zorgen dat documenten werden verwijderd na voltooiing van de verificatie. In zijn prototypestatus was HuurCheck een risico dat op ontploffen stond.

## Wat LaunchStudio Bouwde

Het Manifera-engineeringteam herstructureerde de verificatiebackend van HuurCheck rond een architectuur van dataminimalisatie: de applicatie faciliteert verificatie zonder de gevoelige documenten ooit op zijn eigen infrastructuur op te slaan.

**Verificatiegateway van derden:** In plaats van documenten rechtstreeks te ontvangen en op te slaan, stuurt HuurCheck huurders door naar de gehoste flow van een KYC-verificatieprovider (Know Your Customer). De provider handelt document-upload, identiteitsverificatie en inkomensbevestiging af in zijn gecertificeerde infrastructuur. HuurCheck ontvangt alleen het verificatieresultaat — "identiteit bevestigd, inkomen toereikend voor het opgegeven huurbedrag" of "verificatie onvolledig, reden: document verlopen" — nooit de documenten zelf.

**Alleen resultaatopslag:** De database van HuurCheck slaat alleen het verificatieresultaat op, de tijdstempel, een referentie-ID (zodat de huurder zijn eigen status kan opvragen), en de betrouwbaarheidsscore van de verificatieprovider. Geen paspoortafbeeldingen, geen salarisbedragen, geen werkgeversnamen. De verhuurder ziet "Geverifieerd ✓" of "Nog Niet Geverifieerd" — de minimale informatie die nodig is om een verhuurbeslissing te nemen.

**Automatische datalevenscyclus:** Verificatieresultaten worden automatisch verwijderd 90 dagen na de startdatum van het huurcontract (configureerbaar per verhuurder). De persoonsgegevens van de huurder komen nooit in de database van HuurCheck terecht, en het verificatieresultaat — de enige data die dat wel doet — heeft een gedefinieerde vervaltermijn. Huurders kunnen op elk moment onmiddellijke verwijdering van hun verificatierecord aanvragen via een self-service endpoint.

**Audittrail zonder data:** Elke verificatiegebeurtenis (verzoek aangemaakt, huurder uitgenodigd, verificatie gestart, resultaat ontvangen, resultaat bekeken door verhuurder, resultaat verwijderd) wordt gelogd met tijdstempels en actor-ID's — maar het log bevat geen persoonsgegevens, alleen gebeurtenistypes en anonieme identifiers. Dit voldoet aan de verantwoordingsplicht van de AVG zonder een secundaire opslag van gevoelige informatie te creëren.

## Het Resultaat

HuurCheck lanceerde met een verificatieflow die gevoelige huurdersdata verwerkt zonder deze ooit op te slaan — waardoor het platform een datafacilitator werd in plaats van een verwerkingsverantwoordelijke, met een aanzienlijk eenvoudiger complianceprofiel. In de eerste drie maanden verwerkte HuurCheck 187 huurderverificaties voor 34 verhuurders in Eindhoven, Tilburg, en Den Bosch, met nul gevoelige documenten opgeslagen op de infrastructuur van HuurCheck, op enig moment.

> *"Ik dacht dat compliance betekende een advocaat inhuren en een privacybeleid van 50 pagina's schrijven. Het blijkt dat de beste compliancestrategie is om de data nooit in de eerste plaats te hebben. LaunchStudio ontwierp het systeem zo dat ik niet in de problemen kon komen, zelfs als ik het probeerde."*
> — **Tom Bakker, Oprichter, HuurCheck (Eindhoven)**

**Kosten & Doorlooptijd:** €3.500 (Launch & Grow Pakket, integratie verificatiegateway + alleen-resultaatopslag + datalevenscyclus + audittrail) — live in 14 werkdagen.

---

[LaunchStudio](https://launchstudio.eu/nl/) bouwt data-architecturen die aansprakelijkheid by design minimaliseren — Manifera's engineers beveiligen niet alleen data, ze ontwerpen systemen die het bewaren ervan waar mogelijk vermijden.

[Vertel ons welke gevoelige data uw prototype verwerkt en wij laten zien wat niet opgeslagen hoeft te worden](https://launchstudio.eu/nl/#contact) — de veiligste data is de data die u nooit bewaart.

---

## Veelgestelde Vragen

### Als mijn app gevoelige data moet verwerken, maakt dat mij dan automatisch een AVG-verwerkingsverantwoordelijke?

Dat hangt ervan af of u de data opslaat of alleen de verwerking ervan faciliteert door een gecertificeerde derde partij. Een applicatie die gebruikers doorstuurt naar de gehoste flow van een KYC-provider en alleen een ja/nee-resultaat ontvangt, heeft een aanzienlijk eenvoudiger complianceprofiel dan een applicatie die de onderliggende documenten opslaat.

### Kan een architectuur van dataminimalisatie werken voor elk product dat gevoelige informatie verwerkt?

In veel gevallen wel — het principe van "verwerken maar niet opslaan" is toepasbaar op identiteitsverificatie, betalingsverwerking (Stripe handelt PCI-compliance af zodat u dat niet hoeft te doen), gezondheidsdata (HIPAA-compliant providers handelen opslag af), en veel andere categorieën gevoelige data. De architectuur moet per use case worden ontworpen.

### Beperkt het niet opslaan van gevoelige data wat mijn product kan doen?

Het beperkt bepaalde functies — u kunt bijvoorbeeld de loonstrook van een huurder niet aan de verhuurder tonen als u die nooit heeft opgeslagen. Maar voor de meeste verificatiecases is het resultaat ("geverifieerd" of "niet geverifieerd") wat de gebruiker daadwerkelijk nodig heeft, niet het onderliggende document.

### Wat gebeurt er als de externe verificatieprovider een datalek heeft?

Het lek is de aansprakelijkheid van de provider, niet de uwe — u gebruikt hun gecertificeerde infrastructuur juist zodat uw applicatie de compliancelast niet draagt. Uw blootstelling is beperkt tot de verificatieresultaten die u opslaat, die geen gevoelige persoonsgegevens bevatten.

### Hoeveel kost het gebruik van een externe KYC-provider vergeleken met zelf verificatie afhandelen?

KYC-providers rekenen doorgaans €1-€5 per verificatie. Het bouwen en onderhouden van uw eigen AVG-compliante documentopslag, identiteitsverificatie, en datalevenscyclusbeheer kost aanzienlijk meer aan ontwikkeltijd, infrastructuur, en doorlopende complianceverplichtingen.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Als mijn app gevoelige data moet verwerken, maakt dat mij dan automatisch een AVG-verwerkingsverantwoordelijke?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Dat hangt ervan af of u de data opslaat of alleen de verwerking ervan faciliteert door een gecertificeerde derde partij. Een applicatie die alleen een ja/nee-resultaat ontvangt, heeft een aanzienlijk eenvoudiger complianceprofiel dan een applicatie die de onderliggende documenten opslaat."
      }
    },
    {
      "@type": "Question",
      "name": "Kan een architectuur van dataminimalisatie werken voor elk product dat gevoelige informatie verwerkt?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "In veel gevallen wel - het principe van 'verwerken maar niet opslaan' is toepasbaar op identiteitsverificatie, betalingsverwerking, gezondheidsdata, en veel andere categorieën gevoelige data."
      }
    },
    {
      "@type": "Question",
      "name": "Beperkt het niet opslaan van gevoelige data wat mijn product kan doen?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Het beperkt bepaalde functies, maar voor de meeste verificatiecases is het resultaat wat de gebruiker daadwerkelijk nodig heeft, niet het onderliggende document."
      }
    },
    {
      "@type": "Question",
      "name": "Wat gebeurt er als de externe verificatieprovider een datalek heeft?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Het lek is de aansprakelijkheid van de provider, niet de uwe. Uw blootstelling is beperkt tot de verificatieresultaten die u opslaat, die geen gevoelige persoonsgegevens bevatten."
      }
    },
    {
      "@type": "Question",
      "name": "Hoeveel kost het gebruik van een externe KYC-provider vergeleken met zelf verificatie afhandelen?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "KYC-providers rekenen doorgaans €1-€5 per verificatie. Het bouwen van uw eigen AVG-compliante verificatie-infrastructuur kost aanzienlijk meer aan ontwikkeling en doorlopende compliance."
      }
    }
  ]
}
</script>
