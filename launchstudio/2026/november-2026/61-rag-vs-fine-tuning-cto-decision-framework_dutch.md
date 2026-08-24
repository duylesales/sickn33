---
Titel: "RAG vs. Fine-Tuning: Een Beslissingskader voor CTO's over Kosten en Nauwkeurigheid"
Keywords: RAG vs Fine-Tuning, Retrieval Augmented Generation, Fine-Tuning LLM, Vectorzoekopdrachten, LLM-kosten, CTO Beslissingskader, LaunchStudio, Manifera
Buyer Stage: Decision
---

# RAG vs. Fine-Tuning: Een Beslissingskader voor CTO's over Kosten en Nauwkeurigheid

Elke CTO die een AI-product bouwt, komt uiteindelijk op hetzelfde tweesprong uit: moet het model kennis ophalen op het moment van de vraag, of moet het model getraind worden om die kennis al te kennen? De vraag klinkt academisch totdat de factuur binnenkomt. Teams die fine-tunen terwijl ze retrieval augmented generation (RAG) hadden moeten gebruiken, verbranden regelmatig vijf cijfers aan trainingsruns die verouderd raken zodra de onderliggende data verandert. Teams die op RAG leunen terwijl de taak eigenlijk fine-tuning vereiste, eindigen met een chatbot die "klinkt als ChatGPT met een naamplaatje om" — technisch correct, maar zonder de domeinstem en redeneerpatronen waarvoor klanten betalen. Dit is geen machine-learning-onderzoeksvraag. Het is een bouwkeuze met directe gevolgen voor het verbrandingstempo van kapitaal, latency, en hoe verdedigbaar uw product daadwerkelijk is tegenover een concurrent met dezelfde OpenAI API-sleutel. Dit is het kader waar we CTO's en technische oprichters doorheen leiden voordat er ook maar één regel infrastructuur wordt gebouwd.

## De valse tegenstelling: waarom de meeste teams deze beslissing verkeerd nemen

RAG en fine-tuning worden meestal gepresenteerd als concurrerende strategieën, en dat is de eerste vergissing. RAG is een architectuur — een manier om de output van een model te funderen op opgehaalde documenten (meestal via een vectordatabase zoals Pinecone, Weaviate, Qdrant of pgvector) op het moment van de query. Fine-tuning is een trainingsproces — een manier om de gewichten van het model zelf aan te passen, zodat een gedrag of kennispatroon permanent wordt ingebakken. De ene beantwoordt "wat weet het model", de andere beantwoordt "hoe gedraagt het model zich." Deze twee door elkaar halen leidt ertoe dat oprichters kiezen voor wat hun AI-buildertool (Bolt, Lovable, Cursor) toevallig als eerste opzette, in plaats van wat de daadwerkelijke use case vereist.

Dit onderscheid is belangrijk omdat de twee benaderingen op verschillende manieren falen. Een RAG-systeem met een slechte retriever geeft zelfverzekerd foute antwoorden omdat het het verkeerde document ophaalde. Een fine-getuned model met onvoldoende trainingsdata geeft zelfverzekerd foute antwoorden omdat het het patroon nooit heeft geleerd. Beide zien er voor een eindgebruiker identiek uit — een gehallucineerde factuurregel, een verzonnen juridische verwijzing, een verkeerd product-SKU — maar de oplossing, en de kosten van die oplossing, verschillen volledig.

## Wat RAG werkelijk kost: infrastructuur, geen training

De aantrekkingskracht van RAG is dat er helemaal geen modeltraining nodig is. U embedt uw documenten in een vectordatabase, haalt de top-k relevante fragmenten op tijdens de query, en voegt deze toe aan de promptcontext naast de vraag van de gebruiker. De initiële kosten zijn laag: een embeddingmodel (zoals OpenAI's text-embedding-3-large of een open-source alternatief), een vectorstore en een retrieval-pijplijn. Voor de meeste AI SaaS-producten in het bereik van €0-€2M ARR is dit de juiste standaardkeuze, omdat de kennisbank voortdurend verandert — prijstabellen, productcatalogi, beleidsdocumenten, supporttickets — en RAG stelt u in staat de onderliggende data bij te werken zonder iets opnieuw te trainen.

De echte kosten van RAG dienen zich later aan, en ze zijn architecturaal in plaats van financieel: chunking-strategie, keuze van embeddingmodel, herrangschikking (re-ranking) en — het onderdeel dat de meeste AI-builder-scaffolds volledig overslaan — Row Level Security op de vectortabel zelf. Wij hebben RAG-systemen geaudit die door Bolt en Lovable waren gegenereerd, waarbij de document-embeddings van elke klant in één ongescopte tabel stonden, wat betekende dat een slim geconstrueerde query van Klant A fragmenten kon ophalen die toebehoorden aan Klant B. Dat is geen trainingsprobleem; het is een production-hardening-probleem, en het is precies het verschil tussen "de demo werkte" en "het systeem is veilig met echte klantdata erin."

## Wat fine-tuning werkelijk kost: data, rekenkracht en drift

Fine-tuning is zinvol wanneer de taak draait om *gedrag*, niet om *kennisretrieval* — een specifieke toon, een gestructureerd outputformaat, een classificatiepatroon of een redeneerstijl die retrieval alleen niet kan aanleren. Denk aan een legal-tech-tool die contractclausules moet opstellen in de exacte huisstijl van een kantoor, of een support-triagesysteem dat het oordeel van een senior medewerker moet nabootsen over duizenden historische tickets. Geen enkele hoeveelheid opgehaalde context levert dat betrouwbaar op; het patroon moet in de gewichten worden geleerd.

De kosten zijn reëel en worden vaak onderschat door oprichters die een blogpost lezen waarin staat dat "fine-tuning nu goedkoop is." U heeft een schone, gelabelde trainingsdataset nodig — doorgaans honderden tot duizenden hoogwaardige voorbeelden, wat op zichzelf al een data-engineeringproject is voordat er ook maar getraind wordt. U moet budgetteren voor iteratie: een eerste fine-tune is zelden meteen raak, en elke herhaling kost rekenkracht en dagen doorlooptijd. En u heeft een plan nodig voor drift — een fine-getuned model is een momentopname; wanneer uw product, prijzen of beleid veranderen, weet het model dat niet tenzij u opnieuw traint. Teams die fine-tunen op hun v1-productdata en zes weken later v2-functies uitbrengen, eindigen met twee bronnen van waarheid: de bevroren kennis van het model en de levende productrealiteit, die stilletjes uit elkaar lopen.

## Een kader met vijf vragen voor de beslissing

Voordat we engineeringtijd toewijzen aan een van beide paden, leiden we oprichters door vijf vragen:

1. **Verandert de kennis wekelijks, of is het gedrag stabiel?** Snel veranderende feiten (prijzen, voorraad, beleid) horen thuis in RAG. Stabiele gedragspatronen (toon, formaat, oordeel) zijn kandidaten voor fine-tuning.

2. **Kunt u een bron citeren?** Als uw product gebruikers moet laten zien "hier komt dit antwoord vandaan" — gebruikelijk in legal-tech, healthtech en financiële compliance-tools — is RAG bijna verplicht, omdat fine-getunede modellen niet kunnen terugverwijzen naar een brondocument; ze kunnen alleen een patroon reproduceren.

3. **Wat is uw werkelijke datavolume?** Fine-tuning heeft echte trainingsdata op schaal nodig. Als u 40 voorbeelden heeft van het gewenste gedrag, heeft u nog geen fine-tuning-dataset — u heeft een prompt-engineeringprobleem, en RAG met een sterke systeemprompt zal het beter doen dan een ondergetraind fine-tune-model.

4. **Wat is uw latency- en kostenbudget per query?** RAG voegt een retrieval-round-trip toe (doorgaans 50-200ms) plus een grotere promptcontext, wat de tokenkosten per aanroep verhoogt. Een goed uitgevoerde fine-tune kan kortere, goedkopere completions opleveren tijdens inferentie, ten koste van een grote eenmalige traininginvestering.

5. **Wie is verantwoordelijk voor het faalpatroon?** Een RAG-hallucinatie is meestal een retrievalbug die u binnen enkele uren kunt oplossen door chunking of re-ranking te verbeteren. Een fine-tuning-hallucinatie betekent dat het model iets verkeerds heeft geleerd, en de enige oplossing is een nieuwe trainingscyclus. Als uw team zich geen meerdaagse hersteltijden voor nauwkeurigheidsfouten kan veroorloven, is de snellere iteratiecyclus van RAG operationeel de veiligere keuze, los van theoretische nauwkeurigheidsplafonds.

## De hybride realiteit: de meeste productiesystemen hebben beide nodig

In de praktijk kiezen de CTO's die dit goed aanpakken zelden exclusief voor één van de twee. Een veelvoorkomend, duurzaam patroon dat wij implementeren is RAG voor feitelijke onderbouwing — het ophalen van de juiste productdata, beleidsclausule of accountgegevens — gecombineerd met een licht fine-getunede of zorgvuldig prompt-geëngineerde laag die de toon, structuur en domeinspecifieke redenering bovenop het opgehaalde materiaal aanstuurt. Dit is meer engineeringwerk dan elk van beide benaderingen afzonderlijk, en precies daarom nemen AI-builder-scaffolds dit zelden standaard mee: Bolt, Lovable en Cursor zijn geoptimaliseerd om u snel een werkende demo te laten zien, niet om de retrieval-en-fundering-laag te architecteren die een productiesysteem nauwkeurig en veilig houdt onder echte multi-tenant belasting.

De beslissing is, met andere woorden, niet RAG versus fine-tuning. Het is het voldoende begrijpen van de daadwerkelijke faalpatronen van uw product om te weten welke architectuur — of welke combinatie — de kosten waard is.

## Belangrijkste inzichten

- RAG en fine-tuning lossen verschillende problemen op: RAG bepaalt wat het model weet op het moment van de query, fine-tuning bepaalt hoe het model zich gedraagt. De meeste teams zouden standaard voor RAG moeten kiezen, tenzij ze een specifiek gedragspatroon hebben dat retrieval niet kan aanleren.

- De echte kosten van RAG zitten niet in de vectordatabase — ze zitten in het production-hardening-werk dat de meeste AI-builders overslaan, met name Row Level Security op multi-tenant embeddingtabellen.

- Fine-tuning vereist een echte gelabelde dataset (honderden tot duizenden voorbeelden), een budget voor rekenkracht en iteratie, en een hertrainingsplan voor drift naarmate uw product evolueert — het onderschatten van een van deze drie is de meest voorkomende manier waarop oprichters te veel uitgeven.

- Als uw product om compliance- of vertrouwensredenen een brondocument moet citeren, is RAG bijna verplicht; fine-getunede modellen kunnen een patroon reproduceren maar kunnen niet terugverwijzen naar waar een antwoord vandaan kwam.

- De meest duurzame productiesystemen combineren beide: RAG voor feitelijke onderbouwing, een fine-getunede of zorgvuldig geëngineerde laag voor toon en redenering — architectuur die LaunchStudio implementeert bovenop uw bestaande AI-builder-frontend, zonder een rebuild.

## Stop met gokken op architectuur — Krijg een kader dat past bij uw product

Kiezen tussen RAG en fine-tuning zonder kader betekent meestal kiezen voor wat uw AI-builder toevallig opzette — niet voor wat uw product daadwerkelijk nodig heeft.

LaunchStudio wordt geëxploiteerd door **Manifera**, een internationaal software-engineeringbedrijf opgericht in 2014 en geleid door Oprichter & Managing Director **Herre Roelevink**. Zoals Roelevink het verwoordt: *"We zien een verschuiving in softwarebehoeften. De uitdaging is niet langer om goede ideeën om te zetten in software. Het gaat nu om de architectuur en beveiliging die nodig zijn om die producten tot wasdom te brengen. Wij hebben elf jaar ervaring in precies dat vakgebied."* Door "Nederlands management te combineren met Vietnamees meesterschap", onderhoudt Manifera hoofdkantoren in **Amsterdam, Nederland** (Herengracht 420), een Aziatische hub in **Singapore** (100 Tras Street) en een primair ontwikkelcentrum in **Ho Chi Minh-stad, Vietnam** (Pho Quang Street). Via LaunchStudio evalueren senior engineeringteams de daadwerkelijke retrieval- en kennisarchitectuur van uw AI-product, implementeren ze production-grade RAG-pijplijnen met correcte multi-tenant beveiliging, of scopen ze een fine-tuning-pijplijn waar dat daadwerkelijk gerechtvaardigd is — waardoor een AI-builder-prototype binnen 1 tot 3 weken verandert in een veilige, kostenverantwoorde MVP, zonder rebuild. [Vraag vandaag nog een gratis offerte aan](https://launchstudio.eu/en/#contact) of bekijk hoe het [maatwerk software-ontwikkelteam van Manifera](https://www.manifera.com/services/custom-software-development/) AI-architectuurbeslissingen voor productiesystemen aanpakt.

## Echt voorbeeld

### Een AI-native oprichter in actie: juridische onderzoeksassistent

Priya Ramaswamy, oprichter van een legal-tech-startup, gebruikte **Bolt** om ClauseIQ te bouwen, een AI-copiloot die kleine advocatenkantoren hielp bij het opstellen en beoordelen van contractclausules. In het begin was ze ervan overtuigd dat fine-tuning het "serieuze" engineeringpad was, dus besteedde ze zes weken en ongeveer $18.000 aan rekenkracht om een open-weight model te fine-tunen op een dataset van 300 voorbeeldclausules. Het resultaat gaf vloeiende antwoorden, maar kon niet aangeven van welk precedent of sjabloon een clausule afkomstig was — een breekpunt voor kantoren die een audittrail nodig hadden — en telkens wanneer haar sjabloonbibliotheek werd bijgewerkt, raakte de kennis van het model stilletjes verouderd.

Priya schakelde LaunchStudio in om de kennislaag opnieuw te architecteren zonder haar bestaande, met Bolt gebouwde UI aan te raken. Het engineeringteam verving de fine-getunede aanpak door een production-grade RAG-pijplijn: documenten geëmbed en opgeslagen in een correct met Row Level Security beveiligde Postgres/pgvector-instantie, een re-ranking-stap om het meest relevante clausulesjabloon naar boven te halen, en inline bronvermeldingen bij elk gegenereerd antwoord.

**Resultaat:** ClauseIQ citeert nu voor 100% van de gegenereerde clausules het exacte bronsjabloon, verlaagde de gemiddelde kosten per query met 61% ten opzichte van het fine-getunede model, en kantoren kunnen de sjabloonbibliotheek bijwerken zonder enige hertrainingscyclus.

**Kosten & Doorlooptijd:** € 3.200 (Launch & Grow Pakket) — productieklaar en uitgerold in 10 werkdagen.

---

---

---
## Veelgestelde Vragen

### Is RAG altijd goedkoper dan fine-tuning?

Niet altijd, maar meestal wel voor producten in een vroege fase. RAG heeft lage initiële kosten (embeddings en een vectordatabase) maar doorlopende kosten per query door grotere promptcontexten. Fine-tuning heeft hoge initiële kosten (datalabeling en trainingsrekenkracht) maar kan kortere, goedkopere completions opleveren tijdens inferentie. Voor de meeste AI SaaS-producten onder €2M ARR met snel veranderende kennis maken de lagere initiële kosten en snellere iteratiecyclus van RAG het de kapitaalefficiëntere standaardkeuze.

### Kan ik RAG en fine-tuning samen gebruiken?

Ja, en voor veel productiesystemen is dit het juiste antwoord. Een veelvoorkomend patroon is RAG voor feitelijke onderbouwing — het ophalen van het juiste document, beleid of record — gecombineerd met een fine-getunede of zorgvuldig prompt-geëngineerde laag voor toon, structuur en domeinspecifieke redenering die wordt toegepast bovenop het opgehaalde materiaal.

### Wat is het grootste beveiligingsrisico bij RAG-systemen die door AI-tools zijn gebouwd?

Datalekken tussen tenants (multi-tenant data leakage). AI-builders zoals Bolt, Lovable en Cursor zetten vectordatabasetabellen vaak op zonder correcte Row Level Security, wat betekent dat de query van de ene klant document-embeddings kan ophalen die toebehoren aan een andere klant. Dit is een databasebeveiligingsprobleem, geen machine-learning-probleem, en het moet worden opgelost voordat er echte klantdata in het systeem komt.

### Hoeveel trainingsdata heb ik daadwerkelijk nodig om een model verantwoord te fine-tunen?

Er is geen vast getal, maar als praktische ondergrens beginnen de meeste bruikbare fine-tunes met enkele honderden hoogwaardige gelabelde voorbeelden, en de resultaten verbeteren doorgaans significant tot in de lage duizenden. Als u minder dan 100 voorbeelden heeft van het gewenste gedrag, heeft u waarschijnlijk een prompt-engineeringprobleem dat zich voordoet als een fine-tuning-project, en zal RAG met een sterke systeemprompt een ondergetraind fine-tune-model overtreffen.

### Hoe bepaalt LaunchStudio welke architectuur wordt aanbevolen?

De engineers van LaunchStudio auditen de daadwerkelijke faalpatronen van uw product — of onnauwkeurigheden voortkomen uit ontbrekende kennis (een retrievalprobleem) of verkeerd gedrag (een trainingsprobleem) — evenals uw datavolume, latencybudget en citatievereisten, voordat ze RAG, fine-tuning of een hybride vorm aanbevelen. Het doel is altijd om de architectuur af te stemmen op de werkelijke beperkingen van het product, niet om standaard te kiezen voor het patroon dat het makkelijkst was voor een AI-builder om op te zetten.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Is RAG altijd goedkoper dan fine-tuning?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Niet altijd, maar meestal wel voor producten in een vroege fase. RAG heeft lage initiële kosten (embeddings en een vectordatabase) maar doorlopende kosten per query door grotere promptcontexten. Fine-tuning heeft hoge initiële kosten (datalabeling en trainingsrekenkracht) maar kan kortere, goedkopere completions opleveren tijdens inferentie. Voor de meeste AI SaaS-producten onder €2M ARR met snel veranderende kennis maken de lagere initiële kosten en snellere iteratiecyclus van RAG het de kapitaalefficiëntere standaardkeuze."
      }
    },
    {
      "@type": "Question",
      "name": "Kan ik RAG en fine-tuning samen gebruiken?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ja, en voor veel productiesystemen is dit het juiste antwoord. Een veelvoorkomend patroon is RAG voor feitelijke onderbouwing — het ophalen van het juiste document, beleid of record — gecombineerd met een fine-getunede of zorgvuldig prompt-geëngineerde laag voor toon, structuur en domeinspecifieke redenering die wordt toegepast bovenop het opgehaalde materiaal."
      }
    },
    {
      "@type": "Question",
      "name": "Wat is het grootste beveiligingsrisico bij RAG-systemen die door AI-tools zijn gebouwd?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Datalekken tussen tenants (multi-tenant data leakage). AI-builders zoals Bolt, Lovable en Cursor zetten vectordatabasetabellen vaak op zonder correcte Row Level Security, wat betekent dat de query van de ene klant document-embeddings kan ophalen die toebehoren aan een andere klant. Dit is een databasebeveiligingsprobleem, geen machine-learning-probleem, en het moet worden opgelost voordat er echte klantdata in het systeem komt."
      }
    },
    {
      "@type": "Question",
      "name": "Hoeveel trainingsdata heb ik daadwerkelijk nodig om een model verantwoord te fine-tunen?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Er is geen vast getal, maar als praktische ondergrens beginnen de meeste bruikbare fine-tunes met enkele honderden hoogwaardige gelabelde voorbeelden, en de resultaten verbeteren doorgaans significant tot in de lage duizenden. Als u minder dan 100 voorbeelden heeft van het gewenste gedrag, heeft u waarschijnlijk een prompt-engineeringprobleem dat zich voordoet als een fine-tuning-project, en zal RAG met een sterke systeemprompt een ondergetraind fine-tune-model overtreffen."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe bepaalt LaunchStudio welke architectuur wordt aanbevolen?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "De engineers van LaunchStudio auditen de daadwerkelijke faalpatronen van uw product — of onnauwkeurigheden voortkomen uit ontbrekende kennis (een retrievalprobleem) of verkeerd gedrag (een trainingsprobleem) — evenals uw datavolume, latencybudget en citatievereisten, voordat ze RAG, fine-tuning of een hybride vorm aanbevelen. Het doel is altijd om de architectuur af te stemmen op de werkelijke beperkingen van het product, niet om standaard te kiezen voor het patroon dat het makkelijkst was voor een AI-builder om op te zetten."
      }
    }
  ]
}
</script>
