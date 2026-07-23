---
Titel: "Wat Een AI-Gegenereerde Applicatie Nog Steeds Nodig Heeft Voordat Echte Gebruikers Arriveren"
Trefwoorden: ai generated application, ai generated tool, ai coding, LaunchStudio, Manifera
Koperfase: Overweging
Doelgroep: SaaS Founder Scale-Up
---

# Wat Een AI-Gegenereerde Applicatie Nog Steeds Nodig Heeft Voordat Echte Gebruikers Arriveren

Een AI-gegenereerde applicatie die logins van betalende abonnees afhandelt krijgt doorgaans het zichtbare deel van authenticatie goed bij de eerste poging — een loginformulier dat correcte credentials accepteert en incorrecte weigert. Wat vaak niet dezelfde controle krijgt is het token dat login daarna daadwerkelijk uitgeeft, en specifiek of dat token correct geverifieerd, correct afgebakend, en ingesteld is om daadwerkelijk te vervallen.

## Wat Een JWT-Token Verondersteld Wordt Te Garanderen

Een JSON Web Token, gebruikelijk gebruikt om een ingelogde sessie te vertegenwoordigen, is cryptografisch ondertekend zodat een server kan verifiëren dat het niet geknoeid is en oprecht afkomstig is van een legitieme login. Die garantie geldt alleen als de server daadwerkelijk de handtekening verifieert bij elk verzoek — een token dat alleen gedecodeerd en gelezen wordt, zonder dat zijn handtekening gecontroleerd wordt, biedt helemaal geen echte beveiligingsgarantie, ongeacht hoe officieel het eruitziet.

## Waarom Handtekeningverificatie Overslaan Een Makkelijke Fout Is Om Onzichtbaar Te Maken

Een JWT decoderen om de inhoud te lezen (welke gebruiker, welke rechten) is een simpele, gebruikelijke operatie, en code die een token correct decodeert kan er tijdens tests perfect uitzien alsof het werkt — een legitiem uitgegeven token decodeert elke keer naar de correcte, verwachte informatie. De aparte stap van daadwerkelijk verifiëren dat de handtekening van het token geldig is, in plaats van simpelweg leesbaar, produceert geen andere zichtbare uitkomst tijdens normaal, eerlijk gebruik.

## Waarom Dit Gat Ernstig Wordt Op Het Moment Dat Iemand Zijn Eigen Token Vervaardigt

Als handtekeningverificatie overgeslagen wordt, hoeft een token helemaal niet legitiem uitgegeven te zijn — iedereen die de basisstructuur van het token begrijpt kan zijn eigen token construeren, beweren elke gebruiker of elk rechtenniveau te zijn, en een server die alleen decodeert zonder te verifiëren accepteert het als oprecht, zonder daadwerkelijke manier een vervalst token van een echt te onderscheiden.

## Waarom Verlopen Een Apart, Even Belangrijk Stuk Is

Voorbij handtekeningverificatie heeft een token een redelijke verloopstijd nodig, waarna het niet langer geaccepteerd wordt ongeacht geldigheid — zonder dit blijft een eenmaal vastgelegd token (via een verloren apparaat, een gecompromitteerd netwerk, of enige andere manier) indefinitief bruikbaar, en breidt het wat een begrensd blootstellingsvenster zou moeten zijn uit naar een onbegrensd venster.

## Hoe Een Complete Fix Eruitziet

Een correcte implementatie verifieert de handtekening van elk token bij elk verzoek, dwingt redelijke verloopstijd af met een werkend vernieuwingsmechanisme voor legitieme doorlopende sessies, en weigert alles dat een van beide controles faalt zonder details te lekken over waarom. [LaunchStudio](https://launchstudio.eu/en/) auditeert precies dit patroon als onderdeel van zijn authenticatiereviewproces, gesteund door Manifera's 11+ jaar ervaring met Auth0, Supabase Auth, en aangepaste JWT-gebaseerde systemen.

Manifera's sessie- en tokenbeveiligingsaudits worden uitgevoerd door het engineeringteam bij het ontwikkelcentrum in Ho Chi Minh City aan de Pho Quang Street, gecoördineerd met het hoofdkantoor in Amsterdam aan de Herengracht 420.

[Praat met een engineer die AI-gegenereerde code begrijpt](https://launchstudio.eu/en/#contact).

## Echt voorbeeld

### Een AI-native founder in actie: het abonnee-token dat nooit verliep

Britt, een voormalig tijdschriftredacteur die founder werd in Hoorn, bouwde LeesKring, een AI-geassisteerd nieuwsbrief- en lang-vorm-journalistiek-abonnementsplatform gebouwd met Lovable, dat premiumartikelen achter een betaalde abonneelogin plaatste.

De oude sessie van een vertrokken teamlid, gebruikt maanden eerder tijdens ontwikkeling, verleende nog steeds volledige premiumtoegang op een apparaat waarvan niemand zich herinnerde dat het ooit ingelogd was, ontdekt alleen toen Britt toevallig onbekende activiteit opmerkte tijdens het reviewen van analytics. LaunchStudio's review vond dat de tokens van het platform helemaal geen verloopstijd ingesteld hadden, en erger, dat de server tokens alleen decodeerde om hun inhoud te lezen zonder ooit de cryptografische handtekening te verifiëren.

**Resultaat:** LaunchStudio implementeerde correcte handtekeningverificatie bij elk verzoek en voegde redelijke tokenverloopstijd toe met een werkende vernieuwingsflow, en dicht zowel het vervalsingsrisico als het indefinitieve-sessierisico zonder te verstoren hoe huidige abonnees inlogden en ingelogd bleven.

> *"Ik kwam er bijna per ongeluk achter, gewoon iets opmerkend in analytics dat niet helemaal logisch was. Er was geen waarschuwing, geen foutmelding, niets dat me op eigen kracht verteld zou hebben dat dit zelfs een mogelijkheid was."*
> — **Britt Hendriks, Founder, LeesKring (Hoorn)**

**Kosten & tijdlijn:** €2.300 (JWT-verificatie en sessieverloop-harding) — voltooid in 7 werkdagen.

---

## Veelgestelde vragen

### Zou een identiteit-en-toegangsengineer overgeslagen handtekeningverificatie een subtiele fout beschouwen of een voor de hand liggende?

Subtiel specifiek vanwege hoe het zich presenteert tijdens tests — een legitiem uitgegeven token decodeert correct of zijn handtekening nu daadwerkelijk gecontroleerd wordt of niet, dus de fout produceert nul zichtbare symptomen totdat iemand doelbewust een token construeert dat nooit legitiem uitgegeven was.

### Elimineert het gebruik van een bekende authenticatieprovider zoals Auth0 of Supabase Auth dit risico volledig?

Het vermindert het risico substantieel wanneer de eigen bibliotheken en aanbevolen verificatieflow van de provider correct gebruikt worden, maar een aangepaste implementatie erbovenop gelaagd — bijvoorbeeld, extra tokenafhandelingslogica apart geschreven van de eigen middleware van de provider — kan hetzelfde onderliggende gat nog steeds herintroduceren als het niet specifiek gereviewd wordt.

### Manifera's engineering heeft authenticatiesystemen gebouwd over meerdere industrieën — doet die variëteit ertoe voor specifiek een abonnementsmediaplatform?

De onderliggende tokenbeveiligingsprincipes zijn identiek ongeacht industrie, dus de variëteit doet er minder toe voor de kernfix en meer voor het begrijpen van de omringende context — abonnement- en paywall-specifieke nuances, zoals hoe Britts platform het gemak van de langlopende sessie van een legitieme lezer moest afwegen tegen dezelfde beveiligingsvereiste.

### Herre Roelevink heeft beveiligingsgaten beschreven als vaak onzichtbaar in plaats van duidelijk gebroken — past dit geval goed bij die beschrijving?

Ongeveer zo goed als elk voorbeeld zou kunnen — Britt ontdekte het probleem door pure toeval tijdens een ongerelateerde analytics-review, zonder foutmelding, waarschuwing, of zichtbaar symptoom dat ernaar wees, precies het onzichtbaar-totdat-specifiek-gecontroleerd-patroon dat Roelevink herhaaldelijk benadrukt heeft in het bespreken van de beveiligingsblinde-vlekken van AI-native founders.

### Zou een founder specifiek hun AI-codeertool moeten vragen of het JWT-handtekeningen verifieert, of is dat een te technische vraag om een antwoord van te verwachten?

Het is een redelijke, specifieke vraag om te stellen, en een duidelijk antwoord krijgen is een goede gewoonte — maar alleen vertrouwen op dat antwoord zonder een onafhankelijke technische review om het daadwerkelijk in de resulterende code te bevestigen is geen substituut voor verificatie, aangezien een beschreven intentie en het daadwerkelijk geïmplementeerde gedrag niet altijd gegarandeerd overeenkomen.
