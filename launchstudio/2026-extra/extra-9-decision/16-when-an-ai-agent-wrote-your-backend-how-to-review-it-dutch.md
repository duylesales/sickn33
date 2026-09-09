---
Titel: "Wanneer een AI-Agent Uw Backend Heeft Geschreven: Hoe Beoordeelt U Wat U Niet Kunt Lezen?"
Trefwoorden: AI gegenereerde backend reviewen, agentic coding review, AI code audit methode, vertrouwensgrens review, gehallucineerde dependencies, LaunchStudio, Manifera
Koperfase: Beslissing
Doelgroep: Technische Solo-Oprichter / Indie Hacker
---

# Wanneer een AI-Agent Uw Backend Heeft Geschreven: Hoe Beoordeelt U Wat U Niet Kunt Lezen?

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Wanneer een AI-Agent Uw Backend Heeft Geschreven: Hoe Beoordeelt U Wat U Niet Kunt Lezen?",
  "description": "Veertienduizend regels door een AI-agent gegenereerde backend-code regel voor regel doorlezen is geen realistisch plan. Dit is een gerichte reviewmethode in zes rondes die de specifieke weeffouten van agentic coding blootlegt.",
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
  "datePublished": "2027-01-15",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://launchstudio.eu/nl/blog/wanneer-een-ai-agent-uw-backend-heeft-geschreven-hoe-beoordeelt-u-wat-u-niet-kunt-lezen"
  }
}
</script>

Het is zaterdagochtend na de eindsprint waarin alles eindelijk begon te draaien. Eenenzestig programmabestanden in de map `server/`, ruim veertienduizend regels broncode, gegenereerd over negen promptsessies met een AI-agent verspreid over drie weken. U heeft alles zelf aangestuurd. U heeft elk plan formeel goedgekeurd. Maar als u eerlijk bent, heeft u hooguit een vijfde van de daadwerkelijk opgeleverde code gelezen — en dat vijfde deel betrof voornamelijk de stukken die vastliepen.

Nu staat u op het punt om betalende klanten toe te laten, en uw werkelijke positie voelt ongemakkelijk: u bent de formele eigenaar van een codebase die u niet zelf heeft geschreven en waarvoor u niet volledig kunt instaan. Alles van begin tot eind doorlezen is geen werkbaar plan; bij een aandachtig leestempo van dertig regels per minuut kost dat u acht uur lang de zwaarste vorm van concentratie, en aan het einde bent u het merendeel alweer vergeten. Diagonaal scannen is louter een schijnvertoning.

Wat wél werkt, is een reviewmethodiek die specifiek is ingericht rond de unieke faalmechanismen van agentic coding — faalmechanismen die wezenlijk verschillen van de fouten die menselijke junior ontwikkelaars maken. AI-agents leveren software op die lokaal volkomen logisch oogt, maar globaal inconsistent is: elk afzonderlijk bestand lijkt plausibel, elke functie doet ongeveer wat de functienaam belooft, maar de gevaarlijke risico's schuilen in de naden tussen de verschillende promptsessies. Hieronder vindt u een audit in zes gerichte rondes, waarbij elke ronde het inspectieoppervlak voor de volgende verkleint. Reserveer hiervoor één gefocuste werkdag.

## Ronde 1: Vind de vertrouwensgrens en teken deze uit op papier

Voordat u ook maar één regel code inhoudelijk leest, brengt u eerst het speelveld in kaart. Elke backend bezit een vertrouwensgrens (trust boundary): de scheidslijn waar niet-vertrouwde invoer van buitenaf verandert in vertrouwde interne data. Vrijwel elke ernstige kwetsbaarheid in AI-code bevindt zich op een punt waar die grens geruisloos is overschreden.

Breng elk extern toegangspunt in kaart — niet uit uw hoofd, maar met behulp van grep. Routedefinities, achtergrondwachtrijen, cron-jobs, webhook-ontvangers, websocket-handlers, server actions en GraphQL-resolvers:

```bash
rg -n "app\.(get|post|put|patch|delete)\(|router\.(get|post)|export async function (GET|POST|PUT|PATCH|DELETE)|@(Get|Post)\(" server/ app/ src/ --no-heading
```

Plaats de resultaten in een overzichtelijke tabel met vier kolommen: URL-pad, vereist-authenticatie?, geautoriseerd-waardoor?, schrijft-wat. Vul deze kolommen in door de code daadwerkelijk te bekijken, niet door aannames te doen. Dit overzicht kost u ongeveer veertig minuten en vormt het meest waardevolle document van uw hele audit: het transformeert "veertienduizend regels code" in "eenendertig toegangspunten, waarvan er elf nader onderzoek vereisen."

Twee categorieën springen direct in het oog: endpoints waarvan u het bestaan volstrekt vergeten was — een testroute, een seed-script of een beheerdershulpje uit sessie vier dat nooit is opgeruimd. En endpoints waar de kolom 'geautoriseerd-waardoor' leeg blijft omdat u de handler heeft bekeken en nog steeds niet kunt vaststellen wie er toegang heeft. Beide zijn directe auditbevindingen vóórdat u de code diepgaand heeft bestudeerd.

## Ronde 2: Traceer vier kritieke datastromen van begin tot eind

Lees nu daadwerkelijk code — maar uitsluitend langs vier specifieke paden, waarbij u de datastroom volgt in plaats van de mappenstructuur:

**Registratie (Sign-up).** Waar wordt het wachtwoord gehasht, met welk algoritme en met welke cost factor? Wordt het e-mailadres geverifieerd vóórdat het account bevoegdheden krijgt? Kan een bezoeker een veld `role` meesturen in de request body? Is er een snelheidslimiet (rate limit) actief? AI-modellen genereren stelselmatig een `users`-tabel met een kolom `role` en een database-insert die blindelings de volledige request body overneemt — `...req.body` — waardoor elke oplettende bezoeker zichzelf direct beheerder kan maken.

**Inloggen en sessiebeheer.** Wat zit er precies opgeslagen in het sessietoken of de cookie? Is het cryptografisch ondertekend met een geheim uit de serveromgeving, of met een hardcoded fallback-waarde zoals `'secret'` die de agent toevoegde om lokale tests te laten slagen? Zijn cookies gemarkeerd als `httpOnly`, `secure` en `sameSite`? Hoe maakt uitloggen een sessie ongeldig? Zoek met grep naar `jwt.sign` en inspecteer elke aanroep.

**Betalingsverkeer.** Volg het pad vanaf de aanroep naar de checkout tot het exacte moment waarop toegang wordt verleend. De enige vraag die telt: welk concreet feit zorgt ervoor dat de database een gebruiker als betalend markeert? Als het antwoord een browser-redirect betreft in plaats van een cryptografisch gevalideerde webhook van server naar server, dan heeft u uw meest urgente beveiligingslek te pakken.

**Verwijderen (Delete).** Neem de meest destructieve bewerking die uw platform biedt en traceer deze nauwkeurig. Wie mag dit endpoint aanroepen, welke gerelateerde data wordt gewist (cascade), en is dit herstelbaar? AI-agents zijn dol op `ON DELETE CASCADE` in SQL-definities, simpelweg omdat het foutmeldingen over database-constraints geruisloos oplost.

Het traceren van deze vier datastromen vergt circa anderhalf uur en dekt exact de processen af waar storingen onmiddellijk leiden tot financiële schade of dataverlies. Fouten in de overige onderdelen van de codebase veroorzaken doorgaans hooguit milde ergernis bij gebruikers.

## Ronde 3: Zoek met grep naar de typische patronen die AI-modellen onder druk produceren

Bepaalde codeconstructies ontstaan specifiek doordat een taalmodel een acuut obstakel in de promptsessie moest omzeilen. Het zijn de digitale vingerafdrukken van agentic coding:

```bash
rg -n "catch\s*\([^)]*\)\s*\{\s*\}" --type ts --type js          # ingeslikte foutmeldingen
rg -n "\|\|\s*['\"](secret|dev|changeme|test)" --type ts          # hardcoded fallbacks voor omgevingsvariabelen
rg -n "process\.env\.[A-Z_]+\s*\|\|" --type ts                    # hetzelfde patroon, algemener
rg -n "eslint-disable|@ts-ignore|@ts-expect-error|as any"         # onderdrukte type- en linterfouten
rg -n "SELECT .*\$\{|query\(\s*[\"'`].*\+\s*" --type ts           # handmatig samengestelde SQL-queries
rg -n "Access-Control-Allow-Origin.*\*"                           # veel te permissieve CORS-headers
rg -n "TODO|FIXME|for now|in production you would"                # openhartige bekentenissen van de agent
```

Die laatste categorie verdient speciale aandacht. AI-modellen plaatsen regelmatig een opmerking in de trant van: "In production, verify this signature" — waarna de code met commentaar en al rechtstreeks naar productie wordt gepusht. Zoeken op deze termen levert geregeld binnen enkele minuten serieuze kwetsbaarheden op, compleet voorzien van een door de agent zelf geschreven probleemanalyse.

Het patroon van ingeslikte fouten (lege catch-blocks) is het gevaarlijkst. Een leeg `catch`-blok rondom een webhook-handtekeningverificatie, een autorisatiecontrole of een databasetransactie verandert een acute fout in een geruisloos succes. En dat is exact de reden waarom een applicatie maandenlang fundamenteel onveilig kan draaien zonder dat er ooit een alarmbel afgaat.

## Ronde 4: Controleer of de lijst met afhankelijkheden reëel en noodzakelijk is

Open uw `package.json` en lees elke regel aandachtig door. Dit kost vier minuten en biedt de hoogste verhouding tussen tijdsbesteding en inzicht van dit hele proces.

Stel uzelf bij elk pakket de vraag: herinnert u zich bewust dat u voor deze bibliotheek heeft gekozen? Zo niet, verifieer dan of het pakket daadwerkelijk bestaat als een legitiem, actief onderhouden open-source project met substantiële downloadcijfers en een repository die ouder is dan uw eigen project. AI-modellen verzinnen soms plausibel klinkende bibliotheeknamen die niet bestaan, en aanvallers registreren tegenwoordig exact die namen op npm met kwaadaardige code. Een onbekende package met slechts tweehonderd wekelijkse downloads die twee maanden geleden voor het eerst is gepubliceerd, verdient direct diepgaand wantrouwen.

Kijk daarnaast naar redundantie: drie verschillende datumbibliotheken, twee HTTP-clients, twee validatietools, en zowel `bcrypt` als `argon2` geïnstalleerd terwijl er maar één wordt gebruikt. Er is technisch niets kapot, maar uw bundle is nodeloos zwaar en uw potentiële aanvalsoppervlak is opgehoopt doordat sessie zes geen weet had van de keuzes in sessie twee.

```bash
npm audit --omit=dev
npx depcheck
npm ls --depth=0
```

Verwijder wat nergens wordt geïmporteerd, consolideer duplicaten en zet versienummers vast.

## Ronde 5: Vraag de agent om toelichting, maar verifieer onafhankelijk

In deze ronde zet u het gereedschap in dat de code heeft geschreven — maar met grote terughoudendheid, want de uitleg van een AI-agent vormt waardevolle aanwijzingen, maar nooit een definitief bewijs.

Stel scherpe, geïsoleerde vragen in een verse sessie waarin de repository is ingeladen: *Geef een overzicht van elk endpoint dat een record opvraagt via een ID zonder te controleren of de aanvrager de eigenaar is.* *Waar wordt autorisatie afgedwongen in deze codebase, en gebeurt dat consistent over alle routes?* *Welke omgevingsvariabelen worden uitgelezen in code die naar de browser wordt gestuurd?* *Toon elke plek waar waarden uit de request body ongevalideerd naar de database worden geschreven.*

Beschouw de antwoorden als hypotheses. Elk genoemd punt moet u zelf in het bronbestand verifiëren. Een taalmodel dat wordt gevraagd zijn eigen werk te auditeren heeft een sterke neiging om geruststellende antwoorden te geven, of beschrijft vol overtuiging een controle die aanwezig was in een ander bestand uit een eerdere sessie die nu niet meer in de context staat.

De omgekeerde vraagstelling is aanzienlijk effectiever. Vraag niet "is dit veilig?", maar vraag: *"Schrijf een curl-commando waarmee een aanvaller dit endpoint kan misbruiken als de autorisatie ontbreekt."* Voer dat commando vervolgens zelf uit. Een AI-model is vele malen beter in het ontwerpen van een aanval dan in het objectief beoordelen van zijn eigen verdediging, en het levert u een concrete test op in plaats van een subjectieve mening.

## Ronde 6: Bewijs drie zaken met geautomatiseerde tests

Sluit af met onomstotelijk bewijs. Geen gigantische testsuite, maar drie gerichte tests die elk een aanname valideren die u tot nu toe slechts op goed geloof aannam:

**Isolatie tussen huurders (cross-tenant isolation).** Maak twee accounts aan, zorg dat een record toebehoort aan account B, en vraag dat record op met het authenticatietoken van account A op elk endpoint dat een ID accepteert. Automatiseer dit met een scriptje dat over de tabel uit Ronde 1 loopt. Dit brengt meer echte beveiligingslekken aan het licht dan welke andere activiteit dan ook; IDOR is de fout die AI-agents het meest consistent produceren, simpelweg omdat het model de record-ID in scope heeft en geen reden heeft om over eigenaarschap na te denken tenzij de prompt er specifiek om vroeg.

**Webhook-vervalsing.** Stuur een niet-ondertekend, handmatig samengesteld HTTP-verzoek naar uw webhook-endpoint. Dit moet gegarandeerd een status 4xx retourneren en nul database-aanpassingen doen. Stuur daarna een geldig bericht tweemaal achter elkaar en verifieer dat de tweede aanroep als duplicaat wordt genegeerd (idempotentie).

**Onbedoelde privilegeverhoging (mass assignment).** Verstuur een legitiem profiel-updateverzoek waaraan u handmatig `"role": "admin"` en `"credits": 999999` toevoegt. Lees het record daarna opnieuw uit. Is een van die beschermde velden gewijzigd? Dan heeft u een mass-assignment kwetsbaarheid te pakken — de meest voorkomende fout in door AI geschreven CRUD-operaties.

Drie gerichte tests, gerealiseerd binnen een uur, die voortaan permanent in uw CI/CD-pipeline draaien zodat ditzelfde type kwetsbaarheid in promptsessie tien niet opnieuw kan binnensluipen.

## Wat deze audit oplevert, en hoe u verdergaat

Aan het einde van één gerichte werkdag beschikt u over een sluitende toegangspuntentabel, een lijst met bevindingen gerangschikt op potentiële schade (blast radius) en drie onwrikbare regressietests. Dat levert u een professioneel verdedigbare positie op die grondiger is dan wat de meeste gefinancierde startups over hun eigen code weten.

De lastigere vraag is hoe u de aangetroffen gebreken oplost. Sommige punten zijn binnen twintig minuten verholpen. Andere zaken — zoals het consolideren van versnipperde autorisatie naar één centrale beleidslaag, het invoeren van gecontroleerde databasemigraties en het herstructureren van een betaalstroom die leunt op redirects — zijn structureel van aard. En dat is exact het type werkzaamheden waar AI-agents structureel tekortschieten, omdat het vereist dat het gehele systeem als één samenhangend geheel wordt overzien in plaats van bestand voor bestand.

Dat is het moment waarop oprichters een beroep doen op [LaunchStudio](https://launchstudio.eu/nl/): u behoudt uw eigen code en interface, een senior engineer die dagelijks AI-code auditeert lost de structurele knelpunten op, en alle gemaakte architectuurkeuzes worden helder gedocumenteerd zodat uw volgende promptsessie voortbouwt op duidelijke standaarden. Achter LaunchStudio staat [Manifera](https://www.manifera.com/services/custom-software-development/) met meer dan elf jaar ervaring in enterprise softwareontwikkeling — dezelfde hoogwaardige reviewdiscipline, toegepast op een doeltreffend traject van één tot drie weken tegen een vaste prijs.

Voer de zes rondes eerst zelfstandig uit. Blijkt uw lijst met bevindingen langer dan uw beschikbare tijd toelaat? Geef ons alleen-lezen toegang tot uw repository en wij leveren binnen één werkdag onze bevindingen aan — direct inhoudelijk, zonder vrijblijvende verkooppraatjes.

## Echt voorbeeld

### Eenendertig endpoints, waarvan er twee fataal hadden kunnen zijn

Wessel Duijn ontwikkelde met behulp van een agentic coding tool gedurende vijf weken Merkwacht: een monitoringdienst die vermeldingen van consumentenmerken op online fora en marktplaatsen registreert. Tijdens een besloten bètafase verkocht hij de dienst voor € 149 per maand aan zes marketingbureaus. Wessel is een vaardige softwareontwikkelaar; hij had elke promptsessie zelf geformuleerd en de plannen kritisch beoordeeld. Toch had hij hooguit 20% van de daadwerkelijk gegenereerde code gelezen.

Ronde 1 leverde eenendertig toegangspunten op, waarvan hij er vier in het geheel niet herkende. Daaronder bevond zich een route genaamd `/api/_debug/reindex` uit een vroege sessie, die een klant-ID accepteerde en direct een complete scrapingcyclus startte — volkomen onbeveiligd en uiterst kostbaar, aangezien elke run aanzienlijke bedragen aan proxy-kosten met zich meebracht. De geautomatiseerde isolatietest uit Ronde 6 bracht het tweede ernstige lek aan het licht: het export-endpoint voor merkvermeldingen filterde resultaten op basis van een los `clientId`-queryparameter in plaats van op de actieve gebruikerssessie. Hierdoor kon elk aangesloten bureau de volledige concurrentie-analyses van andere bureaus exporteren. De overige bevindingen waren regulier onderhoud: een leeg catch-blok rondom de Stripe-handtekeningverificatie, een JWT-geheim met een hardcoded fallback en twee vergeten datumbibliotheken.

**Resultaat:** Alle autorisatie werd gecentraliseerd in één uniforme `assertClientAccess`-laag die door alle eenendertig endpoints wordt aangeroepen, de niet-geauthenticeerde debug-route werd verwijderd, webhook-validatie werd strikt en idempotent ingericht, en een cross-tenant isolatietest werd permanent toegevoegd aan de CI-pipeline. Binnen vijf werkdagen was alles gereed, terwijl Wessel's frontend en zijn vertrouwde workflow met de AI-agent volledig behouden bleven.

> *"Dat debug-endpoint was voor mij de grootste schok. Ik was het niet vergeten — ik wist simpelweg niet dat het bestond. Het zat verstopt in een plan dat ik 's nachts om 01:00 uur in week één had goedgekeurd. Het stond al een maand live en kostte me ongemerkt handenvol proxy-credits."*
> — **Wessel Duijn, Oprichter, Merkwacht (Nijmegen)**

**Kosten & Doorlooptijd:** € 2.600 (Launch Ready Pakket) — live binnen 5 werkdagen.

---

## Veelgestelde Vragen

### Kan ik de AI-agent niet gewoon vragen om zijn eigen code te auditen en op dat rapport afgaan?

Gebruik de antwoorden van de agent uitsluitend als suggesties, niet als definitieve conclusies. Een taalmodel dat zijn eigen werk beoordeelt heeft een sterke neiging tot geruststellende formuleringen en beschrijft regelmatig controles die louter in eerdere sessies bestonden. Een aanzienlijk betrouwbaardere techniek is om de agent te vragen een concreet exploit-script of curl-commando te schrijven om een route aan te vallen, en dat vervolgens daadwerkelijk uit te voeren.

### Hoeveel tijd kost deze review in zes rondes voor een gemiddelde backend?

Ongeveer één geconcentreerde werkdag voor een codebase van tienduizend tot twintigduizend regels code: circa veertig minuten voor de toegangspuntentabel, anderhalf uur voor het traceren van de vier datastromen, een halfuur greppen, enkele minuten voor de dependencies, en de resterende tijd voor de gerichte agent-vragen en het schrijven van de drie tests. De benodigde tijd schaalt met het aantal toegangspunten, niet met het aantal regels code.

### Welke bevinding moet ik als eerste oplossen als alles even ernstig lijkt?

Sorteer bevindingen altijd op potentiële schade (blast radius) in plaats van op abstracte ernstlabels. Alles waardoor één klant toegang krijgt tot de gegevens van een andere klant (IDOR) heeft absolute topprioriteit. Daarna volgt alles wat gratis toegang verleent tot betaalde functionaliteit, gevolgd door onomkeerbaar dataverlies. Lege catch-blocks en overtollige bibliotheken zijn slordig, maar kosten u tijd in plaats van het vertrouwen van uw klanten.

### Is door AI gegenereerde backend-code slechter dan het werk van een menselijke junior ontwikkelaar?

Het is wezenlijk anders, niet per se slechter. Code van een AI-agent is per afzonderlijk bestand vaak eleganter en consistenter qua syntax dan het werk van een beginnend programmeur. De zwakte zit echter in de samenhang over meerdere bestanden heen, omdat opeenvolgende sessies geen actieve herinnering hebben aan eerdere architectuurconventies. De fouten clusteren zich in de naden van de applicatie, niet binnen individuele functies.

### Moet ik stoppen met het gebruik van AI-agents zodra mijn codebase in productie draait?

Beslist niet — maar de architectuurafspraken moeten zó expliciet in de codebase verankerd zijn dat het model ze vanzelf oppikt. Zodra autorisatie is ondergebracht in één duidelijke functie, de databasestructuur strikt via migraties verloopt en de CI-pipeline een isolatietest uitvoert, is de kans minimaal dat een nieuwe promptsessie ineens een afwijkend patroon introduceert. Het bestaande patroon is immers zichtbaar in elk bestand dat het model inleest.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Kan ik de AI-agent niet gewoon vragen om zijn eigen code te auditen en op dat rapport afgaan?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Gebruik agent-audits als aanwijzingen, niet als bewijs. Vraag het model liever om een curl-aanvalscommando te genereren en voer dat uit. Een AI is beter in het vinden van exploits dan in het objectief keuren van eigen code."
      }
    },
    {
      "@type": "Question",
      "name": "Hoeveel tijd kost deze review in zes rondes voor een gemiddelde backend?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Circa één werkdag voor 10.000 tot 20.000 regels: 40 minuten voor toegangspunten, 90 minuten voor datastromen, 30 minuten grep-checks, enkele minuten voor dependencies, en de rest voor tests."
      }
    },
    {
      "@type": "Question",
      "name": "Welke bevinding moet ik als eerste oplossen als alles even ernstig lijkt?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Prioriteer op potentiële impact: eerst cross-tenant datalekken (IDOR), daarna het omzeilen van betaalpoorten, en vervolgens onomkeerbaar dataverlies. Code-opschoning en dependencies komen daarna."
      }
    },
    {
      "@type": "Question",
      "name": "Is door AI gegenereerde backend-code slechter dan het werk van een menselijke junior ontwikkelaar?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Het is anders: lokaal per bestand vaak netter geschreven, maar globaal inconsistent omdat verschillende sessies eerdere architectuurconventies niet onthouden. De fouten zitten in de koppelingen."
      }
    },
    {
      "@type": "Question",
      "name": "Moet ik stoppen met het gebruik van AI-agents zodra mijn codebase in productie draait?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Nee. Zodra conventies rondom autorisatie, migraties en isolatietests expliciet zijn vastgelegd, zal de agent deze bestaande architectuurpatronen automatisch volgen in nieuwe promptsessies."
      }
    }
  ]
}
</script>
