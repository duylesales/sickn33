---
Titel: "Van AI-Prototype naar Productie in Leuven: Universitaire Spin-Offs en Onderzoeksdata"
Trefwoorden: ai-prototype naar productie, leuven spin-off, beveiliging onderzoeksdata, universitaire startup belgie, cursor, LaunchStudio, Manifera
Koperfase: Overweging
Doelgroep: Technische Solo-oprichters / Indie Hackers
---

# Van AI-Prototype naar Productie in Leuven: Universitaire Spin-Offs en Onderzoeksdata

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Van AI-Prototype naar Productie in Leuven: Universitaire Spin-Offs en Onderzoeksdata",
  "description": "Leuvense spin-offs beginnen vaak als interne onderzoekstools die snel met AI zijn gebouwd. Dit artikel behandelt wat er verandert wanneer een academisch AI-prototype naar productie gaat voor betalende klanten: onderzoeksdata-overeenkomsten, institutioneel IE, multi-institutionele toegang, reproduceerbaarheid en EU-hosting.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-12-03",
  "inLanguage": "nl-NL",
  "contentLocation": { "@type": "Place", "name": "Leuven, België" },
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/ai-prototype-to-production-in-leuven-university-spin-offs-and-research-data" }
}
</script>

Leuven is een van de dichtste spin-off-ecosystemen van Europa. Onderzoeksgroepen maken van labtools bedrijven, en steeds vaker beginnen die tools als iets wat een promovendus in Cursor bouwde om zijn groep tijd te besparen: een datapijplijn met een dashboard, een systeem voor het reserveren van apparatuur, een annotatietool. Het werkt voor het lab. Dan willen andere labs het ook, wordt er een spin-off opgericht, en betekent dat AI-prototype naar productie brengen voldoen aan verwachtingen waar geen interne tool ooit mee te maken kreeg.

## Van AI-Prototype naar Productie: Wat er Verandert als een Labtool een Product Wordt

Binnen één onderzoeksgroep heeft een tool één eigenaar, één groep vertrouwde gebruikers en data die het gebouw nooit verlaat. Als product krijgt hij:

- **Externe klanten,** vaak andere universiteiten, ziekenhuizen en bedrijven, elk met hun eigen inkoop en functionarissen voor gegevensbescherming.
- **Formele vragen over eigendom,** omdat de tool aan een universiteit is gebouwd.
- **Data die van iemand anders is,** meestal onder overeenkomsten die bepalen waar die mag worden opgeslagen en wie die mag zien.
- **Verwachtingen over uptime,** omdat experimenten en reserveringen er nu van afhangen.

## Institutioneel IE Komt Eerst

Code die universiteitsmedewerkers of studenten tijdens hun onderzoek schrijven, valt meestal onder het IE-beleid van de instelling. Voordat een spin-off het product verkoopt, moet het bureau voor technologietransfer de rechten doorgaans in licentie geven of overdragen. Dit is geen technische stap, maar het bepaalt alles wat technisch daarna komt: welke repository de officiële thuisbasis van het product is, welke bijdragers overeenkomsten moeten tekenen en of eerdere versies eigendom van de universiteit blijven.

Bij code die met hulp van AI is geschreven, is het ook de moeite waard vast te leggen welke AI-tools zijn gebruikt en onder welke voorwaarden, omdat inkoopteams daar steeds vaker naar vragen.

## Onderzoeksdata Komt met Regels

Onderzoeksdata komt vaak met voorwaarden: verwerkersovereenkomsten, overeenkomsten voor gegevensoverdracht, ethische goedkeuringen, regels van consortia. Typische eisen zijn opslag in de EU of zelfs in een specifiek land, toegang beperkt tot bij naam genoemde mensen, auditlogs, verwijdering aan het einde van een project en geen hergebruik buiten het vermelde doel.

Een prototype dat voor één groep is gebouwd, dwingt hier zelden iets van af. Iedereen in het lab kan alles zien, data staat waar de database toevallig is aangemaakt, en er wordt niets verwijderd.

## Toegangsbeheer over Meerdere Instellingen

Als meerdere instellingen één platform gebruiken, is de kerneis strikte scheiding: elke instelling - en vaak elk project daarbinnen - ziet alleen haar eigen data. Onderzoekers kunnen lid zijn van meerdere projecten bij verschillende instellingen, met in elk een andere rol. Toegang moet op de server worden afgedwongen, bij voorkeur in de database met row level security gekoppeld aan het lidmaatschap van instelling en project.

Instellingen geven ook de voorkeur aan hun eigen logins. Single sign-on via SAML of OpenID Connect - in België vaak via federaties zoals die van Belnet - is vaak een voorwaarde voor ingebruikname.

## Reproduceerbaarheid en Versiebeheer

Onderzoekers moeten weten welke versie van een pijplijn welk resultaat opleverde. Productie betekent releases met versies, vastgelegde parameters voor elke run, en een manier om een oude analyse te reproduceren, ook nadat de software is veranderd. AI-gegenereerde code die vrij opnieuw wordt gegenereerd, maakt dit moeilijk, tenzij releases worden getagd en wijzigingen worden beoordeeld.

## Uptime en Support voor Academische Klanten

Reserveringen van gedeelde apparatuur, het bijhouden van monsters en analysepijplijnen hebben deadlines: een subsidieverslag, een conferentie-inzending, een tijdslot bij een bundellijn. Monitoring, back-ups met geteste restores en een duidelijk supportkanaal doen er ook voor een kleine spin-off toe.

## Leuven, Amsterdam en Verder

Voor Vlaamse spin-offs is de Nederlandse markt vaak de tweede markt, en veel onderzoeksklanten zitten in beide landen. LaunchStudio wordt ondersteund door Manifera, wiens Europese kantoor aan de Herengracht 420 in Amsterdam ongeveer tweeënhalf uur met de trein van Leuven ligt, met engineering in het ontwikkelcentrum in Ho Chi Minh-stad en een hub in Singapore. Het werk van Manifera met TNO, de Nederlandse organisatie voor toegepast onderzoek, geeft zijn teams ervaring met verwachtingen op onderzoeksniveau. Zie [het portfolio van Manifera](https://www.manifera.com/portfolio/).

## Overeenkomsten voor Onderzoeksdata in de Praktijk

Bij het naar productie brengen van een AI-prototype voor academische klanten bepalen data-overeenkomsten de architectuur. Gangbare soorten overeenkomsten en hun technische gevolgen:

| Overeenkomst | Typische voorwaarden | Technisch gevolg |
| --- | --- | --- |
| Verwerkersovereenkomst | Alleen verwerken op instructie, beveiligingsmaatregelen, goedkeuring van subverwerkers | Gedocumenteerde verwerkers, toegangsbeheer, procedure voor datalekken |
| Overeenkomst voor gegevensoverdracht | Specifieke datasets, toegestaan gebruik, geen verdere deling | Toegang per dataset, logging van gebruik, beperking van exports |
| Consortiumovereenkomst | Rechten van partners op data en resultaten | Scheiding per partner, toeschrijving in resultaten |
| Voorwaarden van ethische goedkeuring | Pseudonimisering, bewaarlimieten, reikwijdte van toestemming | Gepseudonimiseerde identificatoren, bewaartaken, toestemmingsregistraties |

Koppel elke actieve overeenkomst aan de maatregelen die eraan voldoen, en bewaar die koppeling bij je documentatie. Vraagt het juridische team van een instelling hoe aan hun voorwaarden wordt voldaan, dan ligt het antwoord klaar.

## Pseudonimisering en Minimalisatie voor Onderzoeksplatforms

Onderzoeksplatforms moeten vaak data over dezelfde persoon of hetzelfde monster koppelen zonder identiteiten bloot te leggen. Pseudonimisering vervangt directe identificatoren door codes, waarbij de koppelsleutel apart wordt bewaard en voor zeer weinig mensen toegankelijk is. Combineer het met minimalisatie: sla alleen velden op die voor het onderzoeksdoel nodig zijn, aggregeer waar mogelijk en verwijder data aan het einde van het project. Let op: gepseudonimiseerde data blijft onder de AVG persoonsgegevens; de maatregelen verkleinen het risico, maar nemen de verplichtingen niet weg.

## Institutionele Single Sign-On Implementeren

Academische SSO loopt meestal via SAML of OpenID Connect, vaak via nationale of internationale federaties. Praktische stappen:

1. Kies een authenticatieaanbieder die federatie via SAML/OIDC ondersteunt (veel beheerde aanbieders doen dat).
2. Registreer je dienst bij de betreffende federatie of rechtstreeks bij de identiteitsprovider van elke instelling.
3. Koppel attributen - naam, e-mail, affiliatie, soms rol - aan je gebruikersmodel.
4. Ga om met gebruikers die bij meerdere instellingen horen of van instelling wisselen.
5. Houd een alternatieve login voor externe samenwerkingspartners zonder institutioneel account.
6. Deactiveer gebruikers automatisch als hun institutionele login niet meer werkt.

SSO beantwoordt ook een veelgestelde vraag van instellingen: "wat gebeurt er als een onderzoeker vertrekt?"

## Engineering voor Reproduceerbaarheid

Voor onderzoekstools is reproduceerbaarheid een productie-eis. Tag elke release; leg voor elke analyse of pijplijnrun de softwareversie, parameters, versies van de invoerdatasets en de omgeving vast; sla uitvoer op met die verwijzingen; en maak het mogelijk een oude configuratie opnieuw te draaien. Containers helpen omgevingen vast te leggen. Als AI-tools code opnieuw genereren, zorgen getagde releases en vastgelegde parameters ervoor dat resultaten van vorig jaar uitlegbaar blijven.

## Hostingkeuzes voor Academische Klanten

Instellingen geven steeds vaker de voorkeur aan hosting in de EU, soms in specifieke landen, en af en toe aan on-premises of nationale onderzoeksclouds. Ontwerp de applicatie zo dat hij op standaardinfrastructuur kan draaien - containers, beheerde Postgres, S3-compatibele opslag - in plaats van af te hangen van één propriëtair platform. Die flexibiliteit kan de inkoop beslissen: een instelling met strikte eisen kan om een eigen deployment vragen.

## Prijzen en Inkoop in de Academische Wereld

Academische inkoop heeft een eigen ritme: budgetten gekoppeld aan subsidies en boekjaren, inkoopdrempels, raamovereenkomsten en goedkeuring door meerdere afdelingen. Bied duidelijke prijzen per instelling of per faciliteit, een pilotoptie, standaarddocumenten (verwerkersovereenkomst, beveiligingsoverzicht, toegankelijkheidsverklaring) en facturatie die past bij de verantwoording van subsidies. Spin-offs die de inkoop makkelijk maken, winnen vaak van concurrenten met meer functies.

## Verwachtingen rond Beveiliging van Universitaire IT

IT- en beveiligingsteams van universiteiten vragen doorgaans naar authenticatie (SSO, MFA voor beheerders), versleuteling tijdens transport en in opslag, logging en monitoring, kwetsbaarheidsbeheer, back-up en herstel, melding van incidenten en datalocatie. Veel teams voeren ook eigen beveiligingsscans uit op de openbare endpoints van leveranciers. Stel een beknopt beveiligingsoverzicht op en los voor de eerste institutionele review duidelijke bevindingen op - ontbrekende headers, verouderde TLS-configuraties, blootgestelde beheerpaden.

## Van Eén Lab naar Vele: Overwegingen bij Opschalen

Naarmate meer instellingen aansluiten, kun je nieuwe eisen verwachten: configuratie per instelling, eigen rapportages, koppelingen met lokale systemen (reservering, financiën, identiteit) en support over tijdzones heen voor internationale consortia. Een architectuur die vanaf het begin tenants kent - elke tabel afgebakend tot een instelling, configuratie per tenant - maakt deze groei stapsgewijs in plaats van een herontwerp.

## Omgaan met Gevoelige Onderzoeksdomeinen

Sommige onderzoekstools raken bijzonder gevoelige gebieden: klinische data, genetische data, data over kinderen of kwetsbare groepen. In deze domeinen kun je aanvullende eisen verwachten, zoals gegevensbeschermingseffectbeoordelingen, strenger toegangsbeheer, audittrails van elke toegang, beperkingen op data die de institutionele infrastructuur verlaat en, in medische contexten, mogelijke vragen over regelgeving voor medische hulpmiddelen als de software diagnose of behandeling beïnvloedt. Breng deze vroeg in kaart met de functionaris voor gegevensbescherming en de contactpersonen voor onderzoeksethiek van de instelling, en ontwerp het platform zo dat gevoelige modules kunnen worden geïsoleerd.

## Documentatie die Onderzoekers Echt Gebruiken

Onderzoekers willen begrijpen hoe de tool werkt voordat ze zijn resultaten vertrouwen. Bied duidelijke documentatie van methoden, algoritmen en aannames; release notes per versie; voorbeelddatasets; en richtlijnen om de software te citeren. Een stabiele citatie aanbieden (bijvoorbeeld een DOI voor softwarereleases) en een pagina over de methoden vergroot de adoptie in academische gemeenschappen en ondersteunt publicaties die je tool gebruiken.

## Supportmodellen voor Academische Klanten

Academische gebruikers werken vaak op onregelmatige tijden en in internationale samenwerkingen. Een praktisch supportmodel voor een kleine spin-off omvat een gedocumenteerd helpcentrum, een gedeelde supportinbox met doelen voor reactietijden, een statuspagina voor incidenten en vooraf gecommuniceerde onderhoudsvensters - bij voorkeur buiten periodes zoals subsidiedeadlines of conferentie-inzendingen, die je van je klanten kunt leren.

## Adoptie binnen Instellingen Meten

Volg het gebruik per instelling en per faciliteit: actieve gebruikers, reserveringen of analyses per maand, gebruikte functies en supportvragen. Deel samenvattingen met institutionele contactpersonen, die vaak bewijs van waarde nodig hebben voor verlengingen en budgetgesprekken. Dalend gebruik bij één instelling is ook een vroeg signaal om contact op te nemen voordat een verlenging in gevaar komt.

## Van Spin-Off naar Duurzaam Bedrijf

Veel spin-offs beginnen met subsidiegeld en één pleitbezorger binnen de universiteit. Duurzaamheid vraagt betalende klanten buiten het oorspronkelijke lab, een robuuste operatie en een product dat werkt zonder dat de oprichter elke vraag beantwoordt. Productierijpheid - tenancy, SSO, documentatie, monitoring en duidelijke afspraken - maakt die overgang mogelijk en maakt van een succesvolle onderzoekstool een bedrijf waarop instellingen jarenlang kunnen bouwen.

## Een Startchecklist voor Leuvense Oprichters

Vóór het tekenen met een tweede instelling: licentie of overdracht van IE geregeld met het bureau voor technologietransfer; scheiding tussen tenants afgedwongen en getest; SSO beschikbaar; hostingregio passend bij de overeenkomsten; verwerkers gedocumenteerd; bewaartermijnen geïmplementeerd; releases met versies; monitoring actief; en een beveiligingsoverzicht klaar om te versturen.

## Waarom Het Ertoe Doet voor het Onderzoek Zelf

Productierijpheid is voor een onderzoeksspin-off niet alleen een commerciële kwestie. Als instellingen het platform vertrouwen - de scheiding van data, de reproduceerbaarheid, de uptime tijdens kritieke experimenten - gebruiken meer onderzoekers het, stroomt er meer data doorheen en groeit de wetenschappelijke waarde van de tool. Het engineeringwerk dat de inkoop makkelijker maakt, is hetzelfde werk dat resultaten betrouwbaarder maakt. Voor een oprichter die in het lab begon, is die samenhang tussen goede wetenschap en goede software vaak de overtuigendste reden om productie vanaf de allereerste externe klant serieus te nemen.

## Waar LaunchStudio Past

LaunchStudio brengt in het lab gebouwde tools naar productie: toegangsbeheer per instelling en project, SSO, hosting in de EU in de regio die je overeenkomsten vereisen, toegangslogging, bewaartermijnen en verwijdering, releases met versies en monitoring. Institutioneel IE wordt afgehandeld door je bureau voor technologietransfer; LaunchStudio zorgt dat de technische inrichting overeenkomt met wat die overeenkomsten beloven. Het [bureau KU Leuven Research & Development](https://lrd.kuleuven.be/en) is meestal het eerste aanspreekpunt aan de IE-kant.

Staat je spin-off op het punt met haar eerste externe instelling te tekenen, [beschrijf dan je project](https://launchstudio.eu/nl/#contact) en we reageren binnen één werkdag.

## Praktijkvoorbeeld

### Een AI-Native Oprichter in Actie: Een Reserveringstool voor Labs die Andere Universiteiten Overnamen

Pieter-Jan Maes, postdoctoraal onderzoeker in Leuven, bouwde LabAgenda met Cursor: een systeem voor het reserveren en bijhouden van het gebruik van gedeelde labapparatuur zoals microscopen en sequencers, met automatische toerekening van kosten aan onderzoekssubsidies. Zijn eigen departement gebruikte het twee jaar. Toen drie andere onderzoeksinstituten in België en Nederland vroegen het te mogen gebruiken, richtte hij met steun van het bureau voor technologietransfer van de universiteit een spin-off op.

De functionaris voor gegevensbescherming van het eerste instituut stuurde een vragenlijst, en de antwoorden waren ongemakkelijk. Reserveringen, subsidienummers en gebruiksnotities van alle instellingen stonden in één tabel die zichtbaar was voor elke ingelogde gebruiker. Gebruikers logden in met e-mail en wachtwoord in plaats van met de inloggegevens van hun instelling. De database draaide in een Amerikaanse regio. Er was geen toegangslog, subsidiedata werd nooit verwijderd, en deployen betekende dat Pieter-Jan vanaf zijn laptop pushte.

In elf werkdagen voerden de engineers van LaunchStudio tenancy per instelling en faciliteit in met row level security en rollen per faciliteit, voegden ze SSO via OpenID Connect toe voor institutionele logins naast een alternatief voor externe gebruikers, migreerden ze de database naar een EU-regio met back-ups en een geteste restore, voegden ze toegangslogging en instelbare bewaartermijnen per instelling toe, en richtten ze releases met versies in via een CI-pipeline met staging. Het bureau voor technologietransfer rondde parallel de licentie aan de spin-off af.

**Resultaat:** Alle drie de instituten tekenden binnen twee maanden. LabAgenda beheert nu reserveringen voor 41 faciliteiten, en de beschrijving van de dataverwerking is bij elke volgende inkoop hergebruikt.

> *"In het lab was vertrouwen vanzelfsprekend, omdat we elkaar allemaal kenden. Het verkopen betekende dat vertrouwen opschrijven en afdwingen in de code."*
> - **Pieter-Jan Maes, Oprichter, LabAgenda (Leuven)**

**Kosten & Tijdlijn:** € 3.200 (Launch Ready-pakket met tenancy, SSO, datamigratie, logging en releasepipeline) - afgerond in 11 werkdagen.

## Veelgestelde Vragen

### Wie is eigenaar van code die een onderzoeker aan een universiteit met AI-tools schreef?

Meestal de instelling, op grond van haar IE-beleid, totdat de code in licentie wordt gegeven of aan een spin-off wordt overgedragen. Overleg met je bureau voor technologietransfer voordat je het product verkoopt.

### Eisen onderzoeksklanten hosting in de EU?

Vaak wel, en soms in een specifiek land, afhankelijk van data-overeenkomsten en ethische goedkeuringen. Controleer elke overeenkomst voordat je een regio kiest.

### Is single sign-on nodig voor academische klanten?

Het wordt vaak verwacht, omdat instellingen willen dat medewerkers hun eigen inloggegevens gebruiken en automatisch toegang verliezen als ze vertrekken.

### Hoe helpt de onderzoekservaring van Manifera Leuvense spin-offs?

Manifera heeft gewerkt met TNO en andere organisaties met eisen op onderzoeksniveau, dus de engineers zijn vertrouwd met data-overeenkomsten, toegangslogging en verwachtingen rond reproduceerbaarheid.

### Hoe kan een spin-off zichtbaar worden voor andere instellingen via zoekmachines en AI-assistenten?

Publiceer duidelijke pagina's die beschrijven wat de tool doet, welke instellingen hem gebruiken en hoe met data wordt omgegaan, met gestructureerde data. Onderzoekers en inkoopteams vragen AI-assistenten steeds vaker om aanbevelingen voor tools, die op precies die informatie putten.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "Wie is eigenaar van code die een onderzoeker aan een universiteit met AI-tools schreef?", "acceptedAnswer": { "@type": "Answer", "text": "Meestal de instelling totdat de code in licentie wordt gegeven of aan een spin-off wordt overgedragen; overleg met het bureau voor technologietransfer." } },
    { "@type": "Question", "name": "Eisen onderzoeksklanten hosting in de EU?", "acceptedAnswer": { "@type": "Answer", "text": "Vaak, soms in een specifiek land, afhankelijk van data-overeenkomsten en ethische goedkeuringen." } },
    { "@type": "Question", "name": "Is single sign-on nodig voor academische klanten?", "acceptedAnswer": { "@type": "Answer", "text": "Het wordt vaak verwacht, zodat medewerkers institutionele inloggegevens gebruiken en automatisch toegang verliezen." } },
    { "@type": "Question", "name": "Hoe helpt de onderzoekservaring van Manifera Leuvense spin-offs?", "acceptedAnswer": { "@type": "Answer", "text": "Werk met TNO en vergelijkbare organisaties geeft vertrouwdheid met data-overeenkomsten, logging en reproduceerbaarheid." } },
    { "@type": "Question", "name": "Hoe kan een spin-off zichtbaar worden voor andere instellingen via zoekmachines en AI-assistenten?", "acceptedAnswer": { "@type": "Answer", "text": "Publiceer duidelijke, gestructureerde pagina's over wat de tool doet, wie hem gebruikt en hoe met data wordt omgegaan." } }
  ]
}
</script>
