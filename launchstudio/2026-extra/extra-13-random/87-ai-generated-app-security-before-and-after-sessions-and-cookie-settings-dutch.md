---
Titel: "Beveiliging van AI-gegenereerde apps: Voor en na sessies en cookie-instellingen"
Trefwoorden: beveiliging ai-gegenereerde apps, sessiebeveiliging, cookie flags httponly samesite, csrf bescherming, cursor authenticatie, LaunchStudio, Manifera
Koperfase: Overweging
Doelgroep: Technische Solo-Oprichter / Indie Hacker
---

# Beveiliging van AI-gegenereerde apps: Voor en na sessies en cookie-instellingen

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Beveiliging van AI-gegenereerde apps: Voor en na sessies en cookie-instellingen",
  "description": "Sessies bepalen wie er is ingelogd, maar door AI gegenereerde code gaat daar vaak slordig mee om. Een voor-en-na-blik op sessie- en cookie-instellingen in de beveiliging van AI-apps: opslag, cookie-vlaggen, CSRF, levensduur, uitloggen en sessie-intrekking.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-12-26",
  "inLanguage": "nl-NL",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/ai-generated-app-security-before-and-after-sessions-and-cookie-settings" }
}
</script>

Inloggen is slechts één kort moment; een sessie omvat alles wat daarna komt. Elk afzonderlijk verzoek dat uw applicatie ontvangt, draagt het bewijs mee dat *"dit nog steeds dezelfde gebruiker is die zojuist inlogde"* — via een token of een sessiecookie. Als dat bewijs kan worden gestolen, gemanipuleerd of opnieuw gebruikt, doet de sterkte van uw inlogscherm er totaal niet meer toe. Sessiebeheer is een onderdeel van de beveiliging van AI-gegenereerde software dat tijdens demonstraties zelden aandacht krijgt, omdat een demo nooit test wat er gebeurt op een gedeelde computer, via een kwaadaardige link of na een wachtwoordwijziging.

## Voor: Hoe door AI gegenereerde apps sessies vaak inrichten

Wanneer AI-codeertools zelfgeschreven authenticatie implementeren — of een externe auth-dienst in eigen code wikkelen — duiken telkens dezelfde riskante patronen op:

- **Tokens in `localStorage`,** rechtstreeks uit te lezen door ieder JavaScript-script op de pagina, inclusief kwaadaardig geïnjecteerde scripts (XSS).
- **Cookies zonder essentiële beveiligingsvlaggen** — ontbrekende `HttpOnly`, `Secure` of `SameSite` attributen.
- **Buitensporig lange geldigheid,** zoals tokens die zonder verversing of intrekking 30 dagen lang geldig blijven.
- **Uitlogfuncties die alleen het token in de browser wissen,** terwijl het token zelf op de server volkomen geldig blijft.
- **Geen sessie-intrekking** na een wachtwoordwijziging of na het blokkeren van een account.
- **Geen CSRF-bescherming** op formulieren die gegevens wijzigen met behulp van cookies.
- **Sessie-identificatoren in de URL,** die weglekken via browsergeschiedenis, serverlogs en HTTP-referrer headers.

## Na: Cookie-instellingen die het verschil maken

Bij sessies op basis van cookies nemen drie vlaggen het zwaarste beveiligingswerk voor hun rekening:

- **`HttpOnly`**: JavaScript kan het cookie onder geen beding uitlezen, waardoor een scriptinjectie niet zomaar de sessie kan kapen.
- **`Secure`**: het cookie wordt uitsluitend verstuurd over versleutelde HTTPS-verbindingen.
- **`SameSite=Lax` (of `Strict`)**: de browser verstuurt het cookie niet mee bij verzoeken vanaf externe websites, wat een hele categorie van Cross-Site Request Forgery (CSRF) elimineert.

Voeg hier een specifiek `Path` aan toe, vermijd te ruime `Domain`-instellingen die cookies onnodig delen tussen subdomeinen, en gebruik waar mogelijk het `__Host-`-voorvoegsel voor cookies die strikt aan één enkele host gekoppeld moeten blijven.

## Na: Waar tokens daadwerkelijk horen te leven

Gebruikt uw app stateless tokens (zoals JWT's) in plaats van klassieke serversessies, dan is de opslaglocatie van levensbelang. Tokens in `localStorage` liggen open en bloot voor elk script op uw pagina; een klein XSS-foutje resulteert onmiddellijk in een volledige accountovername. Een veel veiligere architectuur bewaart refresh tokens in `HttpOnly`-cookies, houdt kortlevende access tokens uitsluitend in het werkgeheugen (memory), en roteert het refresh token bij ieder gebruik. Professionele auth-providers passen dit standaard toe; handmatig door AI gegenereerde code vrijwel nooit.

## Na: Doeltreffende CSRF-bescherming

Wanneer de browser sessiecookies automatisch meestuurt, kan een kwaadwillende externe website proberen namens een ingelogde bezoeker ongeziene acties op uw app uit te voeren. `SameSite`-cookies blokkeren het leeuwendeel van deze aanvallen; voor gevoelige handelingen voegt u daarnaast CSRF-tokens toe of vereist u een unieke custom HTTP-header die eenvoudige cross-site formulieren niet kunnen meesturen.

## Na: Levensduur, uitloggen en intrekking

- **Inactiviteitstime-out** en een **absolute maximale levensduur** afgestemd op de gevoeligheid van de data: korter voor financiële of medische apps, ruimer voor alledaagse tools.
- **Uitloggen maakt de sessie ongeldig op de server,** en ruimt niet slechts de browser op.
- **Wachtwoordwijzigingen en accountblokkades trekken direct alle actieve sessies in.**
- **"Overal uitloggen"-functionaliteit** voor gebruikers die vermoeden dat een apparaat is kwijtgeraakt of gestolen.
- **Sessie-overzichten** voor risicovollere applicaties, zodat gebruikers actieve logins en apparaten zelf kunnen controleren.

## Na: Sessiefixatie voorkomen en identifiers roteren

Genereer bij het inloggen en bij elke rechtenwijziging (zoals het openen van een beheerderspaneel) direct een geheel nieuwe sessie-ID, zodat een identifier die vóór het inloggen werd toegekend nooit door een aanvaller kan worden misbruikt.

## Snelle zelfcheck in de browser

Open de ontwikkelaarstools van uw browser (F12), log in op uw applicatie en bekijk Application → Cookies en Local Storage:

- Staan er tokens opgeslagen in Local Storage?
- Tonen uw sessiecookies de vlaggen HttpOnly, Secure en SameSite?
- Werkt een oud verzoek via Postman of cURL nog steeds nadat u op "Uitloggen" heeft geklikt?
- Blijft een ander apparaat ingelogd nadat u uw wachtwoord heeft veranderd?

Het [OWASP Session Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html) biedt hierover een heldere technische standaard.

## Cookies correct instellen in broncode

In door AI gegenereerde code is het verschil tussen een zwak en een ijzersterk sessiecookie een kwestie van een handvol attributen. In een Next.js route handler ziet een veilige configuratie er als volgt uit:

```typescript
import { cookies } from "next/headers";

cookies().set("__Host-session", sessionId, {
  httpOnly: true,     // Niet uit te lezen via JavaScript
  secure: true,       // Uitsluitend via HTTPS
  sameSite: "lax",    // Wordt niet meegestuurd bij externe requests
  path: "/",          // Verplicht voor het __Host- voorvoegsel
  maxAge: 60 * 60 * 8 // Geldigheidsduur van 8 uur
});
```

Het `__Host-`-voorvoegsel dwingt browsers af om het cookie alleen te accepteren als het via HTTPS verzonden wordt, het pad `/` heeft en geen `Domain`-attribuut bevat — waardoor subdomeinen het niet kunnen manipuleren. Veel AI-tools configureren cookies met standaardwaarden, wat in de praktijk neerkomt op géén `HttpOnly` en soms zelfs géén `Secure`.

## Sessietime-outs afstemmen op risiconiveau

| Type applicatie | Inactiviteitstime-out | Absolute maximale duur | Opnieuw inloggen vereist voor |
| --- | --- | --- | --- |
| Laag-risico tools (notities, planning) | Dagen tot weken met refresh | 30–90 dagen | Wijzigen van e-mail of wachtwoord |
| Typische zakelijke SaaS | Enkele uren | 7–30 dagen | Facturatie, data-exports, rolbeheer |
| Financiële, medische of HR-data | 15–60 minuten | 12–24 uur | Iedere gevoelige wijziging of inzage |
| Gedeelde apparaten (receptie, balies) | Minuten | Einde van de werkdag | Iedere nieuwe sessie |

Kies time-outs bewust en licht ze toe aan gebruikers waar ze frictie veroorzaken (*"vanwege de beveiliging vragen we u opnieuw in te loggen om financiële overzichten te downloaden"*).

## Veilig werken met tokens

Applicaties die gebruikmaken van JWT's horen duidelijke regels te hanteren: kortlevende access tokens (enkele minuten); refresh tokens strikt bewaard in HttpOnly-cookies en geroteerd bij elke verversing, voorzien van hergebruiksdetectie (reuse detection) die direct de complete sessie blokkeert zodra een verouderd refresh token opnieuw opduikt; centrale serverregistratie van actieve sessies; en cryptografische validatie van handtekening, vervaldatum en audience bij elk request. Volwassen authenticatiediensten bieden dit standaard; zelfgebouwde oplossingen vanuit prompts slaan deze stappen stelselmatig over.

## CSRF-beveiliging in moderne frameworks

Dankzij `SameSite`-cookies vangt de browser het merendeel van cross-site aanvallen op. Voor extra zekerheid bij gevoelige acties combineert u dit met: een cryptografisch CSRF-token in het formulier dat op de server wordt gevalideerd, of het verplichtstellen van een custom HTTP-header die eenvoudige HTML-formulieren niet kunnen toevoegen. Sommige frameworks controleren standaard de `Origin`-header bij form submissions — controleer altijd of deze beveiliging in uw configuratie daadwerkelijk actief staat.

## Een uitlogknop die sessies ook écht beëindigt

Een correcte uitlogflow doet drie dingen: het verwijdert de sessierij of trekt het refresh token in op de server, overschrijft het cookie in de browser met exact dezelfde attributen en een verlopen datum, en wist eventuele gecachte gebruikersdata in de frontend. "Overal uitloggen" trekt alle actieve tokens van de betreffende gebruiker in de database in. Test dit eenvoudig: log uit in de browser, herhaal een eerder vastgelegd netwerkverzoek met het oude cookie of token via de terminal, en controleer of de server dit verzoek weigert met een foutcode 401.

## Sessiebeveiliging versterken met Content Security Policy

Sessiebeveiliging en bescherming tegen Cross-Site Scripting (XSS) vullen elkaar aan. `HttpOnly`-cookies verhinderen dat kwaadaardige scripts het cookie stelen, maar een geïnjecteerd script kan binnen de actieve pagina nog steeds frauduleuze verzoeken doen namens de gebruiker. Een doordachte Content Security Policy (CSP) die externe scriptbronnen strikt beperkt en inline code verbiedt, voorkomt dat kwaadaardige code überhaupt kan worden uitgevoerd. Samen reduceren ze een XSS-foutje van een fatale accountovername tot een beheersbaar bugje.

## Afwijkend sessiegedrag monitoren

Registreer sessiegerelateerde gebeurtenissen in uw serverlogs: inlogpogingen, token-verversingen, uitlogacties, intrekkingen en mislukte verversingen, inclusief IP-reeksen en user agents. Stel waarschuwingen in voor verdachte patronen, zoals één account dat binnen enkele minuten inlogt vanuit twee verschillende landen, of meldingen van hergebruikte refresh tokens. Bied gebruikers inzicht in hun eigen actieve apparaten zodat zij ongebruikelijke activiteit direct kunnen signaleren.

## Sessies op gedeelde en openbare apparaten

Applicaties die draaien op gedeelde werkplekken — balies, recepties, klaslokalen of productielocaties — vereisen aanvullende maatregelen. Bouw een speciale "gedeeld apparaat"-modus in met zeer korte time-outs, zonder "onthoud mij"-optie, met automatische afmelding aan het eind van de werkdag en snelle pincode-wissels. Zorg ervoor dat gevoelige gegevens bij uitloggen direct uit het browserviewport verdwijnen zodat de "terug"-knop niets toont, en configureer HTTP-cacheheaders zodat de browser gevoelige schermen niet lokaal bewaart.

## Waarom oprichters hier prioriteit aan moeten geven

Sessielekken vallen zelden op tijdens productdemo's, maar ze bepalen wel of een gestolen token of een gedeelde computer resulteert in een compleet datalek. De reparatie is doorgaans voordelig en snel — voornamelijk configuratie en het juist toepassen van beproefde authenticatieplatformen — terwijl het moeten verklaren van een datalek aan klanten en toezichthouders enorme schade aanricht. Zet sessiebeveiliging vóór de lancering op exact hetzelfde prioriteitsniveau als betalingen en databasebeveiliging.

## Voor en na samengevat

Voor: tokens in `localStorage`, cookies zonder veilige vlaggen, sessies die een maand ongewijzigd blijven doorlopen, uitlogknoppen die alleen het scherm leegmaken, geen CSRF-bescherming en sessies die actief blijven na een wachtwoordwijziging. Na: `HttpOnly`, `Secure` en `SameSite`-cookies met host-binding; kortlevende access tokens met geroteerde refresh tokens; server-side intrekking bij uitloggen en wachtwoordherstel; time-outs afgestemd op bedrijfsrisico; CSRF-headers; een robuuste Content Security Policy; en geautomatiseerde regressietests. Voor de gebruiker ziet het inlogscherm er visueel exact hetzelfde uit — het cruciale verschil is dat uw platform nu bestand is tegen accountovernames.

## Eerste stap

Log in op uw eigen app, open de ontwikkelaarstools van de browser en kijk onder Application → Cookies en Local Storage. Ziet u een token rondslingeren in Local Storage of ontbreekt de vlag `HttpOnly` bij uw sessiecookie? Begin dan vandaag nog met die aanpassing.

## Waar LaunchStudio u bij helpt

LaunchStudio beoordeelt sessiebeheer bij elke technische security-audit. We vervangen fragiele zelfgebouwde sessiecode door de veilige standaarden van volwassen auth-providers, configureren strikte cookie-attributen, richten CSRF-bescherming in en implementeren server-side sessie-intrekking. LaunchStudio wordt aangedreven door Manifera. De cybersecurity-achtergrond van CEO Herre Roelevink — medeoprichter van CyberDevOps, nu CFLW Cyber Strategies — vormt het fundament van onze strenge beveiligingscultuur. Manifera's software-engineers werken vanuit Ho Chi Minh City, met accountmanagement aan de Herengracht 420 in Amsterdam. Bekijk [Manifera's over ons pagina](https://www.manifera.com/about-us/).

[Vraag een vaste offerte aan](https://launchstudio.eu/nl/#contact) voor een grondige authenticatie- en sessie-audit.

## Praktijkvoorbeeld

### Een AI-Native Oprichter in Actie: Een Vergaderruimte-App Waar Uitloggen Niet Écht Uitlogde

Sem Evers, facilitair coördinator en oprichter in IJsselstein, bouwde Zaalvrij met behulp van Cursor: bedrijven in verzamelgebouwen reserveren hiermee vergaderruimtes, melden bezoekers aan en ontvangen aan het eind van de maand een verzamelfactuur. Zesentwintig bedrijven verspreid over vier kantoorpanden maakten er intensief gebruik van, veelal via vaste pc's bij de centrale receptiebalie.

Een oplettende receptionist merkte op dat na het uitloggen op de gedeelde balie-pc, een simpele klik op de "Vorige"-knop van de browser de reserveringen van een ander bedrijf weer tevoorschijn toverde — en dat doorklikken gewoon bleef functioneren. Een security-analyse door LaunchStudio legde de oorzaak bloot: Cursor had authenticatie gegenereerd met JWT's die waren opgeslagen in `localStorage`, 30 dagen geldig bleven, en de uitlogknop wiste slechts de lokale variabele uit het browsergeheugen zonder de sessie op de server te beëindigen. Een gekopieerd token bleef onbeperkt werken. Formulieren om boekingen te annuleren misten CSRF-validatie en wachtwoordwijzigingen beëindigden actieve sessies op andere apparaten niet. Daarnaast bleek het bezoekersveld vatbaar voor een reflectieve XSS, waardoor een specifieke URL het token rechtstreeks had kunnen buitmaken.

In vier werkdagen vervingen de engineers van LaunchStudio de kwetsbare token-opzet door de sessie-infrastructuur van Supabase Auth, werden refresh tokens ondergebracht in `HttpOnly`, `Secure`, `SameSite=Lax`-cookies, werd de levensduur van access tokens verkort, werd uitloggen gekoppeld aan directe server-side intrekking, kwam er een inactiviteitstime-out van acht uur voor balie-accounts, kregen gevoelige formulieren CSRF-bescherming, werd de XSS-kwetsbaarheid verholpen met output escaping en een strikte CSP, en werd een functie "overal uitloggen" geactiveerd.

**Resultaat:** Het probleem op gedeelde balies was definitief verleden tijd. Een uitgebreide beveiligingsvragenlijst van een grote nieuwe huurder kon vlekkeloos en zonder aanvullende eisen worden beantwoord. Zaalvrij is inmiddels in twee nieuwe kantoorlocaties uitgerold.

> *"Onze uitlogknop was een beleefd verzoek aan de browser. Nu beëindigt hij de sessie onmiddellijk en definitief."*
> — **Sem Evers, Oprichter, Zaalvrij (IJsselstein)**

**Kosten & Tijdlijn:** €1.100 (harding van sessies en cookies, CSRF-bescherming, XSS-reparatie en migratie naar robuuste auth-provider) — afgerond in 4 werkdagen.

## Veelgestelde Vragen

### Is het opslaan van authenticatietokens in localStorage onveilig?
Ja. Gegevens in `localStorage` zijn direct toegankelijk voor elk JavaScript-script op uw website. Bij een eventueel XSS-lek kan een aanvaller het authenticatietoken direct stelen en het account overnemen.

### Welke beveiligingsvlaggen moeten sessiecookies altijd bevatten?
Minimaal `HttpOnly` (niet uitleesbaar via JavaScript), `Secure` (alleen verzenden over HTTPS) en `SameSite=Lax` of `SameSite=Strict` (bescherming tegen cross-site aanvallen), bij voorkeur met het `__Host-`-voorvoegsel.

### Maakt een klik op "Uitloggen" een token automatisch ongeldig?
Alleen als de server de sessie of het token expliciet intrekt. Veel met AI gebouwde applicaties verwijderen de variabele alleen lokaal uit de browser, waardoor het token op de achtergrond volledig geldig blijft.

### Waarom inspecteert Manifera sessiebeheer bij elke beveiligingscheck?
Omdat kwetsbaarheden in sessiebeheer kleine softwarefoutjes direct laten escaleren tot complete accountovernames. Vanwege Manifera's achtergrond in cybersecurity vormen sessies, cookies en tokens standaard vaste controlepunten.

### Hebben veilige cookie-instellingen invloed op SEO of websitestatistieken?
Sessiecookies hebben geen directe invloed op SEO. Correcte HTTPS-configuratie en sterke beveiligingsheaders versterken juist het vertrouwenssignaal bij zoekmachines, en nauwkeurig afgebakende cookies voorkomen conflicten met analysetools.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Is het opslaan van authenticatietokens in localStorage onveilig?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ja; data in localStorage is leesbaar voor alle scripts op de pagina, waardoor een XSS-lek direct leidt tot een overname van het account."
      }
    },
    {
      "@type": "Question",
      "name": "Welke beveiligingsvlaggen moeten sessiecookies altijd bevatten?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Minimaal HttpOnly, Secure en SameSite (Lax of Strict), bij voorkeur met het __Host- voorvoegsel."
      }
    },
    {
      "@type": "Question",
      "name": "Maakt een klik op 'Uitloggen' een token automatisch ongeldig?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Alleen als de server de sessie daadwerkelijk intrekt; veel AI-apps wissen slechts de variabele in de browser."
      }
    },
    {
      "@type": "Question",
      "name": "Waarom inspecteert Manifera sessiebeheer bij elke beveiligingscheck?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Omdat fouten in sessies kleine bugs direct laten escaleren tot accountovernames; Manifera hanteert hier strikte cybersecurity-standaarden voor."
      }
    },
    {
      "@type": "Question",
      "name": "Hebben veilige cookie-instellingen invloed op SEO of websitestatistieken?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Niet direct op SEO; wel versterken HTTPS en beveiligingsheaders het algehele betrouwbaarheidsprofiel van het domein."
      }
    }
  ]
}
</script>
