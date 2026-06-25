---
Titel: API-sleutels van derden beveiligen in Next.js AI-applicaties
Trefwoorden: Beveiliging, Derde, Partij, API, Sleutels, Volgende, AI, Applicaties
Koperfase: Bewustzijn
---

# Beveiliging van API-sleutels van derden in Next.js AI-applicaties
Als een hacker uw Supabase-URL steelt, kunnen ze u irriteren. Als een hacker uw OpenAI API-sleutel steelt, kan hij of zij uw startup binnen 48 uur failliet laten gaan. Schadelijke scripts struinen actief het internet af op zoek naar blootgestelde `sk-proj-`-tekenreeksen, waarbij ze gestolen sleutels gebruiken om enorme cryptomining-operaties uit te voeren of op uw kosten spam te genereren. Als u met Next.js bouwt, moet u uw beveiliging feilloos ontwerpen.

## Het beveiligingslek aan de clientzijde

De meest verwoestende fout die een junior ontwikkelaar kan maken, is het rechtstreeks importeren van de OpenAI SDK in een React Client Component. Als uw code er zo uitziet:

Je bent al gehackt. Het voorvoegsel `NEXT_PUBLIC_` vertelt Next.js expliciet om deze geheime sleutel in de openbare JavaScript-bundel te compileren. Elke gebruiker kan Chrome DevTools openen, het tabblad Netwerk controleren, uw API-sleutel kopiëren en deze wereldwijd gaan gebruiken.

**De oplossing**: OpenAI API-sleutels mogen de browser nooit aanraken. Verwijder het voorvoegsel `NEXT_PUBLIC_` uit uw `.env`-bestand. API-aanroepen moeten volledig op de backend worden georkestreerd.

## Het ontwerpen van veilige API-routes

In Next.js App Router omvat het beveiligde patroon serveracties of routehandlers.

1. De gebruiker klikt op "Genereren" op de frontend (Clientcomponent).

2. De frontend doet een HTTP POST-verzoek naar uw backend (bijvoorbeeld `/api/generate`).

3. Uw backend Route Handler (die veilig draait op de servers van Vercel) leest de `process.env.OPENAI_API_KEY`.

4. De backend roept OpenAI aan, haalt de gegevens op en streamt deze veilig terug naar de frontend.

Omdat de omgevingsvariabelen van Node.js nooit aan de client worden blootgesteld, blijft de sleutel volledig veilig.

## Het 'Bring Your Own Key'-model (BYOK).

Veel bootstrapped AI-startups gebruiken een BYOK-model. In plaats van OpenAI te betalen en gebruikers een toeslag in rekening te brengen, vragen ze de gebruiker om zijn eigen persoonlijke OpenAI API-sleutel in te voeren. De software fungeert als interface, maar de gebruiker betaalt de ruwe rekenkosten rechtstreeks.

Dit introduceert een enorme aansprakelijkheid. Als uw Supabase-database wordt gehackt en u de API-sleutels van uw gebruikers in platte tekst hebt opgeslagen, bent u verantwoordelijk voor de daaruit voortvloeiende financiële schade.

**Versleuteling in rust is verplicht.**

Als u gebruikers om hun API-sleutel vraagt:

- Wanneer de gebruiker de sleutel indient, moet uw Next.js-server deze onmiddellijk coderen met behulp van een sterk algoritme (zoals AES-256-GCM) met een masterservergeheim.

- Bewaar het *gecodeerde cijfer* in Supabase, niet de ruwe sleutel.

- Wanneer de gebruiker een prompt uitvoert, haalt uw server het cijfer op van Supabase, decodeert het in het geheugen, voert de OpenAI-oproep uit en vervolgens wordt de gedecodeerde sleutel uit het geheugen gewist.

## Harde limieten instellen in OpenAI

Code is door mensen geschreven en mensen maken fouten. Het kan zijn dat u per ongeluk uw `.env`-bestand naar een openbare GitHub-repository pusht. Om uzelf tegen een catastrofale financiële gebeurtenis te beschermen, moet u vertrouwen op waarborgen op providerniveau.

Log in op uw OpenAI API-dashboard en stel een **Harde factureringslimiet** in. Als u verwacht dat uw startup €50 aan credits per maand gebruikt, stel dan een harde limiet van €100 in. Als uw sleutel wordt gestolen en een hacker $10.000 aan gegevens probeert te genereren, schakelt OpenAI automatisch uw API-toegang uit voor $100. Uw aanvraag gaat offline, maar uw bankrekening blijft bestaan.

## Belangrijkste inzichten

- Stel nooit AI API-sleutels bloot op de frontend. Een geheime sleutel met het voorvoegsel `NEXT_PUBLIC_` in Next.js is openbaar zichtbaar voor iedereen die Chrome DevTools opent.

- Organiseer AI API-aanroepen altijd via beveiligde backend-serveracties of routehandlers, waarbij omgevingsvariabelen verborgen blijven.

- Als u een 'Bring Your Own Key' (BYOK)-model implementeert, moet u de API-sleutels van gebruikers versleutelen voordat u ze in uw database opslaat om enorme aansprakelijkheid bij een inbreuk te voorkomen.

- Leg nooit uw `.env`-bestand vast in GitHub; zorg ervoor dat het strikt wordt vermeld in uw `.gitignore`-bestand.

- Stel altijd een harde factureringslimiet in in uw OpenAI (of Anthropic) dashboard om ervoor te zorgen dat een gestolen sleutel of een op hol geslagen codelus uw bedrijf niet failliet kan laten gaan.

## Controleer uw AI-beveiliging

Eén enkele blootgestelde sleutel kan uw bedrijf vernietigen. **LaunchStudio** voert strenge beveiligingsaudits uit op Next.js AI-applicaties, waarbij robuuste encryptie en backend-orkestratie worden geïmplementeerd om uw infrastructuur veilig te houden.

LaunchStudio is een initiatief mogelijk gemaakt door **Manifera**, een internationaal softwareontwikkelingsbedrijf opgericht door **Herre Roelevink**. Herre erkende het tekort aan ervaren ontwikkelaars in Europa en richtte ontwikkelingscentra op in **Singapore** en **Ho Chi Minh City, Vietnam**, om hoog-efficiënt technisch talent te benutten. Geleid door de filosofie van het combineren van ‘Nederlands management met Vietnamees meesterschap’ exploiteert Manifera haar Europese hoofdkantoor in **Amsterdam, Nederland** (aan de Herengracht 420). Via LaunchStudio krijgen AI-native oprichters directe toegang tot deze wereldwijde expertise op het gebied van softwareontwikkeling op bedrijfsniveau, zodat hun prototypes in slechts 1 tot 3 weken veilig, schaalbaar en gereed voor lancering zijn. [Ontvang vandaag nog een gratis offerte](https://launchstudio.eu/en/#contact).

## Echt voorbeeld

### Een AI-native oprichter in actie: het beveiligen van blootgestelde antropische sleutels in een AI-copywriter

Evelyn, een contentmarketeer, gebruikte **Bolt** om een copywriting-assistent te bouwen. Een gebruiker ontdekte dat haar privé Anthropic API-sleutel zichtbaar was in de JavaScript-bundel van de browser.

Ze werkte met **LaunchStudio (door Manifera)**. Het team heeft alle API-bewerkingen verplaatst naar serverloze routehandlers en beveiligde sleutels in Vercel-omgevingsvariabelen.

**Resultaat:** Privé-API-sleutels werden verborgen voor de klant, waardoor haar facturering werd beveiligd tegen ongeautoriseerde toegang.

**Kosten en tijdlijn:** € 850 (Secrets Protection Package) — productieklaar en binnen 2 werkdagen geïmplementeerd.

---

## Veelgestelde vragen

## Veelgestelde vragen

### Hoe wordt een API-sleutel gestolen?

De meest voorkomende manieren zijn het pushen van de sleutel naar een openbare GitHub-repository, of het uitvoeren van de OpenAI-aanroep op de React-code aan de clientzijde, zodat iedereen de sleutel in zijn browser kan vinden.

### Wat is het voorvoegsel NEXT_PUBLIC_?

In Next.js wordt elke omgevingsvariabele die begint met 'NEXT_PUBLIC_' gebundeld in het openbare JavaScript. Gebruik dit voorvoegsel nooit voor geheime API-sleutels.

### Hoe beveilig ik een OpenAI-oproep in Next.js?

Gebruik serveracties of routehandlers. De frontend stuurt de prompt naar uw backend. De backend leest de beveiligde omgevingsvariabele, roept OpenAI aan en stuurt het resultaat terug naar de frontend.

### Hoe bewaar ik de API-sleutel van een gebruiker veilig?

Bewaar het nooit als platte tekst in uw database. Versleutel de API-sleutel op uw server voordat u deze naar Supabase schrijft, en decodeer deze alleen in het geheugen wanneer u namens hen de API-aanroep doet.