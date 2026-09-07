---
Titel: "Wat Uw Engineeringpartner Vanaf Dag Eén Concreet van U Nodig Heeft"
Trefwoorden: onboarding software partner, dag één checklist oprichter, ontwikkelaar toegang geven, prototype overdracht software, voorbereiding software lancering, LaunchStudio, Manifera
Koperfase: Beslissing
Doelgroep: AI-Native Oprichter (Niet-technisch)
---

# Wat Uw Engineeringpartner Vanaf Dag Eén Concreet van U Nodig Heeft

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Wat Uw Engineeringpartner Vanaf Dag Eén Concreet van U Nodig Heeft",
  "description": "Een niet-technische oprichter die zojuist een ontwikkelovereenkomst heeft getekend, heeft de eerste 48 uur één kerntaak: het team deblokkeren. Welke accounts, inloggegevens en besluiten u in welke volgorde klaar moet zetten.",
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
  "datePublished": "2027-01-04",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://launchstudio.eu/nl/blog/what-your-engineering-partner-needs-from-you-day-one"
  }
}
</script>

**Software engineer, maandag 09:14:** "Goedemorgen! We staan klaar om te beginnen. Kun je me uitnodigen voor de repository en het Supabase-project?"  
**Oprichter, maandag 09:20:** "Zeker — wat is precies een repo?"  
**Software engineer, maandag 09:22:** "Het GitHub-project waar je Lovable-app naartoe exporteert. Weet je of die koppeling ooit is gelegd?"  
**Oprichter, woensdag 16:41:** "Gevonden! Het stond gekoppeld aan mijn oude e-mailadres. En ik moet geloof ik eerst het wachtwoord van Supabase resetten, momentje hoor."

Deze dialoog is volstrekt herkenbaar, niemand deed daarin bewust iets verkeerd, en toch heeft het tweeënhalve dag gekost van een ontwikkeltraject van twee weken. Het werk waarvoor u betaalde begon niet op maandagochtend; het begon pas woensdagavond laat. Er veranderde niets aan de offerte, er veranderde niets aan de overeengekomen scope, en toch verdampte zo'n 12% van de ingekochte kalendertijd aan het opzoeken van logins en het resetten van wachtwoorden.

Dit artikel biedt de praktische voorbereidingslijst die dit voorkomt: de specifieke accounts, toegangsrechten en beslissingen die vóór de allereerste werkdag klaar moeten staan — geschreven voor de oprichter die zijn product met Lovable of Bolt heeft gebouwd en nog nooit over DNS-records heeft nagedacht.

## Waarom Dag Eén de Goedkoopste Dag Is om Georganiseerd te Zijn

Een kort, vast geprijsd software-hardening traject kent een fasering die veel oprichters niet direct zien: de eerste twee dagen staan vrijwel geheel in het teken van doorgronden wat er al staat. Een engineer opent uw codebase, analyseert de datastructuren, inspecteert wat uw AI-tool automatisch heeft gegenereerd, en bouwt een mentale blauwdruk op. Elk uur dat een engineer een onderdeel niet kan inzien, moet hij aannames doen — en aannames doen in een tweewekelijks project is de reden waarom een "kleine wijziging" op dag negen plotseling ontaardt in een onaangename verrassing.

Het draait hier om asymmetrie. Het inventariseren van uw accounts kost u misschien negentig minuten aan relatief eenvoudig klikwerk. Doet u dat niet vooraf, dan kost dat het project twee tot vier dagen vertraging — en die dagen gaan direct ten koste van de opleverfase, niet van de start. Een traject van drie weken dat pas op woensdag in week één begint, wordt geen project van vier weken: het blijft een project van drie weken met simpelweg één week minder effectieve ontwikkeltijd. Niemand stuurt u daar een aparte rekening voor; u krijgt simpelweg een minder grondig afgewerkte livegang.

Er is bovendien een verborgen productiviteitsverlies. Wanneer een engineer geblokkeerd raakt, schakelt hij noodgedwongen over naar een andere taak. Terugkeren naar uw codebase betekent dat hij de code opnieuw moet doorgronden. In de praktijk kost een vertraging van twee dagen in week één al snel tweeënhalve dag aan effectieve output. De keuze is dus eenvoudig: negentig minuten van uw tijd op een zondag, of tweeënhalve dag van hun betaalde tijd doordeweeks.

## Bezit Eén: De Repository, en of U er Daadwerkelijk Eigenaar van Bent

Uw code bevindt zich ergens. Als u uw prototype in Lovable of Bolt hebt gebouwd, is er doorgaans een GitHub-koppeling — hetzij eentje die u vaag herinnert te hebben aangeklikt, hetzij eentje die nooit is aangemaakt, waardoor uw broncode uitsluitend in de online werkruimte van de AI-tool leeft. Beide situaties zijn oplosbaar. Wat echter funest is, is pas op maandagochtend ontdekken hoe het zit.

Log vóór dag één in op GitHub en controleer drie concrete zaken:
1. **Bestaat de repository en bevat deze recente code?** Klik erop en verifieer of de datum van de laatste commit ongeveer overeenkomt met de laatste keer dat u wijzigingen hebt aangebracht.
2. **Staat de repository onder uw persoonlijke account of onder een organisatie?** Als deze gekoppeld is aan een oud privé-mailadres waar u amper nog toegang toe hebt, los dat dan direct op. Het halverwege overdragen van een repository is het type klusje van twee uur dat gemakkelijk twee dagen vertraging oplevert.
3. **Is de repository privé?** Als uw repository per ongeluk openbaar staat en ergens een API-sleutel bevat, meld dit dan direct op dag één zodat het team deze kan saneren.

Bestaat er nog helemaal geen GitHub-koppeling? Wees daar direct helder over. In Lovable kunt u GitHub met een paar klikken koppelen via de projectinstellingen; de export duurt hooguit enkele minuten. Door dit vóór aanvang te regelen, landt de eerste commit van de engineer direct in een repository die u bezit, op een account dat u beheert.

## Bezit Twee: De Database- en Backend-Accounts

Achter de meeste AI-gegenereerde applicaties draait een Supabase- of Firebase-omgeving, aangemaakt door uzelf of automatisch op de achtergrond geïnitieerd door de AI-tool. Zoek deze op. Log in bij Supabase en bevestig dat u het projectdashboard en de bijbehorende organisatie ziet. Controleer bij Firebase in de Google Cloud Console of u bent geregistreerd als *Owner*, en niet louter als bewerker op het account van iemand anders.

Een veelvoorkomende valkuil zijn geleende accounts. Verrassend veel prototypes draaien op een Supabase-omgeving die ooit is aangemaakt door een behulpzame kennis "om het even snel werkend te krijgen", of op een gratis account van een voormalige mede-oprichter. Als dat bij u het geval is, los dit dan vóór dag één op — hetzij door het project formeel over te dragen naar uw eigen organisatie, hetzij door een verse database in te richten met een datamigratie.

Noteer direct twee kernfeiten waar uw engineer het eerste uur naar zal vragen:
- Bij benadering het aantal rijen in uw belangrijkste databasetabellen;
- Of de database echte persoonsgegevens van gebruikers bevat.

Het antwoord op die tweede vraag bepaalt de gehele aanpak. Echte persoonsgegevens betekenen dat staging-omgevingen moeten werken met geschoonde data, dat de AVG direct van toepassing is, en dat er nooit rechtstreeks op productie geëxperimenteerd mag worden. Bestaat de database louter uit testdata, dan kan het team aanzienlijk sneller schakelen.

## Bezit Drie: Betalingen — Het Account Dat U Nooit Uit Handen Moet Geven

Betaalproviders zoals Stripe en Mollie verschillen wezenlijk van alle andere accounts op deze lijst: ze raken direct aan uw geldstromen en bedrijfsrekening. De enige juiste werkwijze is: u bezit en beheert het account, deelt nooit uw primaire inloggegevens, en nodigt uw engineeringpartner uit als teamlid met strikt afgebakende rechten.

Maak het account altijd zelf aan op naam van uw onderneming, met uw eigen zakelijke e-mailadres en tweefactorauthenticatie (2FA).
- **In Stripe:** Ga naar *Instellingen → Team* en nodig de engineer uit met de rol **Developer**. Dit geeft toegang tot API-sleutels, webhooks en de testmodus, zónder dat men toegang krijgt tot bankrekeninggegevens, uitbetalingen of de optie om u uit te sluiten.
- **In Mollie:** (vaak de ideale keuze voor Nederlandse gebruikers vanwege de naadloze iDEAL-integratie): voeg de engineer toe als gebruiker binnen uw organisatie en houd het beheer over uitbetalingen en bankrekeningen exclusief onder uw eigen login.

Start dit administratieve traject per direct zodra u de ontwikkelovereenkomst tekent. Zowel Stripe als Mollie voeren strikte identiteits- en bedrijfscontroles uit (Know Your Customer / KYC): controle van uw KvK-nummer, btw-nummer, zakelijke tegenrekening, legitimatiebewijs en soms aanvullende vragen over uw bedrijfsmodel. Deze verificatie duurt van enkele uren tot meerdere werkdagen, en geen enkele engineer kan dit proces versnellen. Als verificatie pas in de lanceringsweek wordt gestart, schuift uw livegang gegarandeerd met een week op.

## Bezit Vier: Domeinnaam, DNS en het E-mailverzenddomein

Dit is het onderdeel dat oprichters het vaakst overslaan, en het is de voornaamste oorzaak van chaos in de week van lancering. Hier komen drie afzonderlijke onderdelen samen die regelmatig met elkaar worden verward:

1. **Uw domeinregistrar:** De partij waar u de domeinnaam hebt aangeschaft (bijv. TransIP, Namecheap, GoDaddy of Cloudflare). Zorg dat u kunt inloggen. Is het domein ooit gekocht door een externe ontwerper, een oud-compagnon of een marketingbureau uit 2024? Achterhaal dit direct. Een domein terugvorderen van iemand die niet meer reageert is een bureaucratisch drama waar geen technische oplossing voor bestaat.
2. **Uw DNS-beheer:** Het configuratiescherm binnen uw registrar (of binnen Cloudflare, als u uw DNS daarheen hebt verhuisd) waar records worden toegevoegd. Uw engineer moet hier records kunnen instellen om uw domeinnaam naar de hosting te verwijzen en om e-mailverzending te autoriseren. In plaats van uw hoofdwachtwoord af te geven, controleert u of uw provider gedelegeerde toegang ondersteunt (Cloudflare biedt bijvoorbeeld een specifieke DNS-beheerdersrol). Kan dit niet, spreek dan af dat u de records zelf invoert terwijl de engineer de waarden met u doorneemt via een kort videogesprek. Dat kost twintig minuten en is vele malen veiliger.
3. **Uw e-mailverzenddomein:** Dit is iets heel anders dan uw reguliere zakelijke inbox. Als uw applicatie wachtwoordresets, orderbevestigingen of notificaties verstuurt, gebeurt dit via een gespecialiseerde transactionele e-maildienst zoals Resend, Postmark of SendGrid. Deze berichten belanden onherroepelijk in de spambox tenzij de juiste SPF-, DKIM- en DMARC-records in uw DNS zijn geconfigureerd en geverifieerd. Deze verificatie en reputatie-opbouw vergen tijd. Richt het verzendaccount vooraf in en geef aan welke dienst u hebt gekozen.

## Bezit Vijf: Een Beknopt Document Dat Uitlegt Wat het Product Werkelijk Doet

Uw engineer kan uw broncode uitstekend lezen. Hij kan echter uw zakelijke intenties niet raden. Schrijf daarom één beknopte pagina — letterlijk één A4 in heldere, niet-technische taal — waarin u vier kernvragen beantwoordt:
1. **Wie gebruikt dit, en welke gebruikersrollen zijn er?** *"Zelfstandige boekhouders melden zich aan en voegen klanten toe; klanten krijgen een alleen-lezen dashboard"* — deze ene zin definieert direct het gehele rechtenmodel.
2. **Waarvoor betaalt men, en via welk model?** Eenmalig, een maandelijks abonnement of pay-per-use? Dit bepaalt de betalingsarchitectuur.
3. **Wat mag onder géén beding gebeuren?** *"Boekhouder A mag onder geen enkel beding de cliënten van Boekhouder B inzien."* Dit maakt van een impliciete aanname een keihard testbare security-eis.
4. **Welke schermen en functies zijn momenteel puur cosmetisch?** Vrijwel elk AI-prototype bevat fraaie schermen die draaien op statische placeholderdata. U weet exact welke dat zijn; zonder toelichting is een engineer uren kwijt om dit zelf uit te vogelen.

Wees volkomen open over dat laatste punt. Er is niets mis met een prototype waarin bepaalde grafieken worden gevoed door hardgecodeerde getallen — dat is precies wat AI-builders opleveren. Het vooraf expliciet benoemen is geen zwaktebod, maar efficiënte afbakening van de scope.

## Bezit Zes: Eén Beslisser, Eén Communicatiekanaal, Eén Reactietermijn

Het laatste dat uw engineeringpartner van u nodig heeft, is geen inlogcode. Het is een duidelijke afspraak over hoe besluiten worden genomen.
- **Wijs één beslisser aan:** Vrijwel zeker uzelf. Iemand die direct knopen kan doorhakken over functionaliteiten zonder eerst met een commissie te moeten overleggen.
- **Kies één centraal communicatiekanaal:** Een gezamenlijk Slack-kanaal, een WhatsApp-groep of e-mail — maar kies er één en houd u daaraan. Vragen die versnipperd binnenkomen via drie verschillende tools worden dubbel of helemaal niet beantwoord, en niemand kan achteraf nagaan wat er is besloten.
- **Spreek een vaste responstermijn af:** Bijvoorbeeld: *"Ik beantwoord inhoudelijke vragen binnen één werkdag, en op dinsdag- en donderdagmiddag ben ik direct bereikbaar."* Deze duidelijkheid is goud waard: het team weet precies wanneer ze vragen kunnen bundelen in plaats van te moeten raden of u van de radar bent verdwenen.

## Wat U Vooral Niet Moet Voorbereiden

U hoeft geen technische systeemeisen op te stellen, geen serverarchitectuur te ontwerpen en geen diepgaand onderzoek te doen naar AWS-clusters. Als u uzelf om middernacht betrapt op het bestuderen van Postgres Row Level Security documentatie: stop direct. U doet dan het werk waarvoor u juist specialisten inhuurt, en u doet het onvermijdelijk minder ervaren.

U hoeft evenmin uw code "op te schonen", ongebruikte schermen te wissen of dingen mooier te maken dan ze zijn. Engineers die dagelijks werken met AI-gegenereerde code weten exact wat ze kunnen verwachten. Vaak wist u bij het opruimen per ongeluk context die de ontwikkelaar juist nodig had.

En wanneer u iets écht niet weet — onder welke login een service hangt, of er e-mails worden verstuurd, wat er gebeurt als twee gebruikers hetzelfde account proberen te registreren — zeg dat dan gewoon eerlijk. *"Dat weet ik niet precies, maar ik denk dat we het hier kunnen vinden"* is een uitstekend antwoord. Een zelfverzekerde gok die later onjuist blijkt te zijn, kost daarentegen dagen. [LaunchStudio](https://launchstudio.eu/nl/) wordt ondersteund door de engineeringkracht van [Manifera](https://www.manifera.com/services/custom-software-development/), met meer dan 11 jaar ervaring. De meest waardevolle eigenschap tijdens een kickoff is nooit de technische woordenschat van een oprichter geweest, maar diens eerlijkheid over wat wel en niet bekend is.

Negentig minuten voorbereiding, zes heldere assets, één beknopt document. Zorg dat dit klaarstaat en uw project start op maandagochtend in plaats van woensdagavond — op een kort fixed-price traject is dat het verschil tussen een ontspannen lancering en een chaotische sprint.

**Twijfelt u over wat er momenteel gekoppeld is in uw Lovable- of Bolt-project? Deel uw link met ons: wij vertellen u exact wat er staat, wat er ontbreekt en wat u moet klaarzetten — kosteloos en vrijblijvend.**

## Praktijkvoorbeeld

### Een Oprichter in Actie: De Negentig Minuten Die een Week Redden

Sanne Vermeulen, voormalig tuinbouwadviseur in Utrecht, bouwde over een periode van zes weekenden met behulp van Lovable de applicatie Kweekplan — een teelt- en gewasrotatieplanner voor kleinschalige tuinders en biologische marktboeren. Ze tekende een vaste fixed-price hardening-opdracht en doorliep de dag vóór de officiële kickoff de complete voorbereidingslijst.

Dat bracht drie concrete knelpunten aan het licht:
1. Haar GitHub-repository bestond wel, maar stond geregistreerd onder een oud Gmail-adres dat ze sinds 2025 niet meer gebruikte. Ze droeg de repository direct over naar haar actieve account.
2. Haar Supabase-project bleek te zijn aangemaakt door een vriend tijdens een meetup; ze verhuisde het project naar haar eigen zakelijke organisatie.
3. Ze beschikte nog over geen enkel Mollie-account, hoewel ze vanaf dag één abonnementen van €9 per maand via iDEAL wilde aanbieden. Ze startte de KvK-verificatie direct op vrijdagmiddag. De verificatie door Mollie nam vier werkdagen in beslag, maar liep nu volledig parallel aan de code-audit in plaats van het ontwikkelwerk te blokkeren.

**Resultaat:** Kweekplan startte op dag één om exact 09:00 uur met volledige toegang voor het ontwikkelteam. De betaalkoppeling met Mollie werd op dag acht in live-modus getest in plaats van op dag twaalf. Het platform ging live op de oorspronkelijk afgesproken datum, waarbij er zelfs twee dagen overbleven voor een grondige end-to-end test van het volledige abonnementsproces.

> *"Ik overwoog eerst om de checklist over te slaan omdat het voelde als administratieve rompslomp. Het bleken de meest waardevolle negentig minuten van het hele project te zijn: ik heb simpelweg een volle week aan ontwikkeltijd teruggewonnen door op zondag even gericht door mijn accounts te lopen."*
> — **Sanne Vermeulen, Oprichter, Kweekplan (Utrecht)**

**Kosten & Doorlooptijd:** €2.400 (Launch Ready pakket, authenticatie-hardening, data-isolatie en Mollie iDEAL-abonnementen) — binnen 11 werkdagen live in productie.

---

## Veelgestelde Vragen

### Wat als mijn code alleen in Lovable bestaat en nooit aan GitHub is gekoppeld?
Dat komt regelmatig voor en is geen enkel probleem. Koppel GitHub eenvoudig via de projectinstellingen van Lovable vóór dag één — het exporteren duurt doorgaans slechts een paar minuten. Hierdoor landt de eerste commit van de engineer direct in een repository die u bezit op uw eigen account. Mocht het exporteren niet lukken, meld dit dan direct vooraf; voor een ervaren engineer is dit binnen tien minuten opgelost, mits hij het vóór maandagochtend weet.

### Moet ik mijn softwarepartner mijn Stripe- of Mollie-inloggegevens geven zodat zij alles inrichten?
Nee, absoluut niet. Maak het betaalaccount altijd zelf aan op naam van uw onderneming met uw eigen e-mailadres en tweestapsverificatie. Nodig de ontwikkelaar in Stripe uit via *Instellingen → Team* met de rol **Developer**. Dit geeft hen toegang tot API-sleutels, webhooks en testomgevingen, terwijl bankgegevens, uitbetalingen en het juridische eigendom volledig in uw eigen handen blijven. In Mollie voegt u hen toe als geautoriseerde gebruiker met beperkte rechten.

### Hoe ver van tevoren moet ik de verificatie bij de betaalprovider starten?
Start dit op de dag dat u de overeenkomst met uw ontwikkelpartner ondertekent. Zowel Stripe als Mollie voeren wettelijk verplichte bedrijfs- en identiteitscontroles uit waarvoor u uw KvK-nummer, btw-nummer en zakelijke bankrekening moet overleggen. Deze controle duurt van enkele uren tot meerdere werkdagen en kan door niemand worden versneld. Start u tijdig, dan loopt dit geruisloos op de achtergrond; start u te laat, dan schuift uw lancering onherroepelijk op.

### Ik heb geen controle over mijn domein — een designer kocht het jaren geleden. Is dat een reëel probleem?
Ja, en het is essentieel om dit direct op te lossen in plaats van te wachten tot de lanceringsweek. Het terugkrijgen van een domeinnaam van een partij die niet meer reageert kan weken in beslag nemen en kent geen technische omweg. Neem direct contact met hen op. Blijken zij onbereikbaar, dan is het aanschaffen van een alternatieve domeinnaam in week één veel verstandiger dan deze blokkade ontdekken op de dag van livegang.

### Moet ik als niet-technische oprichter begrijpen wat SPF, DKIM en DMARC precies zijn?
Nee. U hoeft enkel te weten dat dit DNS-records zijn die bepalen of de e-mails van uw applicatie (zoals wachtwoordresets en welkomstmails) daadwerkelijk aankomen in de inbox van uw gebruikers in plaats van in de spambox. Uw verantwoordelijkheid is ervoor zorgen dat iemand records kan toevoegen aan uw DNS; de verantwoordelijkheid van uw engineeringpartner is bepalen welke specifieke records moeten worden geplaatst.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Wat als mijn code alleen in Lovable bestaat en nooit aan GitHub is gekoppeld?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Dat is gebruikelijk en eenvoudig op te lossen. Koppel GitHub vóór dag één via de Lovable-instellingen zodat de code exporteert naar een eigen repository. Geef het tijdig aan als dit niet lukt."
      }
    },
    {
      "@type": "Question",
      "name": "Moet ik mijn softwarepartner mijn Stripe- of Mollie-inloggegevens geven zodat zij alles inrichten?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Nee. Maak het account zelf aan en nodig de ontwikkelaar uit met een Developer-rol. Hierdoor kunnen zij sleutels en webhooks configureren zonder toegang tot uw bankrekening en uitbetalingen."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe ver van tevoren moet ik de verificatie bij de betaalprovider starten?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Start direct op de dag van ondertekening. KvK- en identiteitscontroles bij Mollie of Stripe duren vaak meerdere werkdagen en kunnen niet worden versneld door ontwikkelaars."
      }
    },
    {
      "@type": "Question",
      "name": "Ik heb geen controle over mijn domein — een designer kocht het jaren geleden. Is dat een reëel probleem?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ja, los dit direct op. Het opeisen van een domeinnaam bij een onbereikbare derde kan weken duren zonder technische omweg. Schaf desnoods tijdig een alternatief domein aan."
      }
    },
    {
      "@type": "Question",
      "name": "Moet ik als niet-technische oprichter begrijpen wat SPF, DKIM en DMARC precies zijn?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Nee, u hoeft alleen te zorgen voor toegang tot uw DNS-beheer. Uw ontwikkelaar weet exact welke records nodig zijn om te voorkomen dat transactionele e-mails in de spambox belanden."
      }
    }
  ]
}
</script>
