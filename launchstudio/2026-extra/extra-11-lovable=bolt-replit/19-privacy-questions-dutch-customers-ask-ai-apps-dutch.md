---
Titel: "Lovable, Supabase en de AVG: zeven vragen die Nederlandse klanten stellen"
Trefwoorden: lovable supabase, ai app beveiliging, AVG vragenlijst startup, subverwerkerslijst, dataretentie verwijdering, LaunchStudio, Manifera
Koperfase: Beslissing
Doelgroep: AI-Native Oprichter (Niet-Technisch)
---

# Lovable, Supabase en de AVG: zeven vragen die Nederlandse klanten stellen

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Lovable, Supabase en de AVG: zeven vragen die Nederlandse klanten stellen",
  "description": "De vragen die binnenkomen zodra een Nederlands bedrijf, zorginstelling of school jouw met AI gebouwde app evalueert, waarom elke vraag gesteld wordt en hoe je verdedigbare antwoorden voorbereidt vóór de vragenlijst op de mat ploft.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-06-21",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/privacy-questions-dutch-customers-ask-ai-apps" }
}
</script>

De e-mail is vriendelijk geformuleerd en verandert in één klap alles: *"Voordat we kunnen overgaan tot ondertekening, heeft onze Functionaris Gegevensbescherming (FG) een aantal vragen over hoe jullie omgaan met dataopslag en privacy."* Als bijlage zit een document met tussen de zeven en veertig vragen. En ergens rond vraag drie realiseer je je dat jouw app al acht maanden live staat zonder dat iemand ooit heeft gecontroleerd waar de database fysiek eigenlijk draait.

Dit is het moment waarop met AI gebouwde SaaS-producten het vaakst vastlopen — niet tijdens de productdemo, niet op de prijs, maar tijdens de security review van de allereerste serieuze zakelijke klant. Wat volgt zijn de zeven vragen die in vrijwel elke Nederlandse privacyvragenlijst terugkomen, wat er achter de schermen daadwerkelijk wordt getoetst, en hoe je vooraf antwoorden formuleert waar je zakelijk en technisch voor kunt instaan.

*Dit betreft algemene technische en operationele informatie, geen formeel juridisch advies. Sommige onderdelen vereisen uiteindelijk de blik van een privacyjurist; het doel van dit artikel is om dat juridische gesprek zo kort en kostenefficiënt mogelijk te maken.*

## Eén: Waar worden de gegevens opgeslagen?

De privacy officer vraagt om een specifiek land of een datacenterregio, niet om de naam van een softwarebedrijf. *"Supabase"* is géén antwoord; *"Frankfurt (eu-central-1), binnen de Europese Unie"* is dat wel.

De reden dat dit altijd als eerste wordt gevraagd, is dat het voor een auditor het eenvoudigst te controleren is en in de praktijk de meeste onaangename verrassingen oplevert. Lovable-projecten die zijn gekoppeld aan Supabase worden standaard regelmatig aangemaakt in een datacenterregio in de Verenigde Staten, zonder dat de oprichter dat tijdens het prompten in de gaten heeft. Nederlandse zorgpraktijken, scholen, gemeenten en mkb-bedrijven stellen dataopslag binnen de EU vrijwel altijd als keiharde inkoopvoorwaarde, ongeacht of de wet onder strikte voorwaarden doorgifte buiten de EU toestaat. Het maakt hun eigen complianceverhaal richting de toezichthouder simpelweg oneindig veel eenvoudiger.

Controleer de hostingregio van je database vandaag nog. Later migreren vereist een databasemigratie met downtime; de juiste regio kiezen vóór lancering kost één muisklik in een dropdownmenu.

## Twee: Wie heeft er allemaal toegang toe?

Niet: *"is het veilig?"* — maar wie, specifiek en bij naam of rol. Het verwachte antwoord noemt heldere categorieën: de eigen gebruikers van de klant op basis van vooraf gedefinieerde rollen; jouw eigen engineeringteam onder strikt gedocumenteerde beheercondities; en subverwerkers uitsluitend voor hun specifieke technische doel.

De ongemakkelijke vervolgvraag luidt steevast: *"en kan de ene klantorganisatie data van een andere klantorganisatie inzien?"* Voor B2B multi-tenant applicaties is dit de vraag waarop de meeste AI-prototypes genadeloos zakken. Een geloofwaardig antwoord vereist dat je dit daadwerkelijk proefondervindelijk hebt getest: twee afzonderlijke accounts in twee verschillende organisaties, die actief hebben geprobeerd elkaars dossiers te openen via aangepaste API-parameters.

## Drie: Mogen we jullie lijst met subverwerkers inzien?

Een subverwerker (sub-processor) is elke externe partij die namens jou persoonsgegevens verwerkt. Voor een doorsnee met AI gebouwde app is die lijst aanzienlijk langer dan oprichters beseffen: je cloud-databaseprovider, je hostingplatform, je transactionele e-maildienst, je betaalprovider, je foutopsporingstool (error tracking), je analyticsplatform en elke AI-model-API (zoals OpenAI of Anthropic) die jouw app aanroept.

Stel deze lijst proactief op als een overzichtelijke tabel van één A4'tje vóórdat iemand erom vraagt: de naam van de dienst, het specifieke doel, welke persoonsgegevens worden geraakt en in welk land de data fysiek wordt verwerkt. Dit kost je een rustige middag wanneer je zelf de regie hebt, maar ontaardt in pure paniek als een inkoopafdeling je een strakke deadline van vijf werkdagen oplegt.

## Vier: Hebben jullie met elk van hen een verwerkersovereenkomst?

Zodra er klantgegevens in het spel zijn, treed jij op als verwerker voor jouw klant, en zijn jouw externe softwareleveranciers weer subverwerkers voor jou. Die hele keten moet juridisch gedekt zijn door verwerkersovereenkomsten (Data Processing Agreements of DPA's).

De meeste gerenommeerde providers bieden een standaard AVG-conforme DPA aan die je met één klik in hun dashboard accepteert. Het werk zit hem niet in het onderhandelen over contracten — het zit hem in weten wélke je hebt ondertekend, het digitaal archiveren van de kopieën en het kunnen tonen ervan. Oprichters ontdekken tijdens een audit regelmatig dat een handig tooltje dat ze op een vrijdagmiddag aan de code toevoegden al maandenlang persoonsgegevens ontvangt zonder dat er ooit iets getekend is.

## Vijf: Hoe lang bewaren jullie gegevens, en hoe worden ze verwijderd?

Twee wezenlijk verschillende vragen in één:

**Bewaartermijn (dataretentie):** het hebben van een expliciet beleid dat vastlegt na welke termijn inactieve data wordt gewist — en het daadwerkelijk geautomatiseerd wissen ervan. Met AI gebouwde apps wissen uit zichzelf vrijwel nooit data, simpelweg omdat niemand daarom vroeg in de prompt. *"We bewaren data oneindig"* is weliswaar een antwoord, maar een bijzonder slecht antwoord dat direct botst met het AVG-begrip van opslagbeperking.

**Verwijdering (recht op vergetelheid):** wat gebeurt er als een eindgebruiker zijn account wil wissen of wanneer een klant het contract opzegt? Kun je alle data van één specifieke persoon of organisatie uit de database verwijderen zonder dat gerelateerde databasetabellen omvallen door foreign key constraints? Wordt data ook geschoond in je error tracker en e-maillogs?

Het antwoord dat enterprise-klanten willen horen: een gedocumenteerde bewaartermijn per datatype, een werkende verwijderfunctie, en een transparante verklaring over back-ups — namelijk dat verwijderde data in historische back-upmomentopnamen blijft bestaan totdat die back-ups volgens een vast schema automatisch verlopen. Dat is volkomen normaal in de IT-sector en wordt gewaardeerd mits je het eerlijk benoemt.

## Zes: Wat gebeurt er als er een datalek is?

Ze toetsen hiermee of je een incident überhaupt zou opmerken en of je op de hoogte bent van de wettelijke verplichtingen.

Onder de Algemene Verordening Gegevensbescherming (AVG) moet een ernstig datalek in principe zonder onredelijke vertraging, en waar mogelijk binnen 72 uur na ontdekking, worden gemeld aan de Autoriteit Persoonsgegevens (AP). Als verwerker voor jouw zakelijke klant ben jij bovendien contractueel verplicht om *hen* direct te informeren, zodat zij aan hun eigen meldplicht kunnen voldoen.

Het struikelblok voor AI-apps is de zinsnede *"na ontdekking"*. Zonder gestructureerde logging, uptime-monitoring en audittrails heb je simpelweg geen enkel technisch middel om een inbreuk op te merken, laat staan om een klant te vertellen welke records zijn ingezien. Kunnen aantonen dat je toegang tot gevoelige tabellen logt en die logs bewaart, verandert een angstaanjagende auditvraag in een geruststellend, professioneel antwoord.

## Zeven: Kunnen we onze data exporteren?

Data-export in een gangbaar, machineleesbaar formaat (zoals JSON of CSV), op elk moment en gegarandeerd bij beëindiging van de overeenkomst. Dit is deels een wettelijk recht (dataportabiliteit), maar vooral een commerciële eis: geen enkele serieuze organisatie accepteert een vendor lock-in waarbij ze hun eigen bedrijfsdata niet meer kunnen meenemen als ze besluiten over te stappen.

Voor de meeste SaaS-applicaties betekent dit het bouwen van een eenvoudige, betrouwbare exportfunctie voor alle organisatiedata. Het bouwen ervan kost een senior engineer een dag werk. Klanten moeten vertellen dat je het niet kunt, kost je de deal.

## Bereid de antwoorden voor vóór de vragenlijst arriveert

Stel één centraal document op — twee pagina's is meer dan voldoende — met daarin: de hostingregio en provider; het autorisatiemodel in heldere taal; de complete subverwerkerslijst; de bewaarplek van alle getekende DPA's; de bewaartermijnen per datatype; de procedure voor dataverwijdering; de inrichting van monitoring en logging; het datalek-escalatieprotocol inclusief contactpersonen; en de werking van de data-export.

Houd dit document up-to-date. Voeg het direct toe als bijlage bij je commerciële voorstel, nog vóór de klant erom vraagt. Oprichters die dit doen merken steevast dat security-audits niet langer weken duren, maar binnen enkele dagen zijn afgerond. De rol van de privacy officer verandert immers van een streng verhoor in een snelle verificatie.

## Wat je écht niet zelf moet doen

Het formeel bepalen of je in een specifieke gegevensstroom verwerkingsverantwoordelijke of verwerker bent, het juridisch dichttimmeren van je algemene voorwaarden en verwerkersovereenkomst voor klanten, en het beoordelen van internationale doorgiftemechanismen horen thuis bij een gespecialiseerde privacyjurist. De fout die veel startups maken is niet dat ze een jurist inschakelen, maar dat ze dat doen vóórdat de technische feiten helder zijn. Dat maakt zo'n juridisch adviestraject onnodig abstract, tijdrovend en kostbaar.

Zorg dat de technische architectuur eerst 100% klopt. Dan is het juridische gesprek binnen een uur klaar.

## Bouwen aan antwoorden waar je voor kunt instaan

Vrijwel alle zeven vragen betreffen software engineering met een compliance-jasje: een datacenterregio bewust configureren, Row Level Security testen en afdwingen, logging en monitoring inrichten, automatische retentie en verwijdering implementeren, data-export bouwen en externe koppelingen inventariseren. LaunchStudio richt exact dit fundament in als onderdeel van het productierijp maken van met AI gebouwde software — zonder de gebruikersinterface die je in Lovable hebt ontworpen aan te tasten. We leveren de benodigde documentatie kant-en-klaar op, waardoor een security-questionnaire verandert in een formele formaliteit.

Hierachter staat Manifera: elf jaar ervaring in enterprise software engineering voor gerenommeerde partijen als Vodafone, TNO en CFLW, vanuit Amsterdam en Ho Chi Minhstad. Bekijk wat het [Launch Ready pakket](https://launchstudio.eu/nl/#packages) inhoudt, of [omschrijf je project](https://launchstudio.eu/nl/#contact) voor een heldere statusbeoordeling binnen één werkdag.

## Als het eerlijke antwoord ongemakkelijk is

Op enig moment in een security-questionnaire stuit je op een vraag waar het eerlijke antwoord luidt: *"dat hebben we momenteel niet ingericht"*. Veel oprichters schieten op dat moment in de verdediging en grijpen naar wollige, vage bewoordingen. Dat is de slechtst denkbare strategie.

Privacy officers beoordelen zulke formulieren dagelijks. Ze prikken onmiddellijk door ontwijkende antwoorden heen. Wolligheid wordt direct geïnterpreteerd als incompetentie of het verdoezelen van risico's — en beide maken direct een einde aan het inkoopproces.

De formulering die wél werkt bestaat uit drie concrete elementen: wat de huidige situatie is, wat je eraan doet, en wanneer het gereed is. *"Wij loggen op dit moment nog geen leesacties op individuele patiëntendossiers. Deze logging wordt deze maand geïmplementeerd en kunnen we voorafgaand aan de definitieve livegang demonstreren."* Dat is een professioneel antwoord waar een auditor mee kan werken. In de praktijk leidt dit vrijwel altijd tot een akkoord onder voorbehoud in plaats van een harde afwijzing.

Twee factoren maken dit geloofwaardig: een keiharde streefdatum (wat aantoont dat je over de implementatie hebt nagedacht), en consistentie (dezelfde tekortkoming op exact dezelfde transparante manier uitleggen aan elke prospect). Het enige wat je te allen tijde moet vermijden, is beweren dat je een beveiligingsmaatregel hebt die in werkelijkheid ontbreekt. Een auditor die daar tijdens een steekproef achter komt, zal jouw product nooit meer vertrouwen.

## Bewaar de compliance-set op een vaste plek

Een praktische tip die veel frustratie voorkomt: het document van twee pagina's zwerft bij veel oprichters rond in een downloadmap, zes maanden verouderd, in een versie die niemand meer kan vinden zodra de volgende klant erom vraagt.

Bewaar dit document in een centrale teammap, voorzien van een versienummer, datum en een beknopt wijzigingslogboek. Werk het direct bij zodra je een nieuwe externe API koppelt — wat in een workflow met AI-tools vaker gebeurt dan je denkt — of wanneer er iets verandert in je hostinginfrastructuur.

Voeg het document standaard toe aan elke serieuze offerte. Het wekt direct de indruk van een volwassen enterprise-leverancier en voorkomt dat inkooptrajecten maandenlang blijven hangen op bureaucratische formulieren.

## Echt voorbeeld

### Een planningstool die zakte voor een audit en zes weken later slaagde

Tessa Blom bouwde Planbaar in Lovable: een planningsapplicatie voor thuiszorgroutes, gebruikt door zelfstandige zorgverleners en kleine zorgorganisaties rond Deventer. Twee kleine zorgteams gebruikten het naar volle tevredenheid. Een derde, grotere zorgorganisatie toonde serieuze interesse, maar stuurde vóór ondertekening een privacyvragenlijst met negentien vragen.

Planbaar faalde op vijf van de zeven kernpunten: het Supabase-project draaide op een Amerikaanse serverregio; er was geen subverwerkerslijst; tijdens de audit bleek dat vertrouwelijke cliëntnotities per ongeluk werden doorgestuurd naar een buitenlandse marketing-e-mailtool en een crash-reporter zonder DPA; er werd nooit data gewist; er was geen logging van wie welke notities las; en er bestond geen mogelijkheid om cliëntdata gestructureerd te exporteren.

Twaalf werkdagen waren nodig voor de sanering: migratie van de complete database naar een gecertificeerd EU-datacenter met een geverifieerde restore-test; de marketingtool volledig losgekoppeld van gevoelige patiëntdata en vervangen door een AVG-conforme transactionele provider; crash-reporting zo geconfigureerd dat persoonsgegevens automatisch worden geanonimiseerd vóór verzending; automatische bewaartermijnen en verwijderfuncties ingericht; read-access logging toegevoegd aan medische dossiers; een complete organisatie-exportfunctie gerealiseerd; en het complete twee-pagina's tellende compliance-pakket opgesteld.

**Resultaat:** Planbaar doorstond de herbeoordeling zes weken later glansrijk en stuurt het privacy-dossier nu standaard mee met elke offerte. De twee bestaande zorgteams ontvingen het document eveneens — waarna een van hen direct besloot te upgraden naar een groter jaarcontract.

> *"Ik dacht telkens dat privacy vooral een juridisch document was dat ik moest laten opstellen. Het bleek te gaan om zes concrete technische dingen die mijn app simpelweg niet deed."*
> — **Tessa Blom, Oprichter, Planbaar (Deventer)**

**Kosten & Doorlooptijd:** € 4.200 (Launch Ready Pakket: datamigratie naar EU-regio, opschonen datastromen, retentie en verwijdering, audit logging, exporttool) — opgeleverd in 12 werkdagen.

## Veelgestelde vragen

### Moet ik dit allemaal al geregeld hebben vóór mijn allereerste klant?

Vóór je eerste *zakelijke* klant (B2B) vrijwel zeker wel, omdat hun inkoopafdeling er direct naar zal vragen. Voor consumentenproducten (B2C) komen deze formele vragenlijsten minder snel op tafel, maar gelden inhoudelijk exact dezelfde wettelijke eisen. Het werk vooraf doen voorkomt acute paniek achteraf.

### Is hosting binnen de EU wettelijk verplicht voor Nederlandse klanten?

Niet automatisch — doorgifte van persoonsgegevens naar landen buiten de EU is juridisch mogelijk mits er passende waarborgen zijn (zoals het EU-US Data Privacy Framework). In de praktijk eisen veel Nederlandse bedrijven, zorginstellingen en overheden EU-hosting echter contractueel, omdat het hun eigen administratieve verantwoording aanzienlijk vereenvoudigt. De commerciële eis is daardoor vaak strenger dan de strikt wettelijke.

### Wat telt precies als een subverwerker?

Elke externe softwareleverancier die in jouw opdracht persoonsgegevens van jouw gebruikers verwerkt: hostingbedrijven, databases, e-maildiensten, betaalproviders, error monitoring tools, websitestatistieken en API's van AI-taalmodellen. Zodra er gebruikersdata doorheen stroomt, hoort de dienst op je subverwerkerslijst te staan.

### Hoe ga ik om met dataverwijdering als data ook in back-ups zit?

Door hier volkomen transparant over te zijn: verwijderde gegevens worden direct en permanent gewist uit de actieve productiedatabase, maar blijven aanwezig in historische back-ups totdat die back-ups volgens een vast retentieschema automatisch worden overschreven. Dit is de geaccepteerde industriestandaard; beweren dat data binnen één seconde uit alle back-ups verdwijnt is technisch ongeloofwaardig.

### Wie stelt de verwerkersovereenkomst (DPA) met mijn klanten op?

Een gespecialiseerde jurist, op basis van de technische feiten die jij aanlevert. Door vooraf je hostingregio, autorisatiemodel, subverwerkerslijst en bewaartermijnen helder op een rij te hebben, maak je van dat juridische traject een korte, betaalbare formaliteit in plaats van een eindeloze discussie.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Moet ik dit allemaal al geregeld hebben vóór mijn allereerste klant?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Voor je eerste zakelijke B2B-klant vrijwel zeker wel, omdat inkoopafdelingen ernaar vragen. Voor B2C komen vragen later, maar gelden dezelfde wettelijke verplichtingen."
      }
    },
    {
      "@type": "Question",
      "name": "Is hosting binnen de EU wettelijk verplicht voor Nederlandse klanten?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Niet strikt wettelijk mits passende waarborgen gelden, maar veel Nederlandse organisaties eisen het contractueel om hun eigen compliance eenvoudig te houden."
      }
    },
    {
      "@type": "Question",
      "name": "Wat telt precies als een subverwerker?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Elke externe dienst die persoonsgegevens verwerkt namens jou: hosting, database, e-mail, betaalproviders, crash-reporters, analytics en AI-model-API's."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe ga ik om met dataverwijdering als data ook in back-ups zit?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Wees transparant: direct gewist uit actieve databases, en aanwezig in back-ups totdat deze volgens schema automatisch verlopen. Dat is de erkende industriestandaard."
      }
    },
    {
      "@type": "Question",
      "name": "Wie stelt de verwerkersovereenkomst (DPA) met mijn klanten op?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Een jurist, gebaseerd op technische feiten die jij aanlevert. Vooraf heldere feiten over regio, rollen en subverwerkers hebben houdt dat traject kort en betaalbaar."
      }
    }
  ]
}
</script>
