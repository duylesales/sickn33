---
Titel: "Wat een met AI gegenereerde applicatie nog steeds nodig heeft voordat echte gebruikers arriveren"
Trefwoorden: ai generated application, ai generated tool, ai coding, LaunchStudio, Manifera
Koperfase: Overweging
Doelgroep: SaaS-oprichter Scale-Up
---

# Wat een met AI gegenereerde applicatie nog steeds nodig heeft voordat echte gebruikers arriveren

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Wat een met AI gegenereerde applicatie nog steeds nodig heeft voordat echte gebruikers arriveren",
  "description": "Een technische verdieping in het afhandelen van sessie-tokens, gefocust op onjuist geverifieerde JWT's.",
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
  "datePublished": "2026-07-28",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://launchstudio.eu/nl/blog/what-an-ai-generated-application-still-needs-before-real-users"
  }
}
</script>

Een met AI gegenereerde applicatie die inlogs van betaalde abonnees afhandelt krijgt het zichtbare gedeelte van authenticatie typisch bij de eerste poging al goed – een inlogformulier dat geldige inloggegevens accepteert en ongeldige weigert. Wat frequent niet dezelfde controle krijgt is het token dat de inlog daadwerkelijk achteraf uitgeeft. En specifiek of dat token op de juiste manier geverifieerd is, correct afgebakend is, en ingesteld is om daadwerkelijk te verlopen.

## Wat een JWT-token verondersteld wordt te garanderen

Een JSON Web Token (JWT), algemeen gebruikt om een ingelogde sessie te vertegenwoordigen, is cryptografisch ondertekend. Zodat een server kan verifiëren dat er niet mee geknoeid is en dat het oprecht afkomstig is van een legitieme inlog. Die garantie houdt alleen stand als de server de handtekening op elk verzoek daadwerkelijk verifieert – een token dat simpelweg wordt gedecodeerd en gelezen, zonder dat de handtekening wordt gecontroleerd, biedt überhaupt geen echte beveiligingsgarantie.

## Waarom het overslaan van handtekeningverificatie een makkelijke, onzichtbare fout is

Het decoderen van een JWT om de inhoud ervan te lezen (welke gebruiker, welke machtigingen) is een eenvoudige, veelvoorkomende handeling. Code die een token correct decodeert kan tijdens het testen perfect lijken te werken – een legitiem uitgegeven token decodeert elke keer naar de correcte, verwachte informatie. De afzonderlijke stap van het daadwerkelijk verifiëren dat de handtekening van het token geldig is produceert tijdens normaal, eerlijk gebruik geen enkel ander zichtbaar resultaat.

## Waarom deze kloof ernstig wordt op het moment dat iemand zijn eigen token opstelt

Als handtekeningverificatie wordt overgeslagen, hoeft een token überhaupt niet legitiem te zijn uitgegeven – iedereen die de basisstructuur van het token begrijpt kan zijn eigen token construeren en beweren elke willekeurige gebruiker of elk machtigingsniveau te zijn. Een server die alleen decodeert zonder te verifiëren zal een zelf opgesteld token als echt accepteren.

## Waarom verloop een afzonderlijk, even belangrijk onderdeel is

Voorbij handtekeningverificatie heeft een token een redelijke vervaltijd nodig waarna het niet langer geaccepteerd wordt. Zonder dit blijft een eenmaal buitgemaakt token voor onbepaalde tijd bruikbaar. Een sessietoken dat op de dag van de productlancering is uitgegeven en een jaar later nog steeds stilletjes geldig is, is het standaardresultaat van het nooit hebben ingesteld van een vervaldatum.

## Wat een complete herstelling inhoudt

Een correcte implementatie verifieert de handtekening van elk token bij elk verzoek, dwingt een redelijke vervaltijd af met een werkend verversingsmechanisme (refresh flow), en weigert alles wat voor een van beide controles zakt. [LaunchStudio](https://launchstudio.eu/nl/) auditeert exact dit patroon als onderdeel van haar authenticatie-beoordelingsproces, ondersteund door Manifera's 11+ jaar ervaring met Auth0, Supabase Auth, en op maat gemaakte op JWT gebaseerde systemen.

Manifera's audits voor sessie- en tokenbeveiliging worden uitgevoerd door het engineeringteam in het ontwikkelingscentrum in Ho Chi Minh-stad aan de Pho Quang-straat, gecoördineerd met het hoofdkantoor in Amsterdam aan de Herengracht 420.

[Praat met een ingenieur die met AI gegenereerde code begrijpt](https://launchstudio.eu/nl/#contact).

## Andere Sessiezwakheden Die Samengaan met Ontbrekende Handtekeningverificatie

Een ontbrekende handtekeningverificatie op JSON Web Tokens komt zelden alleen — het duikt doorgaans op naast een cluster van gerelateerde zwakheden in de sessie-afhandeling die tijdens dezelfde controle direct moeten worden meegenomen:

- **Waar het token aan de client-zijde wordt opgeslagen** — een JWT die in `localStorage` wordt bewaard, kan worden uitgelezen door elk script dat op de pagina draait, inclusief een kwaadaardig script dat is geïnjecteerd via een niet-gerelateerd cross-site scripting (XSS) lek. Een correct geconfigureerd `httpOnly`-cookie is daarentegen voor geen enkel paginascript toegankelijk.
- **Rotatie van refresh tokens** — een langdurig geldig refresh token dat voor onbepaalde tijd wordt hergebruikt in plaats van bij elk gebruik te worden geroteerd en ongeldig gemaakt, geeft een eenmalige diefstal dezelfde oneindige waarde als een gestolen permanent wachtwoord.
- **Intrekking bij uitloggen of wachtwoordwijziging** — op "uitloggen" klikken moet het eerdere token daadwerkelijk onbruikbaar maken, en niet alleen verwijderen uit het huidige browsertabblad. Evenzo moet het wijzigen van een wachtwoord elke andere actieve sessie die aan dat account is gekoppeld direct ongeldig maken.
- **Claims volgens het 'least-privilege' principe** — een token dat brede beheerdersrechten codeert voor elke ingelogde gebruiker, in plaats van uitsluitend de minimale rechten die die specifieke gebruiker daadwerkelijk nodig heeft, verandert elke toekomstige fout in de token-afhandeling in een direct catastrofaal beveiligingslek.

Geen van deze vier punten vereist een fundamenteel andere benadering van authenticatie — gevestigde providers zoals Auth0 of Supabase Auth handelen dit standaard correct af wanneer hun out-of-the-box stromen worden gebruikt zoals bedoeld. Het risico ontstaat vrijwel altijd in de maatwerklogica die er bovenop wordt gebouwd: een zelfgeschreven verversingsmechanisme, een handmatige middleware-functie of een helper voor tokenuitlezing die later is toegevoegd zonder dezelfde strenge controle. Een werkend inlogscherm bewijst dat de voordeur stevig is; het zegt niets over de vraag of elke deur erachter op exact dezelfde manier op slot gaat.

## Echt voorbeeld

### Een AI-native oprichter in actie: Het abonneetoken dat nooit verliep

Britt, een voormalig tijdschriftredacteur die oprichter werd in Hoorn, bouwde LeesKring, een AI-ondersteund platform voor nieuwsbrieven en kwaliteitsjournalistiek gebouwd met Lovable, dat artikelen afschermt achter een betaalde abonnees-inlog.

De oude sessie van een vertrokken teamlid, die maanden eerder tijdens de ontwikkeling werd gebruikt, verleende nog steeds volledige toegang op een apparaat waarvan niemand zich herinnerde dat het ooit was ingelogd. Britt ontdekte het alleen omdat ze toevallig ongebruikelijke activiteit opmerkte tijdens het beoordelen van de statistieken. LaunchStudio's beoordeling vond dat de tokens van het platform überhaupt geen vervaldatum hadden ingesteld. En erger nog: dat de server tokens alleen decodeerde om de inhoud te lezen, zonder ooit de cryptografische handtekening te verifiëren.

**Resultaat:** LaunchStudio implementeerde een correcte handtekeningverificatie bij elk verzoek en voegde een redelijke tokenvervaldatum toe met een werkende verversingsstroom. Dit sloot zowel het risico op vervalsing als het risico op een onbeperkte sessie.

> *"Ik kwam er bijna per ongeluk achter, puur door iets op te merken in de statistieken wat niet helemaal logisch was. Er was geen foutmelding of waarschuwing die me op zichzelf verteld zou hebben dat dit überhaupt een mogelijkheid was."*
> — **Britt Hendriks, Oprichter, LeesKring (Hoorn)**

**Kosten en tijdlijn:** € 2.300 (JWT-verificatie en uitharding van sessieverloop) — voltooid in 7 werkdagen.

---

## Veelgestelde vragen

### Waarom zou een JWT-token in de browser ooit worden geaccepteerd zonder dat de handtekening wordt gecontroleerd?

Omdat een AI-codeertool of een haastig geschreven middleware-functie de payload van het token kan decoderen om gebruikersgegevens zoals een e-mailadres of gebruikers-ID uit te lezen, zonder de cryptografische verificatiestap aan te roepen die bevestigt dat het token daadwerkelijk door de geautoriseerde server is uitgegeven en niet onderweg is gemanipuleerd.

### Zou een verificatiekloof in handtekeningen zoals deze zichtbaar zijn voor gebruikers tijdens het normale inloggen?

Nee, in het geheel niet — legitieme gebruikers die inloggen ontvangen een geldig ondertekend token en het systeem logt hen vlekkeloos in. De kwetsbaarheid bestaat uitsluitend in wat het systeem toestaat wanneer iemand opzettelijk een gewijzigd of ongetekend token aanbiedt, waardoor het onzichtbaar blijft totdat het gericht wordt getest.

### Manifera heeft authenticatiesystemen geïmplementeerd over enterprise-klanten — helpt die achtergrond specifiek bij het beoordelen van token-afhandeling?

Ja, aanzienlijk — enterprise-authenticatievereisten dwingen een grondig begrip af van standaarden zoals OAuth2, OIDC en JWT-levenscycli. Ingenieurs met die achtergrond inspecteren sessie-afhandeling met een getraind oog voor subtiele configuratiefouten die minder ervaren ontwikkelaars gemakkelijk over het hoofd zien.

### Is dit gerelateerd aan de visie van Herre Roelevink dat AI-tools uitstekend zijn in functies maar zwak in beveiligingsrandgevallen?

Ja, direct — een inlogstroom genereren die gebruikers toelaat is een standaardtaak die AI-assistenten moeiteloos produceren. Het afdwingen van strenge cryptografische verificatie bij afwijkende netwerkpakketten vereist echter diepgaande domeinkennis die niet vanzelfsprekend in een beknopte prompt besloten ligt.

### Wat is de snelste manier voor een oprichter om te controleren of zijn eigen tokens cryptografisch worden geverifieerd?

Door een bestaand geldig token uit de browserdeveloper tools te kopiëren, de payload handmatig te wijzigen (bijvoorbeeld door het gebruikers-ID aan te passen) zonder de handtekening opnieuw te berekenen, en dat token mee te sturen naar een beveiligd API-eindpunt. Als de server het verzoek honoreert in plaats van een 401 Unauthorized terug te geven, ontbreekt de handtekeningcontrole.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Waarom zou een JWT-token in de browser ooit worden geaccepteerd zonder dat de handtekening wordt gecontroleerd?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Omdat een AI-codeertool of een haastig geschreven middleware-functie de payload van het token kan decoderen om gebruikersgegevens zoals een e-mailadres of gebruikers-ID uit te lezen, zonder de cryptografische verificatiestap aan te roepen die bevestigt dat het token daadwerkelijk door de geautoriseerde server is uitgegeven en niet onderweg is gemanipuleerd."
      }
    },
    {
      "@type": "Question",
      "name": "Zou een verificatiekloof in handtekeningen zoals deze zichtbaar zijn voor gebruikers tijdens het normale inloggen?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Nee, in het geheel niet — legitieme gebruikers die inloggen ontvangen een geldig ondertekend token en het systeem logt hen vlekkeloos in. De kwetsbaarheid bestaat uitsluitend in wat het systeem toestaat wanneer iemand opzettelijk een gewijzigd of ongetekend token aanbiedt, waardoor het onzichtbaar blijft totdat het gericht wordt getest."
      }
    },
    {
      "@type": "Question",
      "name": "Manifera heeft authenticatiesystemen geïmplementeerd over enterprise-klanten — helpt die achtergrond specifiek bij het beoordelen van token-afhandeling?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ja, aanzienlijk — enterprise-authenticatievereisten dwingen een grondig begrip af van standaarden zoals OAuth2, OIDC en JWT-levenscycli. Ingenieurs met die achtergrond inspecteren sessie-afhandeling met een getraind oog voor subtiele configuratiefouten die minder ervaren ontwikkelaars gemakkelijk over het hoofd zien."
      }
    },
    {
      "@type": "Question",
      "name": "Is dit gerelateerd aan de visie van Herre Roelevink dat AI-tools uitstekend zijn in functies maar zwak in beveiligingsrandgevallen?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ja, direct — een inlogstroom genereren die gebruikers toelaat is een standaardtaak die AI-assistenten moeiteloos produceren. Het afdwingen van strenge cryptografische verificatie bij afwijkende netwerkpakketten vereist echter diepgaande domeinkennis die niet vanzelfsprekend in een beknopte prompt besloten ligt."
      }
    },
    {
      "@type": "Question",
      "name": "Wat is de snelste manier voor een oprichter om te controleren of zijn eigen tokens cryptografisch worden geverifieerd?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Door een bestaand geldig token uit de browserdeveloper tools te kopiëren, de payload handmatig te wijzigen (bijvoorbeeld door het gebruikers-ID aan te passen) zonder de handtekening opnieuw te berekenen, en dat token mee te sturen naar een beveiligd API-eindpunt. Als de server het verzoek honoreert in plaats van een 401 Unauthorized terug te geven, ontbreekt de handtekeningcontrole."
      }
    }
  ]
}
</script>
