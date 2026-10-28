---
Titel: "Lovable Hosting: Omgevingsvariabelen in Drie Omgevingen"
Trefwoorden: lovable hosting, omgevingsvariabelen, beheer van geheimen, stagingconfiguratie, build-time variabelen, LaunchStudio, Manifera
Koperfase: Overweging
Doelgroep: Technische solo-oprichter / Indie hacker
---

# Lovable Hosting: Omgevingsvariabelen in Drie Omgevingen

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Lovable Hosting: Omgevingsvariabelen in Drie Omgevingen",
  "description": "Configuratie is waar door AI gebouwde apps sleutels lekken en deploys breken. Welke variabelen bewust publiek zijn, hoe u ontwikkeling, staging en productie gescheiden houdt, en wat u doet als er een geheim in de bundel belandt.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-10-21",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/lovable-hosting-environment-variables-across-three-environments" }
}
</script>

Twee mislukkingen zijn verantwoordelijk voor de meeste configuratie-incidenten in door AI gebouwde producten, en ze zijn elkaars tegenpolen.

De eerste: een geheim dat op de server had moeten blijven, belandt in het JavaScript dat naar browsers wordt gestuurd, waar iedereen het kan lezen. De tweede: een variabele die in productie had moeten zijn ingesteld, was dat niet, dus de deploy slaagde en de functie deed stilletjes niets - e-mails niet verstuurd, betalingen niet geïnd, fouten niet gemeld.

Beide hebben dezelfde oorsprong. De configuratie werd één keer haastig ingericht, door waarden te plakken waar de tool erom vroeg, en sindsdien heeft niemand ernaar gekeken.

## Publiek en Geheim Zijn Niet Hetzelfde Woord

Moderne frontendframeworks maken onderscheid tussen variabelen die in de browserbundel worden gecompileerd en variabelen die op de server blijven, en dat doen ze met een voorvoegsel in de naam. In op Vite gebaseerde projecten - wat Lovable oplevert - is alles wat met `VITE_` begint publiek. In Next.js is dat `NEXT_PUBLIC_`.

Publiek betekent niet "zichtbaar voor ingelogde gebruikers". Het betekent gecompileerd in een bestand dat iedereen kan downloaden en lezen, voor altijd, in elke kopie van die build.

De regel die daaruit volgt is absoluut: mag een waarde niet bij uw gebruikers bekend zijn, dan mag ze geen publiek voorvoegsel hebben en mag ze niet worden gebruikt in code die in de browser draait. Geen uitzonderingen, geen "het is maar een testsleutel", geen "niemand kijkt toch".

Sommige waarden zijn bewust publiek, en dat is prima. Een anonieme Supabase-sleutel hoort in de browser - de veiligheid ervan komt van row-level security, niet van geheimhouding. Een publieke Stripe-sleutel is per definitie publiek. Analytics-identificaties, de eigen URL van de applicatie, feature flags: allemaal publiek, allemaal onschuldig.

Wat nooit publiek mag zijn: de service role-sleutel van Supabase, elke geheime sleutel van een betaalprovider, database-connection strings, inloggegevens van de e-mailprovider, webhook-signing-secrets, en elke API-sleutel voor een dienst die op gebruik afrekent.

## De Service Role-Sleutel Verdient een Eigen Alinea

Van alle geheimen die een door AI gebouwde Supabase-applicatie verwerkt, is er één categorisch erger om te lekken.

De service role-sleutel omzeilt row-level security volledig. Wie hem heeft, kan elke rij in uw database lezen, wijzigen en verwijderen, ongeacht welke policy u hebt geschreven. Het is geen sleutel met verhoogde rechten; het is een sleutel met alle rechten.

Hij verschijnt met enige regelmaat in frontendcode, omdat een AI-sessie tegen een rechtenfout aanliep en het gebruik van die sleutel de fout liet verdwijnen. Het resultaat werkt perfect en is catastrofaal.

Controleer er specifiek op: doorzoek uw repository naar de variabelenaam, doorzoek uw build-uitvoer, en open het JavaScript van uw live site en zoek daar ook. Vindt u hem, dan vervangt u de sleutel en gaat u ervan uit dat de oude is gecompromitteerd.

## Drie Omgevingen, Drie Sets Waarden

Elke omgeving heeft een eigen volledige set nodig: ontwikkeling op uw machine, staging, productie.

Ontwikkelwaarden komen uit een lokaal bestand dat nooit wordt gecommit. Staging- en productiewaarden staan in de configuratie van uw hostingplatform, één keer ingevoerd, en bij voorkeur zichtbaar voor zo min mogelijk mensen.

Waar het om gaat, is dat ze echt gescheiden zijn. Een stagingomgeving die de database van productie gebruikt, is geen stagingomgeving. Een stagingomgeving die de e-mailgegevens van productie gebruikt, mailt uiteindelijk uw klanten. Een stagingomgeving die de betaalsleutels van productie gebruikt, schrijft uiteindelijk bij iemand geld af.

Heeft een dienst geen testmodus, dan krijgt staging helemaal geen inloggegevens en handelt de code de afwezigheid netjes af. Ontbrekende gegevens falen luid en onschadelijk; geleende productiegegevens falen stil en duur.

## Commit een Voorbeeld, Nooit een Waarde

Het bestand dat opsomt welke variabelen er bestaan, hoort in uw repository. De waarden niet.

Een `.env.example` met elke variabelenaam, een opmerking over waar elke variabele voor is, en een placeholder of een overduidelijk nepwaarde, is een van de waardevolste bestanden die een project kan hebben. Het vertelt een nieuwe developer - of uzelf over acht maanden - precies wat er moet worden ingesteld, informatie die anders in het geheugen van één persoon opgesloten zit.

Daarnaast: een controle bij het opstarten dat elke vereiste variabele aanwezig is, die direct faalt als dat niet zo is. Het alternatief is een deploy die slaagt en een functie die niet werkt, twee weken later ontdekt door een klant.

En bevestig dat uw ignore-regels het lokale bestand echt dekken. Geheimen die in een repository zijn gecommit, blijven na verwijdering in de geschiedenis staan, en daarom is de juiste reactie op het vinden ervan de inloggegevens te vervangen in plaats van het bestand te verwijderen.

## Build-Time Versus Run-Time

Een subtiliteit die verbijsterend gedrag oplevert: publieke variabelen worden ingebakken wanneer de applicatie wordt gebouwd, niet gelezen wanneer ze draait.

Wijzig er een in uw hostingdashboard en er gebeurt niets totdat u opnieuw bouwt. Oprichters wijzigen een waarde, herladen, zien het oude gedrag, en concluderen dat het platform kapot is of de cache verouderd.

Variabelen op de server worden bij het draaien gelezen en gelden bij de volgende aanroep. Hetzelfde dashboard bevat dus twee soorten instellingen die zich anders gedragen, en weten welke welke is bespaart ongeveer eens per kwartaal een middag.

De praktische gewoonte: start na het wijzigen van een publieke variabele een nieuwe build en controleer het in de live uitvoer in plaats van het aan te nemen.

## Preview-Deployments Vragen Aandacht

Platforms die voor elke branch een preview bouwen, zijn een echte productiviteitswinst en een stille blootstelling.

Die previews erven omgevingsvariabelen, wat kan betekenen dat een branch die uit een externe bijdrage is gebouwd draait met inloggegevens die u niet zou uitdelen. En previews zijn vaak publieke URL's, geïndexeerd door zoekmachines, met welke data hun omgeving ook aanwijst.

Twee instellingen lossen het op: previews krijgen hun eigen niet-productiewaarden, en ze worden beschermd tegen publieke toegang en tegen indexering. Beide kosten minuten en geen van beide staat in de meeste opstellingen standaard aan.

## Wanneer een Sleutel Is Gelekt

Ga ervan uit dat elk geheim dat in een publieke bundel, een repository, een schermafbeelding of een supportticket heeft gestaan, gecompromitteerd is, hoe kort ook.

De volgorde is: vervang de inloggegevens eerst bij de provider, zodat de oude niet meer werken; deploy de nieuwe waarde; kijk dan wat de oude kon bereiken en of hij is gebruikt, wat de meeste providers u vanuit hun logs kunnen vertellen. De sleutel uit uw code verwijderen is deel van de oplossing, niet de oplossing zelf - kopieën van uw build en uw repositorygeschiedenis blijven bestaan.

Sluit daarna de route die hem daar bracht, want een sleutel die één keer via frontendcode lekte, lekt opnieuw bij de volgende sessie die tegen dezelfde rechtenfout aanloopt.

## Wie Productie Kan Wijzigen, en Hoe U Dat Zou Weten

Configuratie is een categorie wijzigingen die elke waarborg omzeilt die u rond code hebt gebouwd. Er is geen review, geen testrun, geen deployregistratie - iemand past een veld in een dashboard aan en het gedrag van uw product verandert, direct, overal.

Voor een solo-oprichter is dat acceptabel, mits het risico wordt begrepen. Zodra een tweede persoon toegang heeft, verdient het twee kleine controles.

De eerste is een registratie. De meeste platforms loggen configuratiewijzigingen; zoek dat logboek één keer op, weet waar het staat, en bekijk het als er iets onverklaarbaars begint te gebeuren. Een groot deel van de incidenten waarbij "er niets veranderde en het brak" is een variabele die iemand met goede bedoelingen wijzigde.

De tweede is een lijst van wie toegang heeft, bekeken wanneer mensen beginnen of vertrekken. Een opdrachtnemer die in het voorjaar een week dashboardtoegang kreeg, heeft die in het najaar meestal nog steeds, en dashboardtoegang is meestal toegang tot elk geheim dat het product heeft. Het intrekken is een taak van twee minuten die niemand ooit inplant.

Nog één gewoonte die de moeite waard is: schrijf bij het wijzigen van een productiewaarde op wat en waarom, op dezelfde plek waar u deploys noteert. Configuratiedrift - het geleidelijk uit elkaar lopen van omgevingen doordat waarden in de ene worden gewijzigd en in de andere niet - is onzichtbaar totdat het een fout veroorzaakt die nergens te reproduceren is, en een gedateerde lijst van wijzigingen is de snelste weg terug.

## Dit Inrichten

Voor een bestaand product kost dit doorgaans een halve dag: elke variabele ingedeeld als publiek of geheim met afgedwongen naamgeving, de build-uitvoer en het live JavaScript doorzocht op alles wat er niet hoort, gelekte inloggegevens vervangen, drie volledige omgevingssets ingericht zonder gedeelde inloggegevens, een voorbeeldbestand gecommit met een opstartcontrole op vereiste variabelen, ignore-regels gecontroleerd, preview-deployments voorzien van eigen waarden en beschermd tegen publieke toegang, en een korte notitie die vastlegt waar elke waarde vandaan komt en wie haar kan wijzigen.

LaunchStudio doet dit als onderdeel van productieklaar maken, en vooral het doorzoeken van de bundel vindt vaker wel dan niet iets. De engineers zijn van Manifera - elf jaar, 120+ engineers, klanten als Vodafone, TNO en CFLW.

[Vraag ons uw live bundel te doorzoeken](https://launchstudio.eu/nl/#contact). Het kost vijf minuten.

## Echt voorbeeld

### Een Sleutel in de Bundel Sinds Maart

Jelmer Ottevanger bouwde Inkoopportaal met Lovable: een inkoopportaal waar 19 groothandels prijslijsten publiceren en zo'n 300 winkeliers bestellingen plaatsen.

Vroeg in de bouw liep een AI-sessie tegen een row-level security-fout aan bij het schrijven van een beheerrapport. De oplossing die ze opleverde, gebruikte de service role-sleutel van Supabase, en omdat het rapport in de browser draaide, kreeg de sleutel een publiek voorvoegsel. Het rapport werkte. De sleutel stond sinds maart in elke JavaScript-bundel die vanaf de site werd geserveerd.

Jelmer vond het in september, terwijl hij een artikel als dit las, door de broncode van zijn eigen site te openen en naar de variabelenaam te zoeken.

Eén werkdag, die dezelfde avond begon: de service role-sleutel direct vervangen bij Supabase, vóór al het andere; het beheerrapport herschreven als functie op de server met correcte autorisatie, met de anonieme sleutel en policies zoals de rest van de applicatie; de hele live bundel doorzocht op de andere geheimen, wat een sleutel van de e-mailprovider vond die op dezelfde manier was binnengekomen; beide inloggegevens vervangen en de toegangslogs met de support van Supabase bekeken, zonder onverwachte gebruikspatronen in de periode; drie volledige omgevingssets gescheiden, aangezien staging de database en e-mailgegevens van productie had gedeeld; een voorbeeldbestand gecommit met een opstartcontrole op elf vereiste variabelen; preview-deployments voorzien van eigen waarden en achter toegangsbeveiliging gezet; en een controle vóór de deploy toegevoegd die de build-uitvoer scant op bekende patronen van geheimen en de build laat falen.

**Resultaat:** geen aanwijzing dat de sleutel was gebruikt, wat Jelmer geluk noemt in plaats van een resultaat. De scan tijdens de build heeft sindsdien één nieuwe poging geblokkeerd om een serversleutel vanuit browsercode te gebruiken, in een sessie zes weken later die precies dezelfde fout maakte om precies dezelfde reden.

> *"Het werkte, dus ik heb er nooit meer naar gekeken. De sleutel die de prijzen van elke groothandel kan lezen, stond zes maanden in een bestand dat iedereen kon downloaden."*
> - **Jelmer Ottevanger, Oprichter, Inkoopportaal (Zwijndrecht)**

**Kosten & Doorlooptijd:** €1.700 (vervangen van inloggegevens, herschrijven van beheerrapport, bundelcontrole, scheiding van omgevingen, voorbeeldbestand en opstartvalidatie, previewbeveiliging, geautomatiseerde scan op geheimen in de build) - afgerond in 1 werkdag.

## Veelgestelde vragen

### Welke variabelen zijn veilig om aan de browser bloot te stellen?

Anonieme Supabase-sleutels, publieke betaalsleutels, analytics-identificaties, uw eigen URL's en feature flags. Nooit service role-sleutels, geheime betaalsleutels, database-URL's, e-mailgegevens of webhook-signing-secrets.

### Hoe controleer ik of er een geheim in mijn bundel staat?

Open het JavaScript van uw live site en zoek naar de variabelenaam of de waarde. Doorzoek ook uw repository en uw lokale build-uitvoer. Het kost minuten.

### Waarom had het wijzigen van een variabele geen effect?

Publieke variabelen worden tijdens de build ingecompileerd, dus ze vereisen een nieuwe build. Variabelen op de server worden bij het draaien gelezen en gelden bij de volgende aanroep.

### Wat doe ik als een sleutel is gelekt?

Vervang hem eerst bij de provider, deploy dan de nieuwe waarde, en bekijk daarna de logs van de provider op gebruik van de oude. Hem uit uw code verwijderen is niet genoeg - kopieën blijven bestaan in de geschiedenis en in oude builds.

### Hebben preview-deployments een aparte configuratie nodig?

Ja. Ze erven standaard variabelen, en preview-URL's zijn vaak publiek en indexeerbaar. Geef ze niet-productiewaarden en zet ze achter toegangsbeveiliging.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Welke omgevingsvariabelen zijn veilig om aan de browser bloot te stellen?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Anonieme Supabase-sleutels, publieke betaalsleutels, analytics-ID's, uw eigen URL's en feature flags - nooit service role-sleutels, geheime sleutels, database-URL's of webhook-secrets."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe controleer ik of er een geheim in mijn JavaScript-bundel staat?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Open het JavaScript van de live site en zoek naar de variabelenaam of waarde, en doorzoek ook uw repository en lokale build-uitvoer."
      }
    },
    {
      "@type": "Question",
      "name": "Waarom had het wijzigen van een omgevingsvariabele geen effect?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Publieke variabelen worden tijdens de build ingebakken en vereisen een nieuwe build; variabelen op de server worden bij het draaien gelezen."
      }
    },
    {
      "@type": "Question",
      "name": "Wat moet ik doen als een API-sleutel is gelekt?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Vervang hem eerst bij de provider, deploy de nieuwe waarde, en bekijk daarna de logs van de provider op gebruik van de oude sleutel. Hem uit de code verwijderen is niet genoeg."
      }
    },
    {
      "@type": "Question",
      "name": "Hebben preview-deployments een eigen configuratie nodig?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ja - ze erven standaard productievariabelen en hun URL's zijn vaak publiek en indexeerbaar. Geef ze aparte waarden en toegangsbeveiliging."
      }
    }
  ]
}
</script>
