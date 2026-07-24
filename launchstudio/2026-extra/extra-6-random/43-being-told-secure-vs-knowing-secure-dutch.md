---
Titel: "Het verschil tussen te horen krijgen dat het 'veilig' is en weten dat het veilig is"
Trefwoorden: ai secure, ai security claims, encryption at rest vs in transit, ai app security
Koperfase: Overweging
Doelgroep: AI-Native oprichter (niet-technisch)
---
# Het verschil tussen te horen krijgen dat het 'veilig' is en weten dat het veilig is

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Het verschil tussen te horen krijgen dat het 'veilig' is en weten dat het veilig is",
  "description": "Een opiniestuk over waarom een ai secure-label in uw bouwtool u bijna niets vertelt over of uw product daadwerkelijk veilig is om te lanceren — en wat oprichters in plaats daarvan zouden moeten vragen.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2026-07-25",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/being-told-secure-vs-knowing-secure" }
}
</script>

Hier is een onpopulaire mening: het woord "veilig" dat ergens in de interface van uw AI-ontwikkeltool verschijnt, zou u wantrouwiger moeten maken, niet geruster. Niet omdat de tool per se liegt. Maar omdat "veilig" een enorme hoeveelheid onverdiend werk verricht in één woord, en de meeste oprichters geen manier hebben om te weten wat er eigenlijk mee wordt beloofd.

Die kloof tussen te horen krijgen dat iets ai secure is en het daadwerkelijk weten, is het verschil tussen een product dat zijn eerste echte beveiligingscontrole overleeft en een product dat dat niet doet.

## Waarom "het is veilig" bijna een betekenisloze zin is

Beveiliging is geen enkele eigenschap. Het is een lange lijst van specifieke, apart verifieerbare claims: gegevens versleuteld tijdens transport, gegevens versleuteld in rust, wachtwoorden gehasht in plaats van in platte tekst opgeslagen, toegang correct afgebakend zodat de ene gebruiker de gegevens van een andere niet kan zien, afhankelijkheden vrij van bekende kwetsbaarheden, geheimen buiten de broncode gehouden. Een tool kan volledig eerlijk zijn wanneer hij zegt "uw gegevens zijn versleuteld", terwijl daarmee slechts één van die zes dingen wordt bedoeld.

De oprichter die dat bericht leest, heeft geen manier om te weten welke daarvan wordt bedoeld. Dat is geen tekortkoming die uniek is voor een bepaalde AI-codeertool — het is een structureel probleem van het samenpersen van een technische, meerledige claim tot een geruststelling van twee woorden, gericht op iemand zonder de achtergrond om die uit te pakken.

## Een onderscheid dat geen reden heeft om intuïtief te zijn

Julia Mertens, een oprichter in Renkum, bouwde KliniekAfspraak — een afsprakenapp voor een klein netwerk van klinieken — met Lovable. Op een gegeven moment vertelde de interface haar, botweg, dat haar gegevens versleuteld waren. Dat klopte. Het betekende alleen versleuteld tijdens transport — beschermd tijdens de beweging tussen de browsers van haar gebruikers en haar servers — niet versleuteld in rust, wat betekent onbeschermd zodra de gegevens in de database lagen.

Er is geen reden waarom Julia had moeten weten dat ze moest vragen om welk type het ging. Niets aan de zin "uw gegevens zijn versleuteld" geeft aan dat die slechts de helft van het plaatje beschrijft. Dit is geen kritiek op haar oordeel. Het is precies het soort onderscheid dat pas duidelijk wordt zodra iemand met de juiste achtergrond het uitlegt — en tegen die tijd is het vaak al relevant, omdat er al echte patiëntafspraakgegevens in die database staan.

## Wat "weten" er in de praktijk uitziet

Weten dat uw product veilig is, betekent specifieke vragen kunnen beantwoorden met specifieke antwoorden, geen onderbuikgevoel. Zijn gegevens versleuteld in rust, niet alleen tijdens transport? Zijn wachtwoorden gehasht met een modern algoritme, of ongewijzigd opgeslagen? Kan het personeelsaccount van de ene kliniek de patiëntenlijst van een andere kliniek zien als ze de juiste URL raden? Heeft iemand dat daadwerkelijk geprobeerd?

Geen van deze vragen vereist dat de oprichter engineer wordt. Ze vereisen dat de oprichter stopt met "het is veilig" te accepteren als volledig antwoord en het gaat behandelen als het begin van een gesprek dat iemand met de juiste kwalificaties moet afmaken.

## Waarom dit specifiek meer betekent voor AI-native oprichters

Oprichters die met AI-tools bouwen, bouwen per definitie vaak dingen die ze een paar jaar geleden niet alleen hadden kunnen bouwen — wat op zich echt goed is. Maar de tools die het bouwen toegankelijk maakten, maakten beveiliging niet ook leesbaar. De interface die u vertelt "versleuteld" laat u de versleuteling niet zien. De tool die "auth afhandelt" laat u niet zien wat er gebeurt als een token gestolen wordt. Het vertrouwen dat de interface uitstraalt en de daadwerkelijke staat van het systeem eronder zijn slechts losjes met elkaar verbonden, en oprichters zonder technische achtergrond hebben geen ingebouwde manier om die kloof aan te voelen.

Dat is geen argument tegen het bouwen met AI-tools. Het is een argument om "er staat dat het veilig is" en "het is daadwerkelijk veilig" te behandelen als twee verschillende claims die twee verschillende soorten verificatie nodig hebben — één van de tool, één van iemand die gekwalificeerd is om het te controleren.

Onze technici, werkend vanuit Ho Chi Minh-stad samen met collega's in Amsterdam en Singapore, besteden een aanzienlijk deel van hun tijd aan precies dit soort vertaalwerk — het omzetten van "er staat dat het veilig is" naar een specifieke, gecontroleerde lijst van wat daadwerkelijk waar is. LaunchStudio brengt Manifera's enterprise-grade engineeringstandaard, verfijnd over meer dan 160 opgeleverde projecten, naar dat vertaalwerk. Weet u niet zeker in welke categorie uw eigen product valt, dan kunt u [ons de link naar uw prototype sturen voor een gratis beoordeling van waar het staat](https://launchstudio.eu/en/#contact).

## Echt voorbeeld

### Een AI-native oprichter in actie: de zin die de helft betekende van wat Julia dacht

Julia Mertens had KliniekAfspraak gebouwd om een klein netwerk van klinieken patiëntafspraken te laten beheren zonder gejongleer met telefoontjes en papieren agenda's. De interface van Lovable stelde haar vroeg gerust dat gegevens versleuteld waren — een zin die ze, redelijkerwijs, opvatte als groen licht om verder te gaan met het onboarden van echte klinieken en echte patiëntendossiers.

Toen LaunchStudio het project beoordeelde voorafgaand aan die onboarding, kwam het onderscheid meteen naar boven: de versleuteling waar Julia over verteld was, dekte alleen gegevens tijdens transport. Zodra afspraakgegevens van patiënten de database bereikten, lagen ze daar onversleuteld — leesbaar voor iedereen met directe databasetoegang, of dat nu via een verkeerd geconfigureerde integratie was, een gecompromitteerde inlogcode, of gewoon een over het hoofd geziene toestemmingsinstelling. Voor een systeem dat zorgafspraakgegevens verwerkt, was die lacune geen kleine technische voetnoot.

De technici van Manifera implementeerden versleuteling in rust in de hele database, beoordeelden per kliniek de toegangsrechten, en gaven Julia een samenvatting in gewone taal van precies wat er nu beschermd was en hoe — het soort specifiek antwoord dat "het is veilig" nooit eerder had gegeven.

**Resultaat:** KliniekAfspraak verwerkt patiëntgegevens nu met versleuteling in beide fasen, en Julia heeft een schriftelijke uitleg die ze aan elke IT-contactpersoon van een kliniek kan overhandigen die ernaar vraagt.

> *"Ik wist niet dat er een verschil was tot iemand het me uitlegde. Nu is het het eerste wat ik vraag bij alles wat ik bouw."*
> — **Julia Mertens, oprichter, KliniekAfspraak (Renkum)**

**Kosten en tijdlijn:** € 1.100 (implementatie versleuteling in rust en toegangsbeoordeling) — voltooid in 8 werkdagen.

---

## Veelgestelde vragen

### Wat is het praktische verschil tussen versleuteling tijdens transport en versleuteling in rust?

Versleuteling tijdens transport beschermt gegevens terwijl ze zich verplaatsen tussen het apparaat van een gebruiker en de server, doorgaans via HTTPS. Versleuteling in rust beschermt gegevens zodra ze zijn opgeslagen in de database, zodat ze onleesbaar blijven, zelfs als iemand directe toegang krijgt tot de opslag zelf.

### Waarom zou een AI-codeertool maar één type versleuteling noemen?

Het is niet noodzakelijk opzettelijk misleidend — de tool kan versleuteling tijdens transport standaard implementeren via gangbare webprotocollen, terwijl versleuteling in rust een extra, bewuste configuratiestap vereist die niet altijd automatisch is inbegrepen.

### Hoe kan een niet-technische oprichter beveiligingsclaims verifiëren zonder te leren programmeren?

Door specifieke, afgebakende vragen te stellen, zoals of gegevens versleuteld zijn in rust, of wachtwoorden gehasht zijn, en of de gegevens van de ene gebruiker correct zijn afgeschermd van die van een andere, en een gekwalificeerde engineer te vragen elke vraag rechtstreeks te beantwoorden in plaats van een algemene geruststelling te accepteren.

### Behandelt het team van Manifera dit soort reviews voor de zorg of andere gevoelige gegevens?

Ja, de technici van Manifera in Amsterdam, Singapore en Ho Chi Minh-stad beoordelen regelmatig gegevensverwerking voor producten die gevoelige informatie beheren, inclusief zorggerelateerde tools zoals afspraak- en patiëntbeheersystemen.

### Is dit soort versleutelingslacune gebruikelijk in door AI gegenereerde prototypes?

Het komt vaak genoeg voor om een van de meest voorkomende bevindingen te zijn bij vroege reviews, grotendeels omdat versleuteling in rust een expliciete installatiestap vereist die een snel bewegende prototypebuild gemakkelijk kan overslaan.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "What's the practical difference between encryption in transit and encryption at rest?", "acceptedAnswer": { "@type": "Answer", "text": "Encryption in transit protects data while it moves between a user's device and the server, typically through HTTPS. Encryption at rest protects data once it's stored in the database, so it stays unreadable even if someone gains direct access to the storage itself." } },
    { "@type": "Question", "name": "Why would an AI coding tool only mention one type of encryption?", "acceptedAnswer": { "@type": "Answer", "text": "It's not necessarily misleading on purpose. The tool may implement transit encryption by default through standard web protocols, while encryption at rest requires an additional, deliberate configuration step that isn't always included automatically." } },
    { "@type": "Question", "name": "How can a non-technical founder verify security claims without learning to code?", "acceptedAnswer": { "@type": "Answer", "text": "By asking specific, narrow questions, like whether data is encrypted at rest, whether passwords are hashed, and whether one user's data is properly isolated from another's, and asking a qualified engineer to answer each one directly rather than accepting a general reassurance." } },
    { "@type": "Question", "name": "Does Manifera's team handle this kind of review for healthcare or other sensitive data products?", "acceptedAnswer": { "@type": "Answer", "text": "Yes, Manifera's engineers across Amsterdam, Singapore, and Ho Chi Minh City regularly review data handling for products managing sensitive information, including healthcare-adjacent tools like appointment and patient management systems." } },
    { "@type": "Question", "name": "Is this kind of encryption gap common in AI-generated prototypes?", "acceptedAnswer": { "@type": "Answer", "text": "It's common enough to be one of the most frequent findings in early-stage reviews, largely because encryption at rest requires an explicit setup step that a fast-moving prototype build can easily skip." } }
  ]
}
</script>
