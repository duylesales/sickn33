---
Titel: "Case Study: Graceful Degradation Implementeren bij een LLM-storing in 5 Dagen"
Keywords: Graceful Degradation, LLM-storing, AI SaaS-betrouwbaarheid, Fallback-model, OpenAI-storing, LaunchStudio, Manifera, Replit
Buyer Stage: Decision
---

# Case Study: Graceful Degradation Implementeren bij een LLM-storing in 5 Dagen

Elk AI SaaS-product heeft één enkel storingspunt waar de meeste oprichters pas over nadenken als het al te laat is: de LLM-provider zelf. Wanneer OpenAI of Anthropic een slechte dag heeft, gaat elk product zonder terugvalplan mee onderuit — niet vanwege een bug in de eigen code van de oprichter, maar vanwege een architectuur die nooit rekening hield met die mogelijkheid. Dit is het verhaal van Nadia, een oprichter wiens hele platform plat ging tijdens een storing van OpenAI van drie uur, en hoe LaunchStudio in vijf dagen graceful degradation implementeerde voor haar product, zodat de volgende storing een klein ongemak zou zijn in plaats van een bedrijfsbedreigende gebeurtenis.

## De drie uur die Nadia bijna haar beste klant kostten

Nadia bouwde met Replit een platform voor vergadernotities en actiepunten voor teams op afstand, waarbij GPT-4 het zware werk deed: het transcriberen van vergaderaudio, het samenvatten van belangrijke punten en het automatisch extraheren van actiepunten na elk gesprek. Het product werkte goed genoeg dat een bedrijf van 200 medewerkers net was ingestapt als haar grootste klant tot dan toe, met een proefperiode die zou bepalen of het bedrijfsbreed werd uitgerold.

Op de vierde dag van die proefperiode had OpenAI een regionale storing van iets meer dan drie uur. Nadia's platform had geen enkele vorm van terugval — elke API-aanroep naar OpenAI bleef gewoon hangen tot deze een time-out gaf, en omdat de frontend ook geen foutstatus-afhandeling had, zagen gebruikers een draaiende laadindicator die nooit tot een resultaat kwam. Vergadernotities van zes gesprekken die ochtend gingen stilletjes verloren — niet opgeslagen in een verminderde vorm, niet in een wachtrij gezet voor een nieuwe poging, gewoon weg, omdat de code ervan uitging dat de API-aanroep uiteindelijk zou slagen en er niets was voorzien voor het geval dat niet gebeurde.

De IT-verantwoordelijke van de proefklant merkte het meteen op en stelde een pijnlijke vraag in het gedeelde Slack-kanaal: "Wat gebeurt er als dit weer gebeurt, maar dan tijdens een bestuursvergadering?" Nadia had geen echt antwoord, en ze wist dat het ontbreken daarvan haar de deal kon kosten.

## Waarom "het werkte tijdens het testen" niets zegt over wat er gebeurt tijdens een storing

De ongemakkelijke waarheid waar Nadia mee moest dealen, is dat haar product tijdens ontwikkeling of QA nooit daadwerkelijk had gefaald, omdat de API van OpenAI meestal betrouwbaar genoeg is dat een oprichter die handmatig test zelden een echt storingsscenario triggert. Die betrouwbaarheid creëert een gevaarlijke blinde vlek: teams bouwen en leveren producten uit die hun faalpad nog nooit hebben doorlopen, omdat het faalpad nooit is gebouwd — er was niets om te doorlopen.

Dit is een structureel hiaat, geen codeerfout in de traditionele zin. Nadia's code was niet buggy; ze had gewoon geen mening over wat er moest gebeuren wanneer de AI-provider niet beschikbaar was. Drie specifieke hiaten stapelden zich op tijdens de storing:

- **Geen time-out of circuit breaker.** API-aanroepen naar OpenAI hadden geen geconfigureerde time-out, waardoor verzoeken oneindig bleven hangen in plaats van snel te falen en herstellogica te activeren.

- **Geen terugvalpad.** Er was geen secundair model, gecachet antwoord of verminderde functionaliteitsmodus — toen de primaire aanroep faalde, was er niets anders voor het systeem om te proberen.

- **Geen zichtbare foutstatus voor gebruikers.** De frontend had geen ontwerp voor "de AI is tijdelijk niet beschikbaar." Gebruikers zagen alleen een oneindig draaiende laadindicator, zonder enige aanwijzing over wat er gebeurde of wat te doen — en dat is wat een backend-storing veranderde in een zichtbaar vertrouwensprobleem.

## De vijfdaagse bouw: Falen tot een ontworpen ervaring maken

Nadia nam de dag na de storing contact op met LaunchStudio, met de beslissing over de proefperiode nog maar iets meer dan een week weg. De opdracht richtte zich op één specifiek, afgebakend doel: de volgende LLM-storing overleefbaar maken, zonder de kernproductervaring aan te raken die klanten al waardeerden.

**Dag 1-2: Circuit breakers en time-outs.** Engineers voegden expliciete time-outs toe aan elke LLM-aanroep en wikkelden deze in een circuit breaker-patroon — na een bepaald aantal opeenvolgende storingen binnen een kort venster stopt het systeem volledig met het versturen van verzoeken naar de falende provider gedurende een afkoelperiode, in plaats van elk nieuw verzoek te laten hangen en zich te laten opstapelen. Dit alleen al voorkwam het soort resource-uitputting dat Nadia's storing erger had gemaakt dan nodig, aangezien opgestapelde, hangende verzoeken serverbronnen consumeerden die andere gebruikers hadden kunnen bedienen.

**Dag 2-3: Een fallback naar een secundair model.** Het team koppelde een fallback naar een tweede provider voor de belangrijkste functie — het samenvatten van transcripties — zodat wanneer het primaire model niet beschikbaar was, het systeem automatisch doorschakelde naar de back-up in plaats van volledig te falen. Het fallback-model was niet zo sterk als GPT-4 voor genuanceerde samenvattingen, maar een iets minder gepolijste samenvatting die daadwerkelijk aankomt, is beter dan een perfecte die er nooit komt.

**Dag 3-4: Lokale wachtrijen voor niet-urgente verwerking.** Voor functies waarbij een fallback-model niet praktisch was — actiepunt-extractie, die een hogere nauwkeurigheid vereiste dan het fallback-model betrouwbaar kon leveren — implementeerde het team een lokale wachtrij. Ruwe transcripties werden onmiddellijk en betrouwbaar opgeslagen, ongeacht AI-beschikbaarheid, waarbij verwerking automatisch opnieuw werd geprobeerd zodra de primaire provider herstelde. Niets ging ooit meer stilletjes verloren; in het slechtste geval kwam een resultaat een paar minuten later aan in plaats van nooit.

**Dag 4-5: Eerlijke, ontworpen foutstatussen in de UI.** De frontend werd bijgewerkt om verminderde en volledig gefaalde statussen expliciet te detecteren, waarbij de oneindige laadindicator werd vervangen door een duidelijk bericht: "We ondervinden een tijdelijke vertraging bij de AI-verwerking — uw vergadering is opgeslagen en de notities zijn binnenkort klaar." Gebruikers konden hun ruwe transcript direct zien, zelfs voordat de door AI gegenereerde samenvatting had ingehaald, zodat een gesprek zelfs tijdens een storing nooit volledig onzichtbaar was.

## Het resultaat: De volgende storing was een non-event

Drie weken na de release van de fix had OpenAI een nieuwe, kortere storing — deze keer ongeveer 40 minuten. Nadia's platform schakelde automatisch over naar het secundaire model voor samenvatting, zette de actiepunt-extractie in de wachtrij voor een nieuwe poging, en toonde de hele tijd een duidelijk statusbericht aan gebruikers. Er gingen geen vergadernotities verloren. Er werden geen supporttickets ingediend. De IT-verantwoordelijke van de proefklant, degene die de oorspronkelijke zorg had geuit, merkte helemaal niets — en dat was precies het punt.

Nadia's proefperiode werd twee weken later omgezet in een volledige bedrijfsbrede uitrol. Toen rechtstreeks werd gevraagd wat de doorslag gaf, noemde de IT-verantwoordelijke twee dingen: het product zelf, en het feit dat Nadia terugkwam met een concreet antwoord op "wat gebeurt er als dit weer gebeurt" in plaats van een belofte om ernaar te kijken.

## De bredere les: Betrouwbaarheid is een functie die je moet ontwerpen, niet iets dat je gratis krijgt

Graceful degradation gaat eigenlijk niet echt over de LLM-provider — het gaat over accepteren dat elke externe afhankelijkheid uiteindelijk zal falen, en van tevoren beslissen hoe "goed falen" eruitziet in plaats van dat live te ontdekken, ten overstaan van een klant, tijdens een storing. Het patroon dat Nadia's product nodig had — time-outs, circuit breakers, terugvalpaden en eerlijke UI-statussen — is net zo goed van toepassing op betalingsverwerkers, e-mailbezorgdiensten en elke andere externe API waar een product van afhankelijk is om te functioneren.

De reden dat dit bij de meeste door AI-builders gegenereerde producten wordt overgeslagen, is geen nalatigheid; het is dat het faalpad onzichtbaar is tot de dag dat het nodig is, en niets in een typische ontwikkel- of demo-cyclus dwingt een oprichter om te bouwen voor een scenario dat, statistisch gezien, deze week waarschijnlijk niet gebeurt. De kosten van het overslaan ervan zijn echter asymmetrisch: de meeste weken kost het niets, en dan kost het in één week een proefklant, een bestuursvergadering aan verloren notities, of erger.

Er is ook een monitoringdimensie die oprichters vaak onderschatten. Vóór de fix had Nadia helemaal geen alerting gekoppeld aan mislukte LLM-aanroepen — het eerste dat ze van de storing wist, was het Slack-bericht van de proefklant, uren nadat deze was begonnen. Als onderdeel van dezelfde opdracht koppelde LaunchStudio de statuswijzigingen van de circuit breaker aan een monitoringdashboard met een Slack-melding, zodat een toekomstige storing binnen enkele seconden nadat de faaldrempel is overschreden een melding naar Nadia's team stuurt, in plaats van via een ontevreden klant te worden ontdekt. Weten van een verminderde dienst vóórdat een klant het u moet vertellen, is op zichzelf vaak het verschil tussen een kleine operationele notitie en een vertrouwensschadend incident.

## Belangrijkste inzichten

- De meeste AI SaaS-producten hebben hun faalpad nog nooit daadwerkelijk doorlopen, omdat LLM-providers meestal betrouwbaar genoeg zijn dat handmatig testen zelden een echt storingsscenario triggert — wat betekent dat het faalpad vaak helemaal niet bestaat totdat het tijdens een echt incident wordt afgedwongen.

- Circuit breakers en expliciete time-outs voorkomen dat een enkele providerstoring escaleert tot resource-uitputting veroorzaakt door verzoeken die oneindig blijven hangen en zich opstapelen.

- Een fallback naar een secundair model, zelfs een met iets lagere outputkwaliteit, is bijna altijd beter dan een volledige storing — een bruikbaar resultaat dat te laat aankomt, is beter dan helemaal geen resultaat.

- Eerlijke, ontworpen foutstatussen in de UI veranderen een storing van een onzichtbaar vertrouwensprobleem in een zichtbaar, goed afgehandeld probleem; gebruikers tolereren vertragingen veel beter dan stilte.

- Samenwerken met betrouwbaarheidsspecialisten zoals LaunchStudio (ondersteund door de 11+ jaar ervaring in production engineering van Manifera, vertrouwd door enterprise-klanten zoals Vodafone en TNO) kan graceful degradation voor LLM-storingen binnen ongeveer een week implementeren, waardoor een bedrijfsbedreigende gebeurtenis een non-event wordt voordat het u een klant kost.

## Wacht niet op een storing om erachter te komen dat uw product geen fallback heeft

Als uw AI SaaS-platform nog nooit een echte LLM-providerstoring heeft overleefd, is dat niet omdat het veerkrachtig is — het is omdat het nog niet is getest.

LaunchStudio wordt geëxploiteerd door **Manifera**, een internationaal software-engineeringbedrijf opgericht in 2014 en geleid door Oprichter & Managing Director **Herre Roelevink**. Zoals Roelevink het verwoordt: *"We zien een verschuiving in softwarebehoeften. De uitdaging is niet langer om goede ideeën om te zetten in software. Het gaat nu om de architectuur en beveiliging die nodig zijn om die producten tot wasdom te brengen. Wij hebben elf jaar ervaring in precies dat vakgebied."* Door "Nederlands management te combineren met Vietnamees meesterschap", onderhoudt Manifera hoofdkantoren in **Amsterdam, Nederland** (Herengracht 420), een Aziatische hub in **Singapore** (100 Tras Street) en een primair ontwikkelcentrum in **Ho Chi Minh-stad, Vietnam** (Pho Quang Street). Via LaunchStudio nemen senior engineeringteams uw bestaande door AI gebouwde frontend en implementeren ze productieklare beveiligingscontroles, live betalingsgateways, veilige hosting en monitoring — waardoor uw prototype binnen 1 tot 3 weken verandert in een veilige, compliant MVP, zonder dat een volledige rebuild nodig is. [Vraag vandaag nog een gratis offerte aan](https://launchstudio.eu/en/#contact) of bekijk hoe het [maatwerk software-ontwikkelteam van Manifera](https://www.manifera.com/services/custom-software-development/) production-hardening aanpakt voor AI-gegenereerde codebases.

## Echt voorbeeld

### Een AI-native oprichter in actie: AI-recruitmentscreener

Ingrid, een startup-oprichter, gebruikte **v0** om een AI-gestuurd platform voor het screenen van cv's te bouwen voor recruitmentbureaus. Tijdens een druk wervingsseizoen zorgde een storing van 25 minuten bij Anthropic ervoor dat haar platform tientallen kandidaatbeoordelingen midden in het proces stilletjes liet vallen, waardoor recruiters niet konden zien welke kandidaten daadwerkelijk waren gescreend en welke gewoon uit de wachtrij waren verdwenen.

Ingrid werkte samen met **LaunchStudio (door Manifera)** om een graceful degradation-laag te bouwen. Het engineeringteam voegde persistente taakwachtrijen toe zodat elk screeningverzoek een providerstoring overleefde, implementeerde automatische nieuwe pogingen met exponentiële backoff, en voegde een duidelijke "verwerking vertraagd"-status toe die zichtbaar was voor recruiters in plaats van een stille storing.

**Resultaat:** Ingrid's platform overleefde de volgende providerstoring zonder verloren beoordelingen en zonder verwarring bij recruiters, vergeleken met tientallen stilletjes verloren kandidaten vóór de fix.

**Kosten & Doorlooptijd:** € 1.400 (Launch Ready Pakket) — geïmplementeerd en geverifieerd in 5 werkdagen.

---

---

---
## Veelgestelde Vragen

### Wat is graceful degradation in de context van een AI SaaS-product?

Graceful degradation is de praktijk om een systeem zo te ontwerpen dat wanneer een kernafhankelijkheid — zoals een LLM-provider — niet beschikbaar of traag wordt, het product in een verminderde maar nog steeds bruikbare vorm blijft functioneren, in plaats van volledig te falen. Dit omvat fallback-modellen, verzoekwachtrijen, circuit breakers en duidelijke foutmeldingen in de UI.

### Waarom ving testen Nadia's gebrek aan een fallback niet op vóór de storing?

Omdat LLM-providers meestal betrouwbaar genoeg zijn dat handmatig testen tijdens ontwikkeling zelden een echt storingsscenario triggert. Het faalpad was nooit gebouwd, dus er was niets om te testen — het hiaat was structureel, geen bug die testen normaal gesproken zou opvangen.

### Hoe lang duurt het om graceful degradation voor LLM-storingen te implementeren?

Voor een gerichte bouw zoals die van Nadia — time-outs, circuit breakers, een fallback naar een secundair model, lokale wachtrijen en eerlijke UI-foutstatussen — is vijf werkdagen gebruikelijk, zonder dat wijzigingen aan de kerngebruikerservaring van het product nodig zijn.

### Tast het toevoegen van een fallback-model de outputkwaliteit aan?

Dat kan, licht, voor de specifieke functie die de fallback gebruikt — Nadia's back-upmodel produceerde iets minder gepolijste samenvattingen dan GPT-4. Maar een bruikbaar resultaat dat tijdens een storing aankomt, is bijna altijd te verkiezen boven een volledige storing, en de fallback wordt alleen ingeroepen wanneer de primaire provider daadwerkelijk niet beschikbaar is.

### Wat is het verschil tussen een circuit breaker en gewoon een time-out toevoegen?

Een time-out voorkomt dat een individueel verzoek oneindig blijft hangen, maar zonder circuit breaker probeert elk nieuw verzoek tijdens een storing de aanroep nog steeds en krijgt het nog steeds een time-out, waardoor resourcegebruik zich opstapelt. Een circuit breaker houdt recente storingen bij en stopt volledig met het versturen van verzoeken naar een falende provider gedurende een afkoelperiode, waardoor die resource-uitputting de impact van de storing niet verder verergert.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Wat is graceful degradation in de context van een AI SaaS-product?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Graceful degradation is de praktijk om een systeem zo te ontwerpen dat wanneer een kernafhankelijkheid — zoals een LLM-provider — niet beschikbaar of traag wordt, het product in een verminderde maar nog steeds bruikbare vorm blijft functioneren, in plaats van volledig te falen. Dit omvat fallback-modellen, verzoekwachtrijen, circuit breakers en duidelijke foutmeldingen in de UI."
      }
    },
    {
      "@type": "Question",
      "name": "Waarom ving testen Nadia's gebrek aan een fallback niet op vóór de storing?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Omdat LLM-providers meestal betrouwbaar genoeg zijn dat handmatig testen tijdens ontwikkeling zelden een echt storingsscenario triggert. Het faalpad was nooit gebouwd, dus er was niets om te testen — het hiaat was structureel, geen bug die testen normaal gesproken zou opvangen."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe lang duurt het om graceful degradation voor LLM-storingen te implementeren?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Voor een gerichte bouw zoals die van Nadia — time-outs, circuit breakers, een fallback naar een secundair model, lokale wachtrijen en eerlijke UI-foutstatussen — is vijf werkdagen gebruikelijk, zonder dat wijzigingen aan de kerngebruikerservaring van het product nodig zijn."
      }
    },
    {
      "@type": "Question",
      "name": "Tast het toevoegen van een fallback-model de outputkwaliteit aan?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Dat kan, licht, voor de specifieke functie die de fallback gebruikt — Nadia's back-upmodel produceerde iets minder gepolijste samenvattingen dan GPT-4. Maar een bruikbaar resultaat dat tijdens een storing aankomt, is bijna altijd te verkiezen boven een volledige storing, en de fallback wordt alleen ingeroepen wanneer de primaire provider daadwerkelijk niet beschikbaar is."
      }
    },
    {
      "@type": "Question",
      "name": "Wat is het verschil tussen een circuit breaker en gewoon een time-out toevoegen?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Een time-out voorkomt dat een individueel verzoek oneindig blijft hangen, maar zonder circuit breaker probeert elk nieuw verzoek tijdens een storing de aanroep nog steeds en krijgt het nog steeds een time-out, waardoor resourcegebruik zich opstapelt. Een circuit breaker houdt recente storingen bij en stopt volledig met het versturen van verzoeken naar een falende provider gedurende een afkoelperiode, waardoor die resource-uitputting de impact van de storing niet verder verergert."
      }
    }
  ]
}
</script>
