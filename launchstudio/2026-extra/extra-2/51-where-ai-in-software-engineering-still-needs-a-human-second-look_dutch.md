---
Titel: "Waar AI In Software-Engineering Nog Steeds Een Menselijke Tweede Blik Nodig Heeft"
Trefwoorden: ai in software engineering, ai software engineering, ai coding, LaunchStudio, Manifera
Koperfase: Overweging
Doelgroep: Technische Solo Founder / Indie Hacker
---

# Waar AI In Software-Engineering Nog Steeds Een Menselijke Tweede Blik Nodig Heeft

AI in software-engineering is opmerkelijk goed geworden in het snel produceren van code die herkenbare, gebruikelijke patronen volgt — inclusief patronen die ooit standaardpraktijk waren maar sindsdien overtroffen zijn door betere alternatieven. Een wachtwoord-hashing-implementatie is een specifieke, concrete plek waar dit verschijnt: technisch functioneel, technisch het wachtwoord "hashend," en technisch een algoritme gebruikend waar de beveiligingsgemeenschap jaren geleden van wegging voordat de meeste huidige AI-trainingsdata zelfs samengesteld werd.

## Waarom Niet Alle Hashing-Algoritmes Dezelfde Bescherming Bieden

Een wachtwoord hashen, in plaats van het in platte tekst op te slaan, is een oprecht correcte en belangrijke praktijk — maar niet alle hashing-algoritmes bieden gelijke bescherming tegen moderne kraaktechnieken. Algoritmes ontworpen decennia geleden voor algemene snelheid, in plaats van specifiek voor wachtwoordopslag, kunnen extreem snel berekend worden door een aanvaller met moderne hardware, wat een gestolen hash aanzienlijk makkelijker omkeerbaar maakt dan een geproduceerd door een algoritme specifiek ontworpen om langzaam en doelbewust resource-intensief te zijn.

## Waarom Een AI-Codeertool Naar Een Verouderd Algoritme Zou Kunnen Grijpen

Trainingsdata weerspiegelt code geschreven over vele jaren, inclusief een substantiële hoeveelheid oudere, ooit-gebruikelijke maar nu-verouderde code die algoritmes gebruikt die redelijke keuzes waren toen ze geschreven werden. Zonder een specifieke instructie die een moderne, doelgericht-gebouwde wachtwoord-hashing-algoritme voorkeurt, heeft een codeertool geen bijzondere ingebouwde voorkeur die het wegstuurt van een patroon dat frequent verschijnt en historisch volledig normaal was om te gebruiken.

## Waarom Dit Specifieke Gat Onzichtbaar Is In Elke Functionele Test

Een wachtwoord gehasht met een verouderd algoritme hasht nog steeds correct, staat nog steeds correcte loginverificatie toe, en doorstaat nog steeds elke functionele test die een founder redelijkerwijs zou kunnen draaien — de zwakte wordt alleen relevant in het geval van een databaseinbreuk, wanneer het specifieke gebruikte algoritme bepaalt hoe snel een aanvaller haalbaar de gestolen hashes terug kon keren naar bruikbare wachtwoorden, een scenario dat geen hoeveelheid normale functionele tests ooit simuleert.

## Waarom "Het Is Gehasht, Dus Het Is Prima" Een Begrijpelijke Maar Onvolledige Aanname Is

Founders zonder beveiligingsachtergrond associëren redelijkerwijs "gehasht" met "veilig," aangezien hashen inderdaad dramatisch veiliger is dan platte-tekst-opslag — maar het specifieke gebruikte algoritme doet nog steeds aanzienlijk ertoe, en "gehasht" behandelen als een enkel, uniform beschermingsniveau in plaats van een spectrum van bescherming is een makkelijk, begrijpelijk gat in een verder redelijk beveiligingsinstinct.

## Wat Dit Correct Upgraden Omvat

Een correcte fix vervangt een verouderd hashing-algoritme door een moderne, doelgericht-gebouwde, en migreert zorgvuldig elke bestaande opgeslagen hash zodat gebruikers niet ontwrichtend gedwongen worden hun wachtwoorden te resetten in het proces. [LaunchStudio](https://launchstudio.eu/en/) controleert op precies dit patroon als onderdeel van zijn authenticatiebeveiligingsreview, gesteund door Manifera's 11+ jaar ervaring met moderne cryptografische best practices in productiesystemen.

Manifera's cryptografische en authenticatiereviews worden uitgevoerd door het engineeringteam bij het ontwikkelcentrum in Ho Chi Minh City aan de Pho Quang Street, gecoördineerd met het hoofdkantoor in Amsterdam aan de Herengracht 420.

[Praat met een engineer die AI-gegenereerde code begrijpt](https://launchstudio.eu/en/#contact).

## Echt voorbeeld

### Een AI-native founder in actie: het hashing-algoritme een decennium uit datum

Twan, een voormalig bruiloftsfotograaf die founder werd in Barneveld, bouwde FotoBoeking, een AI-geassisteerd fotostudio-boekingsplatform gebouwd met Cursor, met klantaccounts en boekingsgeschiedenis opgeslagen achter een standaard e-mail-en-wachtwoord-login.

Een fotograafvriend met een cybersecuritydagbaan, die FotoBoekings code reviewde uit professionele nieuwsgierigheid terwijl hij Twan hielp met een ongerelateerde functie, merkte op dat de wachtwoordhashimplementatie een algoritme gebruikte lang beschouwd als ontoereikend voor specifiek wachtwoordopslag, ondanks nog steeds gebruikelijk gezien in algemene codeervoorbeelden. LaunchStudio's vervolgreview bevestigde dat het algoritme correct functioneerde maar betekenisvol zwakkere bescherming bood dan de huidige best practice tegen een potentiële toekomstige databaseinbreuk.

**Resultaat:** LaunchStudio upgradede FotoBoekings wachtwoordhashing naar een modern, doelgericht-gebouwd algoritme en implementeerde een veilig migratiepad voor bestaande accounts, en dicht het gat zonder enige ontwrichtende, gedwongen wachtwoordresets voor huidige gebruikers te vereisen.

> *"Elke login werkte de hele tijd perfect, dus er was oprecht niets dat suggereerde dat er iets mis was. Er was een vriend nodig die toevallig precies wist waarnaar te zoeken, puur door toeval, om het überhaupt op te merken."*
> — **Twan Meijer, Founder, FotoBoeking (Barneveld)**

**Kosten & tijdlijn:** €2.100 (upgrade wachtwoordhashing en veilige accountmigratie) — voltooid in 7 werkdagen.

---

## Veelgestelde vragen

### Zou een cryptografiespecialist dit een urgent risico beschouwen, of een lagere-prioriteit-best-practice-verbetering?

Het hangt af van context, maar over het algemeen behandeld als een betekenisvolle, de moeite waarde fix in plaats van een puur cosmetische verbetering — het risico wordt specifiek alleen gerealiseerd in het geval van een databaseinbreuk, maar gegeven dat inbreuken regelmatig gebeuren over de industrie, is een modern, doelgericht-gebouwd algoritme gebruiken standaard, aanbevolen praktijk in plaats van een optionele extra.

### Raakt dit gat alleen aangepast gebouwde authenticatie, of kan het ook gebeuren met gevestigde authenticatieproviders?

Het is aanzienlijk minder waarschijnlijk met gevestigde providers zoals Auth0 of Supabase Auth, die doorgaans standaard moderne, passende algoritmes gebruiken — het risico is specifiek hoger in aangepast gebouwde authenticatielogica, waar de AI-codeertool de hashingimplementatie direct genereert in plaats van die verantwoordelijkheid te delegeren aan een toegewijde, beveiligingsgerichte provider.

### Manifera's engineering is bijgebleven met cryptografische best practices over vele klantopdrachten — doet die continuïteit ertoe voor het vangen van specifiek verouderde algoritmes?

Ja, direct — cryptografische best practices evolueren na verloop van tijd, en engineers hebben die actief op de hoogte blijven van die veranderingen over doorlopend klantwerk is precies wat een review toestaat een verouderd patroon als verouderd te herkennen, in plaats van simpelweg aan te nemen dat elke hashingimplementatie gelijkwaardig veilig is.

### Herre Roelevink heeft gesproken over de waarde van ervaren engineeringoordeel specifiek op gebieden waar "het werkt" niet hetzelfde is als "het is huidige best practice" — past dit geval bij die beschrijving?

Heel goed — FotoBoekings login werkte vlekkeloos volgens elke functionele maatstaf, en het gat was puur een vraag of de onderliggende techniek huidige best practice weerspiegelde in plaats van historische conventie, precies het oordeelgebaseerde onderscheid dat Roelevinks commentaar op ervaren engineeringtoezicht consistent benadrukt.

### Zou een founder specifiek hun AI-codeertool moeten vragen een modern wachtwoordhashingalgoritme bij naam te gebruiken?

Het is een redelijk, specifiek verzoek dat kan helpen de gegenereerde code in de juiste richting te sturen, hoewel bevestigen dat de tool het gevraagde algoritme daadwerkelijk correct implementeerde, en dat geen ander deel van het authenticatiesysteem afhangt van een verouderd patroon, nog steeds baat heeft bij een onafhankelijke technische review in plaats van alleen op het verzoek te vertrouwen.
