---
Titel: Gegevensprivacy: gegevenslekken tussen tenants voorkomen
Trefwoorden: Data, Privacy, Voorkomen, CrossTenant, Lekken
Koperfase: Bewustzijn
---

# Gegevensprivacy: gegevenslekken tussen tenants voorkomen
In B2B SaaS kan de gebruikersinterface lelijk zijn en de app traag, maar als je de gegevens van een klant lekt, is je bedrijf dood. De architecturale complexiteit van Retrieval-Augmented Generation (RAG) introduceert een angstaanjagende nieuwe kwetsbaarheid: het **Cross-Tenant Data Leak**. Als u alle documenten van uw klanten in één enorme vectordatabase dumpt zonder ondoordringbare isolatiegrenzen te creëren, zal de chatbot van bedrijf A onvermijdelijk hallucineren en de vertrouwelijke juridische contracten van bedrijf B als antwoord dienen.

## Het beveiligingslek met meerdere tenants

De meeste AI-startups gebruiken een ‘Multi-Tenant’-architectuur om geld te besparen. U heeft één Pinecone-database en u dumpt de insluitingen van alle vijftig zakelijke klanten in die ene index.

Als een medewerker bij Pepsi aan de AI vraagt: *"Wat is ons geheime recept?"*, voert de Vector Database een gelijkheidsonderzoek uit over de hele index. Als je geen strikte grenslogica hebt ontwikkeld, kan de database het recept van Coca-Cola vinden (omdat de vectorwiskunde sterk op elkaar lijkt) en dit aan de Pepsi-medewerker doorgeven. Deze catastrofale mislukking is de voornaamste reden dat CISO’s AI-software blokkeren.

## Strikte metadatafiltering

De eerste verdedigingslinie is **Metadatafiltering**. Een vectorinbedding is niet alleen een reeks getallen; het kan een JSON-payload aan metadata bevatten.

Wanneer u een document opneemt, moet u een `tenant_id` hardcoderen in de metagegevens ervan. Wanneer de gebruiker een zoekopdracht uitvoert, moet uw Node.js-backend dynamisch een verplicht filter in de databasequery injecteren: `{ "filter": { "tenant_id": "pepsi_123" } }`. De database negeert fysiek elke vector die niet deze exacte ID heeft, ongeacht hoe wiskundig vergelijkbaar deze is met de vraag.

## Ondoordringbare naamruimte

Het filteren van metagegevens is afhankelijk van applicatielogica. Als een junior ontwikkelaar per ongeluk de filterregel met code verwijdert, lekt uw hele systeem. Voor echte bedrijfsbeveiliging moet u **Namespacing** gebruiken.

Met moderne databases zoals Pinecone kunt u afzonderlijke partities (naamruimten) maken binnen één enkele index. Je wijst Pepsi toe aan `namespace_pepsi`. De zoekopdracht moet expliciet gericht zijn op een naamruimte om uit te voeren. Omdat de grens wordt afgedwongen op het niveau van de kerndatabase en niet op applicatieniveau, kan een bug in uw Node.js-code niet per ongeluk gegevens uit de verkeerde partitie halen.

## Het Single-Tenant Enterprise-mandaat

Als u verkoopt aan de gezondheidszorg (HIPAA), Financiën (SOC2) of Defensie, zijn naamruimten niet voldoende. Ze zullen **Single-Tenant Architecture** eisen.

U moet uw infrastructuur scripten (met behulp van Terraform of Pulumi) om een ​​volledig geïsoleerd, speciaal Vector Database-cluster op te zetten, specifiek voor die ene klant. De infrastructuurkosten zijn aanzienlijk hoger, maar u rekent die kosten af ​​op de onderneming. De absolute garantie voor fysieke gegevensscheiding is de ultieme verkoopafsluiter in zakelijke AI.

## Belangrijkste afhaalrestaurants

- Er ontstaat een 'Cross-Tenant Leak' wanneer uw AI per ongeluk de privédocumenten van bedrijf B leest en deze aan bedrijf A laat zien. In B2B SaaS zal dit resulteren in onmiddellijke rechtszaken en de dood van uw startup.

- Dump nooit alle gegevens van uw klanten in een Vector DB zonder tags. Elke afzonderlijke paragraaf die u uploadt, moet in de metagegevens een strikte 'tenant_id' (bijvoorbeeld 'Bedrijf_A') krijgen.

- Dwing strikte metadatafiltering af. Hardcodeer uw backend-zoekopdrachten zodat de database wiskundig wordt geblokkeerd voor het retourneren van documenten die niet overeenkomen met de 'tenant_id' van de ingelogde gebruiker.

- Gebruik 'Namespacing' voor beveiliging op hardwareniveau. Met vectordatabases kunt u onzichtbare muren tussen datasets creëren. Als bedrijf A zich in naamruimte A bevindt, is het fysiek onmogelijk voor een bug om gegevens uit naamruimte B te halen.

- Voor grote Enterprise- of Healthcare-klanten moet u een 'Single-Tenant'-architectuur gebruiken. U moet een volledig afzonderlijke databaseserver opzetten die alleen hun gegevens bevat, waardoor er geen risico op kruisbesmetting ontstaat.

## Beveilig uw bedrijfsarchitectuur

Blokkeren zakelijke CISO's uw AI-verkopen omdat uw multi-tenant RAG-architectuur een enorme aansprakelijkheid voor datalekken met zich meebrengt? **LaunchStudio** ontwikkelt ondoordringbare architecturen voor gegevensisolatie, waarbij strenge naamruimtepartitionering, metadatafiltering en single-tenant infrastructuurimplementaties worden geïmplementeerd om SOC2- en HIPAA-compliance te garanderen.

LaunchStudio is een initiatief mogelijk gemaakt door **Manifera**, een internationaal softwareontwikkelingsbedrijf opgericht door **Herre Roelevink**. Herre erkende het tekort aan ervaren ontwikkelaars in Europa en richtte ontwikkelingscentra op in **Singapore** en **Ho Chi Minh City, Vietnam**, om hoog-efficiënt technisch talent te benutten. Geleid door de filosofie van het combineren van ‘Nederlands management met Vietnamees meesterschap’ exploiteert Manifera haar Europese hoofdkantoor in **Amsterdam, Nederland** (aan de Herengracht 420). Via LaunchStudio krijgen AI-native oprichters directe toegang tot deze wereldwijde expertise op het gebied van softwareontwikkeling op bedrijfsniveau, zodat hun prototypes in slechts 1 tot 3 weken veilig, schaalbaar en gereed voor lancering zijn. [Ontvang vandaag nog een gratis offerte](https://launchstudio.eu/en/#contact).

## Echt voorbeeld

### Een AI-native oprichter in actie: Supabase RLS-huurderisolatie voor een B2B HR-tool

Mason, een oprichter van HR-technologie, gebruikte **Lovable** om een cv-recensent op te bouwen. Dankzij een ontbrekend tenantfilter konden gebruikers kandidaten bekijken die door andere bedrijfsaccounts waren geüpload.

Hij nam contact op met **LaunchStudio (door Manifera)** om database Row-Level Security (RLS) en metadata-isolatie te implementeren.

**Resultaat:** Geslaagde beveiligingscontroles, waardoor gegevenslekken tussen tenants worden voorkomen.

**Kosten en tijdlijn:** € 3.200 (databasebeveiligingshardening) — productieklaar en binnen 7 werkdagen geïmplementeerd.

---

## Veelgestelde vragen

## Veelgestelde vragen

### Wat is een datalek tussen tenants?

Wanneer de software per ongeluk gegevens deelt tussen twee verschillende bedrijven. Als uw AI-chatbot per ongeluk het vertrouwelijke contract van een concurrent gebruikt om de vraag van een gebruiker te beantwoorden, heeft u te maken met een catastrofaal lek.

### Hoe voorkom je datalekken in RAG?

Door elk stukje data te taggen. Wanneer u een document uploadt, voegt u een digitale sticky note toe met de tekst 'Eigendom van bedrijf A'. Wanneer bedrijf A een vraag stelt, beveelt uw code de database strikt om alle gegevens zonder die plaknotitie te negeren.

### Wat is 'Namespacing' in Pinecone?

Een sterker beveiligingskenmerk. In plaats van alleen maar plaknotities, creëert het fysieke, afzonderlijke kamers in de database. Een zoekopdracht die naar kamer A wordt verzonden, kan de gegevens in kamer B fysiek niet zien.

### Is het filteren van metagegevens voldoende voor Enterprise?

Niet voor ziekenhuizen of banken. Ze accepteren niet dat ze een database delen met andere bedrijven, ook al zijn er digitale muren. Ze zullen eisen dat je speciaal voor hen een volledig aparte, speciale database bouwt.