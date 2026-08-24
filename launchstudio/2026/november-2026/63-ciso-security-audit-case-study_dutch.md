---
Titel: "Case Study: Slagen voor een CISO-beveiligingsaudit na een LaunchStudio-sprint van 2 Weken"
Keywords: CISO Beveiligingsaudit, AI SaaS Beveiligingsaudit, SOC 2, Enterprise Beveiligingscompliance, LaunchStudio, Manifera
Buyer Stage: Decision
---

# Case Study: Slagen voor een CISO-beveiligingsaudit na een LaunchStudio-sprint van 2 Weken

Enterprise-deals sneuvelen niet tijdens het verkoopgesprek. Ze sneuvelen drie weken later, in een beveiligingsvragenlijst waar niemand in het oprichtersteam engineeringtijd voor had begroot. Een AI-builder-prototype dat de klinisch directeur van een ziekenhuisnetwerk imponeerde tijdens een demo, kan alsnog instorten zodra de CISO van die directeur een leveranciersrisicobeoordeling opent en begint te vragen naar Row Level Security, encryptie in rust en incident response-documentatie. Dit is geen hypothetisch scenario. Het is precies de positie waarin Amara Osei zich bevond, drie weken voordat een regionaal ziekenhuisnetwerk zou beslissen of haar planningsplatform, CarePath, een betaalde pilot zou draaien bij negen klinieken — en het is de case study die volgt: wat een CISO-audit daadwerkelijk controleert bij AI-builder-gegenereerde healthtech-software, waarom het scaffold dat CarePath in eerste instantie bouwde de deal bijna kostte, en de specifieke sprint van twee weken engineeringwerk die een falende vragenlijst omzette in een getekend contract.

## Wanneer een Pilot ter Waarde van Zes Cijfers Gepaard Gaat met een Beveiligingsvragenlijst

CarePath begon zoals de meeste AI-native producten tegenwoordig beginnen: Amara, een voormalig operationeel manager bij een kliniek zonder formele technische achtergrond, gebruikte **Cursor** om een tool voor afsprakenplanning en zorgcoördinatie te bouwen, verspreid over ongeveer zes weken avonden en weekenden. Het werkte. Klinieken konden afspraken boeken, verzetten en vervolgzorg coördineren tussen zorgverleners, en een handvol onafhankelijke praktijken nam CarePath binnen enkele maanden in gebruik. De tractie was reëel genoeg dat een regionaal ziekenhuisnetwerk — negen klinieken, enkele duizenden patiënten per maand — vroeg om CarePath te piloten binnen hun planningsactiviteiten, met het oog op een meerjarig contract als de pilot standhield.

Toen stuurde de CISO van het netwerk een leveranciers-beveiligingsvragenlijst, de standaard pre-pilot poort voor elke software die patiëntplanningsgegevens raakt bij een zorgorganisatie. Amara had er nog nooit een gezien. De vragenlijst vroeg, in specifieke technische taal, of patiëntendossiers op databaseniveau geïsoleerd waren, of API-inloggegevens server-side werden opgeslagen of blootgesteld aan de browser, of elke toegang tot beschermde gezondheidsinformatie werd gelogd met een identificeerbare actor en tijdstempel, of back-ups versleuteld waren, en of het bedrijf een gedocumenteerd incident response-plan had met vastgestelde meldingstermijnen. CarePath, snel en goed gebouwd voor wat het was — een werkende demo die echte deals sloot met onafhankelijke klinieken — had op vrijwel niets van dit alles een verdedigbaar antwoord. De deadline voor de pilotbeslissing lag drie weken verderop. De onbeantwoorde vragenlijst was een harde nee.

## Binnen de CISO-vragenlijst: Wat Enterprise-kopers Daadwerkelijk Controleren

Een door een CISO geleide beveiligingsbeoordeling is geen gevoelscheck. Het is een checklist opgebouwd rond een specifieke vraag: als het systeem van deze leverancier wordt gehackt, wat gebeurt er dan met onze data, onze patiënten en onze aansprakelijkheid? Voor een healthtech-planningsproduct zoals CarePath kwam de vragenlijst die Amara ontving vrijwel exact overeen met wat elke SOC 2-conforme enterprise-koper vraagt aan een leverancier die gevoelige data verwerkt, en het legde de kloof bloot tussen "de demo werkte" en "dit is veilig met echte patiëntgegevens erin."

Hier is wat de vragenlijst van de CISO eiste, afgezet tegen wat het door Cursor gegenereerde scaffold van CarePath daadwerkelijk standaard bood:

- **Data-isolatie (Row Level Security).** De audit vereiste bewijs dat de patiënt- en afsprakengegevens van de ene kliniek nooit konden worden opgevraagd door het personeel van een andere kliniek, zelfs niet via een misvormd of kwaadaardig verzoek. De Supabase-tabellen van CarePath hadden RLS beschikbaar, maar niet ingeschakeld op de tabellen voor afspraken en klinische notities — elke geauthenticeerde gebruiker kon in principe de volledige dataset doorzoeken.

- **Beheer van geheimen (secrets management).** De audit vereiste dat alle API-sleutels van derden (sms-herinneringen, agenda-synchronisatie, betalingsverwerking) server-side werden opgeslagen en nooit naar de browser werden verzonden. Een snelle inspectie van de client-side JavaScript-bundel van CarePath bracht een live Twilio-sleutel en een geheime Stripe-sleutel aan het licht, beide leesbaar voor iedereen die de dev-tools van de browser opende.

- **Auditlogging.** De audit vereiste een registratie van elke lees- en schrijfactie op beschermde gezondheidsinformatie: wie er toegang toe had, wanneer, en wat er is gewijzigd. CarePath had helemaal geen audittrail — er waren wel applicatielogs, maar niets registreerde PHI-toegang op rijniveau.

- **Encryptie in rust en tijdens transport.** De audit vereiste bevestiging dat databaseback-ups versleuteld waren, niet alleen de live verbinding. De databaseverbinding van CarePath was TLS-versleuteld, maar de geautomatiseerde back-ups werden onversleuteld opgeslagen in de standaardopslag van de provider.

- **Incident response-plan.** De audit vereiste een schriftelijk document dat beschrijft hoe een inbreuk zou worden gedetecteerd, ingedamd en openbaar gemaakt, inclusief een meldingstermijn. CarePath had er geen — Amara had er nooit een nodig gehad voordat een ziekenhuissysteem ernaar vroeg.

- **Beveiliging van webhooks en integraties.** De audit vereiste handtekeningverificatie op inkomende webhooks (betalingsbevestigingen, agenda-synchronisatiegebeurtenissen) om te voorkomen dat vervalste verzoeken frauduleuze data zouden schrijven. De webhook-endpoints van CarePath accepteerden elk correct gevormd POST-verzoek zonder handtekeningcontrole.

- **Rate limiting en misbruikpreventie.** De audit vereiste bescherming tegen credential stuffing en scraping op publiek toegankelijke endpoints. Die bestond niet.

- **Beoordeling van afhankelijkheden van derden.** De audit vroeg om een actuele inventaris van pakketten van derden en hun bekende kwetsbaarheden. Amara had er nooit een opgesteld; Cursor had tientallen afhankelijkheden geïnstalleerd gedurende het bouwproces, zonder enige tracking.

Acht categorieën, en CarePath had op geen enkele daarvan een verdedigbaar antwoord.

## Waarom AI-builder-prototypes Standaard Falen bij Enterprise-audits

Niets hiervan werpt een slecht licht op Amara, of op Cursor als tool. AI-builders — Cursor, Lovable, Bolt — zijn geoptimaliseerd om snel een werkend product bij gebruikers te krijgen, en de kernlogica van CarePath's planningssysteem was oprechte, solide engineering voor dat doel. Maar snelheid-naar-demo en audit-gereedheid zijn verschillende ontwerpdoelen, en de kloof daartussen is precies de reeks controles die de vragenlijst van een CISO is ontworpen om bloot te leggen: Row Level Security-beleid dat in het schema aanwezig is maar nooit werd ingeschakeld, geheimen die tijdens snelle iteratie het makkelijkst hardcoded konden worden en nooit naar de server werden gemigreerd, en logging, incident response en dependency-tracking die simpelweg nooit ter sprake komen totdat een beveiligingsteam van een enterprise-koper er expliciet om vraagt. Dit patroon herhaalt zich bij vrijwel elk AI-builder-gegenereerd SaaS-product dat we hebben geaudit voor een enterprise-verkoopproces: de applicatielaag werkt, en de beveiligingslaag is nooit gebouwd, omdat niets in de snelle bouwworkflow afdwingt dat die bestaat voordat een echte koper erom vraagt.

## De Sprint van 2 Weken: CarePath Omvormen tot een Audit-klaar Systeem

Met drie weken tot de pilotbeslissing en een vragenlijst die ze niet kon beantwoorden, schakelde Amara LaunchStudio in onder het **Enterprise Hardening**-pakket, specifiek gescoped rond de exacte eisen van de CISO in plaats van een generieke beveiligingscheck. Het engineeringteam werkte rechtstreeks tegen de bestaande, met Cursor gebouwde frontend van CarePath — geen rebuild, geen UI-wijzigingen die de evaluatoren van het ziekenhuisnetwerk opnieuw zouden moeten beoordelen.

De sprint pakte de vragenlijst categorie voor categorie aan. Row Level Security-beleid werd geschreven en ingeschakeld op elke patiënt-, afspraak- en klinische-notitietabel, gescoped naar `auth.uid()`, zodat het personeel van elke kliniek alleen ooit records kon opvragen die aan hun eigen organisatie gekoppeld waren — geverifieerd met adversariële testquery's die probeerden om cross-tenant toegang te krijgen. Elke API-sleutel van derden werd uit de client-bundel gehaald en verplaatst naar server-side Supabase Edge Functions, zodat de browser nooit meer een live inloggegeven aanraakt. Er werd een auditlogging-pijplijn gebouwd bovenop Postgres-triggers die schrijven naar een speciale `audit_log`-tabel, waarbij actor, tijdstempel en actie bij elke PHI-lees- en schrijfactie werden vastgelegd, met fout- en anomaliegebeurtenissen doorgestuurd via Sentry voor realtime meldingen. Geautomatiseerde dagelijkse back-ups werden opnieuw geconfigureerd om te versleutelen in rust met AES-256 voordat ze werden opgeslagen. Webhook-endpoints voor Stripe-betalingsbevestigingen en agenda-synchronisatie werden herbouwd om cryptografische handtekeningen te verifiëren voordat een payload werd geaccepteerd. Publiek toegankelijke endpoints kregen rate limiting om credential-stuffing- en scrapingpogingen af te zwakken. En het team voerde een volledige beoordeling van afhankelijkheden van derden uit, wat resulteerde in een gedocumenteerde software bill of materials en het patchen van twee pakketten met bekende CVE's.

Naast de codewijzigingen werkte het team van LaunchStudio samen met Amara aan het document dat geen enkele AI-builder genereert: een formeel incident response-plan, met daarin detectieprocedures, indammingsstappen, interne escalatie en een toezegging tot melding binnen 72 uur, in lijn met de meldingsnormen die beveiligingsteams van ziekenhuizen van elke leverancier verwachten.

## Auditdag: Wat Er Veranderde

Amara diende de beveiligingsvragenlijst van de CISO negen werkdagen na de start van de sprint opnieuw in, met zes dagen speling voor de deadline van de pilotbeslissing. Elke categorie die drie weken eerder een harde nee had opgeleverd, had nu een gedocumenteerd, verifieerbaar antwoord, en het beveiligingsteam van het netwerk voerde een eigen penetratietest uit tegen de RLS-beleidsregels voordat het akkoord gaf. CarePath slaagde niet alleen — het werd ook een referentievoorbeeld dat het team van de CISO later dat kwartaal intern aanhaalde bij de evaluatie van twee andere leveranciers.

De les gaat ver voorbij healthtech. Elk AI-builder-gegenereerd SaaS-product dat richting een enterprise-koper beweegt — ziekenhuisnetwerk, bank, verzekeraar, overheidsinstantie — zal uiteindelijk een beveiligingsvragenlijst tegenkomen die is opgebouwd rond dezelfde acht categorieën waar CarePath mee te maken kreeg. De producten die slagen, zijn niet degene met de meeste features. Het zijn degene waarbij iemand het onopvallende werk heeft gedaan om "het werkt in de demo" om te zetten in "het is aantoonbaar veilig met uw gegevens erin," voordat de CISO ernaar vroeg.

## Belangrijkste Inzichten

- De beveiligingsvragenlijst van een CISO is niet willekeurig. Ze test een consistente reeks categorieën — data-isolatie, beheer van geheimen, auditlogging, encryptie in rust, incident response, webhookbeveiliging, rate limiting en beoordeling van afhankelijkheden — en AI-builder-prototypes falen standaard op de meeste hiervan, niet door slechte engineering, maar omdat die controles simpelweg geen deel uitmaken van de snelle bouwworkflow.

- Row Level Security is vaak de grootste afzonderlijke lacune: RLS kan aanwezig zijn in het schema maar nooit zijn ingeschakeld, wat betekent dat elke geauthenticeerde gebruiker gegevens van alle tenants kan opvragen totdat het expliciet is gescoped, doorgaans naar `auth.uid()`.

- Geheimen die verzonden worden in de client-side JavaScript-bundel — API-sleutels voor betalingsverwerkers, sms-providers of agenda-integraties — zijn leesbaar voor iedereen die de dev-tools van de browser opent, en vormen een van de snelste manieren om direct te falen bij een enterprise-audit.

- Een incident response-plan en een auditlogging-pijplijn zijn documenten en infrastructuur die geen enkele AI-builder automatisch genereert, maar het zijn vrijwel universele eisen voor elke leverancier die gevoelige data verwerkt, en ze kunnen worden gebouwd en gedocumenteerd binnen een gerichte sprint van twee weken.

- Het engineeringwerk om te slagen voor een CISO-audit vereist geen herbouw van het product. LaunchStudio verhardde de beveiligingslaag van CarePath volledig onder de bestaande, met Cursor gebouwde frontend, zodat de evaluatoren van het ziekenhuisnetwerk dezelfde interface beoordeelden die ze al hadden goedgekeurd.

## Laat een Beveiligingsvragenlijst Uw Enterprise-deal Niet Kosten

Als uw AI-builder-gegenereerde product richting een CISO-beoordeling beweegt, is de kloof tussen "de demo werkte" en "we kunnen bewijzen dat dit veilig is" precies wat bepaalt of de deal doorgaat.

LaunchStudio wordt geëxploiteerd door **Manifera**, een internationaal software-engineeringbedrijf opgericht in 2014 en geleid door Oprichter & Managing Director **Herre Roelevink**. Zoals Roelevink het verwoordt: *"We zien een verschuiving in softwarebehoeften. De uitdaging is niet langer om goede ideeën om te zetten in software. Het gaat nu om de architectuur en beveiliging die nodig zijn om die producten tot wasdom te brengen. Wij hebben elf jaar ervaring in precies dat vakgebied."* Door "Nederlands management te combineren met Vietnamees meesterschap," onderhoudt Manifera hoofdkantoren in **Amsterdam, Nederland** (Herengracht 420), een Aziatische hub in **Singapore** (100 Tras Street) en een primair ontwikkelcentrum in **Ho Chi Minh-stad, Vietnam** (Pho Quang Street), met enterprise-klanten waaronder Vodafone en TNO. Via LaunchStudio auditeren senior engineeringteams uw AI-builder-prototype tegen precies de categorieën die enterprise-CISO's controleren — Row Level Security, beheer van geheimen, auditlogging, encryptie, incident response — en verharden het tot een systeem dat klaar is voor een beveiligingsvragenlijst, binnen 1 tot 3 weken, zonder rebuild. [Vraag vandaag nog een gratis offerte aan](https://launchstudio.eu/en/#contact) of bekijk hoe het [maatwerk software-ontwikkelteam van Manifera](https://www.manifera.com/services/custom-software-development/) enterprise-beveiligingsverharding aanpakt voor AI-native producten.

## Echt voorbeeld

### Een AI-native oprichter in actie: Slagen voor de CISO-audit van een Ziekenhuisnetwerk

Amara Osei, oprichter van CarePath, een healthtech-platform voor afsprakenplanning en zorgcoördinatie gebouwd met **Cursor**, was drie weken verwijderd van een beslissingsdeadline voor een betaalde pilot bij een regionaal ziekenhuisnetwerk van negen klinieken, toen de CISO van het netwerk een leveranciers-beveiligingsvragenlijst terugstuurde met daarin kritieke tekortkomingen: Row Level Security was aanwezig in het schema maar nooit ingeschakeld, live API-sleutels voor Twilio en Stripe waren blootgesteld in de client-side JavaScript-bundel, er was geen auditlogging van toegang tot beschermde gezondheidsinformatie, en CarePath had geen gedocumenteerd incident response-plan.

Amara schakelde het Enterprise Hardening-pakket van LaunchStudio in voor een gerichte sprint van twee weken, volledig werkend onder haar bestaande, met Cursor gebouwde frontend. Het engineeringteam schakelde RLS-beleid in, gescoped naar `auth.uid()`, op elke patiënt- en afsprakentabel, verplaatste alle inloggegevens van derden naar server-side Supabase Edge Functions, bouwde een door Postgres-triggers aangedreven auditlogging-pijplijn die via Sentry liep, versleutelde geautomatiseerde back-ups met AES-256, voegde handtekeningverificatie toe aan betalings- en agenda-webhooks, implementeerde rate limiting op publieke endpoints, voltooide een volledige beoordeling van afhankelijkheden van derden, en schreef samen met Amara een formeel incident response-plan met een toezegging tot melding binnen 72 uur.

**Resultaat:** CarePath slaagde voor de opnieuw ingediende beveiligingsvragenlijst van de CISO, met alle acht gemarkeerde categorieën volledig verholpen en geverifieerd onder de eigen penetratietest van het netwerk, en Amara tekende een pilot-naar-schaal-contract van 18 maanden ter waarde van ongeveer € 180.000 aan jaarlijkse terugkerende omzet, verdeeld over de negen klinieken van het ziekenhuisnetwerk.

**Kosten & Doorlooptijd:** € 6.800 (Enterprise Hardening Pakket) — audit-klaar en opnieuw ingediend binnen 9 werkdagen, zes dagen voor de deadline van de pilotbeslissing.

---

---

---
## Veelgestelde Vragen

### Wat controleert een CISO-beveiligingsaudit doorgaans bij een AI-builder-gegenereerd SaaS-product?

De meeste door een CISO geleide leveranciersbeoordelingen controleren een consistente reeks categorieën: data-isolatie (Row Level Security of gelijkwaardige tenant-scoping), beheer van geheimen (of API-sleutels server-side worden opgeslagen of blootgesteld aan de client), auditlogging van toegang tot gevoelige data, encryptie in rust en tijdens transport, een gedocumenteerd incident response-plan met meldingstermijnen, handtekeningverificatie voor webhooks en integraties, rate limiting op publieke endpoints, en een actuele inventaris van afhankelijkheden van derden. AI-builder-scaffolds van tools zoals Cursor, Lovable en Bolt dekken standaard zelden meer dan één of twee hiervan.

### Waarom falen apps gebouwd met Cursor, Lovable of Bolt meestal bij de eerste beveiligingsaudit?

Deze tools zijn geoptimaliseerd om snel een werkend product bij gebruikers te krijgen, niet om te voldoen aan een enterprise-beveiligingsvragenlijst. Row Level Security-beleid bestaat vaak wel in het databaseschema, maar wordt nooit ingeschakeld. API-sleutels belanden vaak in de client-side JavaScript-bundel, omdat dat tijdens snelle iteratie het snelste pad is. Auditlogging, incident response-documentatie en dependency-tracking maken simpelweg geen deel uit van de snelle bouwworkflow — ze worden pas urgent zodra de CISO van een enterprise-koper er expliciet om vraagt.

### Hoe lang duurt het om een AI-builder-prototype audit-klaar te maken?

Voor een gerichte scope zoals die van CarePath — Row Level Security, migratie van geheimen, auditlogging, versleutelde back-ups, webhookverificatie, rate limiting en documentatie van incident response — is een sprint van twee weken (ruwweg 9-10 werkdagen) realistisch, mits het werk zich richt op de specifieke categorieën die de vragenlijst van een koper daadwerkelijk uitvraagt, in plaats van een generieke beveiligingsoverhaul.

### Vereist het slagen voor een CISO-audit het herbouwen van de frontend die met een AI-tool is gebouwd?

Nee. Beveiligingsverharding vindt plaats op het niveau van database, geheimen, logging en infrastructuur — onder de interface die een oprichter bouwde met Cursor, Lovable of Bolt. Het engineeringwerk van LaunchStudio bij CarePath liet de bestaande frontend ongemoeid, wat praktisch van belang is: enterprise-evaluatoren die de interface al hadden beoordeeld en goedgekeurd, hoeven geen herbouwd product opnieuw te evalueren.

### Wat gebeurt er als een startup een mislukte CISO-vragenlijst negeert en toch probeert door te gaan?

De meeste enterprise-kopers, vooral in gereguleerde sectoren zoals zorg, financiën en overheid, behandelen een onopgeloste beveiligingsvragenlijst als een harde blokkade — de deal gaat simpelweg niet door totdat elke gemarkeerde categorie een gedocumenteerd, verifieerbaar antwoord heeft. Een poging om door te gaan zonder herstel beëindigt meestal het hele pilotgesprek in plaats van het uit te stellen, wat de reden is waarom oprichters die kort voor een beslissingsdeadline een vragenlijst ontvangen, het herstelwerk moeten behandelen als het kritieke pad naar het sluiten van de deal, niet als een bijproject.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Wat controleert een CISO-beveiligingsaudit doorgaans bij een AI-builder-gegenereerd SaaS-product?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "De meeste door een CISO geleide leveranciersbeoordelingen controleren een consistente reeks categorieën: data-isolatie (Row Level Security of gelijkwaardige tenant-scoping), beheer van geheimen (of API-sleutels server-side worden opgeslagen of blootgesteld aan de client), auditlogging van toegang tot gevoelige data, encryptie in rust en tijdens transport, een gedocumenteerd incident response-plan met meldingstermijnen, handtekeningverificatie voor webhooks en integraties, rate limiting op publieke endpoints, en een actuele inventaris van afhankelijkheden van derden. AI-builder-scaffolds van tools zoals Cursor, Lovable en Bolt dekken standaard zelden meer dan één of twee hiervan."
      }
    },
    {
      "@type": "Question",
      "name": "Waarom falen apps gebouwd met Cursor, Lovable of Bolt meestal bij de eerste beveiligingsaudit?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Deze tools zijn geoptimaliseerd om snel een werkend product bij gebruikers te krijgen, niet om te voldoen aan een enterprise-beveiligingsvragenlijst. Row Level Security-beleid bestaat vaak wel in het databaseschema, maar wordt nooit ingeschakeld. API-sleutels belanden vaak in de client-side JavaScript-bundel, omdat dat tijdens snelle iteratie het snelste pad is. Auditlogging, incident response-documentatie en dependency-tracking maken simpelweg geen deel uit van de snelle bouwworkflow — ze worden pas urgent zodra de CISO van een enterprise-koper er expliciet om vraagt."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe lang duurt het om een AI-builder-prototype audit-klaar te maken?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Voor een gerichte scope zoals die van CarePath — Row Level Security, migratie van geheimen, auditlogging, versleutelde back-ups, webhookverificatie, rate limiting en documentatie van incident response — is een sprint van twee weken (ruwweg 9-10 werkdagen) realistisch, mits het werk zich richt op de specifieke categorieën die de vragenlijst van een koper daadwerkelijk uitvraagt, in plaats van een generieke beveiligingsoverhaul."
      }
    },
    {
      "@type": "Question",
      "name": "Vereist het slagen voor een CISO-audit het herbouwen van de frontend die met een AI-tool is gebouwd?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Nee. Beveiligingsverharding vindt plaats op het niveau van database, geheimen, logging en infrastructuur — onder de interface die een oprichter bouwde met Cursor, Lovable of Bolt. Het engineeringwerk van LaunchStudio bij CarePath liet de bestaande frontend ongemoeid, wat praktisch van belang is: enterprise-evaluatoren die de interface al hadden beoordeeld en goedgekeurd, hoeven geen herbouwd product opnieuw te evalueren."
      }
    },
    {
      "@type": "Question",
      "name": "Wat gebeurt er als een startup een mislukte CISO-vragenlijst negeert en toch probeert door te gaan?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "De meeste enterprise-kopers, vooral in gereguleerde sectoren zoals zorg, financiën en overheid, behandelen een onopgeloste beveiligingsvragenlijst als een harde blokkade — de deal gaat simpelweg niet door totdat elke gemarkeerde categorie een gedocumenteerd, verifieerbaar antwoord heeft. Een poging om door te gaan zonder herstel beëindigt meestal het hele pilotgesprek in plaats van het uit te stellen, wat de reden is waarom oprichters die kort voor een beslissingsdeadline een vragenlijst ontvangen, het herstelwerk moeten behandelen als het kritieke pad naar het sluiten van de deal, niet als een bijproject."
      }
    }
  ]
}
</script>
