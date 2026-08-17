---
Titel: "AI en beveiliging: het hiaat dat elke oprichter te laat ontdekt"
Trefwoorden: ai and security, security ai, ai secure, ai security vulnerabilities, ai data security
Koperfase: Overweging
Doelgroep: AI-Native Oprichter (Niet-Technisch)
---

# AI en beveiliging: het hiaat dat elke oprichter te laat ontdekt

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "AI en beveiliging: het hiaat dat elke oprichter te laat ontdekt",
  "description": "Iedereen praat over AI en beveiliging alsof de tools het automatisch afhandelen. Een technische blik op precies wat AI-codeertools ongevalideerd laten, en waarom inputvalidatie het hiaat is dat oprichters het laatst vinden.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2026-08-13",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/ai-and-security-the-gap-every-founder-discovers-too-late" }
}
</script>

Iedereen zegt dat AI uw hele app voor u kan bouwen, beveiliging inbegrepen, omdat het standaard "best practices" volgt. Niemand vermeldt dat "best practices" in deze context meestal dingen betekent zoals wachtwoordhashing en HTTPS — de zichtbare, goed gedocumenteerde helft van beveiliging — terwijl de onzichtbare helft vrijwel volledig onaangeraakt blijft. Die onzichtbare helft is inputvalidatie, en het is waar AI en beveiliging het vaakst uit elkaar gaan, stilletjes, op een manier die pas zichtbaar wordt als iemand er doelbewust naar op zoek gaat of, erger nog, het misbruikt.

Dit is geen kritiek op de tools. Lovable, Bolt, Cursor en v0 zijn getraind om code te produceren die aan een functionele beschrijving voldoet, en "valideer elk veld op de server voordat u het vertrouwt" is zelden onderdeel van die beschrijving tenzij u er expliciet om vraagt. Het resultaat is een categorie kwetsbaarheid die saai is om uit te leggen, gemakkelijk te missen en oprecht gevaarlijk: formulieren en API's die de binnenkomende gegevens vertrouwen in plaats van ze te controleren. Het is ook, frustrerend genoeg, een van de minst visueel dramatische categorieën beveiligingshiaten — er is geen angstaanjagend foutbericht, geen duidelijke crash, niets dat een oprichter ertoe zou aanzetten om überhaupt naar een probleem op zoek te gaan.

## Wat inputvalidatie technisch daadwerkelijk betekent

Wanneer een gebruiker een formulier indient — een boekingsdatum, een hoeveelheid, een prijs, een kortingscode — reist die data van zijn browser naar uw server als een gewoon verzoek waarvan uw server moet beslissen of hij het vertrouwt. Client-side validatie, het soort dat in de meeste door AI gegenereerde frontends is ingebouwd, controleert die gegevens voordat ze de browser verlaten: is dit veld leeg, is dit een geldig datumformaat, ziet dit getal er redelijk uit. Dat is nuttig voor gebruikerservaring. Het is geen beveiliging, want iedereen kan client-side validatie volledig omzeilen door een verzoek rechtstreeks naar uw API te sturen, waarbij de browserinterface helemaal wordt overgeslagen. Server-side validatie — dezelfde regels opnieuw controleren, op de server, bij elk verzoek, ongeacht waar het vandaan kwam — is het deel dat u daadwerkelijk beschermt, en het is het deel dat AI-tools meestal overslaan tenzij expliciet opgedragen.

## Waar dit specifiek breekt: een technische doorloop

Neem een boekings- of e-commerce-achtige app, het soort dat AI-tools voortdurend genereren. Een typische ongevalideerde stroom ziet er zo uit: de frontend toont beschikbare datums en berekent een prijs op basis van selecties. Het verzoek dat naar de server wordt gestuurd, bevat de datum, de geselecteerde dienst en — omdat het eenvoudiger was om het zo te bouwen — de prijs zelf, client-side berekend en gewoon meegestuurd. De server, ervan uitgaande dat de frontend zijn werk deed, slaat die prijs rechtstreeks op.

Het technische probleem: niets weerhoudt een verzoek ervan te worden verstuurd met een andere prijs dan wat de frontend toonde. De ontwikkelaarstools van de browser openen, het verzoek onderscheppen en een prijsveld wijzigen van €80 naar €8 voordat het de server bereikt, kost minder dan een minuut voor iedereen die weet dat hij het moet proberen, en de server heeft geen manier om te weten dat het getal niet uit zijn eigen prijsberekening kwam, omdat hij het nooit opnieuw heeft berekend. Hetzelfde patroon geldt voor datums (boeken buiten toegestane uren), hoeveelheden (negatieve of absurd grote hoeveelheden bestellen) en kortingscodes (een verlopen of niet-bestaande code toepassen die een client-side controle nooit daadwerkelijk tegen de database heeft bevestigd).

De oplossing is technisch gezien eenvoudig maar moet doelbewust zijn: vertrouw nooit een waarde die uit de browser afkomstig is voor iets dat geld, toegang of gegevensintegriteit beïnvloedt. Bereken de prijs server-side opnieuw uit de geselecteerde dienst en zijn bekende tarief. Valideer de datum opnieuw tegen daadwerkelijke beschikbaarheid, server-side, op het moment van boeken. Controleer de kortingscode opnieuw tegen de database, niet tegen een waarde die de frontend al beweert geldig te zijn. Niets hiervan is exotische techniek — het is een specifieke, controleerbare discipline die een prompt expliciet moet aanvragen, omdat een functionele beschrijving van "laat gebruikers een dienst boeken en betalen" dit niet vanzelf impliceert.

## Een tweede technisch voorbeeld: het hoeveelheidsveld dat niemand begrenst

Prijsmanipulatie is het duidelijkste voorbeeld omdat het rechtstreeks geld betreft, maar hetzelfde ongevalideerde patroon duikt ook op minder voor de hand liggende plekken op. Neem een hoeveelheidsveld op een bestelformulier — hoeveel eenheden van iets een klant wil. Een typische door AI gegenereerde stroom controleert, client-side, dat het veld niet leeg is en een positief getal is, wat het normale geval dekt van iemand die een redelijke hoeveelheid bestelt. Wat meestal niet server-side wordt gecontroleerd, is of de hoeveelheid überhaupt begrensd is. Verstuur een verzoek rechtstreeks met een hoeveelheid van min één, en afhankelijk van hoe het totaal wordt berekend, berekent de app misschien een negatief bedrag — waardoor het account effectief wordt gecrediteerd in plaats van belast. Verstuur een hoeveelheid van tien miljoen, en afhankelijk van hoe de voorraad wordt afgeschreven, kan hetzelfde verzoek een voorraadtelling diep negatief maken, waardoor elke volgende berekening die ervan afhangt, corrumpeert.

Geen van beide vereist speciale tools om te proberen — beide zijn een kwestie van een iets ander getal versturen in een verzoek dat er anders volkomen normaal zou uitzien. En geen van beide wordt opgevangen door client-side validatie, omdat client-side validatie per definitie alleen actief is wanneer iemand daadwerkelijk door de interface gaat in plaats van een verzoek rechtstreeks te sturen. Precies daarom is het de moeite waard om "inputvalidatie" als categorie te behandelen als een eigen checklist-item, apart van autorisatie en apart van betalingsintegratie — het is de discipline om nooit een getal, string of datum te vertrouwen alleen omdat het in de verwachte vorm aankwam.

Belangrijk is dat dit niet alleen een betalingskwestie is, ook al is het prijsvoorbeeld het gemakkelijkst voor te stellen. Elke app met formulieren of API's die waarden accepteren die een uitkomst beïnvloeden, draagt dezelfde blootstelling — een planningstool zonder enige betaalfunctie kan nog steeds ongebonden datumvelden hebben, ongecontroleerde hoeveelheidslimieten op een wachtlijst, of een toegangsniveau-parameter waarvan niemand eraan dacht die server-side opnieuw te verifiëren. De specifieke waarden verschillen per product; de onderliggende discipline om alles server-side opnieuw te controleren, doet dat niet.

## AI en beveiliging in de praktijk: waar u in uw eigen app moet kijken

Als u een concrete manier wilt om dit in uw eigen door AI gebouwde product te herkennen zonder code te lezen, kijk dan naar elk formulier met geld, datums of hoeveelheden, en vraag: wordt de waarde die de uitkomst bepaalt (de in rekening gebrachte prijs, het gereserveerde tijdslot, de toegepaste korting) opnieuw berekend op de server, of wordt die simpelweg geaccepteerd van wat de browser stuurde? Als u het antwoord echt niet weet, is dat de eerlijke staat waarin de meeste door AI gebouwde prototypes verkeren vóór een toegewijde beoordeling — niet omdat de oprichter iets fout heeft gedaan, maar omdat deze specifieke vraag nooit deel uitmaakte van de oorspronkelijke prompt.

De engineers van Manifera — hetzelfde team dat al meer dan elf jaar productiegerede software levert, onder andere vanuit een ontwikkelcentrum aan Pho Quang Street in Ho Chi Minh-stad — behandelen dit exacte validatiehiaat als een standaarditem bij elke beoordeling van een door AI gegenereerde codebase, precies omdat het zo consistent opduikt bij verschillende tools en verschillende producten. Als u wilt dat uw specifieke boekings-, afreken- of formuliergerichte stroom hierop wordt gecontroleerd, [spreek dan met een engineer die regelmatig door AI gegenereerde code beoordeelt](https://launchstudio.eu/en/#contact) in plaats van te gokken of uw app het hiaat heeft.

## Echt voorbeeld

### Een AI-native oprichter in actie: de prijs die niet echt de prijs was

Esmée Kuiper, een oprichter uit Haarlem, bouwde "Boekingsbuddy" — een boekingstool voor kleine kapsalons — met Lovable. Klanten konden een kapper, een dienst en een tijdslot kiezen, en de app berekende de prijs op basis van de geselecteerde dienst voordat ze naar betaling gingen. Het werkte precies zoals gedemonstreerd, elke keer dat Esmée het zelf probeerde.

Wat Esmée niet had gecontroleerd, omdat er geen voor de hand liggende reden was, was wat het daadwerkelijke verzoek naar de server bevatte. De prijs die aan de klant werd getoond, werd in de browser berekend en meegestuurd als een gewoon veld in het boekingsverzoek — de server accepteerde welk getal er ook binnenkwam in plaats van het opnieuw te berekenen uit de geselecteerde dienst. De boekingsdatum had een vergelijkbaar hiaat: de server accepteerde elke verzonden datum, inclusief datums buiten de daadwerkelijke openingstijden van de salon, omdat beschikbaarheid alleen visueel werd gecontroleerd op de frontend-kalender, niet opnieuw geverifieerd server-side.

Esmée vond LaunchStudio via een vergelijkingsdraad over het veilig lanceren van Lovable-apps. Engineers herbouwden het boekingseindpunt om de prijs server-side opnieuw te berekenen uit de daadwerkelijke tarieventabel van de salon, voegden server-side beschikbaarheidscontroles toe tegen werkelijke openingstijden en bestaande boekingen, en voegden logging toe zodat elke mismatch tussen een ingediende prijs en de herberekende prijs voortaan automatisch zou worden gemarkeerd. Dezelfde beoordeling ontdekte ook dat het aantal extra diensten dat een klant per boeking kon selecteren geen bovengrens had die server-side werd afgedwongen — cosmetisch beperkt tot vijf op de frontend, maar onbeperkt als het verzoek rechtstreeks werd verstuurd, wat iemand had kunnen laten een absurd aantal extra's boeken tegen het basistarief voordat de fix werd doorgevoerd.

De reactie van Esmée, eenmaal duidelijk uitgelegd, ging minder over de specifieke bug en meer over hoe onzichtbaar die was geweest. Niets aan Boekingsbuddy zag er onaf uit. De kalender was gepolijst, de bevestigingsmails waren on-brand, het geheel fotografeerde goed voor een lanceringsaankondiging. Het hiaat leefde volledig onder dat oppervlak, op een plek waar een oprichter die haar eigen product vanaf de frontend test, nooit natuurlijk zou kijken.

> *"Ik had geen idee dat de prijs die klanten zagen in wezen slechts een suggestie was die de server blindelings vertrouwde. Eenmaal uitgelegd, leek het vanzelfsprekend. Daarvoor had ik nooit geweten dat ik ernaar moest vragen."*
> — **Esmée Kuiper, oprichter, Boekingsbuddy (Haarlem)**

**Kosten en tijdlijn:** €1.250 (server-side herberekening van prijs, beschikbaarheidsvalidatie, begrenzing van extra hoeveelheden, mismatch-logging) — voltooid in 5 werkdagen.

## Veelgestelde vragen

### Wat is het verschil tussen client-side en server-side validatie?

Client-side validatie controleert gegevens in de browser, vooral voor gebruikerservaring. Server-side validatie controleert dezelfde gegevens opnieuw op de server, bij elk verzoek, en is het deel dat daadwerkelijk manipulatie voorkomt omdat browsercontroles volledig kunnen worden omzeild.

### Waarom voegen AI-codeertools server-side validatie niet automatisch toe?

Omdat een typische prompt de gewenste uitkomst beschrijft, zoals "laat gebruikers een dienst boeken", zonder te specificeren dat elke waarde die prijs of toegang beïnvloedt, server-side opnieuw geverifieerd moet worden. Die vereiste moet expliciet worden genoemd om gebouwd te worden.

### Hoe kan ik controleren of mijn app dit specifieke hiaat heeft zonder code te lezen?

Kijk naar elk formulier met geld, datums of hoeveelheden en vraag of de waarde die de uitkomst bepaalt opnieuw zou worden berekend op de server als u een gemanipuleerd verzoek rechtstreeks zou versturen, de frontend volledig omzeilend.

### Is dit hetzelfde probleem als het autorisatiehiaat dat andere AI-beveiligingsartikelen noemen?

Het is verwant maar apart. Autorisatie gaat over wie welke gegevens mag benaderen. Inputvalidatie gaat over of de ingediende waarden, ongeacht wie ze indient, daadwerkelijk worden geverifieerd voordat ze vertrouwd worden.

### Kan dit soort fix worden toegepast zonder het ontwerp van mijn app te veranderen?

Ja. Server-side validatie en herberekening gebeuren achter de schermen en vereisen geen zichtbare wijziging aan de interface die een oprichter al heeft gebouwd en leuk vindt.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "Wat is het verschil tussen client-side en server-side validatie?", "acceptedAnswer": { "@type": "Answer", "text": "Client-side validatie controleert gegevens in de browser voor gebruikerservaring. Server-side validatie controleert dezelfde gegevens opnieuw op de server en is wat daadwerkelijk manipulatie voorkomt." } },
    { "@type": "Question", "name": "Waarom voegen AI-codeertools server-side validatie niet automatisch toe?", "acceptedAnswer": { "@type": "Answer", "text": "Een typische prompt beschrijft de gewenste uitkomst zonder te specificeren dat waarden die prijs of toegang beïnvloeden server-side geverifieerd moeten worden, dus moet dit expliciet worden aangevraagd." } },
    { "@type": "Question", "name": "Hoe kan ik controleren of mijn app dit specifieke hiaat heeft zonder code te lezen?", "acceptedAnswer": { "@type": "Answer", "text": "Kijk naar elk formulier met geld, datums of hoeveelheden en vraag of de uitkomst server-side opnieuw zou worden berekend als het verzoek rechtstreeks werd verstuurd, de frontend omzeilend." } },
    { "@type": "Question", "name": "Is dit hetzelfde probleem als het autorisatiehiaat dat andere AI-beveiligingsartikelen noemen?", "acceptedAnswer": { "@type": "Answer", "text": "Het is verwant maar apart. Autorisatie gaat over wie welke gegevens mag benaderen. Inputvalidatie gaat over of ingediende waarden worden geverifieerd voordat ze vertrouwd worden." } },
    { "@type": "Question", "name": "Kan dit soort fix worden toegepast zonder het ontwerp van mijn app te veranderen?", "acceptedAnswer": { "@type": "Answer", "text": "Ja. Server-side validatie gebeurt achter de schermen en vereist geen zichtbare wijziging aan de bestaande interface." } }
  ]
}
</script>
