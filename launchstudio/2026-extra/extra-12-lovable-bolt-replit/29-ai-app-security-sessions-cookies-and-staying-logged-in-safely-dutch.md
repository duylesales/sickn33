---
Titel: "AI-Appbeveiliging: Sessies, Cookies en Veilig Ingelogd Blijven"
Trefwoorden: ai-appbeveiliging, sessiebeheer, httpOnly-cookies, opslag van tokens, sessies intrekken, CSRF, LaunchStudio, Manifera
Koperfase: Overweging
Doelgroep: Technische solo-oprichter / Indie hacker
---

# AI-Appbeveiliging: Sessies, Cookies en Veilig Ingelogd Blijven

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "AI-Appbeveiliging: Sessies, Cookies en Veilig Ingelogd Blijven",
  "description": "Waar een door AI gebouwde app haar sessietoken bewaart, bepaalt hoe erg een cross-site-scriptingfout wordt. Keuzes voor opslag, een verlooptijd die bij uw product past, een gestolen sessie intrekken, en het uitloggen dat dat niet doet.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-11-10",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/ai-app-security-sessions-cookies-and-staying-logged-in-safely" }
}
</script>

Een sessie is het antwoord op een vraag die uw applicatie bij elk verzoek stelt: wie is dit. Doet u dat verkeerd, dan is elke andere maatregel die u hebt gebouwd decoratie, want een aanvaller met een geldige sessie is voor uw code uw klant.

Door AI gebouwde applicaties doen het ideale pad meestal goed - mensen loggen in, blijven ingelogd, loggen uit - en laten drie dingen onbesproken: waar het token staat, hoe lang het geldig is, en wat u kunt doen als er een wordt gestolen.

Het derde is degene waarvan oprichters op het slechtste moment ontdekken dat ze het nodig hebben.

## Waar het Token Staat, Bepaalt Hoe Erg XSS Wordt

Twee opties, en het verschil is niet subtiel.

**Local storage** is leesbaar voor elk JavaScript dat op uw pagina draait. Dat omvat uw code, elke afhankelijkheid die u installeerde, alles wat via een cross-site-scriptingfout wordt ingevoegd, en elk script van derden dat u voor analytics of supportchat toevoegde. Eén XSS-fout ergens in uw applicatie betekent dat elk sessietoken kan worden gelezen en weggesluisd.

**Een httpOnly-cookie** kan door JavaScript helemaal niet worden gelezen. De browser voegt het automatisch toe aan verzoeken en uw code ziet het nooit. Dezelfde XSS-fout is nu veel minder waard: de aanvaller kan binnen de pagina handelen terwijl het slachtoffer er is, maar kan de sessie niet meenemen en elders op zijn gemak gebruiken.

De meeste door AI gegenereerde authenticatiecode gebruikt local storage, omdat het het eenvoudigste is wat werkt en omdat veel clientbibliotheken het standaard doen. Overstappen op cookies is in sommige stacks een configuratiewijziging en in andere een dag werk, en het is de waardevolste wijziging in dit artikel.

Het cookie heeft drie attributen nodig om de moeite waard te zijn: httpOnly zodat script het niet kan lezen, secure zodat het alleen via HTTPS reist, en sameSite op lax of strict zodat het niet wordt meegestuurd bij verzoeken vanaf andere sites. Met sameSite lax verdwijnt het meeste CSRF-risico; voeg voor alles wat gevoelig is ook een expliciet CSRF-token toe.

## De Verlooptijd Moet bij Uw Product Passen

Er is geen universeel juiste sessieduur. Er is een juiste duur voor wat uw product doet.

Een tool die mensen de hele dag vanaf een vaste werkplek gebruiken - een planbord, een werkplaatssysteem - kan mensen weken ingelogd houden, want elke ochtend een login afdwingen levert gedeelde accounts en opgeschreven wachtwoorden op. Een product met gezondheids-, financiële of persoonsgegevens op gedeelde apparaten heeft uren nodig.

Twee mechanismen, samen gebruikt. Een kortlevend access token, minuten geldig, dat het venster beperkt waarin een gestolen exemplaar bruikbaar is. En een langer levend refresh token dat stilletjes nieuwe access tokens uitgeeft, zodat de gebruiker niet wordt onderbroken. De meeste authenticatieproviders, waaronder Supabase, doen dit standaard - het deel dat oprichters moeten beslissen, is de levensduur van het refresh token, en dat is het echte antwoord op "hoe lang blijven mensen ingelogd".

Voeg een inactiviteitstime-out toe waar de data dat rechtvaardigt: sessies die eindigen na een periode zonder activiteit, los van de absolute verlooptijd. En wees bewust met "onthoud mij" - dat moet de levensduur van het refresh token verlengen, niet de verlooptijd volledig uitschakelen.

## U Moet een Sessie Kunnen Beëindigen

Dit is de mogelijkheid die de meeste kleine producten missen, en degene die er bij een incident toe doet.

Wordt een laptop gestolen, raakt een telefoon kwijt, vertrekt een medewerker, of wordt vermoed dat een token is gestolen, dan moet iemand die sessie direct kunnen beëindigen. Met stateless tokens die geldig zijn tot ze verlopen, is het eerlijke antwoord vaak dat u dat niet kunt - het token werkt tot het verloopt, wat u ook doet.

Twee dingen maken intrekken echt. Houd een registratie bij van actieve sessies, zodat refresh tokens ongeldig kunnen worden gemaakt en een sessie echt eindigt. En bied de twee handelingen die mensen nodig hebben: overal uitloggen, beschikbaar voor de gebruiker, en een account geforceerd uitloggen, beschikbaar voor u.

Toon de gebruiker, nu u dat toch bouwt, zijn actieve sessies - apparaat, globale locatie, laatst gebruikt. Het kost weinig, het is de functie waarmee een klant een sessie opmerkt die hij niet herkent, en zakelijke kopers die uw beveiligingspagina lezen, verwachten het steeds vaker.

## Uitloggen Moet Echt Uitloggen

Test dit op uw eigen product. Log uit, gebruik dan de terugknop van de browser, en probeer een handeling.

In een verrassend aantal door AI gebouwde applicaties maakt uitloggen de interface leeg en laat het de sessie geldig. Het token werd van de client verwijderd, of niet, en op de server werd niets ongeldig gemaakt. Iedereen met het apparaat - of met een kopie van het token - blijft geauthenticeerd.

Uitloggen moet de sessie op de server ongeldig maken, het cookie wissen, en alle gecachete gebruikersdata die de client vasthoudt weggooien. Dat laatste is waar gegenereerde code lekt: een bibliotheek voor het ophalen van data houdt de antwoorden van de vorige gebruiker in het geheugen, en de volgende persoon die op dat apparaat inlogt, ziet heel even het dashboard van een ander voordat zijn eigen dashboard laadt.

## Vernieuw bij een Wijziging in Rechten

Op twee momenten is een nieuwe sessie-identificatie nodig in plaats van een hergebruikte.

**Bij het inloggen.** Overleeft een sessie-identificatie die vóór authenticatie werd uitgegeven de authenticatie, dan deelt een aanvaller die die identificatie in de browser van een slachtoffer plantte nu diens geauthenticeerde sessie. Dit heet session fixation, en de verdediging is simpelweg bij een geslaagde login een nieuwe sessie uit te geven.

**Bij het wijzigen van het wachtwoord.** Een wachtwoord wijzigen moet elke andere sessie van dat account beëindigen. Dat is wat gebruikers verwachten dat de handeling betekent, en het is de natuurlijke reactie op "ik denk dat iemand toegang heeft" - en daarom moet het werken voor degene die het doet.

## Multi-Tenant Producten Hebben een Tweede Vraag

Bij een product waarin één persoon bij meerdere organisaties kan horen - een accountant die twaalf klanten bedient, een consultant die voor drie klanten werkt - beantwoordt de sessie de vraag wie, en moet iets anders de vraag welke beantwoorden.

De fout is de huidige organisatie in de client te bewaren en bij elk verzoek mee te sturen. Wat de browser stuurt, kan de browser veranderen, dus een identificatie die vanaf de pagina wordt verstuurd, is een verzoek en geen feit. Producten die zo zijn gebouwd, staan één aangepaste waarde verwijderd van een klant die de data van een andere klant leest, en het hoort bij de meest voorkomende ernstige bevindingen in snel gebouwde multi-tenant applicaties.

De juiste opzet slaat de actieve organisatie op de server op als deel van de sessie, alleen te wijzigen via een expliciete handeling die het lidmaatschap controleert. Elk volgend verzoek leidt de organisatie dan af van de sessie, en de client kan er helemaal geen invloed op uitoefenen.

Er volgen twee details. Wisselen van organisatie moet het sessierecord vernieuwen of op zijn minst bijwerken, zodat de wijziging controleerbaar is - weten in welke context een handeling werd uitgevoerd, doet ertoe wanneer iemand vraagt wat er gebeurde. En elke query moet nog steeds filteren op de organisatie uit de sessie in plaats van een waarde te vertrouwen die aan een functie werd doorgegeven, want de grens is maar zo goed als de minst zorgvuldige plek waar ze wordt aangeroepen.

Test het zoals een aanvaller dat zou doen: log in als gebruiker die bij twee organisaties hoort, handel in de ene, en speel hetzelfde verzoek opnieuw af met de identificatie van de andere organisatie ingevuld. Het juiste antwoord is een weigering.

## Wat in een Token Hoort, en Wat U Opzoekt

Tokens kunnen claims bevatten - de rol van de gebruiker, zijn organisatie, zijn rechten - en dat voorkomt bij elk verzoek een database-opzoeking. Het bevriest die waarden ook voor de levensduur van het token, en dat is de afweging die niemand uitlegt.

Een rol die is ingebed in een access token dat een uur geldig is, betekent dat een gebruiker die van beheerder is teruggezet nog tot een uur beheerdersrechten houdt. Voor de meeste producten is dat acceptabel bij een kortlevend token en onacceptabel bij een langlevend, wat nog een argument is voor korte access tokens met frequente vernieuwing.

De praktische verdeling: zet identiteit in het token - wie dit is, welke sessie - en zoek autoriteit op. Rollen, rechten, abonnementsstatus en lidmaatschap van organisaties worden uit uw database gelezen als deel van de rechtencontrole die elk betekenisvol endpoint toch al uitvoert. De opzoeking is één geïndexeerde query, kort gecachet als dat ertoe doet, en het betekent dat een rechtenwijziging bij het volgende verzoek ingaat in plaats van bij de volgende login.

Twee verwante gewoontes. Vertrouw nooit een claim waarop de client invloed kan hebben gehad - kwam een waarde binnen in de inhoud van een verzoek in plaats van in een ondertekend token, dan is het invoer. En controleer bij elk verzoek de handtekening en verlooptijd van het token op de server, in plaats van het te decoderen en de velden te lezen, een fout die vaker in gegenereerde code voorkomt dan zou moeten.

## Dit Inrichten

Voor een bestaand product kost dit doorgaans één dag: sessietokens verplaatst van local storage naar httpOnly-, secure- en sameSite-cookies met CSRF-bescherming waar nodig, levensduur van access- en refresh tokens passend bij het product gekozen met een inactiviteitstime-out waar de data dat rechtvaardigt, een registratie van actieve sessies op de server die echt intrekken mogelijk maakt, overal uitloggen voor gebruikers en geforceerd uitloggen voor support, een zichtbare lijst met actieve sessies, uitloggen gecontroleerd op ongeldig maken op de server en het wissen van clientcaches, en vernieuwing van sessies bij inloggen en bij wachtwoordwijziging.

LaunchStudio behandelt dit in de beveiligingsreview, en de bevinding over local storage komt in de ruime meerderheid van de door AI gebouwde applicaties die wij bekijken voor. De engineers zijn van Manifera - elf jaar, 120+ engineers, voor klanten als Vodafone, TNO en CFLW.

[Vraag ons te controleren waar uw app haar token bewaart](https://launchstudio.eu/nl/#contact). Het kost twee minuten en bepaalt hoeveel een toekomstige fout u kost.

## Echt voorbeeld

### Een Sessie Die de Medewerker Overleefde

Roos Verhagen bouwde Zorgplanning in Lovable: dienst- en cliëntplanning voor thuiszorgorganisaties, 18 organisaties met samen zo'n 900 zorgverleners.

Een planner bij een van de organisaties vertrok na een meningsverschil. De manager van de organisatie verwijderde haar account op haar laatste dag en beschouwde de zaak als afgesloten.

Drie weken later verschenen er wijzigingen in de planning die niemand kon verklaren: diensten die 's nachts waren verschoven, twee cliëntbezoeken verwijderd. Op de tablet van de voormalige planner stond de applicatie nog open, en de sessie was nog geldig, omdat het refresh token dat bij haar laatste login was uitgegeven 90 dagen geldig was en het verwijderen van de accountrij het niet ongeldig had gemaakt. Haar browser bleef access tokens vernieuwen tegen een gebruikersrecord dat niet meer bestond, en de applicatie - die het token controleerde in plaats van het account - bleef ze accepteren.

Twee werkdagen: sessietokens verplaatst van local storage naar httpOnly-, secure- en sameSite-cookies, met CSRF-tokens op verzoeken die iets wijzigen; een sessietabel die elke actieve sessie vastlegt met apparaat, laatst gebruikt en globale locatie; het deactiveren van een account uitgebreid zodat alle sessies direct ongeldig worden, net als bij een wachtwoordwijziging; overal uitloggen toegevoegd voor gebruikers en geforceerd uitloggen voor beheerders van organisaties, die nu zelf de toegang van een vertrekkende medewerker kunnen beëindigen; de levensduur van het access token ingekort tot 30 minuten met een refresh-levensduur van 14 dagen, samen met de organisaties gekozen in plaats van op de standaard, plus een inactiviteitstime-out van 12 uur passend bij gedeelde tablets op zorglocaties; uitloggen gecorrigeerd zodat het op de server ongeldig maakt en de datacache van de client wist, die bij het wisselen een seconde lang de cliëntenlijst van de vorige gebruiker had getoond; vernieuwing van de sessie bij inloggen; en een zichtbaar scherm met actieve sessies.

**Resultaat:** de ongeautoriseerde wijzigingen werden gereconstrueerd uit de audittrail en gecorrigeerd, en de organisatie meldde het incident intern zoals vereist. Het scherm met actieve sessies is sindsdien door drie organisaties gebruikt om tablets te vinden die ingelogd waren achtergelaten op cliëntlocaties - een probleem waarvan geen van hen wist dat ze het hadden.

> *"We hadden haar account verwijderd. Iedereen in de kamer geloofde dat ze daarmee buiten stond. Haar tablet bleef drie weken werken."*
> - **Roos Verhagen, Oprichter, Zorgplanning (Apeldoorn)**

**Kosten & Doorlooptijd:** €2.700 (sessieopslag in cookies met CSRF-bescherming, sessieregistratie en intrekken, ongeldig maken bij deactivering en wachtwoordwijziging, overal uitloggen en geforceerd uitloggen door beheerders, beleid voor levensduur en inactiviteit, correctie van uitloggen en cache, vernieuwing van sessies, scherm met actieve sessies) - afgerond in 2 werkdagen.

## Veelgestelde vragen

### Is local storage veilig voor sessietokens?

Nee. Elk JavaScript op uw pagina kan het lezen, inclusief ingevoegd script en bibliotheken van derden. Een httpOnly-cookie kan niet door script worden gelezen, wat de waarde van een XSS-fout sterk vermindert.

### Hoe lang moeten gebruikers ingelogd blijven?

Afgestemd op het product. Interne tools die de hele dag worden gebruikt, kunnen weken; alles met gezondheids-, financiële of persoonsgegevens op gedeelde apparaten hoort uren te zijn, met een inactiviteitstime-out.

### Kan ik een sessie beëindigen voordat ze verloopt?

Alleen als u op de server een registratie van sessies bijhoudt en refresh tokens ongeldig maakt. Zonder dat blijft een stateless token geldig totdat het verloopt, wat u ook doet.

### Beëindigt het verwijderen van een gebruikersaccount zijn sessies?

Niet automatisch. Deactivering van een account, wachtwoordwijziging en verwijdering door een beheerder moeten allemaal expliciet sessies ongeldig maken, anders blijft een ingelogd apparaat werken.

### Wat houdt correct uitloggen in?

De sessie op de server ongeldig maken, het cookie wissen, en gecachete data op de client weggooien. Alleen de interface leegmaken laat de sessie geldig en kan de data van de vorige gebruiker tonen.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Is local storage veilig voor sessietokens?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Nee - elk script op de pagina kan het lezen. httpOnly-cookies zijn onleesbaar voor JavaScript, wat de schade van een XSS-fout sterk beperkt."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe lang moet een sessie duren?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Afgestemd op het product: weken voor interne tools die de hele dag worden gebruikt, uren met een inactiviteitstime-out voor gevoelige data op gedeelde apparaten."
      }
    },
    {
      "@type": "Question",
      "name": "Kan een sessie worden ingetrokken voordat ze verloopt?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Alleen met een registratie van sessies op de server en het ongeldig maken van refresh tokens. Anders blijft een stateless token geldig totdat het verloopt."
      }
    },
    {
      "@type": "Question",
      "name": "Beëindigt het verwijderen van een gebruiker zijn actieve sessies?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Niet standaard. Deactivering, wachtwoordwijziging en verwijdering door een beheerder moeten elk expliciet sessies ongeldig maken."
      }
    },
    {
      "@type": "Question",
      "name": "Wat moet uitloggen werkelijk doen?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Op de server ongeldig maken, het cookie wissen en gecachete data op de client weggooien - alleen de interface leegmaken laat de sessie bruikbaar."
      }
    }
  ]
}
</script>
