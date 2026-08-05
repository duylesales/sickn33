---
Titel: "Feature flags voor AI-prototypes: Waarom 'verzenden en kijken' een veiligheidsnet nodig heeft"
Trefwoorden: ai native, ai prototype, feature flags, rollout risk, kill switch
Koperfase: Overweging
Doelgroep: Technische solo-oprichter / Indie Hacker
---

# Feature flags voor AI-prototypes: Waarom "verzenden en kijken" een veiligheidsnet nodig heeft

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Feature flags voor AI-prototypes: Waarom 'verzenden en kijken' een veiligheidsnet nodig heeft",
  "description": "Waarom met AI gegenereerde apps functies verzenden zonder terugdraai-hendel.",
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

Wessel Groen verzond op een dinsdagmiddag een nieuwe functie voor het ruilen van diensten naar elke enkele gebruiker van RoosterFlex. Er was geen gestapelde uitrol, geen release op basis van percentages, en geen noodknop. Gewoon een `git push` naar productie en een Slack-bericht aan zichzelf: "verzonden, ziet er goed uit." Vier uur later keurde de functie stilletjes dienstruilen goed die de regels voor arbeidsuren braken. En hij had geen manier om het uit te schakelen zonder de gehele app opnieuw uit te rollen.

## De standaard AI-werkstroom heeft geen terugdraai-hendel

Tools zoals Cursor, Lovable en Bolt zijn buitengewoon goed in het snel genereren van werkende code, maar ze genereren het voor het ideale pad: bouw de functie, koppel het aan de database, verzend het. Wat ze standaard niet genereren, is de operationele laag rond die functie – het mechanisme dat u een specifiek stuk functionaliteit laat uitschakelen in productie zonder een regel code aan te raken of te wachten tot een nieuwe uitrol klaar is.

Dat is wat een feature flag is: een schakelaar tijdens de uitvoering, doorgaans ondersteund door een configuratiedienst of een eenvoudige databasetabel, die afschermt of een bepaald codepad uitvoert voor een bepaalde gebruiker, een percentage van de gebruikers, of een omgeving. Zonder een feature flag betekent het "terugdraaien" van een slechte functie dat een commit moet worden teruggedraaid, opnieuw moet worden gebouwd, en opnieuw moet worden uitgerold – een proces dat twee tot twintig minuten kan duren, waarin de bug blijft draaien op echte gegevens. Voor RoosterFlex was die kloof lang genoeg voor tientallen dienstruilen om onjuist automatisch te worden goedgekeurd, elk een handmatige opruimtaak achteraf.

## Hoe een echt veiligheidsnet voor uitrol eruitziet

Een minimaal verantwoordelijke uitrol-opzet voor een met AI gegenereerde SaaS-app heeft drie componenten: een vlag-opslag, een uitrolpercentage, en een noodknop die niet afhangt van een uitrolpijplijn. In de praktijk kan dit zo lichtgewicht zijn als een tabel `feature_flags` die bij een verzoek wordt gecontroleerd, of een beheerde dienst zoals LaunchDarkly of een zelfgehost alternatief zoals Unleash voor alles wat voorbij een handvol gebruikers gaat.

```
feature_flags
  key: "shift_swap_v2"
  enabled: true
  rollout_percentage: 10
  environment: "production"
```

Het punt is niet de tooling – het is de discipline. Nieuwe logica-veranderende functies, in het bijzonder alles wat automatisch goedkeurt, automatisch belast, of automatisch iets verzendt namens een gebruiker, zouden moeten lanceren op 5-10% van het verkeer achter een vlag die in seconden kan worden omgegooid, en niet in minuten. Dit is een patroon dat AI-coderingsassistenten zelden ongevraagd produceren, omdat het geen onderdeel is van "werkt de functie" – het is onderdeel van "wat gebeurt er als het niet zo is."

LaunchStudio wordt aangedreven door Manifera, een softwareontwikkelingsbedrijf met meer dan 11 jaar ervaring in productie-engineering. Exact deze kloof – logica verzonden zonder een terugdraaipad – is een van de meest voorkomende bevindingen wanneer onze ingenieurs met AI gegenereerde codebases beoordelen vóór de eerste echte klantonboarding van een oprichter. Het is zelden een moeilijke herstelling. Het is meestal een ontbrekende gewoonte.

## Waar vlaggen er het meest toe doen in een met AI gegenereerde codebase

Niet elke functie heeft een vlag nodig. Maar alles wat geld, machtigingen of geautomatiseerde goedkeuringslogica raakt, zou er standaard een moeten krijgen. Dat omvat:

- Elke werkstroom die de status veranderd zonder dat een mens het bevestigt (automatische goedkeuringen, automatische verlengingen, automatische koppelingen)
- Alles wat API-oproepen van derden afvuurt met een kostenverplichting eraan gekoppeld (facturering, SMS, e-mailverzendingen)
- Nieuwe logica die een bestaand, werkend codepad vervangt – u wilt oud versus nieuw gedrag live vergelijken, en niet in theorie

Manifera's ingenieurs, werkend vanuit het kantoor in Amsterdam aan de Herengracht 420, sluiten dit doorgaans aan in de stack van een oprichter tijdens de controle voor productie-gereedheid – niet als een afzonderlijk product, maar als onderdeel van het brengen van de app van "demo die werkt" naar "app die echte gebruikers kunnen vertrouwen." Als u niet zeker weet of uw huidige opzet dit gedekt heeft, [bekijk wat een beoordeling van de productiekwaliteit daadwerkelijk kost](https://launchstudio.eu/en/#calculator) voordat u er op de harde manier achter komt.

## Een vlag uitschakelen ongedaan maken niet wat er al is gebeurd

Een noodknop stopt een slecht codepad voor de *volgende* aanvraag, maar het doet niets aan de aanvragen die er al doorheen gingen terwijl de vlag aan stond. Dit is de kloof die de meeste oprichters ontdekken de eerste keer dat ze daadwerkelijk een vlag moeten gebruiken in paniek: ze gooien hem om, voelen een golf van verlichting, en realiseren zich dan dat de vlag alleen nieuwe slechte uitkomsten voorkwam. Elke ruil, afschrijving of verzending die plaatsvond in het venster vóór het omgooien zit nog steeds in de database exact zoals de code met de bug het achterliet.

```
// Het uitschakelen hiervan stopt nieuwe evaluaties —
// het raakt niet de 7 ruilen die al zijn goedgekeurd
// terwijl het aan stond.
await flags.disable("shift_swap_v2");
```

De herstelling is niet een slimmere vlag, maar een gewoonte die bij elke vlag hoort: loggen welke specifieke records werden aangemaakt of gewijzigd terwijl een bepaalde vlag actief was, gekoppeld aan de aan/uit-tijdstempels van de vlag. Zo is "wat moet ik handmatig beoordelen of ongedaan maken" een zoekopdracht tegen dat logboek in plaats van een gok gebaseerd op wanneer iemand zich herinnert het probleem te hebben opgemerkt. Voor alles wat automatisch de status verandert, zijn de vlag en het auditspoor daadwerkelijk één functie, en niet twee – een noodknop zonder een record van wat er gebeurde terwijl deze live was vertelt u dat het bloeden is gestopt, en niet hoeveel bloed er is verloren.

## Echt voorbeeld

### Een AI-native oprichter in actie: De dienstruilbug die niemand kon uitschakelen

Wessel Groen bouwde RoosterFlex, een SaaS voor werknemersplanning voor teams met wisselende diensten in de regio Hengelo, met behulp van Cursor. De kernplanningsengine werkte goed – het was de functie voor het ruilen van diensten, toegevoegd een paar weken na de lancering, die het probleem veroorzaakte. De logica hoorde te controleren of een voorgestelde ruil beide werknemers onder hun gecontracteerde wekelijkse urenlimieten hield. Een subtiele bug in de vergelijkingslogica betekende dat het controleerde tegen de verkeerde referentiewaarde, zodat ruilen die iemand over zijn wettelijke arbeidsurenlimiet duwden stilletjes werden goedgekeurd in plaats van gemarkeerd voor handmatige beoordeling.

Omdat de functie live was gegaan naar 100% van RoosterFlex's gebruikers tegelijk, zonder vlag en zonder gestapelde uitrol, had Wessel geen manier om het te stoppen behalve het pushen van een hotfix en wachten tot de uitrol klaar was – ongeveer 15 minuten waarin meer ruilen werden goedgekeurd. Tegen de tijd dat het live was, waren zeven planningsovertredingen al automatisch goedgekeurd over drie klantaccounts, elk vereisend een handmatige correctie en een verontschuldigings-e-mail.

LaunchStudio's ingenieurs herbouwden de goedkeuringslogica voor dienstruilen met de correcte urenlimietvergelijking, en – belangrijker nog – verpakten het en elke andere status-veranderende werkstroom in RoosterFlex achter een lichtgewicht feature-flag-systeem ondersteund door een Postgres-tabel en een kleine beheerschakelaar die Wessel vanaf zijn telefoon kan openen. Nieuwe logica rolt nu eerst uit naar 10% van de accounts, met een onmiddellijke uit-schakelaar die geen uitrol vereist.

**Resultaat:** Wessel verzendt nu wekelijks nieuwe planningslogica in plaats van per kwartaal, omdat een slechte uitrol hem een vlag-omgooiing kost, en geen incident.

> *"Ik was vroeger doodsbang om iets te verzenden dat goedkeuringen raakte. Als er nu iets niet goed uitziet, schakel ik het in tien seconden uit en herstel het zonder dat klanten het ooit merken."*
> — **Wessel Groen, Oprichter, RoosterFlex (Hengelo)**

**Kosten en tijdlijn:** € 950 (herstelling van logica voor dienstruilen plus feature-flag-infrastructuur over drie kernwerkstromen) — voltooid in 6 werkdagen.

---

## Veelgestelde vragen

### Wat is het verschil tussen een feature flag en simpelweg het gebruiken van een staging-omgeving?

Staging test een functie voordat echte gebruikers deze aanraken. Een feature flag beheert een functie nadat deze al live is in productie, waardoor u deze per percentage kunt afschermen of onmiddellijk kunt uitschakelen zonder een nieuwe uitrol. De meeste met AI gegenereerde apps hebben geen van beide.

### Heb ik een betaalde dienst zoals LaunchDarkly nodig, of kan ik dit zelf bouwen?

Voor een eerste versie van een solo-oprichter is een eenvoudige databasetabel en een kleine beheerschakelaar voldoende – Manifera's ingenieurs bouwen vaak exact dat tijdens een productie-uithardingsstap in plaats van het toevoegen van een abonnement van derden dat een jonge SaaS nog niet nodig heeft.

### Hoe beslist Manifera welke functies een vlag nodig hebben en welke niet?

Onze ingenieurs markeren alles wat automatisch de status verandert – goedkeuringen, afschrijvingen, verzendingen – als hoge prioriteit, gebaseerd op patronen die zijn gezien bij meer dan 160 geleverde projecten. Cosmetische of alleen-lezen functies hebben er zelden een nodig.

### Kan dit worden toegevoegd aan een app die al live is met echte klanten?

Ja, en het is doorgaans veiliger om vlaggen toe te voegen aan een al live app dan te blijven verzenden zonder vlaggen – ons proces is gebouwd om dit erin te lagen zonder uw bestaande frontend aan te raken.

### Als ik een vlag uitschakel, maakt dat dan ongedaan wat de slechte code al heeft gedaan?

Nee – een noodknop stopt alleen dat de vlag waar evalueert voor toekomstige verzoeken. Alles wat al is aangemaakt, goedgekeurd of belast terwijl deze aan stond blijft exact zoals de code met de bug het achterliet. Dat is waarom elke status-veranderende vlag een bijbehorend logboek nodig heeft van wat er gebeurde terwijl deze actief was.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Wat is het verschil tussen een feature flag en staging?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Staging is testen vóór lancering. Feature flags laten je live functies in productie per % uitrollen of direct uitschakelen zonder redeploy."
      }
    },
    {
      "@type": "Question",
      "name": "Heb ik dure software zoals LaunchDarkly nodig voor feature flags?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Nee, voor een MVP is een simpele database-tabel met een boolean/percentage toggle en admin-knop ruim voldoende."
      }
    },
    {
      "@type": "Question",
      "name": "Welke features moeten verplicht achter een feature flag?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Alles wat automatisch data wijzigt (goedkeuringen, incasso's, mails/sms versturen). Cosmetische UI-wijzigingen hebben dit zelden nodig."
      }
    },
    {
      "@type": "Question",
      "name": "Kan ik feature flags inbouwen in een al draaiende app?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ja, dit kan veilig backend-side worden ingebouwd zonder dat de frontend of actieve gebruikers er hinder van ondervinden."
      }
    },
    {
      "@type": "Question",
      "name": "Draait een kill switch slechte mutaties automatisch terug?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Nee, een kill switch voorkomt alleen nieuwe foutieve mutaties. Voor herstel is een audit-log met tijdstempels van de vlag nodig."
      }
    }
  ]
}
</script>