---
Titel: "Wat de technici van LaunchStudio daadwerkelijk doen in de eerste 48 uur van een nieuw project"
Trefwoorden: ai app dev, ai prototype to production, engineering onboarding, ai code review process
Koperfase: Overweging
Doelgroep: AI-Native oprichter (niet-technisch)
---
# Wat de technici van LaunchStudio daadwerkelijk doen in de eerste 48 uur van een nieuw project

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Wat de technici van LaunchStudio daadwerkelijk doen in de eerste 48 uur van een nieuw project",
  "description": "Een blik achter de schermen van LaunchStudio's proces voor de eerste 48 uur bij ai app dev-projecten, aan de hand van de onboarding van een echte oprichter, van read-only beoordeling tot fixplan.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2026-07-25",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/first-48-hours-new-project" }
}
</script>

De meeste oprichters die een prototype overdragen, hebben geen idee wat er aan de andere kant gebeurt. U stuurt een link naar een repository, misschien een Loom-video die uitlegt wat de app moet doen, en dan... stilte, totdat iemand u vertelt wat er mis is mee. Die kloof voelt risicovol als u nog nooit met een engineeringteam hebt gewerkt. Dus hier is precies wat er gebeurt in de eerste 48 uur nadat een project op ons bureau belandt, aan de hand van een echt project als leidraad: een enquêtetool genaamd MeetGoed, gebouwd in Cursor door een oprichter genaamd Sven Kramer uit Breda.

Sven had MeetGoed gebouwd om evenementorganisatoren gestructureerde feedback te laten verzamelen zonder te worstelen met SurveyMonkey-sjablonen. Het product werkte. Demo's verliepen soepel. Hij had het nog nooit door een professionele technicus laten aanraken voordat hij het naar ons stuurde, wat typisch is voor ai app dev-projecten die beginnen als één persoon en een chatvenster.

## Uur 0-4: de read-only ronde

Niemand raakt de codebase aan in de eerste vier uur. Een technicus kloont de repository, start deze lokaal op, en leest — elke route, elke database-aanroep, elke verwijzing naar een omgevingsvariabele — zonder ook maar één regel te wijzigen. Het doel is een mentale kaart: wat doet deze app daadwerkelijk, versus wat de oprichter denkt dat hij doet.

Voor MeetGoed leverde deze ronde binnen ongeveer negentig minuten het eerste rode vlaggetje op: API-sleutels voor de e-maildienst waren rechtstreeks hardcoded in een client-side bestand, zichtbaar voor iedereen die de ontwikkelaarstools van de browser opende. Sven had er geen idee van. Cursor had een werkende integratie gegenereerd; het had geen veilige gegenereerd, en er is geen reden waarom het dat wel zou doen — de tool optimaliseerde voor "de e-mails worden verzonden," niet voor "de e-mails worden veilig verzonden."

## Uur 4-16: kwetsbaarheidstriage

Hier verandert de kaart uit fase één in een geprioriteerde lijst. Niet alles wat gevonden wordt, krijgt dezelfde behandeling. Onze technici verdelen bevindingen in drie bakken: oplossen voordat iets anders productie raakt, oplossen voordat de volgende functie live gaat, en uiteindelijk oplossen.

Voor Svens project stapelden zich drie items op elkaar in de bak "eerst oplossen," wat gebruikelijk is — problemen in door AI gegenereerde code komen zelden alleen voor:

- De blootgestelde API-sleutels, al genoemd, die onmiddellijk naar de serverzijde moesten verhuizen.
- Geen rate limiting op het enquête-inzendpunt, wat betekende dat één script de database kon overspoelen met nepreacties of Svens e-mailrekening in een middag kon opblazen.
- Ontbrekende invoervalidatie op verschillende formuliervelden, wat betekende dat de backend vertrouwde op alles wat de frontend stuurde — een gat dat AI-codeertools vaak open laten omdat validatielogica in een demo niet visueel opvalt.

Geen van deze zou in een productdemo zijn opgedoken. Alle drie zouden ze in de eerste week met echt verkeer zijn opgedoken.

## Uur 16-36: het fixplan en het gesprek met de oprichter

Tegen uur zestien is er meestal een document, niet alleen een gesprek — een schriftelijke lijst van wat er is gevonden, waarom het ertoe doet in gewone taal, en wat de fix inhoudt. Dit is bewust geen muur van jargon. Sven kreeg een telefoontje waarin het probleem met de API-sleutel werd uitgelegd als "op dit moment kan iedereen die de browserconsole opent het wachtwoord van uw e-mailaccount zien," wat een zin is waar een niet-technische oprichter meteen naar kan handelen.

Dit is ook de fase waarin de scope wordt vastgelegd. Onze technici worden ondersteund door Manifera, een softwareontwikkelingsbedrijf met meer dan 11 jaar ervaring in productie-engineering, en die ervaring komt hier vooral naar voren: weten welke fixes snel zijn en welke complexiteit verbergen. Het team dat aan Svens beoordeling werkte, maakt deel uit van dezelfde in Amsterdam gevestigde groep die LaunchStudio's Europese activiteiten runt, en zij hebben dit exacte gestapelde patroon — blootgestelde sleutels, geen rate limiting, geen validatie — vaak genoeg gezien om te weten dat de volgorde ertoe doet. Los eerst validatie op en de rate limiter heeft minder rommelig verkeer om uit te filteren.

## Uur 36-48: wat live gaat, wat wacht

Het laatste stuk is waar de prioritaire fixes daadwerkelijk worden geschreven, getest tegen de bestaande frontend, en bevestigd dat ze niets breken waar Svens gebruikers al op vertrouwden. We raken zijn UI niet aan. De belofte achter LaunchStudio is productie-infrastructuur zonder een frontend-herbouw, en die belofte wordt hier het hardst getest, in de eerste 48 uur, wanneer het het snelst zou zijn om gewoon vanaf nul te herschrijven in plaats van eromheen te werken.

Als u wilt zien hoe dit past in het bredere traject, loopt onze [procesomschrijving](https://launchstudio.eu/en/#process) door wat er na deze eerste twee dagen gebeurt. Voor teams die evalueren of hun eigen codebase dit soort ronde nodig heeft voordat deze live gaat, volgt Manifera's werk in [softwareontwikkeling op maat](https://www.manifera.com/services/custom-software-development/) dezelfde eerst-lezen, dan-oplossen-discipline op grotere schaal.

## Echt voorbeeld

### Een AI-native oprichter in actie: MeetGoeds eerste weekendbeoordeling

Sven Kramer bouwde MeetGoed alleen, over meerdere weekenden, met Cursor voor het grootste deel van de backendlogica voor het aanmaken van enquêtes, het verzamelen van reacties en e-mailmeldingen aan organisatoren. Het werkte goed genoeg dat twee lokale evenementenbedrijven al hadden ingestemd met een pilot. Hij had zelf geen regel van de gegenereerde code aangeraakt en had geen manier om te beoordelen of het veilig was om voor echte klanten te zetten.

De eerste 48-uursbeoordeling van onze technici vond de hierboven beschreven gestapelde problemen: hardcoded API-sleutels zichtbaar aan client-zijde, geen rate limiting op inzendingen, en formuliervelden zonder validatie aan de serverzijde. Elk van deze problemen apart was een beheersbare fix. Samen betekenden ze dat MeetGoed één nieuwsgierige bezoeker verwijderd was van een gelekt e-mailwachtwoord, een overspoelde inbox, of gecorrumpeerde enquêtegegevens.

De fix verplaatste de e-mailcredentials naar de serverzijde achter een omgevingsvariabele, voegde verzoekthrottling toe aan het inzendpunt, en legde validatie aan op elk publiek toegankelijk formulierveld — allemaal zonder te veranderen hoe MeetGoed eruitzag of aanvoelde voor Svens pilotgebruikers. Hij hield zijn frontend precies zoals Cursor die had gebouwd.

**Resultaat:** MeetGoed lanceerde zijn twee pilotprogramma's op schema, waarbij de oprichter potentiële evenementenklanten eerlijk kon vertellen dat de datapijplijn professioneel was beoordeeld.

> *"Ik dacht dat het opsturen van de code een herbouw zou betekenen. In plaats daarvan vertelden ze me wat er daadwerkelijk kapot was en losten alleen dat op. Ik begrijp rate limiting nog steeds niet helemaal, maar ik begrijp nu waarom ik het nodig had."*
> — **Sven Kramer, oprichter, MeetGoed (Breda)**

**Kosten en tijdlijn:** € 1.200 (beveiligingstriage en fixes voor blootgestelde sleutels, rate limiting en invoervalidatie) — voltooid in 6 werkdagen.

---

## Veelgestelde vragen

### Wat gebeurt er als de oprichter niet weet wat zijn eigen code doet?

Dat is de standaard, niet de uitzondering. De 48-uursbeoordeling is gebouwd voor oprichters die hebben gebouwd met Cursor, Lovable, Bolt of v0 en nog nooit zelf een codebase hebben doorgelicht — de read-only ronde bestaat juist zodat niemand zijn eigen code hoeft uit te leggen voordat deze wordt beoordeeld.

### Zijn er in de eerste 48 uur wijzigingen aan de frontend?

Nee. De beoordelings- en triagefasen zijn volledig gericht op backend, infrastructuur en beveiliging. De technici van LaunchStudio, ondersteund door Manifera's 120+ technici, werken rond uw bestaande frontend in plaats van deze te vervangen.

### Hoe bepaalt LaunchStudio wat er als eerste wordt opgelost?

Bevindingen worden ingedeeld in direct risico, prioriteit vóór lancering, en langetermijnopschoning. Items met direct risico — zoals de blootgestelde API-sleutels in Svens project — worden als eerste aangepakt, ongeacht wat er verder op de roadmap staat.

### Is dit proces anders voor een Lovable- of Bolt-project dan voor een Cursor-project?

De tools laten verschillende sporen na — Bolt-projecten hebben bijvoorbeeld andere deployment-eigenaardigheden dan Cursor-projecten — maar de structuur van eerst lezen, dan trieren blijft hetzelfde bij al deze tools.

### Waar is het team gevestigd dat deze beoordeling uitvoert?

Projectbeoordelingen voor Europese oprichters lopen doorgaans via LaunchStudio's Amsterdamse team, werkend vanuit Herengracht 420, hoewel de onderliggende engineeringgroep meerdere vestigingen omvat.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "What happens if the founder doesn't know what their own code does?", "acceptedAnswer": { "@type": "Answer", "text": "That's the default, not the exception. The 48-hour review is built for founders who built with Cursor, Lovable, Bolt, or v0 and have never audited a codebase themselves." } },
    { "@type": "Question", "name": "Does the first 48 hours involve any changes to the frontend?", "acceptedAnswer": { "@type": "Answer", "text": "No, the review and triage stages are entirely backend, infrastructure, and security-focused, and LaunchStudio's engineers work around the existing frontend rather than replacing it." } },
    { "@type": "Question", "name": "How does LaunchStudio decide what to fix first?", "acceptedAnswer": { "@type": "Answer", "text": "Findings are bucketed into immediate risk, pre-launch priority, and long-term cleanup, with immediate risk items addressed before anything else on the roadmap." } },
    { "@type": "Question", "name": "Is this process different for a Lovable or Bolt project versus a Cursor project?", "acceptedAnswer": { "@type": "Answer", "text": "The tools leave different fingerprints, but the read-first, triage-second structure stays consistent across all of them." } },
    { "@type": "Question", "name": "Where is the team doing this review based?", "acceptedAnswer": { "@type": "Answer", "text": "Project reviews for European founders typically run through LaunchStudio's Amsterdam team, working out of Herengracht 420, though the underlying engineering group spans multiple offices." } }
  ]
}
</script>
