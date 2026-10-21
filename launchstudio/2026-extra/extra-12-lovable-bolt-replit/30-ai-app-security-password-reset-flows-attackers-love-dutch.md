---
Titel: "AI-Appbeveiliging: Wachtwoordresets Waar Aanvallers dol op Zijn"
Trefwoorden: ai-appbeveiliging, wachtwoord resetten, accountherstel, verlooptijd van tokens, user enumeration, e-mailadres wijzigen, LaunchStudio, Manifera
Koperfase: Overweging
Doelgroep: Technische solo-oprichter / Indie hacker
---

# AI-Appbeveiliging: Wachtwoordresets Waar Aanvallers dol op Zijn

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "AI-Appbeveiliging: Wachtwoordresets Waar Aanvallers dol op Zijn",
  "description": "Het resetten van een wachtwoord is de achterdeur van elk account, en door AI gegenereerde implementaties gaan er op consistente manieren de mist mee in. Ontwerp van tokens, enumeration, de e-mailwijziging die niemand beschermt, en wat u doet na een reset.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-11-12",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/ai-app-security-password-reset-flows-attackers-love" }
}
</script>

Elk account in uw product heeft twee deuren. De voordeur is het inlogformulier, waar oprichters over nadenken, dat ze testen en waar ze soms een tweede factor aan toevoegen. De achterdeur is het resetten van het wachtwoord, die bestaat om iemand binnen te laten zonder het wachtwoord te kennen — in tien minuten gebouwd, één keer, en nooit meer bekeken.

Een aanvaller die tussen de twee kiest, kiest niet de voordeur.

Dit is een middag waard juist omdat het zo weinig glamoureus is. Niemand geeft een demo van een resetproces. Niemand merkt dat het werkt. En het is het mechanisme waarmee accounts worden overgenomen in producten die verder zorgvuldig zijn gebouwd.

## Wat een Resettoken Moet Zijn

Zes eigenschappen, en gegenereerde implementaties missen er doorgaans twee of drie.

**Onvoorspelbaar.** Gegenereerd uit een cryptografisch veilige bron, lang genoeg om raden hopeloos te maken. Een token dat is afgeleid van een tijdstempel, een e-mailadres of een oplopende waarde, kan worden gemaakt door iedereen die erover nadenkt.

**Kortlevend.** Vijftien tot zestig minuten. Een resetlink die een week geldig is, is een sleutel in een inbox — en inboxen worden doorgestuurd, gesynchroniseerd naar apparaten, en soms door andere mensen gelezen.

**Eenmalig.** Ongeldig gemaakt op het moment dat het wordt gebruikt. Een link die nog werkt nadat het wachtwoord is gewijzigd, is een link die een aanvaller later kan gebruiken, nadat hij de e-mail één keer heeft onderschept.

**Gebonden aan één account**, en elk eerder openstaand token voor dat account ongeldig makend, zodat het aanvragen van een nieuwe reset de oude annuleert.

**Gehasht opgeslagen**, niet als platte tekst. Uw database is de enige plek waar het token niet leesbaar moet zijn, om dezelfde reden dat u geen wachtwoorden opslaat.

**Ongeldig gemaakt bij gebruik van elke andere herstelroute**, zodat een reset en een e-mailwijziging niet tegelijk kunnen lopen.

## Zeg Hetzelfde, Of het Account Nu Bestaat of Niet

Zegt uw resetformulier "geen account met dat e-mailadres" bij onbekende adressen en "controleer uw inbox" bij bekende, dan hebt u een instrument gebouwd om te bevestigen wie uw product gebruikt.

Dat doet er meer toe dan het klinkt. Voor een product in een gevoelige categorie — schuldhulpverlening, juridisch advies, zorg, een datingdienst — is het lidmaatschap zelf vertrouwelijk. En voor elk product is een bevestigde lijst met echte klantadressen wat een phishingcampagne effectief maakt.

Het juiste antwoord is in beide gevallen identiek: *als er een account bestaat voor dat adres, hebben we een link gestuurd*. Dezelfde tekst, dezelfde status, en ongeveer dezelfde timing — een antwoord dat bij onbekende adressen direct terugkomt en bij echte 400 milliseconden duurt, lekt dezelfde informatie via de klok.

Dezelfde discipline geldt voor registratie en inloggen, waar "dit e-mailadres is al geregistreerd" het meest voorkomende enumerationlek in door AI gebouwde producten is.

## Beperk het Verzoek, Niet Alleen de Poging

Twee limieten, en de tweede ontbreekt meestal.

Beperk resetverzoeken per account en per adres, zodat een aanvaller geen honderden tokens voor één slachtoffer kan genereren — wat zowel de kans op onderschepping vergroot als de persoon overspoelt met mail.

Beperk resetverzoeken per IP-adres en per tijdvak, omdat hetzelfde endpoint op verzoek e-mail stuurt naar willekeurige adressen. Zonder limiet is uw product een gratis mailingtool met de reputatie van uw domein eraan vast, en het eerste gevolg is dat uw legitieme mail in spamfolders terechtkomt.

## Beëindig Na een Reset Al het Andere

Een wachtwoordreset betekent vaak "ik denk dat iemand anders toegang heeft". Het proces moet zich gedragen alsof dat waar is.

Maak elke andere sessie van het account ongeldig, zodat een aanvaller die is ingelogd wordt uitgelogd. Laat het e-mailadres van het account weten dat het wachtwoord is gewijzigd, met een tijdstip en een manier om te reageren als het niet de eigenaar was — verstuurd naar het adres dat op het moment van de wijziging bekend was, want dat is de melding die een lopende accountovername opvangt.

En log de gebruiker niet automatisch in via de resetlink zelf. De link bewijst toegang tot een inbox; vragen om in te loggen met het nieuwe wachtwoord bewijst dat hij het heeft gekozen.

## De E-mailwijziging Is de Echte Kwetsbaarheid

Wachtwoordresets krijgen aandacht. Het e-mailadres van een account wijzigen krijgt er bijna geen, en het is de krachtigere handeling — wie het adres beheert, beheert elke toekomstige reset.

Drie beschermingen, en door AI gegenereerde implementaties hebben er zelden een.

Vereis het huidige wachtwoord, of een tweede factor, voordat de wijziging wordt geaccepteerd. Controleer het nieuwe adres door er een bevestigingslink naartoe te sturen, en pas de wijziging pas toe als erop is geklikt. En informeer het oude adres, met een periode waarin de wijziging vanuit dat bericht kan worden teruggedraaid.

Dat laatste redt een account wanneer een sessie al is gecompromitteerd: de aanvaller wijzigt het e-mailadres, de echte eigenaar krijgt een bericht op het oude adres, en één klik maakt het ongedaan.

## Herstel via Support Is de Menselijke Versie

Uiteindelijk verliest iemand de toegang tot zijn e-mail en schrijft hij u. Wat u daarna doet, is uw accountherstelproces, of u het nu hebt ontworpen of niet.

Bepaal vooraf welk bewijs u vraagt — iets wat alleen de accounthouder zou weten, bevestiging van een andere gebruiker in dezelfde organisatie, een geverifieerd betaalgegeven — en schrijf het op. Volg het dan, ook als de persoon gefrustreerd en hooggeplaatst is en haast heeft, want dat is precies de druk die een social-engineeringpoging uitoefent.

Leg elk handmatig herstel vast: wie het vroeg, wat werd gecontroleerd, wie het goedkeurde. Voor een zakelijk product is dat ook waar de beveiligingsvragenlijst van een klant naar vraagt.

## Wachtwoordregels Die Helpen in Plaats van Irriteren

Nu u toch in dit deel van het product bent, zijn de regels rond het wachtwoord zelf het herzien waard, omdat het conventionele advies dat de meeste gegenereerde code implementeert inmiddels als ronduit onbehulpzaam wordt beschouwd.

Samenstellingseisen — één hoofdletter, één cijfer, één symbool — duwen mensen naar voorspelbare vervangingen en een briefje in een la. Verplichte wijziging elke 90 dagen levert hetzelfde wachtwoord op met een oplopend cijfer. Beide zijn jaren geleden uit serieuze richtlijnen geschrapt, en beide verschijnen nog in nieuwe applicaties omdat ze in de trainingsdata staan.

Wat de huidige richtlijnen ondersteunen: een minimale lengte van ten minste twaalf tekens zonder samenstellingsregels en zonder willekeurig maximum onder de 64; het gekozen wachtwoord controleren tegen een lijst met bekende gelekte wachtwoorden, wat een gratis API-aanroep is en de echt gevaarlijke keuzes vangt; spaties en de volledige tekenset toestaan, zodat wachtzinnen werken; en wachtwoorden nooit volgens schema laten verlopen, alleen bij aanwijzingen van compromittering.

Sla ze op met een modern hashalgoritme dat voor dit doel is ontworpen. Gebruikt u een authenticatieprovider, dan is dit geregeld; hasht een deel van uw applicatie zelf wachtwoorden — wat gebeurt in door AI gebouwde producten die een tweede inlogroute voor beheerders toevoegden — controleer dan wat het gebruikt, want een snelle algemene hash is het verkeerde instrument en komt met enige regelmaat voor.

Nog iets kleins dat het supportvolume meetbaar vermindert: laat mensen zien wat ze typten. Een knop om het wachtwoordveld zichtbaar te maken, is geen beveiligingszwakte, en voorkomt heel veel mislukte logins.

En behandel de rate limiting van het inlogformulier zelf als deel van dit werk: een klein aantal pogingen per account en per adres, met een vertraging in plaats van een permanente blokkade, zodat een vastberaden gokker wordt gestopt zonder iemand een manier te geven om uw klanten bewust buiten hun eigen account te sluiten.

## Dit Inrichten

Voor een bestaand product kost dit doorgaans een halve dag: resettokens veilig gegenereerd, binnen een uur verlopend, eenmalig, gehasht opgeslagen en eerdere tokens ongeldig makend; identieke antwoorden en timing, ongeacht of een account bestaat, ook toegepast op registratie en inloggen; rate limits per account en per IP; alle andere sessies ongeldig gemaakt bij een reset, met een melding naar het bekende adres; geen automatisch inloggen via de link; e-mailwijzigingen die het huidige wachtwoord vereisen, met bevestiging op het nieuwe adres en een omkeerbare melding naar het oude; en een geschreven procedure voor herstel via support met een registratie van elk gebruik.

LaunchStudio behandelt herstelprocessen in de beveiligingsreview, waar ze consequent zwakker zijn dan de login die ze beschermen. De engineers zijn van Manifera — elf jaar, 120+ engineers, klanten als Vodafone, TNO en CFLW.

[Vraag ons een reset te proberen op uw eigen account](https://launchstudio.eu/nl/#contact). Het is de snelste beveiligingstest die wij doen.

## Echt voorbeeld

### Een Account Overgenomen via de E-mailwijziging

Gerben Stuiver bouwde Klantportaal in Lovable: een klantportaal voor accountants- en administratiekantoren, waar 62 kantoren documenten en berichten delen met zo'n 4.000 zakelijke klanten.

Het resetten van het wachtwoord was redelijk: een willekeurig token dat na 24 uur verliep. Het wijzigen van het e-mailadres was helemaal niet beschermd. Een ingelogde gebruiker kon het adres op het account wijzigen zonder bevestiging met wachtwoord, zonder controle van het nieuwe adres, en zonder melding aan het oude.

De laptop van een klant werd via ongerelateerde malware gecompromitteerd en het sessiecookie werd gestolen. De aanvaller gebruikte de sessie om het e-mailadres van het account te wijzigen in een adres dat hij beheerde, wachtte tot de sessie verliep, en gebruikte daarna het gewone resetproces — dat nu naar zijn adres stuurde — om een wachtwoord in te stellen. Hij had het account voorgoed, en de echte eigenaar zat buitengesloten zonder ergens een melding van te krijgen.

Het bedrijf ontdekte het toen hun accountant een documentverzoek noemde dat ze niet hadden gedaan.

Twee werkdagen: e-mailwijzigingen vereisen nu het huidige wachtwoord, sturen een bevestigingslink naar het voorgestelde nieuwe adres, worden pas toegepast na bevestiging, en informeren het oude adres met een terugdraailink die 48 uur geldig is; de levensduur van resettokens teruggebracht van 24 uur naar 30 minuten, eenmalig gemaakt, gehasht opgeslagen, en eerdere openstaande tokens ongeldig makend; identieke antwoorden en timing voor bekende en onbekende adressen bij reset, registratie en inloggen, die eerder duidelijk zeiden of een e-mailadres was geregistreerd; rate limits per account en per IP op het reset-endpoint, dat er geen had en de maand ervoor was gebruikt om op één middag 900 resetmails te versturen; alle sessies ongeldig gemaakt bij een wachtwoordwijziging, met een melding naar het bekende adres; automatisch inloggen via de resetlink verwijderd; en een geschreven procedure voor herstel via support die bevestiging vereist van een tweede contactpersoon bij hetzelfde kantoor, met elk gebruik vastgelegd.

**Resultaat:** het account werd handmatig hersteld en het incident werd gemeld aan het getroffen bedrijf en hun accountant. In het jaar daarna is de melding naar het oude adres vier keer verstuurd bij een e-mailwijziging, waarvan er één werd teruggedraaid door een klant die de wijziging niet had gedaan — een poging tot overname die binnen elf minuten werd opgevangen door een bericht dat niets kostte om te versturen.

> *"Iedereen beschermt het wachtwoord. Niemand beschermt het adres waar de wachtwoordreset naartoe gaat, en dat is degene die het account echt bezit."*
> — **Gerben Stuiver, Oprichter, Klantportaal (Zwolle)**

**Kosten & Doorlooptijd:** €2.300 (bescherming van e-mailwijziging met bevestiging en terugdraaien, versteviging van resettokens, verwijderen van enumeration in drie processen, rate limiting, ongeldig maken van sessies en melding, procedure voor herstel via support) — afgerond in 2 werkdagen.

## Veelgestelde vragen

### Hoe lang moet een wachtwoordresetlink geldig zijn?

Vijftien tot zestig minuten, eenmalig, en ongeldig gemaakt wanneer er een nieuwere wordt aangevraagd. Een link die een dag of een week geldig is, is een sleutel in een inbox.

### Waarom mag het resetformulier niet zeggen of een account bestaat?

Omdat het bevestigt wie uw product gebruikt — wat vertrouwelijk is voor gevoelige categorieën en, voor elk product, een phishingcampagne een geverifieerde adressenlijst geeft. Houd het antwoord en de timing ervan identiek.

### Moet een resetlink de gebruiker automatisch inloggen?

Nee. De link bewijst toegang tot een inbox. Vraag om in te loggen met het nieuwe wachtwoord, zodat het account wordt betreden door iemand die de inloggegevens kent.

### Wat beschermt het wijzigen van het e-mailadres op een account?

Het huidige wachtwoord of een tweede factor, bevestiging op het nieuwe adres voordat de wijziging wordt toegepast, en een melding naar het oude adres met een terugdraailink. De meeste door AI gebouwde producten hebben geen van deze.

### Wat moet er na een wachtwoordreset met andere sessies gebeuren?

Ze moeten allemaal eindigen. Een reset betekent vaak dat de gebruiker vermoedt dat iemand anders toegang heeft, en het proces moet zich gedragen alsof dat waar is.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Hoe lang moet een wachtwoordresetlink geldig zijn?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Vijftien tot zestig minuten, eenmalig, gehasht opgeslagen, en ongeldig gemaakt wanneer er een nieuwer verzoek wordt gedaan."
      }
    },
    {
      "@type": "Question",
      "name": "Waarom mag een resetformulier niet onthullen of een account bestaat?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Het bevestigt wie uw klanten zijn — op zichzelf gevoelig en de basis van een effectieve phishinglijst. Houd de tekst en timing van het antwoord identiek."
      }
    },
    {
      "@type": "Question",
      "name": "Moet een resetlink de gebruiker automatisch inloggen?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Nee. De link bewijst alleen toegang tot een inbox; vereis een login met het nieuw gekozen wachtwoord."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe moet een wijziging van het e-mailadres worden beschermd?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Vereis het huidige wachtwoord of een tweede factor, bevestig op het nieuwe adres vóór toepassing, en informeer het oude adres met een terugdraailink."
      }
    },
    {
      "@type": "Question",
      "name": "Wat gebeurt er met sessies na een wachtwoordreset?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ze moeten allemaal ongeldig worden gemaakt, aangezien een reset meestal betekent dat de gebruiker vermoedt dat iemand anders toegang heeft."
      }
    }
  ]
}
</script>
