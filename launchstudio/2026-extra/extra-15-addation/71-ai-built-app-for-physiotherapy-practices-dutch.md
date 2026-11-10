---
Titel: "Een Door AI Gebouwde App voor Fysiotherapiepraktijken naar Productie Brengen"
Trefwoorden: fysiotherapie app laten bouwen, zorg app avg supabase, medische data beveiliging saas, oefenprogramma app fysiotherapeut, LaunchStudio, Manifera
Koperfase: Overweging
Doelgroep: AI-Native Oprichter (Niet-Technisch)
---

# Een Door AI Gebouwde App voor Fysiotherapiepraktijken naar Productie Brengen

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Een Door AI Gebouwde App voor Fysiotherapiepraktijken naar Productie Brengen",
  "description": "Fysiotherapeuten en zorgondernemers bouwen met behulp van AI-tools steeds vaker eigen applicaties voor oefenschema's, voortgangsregistratie en patiëntencommunicatie. Deze gids legt uit wat er technisch en juridisch vereist is om een prototype om te vormen tot een veilige productie-app: strikte praktijkscheiding, autorisatie op basis van de behandelrelatie, omgaan met bijzondere persoonsgegevens onder de AVG en WGBO, verplichte MFA, auditlogging, private opslag en betrouwbare back-ups.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-06-27",
  "inLanguage": "nl-NL",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/ai-built-app-for-physiotherapy-practices" },
  "citation": [
    { "@type": "CreativeWork", "name": "Autoriteit Persoonsgegevens: Gegevens over gezondheid", "url": "https://www.autoriteitpersoonsgegevens.nl/themas/gezondheid/medische-gegevens" },
    { "@type": "CreativeWork", "name": "NEN 7510 Informatiebeveiliging in de zorg", "url": "https://www.nen.nl/nen-7510-1-2017-nl" },
    { "@type": "CreativeWork", "name": "Rijksoverheid: Wet op de geneeskundige behandelingsovereenkomst (WGBO)", "url": "https://www.rijksoverheid.nl/onderwerpen/patientenrecht/wet-op-de-geneeskundige-behandelingsovereenkomst-wgbo" },
    { "@type": "CreativeWork", "name": "Supabase: Row Level Security", "url": "https://supabase.com/docs/guides/database/postgres/row-level-security" }
  ]
}
</script>

Fysiotherapeuten en zorgondernemers lopen in hun dagelijkse praktijk voortdurend tegen dezelfde beperkingen aan: traditionele EPD-software (elektronische patiëntendossiers) is vaak log, duur en weinig gebruiksvriendelijk voor patiënten. Steeds meer praktijkhouders grijpen daarom naar moderne AI-builders zoals Lovable, Bolt of v0 om zelf een oplossing te ontwerpen. Binnen enkele avonden staat er een prachtig werkend prototype: therapeuten stellen persoonlijke huiswerkoefeningen samen uit een videobibliotheek, patiënten bekijken instructies op hun smartphone en registreren dagelijks hun pijnscores en herstelprogressie.

In de eigen vertrouwde praktijk werkt dit vaak geweldig. Maar zodra collega-praktijken of een regionale zorggroep interesse tonen om het platform over te nemen, verandert de spelregelkaart drastisch. Wat begon als een handig hulpmiddel, valt nu onder de strenge wet- en regelgeving voor medische gegevensverwerking: de AVG (bijzondere categorieën van persoonsgegevens), de WGBO (bewaarplicht van 20 jaar) en normenkaders zoals NEN 7510.

Deze gids legt uit welke technische waarborgen onmisbaar zijn om een met AI gebouwde fysiotherapie-app gereed te maken voor brede, professionele ingebruikname door zorgverleners.

## Belangrijkste Inzichten

- **Oefenschema's, pijnscores en herstelmetingen zijn gezondheidsgegevens** onder de AVG; behandel deze altijd als bijzondere persoonsgegevens met de hoogste beveiligingsnormen.
- **Autorisatie moet gebaseerd zijn op de behandelrelatie:** een fysiotherapeut mag uitsluitend patiënten inzien die actief bij hem of haar onder behandeling zijn, met een gelogde regeling voor waarneming.
- **Twee-factor-authenticatie (MFA) is verplicht** voor alle zorgverleners en praktijkmedewerkers.
- **Richt een onveranderbaar auditlog in:** elke inzage, wijziging en export van patiëntgegevens moet onweerlegbaar en traceerbaar worden gelogd.
- **Houd rekening met de medische bewaarplicht:** het verwijderen van een patiëntaccount in de app mag de wettelijke bewaarplicht van het behandeldossier (20 jaar conform WGBO) niet schenden.

## Waarom Gezondheidsdata een Andere Aanpak Vereist

In een standaard B2B SaaS-applicatie volstaat het scheiden van data per organisatie. In de zorgsector ligt de lat wezenlijk hoger:

1. **Bijzondere persoonsgegevens (AVG art. 9):** gegevens over fysieke klachten, blessures, behandelhistorie en medische notities mogen niet zomaar worden verwerkt zonder expliciete wettelijke grondslag of uitdrukkelijke toestemming.
2. **Beroepsgeheim en behandelrelatie:** therapeuten binnen een grote maatschap of gezondheidscentrum mogen elkaars patiëntendossiers niet zomaar openen, tenzij er sprake is van collegiale waarneming of multidisciplinaire behandeling.
3. **Patiëntenrechten:** patiënten hebben recht op inzage, correctie en een digitaal afschrift van hun dossier, maar het 'recht op vergetelheid' stuit op de wettelijke bewaarplicht van de behandelaar.

## Essentiële Architectuuraanpassingen voor Zorg-Apps

### 1. Autorisatie op Basis van Behandelrelaties (RLS)

In door AI gegenereerde code hebben therapeuten vaak ongehinderd toegang tot alle records binnen een praktijk. Richt de database-policies (zoals Supabase RLS) opnieuw in op basis van expliciete behandelkoppelingen:

- **Praktijkscheiding:** strikte scheiding op het hoogste niveau (`practice_id`).
- **Primaire behandelaar:** een therapeut ziet standaard alleen patiënten waaraan hij gekoppeld is via een actieve behandelrelatie (`treatment_relationship`).
- **Waarnemingsmechanisme:** bij ziekte of vakantie kan een collega tijdelijk de status van waarnemer krijgen. Elke inzage door een waarnemer wordt voorzien van een specifieke auditmarkering.
- **Praktijkmanagers:** hebben uitsluitend toegang tot administratieve data (planning, facturatie, licenties), nooit tot inhoudelijke medische notities of oefenresultaten.

### 2. Verplichte Twee-Factor-Authenticatie (MFA)

Eenvoudige wachtwoorden zijn ontoereikend voor toegang tot patiëntgegevens. Dwing Time-based One-Time Passwords (TOTP via apps zoals Google Authenticator) verplicht af voor elk praktijkaccount. Blokkeer toegang tot patiëntendossiers zolang MFA niet succesvol is geactiveerd.

### 3. Onveranderbare Auditlogging

Bij elk tuchtrechtelijk geschil, incident of periodieke audit moet de praktijkhouder kunnen aantonen wie wanneer welk dossier heeft geopend. Log automatisch in een append-only databasetabel:
- Tijdstempel (UTC)
- Gebruikers-ID en rol van de behandelaar
- Patiënt-ID
- Type actie (`VIEW`, `EDIT`, `EXPORT`, `ASSIGN_EXERCISE`)
- IP-adres en sessiekenmerken

Deze tabel mag door niemand - ook niet door de praktijkeigenaar - kunnen worden aangepast of gewist.

### 4. Veilige Bestandsopslag voor Media

Patiënten uploaden regelmatig foto's van zwellingen, littekens of video's van hun bewegingspatroon ter beoordeling door de fysiotherapeut. 
- Bewaar deze bestanden **nooit in een publieke storage-bucket**.
- Verhuis media naar een strikt private bucket.
- Verwijder EXIF-metadata (zoals GPS-locaties) bij het uploaden.
- Serveer bestanden uitsluitend via kortlevende, cryptografisch ondertekende URL's (signed URL's met een geldigheid van maximaal 10 tot 15 minuten).

### 5. Strikte Scheiding Tussen Staging en Productie

AI-builders kopiëren soms argeloos productiedata naar een test- of stagingomgeving om nieuwe features uit te proberen. In de zorg is dit een ernstig datalek. Gebruik in test- en demonstratieomgevingen uitsluitend **synthetische patiëntdata** met gefingeerde namen en klachten.

## Verwerkersovereenkomsten en Hosting binnen de EU

Wanneer een andere praktijk uw software afneemt, wordt die praktijk de 'Verwerkingsverantwoordelijke' en uw SaaS-bedrijf de 'Verwerker'. U bent wettelijk verplicht om een sluitende Verwerkersovereenkomst (DPA) aan te bieden. Zorg dat:
- Alle data (inclusief backups) fysiek binnen de Europese Economische Ruimte (bijv. AWS of Supabase datacenters in Frankfurt) wordt gehost.
- U een actuele lijst met subverwerkers (zoals e-mail- of sms-diensten) beschikbaar heeft.
- Er een getest protocol is voor het melden van datalekken binnen 72 uur.

## Hoe LaunchStudio Helpt

LaunchStudio transformeert met AI gebouwde gezondheidsapps naar betrouwbare, enterprise-ready platforms: het herontwerpen van het autorisatiemodel op basis van behandelrelaties via Row Level Security, implementatie van verplichte MFA en tamper-proof auditlogging, het beveiligen van medische media-opslag, inrichten van AVG-conforme EU-cloudinfrastructuur met point-in-time recovery, en het opstellen van de benodigde documentatie voor verwerkersovereenkomsten.

Deze trajecten vallen doorgaans binnen ons **Launch & Grow** pakket (€2.500 - €7.500 plus €49 per maand), inclusief managed hosting, 24/7 monitoring en prioriteitssupport. Bereken uw investering direct met onze [prijscalculator](https://launchstudio.eu/nl/#calculator).

LaunchStudio is onderdeel van Manifera, een softwareontwikkelingsbedrijf met 11+ jaar ervaring, 160+ succesvolle projecten en 120+ gespecialiseerde engineers. De cybersecurity-achtergrond van CEO Herre Roelevink waarborgt dat uw zorgapplicatie voldoet aan de strengste security-audits. Oprichters ontmoeten ons team aan de Herengracht 420 in Amsterdam; de software-engineering vindt plaats in ons ontwikkelcentrum aan de Pho Quang Street in Ho Chi Minh City en onze hub aan Tras Street in Singapore.

## Praktijkvoorbeeld

### Een AI-Native Oprichter in Actie: De Oefenapp Die een Keten van 14 Praktijken Wilde Uitrollen

Wouter Smit, fysiotherapeut met twee succesvolle praktijken in de regio Utrecht, bouwde Oefenmaatje met Lovable en Supabase: een intuïtieve app waarin therapeuten huiswerkprogramma's samenstellen en patiënten dagelijks hun oefeningen en pijnscores bijhouden. Na een jaar intensief gebruik in zijn eigen praktijken toonde een regionale keten van veertien fysiotherapiepraktijken concrete interesse om het systeem praktijkbreed in te voeren.

De kwaliteitsfunctionaris van de keten legde echter een strikte lijst met compliance-eisen op tafel waar het prototype geenszins aan voldeed. Alle therapeuten binnen Wouters account konden elkaars patiënten inzien. Oefenvideo's en door patiënten geüploade foto's stonden in een openbare Supabase-bucket met voorspelbare bestandsnamen. Er was geen auditlog aanwezig, MFA ontbrak, en een officiële verwerkersovereenkomst was nooit opgesteld. Wanneer een patiënt zijn account in de app verwijderde, werd het complete behandelverloop gewist - wat in strijd was met de wettelijke bewaarplicht van het EPD. Tot overmaat van ramp bleek de staging-omgeving een ongeanonimiseerde kopie van echte patiëntendata te bevatten.

LaunchStudio bracht het platform op professioneel medisch niveau. Gegevens werden strikt gescheiden per praktijk en therapeuten werden via RLS beperkt tot uitsluitend hun eigen actieve patiënten, aangevuld met een gelogde waarnemingsfunctie. Twee-factor-authenticatie (MFA) werd verplicht gesteld voor alle medewerkers. Elke inzage en export van patiëntgegevens werd vastgelegd in een onveranderbaar auditlog. Media werd gemigreerd naar private storage met kortlevende signed URL's. De accountverwijderingsflow werd herzien: patiënten kunnen hun app-toegang stopzetten, terwijl klinische behandeldata conform de wettelijke bewaartermijn bewaard blijft voor de praktijk. Echte data werd direct uit staging verwijderd en vervangen door synthetische testprofielen, de hosting werd verankerd in Frankfurt met geteste point-in-time recovery, en engineers stelden een compleet beveiligingsdossier op voor de verwerkersovereenkomst van de praktijkketen.

**Resultaat:** De kwaliteitscommissie van de keten keurde Oefenmaatje binnen vier weken goed. De software werd succesvol uitgerold over alle veertien praktijken, met meer dan 4.000 actieve patiënten binnen zes maanden. Wouter startte kort daarna verkennende gesprekken voor een formele koppeling met landelijke EPD-leveranciers.

> *"Ik had de app gebouwd als enthousiaste fysiotherapeut. Om hem geschikt te maken voor andere praktijken, moest ik leren denken als de hoeder van andermans medische patiëntendossiers."*
> - **Wouter Smit, Oprichter, Oefenmaatje (Utrecht)**

**Kosten & Doorlooptijd:** €6.700 (Launch & Grow pakket: autorisatie op behandelrelaties, verplichte MFA, auditlogging, private storage, bewaartermijn-architectuur, EU-hosting en DPA-documentatie) - afgerond in 17 werkdagen.

## Veelgestelde Vragen

### Kan ik een professionele fysiotherapie-app bouwen met behulp van Lovable of Bolt?

Jazeker, AI-builders zijn buitengewoon effectief om de gebruikersinterface en logische workflows razendsnel op te zetten. Echter, voordat u echte patiënten buiten een kleinschalige pilot toelaat, dient u de backendfundamenten professioneel in te richten: autorisatie op basis van behandelrelaties, verplichte MFA, auditlogging, private mediaopslag, Europese hosting en formele verwerkersovereenkomsten.

### Vallen oefenschema's en pijnscores juridisch onder gezondheidsgegevens?

Ja, zonder uitzondering. Oefeningen die worden voorgeschreven voor specifieke fysieke klachten, geregistreerde pijnscores en mobiliteitsmetingen geven direct inzicht in de gezondheidstoestand van een persoon. Onder de AVG kwalificeert dit als een bijzondere categorie van persoonsgegevens, wat strenge organisatorische en technische beveiligingsmaatregelen vereist.

### Wat gebeurt er met de data wanneer een aangesloten praktijk stopt met mijn SaaS?

De fysiotherapiepraktijk blijft te allen tijde wettelijk verantwoordelijk voor het patiëntendossier en de bijbehorende bewaartermijn. Bied een volledige en gestructureerde data-export aan in een open formaat, spreek een duidelijke overgangsperiode af, en vernietig de gegevens na formele bevestiging conform de afspraken in de verwerkersovereenkomst.

### Hoe helpt de ervaring van Manifera bij het bouwen van gezondheidszorg-apps?

Manifera ontwikkelt al ruim 11 jaar software onder strenge beveiligings- en compliance-eisen, en de CEO heeft een achtergrond in cybersecurity. LaunchStudio benut deze expertise om zorgapplicaties direct te voorzien van de juiste autorisatie, auditlogging en privacywaarborgen waar professionele inkopers en toezichthouders op toetsen.

### Helpt een beveiligde en goed gedocumenteerde app bij het werven van nieuwe praktijken?

Absoluut. Praktijkhouders en zorggroepen zijn uiterst huiverig voor datalekken en aansprakelijkheid. Heldere, transparante informatie op uw website over NEN 7510-principes, AVG-naleving, datalocatie en beveiliging geeft de doorslag in inkooptrajecten en zorgt voor uitstekende aanbevelingen in AI-zoekmachines.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Kan ik een professionele fysiotherapie-app bouwen met behulp van Lovable of Bolt?",
      "acceptedAnswer": { "@type": "Answer", "text": "Ja; richt vóór bredere uitrol wel strikte praktijkscheiding, RLS op behandelrelaties, MFA, auditlogging, private storage en EU-hosting in." }
    },
    {
      "@type": "Question",
      "name": "Vallen oefenschema's en pijnscores juridisch onder gezondheidsgegevens?",
      "acceptedAnswer": { "@type": "Answer", "text": "Ja; oefeningen voor klachten en pijnscores zijn bijzondere persoonsgegevens onder de AVG met strenge wettelijke beveiligingseisen." }
    },
    {
      "@type": "Question",
      "name": "Wat gebeurt er met de data wanneer een aangesloten praktijk stopt met mijn SaaS?",
      "acceptedAnswer": { "@type": "Answer", "text": "Bied een volledige export aan, hanteer een overgangsperiode en wis gegevens na bevestiging conform de verwerkersovereenkomst." }
    },
    {
      "@type": "Question",
      "name": "Hoe helpt de ervaring van Manifera bij het bouwen van gezondheidszorg-apps?",
      "acceptedAnswer": { "@type": "Answer", "text": "Manifera bouwt al 11+ jaar software onder strikte security-eisen en LaunchStudio implementeert de vereiste autorisaties, logging en databescherming." }
    },
    {
      "@type": "Question",
      "name": "Helpt een beveiligde en goed gedocumenteerde app bij het werven van nieuwe praktijken?",
      "acceptedAnswer": { "@type": "Answer", "text": "Ja; transparante informatie over AVG-naleving, medische bewaartermijnen en security stelt praktijkhouders gerust en versnelt de adoptie." }
    }
  ]
}
</script>
