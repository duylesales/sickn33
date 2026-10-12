---
Titel: "Supabase Security: Row Level Security Policies Die Standhouden"
Trefwoorden: supabase security, row level security, rls policies, ai app security, Lovable, LaunchStudio, Manifera
Koperfase: Decision
Doelgroep: Technical Solo Founder / Indie Hacker
---

# Supabase Security: Row Level Security Policies Die Standhouden

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Supabase Security: Row Level Security Policies Die Standhouden",
  "description": "Row level security is het enige controlemechanisme tussen uw publieke API-sleutel en de klantdata. Hoe policies werkelijk evalueren, de fouten die ze louter decoratief maken, en hoe u ze test door zelf in te breken.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-08-12",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/supabase-security-row-level-security-policies-that-hold" }
}
</script>

Dit is de ongemakkelijke realiteit van een applicatie die op Supabase draait: uw publieke anon-sleutel staat open en bloot in de broncode van de browser, waar iedereen hem kan kopiëren. Die sleutel maakt rechtstreeks verbinding met de automatisch gegenereerde REST- en GraphQL-API. Die API heeft toegang tot elke tabel in uw database. En het enige wat een nieuwsgierige bezoeker scheidt van uw volledige klantendatabase, is een reeks regels geschreven in SQL die de meeste oprichters nog nooit met eigen ogen hebben gelezen.

Die regels heten Row Level Security (RLS) policies. Wanneer ze correct zijn ingericht, is de architectuur buitengewoon robuust: de beveiliging bevindt zich diep in de database-engine zelf, waar deze onverbiddelijk geldt, ongeacht welke query binnenkomt of wie deze heeft geschreven. Maar wanneer ze ontbreken, onvolledig zijn of puur zijn geschreven om een foutmelding snel weg te poetsen, is uw architectuur in feite een openbare database met niet meer dan een dun inlogschermpje ervoor.

Dit is het meest ingrijpende onderdeel van een met AI gebouwd softwareproduct. En het is precies het onderdeel dat AI-codegeneratoren het minst betrouwbaar aanmaken — want RLS-policies coderen uw specifieke bedrijfslogica, en de AI begrijpt uw bedrijfsregels niet uit zichzelf.

## Wat de Policy Werkelijk Evalueert

Een policy is een logische voorwaarde die wordt geëvalueerd voor elke rij, bij elke database-operatie, voor elk inkomend verzoek. Als de voorwaarde waar (`true`) is, is de rij zichtbaar of wordt de mutatie toegestaan. Als de voorwaarde onwaar (`false`) is, bestaat de rij simpelweg niet voor dat verzoek — geen foutmelding, geen permissie-weigering, puur stilzwijgende afwezigheid.

Die stilte is aan twee kanten gevaarlijk. Een policy die te permissief is, geeft geen enkel signaal; alles werkt feilloos in de UI, maar er is veel te veel data openbaar inzichtelijk. Een policy die te restrictief is, zorgt ervoor dat data plotseling mysterieus verdwijnt uit schermen — wat oprichters meestal als eerste opmerken en vervolgens op de slechtst mogelijke manier "oplossen".

Elk verzoek draagt een identiteit mee. Voor een ingelogde gebruiker is dat diens account-ID en de claims in het JSON Web Token (JWT). Voor een anonieme bezoeker is het een beperkte anon-rol. Voor servercode die gebruikmaakt van de bevoorrechte `service_role`-sleutel worden RLS-policies volledig omzeild — en dat is precies de reden waarom die sleutel nooit ofte nimmer in de browser mag belanden.

## Inschakelen Is Niet Hetzelfde Als Beveiligen

Dit zijn twee volstrekt gescheiden stappen, en het misverstand ertussen is waar datalekken ontstaan.

Het inschakelen van Row Level Security op een tabel (`ALTER TABLE ... ENABLE ROW LEVEL SECURITY;`) betekent dat de tabel vanaf dat moment standaard alles weigert (default-deny). Het schrijven van policies betekent dat u expliciet specificeert wat wel is toegestaan. Een tabel met RLS ingeschakeld maar zonder policies is onzichtbaar voor de frontend, waardoor de applicatie kapot lijkt. Maar een tabel met geschreven policies waarbij RLS **niet** expliciet is ingeschakeld, staat wijd open voor de hele wereld — terwijl de UI perfect functioneert.

Dat tweede geval is het meest risicovolle scenario: niets in de draaiende applicatie wijst op een probleem. De policies staan netjes in het dashboard, u herinnert zich dat u ze heeft geconfigureerd, maar PostgreSQL raadpleegt ze in werkelijkheid nooit.

Controleer elke tabel afzonderlijk. Niet alleen de tabellen die u belangrijk vindt, maar letterlijk elke tabel — inclusief hulptabellen die een AI-tool automatisch heeft aangemaakt en die u zelf nog nooit heeft geopend.

## Vier Manieren Waarop Policies in de Praktijk Falen

**Geschreven om een foutmelding te muilkorven.** Een feature toont geen data in de frontend, de snelste fix van de AI-agent is een policy die alles toestaat (`USING (true)`), en dat is precies wat er gegenereerd wordt wanneer de prompt luidt: *"deze query geeft geen rijen terug, los dit op"*. De functionaliteit werkt weer en de tabel is op slag openbaar.

**Alleen `SELECT` afdekken.** Leestoegang is de bewerking waar de meeste mensen aan denken. `INSERT`, `UPDATE` en `DELETE` vereisen elk hun eigen specifieke policy. Een applicatie waarin gebruikers uitsluitend hun eigen records kunnen inzien, maar willekeurige records van concurrenten kunnen overschrijven of verwijderen, is een veelvoorkomend en ernstig resultaat van halve beveiliging.

**Blind vertrouwen op een waarde die de client meestuurt.** Een policy die de eigenaar van een rij vergelijkt met een `user_id` die als parameter vanuit de frontend wordt meegestuurd in plaats van afgeleid uit `auth.uid()`, is louter decoratief. De browserclient kan elke willekeurige identifier meesturen. Eigenaarschap moet altijd afkomstig zijn uit de cryptografisch geverifieerde sessie, nooit uit een meegestuurde payload.

**Vertrouwen op een claim die de gebruiker zelf kan wijzigen.** Een policy die controleert of een token beheerdersrechten claimt, is slechts zo veilig als het proces dat die rol toekent. Als de rolkolom (`is_admin` of `role`) zich in een profieltabel bevindt die gebruikers zelf via een profielscherm kunnen updaten, kunnen ze zichzelf promoveren tot beheerder. Deze specifieke kwetsbaarheid komt voortdurend voor in met AI gegenereerde apps, omdat een rol opslaan naast de gebruikersnaam de meest voor de hand liggende opzet lijkt.

## Eigenaarschap, Lidmaatschap en de Structuur van Uw Regels

Vrijwel elk SaaS-product vereist een van twee modellen:

**Eigenaarschap (Ownership):** elke rij behoort toe aan exact één gebruikersaccount, en alleen dat account mag de rij zien of muteren. Eenvoudig, en prima geschikt voor strikt persoonlijke B2C-tools.

**Lidmaatschap (Membership / Multi-tenancy):** rijen behoren toe aan een organisatie of bedrijf, en individuele gebruikers zijn lid van organisaties, eventueel met verschillende rollen (zoals beheerder, medewerker of alleen-lezen). Dit dekt vrijwel elk B2B-product af, en het vereist een doordachte databasestructuur: een tabel voor organisaties, een koppeltabel die gebruikers koppelt aan organisaties met een rol, en RLS-policies die lidmaatschap valideren in plaats van individueel eigenaarschap.

De fout die u koste wat het kost moet vermijden, is beginnen met een simpel eigenaarschap-model omdat dat sneller bouwt, om er zes maanden later achter te komen dat zakelijke klanten willen dat collega's elkaars gegevens kunnen inzien. Het achteraf ombouwen van een database naar een lidmaatschapsmodel raakt elke afzonderlijke tabel en elke policy. Als de kans bestaat dat uw klanten bedrijven zijn, richt lidmaatschap dan direct vanaf dag één in; het kost nu een middag extra en scheelt u later twee weken crisiswerk.

## De Prestatiekant Waar Niemand Over Spreekt

RLS-policies worden uitgevoerd op elke individuele rij van elke databasequery. Wat er in die policy staat, heeft directe gevolgen voor de responstijd van uw applicatie.

Een policy die voor elke geëvalueerde rij een subquery of join uitvoert op een andere tabel, kan een snelle zoekopdracht dramatisch vertragen naarmate de database groeit. Twee maatregelen zijn standaard vereist: indexeer altijd de kolommen waarop uw policies filteren (zoals `tenant_id` of `user_id`), en structureer policies zo dat zware checks slechts eenmaal per query worden geëvalueerd in plaats van per individuele rij. Als uw applicatie merkbaar trager werd nadat RLS werd toegevoegd, is dit vrijwel altijd de oorzaak — en de verkeerde reflex is om de policies weer uit te zetten.

## Policies Testen Door Erop Aan te Vallen

Het lezen van SQL-code vertelt u wat u *bedoelde*. Alleen een penetratietest vertelt u wat de database *daadwerkelijk doet*.

Maak twee testaccounts aan in twee verschillende browsers, bij voorkeur gekoppeld aan twee verschillende organisaties. Voer vervolgens systematisch de volgende stappen uit: probeer een record van het andere account te openen door de ID in de URL aan te passen. Probeer het record van de ander via de console te bewerken (`UPDATE`). Probeer het te verwijderen (`DELETE`). Probeer een nieuw record aan te maken dat gekoppeld is aan het ID van de ander (`INSERT`). Log uit en herhaal exact dezelfde pogingen als anonieme bezoeker. Probeer ten slotte met uitsluitend uw publieke anon-key via een HTTP-client (zoals Postman of cURL) alle tabellen in de database op te vragen — inclusief tabellen die uw frontend nergens aanroept.

Die laatste stap brengt steevast de vergeten hulptabellen aan het licht, en het kost niet meer dan vijf minuten. Elke query die data retourneert die niet zichtbaar had mogen zijn, is een beveiligingslek — en elk lek dat u nu vindt, had anders door een buitenstaander ontdekt kunnen worden.

## Schrijf de Toegangsregels Eerst in Gewone Mensentaal

Voordat u ook maar één regel SQL tikt, stelt u een document van één pagina op: per tabel wie mag lezen, wie mag aanmaken, wie mag wijzigen en wie mag verwijderen, en op basis van welke voorwaarde. Voor de meeste softwareproducten volstaan twintig regels tekst.

Dit document vervult drie cruciale functies. Het maakt het schrijven van policies een kwestie van vertalen in plaats van improviseren. Het geeft u een waterdichte checklist om tests tegenaan te houden. En het is het tastbare artefact dat u kunt overhandigen aan een security auditor of een zakelijke klant die vraagt hoe autorisatie is geregeld — een vraag die anders tot een pijnlijke stilte leidt.

## Hoe Een Gezonde Beveiligingslaag Eruitziet

Elke tabel heeft RLS expliciet ingeschakeld, individueel gecontroleerd. Elke tabel heeft afzonderlijke policies voor `SELECT`, `INSERT`, `UPDATE` en `DELETE`. Gebruikersidentiteit wordt ontleend aan de cryptografische sessie, nooit aan clientparameters. Gebruikersrollen staan in een tabel die gebruikers zelf niet kunnen bewerken. Het autorisatiemodel ligt schriftelijk vast. Het geheel is geverifieerd via vijandige tests vanaf een tweede account en zonder login. En de `service_role`-sleutel bestaat uitsluitend in beveiligde backend-omgevingen.

Voor een gemiddelde applicatie is dit ongeveer één werkdag werk. Het is het verschil tussen een softwareproduct dat een Nederlandse mkb-ondernemer of enterprise veilig kan afnemen, en een product dat bij de eerste serieuze security-audit door het ijs zakt.

## Policies Correct Houden Terwijl Het Product Groeit

De regels één keer goed krijgen is het eenvoudigste deel. Ze correct houden gedurende een jaar vol continue feature-ontwikkeling is waar de meeste applicaties geruisloos degraderen.

**Elke nieuwe tabel vereist een bewuste beslissing, geen aanname.** Op het moment dat een tabel wordt aangemaakt — door uzelf, een collega of een AI-agent — moet iemand vastleggen wie rijen mag lezen, toevoegen, wijzigen en wissen. Een tabel die tijdens een drukke sprint wordt aangemaakt onder het mom van "dat beveiligen we later wel", wordt in de praktijk nooit beveiligd, omdat de applicatie er ogenschijnlijk prima mee draait.

Maak er een vaste routine van: een tabel is pas klaar wanneer RLS is ingeschakeld, vier policies zijn gedefinieerd, en er een regel is toegevoegd aan het centrale autorisatiedocument. Dat kost drie minuten, en het voorkomt de geleidelijke opeenhoping van onbeschermde tabellen die bij vrijwel elke audit naar boven komt.

**Migraties moeten hun eigen policies bevatten.** Als een tabel wordt aangemaakt via een SQL-migratiebestand, horen de bijbehorende RLS-policies in datzelfde bestand te staan. Policies die handmatig in een dashboard worden aangeklikt, bestaan alleen in die specifieke database. Bij een database-restore, een staging-omgeving of een lokale ontwikkelomgeving ontstaat dan een systeem waarin de data aanwezig is maar de beveiliging ontbreekt — de gevaarlijkste situatie denkbaar, omdat alles functioneert.

**Wees alert op policies die worden verwijderd in plaats van hersteld.** Wanneer een nieuwe feature faalt met een permissiefout, zijn er twee oplossingen: de juiste permissie toekennen of de controle tijdelijk uitschakelen. Die tweede optie is sneller. Over een heel jaar bezien holt die asymmetrie een zorgvuldig ontworpen beveiligingsmodel stap voor stap uit. Het reviewen van wijzigingen in policy-bestanden levert meer beveiligingswaarde op dan vrijwel elk ander onderdeel van de codebase.

**Test opnieuw na structurele databasewijzigingen.** Het toevoegen van een kolom, het splitsen van een tabel, het introduceren van een nieuwe gebruikersrol of een wijziging in tenant-structuren kan eerdere aannames in policies ongeldig maken. De vijandige test tussen twee accounts kost vijf minuten en hoort thuis in de vaste release-procedure voorafgaand aan elke deployment die het databaseschema raakt.

**Plan elk kwartaal een audit in.** Maak een lijst van alle tabellen, verifieer dat RLS overal actief is, controleer de aanwezigheid van de vier policies, en voer de cross-account test uit. Een half uur per kwartaal volstaat om sluipende kwetsbaarheden te elimineren voordat ze schade aanrichten.

## Het Autorisatiemodel Definitief Goed Inrichten

Voor een draaiende applicatie met actieve gebruikers is dit overzichtelijk precisiewerk in plaats van een complete herbouw.

LaunchStudio pakt dit aan volgens een vaste systematiek: elke tabel wordt geïnventariseerd inclusief de vergeten hulptabellen, het autorisatiemodel wordt samen met u in heldere taal uitgeschreven, RLS wordt overal geactiveerd, policies worden per bewerking geschreven met sessie-gebaseerde identiteit, gebruikersrollen worden verplaatst naar afgeschermde tabellen, database-indexen worden toegevoegd om vertraging te voorkomen, en het volledige geheel wordt geverifieerd via actieve inbraaktests vanaf een extern account — zonder dat de interface die u heeft gebouwd wordt aangetast, en met volledige documentatie zodat u de regels zelfstandig kunt onderhouden.

De engineers zijn afkomstig van Manifera: elf jaar ervaring met enterprise databases en beveiliging voor klanten zoals Vodafone, TNO en CFLW, vanuit Amsterdam (Herengracht 420) en Ho Chi Minhstad. [Stuur ons uw project](https://launchstudio.eu/nl/#contact) voor een gerichte analyse, doorgaans binnen één werkdag, of bekijk de specificaties van het [Launch Ready pakket](https://launchstudio.eu/nl/#packages).

## Echt voorbeeld

### Een Ledentabel Die Elk Lid Kon Uitlezen

Koen Vermeulen bouwde Ledenadmin met Lovable: ledenadministratie-software die werd gebruikt door vijf sportverenigingen in en rondom Helmond — twee voetbalclubs, een tennisvereniging, een zwemclub en een turnvereniging. In totaal circa 4.000 leden, inclusief namen, adressen, geboortedata, IBAN-nummers voor automatische incasso en in sommige gevallen vertrouwelijke medische notities voor trainers.

Row Level Security was weliswaar ingeschakeld op de ledentabel, maar de actieve policy stond iedere geauthenticeerde gebruiker toe om alle rijen op te vragen (`SELECT true`). Die regel was tijdens de ontwikkelfase haastig ingevoerd toen een ledenlijst leeg bleef en de snelste oplossing een regel was die alle rijen teruggaf.

Elk lid met een inlogaccount — alle 4.000 leden — kon de volledige gegevens van elk ander lid inzien, dwars door alle vijf de verenigingen heen, door de openbare Supabase-API rechtstreeks aan te roepen met de publieke anon-key uit de broncode van de browser.

Niemand had dat nog gedaan. Het probleem kwam aan het licht toen de penningmeester van de tennisclub, die zelf in de IT-sector werkte, vroeg hoe de scheiding tussen de verschillende verenigingen technisch gewaarborgd was en geen genoegen nam met een ontwijkend antwoord.

Negen werkdagen aan gerichte interventies: een volwaardige organisatie- en lidmaatschapsstructuur werd opgezet waarin elke vereniging een strikt gescheiden tenant vormt met specifieke rollen voor lid, commissielid en beheerder; policies werden per tabel en per database-operatie herschreven met identiteit ontleend aan de sessie (`auth.uid()`); de rolkolom werd uit het bewerkbare gebruikersprofiel gehaald en ondergebracht in een lidmaatschapstabel waar gebruikers zelf geen schrijfrechten op hebben; bankgegevens en IBAN's werden verplaatst naar een aparte tabel die uitsluitend door clubbestuurders kan worden gelezen; indexen werden toegevoegd op de lidmaatschapskolommen nadat een policy-check een ledenoverzicht vertraagde; het autorisatiemodel werd vastgelegd in een helder document van één pagina; en het geheel werd uitvoerig getest vanuit drie verschillende accounts bij verschillende clubs plus een niet-ingelogde client, inclusief een geautomatiseerde scan van alle tabellen met uitsluitend de publieke sleutel.

Die laatste scan bracht nog twee vergeten tabellen aan het licht die de frontend niet meer gebruikte — een oude import-stagtabel met een verouderde kopie van de ledenlijst en een ongebruikte audit-tabel — die beide openbaar leesbaar bleken en direct werden opgeruimd.

**Resultaat:** De vijf sportclubs ondertekenden de gezamenlijke verwerkersovereenkomst (DPA) die eerder was vastgelopen, en Koen beschikt nu over een officieel beveiligingsdocument dat hij direct overlegt wanneer een verenigingsbestuur vraagt naar data-isolatie.

> *"Vierduizend verenigingsleden konden elkaars bankrekeningnummers inzien omdat anderhalf jaar geleden een lijst leeg bleef en ik de foutmelding snel wilde laten verdwijnen."*
> — **Koen Vermeulen, Oprichter, Ledenadmin (Helmond)**

**Kosten & Doorlooptijd:** €4.600 (organisatie- en lidmaatschapsmodel, herinrichting policies per bewerking, afscherming van rollen, database-indexering, documentatie en penetratietesten) — afgerond in 9 werkdagen.

## Veelgestelde vragen

### Is het inschakelen van Row Level Security op zichzelf voldoende?

Nee. Het inschakelen zorgt er alleen voor dat de tabel standaard alle verzoeken weigert; policies bepalen vervolgens wat wel mag. Het grootste gevaar schuilt in het omgekeerde: policies schrijven op een tabel waar RLS per ongeluk nooit is ingeschakeld, waardoor de tabel wagenwijd open blijft staan zonder dat de interface een fout geeft.

### Waarom worden er zo vaak policies geschreven die alles toestaan?

Omdat een query die geen data oplevert een direct zichtbare bug is in de interface, en een permissieve policy (`USING (true)`) die foutmelding onmiddellijk laat verdwijnen. Dat is de snelste fix en precies wat een AI-agent genereert wanneer de opdracht luidt: "deze query geeft niets terug, los het op".

### Mag een policy vertrouwen op een ID die de frontend meestuurt?

Absoluut niet. Alles wat een client meestuurt in een verzoek kan door een gebruiker worden gemanipuleerd. Eigenaarschap en lidmaatschap moeten altijd worden afgeleid uit het cryptografisch geverifieerde sessietoken (`auth.uid()`), en rollen moeten in een tabel staan die niet door gebruikers kan worden gewijzigd.

### Heb ik aparte policies nodig voor updates en deletes?

Ja. Elke database-operatie (`SELECT`, `INSERT`, `UPDATE`, `DELETE`) wordt afzonderlijk beheerd. Het uitsluitend beveiligen van `SELECT` is een veelvoorkomend beveiligingslek: gebruikers kunnen dan weliswaar alleen hun eigen records inzien, maar willekeurige records van anderen overschrijven of wissen.

### Hoe weet ik zeker dat mijn policies waterdicht zijn?

Door ze actief aan te vallen. Maak twee accounts aan in verschillende browsers, probeer elkaars records uit te lezen, te wijzigen, te verwijderen en aan te maken, herhaal dit terwijl u bent uitgelogd, en vraag tenslotte alle tabellen op met uitsluitend uw publieke anon-key. Dat is hoe verborgen datalekken aan het licht komen.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Is het inschakelen van Row Level Security op zichzelf voldoende?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Nee. Het inschakelen weigert standaard alles en policies bepalen wat is toegestaan. Het grootste risico zijn tabellen met policies waar RLS nooit daadwerkelijk is geactiveerd."
      }
    },
    {
      "@type": "Question",
      "name": "Waarom worden er zo vaak policies geschreven die alles toestaan?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Omdat een lege query een zichtbare bug is en een permissieve policy dit direct verhelpt — precies wat AI genereert bij de prompt 'los deze lege query op'."
      }
    },
    {
      "@type": "Question",
      "name": "Mag een policy vertrouwen op een ID die de frontend meestuurt?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Nee. Identiteit moet afkomstig zijn uit het geverifieerde sessietoken (auth.uid()), en rollen moeten in tabellen staan die gebruikers niet zelf kunnen muteren."
      }
    },
    {
      "@type": "Question",
      "name": "Heb ik aparte policies nodig voor updates en deletes?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ja. Elke bewerking vereist eigen regels. Alleen SELECT beveiligen laat records kwetsbaar voor ongeautoriseerde wijzigingen en verwijderingen door derden."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe weet ik zeker dat mijn policies waterdicht zijn?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Door een actieve penetratietest: twee accounts die over en weer elkaars data proberen te muteren, herhaald zonder login, plus een tabel-enumeratie met de anon-key."
      }
    }
  ]
}
</script>
