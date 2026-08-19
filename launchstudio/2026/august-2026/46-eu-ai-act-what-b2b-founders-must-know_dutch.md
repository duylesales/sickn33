---
Titel: "De Europese AI Act: Wat B2B-Founders Moeten Weten Vóór de Lancering"
Trefwoorden: AI security risico, AI privacy problemen, AI SaaS, AI-native, AI deployment, AI en softwareontwikkeling, LaunchStudio, Manifera
Koperfase: Bewustzijn
---

# De Europese AI Act: Wat B2B-Founders Moeten Weten Vóór de Lancering

Dacht u dat de AVG/GDPR al complex was? Bereid u dan voor op de Europese Artificial Intelligence Act (AI Act). Als 's werelds eerste alomvattende wetgevingskader voor kunstmatige intelligentie, gefaseerd van kracht tussen 2024 en 2027, bepaalt deze wet niet alleen hoe u met data omgaat; het dicteert exact wát u juridisch mag bouwen en hoe u de veiligheid moet aantonen vóórdat u lanceert. Heeft u klanten in Europa — of wordt de output van uw software binnen de EU gebruikt, ongeacht waar uw onderneming is gevestigd — dan moet u het getrapte risicomodel van de AI Act door en door kennen om verlammende boetes te voorkomen.

## De Risicogebaseerde Benadering

Het kenmerk van de Europese AI Act is dat de wet niet de onderliggende technologie reguleert, maar het specifieke **toepassingsgebied (use case)**. Een Large Language Model is op zichzelf niet illegaal, maar de wijze van inzet kan dat wél zijn — exact hetzelfde samenvattingsmodel valt onder "Minimaal Risico" wanneer het vergadernotities structureert, maar onder "Hoog Risico" wanneer het cv's van sollicitanten beoordeelt. De wet onderscheidt vier formele risicocategorieën:

## 1. Onaanvaardbaar Risico (Verboden Systemen)

Deze categorie systemen is categorisch verboden in de Europese Unie — er bestaat geen enkele compliance-route:
- **Social Scoring:** Het beoordelen of rangschikken van burgers op basis van sociaal gedrag of betrouwbaarheidsscores.
- **Subliminale Manipulatie:** AI-systemen die subliminale technieken inzetten om menselijk gedrag te manipuleren op een wijze die schade veroorzaakt.
- **Realtime Biometrische Identificatie:** Biometrische surveillance op afstand in openbare ruimtes door handhavingsinstanties (behoudens zeer strikte uitzonderingen).
- **Ongericht Scrapen van Gezichtsscans:** Het massaal schrapen van camerabeelden of online foto's om biometrische gezichtsherkenningsdatabases op te bouwen.

Boetes voor het exploiteren van verboden systemen kunnen oplopen tot maar liefst **€ 35 miljoen of 7% van de wereldwijde jaaromzet**.

## 2. Hoog Risico (Strikt Gereguleerd)

Hier lopen de meeste B2B softwarebedrijven tegenaan, vaak zonder het vooraf te beseffen. Een AI-systeem is "Hoog Risico" als het fungeert als veiligheidscomponent of valt binnen de domeinen van Annex III:
- **HR & Werving:** AI-software die cv's screent, sollicitanten rangschikt of automatische afwijzingen verstuurt.
- **Financiële Dienstverlening (FinTech):** AI die kredietwaardigheid berekent, leningen toekent of verzekeringspremies vaststelt.
- **Onderwijs (EdTech):** Algoritmes die examens beoordelen of toelating tot onderwijsinstellingen bepalen.
- **Essentiële Infrastructuur & Rechtshandhaving:** Systemen voor risicobeoordeling in justitiële contexten.

Bouwt u een Hoog Risico AI-systeem, dan bent u verplicht om:
1. Een doorlopend risicomanagementsysteem te hanteren over de gehele levenscyclus;
2. Trainingsdata te valideren op representativiteit en afwezigheid van vooroordelen (bias);
3. Volledige technische documentatie en automatische logging van elke AI-beslissing (Articles 11-12) bij te houden;
4. Een aantoonbare **Human-in-the-Loop (HITL)** in te richten: een menselijke medewerker met de bevoegdheid en context om algoritmes direct te overrulen;
5. Een formele conformiteitsbeoordeling (Conformity Assessment) te voltooien vóór marktintroductie.

## 3. Beperkt Risico (Transparantieverplichting)

De meeste standaard generatieve AI-applicaties (klantenservice-chatbots, marketing-copywriters, AI-beeldgeneratoren) vallen in deze categorie. De kernverplichting onder Artikel 50 luidt: **Transparantie**.

U moet gebruikers expliciet en direct informeren dat zij communiceren met een AI-systeem en niet met een mens. Bovendien moeten synthetische media (deepfakes, AI-gegenereerde audio of beeld) duidelijk en machinaal leesbaar gemarkeerd zijn als kunstmatig gegenereerd (conform C2PA-standaarden).

## 4. Minimaal Risico (Niet Gereguleerd)

Hieronder vallen AI-gestuurde spamfilters, videogames met AI-NPC's en voorraadoptimalisatie-algoritmes. Deze systemen mogen zonder aanvullende wettelijke beperkingen worden ontwikkeld en geëxploiteerd.

## General Purpose AI (GPAI) Modellen en Systemisch Risico

Bouwt u voort op grote basismodellen of ontwikkelt u zelf foundation models, dan gelden de specifieke regels voor "General Purpose AI" (Hoofdstuk V). Modellen die een rekenkracht-drempel overschrijden (circa 10^25 FLOPs tijdens training) worden aangemerkt als systemisch risicovol en moeten verplichte model-evaluaties, red-teaming en incidentrapportages aan het AI Office van de Europese Commissie overleggen.

## Risicoclassificatie is een Engineering-Vraagstuk, Geen Papieren Oefening

Het correct bepalen en inrichten van uw risicoclassificatie vereist een diepe analyse van uw software-architectuur en beslislogica. Dit is exact waar Manifera sinds **2014** in gespecialiseerd is, met 160+ gerealiseerde projecten voor opdrachtgevers zoals Vodafone en TNO vanuit haar Europese hoofdkantoor aan de Herengracht 420 in Amsterdam. Zoals Herre Roelevink, Oprichter & Managing Director van Manifera, stelt: "We zien een duidelijke verschuiving in softwarebehoeften. De uitdaging is niet langer om goede ideeën om te zetten in software. Het gaat nu om de architectuur en beveiliging die nodig zijn om die producten naar volwassenheid te brengen. Wij hebben elf jaar ervaring in exact dat vakgebied." Bekijk Manifera's [offshore softwareontwikkeling diensten](https://www.manifera.com/services/offshore-software-development/).

## Belangrijkste Inzichten

- De Europese AI Act is wereldwijd van toepassing op elke softwareontwikkelaar waarvan de AI-output binnen de Europese Unie wordt gebruikt.
- De wet reguleert het toepassingsgebied van de AI via vier risiconiveaus: Onaanvaardbaar, Hoog, Beperkt en Minimaal Risico.
- Hoog Risico AI (werving, kredietscores, onderwijs) vereist strenge technische logging, bias-testen en verplicht menselijk toezicht (Human-in-the-Loop).
- Generatieve AI valt doorgaans onder Beperkt Risico en verplicht heldere transparantie over AI-interacties en machinaal leesbare labels op synthetische media.
- Boetes voor overtredingen lopen op tot € 35 miljoen of 7% van de wereldwijde jaaromzet voor verboden AI-toepassingen.
- GPAI-modellen en fine-tuned open-source LLM's kunnen onderhevig zijn aan aanvullende transparantie- en evaluatieverplichtingen.

## Laat Uw AI-Systeem Auditen op AI Act Compliance

Bouwt u onbedoeld een 'Hoog Risico' systeem zonder verplichte documentatie? **LaunchStudio** voert technische en architectonische audits uit om te garanderen dat uw B2B SaaS voldoet aan alle transparantie-, logging- en toezichteisen van de Europese AI Act vóór uw marktintroductie. Bereken uw kosten via de [LaunchStudio prijscalculator](https://launchstudio.eu/en/#calculator).

LaunchStudio is een initiatief mogelijk gemaakt door **Manifera**, een internationaal softwareontwikkelingsbedrijf opgericht in **2014** door **Herre Roelevink**. Vanuit het inzicht in het tekort aan ervaren softwareontwikkelaars in Europa, richtte Herre ontwikkelingshubs op in **Singapore** (100 Tras Street #16-01, 100 AM) en **Ho Chi Minhstad, Vietnam** (Floor 11, Block C, 10 Pho Quang Street), om hoogwaardig engineeringtalent in te zetten. Geleid door de filosofie van het combineren van "Nederlands management met Vietnamees meesterschap", opereert Manifera haar Europese hoofdkantoor aan de **Herengracht 420, 1017 BZ Amsterdam, Nederland**. Via LaunchStudio krijgen AI-native oprichters direct toegang tot deze enterprise-grade software-expertise om hun prototypes binnen 1 tot 3 weken veilig, schaalbaar en lanceringsklaar te maken. [Vraag direct een offerte aan](https://launchstudio.eu/en/#contact).

## Echt voorbeeld

### Een AI-Native Oprichter in Actie: Audittrails voor Besluitvorming Bouwen voor een AI-Recruiter

Lincoln, oprichter van een HR-tech startup, gebruikte **Lovable** om een geautomatiseerde recruitment-app te bouwen. Omdat zijn software kandidaten automatisch filterde en rangschikte vóór menselijke review, viel de app direct onder de categorie Hoog Risico van de nieuwe Europese AI Act.

Hij schakelde **LaunchStudio (door Manifera)** in om geautomatiseerde databaseloggers in te richten die voor elke geëvalueerde kandidaat de AI-scoringscriteria, modelversies en beslisfactoren onveranderlijk vastlegden, inclusief een menselijk goedkeuringsscherm.

**Resultaat:** De applicatie voldeed volledig aan de documentatie- en toezichteisen van de AI Act, wat een succesvolle Europese expansie veiligstelde.

**Kosten & Tijdlijn:** €2.400 (AI Act Audit Trail Pakket) — productieklaar en binnen 6 werkdagen live opgeleverd.

---

## Veelgestelde Vragen

### Wat is de Europese AI Act?

's Werelds eerste allesomvattende wetgeving voor AI die verplichtingen en beperkingen oplegt op basis van het maatschappelijk risico van de specifieke AI-toepassing.

### Is de AI Act van toepassing op bedrijven buiten Europa?

Ja. Zodra een Amerikaans of Aziatisch bedrijf AI-diensten aanbiedt aan gebruikers in de EU, of de output binnen de EU wordt ingezet, is de wetgeving onverkort van kracht.

### Wat valt onder een 'Hoog Risico' AI-systeem?

AI-toepassingen die ingrijpen op essentiële levensgebieden: werving en selectie, krediet- en risicobeoordeling, toelating tot onderwijs en kritieke infrastructuur.

### Welke AI-toepassingen zijn categorisch verboden?

Social scoring door overheden of bedrijven, manipulatieve subliminale gedragsbeïnvloeding en het massaal schrapen van gezichtsafbeeldingen voor biometrische databases.

### Hoe ondersteunt LaunchStudio bij de AI Act?

LaunchStudio en Manifera auditen uw software-architectuur, bepalen uw exacte risicoklasse en bouwen de vereiste databaselogging, transparantielabels en Human-in-the-Loop workflows in.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Wat is de Europese AI Act?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Een Europees wetgevingskader dat AI-systemen classificeert en reguleert op basis van vier concrete risicocategorieën."
      }
    },
    {
      "@type": "Question",
      "name": "Is de AI Act van toepassing op bedrijven buiten Europa?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ja, de wet geldt wereldwijd zodra de software of de AI-output wordt gebruikt door personen of bedrijven binnen de EU."
      }
    },
    {
      "@type": "Question",
      "name": "Wat valt onder een 'Hoog Risico' AI-systeem?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "AI voor sollicitatieselectie, kredietbeoordeling, examencorrectie en risico-analyses in gereguleerde sectoren."
      }
    },
    {
      "@type": "Question",
      "name": "Welke AI-toepassingen zijn categorisch verboden?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Social scoring, subliminale gedragsmanipulatie en het ongericht schrapen van gezichten voor biometrische herkenning."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe ondersteunt LaunchStudio bij de AI Act?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "LaunchStudio bouwt de verplichte technische logging, transparantiedialogen en Human-in-the-Loop architecturen."
      }
    }
  ]
}
</script>
