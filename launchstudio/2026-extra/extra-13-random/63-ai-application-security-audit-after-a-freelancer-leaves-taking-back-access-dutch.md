---
Titel: "Beveiligingsaudit van AI-Apps na Vertrek van een Freelancer: Toegangsrechten Terugnemen"
Trefwoorden: ai applicatie beveiligingsaudit, freelancer offboarding, toegangsrechten intrekken, code eigenaarschap, account eigenaarschap, LaunchStudio, Manifera
Koperfase: Bewustwording
Doelgroep: AI-Native Oprichter (Niet-Technisch)
---

# Beveiligingsaudit van AI-Apps na Vertrek van een Freelancer: Toegangsrechten Terugnemen

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Beveiligingsaudit van AI-Apps na Vertrek van een Freelancer: Toegangsrechten Terugnemen",
  "description": "Wanneer een freelancer of mede-oprichter vertrekt, blijven toegekende rechten vaak geruisloos actief. Dit artikel beschrijft de toegangs-audit die elke ondernemer moet uitvoeren - repositories, hosting, databases, API-sleutels, domeinen en betaalaccounts - inclusief de juridische kant van IE-overdracht.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-12-02",
  "inLanguage": "nl-NL",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/ai-application-security-audit-after-a-freelancer-leaves-taking-back-access" }
}
</script>

De freelancer die je hielp je Lovable-app af te maken, was vriendelijk, snel en werkt inmiddels voor een andere klant. Er ging niets mis. Maar ergens kan een GitHub-account dat jij niet beheert nog steeds code naar je repository pushen, werkt een Supabase-sleutel die tijdens het debuggen is gekopieerd nog steeds, en wordt je domein volgend jaar maart verlengd op zijn creditcard. Een beveiligingsaudit van je AI-applicatie nadat een bijdrager is vertrokken, gaat niet over wantrouwen. Het gaat erom zeker te weten dat de enige mensen die je product kunnen veranderen de mensen zijn die dat horen te kunnen.

## Waarom Toegang Langer Leeft dan de Samenwerking

Een AI-app snel bouwen betekent snel toegang uitdelen. Een freelancer heeft de repository nodig, de database, het hostingdashboard, soms de betaalaanbieder om webhooks te testen. Een medeoprichter richt het domein en de e-mailaanbieder in onder zijn eigen account, omdat dat sneller is. Niemand schrijft dit op, en als de samenwerking eindigt, draait niemand het terug.

Dat doet er om drie redenen toe. Accounts van voormalige bijdragers kunnen worden gecompromitteerd, ook als de mensen zelf betrouwbaar zijn. Je kunt bij een incident niet snel handelen als een account dat je nodig hebt wordt beheerd door iemand die niet meer reageert. En investeerders en klanten stellen steeds vaker precies deze vraag: wie heeft toegang tot je productiesystemen?

## De Beveiligingsaudit van een AI-Applicatie voor Toegang, Gebied voor Gebied

**Coderepository.** Maak een lijst van elke collaborator en deploy key op GitHub, GitLab of Bitbucket. Verwijder iedereen die geen toegang meer nodig heeft. Controleer of de repository zelf eigendom is van je bedrijfsaccount of van iemands persoonlijke account; draag hem zo nodig over.

**Projecten in AI-bouwers.** Lovable, Bolt, Replit en vergelijkbare tools hebben hun eigen manier van projecten delen. Voormalige bijdragers kunnen mogelijk nog bewerken en publiceren.

**Hosting en deployment.** Vercel, Netlify, Replit Deployments, AWS of DigitalOcean - controleer teamleden, API-tokens en gekoppelde Git-integraties.

**Database en backend.** Leden van het Supabase- of Firebase-project, plus sleutels. Service role keys en beheerdersinloggegevens die een freelancer gebruikte, horen te worden geroteerd, niet alleen zijn gebruiker verwijderd.

**Geheimen en API-sleutels.** Betaalaanbieders, e-mailaanbieders, API's van AI-modellen, kaarten en analytics. Iedereen die een geheime sleutel heeft gezien, kan die nog hebben. Roteer elke sleutel die een vertrokken bijdrager kan hebben gezien.

**Domein en DNS.** Wie is eigenaar van het account bij de registrar? Met wiens kaart wordt de verlenging betaald? Een domein verliezen is een van de weinige echt onherstelbare incidenten.

**E-mail, analytics en supporttools.** Google Workspace, transactionele e-mail, analyticsdashboards, helpdesk en foutregistratie.

**App-stores.** Ontwikkelaarsaccounts bij Apple en Google, als je een mobiele app hebt.

## De Volgorde van Roteren

Sleutels roteren kan productie breken als het onzorgvuldig gebeurt. Een veilige volgorde: maak eerst een lijst van elke plek waar een sleutel wordt gebruikt, maak dan de nieuwe sleutel aan, werk alle omgevingen bij, deploy, bevestig dat alles werkt, en trek pas daarna de oude sleutel in. Doe betaal- en databasesleutels op rustige uren, en houd een schriftelijke log bij van wat wanneer is geroteerd.

## De Contractuele Kant

Toegang is technisch; eigendom is juridisch. Controleer of je schriftelijke afspraken hebt met voormalige bijdragers waarin het intellectueel eigendom van de code aan je bedrijf wordt overgedragen, en of eventuele geheimhoudingsverplichtingen na het einde van de samenwerking doorlopen. Is er code geschreven zonder afspraak, vraag dan nu, terwijl de verhoudingen goed zijn, om een eenvoudige overdracht van IE. Dit is het soort document dat tijdens een financieringsronde of overname heel duur wordt om te verkrijgen.

## Maak Offboarding Routine

Voor de toekomst maakt een korte offboardingchecklist van een stressvolle audit een routine van tien minuten:

- Geef bijdragers persoonlijke accounts, nooit gedeelde logins
- Gebruik op elk platform teamfuncties, eigendom van het bedrijfsaccount
- Leg vast welke geheimen elke persoon kan zien
- Bij vertrek: accounts verwijderen, geheimen roteren, eigendom van alles bevestigen, de IE-overdracht archiveren

## Een Sjabloon voor een Toegangsregister

Het centrale resultaat van een beveiligingsaudit van een AI-applicatie gericht op toegang is een toegangsregister - een levend document met elk systeem en wie er toegang toe heeft:

| Systeem | Doel | Eigenaarsaccount | Mensen met toegang | Toegangsniveau | 2FA | Laatst beoordeeld |
| --- | --- | --- | --- | --- | --- | --- |
| GitHub-repository | Broncode | Bedrijfsorganisatie | Oprichter, ontwikkelaar | Beheerder, schrijven | Ja | Datum |
| Supabase-project | Database, authenticatie, opslag | Bedrijfs-e-mail | Oprichter | Eigenaar | Ja | Datum |
| Vercel | Hosting | Bedrijfsteam | Oprichter, ontwikkelaar | Eigenaar, lid | Ja | Datum |
| Mollie | Betalingen | Bedrijf | Oprichter, boekhouder | Eigenaar, alleen-lezen | Ja | Datum |
| Domeinregistrar | Domein, DNS | Bedrijf | Oprichter | Eigenaar | Ja | Datum |
| E-mailaanbieder | Transactionele e-mail | Bedrijf | Oprichter | Eigenaar | Ja | Datum |
| Foutregistratie | Monitoring | Bedrijfsorganisatie | Oprichter, ontwikkelaar | Beheerder, lid | Ja | Datum |

Houd daarnaast een register van geheimen bij met per sleutel de naam, de dienst waar hij bij hoort, waar hij is opgeslagen en wanneer hij voor het laatst is geroteerd - nooit de waarde zelf. Bekijk beide maandelijks en nadat iemand bijkomt of vertrekt.

## Sleutels Roteren Zonder Downtime

Roteren is waar het opschonen van toegang het vaakst storingen veroorzaakt. Een veilige procedure per sleutel:

1. **Vind elk gebruik:** omgevingsvariabelen in elke omgeving, CI-geheimen, automatiseringstools, mobiele apps, koppelingen met partners.
2. **Maak de nieuwe sleutel aan** in het dashboard van de aanbieder terwijl de oude nog werkt.
3. **Werk elk gebruik bij** met de nieuwe sleutel en deploy.
4. **Verifieer** in logs of het dashboard van de aanbieder dat verzoeken nu de nieuwe sleutel gebruiken.
5. **Trek de oude sleutel in.**
6. **Leg de rotatie vast** in het register van geheimen.

Plan het roteren van databasewachtwoorden en service role keys op rustige uren en houd een terugvalplan achter de hand. Voor ondertekeningsgeheimen van webhooks staan sommige aanbieders tijdens een overgangsperiode twee actieve geheimen toe.

## Achtergebleven Toegang op Onverwachte Plekken

Voormalige bijdragers houden vaak toegang op plekken waar niemand kijkt:

- **Persoonlijke toegangstokens** op GitHub of hostingplatforms, aangemaakt voor lokale deployments.
- **Deploy keys en CI-geheimen** in forks of oude repositories.
- **OAuth-apps** die gemachtigd zijn namens je accounts te handelen.
- **Automatiseringstools** (n8n, Make, Zapier) die met hun inloggegevens zijn gekoppeld.
- **Gedeelde wachtwoordmanagers of chatberichten** met sleutels erin.
- **Lokale `.env`-bestanden** op hun computers - daarom is roteren, niet alleen verwijderen, belangrijk.
- **Back-upkopieën of exports** van je database die ze mogelijk hebben gedownload.

Vraag vertrekkende bijdragers beleefd en schriftelijk om lokale kopieën van code, data en inloggegevens te verwijderen en te bevestigen dat ze dat hebben gedaan.

## Offboardingchecklist

Loop bij elk vertrek het volgende door:

- Verwijder uit repository, AI-bouwer, hosting, database, betalingen, e-mail, analytics, monitoring en supporttools.
- Trek persoonlijke tokens en OAuth-machtigingen in die ze hebben aangemaakt.
- Roteer elk geheim dat ze kunnen hebben gezien.
- Draag het eigendom over van elk account dat op hun naam is geregistreerd.
- Werk de registers van toegang en geheimen bij.
- Verzamel een ondertekende IE-overdracht en een bevestiging dat lokale kopieën zijn verwijderd.
- Controleer recente activiteitenlogs op iets ongewoons.

Bewaar de checklist bij je bedrijfsdocumenten en voer hem uit op de dag dat de samenwerking eindigt.

## Onboarding met Offboarding in Gedachten

De meeste pijn bij offboarding ontstaat bij onboarding. Geef iemand die begint persoonlijke accounts via teamfuncties die eigendom zijn van het bedrijf, de minimaal benodigde toegang, waar mogelijk alleen geheimen voor development, en een schriftelijke overeenkomst over IE en geheimhouding. Leg in het toegangsregister vast wat ze hebben gekregen. Bij vertrek is het terugdraaien dan snel gedaan.

## Juridische Afspraken die de Moeite Waard Zijn

Voor freelancers en opdrachtnemers hoort een eenvoudige overeenkomst het volgende te regelen: de scope van het werk, betaling, overdracht van intellectueel eigendom aan je bedrijf bij creatie of betaling, geheimhouding, verplichtingen rond gegevensbescherming als ze persoonsgegevens verwerken, teruggave of verwijdering van materialen aan het einde, en het niet behouden van toegang. Sjablonen zijn beschikbaar bij de Kamer van Koophandel en juridische diensten; een advocaat kan er in een uur een aanpassen. Voor code die al zonder overeenkomst is geschreven, is een korte IE-overdracht met terugwerkende kracht meestal makkelijk te verkrijgen zolang de relatie goed is.

## Signalen van Misbruik om op te Letten

Bekijk na iemands vertrek de logs van de weken ervoor en de dagen erna: ongebruikelijke logins, grote data-exports, wijzigingen in betaalinstellingen, nieuwe beheerders, verwijderde back-ups of nieuwe API-sleutels. De meeste vertrekken zijn volkomen onschuldig, maar een snelle controle geeft gemoedsrust en, in zeldzame gevallen, een vroege waarschuwing.

## Er een Routine van Maken

Toegangshygiëne werkt het best als maandelijkse gewoonte: tien minuten om het register met de werkelijkheid te vergelijken, verouderde toegang te verwijderen en geplande rotaties te noteren. Oprichters die er een routine van maken, krijgen zelden te maken met stressvolle opruimacties - en kunnen een vraag van een investeerder of klant over toegang binnen enkele seconden beantwoorden.

## Bijzondere Gevallen: Medeoprichters en Bureaus

Het vertrek van een medeoprichter is complexer dan dat van een freelancer, omdat medeoprichters vaak de accounts zelf hebben aangemaakt en mogelijk aandelen hebben. Regel toegang en eigendom in dezelfde aandeelhoudersovereenkomst of scheidingsovereenkomst: welke accounts worden overgedragen, wanneer, en hoe inloggegevens worden overhandigd. Vraag bureaus die je app hebben gebouwd om een formele overdracht - overdracht van de repository, inloggegevens, documentatie, een lijst van accounts bij derden die ze namens jou hebben aangemaakt - voordat de laatste factuur wordt betaald. Beide situaties zijn veel makkelijker op te lossen zolang de relaties goed zijn.

## Minimale Rechten voor het Dagelijkse Werk

Toegangsaudits laten vaak zien dat iedereen eigenaars- of beheerdersrechten heeft, simpelweg omdat dat het makkelijkst was. Beperk rechten tot wat elke persoon nodig heeft: ontwikkelaars hoeven zelden de facturatie te wijzigen, boekhouders hebben alleen-lezentoegang tot betalingen nodig, supportmedewerkers hebben een supportweergave nodig in plaats van toegang tot de database. Minder accounts met veel rechten betekent minder manieren waarop een gecompromitteerd account ernstige schade kan aanrichten - en een kortere lijst om elke maand te controleren.

## Wat Investeerders en Klanten Vragen

Vragenlijsten bij due diligence en beveiligingsreviews van grote klanten vragen vaak: Wie heeft beheerdersrechten op productie? Hoe wordt toegang verleend en ingetrokken? Wordt MFA afgedwongen? Hoe worden geheimen beheerd en geroteerd? Wanneer is de toegang voor het laatst beoordeeld? Een actueel toegangsregister en een offboardingchecklist beantwoorden alle vijf. Oprichters die deze documenten direct kunnen delen, vallen op - en vermijden de zoektocht die van een routinevraag een week speurwerk maakt.

## Hulpmiddelen die Helpen

Verschillende tools maken toegangsbeheer makkelijker voor kleine teams: een wachtwoordmanager voor het team voor gedeelde inloggegevens, SSO voor werkplektools waar dat betaalbaar is, secret managers voor applicatiesleutels, en instellingen van GitHub-organisaties die 2FA voor leden afdwingen. Geen ervan is strikt nodig, maar elk verkleint de kans dat toegang zich ongemerkt in persoonlijke accounts ophoopt.

## Het Principe

Toegang hoort altijd van het bedrijf te zijn en aan mensen te worden verleend - nooit andersom. Als dat principe overeind blijft, kunnen bijdragers komen en gaan zonder deuren open te laten achter zich.

## Begin Vandaag

Open nu de lijst met collaborators van je repository en de ledenlijst van je databaseproject. Iedereen die daar staat en er niet hoort te staan, is je eerste bevinding.

## Waar LaunchStudio Past

LaunchStudio voert toegangsaudits uit als onderdeel van zijn beveiligingsreviews: elk account, elke sleutel en elke koppeling in kaart gebracht, eigendom samengebracht onder je bedrijf met tweestapsverificatie, geheimen veilig geroteerd en een schriftelijk toegangsregister overgedragen. De code blijft in je repository, gedocumenteerd, en niemand bij LaunchStudio houdt na het project toegang, tenzij je om managed hosting vraagt.

LaunchStudio wordt aangedreven door Manifera, een softwareontwikkelbedrijf met 11+ jaar ervaring en een oprichter, Herre Roelevink, met een achtergrond in cybersecurity. Manifera werkt vanuit Amsterdam (Herengracht 420), Singapore (Tras Street) en Ho Chi Minh-stad. Zie [de over-ons-pagina van Manifera](https://www.manifera.com/about-us/); de [gids van GitHub over het beoordelen van toegang tot repositories](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/managing-repository-settings/managing-teams-and-people-with-access-to-your-repository) is een praktisch startpunt.

[Plan een gratis kennismakingsgesprek van 15 minuten](https://launchstudio.eu/nl/#contact) als je niet zeker weet wie je productiesystemen nog kan bereiken.

## Praktijkvoorbeeld

### Een AI-Native Oprichter in Actie: Een Marktplaats voor Verhuishulp en Vier Vergeten Accounts

Nadia Bakkali, voormalig logistiek planner in Alphen aan den Rijn, bouwde Verhuisvriend in Lovable met hulp van twee freelancers: een marktplaats waar mensen die verhuizen per uur lokale helpers en busjes boeken, met Mollie-betalingen en chat. Na de lancering vertrokken beide freelancers, en Nadia runde het platform acht maanden alleen, met een groei naar 1.700 afgeronde klussen.

Toen een groter verhuisbedrijf een samenwerking voorstelde, vroeg de IT-manager wie toegang had tot de productiesystemen van Verhuisvriend. Nadia kon dat niet beantwoorden. De audit van LaunchStudio vond dat één freelancer nog eigenaar was van de GitHub-repository en het Supabase-project; de ander had nog een plek in het Vercel-team en een persoonlijk toegangstoken waarmee kon worden gedeployd; de live API-sleutel van Mollie was tijdens het testen in een gedeelde chat geplakt en nooit geroteerd; het domein stond op naam van de eerste freelancer; en geen van beide freelancers had een IE-overdracht getekend.

De engineers van LaunchStudio droegen de repository en het Supabase-project over naar Nadia's bedrijfsaccount, verwijderden beide freelancers van alle platforms, trokken het Vercel-token in, roteerden de sleutels van Mollie, de Supabase service role, e-mail en kaarten in een geplande volgorde zonder downtime, zetten overal tweestapsverificatie aan en stelden een toegangsregister op. Nadia nam contact op met de freelancers, die binnen een week het domein overdroegen en IE-overdrachten tekenden.

**Resultaat:** Nadia stuurde het toegangsregister naar het verhuisbedrijf, en de samenwerking ging door. Verhuisvriend voert nu een offboardingchecklist van tien minuten uit telkens als een opdrachtnemer stopt.

> *"Niemand had iets verkeerds gedaan. Maar als een van hen zijn laptop was kwijtgeraakt, was hij mijn bedrijf er meteen bij kwijt geweest."*
> - **Nadia Bakkali, Oprichter, Verhuisvriend (Alphen aan den Rijn)**

**Kosten & Tijdlijn:** € 1.300 (toegangsaudit, overdracht van eigendom, rotatie van sleutels en toegangsregister) - afgerond in 5 werkdagen.

## Veelgestelde Vragen

### Wat moet een beveiligingsaudit van een AI-applicatie controleren nadat een freelancer is vertrokken?

Elk account en elke sleutel die de freelancer kon bereiken: repository, projecten in AI-bouwers, hosting, database, aanbieders van betalingen, e-mail en analytics, de domeinregistrar en app-stores - plus of het IE formeel aan je bedrijf is overgedragen.

### Is het verwijderen van het gebruikersaccount van een freelancer genoeg?

Nee. Sleutels en tokens die ze hebben gezien of aangemaakt, blijven werken nadat hun account is verwijderd. Roteer ook geheimen en trek persoonlijke toegangstokens en deploy keys in.

### Kan het roteren van API-sleutels mijn live app breken?

Dat kan, als het in de verkeerde volgorde gebeurt. Maak de nieuwe sleutel aan, werk elke omgeving bij, deploy en verifieer, en trek daarna de oude sleutel in - bij voorkeur op een rustig moment.

### Waarom behandelt Manifera toegangsbeheer als onderdeel van beveiliging, niet van administratie?

Omdat veel echte incidenten beginnen met vergeten toegang in plaats van slimme exploits. De achtergrond in cybersecurity van Herre Roelevink heeft de opvatting van Manifera gevormd dat weten wie productie kan veranderen een basis van beveiliging is.

### Kan duidelijk eigendom helpen bij samenwerkingen en door AI gestuurde due diligence?

Ja. Partners, investeerders en steeds vaker geautomatiseerde leveranciersbeoordelingen vragen wie je systemen beheert. Een gedocumenteerd toegangsregister beantwoordt die vraag direct en laat volwassenheid zien.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "Wat moet een beveiligingsaudit van een AI-applicatie controleren nadat een freelancer is vertrokken?", "acceptedAnswer": { "@type": "Answer", "text": "Elk account en elke sleutel die de freelancer kon bereiken, plus of het IE formeel aan het bedrijf is overgedragen." } },
    { "@type": "Question", "name": "Is het verwijderen van het gebruikersaccount van een freelancer genoeg?", "acceptedAnswer": { "@type": "Answer", "text": "Nee. Roteer ook geheimen en trek persoonlijke tokens en deploy keys in." } },
    { "@type": "Question", "name": "Kan het roteren van API-sleutels mijn live app breken?", "acceptedAnswer": { "@type": "Answer", "text": "Alleen in de verkeerde volgorde: aanmaken, bijwerken, deployen, verifiëren en dan intrekken." } },
    { "@type": "Question", "name": "Waarom behandelt Manifera toegangsbeheer als onderdeel van beveiliging, niet van administratie?", "acceptedAnswer": { "@type": "Answer", "text": "Veel incidenten beginnen met vergeten toegang; weten wie productie kan veranderen is een basis van beveiliging." } },
    { "@type": "Question", "name": "Kan duidelijk eigendom helpen bij samenwerkingen en door AI gestuurde due diligence?", "acceptedAnswer": { "@type": "Answer", "text": "Ja. Een gedocumenteerd toegangsregister beantwoordt vragen van leveranciersbeoordelingen en investeerders direct." } }
  ]
}
</script>
