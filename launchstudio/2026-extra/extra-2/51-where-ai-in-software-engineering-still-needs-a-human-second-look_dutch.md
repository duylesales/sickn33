---
Titel: "Waar AI in software-engineering nog steeds een menselijke tweede blik nodig heeft"
Trefwoorden: ai in software engineering, ai software engineering, ai coding, LaunchStudio, Manifera
Koperfase: Overweging
Doelgroep: Technische solo-oprichter / Indie Hacker
---

# Waar AI in software-engineering nog steeds een menselijke tweede blik nodig heeft

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Waar AI in software-engineering nog steeds een menselijke tweede blik nodig heeft",
  "description": "Een technische verdieping in verouderde algortimen voor wachtwoord-hashing die stilletjes door een AI-coderingsassistent zijn gegenereerd.",
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
  "datePublished": "2026-08-02",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://launchstudio.eu/nl/blog/where-ai-in-software-engineering-still-needs-a-human-second-look"
  }
}
</script>

AI in software-engineering is opmerkelijk goed geworden in het snel produceren van code die herkenbare, veelvoorkomende patronen volgt – inclusief patronen die ooit de standaardpraktijk waren, maar sindsdien zijn vervangen door betere alternatieven. Een implementatie voor het hashen van wachtwoorden is een specifieke, concrete plek waar dit verschijnt: technisch functioneel, technisch "het wachtwoord hashend", en technisch een algoritme gebruikend waar de beveiligingscommunity al jaren geleden afstand van heeft genomen.

## Waarom niet alle hash-algoritmen dezelfde bescherming bieden

Het hashen van een wachtwoord, in plaats van het opslaan in platte tekst, is een oprecht correcte en belangrijke praktijk. Maar niet alle hash-algoritmen bieden gelijke bescherming tegen moderne kraaktechnieken. Algoritmen die decennia geleden zijn ontworpen voor algemene snelheid, kunnen extreem snel worden berekend door een aanvaller met moderne hardware. Dit maakt een gestolen hash aanzienlijk gemakkelijker te herleiden dan een hash geproduceerd door een algoritme dat specifiek ontworpen is om traag en bronintensief te zijn.

## Waarom een AI-tool naar een verouderd algoritme kan grijpen

Trainingsdata weerspiegelt code die over vele jaren is geschreven, inclusief een aanzienlijke hoeveelheid oudere code die algoritmen gebruikt die redelijke keuzes waren op het moment dat ze geschreven werden. Zonder specifieke instructies heeft een AI-tool geen ingebouwde voorkeur die het wegleidt van een patroon dat frequent verschijnt en historisch normaal was.

## Waarom deze specifieke kloof onzichtbaar is in elke functionele test

Een wachtwoord dat gehashed is met een verouderd algoritme hasht nog steeds correct, staat nog steeds correcte inlogverificatie toe, en slaagt voor elke functionele test. De zwakheid wordt pas relevant in het geval van een database-inbreuk, wanneer het specifieke algoritme bepaalt hoe snel een aanvaller de gestolen hashes kan herleiden.

## Waarom "het is gehashed, dus het is prima" een incomplete aanname is

Oprichters zonder beveiligingsachtergrond associëren "gehashed" redelijkerwijs met "veilig", aangezien hashen inderdaad dramatisch veiliger is dan opslag in platte tekst. Maar het specifieke algoritme maakt nog steeds aanzienlijk uit.

## Wat het op de juiste manier upgraden hiervan inhoudt

Een correcte herstelling vervangt een verouderd hash-algoritme door een modern, speciaal gebouwd algoritme (zoals bcrypt, scrypt, of Argon2id), en migreert alle bestaande opgeslagen hashes zorgvuldig zonder dat gebruikers verstoord worden door verplicht hun wachtwoord te herstellen. [LaunchStudio](https://launchstudio.eu/nl/) controleert op exact dit patroon als onderdeel van haar beoordeling van authenticatiebeveiliging, ondersteund door Manifera's 11+ jaar ervaring met moderne cryptografische praktijken.

Manifera's beoordelingen van cryptografie en authenticatie worden uitgevoerd door het engineeringteam in het ontwikkelingscentrum in Ho Chi Minh-stad aan de Pho Quang-straat, gecoördineerd met het hoofdkantoor in Amsterdam aan de Herengracht 420.

[Praat met een ingenieur die met AI gegenereerde code begrijpt](https://launchstudio.eu/nl/#contact).

## Een Zelfcontrole van Tien Minuten Vóórdat U een Volledige Beoordeling Boekt

De meeste oprichters kunnen hun eigen cryptografie niet zelfstandig auditeren, maar er is een snelle, praktische manier om in elk geval te weten welke gerichte vraag u moet stellen. Open de authenticatiecode van uw project, of vraag het uw AI-codeerassistent rechtstreeks, en zoek naar de specifieke functie of pakketnaam die de opslag van wachtwoorden afhandelt.

**Hoe een moderne implementatie er doorgaans uitziet**

- Verwijzingen naar `bcrypt`, `argon2`, `scrypt` of `pbkdf2` — dit zijn moderne, trage hash-algoritmen die specifiek zijn ontworpen voor wachtwoordopslag en die elk aanzienlijke rekenkracht vereisen per poging, precies om grootschalige geautomatiseerde aanvallen te vertragen.
- Een expliciete configuratie voor 'werklast' of 'moeilijkheidsgraad' — een getal (zoals een bcrypt-cost factor van minimaal 10 tot 12) dat bepaalt hoeveel rekenwerk nodig is om elke hash te berekenen, waardoor de beveiliging in de loop van de tijd kan worden opgeschaald naarmate hardware sneller wordt.
- Automatische 'salting' per wachtwoord — moderne bibliotheken genereren standaard automatisch een unieke willekeurige salt voor elk wachtwoord, waardoor twee gebruikers met exact hetzelfde wachtwoord toch volstrekt verschillende opgeslagen hashwaarden in de database krijgen.

**Waarschuwingssignalen die onmiddellijke aandacht vereisen**

- Functies zoals `md5()`, `sha1()`, `sha256()` of `sha512()` die rechtstreeks op het wachtwoord worden aangeroepen zonder trage hash-functie of unieke salt — dit zijn snelle cryptografische algoritmen die uitstekend zijn voor het verifiëren van bestandsintegriteit, maar volstrekt ongeschikt voor wachtwoorden omdat moderne grafische kaarten (GPU's) miljarden combinaties per seconde kunnen berekenen.
- Wachtwoorden die in platte tekst worden opgeslagen — hoewel dit zeldzaam is bij gevestigde auth-bibliotheken, kan een zelfgeschreven registratiestroom in een vroeg prototype wachtwoorden per ongeluk rechtstreeks in een ongehashte kolom opslaan.

Deze controle van tien minuten vertelt u niet of uw volledige authenticatiestroom vlekkeloos is ingericht, maar het beantwoordt wel direct de meest kritieke vraag over de bescherming van de inloggegevens van uw gebruikers.

## Echt voorbeeld

### Een AI-native oprichter in actie: Het hash-algoritme dat een decennium achterliep

Twan, een voormalig bruiloftsfotograaf die oprichter werd in Barneveld, bouwde FotoBoeking, een AI-ondersteund platform voor het boeken van fotostudio's gebouwd met Cursor, dat klantaccounts en boekingsgeschiedenis opslaat achter een standaard inlog.

Een vriend die fotograaf is met een baan in cybersecurity bekeek FotoBoeking's code uit professionele nieuwsgierigheid en opmerkte dat de wachtwoord-hashing-implementatie een algoritme gebruikte (zoals ongezouten MD5 of SHA-1) dat lang als onvoldoende werd beschouwd. LaunchStudio's vervolgbeoordeling bevestigde dat het algoritme functioneel correct werkte, maar betekenisvol zwakkere bescherming bood tegen een potentiële toekomstige database-inbreuk.

**Resultaat:** LaunchStudio upgrade de wachtwoord-hashing van FotoBoeking naar een modern algoritme en implementeerde een veilig migratiepad voor bestaande accounts. Dit sloot de kloof zonder dat er verplichte wachtwoord-resets nodig waren voor huidige gebruikers.

> *"Elke inlog werkte de hele tijd perfect, dus er was oprecht niets dat suggereerde dat er iets mis was. Er was een vriend voor nodig die toevallig exact wist waar hij naar moest kijken om het überhaupt op te merken."*
> — **Twan Meijer, Oprichter, FotoBoeking (Barneveld)**

**Kosten en tijdlijn:** € 2.100 (upgrade van wachtwoord-hashing en veilige accountmigratie) — voltooid in 7 werkdagen.

---

## Veelgestelde vragen

### Zou een cryptografiespecialist het gebruik van verouderde hash-algoritmen beschouwen als een urgent risico?

Ja, zeer ernstig — verouderde algoritmen zoals MD5 of enkelvoudige SHA-hashes kunnen met moderne GPU-hardware miljarden keren per seconde worden berekend. Als een database met dergelijke hashes ooit uitlekt, kunnen de originele wachtwoorden van vrijwel alle gebruikers binnen enkele uren worden gekraakt.

### Komt dit probleem alleen voor bij zelfgebouwde authenticatie, of ook bij bekende auth-providers?

Vrijwel uitsluitend bij zelfgebouwde authenticatie of verouderde code-voorbeelden die door een AI-tool zijn gegenereerd. Gevestigde authenticatiediensten (zoals Supabase Auth, Firebase of Auth0) gebruiken standaard moderne en veilige algoritmen zoals bcrypt of argon2.

### Hoe houdt het engineeringteam van Manifera gelijke tred met de nieuwste cryptografische richtlijnen?

Door strikt de actuele standaarden van internationale beveiligingsautoriteiten zoals NIST en OWASP te hanteren. Dit waarborgt dat software altijd gebruikmaakt van up-to-date, trage hash-functies met adequate salt- en cost-factoren.

### Hoe sluit dit aan bij de stelling van Herre Roelevink dat 'het werkt' iets heel anders is dan 'het is best practice'?

Een inlogsysteem dat werkt met MD5-hashes valideert wachtwoorden razendsnel en laat gebruikers vlekkeloos inloggen — functioneel werkt het perfect. Technisch en beveiligingsmatig is het echter een tikkende tijdbom. Het signaleren van dat verschil vereist senior technische expertise.

### Moet een oprichter zijn AI-assistent expliciet vragen om een specifiek hash-algoritme zoals Argon2 of bcrypt?

Ja, dat is een uitstekende gerichte instructie die voorkomt dat het model terugvalt op eenvoudigere of verouderde methoden. Daarnaast blijft het essentieel om te laten verifiëren of de bibliotheek correct is geconfigureerd met een voldoende hoge cost factor.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Zou een cryptografiespecialist het gebruik van verouderde hash-algoritmen beschouwen als een urgent risico?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ja, zeer ernstig — verouderde algoritmen zoals MD5 of enkelvoudige SHA-hashes kunnen met moderne GPU-hardware miljarden keren per seconde worden berekend. Als een database met dergelijke hashes ooit uitlekt, kunnen de originele wachtwoorden van vrijwel alle gebruikers binnen enkele uren worden gekraakt."
      }
    },
    {
      "@type": "Question",
      "name": "Komt dit probleem alleen voor bij zelfgebouwde authenticatie, of ook bij bekende auth-providers?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Vrijwel uitsluitend bij zelfgebouwde authenticatie of verouderde code-voorbeelden die door een AI-tool zijn gegenereerd. Gevestigde authenticatiediensten (zoals Supabase Auth, Firebase of Auth0) gebruiken standaard moderne en veilige algoritmen zoals bcrypt of argon2."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe houdt het engineeringteam van Manifera gelijke tred met de nieuwste cryptografische richtlijnen?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Door strikt de actuele standaarden van internationale beveiligingsautoriteiten zoals NIST en OWASP te hanteren. Dit waarborgt dat software altijd gebruikmaakt van up-to-date, trage hash-functies met adequate salt- en cost-factoren."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe sluit dit aan bij de stelling van Herre Roelevink dat 'het werkt' iets heel anders is dan 'het is best practice'?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Een inlogsysteem dat werkt met MD5-hashes valideert wachtwoorden razendsnel en laat gebruikers vlekkeloos inloggen — functioneel werkt het perfect. Technisch en beveiligingsmatig is het echter een tikkende tijdbom. Het signaleren van dat verschil vereist senior technische expertise."
      }
    },
    {
      "@type": "Question",
      "name": "Moet een oprichter zijn AI-assistent expliciet vragen om een specifiek hash-algoritme zoals Argon2 of bcrypt?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ja, dat is een uitstekende gerichte instructie die voorkomt dat het model terugvalt op eenvoudigere of verouderde methoden. Daarnaast blijft het essentieel om te laten verifiëren of de bibliotheek correct is geconfigureerd met een voldoende hoge cost factor."
      }
    }
  ]
}
</script>
