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

Inloggen is een moment; een sessie is alles wat daarna komt. Elk verzoek dat uw app ontvangt, draagt een bewijs mee dat "dit nog steeds de gebruiker is die heeft ingelogd" — een token of een cookie. Kan dat bewijs worden gestolen, vervalst of hergebruikt, dan doet de sterkte van uw inlogscherm er niet toe. Sessiebeheer is een onderdeel van de beveiliging van AI-gegenereerde apps dat in demo's zelden aandacht krijgt, omdat demo's nooit testen wat er met een sessie gebeurt op een gedeelde computer, bij een kwaadaardige link of na een wachtwoordwijziging.

## Vooraf: Hoe AI-Gegenereerde Apps Vaak met Sessies Omgaan

Als AI-tools eigen authenticatie implementeren — of de authenticatie van een aanbieder in eigen code verpakken — zijn veelvoorkomende patronen:

- **Tokens in localStorage,** leesbaar voor elk JavaScript op de pagina, inclusief geïnjecteerde scripts.
- **Cookies zonder beveiligingsvlaggen** — zonder `HttpOnly`, `Secure` of `SameSite`.
- **Zeer lange levensduur,** zoals tokens die 30 dagen geldig zijn zonder vernieuwing of intrekking.
- **Uitloggen dat alleen het token in de browser verwijdert,** terwijl het token zelf op de server geldig blijft.
- **Geen intrekking van sessies** na wachtwoordwijzigingen of het verwijderen van een account.
- **Geen CSRF-bescherming** op formulieren met cookie-authenticatie die data wijzigen.
- **Sessie-identificatoren in URL's,** die lekken via de browsergeschiedenis, logs en referrer-headers.

## Daarna: Cookie-Instellingen die Ertoe Doen voor de Beveiliging van AI-Gegenereerde Apps

Bij sessies op basis van cookies doen drie vlaggen het meeste werk:

- **`HttpOnly`**: JavaScript kan de cookie niet lezen, dus een scriptinjectie kan de sessie niet zomaar stelen.
- **`Secure`**: de cookie wordt alleen via HTTPS verstuurd.
- **`SameSite=Lax` (of `Strict`)**: de browser stuurt de cookie bij de meeste verzoeken vanaf andere sites niet mee, wat een groot deel van cross-site request forgery blokkeert.

Voeg een verstandig `Path` toe, vermijd te brede `Domain`-instellingen die cookies onnodig over subdomeinen delen, en gebruik waar mogelijk het voorvoegsel `__Host-` voor cookies die aan één host gebonden moeten blijven.

## Daarna: Waar Tokens Staan

Gebruikt uw app tokens (bijvoorbeeld JWT's) in plaats van serversessies, dan doet de opslag ertoe. Tokens in `localStorage` liggen open voor elk script dat op uw pagina draait; een XSS-lek wordt dan een accountovername. Veiligere patronen bewaren refresh tokens in `HttpOnly`-cookies, houden access tokens kortlevend en in het geheugen, en roteren refresh tokens bij gebruik. Volwassen authenticatieaanbieders implementeren deze patronen; eigen code doet dat vaak niet.

## Daarna: CSRF-Bescherming

Stuurt de browser sessiecookies automatisch mee, dan kan een andere site proberen de browser van een ingelogde gebruiker een verzoek naar uw app te laten sturen. `SameSite`-cookies beperken het meeste hiervan; voeg voor gevoelige acties CSRF-tokens toe of vereis een eigen header die formulieren van andere sites niet kunnen instellen.

## Daarna: Levensduur, Uitloggen en Intrekken

- **Inactiviteitstime-out** en **absolute levensduur** passend bij de data: korter voor financiële of gezondheidsapps, langer voor tools met weinig risico.
- **Uitloggen maakt de sessie op de server ongeldig,** niet alleen in de browser.
- **Wachtwoordwijziging en accountverwijdering trekken alle sessies in.**
- **"Overal uitloggen"** voor gebruikers die een kwijtgeraakt apparaat vermoeden.
- **Overzicht van sessies** voor apps met een hoger risico, zodat gebruikers actieve apparaten kunnen zien.

## Daarna: Session Fixation en Rotatie

Geef bij het inloggen en bij een wijziging van rechten (bijvoorbeeld na het openen van de beheermodus) een nieuwe sessie-identificator uit, zodat een identificator die vóór het inloggen is ingesteld niet door een aanvaller kan worden hergebruikt.

## Snelle Zelfcontrole

Open de ontwikkelaarstools van uw browser, log in en kijk bij Application → Cookies en Local Storage:

- Staan er tokens in localStorage?
- Tonen uw sessiecookies HttpOnly, Secure en SameSite?
- Werkt het opnieuw afspelen van een oud verzoek na het uitloggen nog steeds?
- Wordt een ander apparaat uitgelogd nadat u op één apparaat uw wachtwoord hebt gewijzigd?

Het [OWASP Session Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html) behandelt de details.

## Cookies Correct Instellen, in Code

Voor de beveiliging van AI-gegenereerde apps is het verschil tussen een zwakke en een sterke sessiecookie een handvol attributen. In een route handler van Next.js ziet het correct instellen van een sessiecookie er zo uit:

```typescript
import { cookies } from "next/headers";

cookies().set("__Host-session", sessionId, {
  httpOnly: true,     // niet leesbaar voor JavaScript
  secure: true,       // alleen via HTTPS
  sameSite: "lax",    // niet meegestuurd bij de meeste verzoeken vanaf andere sites
  path: "/",          // vereist voor het voorvoegsel __Host-
  maxAge: 60 * 60 * 8 // 8 uur
});
```

Het voorvoegsel `__Host-` vertelt browsers de cookie alleen te accepteren als die beveiligd is, het pad `/` heeft en geen domeinattribuut — wat voorkomt dat subdomeinen hem overschrijven. Veel AI-gegenereerde implementaties stellen cookies in met standaardattributen, wat meestal betekent: geen `HttpOnly` en soms geen `Secure`.

## De Levensduur van Sessies Kiezen naar Risico

| Soort app | Inactiviteitstime-out | Absolute levensduur | Opnieuw authenticeren voor |
| --- | --- | --- | --- |
| Tool met weinig risico (notities, planning) | Dagen tot weken met vernieuwing | 30–90 dagen | E-mailadres of wachtwoord wijzigen |
| Typische SaaS met bedrijfsdata | Uren | 7–30 dagen | Facturatie, exports, rolwijzigingen |
| Financiële, gezondheids- of HR-data | 15–60 minuten | 12–24 uur | Elke gevoelige weergave of wijziging |
| Gedeelde apparaten (receptie, klaslokalen) | Minuten | Dezelfde werkdag | Elke sessie |

Kies de levensduur bewust en leg die uit aan gebruikers waar het frictie veroorzaakt ("log voor uw veiligheid opnieuw in om documenten te downloaden").

## Sessies op Basis van Tokens, Veilig Gedaan

Apps die JWT's of vergelijkbare tokens gebruiken, horen een paar regels te volgen: kortlevende access tokens (minuten); refresh tokens opgeslagen in HttpOnly-cookies, bij elk gebruik geroteerd, met detectie van hergebruik die de hele sessie intrekt als een oud refresh token weer opduikt; registraties van actieve sessies op de server, zodat ze kunnen worden ingetrokken; en verificatie van handtekening, vervaltijd en doelgroep van het token bij elk verzoek. Volwassen authenticatieaanbieders implementeren deze patronen; eigen implementaties die door AI-tools zijn gegenereerd, slaan rotatie en intrekking vaak helemaal over.

## CSRF-Bescherming in Moderne Frameworks

Met SameSite-cookies blokkeert de browser de meeste cross-site request forgery. Gebruik voor extra bescherming bij gevoelige acties een van deze methoden: synchronisatietokens (een willekeurig token in het formulier, op de server geverifieerd), double-submit cookies, of het vereisen van een eigen header die eenvoudige formulieren van andere sites niet kunnen instellen. Sommige frameworks bieden standaard CSRF-bescherming voor formulieracties — bijvoorbeeld door de Origin-header te controleren — maar controleer dat die in uw configuratie actief is in plaats van het aan te nemen.

## Uitloggen dat Sessies Echt Beëindigt

Een correcte uitlog: verwijdert de sessieregistratie of trekt het refresh token op de server in, wist de cookie met dezelfde attributen als waarmee die werd ingesteld, en maakt eventuele gecachete gebruikersdata in de client ongeldig. "Overal uitloggen" trekt alle sessies van de gebruiker in. Test het: log uit en speel daarna een eerder vastgelegd verzoek met de oude cookie of het oude token opnieuw af. Dat moet mislukken.

## Sessiebeveiliging en Content Security Policy

Bescherming van sessies en bescherming tegen XSS versterken elkaar. HttpOnly-cookies voorkomen dat geïnjecteerde scripts sessiecookies lezen, maar scripts kunnen binnen de pagina nog steeds namens de gebruiker handelen. Een Content Security Policy die scriptbronnen beperkt en inline scripts weigert, verkleint de kans dat geïnjecteerde code überhaupt draait. Samen maken ze van een XSS-bug in plaats van een mogelijke accountovername een veel kleiner probleem.

## Afwijkingen in Sessies Monitoren

Log sessie-events — inloggen, vernieuwen, uitloggen, intrekken, mislukte vernieuwing — met IP-bereiken en user agents. Stel meldingen in bij patronen zoals veel sessies voor één account vanuit verschillende landen binnen enkele minuten, het afgaan van de detectie van hergebruik van refresh tokens, of pieken in mislukte inlogpogingen. Gebruikers kunnen ook hun actieve sessies en recente inlogpogingen te zien krijgen, zodat ze zelf verdachte activiteit kunnen opmerken.

## Sessiegedrag Testen

Voeg geautomatiseerde tests toe voor: cookieattributen bij inlogantwoorden; geweigerde toegang na uitloggen met de oude cookie; ingetrokken sessies na een wachtwoordwijziging; rotatie van refresh tokens en detectie van hergebruik; CSRF-bescherming op endpoints die de staat wijzigen; en het afdwingen van de inactiviteitstime-out. Deze tests beschermen tegen regressies wanneer authenticatiecode opnieuw wordt gegenereerd of geherstructureerd.

## Sessies op Gedeelde en Openbare Apparaten

Apps die op gedeelde apparaten worden gebruikt — receptiebalies, klaslokalen, werkplaatsen, kiosken — hebben een speciale aanpak nodig. Bied een modus "gedeeld apparaat" met korte inactiviteitstime-outs, zonder "ingelogd blijven", met automatisch uitloggen aan het einde van de werkdag en snel wisselen van gebruiker via een pincode bovenop een sessie op apparaatniveau. Wis gevoelige data van de pagina als de sessie eindigt, zodat de terugknop eerdere schermen niet onthult; stel cacheheaders in op geauthenticeerde pagina's om te voorkomen dat browsers ze opslaan.

## Sessies in Mobiele Apps

Mobiele apps houden gebruikers doorgaans langer ingelogd, wat redelijk is omdat het apparaat zelf meestal beveiligd is. Bewaar tokens in de veilige opslag van het platform (Keychain of Keystore), niet in gewone lokale opslag; gebruik rotatie van refresh tokens; maak intrekking op afstand mogelijk vanuit de webapp ("op alle apparaten uitloggen"); en vereis bevestiging met biometrie of pincode voor gevoelige acties als de app financiële of gezondheidsdata verwerkt.

## Cookies van Derden en Ingesloten Apps

Wordt uw app ingesloten in andere sites (bijvoorbeeld als boekingswidget) of gebruikt hij authenticatie over domeinen heen, dan beïnvloeden beperkingen van browsers op cookies van derden de sessies. Plan hiervoor: geef de voorkeur aan eigen domeinen voor authenticatie, gebruik inlogflows met redirects in plaats van cookies in iframes, en test in browsers met strikte privacyinstellingen. Ingesloten widgets die op cookies van derden vertrouwen, werken voor een groeiend deel van de gebruikers vaak ongemerkt niet meer.

## Een Checklist voor Sessiebeveiliging

Bevestig vóór de lancering: sessiecookies zijn HttpOnly, Secure en SameSite, waar mogelijk met het voorvoegsel `__Host-`; geen tokens in localStorage; access tokens kortlevend, refresh tokens geroteerd met detectie van hergebruik; uitloggen en wachtwoordwijziging trekken sessies op de server in; inactiviteitstime-outs en absolute time-outs passen bij de gevoeligheid van de data; CSRF-bescherming actief op verzoeken die de staat wijzigen; een Content Security Policy aanwezig; geauthenticeerde pagina's niet gecachet door browsers; afwijkingen in sessies gelogd; en geautomatiseerde tests die dit gedrag dekken.

## Waarom Oprichters Zich Hier Druk om Moeten Maken

Fouten in sessies komen zelden naar boven in demo's, maar ze bepalen of één gestolen token of een gedeelde computer uitmondt in een accountovername. Ze zijn meestal goedkoop op te lossen — vooral configuratie en het gebruik van een volwassen authenticatieaanbieder — en duur om na een incident uit te leggen. Zet sessiebeveiliging vóór de lancering op dezelfde lijst als toegangsbeheer en betalingen.

## Vooraf en Daarna, Samengevat

Vooraf: tokens in localStorage, cookies zonder vlaggen, sessies die een maand duren, uitloggen dat alleen het token verbergt, geen CSRF-bescherming en geen intrekking na een wachtwoordwijziging. Daarna: HttpOnly-, Secure- en SameSite-cookies gebonden aan de host; kortlevende access tokens met geroteerde refresh tokens; intrekking op de server bij uitloggen en wachtwoordwijziging; time-outs passend bij het risico; CSRF-bescherming bij gevoelige acties; een Content Security Policy; gelogde afwijkingen; en tests die dat allemaal op zijn plek houden. De interface ziet er in beide gevallen hetzelfde uit — het verschil is of een gestolen token, een gedeelde computer of een kwaadaardige link kan uitmonden in het account van iemand anders.

## Eerste Stap

Log in op uw app, open de ontwikkelaarstools van de browser en kijk bij Application → Cookies en Local Storage. Ziet u een token in Local Storage of een sessiecookie zonder HttpOnly, begin dan daar.

## Waar LaunchStudio Past

LaunchStudio beoordeelt sessiebeheer bij elke controle van de authenticatie en vervangt eigen sessiecode meestal door de veilige standaarden van de authenticatieaanbieder, voegt correcte cookievlaggen toe, CSRF-bescherming, uitloggen en intrekken op de server, en een passende levensduur. LaunchStudio wordt aangedreven door Manifera, wiens CEO Herre Roelevink een achtergrond in cybersecurity heeft — inclusief het medeoprichten van CyberDevOps, nu CFLW Cyber Strategies — die een reviewcultuur vormt waarin beveiliging voorop staat. De engineers van Manifera werken in Ho Chi Minh-stad, met klantcontact via de Herengracht 420 in Amsterdam. Zie [de over-ons-pagina van Manifera](https://www.manifera.com/about-us/).

[Vraag een offerte tegen vaste prijs aan](https://launchstudio.eu/nl/#contact) voor een review van authenticatie en sessies.

## Praktijkvoorbeeld

### Een AI-Native Oprichter in Actie: Een App voor Vergaderruimtes Waarin Uitloggen Niet Uitlogde

Sem Evers, facilitair coördinator en oprichter in IJsselstein, bouwde Zaalvrij met Cursor: bedrijven in gedeelde kantoorgebouwen boeken vergaderruimtes, beheren bezoekers en krijgen maandelijkse facturen voor het gebruik. Zesentwintig bedrijven in vier gebouwen gebruikten het, vaak vanaf gedeelde receptiecomputers.

Een receptioniste meldde dat na het uitloggen op de gedeelde computer de terugknop van de browser de boekingen van een ander bedrijf liet zien — en dat doorklikken nog steeds werkte. De review legde uit waarom: Cursor had JWT-authenticatie geïmplementeerd met tokens in localStorage, 30 dagen geldig, en uitloggen verwijderde het token alleen uit de browser zonder het ongeldig te maken. Een gekopieerd token bleef werken. Cookies voor een functie "ingelogd blijven" misten de vlaggen HttpOnly en SameSite, formulieren voor het annuleren van boekingen hadden geen CSRF-bescherming, en een wachtwoordwijziging beëindigde andere sessies niet. Een reflected XSS in het veld voor de naam van een bezoeker betekende dat een speciaal gemaakte link het token uit localStorage had kunnen lezen.

In vier werkdagen vervingen de engineers van LaunchStudio de eigen JWT-afhandeling door sessies van Supabase Auth, sloegen ze refresh tokens op in HttpOnly-, Secure- en SameSite=Lax-cookies, verkortten ze de levensduur van access tokens, maakten ze sessies op de server ongeldig bij uitloggen en bij een wachtwoordwijziging, voegden ze een inactiviteitstime-out van acht uur toe voor accounts die als gebruik op een gedeelde computer zijn gemarkeerd, beschermden ze formulieren die de staat wijzigen met CSRF-tokens, losten ze de XSS op met output-escaping en een Content Security Policy, en voegden ze "overal uitloggen" toe.

**Resultaat:** Het probleem met de gedeelde computer verdween, en een latere beveiligingsvragenlijst van een grotere huurder werd zonder vervolgvragen beantwoord. Zaalvrij is sindsdien in gebruik genomen in nog twee kantoorgebouwen.

> *"Onze uitlogknop was een beleefde suggestie. Nu beëindigt hij de sessie echt."*
> — **Sem Evers, Oprichter, Zaalvrij (IJsselstein)**

**Kosten & Tijdlijn:** € 1.100 (versterking van sessies en cookies, CSRF-bescherming, oplossing voor XSS en migratie naar een authenticatieaanbieder) — afgerond in 4 werkdagen.

## Veelgestelde Vragen

### Is het opslaan van tokens in localStorage onveilig?

Het stelt ze bloot aan elk JavaScript op de pagina, waardoor een XSS-lek een accountovername wordt. HttpOnly-cookies voor refresh tokens en kortlevende access tokens in het geheugen zijn veiliger.

### Welke cookievlaggen horen sessiecookies te hebben?

HttpOnly, Secure en SameSite (Lax of Strict), met een beperkt pad en domein.

### Maakt uitloggen een token ongeldig?

Alleen als de server het intrekt. Veel AI-gegenereerde apps verwijderen het alleen uit de browser, waardoor het geldig blijft.

### Waarom beoordeelt Manifera sessies bij elke beveiligingscontrole?

Omdat fouten in sessies kleine bugs veranderen in accountovernames. De wortels van Manifera in cybersecurity maken sessies, tokens en cookies tot vaste onderdelen van elke review.

### Beïnvloeden veilige cookie-instellingen SEO of analytics?

Sessiecookies hebben geen invloed op SEO. Correcte beveiligingsheaders en HTTPS dragen bij aan vertrouwenssignalen voor browsers en zoekmachines, en goed afgebakende cookies voorkomen conflicten met analyticstools.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "Is het opslaan van tokens in localStorage onveilig?", "acceptedAnswer": { "@type": "Answer", "text": "Het stelt tokens bloot aan scripts op de pagina; gebruik HttpOnly-cookies voor refresh tokens en kortlevende access tokens in het geheugen." } },
    { "@type": "Question", "name": "Welke cookievlaggen horen sessiecookies te hebben?", "acceptedAnswer": { "@type": "Answer", "text": "HttpOnly, Secure en SameSite, met een beperkt pad en domein." } },
    { "@type": "Question", "name": "Maakt uitloggen een token ongeldig?", "acceptedAnswer": { "@type": "Answer", "text": "Alleen als het op de server wordt ingetrokken; veel AI-apps verwijderen het alleen in de browser." } },
    { "@type": "Question", "name": "Waarom beoordeelt Manifera sessies bij elke beveiligingscontrole?", "acceptedAnswer": { "@type": "Answer", "text": "Fouten in sessies veranderen kleine bugs in overnames; de wortels in cybersecurity maken ze tot vaste controles." } },
    { "@type": "Question", "name": "Beïnvloeden veilige cookie-instellingen SEO of analytics?", "acceptedAnswer": { "@type": "Answer", "text": "Niet direct SEO; HTTPS en headers ondersteunen vertrouwen, en afgebakende cookies voorkomen conflicten met analytics." } }
  ]
}
</script>
