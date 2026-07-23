---
Titel: "Feature Flags voor AI-prototypes: waarom 'Ship it and See' een vangnet nodig heeft"
Trefwoorden: ai native, ai prototype, feature flags, rollout risk, kill switch
Koperfase: Overweging
Doelgroep: Technische Solo-oprichter / Indie Hacker
---
# Functievlaggen voor AI-prototypes: waarom 'verzenden en zien' een vangnet nodig heeft

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Feature Flags voor AI-prototypes: waarom 'Ship it and See' een vangnet nodig heeft",
  "description": "Waarom door AI gegenereerde apps functies leveren zonder terugdraaihendel, en hoe functievlaggen en gefaseerde implementaties voorkomen dat een slechte implementatie een live incident wordt.",
  "author": {
    "@type": "Organization",
    "name": "LaunchStudio",
    "url": "https://launchstudio.eu/en/"
  },
  "publisher": {
    "@type": "Organization",
    "name": "Manifera",
    "url": "https://www.manifera.com"
  },
  "datePublished": "2026-07-22",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://launchstudio.eu/en/blog/feature-flags-ai-prototype-rollout-risk"
  }
}
</script>

Wessel Groen heeft op dinsdagmiddag een nieuwe shift-swap-functie naar elke gebruiker van RoosterFlex verzonden. Er was geen gefaseerde uitrol, geen op percentages gebaseerde release, geen kill switch. Gewoon een 'git-push' naar productie en een Slack-bericht aan zichzelf: "ingezet, ziet er goed uit." Vier uur later keurde de functie stilletjes ploegenwissels goed die in strijd waren met de regels voor arbeidsuren, en hij kon deze functie niet uitschakelen zonder de hele app opnieuw te implementeren.

## De standaard AI-workflow heeft geen terugdraaihendel

Tools als Cursor, Lovable en Bolt zijn buitengewoon goed in het snel genereren van werkende code, maar ze genereren deze voor de goede weg: de functie bouwen, naar de database sturen en verzenden. Wat ze niet standaard genereren is de operationele laag rond die functie: het mechanisme waarmee je een specifiek stuk functionaliteit in productie kunt uitschakelen zonder een regel code aan te raken of te wachten tot een nieuwe implementatie is voltooid.

Dat is wat een feature flag is: een runtime-switch, meestal ondersteund door een configuratieservice of een eenvoudige databasetabel, die bepaalt of een bepaald codepad wordt uitgevoerd voor een bepaalde gebruiker, percentage gebruikers of omgeving. Zonder deze betekent het 'terugdraaien' van een slechte functie het ongedaan maken van een commit, het opnieuw opbouwen en opnieuw inzetten - een proces dat tussen de twee en twintig minuten kan duren, waarbij de bug voortdurend tegen echte gegevens aanloopt. Voor RoosterFlex was die kloof lang genoeg om tientallen ploegenwissels automatisch ten onrechte te laten goedkeuren, waarbij elke taak daarna handmatig moest worden opgeschoond.

## Hoe een echt uitrolveiligheidsnet eruit ziet

Een minimaal verantwoorde implementatieconfiguratie voor een door AI gegenereerde SaaS-app bestaat uit drie componenten: een flagstore, een implementatiepercentage en een kill switch die niet afhankelijk is van een implementatiepijplijn. In de praktijk kan dit net zo licht zijn als een `feature_flags`-tabel die op verzoek wordt gecontroleerd, of een beheerde service zoals LaunchDarkly of een zelfgehost alternatief zoals Unleash voor alles behalve een handvol gebruikers.

```
feature_flags
  key: "shift_swap_v2"
  enabled: true
  rollout_percentage: 10
  environment: "production"
```

Het punt is niet de tooling, maar de discipline. Nieuwe logica-veranderende functies, vooral alles wat automatisch iets goedkeurt, in rekening brengt of automatisch namens een gebruiker iets verzendt, zou bij 5-10% van het verkeer moeten worden gelanceerd achter een vlag die binnen enkele seconden kan worden uitgezet, niet minuten. Dit is een patroon dat AI-codegeneratoren zelden ongevraagd produceren, omdat het geen deel uitmaakt van "werkt de functie" - het maakt deel uit van "wat er gebeurt als het niet werkt."

LaunchStudio wordt mogelijk gemaakt door Manifera, een softwareontwikkelingsbedrijf met meer dan 11 jaar ervaring in productie-engineering, en dit exacte hiaat (logica geleverd zonder rollback-pad) is een van de meest voorkomende bevindingen wanneer onze ingenieurs door AI gegenereerde codebases beoordelen voordat een oprichter voor het eerst een echte klant onboardt. Het is zelden een moeilijke oplossing. Het is meestal een ontbrekende gewoonte.

## Waar vlaggen het belangrijkst zijn in een door AI gegenereerde codebase

Niet elke functie heeft een vlag nodig. Maar alles wat met geld, machtigingen of geautomatiseerde goedkeuringslogica te maken heeft, zou er standaard een moeten krijgen. Dat omvat:

- Elke workflow die van status verandert zonder dat een mens dit bevestigt (automatische goedkeuringen, automatische verlengingen, automatische matching)
- Alles dat API-oproepen van derden activeert, waaraan kosten zijn verbonden (facturering, sms, e-mailverzending)
- Nieuwe logica die een bestaand, werkend codepad vervangt - je wilt oud en nieuw gedrag live vergelijken, niet in theorie

De technici van Manifera, werkzaam vanuit het Amsterdamse kantoor aan de Herengracht 420, koppelen dit doorgaans aan de stapel van een oprichter tijdens de productiegereedheidsfase – niet als een afzonderlijk product, maar als onderdeel van het krijgen van de app van 'demo die werkt' naar 'app die echte gebruikers kunnen vertrouwen'. Als u niet zeker weet of uw huidige installatie dit dekt, [kijk dan wat een beoordeling van de productiegereedheid daadwerkelijk kost](https://launchstudio.eu/en/#calculator) voordat u er op de harde manier achter komt.

## Echt voorbeeld

### Een AI-Native-oprichter in actie: de Shift-Swap-bug die niemand kon uitschakelen

Wessel Groen bouwde met Cursor RoosterFlex, een medewerker die SaaS inroostert voor ploegendiensten in de regio Hengelo. De kernplanningsengine werkte goed; het was de shift-swap-functie, die een paar weken na de lancering werd toegevoegd, die het probleem veroorzaakte. De logica was bedoeld om te controleren of een voorgestelde ruil beide werknemers binnen de afgesproken wekelijkse urenlimieten hield. Een subtiele bug in de vergelijkingslogica zorgde ervoor dat er werd getoetst aan de verkeerde referentiewaarde, zodat swaps die iemand over de wettelijke arbeidsurenlimiet heen duwden, stilzwijgend werden goedgekeurd in plaats van gemarkeerd voor handmatige beoordeling.

Omdat de functie in één keer live was gegaan naar 100% van de gebruikers van RoosterFlex, zonder vlag en zonder gefaseerde uitrol, had Wessel geen andere manier om deze te stoppen dan een hotfix te pushen en te wachten tot de implementatie was voltooid - ongeveer 15 minuten waarin steeds meer swaps werden goedgekeurd. Tegen de tijd dat het live ging, waren er al zeven planningsovertredingen automatisch goedgekeurd voor drie klantaccounts, die elk een handmatige correctie en een verontschuldigingsmail vereisten.

De technici van LaunchStudio hebben de goedkeuringslogica voor shift-swap opnieuw opgebouwd met de juiste uurlimietvergelijking, en – nog belangrijker – deze en elke andere statusveranderende workflow in RoosterFlex verpakt, achter een lichtgewicht feature flag-systeem, ondersteund door een Postgres-tabel en een kleine beheerdersschakelaar waartoe Wessel toegang heeft vanaf zijn telefoon. Nieuwe logica wordt nu als eerste uitgerold naar 10% van de accounts, met een onmiddellijke uitschakeling waarvoor geen implementatie vereist is.

**Resultaat:** Wessel verzendt nu wekelijks nieuwe planningslogica in plaats van elk kwartaal, omdat een slechte implementatie hem een ​​vlagwissel kost, en geen incident.

> *"Vroeger was ik doodsbang om iets te verzenden dat de goedkeuringen raakte. Als iets er nu niet uitziet, schakel ik het binnen tien seconden uit en repareer ik het zonder dat de klant het zelfs maar merkt."*
> — **Wessel Groen, Oprichter RoosterFlex (Hengelo)**

**Kosten en tijdlijn:** € 950 (shift-swap logica plus feature flag-infrastructuur voor drie kernworkflows) — voltooid in 6 werkdagen.

---

## Veelgestelde vragen

### Wat is het verschil tussen een feature flag en alleen het gebruik van een staging-omgeving?

Staging test een functie voordat echte gebruikers deze aanraken; een functievlag bestuurt een functie nadat deze al live in productie is, zodat je deze per percentage kunt afsluiten of direct kunt uitschakelen zonder een nieuwe implementatie. De meeste door AI gegenereerde apps hebben geen van beide.

### Heb ik een betaalde dienst zoals LaunchDarkly nodig, of kan ik deze zelf bouwen?

Voor de eerste versie van een solo-oprichter zijn een eenvoudige databasetabel en een kleine beheerdersschakelaar voldoende. De technici van Manifera bouwen vaak precies datgene tijdens een productiehardingsfase in plaats van een abonnement van derden toe te voegen dat een jonge SaaS nog niet nodig heeft.

### Hoe beslist Manifera welke functies een vlag nodig hebben en welke niet?

Onze technici markeren alles wat automatisch van status verandert – goedkeuringen, kosten, verzendingen – als hoge prioriteit, op basis van patronen die te zien zijn in meer dan 160 opgeleverde projecten; cosmetische of alleen-lezen-functies hebben er zelden een nodig.

### Kan dit worden toegevoegd aan een app die al live is bij echte klanten?

Ja, en het is meestal veiliger om vlaggen toe te voegen aan een app die al live is dan om zonder deze te blijven verzenden - [ons proces](https://launchstudio.eu/en/#process) is gebouwd om dit in lagen te verwerken zonder uw bestaande frontend te raken.

### Werkt LaunchStudio alleen met door Cursor gebouwde apps, of ook met andere AI-tools?

We werken met Lovable-, Bolt-, Cursor- en v0-output - de onderliggende kloof (geen uitrol vangnet) komt naar voren, ongeacht welke AI-tool de originele code heeft gegenereerd, wat consistent is met wat de technici van Manifera zien in hun bredere klantenbestand, waaronder Vodafone en CFLW.

Praat met een ingenieur die de door AI gegenereerde code begrijpt — [beschrijf hier uw project](https://launchstudio.eu/en/#contact) en we reageren binnen één werkdag.

Voor meer informatie over hoe Manifera builds op productieniveau benadert, zie [Manifera's diensten voor softwareontwikkeling op maat](https://www.manifera.com/services/custom-software-development/).

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What's the difference between a feature flag and just using a staging environment?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Staging tests a feature before real users touch it; a feature flag controls a feature after it's already live in production, letting you gate it by percentage or turn it off instantly without a new deploy. Most AI-generated apps have neither."
      }
    },
    {
      "@type": "Question",
      "name": "Do I need a paid service like LaunchDarkly, or can I build this myself?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "For a solo founder's first version, a simple database table and a small admin toggle is enough \u2014 Manifera's engineers often build exactly that during a production hardening pass rather than adding a third-party subscription a young SaaS doesn't need yet."
      }
    },
    {
      "@type": "Question",
      "name": "How does Manifera decide which features need a flag and which don't?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Our engineers flag anything that changes state automatically \u2014 approvals, charges, sends \u2014 as high priority, based on patterns seen across 160+ delivered projects; cosmetic or read-only features rarely need one."
      }
    },
    {
      "@type": "Question",
      "name": "Can this be added to an app that's already live with real customers?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes, and it's usually safer to add flags to an already-live app than to keep shipping without them \u2014 our process is built to layer this in without touching your existing frontend."
      }
    },
    {
      "@type": "Question",
      "name": "Does LaunchStudio only work with Cursor-built apps, or other AI tools too?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "We work across Lovable, Bolt, Cursor, and v0 output \u2014 the underlying gap shows up regardless of which AI tool generated the original code, consistent with what Manifera's engineers see across their broader client base including Vodafone and CFLW."
      }
    }
  ]
}
</script>