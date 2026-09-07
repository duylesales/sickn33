---
Titel: "U Bent Tussentijds Overgestapt van Bolt Naar Cursor: Wat Dat Kost Bij de Lancering"
Trefwoorden: Bolt naar Cursor migratie, kosten overstap AI tools, verweesde configuratie lancering, dubbele omgevingsvariabelen, AI codebase archeologie, LaunchStudio, Manifera
Koperfase: Beslissing
Doelgroep: Technische Solo-Oprichter / Indie Hacker
---

# U Bent Tussentijds Overgestapt van Bolt Naar Cursor: Wat Dat Kost Bij de Lancering

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "U Bent Tussentijds Overgestapt van Bolt Naar Cursor: Wat Dat Kost Bij de Lancering",
  "description": "Het exporteren van een Bolt-project naar een lokale repository om door te bouwen in Cursor is een uitstekende beslissing. Het laat echter zeven specifieke soorten technisch puin achter. Een overzicht van de risico's en hoe u ze oplost.",
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
  "datePublished": "2027-01-22",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://launchstudio.eu/nl/blog/u-bent-tussentijds-overgestapt-van-bolt-naar-cursor-wat-dat-kost-bij-de-lancering"
  }
}
</script>

Twee git-commits, vijf weken uit elkaar. De eerste luidt `initial commit` en bevat vierentachtig programmabestanden waarvan u er niet één zelf heeft getypt. De tweede commit, van gisteravond laat, luidt `fix org invite flow` en is de vierhonderdste in een lange reeks van gewoon, noest programmeerwerk.

Alles tussen die twee commits vertelt het verhaal van een gezonde strategische keuze. Bolt bezorgde u binnen één weekend een werkende full-stack applicatie; op het moment dat het prompten omslachtiger werd dan zelf regels code intypen, exporteerde u het project naar een lokale git-repository en schakelde u over naar Cursor. Dat is exact de juiste volgorde, en vrijwel elke oprichter die daadwerkelijk een product lanceert volgt een variant van dit pad.

Maar die overstap brengt kosten met zich mee. En die rekening wordt niet voldaan op het moment van overstappen — hij wordt gepresenteerd bij de lancering, in de vorm van technisch achterstallig puin waar geen van beide tools zich verantwoordelijk voor voelt. Bolt weet niet dat u vertrokken bent. Cursor heeft geen idee wat er vóór zijn komst is gebeurd. Hieronder vindt u de gespecificeerde rekening: zeven categorieën van achtergebleven residu, wat elk risico u daadwerkelijk kost, en hoeveel tijd er nodig is om het definitief op te ruimen.

## Post 1: Git-historie die pas begint bij het interessante deel

Een `initial commit` met vierentachtig bestanden tegelijk is geen historie. Het is een momentopname waarbij alles wat eraan voorafging geruisloos is gewist.

De praktische schade manifesteert zich op de dag dat u `git bisect` nodig heeft — een functionaliteit vertoont al wekenlang subtiele fouten en u wilt achterhalen welke specifieke commit dit heeft geïntroduceerd. Als de oorzaak zich bevindt in de oorspronkelijke vierentachtig geïmporteerde bestanden, botst bisect tegen een blinde muur en meldt dat de fout er "altijd al in zat". Dat klopt feitelijk, maar helpt u niets verder. Hetzelfde geldt voor `git blame`: elke regel van de initiële opzet staat op uw naam, op één datum, zonder enige context of beweegreden.

U kunt de verloren git-historie niet terughalen. Wat u wél binnen twintig minuten kunt doen, is de oorsprong formeel documenteren: voeg een bestand `docs/ORIGINS.md` toe waarin u vastlegt welke tool de basis heeft gegenereerd, op welke datum, welke frameworkversies zijn geselecteerd, en welke architectuurbeslissingen aantoonbaar door Bolt zijn genomen in plaats van door uzelf. Dit klinkt wellicht bureaucratisch, totdat een freelance ontwikkelaar, een potentiële technische medeoprichter of een due-diligence team van een overnemende partij vraagt waarom er voor een specifieke bibliotheek is gekozen en niemand het antwoord weet.

**Kosten bij verwaarlozing:** urenlang verwarrend speurwerk op het slechtst denkbare moment. **Kosten om op te lossen:** 20 minuten.

## Post 2: Twee actieve deployment-targets die allebei live staan

Dit is de categorie die in de praktijk tot acute beveiligingsincidenten leidt.

Bolt implementeert met één muisklik naar Netlify. Toen u overstapte naar Cursor en uw code naar GitHub pushte, koppelde u hoogstwaarschijnlijk Vercel aan, simpelweg omdat dat uw vertrouwde platform is. Niemand heeft echter ooit de Netlify-koppeling ontkoppeld. Die staat nog altijd vrolijk builds uit te voeren bij elke push naar de oude branch, serveert nog altijd een actieve URL, en die URL zwerft wellicht nog rond in een Slack-bericht, een e-mail naar een investeerder of uw eigen bladwijzers.

Het milde faalscenario is dat een klant of prospect per ongeluk de verouderde URL gebruikt en een bug rapporteert die u weken geleden al heeft opgelost. Het ernstige scenario is dat die verouderde deployment nog altijd verbonden is met uw actuele productiedatabase en daar oude code op uitvoert. Dat is geen communicatieprobleem meer, maar een acute bedreiging voor uw data-integriteit.

Voer een gerichte audit uit: log in op Netlify, Vercel, Cloudflare Pages en elke andere hostingprovider die u ooit heeft geraadpleegd. Maak een lijst van alle sites die nog aan deze repository gekoppeld staan en verwijder alles wat u niet actief gebruikt. Controleer daarnaast uw DNS-records op vergeten subdomeinen die naar oude omgevingen verwijzen.

**Kosten bij verwaarlozing:** een verloren werkdag, of een ernstig data-incident. **Kosten om op te lossen:** 30 minuten.

## Post 3: Omgevingsvariabelen gedefinieerd op drie plekken, die nergens overeenstemmen

Tegen de tijd dat de overstap is afgerond, bestaat dezelfde omgevingsvariabele doorgaans op vier verschillende locaties: in de configuratie van Bolt, op de Netlify-site, in het Vercel-project en in uw lokale `.env`-bestand. Deze waarden gaan onvermijdelijk uit elkaar lopen. De klassieke misser is een Stripe-sleutel die op de ene plek op `sk_test_` staat en op de andere op `sk_live_`. Het gevolg: testtransacties in productie, of nog veel erger, daadwerkelijke creditcardafschrijvingen vanuit een testomgeving.

Daarnaast is er een subtielere valkuil: de naamgevingsconventies van Bolt wijken vaak af van wat u zelf in Cursor kiest. Zo ontstaat er een situatie waarin `VITE_SUPABASE_URL` uit de oorspronkelijke Bolt-scaffold overleeft, terwijl u in latere code `NEXT_PUBLIC_SUPABASE_URL` introduceert. Beide variabelen worden tijdens runtime uitgelezen, beide zijn gedefinieerd, maar ze wijzen mogelijk naar twee volstrekt verschillende databases. En een variabele die op de ene plek hernoemd is terwijl de oude naam elders overleeft, fungeert als een fallback die geruisloos verouderde waarden blijft serveren.

Stel één gezaghebbende lijst op: een gecommit `.env.example`-bestand dat elke variabele opsomt die de applicatie uitleest, voorzien van een korte toelichting per regel en zónder de geheime waarden zelf. Synchroniseer elke live omgeving met dit voorbeeldbestand en verwijder variabelen die niet op de lijst voorkomen. Controleer tevens via grep of er geen geheimen zijn voorzien van een publiek client-voorvoegsel — de export vanuit Bolt is exact het moment waarop die fout permanent bevroren raakt.

**Kosten bij verwaarlozing:** van een falende deployment tot foutieve creditcardincasso's. **Kosten om op te lossen:** 1 tot 2 uur.

## Post 4: Een Supabase-project met twee generaties aan databasestructuren

Bolt heeft destijds uw tabellen aangemaakt en waarschijnlijk een aantal basale RLS-policies geconfigureerd. Cursor genereerde vervolgens migratiebestanden — maar omdat de tabellen lokaal al bestonden, werden de vroege migraties overgeslagen, handmatig aangepast of uitgevoerd tegen een database die niet overeenkwam met de aannames van het migratiescript.

Het resultaat is een live database die restanten van beide tijdperken bevat: een tabel `profiles` uit de Bolt-fase en een tabel `users` uit de Cursor-periode, beide gedeeltelijk gevuld met data. RLS-policies uit de Bolt-fase die nooit zijn herzien nadat de onderliggende datastructuur veranderde — zoals een beleidsregel die verwijst naar een kolom die inmiddels is verwijderd, of een regel die filtert op `user_id` op een tabel die inmiddels is omgebouwd naar `org_id`. Twee van dit soort conflicten kunnen ertoe leiden dat tabellen *wagenwijd openstaan*: een policy waarvan de voorwaarde nergens meer op matcht, kan afhankelijk van de formulering permissief falen en iedereen toegang geven.

Voer een grondige diff uit en inspecteer de werkelijkheid:

```bash
supabase db diff --linked
```

Lees vervolgens elk actief beveiligingsbeleid rechtstreeks uit de database uit:

```sql
select tablename, policyname, cmd, qual, with_check from pg_policies where schemaname='public';
select relname, relrowsecurity from pg_class where relnamespace='public'::regnamespace and relkind='r';
```

Elke tabel met uitgeschakelde RLS, elke beleidsregel met een `qual` van `true`, en elke policy die verwijst naar een niet-bestaande kolom is een directe bevinding. De vereiste eindstaat is een samengevoegde (squashed) baseline-migratie die exact overeenkomt met productie, waarna alle toekomstige wijzigingen strikt via versiebeheer verlopen.

**Kosten bij verwaarlozing:** de meest waarschijnlijke bron van een acuut datalek in een gemigreerde codebase. **Kosten om op te lossen:** een halve werkdag.

## Post 5: Dependencies bevroren op het moment van export

Bolt heeft versies van bibliotheken vastgepind die actueel waren op de specifieke dag dat uw project werd gegenereerd, en afgestemd op wat binnen een browser-gebaseerde WebContainer kan draaien. Dat brengt twee concrete nadelen met zich mee.

Ten eerste staat de tijd niet stil: sommige van die vastgepinde versies bevatten inmiddels bekende kwetsbaarheden. Een commando zoals `npm audit --omit=dev` toont dit binnen enkele seconden. Ten tweede, en veel minder voor de hand liggend: WebContainer kan geen native Node-addons uitvoeren. Bolt heeft daardoor doelbewust om native bibliotheken heen gewerkt. Als uw applicatie afbeeldingen verwerkt, PDF-documenten genereert of geavanceerde cryptografie toepast, maakt u mogelijk gebruik van trage, pure-JavaScript alternatieven die puur zijn geselecteerd vanwege de browser-sandbox. Dat is niet per se fout, maar het is een keuze die vóór u is gemaakt om redenen die nu niet meer gelden.

Voeg daar de onvermijdelijke duplicatie aan toe: Bolt installeerde de ene datumtool, u greep in Cursor naar een andere, en nu zitten ze er allebei in. Met `npx depcheck` en `npm ls --depth=0` lost u deze wildgroei binnen een middag op.

**Kosten bij verwaarlozing:** trage performance en vermijdbare beveiligingsrisico's. **Kosten om op te lossen:** 2 tot 3 uur.

## Post 6: Twee stijlen voor dezelfde taak, zonder duidelijke winnaar

Door Bolt gegenereerde code bezit een specifieke huisstijl: de manier waarop data wordt opgehaald, hoe fouten worden afgehandeld en hoe API-antwoorden worden gestructureerd. Uw handgeschreven code in Cursor heeft uw eigen voorkeuren. Beide stijlen zijn gelijktijdig aanwezig. En Cursor — dat telkens het geopende bestand als context inleest — bouwt vrolijk voort op het patroon dat het toevallig in dat specifieke bestand aantreft. Hierdoor raakt de tweedeling definitief verankerd.

Concreet treft u aan: twee manieren om uw eigen backend aan te roepen, twee verschillende JSON-structuren voor foutmeldingen, twee methoden om de gebruikerssessie uit te lezen, en soms zelfs twee gescheiden inlogstromen. Er is functioneel niets kapot, maar het gevaar is dat een beveiligingsoplossing die u op het ene pad doorvoert, het andere pad onaangeroerd laat.

De oplossing is geen grootscheepse, tijdrovende refactor. Het volstaat om een `.cursorrules`-bestand aan te maken waarin u de conventies expliciet vastlegt: hoe autorisatie universeel wordt afgedwongen, waar API-calls thuishoren en hoe foutmeldingen gestructureerd zijn. Breng vervolgens de meest kritieke bestanden (authenticatie, datatoegang, betalingen) in lijn met die regel, en laat de overige bestanden geleidelijk convergeren zodra u eraan werkt.

**Kosten bij verwaarlozing:** een beveiligingspatch die slechts op één van de twee routes wordt toegepast. **Kosten om op te lossen:** 2 uur voor de richtlijnen, geleidelijke convergentie daarna.

## Post 7: Aannames die alleen geldig waren in een browser-sandbox

De laatste en meest fijnzinnige categorie. Code die is ontworpen voor WebContainer bevat stilzwijgende aannames over bestandssystemen, procesduur en de runtime-omgeving. Op een echte Node-server — en met name in een serverless cloud-omgeving zoals Vercel — worden achtergrondtaken die zijn gestart met een losse `setTimeout` mogelijk nooit uitgevoerd, simpelweg omdat de serverless-functie direct bevriest zodra het HTTP-antwoord is verzonden. Bestanden wegschrijven naar een lokaal pad verdwijnen geruisloos bij de volgende aanroep. En langdurige taken worden hard afgebroken door de time-out van het platform.

Heeft uw applicatie taken die plaatsvinden "nadat" een aanvraag is afgerond — zoals het versturen van een bevestigingsmail, het genereren van een rapport of het aanroepen van een AI-model? Controleer hoe deze worden aangeroepen. Als de taak niet expliciet wordt ge-`await` of overgedragen aan een echte achtergrondwachtrij, is de uitvoering in productie een kwestie van puur geluk.

**Kosten bij verwaarlozing:** willekeurige, moeilijk reproduceerbare fouten voor gebruikers. **Kosten om op te lossen:** 2 tot 4 uur om asynchrone taken correct af te handelen.

## De balans opmaken

Zeven concrete posten, gezamenlijk goed voor ongeveer één gefocust weekend werk: een uurtje documentatie, twee uur hygiëne rondom omgevingsvariabelen en deployments, een halve dag aan de database, een middag voor de dependencies en twee uur voor de editor-conventies. Dit veronderstelt uiteraard dat u precies weet waar u moet zoeken. De reden dat men deze kosten stelselmatig onderschat, is dat geen van deze problemen zich aandient als een zichtbare bug — de applicatie blijft gedurende het hele traject gewoon functioneren, en exact daardoor overleeft dit puin tot aan de livegang.

Heeft u dat weekend beschikbaar? Voer het dan zelfstandig uit. Heeft u die tijd niet — en op het moment dat u overstapt tussen tools is dat meestal omdat u zo dicht bij lancering bent dat uw aandacht bij klanten hoort te liggen — dan is dit een helder afgebakende scope om uit te besteden. Het is het klassieke profiel van een [LaunchStudio](https://launchstudio.eu/nl/)-traject: uw code blijft uw exclusieve eigendom, inclusief beide generaties, en senior engineers die dit proces tientallen keren hebben doorlopen ruimen het puin op, consolideren de database en leveren een helder gedocumenteerde repository op waarin u met een gerust hart in Cursor verder bouwt. Vaste prijs binnen het Launch Ready-tarief van € 800 tot € 3.500, met een doorlooptijd van één tot drie weken — een fractie van wat een bureau rekent voor een onnodige complete herbouw. Onze engineers zijn afkomstig van [Manifera](https://www.manifera.com/services/custom-software-development/), waar men al meer dan elf jaar gespecialiseerd is in het overnemen, opschonen en professionaliseren van bestaande softwareprojecten.

Wilt u weten wat uw overstap precies heeft achtergelaten? [Bekijk hoe andere oprichters van een hybride codebase naar een succesvol live product gingen](https://launchstudio.eu/nl/#proof) — en deel uw repository voor een vrijblijvende technische scan.

## Praktijkvoorbeeld

### De vergeten Netlify-uitrol waar sinds oktober niemand naar had omgekeken

Sem Vaandrager ontwikkelde met behulp van Bolt in één weekend Rittenboek: een ritten- en onkostenregistratie voor Nederlandse zzp'ers, compleet met automatische categorisering en een kwartaalexport voor de boekhouder. Drie weken later exporteerde hij de codebase naar GitHub en zette hij de ontwikkeling voort in Cursor, waar hij ondersteuning voor meerdere voertuigen, een portaal voor accountants en Mollie-abonnementskoppelingen toevoegde. Tegen januari telde hij 240 betalende gebruikers tegen een tarief van € 7 per maand.

Onze pre-launch review bracht het technische residu in exact de hierboven beschreven volgorde aan het licht. De oorspronkelijke Netlify-deployment bleek nog altijd actief te builden vanaf een verouderde branch én was nog steeds rechtstreeks verbonden met de live Supabase-productiedatabase — vier maanden aan afwijkende code, online bereikbaar via een URL die een groep vroege gebruikers als bladwijzer had opgeslagen. Twee van de actieve RLS-policies dateerden nog uit de Bolt-fase en refereerden aan een `user_id`-kolom op een tabel die inmiddels was omgebouwd naar organisaties; deze policies matchten daardoor op niets, waardoor de databasetoegang willekeurig openstond. En de kwartaalexport — de belangrijkste functionaliteit voor boekhouders — werd aangeroepen via een niet-afgewachte (`unawaited`) asynchrone functie. Hierdoor werd circa één op de vijftien exportverzoeken halverwege afgebroken door de serverless runtime. Sem was al twee weken bezig geweest met het aanpassen van SPF- en DKIM-records in de overtuiging dat het een e-mailbezorgprobleem was.

**Resultaat:** De verouderde Netlify-omgeving werd definitief ontkoppeld, alle omgevingsvariabelen werden geconsolideerd in één gecommit `.env.example`, de RLS-policies werden gecorrigeerd en vastgelegd in een opgeschoonde baseline-migratie, en de exporttaak werd ondergebracht in een betrouwbare wachtrij met automatische herstelpogingen. Vijf werkdagen doorlooptijd, zonder ook maar één aanpassing aan de gebruikersinterface.

> *"Die exportfout was achteraf bijna komisch. Ik was twee weken lang geobsedeerd bezig met SPF- en DKIM-records omdat ik dacht dat de mail niet aankwam. In werkelijkheid werd het rapport niet eens gegenereerd — de serverless-functie had de verbinding al verbroken vóórdat het bestand klaar was."*
> — **Sem Vaandrager, Oprichter, Rittenboek (Zwolle)**

**Kosten & Doorlooptijd:** € 2.300 (Launch Ready Pakket) — live binnen 5 werkdagen.

---

## Veelgestelde Vragen

### Had ik de overstap moeten vermijden en gewoon binnen één tool moeten blijven?

Nee, beslist niet. Overstappen op het moment dat prompten tijdrovender wordt dan direct programmeren is een gezond ontwikkelaarsinstinct. Langer in een browser-omgeving blijven hangen kost op termijn aanzienlijk meer tijd dan het opruimen van het residu. De fout is niet de overstap zélf, maar de aanname dat een exportbestand een schone overdracht is, terwijl het in werkelijkheid twee verschillende codebases betreft die één map delen.

### Kan ik de git-historie van mijn Bolt-project alsnog importeren?

Niet op een zinvolle manier. De promptgeschiedenis van Bolt is geen reguliere git-boom die geconverteerd kan worden. De meest effectieve maatregel is het vastleggen van de oorsprong in documentatie — welke tool de basis heeft gelegd, op welke datum, welke bibliotheken zijn gekozen en welke beslissingen niet van uzelf waren — in plaats van het krampachtig reconstrueren van commits die nooit hebben bestaan.

### Hoe spoor ik vergeten deployments op die ik uit het oog ben verloren?

Controleer het dashboard van elke hostingprovider waar u ooit een account heeft aangemaakt op actieve koppelingen met uw repository. Controleer vervolgens de DNS-records van uw hoofddomein op onbekende CNAME-verwijzingen, en doorzoek uw eigen verzonden e-mails en Slack-berichten op links die eindigen op `.netlify.app` of `.vercel.app`. Die laatste zoekactie levert vrijwel altijd de vergeten URL op die nog ergens circuleert.

### Zijn de door Bolt gegenereerde RLS-policies veilig om te behouden?

Sommige wel, maar elke policy moet regel voor regel worden gecontroleerd tegen uw huidige databasestructuur. Beleidsregels die verwijzen naar kolommen die later zijn hernoemd of omgebouwd naar team-structuren vormen een acuut risico: een voorwaarde die op niets meer matcht, kan afhankelijk van de opzet onbedoeld alle data openbaar maken.

### Is het de moeite waard om een regelsbestand voor mijn code-editor te schrijven?

Jazeker, het is de meest rendabele handeling op de hele lijst. Zonder duidelijke richtlijnen blijft het AI-model willekeurig de stijl overnemen van het bestand dat toevallig geopend staat, waardoor de kloof tussen geïmporteerde code en uw eigen werk permanent blijft bestaan. Een beknopt regelsbestand over autorisatie, API-aanroepen en foutafhandeling zorgt ervoor dat nieuwe code direct convergeert naar één uniforme standaard.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Had ik de overstap moeten vermijden en gewoon binnen één tool moeten blijven?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Nee. Overstappen zodra prompten trager wordt dan zelf coderen is de juiste keuze. De fout is niet de overstap, maar de aanname dat een geëxporteerd project een schone codebase is in plaats van twee generaties code die één map delen."
      }
    },
    {
      "@type": "Question",
      "name": "Kan ik de git-historie van mijn Bolt-project alsnog importeren?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Nee, niet zinvol. Leg de herkomst vast in een document (tool, datum, framework-versies, initiële keuzes) in plaats van te proberen commits te reconstrueren die nooit hebben bestaan."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe spoor ik vergeten deployments op die ik uit het oog ben verloren?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Controleer dashboards van Netlify, Vercel en Cloudflare op gekoppelde repositories, controleer DNS-records op oude subdomeinen en zoek in eigen mail en chat naar .netlify.app of .vercel.app links."
      }
    },
    {
      "@type": "Question",
      "name": "Zijn de door Bolt gegenereerde RLS-policies veilig om te behouden?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Alleen na handmatige verificatie tegen het huidige schema. Policies die verwijzen naar hernoemde kolommen of gewijzigde permissies kunnen permissief falen en tabellen onbedoeld openzetten."
      }
    },
    {
      "@type": "Question",
      "name": "Is het de moeite waard om een regelsbestand voor mijn code-editor te schrijven?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ja, dit is de meest rendabele ingreep. Zonder regelsbestand kopieert het model willekeurige stijlen uit geopende bestanden. Een expliciet bestand dwingt één consistente architectuur af."
      }
    }
  ]
}
</script>
