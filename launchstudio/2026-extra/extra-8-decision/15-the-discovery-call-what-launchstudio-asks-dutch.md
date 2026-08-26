---
Titel: "De Discovery Call: Wat LaunchStudio Daadwerkelijk Vraagt en Waarom"
Trefwoorden: LaunchStudio discovery call, scoping gesprek software, wat vraagt een software partner, AI codebase intake, technische audit intake, LaunchStudio, Manifera
Koperfase: Beslissing
Doelgroep: AI-Native Oprichter (Niet-technisch)
---

# De Discovery Call: Wat LaunchStudio Daadwerkelijk Vraagt en Waarom

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "De Discovery Call: Wat LaunchStudio Daadwerkelijk Vraagt en Waarom",
  "description": "De intake bij LaunchStudio is geen glad verkoopgesprek, maar een gestructureerde technische diagnose. Een overzicht van de exacte vragen die we stellen en waarom 'ik weet het niet' vaak het meest nuttige antwoord is.",
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
    "@id": "https://launchstudio.eu/nl/blog/the-discovery-call-what-launchstudio-asks"
  }
}
</script>

Veel niet-technische oprichters zien op tegen een technische intake call met een software-engineeringbedrijf. De angst om 'door de mand te vallen', moeilijke vragen over architectuur niet te kunnen beantwoorden of overrompeld te worden door onbegrijpelijk jargon is wijdverbreid.

Bij LaunchStudio is de **Discovery Call (Scoping Call)** echter uitdrukkelijk niet ontworpen om uw technische kennis te testen. Het is een gestructureerde, vriendelijke diagnose waarin we samen ontdekken waar uw prototype staat en wat er nodig is om veilig live te gaan. In dit artikel leest u exact welke vragen we stellen, waarom we ze stellen, en waarom het antwoord *"dat weet ik eigenlijk niet"* voor onze engineers vaak het meest waardevolle startpunt is.

## De Vier Categorieën Vragen Tijdens de Discovery Call

In een videogesprek van 20 tot 30 minuten doorlopen we vier specifieke domeinen:

### 1. Functionele Flow & Gebruikerscontext
- *"Wie zijn uw eindgebruikers (consumenten, zzp'ers of zakelijke accounts)?"*
- *"Hebben gebruikers verschillende rollen (bijvoorbeeld beheerder, medewerker, read-only)?"*
- **Waarom we dit vragen:** Dit vertelt ons direct hoe complex de autorisatie- en multi-tenant logica moet zijn.

### 2. Gevoelige Data & Externe Integraties
- *"Welke gevoelige data verwerkt de applicatie (wachtwoorden, medische data, financiële rapporten)?"*
- *"Welke externe API's en tools gebruikt u (Stripe, OpenAI, Resend, Mollie)?"*
- **Waarom we dit vragen:** Dit bepaalt waar we encryptie moeten toepassen en welke API-endpoints cryptografisch geverifieerd moeten worden.

### 3. De Ontstaansgeschiedenis van de Codebase
- *"Met welke AI-tool is het prototype gebouwd (Lovable, Bolt, Cursor, v0)?"*
- *"Heeft u zelf handmatig code aangepast of externe bibliotheken geïnstalleerd?"*
- **Waarom we dit vragen:** Elke AI-builder heeft zijn eigen karakteristieke patronen en valkuilen. Dit helpt ons binnen enkele minuten gericht naar bekende risico's te zoeken.

### 4. Zakelijke Randvoorwaarden & Deadlines
- *"Wanneer wilt u live gaan voor uw eerste betalende klanten?"*
- *"Zijn er formele compliance-eisen (zoals AVG-verklaringen of DPIA's van klanten)?"*
- **Waarom we dit vragen:** Hiermee bepalen we welke technische punten absolute prioriteit hebben voor de lancering.

## Waarom "Ik Weet Het Niet" Een Uitstekend Antwoord Is

Veel oprichters voelen zich opgelaten als ze moeten zeggen dat ze niet weten hoe hun database-beveiliging is geconfigureerd. Maar voor onze engineers is dit juist uiterst waardevolle informatie:

- Als u zegt: *"Ik weet niet of Supabase Row-Level Security aanstaat,"* noteren we direct dat onze engineer dit zélf in de repository moet verifiëren.
- Een offerte die gebaseerd is op aannames leidt tot meerwerk. Een offerte die gebaseerd is op directe codebase-verificatie garandeert een **onwrikbare vaste prijs**.

## Wat Gebeurt Er Na de Call?

Direct na het gesprek logt een senior engineer van Manifera in op uw repository of inspecteert de gedeelde code. Binnen 24 tot 48 uur ontvangt u een overzichtelijk, schriftelijk voorstel met een exacte vaste prijs (€800 tot €7.500) en een gegarandeerde doorlooptijd.

[LaunchStudio](https://launchstudio.eu/nl/) maakt software-intakes eerlijk, deskundig en ontspannen, ondersteund door 11+ jaar enterprise ervaring van Manifera.

[Boek uw discovery call](https://launchstudio.eu/nl/#contact) — u hoeft geen expert te zijn; breng mee wat u weet en wij zoeken de rest uit.

## Real example

### Een AI-Native Oprichter in de Praktijk: Een Accurate Vaste Offerte Bij de Eerste Poging

Marieke Hendriks, oprichter van PitchPrep in Groningen (een met Bolt gebouwde tool waarmee startups investeerderspitches kunnen oefenen met AI-feedback), had eerder een nare ervaring met een freelancer. De freelancer had een offerte afgegeven op basis van twee alinea's e-mailtekst, maar verdubbelde de prijs na drie weken omdat de authenticatie 'ingewikkelder bleek dan gedacht'.

Marieke kwam voorbereid naar LaunchStudio's discovery call om eerlijk toe te geven wat ze niet wist. Op de vraag of Row-Level Security in Supabase goed was ingesteld, antwoordde ze openlijk dat ze geen idee had.

**Resultaat:** Twee dagen na de call inspecteerde de Manifera-engineer de repository, stelde vast dat RLS gedeeltelijk aanstond maar een kritiek lek bevatte op de audio-opnametabel, en bracht een vaste offerte uit van €1.900. Het project werd exact binnen die prijs en 9 werkdagen live gezet, zonder enige scope-verrassing.

> *"Bij eerdere partijen voelde 'ik weet het niet' als een zwaktebod. Bij LaunchStudio bleek het het meest nuttige wat ik kon zeggen: ze zochten het direct zelf uit in de code en gaven me een vaste prijs die niet meer veranderde."*  
> — **Marieke Hendriks, Oprichter PitchPrep (Groningen)**

**Kosten & Doorlooptijd:** €1.900 (Launch Ready Pakket, Supabase RLS reparatie & API-beveiliging) — live in 9 werkdagen.

---

## Veelgestelde Vragen

### Moet ik technische kennis hebben om een discovery call bij LaunchStudio in te plannen?
Nee, absoluut niet. Onze vragen gaan over hoe uw product werkt en wie uw klanten zijn. De technische verificatie in de broncode voeren onze senior engineers zelfstandig uit.

### Waarom kijkt LaunchStudio direct in de codebase in plaats van alleen af te gaan op de call?
Omdat wat een oprichter vertelt en wat er werkelijk in de code staat door de aard van AI-tools vaak verschilt. Directe inspectie voorkomt scope-verrassingen en maakt een 100% vaste prijsgarantie mogelijk.

### Wat als ik het antwoord op een technische vraag tijdens het gesprek niet weet?
Dat is volkomen normaal en zelfs heel nuttig. Het vertelt onze engineer exact welke onderdelen we direct in de repository moeten onderzoeken.

### Hoe snel na de discovery call ontvang ik de definitieve offerte?
Meestal binnen 24 tot 48 uur na afloop van het gesprek en de initiële codebase review.

### Verplicht de discovery call mij tot het afnemen van een pakket?
Nee. De discovery call is 100% gratis en vrijblijvend. U ontvangt een schriftelijk advies en offerte en bepaalt zelf of en wanneer u wilt starten.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Moet ik technische kennis hebben om een discovery call bij LaunchStudio in te plannen?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Nee, de call richt zich op de werking en gebruikers van uw app; onze senior engineers onderzoeken de technische code zelfstandig."
      }
    },
    {
      "@type": "Question",
      "name": "Waarom kijkt LaunchStudio direct in de codebase in plaats van alleen af te gaan op de call?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Omdat directe code-inspectie verborgen AI-fouten opspoort en de basis vormt voor een onwrikbare, betrouwbare vaste prijsgarantie."
      }
    },
    {
      "@type": "Question",
      "name": "Wat als ik het antwoord op een technische vraag tijdens het gesprek niet weet?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Dat is volkomen prima en waardevol; het wijst onze engineers direct de weg naar de componenten die verificatie vereisen."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe snel na de discovery call ontvang ik de definitieve offerte?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Binnen 24 tot 48 uur na het gesprek ontvangt u een compleet schriftelijk voorstel met vaste prijs en doorlooptijd."
      }
    },
    {
      "@type": "Question",
      "name": "Verplicht de discovery call mij tot het afnemen van een pakket?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Nee, het intakegesprek is 100% gratis en vrijblijvend, zonder enige aankoopverplichting."
      }
    }
  ]
}
</script>
