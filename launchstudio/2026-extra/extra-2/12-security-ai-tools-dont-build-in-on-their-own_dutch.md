---
Titel: "Beveiliging die AI-tools niet uit zichzelf inbouwen"
Trefwoorden: security ai, ai secure, ai coding, LaunchStudio, Manifera
Koperfase: Overweging
Doelgroep: Technische solo-oprichter / Indie Hacker
---

# Beveiliging die AI-tools niet uit zichzelf inbouwen

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Beveiliging die AI-tools niet uit zichzelf inbouwen",
  "description": "Er is een specifieke ironie in een beveiligingsmonitoringsproduct dat zelf wachtwoorden in platte tekst opslaat. Een technische verdieping.",
  "author": {
    "@type": "Organization",
    "name": "LaunchStudio",
    "url": "https://launchstudio.eu/en/"
  },
  "publisher": {
    "@type": "Organization",
    "name": "Manifera",
    "url": "https://www.manifera.com"
  },
  "datePublished": "2026-07-23",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://launchstudio.eu/en/blog/security-ai-tools-dont-build-in-on-their-own"
  }
}
</script>

Er is een specifieke, bijna ongemakkelijke ironie die vaker naar boven komt dan oprichters verwachten: een product waarvan het gehele uitgangspunt is om andere bedrijven te helpen hun eigen beveiliging te monitoren, kan zelf gebouwd zijn met een opzichtige beveiligingskloof. De AI-coderingsassistent die het bouwde heeft namelijk geen specifiek bewustzijn van de missie van het product – het bouwt simpelweg wat beschreven is, op dezelfde manier zoals het dat zou doen voor elk ander soort app.

## Waarom domein zich niet vertaalt naar implementatie

Het bouwen van een op beveiliging gericht product vereist dat een oprichter zorgvuldig nadenkt over beveiliging als een functie – welke dreigingen te detecteren, welke waarschuwingen te verzenden, welke dashboards te tonen. Het vereist niet automatisch, of produceert niet, zorgvuldig nadenken over beveiliging als een eigenschap van de codebase zelf – hoe wachtwoorden worden opgeslagen, hoe sessies worden beheerd, hoe de onderliggende infrastructuur wordt beschermd. Dit zijn twee volledig afzonderlijke zorgen die toevallig het woord "beveiliging" delen. En een AI-coderingsassistent pakt de eerste aan omdat het erom gevraagd werd, zonder de tweede aan te pakken omdat het dat niet werd.

## De specifieke tekstboekfout: Plattekst wachtwoord-terugval (Plaintext Password Fallback)

Een van de oudste, meest bekende anti-patronen in beveiliging is het opslaan van gebruikerswachtwoorden in platte tekst (plaintext), of het terugvallen op plattekst-opslag wanneer een hashing-bibliotheek niet goed is geconfigureerd. Met AI gegenereerde authenticatiecode bevat soms een werkende hashing-implementatie voor het primaire aanmeldingspad, terwijl een secundair pad – een door een beheerder aangemaakt account, een in bulk geïmporteerde lijst, de voltooiing van het opnieuw instellen van een wachtwoord – terugvalt op het rechtstreeks opslaan van het nieuwe wachtwoord, ongehasht, omdat dat secundaire pad niet zo grondig gespecificeerd was in de oorspronkelijke prompt.

## Waarom een werkende inlog dit niet uitsluit

Het met succes inloggen bewijst alleen dat wat opgeslagen is overeenkomt met wat vergeleken wordt tijdens de inlog – het zegt niets over de indeling waarin die waarde is opgeslagen. Een plattekst-wachtwoord en een op de juiste manier gehasht wachtwoord kunnen beide een gebruiker correct authenticeerbaar maken tijdens normaal gebruik; het verschil wordt pas catastrofaal in het geval van een inbreuk op de database, wat het dagelijkse testen van een oprichter nooit zal simuleren.

## Waarom deze specifieke kloof de neiging heeft zich te verbergen in secundaire paden

Oprichters en AI-tools hebben beide de neiging om de aandacht te richten op de primaire, meest gebruikte stroom – het aanmeldingsformulier dat een nieuwe gebruiker als eerste ziet. Secundaire paden voor het aanmaken van accounts, later toegevoegd of minder zorgvuldig gespecificeerd, zijn exact waar inconsistente afhandeling binnensluipt. Elk nieuw pad is namelijk effectief een verse implementatiebeslissing in plaats van een uitbreiding van een al beoordeelde beslissing.

Dit patroon stapelt zich over de tijd op: het primaire aanmeldingsformulier wordt typisch herhaaldelijk getest gedurende weken van ontwikkeling, waarbij de meest duidelijke problemen worden opgevangen door loutere herhaling. Een secundair pad dat één keer gebouwd is, één keer getest is, en nooit meer heroverwogen wordt, krijgt niets van die opgebouwde zorgvuldigheid. Tegen de tijd dat een product drie of vier manieren heeft om een account aan te maken, kan de kloof tussen hoe zorgvuldig elk pad werd beoordeeld enorm zijn. Dit geldt zelfs als een gebruiker of auditor die naar het voltooide product kijkt geen manier heeft om die geschiedenis te zien.

## Wat een oprechte herstelling vereist

Het sluiten van deze kloof betekent het auditeren van elk enkel pad dat een opgeslagen wachtwoord aanmaakt of bijwerkt – en niet alleen het hoofdpad – en bevestigen dat elk pad dezelfde correcte hashing conequent toepast, en vervolgens eventuele bestaande in platte tekst opgeslagen waarden veilig migreert. [LaunchStudio](https://launchstudio.eu/en/) voert exact dit soort authenticatie-audit uit over het gehele pad, ondersteund door Manifera's 11+ jaar op beveiliging gefocuste engineering-ervaring. Dit omvat werk gerelateerd aan cybersecurity-onderzoek via CEO Herre Roelevink's eerdere achtergrond bij CFLW Cyber Strategies.

Manifera's authenticatie-audits worden uitgevoerd door het engineeringteam in het ontwikkelingscentrum in Ho Chi Minh-stad aan de Pho Quang-straat, met klantrelaties beheerd vanuit het hoofdkantoor in Amsterdam aan de Herengracht 420.

[Praat met een ingenieur die met AI gegenereerde code begrijpt](https://launchstudio.eu/en/#contact).

## Een kader om elk wachtwoord-afhandelingspad zelf te auditeren

Het sluiten van deze kloof vereist geen beveiligingscertificering – het vereist het systematisch wantrouwen van elk pad dat een wachtwoord raakt, inclusief paden die te klein lijken om er toe te doen. De meeste oprichters kunnen hun eigen codebase hier in minder dan een uur doorheen lopen als ze weten waar ze naar moeten kijken.

**Som elk proces op dat een opgeslagen wachtwoord aanmaakt of wijzigt**

- Het primaire aanmeldingsformulier
- Door de beheerder aangemaakt of door de beheerder ondersteund aanmaken van accounts
- In bulk importeren of op CSV gebaseerd aanmaken van gebruikers
- Voltooiing van het opnieuw instellen van het wachtwoord
- "Wachtwoord wijzigen" van binnenuit een geauthenticeerde accountinstellingenpagina
- Elke logica voor het samenvoegen of migreren van accounts die na de oorspronkelijke build werd toegevoegd

**Controleer de opgeslagen waarde rechtstreeks, niet het resultaat van de inlog**

Een geslaagde inlog bewijst niets over de opslagindeling – de enige betrouwbare controle is het kijken naar het daadwerkelijke databaserecord nadat elk pad draait en bevestigen dat het een gehashte waarde is (typisch een lange tekenreeks die begint met zoiets als `$2b$` voor bcrypt), en niet het plattekst-wachtwoord zelf. Dit is een controle van vijf minuten per pad, en het is de meest directe manier om deze specifieke kloof op te vangen.

**Let op deze veelvoorkomende terugval-triggers**

1. Een secundair pad geïmplementeerd door het kopiëren en plakken van de code van het hoofdpad, en vervolgens genoeg gewijzigd dat de hashing-aanroep per ongeluk werd verwijderd
2. Een beheerders-tool later gebouwd, onder tijdsdruk, die rechtstreeks naar de database schrijft zonder te routeren via dezelfde authenticatiedienst die de hoofdapp gebruikt
3. Een "snelle herstelling" voor een ondersteuningsverzoek — een oprichter die handmatig het wachtwoord van een gebruiker herstelt door de database rechtstreeks in platte tekst zuiver te bewerken, met de bedoeling het "binnen een minuut" te hashen en er nooit meer naar terug te keren
4. Een migratiescript dat gebruikers tussen systemen verplaatst en de indeling van het bronsysteem behoudt, waardoor plattekst stilletjes wordt meegenomen

**Plan de opschoning voor alles wat al getroffen is**

Als een audit bestaande in platte tekst opgeslagen wachtwoorden vindt, is de herstelling niet alleen het voortaan hashen van de waarden – elke getroffen gebruiker moet zijn wachtwoord laten roteren. Een plattekst-waarde die al in een database zat, zelfs kortstondig, moet namelijk worden behandeld als gecompromitteerd op dezelfde manier zoals een blootgestelde API-sleutel dat zou worden. Een verplichte e-mail voor het opnieuw instellen van het wachtwoord aan getroffen gebruikers, met een korte, eerlijke uitleg, is de standaard, verdedigbare manier om dit af te handelen in plaats van het stilletjes opnieuw hashen van de bestaande waarde.

**Maak dit systematisch, niet alleen gedocumenteerd**

Waar mogelijk, routeer elke operatie voor het aanmaken van accounts en het wijzigen van wachtwoorden via één enkele, gedeelde authenticatiefunctie in plaats van het opnieuw implementeren van wachtwoordafhandeling in elk nieuw pad. Dit herstelt niet alleen de kloof van vandaag, het voorkomt structureel dat een vijfde onontdekt pad hetzelfde probleem volgend kwartaal herintroduceert.

## Echt voorbeeld

### Een AI-native oprichter in actie: De monitoring-tool die zichzelf niet monitorde

Iris, een voormalig IT-compliance-officer die oprichter werd in Apeldoorn, bouwde WachtPost, een AI-ondersteund beveiligingswaarschuwings-monitoringdashboard voor kleine bedrijven gebouwd met Cursor. Ze bood zowel self-service aanmelding als een door de beheerder ondersteund onboardingpad voor minder technische klanten.

Tijdens het voorbereiden van een beveiligingsaudit door de klant van WachtPost als leverancier, vroeg Iris's technische adviseur om te zien hoe wachtwoorden werden gehasht. Het self-service aanmeldingspad was correct gehasht – maar accounts aangemaakt via door de beheerder ondersteunde onboarding, later toegevoegd in de ontwikkeling, sloegen het door de klant gekozen wachtwoord rechtstreeks op in platte tekst.

**Resultaat:** LaunchStudio auditeerde elk pad voor het aanmaken van accounts in WachtPost, paste consistente hashing toe over alle paden, en migreerde veilig de getroffen in platte tekst opgeslagen wachtwoorden. Dit sloot de inconsistentie voordat het de audit van de klant bereikte.

> *"Het gehele punt van WachtPost is het vertellen aan andere bedrijven over exact dit soort kloven. Het vinden ervan in mijn eigen product voordat een klant dat deed was een oprecht nederig makend moment."*
> — **Iris van Dongen, Oprichter, WachtPost (Apeldoorn)**

**Kosten en tijdlijn:** € 2.600 (volledige authenticatiepad-audit en wachtwoordmigratie) — voltooid in 9 werkdagen.

---

## Veelgestelde vragen

### Zou een ervaren beveiligingsauditor verbaasd zijn dat een op beveiliging gericht product deze specifieke kloof had?

Niet in het bijzonder – auditors verwachten specifiek elk pad voor het aanmaken van accounts onafhankelijk te controleren, precies omdat secundaire paden zo gebruikelijk inconsistent zijn met het hoofdpad.

### Is het opslaan van wachtwoorden in platte tekst nog steeds een veelvoorkomend probleem?

Het blijft veelvoorkomend specifiek in secundaire of later toegevoegde paden, zelfs in voor het overige goed gebouwde producten.

### Vormt een cybersecurity-achtergrond via CFLW de beoordelingsmethodologie?

Ja, het vormt de methodologie rechtstreeks – het behandelen van elk pad voor het aanmaken van accounts als onafhankelijk verdacht totdat het geverifieerd is, is een gewoonte die voortvloeit uit toegewijde cybersecurity-praktijk.

### Vereist dit soort audit toegang tot de live gebruikersdatabase van een oprichter?

Het kan typisch beoordeeld worden door de codepaden zelf te beoordelen zonder dat er rechtstreekse toegang tot live klantgegevens nodig is.

### Moet een oprichter aannemen dat zijn AI-tool overal hetzelfde authenticatiepatroon gebruikte?

Nee – zoals WachtPost's case rechtstreeks toont, biedt een correct geïmplementeerde primaire stroom geen garantie over secundaire of later toegevoegde stromen.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Zouden ervaren auditors verbaasd zijn dat een beveiligingsproduct deze kloof had?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Niet in het bijzonder — auditors verwachten elk pad voor het aanmaken van accounts onafhankelijk te controleren."
      }
    },
    {
      "@type": "Question",
      "name": "Is opslag van wachtwoorden in platte tekst nog steeds veelvoorkomend?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ja, vooral in secundaire paden, aangezien een nieuw codepad niet automatisch de lessen erft."
      }
    },
    {
      "@type": "Question",
      "name": "Vormt een cybersecurity-achtergrond de beoordelingsmethodologie?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ja, het behandelen van elk accountpad als verdacht totdat het geverifieerd is komt uit die praktijk."
      }
    },
    {
      "@type": "Question",
      "name": "Vereist dit soort audit toegang tot live klantgegevens?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Nee, het kan beoordeeld worden door de codepaden te bekijken zonder directe toegang tot live data."
      }
    },
    {
      "@type": "Question",
      "name": "Moet een oprichter aannemen dat hetzelfde patroon overal gebruikt is?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Nee — een correcte primaire stroom biedt geen garantie over later toegevoegde secundaire stromen."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe moeten reeds getroffen accounts met plattekst-wachtwoorden behandeld worden?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ze moeten gedwongen roteren via een reset-e-mail, aangezien blootgestelde plattekst als gecompromitteerd geldt."
      }
    }
  ]
}
</script>
