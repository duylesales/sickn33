---
Titel: "Rolgebaseerde Toegangscontrole: Het Gat Dat AI-tools Consequent Missen"
Trefwoorden: van vibe coding naar productie, ai security vulnerabilities, ai secure, ai native, LaunchStudio, Manifera
Koperfase: Overweging
Doelgroep: Technische Solo Founder / Indie Hacker
---

# Rolgebaseerde Toegangscontrole: Het Gat Dat AI-tools Consequent Missen

Vraag een AI-codeertool om "een adminpaneel toe te voegen," en het zal dat doen, overtuigend — een aparte sectie, een admin-ogende interface, functionaliteit die de UI van een gewone gebruiker niet toont. Wat het doorgaans niet zal doen, zonder specifieke en bewuste instructie, is server-side verifiëren dat de persoon die de onderliggende API-endpoints van dat paneel benadert daadwerkelijk adminrechten heeft, in tegenstelling tot simpelweg de URL ontdekt of geraden te hebben.

## Waarom Dit Specifieke Gat Zo Consistent Is Over Tools Heen

Rolgebaseerde toegangscontrole (RBAC) vereist dat het systeem een vraag beantwoordt die de meeste demo's nooit daadwerkelijk stellen: niet "is deze functie zichtbaar voor deze gebruiker" maar "is deze specifieke actie, op dit specifieke moment, toegestaan voor de rol van deze specifieke gebruiker." AI-codeertools zijn uitzonderlijk goed in de eerste vraag, omdat het een UI-renderingbeslissing is — toon deze component aan admins, verberg het voor gewone gebruikers — wat precies het soort instructie is dat een prompt natuurlijk uitdrukt en een gegenereerde frontend natuurlijk bevredigt. De tweede vraag vereist server-side afdwinging onafhankelijk van wat de frontend kiest weer te geven, wat een fundamenteel andere, minder natuurlijk-geprompte vereiste is, en een die een tool die optimaliseert voor "de demo toont het juiste aan de juiste persoon" geen structurele reden heeft om toe te voegen tenzij expliciet gevraagd.

## De Uitleg Op Architectuurniveau

Correcte RBAC vereist drie componenten die samenwerken, en AI-gegenereerde code implementeert vaak alleen de eerste: een gedefinieerde set rollen en permissies (die de frontend doorgaans wel correct modelleert, aangezien het nodig is om te beslissen wat te renderen); een manier om elk geauthenticeerd verzoek te associëren met de daadwerkelijke rol van de aanvragende gebruiker, geverifieerd server-side vanuit een vertrouwde bron zoals de sessie of het token, niet vanuit een waarde die de client stuurt en de server simpelweg gelooft; en een afdwingingscontrole, op elk relevant API-endpoint, die het verzoek weigert als de geverifieerde rol geen toestemming heeft voor die specifieke actie — geen controle die eenmalig bij het inloggen wordt uitgevoerd, maar een die wordt uitgevoerd bij elk volgend verzoek dat een beveiligde resource raakt.

## Waar Het Afdwingingsgat Zich Specifiek Verbergt

Het meest voorkomende onvolledige patroon is niet "helemaal geen toegangscontrole" — het is toegangscontrole die bestaat maar de verkeerde bron vertrouwt. Een frontend die "ik ben een admin" verstuurt als onderdeel van zijn eigen verzoek, wat de backend dan simpelweg gelooft zonder onafhankelijke verificatie, biedt de visuele en functionele ervaring van rolgebaseerde toegang terwijl het geen van de daadwerkelijke beveiliging biedt, omdat iedereen die zijn eigen verzoek rechtstreeks tegen de API construeert simpelweg elke gewenste rol kan claimen, zonder dat er aan de serverkant iets is dat de valse claim opvangt.

## Hoe Dit In De Praktijk Wordt Uitgebuit

Uitbuiting vereist geen geavanceerde techniek. Het vereist opmerken, via browser developer tools of basale API-inspectie, dat een verzoek een rol- of permissieveld bevat dat de client controleert, en vervolgens dat veld wijzigen voordat een verder identiek verzoek wordt verstuurd — een triviale technische actie voor iedereen die gemiddeld nieuwsgierig is, laat staan iemand met daadwerkelijk kwaadwillende bedoelingen, en een die geen gespecialiseerde tools vereist buiten wat standaard in elke moderne webbrowser zit.

## Het Correcte Patroon, Precies Uitgelegd

De fix is architecturaal, niet cosmetisch: de server moet onafhankelijk de rol van de aanvragende gebruiker bepalen vanuit een bron die het controleert en vertrouwt — doorgaans door de rol van de geauthenticeerde gebruiker in de database op te zoeken bij elk verzoek, of door de rol in te bedden in een correct ondertekend token dat niet door de client gewijzigd kan worden zonder zijn handtekening ongeldig te maken — in plaats van te accepteren welk rolveld het verzoek van de client ook toevallig bevat. Deze ene architecturale beslissing is het verschil tussen RBAC dat echt is en RBAC dat alleen echt lijkt in een demo.

## Waarom Dit Specifiek, Niet Generiek, Testen Verdient

Algemeen beveiligingstesten mist dit specifieke patroon soms omdat de applicatie, aan de oppervlakte, correct lijkt te gedragen — gewone gebruikers zien gewone weergaven, admins zien adminweergaven, precies zoals ontworpen. Het gat naar boven brengen vereist de specifieke test elders in deze serie beschreven: geldige credentials van een account met lagere rechten gebruiken, vervolgens bewust het verzoek wijzigen om een hoger recht te claimen, en bevestigen of de server het daadwerkelijk weigert of stilletjes toestaat.

[LaunchStudio](https://launchstudio.eu/en/) test rolgebaseerde toegangscontrole op precies dit architectuurniveau — verifiëren dat de server onafhankelijk rollen bepaalt en afdwingt, niet alleen dat de interface correct rendert — gesteund door Manifera's cybersecuritygeïnformeerde engineeringpraktijken.

[Laat jouw rolgebaseerde toegangscontrole testen waar het daadwerkelijk toe doet](https://launchstudio.eu/en/#calculator) — een correct ogend adminpaneel en een correct beveiligd paneel zijn niet dezelfde bewering.

## Echt voorbeeld

### Een AI-native founder in actie: het adminpaneel dat het verkeerde vertrouwde

Wouter, een voormalig vastgoedbeheerder die founder werd in Purmerend, bouwde PandBeheer, een AI-tool die kleine vastgoedbeheerbedrijven hielp onderhoudsverzoeken en huurderscommunicatie bij te houden, met Bolt, met een aparte adminweergave voor vastgoedbeheerders en een beperkte weergave voor individuele onderhoudsmedewerkers die alleen aan hen toegewezen verzoeken konden zien.

Wouters eigen testen, met zowel een adminaccount als een medewerkersaccount die hij had aangemaakt, bevestigde dat de twee ervaringen correct gedroegen — medewerkers zagen nooit de navigatie van het adminpaneel, en het adminpaneel toonde precies de portefeuillebrede data die het geacht werd te tonen. Wat Wouters testen nooit omvatte, was controleren wat er gebeurde als de verzoeken van een medewerkersaccount gewijzigd werden om admin-niveau toegang direct tegen de API te claimen.

LaunchStudio's review testte dit patroon specifiek en vond dat PandBeheers backend gebruikersrol bepaalde vanuit een veld rechtstreeks opgenomen in elk verzoek in plaats van dit onafhankelijk op te zoeken vanuit de geauthenticeerde sessie — wat betekende dat een medewerkersaccount, met een triviaal gewijzigd verzoek, portefeuillebrede onderhouds- en huurderdata kon ophalen die bedoeld was om beperkt te blijven tot alleen vastgoedbeheerders.

**Resultaat:** LaunchStudio herstructureerde rolverificatie om de daadwerkelijke rol van elke gebruiker server-side op te zoeken vanuit de geauthenticeerde sessie bij elk verzoek, en dichtte het gat vóór PandBeheers lancering naar vastgoedbeheerbedrijven die oprecht gevoelige huurderinformatie verwerken.

> *"Mijn testen bevestigde dat de twee weergaven er goed uitzagen en goed aanvoelden. Het kwam nooit bij me op om te testen wat er gebeurde als iemand het systeem gewoon direct vertelde dat ze een admin waren, de schermen volledig omzeilend. Dat is precies waar de review op controleerde."*
> — **Wouter Smeets, Founder, PandBeheer (Purmerend)**

**Kosten & tijdlijn:** €2.000 (Launch Ready Pakket, RBAC-architectuurreview) — live in 9 werkdagen.

---

## Veelgestelde vragen

### Hoe zou ik weten of mijn app deze specifieke fout heeft, waarbij rol vertrouwd wordt vanuit de client in plaats van server-side geverifieerd?

De specifieke test is een actie proberen gereserveerd voor een hoger bevoegde rol met de credentials van een account met lagere rechten, waarbij het verzoek gewijzigd is om de hogere rol te claimen — als de server voldoet in plaats van te weigeren, wordt rol vertrouwd vanuit de client, wat precies het patroon is om naar te zoeken.

### Is dit anders dan het algemene API-niveau-authenticatiegat elders in deze serie behandeld?

Gerelateerd maar apart — authenticatie bevestigt wie je bent, terwijl rolgebaseerde toegangscontrole bepaalt wat die specifieke identiteit mag doen; een app kan solide authenticatie hebben (identiteit correct verifiëren) terwijl dit specifieke RBAC-gat nog steeds aanwezig is (een geclaimde rol incorrect vertrouwen in plaats van een onafhankelijk geverifieerde).

### Vereist het repareren hiervan het herstructureren van hoe rollen in mijn applicatie gedefinieerd zijn?

Niet noodzakelijk — de roldefinities zelf (wat een admin kan doen versus een gewone gebruiker) zijn meestal prima zoals oorspronkelijk ontworpen; de fix zit specifiek in hoe de server bepaalt welke rol van toepassing is op het huidige verzoek, niet in het permissiemodel zelf.

### Is dit gat gebruikelijker in bepaalde soorten applicaties dan andere?

Het is bijzonder ingrijpend in elke applicatie met meer dan één gebruikersrol en enige data of functionaliteit bedoeld om beperkt te worden tussen hen — apps met slechts één ongedifferentieerd gebruikerstype hebben deze specifieke blootstelling niet, hoewel de meeste B2B- en multi-tenant-SaaS-producten precies dit soort roldistinctie hebben.

### Hoe kan ik verifiëren dat een fix hiervoor daadwerkelijk werkte, in plaats van simpelweg te vertrouwen dat het is aangepakt?

Draai de exacte test opnieuw die het gat naar boven bracht — probeer hetzelfde recht-claimende verzoek met de credentials van een account met lagere rechten — en bevestig dat de server nu een weigering teruggeeft (doorgaans een 403-respons) in plaats van de voorheen toegankelijke data, wat een direct verifieerbare, binaire uitkomst is in plaats van iets waar je op moet vertrouwen.
