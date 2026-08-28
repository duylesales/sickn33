---
Titel: "Case Study: Een Enterprise Beveiligingsvragenlijst Doorstaan in 10 Werkdagen"
Trefwoorden: Case study security questionnaire, enterprise deal acceleration, VSAQ audit, LaunchStudio, Manifera
Koperfase: Beslissing
Doelgroep: Enterprise Founders / Sales Engineers
---

# Case Study: Een Enterprise Beveiligingsvragenlijst Doorstaan in 10 Werkdagen

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Case Study: Een Enterprise Beveiligingsvragenlijst Doorstaan in 10 Werkdagen",
  "description": "Hoe een AI HR-tool uit Utrecht een contract van €120k sloot na het succesvol voltooien van een 250-vragen InfoSec review binnen 10 dagen.",
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
  "datePublished": "2026-08-69",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://launchstudio.eu/nl/blog/enterprise-security-questionnaire-case-study"
  }
}
</script>

AI-builders kunnen een werkende SaaS-product sneller dan ooit bij een prospect krijgen. Maar enterprise-kopers geven geen groen licht op basis van een demo — ze geven groen licht op basis van een vragenlijst. Dit is het waargebeurde verhaal van Fatima Al-Sayed, oprichter van een AI-platform voor sales-enablement, die zag hoe een veelbelovende deal met een enterprise-klant, ter waarde van zes cijfers, vastliep in de inkoopprocedure toen haar werd gevraagd schriftelijk te bewijzen dat haar door AI gegenereerde backend vertrouwd kon worden met de gegevens van een Fortune 500-bedrijf. Ze kon slechts 11 van de 40 vragen eerlijk met "ja" beantwoorden. Hier leest u precies wat ze heeft opgelost, in welke volgorde, en hoe ze van een score van 11/40 naar een gesloten deal ging in minder dan drie weken.

## De deal die bijna sneuvelde in de inkoopprocedure

Fatima bouwde PitchCraft AI, een tool die AI gebruikt om verkooppresentaties te genereren en te scoren aan de hand van de openbare rapportages en nieuwssignalen van een koper, in zes intensieve weken met **Bolt**. Het product werkte. Het werkte zo goed dat een mid-market sales director bij een Europese verzekeringsgroep het intern verdedigde na een demo van 20 minuten, en binnen enkele dagen had Fatima een mondelinge toezegging voor een pilot met 200 gebruikers.

Vervolgens ging de deal naar de inkoopafdeling, en die stuurde het door naar het informatiebeveiligingsteam van de verzekeraar. Wat terugkwam was geen afwijzing — het was erger, op de manier waarop alleen papierwerk erger kan zijn. Een vragenlijst met 40 items over leveranciersbeveiliging, het soort dat elk enterprise-bedrijf tegenwoordig uitvoert voordat een SaaS-tool in aanraking komt met gegevens van medewerkers of klanten, met een strikte kanttekening: de interne beoordelingscommissie kwam over 10 werkdagen bijeen, en onbeantwoorde of onbevredigende items zouden standaard als "nee" worden geteld, wat zou resulteren in een afgewezen leverancier.

Fatima opende de spreadsheet met de verwachting deze in een middag door te nemen. Ze kwam er in één zitting niet doorheen. Er werd gevraagd naar zaken waar ze werkelijk nooit bij had stilgestaan terwijl ze drie weken diep in Bolt-prompts zat om haar pitch-scoring-UI er goed uit te laten zien.

## Elf van de veertig: wat de vragenlijst daadwerkelijk vroeg

De vragenlijst was georganiseerd in acht secties, en toen Fatima deze eerlijk had doorgewerkt, kon ze slechts 11 van de 40 items met vertrouwen op "ja" zetten — grotendeels de eenvoudige, zoals het afdwingen van HTTPS op haar domein en een gepubliceerd privacybeleid. De categorieën die haar de das omdeden, waren precies de categorieën waar enterprise-beveiligingsteams het meest om geven:

- **Versleuteling in rust en tijdens overdracht**: Ze kon bevestigen dat TLS actief was aan de frontend-zijde, maar had geen documentatie over of haar Supabase-database versleuteling in rust afdwong, en geen antwoord op hoe encryptiesleutels werden beheerd of geroteerd.

- **Row Level Security / tenant-isolatie**: De vragenlijst vroeg in gewone taal: "Hoe wordt klantdata logisch geïsoleerd van andere tenants in een multi-tenant omgeving?" Fatima's eerlijke antwoord was dat isolatie werd afgehandeld in de querylogica van haar applicatie, niet afgedwongen op databaseniveau — precies het soort antwoord dat een technische beoordeling op het eerste gezicht al doet mislukken.

- **Incident response-plan**: Er was er geen. Geen gedocumenteerd escalatiepad, geen gedefinieerde tijdlijn voor het melden van datalekken, niets om bij de vragenlijst te voegen.

- **Lijst van subverwerkers**: De verzekeraar wilde een volledige lijst van elke derde partij die hun gegevens verwerkte — hostingprovider, databaseleverancier, LLM-provider, e-maildienst — inclusief bevestiging dat elk van hen een ondertekende verwerkersovereenkomst (DPA) had. Fatima had er nooit een samengesteld.

- **Toegangscontrolebeleid**: Een schriftelijk beleid waarin staat wie binnen PitchCraft AI toegang heeft tot productiegegevens, hoe toegang wordt verleend en ingetrokken, en of least-privilege-principes worden toegepast. Ze had hier niets van op schrift staan.

- **Back-up en disaster recovery**: De vragenlijst vroeg om gedefinieerde Recovery Point- en Recovery Time-doelstellingen, en bewijs dat back-ups daadwerkelijk werden getest door ze te herstellen, niet alleen dat ze werden gemaakt.

- **Geschiedenis van penetratietests**: Een hard "nee" — er was nooit beveiligingstests door een derde partij uitgevoerd.

- **SSO-ondersteuning**: Het IT-beleid van de verzekeraar vereiste dat elke leverancier die medewerkersaccounts raakte, enterprise single sign-on (SAML of OIDC) ondersteunde. PitchCraft AI had alleen inloggen via e-mail en wachtwoord.

Elf ja's van de 40 was geen onvoldoende omdat Fatima met opzet iets onveiligs had gebouwd — het was een onvoldoende omdat Bolt haar een werkend product had opgeleverd, geen bedrijf dat ooit was geauditeerd. Dat zijn verschillende dingen, en enterprise-kopers zijn de eersten die het verschil opmerken.

## Tien werkdagen: de Enterprise Hardening-sprint

Fatima nam nog dezelfde middag contact op met LaunchStudio, met de deadline van de beoordelingscommissie rood omcirkeld. De engineers van LaunchStudio, ondersteund door Manifera, brachten de gap-analyse in kaart aan de hand van de vragenlijst zelf — waarbij elk onbeantwoord item werd behandeld als een werkticket in plaats van uit te gaan van een generieke beveiligingschecklist — en voerden het **Enterprise Hardening**-pakket uit als een gerichte sprint van 10 werkdagen, zonder de bestaande, met Bolt gebouwde frontend van Fatima aan te raken:

1. **Versleuteling geverifieerd en gedocumenteerd**: Het team bevestigde en documenteerde AES-256-versleuteling in rust op de Supabase/Postgres-laag, dwong TLS 1.2+ met HSTS af op elk endpoint, en schreef een samenvatting van één pagina over de versleuteling die Fatima rechtstreeks aan de vragenlijst kon toevoegen — waardoor een vage technische claim veranderde in een specifiek, controleerbaar antwoord.

2. **RLS-gebaseerde tenant-isolatie**: Dit was het middelpunt van de sprint. Engineers implementeerden Row Level Security-beleid gekoppeld aan `auth.uid()` en account-ID op elke tabel met klant-pitchdata, zodat tenant-isolatie werd afgedwongen door de database zelf — niet door applicatiecode die door een bug omzeild zou kunnen worden. De isolatievraag in de vragenlijst veranderde van een ongemakkelijke uitleg in een antwoord van één regel, onderbouwd met beleidscode.

3. **Een gedocumenteerd incident response-plan**: LaunchStudio stelde een formeel IR-plan op voor detectie, interne escalatie, klantmeldingstermijnen afgestemd op de 72-uurs meldplicht voor datalekken van de AVG/GDPR, en een aangewezen verantwoordelijke voor de respons — Fatima zelf, totdat het bedrijf groot genoeg zou zijn voor een toegewijde rol.

4. **Een volledige lijst van subverwerkers**: Het team stelde een lijst samen van elke derde partij in de stack van PitchCraft AI — Supabase, Stripe, de LLM-provider, de transactionele e-maildienst en het hostingplatform — bevestigde dat elk een ondertekende DPA had, en formatteerde de lijst precies zoals enterprise-beveiligingsteams die verwachten te ontvangen.

5. **Een schriftelijk toegangscontrolebeleid**: Een kort, concreet document waarin rolgebaseerde toegang tot productiesystemen wordt beschreven, verplichte offboarding-stappen wanneer een teamlid vertrekt, en least-privilege-standaardinstellingen voor elke nieuwe medewerker of contractor.

6. **Geautomatiseerde, geteste back-ups**: Point-in-time recovery werd ingeschakeld op de database, de back-upfrequentie en bewaartermijn werden gedocumenteerd tegen gedefinieerde RPO/RTO-doelen, en het team voerde een live testherstel uit om te bewijzen dat de back-ups daadwerkelijk werkten — niet alleen dat ze bestonden.

7. **SSO-ondersteuning**: Engineers voegden op SAML gebaseerde single sign-on-ondersteuning toe, zodat medewerkers van de verzekeraar konden inloggen via hun eigen identiteitsprovider, waarmee werd voldaan aan de IT-beleidsvereiste die eerder een harde blokkade vormde.

## Slagen voor de technische beoordeling

Fatima diende de vragenlijst opnieuw in op dag negen, één dag voor de deadline van de beoordelingscommissie. Deze keer waren 37 van de 40 items eerlijke "ja"-antwoorden, elk onderbouwd door een echt document of een echt beleid waar ze naar kon verwijzen. De overige drie — een voltooide penetratietest door een derde partij, SOC 2 Type II-certificering en multi-regio failover — werden openlijk vermeld als items op haar roadmap voor het volgende kwartaal, met streefdata in plaats van vage beloftes.

Die eerlijkheid deed er net zoveel toe als de daadwerkelijke oplossingen. Tijdens het gesprek over de technische beoordeling nam de beveiligingsanalist van de verzekeraar de RLS-beleidsdocumentatie, de lijst van subverwerkers en het incident response-plan regel voor regel door, en accepteerde de drie roadmap-items zonder bezwaar, omdat al het overige in de inzending verifieerbaar en specifiek was in plaats van defensief. Drie weken later werd de pilot goedgekeurd, het contract getekend, en had PitchCraft AI zijn eerste enterprise-klant.

## De les voor AI-oprichters

Het verhaal van Fatima wordt eerder de norm dan de uitzondering. Naarmate meer enterprise-kopers AI-tools van kleine, snel bewegende teams adopteren, hebben hun inkoop- en beveiligingsafdelingen daarop gereageerd door vragenlijsten voor leveranciers langer en technischer te maken, niet korter. Een gepolijste demo, gebouwd in Bolt, Lovable of Cursor, kan de interne voorstander van het bedrijf overtuigen — maar het is de vragenlijst, beoordeeld door mensen die de demo nooit zullen zien, die daadwerkelijk beslist of de deal doorgaat.

De oprichters die deze deals verliezen, zijn niet degenen met slechtere producten. Het zijn degenen die de kloof tussen "het werkt" en "het is aantoonbaar veilig" voor het eerst ontdekken terwijl een klok van 10 werkdagen al loopt. De oprichters die deze deals winnen, zijn degenen die de vragenlijst zelf als specificatie behandelen — en engineers inschakelen die al weten hoe ze deze punt voor punt kunnen beantwoorden, vóór de deadline verstrijkt.

## Belangrijkste inzichten

- Een vendor security questionnaire test gedocumenteerde, aantoonbare beheersmaatregelen — versleuteling, tenant-isolatie, incident response, back-ups, SSO — niet of het product werkt tijdens een demo.

- Row Level Security die wordt afgedwongen in applicatiecode, niet op databaseniveau, voldoet niet aan een enterprise-vraag over tenant-isolatie — beoordelaars willen beleid afgedwongen zien op een plek waar een bug in uw code dit niet kan omzeilen.

- Een volledige lijst van subverwerkers met ondertekende DPA's, een schriftelijk toegangscontrolebeleid en een gedocumenteerd incident response-plan zijn papierwerk dat enterprise-kopers vóór het contract vereisen, geen optionele extra's voor later.

- Het eerlijk melden van hiaten, met een specifieke roadmap en data, slaagt veel vaker voor een technische beoordeling dan vage geruststelling — beoordelaars belonen transparantie boven glans.

- Een gerichte hardening-sprint die direct is afgestemd op de eigen items van de vragenlijst — in plaats van een generieke beveiligingschecklist — is wat een deadline van 10 werkdagen verandert van een bedreiging in een haalbare planning.

## Laat een vragenlijst uw enterprise-deal niet kelderen

Als een enterprise-prospect stil is geworden sinds de inkoopafdeling betrokken raakte, is de vragenlijst in hun inbox daar zeer waarschijnlijk de reden van — en de klok erop loopt korter dan het aanvoelt.

LaunchStudio wordt geëxploiteerd door **Manifera**, een internationaal software-engineeringbedrijf opgericht in 2014 en geleid door Oprichter & Managing Director **Herre Roelevink**. Manifera brengt meer dan 11 jaar ervaring in production engineering naar precies dit soort hiaten, met een staat van dienst bij enterprise-klanten waaronder Vodafone en TNO, onder dezelfde mate van controle die het beveiligingsteam van uw prospect nu op u toepast. Door "Nederlands management te combineren met Vietnamees meesterschap", onderhoudt Manifera hoofdkantoren in **Amsterdam, Nederland** (Herengracht 420), een Aziatische hub in **Singapore** (100 Tras Street) en een primair ontwikkelcentrum in **Ho Chi Minh-stad, Vietnam** (Pho Quang Street). Via LaunchStudio nemen senior engineeringteams uw bestaande door AI gebouwde frontend en implementeren ze productieklare beveiligingscontroles, live betalingsgateways, veilige hosting en monitoring — waardoor uw prototype binnen 1 tot 3 weken verandert in een veilige, compliant MVP, zonder dat een volledige rebuild nodig is. [Vraag vandaag nog een gratis offerte aan](https://launchstudio.eu/en/#contact) of bekijk hoe het [maatwerk software-ontwikkelteam van Manifera](https://www.manifera.com/services/custom-software-development/) production-hardening aanpakt voor AI-gegenereerde codebases.

## Echt voorbeeld

### Een AI-native oprichter in actie: Enterprise sales-enablement SaaS

Fatima Al-Sayed gebruikte **Bolt** om PitchCraft AI te bouwen, een AI-platform voor sales-enablement, in zes weken. Het inkoopteam van een grote enterprise-prospect stuurde een vragenlijst met 40 items over leveranciersbeveiliging, met betrekking tot versleuteling, tenant-isolatie, incident response, subverwerkers, toegangscontrole, back-ups, penetratietests en SSO — en Fatima kon slechts 11 van de 40 items eerlijk met "ja" beantwoorden, met nog 10 werkdagen te gaan voor de interne beoordelingsdeadline van het enterprise-bedrijf.

Fatima werkte samen met **LaunchStudio (door Manifera)** om het hiaat te dichten. De Enterprise Hardening-sprint verifieerde en documenteerde versleuteling in rust en tijdens overdracht, implementeerde RLS-gebaseerde tenant-isolatie op databaseniveau, stelde een formeel incident response-plan op, stelde een volledige lijst van subverwerkers samen met ondertekende DPA's, schreef een toegangscontrolebeleid, activeerde en testte geautomatiseerde back-ups, en voegde op SAML gebaseerde SSO-ondersteuning toe.

**Resultaat:** Fatima ging van 11/40 naar 37/40 eerlijke "ja"-antwoorden, waarbij de overige 3 werden gemeld als roadmap-items die het enterprise-bedrijf accepteerde. Ze slaagde voor de technische beoordeling en sloot de enterprise-deal 3 weken later.

**Kosten & Doorlooptijd:** € 5.400 (Enterprise Hardening Pakket) — 10 werkdagen.

---

---

---

## Veelgestelde Vragen

### Waarom falen AI-builder prototypes zo vaak op enterprise beveiligingsvragenlijsten?

Tools zoals Bolt, Lovable en Cursor zijn geoptimaliseerd om snel werkende functies te bouwen, niet om de beheersmaatregelen te documenteren die enterprise-beveiligingsteams vereisen — beheer van encryptiesleutels, tenant-isolatie op databaseniveau, incident response-plannen, overeenkomsten met subverwerkers en geteste back-ups. Een prototype kan perfect functioneren in een demo en toch nul eerlijke "ja"-antwoorden hebben op het merendeel van een formele vragenlijst, omdat die beheersmaatregelen nooit zijn gebouwd of gedocumenteerd.

### Wat is het verschil tussen tenant-isolatie op applicatieniveau en op databaseniveau?

Isolatie op applicatieniveau vertrouwt op de eigen querylogica van de app om data te filteren op account — bijvoorbeeld door alleen rijen op te halen waarvan het klant-ID overeenkomt. Als er een bug in die logica zit, kan de ene tenant de data van een andere tenant zien. Isolatie op databaseniveau, afgedwongen via Row Level Security-beleid gekoppeld aan de geauthenticeerde gebruiker, weigert niet-geautoriseerde query's al bij de database zelf, zodat geen enkele applicatiebug cross-tenant data kan lekken. Enterprise-beveiligingsbeoordelaars zoeken specifiek naar de tweede vorm.

### Is het oké om "nee" te antwoorden of een hiaat te melden op een beveiligingsvragenlijst?

Ja, en dat is vaak beter dan een vaag of ontwijkend "ja". Enterprise-beoordelaars zijn getraind om opgeblazen antwoorden te herkennen, en een zelfverzekerd, onwaar "ja" dat niet standhoudt bij een technisch vervolggesprek richt meer schade aan dan een eerlijk "nog niet, gepland voor Q4" met een specifiek plan erbij. De technische beoordeling van Fatima slaagde met drie eerlijk gemelde roadmap-items juist omdat al het overige in haar inzending verifieerbaar was.

### Hoe lang duurt het doorgaans om je voor te bereiden op een enterprise beveiligingsbeoordeling?

Voor een oprichter die start vanuit een AI-builder-prototype zonder eerdere beveiligingsdocumentatie, is een gerichte sprint van 10 werkdagen — direct afgestemd op de eigen items van de vragenlijst in plaats van op een generieke checklist — realistisch om het merendeel van de hiaten te dichten, zoals bij Fatima. De exacte omvang hangt af van hoeveel items geheel nieuw infrastructuurwerk vereisen, zoals het toevoegen van SSO of het migreren naar door de database afgedwongen RLS, versus items die alleen het documenteren van reeds bestaande beheersmaatregelen vereisen.

### Wat is de relatie van LaunchStudio met Manifera, en waarom is dat van belang bij enterprise-deals?

LaunchStudio wordt geëxploiteerd door Manifera, een internationaal software-engineeringbedrijf opgericht in 2014 door Herre Roelevink, met meer dan 11 jaar ervaring in production engineering en enterprise-klanten waaronder Vodafone en TNO. Dat is direct van belang voor een verhaal zoals dat van Fatima, omdat dezelfde disciplines die Manifera toepast voor enterprise-klanten — RLS-beleidsontwerp, gedocumenteerde incident response, beheer van subverwerkers en DPA's — precies zijn waar een enterprise-vragenlijst op test, alleen dan afgestemd en geprijsd op de tijdlijn en het budget van een oprichter.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Waarom falen AI-builder prototypes zo vaak op enterprise beveiligingsvragenlijsten?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Tools zoals Bolt, Lovable en Cursor zijn geoptimaliseerd om snel werkende functies te bouwen, niet om de beheersmaatregelen te documenteren die enterprise-beveiligingsteams vereisen — beheer van encryptiesleutels, tenant-isolatie op databaseniveau, incident response-plannen, overeenkomsten met subverwerkers en geteste back-ups. Een prototype kan perfect functioneren in een demo en toch nul eerlijke \"ja\"-antwoorden hebben op het merendeel van een formele vragenlijst, omdat die beheersmaatregelen nooit zijn gebouwd of gedocumenteerd."
      }
    },
    {
      "@type": "Question",
      "name": "Wat is het verschil tussen tenant-isolatie op applicatieniveau en op databaseniveau?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Isolatie op applicatieniveau vertrouwt op de eigen querylogica van de app om data te filteren op account — bijvoorbeeld door alleen rijen op te halen waarvan het klant-ID overeenkomt. Als er een bug in die logica zit, kan de ene tenant de data van een andere tenant zien. Isolatie op databaseniveau, afgedwongen via Row Level Security-beleid gekoppeld aan de geauthenticeerde gebruiker, weigert niet-geautoriseerde query's al bij de database zelf, zodat geen enkele applicatiebug cross-tenant data kan lekken. Enterprise-beveiligingsbeoordelaars zoeken specifiek naar de tweede vorm."
      }
    },
    {
      "@type": "Question",
      "name": "Is het oké om \"nee\" te antwoorden of een hiaat te melden op een beveiligingsvragenlijst?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ja, en dat is vaak beter dan een vaag of ontwijkend \"ja\". Enterprise-beoordelaars zijn getraind om opgeblazen antwoorden te herkennen, en een zelfverzekerd, onwaar \"ja\" dat niet standhoudt bij een technisch vervolggesprek richt meer schade aan dan een eerlijk \"nog niet, gepland voor Q4\" met een specifiek plan erbij. De technische beoordeling van Fatima slaagde met drie eerlijk gemelde roadmap-items juist omdat al het overige in haar inzending verifieerbaar was."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe lang duurt het doorgaans om je voor te bereiden op een enterprise beveiligingsbeoordeling?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Voor een oprichter die start vanuit een AI-builder-prototype zonder eerdere beveiligingsdocumentatie, is een gerichte sprint van 10 werkdagen — direct afgestemd op de eigen items van de vragenlijst in plaats van op een generieke checklist — realistisch om het merendeel van de hiaten te dichten, zoals bij Fatima. De exacte omvang hangt af van hoeveel items geheel nieuw infrastructuurwerk vereisen, zoals het toevoegen van SSO of het migreren naar door de database afgedwongen RLS, versus items die alleen het documenteren van reeds bestaande beheersmaatregelen vereisen."
      }
    },
    {
      "@type": "Question",
      "name": "Wat is de relatie van LaunchStudio met Manifera, en waarom is dat van belang bij enterprise-deals?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "LaunchStudio wordt geëxploiteerd door Manifera, een internationaal software-engineeringbedrijf opgericht in 2014 door Herre Roelevink, met meer dan 11 jaar ervaring in production engineering en enterprise-klanten waaronder Vodafone en TNO. Dat is direct van belang voor een verhaal zoals dat van Fatima, omdat dezelfde disciplines die Manifera toepast voor enterprise-klanten — RLS-beleidsontwerp, gedocumenteerde incident response, beheer van subverwerkers en DPA's — precies zijn waar een enterprise-vragenlijst op test, alleen dan afgestemd en geprijsd op de tijdlijn en het budget van een oprichter."
      }
    }
  ]
}
</script>
