---
Titel: "Hoe Ruim Ik Dubbele Code Op in een Lovable-Project?"
Trefwoorden: dubbele code lovable, lovable project refactoren, ai-gegenereerde code opruimen, technische schuld lovable, LaunchStudio, Manifera
Koperfase: Overweging
Doelgroep: AI-Native Oprichter (Niet-Technisch)
---

# Hoe Ruim Ik Dubbele Code Op in een Lovable-Project?

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Hoe Ruim Ik Dubbele Code Op in een Lovable-Project?",
  "description": "Na maanden prompten bevatten Lovable-projecten vaak dezelfde logica op veel plekken: meerdere manieren om data op te halen, herhaalde rechtencontroles, gedupliceerde componenten en meerdere libraries voor dezelfde taak. Deze gids legt uit waarom duplicatie ontstaat, waarom het bugs veroorzaakt, hoe u het vindt, wat u als eerste samenvoegt, hoe u veilig refactort zonder de app of de workflow van Lovable te breken, en hoe u voorkomt dat duplicatie terugkomt.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-08-04",
  "inLanguage": "nl-NL",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/how-do-i-clean-up-duplicate-code-in-a-lovable-project" },
  "citation": [
    { "@type": "CreativeWork", "name": "Lovable documentation", "url": "https://docs.lovable.dev/" },
    { "@type": "CreativeWork", "name": "Martin Fowler: Refactoring", "url": "https://martinfowler.com/books/refactoring.html" },
    { "@type": "CreativeWork", "name": "jscpd: Copy/paste detector", "url": "https://github.com/kucherenko/jscpd" },
    { "@type": "CreativeWork", "name": "OWASP Top 10 2021: A01 Broken Access Control", "url": "https://owasp.org/Top10/A01_2021-Broken_Access_Control/" }
  ]
}
</script>

**Kort antwoord:** Zoek eerst de duplicatie die risico oplevert, niet alles tegelijk. In Lovable-projecten zit de schadelijkste duplicatie meestal in datatoegang, rechtencontroles, berekeningen van bedragen en datums en kerncomponenten. Voeg die samen in gedeelde modules, beschermd door tests, in kleine stappen, waarbij elke wijziging op staging wordt gecontroleerd. Houd het project compatibel met Lovable door via GitHub te synchroniseren en één grote herstructurering te vermijden, en schrijf projectinstructies die Lovable vertellen de gedeelde modules te hergebruiken, zodat duplicatie niet terugkomt met de volgende prompt.

## Belangrijkste Punten

- **Duplicatie is een natuurlijk gevolg van ontwikkelen met prompts:** elke prompt lost zijn eigen probleem op, vaak door nieuwe code te schrijven in plaats van bestaande code te hergebruiken.
- **Gedupliceerde logica veroorzaakt inconsistent gedrag en terugkerende bugs,** omdat fixes in één kopie terechtkomen terwijl andere kapot blijven.
- **Duplicatie rond beveiliging is het gevaarlijkst:** rechtencontroles die inconsistent worden herhaald over schermen en functies.
- **Refactor in kleine, geteste stappen** in plaats van grote delen in één keer te herschrijven.
- **Voorkom herhaling** met gedeelde modules, duidelijke conventies en projectinstructies voor AI-tools.

## Waarom Lovable-Projecten Duplicatie Verzamelen

Wanneer u Lovable om een functie vraagt, genereert het code die die functie laat werken. Het weet niet altijd, of geeft geen prioriteit aan, dat vergelijkbare code elders al bestaat. Over maanden levert dat op:

- Meerdere functies die dezelfde data ophalen met net andere filters
- Herhaalde rechtencontroles, sommige strenger dan andere
- Meerdere helpers voor het opmaken van datums en bedragen
- Vergelijkbare componenten met kleine visuele verschillen
- Twee of drie libraries die hetzelfde doen, zoals datumafhandeling of iconen
- Kopieën van de Supabase-client die op meerdere plekken worden geïnitialiseerd
- Validatieregels die in formulieren worden herhaald en elkaar soms tegenspreken

Niets hiervan is ongebruikelijk. Menselijke teams creëren ook duplicatie. AI-tools doen het alleen sneller.

## Waarom Het Ertoe Doet

| Probleem | Voorbeeld |
| --- | --- |
| Inconsistent gedrag | De factuurlijst toont bedragen inclusief btw, het dashboard exclusief |
| Terugkerende bugs | Een bug wordt in één kopie van een functie opgelost en komt via een andere terug |
| Gaten in beveiliging | Het ene scherm controleert het lidmaatschap van de organisatie, een ander laadt dezelfde data zonder die controle |
| Tragere ontwikkeling | Elke wijziging moet op meerdere plekken worden doorgevoerd |
| Grotere bundles | Meerdere libraries voor hetzelfde doel vertragen de app |
| Verwarrend voor developers | Nieuwe developers weten niet welke versie de juiste is |
| Verwarrend voor AI-tools | Lovable pikt inconsistente patronen op en herhaalt ze |

De regel over beveiliging verdient nadruk. Gebrekkige toegangscontrole is het grootste risico in de OWASP Top 10. Wanneer rechtenlogica wordt gedupliceerd, is één kopie makkelijk zwakker, en die zwakste kopie bepaalt uw werkelijke beveiliging.

## Stap 1: Zorg Dat de Code in GitHub Staat

Koppel uw Lovable-project aan GitHub als dat nog niet zo is. Dat geeft u een volledige geschiedenis, laat u werken op branches, tools op de code draaien en terugdraaien als er iets misgaat. Onze gids over [Lovable-code exporteren naar GitHub en verder bouwen](https://launchstudio.eu/nl/blog/how-to-export-lovable-code-to-github-and-keep-building) legt de workflow uit.

## Stap 2: Vind de Duplicatie

Praktische manieren om duplicaten te vinden:

- **Tools die kopieer- en plakwerk detecteren,** zoals jscpd, scannen de codebase en noemen blokken gedupliceerde code.
- **Zoek naar patronen:** bijvoorbeeld elke plek die `supabase.from('invoices')` aanroept, elke `createClient(`-aanroep of elke functie die datums opmaakt.
- **Controleer afhankelijkheden:** bekijk de packages in `package.json` en zoek naar overlappende libraries.
- **Vraag een AI-tool:** "Noem alle functies die facturen ophalen en hoe ze verschillen" of "Zoek alle plekken waar het lidmaatschap van een organisatie wordt gecontroleerd."
- **Bekijk grote bestanden:** zeer grote componenten bevatten vaak logica die ook elders bestaat.

Leg de bevindingen vast in een korte lijst, gegroepeerd per gebied.

## Stap 3: Prioriteer

Niet alle duplicatie is het waard om nu op te lossen. Prioriteer op risico en hoe vaak er iets verandert:

| Prioriteit | Gebied | Waarom |
| --- | --- | --- |
| 1 | Rechten- en toegangscontroles | Beveiligingsrisico |
| 2 | Datatoegang voor kernentiteiten | Consistentie, prestaties, beveiliging |
| 3 | Berekeningen van bedragen, btw en datums | Correctheid, vertrouwen van klanten |
| 4 | Validatieregels | Datakwaliteit |
| 5 | Kerncomponenten van de interface, zoals formulieren, tabellen en dialogen | Consistentie, toegankelijkheid |
| 6 | Dubbele libraries | Bundlegrootte, onderhoud |
| 7 | Kleine helpers en styling | Laag risico, oplossen wanneer het uitkomt |

## Stap 4: Voeg Tests Toe vóór het Refactoren

Refactoren betekent de structuur veranderen zonder het gedrag te veranderen. Met tests weet u dat het gedrag niet veranderd is. Voeg vóór het samenvoegen van een gebied tests toe voor het gedrag dat ertoe doet:

- **Toegangscontrole:** gebruiker A kan de data van gebruiker B niet lezen of wijzigen, via elke route die die data raakt
- **Berekeningen:** totalen, btw en afronding voor representatieve gevallen
- **Belangrijke flows:** aanmelden, afrekenen, kernrecords aanmaken en bewerken

Zelfs een bescheiden testsuite rond de gebieden die u wijzigt, maakt refactoren veel veiliger.

## Stap 5: Voeg Samen in Kleine Stappen

Per gebied:

1. **Maak een gedeelde module,** zoals een bestand voor datatoegang voor facturen met functies als `listInvoices(ctx)` en `getInvoice(ctx, id)`, of een helper `formatMoney`.
2. **Zet de beste versie van de logica** in de module, kies het juiste gedrag waar kopieën verschillen, en stem af met de producteigenaar als dat onduidelijk is.
3. **Vervang één gebruik tegelijk,** en draai na elke wijziging de tests.
4. **Verwijder de oude kopieën** zodra alle gebruiken naar de gedeelde module verwijzen.
5. **Deploy naar staging,** test handmatig en breng het daarna uit.

Voeg in Supabase-apps de rechtenlogica waar mogelijk samen op databaseniveau: Row Level Security-policies dwingen regels af voor elke query, ongeacht welke frontendfunctie hem uitvoert. Dan hoeft u niet meer te vertrouwen op elke gedupliceerde controle.

## Stap 6: Verwijder Dubbele Libraries

Kies één library per doel, vervang het gebruik van de andere en verwijder ze uit `package.json`. Controleer de bundlegrootte voor en na; de verbetering is vaak zichtbaar in de laadtijden van pagina's.

## Het Project Lovable-Vriendelijk Houden

Als u na het opruimen in Lovable blijft bouwen:

- **Werk via GitHub,** zodat Lovable de gerefactorde code synchroniseert.
- **Refactor stapsgewijs,** in plaats van het hele project in één keer te herstructureren, wat het begrip van Lovable van de codebase in de war kan brengen.
- **Houd vertrouwde structuren aan** waar Lovable ze verwacht, zoals mappen voor componenten en pagina's.
- **Test na het refactoren een paar Lovable-prompts** op een branch of stagingproject, om te zien of het de nieuwe modules hergebruikt.

## Voorkomen Dat Duplicatie Terugkomt

De belangrijkste stap. Zonder deze stap brengen de prompts van de komende weken de duplicatie terug:

- **Projectinstructies:** beschrijf gedeelde modules en conventies, zoals "Alle databasetoegang loopt via `src/data/`", "Gebruik `formatMoney` voor alle bedragen", "Gebruik het component `DataTable` voor lijsten" en "Voeg geen nieuwe datumlibraries toe."
- **Gewoonten bij prompten:** noem bij een vraag om een functie welke bestaande modules gebruikt moeten worden.
- **Review nieuwe code:** controleer op nieuwe functies die gedeelde functies dupliceren.
- **Geautomatiseerde controles:** draai detectie van duplicatie in CI en volg de trend.
- **Periodiek opruimen:** plan elke maand of twee kleine sessies om samen te voegen.

## Een Voorbeeld van Samenvoegen: Datatoegang

Neem een project waarin facturen op vijf plekken worden geladen: de factuurlijst, de dashboardwidget, de detailpagina van een klant, de exportfunctie en een functie voor e-mailherinneringen. Elke plek gebruikt een net andere query; twee vergeten op organisatie te filteren, één selecteert alle kolommen inclusief interne notities en één berekent totalen in de browser.

Samenvoegen kan er zo uitzien:

1. **Schrijf tests** die bevestigen dat een gebruiker alleen de facturen van zijn organisatie kan zien, en dat totalen voor een paar testfacturen overeenkomen met de verwachte waarden.
2. **Schakel Row Level Security in of scherp die aan** op de facturentabel, zodat elke query beperkt is tot de organisatie van de gebruiker, ongeacht de frontendcode.
3. **Maak een module** met `listInvoices`, `getInvoice` en `getInvoiceTotals`, die alleen benodigde kolommen selecteert en totalen op de server of in een databaseview berekent.
4. **Vervang de query van de factuurlijst** door `listInvoices`, draai de tests en controleer de pagina.
5. **Herhaal dit** voor het dashboard, de klantpagina, de export en de herinneringsfunctie, één voor één.
6. **Verwijder de oude queries,** doorzoek de codebase om te bevestigen dat er geen meer over zijn, en neem de module op in de projectinstructies.

Elke stap is klein en omkeerbaar, en de app blijft de hele tijd werken. Het resultaat is één plek om bugs op te lossen, één plek om prestaties te optimaliseren en één plek waar AI-tools het patroon vinden om te volgen.

## Voortgang Meten

Volg voor en na een paar eenvoudige getallen: het aantal gedupliceerde blokken volgens de detectietool, het aantal afhankelijkheden, de bundlegrootte en het aantal bugs dat terugkomt nadat het is opgelost. Zien dat deze in de goede richting bewegen, helpt de bestede tijd te verantwoorden en laat zien wanneer u kunt stoppen.

## Wanneer U Stopt

Perfecte deduplicatie is niet het doel. Sommige duplicatie is onschuldig of zelfs verstandig, zoals twee vergelijkbare componenten die waarschijnlijk uit elkaar gaan groeien. Stop wanneer de gebieden met hoog risico zijn samengevoegd, tests ze beschermen en nieuwe code de conventies volgt. Besteed de resterende tijd aan klanten en functies.

## Wanneer Opruimen een Herbouw Wordt

Als duplicatie zo omvangrijk is dat bijna elke functie meerdere keren op onverenigbare manieren is gebouwd, en tests ontbreken, kan een gestructureerde gedeeltelijke herbouw van de backendlaag sneller zijn dan stapsgewijs samenvoegen. Ook dan kan de interface die Lovable genereerde meestal behouden blijven. Onze gids over [herbouwen versus refactoren](https://launchstudio.eu/nl/blog/rebuild-vs-refactor-an-ai-built-app) helpt bij de beslissing.

## Ongebruikte Code

Naast duplicatie verzamelen Lovable-projecten ongebruikte code: verlaten pagina's, componenten van verwijderde functies en helpers die niemand aanroept. Tools die ongebruikte exports en bestanden detecteren, helpen ze te vinden. Dode code verwijderen vermindert de verwarring voor zowel developers als AI-tools.

## Hoe LaunchStudio Helpt

LaunchStudio ruimt door AI gegenereerde codebases op zonder ze opnieuw te bouwen: duplicatie vinden en prioriteren, tests toevoegen rond kritiek gedrag, datatoegang, rechten en berekeningen samenvoegen in gedeelde modules, toegang afdwingen in de database met Row Level Security, dubbele libraries verwijderen, projecten compatibel houden met Lovable en projectinstructies schrijven die voorkomen dat duplicatie terugkomt.

Het **Launch Ready**-pakket (€800-€3.500) omvat een gerichte opruiming van gebieden met hoog risico, samen met het versterken van de beveiliging en deployment; **Launch & Grow** (€2.500-€7.500 plus €49 per maand) voegt beheerde hosting, monitoring en prioriteitssupport toe voor doorlopende ontwikkeling. Gebruik de [prijscalculator](https://launchstudio.eu/nl/#calculator) voor een schatting.

LaunchStudio wordt ondersteund door Manifera, een softwareontwikkelingsbedrijf met 11+ jaar ervaring, 160+ opgeleverde projecten en 120+ engineers, dat codebases onderhoudt en refactort voor enterpriseklanten. Oprichters ontmoeten het team aan de Herengracht 420 in Amsterdam; de engineering gebeurt in het ontwikkelcentrum aan de Pho Quang Street in Ho Chi Minh City, met een hub aan de Tras Street in Singapore.

## Praktijkvoorbeeld

### Een AI-Native Oprichter in Actie: Zeven Manieren om een Project te Laden

Daan Hofstra bouwde Projectkompas in tien maanden in Lovable: een projectmanagementtool voor kleine marketingbureaus, met klanten, projecten, taken, urenregistratie en facturatie. Het werkte, maar elke nieuwe functie leek iets anders te breken. Een bug in de factuurtotalen werd drie keer opgelost en kwam steeds terug, en een gebruiker van het ene bureau zag ooit een project van een ander bureau in een dashboardwidget.

Een scan op duplicatie vond zeven verschillende functies die projecten laadden, met verschillende filters, waarvan er maar vier het bureau controleerden. Bedragen werden op vijf manieren opgemaakt, waarvan twee de btw negeerden. Er waren drie datumlibraries, twee iconenlibraries, vier vergelijkbare tabelcomponenten en de Supabase-client werd in zes bestanden geïnitialiseerd. De terugkerende factuurbug bleek te bestaan uit drie kopieën van de berekening van het totaal, elk op een ander moment apart opgelost.

LaunchStudio voegde eerst Row Level Security-policies per bureau toe op alle tabellen, zodat geen enkele frontendfunctie data van een ander bureau kon laden, en schreef tests voor toegangscontrole en factuurberekeningen. Projecten, taken en facturen kregen gedeelde modules voor datatoegang, en de zeven projectladers werden één voor één vervangen. Eén module voor bedragen regelde btw en afronding, er bleven één datumlibrary en één iconenlibrary over, de tabelcomponenten werden samengevoegd tot één toegankelijk component, en één Supabase-client werd vanuit één bestand geëxporteerd. Projectinstructies vertelden Lovable welke modules en componenten het moest gebruiken, en er werd een controle op duplicatie aan CI toegevoegd.

**Resultaat:** De factuurbug is niet teruggekomen, het lek tussen bureaus is gedicht en de bundlegrootte van de app daalde met ongeveer een derde. Daan bleef in Lovable bouwen, en de nieuwe functies hergebruiken nu de gedeelde modules, terwijl de controle op duplicatie stabiel blijft.

> *"Elke keer dat ik iets oploste, had Lovable ergens nog een kopie. Door de kern samen te voegen, gedraagt de app zich eindelijk als één product."*
> - **Daan Hofstra, Oprichter, Projectkompas (Groningen)**

**Kosten & Doorlooptijd:** €3.500 (Launch Ready-pakket: analyse van duplicatie, RLS per bureau, tests, gedeelde modules, samenvoegen van libraries, samenvoegen van componenten en AI-instructies) - afgerond in 10 werkdagen.

## Veelgestelde Vragen

### Waarom bevat mijn Lovable-project zoveel dubbele code?

Omdat elke prompt code genereert om een specifiek verzoek op te lossen, vaak zonder te hergebruiken wat al bestaat. Over veel prompts verschijnt vergelijkbare logica op veel plekken. Dat is normaal bij ontwikkelen met prompts en is te beheersen met gedeelde modules, tests en projectinstructies.

### Is dubbele code gevaarlijk?

Dat kan. Gedupliceerde logica leidt tot inconsistent gedrag en terugkerende bugs, en gedupliceerde rechtencontroles kunnen gaten in de beveiliging achterlaten waar één kopie zwakker is. Toegangscontrole samenvoegen in databasepolicies en gedeelde modules neemt dat risico weg.

### Kan ik Lovable blijven gebruiken na het refactoren?

Ja, als u via GitHub werkt, stapsgewijs refactort en vertrouwde projectstructuren aanhoudt. Schrijf projectinstructies die de gedeelde modules beschrijven zodat Lovable ze hergebruikt, en test na het opruimen een paar prompts op een branch.

### Hoe helpt de ervaring van Manifera bij het opruimen van code?

Manifera onderhoudt en refactort al 11+ jaar codebases voor enterpriseklanten. LaunchStudio past die ervaring toe op door AI gegenereerde projecten, door gebieden met hoog risico veilig samen te voegen zonder de delen te herschrijven die al werken.

### Verbetert het opruimen van code de snelheid en zichtbaarheid van mijn app?

Vaak wel. Dubbele libraries en inefficiënt laden van data verwijderen maakt pagina's kleiner en sneller, wat de gebruikerservaring verbetert en zoekmachines en AI-antwoordmachines helpt uw openbare pagina's betrouwbaar te bereiken.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "inLanguage": "nl-NL",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Waarom bevat mijn Lovable-project zoveel dubbele code?",
      "acceptedAnswer": { "@type": "Answer", "text": "Elke prompt lost zijn eigen verzoek op zonder bestaande code te hergebruiken; beheers het met gedeelde modules, tests en instructies." }
    },
    {
      "@type": "Question",
      "name": "Is dubbele code gevaarlijk?",
      "acceptedAnswer": { "@type": "Answer", "text": "Het kan inconsistent gedrag, terugkerende bugs en zwakke rechtencontroles veroorzaken; voeg samen in RLS en gedeelde modules." }
    },
    {
      "@type": "Question",
      "name": "Kan ik Lovable blijven gebruiken na het refactoren?",
      "acceptedAnswer": { "@type": "Answer", "text": "Ja, via GitHub, stapsgewijze wijzigingen en instructies die gedeelde modules beschrijven." }
    },
    {
      "@type": "Question",
      "name": "Hoe helpt de ervaring van Manifera bij het opruimen van code?",
      "acceptedAnswer": { "@type": "Answer", "text": "Manifera refactort al 11+ jaar enterprise-codebases en voegt veilig samen zonder te herschrijven." }
    },
    {
      "@type": "Question",
      "name": "Verbetert het opruimen van code de snelheid en zichtbaarheid van mijn app?",
      "acceptedAnswer": { "@type": "Answer", "text": "Vaak; kleinere bundles en efficiënt laden van data maken pagina's sneller voor gebruikers en crawlers." }
    }
  ]
}
</script>
