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
  "description": "Wachtwoordherstel en magic links vormen de geruisloze achterdeur in de beveiliging van AI-gebouwde apps. Dit artikel behandelt token-entropie, verlooptermijnen, eenmalig gebruik, host header poisoning, enumeratie, sessie-invalidatie en e-mailbezorging — inclusief checklist voor technische oprichters.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-12-01",
  "inLanguage": "nl-NL",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/ai-generated-app-security-password-resets-and-magic-links-done-right" }
}
</script>

Aanvallers kraken zelden je standaard inlogformulier. Ze lopen er simpelweg omheen. De wachtwoordherstelfunctie — en zijn moderne variant, de *magic link* — is een tweede volwaardige toegangsweg tot elk gebruikersaccount. Binnen de beveiliging van met AI gebouwde applicaties is dit steevast een van de minst onderzochte onderdelen van de codebase. Het inlogscherm krijgt alle aandacht omdat iedereen het dagelijks gebruikt; de herstelstroom wordt tijdens het bouwen één keer getest en daarna vergeten. En dat maakt deze route juist zo aantrekkelijk voor kwaadwillenden.

Draait je authenticatie volledig op een volwassen en beproefde dienst zoals Supabase Auth, Auth0 of Firebase Auth, dan worden de meeste risico's standaard voor je afgevangen — mits je er geen eigen maatwerkcode omheen hebt gebouwd. De problemen beginnen wanneer een AI-tool gevraagd wordt om een eigen herstellogica of een op maat gemaakte "wachtwoordloze" inlogmethode te genereren.

## Wat een Herstellink Werkelijk Is

Een link voor wachtwoordherstel is in feite een tijdelijk wachtwoord met superrechten. Iedereen die over die specifieke link beschikt, kan het account direct overnemen. Elk beveiligingskenmerk dat van belang is voor een regulier wachtwoord, geldt onverminderd voor het token in die URL: hoe moeilijk het te raden is, hoe lang het geldig blijft, langs welke routes het reist en of het meerdere keren kan worden gebruikt.

## Zeven Klassieke Fouten in AI-Gegenereerde Herstelstromen

**1. Eenvoudig te raden tokens.** Tokens gegenereerd met `Math.random()`, tijdstempels, gebruikers-ID's of korte numerieke cijfercodes zijn voorspelbaar of via 'brute force' te kraken. Tokens moeten afkomstig zijn van een cryptografisch veilige random-generator (`crypto.randomBytes`) en voldoende lang zijn — minimaal 128 bits.

**2. Geen verlooptermijn, of een veel te lange.** Links die dagenlang of oneindig geldig blijven, veranderen elke oude e-mail in iemands inbox in een permanente huissleutel. Een geldigheid van 15 tot maximaal 60 minuten is de norm voor herstellinks; voor magic links vaak zelfs korter.

**3. Herbruikbare tokens.** Zodra een wachtwoord succesvol is gewijzigd, moet het gebruikte token direct ongeldig worden gemaakt. Veel AI-gegenereerde code laat het token actief tot de officiële vervaltijd, waardoor iedereen die de link later onder ogen krijgt (in een doorgestuurde mail, browsergeschiedenis of gedeeld scherm) opnieuw kan inloggen.

**4. Tokens ongecodeerd (plain text) opslaan in de database.** Als hersteltokens als platte tekst in de database staan, kan iedereen met leesrechten op die tabel — of via een gelekte database-backup — direct elk account overnemen waar een herstelverzoek voor openstaat. Sla tokens altijd gehasht op (bijv. met SHA-256), exact zoals je met wachtwoorden doet.

**5. Host Header Poisoning.** AI-code construeert de reset-URL vaak dynamisch op basis van de `Host`-header van het binnenkomende HTTP-verzoek. Een aanvaller die een herstelverzoek indient met een gemanipuleerde host-header kan ervoor zorgen dat het e-mailbericht naar het domein van de aanvaller linkt. Zodra het slachtoffer klikt, ontvangt de aanvaller het geldige token. Bouw URL's altijd op vanuit een hard geconfigureerde basis-URL in je omgevingsvariabelen.

**6. Gebruikers-enumeratie.** Foutmeldingen zoals "Er bestaat geen account met dit e-mailadres" vertellen aanvallers precies welke e-mailadressen klant bij jou zijn. Toon altijd dezelfde neutrale bevestiging: "Als dit adres bij ons bekend is, hebben we een herstellink verzonden."

**7. Bestaande sessies blijven actief na herstel.** Wanneer iemand zijn wachtwoord reset — vaak uit vrees dat het gecompromitteerd is — moeten alle bestaande actieve sessies op andere apparaten direct worden beëindigd. AI-code vergeet dit vrijwel altijd en overschrijft alleen de wachtwoord-hash in de database.

## Magic Links: Dezelfde Regels, Plus Eén Extra Uitdaging

Magic links zijn functioneel identiek aan wachtwoordherstellinks, maar dan bedoeld voor regulier inloggen. Alle bovenstaande regels zijn van kracht, plus één specifiek operationeel probleem: zakelijke mailfilters en beveiligingsscanners "klikken" vaak automatisch op binnenkomende links om ze op malware te controleren. Hierdoor verbruiken deze bots het eenmalige token vóórdat de daadwerkelijke gebruiker de mail opent. De oplossing is een tussenpagina met een expliciete bevestigingsknop ("Klik hier om in te loggen"), of het gebruik van een korte numerieke eenmalige code.

## Rate Limiting en Monitoring

Endpoints voor wachtwoordherstel en magic links moeten strikt worden gelimiteerd per e-mailadres én per IP-adres. Dit voorkomt grootschalige gebruikers-enumeratie en beschermt je e-mailprovider tegen misbruik als spamkanaal.

## E-Mailbezorging Is een Veiligheidscomponent

Een herstelmail die in de spammap belandt zorgt voor frustratie en supporttickets; een herstelmail verzonden vanaf een ongeauthenticeerd domein leert gebruikers bovendien om verdachte e-mails te vertrouwen. Gebruik een gespecialiseerde transactionele e-maildienst (zoals Resend of Postmark), configureer SPF-, DKIM- en DMARC-records foutloos en houd herstelmails rustig, herkenbaar en zakelijk.

## Veilige Implementatie van Reset Tokens

Zo ziet een veilige implementatie in TypeScript eruit:

```typescript
import { randomBytes, createHash } from "crypto";

export function createResetToken() {
  const token = randomBytes(32).toString("base64url");       // gaat naar de gebruiker
  const tokenHash = createHash("sha256").update(token).digest("hex"); // gaat naar de database
  const expiresAt = new Date(Date.now() + 30 * 60 * 1000);   // 30 minuten geldig
  return { token, tokenHash, expiresAt };
}
```

De database bewaart uitsluitend `tokenHash`, `user_id`, `expires_at` en `used_at`. Zodra de gebruiker op de link klikt, hasht de applicatie het ontvangen token, zoekt het bijbehorende record op, markeert het als gebruikt in dezelfde databasetransactie als de wachtwoordwijziging en beëindigt alle openstaande sessies van die gebruiker. Mocht de database ooit lekken, dan heeft een hacker niets aan de opgeslagen hashes; lekt de e-mail na gebruik, dan is het token al ongeldig.

## Veilige URL-Opbouw Zonder Host Header Poisoning

Stel de herstellink altijd samen vanuit een vaste omgevingsvariabele:

```typescript
const base = process.env.APP_BASE_URL; // bijv. https://app.jouwbedrijf.nl
const link = `${base}/reset-password?token=${encodeURIComponent(token)}`;
```

Controleer bij het opstarten van de server of `APP_BASE_URL` is ingesteld en in productie altijd met HTTPS begint. Dit voorkomt effectief host header poisoning.

## Aanbevolen Rate Limits voor Authenticatie

| Endpoint | Per e-mailadres | Per IP-adres | Actie bij overschrijding |
| --- | --- | --- | --- |
| Aanvraag herstel / magic link | 3–5 per uur | 20 per uur | Zelfde neutrale melding; geen e-mail versturen |
| Indienen hersteltoken | 5 pogingen per token | 30 per uur | Token direct ongeldig verklaren |
| Inlogpogingen | 5–10 per 15 min | 50 per 15 min | Tijdelijke time-out met neutrale melding |
| Eenmalige cijfercode (OTP) | 5 pogingen per code | 30 per uur | Code direct ongeldig verklaren |

## Waar LaunchStudio Past

LaunchStudio licht authenticatiestromen grondig door als vast onderdeel van security-trajecten. Juist bij wachtwoordherstel en wachtwoordloze logins blijkt op maat gegenereerde AI-code vaak onveilig en kwetsbaar. Wij vervangen wankele maatwerkoplossingen door beproefde, robuuste flows van gevestigde providers of brengen de custom implementatie op enterprise-beveiligingsniveau.

LaunchStudio wordt ondersteund door Manifera, waarvan CEO Herre Roelevink zijn loopbaan startte in cybersecurity (als medeoprichter van CyberDevOps, nu CFLW Cyber Strategies). De engineers in Ho Chi Minhstad bouwen al ruim 11 jaar authenticatiesystemen voor zakelijke enterprise-omgevingen. Bekijk [Manifera's over ons pagina](https://www.manifera.com/about-us/) en raadpleeg het officiële [OWASP Forgot Password Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Forgot_Password_Cheat_Sheet.html).

Twijfel je over de veiligheid van jouw herstelstroom? [Laat een engineer meekijken](https://launchstudio.eu/nl/#contact).

## Praktijkvoorbeeld

### Een AI-Native Oprichter in Actie: Een Planningssysteem voor Schoonmaakbedrijven met een Zescijferig Lek

Tijmen Boersma, eigenaar van een facilitair schoonmaakbedrijf in Almelo, bouwde Poetsplan in Cursor: een SaaS-planningsplatform voor schoonmaakbedrijven, waar planners roosters toewijzen aan panden en klanten voltooide rondes kunnen inzien, inclusief pandnotities en toegangscodes van alarmcentrales. Tweeëntwintig schoonmaakbedrijven in Twente sloten zich aan.

Tijmen had Cursor gevraagd om een "wachtwoordloze inlogmethode via een e-mailcode". De gegenereerde code verstuurde een zescijferige numerieke code die 24 uur geldig bleef, zónder enige limiet op het aantal inlogpogingen. Een IT-bewuste klant testte de login en wist via een simpel geautomatiseerd scriptje binnen een middag iemands account binnen te dringen. Een grondige security-audit bracht nog meer risico's aan het licht: de traditionele wachtwoordherstelfunctie bouwde links op via de `Host`-header van het verzoek, hersteltokens stonden ongecodeerd in de database, eerdere sessies bleven gewoon actief na een wachtwoordwijziging, en het formulier meldde "onbekend e-mailadres" als iemand nog geen account had.

De engineers van LaunchStudio saneerden de complete inloglaag: de maatwerklogica werd vervangen door de ingebouwde flows van Supabase Auth, met een geldigheid van tien minuten, cryptografisch gehashte eenmalige tokens en een bevestigingsknop tegen automatische e-mailscanners; er werden strikte rate limits ingesteld per e-mail en IP-adres met blokkades bij misbruik; herstellinks kregen een vaste basis-URL; bij een wachtwoordwijziging werden alle openstaande sessies direct beëindigd inclusief notificatiemail; foutmeldingen werden geüniformeerd; en e-mails werden verplaatst naar een professioneel geauthenticeerd domein. Bovendien werden pand-alarmcodes voortaan strikt afgeschermd met specifieke autorisatierollen.

**Resultaat:** Een hernieuwde pentest van de zakelijke klant toonde aan dat het systeem potdicht zat, waardoor Poetsplan glansrijk slaagde voor de leveranciersaudit. Het platform groeide in de maanden daarna door naar 35 aangesloten schoonmaakbedrijven.

> *"Ik vroeg om gebruiksgemak en kreeg een digitaal cijferslot van zes cijfers waar iedereen oneindig aan mocht draaien. De oplossing was simpel: gewoon gebruiken wat professionele auth-providers al standaard perfect op orde hebben."*
> — **Tijmen Boersma, Oprichter, Poetsplan (Almelo)**

**Kosten & Tijdlijn:** € 1.150 (vervanging van authenticatiestromen, rate limiting, sessie-invalidatie en e-mailconfiguratie) — afgerond in 4 werkdagen.

## Veelgestelde Vragen

### Hoe lang mag een link voor wachtwoordherstel geldig blijven?

Doorgaans 15 tot maximaal 60 minuten, en uitsluitend voor eenmalig gebruik. Links voor eenmalige magic logins zijn vaak nog korter geldig (bijv. 5 tot 15 minuten). Een langere geldigheid maakt van oude e-mails een permanent beveiligingsrisico.

### Zijn zescijferige e-mailcodes veilig voor inloggen?

Alleen wanneer ze gecombineerd worden met zeer strikte rate limits, een korte vervaltijd en automatische blokkades na een handvol foute pogingen. Zonder die beveiliging kan een zescijferige code binnen enkele uren worden gekraakt via geautomatiseerde scripts.

### Moet ik zelf een herstelstroom bouwen of de ingebouwde functies van mijn auth-provider gebruiken?

Gebruik altijd de ingebouwde stroom van je provider (zoals Supabase Auth of Firebase). Op maat gegenereerde AI-code introduceert op dit vlak bijna gegarandeerd zwakke tokens, ontbrekende verlooptermijnen en host header poisoning.

### Waarom hecht Manifera zoveel waarde aan authenticatiebeveiliging?

Accountovernames behoren tot de meest verwoestende en meest voorkomende incidenten bij jonge SaaS-bedrijven. Vanwege de achtergrond van Manifera's CEO in cybersecurity vormt een diepgaande inspectie van de inlogstromen altijd een vast vertrekpunt.

### Hebben veilige inlogprocessen invloed op het online vertrouwen en SEO?

Indirect zeker. Gecompromitteerde accounts leiden tot reputatieschade, negatieve recensies en klachten die zoekmachines en AI-zoekmodellen direct oppikken. Bovendien beschermt een goed geauthenticeerd e-maildomein de afleverbaarheid van al je communicatie.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Hoe lang mag een link voor wachtwoordherstel geldig blijven?",
      "acceptedAnswer": { "@type": "Answer", "text": "Doorgaans 15 tot 60 minuten en uitsluitend voor eenmalig gebruik; magic links zijn vaak nog korter geldig." }
    },
    {
      "@type": "Question",
      "name": "Zijn zescijferige e-mailcodes veilig voor inloggen?",
      "acceptedAnswer": { "@type": "Answer", "text": "Alleen met strikte rate limits, korte geldigheid en lockouts; anders zijn ze kwetsbaar voor brute-force aanvallen." }
    },
    {
      "@type": "Question",
      "name": "Moet ik zelf een herstelstroom bouwen of de ingebouwde functies van mijn auth-provider gebruiken?",
      "acceptedAnswer": { "@type": "Answer", "text": "Gebruik altijd de ingebouwde flows van je provider; zelfbouw via AI introduceert vaak ernstige beveiligingslekken." }
    },
    {
      "@type": "Question",
      "name": "Waarom hecht Manifera zoveel waarde aan authenticatiebeveiliging?",
      "acceptedAnswer": { "@type": "Answer", "text": "Accountovername is een van de grootste bedreigingen voor jonge SaaS-bedrijven; Manifera's roots liggen in cybersecurity." }
    },
    {
      "@type": "Question",
      "name": "Hebben veilige inlogprocessen invloed op het online vertrouwen en SEO?",
      "acceptedAnswer": { "@type": "Answer", "text": "Indirect ja, want accountovernames leiden tot negatieve reviews en beschadiging van de domeinreputatie bij mailproviders." }
    }
  ]
}
</script>
