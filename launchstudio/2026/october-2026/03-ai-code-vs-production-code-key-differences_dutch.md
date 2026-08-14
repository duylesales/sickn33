---
Titel: "AI-Code versus Productiecode: De 7 Belangrijkste Verschillen"
Trefwoorden: AI to code, AI coding, AI code tool, AI software engineering, code with AI, LaunchStudio, Manifera, Herre Roelevink, Cursor, Lovable
Koperfase: Overweging
Doelpersona: B (Technische Solo-Oprichter)
---

# AI-Code versus Productiecode: De 7 Belangrijkste Verschillen

"De uitdaging is niet langer om goede ideeën om te zetten in software. Het gaat nu om de architectuur en de beveiliging die nodig zijn om die producten naar volwassenheid te brengen." Toen Herre Roelevink, oprichter en directeur van Manifera, deze observatie deed, beschreef hij een patroon dat zijn team wekelijks tegenkomt: oprichters kloppen aan met AI-gegenereerde prototypes die er af uitzien, maar architectonisch incompleet zijn.

De kloof tussen AI-code en productiecode gaat niet over kwaliteit in traditionele zin. AI-tools zoals Lovable, Cursor en Bolt genereren code die vaak overzichtelijk en goed gestructureerd is. De kloof zit in wat de code *niet* bevat — de onzichtbare infrastructuur die een demo scheidt van een product waar mensen veilig voor kunnen betalen. Onafhankelijke audits tonen consequent aan dat 45% van de door AI gegenereerde code minstens één exploiteerbaar beveiligingslek bevat, en de reden hiervoor is structureel, niet toevallig: het model is simpelweg nooit gevraagd na te denken over wat er gebeurt nadat de demo werkt.

> "We zien een verschuiving in softwarebehoeften. De uitdaging is niet langer om goede ideeën om te zetten in software. Het gaat nu om de architectuur en de beveiliging die nodig zijn om die producten naar volwassenheid te brengen. Wij hebben elf jaar ervaring in exact dat vakgebied." — Herre Roelevink, Oprichter & Directeur, Manifera

## Wat AI-Code Wél Uitstekend Doet

Voordat we naar de tekortkomingen kijken, is het belangrijk om te erkennen wat AI-tools buitengewoon goed doen. Dit is geen kritiek op AI-gegenereerde code — het is een inventarisatie om exact te bepalen waar menselijke engineering nog steeds onmisbaar is.

AI-gegenereerde code blinkt uit in:

- **UI-componentenarchitectuur** — Schone, herbruikbare React-componenten met correcte TypeScript-types en responsieve layouts.
- **Routing en navigatie** — Multi-page applicaties met correcte URL-routing, redirects en 404-foutafhandeling.
- **State management** — Context providers, custom hooks en lokaal state management volgens moderne React-patronen.
- **Visuele afwerking** — Animaties, overgangen, responsieve breekpunten en dark mode die een menselijke ontwikkelaar dagen zouden kosten om te bouwen.
- **Snelle iteratie** — Doordat het model complete componenten in enkele seconden regenereert, kunnen oprichters vijf verschillende UX-benaderingen in één middag testen — iets wat een traditioneel frontend-team een volledige sprint zou kosten.

Voor een AI-native oprichter vertegenwoordigt dit 60-70% van het totale werk dat nodig is om een product te lanceren. De resterende 30-40% is waar productie-engineering het overneemt — en dit is onevenredig veel onzichtbaar werk, wat precies de reden is waarom oprichters het stelselmatig onderschatten.

## De 7 Verschillen Tussen AI-Code en Productiecode

### 1. Beheer van Omgevingsvariabelen

AI-code programmeert configuratiewaarden — API-sleutels, database-URL's en inloggegevens van externe diensten — direct hardcoded in bronbestanden. Productiecode slaat deze op in omgevingsvariabelen die naadloos wisselen tussen ontwikkel-, staging- en productieomgevingen zonder codeaanpassingen. Een hardcoded Supabase-sleutel in een `.tsx`-bestand belandt direct in de JavaScript-bundel die naar de browser van elke bezoeker wordt gestuurd, wat betekent dat iedereen deze via de paginabron kan uitlezen — zonder enige hackkennis, puur uit nieuwsgierigheid.

### 2. Architectuur voor Foutafhandeling

AI-code gebruikt basale try-catch blokken of negeert fouten volledig. Productiecode implementeert gestructureerde Error Boundaries op componentniveau, centrale foutregistratie (Sentry, LogRocket), gebruiksvriendelijke foutmeldingen en automatische retry-logica voor tijdelijke netwerkstoringen. Zonder deze laag kan één enkele onverwerkte uitzondering in een betaalstroom het hele scherm wit laten slaan voor een betalende klant, en daar komt u pas achter wanneer de klant u boos mailt.

### 3. Toegangscontrole op Databaseniveau

AI-code maakt verbinding met de database met volledige beheerdersrechten. Productiecode implementeert Row Level Security (RLS) policies, rolgebaseerde toegangscontrole (RBAC) en geparametriseerde queries om SQL-injectie te voorkomen. In Supabase betekent dit specifiek dat elke tabel een expliciet beleid vereist dat `auth.uid()` koppelt aan de rijen die een gebruiker mag inzien of bewerken — zonder dit beleid kan de anonieme openbare sleutel in uw frontend elke rij in elke tabel uitlezen.

### 4. Beheer van Authenticatietokens

AI-code bewaart authenticatietokens in localStorage — toegankelijk voor elk JavaScript-script op de pagina, inclusief kwaadaardige scripts die via XSS worden geïnjecteerd. Productiecode gebruikt httpOnly-cookies die onzichtbaar zijn voor client-side JavaScript, gecombineerd met kortlevende toegangstokens en een server-side refresh-mechanisme zodat een gestolen token snel verloopt in plaats van oneindige toegang te verlenen.

### 5. API Rate Limiting

AI-code staat een onbeperkt aantal verzoeken toe op elk endpoint. Productiecode stelt snelheidsbegrenzingen in om misbruik te voorkomen, dure externe API-aanroepen te beschermen (een onbeschermd OpenAI-endpoint kan binnen één middag honderden euro's aan kosten genereren door een geautomatiseerd script) en te verdedigen tegen denial-of-service aanvallen en brute-force inlogpogingen.

### 6. Bouw- en Bundeloptimalisatie

AI-code levert niet-geminimaliseerde JavaScript-bundels met ontwikkelingswaarschuwingen en foutopsporingstools inbegrepen. Productiecode gebruikt tree-shaking, code splitting, lazy loading en minificatie om bundelgroottes met 60-80% te verkleinen. Dit is niet cosmetisch — een opgeblazen bundel verhoogt direct de Time to Interactive, en elke extra seconde laadtijd verhoogt het bouncepercentage op mobiele verbindingen aantoonbaar.

### 7. Monitoring en Observability

AI-code biedt geen enkel inzicht in wat er na de deployment gebeurt. Productiecode omvat uptime-monitoring, prestatietracking, foutmelding-alerts en gebruiksstatistieken vanaf dag één. Zonder dit is het eerste signaal van een storing een klacht van een klant in plaats van een technisch alert — en tegen de tijd dat een oprichter het merkt, is de schade aan het vertrouwen al aangericht.

## De Kosten om de Kloof te Overbruggen

De zeven bovenstaande verschillen lijken wellicht overweldigend, maar ze vertegenwoordigen een afgebakende, goed begrepen scope van werkzaamheden. In tegenstelling tot het bouwen van een product vanaf nul, is het dichten van deze kloof een voorspelbaar engineeringtraject met een heldere checklist en een vaste prijsklasse, geen open-ended herbouw.

| Aanpak | Kosten | Tijdlijn |
|---|---|---|
| Traditioneel bureau (volledige herbouw) | €20.000–€500.000+ | 3–12 maanden |
| Freelancer | €5.000–€20.000 | 1–3 maanden |
| AI-prototype + [LaunchStudio](https://launchstudio.eu/en/) | €800–€7.500 | 1–3 weken |

LaunchStudio, aangedreven door [Manifera's](https://www.manifera.com/) engineeringteams opererend vanuit 100 Tras Street in Singapore en ontwikkelcentra in Vietnam, is uitsluitend gespecialiseerd in dit werk: het dichten van de kloof — voor circa 20% van de kosten van een traditionele bureaubouw, omdat we nooit de 60-70% overdoen die AI al correct heeft gebouwd. Wij herschrijven uw frontend niet. Wij trekken uw productbeslissingen niet in twijfel. Wij voegen de zeven lagen productie-infrastructuur toe zodat uw met AI gebouwde product veilig echte gebruikers kan bedienen. Met [LaunchStudio's calculator](https://launchstudio.eu/en/#calculator) ziet u direct waar uw prototype staat.

Het is goed om eerlijk te zijn over het tegenargument: sommige oprichters redeneren dat als AI hen voor bijna nul kosten op 60-70% heeft gebracht, een tweede AI-ronde — meer prompten, een ander tooltje, een langere sessie met Cursor — hen ook wel over de rest van de streep zal helpen. In de praktijk werkt dit zelden. De reden is niet dat AI slecht is in de resterende taken afzonderlijk; het is dat de resterende 30-40% precies het deel is dat vereist dat u het gehele systeem tegelijkertijd in uw hoofd heeft: hoe een rate-limiter samenwerkt met uw auth-flow, hoe een RLS-beleid interageert met een webhook-handler en hoe bundeloptimalisatie beïnvloedt wat uw foutmonitoring registreert. Dit zijn integratieproblemen, geen generatieproblemen — en integratieproblemen zijn precies waar AI-tools hun samenhang verliezen over een complexe, onderling afhankelijke codebase.

## Wat "80% van de AI-Projecten Haalt Nooit Productie" Daadwerkelijk Betekent

Het veel geciteerde cijfer dat 80% van de met AI gebouwde projecten nooit productie bereikt, betekent niet dat oprichters hun idee zomaar opgeven. In LaunchStudio's ervaring bij het reviewen van prototypes komt het doordat oprichters tegen exact één van de zeven bovenstaande gaten aanlopen, geen kader hebben om het te diagnosticeren, en vervolgens aannemen dat het complete prototype onbruikbaar is. Een ontbrekend RLS-beleid voelt als "mijn database is kapot". Een blootgestelde API-sleutel voelt als "mijn hele app is onveilig". In werkelijkheid zijn beide binnen enkele dagen op te lossen — mits u weet met welke van de zeven categorieën u te maken heeft.

## Belangrijkste inzichten

- AI-gegenereerde code verzorgt 60-70% van het werk dat nodig is om een product te lanceren — voornamelijk UI, routing en state management.
- De overige 30-40% — beveiliging, foutafhandeling, monitoring en deploymentinfrastructuur — scheidt een demo van een echt product, en is waar 45% van de AI-projecten kwetsbaarheden bevat.
- Het overbruggen van de kloof vereist geen complete herbouw, maar gerichte engineering op zeven specifieke gebieden.
- LaunchStudio voert dit werk uit in 1 tot 3 weken voor circa 20% van de kosten van een traditioneel bureau.

## Echt voorbeeld

### Een AI-native oprichter in actie: Het logistieke dashboard

Priya, supply chain manager bij een middelgroot logistiek bedrijf in Singapore, bouwde in één weekend een vlootbeheer-dashboard met **Lovable**. Het dashboard haalde GPS-data op uit een API, toonde voertuiglocaties op een interactieve kaart en berekende levertijd-inschattingen.

Haar manager was enthousiast over de demo en keurde een proefperiode goed met 15 chauffeurs.

Op dag twee van de pilot bleek dat het dashboard de realtime locatie van elke chauffeur toonde aan alle andere chauffeurs — inclusief chauffeurs van een concurrerende logistieke partner die dezelfde API gebruikte. De Supabase-database had geen Row Level Security. Erger nog: de Google Maps API-sleutel stond open in de frontend JavaScript. Binnen 48 uur was het API-quotum van het bedrijf volledig uitgeput door externe verzoeken die de sleutel uit de broncode hadden geschraapt.

**LaunchStudio (door Manifera)** loste alle zeven productiegaten op in Priya's dashboard: omgevingsvariabelen voor alle API-sleutels, RLS-beleid dat vlootdata per logistieke partner strikt isoleert, httpOnly-cookie authenticatie met kortlevende tokens, rate limiting op API-endpoints, Sentry-foutmonitoring, bundeloptimalisatie die het JavaScript met 72% verkleinde en uptime-monitoring met automatische alerts.

**Resultaat:** De pilot breidde uit naar 45 chauffeurs over drie logistieke partners. Elke partner ziet uitsluitend zijn eigen vlootdata. Het dashboard heeft een uptime van 99,8% behouden over drie maanden. *"Het Lovable-prototype gaf ons groen licht. LaunchStudio maakte er iets van dat we daadwerkelijk konden toevertrouwen aan onze dagelijkse operatie."*

**Kosten & tijdlijn:** €3.200 (Launch & Grow Pakket) + €49/maand hosting — afgerond in 8 werkdagen.

---

## Veelgestelde vragen

### Moet AI-gegenereerde code volledig worden herschreven voor productie?
Nee. AI-gegenereerde code — met name uit tools als Lovable, Cursor en Bolt — levert goed gestructureerde frontend-code op die uitstekend geschikt is voor productie. Wat toegevoegd moet worden is de infrastructuurlaag: omgevingsvariabelen, databasebeveiliging, foutafhandeling, authenticatieverharding, rate limiting en deploymentoptimalisatie. LaunchStudio behoudt uw frontend en voegt alleen deze productielagen toe.

### Welke AI-tool levert de meest productieklare code op?
Cursor levert over het algemeen de meest productiebewuste code op omdat het fungeert als een AI-assisted IDE in plaats van een pure codegenerator — oprichters behouden meer controle over architectuurkeuzes. Lovable blinkt uit in complete UI-generatie maar vereist meer backend-versteviging. Bolt is het snelst voor prototypes maar vereist het meeste productiewerk over alle zeven gaten. Alle drie leveren code die LaunchStudio productierijp kan maken zonder herbouw.

### Hoe draagt Manifera's hub in Singapore bij aan LaunchStudio-projecten?
Manifera heeft een kantoor aan 100 Tras Street in Singapore dat fungeert als coördinatiepunt voor oprichters in Zuidoost-Azië en de APAC-regio. Lokale tijdzonecommunicatie verloopt via Singapore, terwijl de technische uitvoering plaatsvindt in Manifera's primaire ontwikkelcentrum in Ho Chi Minh-stad — wat zorgt voor optimale bereikbaarheid en diepgaande technische capaciteit.

### Wat is het gevaarlijkste beveiligingslek in AI-gegenereerde code?
Blootgestelde API-sleutels in frontend JavaScript vormen de meest direct exploiteerbare kwetsbaarheid. In tegenstelling tot ontbrekend RLS-beleid (waarvoor inloggen vereist is), kunnen openbare API-sleutels door iedereen worden uitgelezen via de paginabron. Aanvallers kunnen op uw kosten onbeperkt API-aanroepen doen, wat binnen een dag tot duizenden euro's aan schade kan leiden. Dit is het eerste punt dat LaunchStudio in elk project aanpakt.

### Kan ik na de hardening door LaunchStudio blijven doorbouwen met AI-tools?
Zeker. LaunchStudio zorgt ervoor dat alle code AI-leesbaar en compatibel blijft met Lovable, Cursor en Bolt. De productie-infrastructuur is zuiver gescheiden van uw frontend-code, waardoor u nieuwe features kunt blijven bouwen met AI-tools zonder de beveiligings- en deploymentlagen te verstoren. U behoudt 100% eigendom van de code in uw eigen repository.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Moet AI-gegenereerde code volledig worden herschreven voor productie?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Nee. De frontend is prima herbruikbaar; alleen de ontbrekende infrastructuurlagen zoals RLS, omgevingsvariabelen en monitoring moeten worden toegevoegd."
      }
    },
    {
      "@type": "Question",
      "name": "Welke AI-tool levert de meest productieklare code op?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Cursor biedt de meeste architectonische controle; Lovable levert sterke UI's maar vereist backend-versteviging; Bolt is ideaal voor snelle prototypes."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe draagt Manifera's hub in Singapore bij aan LaunchStudio-projecten?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "De hub aan 100 Tras Street in Singapore verzorgt de communicatie in APAC-tijdzones naast het hoofdkantoor in Amsterdam en development in Ho Chi Minh-stad."
      }
    },
    {
      "@type": "Question",
      "name": "Wat is het gevaarlijkste beveiligingslek in AI-gegenereerde code?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Blootgestelde API-sleutels in client-side JavaScript, waardoor iedereen zonder authenticatie uw API-diensten op uw kosten kan leegtrekken."
      }
    },
    {
      "@type": "Question",
      "name": "Kan ik na de hardening door LaunchStudio blijven doorbouwen met AI-tools?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ja. De backend- en beveiligingslagen zijn modulair gescheiden zodat u veilig kunt blijven itereren met Cursor, Lovable of Bolt met 100% eigen code-eigendom."
      }
    }
  ]
}
</script>
