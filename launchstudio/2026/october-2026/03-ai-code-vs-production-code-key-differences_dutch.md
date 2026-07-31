---
Titel: AI To Code Projecten Transuleren naar Productie
Trefwoorden: ai to code, ai coding, ai code tool, ai software engineering, code met ai, launchstudio, manifera, herre roelevink, cursor, lovable
Koperfase: Overweging
Doelpersona: B (Technische Solo-Oprichter)
---

# AI To Code Projecten Transuleren naar Productie

"De uitdaging is niet langer om goede ideeën om te zetten in software. Het gaat om de architectuur en de beveiliging die nodig zijn om die producten tot wasdom te brengen." Toen Herre Roelevink, Oprichter en Directeur van Manifera, deze observatie deed, beschreef hij een patroon dat zijn team wekelijks tegenkomt: oprichters komen aan met door AI gegenereerde prototypes die er klaar uitzien, maar architectonisch onvolledig zijn.

De kloof tussen AI-code en productiecode gaat niet over kwaliteit in de traditionele zin. AI-tools zoals Lovable, Cursor en Bolt genereren code die vaak goed gestructureerd en leesbaar is. De kloof gaat over wat de code niet bevat — de onzichtbare infrastructuur die een demo scheidt van een product waar mensen veilig voor kunnen betalen. Onafhankelijke audits tonen consistent aan dat 45% van de door AI gegenereerde code minstens één misbruikbaar beveiligingsgat bevat, en de reden is structureel, niet toevallig: het model is nooit gevraagd om na te denken over wat er gebeurt nadat de demo werkt.

> "We zien een verschuiving in softwarebehoeften. De uitdaging is niet langer om goede ideeën en producten om te zetten in software. Het gaat nu om de architectuur en de beveiliging die nodig zijn om die producten tot wasdom te brengen. Wij hebben elf jaar ervaring met precies dat." — Herre Roelevink, Oprichter & Directeur, Manifera

## Wat AI-Code Goed Doet

Voordat we de tekortkomingen bekijken, is het de moeite waard om te erkennen wat AI-tools uitzonderlijk goed doen. Dit is geen kritiek op door AI gegenereerde code — het is een inventarisatie om te bepalen waar menselijke engineering nog steeds vereist is.

Door AI gegenereerde code is uitstekend in:

- **UI componentenarchitectuur** — Schone, herbruikbare React-componenten met juiste prop-typing en responsieve lay-outs.
- **Routing en navigatie** — Multi-page applicaties met juiste URL-routing, omleidingen en 404-afhandeling.
- **State-beheer** — Context-providers, custom hooks en lokaal state-beheer die moderne React-patronen volgen.
- **Visuele afwerking** — Animaties, overgangen, responsieve breekpunten en ondersteuning voor donkere modus die een menselijke ontwikkelaar dagen zou kosten om te implementeren.
- **Snelle iteratie** — Omdat het model in enkele seconden hele componenten kan hergenereren, kunnen oprichters in één middag vijf verschillende UX-benaderingen testen, iets waar een traditioneel frontend-team een volledige sprint over zou doen.

Voor een AI-native oprichter vertegenwoordigt dit 60-70% van het totale werk dat nodig is om een product te lanceren. De resterende 30-40% is waar productie-engineering het overneemt — en dat is onevenredig veel onzichtbaar werk, wat precies is waarom oprichters het onderschatten.

## De 7 Verschillen Tussen AI-Code en Productiecode

### 1. Beheer van Omgevingsvariabelen

AI-code hardcodeert configuratiewaarden — API-sleutels, database-URL's, referenties van derden — rechtstreeks in bronbestanden. Productiecode slaat deze op in omgevingsvariabelen die veranderen tussen ontwikkel-, staging- en productieomgevingen zonder code te wijzigen. Een gehardcodeerde Supabase-sleutel in een `.tsx`-bestand wordt rechtstreeks gebundeld in de JavaScript die naar de browser van elke bezoeker wordt gestuurd, wat betekent dat iedereen deze kan opsporen door de paginabron te bekijken.

### 2. Foutafhandelingsarchitectuur

AI-code gebruikt eenvoudige try-catch-blokken of negeert fouten volledig. Productiecode implementeert gestructureerde foutgrenzen op componentniveau, gecentraliseerde foutregistratie (Sentry, LogRocket), gebruiksvriendelijke foutmeldingen en automatische retry-logica voor tijdelijke storingen. Zonder deze laag kan een enkele onbehandelde uitzondering in een afrekenstroom de hele app op een wit scherm laten lopen voor een betalende klant.

### 3. Database-Toegangscontrole

AI-code maakt verbinding met de database met volledige administratieve rechten. Productiecode implementeert Row Level Security-beleid, rolgebaseerde toegangscontrole en query-parameterisering om SQL-injectie te voorkomen. In Supabase betekent dit specifiek dat elke tabel een expliciet beleid nodig heeft dat `auth.uid()` koppelt aan de rijen die een gebruiker mag aanraken.

### 4. Beheer van Authenticatietokens

AI-code slaat authenticatietokens op in localStorage — toegankelijk voor alle JavaScript die op de pagina draait, inclusief kwaadaardige scripts die via XSS zijn geïnjecteerd. Productiecode gebruikt httpOnly cookies die onzichtbaar zijn voor client-side JavaScript, gekoppeld aan kortstondige toegangstokens en een server-side verversingsmechanisme.

### 5. API Snelheidsbeperking (Rate Limiting)

AI-code staat onbeperkte verzoeken toe naar elk eindpunt. Productiecode implementeert snelheidsbeperking om misbruik te voorkomen, dure API-aanroepen van derden te beschermen en te verdedigen tegen denial-of-service-aanvallen en brute-force inlogpogingen.

### 6. Build-Optimalisatie

AI-code verstuurt ongedetailleerde JavaScript-bundels met waarschuwingen voor ontwikkelmodus en debuggingtools inbegrepen. Productiecode gebruikt tree-shaking, code-splitting, lazy loading en minificatie om bundelgrootte met 60-80% te verminderen. Dit verlaagt de Time to Interactive en verbetert de mobiele prestaties.

### 7. Monitoring en Observabiliteit

AI-code biedt geen zichtbaarheid in wat er gebeurt na de uitrol. Productiecode bevat uptime-monitoring, prestatievolgers, foutwaarschuwingen en gebruiksanalyses vanaf dag één. Zonder dit is het eerste signaal van een storing een klacht van een klant.

## De Kosten van het Dichten van de Kloof

De zeven bovenstaande verschillen lijken misschien overweldigend, maar ze vertegenwoordigen een afgebakend, goed begrepen werkgebied. Anders dan het vanaf nul opbouwen van een product, is het dichten van de kloof een voorspelbare technische taak met een bekende checklist en een bekend kostenbereik.

| Benadering | Kosten | Doorlooptijd |
|---|---|---|
| Traditioneel bureau (volledige herbouw) | €20.000–€500.000+ | 3–12 maanden |
| Freelancer | €5.000–€20.000 | 1–3 maanden |
| AI-prototype + [LaunchStudio](https://launchstudio.eu/en/) | €800–€7.500 | 1–3 weken |

LaunchStudio, aangedreven door [Manifera's](https://www.manifera.com/) engineeringteams die werken vanuit 100 Tras Street in Singapore en ontwikkelcentra in Vietnam, is gespecialiseerd in dit werk — ongeveer 20% van wat een traditionele bureau-herbouw kost, omdat we nooit de 60-70% van de app die AI al correct heeft gebouwd opnieuw doen. We herontwerpen uw frontend niet. We stellen uw productbeslissingen niet ter discussie. We voegen de zeven lagen van productie-infrastructuur toe zodat uw met AI gebouwde product veilig echte gebruikers kan bedienen.

## Wat "80% van de AI-Projecten Bereikt Nooit Productie" Echt Betekent

Het vaak geciteerde cijfer dat 80% van de met AI gebouwde projecten nooit productie bereikt, gaat er niet om dat oprichters hun idee opgeven. In LaunchStudio's ervaring bij het beoordelen van prototypes gaat het erom dat oprichters op precies één van de zeven bovenstaande gaten stuiten en aannemen dat het hele prototype onbruikbaar is. Een ontbrekend RLS-beleid voelt als "mijn database is kapot." Een blootgestelde API-sleutel voelt als "mijn hele app is onveilig." In werkelijkheid zijn beide in enkele dagen op te lossen.

## Belangrijkste Inzichten

- Door AI gegenereerde code verzorgt 60-70% van het werk dat nodig is om een product te lanceren — voornamelijk UI, routing en state-beheer.
- De resterende 30-40% — beveiliging, foutafhandeling, monitoring en deployment-infrastructuur — scheidt een demo van een product.
- Het dichten van de kloof vereist geen herbouw, maar gerichte productie-engineering op zeven specifieke gebieden.
- LaunchStudio voert dit werk uit in 1-3 weken tegen ongeveer 20% van de kosten van een traditioneel bureau.

## Echt Voorbeeld

### Een AI-Native Oprichter in Actie: Het Logistieke Dashboard

Priya, een supply chain manager bij een middelgroot logistiek bedrijf in Singapore, bouwde in één weekend een vlootvolgdashboard met **Lovable**. Het dashboard haalde GPS-data op uit een API, toonde voertuiglocaties op een interactieve kaart en genereerde schattingen van levertijden.

Haar manager was onder de indruk van de demo. Het bedrijf keurde een pilot goed met 15 chauffeurs.

Op dag twee van de pilot stelde het dashboard de realtime locatie van elke chauffeur bloot aan elke andere chauffeur — inclusief chauffeurs van een concurrerende logistieke partner die dezelfde API deelden. De Supabase-database had geen Row Level Security. Erger nog, de Google Maps API-sleutel was ingebed in de frontend JavaScript. Binnen 48 uur was de API-quota van het bedrijf uitgeput door ongeautoriseerde externe verzoeken.

**LaunchStudio (door Manifera)** pakte alle zeven productiekloven aan in Priya's dashboard: omgevingsvariabelen voor alle API-sleutels, RLS-beleid dat vlootgegevens per bedrijf isoleerde, httpOnly cookie-gebaseerde authenticatie met kortstondige tokens, snelheidsbeperking op API-eindpunten, foutmonitoring via Sentry, build-optimalisatie die de JavaScript-bundel met 72% verminderde, en uptime-monitoring met automatische waarschuwingen.

**Resultaat:** De pilot werd uitgebreid naar 45 chauffeurs over drie logistieke partners. Elke partner ziet alleen zijn eigen vlootgegevens. Het dashboard heeft over drie maanden een uptime van 99,8% behouden. *"Het Lovable-prototype gaf ons groen licht. LaunchStudio maakte er iets van dat we daadwerkelijk konden vertrouwen in onze operaties."*

**Kosten & Doorlooptijd:** €3.200 (Launch & Grow-pakket) + €49/maand hosting — afgerond in 8 werkdagen.

---

## Veelgestelde Vragen (FAQ)

### 1. Moet door AI gegenereerde code volledig worden herschreven voor productie?
Nee. Door AI gegenereerde frontend-code — met name van tools zoals Lovable, Cursor en Bolt — levert goed gestructureerde code op die geschikt is voor productie. Wat moet worden toegevoegd is de infrastructuurlaag: beheer van omgevingsvariabelen, database-beveiligingsbeleid, foutafhandeling, authenticatiehardening, snelheidsbeperking en deployment-optimalisatie. LaunchStudio behoudt uw frontend en voegt alleen deze productielagen toe.

### 2. Welke AI-codingtool levert de meest productieklare output op?
Cursor levert over het algemeen de meest productiebewuste code op omdat het werkt als een AI-ondersteunde IDE in plaats van een volledige codegenerator. Lovable blinkt uit in volledige UI-generatie maar vereist meer backend-hardening. Bolt is het snelst voor prototyping maar heeft doorgaans het meeste werk nodig op alle zeven kloofgebieden. Alle drie leveren code op die LaunchStudio naar productierijpheid kan brengen.

### 3. Hoe draagt Manifera's Singapore-hub bij aan LaunchStudio-projecten?
Manifera onderhoudt een Aziatische hub aan 100 Tras Street in Singapore die dient als coördinatiepunt voor oprichters in Zuidoost-Azië. Voor projecten uit die regio biedt de Singapore-hub communicatie in de lokale tijdzone, terwijl de uitvoering plaatsvindt via Manifera's primaire ontwikkelcentrum in Ho Chi Minh City — wat zowel toegankelijkheid als diepe technische capaciteit garandeert.

### 4. Wat is het meest gevaarlijke beveiligingsgat in door AI gegenereerde code?
Blootgestelde API-sleutels in frontend JavaScript vertegenwoordigen de meest direct misbruikbare kwetsbaarheid. Anders dan ontbrekend RLS-beleid (dat authenticatie vereist om te misbruiken), kunnen blootgestelde API-sleutels door iedereen worden verzameld die de paginabron bekijkt. Aanvallers kunnen uw sleutels gebruiken om op uw kosten onbeperkt API-aanroepen te doen.

### 5. Kan ik blijven bouwen met AI-tools nadat LaunchStudio mijn app productie-klaar heeft gemaakt?
Absoluut. LaunchStudio zorgt ervoor dat alle code AI-leesbaar en compatibel blijft met Lovable, Cursor en Bolt. Uw productie-infrastructuur is netjes gescheiden van uw frontend-code, wat betekent dat u kunt blijven itereren op functies met AI-tools zonder de beveiligingslagen die LaunchStudio heeft geïmplementeerd te verbreken. U bezit 100% van de code.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Moet door AI gegenereerde code volledig worden herschreven voor productie?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Nee. AI-gegenereerde frontend-code is goed gestructureerd en geschikt voor productie. Wat moet worden toegevoegd is de infrastructuurlaag: omgevingsvariabelen, database-beveiliging, foutafhandeling, auth-hardening, snelheidsbeperking en deployment-optimalisatie."
      }
    },
    {
      "@type": "Question",
      "name": "Welke AI-codingtool levert de meest productieklare output op?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Cursor levert over het algemeen de meest productiebewuste code op. Lovable blinkt uit in UI-generatie maar vereist meer backend-hardening. Bolt is het snelst voor prototyping. Alle drie leveren code die LaunchStudio naar productierijpheid kan brengen."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe draagt Manifera's Singapore-hub bij aan LaunchStudio-projecten?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Manifera's hub aan 100 Tras Street in Singapore biedt communicatie in de lokale tijdzone voor oprichters in Zuidoost-Azië, terwijl uitvoering plaatsvindt via het primaire ontwikkelcentrum in Ho Chi Minh City."
      }
    },
    {
      "@type": "Question",
      "name": "Wat is het meest gevaarlijke beveiligingsgat in door AI gegenereerde code?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Blootgestelde API-sleutels in frontend JavaScript. Anders dan ontbrekend RLS-beleid kunnen blootgestelde API-sleutels door iedereen worden verzameld die de paginabron bekijkt en gebruikt worden voor onbeperkte aanroepen op uw kosten."
      }
    },
    {
      "@type": "Question",
      "name": "Kan ik blijven bouwen met AI-tools nadat LaunchStudio mijn app productie-klaar heeft gemaakt?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ja. LaunchStudio zorgt ervoor dat alle code AI-leesbaar en compatibel blijft met Lovable, Cursor en Bolt. Productie-infrastructuur is netjes gescheiden van frontend-code, dus u kunt blijven itereren met AI-tools."
      }
    }
  ]
}
</script>
