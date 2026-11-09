---
Titel: "Wat U Stuurt Vóór Uw Eerste Gesprek over Productie"
Trefwoorden: voorbereiden gesprek ontwikkelaar, wat sturen naar bureau voor offerte, kennismakingsgesprek productiegereedheid, briefing app voor offerte, LaunchStudio, Manifera
Koperfase: Beslissing
Doelgroep: AI-Native Oprichter (Niet-Technisch)
---

# Wat U Stuurt Vóór Uw Eerste Gesprek over Productie

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Wat U Stuurt Vóór Uw Eerste Gesprek over Productie",
  "description": "Een voorbereidingsgids voor oprichters vóór een kennismakingsgesprek over het productierijp maken van een app gebouwd met Lovable, Bolt, v0, Cursor of Claude Code: de samenvatting van één pagina, de lijst met tools en diensten, soorten gebruikers en rechten, betalingen, gegevens, bekende problemen, deadlines en eisen van klanten, hoe u toegang veilig deelt, wat u niet moet sturen en hoe voorbereiding leidt tot een snellere, nauwkeurigere vaste offerte.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-10-21",
  "inLanguage": "nl-NL",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/what-to-send-before-your-first-call-about-production" },
  "citation": [
    { "@type": "CreativeWork", "name": "GitHub: Inviting collaborators to a personal repository", "url": "https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-personal-account-on-github/managing-access-to-your-personal-repositories/inviting-collaborators-to-a-personal-repository" },
    { "@type": "CreativeWork", "name": "Supabase: Access control for organisations", "url": "https://supabase.com/docs/guides/platform/access-control" },
    { "@type": "CreativeWork", "name": "Vercel: Team members and roles", "url": "https://vercel.com/docs/rbac/access-roles" },
    { "@type": "CreativeWork", "name": "OWASP: Secrets Management Cheat Sheet", "url": "https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html" }
  ]
}
</script>

**Kort antwoord:** Stuur vóór uw eerste gesprek over het productierijp maken van uw app een samenvatting van één pagina over wat de app doet, een lijst met de tools en diensten die hij gebruikt, de soorten gebruikers en wat elk mag zien, of hij betalingen verwerkt of gevoelige gegevens opslaat, eventuele problemen die u heeft opgemerkt, uw deadline en eventuele eisen van klanten. Deel als het kan ook leestoegang tot de code. Stuur geen wachtwoorden of geheime sleutels per e-mail. Met deze informatie duurt het kennismakingsgesprek 15 minuten en volgt de vaste offerte snel en nauwkeurig.

Oprichters stellen het contact met een ontwikkelpartner soms uit omdat ze het gevoel hebben dat ze zich "goed moeten voorbereiden" of eerst de technische details moeten begrijpen. Dat hoeft niet. Wat het meest helpt, is eenvoudige informatie over uw app en uw bedrijf, die alleen u heeft. Deze pagina zet op een rij wat u stuurt, waarom het telt en wat u beter weglaat.

## Belangrijkste Punten

- **Een samenvatting van één pagina** in uw eigen woorden is het nuttigste wat u kunt sturen.
- **Een lijst met tools en diensten** laat zien waar de app draait en wie wat bezit.
- **Soorten gebruikers en hun rechten** brengen de grootste beveiligingsvragen aan het licht.
- **Bekende problemen en deadlines** bepalen de prioriteiten en de planning.
- **Stuur nooit wachtwoorden of geheime sleutels;** nodig mensen in plaats daarvan uit in accounts.

## 1. Een Samenvatting van Uw App op Eén Pagina

Schrijf een paar alinea's, alsof u uw app uitlegt aan een slimme vriend:

- Wat doet de app, en voor wie?
- Hoe lang is hij al live, en hoeveel gebruikers of klanten heeft hij?
- Wat is de belangrijkste route die een gebruiker doorloopt?
- Wat komt er aan: nieuwe klanten, een lancering, een demo voor investeerders?

U heeft geen technische termen nodig. "Sportscholen plannen er lessen mee, leden boeken en betalen, trainers zien hun eigen lessen" vertelt ons meer dan een lijst met frameworks.

## 2. Tools en Diensten

Zet alles op een rij wat de app gebruikt, voor zover u het weet:

| Categorie | Voorbeelden |
| --- | --- |
| AI-bouwtools | Lovable, Bolt, v0, Cursor, Claude Code |
| Code | GitHub-repository, of code alleen in de builder |
| Database en authenticatie | Supabase, Firebase, Neon, Clerk |
| Hosting | Vercel, Netlify, de eigen hosting van de builder |
| Betalingen | Stripe, Mollie |
| E-mail | Resend, Postmark, Brevo, de standaardmail van de databaseprovider |
| AI-providers | OpenAI, Anthropic, Google, Mistral |
| Integraties | Exact Online, HubSpot, Google Agenda, Shopify |
| Domein | Registrar en wie het heeft geregistreerd |
| Overig | Analytics, foutregistratie, bestandsopslag, sms |

Noteer bij elk in wiens account het staat: dat van u, van uw bedrijf, van een medeoprichter, van een freelancer. Vragen over eigendom horen bij de belangrijkste punten die we controleren, en ze vroeg kennen bespaart dagen.

## 3. Soorten Gebruikers en Wat Elk Mag Zien

Beschrijf de soorten gebruikers en hun rechten in begrijpelijke taal, bijvoorbeeld:

- "Klanten zien alleen hun eigen bestellingen en facturen."
- "Medewerkers bij een klantbedrijf zien de bestellingen van hun bedrijf; alleen financiën ziet facturen."
- "Ons supportteam ziet alle klanten, maar kan betalingen niet wijzigen."
- "Beheerders kunnen alles."

Tegen deze beschrijving testen we wanneer we de toegang tot de database beoordelen. De ernstigste problemen in apps gebouwd met AI zijn meestal verschillen tussen wat oprichters denken dat gebruikers kunnen zien en wat de app werkelijk toestaat.

## 4. Betalingen

Als de app geld ontvangt, beschrijf dan hoe: eenmalige betalingen, abonnementen, aanbetalingen, marktplaatsen met uitbetalingen. Welke provider, welke betaalmethoden, welke abonnementen? Hebben klanten ooit betaald zonder toegang te krijgen, of toegang gekregen zonder te betalen? Elk zulk verhaal is waardevol.

## 5. Gegevens

Wat voor gegevens slaat de app op? Alleen namen en e-mailadressen, of ook adressen, documenten, gezondheidsinformatie, financiële gegevens, gegevens van kinderen, gegevens van medewerkers? Waar denkt u dat ze worden gehost? Hebben klanten gevraagd naar de locatie van gegevens of een verwerkersovereenkomst gestuurd? Gevoelige gegevens veranderen de scope en zijn beter vroeg bekend.

## 6. Bekende Problemen

Zet alles op een rij wat u zorgen baart of is misgegaan: trage pagina's, e-mails in de spam, een testaccount dat de gegevens van iemand anders zag, betalingen die misgingen, fouten na een bepaalde wijziging, functies die u niet durft aan te raken. Zelfs vage gevoelens helpen, zoals "ik weet niet zeker of de beheerpagina beveiligd is". Niets wat u noemt, zal ons verrassen; dit zijn de problemen die we elke week oplossen.

## 7. Deadlines en Beperkingen

Is er een datum die telt: een lancering, een vakbeurs, een pilot met een klant, een demo voor investeerders, het begin van een schooljaar? Is er een budget waarbinnen u moet blijven? Zijn er periodes waarin de app niet mag veranderen, zoals een druk seizoen? Deadlines bepalen hoe we plannen en wat voorrang krijgt.

## 8. Eisen van Klanten of Investeerders

Als een klant een beveiligingsvragenlijst, een verwerkersovereenkomst, eisen voor toegankelijkheid of een verzoek om SSO heeft gestuurd, voeg dat dan toe. Als een investeerder vragen voor technische due diligence heeft gesteld, voeg die ook toe. Deze documenten bepalen de scope vaak preciezer dan wat dan ook.

## 9. Toegang, Veilig Gedeeld

Als u zich er prettig bij voelt, geef ons dan vóór het gesprek leestoegang, zodat we kort kunnen kijken en nauwkeurig kunnen offreren:

- **GitHub:** nodig ons uit als collaborator met leestoegang tot de repository
- **Builder:** sommige builders laten u medewerkers uitnodigen of een projectlink delen
- **Supabase, Vercel en andere:** nodig ons uit met een alleen-lezen- of ontwikkelaarsrol als die beschikbaar is

Als u nog niet klaar bent om toegang te delen, is dat prima. We kunnen beginnen met schermdelen tijdens het gesprek en een beschrijving van uw opzet.

## Wat U Niet Moet Sturen

- **Wachtwoorden** voor welk account dan ook
- **Geheime sleutels** zoals service role keys van Supabase, geheime sleutels van Stripe of API-tokens
- **Exports van klantgegevens** of databasedumps
- **Screenshots met persoonsgegevens** van uw klanten

Als u al ergens een geheim heeft gedeeld, zoals in een chat of e-mail, vermeld het dan; we helpen het als een van de eerste stappen te roteren.

## Een Eenvoudig Sjabloon

U kunt dit kopiëren en invullen:

1. Naam van de app en een omschrijving in één zin
2. Gebruikers en klanten nu, en verwacht over zes maanden
3. Gebruikte tools en diensten, en in wiens account elk staat
4. Soorten gebruikers en wat elk mag zien en doen
5. Betalingen: provider, model en eventuele problemen
6. Gegevens: soorten persoonsgegevens of gevoelige gegevens
7. Bekende problemen of zorgen
8. Deadline en waarom die telt
9. Eisen van klanten of investeerders, bijgevoegd indien beschikbaar
10. Toegang die u vóór het gesprek kunt delen

Dit sturen kost meestal 20 tot 30 minuten en maakt het gesprek veel nuttiger.

## Wat Er in het Gesprek Gebeurt

Het kennismakingsgesprek duurt ongeveer 15 minuten. We bevestigen wat u heeft gestuurd, stellen een paar vervolgvragen, leggen uit waar we naar zouden kijken en of Launch Ready of Launch & Grow waarschijnlijk past, en spreken de volgende stap af: meestal een korte blik op het project met leestoegang, gevolgd door een schriftelijke vaste offerte binnen één of twee werkdagen. Als uw app ons niet nodig heeft, of iets nodig heeft wat wij niet doen, zeggen we dat.

## Waarom Voorbereiding Leidt tot Betere Offertes

Vaste prijzen hangen af van juiste aannames. Als we uw tools, gebruikers, betalingen, gegevens en problemen vooraf kennen, kan de offerte specifieke onderdelen van de scope noemen, zoals "policies herschrijven voor de elf tabellen met klantgegevens, getest met accounts voor klant, medewerker en beheerder", in plaats van algemene uitspraken. Dat maakt de prijs betrouwbaarder, vermindert verrassingen tijdens het project en maakt de offerte eenvoudiger te vergelijken met andere.

## Als U de Antwoorden Niet Weet

Veel oprichters weten niet waar hun database wordt gehost, of er policies bestaan of wie het domein heeft geregistreerd. Dat is normaal, zeker als een freelancer in het begin heeft geholpen of de AI-tool alles heeft ingericht. Schrijf "weet ik niet zeker" en ga verder. Het uitzoeken is onderdeel van ons werk, en het overzicht van accounts dat we maken, beantwoordt deze vragen voorgoed.

## Delen met Andere Leveranciers

Dezelfde voorbereiding werkt voor elke leverancier. Als u er meerdere vergelijkt, stuur dan iedereen dezelfde samenvatting en toegang, zodat hun offertes op dezelfde informatie zijn gebaseerd. Dat maakt offertes veel eenvoudiger te vergelijken en laat zien welke leveranciers echt naar uw app hebben gekeken.

## Vragen die U Ons Misschien Wilt Stellen

Het kennismakingsgesprek is ook uw kans om ons te beoordelen. Nuttige vragen zijn: hoe test u dat gebruikers elkaars gegevens niet kunnen zien, wie gaat er aan het project werken, waar komen de accounts te staan, wat ontvang ik aan het einde, wat gebeurt er als u iets onverwachts vindt en welke ondersteuning krijg ik na de lancering? We beantwoorden deze vragen graag, en de antwoorden komen schriftelijk terug in de offerte.

## Na het Gesprek

Binnen één of twee werkdagen na het gesprek en de korte blik op uw project ontvangt u een schriftelijke offerte met scope, aannames, uitsluitingen, planning en vaste prijs. Er is geen verplichting. Als u besluit door te gaan, spreken we een startdatum af en sturen we een korte lijst met accounts waarvoor u ons uitnodigt. Als u besluit dat niet te doen, heeft u nog steeds een duidelijker beeld van de risico's van uw app dan daarvoor.

## Prijsreferentie

| Pakket | Prijs |
| --- | --- |
| Launch Ready | €800-€3.500 vast, inclusief 48 uur ondersteuning na de lancering |
| Launch & Grow | €2.500-€7.500 vast, plus €49 per maand voor doorlopende zorg |

Gebruik de [prijscalculator](https://launchstudio.eu/nl/#calculator) voor een indicatie vóór het gesprek.

## Screenshots en Korte Opnames

Als iets makkelijker te laten zien is dan te beschrijven, helpen een paar screenshots of een schermopname van twee minuten van de belangrijkste route veel: hoe een nieuwe gebruiker zich registreert, wat een beheerder ziet, waar een probleem optreedt. Zorg ervoor dat er geen persoonsgegevens van klanten zichtbaar zijn, of gebruik een testaccount. Een korte doorloop die u met uw telefoon opneemt, is vaak nuttiger dan een lange schriftelijke uitleg.

## Taal en Vorm

Stuur de informatie in het Nederlands of het Engels, wat voor u het makkelijkst is. Een document, een e-mail of zelfs de uitgeschreven tekst van een spraakmemo werkt. Volledigheid telt zwaarder dan een verzorgde vorm.

## Waarom Oprichters voor LaunchStudio Kiezen

LaunchStudio wordt ondersteund door Manifera, een softwareontwikkelingsbedrijf met 11+ jaar ervaring, 160+ opgeleverde projecten en 120+ engineers, dat werkt voor klanten zoals Vodafone en TNO. Oprichters ontmoeten het team aan de Herengracht 420 in Amsterdam; de engineering gebeurt in het ontwikkelcentrum van Manifera aan de Pho Quang Street in Ho Chi Minh City, met een hub aan de Tras Street in Singapore. Een korte, eerlijke beschrijving van uw app is alles wat we nodig hebben om te beginnen.

## Praktijkvoorbeeld

### Een AI-Native Oprichter in Actie: Twintig Minuten Voorbereiding, de Volgende Dag een Offerte

Nadia Bouzid runt vanuit Rotterdam een SaaS voor tolken en vertaalbureaus, gebouwd met Bolt en Supabase, waarin bureaus tolkopdrachten toewijzen, tolken ze accepteren en facturen maandelijks worden aangemaakt. Vóór haar eerste gesprek met LaunchStudio vulde ze het sjabloon in ongeveer twintig minuten in. Ze noemde Bolt, Supabase, Netlify, Mollie en Postmark, noteerde dat het Supabase-project was aangemaakt door een freelancer die haar in het begin had geholpen en schreef dat tolken alleen hun eigen opdrachten en tarieven mochten zien, terwijl bureaus hun eigen tolken en facturen mochten zien.

Bij bekende problemen schreef ze: "Een tolk vertelde me ooit dat ze het uurtarief van een andere tolk kon zien. Ik denk dat ik het met een prompt heb opgelost, maar ik weet het niet zeker." Ze voegde een beveiligingsvragenlijst toe van de tolkdienst van een ziekenhuis en vermeldde een pilot die over vijf weken zou starten. Ze nodigde LaunchStudio uit in de GitHub-repository met leestoegang.

Het kennismakingsgesprek duurde vijftien minuten. De korte blik bevestigde dat de eerdere reparatie het tarief in de interface had verborgen, maar het via de API leesbaar had gelaten, en dat het Supabase-project nog in het account van de freelancer stond. De schriftelijke offerte, €3.100 binnen Launch Ready, kwam de volgende ochtend binnen met achttien specifieke onderdelen, waaronder de overdracht van eigendom, policies voor bureaus en tolken met tests en ondersteuning bij de vragenlijst van het ziekenhuis.

**Resultaat:** Het project startte drie dagen later en was een week vóór de pilot klaar. Het ziekenhuis accepteerde de antwoorden op de vragenlijst, en Nadia zei dat de voorbereiding haar vanaf het eerste gesprek het gevoel gaf de regie te hebben.

> *"Ik dacht dat ik mijn app technisch moest begrijpen voordat ik iemand belde. Ik hoefde hem alleen eerlijk te beschrijven. Het technische deel was hun werk."*
> - **Nadia Bouzid, Oprichter, Tolkplanner (Rotterdam)**

**Kosten & Doorlooptijd:** €3.100 (Launch Ready-pakket: overdracht van eigendom, policies op basis van rollen met tests, controles van betalingen en e-mail, ondersteuning bij de vragenlijst en productieopzet) - offerte binnen één werkdag, project afgerond in 8 werkdagen.

## Veelgestelde Vragen

### Wat moet ik voorbereiden vóór een gesprek over het productierijp maken van mijn app?

Een korte samenvatting van de app, een lijst met tools en diensten met het eigendom van de accounts, soorten gebruikers en rechten, details over betalingen, soorten gegevens, bekende problemen, deadlines en eventuele eisen van klanten of investeerders. Leestoegang tot de code helpt, maar is optioneel.

### Moet ik vóór het gesprek wachtwoorden of sleutels delen?

Nee. Stuur nooit wachtwoorden of geheime sleutels per e-mail of chat. Nodig ons uit in accounts met onze eigen logins en passende rollen. Als er eerder een geheim is gedeeld, vermeld het dan en we helpen het te roteren.

### Wat als ik niet weet welke diensten mijn app gebruikt?

Schrijf op wat u weet en markeer de rest als onzeker. Het uitzoeken is onderdeel van ons werk, en het overzicht van accounts dat we tijdens het project maken, beantwoordt deze vragen blijvend.

### Hoe maakt de ervaring van Manifera het eerste gesprek efficiënt?

Manifera heeft in 11+ jaar met 120+ engineers 160+ projecten afgebakend en opgeleverd, voor klanten zoals Vodafone en TNO. LaunchStudio weet welke vragen tellen bij apps gebouwd met AI, dus een kort, goed voorbereid gesprek is genoeg voor een nauwkeurige offerte.

### Moet ik doelen rond SEO of zichtbaarheid noemen?

Ja, kort. Als openbare pagina's, posities in zoekmachines of hoe AI-antwoordmachines uw product beschrijven belangrijk voor u zijn, vermeld het dan. De productieopzet dekt de technische basis, en uw doelen kennen helpt ons prioriteit te geven aan de prestaties en metadata van openbare pagina's.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "inLanguage": "nl-NL",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Wat moet ik voorbereiden vóór een gesprek over het productierijp maken van mijn app?",
      "acceptedAnswer": { "@type": "Answer", "text": "Een korte samenvatting van de app, een lijst met tools en diensten met het eigendom van de accounts, soorten gebruikers en rechten, details over betalingen, soorten gegevens, bekende problemen, deadlines en eventuele eisen van klanten of investeerders. Leestoegang tot de code helpt, maar is optioneel." }
    },
    {
      "@type": "Question",
      "name": "Moet ik vóór het gesprek wachtwoorden of sleutels delen?",
      "acceptedAnswer": { "@type": "Answer", "text": "Nee. Stuur nooit wachtwoorden of geheime sleutels per e-mail of chat." }
    },
    {
      "@type": "Question",
      "name": "Wat als ik niet weet welke diensten mijn app gebruikt?",
      "acceptedAnswer": { "@type": "Answer", "text": "Schrijf op wat u weet en markeer de rest als onzeker. Het uitzoeken is onderdeel van ons werk, en het overzicht van accounts dat we tijdens het project maken, beantwoordt deze vragen blijvend." }
    },
    {
      "@type": "Question",
      "name": "Hoe maakt de ervaring van Manifera het eerste gesprek efficiënt?",
      "acceptedAnswer": { "@type": "Answer", "text": "Manifera heeft in 11+ jaar met 120+ engineers 160+ projecten afgebakend en opgeleverd, voor klanten zoals Vodafone en TNO. LaunchStudio weet welke vragen tellen bij apps gebouwd met AI, dus een kort, goed voorbereid gesprek is genoeg voor een nauwkeurige offerte." }
    },
    {
      "@type": "Question",
      "name": "Moet ik doelen rond SEO of zichtbaarheid noemen?",
      "acceptedAnswer": { "@type": "Answer", "text": "Ja, kort. Als openbare pagina's, posities in zoekmachines of hoe AI-antwoordmachines uw product beschrijven belangrijk voor u zijn, vermeld het dan." }
    }
  ]
}
</script>
