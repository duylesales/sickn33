---
Titel: "Hoe Voeg Ik Zoeken Toe aan Mijn Supabase-App?"
Trefwoorden: supabase zoeken, full text search postgres, zoekfunctie lovable, pg_trgm fuzzy search, LaunchStudio, Manifera
Koperfase: Overweging
Doelgroep: Technische Solo-Oprichter / Indie Hacker
---

# Hoe Voeg Ik Zoeken Toe aan Mijn Supabase-App?

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Hoe Voeg Ik Zoeken Toe aan Mijn Supabase-App?",
  "description": "AI-gebouwde apps implementeren zoeken vaak door alles in de browser te laden. Deze gids legt betere opties in Supabase uit: gefilterde queries, full-text search in Postgres met ondersteuning voor Nederlands, fuzzy matching met pg_trgm en semantisch zoeken met pgvector, allemaal met respect voor Row Level Security.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-03-07",
  "inLanguage": "nl-NL",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/how-do-i-add-search-to-my-supabase-app" },
  "citation": [
    { "@type": "CreativeWork", "name": "Supabase: Full text search", "url": "https://supabase.com/docs/guides/database/full-text-search" },
    { "@type": "CreativeWork", "name": "Supabase: pgvector", "url": "https://supabase.com/docs/guides/database/extensions/pgvector" },
    { "@type": "CreativeWork", "name": "Supabase: Database performance", "url": "https://supabase.com/docs/guides/platform/performance" },
    { "@type": "CreativeWork", "name": "Supabase: Row Level Security", "url": "https://supabase.com/docs/guides/database/postgres/row-level-security" }
  ]
}
</script>

**Kort antwoord:** zoek in de database, niet in de browser. Gebruik voor eenvoudige behoeften gefilterde queries met indexen. Gebruik voor het doorzoeken van tekst, zoals beschrijvingen of notities, de full-text search van Postgres met de juiste taalconfiguratie (Nederlands, Engels of beide). Voeg voor zoeken op namen dat tegen typfouten kan de extensie `pg_trgm` toe. Gebruik voor "vind dingen die hetzelfde betekenen" embeddings met `pgvector`. Al deze technieken draaien in Supabase en respecteren Row Level Security als ze correct worden aangeroepen.

## Belangrijkste Punten

- **Zoek in de database, niet in de browser.** Elk record laden om in JavaScript te filteren is traag en kan gegevens lekken die Row Level Security zou moeten verbergen.
- **PostgreSQL biedt meerdere zoektools:** geïndexeerde filters, full-text search met taalconfiguraties waaronder Nederlands, trigramovereenkomst met `pg_trgm` en vectorovereenkomst met `pgvector`.
- **Full-text search met de Nederlandse configuratie gaat om met stemming,** zodat "fietsen" overeenkomt met "fiets"; trigrammatching voegt tolerantie voor typfouten toe.
- **Semantisch zoeken met embeddings** vindt resultaten op betekenis voor kennisbanken, supportcontent en overzichten.
- **Zoeken moet dezelfde toegangsregels respecteren** als de rest van uw app; zoekendpoints zijn een veelvoorkomende plek waar die regels per ongeluk worden omzeild.

## Het Patroon om te Vermijden

Lovable en Bolt implementeren zoeken vaak zo: alle records ophalen en ze dan in JavaScript filteren. Met 50 rijen werkt dat. Met 50.000 bevriezen pagina's, stijgen de kosten voor dataverkeer en - erger nog - als Row Level Security te ruim is, stuurt u mogelijk gegevens van andere gebruikers naar de browser om ze daar weg te filteren.

## De Juiste Zoekmethode Kiezen

| Behoefte | Techniek | Voorbeeld |
| --- | --- | --- |
| Exacte filters | Geïndexeerde `where`-clausules | Status = open, plaats = Utrecht |
| Overeenkomst op begin | `ilike 'term%'` met index | Klantnamen die beginnen met "Van" |
| Woorden in lange tekst | Full-text search (`tsvector`) | Beschrijvingen en notities doorzoeken |
| Tolerantie voor typfouten | Overeenkomst via `pg_trgm` | "Jansen" vindt "Janssen" |
| Op betekenis | Embeddings met `pgvector` | "goedkope kamer bij het station" vindt relevante advertenties |

## Full-Text Search in de Praktijk

Voeg een gegenereerde kolom `tsvector` toe die de velden combineert die doorzoekbaar moeten zijn, met een taalconfiguratie zoals `dutch` of `english`, en een GIN-index daarop. Bevraag hem met `websearch_to_tsquery`, dat natuurlijke invoer van gebruikers accepteert. Voor tweetalige apps slaat u beide configuraties op of kiest u de taal per record.

De Nederlandse configuratie gaat om met stemming, zodat "fietsen" overeenkomt met "fiets". Niet elke samenstelling wordt goed afgehandeld, en daar kan `pg_trgm` aanvullen.

## Zoeken dat Tegen Typfouten Kan

Schakel `pg_trgm` in, voeg een trigramindex toe op namen of titels en sorteer resultaten op overeenkomst. Zo voelt zoeken vergevingsgezind aan voor namen, producttitels en adressen.

## Semantisch Zoeken

Genereer voor kennisbanken, supportcontent of advertenties die op veel manieren worden beschreven, voor elk record embeddings met een AI-model en sla ze op met `pgvector`. Genereer embeddings op de server, houd de API-sleutel in een edge function en combineer semantische resultaten met gewone filters.

## Houd de Beveiliging Intact

- Roep zoeken aan via de normale Supabase-client zodat Row Level Security geldt, of via databasefuncties met passende beveiligingsinstellingen
- Vermijd zoekfuncties met `security definer` die RLS omzeilen, tenzij ze dezelfde controles toepassen
- Beperk het aantal resultaten en pagineer

## Tips voor Prestaties

- Indexeer alles waarop u filtert of sorteert
- Gebruik debouncing bij zoekinvoer, zodat u niet bij elke toetsaanslag een query uitvoert
- Geef alleen de kolommen terug die de resultatenlijst nodig heeft

## Hoe Full-Text Search in PostgreSQL Werkt

De full-text search van PostgreSQL zet tekst om in een `tsvector`, een lijst van genormaliseerde woorden (lexemen) met posities, op basis van een taalconfiguratie die stemming en stopwoorden afhandelt. Queries worden omgezet in een `tsquery`. De operator `@@` controleert of een document overeenkomt met een query, en rangschikkingsfuncties ordenen resultaten op relevantie. Een GIN-index op de kolom `tsvector` maakt zoeken snel, ook in grote tabellen. Supabase documenteert dit in de gids over full-text search, en dezelfde concepten gelden in elke PostgreSQL-database.

## Taalconfiguraties Kiezen

PostgreSQL wordt geleverd met configuraties voor veel talen, waaronder `dutch` en `english`. De configuratie bepaalt hoe woorden tot hun stam worden teruggebracht: in het Nederlands worden meervouds- en werkwoordsvormen teruggebracht tot een gemeenschappelijke stam, zodat zoekopdrachten verwante vormen vinden. Voor tweetalige content kunt u een taal per record opslaan en de `tsvector` met de bijbehorende configuratie opbouwen, of aparte kolommen per taal bijhouden. Samenstellingen, die in het Nederlands veel voorkomen, worden niet altijd gesplitst; trigrammatching op belangrijke velden vult dat gat.

## Rangschikking en Relevantie

Niet alle overeenkomsten zijn gelijk. Geef velden een verschillend gewicht - een overeenkomst in de titel hoort zwaarder te tellen dan een in de beschrijving - met de weegfuncties van PostgreSQL bij het opbouwen van de `tsvector`. Combineer tekstrelevantie waar nuttig met bedrijfssignalen, zoals recentheid, populariteit of beschikbaarheid. Test de rangschikking met echte zoekopdrachten van uw gebruikers; de beste rangschikking is die waarbij het resultaat dat mensen werkelijk kiezen bovenaan staat.

## Trigramzoeken voor Namen en Typfouten

De extensie `pg_trgm` splitst tekst in reeksen van drie tekens en meet de overeenkomst daartussen. Dat is ideaal voor namen, producttitels en adressen, waarbij gebruikers termen verkeerd spellen of maar half onthouden. Met een trigramindex geven queries zoals "vind klanten met een naam die lijkt op 'Janssen'" snel "Jansen" en "Janssens" terug. Stel een drempel voor overeenkomst in die het evenwicht tussen volledigheid en precisie voor uw gegevens bewaart.

## Semantisch Zoeken met pgvector

Voor content waarbij gebruikers in hun eigen woorden beschrijven wat ze zoeken - helpartikelen, productbeschrijvingen, documenten - vindt semantisch zoeken resultaten op betekenis. U genereert voor elk record een embedding (een numerieke vector) met een AI-model, slaat die op met de extensie `pgvector` en vergelijkt die met de embedding van de zoekopdracht van de gebruiker. Praktische aandachtspunten:

- Genereer embeddings op de server en houd de API-sleutel geheim
- Maak opnieuw embeddings wanneer de inhoud van records verandert
- Combineer semantische resultaten met filters op organisatie, status en rechten
- Overweeg hybride zoeken, waarbij scores van full-text en semantisch zoeken worden gemengd, voor het beste van beide
- Onthoud dat het versturen van content naar een provider van embeddings een verwerking van persoonsgegevens is als de content die bevat

## Prestaties op Schaal

De prestaties van zoeken hangen af van indexen en de vorm van de query. Gebruik GIN-indexen voor full-text en trigramzoeken, passende vectorindexen voor embeddings, en filters op geïndexeerde kolommen zoals het organisatie-ID. Pagineer resultaten en geef alleen de kolommen terug die de resultatenlijst nodig heeft. Gebruik in de interface debouncing bij zoekinvoer, zodat u niet bij elke toetsaanslag een query verstuurt. De richtlijnen voor prestaties en de queryrapporten van Supabase helpen trage zoekopdrachten op te sporen.

## Zoeken Veilig Houden

Zoeken loopt voor het gemak vaak via databasefuncties of views. Zorg dat die Row Level Security respecteren: views die met `security_invoker` zijn aangemaakt, passen de rechten van de aanroeper toe, terwijl functies met `security definer` met verhoogde rechten draaien en zelf controles moeten toepassen. Geef openbare gebruikers alleen openbare velden terug, en test zoeken als twee gebruikers uit verschillende organisaties om te bevestigen dat geen van beiden de resultaten van de ander ziet.

## Wanneer U een Aparte Zoekdienst Gebruikt

Aparte zoekmachines bieden geavanceerde functies zoals facetten, synoniemen en tolerantie voor typfouten die op zoeken zijn afgestemd. Voor de meeste apps in de oprichtersfase zijn de mogelijkheden van PostgreSQL voldoende, en ze voorkomen een extra dienst die u moet beveiligen, synchroniseren en betalen. Overweeg een aparte dienst wanneer zoeken centraal komt te staan in uw product, de hoeveelheid gegevens zeer groot wordt of u functies nodig heeft die PostgreSQL niet gemakkelijk biedt.

## De Zoekervaring Ontwerpen

Goed zoeken gaat net zo goed over de interface als over de database. Toon resultaten terwijl gebruikers typen, na een korte vertraging, met duidelijke markering van de gevonden termen. Bied filters op de kenmerken waar gebruikers om geven, zoals locatie, categorie, status of datum. Ga behulpzaam om met lege resultaten, met suggesties of verwante items in plaats van een lege pagina. Houd het zoekveld zichtbaar op de pagina's waar gebruikers het het meest nodig hebben. Maak filters voor mobiele gebruikers makkelijk te openen en te sluiten.

## De Kwaliteit van Zoeken Meten

Leg zoekopdrachten vast (zonder onnodige persoonsgegevens): de zoekopdracht, het aantal resultaten en welk resultaat de gebruiker eventueel aanklikte. Bekijk wekelijks de zoekopdrachten zonder resultaten; ze laten ontbrekende content zien, synoniemen die u nodig heeft en spellingsvarianten. Houd bij hoe vaak gebruikers hun zoekopdracht verfijnen; vaak verfijnen wijst op problemen met de rangschikking. Deze kleine gegevens leiden tot gestage verbeteringen.

## Synoniemen en Vaktaal

Gebruikers gebruiken zelden de woorden die in uw database staan. Een loodgieter wordt misschien gezocht als "loodgieter", "installateur" of "cv-monteur"; een product kan een merknaam en een algemene naam hebben. Houd een kleine tabel met synoniemen bij en breid zoekopdrachten daarmee uit, of neem alternatieve termen op in de geïndexeerde tekst. Dit is een van de goedkoopste manieren om zoeken te verbeteren voor een Nederlands publiek, waar regionale en vakwoorden verschillen.

## Veelgemaakte Fouten

- Alle records in de browser filteren
- Zoekfuncties die Row Level Security omzeilen
- Privévelden samen met openbare velden indexeren
- Geen index op de zoekkolom
- Zoekopdrachten zonder resultaten negeren

## Een Stappenplan

1. Bepaal welke zoekopdrachten gebruikers het vaakst doen en welke velden ze doorzoeken.
2. Voeg een gegenereerde kolom `tsvector` toe met de juiste taalconfiguratie en een GIN-index.
3. Voeg `pg_trgm` en een trigramindex toe voor namen en titels.
4. Verplaats zoeken naar een databasefunctie die toegangsregels toepast en alleen de benodigde kolommen teruggeeft.
5. Pagineer en gebruik debouncing in de interface.
6. Leg zoekopdrachten vast en bekijk wekelijks de zoekopdrachten zonder resultaten.
7. Overweeg semantisch zoeken zodra tekstzoeken goed werkt en gebruikers nog steeds moeite hebben.

## De Opbrengst

Snel, nauwkeurig zoeken laat producten professioneel aanvoelen en bespaart gebruikers elke dag tijd. Uitgevoerd in de database met de juiste toegangsregels, neemt het ook een van de stille datalekken weg die in AI-gebouwde apps vaak voorkomen.

## Zoeken voor een Nederlands Publiek

Nederlandse gebruikers zoeken met samenstellingen, regionale termen en Engelse leenwoorden door elkaar. Gebruik de Nederlandse configuratie voor stemming, voeg trigrammatching toe om samenstellingen en typfouten op te vangen, houd een lijst met synoniemen bij voor vak- en regionale woorden, en overweeg zowel Nederlandse als Engelse termen te indexeren voor producten die door internationale teams worden gebruikt. Test met echte zoekopdrachten van Nederlandse klanten; kleine aanpassingen in woordenschat leveren vaak grote verbeteringen op.

## Samenvatting

Indexeer de juiste kolommen, gebruik de Nederlandse of Engelse configuratie, voeg trigrammatching toe voor namen, houd zoeken binnen uw toegangsregels en leer van zoekopdrachten zonder resultaten.

## Verder Lezen

Als zoeken traag is naast andere schermen, behandelt onze gids over de vraag of een Lovable-app echte gebruikers aankan indexen, prestaties van RLS en het samenvoegen van queries uitgebreider.

## Het Laten Bouwen

LaunchStudio vervangt zoeken in de browser door zoeken in de database als onderdeel van prestatie- en productiewerk, meestal een tot drie dagen. LaunchStudio wordt ondersteund door Manifera, waarvan de engineers al 11+ jaar zoekfuncties bouwen voor enterprisedatasystemen, in Ho Chi Minh-stad, Singapore en Amsterdam; zie [de technologieën van Manifera](https://www.manifera.com/about-us/manifera-technologies/). Supabase documenteert [full-text search](https://supabase.com/docs/guides/database/full-text-search) en [pgvector](https://supabase.com/docs/guides/database/extensions/pgvector). Als zoeken een van meerdere trage functies is, zie dan ons artikel over de vraag of [een Lovable-app echte gebruikers aankan](https://launchstudio.eu/nl/blog/can-a-lovable-app-handle-real-users).

## Praktijkvoorbeeld

### Een AI-Native Oprichter in Actie: De Zoekfunctie van de Tweedehands Boekwinkels die de Voorraad van Anderen Toonde

Pauline Smeets runt een netwerk van tweedehands boekwinkels in Limburg en bouwde Boekenspoor in Lovable: winkels zetten hun voorraad online, en lezers zoeken in alle winkels tegelijk. Winkeleigenaren hadden daarnaast een privédashboard met inkoopprijzen en notities over leveranciers. Met 38.000 boeken online duurde zoeken enkele seconden en bevroren oudere telefoons.

De zoekfunctie laadde elk boekrecord, inclusief privévelden, in de browser en filterde lokaal. Omdat de policy van de boekentabel alle kolommen aan iedereen teruggaf, waren de inkoopprijzen van winkeleigenaren zichtbaar in de netwerkantwoorden voor elke bezoeker.

LaunchStudio splitste openbare en privévelden in aparte tabellen met eigen policies, voegde een kolom voor full-text search toe met Nederlandse configuratie over titel, auteur en beschrijving, voegde trigrammatching toe voor auteursnamen, pagineerde de resultaten en verplaatste het zoeken naar een databasefunctie die alleen openbare velden teruggeeft.

**Resultaat:** Zoekantwoorden daalden naar ruim onder een halve seconde, privéprijzen verdwenen uit openbare antwoorden, en lezers vonden meer boeken: het aantal zoekopdrachten zonder resultaten daalde sterk dankzij stemming en tolerantie voor typfouten.

> *"Zoeken was traag, dat merkte ik. Het lekte ook de inkoopprijzen van elke winkel, en dat merkte ik niet."*
> - **Pauline Smeets, Oprichter, Boekenspoor (Maastricht)**

**Kosten & Doorlooptijd:** €1.850 (Launch Ready-pakket: splitsing van het schema, RLS, full-text en trigramzoeken, paginering en zoekfunctie) - afgerond in 6 werkdagen.

## Veelgestelde Vragen

### Ondersteunt Supabase full-text search?

Ja. Supabase draait op PostgreSQL, dat ingebouwde full-text search heeft met taalconfiguraties, waaronder Nederlands en Engels. Voeg een zoekkolom en een index toe voor goede prestaties.

### Hoe maak ik zoeken tolerant voor typfouten?

Schakel de extensie `pg_trgm` in en gebruik overeenkomstmatching met een trigramindex. Dat werkt goed voor namen, titels en adressen, en vult full-text search aan.

### Wanneer gebruik ik vectorzoeken?

Wanneer gebruikers in hun eigen woorden beschrijven wat ze zoeken en exacte woordovereenkomsten relevante resultaten missen, zoals bij supportartikelen, advertenties of documenten. Vectorzoeken met `pgvector` vindt resultaten op betekenis.

### Hoe houdt Manifera zoeken veilig?

Door zoeken via dezelfde toegangsregels te laten lopen als al het andere en openbare gebruikers alleen openbare velden terug te geven. De 11+ jaar datasystemen van Manifera laten zien dat zoekendpoints een veelvoorkomende plek zijn waar toegangsregels per ongeluk worden omzeild.

### Heeft interne zoekfunctionaliteit invloed op SEO?

Niet direct, en pagina's met interne zoekresultaten horen meestal niet geïndexeerd te worden. Goede interne zoekfunctionaliteit verbetert wel de betrokkenheid, en goed opgebouwde overzichtspagina's blijven wat zoekmachines en AI-assistenten moeten crawlen.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "inLanguage": "nl-NL",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Ondersteunt Supabase full-text search?",
      "acceptedAnswer": { "@type": "Answer", "text": "Ja, via full-text search in PostgreSQL met Nederlandse en Engelse configuraties en indexen." }
    },
    {
      "@type": "Question",
      "name": "Hoe maak ik zoeken tolerant voor typfouten?",
      "acceptedAnswer": { "@type": "Answer", "text": "Gebruik overeenkomst via pg_trgm met een trigramindex." }
    },
    {
      "@type": "Question",
      "name": "Wanneer gebruik ik vectorzoeken?",
      "acceptedAnswer": { "@type": "Answer", "text": "Wanneer betekenis belangrijker is dan exacte woorden, met embeddings in pgvector." }
    },
    {
      "@type": "Question",
      "name": "Hoe houdt Manifera zoeken veilig?",
      "acceptedAnswer": { "@type": "Answer", "text": "Zoeken volgt dezelfde toegangsregels en geeft openbare gebruikers alleen openbare velden terug." }
    },
    {
      "@type": "Question",
      "name": "Heeft interne zoekfunctionaliteit invloed op SEO?",
      "acceptedAnswer": { "@type": "Answer", "text": "Niet direct; pagina's met zoekresultaten horen meestal niet geïndexeerd te worden, overzichtspagina's wel." }
    }
  ]
}
</script>
