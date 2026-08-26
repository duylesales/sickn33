---
Titel: "Kiezen Tussen Row-Level Security en Autorisatie op Applicatieniveau voor Multi-Tenant AI"
Keywords: Row-Level Security, Applicatielaag Autorisatie, Multi-Tenant SaaS, Supabase RLS, Tenant Isolatie, LaunchStudio, Manifera
Buyer Stage: Decision
---

# Kiezen Tussen Row-Level Security en Autorisatie op Applicatieniveau voor Multi-Tenant AI

Elk multi-tenant AI SaaS-product moet vroeg of laat hetzelfde fundamentele vraagstuk oplossen: wáár bevindt zich de logica die ervoor zorgt dat data van de ene klant strikt onzichtbaar blijft voor de andere? Er zijn twee wezenlijk verschillende architectonische benaderingen: Row-Level Security (RLS) gehandhaafd op databaseniveau, of autorisatiecontroles geprogrammeerd in de applicatiecode. Codebases gegenereerd door Lovable, Bolt en Cursor eindigen helaas vaak met een inconsistente, halfslachtige mix van beide, wat risicovoller is dan een bewuste keuze voor één van de twee methoden. Dit artikel legt uit wat beide benaderingen inhouden, waar de krachten liggen, en hoe u de juiste keuze maakt voor uw product.

## Wat Row-Level Security Daadwerkelijk Doet

Row-Level Security is een ingebouwde PostgreSQL-functionaliteit — standaard beschikbaar in Supabase — waarmee toegangsbeleid (*policies*) direct aan een databasetabel wordt gekoppeld. De database bepaalt zelf welke rijen een specifieke query mag inzien of wijzigen op basis van de geauthenticeerde gebruiker (`auth.uid()`) of een tenant-ID kolom. Dit betekent dat zelfs een ruwe SQL-query, een programmeerfout in de backend of een gecompromitteerd API-endpoint nooit gegevens van een andere tenant kan uitlezen. De beveiliging is verankerd in de datalaag zelf, volledig onafhankelijk van de bovenliggende applicatiecode.

## Wat Autorisatie op Applicatieniveau Daadwerkelijk Doet

Bij autorisatie op applicatieniveau bevindt alle toegangscontrolelogica zich in uw backendcode. Een API-route verifieert de identiteit en rechten van de verzoekende gebruiker, stelt een databasequery samen die expliciet filtert op de toegestane data (`WHERE tenant_id = x`), en retourneert alleen die resultaten. De database heeft in dit model geen enkel inherent besef van klantscheiding — hij retourneert simpelweg wat de query opvraagt. De volledige verantwoordelijkheid voor correcte datasegregatie ligt bij de ontwikkelaar die de query samenstelt.

## De Fundamentele Afweging: Defense in Depth vs. Flexibiliteit

Het verschil zit niet in welke methode abstract gezien "veiliger" is, maar in hoe het systeem faalt bij menselijke fouten en hoeveel flexibiliteit er is voor complexe bedrijfslogica:

**RLS faalt veilig (*fail-safe*); applicatie-autorisatie faalt open (*fail-open*).** Als een ontwikkelaar bij autorisatie op applicatieniveau vergeet een `WHERE tenant_id = x` clausule toe te voegen aan een nieuw API-endpoint, retourneert het endpoint zonder waarschuwing alle data van alle klanten. De fout blijft onopgemerkt totdat een klant data van een concurrent op zijn scherm ziet. Onder RLS maakt zo'n vergeten clausule niet uit: het databasebeleid blijft van kracht, waardoor de query automatisch een lege of correct gefilterde resultatenset oplevert. Dit principe van *defense in depth* is het grootste praktische voordeel van RLS.

**Applicatie-autorisatie verwerkt complexe, contextuele logica natuurlijker.** Autorisatieregels die afhangen van meerdere dynamische factoren — een gebruikersrol, de vertrouwelijkheidsstatus van een document, tijdelijke toegang en verificatie via een extern IAM-systeem — zijn in applicatiecode vaak helderder te modelleren dan in complexe Postgres-policy expressies, die bij te veel bedrijfslogica moeilijk testbaar en traag kunnen worden.

**RLS geldt automatisch voor elk toegangspad; applicatie-autorisatie moet overal opnieuw worden toegepast.** Een nieuw beheerdersscript, een data-exportfunctie, een directe query via een beheertool of een toekomstig mobiel endpoint — onder RLS erven al deze paden automatisch dezelfde databescherming. Bij applicatie-autorisatie moet elk nieuw endpoint de filters opnieuw foutloos implementeren.

## Waar Dit Specifiek Misgaat bij AI-Builders

Door Lovable, Bolt en Cursor gegenereerde Supabase-omgevingen bevatten zeer frequent tabellen waarbij RLS in het dashboard *aan* staat, maar waarbij het gekoppelde beleid *default-permissive* is ingesteld (bijvoorbeeld `USING (true)`). Dit beperkt in werkelijkheid niets. Dit wekt een gevaarlijke schijnveiligheid: een oprichter ziet een groen vinkje bij RLS en veronderstelt dat zijn tenant-isolatie geregeld is, terwijl elke ingelogde gebruiker via de API de records van alle andere bedrijven kan opvragen.

Omgekeerd genereren AI-tools individuele API-routes weliswaar netjes, maar hebben ze geen overkoepelend mechanisme om te waarborgen dat elk nieuw gegenereerd endpoint consistent de juiste tenant-filters toepast.

## Een Praktische Aanbeveling: Gelaagde Beveiliging

Voor veruit de meeste multi-tenant AI SaaS-applicaties op Supabase of Postgres is de juiste oplossing niet kiezen tussen de twee, maar ze **gelaagd combineren**:

1. **RLS als ononderhandelbare basisbescherming:** Elke tabel met tenant-gevoelige data krijgt een strikte RLS-policy op `tenant_id`. Dit sluit het risico van menselijke vergeetachtigheid op dataniveau definitief uit (*fail-safe*).

2. **Applicatielogica voor complexe autorisatie:** Complexe rechtenstructuren (rolhiërarchieën, tijdsgebonden delegaties, externe permissiechecks) worden gemodelleerd in de applicatielaag bóvenop het RLS-fundament.

## De Prestatie-Mythe Rondom RLS

Oprichters vrezen soms dat RLS queries drastisch vertraagt. Een zorgvuldig geschreven RLS-policy die filtert op een geïndexeerde `tenant_id`-kolom voegt in werkelijkheid slechts een fractie van een milliseconde overhead toe — volstrekt onzichtbaar naast de rekentijd van een LLM. Vertragingen ontstaan alleen wanneer een policy ongeïndexeerde joins over meerdere zware tabellen uitvoert. Dat is geen structureel RLS-probleem, maar een kwestie van ontbrekende database-indexen.

## De Aanpak van LaunchStudio

LaunchStudio hanteert RLS als verplichte standaard voor multi-tenant architecturen, gevalideerd via *adversarial penetration testing*: we testen actief of kwaadwillende of afwijkende queries van tenant A gegevens van tenant B kunnen forceren. Waar complexe bedrijfsrechten nodig zijn, bouwen we deze netjes in de applicatielaag bovenop het RLS-fundament.

Dit valt doorgaans onder het **Relaunch & Scale**-pakket (ongeveer €2.500–€4.500) voor een standaard multi-tenant audit en RLS-implementatie, of **Enterprise Hardening** (€5.000–€7.500) voor oprichters die moeten voldoen aan strenge enterprise security reviews, opgeleverd in 1 tot 3 weken.

## Belangrijkste Inzichten

- RLS faalt veilig (*fail-safe*) omdat het databasebeleid altijd geldt, terwijl applicatie-autorisatie faalt open (*fail-open*) bij een vergeten filter in een nieuw endpoint.

- RLS beschermt automatisch alle toegangspaden, inclusief toekomstige API-endpoints, exports en beheerscripts.

- AI-builders leveren RLS regelmatig op met "alles-toegestaan"-policies die schijnveiligheid creëren.

- Complexe rolstructuren en dynamische permissies worden het best gemodelleerd in de applicatielaag bóvenop een solide RLS-basis.

- LaunchStudio implementeert en valideert gelaagde multi-tenant isolatie met geautomatiseerde penetratietests binnen 1 tot 3 weken.

## Laat uw Multi-Tenant Beveiliging Bewijzen, Niet Aannemen

Voordat het securityteam van een enterprise-klant vraagt hoe u data van verschillende klanten scheidt, moet uw architectuur bestand zijn tegen strenge pentests, niet alleen tegen een vrolijke demo.

LaunchStudio wordt beheerd door **Manifera**, een internationaal software engineering-bedrijf opgericht in 2014 onder leiding van Oprichter & Managing Director **Herre Roelevink**. Manifera brengt 11+ jaar ervaring in productie-engineering en enterprise-klanten zoals Vodafone en TNO mee naar elk security- en compliance-traject voor AI SaaS-oprichters. Met de filosofie "Nederlands management gecombineerd met Vietnamees meesterschap" heeft Manifera haar hoofdkantoor in **Amsterdam, Nederland** (Herengracht 420), een Asia-hub in **Singapore** (100 Tras Street) en een primair ontwikkelcentrum in **Ho Chi Minhstad, Vietnam** (Pho Quang Street). Via LaunchStudio implementeren en verifiëren senior engineeringteams Row-Level Security en gelaagde autorisatie — waarmee uw prototype in 1 tot 3 weken verandert in een veilige, enterprise-ready MVP, zonder herbouw. [Vraag vandaag nog een gratis offerte aan](https://launchstudio.eu/nl/#contact) of ontdek hoe het [maatwerk software development team](https://www.manifera.com/nl/services/maatwerk-software-ontwikkeling/) van Manifera tenant-isolatie implementeert voor AI-codebases.

## Echt voorbeeld

### Een AI-Native Oprichter in de Praktijk: Patiënt-Intake Assistent voor Klinieken

Priya, voormalig consultant in de zorgsector, gebruikte **Bolt** om een AI-intake assistent te bouwen waarmee klinieken met meerdere locaties medische vragenlijsten konden verwerken. Haar door Bolt gegenereerde Supabase-database had RLS ingeschakeld staan in het dashboard, waardoor Priya aannam dat de datasegregatie in orde was. Tijdens een pre-launch security review bleek echter dat de policies op de patiëntentabel default-permissive waren ingesteld: elke ingelogde medewerker van kliniek A kon ongehinderd patiëntgegevens van kliniek B opvragen.

Priya schakelde LaunchStudio in om dit structureel te herstellen vóór de uitrol bij haar eerste zorgnetwerk. Het team herschreef alle tabellen met strikte RLS-policies op basis van `clinic_id` en rol, en voegde een applicatielaag toe voor een complexe uitzondering: een reizende arts die tijdelijk geautoriseerde toegang tot meerdere locaties nodig had.

**Resultaat:** Adversarial security tests bevestigden nul ongeautoriseerde toegang over kliniekgrenzen heen, en Priya kon een officieel auditrapport overleggen aan het securityteam van het zorgnetwerk.

**Kosten & Doorlooptijd:** €4.100 (Enterprise Hardening Pakket) — RLS-audit, herstel en autorisatielagen afgerond in 13 werkdagen.

---

---

---
## Veelgestelde Vragen

### Moet ik Row-Level Security of applicatie-autorisatie gebruiken voor mijn multi-tenant AI SaaS?

Voor vrijwel alle op Postgres gebaseerde producten is het antwoord: combineer beide op de juiste manier. Gebruik RLS als de onwrikbare basisbescherming die data altijd afschermt op databaseniveau, en gebruik de applicatielaag voor complexe, contextuele roltoewijzingen.

### Wat betekent het dat RLS "veilig faalt" (*fail-safe*) ten opzichte van applicatielogica?

Als een programmeur een filter vergeet in een nieuw API-endpoint, blokkeert de RLS-databasepolicy de toegang alsnog automatisch. Bij zuivere applicatie-autorisatie leidt een vergeten filter direct tot het lekken van data van alle klanten, omdat de database zelf geen restricties kent.

### Waarom creëren AI-builders zoals Bolt of Lovable vaak schijnveiligheid rondom RLS?

Omdat deze tools RLS in de databaseschema's vaak aanzetten met standaardregels die alles toestaan (`USING (true)`). In het dashboard staat een groen vinkje bij RLS, maar in werkelijkheid is de data voor iedereen toegankelijk.

### Is autorisatie op applicatieniveau ooit voldoende op zichzelf?

Alleen wanneer u een database gebruikt die geen native row-level beveiliging ondersteunt, of wanneer rechten volledig afhangen van externe systemen die per verzoek moeten worden geraadpleegd. Zelfs dan blijft het een bewuste afweging om het risico van *fail-open* te accepteren.

### Hoe controleert LaunchStudio of RLS daadwerkelijk waterdicht is?

Via geautomatiseerde *adversarial testing*: we voeren gerichte aanvallen en afwijkende queries uit vanuit het perspectief van tenant A om te bewijzen dat records van tenant B onder geen enkele voorwaarde kunnen worden ingezien of gemuteerd.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Moet ik Row-Level Security of applicatie-autorisatie gebruiken voor mijn multi-tenant AI SaaS?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Voor vrijwel alle op Postgres gebaseerde producten is het antwoord: combineer beide op de juiste manier. Gebruik RLS als de onwrikbare basisbescherming die data altijd afschermt op databaseniveau, en gebruik de applicatielaag voor complexe, contextuele roltoewijzingen."
      }
    },
    {
      "@type": "Question",
      "name": "Wat betekent het dat RLS \"veilig faalt\" (fail-safe) ten opzichte van applicatielogica?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Als een programmeur een filter vergeet in een nieuw API-endpoint, blokkeert de RLS-databasepolicy de toegang alsnog automatisch. Bij zuivere applicatie-autorisatie leidt een vergeten filter direct tot het lekken van data van alle klanten, omdat de database zelf geen restricties kent."
      }
    },
    {
      "@type": "Question",
      "name": "Waarom creëren AI-builders zoals Bolt of Lovable vaak schijnveiligheid rondom RLS?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Omdat deze tools RLS in de databaseschema's vaak aanzetten met standaardregels die alles toestaan (USING (true)). In het dashboard staat een groen vinkje bij RLS, maar in werkelijkheid is de data voor iedereen toegankelijk."
      }
    },
    {
      "@type": "Question",
      "name": "Is autorisatie op applicatieniveau ooit voldoende op zichzelf?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Alleen wanneer u een database gebruikt die geen native row-level beveiliging ondersteunt, of wanneer rechten volledig afhangen van externe systemen die per verzoek moeten worden geraadpleegd. Zelfs dan blijft het een bewuste afweging om het risico van fail-open te accepteren."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe controleert LaunchStudio of RLS daadwerkelijk waterdicht is?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Via geautomatiseerde adversarial testing: we voeren gerichte aanvallen en afwijkende queries uit vanuit het perspectief van tenant A om te bewijzen dat records van tenant B onder geen enkele voorwaarde kunnen worden ingezien of gemuteerd."
      }
    }
  ]
}
</script>
