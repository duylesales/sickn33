---
Titel: "Supabase-beveiliging: sessies, rollen en het probleem met de admin-vlag"
Trefwoorden: supabase beveiliging, authenticatie rollen admin vlag, sessiebeheer AI app, privilege escalation prototype, ai app beveiliging, LaunchStudio, Manifera
Koperfase: Beslissing
Doelgroep: Technische solo-oprichter / Indie hacker
---

# Supabase-beveiliging: sessies, rollen en het probleem met de admin-vlag

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Supabase-beveiliging: sessies, rollen en het probleem met de admin-vlag",
  "description": "Hoe met AI gegenereerde apps doorgaans identiteit en rechten modelleren, waarom een admin-veld in een gebruikerstabel een kwetsbaarheid is in plaats van een feature, en hoe je een betrouwbaar rollensysteem opbouwt.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-06-16",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/sessions-roles-and-admin-flags-in-ai-built-apps" }
}
</script>

Ergens in vrijwel elke met AI gebouwde applicatie bevindt zich een databasekolom met de naam `is_admin`, of een veld `role` met de waarde "admin", opgeslagen in exact dezelfde tabel als de weergavenaam en profielfoto van de gebruiker. Het werkt ogenschijnlijk prima: het beheerdersdashboard verschijnt voor de juiste mensen en blijft keurig verborgen voor reguliere gebruikers.

De vraag die bepaalt of dit een handige functionaliteit is of een kritiek beveiligingslek, luidt: wie heeft het recht om naar die specifieke kolom te schrijven? In een alarmerend groot aantal prototypes is het antwoord: de gebruiker zelf.

## Drie vragen die elke applicatie moet beantwoorden

Authenticatie in een serieus product is niet één vraagstuk, maar drie afzonderlijke lagen. Met AI gegenereerde apps lossen doorgaans de eerste laag soepel op, en behandelen de overige twee min of meer per ongeluk:

**Wie ben je?** Inloggen, sessies, tokens. Supabase Auth, Auth0, Firebase en vergelijkbare diensten handelen dit uitstekend af. Dat is precies de reden waarom met AI gebouwde apps zo snel over een werkend inlogscherm beschikken.

**Wat mag je doen?** Rollen, permissies, eigenaarschap van data. Dit is waar prototypes het zwakst zijn, omdat hiervoor diepgaande kennis nodig is van jouw specifieke bedrijfslogica - kennis die simpelweg niet in je initiële prompt zat.

**Klopt dat op dít exacte moment nog steeds?** Sessies verlopen, rollen veranderen, accounts worden geblokkeerd en abonnementen worden beëindigd. Een permissie die eenmalig bij het inloggen wordt bepaald en daarna nooit meer wordt geverifieerd, is een bevoegdheid die veel langer actief blijft dan gerechtvaardigd is.

## Waarom een admin-veld in de gebruikerstabel gevaarlijk is

Dit ontwerppatroon is alomtegenwoordig omdat het de meest voor de hand liggende structuur is die een taalmodel kan genereren: gebruikers hebben eigenschappen, beheerder zijn is een eigenschap, dus die hoort thuis in de tabel `users` of `profiles`.

Het acute gevaar ontstaat zodra die tabel wordt ontsloten via een automatisch gegenereerde API - zoals standaard het geval is in een typische Supabase-omgeving - en het database-toegangsbeleid (Row Level Security) gebruikers toestaat om hun eigen rij bij te werken. Op het eerste gezicht klinkt dat logisch: een gebruiker moet immers zijn eigen naam kunnen aanpassen. Maar tenzij het beleid expliciet het bijwerken van die specifieke rol-kolom blokkeert, betekent dit dat een gebruiker een updateverzoek kan sturen waarin hij zijn eigen rol verandert in `admin`.

De aanval vereist geen speciale tools of hackersvaardigheden: open het tabblad Netwerk in de browserontwikkelaarstools, bekijk het JSON-formaat van een profielwijziging en stuur hetzelfde verzoek opnieuw met één extra veld: `"role": "admin"`. Als jouw applicatie vervolgens simpelweg de rol uit die profieltabel uitleest om beheerdersrechten toe te kennen, heb je zojuist volledige beheerdersrechten weggegeven via een doodgewoon instellingenformulier.

Er is nog een subtielere variant. Sommige gegenereerde apps controleren de rol uitsluitend in de browser (client-side) en bepalen aan de hand daarvan welke knoppen of menu's worden getoond. Een knop verbergen in de gebruikersinterface is echter geen beveiligingscontrole - iedereen kan het achterliggende API-endpoint direct aanroepen. Als de server de rol niet onafhankelijk verifieert, wordt je admin-paneel slechts beschermd door de beleefdheid van de bezoeker.

## Hoe een solide rollenmodel eruitziet

**Rollen leven op een plek waar gebruikers nooit naartoe kunnen schrijven.** Een aparte koppeltabel met strikte policies die het toelaten om je eigen rol te lezen, maar elke schrijfactie categorisch verbieden. Of custom JWT-claims die uitsluitend via serverfuncties worden gemuteerd. De kolom die je gebruikers mogen bewerken en de kolom die macht verleent, mogen nooit dezelfde kolom zijn.

**Permissies worden afgedwongen op de datalaag.** Niet in de frontend-interface en niet uitsluitend in een API-route. In een applicatie met Supabase betekent dit Row Level Security (RLS) policies die de rol van de aanvrager verifiëren voor elke gevoelige database-operatie. Zo kan een endpoint nooit omzeild worden door de database-API rechtstreeks te bevragen.

**De server beslist, de interface volgt.** Toon gerust een beheerdersmenu op basis van een rol in de frontend - maar elke geprivilegieerde bewerking moet de rol opnieuw op de server valideren, alsof de grafische interface helemaal niet bestaat.

**Rollen zijn overzichtelijk en vernoemd naar de organisatie.** Eigenaar, medewerker, lid, lezer. Vier of vijf heldere, goed begrepen rollen werken oneindig veel beter dan twintig fijnmazige permissievlaggen die niemand meer kan overzien en die snel afwijken van de werkelijkheid.

**Wijzigingen zijn direct van kracht.** Wanneer iemand uit een team wordt verwijderd of in rang wordt verlaagd, moet het eerstvolgende verzoek dat direct weerspiegelen. Als je app permissies langdurig cacht in een JWT-token, blijft een verwijderde medewerker bevoegd totdat dat token verloopt - precies het risico dat je wilde elimineren.

## De multi-tenant valkuil

De meest ernstige variant van dit probleem treedt op bij B2B-applicaties die worden verkocht aan organisaties: een tandartspraktijk, een school of een logistiek bedrijf. Gebruikers behoren tot een organisatie, en gegevens behoren tot een organisatie.

Gegenereerde apps dwingen standaard vaak alleen af: "je kunt je eigen records inzien". Dat is immers de enige regel die een prototype voor één enkele gebruiker nodig heeft. Wat structureel wordt vergeten, is de tweede noodzakelijke voorwaarde: je mag records zien die toebehoren aan jouw organisatie, en *uitsluitend* die van jouw organisatie.

De resulterende kwetsbaarheid ziet er in de praktijk zo uit: een medewerker van Praktijk A kan medische dossiers van Praktijk B inzien door simpelweg een ID in het webadres te wijzigen, omdat elke beveiligingsregel alleen controleert of de bezoeker is ingelogd, niet voor welk bedrijf. Voor een B2B-product is dit niet zomaar een programmeerfout; het is de exacte vraag die op elk security-questionnaire van zakelijke inkopers staat, en de reden waarom grote deals stranden tijdens de security-audit.

Dit structureel oplossen betekent dat elke query en elke RLS-policy een organisatievoorwaarde bevat, en dat het organisatie-ID altijd afkomstig is van de betrouwbare serversessie, nooit uit invoer die door de browser is meegegeven.

## Sessies: het onderdeel dat iedereen één keer instelt en daarna vergeet

**Levensduur van tokens.** Oneindig lange sessies zijn gemakkelijk voor gebruikers, maar betekenen dat een gestolen token wekenlang bruikbaar blijft. Korte sessies met automatische refresh-tokens zijn de industriestandaard; de standaardwaarde die je AI-builder koos, was geoptimaliseerd voor ontwikkelgemak, niet voor jouw bedrijfsrisico.

**Sessie-ongeldigverklaring bij wachtwoordwijziging.** Als het wijzigen van een wachtwoord actieve sessies op andere apparaten niet direct beëindigt, kan een gebruiker die vermoedt dat zijn account is gehackt de indringer niet daadwerkelijk buitensluiten.

**Uitloggen dat de server bereikt.** Alleen de lokale browseropslag leegmaken beëindigt een sessie niet op de server.

**Geblokkeerde accounts.** Een inlog blokkeren doet niets tegen een sessie die op dat moment al actief is, tenzij je backend de actieve accountstatus bij elk binnenkomend verzoek controleert.

## Test je eigen permissiemodel in twintig minuten

- Maak twee normale testaccounts aan en één beheerdersaccount. Log in als normale gebruiker.
- Open het tabblad Netwerk in je browser, zoek het verzoek op waarmee je profiel wordt bijgewerkt, en verstuur het opnieuw met een extra veld `role: "admin"` of `is_admin: true`. Controleer vervolgens of je rol is gewijzigd.
- Roep een admin-endpoint rechtstreeks aan in de browser of via curl terwijl je bent ingelogd als normale gebruiker, buiten de gebruikersinterface om.
- Als je product organisaties of teams ondersteunt, maak dan twee verschillende organisaties aan en probeer gegevens van de andere organisatie op te vragen door een ID in de URL aan te passen.
- Wijzig je wachtwoord in de ene browser en kijk of je in een tweede browser nog steeds ongehinderd bent ingelogd.
- Verwijder een teamlid uit een organisatie en test hoe lang diegene nog toegang houdt tot gevoelige data.

Elk van deze tests kost niet meer dan een paar regels in de browserconsole en representeert een veelvoorkomend incidentpatroon. Alles wat slaagt, is een serieus beveiligingsrisico.

## De beveiligingslaag bouwen die nooit werd geprompt

Permissiemodellering is het duidelijkste voorbeeld van werk dat niet automatisch door AI gegenereerd kan worden, omdat de regels voortvloeien uit jouw bedrijfsmodel en niet uit generieke codevoorbeelden. De engineers van LaunchStudio bouwen dit fundament als onderdeel van de afronding: rollen verplaatst naar tabellen waar gebruikers niet naar kunnen schrijven, Row Level Security afgedwongen op databaseniveau, multi-tenant isolatie consequent toegepast, sessiebeveiliging aangescherpt en alle bevoegdheden gevalideerd op de server.

De frontend die je in Lovable, Bolt of Cursor hebt gebouwd blijft onaangetast, de intellectuele eigendom blijft van jou, en het resultaat wordt schoon gedocumenteerd en AI-leesbaar achtergelaten. Dit is het [Launch Ready pakket](https://launchstudio.eu/nl/#packages), gerealiseerd door het team van Manifera vanuit Amsterdam en Ho Chi Minhstad, met elf jaar ervaring in bedrijfskritische softwaresystemen voor klanten zoals Vodafone, TNO en CFLW.

Heb je een `is_admin`-kolom in je database en weet je niet 100% zeker wie daarnaartoe kan schrijven? [Praat met een engineer die AI-gegenereerde code begrijpt](https://launchstudio.eu/nl/#contact).

## Uitnodigingen: de stroom die geruisloos rechten lekt

Als je applicatie teams of organisaties ondersteunt, verdient het uitnodigingsproces extra aandacht. Dit is namelijk de plek waar toegangsbeslissingen worden genomen door eindgebruikers die niet stilstaan bij beveiliging:

**Uitnodigingslinks zijn feitelijk inloggegevens.** Een link die met één klik lidmaatschap verleent, is een digitale sleutel die per e-mail wordt verstuurd. Deze link moet eenmalig bruikbaar zijn, strikt gekoppeld aan één specifiek e-mailadres en voorzien zijn van een vervaldatum - maximaal zeven dagen is een gezonde termijn. Gegenereerde flows produceren regelmatig uitnodigingslinks die voor altijd en door iedereen gebruikt kunnen worden, waardoor links worden doorgestuurd, in groepsapps belanden en jarenlang actief blijven.

**De rechten van de uitnodiger begrenzen de uitnodiging.** Een gewoon teamlid mag nooit een beheerder kunnen uitnodigen. Als de rol in de browser wordt geselecteerd en met het formulierverzoek wordt meegestuurd, kan deze worden gemanipuleerd. De server moet daarom altijd controleren of de uitnodiger zelf wel bevoegd is om die rol toe te kennen.

**Een e-mailwijziging is een toegangsverandering.** Als een gebruiker zijn account-e-mailadres kan wijzigen zonder het nieuwe adres te bevestigen, kan een uitnodiging die aan een specifiek e-mailadres is gekoppeld eenvoudig worden gekaapt. Vereis altijd verificatie van het nieuwe adres én stuur een notificatie naar het oude adres.

**Verwijdering moet onmiddellijk en volledig zijn.** Wanneer een medewerker een organisatie verlaat, moeten diens sessies voor die organisatie bij het eerstvolgende verzoek direct worden geblokkeerd - niet pas wanneer een sessietoken over een week verloopt. Test dit expliciet: verwijder een gebruiker in browser A en probeer direct een organisatiedossier te openen in browser B.

**Openstaande uitnodigingen zijn statusrecords.** Een uitnodiging die is verstuurd naar iemand die nog niet heeft geaccepteerd, voor een organisatie die inmiddels is overgedragen of verwijderd, mag nooit automatisch toegang geven tot wat zich nu op die plek bevindt.

Elk van deze punten betreft kleine stukjes validatielogica. Samen bepalen ze of je teamfunctionaliteit een waardevolle toevoeging is, of de grootste openstaande achterdeur in je product.

## Echt voorbeeld

### Een veterinair platform waar elke praktijk elkaars patiëntendossiers kon inzien

Marijn Kuipers bouwde DierZorg in Lovable: een gedeeld softwareplatform waarmee onafhankelijke dierenartsenpraktijken rond Apeldoorn afspraken en patiëntendossiers beheren. Elf dierenartsenpraktijken hadden zich al aangesloten vóór de eerste professionele security review plaatsvond.

Twee bevindingen waren doorslaggevend. De profieltabel van gebruikers bevatte een veld `role` met een database-policy die gebruikers toestond hun eigen rij bij te werken. Hierdoor kon elke geregistreerde dierenartsassistent zichzelf binnen tien seconden promoveren tot systeembeheerder door één JSON-veld toe te voegen aan het profielformulier. Daarnaast controleerde het data-toegangsbeleid alleen of de aanvrager was ingelogd en het specifieke consult had aangemaakt - er werd nergens gecontroleerd tot welke praktijk het dossier behoorde. Een dierenarts bij Praktijk A kon daardoor patiëntendossiers van Praktijk B openen door simpelweg een volgnummer in de URL aan te passen.

De tweede bevinding raakte direct de commerciële toekomst van het bedrijf: DierZorg zat op dat moment midden in inkoopgesprekken met een regionale maatschap van negen dierenklinieken, waarvan het security-questionnaire exact naar deze gegevensscheiding vroeg.

Negen werkdagen waren nodig om de architectuur waterdicht te maken: rollen verplaatst naar een aparte, door de server beheerde koppeltabel met alleen-lezen rechten voor gebruikers; alle beheerdersbewerkingen server-side gevalideerd; een strikte organisatieconditie toegevoegd aan elke databasequery en RLS-policy waarbij het praktijk-ID betrouwbaar uit de serversessie wordt gehaald; sessies direct ongeldig verklaard bij wachtwoordwijziging of praktijkverwijdering; en een geautomatiseerde testsuite ingericht die met twee verschillende praktijkaccounts inlogt en verifieert dat geen van beiden data van de ander kan inzien.

**Resultaat:** de groep van negen klinieken tekende zes weken later na een vlekkeloze security-audit, en DierZorg draait de permissietestsuite nu automatisch bij elke nieuwe release.

> *"Iedereen had zichzelf vanuit de profielinstellingen tot admin kunnen bombarderen. Het platform stond al vier maanden live en de enige reden dat er niets misging, is dat niemand het had geprobeerd."*
> - **Marijn Kuipers, Oprichter, DierZorg (Apeldoorn)**

**Kosten & Doorlooptijd:** € 3.700 (Launch Ready Pakket: rollenmodel, multi-tenant isolatie, sessiebeveiliging en permissietests) - afgerond in 9 werkdagen.

## Veelgestelde vragen

### Wat is er mis met het opslaan van een rol in de gebruikerstabel?

Op zichzelf niets, mits gebruikers technisch niet naar die kolom kunnen schrijven. Het probleem ontstaat wanneer een Row Level Security-beleid gebruikers toestaat hun eigen profielrij bij te werken en de rol in diezelfde rij staat. Hierdoor kan een gebruiker zichzelf beheerdersrechten toekennen door één extra veld mee te sturen in een regulier profielverzoek.

### Is het verbergen van het admin-menu voldoende om het te beveiligen?

Nee, absoluut niet. Een element verbergen in de gebruikersinterface haalt alleen de visuele link weg, niet de daadwerkelijke technische mogelijkheid. Iedereen kan het achterliggende API-endpoint direct aanroepen. Elke bevoorrechte operatie moet daarom altijd onafhankelijk op de server worden gevalideerd, ongeacht wat de interface toont.

### Hoe voorkom ik dat de ene klantorganisatie de data van de andere ziet?

Elke databasequery en Row Level Security policy moet een expliciete organisatievoorwaarde bevatten. Cruciaal hierbij is dat het organisatie-ID altijd afkomstig is van de geverifieerde serversessie, en nooit van een parameter die de browser van de gebruiker vrij kan meesturen. Dit is het meest voorkomende beveiligingslek in B2B-prototypes.

### Moeten gebruikerssessies snel verlopen?

Kortere sessies met automatische refresh-tokens zijn de gangbare standaard. Nog belangrijker dan de exacte tijdsduur is de directe ongeldigverklaring van sessies: actieve sessies moeten onmiddellijk worden beëindigd zodra een wachtwoord verandert, een account wordt geblokkeerd of een medewerker uit een team wordt verwijderd.

### Kan ik dit zelf testen zonder diepgaande technische hulp?

Grotendeels wel. Maak twee testaccounts aan, probeer elkaars gegevens te openen door ID's in de URL te wijzigen, probeer een rol-veld mee te sturen bij een profielwijziging, en controleer of een wachtwoordwijziging in de ene browser de sessie in een andere browser direct beëindigt. Elk experiment dat slaagt, legt een kwetsbaarheid bloot die directe actie vereist.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Wat is er mis met het opslaan van een rol in de gebruikerstabel?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Niets, mits gebruikers niet naar die kolom kunnen schrijven. Het probleem ontstaat wanneer gebruikers hun eigen profielrij mogen updaten waarin ook de rol staat, waardoor ze zichzelf met één extra veld admin kunnen maken."
      }
    },
    {
      "@type": "Question",
      "name": "Is het verbergen van het admin-menu voldoende om het te beveiligen?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Nee. Het verbergen van een knop verwijdert alleen de visuele weergave, niet de mogelijkheid. Geprivilegieerde bewerkingen moeten altijd server-side worden geverifieerd, los van de interface."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe voorkom ik dat de ene klantorganisatie de data van de andere ziet?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Elke query en policy moet een organisatievoorwaarde bevatten, waarbij het organisatie-ID afkomstig is van de betrouwbare serversessie en niet vanuit de browser. Dit is het meest voorkomende lek in B2B-prototypes."
      }
    },
    {
      "@type": "Question",
      "name": "Moeten gebruikerssessies snel verlopen?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Kortere sessies met refresh-tokens zijn de standaard, maar directe invalidatie is belangrijker: sessies moeten eindigen bij wachtwoordwijziging, accountblokkade en verwijdering uit een organisatie."
      }
    },
    {
      "@type": "Question",
      "name": "Kan ik dit zelf testen zonder diepgaande technische hulp?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Grotendeels wel: maak twee accounts, probeer elkaars data te lezen via aangepaste ID's, voeg een rolveld toe aan een profielupdate en controleer of wachtwoordwijziging andere browsers uitlogt."
      }
    }
  ]
}
</script>
