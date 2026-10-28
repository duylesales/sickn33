---
Titel: "Beveiliging van AI-Apps: Wachtwoordherstel en Magic Links Goed Inrichten"
Trefwoorden: ai gegenereerde app beveiliging, wachtwoordherstel beveiliging, magic link inloggen, accountovername, cursor authenticatie, LaunchStudio, Manifera
Koperfase: Overweging
Doelgroep: Technische Solo-oprichters / Indie Hackers
---

# Beveiliging van AI-Apps: Wachtwoordherstel en Magic Links Goed Inrichten

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Beveiliging van AI-Apps: Wachtwoordherstel en Magic Links Goed Inrichten",
  "description": "Wachtwoordherstel en magic links vormen de geruisloze achterdeur in de beveiliging van AI-gebouwde apps. Dit artikel behandelt token-entropie, verlooptermijnen, eenmalig gebruik, host header poisoning, enumeratie, sessie-invalidatie en e-mailbezorging - inclusief checklist voor technische oprichters.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-12-01",
  "inLanguage": "nl-NL",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/ai-generated-app-security-password-resets-and-magic-links-done-right" }
}
</script>

Aanvallers breken zelden je inlogformulier. Ze gaan eromheen. De flow voor wachtwoordherstel - en zijn neefje, de magic link - is een tweede weg naar elk account, en binnen de beveiliging van AI-gegenereerde apps is het een van de minst onderzochte delen van de codebase. Het inlogscherm krijgt aandacht omdat iedereen het gebruikt. De herstelflow wordt zelden gebruikt, één keer getest en daarna vergeten, en dat is precies wat hem aantrekkelijk maakt.

Draait je authenticatie volledig op een volwassen aanbieder zoals Supabase Auth, Auth0 of Firebase Auth, dan wordt het meeste hiervan voor je geregeld - zolang je het niet in eigen code hebt verpakt. De problemen beginnen als een AI-tool zijn eigen herstellogica genereert, of zijn eigen "wachtwoordloze" login, bovenop die aanbieder.

## Wat een Herstellink Echt Is

Een herstellink is een tijdelijk wachtwoord. Wie hem heeft, kan het account overnemen. Elke eigenschap die voor een wachtwoord telt, telt ook voor het token in die link: hoe moeilijk het te raden is, hoe lang het geldig is, waar het langs reist en of het opnieuw kan worden gebruikt.

## Beveiliging van AI-Gegenereerde Apps: Zeven Fouten in Herstelflows

**1. Raadbare tokens.** Tokens gemaakt met `Math.random()`, tijdstempels, gebruikers-ID's of korte numerieke codes kunnen worden voorspeld of met brute force worden geraden. Tokens moeten uit een cryptografisch veilige randomgenerator komen en lang genoeg zijn - 128 bits of meer.

**2. Geen vervaltijd, of een lange.** Links die dagen of voor altijd werken, maken van elke oude e-mail in iemands inbox een sleutel. Vijftien tot zestig minuten is gebruikelijk voor herstel; magic links zijn vaak korter geldig.

**3. Herbruikbare tokens.** Na een geslaagd herstel hoort het token ongeldig te worden. Veel gegenereerde flows laten het geldig, zodat iedereen die de link later ziet - in een doorgestuurde e-mail, een gedeeld scherm, de browsergeschiedenis - hem opnieuw kan gebruiken.

**4. Tokens opgeslagen als platte tekst.** Slaat de database hersteltokens ongewijzigd op, dan kan iedereen met leestoegang tot die tabel, of een gelekte back-up, accounts met een lopend herstel overnemen. Sla een hash op, zoals je bij een wachtwoord zou doen.

**5. Host header poisoning.** Gegenereerde code bouwt de herstel-URL vaak op uit de host-header van het binnenkomende verzoek. Een aanvaller die voor jouw account een herstel aanvraagt met een vervalste host-header, kan ervoor zorgen dat de e-mail die jij ontvangt naar zijn domein wijst; klik je erop, dan ontvangt hij jouw token. Bouw URL's op vanuit een vaste, geconfigureerde basis-URL.

**6. Enumeratie.** "Geen account gevonden met dat e-mailadres" vertelt een aanvaller welke adressen klant zijn. Reageer altijd met dezelfde melding.

**7. Sessies overleven het herstel.** Herstelt iemand een wachtwoord - vaak omdat hij vermoedt dat zijn account is gecompromitteerd - dan horen bestaande sessies elders te eindigen. AI-gegenereerde flows werken meestal alleen de wachtwoordhash bij.

## Voor Magic Links Gelden Dezelfde Regels, en Nog Eén

Magic links zijn wachtwoordherstel dat als login wordt gebruikt. Alles hierboven geldt, plus een overweging over waar de link wordt geopend. Sommige zakelijke e-mailsystemen en beveiligingsscanners "klikken" links automatisch aan om ze te controleren, waardoor tokens voor eenmalig gebruik kunnen worden verbruikt voordat de gebruiker dat doet. Veelgebruikte oplossingen zijn een bevestigingspagina waarop een knop moet worden ingedrukt om het inloggen af te ronden, of korte eenmalige codes als alternatief.

## Rate Limits en Monitoring

Endpoints voor herstel en magic links hebben rate limits per e-mailadres en per IP nodig, zowel om enumeratie op schaal te voorkomen als om te verhinderen dat je e-mailaanbieder wordt gebruikt om mensen te spammen. Log herstelverzoeken en voltooiingen, en stel meldingen in bij ongebruikelijke pieken.

## E-mailbezorging Is Onderdeel van de Beveiliging

Een herstelmail die in de spam belandt, is een supportticket; een herstelmail die vanaf een niet-geauthenticeerd domein wordt verstuurd, leert gebruikers phishing-lookalikes te vertrouwen. Gebruik een aanbieder van transactionele e-mail, publiceer SPF-, DKIM- en DMARC-records, en houd herstelmails eenvoudig, in je huisstijl en consistent.

## Een Checklist voor Je Codebase

- Tokens uit een veilige randomgenerator, 128+ bits
- Gehasht opgeslagen, met vervaltijd en eenmalig gebruik
- Herstel-URL opgebouwd uit de geconfigureerde basis-URL, nooit uit de host van het verzoek
- Identiek antwoord voor bekende en onbekende e-mailadressen
- Rate limits per e-mailadres en IP
- Alle sessies ingetrokken na herstel; gebruiker per e-mail geïnformeerd
- Magic links beschermd tegen het vooraf aanklikken door scanners
- Transactionele e-mail met geauthenticeerd domein

Het [OWASP Forgot Password Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Forgot_Password_Cheat_Sheet.html) gaat dieper en is kort genoeg om in één keer te lezen.

## Hersteltokens Correct Genereren en Opslaan

Een correcte implementatie van hersteltokens voor de beveiliging van AI-gegenereerde apps is kort, en het waard om te zien:

```typescript
import { randomBytes, createHash } from "crypto";

export function createResetToken() {
  const token = randomBytes(32).toString("base64url");       // naar de gebruiker gestuurd
  const tokenHash = createHash("sha256").update(token).digest("hex"); // opgeslagen
  const expiresAt = new Date(Date.now() + 30 * 60 * 1000);   // 30 minuten
  return { token, tokenHash, expiresAt };
}
```

De database slaat alleen `tokenHash`, `user_id`, `expires_at` en `used_at` op. Klikt de gebruiker op de link, dan hasht de app het ontvangen token, zoekt een overeenkomend, niet-verlopen en ongebruikt record op, markeert het als gebruikt in dezelfde transactie als de wachtwoordwijziging, en trekt andere sessies in. Lekt de database, dan zijn de opgeslagen hashes nutteloos voor een aanvaller; lekt de e-mail na gebruik, dan is het token al verbruikt.

## URL's Veilig Opbouwen

De herstellink moet uit de configuratie worden opgebouwd, nooit uit het binnenkomende verzoek:

```typescript
const base = process.env.APP_BASE_URL; // bijv. https://app.example.nl
const link = `${base}/reset-password?token=${encodeURIComponent(token)}`;
```

Valideer bij het opstarten dat `APP_BASE_URL` is ingesteld en in productie HTTPS gebruikt. Deze ene regel elimineert host header poisoning, een van de elegantere manieren waarop aanvallers hersteltokens stelen.

## Rate Limits op Endpoints voor Herstel en Inloggen

Verstandige limieten voor kleine apps:

| Endpoint | Per e-mailadres | Per IP | Antwoord bij overschrijding |
| --- | --- | --- | --- |
| Herstel / magic link aanvragen | 3–5 per uur | 20 per uur | Dezelfde generieke melding; geen e-mail verstuurd |
| Hersteltoken indienen | 5 pogingen per token | 30 per uur | Token ongeldig maken na de limiet |
| Inloggen | 5–10 mislukte pogingen per 15 min | 50 per 15 min | Tijdelijke blokkade, generieke melding |
| Eenmalige code verifiëren | 5 pogingen per code | 30 per uur | Code ongeldig maken |

Limieten horen op de server te worden afgedwongen, bij voorkeur in een gedeelde opslag zodat ze over serverless instances heen gelden. Log het bereiken van limieten; een piek is vaak het eerste teken van credential stuffing of enumeratie.

## Kiezen tussen Links en Codes

Magic links zijn handig op hetzelfde apparaat; eenmalige codes werken beter als gebruikers hun e-mail op een telefoon lezen en op een laptop inloggen. Veel apps bieden beide. Gebruik voor codes minstens zes cijfers met strikte limieten op pogingen en een korte vervaltijd, of langere alfanumerieke codes; gebruik voor links lange willekeurige tokens. Koppel het token in beide gevallen aan het e-mailadres en, waar mogelijk, aan de browsersessie die het aanvroeg, zodat een elders onderschepte code minder bruikbaar is.

## Accountherstel buiten E-mail om

Verliest een gebruiker de toegang tot zijn e-mail, dan wordt herstel een supportproces - en een doelwit voor social engineering. Leg vooraf vast welk bewijs je accepteert (bijvoorbeeld toegang tot een geverifieerd telefoonnummer, recente betaalgegevens of identiteitsverificatie bij waardevolle accounts), log herstelacties, informeer het oude e-mailadres over de wijziging en hanteer een afkoelperiode vóór gevoelige acties. Bied bij apps met gevoelige data tweestapsverificatie met herstelcodes aan, zodat gebruikers zonder support kunnen herstellen.

## Meldingen die Gebruikers Helpen Aanvallen te Herkennen

Stuur een e-mail als een wachtwoord wordt gewijzigd, een nieuw apparaat inlogt, het e-mailadres wordt gewijzigd of tweestapsverificatie wordt uitgezet. Voeg advies toe voor als "ik dit niet was", met een link om het account te beveiligen. Deze meldingen kosten bijna niets en maken van gebruikers een vroegtijdig waarschuwingssysteem tegen accountovername.

## Authenticatieflows Testen

Authenticatie verdient eigen tests: tokens verlopen, kunnen niet opnieuw worden gebruikt en werken niet voor andere accounts; herstellinks gebruiken de geconfigureerde basis-URL; sessies worden na een wachtwoordwijziging ingetrokken; rate limits gaan af bij de juiste drempels; en antwoorden zijn identiek voor bekende en onbekende e-mailadressen. Voeg ze toe aan CI, zodat wijzigingen met hulp van AI in de authenticatiecode deze eigenschappen niet ongemerkt kunnen verzwakken.

## Wanneer Je de Flows van Je Aanbieder Gebruikt

Volwassen authenticatieaanbieders implementeren het meeste hiervan standaard. De betrouwbaarste aanpak voor AI-gebouwde apps is meestal de herstel- en magic-linkflows van de aanbieder direct te gebruiken, vervaltijd, redirect-URL's en rate limits in de instellingen van de aanbieder te configureren, en ze niet in eigen code te verpakken tenzij daar een duidelijke reden voor is. De meeste kwetsbaarheden op dit gebied komen uit eigen wrappers, niet uit de aanbieders zelf.

## Tweestapsverificatie als Volgende Stap

Bied bij apps met gevoelige data of beheerdersbevoegdheden tweestapsverificatie aan. Authenticator-apps (TOTP) en passkeys zijn sterker dan sms-codes, die kwetsbaar zijn voor simswapping. Geef herstelcodes bij het instellen, laat gebruikers hun apparaten beheren, en vereis opnieuw inloggen voordat tweestapsverificatie kan worden uitgezet. Maak het verplicht voor accounts van medewerkers en beheerders. De meeste authenticatieaanbieders ondersteunen deze functies; ze aanzetten is vaak een kwestie van configuratie in plaats van een ontwikkelproject.

## Passkeys: Waar Authenticatie Naartoe Gaat

Passkeys vervangen wachtwoorden door cryptografische inloggegevens die op de apparaten van gebruikers worden bewaard en door hun platform worden gesynchroniseerd. Ze zijn bestand tegen phishing en credential stuffing en maken wachtwoordherstel in veel gevallen overbodig. De ondersteuning groeit in browsers, besturingssystemen en bij authenticatieaanbieders. Voor nieuwe AI-gebouwde apps is het aanbieden van passkeys naast inloggen via e-mail een steeds praktischere optie - en het verkleint het aanvalsoppervlak dat dit artikel beschrijft.

## Veelgestelde Vragen van Gebruikers

Gebruikers vragen soms waarom herstellinks snel verlopen of waarom ze geen e-mail hebben ontvangen. Beantwoord beide op je helppagina's: links verlopen om accounts te beschermen; e-mails kunnen een minuut duren of in de spam belanden; om veiligheidsredenen vertelt de app niet of een e-mailadres een account heeft. Duidelijke uitleg vermindert supportvragen en helpt gebruikers begrijpen dat frictie bescherming is.

## Een Laatste Controle vóór de Lancering

Vraag een herstel aan voor een echt account en bekijk alles: het afzenderdomein van de e-mail, de host van de link, hoe lang hij werkt, of hij twee keer werkt, of andere sessies na gebruik eindigen en of je een melding ontvangt. Vraag daarna een herstel aan voor een adres dat niet bestaat en vergelijk het antwoord. Tien minuten testen verifieert de hele flow van begin tot eind.

## Waarom Dit de Aandacht van de Oprichter Verdient

Flows voor wachtwoordherstel en magic links komen zelden voor in demo's, en oprichters klikken ze na de lancering zelden aan. Toch bepalen ze of een aanvaller een account kan overnemen zonder ooit het wachtwoord te kennen. Een paar uur besteed aan tokensterkte, vervaltijd, eenmalig gebruik, veilige URL's, rate limits en het intrekken van sessies beschermt elk account in je app - inclusief je eigen beheerdersaccount, vaak het waardevolste doelwit van allemaal. Zet de controles op je lanceringslijst naast betalingen en toegangsbeheer, waar ze horen.

## Waar LaunchStudio Past

LaunchStudio beoordeelt authenticatieflows bij elke beveiligingsronde, en logica voor herstel en magic links is waar eigen AI-gegenereerde code het vaakst moet worden vervangen door een ingebouwde flow van een aanbieder of een versterkte implementatie. LaunchStudio wordt aangedreven door Manifera, wiens CEO Herre Roelevink zijn loopbaan in cybersecurity begon - hij was medeoprichter van CyberDevOps, nu CFLW Cyber Strategies - en wiens engineers in Ho Chi Minh-stad al meer dan 11 jaar authenticatie bouwen voor enterprisesystemen. Zie [de over-ons-pagina van Manifera](https://www.manifera.com/about-us/).

Weet je niet zeker wie je herstelflow heeft geschreven, [praat dan met een engineer die AI-gegenereerde code begrijpt](https://launchstudio.eu/nl/#contact).

## Praktijkvoorbeeld

### Een AI-Native Oprichter in Actie: Een Planner voor Schoonmaakbedrijven met een Achterdeur van Zes Cijfers

Tijmen Boersma, die een schoonmaakbedrijf voor bedrijfspanden heeft in Almelo, bouwde Poetsplan met Cursor: een plannings-SaaS voor schoonmaakbedrijven, waarin planners schoonmakers toewijzen aan kantoorgebouwen en klanten voltooide rondes en toegangsnotities voor gebouwen zien - inclusief alarmcodes. Tweeëntwintig schoonmaakbedrijven in Twente gebruikten het.

Tijmen had Cursor gevraagd om "inloggen zonder wachtwoord met een code per e-mail". Het resultaat stuurde een numerieke code van zes cijfers, 24 uur geldig, zonder limiet op het aantal pogingen. Een klant met oog voor beveiliging testte het en raadde met een eenvoudig script binnen een middag zijn weg in een testaccount binnen. De review vond meer: de aparte flow voor wachtwoordherstel bouwde zijn link op uit de host-header van het verzoek, tokens werden als platte tekst opgeslagen, herstel beëindigde geen andere sessies, en het inlogformulier meldde "onbekend e-mailadres" voor niet-klanten.

De engineers van LaunchStudio vervingen de eigen inlog- en herstelcode door de ingebouwde flows van Supabase Auth, configureerden een vervaltijd van tien minuten, gehashte tokens voor eenmalig gebruik en een bevestigingsstap die e-mailscanners overleeft, voegden rate limits per e-mailadres en IP toe met blokkades na pogingen, zetten herstel-URL's vast op een geconfigureerde basis-URL, trokken bij een wachtwoordwijziging alle sessies in met een meldingsmail, maakten foutmeldingen gelijk en verplaatsten het versturen naar een geauthenticeerd domein. Alarmcodes werden daarnaast beperkt tot de rol van planner.

**Resultaat:** De vervolgtest van de klant vond geen weg naar binnen, en Poetsplan doorstond de beveiligingscontrole voor leveranciers van die klant. Het is sindsdien gegroeid naar 35 schoonmaakbedrijven.

> *"Ik vroeg om gemak en kreeg een slot met zes cijfers en onbeperkt raden. De oplossing was vooral gebruiken wat mijn authenticatieaanbieder al goed deed."*
> - **Tijmen Boersma, Oprichter, Poetsplan (Almelo)**

**Kosten & Tijdlijn:** € 1.150 (vervanging van authenticatieflows, rate limiting, sessiebeheer en inrichting van e-mail) - afgerond in 4 werkdagen.

## Veelgestelde Vragen

### Hoe lang moet een link voor wachtwoordherstel geldig blijven?

Doorgaans 15 tot 60 minuten, en maar één keer te gebruiken. Links voor magisch inloggen zijn vaak korter geldig. Langere geldigheid maakt van oude e-mails permanente sleutels tot accounts.

### Zijn e-mailcodes van zes cijfers veilig om mee in te loggen?

Alleen met strikte rate limits, een korte vervaltijd en blokkades. Zonder die maatregelen kan een code van zes cijfers snel met brute force worden geraden. Lange willekeurige links of flows die door de aanbieder worden beheerd, zijn veiligere standaarden.

### Moet ik mijn eigen herstelflow bouwen of die van mijn authenticatieaanbieder gebruiken?

Gebruik waar mogelijk de ingebouwde flow van de aanbieder. Eigen flows zijn waar AI-gegenereerde code het vaakst raadbare tokens, ontbrekende vervaltijd en problemen met de host-header introduceert.

### Waarom legt Manifera bij elke review de nadruk op authenticatie?

Accountovername is een van de meest schadelijke en veelvoorkomende aanvallen op kleine apps. De wortels van Manifera in cybersecurity, via het eerdere werk van Herre Roelevink, maken authenticatieflows tot een standaard eerste controle in plaats van een optionele extra.

### Beïnvloedt veilig inloggen de vertrouwenssignalen online?

Indirect. Accountovernames leiden tot openbare klachten en reviews die zoekmachines en AI-antwoordmachines tonen. Schone, geauthenticeerde e-mails beschermen ook de reputatie van je domein bij inboxaanbieders.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "Hoe lang moet een link voor wachtwoordherstel geldig blijven?", "acceptedAnswer": { "@type": "Answer", "text": "Doorgaans 15 tot 60 minuten en eenmalig te gebruiken; magic links vaak korter." } },
    { "@type": "Question", "name": "Zijn e-mailcodes van zes cijfers veilig om mee in te loggen?", "acceptedAnswer": { "@type": "Answer", "text": "Alleen met strikte rate limits, korte vervaltijd en blokkades; anders kunnen ze met brute force worden geraden." } },
    { "@type": "Question", "name": "Moet ik mijn eigen herstelflow bouwen of die van mijn authenticatieaanbieder gebruiken?", "acceptedAnswer": { "@type": "Answer", "text": "Gebruik de ingebouwde flow van de aanbieder; eigen flows zijn waar AI-code zwakke tokens en problemen met de host-header introduceert." } },
    { "@type": "Question", "name": "Waarom legt Manifera bij elke review de nadruk op authenticatie?", "acceptedAnswer": { "@type": "Answer", "text": "Accountovername komt vaak voor en is schadelijk; de cybersecuritywortels van Manifera maken authenticatie tot een standaard eerste controle." } },
    { "@type": "Question", "name": "Beïnvloedt veilig inloggen de vertrouwenssignalen online?", "acceptedAnswer": { "@type": "Answer", "text": "Indirect, door klachten over overnames te voorkomen en de reputatie van het e-maildomein te beschermen." } }
  ]
}
</script>
