---
Titel: "Lovable Supabase: Supabase Verlaten voor Gewone Postgres"
Trefwoorden: lovable supabase, migreren van Supabase, managed Postgres, auth-migratie, vendor lock-in, LaunchStudio, Manifera
Koperfase: Beslissing
Doelgroep: SaaS Scale-Up
---

# Lovable Supabase: Supabase Verlaten voor Gewone Postgres

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Lovable Supabase: Supabase Verlaten voor Gewone Postgres",
  "description": "Wanneer een product Supabase ontgroeit, wat er echt moet verhuizen: de database is makkelijk, auth en opslag niet. De eerlijke redenen om te vertrekken, de redenen die geen redenen zijn, en de volgorde die werkt.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-10-19",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/lovable-supabase-leaving-supabase-for-plain-postgres" }
}
</script>

Laten we beginnen met het advies, omdat de meeste artikelen over dit onderwerp het wegstoppen: voor het overgrote deel van de producten die met Lovable zijn gebouwd, is op Supabase blijven de juiste beslissing, en de migratie die wordt overwogen is een oplossing voor een probleem dat een goedkopere oplossing heeft.

Dat gezegd hebbende: sommige producten ontgroeien het wel, en die zijn beter geholpen met begrijpen wat de verhuizing echt inhoudt dan met het halverwege ontdekken. De database is het makkelijke deel. Alles wat rond de database is gebouwd, is het werk.

## De Redenen Die Geen Redenen Zijn

Vier motieven komen steeds terug en geen ervan houdt stand bij nadere beschouwing.

**"Het wordt duur."** Vergelijk eerlijk. De rekening van Supabase dekt een beheerde database, authenticatie, opslag, een API-laag en back-ups. Dat vervangen door een beheerde Postgres-instantie plus een authdienst plus objectopslag plus de engineeringtijd om ze aan elkaar te koppelen, is vaak duurder, en altijd duurder als u het onderhoud meetelt.

**"De prestaties zijn slecht."** Bijna altijd ontbrekende indexen, N+1-queries of slecht beheerde verbindingen. Die problemen verhuizen met u mee. Een product dat op Supabase traag is, is overal traag, tegen hogere kosten.

**"We raken misschien vast."** Supabase is Postgres. Uw data, schema, functies en triggers zijn standaard en overdraagbaar. De lock-in is alleen echt bij auth, opslag en realtime - en zelfs daar is hij bescheiden.

**"Investeerders vroegen naar schaal."** Supabase draait producten die aanzienlijk groter zijn dan het uwe. Moet de vraag worden beantwoord, dan is het antwoord een capaciteitsplan, geen migratie.

## De Redenen Die Echt Zijn

Drie, en ze zijn allemaal structureel in plaats van technische ergernissen.

**Een wettelijke of contractuele eis over waar data staat of wie het beheert.** Een klant uit de publieke sector, een zorgcontract, of een inkoopproces bij een groot bedrijf dat een specifieke regio, provider of certificering eist waaraan u op uw huidige plan niet kunt voldoen. Dit is de meest voorkomende echte reden, en ze komt meestal binnen met een groot contract eraan vast.

**Een schaal of werklast waarvoor het platform niet is ingericht.** Heel veel schrijfacties, grote analytische werklasten naast transactionele, of behoefte aan Postgres-extensies en configuratie die de beheerde omgeving niet biedt.

**Een bewuste architecturale consolidatie.** U draait elders al substantiële infrastructuur, en de database ernaast hebben - hetzelfde netwerk, dezelfde monitoring, hetzelfde team - is in totaal eenvoudiger. Dit is een echte reden, en ze geldt voor minder kleine producten dan er denken dat ze geldt.

## Wat Makkelijk Verhuist

De database zelf is echt eenvoudig. Het is Postgres: exporteer, herstel, controleer de aantallen rijen. Uw schema, indexen, constraints, functies en triggers komen allemaal mee.

Twee kanttekeningen. Supabase installeert een handvol extensies, waarvan u er misschien enkele gebruikt zonder het te weten - controleer dat voordat u aanneemt dat het doel ze ondersteunt. En row-level security-policies komen mee, maar ze verwijzen naar de identiteit van de aanroepende gebruiker, die na de verhuizing niet meer door de auth van Supabase wordt geleverd. Die policies moeten worden herschreven tegen het mechanisme dat ervoor in de plaats komt.

Reken voor dit deel een dag, waarvan het meeste controle is in plaats van overzetten.

## Wat Niet Makkelijk Verhuist

**Authenticatie is het moeilijke deel.** Wachtwoordhashes kunnen meestal worden geëxporteerd en geïmporteerd, zodat gebruikers hun wachtwoord niet hoeven te resetten - maar de tokens die uw applicatie uitgeeft veranderen van formaat, elke sessie wordt bij de overstap ongeldig, en alles wat afhangt van de identiteitsclaim in die tokens moet worden herschreven. Dat omvat elke row-level security-policy, en daarom zijn de twee stukken werk eigenlijk één.

Sociale logins moeten bij elke provider opnieuw worden ingericht, en de redirect-URL's bijgewerkt. Gebruikers die zich met Google aanmeldden, behouden hun account alleen als u ze op e-mailadres koppelt, wat zorg vereist om te voorkomen dat u twee mensen samenvoegt die één adres delen.

**Opslag is kopiëren plus herschrijven.** De objecten verplaatsen is een script. Het werk zit in elke plek waar uw applicatie een Supabase-URL genereerde, elk mechanisme voor ondertekende URL's, elk uploadpad, en elke permanente link die al naar een klant is verstuurd.

**Realtime heeft geen directe vervanger.** Hangt uw product af van live updates, dan is dat een component dat u nu bouwt of koopt.

**Edge functions zijn gewone code** en zijn makkelijk over te zetten, maar hun deployment, geheimen en aanroep veranderen allemaal.

## De Volgorde Die Werkt

Doe het in fasen terwijl het product de hele tijd blijft draaien. Alles tegelijk is hoe een weekend een week wordt.

Verplaats eerst de database en laat de applicatie tijdens een kort onderhoudsvenster naar de nieuwe wijzen. Laat auth en opslag waar ze zijn - Supabase-auth kan blijven werken tegen een database die u niet meer bij hen host, en die eigenschap maakt een gefaseerde migratie überhaupt mogelijk.

Migreer daarna de authenticatie. Dit is de overstap met zichtbaar effect voor gebruikers: sessies eindigen, iedereen logt opnieuw in. Doe het op een rustig uur, communiceer vooraf, en heb een geteste route terug.

Migreer vervolgens de opslag, met een periode waarin uw applicatie van beide locaties leest, zodat niets breekt terwijl objecten worden gekopieerd.

Verwijder ten slotte de resterende afhankelijkheden en sluit het account - na een behoorlijke tussenperiode, met eerst een gecontroleerde back-up.

## Voordat U zich Vastlegt

Twee stukken werk zijn het doen waard voordat u beslist, en beide hebben waarde, ook als u blijft.

Voer een volledige hersteltest uit op uw huidige opzet. Een product waarvan het team nooit een back-up heeft teruggezet, is niet klaar om iets te migreren, en de oefening laat vaak zien dat herstel niet werkt zoals werd aangenomen.

En oefen de migratie op een kopie. Zet de database ergens anders terug, laat een stagingapplicatie ernaar wijzen, migreer een deel van de gebruikers en objecten, en meet de tijd van elke stap. De generale repetitie vertelt u de werkelijke duur, vindt de extensie waarvan u niet wist dat u die gebruikte, en verandert de overstap van een evenement in een herhaling.

## De Middenweg Die Oprichters Missen

Tussen blijven en vertrekken is er een derde opzet die de meeste echte redenen oplost: houd Supabase en verander de vorm.

Eisen rond datalocatie worden vaak vervuld met een andere regio of een plan met andere voorwaarden. Vragen uit inkoopprocessen gaan vaak over certificeringen en contractuele toezeggingen die op hogere niveaus bestaan. Behoeften aan extensies en configuratie worden soms opgelost met een eigen instantie.

Vraag het vóór u migreert. Een gesprek met een leverancier is goedkoper dan een engineeringproject, en het antwoord is verrassend vaak dat datgene waar u drie weken aan wilt bouwen al bestaat als instelling.

## Verklein de Lock-In Zonder te Verhuizen

Er is een reeks wijzigingen die een toekomstige migratie goedkoop maakt, weinig kost, en uw product verbetert, of u nu ooit vertrekt of niet. Speelt de vraag bij u, dan is dit het werk om in plaats daarvan te doen.

**Zet het platform achter uw eigen grens.** Applicatiecode die overal de Supabase-client aanroept, is code waarin elk bestand weet welke leverancier u gebruikt. Dezelfde code die uw eigen datafuncties aanroept - die van binnen toevallig Supabase gebruiken - verandert op één plek als dat ooit verandert. Dit is gewoon goede structuur, en het is de grootste bepalende factor voor de kosten van een migratie.

**Bezit uw eigen identiteitsmodel.** Houd een eigen gebruikerstabel bij met eigen identificaties, gekoppeld aan de identiteit bij de authprovider in plaats van erop gesleuteld. Dan verandert het wisselen van provider één kolom, niet elke foreign key in het schema.

**Sla bestandsverwijzingen op, geen URL's.** Een databasekolom met een volledige Supabase-URL is een kolom die bij migratie moet worden herschreven en die breekt in elke al verstuurde e-mail. Een kolom met een pad, waarbij URL's bij het lezen worden gegenereerd, is per definitie overdraagbaar.

**Houd migraties in uw repository.** Een schema dat alleen in een dashboard bestaat, kan nergens opnieuw worden aangemaakt, wat zelfs een generale repetitie onmogelijk maakt.

Doe deze vier en de migratie waar u zich zorgen over maakt, wordt twee weken in plaats van een kwartaal - en in het veel waarschijnlijkere geval dat u nooit migreert, hebt u een schonere codebase en een product dat makkelijker aan iemand anders over te dragen is.

## Dit Inrichten

Een gefaseerde migratie voor een klein product kost doorgaans twee tot drie weken: een generale repetitie op een kopie met de tijd van elke stap gemeten, databasemigratie met controle van extensies en policies, een authenticatie-overstap inclusief import van wachtwoordhashes, opnieuw inrichten van sociale logins en herschrijven van policies tegen de nieuwe identiteitsbron, opslag gekopieerd met een periode van lezen uit beide en bestaande links afgehandeld, realtime vervangen indien gebruikt, edge functions opnieuw uitgerold met hun geheimen, monitoring en back-ups ingericht op het nieuwe platform met een daadwerkelijk geteste herstelactie, en de oude omgeving na een gecontroleerde tussenperiode buiten gebruik gesteld.

LaunchStudio doet beide helften van dit gesprek - inclusief oprichters vertellen dat ze niet moeten migreren, wat de vaker voorkomende uitkomst is. De engineers zijn van Manifera: elf jaar, 160+ projecten, infrastructuurwerk voor klanten als Vodafone, TNO en CFLW, vanuit Amsterdam en Ho Chi Minh-stad.

[Vertel ons waarom u overweegt te verhuizen](https://launchstudio.eu/nl/#contact). De helft van de tijd is het antwoord een index.

## Echt voorbeeld

### Een Contract Dat een Ander Antwoord Vereiste

Gerlof Tichelaar bouwde Zorgdossier in Lovable: administratie van zorgplannen voor kleinschalige woonzorgaanbieders, 26 organisaties, zo'n 1.400 bewoners.

De migratie was niet zijn idee. Een regionale zorggroep bood een contract aan voor negen locaties, en hun inkoop eiste dat persoonsgegevens werden verwerkt op infrastructuur onder een specifieke overeenkomst met een genoemde certificering, in een specifieke regio, met contractuele voorwaarden die zijn plan niet bood. Het contract was meer waard dan zijn bestaande omzet.

Hij vroeg het eerst aan Supabase, de stap die de meeste oprichters overslaan, en een deel van de eis was op andere voorwaarden te vervullen. De regio en certificering niet, gezien zijn tijdlijn.

Zestien werkdagen verspreid over drie weken: een volledige generale repetitie op een kopie, die twee gebruikte extensies vond die het doel standaard niet inschakelde en de werkelijke overstap op 40 minuten mat in plaats van de aangenomen twee uur; de database gemigreerd naar beheerde Postgres in de vereiste regio, met aantallen rijen en constraintcontroles gecontroleerd tegen de bron; authenticatie verplaatst met wachtwoordhashes geïmporteerd, zodat geen enkele zorgverlener iets hoefde te resetten, 31 row-level security-policies herschreven tegen de nieuwe identiteitsclaim, en sociale login opnieuw ingericht voor de twee organisaties die het gebruikten; een periode van twee weken lezen uit beide opslaglocaties terwijl 94.000 documenten werden gekopieerd, met eerder uitgegeven links omgeleid in plaats van gebroken; realtime vervangen door polling op de twee schermen die het gebruikten, nadat was vastgesteld dat live updates klinisch niet nodig waren; back-ups ingericht met een uitgevoerde en getimede herstelactie; en het oude project na een maand buiten gebruik gesteld met een gecontroleerd archief.

**Resultaat:** het contract werd getekend. Gerlofs maandelijkse infrastructuurkosten stegen van €85 naar €310, wat hij het minst interessante getal van het project noemt. De generale repetitie is het deel dat hij andere oprichters aanraadt: de overstap van 40 minuten vond plaats om zes uur op een zondagochtend en niemand merkte het.

> *"Ik migreerde niet omdat Supabase niet goed genoeg was. Ik migreerde omdat een inkoopafdeling een specifiek antwoord nodig had, en dat is de enige reden waarom ik het opnieuw zou doen."*
> - **Gerlof Tichelaar, Oprichter, Zorgdossier (Leeuwarden)**

**Kosten & Doorlooptijd:** €11.800 (generale repetitie, databasemigratie met controle van extensies en constraints, auth-overstap met import van hashes en herschrijven van 31 policies, opslagkopie met lezen uit beide en omleiden van links, vervanging van realtime, controle van back-up en herstel, buiten gebruik stellen) - afgerond in 16 werkdagen.

## Veelgestelde vragen

### Is Supabase moeilijk te verlaten?

De database niet - dat is standaard Postgres. Authenticatie, opslag en realtime zijn het werk, en authenticatie is degene met zichtbaar effect voor gebruikers, omdat elke sessie bij de overstap eindigt.

### Moeten mijn gebruikers hun wachtwoord resetten?

Niet als wachtwoordhashes worden geëxporteerd en geïmporteerd, wat normaal gesproken mogelijk is. Ze worden bij de overstap uitgelogd en moeten opnieuw inloggen.

### Is migreren goedkoper dan blijven?

Meestal niet. De prijs van Supabase dekt een database, auth, opslag, een API en back-ups; die afzonderlijk vervangen plus de engineeringtijd is vaak duurder om te draaien en altijd duurder om te onderhouden.

### Mijn app is traag - lost verhuizen dat op?

Bijna nooit. Traagheid zijn meestal ontbrekende indexen, N+1-queries of slecht beheerde verbindingen, en die reizen tegen hogere kosten met u mee.

### Wat moet ik doen voordat ik beslis?

Vraag de leverancier of uw eis op andere voorwaarden te vervullen is, voer een hersteltest uit op wat u hebt, en oefen de migratie op een kopie. Alle drie zijn nuttig, ook als u blijft.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Is het moeilijk om van Supabase weg te migreren?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "De database is standaard Postgres en verhuist makkelijk. Authenticatie, opslag en realtime zijn het echte werk, waarbij auth de enige overstap met zichtbaar effect voor gebruikers veroorzaakt."
      }
    },
    {
      "@type": "Question",
      "name": "Moeten gebruikers na een migratie hun wachtwoord resetten?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Normaal niet - wachtwoordhashes kunnen worden geëxporteerd en geïmporteerd. Iedereen wordt bij de overstap uitgelogd en moet opnieuw inloggen."
      }
    },
    {
      "@type": "Question",
      "name": "Is Supabase verlaten goedkoper?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Meestal niet. De rekening dekt database, auth, opslag, API en back-ups; gelijkwaardige onderdelen apart samenstellen kost meer om te draaien en te onderhouden."
      }
    },
    {
      "@type": "Question",
      "name": "Lost migreren van Supabase prestatieproblemen op?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Bijna nooit. Ontbrekende indexen, N+1-queries en slecht beheerde verbindingen reizen met u mee en kosten elders meer."
      }
    },
    {
      "@type": "Question",
      "name": "Wat moet ik doen voordat ik besluit te migreren?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Vraag de leverancier of de eis op andere voorwaarden te vervullen is, test het herstel van uw huidige back-ups, en oefen de migratie op een kopie."
      }
    }
  ]
}
</script>
