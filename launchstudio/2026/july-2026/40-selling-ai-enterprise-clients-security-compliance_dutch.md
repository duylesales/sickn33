---
Titel: "Verkopen aan Enterprise klanten: Compliance en Security AI"
Trefwoorden: AI And Security, AI Security Risk, AI Security Vulnerabilities, AI Data Security, AI Privacy Issues, AI SaaS Platform, AI Software Engineering
Koperfase: Bewustzijn
---

# Verkopen aan Enterprise klanten: Compliance en Security AI

U heeft een AI-tool gebouwd die complexe juridische contracten in enkele seconden samenvat. Individuele advocaten zijn er dol op en betalen $ 30 per maand. Dus pitcht u het bij een groot advocatenkantoor om een jaarcontract van $ 50.000 binnen te halen. De managing partner is enthousiast over de demo, tekent akkoord, en draagt u vervolgens over aan IT Procurement en de Chief Information Security Officer (CISO). Zes weken nadat de deal binnen leek, sturen zij u een vragenlijst van 40 beveiligingsvragen en willen weten: "Waar gaan de gegevens naartoe?" Als uw antwoord is "We sturen het gewoon naar OpenAI", is de deal dood — niet omdat uw product niet werkt, maar omdat niemand in uw team een vraag kon beantwoorden die vanaf dag één in de architectuur ingebouwd had moeten zijn. Dit is geen zeldzame uitzondering die alleen voor Fortune 500-namen geldt; zelfs middelgrote bedrijven met 200 werknemers voeren tegenwoordig een formele beveiligingsbeoordeling uit voordat zij iets boven de ongeveer € 10.000 per jaar tekenen. Hier leest u hoe u door de enterprise AI-handschoen navigeert — en wint.

## De angst van bedrijven: gegevenslekken

Bedrijven zijn doodsbang voor generatieve AI, en die angst is niet abstract. In 2023 plakten Samsung-medewerkers binnen één maand bij drie afzonderlijke gelegenheden bedrijfseigen halfgeleider-broncode en interne vergadernotities in ChatGPT, waarna het bedrijf publieke AI-tools volledig verbood. De Italiaanse gegevensbeschermingsautoriteit verbood ChatGPT zelfs kortstondig landelijk vanwege AVG-zorgen. Verhalen als deze zijn de reden waarom de belangrijkste richtlijn van elke CISO is om ervoor te zorgen dat vertrouwelijke klantgegevens, financiële gegevens of bedrijfsgeheimen nooit worden opgenomen in de trainingspijplijn van een model van een derde partij, om vervolgens later opnieuw aan een concurrent te worden getoond.

Als u een AI-wrapper bent, bent u een datadoorgeefluik tussen de gevoelige gegevens van de onderneming en een LLM-aanbieder van een derde partij. U moet met documentatie — en niet alleen met een mondelinge belofte — bewijzen dat die leiding is afgedicht. De meeste grote organisaties houden tegenwoordig een interne lijst met "goedgekeurde AI-leveranciers" bij, en tools die daar niet op staan worden op netwerkniveau geblokkeerd via egress-filtering: de bedrijfsfirewall weigert simpelweg uitgaand verkeer naar niet-goedgekeurde API-domeinen. Die filter passeren is een voorwaarde, geen leuke extra.

## Stap 1: Het API-onderscheid

De eerste misvatting die u bij inkoopteams moet wegnemen, is het verschil tussen de consumenten-app ChatGPT en de OpenAI API.

OpenAI stelt expliciet dat gegevens die via de **betaalde API** worden ingediend, niet worden gebruikt om hun modellen te trainen en slechts 30 dagen worden bewaard, uitsluitend voor misbruikmonitoring. De commerciële API-voorwaarden van Anthropic bevatten een gelijkwaardige toezegging voor Claude. U moet dit duidelijk vastleggen in een ondertekende Verwerkersovereenkomst (DPA) — niet alleen een link naar een openbare beleidspagina. Juridische afdelingen van ondernemingen willen een contract, en de meeste SOC 2-bewuste kopers vragen ook om uw volledige lijst van subverwerkers. Als uw stack OpenAI, Pinecone, Twilio en Stripe raakt, zijn dat onder de AVG allemaal subverwerkers die u moet vermelden.

*Pro-tip*: Voor strikte klanten kunt u Zero Data Retention (ZDR) aanvragen bij OpenAI en Anthropic, waardoor zij zelfs de logboeken van 30 dagen voor misbruikmonitoring niet bewaren. Beide aanbieders versleutelen gegevens standaard onderweg (TLS 1.2/1.3) en in rust (AES-256) — ken deze specificaties uit uw hoofd, want een CISO zal ernaar vragen.

## Stap 2: De zelfgehoste "air-gapped"-optie

Voor sectoren als de gezondheidszorg (HIPAA) of defensie zal "We gebruiken de OpenAI API" nooit voldoen aan de eisen, ongeacht het beleid van OpenAI zelf. De gegevens kunnen simpelweg een goedgekeurde netwerkgrens niet verlaten, punt.

Er is een tussenweg die de meeste oprichters te snel overslaan: kijk, voordat u een volledig zelfgehoste stack bouwt, naar Azure OpenAI Service of AWS Bedrock. Beide bieden toegang tot modellen van GPT-4- of Claude-klasse, waarbij de inferentie volledig binnen de eigen cloudomgeving van de klant draait, onder hun bestaande enterprise-overeenkomst, met contractuele garanties dat er niet wordt getraind en met regionale controle over gegevensresidentie (een EU-klant kan inferentie vastzetten op Ierland of Frankfurt). Hiermee behaalt u 80% van de compliance-winst zonder de infrastructuurlast.

Als dat nog steeds niet volstaat — vaak het geval bij defensie, overheid of de strengste zorginstellingen — implementeert u een daadwerkelijk zelfgehost open-source model (Llama 3.1 70B, Mistral Large of Qwen 2.5) op een Virtual Private Cloud (VPC) die volledig aan die klant is toegewezen, geserveerd via een inferentieframework zoals vLLM. Wees eerlijk over de kosten: een toegewijde A100- of H100-GPU-cluster die een model van 70B in productielatentie kan bedienen, kost al snel tienduizenden euro's per maand, tegenover een paar honderd euro aan verbruiksgebaseerde API-kosten. Bouw dit alleen als een getekend enterprise-contract de vaste kosten rechtvaardigt — nooit speculatief.

## Stap 3: Databasebeveiliging (bewijzen dat u niet de zwakke schakel bent)

Zelfs als de API van OpenAI of Anthropic waterdicht is, zal de onderneming *uw* infrastructuur even grondig controleren. Als u een AI-bouwer heeft gebruikt om uw app te genereren en Supabase Row Level Security (RLS) uitgeschakeld heeft gelaten, of een service-role-sleutel in de frontendbundel heeft meegeleverd, faalt u de audit voordat de vergadering is afgelopen.

U moet aantonen — met bewijs dat een beveiligingsbeoordelaar zelfstandig kan verifiëren:

- **Beveiliging op rijniveau**: databasegehandhaafd beleid (Postgres RLS op Supabase, of gelijkwaardig) dat wiskundig bewijst — niet slechts belooft op applicatieniveau — dat Gebruiker A geen rijen van Gebruiker B kan opvragen, zelfs niet met een geconstrueerd verzoek.

- **Encryptie in rust en onderweg**: AES-256 voor opgeslagen gegevens, HTTPS/TLS voor al het verkeer, en — steeds vaker gevraagd door kopers in de financiële en zorgsector — door de klant beheerde encryptiesleutels (CMEK), zodat de onderneming het sleutelmateriaal beheert, niet alleen de leverancier.

- **Op rollen gebaseerde toegangscontrole (RBAC)**: de bedrijfsbeheerder moet kunnen definiëren wie binnen de eigen organisatie welke gegevens ziet, ingedeeld naar afdeling, anciënniteit of dossier — dit is een minimumvereiste voor elke B2B-tool met meerdere gebruikers.

- **Auditregistratie**: een onveranderlijk logboek (opgebouwd met bijvoorbeeld pgAudit of een speciale Supabase-audittrigger-tabel) dat precies registreert wie welk record heeft geopend, geëxporteerd of verwijderd, en wanneer, bewaard zolang het compliance-regime van de klant dat vereist.

Dit is de stap waarop de meeste door AI gegenereerde prototypes stilletjes falen voordat een CISO ze ooit ziet. Onafhankelijke audits tonen consequent aan dat ongeveer 45% van de door AI gegenereerde code minstens één uitbuitbaar beveiligingslek bevat — ontbrekend RLS-beleid, hardgecodeerde API-sleutels en niet-geverifieerde beheerroutes zijn de drie meest voorkomende bevindingen. Dit is een belangrijke reden waarom naar schatting 80% van de met AI gebouwde projecten nooit een stabiele productiestatus bereikt: de demo werkt perfect voor de oprichter die hem alleen test, en valt uiteen zodra een beveiligingsbeoordelaar begint te zoeken naar de gaten die AI-bouwers nooit dichten.

## Stap 4: Nalevingscertificeringen (SOC 2 en ISO 27001)

Uiteindelijk zullen grote ondernemingen een formeel auditrapport eisen. In de VS is dat meestal SOC 2 Type II — een audit door een derde partij die verifieert dat u strikte beveiligingspraktijken volgt (ontwikkelaars raken de productiedatabase niet direct aan, laptops zijn versleuteld, er vinden antecedentenonderzoeken plaats, incidentrespons is gedocumenteerd) over een langere observatieperiode, doorgaans 3 tot 12 maanden, en niet slechts een momentopname zoals het lichtere SOC 2 Type I. Europese zakelijke kopers, met name in Nederland en de bredere EU, vragen vaak om ISO 27001 in plaats van, of naast, SOC 2 — het is de wereldwijd meer erkende standaard buiten de VS en is doorgaans wat EU-inkoopteams als eerste verwachten.

Het behalen van een van beide kost echt tijd en geld — vaak € 10.000 tot € 30.000 met behulp van compliance-automatiseringsplatforms zoals Vanta, Drata of Secureframe, plus de vergoeding van de auditor. Ga hier pas mee aan de slag als een zakelijke klant er actief om vraagt; het is een slechte besteding van de schaarse tijd van een oprichter vóór inkomsten. Maar ontwerp uw app vanaf dag één op een veilige manier — RLS, encryptie, auditlogboeken, toegangscontrole — zodat het behalen van certificering op het juiste moment een documentatie-oefening is bovenop infrastructuur die u al heeft, en geen totale herbouw onder tijdsdruk. Als u midden in een auditcyclus zit wanneer een nieuwe deal zich aandient, kan uw auditor een "bridge letter" afgeven die de periode sinds uw laatste rapport dekt — weet dat dit bestaat, zodat u geen deal verliest door administratieve timing.

## Stap 5: AVG, de EU AI-verordening en gegevensresidentie

Als een van uw zakelijke prospects in de EU is gevestigd — een vrijwel zekerheid als u vanuit Amsterdam, Rotterdam of elders in Nederland bouwt — is SOC 2 alleen niet genoeg om de deal te sluiten. EU-kopers voegen daar AVG Artikel 28-verplichtingen voor verwerkers aan toe (uw DPA heeft specifieke clausules nodig over aansprakelijkheid van subverwerkers en meldingstermijnen bij datalekken), Standaardcontractbepalingen voor elke niet-EU-subverwerker, en steeds vaker eisen onder de EU AI-verordening, die vanaf 2025 en 2026 geleidelijk transparantie- en risicobeheerverplichtingen voor AI-systemen invoert. Een tool die juridische contracten samenvat binnen een gereguleerde sector kan in een hogere risicocategorie vallen dan een generieke chatbot, wat uw documentatielast aanzienlijk verandert.

In de praktijk betekent dit dat zakelijke kopers in de financiële sector, gezondheidszorg en publieke sector in de EU steeds vaker eisen dat inferentie binnen EU/EER-datacenters blijft — zowel OpenAI als Azure bieden inmiddels EU-dataresidentieregio's om precies deze reden. Dit vanaf het begin inbouwen, in plaats van het onder deal-druk achteraf toe te voegen, is aanzienlijk goedkoper. Dit is ook waar een Europese engineeringpartner met EU-ervaring een echt voordeel wordt in plaats van een leuke bijkomstigheid: het is een belangrijke reden waarom Manifera — het moederbedrijf van LaunchStudio, opgericht in **2014** en gevestigd in **Amsterdam, Nederland** (Herengracht 420, 1017 BZ) — een specifieke praktijk heeft opgebouwd rond AVG-bewuste infrastructuur voor klanten zoals Vodafone en TNO, naast de ontwikkelingscentra in Singapore en Ho Chi Minh City.

## Belangrijkste inzichten

- Zakelijke klanten zijn bang dat AI hun bedrijfseigen gegevens opneemt in een model van een derde partij; u moet gegevensisolatie garanderen met documentatie, niet met mondelinge geruststelling.

- Leer inkoopteams dat betaalde API's (OpenAI/Anthropic) niet trainen op klantgegevens — en wees voorbereid om uw volledige lijst van subverwerkers te noemen, want dat is een standaardvraag.

- Bied voor strikte sectoren (gezondheidszorg, financiën, defensie) Azure OpenAI Service of AWS Bedrock als tussenweg aan, voordat u zich vastlegt op een volledig zelfgehost open-source model op een toegewezen VPC.

- Uw eigen infrastructuur moet beveiligingsaudits doorstaan: Supabase RLS, encryptie in rust en onderweg, RBAC en onveranderlijke auditregistratie zijn verplicht, geen optionele extra's.

- Ontwerp vroeg voor beveiliging, zodat SOC 2 of ISO 27001 een documentatie-oefening wordt in plaats van een herbouw — en onthoud dat EU-kopers vaak ook AVG-/EU AI-verordening-afstemming willen, naast een van beide certificeringen.

- Ongeveer 45% van de door AI gegenereerde code bevat uitbuitbare kwetsbaarheden, wat een belangrijke reden is waarom 80% van de met AI gebouwde projecten nooit productie bereikt — dat gat dichten vóór uw eerste zakelijke beveiligingsbeoordeling is het verschil tussen een getekend contract en een dode deal.

## Slaag voor de Enterprise Security Audit

Verlies geen contract van $ 50.000 omdat uw AI-app niet door de beveiligingsbeoordeling is gekomen. LaunchStudio versterkt uw database, implementeert RLS, richt auditregistratie in en bereidt uw infrastructuur voor op SOC 2, ISO 27001 of AVG-conforme zakelijke compliance — doorgaans voor ongeveer 20% van wat een traditioneel ontwikkelingsbureau voor hetzelfde verhardingswerk zou rekenen, en meestal binnen 1 tot 3 weken.

Zoals **Herre Roelevink, oprichter en Managing Director van Manifera**, het verwoordt: "We zien een verschuiving in softwarebehoeften. De uitdaging is niet langer het omzetten van goede ideeën in software. Het gaat nu om de architectuur en beveiliging die nodig zijn om die producten tot volwassenheid te brengen. Wij hebben elf jaar ervaring in precies dat." LaunchStudio wordt beheerd door **Manifera**, een internationaal software-engineeringbedrijf, opgericht in **2014**, met hoofdkantoor in **Amsterdam, Nederland** (Herengracht 420, 1017 BZ) en ontwikkelingscentra in **Singapore** (100 Tras Street #16-01) en **Ho Chi Minh City, Vietnam**. Via LaunchStudio implementeren onze senior engineeringteams uw door AI gebouwde frontend en voegen ze productieklare beveiligingscontroles, live betalingsgateways, veilige hosting en compliance op ondernemingsniveau toe, waardoor uw prototype wordt getransformeerd in een veilige, auditklare MVP. [Bekijk wat uw compliance-verhardingsproject zou kosten](https://launchstudio.eu/en/#calculator), of bekijk [het enterprise-portfolio van Manifera](https://www.manifera.com/portfolio/), opgebouwd voor klanten zoals Vodafone en TNO.

## Echt voorbeeld

### Een AI-native oprichter in actie: CRM SaaS voor de gezondheidszorg

Violet, een startup-oprichter, gebruikte **Lovable** om een CRM SaaS-prototype voor de gezondheidszorg te bouwen. Het product werkte prachtig in demo's — een strakke interface, snelle dossierweergave, een oprecht bruikbare workflow voor patiëntbeheer. Maar toen ze het aan een zakelijke zorgklant voorlegde voor een betaalde pilot, liep de deal vast bij de compliance-beoordeling: er was geen auditspoor dat liet zien wie patiëntendossiers had bekeken of gewijzigd, geen encryptie afgedwongen op databaseniveau boven wat Supabase standaard bood, en geen automatische sessievervaltijd — waardoor een onbeheerde laptop onbeperkt ingelogd bleef, een directe HIPAA-rode vlag voor elk beveiligingsteam in de zorgsector.

Violet werkte samen met **LaunchStudio (door Manifera)** om het product lanceringsklaar te maken. Het technische team bouwde uitgebreide auditregistratie voor elke schrijf- en leesbewerking op de patiëntendossiertabellen, implementeerde end-to-end encryptie voor gegevens in rust en onderweg, en configureerde automatische sessie-time-outs met herauthenticatie na periodes van inactiviteit — precies de drie hiaten die haar zakelijke beoordeling hadden vastgezet.

**Resultaat:** Violet slaagde bij haar volgende inzending voor de bedrijfsveiligheidsaudit en verzekerde zich van een zakelijk jaarcontract ter waarde van € 30.000.

**Kosten en tijdlijn:** € 4.500 (Compliance- en beveiligingspakket) — productieklaar en binnen 15 werkdagen geïmplementeerd.

---

---
## Veelgestelde vragen

### Waarom wijzen zakelijke klanten standaard AI-wrappers af?

Ze zijn bang dat hun bedrijfseigen gegevens naar publieke modellen worden gestuurd en mogelijk worden gebruikt voor training, of blootgesteld raken door zwakke infrastructuur. Als uw app afhankelijk is van standaard-API's zonder een ondertekende Verwerkersovereenkomst, een gedocumenteerde lijst van subverwerkers en verharde databasebeveiliging, schendt dit de meeste bedrijfsbeveiligingsbeleidsregels nog voordat een mens uw product beoordeelt.

### Traint OpenAI op gegevens die via de API worden verzonden?

Nee. Gegevens die naar de betaalde API van OpenAI worden verzonden, worden niet gebruikt voor modeltraining en worden slechts 30 dagen bewaard voor misbruikmonitoring (of nul dagen met een Zero Data Retention-overeenkomst). U moet dit onderscheid duidelijk maken aan inkoopteams, die de API vaak verwarren met het consumentenproduct ChatGPT — en het moet in uw DPA staan, niet alleen mondeling worden gezegd.

### Hoe kan ik een zakelijke klant volledige gegevensprivacy garanderen?

Begin met Azure OpenAI Service of AWS Bedrock, die topmodellen laten draaien binnen de eigen cloudomgeving van de klant, met contractuele garanties dat er niet wordt getraind en met regionale gegevensresidentie. Bied voor de strengste kopers (defensie, sommige zorginstellingen) een volledig zelfgehost open-source model zoals Llama 3.1 of Mistral Large aan op een toegewezen Virtual Private Cloud, hoewel de GPU-infrastructuurkosten pas zinvol zijn zodra een contract dit rechtvaardigt.

### Wat is SOC 2-compliance, en heb ik dit nodig — of moet ik in plaats daarvan ISO 27001 nastreven?

SOC 2 Type II is een overwegend Amerikaanse audit door een derde partij van uw beveiligingspraktijken over een observatieperiode van 3 tot 12 maanden; ISO 27001 is het equivalent waar de meeste zakelijke EU-kopers eerst om vragen. Beide vereisen sterke interne beveiligingscontroles en infrastructuurverharding om te slagen, en beide kosten echte tijd en geld — streef er pas naar zodra een concrete zakelijke deal erom vraagt, maar bouw uw infrastructuur vanaf dag één veilig, zodat de audit een formaliteit is.

### Hoe helpt de relatie tussen LaunchStudio en Manifera mij bij het doorstaan van een zakelijke beveiligingsbeoordeling?

LaunchStudio past dezelfde discipline voor beveiligingsverharding toe die Manifera heeft gebruikt bij meer dan 160 zakelijke projecten — voor klanten zoals Vodafone en TNO — op AI-wrapperprojecten met een vaste scope. Dat telt direct mee in een zakelijk verkoopproces: u kunt een sceptische CISO verwijzen naar een 11 jaar oud, in Amsterdam gevestigd engineeringbedrijf met een echt compliance-trackrecord achter uw app, in plaats van hen te vragen de AI-gegenereerde codebase van een solo-oprichter op goed vertrouwen te accepteren.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Waarom wijzen zakelijke klanten standaard AI-wrappers af?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ze zijn bang dat hun bedrijfseigen gegevens naar publieke modellen worden gestuurd en mogelijk worden gebruikt voor training, of blootgesteld raken door zwakke infrastructuur. Als uw app afhankelijk is van standaard-API's zonder een ondertekende Verwerkersovereenkomst, een gedocumenteerde lijst van subverwerkers en verharde databasebeveiliging, schendt dit de meeste bedrijfsbeveiligingsbeleidsregels nog voordat een mens uw product beoordeelt."
      }
    },
    {
      "@type": "Question",
      "name": "Traint OpenAI op gegevens die via de API worden verzonden?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Nee. Gegevens die naar de betaalde API van OpenAI worden verzonden, worden niet gebruikt voor modeltraining en worden slechts 30 dagen bewaard voor misbruikmonitoring (of nul dagen met een Zero Data Retention-overeenkomst). U moet dit onderscheid duidelijk maken aan inkoopteams, die de API vaak verwarren met het consumentenproduct ChatGPT — en het moet in uw DPA staan, niet alleen mondeling worden gezegd."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe kan ik een zakelijke klant volledige gegevensprivacy garanderen?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Begin met Azure OpenAI Service of AWS Bedrock, die topmodellen laten draaien binnen de eigen cloudomgeving van de klant, met contractuele garanties dat er niet wordt getraind en met regionale gegevensresidentie. Bied voor de strengste kopers (defensie, sommige zorginstellingen) een volledig zelfgehost open-source model zoals Llama 3.1 of Mistral Large aan op een toegewezen Virtual Private Cloud, hoewel de GPU-infrastructuurkosten pas zinvol zijn zodra een contract dit rechtvaardigt."
      }
    },
    {
      "@type": "Question",
      "name": "Wat is SOC 2-compliance, en heb ik dit nodig — of moet ik in plaats daarvan ISO 27001 nastreven?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "SOC 2 Type II is een overwegend Amerikaanse audit door een derde partij van uw beveiligingspraktijken over een observatieperiode van 3 tot 12 maanden; ISO 27001 is het equivalent waar de meeste zakelijke EU-kopers eerst om vragen. Beide vereisen sterke interne beveiligingscontroles en infrastructuurverharding om te slagen, en beide kosten echte tijd en geld — streef er pas naar zodra een concrete zakelijke deal erom vraagt, maar bouw uw infrastructuur vanaf dag één veilig, zodat de audit een formaliteit is."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe helpt de relatie tussen LaunchStudio en Manifera mij bij het doorstaan van een zakelijke beveiligingsbeoordeling?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "LaunchStudio past dezelfde discipline voor beveiligingsverharding toe die Manifera heeft gebruikt bij meer dan 160 zakelijke projecten — voor klanten zoals Vodafone en TNO — op AI-wrapperprojecten met een vaste scope. Dat telt direct mee in een zakelijk verkoopproces: u kunt een sceptische CISO verwijzen naar een 11 jaar oud, in Amsterdam gevestigd engineeringbedrijf met een echt compliance-trackrecord achter uw app, in plaats van hen te vragen de AI-gegenereerde codebase van een solo-oprichter op goed vertrouwen te accepteren."
      }
    }
  ]
}
</script>
