---
Titel: "AI-Code naar Productie: Waarom 'Merge naar Main' Géén Releaseproces Is"
Trefwoorden: ai code naar productie, cursor deployment, releaseproces, stagingomgeving, ci/cd voor ai code, LaunchStudio, Manifera
Koperfase: Overweging
Doelgroep: Technische Solo-Oprichter / Indie Hacker
---

# AI-Code naar Productie: Waarom 'Merge naar Main' Géén Releaseproces Is

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "AI-Code naar Productie: Waarom 'Merge naar Main' Géén Releaseproces Is",
  "description": "Technische oprichters die Cursor gebruiken releasen AI-code vaak direct door naar main te pushen en de host automatisch te laten deployen. Dit artikel legt uit hoe een minimaal, volwaardig releaseproces eruitziet: checks, staging, migraties, rollbacks en wie de knop indrukt.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-10-03",
  "inLanguage": "nl-NL",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/ai-code-to-production-why-merge-to-main-is-not-a-release" }
}
</script>

Als u uw applicatie bouwt met Cursor, ziet uw releaseproces er waarschijnlijk zo uit: u accepteert de diff, werpt er een snelle blik op, maakt een commit, pusht naar `main`, en laat Vercel of Netlify de boel binnen een minuut automatisch uitrollen. Het voelt professioneel, want er is git en er draait een pipeline. Maar voor het overbrengen van AI-code naar productie is dit tevens een van de meest risicovolle werkwijzen die een solo-oprichter kan hanteren — niet omdat een afzonderlijke stap verkeerd is, maar omdat er tussen "het taalmodel heeft dit geschreven" en "klanten gebruiken dit nu" niets is ingebouwd dat 'nee' kan zeggen.

Dit is een praktische gids voor technische oprichters: wat een minimaal releaseproces daadwerkelijk vereist, waarom door AI gegenereerde code-diffs dit belangrijker maken in plaats van minder belangrijk, en hoe u dit inricht zonder een compact productteam te veranderen in een bureaucratische molen.

## Wat Automatisch Deployen Vanaf Main U Echt Oplevert

Automatisch deployen is een leveringsmechanisme, geen releaseproces. Het garandeert uitsluitend dat alles wat op de `main`-branch staat, razendsnel in productie belandt. Het zegt helemaal niets over de vraag of wát er op `main` staat daar überhaupt wel hoort te staan.

Bij handgeschreven code wordt dat gat deels opgevangen door het eigen begrip van de ontwikkelaar: u heeft elke regel zelf getypt, dus u weet bij benadering welke componenten worden geraakt. Bij code die door AI is geschreven, is het verschil (de diff) vaak aanzienlijk groter dan de wijziging waar u om vroeg. Vraagt u Cursor om een datumformaat op de factuurpagina te corrigeren, dan kan het zomaar zijn dat het model ook een helper-functie refactort die door vijf andere pagina's wordt gebruikt, een dependency update, of een databasequery aanpast "ter wille van de consistentie". De code ziet er plausibel uit, de tests die u heeft slagen (als u ze al heeft), en de onbedoelde neveneffecten belanden direct bij uw betalende klanten.

## De Vijf Sluizen Die AI-Code Nodig Heeft Vóór Productie

U heeft geen log corporate change-advisory board nodig. U heeft vijf sluizen (gates) nodig, die stuk voor stuk geautomatiseerd kunnen worden of teruggebracht kunnen worden tot een overzichtelijke checklist.

**Sluis 1: Geautomatiseerde controles bij elke push.** Type-checking, linting en alle bestaande tests draaien in CI (GitHub Actions volstaat uitstekend) op een afzonderlijke branch — niet direct op `main`. Falen de checks, dan wordt het samenvoegen (mergen) geblokkeerd. Dit vangt direct de klassieke AI-fout op waarbij code er logisch uitziet, maar verwijst naar een variabele of functie die elders al is hernoemd of gewist.

**Sluis 2: Een preview- of staging-deployment.** Elke branch wordt uitgerold naar een omgeving die identiek is aan productie maar het niet ís, gekoppeld aan een staging-database met fictieve of geanonimiseerde data. Daar klikt u de wijziging handmatig door. Vrijwel elk modern hostingplatform biedt gratis preview-deployments; het ontbrekende puzzelstukje is meestal de afzonderlijke database.

**Sluis 3: Databasemigraties als een aparte, handmatig beoordeelde stap.** Wijzigingen in het databaseschema mogen nooit geruisloos meeliften met een frontend-code deploy. AI-tools genereren zonder blikken of blozen een migratie die een kolom wist en opnieuw aanmaakt om het datatype te wijzigen. Op staging is dat hooguit onhandig; op productie wist het onherroepelijk uw klantdata.

**Sluis 4: Een rollback-procedure die u daadwerkelijk heeft uitgeprobeerd.** Uw hostingplatform kan een vorige build waarschijnlijk met één klik herstellen. De cruciale vraag is of dat nog steeds werkt nadat er een databasemigratie is uitgevoerd. Een rollback-plan dat de database negeert, is slechts een half plan.

**Sluis 5: Een mens die bewust besluit te releasen.** Zelfs voor een solo-oprichter moet de uiteindelijke merge naar `main` een bewuste handeling zijn, uitgevoerd op een verstandig tijdstip — niet om 23:40 uur op vrijdagavond omdat de diff er op het eerste gezicht goed uitzag.

## Waarom AI-Diffs Strengere Sluizen Vereisen, Niet Soepelere

Er heerst soms de intuïtie dat door AI gegenereerde code "vast wel in orde" is, omdat het model getraind is op gangbare patronen. Die gangbare patronen vormen nu juist het probleem. Het model genereert wat typisch is, en wat typisch is in openbare codebases omvat vaak te lakse CORS-instellingen, ontbrekende autorisatiechecks en try-catch-blokken die foutmeldingen geruisloos inslikken. Onderzoek dat LaunchStudio regelmatig aanhaalt, toont aan dat circa 45% van de door AI gegenereerde code kwetsbaarheden op het gebied van beveiliging bevat; u wilt niet dat uw releaseproces de plek is waar die statistiek in de praktijk op uw klanten wordt uitgetest.

Daarnaast is er een volume-effect. Een oprichter die met Cursor werkt, produceert vaak drie tot vier keer zoveel commits per week als met de hand. Meer wijzigingen betekent meer kans op regressies. De geautomatiseerde sluizen schalen moeiteloos mee met dat volume; uw menselijke concentratie doet dat niet.

## Staging Is Vooral een Dataprobleem

Technische oprichters zeggen geregeld dat ze "al een staging-omgeving hebben", omdat elke branch immers een preview-URL krijgt. Controleer echter goed waar die preview-URL zijn data vandaan haalt. In een verrassend groot deel van de codebases die LaunchStudio auditeert, wijzen preview-deployments rechtstreeks naar de productiedatabase, omdat de omgevingsvariabelen bij aanvang eenmalig zijn gekopieerd en nooit meer zijn gescheiden.

Dat betekent dat een testregistratie op een preview-branch een echte gebruiker aanmaakt in productie, dat een testbetaling met een verkeerde sleutel echte transacties kan triggeren via Stripe of Mollie, en dat een migratie die u "even wilde uitproberen" live klantdata raakt. Een staging-omgeving is pas écht staging als de data strikt gescheiden is. Supabase branching, een tweede Supabase-project of een aparte Postgres-instantie functioneren allemaal prima; het uitgangspunt is dat productie-inloggegevens nooit mogen voorkomen in niet-productieomgevingen.

## Rollbacks en de Valkuil van Migraties

Het meest voorkomende productie-incident dat LaunchStudio aantreft bij met Cursor gebouwde applicaties is geen applicatiecrash. Het is een zogeheten 'forward-only' migratie die niet zomaar kan worden teruggedraaid: een kolom die is hernoemd, een tabel die is geherstructureerd, of een standaardwaarde die is gewijzigd. De applicatiecode is binnen dertig seconden teruggedraaid naar de vorige versie; de datawijziging in de database niet.

De beproefde methodiek hiervoor is het 'expand-and-contract' patroon:

1. **Expand (Uitbreiden):** voeg de nieuwe kolom of tabel toe naast de bestaande structuur.
2. **Migrate (Migreren):** breng code naar productie die naar beide schrijft en leest uit de nieuwe structuur.
3. **Contract (Inkrimpen):** zodra alles stabiel draait, verwijdert u de oude kolom in een latere, afzonderlijke release.

Elke stap is op zichzelf veilig terug te draaien. Het vergt één extra deployment, maar het sluit het horrorscenario uit waarin code en database na een rollback niet meer met elkaar overeenstemmen. De [PostgreSQL-documentatie over ALTER TABLE](https://www.postgresql.org/docs/current/sql-altertable.html) is het lezen waard om te begrijpen welke bewerkingen tabellen tijdelijk blokkeren (locken) of volledig herschrijven.

## Een Release-Checklist Die U Direct Kunt Kopiëren

- Branch gepusht, CI staat op groen (TypeScript checks, linting, tests)
- Preview-omgeving uitgerold tegen staging-data, kerngebruikersstroom succesvol doorlopen
- Eventuele databasemigratie afzonderlijk beoordeeld en gemarkeerd als wel/niet direct omkeerbaar
- Indien niet direct omkeerbaar: handmatige back-up gemaakt direct vóór de release
- Uitrol uitgevoerd tijdens uren waarin u de applicatie nog minimaal 30 minuten actief kunt monitoren
- Foutopsporing (monitoring) gecontroleerd 30 minuten na livegang
- Duidelijke rollback-stappen genoteerd in de beschrijving van de pull request

Zodra dit een vaste routine is, kost het u hooguit tien minuten per release. De allereerste keer dat het een fatale uitval voorkomt, heeft het zijn waarde voor het hele jaar al bewezen.

## Een Minimale CI-Pipeline in de Praktijk

Praten over "sluizen" kan abstract klinken. Hieronder ziet u hoe een minimale CI-configuratie voor een met Cursor gebouwde Next.js- en Supabase-app eruitziet in GitHub Actions. Het is bewust beknopt gehouden — de essentie is dat het automatisch draait op elke pull request en het mergen fysiek blokkeert bij een fout:

```yaml
name: ci
on:
  pull_request:
    branches: [main]
jobs:
  checks:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with: { node-version: 20, cache: npm }
      - run: npm ci
      - run: npm run typecheck
      - run: npm run lint
      - run: npm test -- --run
      - name: Scan for secrets
        uses: gitleaks/gitleaks-action@v2
      - name: Flag destructive migrations
        run: |
          if grep -RinE "drop (table|column)|alter column .* type" supabase/migrations/; then
            echo "Destructieve migratie gevonden: vereist expliciete menselijke review"; exit 1
          fi
```

In combinatie met branch protection op GitHub — waarbij deze job verplicht moet slagen én uw eigen goedkeuring vereist is — kan AI-gegenereerde code de beveiliging niet meer omzeilen. Niet door een vermoeide oprichter om middernacht, en niet door een autonome agent.

De controle op migraties is bewust pragmatisch. Het verbiedt niet om een kolom te verwijderen; het dwingt af dat een mens er bewust naar kijkt. In de praktijk voegt u simpelweg een override-label of een opmerking toe aan de pull request voor doelbewuste destructieve aanpassingen, waarna de rest soepel doorloopt.

## Supabase-Migraties in de Praktijk

Voor Supabase-projecten verloopt de meest betrouwbare workflow via SQL-bestanden in de repository, toegepast via de Supabase CLI in plaats van via het online dashboard:

1. Voer de schemawijziging eerst lokaal of op een branch-database uit.
2. Genereer een migratiebestand met `supabase db diff` en lees dit aandachtig door — door AI gegenereerde diffs bevatten regelmatig meer wijzigingen dan u verwacht.
3. Commit de migratie in een eigen pull request, met een notitie over de omkeerbaarheid.
4. Pas de migratie via CI toe op staging en test de app grondig.
5. Maak een back-up (of controleer of point-in-time recovery actief is) en pas de migratie toe op productie.

De tabel-editor in het Supabase-dashboard is verleidelijk eenvoudig, maar elke aanpassing die daar handmatig wordt gedaan, is onzichtbaar voor uw git-historie en voor de volgende collega die staging probeert op te zetten. Vrijwel elk probleem waarbij "staging niet overeenkomt met productie" is terug te voeren op één handmatige dashboard-edit uit het verleden.

## Een Release Actief Volgen in Plaats van Hopen op Zegen

Een release is niet klaar op het moment dat het deployment-lampje op groen springt. Controleer in de eerste 30 minuten standaard drie zaken: de foutopsporing (Sentry/Logflare) op nieuwe typen fouten, de responstijden van uw twee drukste endpoints, en doorloop één complete kernstroom in productie als echte gebruiker. Ziet een van de drie er verdacht uit, draai de release dan direct terug en onderzoek het probleem pas daarna. De kosten van een onnodige rollback zijn enkele minuten; de kosten van 'live debuggen' terwijl klanten vastlopen zijn gigantisch. Na een paar weken is dit een routine die minder tijd kost dan het zetten van een kop koffie.

## Drie Reële Releasescenario's, Correct Aangepakt

**Een tekstwijziging.** Cursor past de prijzen en copy aan op de marketingpagina. CI slaagt, de preview ziet er strak uit, u merget overdag. Totale extra inspanning: twee minuten ten opzichte van direct naar `main` pushen. Het proces vertraagt triviale aanpassingen nauwelijks — en dat maakt het duurzaam vol te houden.

**Een nieuwe feature met een schemawijziging.** U introduceert de mogelijkheid om een lidmaatschap tijdelijk te pauzeren (zoals in het onderstaande praktijkvoorbeeld). De migratie gaat in een eigen pull request die uitsluitend een optionele (nullable) kolom en een nieuwe statuswaarde toevoegt, vooraf gereviewd en uitgerold. De featurecode volgt in een tweede pull request, bij voorkeur achter een feature flag. Bestaande rijen blijven onaangeroerd, en bij een eventuele rollback blijft de database 100% compatibel.

**Een urgente hotfix tijdens een live storing.** Betalingen lopen vast. De snelste veilige route is: rol direct terug naar de laatste stabiele deploy, bevestig dat betalingen weer binnenkomen, en ontwikkel de fix vervolgens rustig op een aparte branch met CI-dekking. Weersta de verleiding om "voor deze ene keer" direct in productiecode te sleutelen — tijdens incidenten richt ongevalideerde code traditioneel de grootste ravage aan.

## Tekenen Dat Uw Releaseproces Werkt

Na een maand merkt u direct resultaat: aanzienlijk minder "wat is hier zojuist veranderd?"-momenten, geautomatiseerde CI die af en toe een foute merge tegenhoudt (het bewijs dat het vangnet werkt), geen data-verrassingen na releases, en rollbacks die binnen enkele minuten geregeld zijn. Als CI overigens nóóit faalt, is uw code ofwel miraculeus perfect, of zijn uw controles te laks ingericht; meestal het laatste. Voeg eens een negatieve test toe voor de belangrijkste permissie in uw app en kijk of het systeem alarmslaat.

## Wanneer het Proces Eenvoudiger Mag Blijven

Niet elk project vereist vanaf dag één alle vijf de sluizen. Een statische marketingwebsite zonder database kan prima direct vanaf `main` deployen. Een interne tool voor vijf directe collega's kan voorlopig zonder preview-deployments. De sluizen worden echter onmisbaar zodra er sprake is van echte klantdata, online betalingen of contractuele uptime — en voor de meeste met AI gebouwde SaaS-applicaties is dat exact het moment waarop ze het waard zijn om gelanceerd te worden.

## Waar LaunchStudio U Ondersteunt

Voor technische oprichters is de rol van LaunchStudio meestal niet om uw features te schrijven. Onze rol is om het betrouwbare fundament onder uw AI-code naar productie-workflow te leggen: CI ingericht, staging strikt gescheiden, geheimen per omgeving beveiligd, migratiestromen gestroomlijnd en monitoring actief gekoppeld. De technische expertise hierachter is afkomstig van Manifera, dat al meer dan 11 jaar enterprise-kwaliteit levert aan innovatieve bedrijven van Amsterdam tot Singapore. U blijft uw code schrijven in Cursor zoals u gewend bent; het cruciale verschil is wat er voortaan tussen uw diff en uw betalende klanten staat.

Klinkt dit herkenbaar? [Spreek met een engineer die AI-code door en door begrijpt](https://launchstudio.eu/nl/#contact) — het eerste gesprek kost 15 minuten en levert u een vaste prijs en plan op. Manifera's bredere [web app development praktijk](https://www.manifera.com/services/web-app-develop/) hanteert exact dezelfde pipeline-patronen op grotere schaal.

## Praktijkvoorbeeld

### Een AI-Native Oprichter in Actie: De Boulderhal-App Die Zichzelf Offline Deployde

Daan Visser, voormalig data-analist in Delft, bouwde PlankPal met behulp van Cursor: een ledenadministratie- en incheck-app voor twee lokale boulderhallen. Leden scanden een QR-code bij de ingang; balievrijwilligers zagen direct de live bezetting en verlopende abonnementen. Daan pushte meerdere keren per dag naar `main`, waarna Vercel elke push automatisch uitrolde.

Op een donderdagavond vroeg Daan Cursor om een status voor "gepauzeerd lidmaatschap" toe te voegen. De gegenereerde databasemigratie zette de statuskolom om van platte tekst naar een ENUM-type, en herschreef daarbij per ongeluk alle bestaande rijen — waarbij alle statussen die de ENUM niet herkende automatisch op `NULL` werden gezet. De deployment duurde veertig seconden. Gedurende de twee uur daarna werden tientallen leden met een geldig abonnement bij de deur geweigerd, omdat het incheckscherm een lege status interpreteerde als verlopen. Het terugdraaien van de code hielp niet, want de database was immers al gewijzigd.

De engineers van LaunchStudio herstelden de beschadigde rijen direct via een point-in-time back-up en bouwden vervolgens een solide releaseproces rondom Daans workflow: GitHub Actions die type-checks en geautomatiseerde inchecktests uitvoeren op elke branch, een gescheiden Supabase staging-project met representatieve testdata, migraties ondergebracht in eigen gecontroleerde pull requests, en een verplichte rollback-instructie in elk PR-sjabloon. Foutopsporing werd gekoppeld aan Daans smartphone.

**Resultaat:** Gedurende de vier maanden daarna voerde PlankPal 212 succesvolle releases uit. De CI-pipeline blokkeerde in die periode negen keer een foute merge, waaronder twee databasemigraties die bestaande data overschreven zouden hebben. Er vond geen enkele incheckstoring meer plaats.

> *"Ik had een pipeline, dus ik dacht dat ik een releaseproces had. Wat ik werkelijk had, was een angstaanjagend snelle manier om alles wat Cursor bedacht linea recta naar productie te sturen."*
> — **Daan Visser, Oprichter, PlankPal (Delft)**

**Kosten & Tijdlijn:** €1.600 (inrichten release-pipeline, staging-scheiding, migratieworkflow en dataherstel) — opgeleverd in 6 werkdagen.

## Veelgestelde Vragen

### Is auto-deploy vanaf main altijd een slecht idee?

Niet altijd. Voor een statische marketingwebsite is het prima verdedigbaar. Het wordt pas riskant zodra uw applicatie beschikt over een database met echte klantgegevens en betalende gebruikers, omdat code- en datawijzigingen dan synchroon moeten worden gereleased en teruggedraaid.

### Hoeveel tests heeft een AI-app nodig voordat dit proces zinvol is?

Minder dan u denkt. Vijf tot tien gerichte tests die registratie, inloggen, de kernfunctionaliteit en het betalingsproces dekken, vangen het leeuwendeel van ernstige regressies af. Bovendien voert de CI-sluis ook TypeScript type-checks uit, wat al enorm veel AI-fouten automatisch tegenhoudt.

### Kan Cursor de CI-pipeline en tests niet gewoon voor mij schrijven?

Cursor kan zeker een prima startpunt genereren. Het risico is echter dat door AI geschreven tests vaak zoveel componenten 'mocken' dat ze altijd slagen, ongeacht het werkelijke gedrag van de app. Een ervaren engineer die controleert wat de tests daadwerkelijk bewijzen, levert hier direct rendement op.

### Wat voegt de ervaring van Manifera toe aan het releaseproces van een solo-oprichter?

Vooral patroonherkenning. De engineers van Manifera hebben in ruim 160 projecten exact gezien welke releasefouten tot echte incidenten leiden. Daardoor richten zij een minimaal, doelgericht proces in — zonder overbodige bureaucratie, maar met keiharde sluizen waar data of geld op het spel staan.

### Draagt een gedegen releaseproces bij aan online vindbaarheid en SEO?

Jazeker, indirect maar wezenlijk. Minder foutieve releases betekent minder momenten waarop zoekmachines en AI-crawlers op foutpagina's stuiten, minder verbroken links en consistentere laadtijden. Zowel traditionele zoekmachines als AI-antwoordmachines geven de voorkeur aan platforms met een hoge, betrouwbare uptime.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Is auto-deploy vanaf main altijd een slecht idee?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Nee, voor statische sites volstaat het prima. Het wordt pas gevaarlijk zodra een app een database met echte gebruikers en betalingen bevat, omdat code en data dan gezamenlijk moeten worden beheerd en teruggedraaid."
      }
    },
    {
      "@type": "Question",
      "name": "Hoeveel tests heeft een AI-app nodig voordat dit proces zinvol is?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Vijf tot tien gerichte tests voor inloggen, registratie, de kernfunctie en betalingen vangen de meeste regressies op. CI voert daarnaast type-checks uit die veel AI-fouten direct detecteren."
      }
    },
    {
      "@type": "Question",
      "name": "Kan Cursor de CI-pipeline en tests niet gewoon voor mij schrijven?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Het kan een opzet maken, maar AI-tests mocken vaak te veel waardoor ze altijd slagen. Een menselijke engineer die verifieert wat er echt getest wordt, voorkomt schijnzekerheid."
      }
    },
    {
      "@type": "Question",
      "name": "Wat voegt de ervaring van Manifera toe aan het releaseproces van een solo-oprichter?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Patroonherkenning uit 160+ projecten: een pragmatisch proces zonder bureaucratie, maar met waterdichte sluizen op data- en betalingsstromen."
      }
    },
    {
      "@type": "Question",
      "name": "Draagt een gedegen releaseproces bij aan online vindbaarheid en SEO?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Indirect wel. Minder foute releases voorkomt dat zoekmachinecrawlers foutpagina's tegenkomen en waarborgt uptime, wat zoekmachines en AI-systemen positief waarderen."
      }
    }
  ]
}
</script>
