---
Titel: "AI-Appbeveiliging: IDOR, de Fout Die AI-Code het Vaakst Schrijft"
Trefwoorden: ai-appbeveiliging, IDOR, gebrekkige toegangscontrole, autorisatiecontroles, eigenaarschap van objecten, LaunchStudio, Manifera
Koperfase: Overweging
Doelgroep: Technische solo-oprichter / Indie hacker
---

# AI-Appbeveiliging: IDOR, de Fout Die AI-Code het Vaakst Schrijft

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "AI-Appbeveiliging: IDOR, de Fout Die AI-Code het Vaakst Schrijft",
  "description": "Verander het nummer in de URL en u ziet het record van een ander. Waarom door AI gegenereerde endpoints eigenaarschapscontroles weglaten, hoe u ze in een middag allemaal vindt, en het patroon dat voorkomt dat het terugkomt.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-11-14",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/ai-app-security-idor-the-bug-ai-code-writes-most-often" }
}
</script>

Open een record in uw eigen product en kijk naar de adresbalk. Er staat een identificatie in. Verander die in een andere en laad opnieuw.

Ziet u de data van iemand anders, dan hebt u een insecure direct object reference - en draait u een applicatie die grotendeels met AI-tools is gebouwd, dan is de kans daarop merkbaar groter dan de helft. Bij beveiligingsreviews van met Lovable, Bolt en Cursor gebouwde producten is dit de vaakst gevonden ernstige fout, nog vóór blootgestelde sleutels en publieke opslagbuckets.

Het is ook de makkelijkst te misbruiken fout. Geen tools, geen vaardigheid, geen kennis van beveiliging. Een nieuwsgierige klant met een browser vindt het per ongeluk, en sommigen kijken verder voordat ze het u vertellen.

## Waarom Gegenereerde Code Dit Doet

Vraag een tool een pagina te bouwen die een factuur toont, en ze schrijft precies dat: neem de identificatie, haal de factuur op, toon haar. Het verzoek is vervuld. De code is correct in de zin dat ze doet wat haar werd gevraagd.

Niemand vroeg "en controleer of de persoon die erom vraagt die mag zien", dus niemand schreef het. Autorisatie is geen functie; het is een afwezigheid, en afwezigheden zijn precies wat een tool die op verzoeken werkt niet oplevert.

Het stapelt zich op. Zodra één endpoint het patroon volgt, imiteren latere sessies het, en het twintigste endpoint heeft dezelfde vorm als het eerste, omdat consistentie is waar het model goed in is. De fout zit dus zelden op één plek - het is een eigenschap van de hele applicatie.

## Authenticatie Is Geen Autorisatie

Het gangbare misverstand: "mijn endpoints vereisen een login, dus ze zijn beschermd".

Authenticatie beantwoordt wie u bent. Autorisatie beantwoordt of u dit met dit ding mag doen. Een ingelogde gebruiker is nog steeds een vreemde voor elk record dat niet van hem is, en een applicatie die alleen het eerste controleert, heeft van elke klant een beheerder gemaakt van de data van alle anderen.

De controle die ontbreekt, heeft altijd dezelfde vorm: hoort het object dat in dit verzoek wordt genoemd bij het account dat het verzoek doet?

## Ze Allemaal Vinden in Eén Middag

Dit is mechanisch in plaats van slim.

Maak een lijst van elk endpoint en elke pagina die een identificatie aanneemt - een record-ID, een documentreferentie, een bestandspad, een slug, alles wat een specifiek ding benoemt. In een typisch door AI gebouwd product zijn dat dertig tot zestig plekken.

Maak twee accounts aan in twee verschillende organisaties. Noteer in de eerste de identificaties van een handvol records. Vraag ze daarna, ingelogd als de tweede, een voor een op.

Elk geval dat data teruggeeft in plaats van een weigering, is een bevinding. Doe het voor lezen, en herhaal het dan voor bijwerken en verwijderen, die meestal erger zijn en vaak over het hoofd worden gezien omdat de interface er geen duidelijke route naartoe biedt.

Neem de endpoints mee die uw interface niet direct aanroept: exports, pdf-generatie, downloads van bestanden, de API die uw mobiele app gebruikt, webhookhandlers, alles wat een eerdere versie heeft achtergelaten.

## Maak Eigenaarschap Deel van de Query

Er zijn twee manieren om elk geval op te lossen, en een ervan is beter.

De kwetsbare oplossing: haal het record op, vergelijk dan de eigenaar met de huidige gebruiker, en beslis dan. Het werkt, en het moet in elke handler correct worden herhaald, voor altijd, door iedereen, inclusief de volgende AI-sessie.

De duurzame oplossing: zorg dat de query zelf geen rijen van een ander account kan teruggeven. Haal de factuur op *waar de ID deze is en de organisatie die van de sessie is*. Er is geen vergelijking om te vergeten, omdat een record dat niet bij de aanroeper hoort gewoon niet wordt gevonden.

In Supabase is row-level security dit idee, afgedwongen door de database, en daarom is het de moeite waard het goed te doen: een policy geldt voor elke query vanuit elk codepad, inclusief paden die later worden geschreven door iemand die uw afspraken nooit heeft gelezen. Controles op applicatieniveau en databasepolicies samen zijn broek en bretels, en voor een product met data van anderen zijn beide gerechtvaardigd.

## Niet te Raden Identificaties Zijn Geen Oplossing

Een veelvoorkomende reactie is overstappen van oplopende getallen naar willekeurige identificaties, zodat niemand de ID van een ander record kan raden.

Doe het - oplopende identificaties lekken uw volume en nodigen uit tot enumeration - maar verwar het niet met een oplossing. Identificaties verschijnen in URL's die worden gedeeld, in exports, in supporttickets, in referrer-headers, in de browsergeschiedenis van een klant op een gedeelde computer. Een niet te raden identificatie die toegang geeft aan wie haar heeft, is een capability, en capabilities lekken.

De autorisatiecontrole moet er hoe dan ook zijn. Willekeurige identificaties maken toevallige ontdekking moeilijker; ze maken toegang niet gecontroleerd.

## Het Geneste Geval Dat Iedereen Mist

Zelfs producten met eigenaarschapscontroles missen routinematig één patroon: een object dat via een ouder wordt bereikt.

Het endpoint controleert dat het project bij uw organisatie hoort, en haalt daarna een taak op met de opgegeven identificatie - zonder te bevestigen dat de taak bij dat project hoort. Vul de taakidentificatie van een andere organisatie in en de controle slaagt terwijl het verkeerde record wordt teruggegeven.

De regel: elke identificatie in het verzoek wordt gecontroleerd tegen het pad dat ernaartoe leidde, niet alleen de eerste. In de praktijk betekent dat dat de query het kind beperkt tot zijn ouder, en de ouder tot het account.

## Voorkom Dat Het Terugkomt

De bevindingen van vandaag oplossen is de helft van het werk. De andere helft is zorgen dat het endpoint dat volgende maand wordt geschreven de controle heeft.

Drie dingen bereiken dat op de schaal van een klein product. Een gedeelde hulpfunctie die records ophaalt binnen het huidige account, zodat de natuurlijke manier om een query te schrijven de veilige is - en de onveilige bewuste moeite vereist. Row-level security in de database als de laag die er niet van afhangt dat iemand eraan denkt. En een test die elk endpoint doorloopt als gebruiker van een tweede organisatie en de build laat falen als er iets data teruggeeft.

Die laatste kost een middag om te schrijven en is de waardevolste test die een door AI gebouwd product kan hebben, omdat ze blijft werken terwijl de code eromheen wordt herschreven door tools die uw beveiligingsnotities nooit hebben gelezen.

## Velden Hebben Ook Rechten

Zodra de toegang op recordniveau klopt, blijft er één laag over die makkelijk over het hoofd wordt gezien: welke velden binnen een record een bepaalde gebruiker mag lezen of schrijven.

De leeskant verschijnt wanneer een endpoint een hele rij teruggeeft. Een teamlid met beperkte rechten opent het profiel van een collega en het antwoord bevat een salarisveld, een interne notitie of een risicoscore - verborgen door de interface, duidelijk zichtbaar in het netwerktabblad. De oplossing is de velden terug te geven die bij de aanvrager passen in plaats van het hele record, wat nog een reden is om gevormde views bloot te stellen in plaats van tabellen.

De schrijfkant is gevaarlijker en heet mass assignment. Een endpoint dat een inhoud accepteert en elke sleutel daarin op het record toepast, laat een gebruiker velden meesturen die niemand bedoelde dat hij zou instellen - een rol, een accountidentificatie, een abonnementsniveau, een geverifieerd-vlag. Gegenereerde code doet dit voortdurend, omdat de hele inhoud aan een update doorgeven het kortste is om te schrijven.

De oplossing is een lijst in plaats van een filter: zeg expliciet welke velden dit endpoint accepteert en negeer al het andere. Nooit een lijst van velden om uit te sluiten, want dat is een lijst van wat iemand zich die dag herinnerde.

Test het direct. Neem een legitiem updateverzoek, voeg een veld toe dat de gebruiker niet zou mogen beheren - `role: "admin"` is het klassieke voorbeeld - en verstuur het. Wordt de waarde toegepast, dan hebt u een privilege-escalatie gevonden, en die is meestal met één regel te dichten.

Doe hetzelfde voor de velden die uw interface alleen verbergt. Een uitgeschakeld invoerveld, een kolom die uit een tabel is gehaald, een sectie die alleen aan managers wordt getoond - elk is een presentatiekeuze, en de server moet dezelfde beslissing zelfstandig nemen, anders is de keuze alleen adviserend.

## Dit Inrichten

Voor een bestaand product kost dit doorgaans één tot twee dagen: een inventarisatie van elk endpoint dat een identificatie aanneemt, systematisch testen tussen accounts voor lezen, bijwerken en verwijderen, inclusief exports, downloads en verouderde endpoints, elke bevinding opgelost door de query te beperken in plaats van na het ophalen te vergelijken, geneste identificaties gecontroleerd tegen hun ouders, row-level security-policies op elke tabel met controle tussen tenants, oplopende identificaties vervangen waar ze in URL's staan, een beperkte hulpfunctie voor datatoegang ingevoerd als standaardpatroon, en een geautomatiseerde test tussen accounts gekoppeld aan uw controles.

LaunchStudio doet dit bij elke beveiligingsreview, en het is de bevinding die we verwachten in plaats van hopen te vinden. De engineers zijn van Manifera - elf jaar, 120+ engineers, klanten als Vodafone, TNO en CFLW.

[Vraag ons een van uw records te openen vanuit een ander account](https://launchstudio.eu/nl/#contact). Het kost tien minuten en het is de test die er het meest toe doet.

## Echt voorbeeld

### Het Factuurnummer in de URL

Coen Bleeker bouwde Factuurstroom in Lovable: facturatie en betalingsopvolging voor freelancers en kleine bureaus, 380 gebruikers in heel Nederland.

Facturen waren bereikbaar via een URL die eindigde op een oplopend nummer. Elk endpoint vereiste een geldige sessie en geen enkel endpoint controleerde eigenaarschap. Een gebruiker die in zijn eigen account was ingelogd, kon elk nummer invoeren en de bijbehorende factuur zien - naam en adres van de klant, de factuurregels, de bedragen, en de bankgegevens van de freelancer zelf.

Een gebruiker vond het door zijn eigen factuurnummer verkeerd in te typen en op die van iemand anders uit te komen. Hij probeerde er nog drie, en schreef toen Coen. Hij had daarbij vier facturen gezien van drie verschillende bedrijven.

Twee werkdagen: een inventarisatie van 47 endpoints met identificaties, waarvan er 31 geen eigenaarschapscontrole hadden; die allemaal opgelost door queries te beperken tot het account van de sessie in plaats van na het ophalen te vergelijken, met een gedeelde hulpfunctie voor datatoegang zodat de standaardmanier om een record op te halen de beperkte is; geneste gevallen gecorrigeerd, inclusief factuurregels en betaalrecords die op identificatie werden opgehaald zonder de bovenliggende factuur te controleren; row-level security ingeschakeld en policies geschreven op alle 14 tabellen, terwijl het eerder op vier aanstond; oplopende factuuridentificaties in URL's vervangen door willekeurige, met het leesbare factuurnummer behouden als apart weergaveveld; een geautomatiseerde test toegevoegd die inlogt als gebruiker van een tweede organisatie en elke bekende identificatie opvraagt, en de build laat falen bij elk antwoord met data; en toegangslogs over de voorafgaande periode bekeken om de omvang van de blootstelling vast te stellen.

**Resultaat:** de logcontrole vond 61 verzoeken tussen accounts in veertien maanden, waarvan er 54 kwamen van de vier gebruikers die het door een tikfout vonden en stopten. De overige zeven kwamen van één account op één avond. Coen informeerde de betrokken bedrijven en de Autoriteit Persoonsgegevens. De geautomatiseerde test is sindsdien twee keer gefaald bij nieuwe endpoints, beide opgevangen vóór de deploy.

> *"Iedereen die kon inloggen, kon elke factuur in het systeem lezen door een ander nummer in te typen. Ik had een week aan tweestapsverificatie besteed en de voordeur van elk record open laten staan."*
> - **Coen Bleeker, Oprichter, Factuurstroom (Nijmegen)**

**Kosten & Doorlooptijd:** €3.800 (inventarisatie van endpoints en testen tussen accounts, 31 autorisatieherstellingen met beperkte datatoegang, controle van geneste identificaties, row-level security op alle tabellen, vervangen van identificaties, geautomatiseerde test tussen tenants, controle van toegangslogs en incidentdocumentatie) - afgerond in 2 werkdagen.

## Veelgestelde vragen

### Wat is een IDOR?

Een endpoint dat een object teruggeeft of wijzigt op basis van een identificatie in het verzoek, zonder te controleren of de aanvrager er recht op heeft. Het nummer in een URL veranderen en het record van een ander zien, is het klassieke symptoom.

### Beschermt een loginvereiste ertegen?

Nee. Authenticatie stelt vast wie u bent; autorisatie stelt vast wat u mag doen. Een ingelogde gebruiker is nog steeds een vreemde voor elk record dat niet van hem is.

### Lossen willekeurige identificaties het probleem op?

Nee. Ze voorkomen toevallig raden, maar identificaties lekken via gedeelde URL's, exports, supporttickets en browsergeschiedenis. De eigenaarschapscontrole moet er hoe dan ook zijn.

### Wat is de duurzaamste oplossing?

Beperk de query zodat rijen van een ander account niet kunnen worden teruggegeven, in plaats van op te halen en dan te vergelijken. Voeg row-level security in de database toe, zodat de regel ook geldt voor codepaden die later worden geschreven.

### Hoe voorkom ik dat het terugkomt?

Een gedeelde, beperkte hulpfunctie voor datatoegang, zodat de makkelijke manier de veilige is, databasepolicies die niet van geheugen afhangen, en een geautomatiseerde test die elk endpoint opvraagt als gebruiker van een tweede organisatie.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Wat is een insecure direct object reference?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Een endpoint dat handelt op een object dat in het verzoek wordt genoemd, zonder te controleren of de aanvrager er recht op heeft - een ID in de URL veranderen toont het record van een andere gebruiker."
      }
    },
    {
      "@type": "Question",
      "name": "Beschermt een loginvereiste tegen IDOR?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Nee. Authenticatie zegt wie u bent; autorisatie zegt waar u bij mag. Ingelogde gebruikers zijn nog steeds vreemden voor de records van andere accounts."
      }
    },
    {
      "@type": "Question",
      "name": "Lossen willekeurige identificaties IDOR op?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Nee. Ze stoppen toevallig raden, maar identificaties lekken via gedeelde links, exports en supporttickets. De eigenaarschapscontrole blijft nodig."
      }
    },
    {
      "@type": "Question",
      "name": "Wat is de duurzaamste manier om het op te lossen?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Beperk de query tot het account van de aanroeper zodat vreemde rijen niet kunnen worden teruggegeven, en dwing dezelfde regel af met row-level security in de database."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe voorkom ik dat IDOR terugkomt?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Een beperkte hulpfunctie voor datatoegang als standaardpatroon, databasepolicies die niet van geheugen afhangen, en een geautomatiseerde test tussen accounts in uw build."
      }
    }
  ]
}
</script>
