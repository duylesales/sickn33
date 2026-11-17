---
Titel: "Case Study: Multi-Tenant RLS Implementeren om Uw Zorg AI Database te Beveiligen"
Trefwoorden: Case study healthcare AI, Supabase RLS multi-tenant, medische data privacy, NEN 7510, LaunchStudio, Manifera
Koperfase: Beslissing
Doelgroep: HealthTech Founders / Security Engineers
---

# Case Study: Multi-Tenant RLS Implementeren om Uw Zorg AI Database te Beveiligen

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Case Study: Multi-Tenant RLS Implementeren om Uw Zorg AI Database te Beveiligen",
  "description": "Hoe een medische AI-startup in Utrecht voldeed aan NEN 7510 en AVG door waterdichte Supabase Row Level Security in te voeren.",
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
  "datePublished": "2026-08-57",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://launchstudio.eu/nl/blog/case-study-slashing-customer-support-costs-80-ai"
  }
}
</script>

Voor snelgroeiende technologiebedrijven is de klantenservice vaak het slachtoffer van het eigen commerciële succes. Hoe sneller het aantal actieve gebruikers groeit, hoe sneller de support-wachtrij ontploft - wat bedrijven dwingt om continu nieuwe eerstelijns supportmedewerkers aan te nemen om te voorkomen dat de reactietijden instorten. Deze casestudy beschrijft hoe LaunchStudio een Series B FinTech startup ("PayFlow") hielp deze lineaire kostenexplosie te doorbreken door een geavanceerde Retrieval-Augmented Generation (RAG) agent te implementeren, waarmee **62% van de supporttickets volledig autonoom werd opgelost** en jaarlijks **$ 800.000 aan loonkosten werd bespaard**.

## De Crisis: De Lawine aan Eerstelijns Supporttickets

PayFlow levert een betalingsgateway voor e-commerce via API's. Toen het platform de grens van 100.000 aangesloten webwinkels passeerde, explodeerde de Zendesk-wachtrij naar 1.500 tickets per dag. Meer dan 70% van deze tickets betrof repetitieve eerstelijns (Tier 1) vragen: *"Hoe reset ik mijn API-sleutel?"*, *"Waarom faalt deze betaling met Foutcode 402?"*, of *"Wat is het retry-beleid voor mislukte uitbetalingen?"* - vragen met een eenduidig antwoord dat simpelweg opgezocht moest worden in de documentatie.

PayFlow had eerder traditionele beslisboom-chatbots geprobeerd. Dat was een drama. Als een gebruiker ook maar minimaal afweek van het voorgeprogrammeerde script, faalde de bot en werd het ticket alsnog geëscaleerd naar een menselijke medewerker (een escalatieratio van 95%). Klanten raakten gefrustreerd en de kosten bleven onverminderd hoog.

## De Oplossing: De Semantische RAG-Support-Agent

Wij vervingen de rigide beslisboom door een volwaardige semantische RAG-architectuur die documentatie begrijpend leest:

1. **Data-Inname en Vectorisatie:** We vectoriseerden PayFlow's complete 500-pagina's tellende documentatiewebsite, hun interne Notion-kennisbank en de transcripts van 50.000 eerder succesvol opgeloste Zendesk-tickets. Deze data werd opgeknipt in semantische chunks en opgeslagen in een Pinecone vectordatabase met metadata over documentversies.
2. **De Agent-Workflow:** Zodra een merchant een vraag intypt, converteert de backend de vraag in een embedding-vector en zoekt Pinecone naar conceptueel overeenkomstige documenten (zodat "waarom werd mijn betaling geweigerd" en "Foutcode 402 troubleshooting" exact dezelfde brondocumenten opleveren).
3. **LLM-Synthese:** Een snel model met lage latentie (Claude 3.5 Haiku) analyseert de opgehaalde documenten en formuleert direct een helder, conversationeel antwoord op maat, inclusief een klikbare bronverwijzing naar de officiële documentatie.

## De Cruciale Pijler: Een Zero-Hallucinatie Architectuur

In de financiële sector is het hallucineren van foutieve antwoorden over transacties een onaanvaardbaar risico. We losten dit op met een strikte systeemprompt en betrouwbaarheidsscores:

**Systeemprompt:** *"Je bent een technische support engineer. Beantwoord de vraag UITSLUITEND op basis van de meegeleverde brondocumenten. Bevatten de documenten niet het exacte antwoord, of is je betrouwbaarheidsscore lager dan 90%, retourneer dan uitsluitend de exacte term: 'ESCALATE_TO_HUMAN'."*

Zodra de AI deze term retourneerde, stuurde de backend het ticket geruisloos door naar een menselijke Zendesk-medewerker, inclusief het volledige gespreksverloop. De klant ervoer geen haperende bot, maar een vloeiende overdracht naar een menselijke specialist die direct over alle context beschikte.

## De ROI en Zakelijke Resultaten

Het systeem werd gelanceerd bij 10% van de gebruikers en na twee weken van strenge kwaliteitsmonitoring wereldwijd uitgerold:

- **Deflection Rate:** De AI loste **62% van alle inkomende supporttickets volledig zelfstandig op**, zonder tussenkomst van een menselijke medewerker.
- **Oplostijd:** De gemiddelde doorlooptijd voor eerstelijnstickets daalde van 4,5 uur wachttijd naar slechts **8 seconden** (24/7 realtime beschikbaar).
- **Directe Besparing:** PayFlow schrapte de geplande aanname van 12 extra supportmedewerkers, wat een **directe jaarlijkse besparing van $ 800.000** opleverde.
- **Klanttevredenheid (CSAT):** De CSAT-score steeg met **15%**. Klanten kregen liever binnen 8 seconden een accuraat AI-antwoord met bronverwijzing dan urenlang te wachten op een menselijke reactie.

Ongeveer 45% van de AI-gegenereerde code bevat kwetsbaarheden; professionele RAG-architecturen vereisen strenge beveiliging en autorisatielagen alvorens ze met productiedatabases communiceren. Manifera bouwt deze enterprise-systemen sinds **2014**, met 160+ gerealiseerde projecten voor onder meer Vodafone en TNO vanuit haar Europese hoofdkantoor aan de Herengracht 420 in Amsterdam. Zoals Herre Roelevink, Oprichter & Managing Director van Manifera, stelt: "We zien een verschuiving in softwarebehoeften. De uitdaging is niet langer om goede ideeën om te zetten in software. Het gaat nu om de architectuur en beveiliging die nodig zijn om die producten naar volwassenheid te brengen. Wij hebben elf jaar ervaring in exact dat vakgebied." Bekijk Manifera's [maatwerk softwareontwikkeling diensten](https://www.manifera.com/services/custom-software-development/).

## Wat Is een RAG-Support-Agent?

Een RAG-support-agent is een AI-assistent die klantvragen beantwoordt door eerst relevante passages op te halen uit uw eigen documentatie en opgeloste tickets, en vervolgens een taalmodel te vragen een antwoord te schrijven dat uitsluitend op die passages is gebaseerd. Retrieval-Augmented Generation houdt het antwoord verankerd in de werkelijke kennis van uw bedrijf, in plaats van in de algemene trainingsdata van het model.

Het verschil met eerdere benaderingen wordt het duidelijkst naast elkaar:

| Aanpak | Hoe het antwoordt | Kan onverwachte formuleringen aan | Risico op hallucinatie | Typisch resultaat |
|---|---|---|---|---|
| Beslisboom-chatbot | Volgt een vooraf geschreven menu of script | Nee | Laag, maar zelden nuttig | Hoge escalatieratio, gefrustreerde gebruikers |
| Generieke LLM-chatbot | Antwoordt vanuit de algemene kennis van het model | Ja | Hoog | Vloeiende antwoorden die over uw product onjuist kunnen zijn |
| RAG-agent met escalatie | Haalt uw documenten op, antwoordt alleen daaruit, escaleert bij twijfel | Ja | Laag, mits betrouwbaarheidsdrempels worden afgedwongen | Echte deflectie met een veilige menselijke terugvaloptie |

De derde rij is wat PayFlow in productie nam. De escalatieregel is net zo belangrijk als de retrieval: een RAG-agent die niet kan zeggen "dat weet ik niet", is nog steeds een generieke chatbot met beter bronmateriaal.

## Hoe Implementeert U een RAG-Support-Agent? Stap voor Stap

De snelste veilige route naar een AI-support-agent begint bij uw bestaande tickethistorie, niet bij het model. Een praktische implementatievolgorde ziet er zo uit:

1. **Analyseer uw ticketcategorieën.** Exporteer enkele maanden aan tickets uit Zendesk of Intercom en groepeer ze op intentie. De categorieën die vaak voorkomen, repetitief zijn en al gedocumenteerd zijn, vormen uw eerste deflectiedoelen.
2. **Schoon de kennisbank op.** Verwijder verouderde artikelen, voeg dubbele artikelen samen en voorzie elk document van een datum van laatste controle. Retrieval kan nooit nauwkeuriger zijn dan de content die wordt opgehaald.
3. **Knip op en embed.** Splits documenten in samenhangende secties, genereer embeddings en sla ze op in een vectordatabase zoals Pinecone of pgvector, met metadata over productonderdeel, actualiteit en zichtbaarheid voor klanten.
4. **Schrijf de grounding-prompt.** Instrueer het model om alleen te antwoorden op basis van de opgehaalde context, de bron te vermelden en een vaste escalatieterm terug te geven wanneer de context onvoldoende is.
5. **Bouw het geruisloze escalatiepad.** Stuur geëscaleerde gesprekken door naar een menselijke wachtrij, met het volledige transcript en de opgehaalde documenten als bijlage, zodat de medewerker nooit opnieuw hoeft te beginnen.
6. **Draai in schaduwmodus.** Laat de AI conceptantwoorden opstellen die menselijke medewerkers beoordelen maar niet versturen. Vergelijk die concepten met wat de medewerkers daadwerkelijk schreven.
7. **Rol geleidelijk uit.** Lanceer bij een klein deel van de gebruikers, zoals PayFlow deed met 10%, en verbreed pas wanneer deflectie, escalatienauwkeurigheid en CSAT stabiel blijven.
8. **Houd de lus draaiende.** Voer nieuw opgeloste tickets terug in de index en beoordeel elke week een steekproef van AI-antwoorden.

## AI-Beveiliging voor Support-Agents: Tenant-Isolatie en Row Level Security

Een support-agent die accountgegevens kan opzoeken, mag uitsluitend de data zien van de klant met wie hij op dat moment communiceert. In een multi-tenant AI SaaS is dat de belangrijkste beveiligingsmaatregel van het hele systeem, en die hoort te worden afgedwongen in de database, niet in de prompt.

Promptinstructies zoals "bespreek alleen het account van deze gebruiker" vormen geen beveiligingsgrens, omdat prompt injection ze kan omzeilen. De grens hoort in de datalaag:

- **Row Level Security (RLS).** In PostgreSQL, en in platforms die erop gebouwd zijn zoals Supabase, beperken RLS-policies elke query tot de rijen die bij de geauthenticeerde tenant horen. Zelfs als de tool-aanroep van de agent wordt gemanipuleerd, weigert de database de records van een andere tenant terug te geven.
- **Afgebakende credentials voor tools.** De agent hoort interne API's aan te roepen met een kortlevend token dat aan de huidige gebruiker is gekoppeld, nooit met een servicesleutel die alles kan lezen.
- **Gefilterde retrieval.** Gedeelde publieke documentatie kan in één index staan, maar klantspecifieke content moet worden gescheiden via een namespace of metadatafilter, zodat de tickets van de ene merchant nooit voor een andere worden opgehaald.
- **Redactie en logging.** Verwijder overbodige persoonsgegevens voordat ze het model bereiken, en log elke tool-aanroep voor audits.
- **Verwerkersverplichtingen.** Onder artikel 28 van de AVG (GDPR) zijn de modelaanbieder en de leverancier van de vectordatabase subverwerkers. Ze horen dus in uw verwerkersovereenkomsten en in de lijst met subverwerkers die u aan klanten toont.

Deze maatregelen maken van een slim prototype een AI-implementatie die een beveiligingsbeoordelaar in FinTech of de zorg daadwerkelijk goedkeurt.

### Wat betekent dit voor zorgtoepassingen en NEN 7510?

Voor Nederlandse zorgorganisaties komt daar een extra laag bij. NEN 7510 is de Nederlandse norm voor informatiebeveiliging in de zorg, en zorginstellingen verwachten doorgaans dat leveranciers die met patiëntgegevens werken aantoonbaar volgens die norm handelen. Gezondheidsgegevens vallen bovendien onder de bijzondere categorieën persoonsgegevens van artikel 9 van de AVG, waarvoor strengere eisen gelden. In de praktijk betekent dit voor een AI-support-agent in de zorg: tenant-isolatie via RLS is geen optie maar een vereiste, elke inzage in dossiergegevens wordt gelogd, gevoelige gegevens worden zoveel mogelijk weggelaten voordat ze een extern model bereiken, en u kunt per subverwerker uitleggen waar de data wordt verwerkt. Wie dit vanaf de eerste versie in de architectuur verwerkt, voorkomt dat een veelbelovende pilot strandt op de inkoop- of securitytoets van een ziekenhuis of zorggroep.

## Veelgemaakte Fouten bij het Inzetten van AI in de Klantenservice

De meeste mislukte AI-supportprojecten stranden op proces en data, niet op de keuze van het model. De terugkerende fouten zijn:

- **Alleen deflectie meten.** Een bot die tickets sluit doordat gebruikers gefrustreerd afhaken, ziet er prachtig uit in een deflectiegrafiek. Meet escalatienauwkeurigheid en CSAT ernaast.
- **Verouderde documentatie indexeren.** Als oude artikelen in de index blijven staan, herhaalt de agent vol overtuiging achterhaalde antwoorden.
- **De menselijke optie verbergen.** Klanten moeten altijd een mens kunnen bereiken. Een zichtbare overdrachtsmogelijkheid vergroot juist het vertrouwen in de AI-antwoorden.
- **De agent brede schrijfrechten geven.** Begin met alleen-lezen opzoekacties. Acties zoals terugbetalingen of accountwijzigingen vereisen expliciete toegangsscopes en in eerste instantie menselijke goedkeuring.
- **De beveiligingsreview overslaan.** Door AI gegenereerde integratiecode bevat vaak blootgestelde sleutels of ontbrekende autorisatiecontroles. Laat die code beoordelen voordat de agent productiedata aanraakt.

## Belangrijkste Inzichten

- Traditionele beslisboom-chatbots falen bij natuurlijke spreektaal en lossen support-overbelasting zelden structureel op.
- RAG-architecturen stellen AI in staat duizenden pagina's aan documentatie en historische tickets semantisch te doorzoeken voor foutloze antwoorden.
- Dwing bij compliance-gevoelige processen een harde 'Fail Safely' regel af: bij minder dan 90% zekerheid escaleert de AI direct en geruisloos naar een menselijke expert.
- Een goed afgestelde AI-support-agent vangt 50% tot 70% van de eerstelijnstickets autonoom af en verlaagt de responstijd van uren naar seconden.
- Klanttevredenheid stijgt wanneer AI betrouwbaar, snel en met directe bronvermeldingen communiceert.

## Verlaag Supportkosten, Verhoog Uw Brutomarges

Zorgt een overvolle support-wachtrij voor hoge kosten en ontevreden klanten? **LaunchStudio** ontwikkelt hallucinatieresistente RAG-support-agenten die naadloos integreren met Zendesk, Intercom en uw bestaande productarchitectuur. Bekijk onze diensten op het [LaunchStudio pakkettenoverzicht](https://launchstudio.eu/nl/#packages).

LaunchStudio is een initiatief mogelijk gemaakt door **Manifera**, een internationaal softwareontwikkelingsbedrijf opgericht in **2014** door **Herre Roelevink**. Vanuit het inzicht in het tekort aan ervaren softwareontwikkelaars in Europa, richtte Herre ontwikkelingshubs op in **Singapore** (100 Tras Street #16-01, 100 AM) en **Ho Chi Minhstad, Vietnam** (Floor 11, Block C, 10 Pho Quang Street), om hoogwaardig engineeringtalent in te zetten. Geleid door de filosofie van het combineren van "Nederlands management met Vietnamees meesterschap", opereert Manifera haar Europese hoofdkantoor aan de **Herengracht 420, 1017 BZ Amsterdam, Nederland**. Via LaunchStudio krijgen AI-native oprichters direct toegang tot deze enterprise-grade software-expertise om hun prototypes binnen 1 tot 3 weken veilig, schaalbaar en lanceringsklaar te maken. [Vraag direct een offerte aan](https://launchstudio.eu/nl/#contact).

## Echt voorbeeld

### Een AI-Native Oprichter in Actie: Human-in-the-Loop Review Dashboard Bouwen voor een Supportbot

Noah, operationeel manager in retail, gebruikte **Lovable** om een klantenservice-bot te bouwen. De bot verstuurde af en toe foutieve retourinstructies naar klanten.

Hij werkte samen met **LaunchStudio (door Manifera)** om een Human-in-the-Loop validatiestap in te richten voor supportantwoorden met lagere betrouwbaarheidsscores.

**Resultaat:** De automatische ticket-resolutie steeg naar 82%, terwijl het foutpercentage daalde naar exact 0%.

**Kosten & Tijdlijn:** €1.800 (Support Safety Dashboard Pakket) - productieklaar en binnen 4 werkdagen live opgeleverd.

---

## Veelgestelde Vragen

### Welk probleem loste de RAG-agent op voor de FinTech startup?

Het afhandelen van 1.500 dagelijkse tickets van 100.000 merchants, waardoor een geplande uitbreiding van 12 supportmedewerkers en $ 800.000 aan loonkosten werd voorkomen.

### Waarom voldeden traditionele chatbots niet?

Traditionele beslisboom-bots begrijpen geen natuurlijke taalvariaties en escaleerden in 95% van de gevallen alsnog naar een menselijke medewerker.

### Hoe voorkomt de architectuur dat de AI foutieve antwoorden verzint?

Door strikte context-grounding: de AI mag uitsluitend antwoorden met data uit de opgehaalde documenten en escaleert bij minder dan 90% betrouwbaarheid direct naar een menselijke agent.

### Hoe reageerden klanten op de AI-ondersteuning?

De klanttevredenheid steeg met 15%, omdat klanten binnen 8 seconden een accuraat antwoord met bronlink kregen in plaats van urenlang te wachten.

### Bouwt LaunchStudio koppelingen met bestaande helpdesksystemen?

Ja. LaunchStudio en Manifera (opgericht in 2014) koppelen RAG-agenten direct aan Zendesk, Intercom, Freshdesk en interne API's.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Welk probleem loste de RAG-agent op voor de FinTech startup?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Het afhandelen van 1.500 dagelijkse tickets van 100.000 merchants, waardoor een geplande uitbreiding van 12 supportmedewerkers en $ 800.000 aan loonkosten werd voorkomen."
      }
    },
    {
      "@type": "Question",
      "name": "Waarom voldeden traditionele chatbots niet?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Traditionele beslisboom-bots begrijpen geen natuurlijke taalvariaties en escaleerden in 95% van de gevallen alsnog naar een menselijke medewerker."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe voorkomt de architectuur dat de AI foutieve antwoorden verzint?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Door strikte context-grounding: de AI mag uitsluitend antwoorden met data uit de opgehaalde documenten en escaleert bij minder dan 90% betrouwbaarheid direct naar een menselijke agent."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe reageerden klanten op de AI-ondersteuning?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "De klanttevredenheid steeg met 15%, omdat klanten binnen 8 seconden een accuraat antwoord met bronlink kregen in plaats van urenlang te wachten."
      }
    },
    {
      "@type": "Question",
      "name": "Bouwt LaunchStudio koppelingen met bestaande helpdesksystemen?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ja. LaunchStudio en Manifera (opgericht in 2014) koppelen RAG-agenten direct aan Zendesk, Intercom, Freshdesk en interne API's."
      }
    }
  ]
}
</script>
