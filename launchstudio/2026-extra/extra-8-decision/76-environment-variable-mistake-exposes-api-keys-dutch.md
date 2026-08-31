---
Titel: "De Environment Variable-Fout Die Elke API-Sleutel in Uw Frontend Blootlegt"
Trefwoorden: environment variable beveiliging, API-sleutel blootgesteld frontend, next public env variable, client-side API-sleutel lek, veilige environment variables, LaunchStudio, Manifera
Koperfase: Beslissing
Doelgroep: Technische Solo-Oprichter / Indie Hacker
---

# De Environment Variable-Fout Die Elke API-Sleutel in Uw Frontend Blootlegt

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "De Environment Variable-Fout Die Elke API-Sleutel in Uw Frontend Blootlegt",
  "description": "Uw OpenAI-sleutel, uw Stripe secret, uw databasewachtwoord — als een van deze begint met NEXT_PUBLIC_ of VITE_, staan ze in uw frontend-bundel, zichtbaar voor iedereen die de developer tools van de browser opent. Hier is de oplossing.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2026-12-31",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/environment-variable-mistake-exposes-api-keys" }
}
</script>

Open uw browser. Navigeer naar uw live applicatie. Druk op F12. Klik op het tabblad "Sources". Zoek naar "sk_" of "key" of "secret" in alle geladen bestanden. Als u uw Stripe secret key, uw OpenAI API-sleutel, uw databaseverbindingsstring of een andere credential ingebed vindt in een JavaScript-bestand, heeft u zojuist de meest voorkomende en gevaarlijkste beveiligingsfout in AI-gegenereerde applicaties gedemonstreerd — en iedereen die uw site bezoekt kan exact dezelfde zoekopdracht uitvoeren.

## Hoe de Fout Ontstaat

In Next.js worden environment variables met het voorvoegsel `NEXT_PUBLIC_` gebundeld in de client-side JavaScript en zijn ze toegankelijk in de browser. In Vite (dat Lovable gebruikt) zijn variabelen met het voorvoegsel `VITE_` op vergelijkbare wijze blootgesteld. Deze voorvoegsels bestaan voor een legitiem doel: het delen van niet-gevoelige configuratie (de URL van uw app, een publieke analytics-ID, een Supabase anon key) met de frontend. Het probleem is dat AI-tools — die .env-bestanden genereren op basis van wat de code moet benaderen — gevoelige credentials vaak voorzien van `NEXT_PUBLIC_` of `VITE_` omdat de AI ziet dat de credential wordt gebruikt in een frontend-component en besluit dat deze beschikbaar moet zijn in de browser. De logica van de AI is technisch correct (de code verwijst inderdaad naar de variabele in de browser) en catastrofaal fout (de credential had daar nooit mogen staan).

## Wat Er Werkelijk Wordt Blootgelegd

De credentials die het vaakst worden aangetroffen in frontend-bundels van AI-gegenereerde applicaties zijn: **Stripe secret keys** (waarmee iedereen kosten in rekening kan brengen, terugbetalingen kan aanmaken en toegang heeft tot klantgegevens in uw Stripe-account), **OpenAI API-sleutels** (waarmee iedereen API-calls kan maken die aan uw account worden gefactureerd), **databaseverbindingsstrings** (waarmee directe databasetoegang mogelijk is, buiten uw applicatie om), **e-maildienst API-sleutels** (waarmee iedereen e-mails kan versturen vanaf uw domein) en **secrets van externe diensten** (elke API-sleutel die alleen server-side hoorde te zijn, maar werd voorzien van een client-toegankelijk voorvoegsel). Elk hiervan vertegenwoordigt een andere categorie schade — van financieel verlies (ongeautoriseerde API-kosten) tot datalekken (directe databasetoegang) tot reputatieschade (e-mails verstuurd vanaf uw domein door aanvallers).

## De Oplossing Is Architecturaal, Niet Cosmetisch

De oplossing is niet het hernoemen van de variabele — het is het herstructureren van waar de code die de credential gebruikt, draait. Gevoelige API-calls (OpenAI, Stripe-charges, databaseschrijfacties) moeten op de server gebeuren, niet in de browser. De frontend stuurt een verzoek naar uw server-side API-endpoint, en het API-endpoint — dat op de server draait en toegang heeft tot environment variables zonder het voorvoegsel `NEXT_PUBLIC_` of `VITE_` — voert de daadwerkelijke API-call uit met de geheime credential. De browser ziet de sleutel nooit, bundelt hem nooit en legt hem nooit bloot. Dit patroon (API-route als proxy) is standaard in productieapplicaties, maar ontbreekt vaak in AI-gegenereerde code omdat de AI-tool prioriteit geeft aan het werkend krijgen van de functie boven het correct inrichten van het beveiligingsmodel.

Voor Next.js betekent dit het verplaatsen van gevoelige API-calls naar API-routes (de map `/app/api/`). Voor Vite-applicaties betekent het toevoegen van een backend-server (Express, Hono of een serverless functie) die de gevoelige operaties afhandelt. De frontend roept uw API aan; uw API roept de externe dienst aan. De credential blijft op de server.

[LaunchStudio](https://launchstudio.eu/nl/) controleert elke environment variable in uw prototype en verplaatst gevoelige credentials naar de server — Manifera's engineers hebben blootgestelde sleutels aangetroffen in de meerderheid van de AI-gegenereerde codebases die zij hebben beoordeeld.

[Stuur ons uw repository en wij vertellen u welke credentials momenteel zichtbaar zijn in uw frontend](https://launchstudio.eu/nl/#contact) — de check duurt enkele minuten, en de oplossing voorkomt de meest voorkomende beveiligingsinbreuk in AI-gegenereerde applicaties.

## Praktijkvoorbeeld

### Een AI-Native Oprichter in de Praktijk: De API-Sleutel Die Zichtbaar Was Voor Elke Bezoeker

Kasper van Dijk, een indie hacker in Leiden, bouwde KenMerk, een met Cursor gebouwde merkanalysetool die OpenAI's API gebruikte om websiteteksten te analyseren en merkpositioneringsrapporten te genereren. Een betatester merkte terloops op: "Trouwens, ik kan uw OpenAI-sleutel zien in de paginabron." Kasper controleerde het — zijn `VITE_OPENAI_API_KEY` stond ingebed in de gecompileerde JavaScript-bundel, leesbaar voor iedereen die de site bezocht.

In de drie weken dat de sleutel blootgesteld was geweest, had iemand (of een bot) hem gebruikt om voor $340 aan ongeautoriseerde OpenAI-kosten te genereren. Kasper roteerde de sleutel onmiddellijk, maar wist niet hoe hij de code moest herstructureren om dezelfde fout met een nieuwe sleutel te voorkomen.

Het Manifera-team van LaunchStudio herstructureerde KenMerks OpenAI-integratie: de frontend roept nu een Supabase Edge Function aan (server-side), die de OpenAI-sleutel bewaart in server-only environment variables en het API-verzoek doorgeeft. De frontend ziet de sleutel nooit. Daarnaast controleerde het team alle andere environment variables en verplaatste drie extra credentials (een SendGrid API-sleutel, een databaseadmin-wachtwoord en een webhook signing secret) van client-voorvoegsels naar server-only variabelen.

**Resultaat:** Nul credentials blootgesteld in de frontend-bundel. De $340 aan ongeautoriseerde kosten was de totale prijs van de les — en de herstructurering die toekomstige blootstelling voorkwam, kostte minder dan de ongeautoriseerde kosten zelf.

> *"Ik wist niet dat VITE_ 'zichtbaar voor iedereen' betekende. Ik dacht dat het 'dit is een Vite-project' betekende. Drie weken lang stond mijn API-sleutel publiek, wat me $340 kostte en me een les leerde die ik had moeten leren vóór de lancering."*
> — **Kasper van Dijk, Oprichter, KenMerk (Leiden)**

**Kosten & Doorlooptijd:** €900 (Launch Ready Pakket, audit van environment variables + herstructurering API-routes) — live in 3 werkdagen.

---

## Veelgestelde Vragen

### Hoe controleer ik nu meteen of mijn API-sleutels blootgesteld zijn in mijn frontend?
Bezoek uw live site, open de browser DevTools (F12), ga naar het tabblad Sources en zoek naar fragmenten van uw API-sleutels (bijvoorbeeld de eerste paar tekens van uw OpenAI-sleutel). Als u ze vindt, zijn ze blootgesteld.

### Hoort de Supabase anon key wel in de frontend te staan?
Ja — de Supabase anon key is ontworpen om publiek te zijn. Deze wordt gebruikt voor client-side queries en is veilig om bloot te stellen omdat Row-Level Security-beleid (niet de sleutel) de datatoegang regelt. Secret keys (service_role) mogen nooit in de frontend staan.

### Als ik het NEXT_PUBLIC_-voorvoegsel verwijder, blijft mijn frontend-code die de variabele gebruikt dan werken?
Nee — dat is precies het punt. De code die de variabele gebruikt, moet worden verplaatst naar een server-side API-route. De frontend roept uw API-route aan in plaats van de externe API-call rechtstreeks te maken.

### Kan iemand die mijn blootgestelde API-sleutel vindt toegang krijgen tot mijn klantgegevens?
Dat hangt af van de sleutel. Een Stripe secret key geeft volledige toegang tot uw Stripe-account, inclusief klantgegevens, charges en terugbetalingen. Een OpenAI-sleutel geeft de mogelijkheid om API-calls te maken op uw account. Een databaseverbindingsstring geeft directe databasetoegang tot alle gegevens.

### Hoe snel wordt een gelekte API-sleutel misbruikt?
Geautomatiseerde bots scannen continu publieke GitHub-repositories en live applicaties op blootgestelde credentials. Een sleutel die naar een publieke repo wordt gepusht of in een frontend-bundel wordt gedeployed, kan binnen minuten tot uren na blootstelling worden misbruikt.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "Hoe controleer ik nu meteen of mijn API-sleutels blootgesteld zijn in mijn frontend?", "acceptedAnswer": { "@type": "Answer", "text": "Bezoek uw live site, open de browser DevTools (F12), ga naar het tabblad Sources en zoek naar fragmenten van uw API-sleutels. Als u ze vindt, zijn ze blootgesteld." } },
    { "@type": "Question", "name": "Hoort de Supabase anon key wel in de frontend te staan?", "acceptedAnswer": { "@type": "Answer", "text": "Ja — de anon key is ontworpen om publiek te zijn. Row-Level Security-beleid regelt de datatoegang, niet de sleutel. Secret keys (service_role) mogen nooit in de frontend staan." } },
    { "@type": "Question", "name": "Als ik het NEXT_PUBLIC_-voorvoegsel verwijder, blijft mijn frontend-code dan werken?", "acceptedAnswer": { "@type": "Answer", "text": "Nee — de code moet worden verplaatst naar een server-side API-route. De frontend roept uw API-route aan in plaats van de externe API-call rechtstreeks te maken." } },
    { "@type": "Question", "name": "Kan iemand die mijn blootgestelde API-sleutel vindt toegang krijgen tot mijn klantgegevens?", "acceptedAnswer": { "@type": "Answer", "text": "Dat hangt af van de sleutel. Een Stripe secret key geeft volledige toegang tot uw Stripe-account. Een OpenAI-sleutel geeft de mogelijkheid om API-calls te maken. Een databaseverbindingsstring geeft directe databasetoegang." } },
    { "@type": "Question", "name": "Hoe snel wordt een gelekte API-sleutel misbruikt?", "acceptedAnswer": { "@type": "Answer", "text": "Geautomatiseerde bots scannen continu. Een sleutel die in een frontend-bundel wordt gedeployed, kan binnen minuten tot uren worden misbruikt." } }
  ]
}
</script>
