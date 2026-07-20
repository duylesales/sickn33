---
Titel: "Hoe Voeg Je Authenticatie Toe aan Je Lovable-app zonder Hem te Breken"
Trefwoorden: AI-app-ontwikkeling, AI-codeontwikkeling, AI-app bouwen, AI-ontwikkeling, LaunchStudio, Manifera
Koperfase: Beslissing
Doelgroep: Technische Solo Founder / Indie Hacker
---

# Hoe Voeg Je Authenticatie Toe aan Je Lovable-app zonder Hem te Breken

Authenticatie klinkt als één enkele functie. In de praktijk is het een wijziging die bijna alles raakt: elke pagina moet weten wie is ingelogd, elke databasequery moet respecteren wie welke data bezit, en elke bestaande functie die je al hebt gebouwd, moet exact blijven werken zoals voorheen, alleen nu gescoped naar de juiste gebruiker. Daarom breekt het toevoegen van authenticatie aan een bestaand Lovable-prototype vaker dingen dan founders verwachten.

## Waarom Authenticatie Anders Is dan een Normale Functietoevoeging

De meeste functietoevoegingen zijn additief — je voegt iets nieuws toe zonder te verstoren wat al bestaat. Authenticatie is structureel — het verandert de fundamentele aanname waarop je hele applicatie is gebouwd, van "er is één impliciete gebruiker" naar "er zijn veel verschillende gebruikers, en elk stukje data en elke actie moet correct gescoped zijn naar de juiste." Deze aanname achteraf inbouwen raakt veel meer van je codebase dan een typische functie.

## Het Veelvoorkomende Faalpatroon

Een founder vraagt Lovable (of Bolt, of Cursor) om "login toe te voegen," en de AI-tool genereert een redelijk uitziende authenticatieflow — een loginpagina, een aanmeldpagina, een sessietoken. Wat vaak niet automatisch gebeurt, is het bijwerken van elke bestaande databasequery en pagina om die authenticatie daadwerkelijk te respecteren: alleen de data van de ingelogde gebruiker tonen, toegang tot pagina's blokkeren zonder geldige sessie, en voorkomen dat één gebruiker bij de records van een andere komt door een URL te manipuleren. De loginpagina werkt. De daadwerkelijke bescherming vaak niet, stilletjes.

## Een Veiligere Volgorde voor het Toevoegen van Authenticatie

1. **Kies eerst een productiewaardige authenticatieprovider** (Supabase Auth, Auth0, NextAuth) in plaats van de AI-tool authenticatielogica vanaf nul te laten bouwen — gevestigde providers handelen beveiligingsdetails (wachtwoordhashing, sessiebeheer, tokenverval) standaard correct af.
2. **Breng elke bestaande functie en datatabel in kaart** die gebruikersgescoped moet worden voordat je code schrijft, zodat niets wordt gemist.
3. **Update databasequery's systematisch**, en zorg ervoor dat elke enkele query die gebruikersdata raakt, correcte filtering bevat — niet alleen de pagina's die je je herinnert te checken.
4. **Test cross-gebruiker-toegang expliciet** — maak twee testaccounts aan en probeer bewust bij de data van het ene account te komen vanuit het andere voordat je het werk als voltooid beschouwt.
5. **Voeg bescherming op databaseniveau toe** (zoals Supabase Row Level Security) als tweede verdedigingslinie, zodat zelfs een gemiste check op applicatieniveau niet leidt tot volledige datablootstelling.

## Waarom Dit een Beoordeling Waard Is

Omdat authenticatie je hele applicatie tegelijk raakt, zijn fouten hier zowel makkelijk te maken als ongewoon kostbaar — een authenticatiegat breekt niet alleen een functie, het kan de privédata van elke gebruiker tegelijk blootstellen aan elke andere gebruiker. Deze combinatie van brede impact en makkelijk te missen subtiliteit is precies waarom [LaunchStudio](https://launchstudio.eu/en/) authenticatie-implementatie behandelt als een van zijn meest zorgvuldig beoordeelde engineeringtaken, gesteund door Manifera's beveiligingsachtergrond geworteld in Herre Roelevinks cybersecuritywerk met CFLW en TNO.

[Laat je authenticatie-implementatie beoordelen](https://launchstudio.eu/en/#contact) voordat echte gebruikers echte accounts met echte data beginnen aan te maken.

## Echt voorbeeld

### Een AI-native founder in actie: een authenticatiegat vangen voordat er schade ontstond

Fenna, een personal trainer met een kleine studio in Sittard, bouwde FitVolg, een tool voor trainingsprogramma's en voortgangstracking voor haar personal-training-klanten, met Lovable. Ze vroeg Lovable om een loginsysteem toe te voegen zodat elke klant alleen zijn eigen trainingsplannen kon zien, en de resulterende login- en aanmeldpagina's zagen er correct uit en functioneerden soepel in haar eigen tests.

Voordat ze FitVolg uitrolde naar haar daadwerkelijke klantenbestand, testte Fenna's broer, een software-engineer, het uit nieuwsgierigheid en ontdekte dat, hoewel de loginpagina werkte, de trainingsplanpagina's zelf nog steeds data ophaalden via een simpele URL-parameter zonder server-side check die bevestigde dat de ingelogde gebruiker dat plan daadwerkelijk bezat — wat betekende dat elke klant, eenmaal ingelogd, de trainingsgeschiedenis en persoonlijke notities van elke andere klant kon bekijken door simpelweg een getal in de adresbalk van de browser te veranderen.

Fenna nam contact op met LaunchStudio om authenticatie correct te implementeren in plaats van het risico te lopen dat dit gat haar daadwerkelijke klanten zou bereiken. Het Manifera-team migreerde FitVolg naar Supabase Auth met correcte Row Level Security, auditte systematisch elke bestaande pagina en query op correcte gebruikersscoping, en voegde geautomatiseerde tests toe die specifiek cross-gebruiker-datatoegang controleerden vóór deployment.

**Resultaat:** FitVolg lanceerde naar Fenna's 24 personal-training-klanten met geverifieerde, geteste data-isolatie — een gat dat, als het echte klanten had bereikt, gevoelige persoonlijke fitness- en gezondheidsnotities zou hebben blootgesteld tussen mensen die elkaar vaak persoonlijk kenden binnen haar studio.

> *"Mijn broer vond het per ongeluk, uit nieuwsgierigheid aan het testen. Als een klant het als eerste had gevonden, was het een ramp geweest — sommige van mijn klanten kennen elkaar. LaunchStudio voegde niet alleen een loginpagina toe, ze verifieerden dat het mensen daadwerkelijk beschermde."*
> — **Fenna Kuipers, Founder, FitVolg (Sittard)**

**Kosten & tijdlijn:** €1.700 (Launch Ready Pakket, authenticatiehardening) — voltooid in 7 werkdagen.

---

## Veelgestelde vragen

### Kan ik de authenticatie van mijn eigen Lovable-app zelf testen op dit soort gaten?

Ja, gedeeltelijk. Maak twee testaccounts aan, log in als de ene, en probeer zichtbare ID-nummers in de URL of browserontwikkelaarstools te veranderen om bij data van een ander account te komen. Als je slaagt, is er een echt gat. Deze test vangt niet elk mogelijk probleem, maar vangt wel de meest voorkomende categorie.

### Is Supabase Auth of een op maat gebouwd loginsysteem veiliger voor een Lovable-app?

Supabase Auth (of een andere gevestigde provider) is bijna altijd veiliger dan een op maat gebouwd systeem, aangezien gevestigde providers hun kernbeveiligingslogica — wachtwoordhashing, sessieafhandeling, tokenbeveiliging — jarenlang uitgebreid hebben getest en gehard, wat zeer moeilijk correct te repliceren is vanaf nul in een snelle, door AI gegenereerde implementatie.

### Hoe lang duurt het doorgaans om authenticatie correct achteraf in een bestaand prototype in te bouwen?

Voor een matig complexe app duurt dit doorgaans één tot twee weken wanneer het grondig wordt gedaan, inclusief de systematische query-audit en testfase — betekenisvol langer dan de paar minuten die een AI-tool nodig heeft om de loginpagina zelf te genereren, omdat het echte werk in de scoping en verificatie zit.

### Wat is Row Level Security en waarom noemt het artikel het een "tweede verdedigingslinie"?

Row Level Security is een functie op databaseniveau (beschikbaar in Supabase en PostgreSQL) die toegangsregels direct in de database afdwingt, onafhankelijk van je applicatiecode. Zelfs als je applicatiecode een bug heeft die vergeet data correct te filteren, kan RLS nog steeds ongeautoriseerde toegang blokkeren op databaseniveau — daarom is het waardevol als back-up, niet alleen als primair mechanisme.

### Is Manifera's cybersecurityachtergrond specifiek van toepassing op authenticatie-implementatie?

Ja. Herre Roelevinks achtergrond als medeoprichter van CyberDevOps (nu CFLW Cyber Strategies) en het ontwikkelen van de Dark Web Monitor-tool met TNO weerspiegelt een security-first-oriëntatie die direct doorwerkt in hoe Manifera en LaunchStudio authenticatie benaderen — het behandelen als een beveiligingskritieke implementatie, niet slechts een functionele functie.
