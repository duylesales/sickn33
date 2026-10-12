---
Titel: "Lovable Beveiliging: De Dependencies Die Je Niet Zelf Hebt Gekozen"
Trefwoorden: lovable beveiliging, ai app beveiliging, kwetsbaarheden in packages, lockfile reproduceerbare build, supply chain kleine saas, LaunchStudio, Manifera
Koperfase: Overweging
Doelgroep: Technische Solo-Oprichter / Indie Hacker
---

# Lovable Beveiliging: De Dependencies Die Je Niet Zelf Hebt Gekozen

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Lovable Beveiliging: De Dependencies Die Je Niet Zelf Hebt Gekozen",
  "description": "AI-builders installeren namens jou talloze packages, waardoor een kleine app al snel op honderden bibliotheken leunt. Welke risico's daadwerkelijk reëel zijn, wat een lockfile beschermt en de maandelijkse updateroutine die de moeite waard is.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-07-26",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/lovable-security-dependencies-you-did-not-choose" }
}
</script>

Open de lijst met packages in een Lovable- of Bolt-project en begin te tellen. Een bescheiden webapplicatie — een handvol schermen, een invoerformulier, een grafiekje — leunt al snel op honderden verschillende packages (bibliotheken). Vrijwel geen daarvan heb je zelf uitgekozen, van de meeste heb je nog nooit gehoord, en ze draaien allemaal met exact dezelfde rechten als de code die je zelf hebt geschreven.

Dat is geen schandaal. Het is simpelweg hoe moderne softwareontwikkeling werkt, en hetzelfde geldt voor applicaties die volledig met de hand zijn geschreven. Het wezenlijke verschil bij met AI gebouwde software is dat niemand op enig moment heeft stilgestaan bij de vraag of een pakket wel strikt noodzakelijk was, actief wordt onderhouden, of betrouwbaar is — simpelweg omdat de AI-tool het pakket geruisloos toevoegde tijdens het oplossen van jouw prompt.

## Wat Er Namens Jou Wordt Geïnstalleerd

Vraag een AI-builder om een datumkiezer en hij installeert een complete datumlibrary. Vraag om een dashboardgrafiek en hij installeert een charting-pakket, dat op zijn beurt een render-utility installeert, die weer drie hulpbibliotheken meebrengt. Vraag om animaties, iconensets, formuliervalidatie of bestandsverwerking — elk afzonderlijk verzoek voegt één pakket toe waar je om vroeg, en een stuk of tien waar je nooit van had gehoord.

Die tweede groep noemen we *transitieve dependencies*, en in een gemiddeld project overtreffen ze je directe keuzes met een factor tien. Dat is tevens de plek waar vrijwel alle beveiligingsrisico's zich verschuilen, simpelweg omdat je er geen enkele relatie mee hebt: je hebt de naam nooit gelezen, nooit gecontroleerd of het pakket nog wordt onderhouden, en je zou het niet merken als het pakket stilletjes van eigenaar wisselt.

## Waarom Dit een Beveiligingsvraagstuk Is en Geen Schoonmaakklusje

Elke package in je dependency-boom voert code uit met de volledige bevoegdheden van jouw applicatie. Een gecompromitteerd pakket in je frontend kan stilletjes meekijken met wat gebruikers intikken. Een gecompromitteerd pakket in je servercode of edge function kan je omgevingsvariabelen uitlezen — precies de plek waar je geheime database-sleutels en API-tokens bewaard worden.

De reële dreigingen voor een startende SaaS-applicatie, op volgorde van waarschijnlijkheid:

**Bekende kwetsbaarheden in verouderde versies.** De overweldigende meerderheid van reële incidenten. Een library bevat een gedocumenteerd beveiligingslek, er bestaat al lang een patch voor, maar jouw project is nooit geüpdatet omdat niemand ernaar keek.

**Verlaten packages (abandonware).** Ooit gebouwd door één hobbyist die er drie jaar geleden mee is gestopt. Er komt geen beveiligingsupdate zodra er een lek wordt gevonden; het is een sluipende opeenstapeling van technisch risico.

**Typosquatting.** Een kwaadaardig pakket met een naam die één letter afwijkt van een populaire library, gepubliceerd om typefouten op te vangen. Dit is het punt waar het blindelings installeren door AI extra risico oplevert: een aannemelijk klinkende bibliotheeknaam is exact het lokmiddel dat aanvallers gebruiken.

**Gekortwiekte maintainer-accounts.** Zeldzaam, breed uitgemeten in het tech-nieuws, maar de reden dat de softwarewereld dit serieus neemt: een legitiem pakket publiceert ineens een gemanipuleerde versie, en iedereen die zonder vaste versienummers bouwt haalt de malware binnen.

Let op wat er níet in dit overzicht staat: een gerichte aanval waarbij criminelen specifiek jouw applicatie via een gerichte package proberen te hacken. Voor een Nederlandse B2B-startup is het werkelijke gevaar dat je verstrikt raakt in een willekeurige, geautomatiseerde scanner in plaats van doelwit te zijn van spionage.

## Wat een Bedrijf van Jouw Omvang Daadwerkelijk Moet Doen

Proportionaliteit is hier het sleutelwoord. Een oprichter met tweehonderd gebruikers heeft geen complex supply-chain securityprogramma nodig. De onderstaande beknopte maatregelen dekken de reële dreigingen ruimschoots af:

**Houd een lockfile bij, en commit die in Git.** Dit is met afstand de belangrijkste stap, en schrikbarend vaak ontbreekt deze in AI-gegenereerde projecten.

**Draai periodiek een audit-commando** en léés wat de output zegt, in plaats van blindelings te schrikken van het getal.

**Update gecontroleerd en volgens een vast schema,** in plaats van nooit of willekeurig continu.

**Weet wat je directe afhankelijkheden zijn** en verwijder pakketten die je niet meer gebruikt.

**Inspecteer wat de AI-agent nieuw voor je installeert,** vooral bij tools die autonoom packages mogen toevoegen zonder voorafgaande toestemming.

Dat is het complete programma. Eén uur onderhoud per maand, en je bent veiliger dan het leeuwendeel van je concurrenten.

## Waarom Lockfiles Belangrijker Zijn Dan de Audit Zelf

Een lockfile (`package-lock.json`, `pnpm-lock.yaml`, `yarn.lock`) legt de exacte, cryptografisch gevalideerde versie vast van elk afzonderlijk pakket — zowel direct als indirect — dat jouw project gebruikt. Zonder lockfile kan een build morgen totaal andere versies installeren dan een build vandaag, waardoor je productieomgeving stilletjes kan afwijken van wat je lokaal hebt getest, zonder dat iemand bewust code heeft gewijzigd.

Twee grote voordelen voor je beveiliging: een lockfile zorgt ervoor dat een gecompromitteerde nieuwe package-release nooit automatisch jouw productieomgeving binnensluipt — jij bepaalt zélf wanneer je upgradet. En wanneer er iets omvalt, is exact traceerbaar welke wijziging de oorzaak was.

Heeft je project geen lockfile in versiebeheer staan? Dat is je allereerste actiepunt, en het kost één minuut werk.

## Geautomatiseerde Updates: Nuttig Maar Vaak een Ruisbron

Tools zoals Dependabot of Renovate die automatisch een pull request openen zodra er een nieuwere package-versie beschikbaar is, zijn nuttig. Op standaardinstellingen zijn ze voor een solo-oprichter echter verlammend: een applicatie met honderden packages genereert sneller update-notificaties dan één mens kan verwerken, waardoor uiteindelijk álle meldingen genegeerd worden — inclusief die ene kritieke beveiligingsupdate.

De configuratie die wél werkt voor een compact team: beveiligingsupdates direct en afzonderlijk melden; alle overige functionele updates maandelijks in één gebundelde batch aanbieden; en patch-updates groeperen. Het doel is een minimaal aantal meldingen dat je daadwerkelijk leest en test.

## Beslissen of Je een Package Überhaupt Moet Toevoegen

Het allerbeste dependency-beheer is simpelweg zo min mogelijk toevoegen. Stel jezelf drie vragen vóórdat je een nieuw pakket accepteert, of het nu door de AI is voorgesteld of door jezelf:

**Heb ik echt een complete library nodig voor deze taak?** Een zware datumlibrary toevoegen puur om één tijdstempel te formatteren is een enorm risico-oppervlak voor een triviale taak; moderne JavaScript-functies lossen dit vaak native op.

**Wordt het pakket actief onderhouden?** Recente releases op GitHub/npm, openstaande issues die worden beantwoord, en meerdere actieve bijdragers.

**Hoeveel extra ballast sleept het mee?** Een package dat zelf veertig andere libraries installeert, zadelt jou op met veertig nieuwe potentiële kwetsbaarheden.

Wanneer een AI-tool voorstelt om een nieuw pakket te installeren, is dit hét moment om in te grijpen. De AI optimaliseert immers voor het direct oplossen van jouw prompt, niet voor de omvang en veiligheid van de codebase die hij achterlaat.

## De Audit Die Je Vandaag Kunt Uitvoeren

Open je project en voer het audit-commando van je package manager uit (`npm audit` of `pnpm audit`). Doe vervolgens wat de meesten overslaan: lées de details in plaats van in paniek te raken door het aantal meldingen.

Stel bij elke gemelde kwetsbaarheid twee nuchtere vragen: **Draait deze code daadwerkelijk in productie**, of betreft het een lokale build-tool die de browser van de gebruiker nooit bereikt? En **is het kwetsbare codepad iets wat mijn applicatie daadwerkelijk aanroept**? Een lek in een exotische functie die nergens in jouw code wordt gebruikt, vormt in de praktijk geen acuut gevaar.

Dit onderscheid is cruciaal: een ongefilterd audit-rapport toont op een gemiddeld project al snel tientallen waarschuwingen, wat leidt tot verlamming. Zodra je filtert op reële impact, blijven er bij de meeste projecten slechts een handvol punten over die daadwerkelijk aandacht vragen.

Inspecteer daarna je directe packages in `package.json` en verwijder alles wat overbodig is — projecten verzamelen vaak bibliotheken van eerdere experimenten en verwijderde schermen die stilletjes zijn blijven hangen.

## Wanneer een Melding Écht Urgent Is

Behandel als **acuut**: alles in code die op je productieserver draait, alles in je authenticatie- of betaalstroom, elke kwetsbaarheid die wordt omschreven als 'Remote Code Execution' (RCE), en alles in packages die bestandsuploads of gebruikersinvoer verwerken.

Behandel als **gepland onderhoud**: ontwikkeltools (dev-dependencies), lokale linters, en fouten in codepaden die jouw applicatie niet aanraakt.

Behandel als **ruis**: waarschuwingen over packages die je al hebt verwijderd of libraries waarvan je na analyse weet dat de kwetsbare functie nergens wordt aangeroepen.

Leg deze triage één keer vast in een korte notitie. Het verandert toekomstige security-audits van een stressmoment in een taak van tien minuten.

## Het Fundament Neerzetten

Voor de meeste met AI gebouwde SaaS-applicaties is dit een overzichtelijk traject dat daarna stabiel blijft: een lockfile vastgelegd in Git zodat builds reproduceerbaar zijn, alle packages geaudit en getriageerd op reële productie-impact, ongebruikte bibliotheken gesaneerd, geautomatiseerde updates ingesteld op nuttige signalen in plaats van ruis, en een duidelijke procedure voor toekomstige meldingen.

Dit vormt een vast onderdeel van het [Launch Ready pakket](https://launchstudio.eu/nl/#packages), uitgevoerd zonder de gebruikersinterface aan te raken die je in Lovable hebt gebouwd. De engineers zijn van Manifera: elf jaar ervaring in het onderhouden van productiesystemen voor opdrachtgevers als Vodafone, TNO en CFLW, vanuit Amsterdam en Ho Chi Minhstad, waar dependency-hygiëne een vaste dagelijkse discipline is.

Geeft jouw audit-commando een alarmerend getal dat je al weken voor je uitschuift? [Beschrijf je project](https://launchstudio.eu/nl/#contact) en we vertellen je exact welke punten er werkelijk toe doen, meestal binnen één werkdag.

## Frontend- versus Serverpackages: Twee Fundamenteel Andere Risico's

Een onderscheid dat het triageren vele malen eenvoudiger maakt, en dat standaard scanner-rapporten niet voor je maken:

**Een package die in de browser draait** voert code uit op het apparaat van de eindgebruiker, met toegang tot wat diegene op dat moment ziet en typt. Een beveiligingslek hier kan formuliersinvoer stelen of sessietokens in de pagina uitlezen. Het kan echter nooit bij je database-wachtwoorden, want die zijn daar simpelweg niet aanwezig.

**Een package die op je server of in een edge function draait** executeert met de volledige privileges van jouw backend. Een lek daar kan omgevingsvariabelen uitlezen — inclusief je Supabase master key, betaalgeheimen en AI-tokens — en namens jouw app kwaadaardige database-operaties uitvoeren.

**Build-time packages** draaien uitsluitend op de computer die de code compileert en belanden nooit bij de eindgebruiker. Een lek hier is een zorg voor grote concerns met gedeelde CI/CD-servers, maar verwaarloosbaar voor een solo-oprichter die lokaal bouwt.

De praktische vuistregel: wanneer een scanner vijftig problemen meldt, sorteer ze dan eerst op deze drie categorieën. Server-side packages los je direct op, browserpackages daarna, en build-tools behandel je als regulier onderhoud. Die ene sortering brengt een intimiderende lijst vrijwel altijd terug naar een behapbare middag werk.

## Echt voorbeeld

### Tweehonderd Waarschuwingen, Vier Die Er Werkelijk Toe Deden

Denise Kuiper runde Boekhoudmaat in Lovable: een gebruiksvriendelijke administratie-app voor circa 150 zzp'ers rond Utrecht en Amersfoort. De accountant van een potentiële zakelijke klant vroeg of zij haar softwarebibliotheken up-to-date hield, waarna ze voor het eerst in veertien maanden een audit uitvoerde.

Het rapport toonde meer dan tweehonderd beveiligingswaarschuwingen. Ze bracht een slapeloze avond door met het lezen over supply-chain hacks en trok de conclusie dat haar product één groot veiligheidsrisico was.

De technische intake bracht de realiteit binnen drie uur aan het licht. Ongeveer driekwart van de meldingen betrof build-tools die de server of browser van gebruikers nooit bereikten. Een ander deel zat in functies die haar app helemaal niet aanriep. Wat overbleef waren vier concrete kwetsbaarheden die er écht toe deden: een verouderde authenticatiehelper met een bekend lek, twee packages in de uploadmodule voor facturen, en een verlaten library voor het parsen van CSV-bestanden die al vier jaar niet was bijgewerkt.

Vier werkdagen werk: een lockfile vastgelegd in Git (aangezien die ontbrak en builds daardoor niet reproduceerbaar waren); de vier reële kwetsbaarheden verholpen, waarbij de verlaten library werd vervangen door een actieve standaard; 31 ongebruikte packages verwijderd die waren blijven hangen na eerdere tests; geautomatiseerde updates ingesteld zodat beveiligingslekken direct gemeld worden en de rest maandelijks wordt gebundeld; en een korte triagehandleiding opgesteld waarmee toekomstige rapporten in tien minuten te beoordelen zijn.

**Resultaat:** de vraag van de accountant werd beantwoord met een gedocumenteerd beleid, en de maandelijkse updatecontrole kost Denise sindsdien minder dan een kwartier, waarbij er in negen maanden tijd slechts twee beveiligingspatches hoefden te worden doorgevoerd.

> *"Die tweehonderd meldingen gaven me het gevoel dat mijn hele app van bordkarton was gemaakt. Vier ervan waren echt gevaarlijk, maar ik had geen schijn van kans om te zien welke vier dat waren zonder iemand die me liet zien waar ik moest kijken."*
> — **Denise Kuiper, Oprichter, Boekhoudmaat (Utrecht)**

**Kosten & Doorlooptijd:** € 1.450 (lockfile en reproduceerbare builds, triage, vier herstelacties, updateconfiguratie, gedocumenteerd triagebeleid) — afgerond in 4 werkdagen.

## Veelgestelde vragen

### Hoeveel afhankelijkheden (dependencies) heeft een gemiddelde AI-app?

Vaak honderden zodra je transitieve dependencies meetelt, met doorgaans tien indirecte bibliotheken voor elke directe package die je hebt gekozen. Dat is volkomen normaal in modern webdevelopment; het verschil is dat bij AI-bouw niemand vooraf heeft gecontroleerd of ze allemaal nodig waren.

### Wat is een lockfile en waarom is het cruciaal?

Een lockfile legt de exacte versies van alle gebruikte packages vast, waardoor builds 100% reproduceerbaar zijn en pas gepubliceerde (potentieel gecompromitteerde) versies niet automatisch binnensluipen. Een ontbrekende lockfile in Git is het allereerste wat je moet herstellen.

### Mijn audit-tool meldt honderden kwetsbaarheden. Is mijn app onveilig?

Meestal niet in die mate. Het leeuwendeel van de meldingen betreft build-tools die nooit in productie draaien, of functies die jouw applicatie niet gebruikt. Triageer altijd door te vragen of de code in productie draait en of jouw software het kwetsbare pad daadwerkelijk aanroept.

### Moet ik geautomatiseerde dependency-updates inschakelen?

Ja, mits zorgvuldig geconfigureerd. Op standaardinstellingen produceert een project zoveel pull requests dat je ze niet meer kunt bijhouden en uiteindelijk alles negeert. Stel het zo in dat security-updates direct binnenkomen en reguliere updates maandelijks worden gebundeld.

### Hoe voorkom ik dat een AI-builder onnodige packages toevoegt?

Grijp direct in zodra de tool een nieuwe library voorstelt: vraag of de complete bibliotheek echt nodig is voor deze specifieke taak, of deze actief wordt onderhouden, en hoeveel extra packages er meekomen. De AI optimaliseert voor jouw directe prompt, niet voor een slanke en veilige codebase.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Hoeveel afhankelijkheden (dependencies) heeft een gemiddelde AI-app?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Vaak honderden via transitieve dependencies, circa tien indirecte voor elke directe package — normaal voor modern web, maar ongecontroleerd bij AI-bouw."
      }
    },
    {
      "@type": "Question",
      "name": "Wat is een lockfile en waarom is het cruciaal?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Het legt exacte versies vast zodat builds reproduceerbaar zijn en nieuwe versies niet automatisch binnensluipen; ontbreken in Git is prioriteit één."
      }
    },
    {
      "@type": "Question",
      "name": "Mijn audit-tool meldt honderden kwetsbaarheden. Is mijn app onveilig?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Meestal niet in die mate: veel meldingen betreffen build-tools of niet-gebruikte codepaden. Triageer op productiegebruik en bereikbaarheid."
      }
    },
    {
      "@type": "Question",
      "name": "Moet ik geautomatiseerde dependency-updates inschakelen?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ja, mits goed ingesteld: security-updates direct en apart melden, overige updates maandelijks bundelen om waarschuwingsmoeheid te voorkomen."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe voorkom ik dat een AI-builder onnodige packages toevoegt?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Grijp in bij voorstellen: vraag of de hele library nodig is, of hij onderhouden wordt en hoeveel extra ballast hij meebrengt."
      }
    }
  ]
}
</script>
