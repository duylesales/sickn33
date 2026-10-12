---
Titel: "Supabase Beveiliging: Edge Functions en Waar de Veiligheidsgrens Ligt"
Trefwoorden: supabase beveiliging, ai app beveiliging, edge functions server side, aanroeper verifiëren, geheimen in functies, LaunchStudio, Manifera
Koperfase: Beslissing
Doelgroep: Technische Solo-Oprichter / Indie Hacker
---

# Supabase Beveiliging: Edge Functions en Waar de Veiligheidsgrens Ligt

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Supabase Beveiliging: Edge Functions en Waar de Veiligheidsgrens Ligt",
  "description": "Edge functions vormen de vertrouwde serverhelft van een AI-gebouwde applicatie. Welke bewerkingen daar thuishoren, hoe je de aanroeper verifieert, wat je valideert op de grens en de fouten die een functie net zo kwetsbaar maken als de browser.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-07-21",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/supabase-security-edge-functions-and-boundaries" }
}
</script>

Elke software-applicatie heeft een fundamentele scheidslijn. Aan de ene kant bevindt zich code waarover jij de volledige controle hebt, draaiend op beveiligde infrastructuur onder jouw beheer. Aan de andere kant draait code op het apparaat van een willekeurige vreemde, die deze code naar believen kan inzien, manipuleren en herhaaldelijk kan verzenden.

In een met AI gebouwd product is die scheidslijn opvallend vaak onzichtbaar. De AI-tool genereerde immers beide helften in dezelfde sessie, in dezelfde programmeertaal (TypeScript of JavaScript), in mappen die vlak naast elkaar staan. Niets in de editor verklapt dat de ene map een vertrouwde omgeving is en de andere per definitie onveilig. Supabase Edge Functions zijn de plek waar de vertrouwde helft leeft. Begrijpen wat daar thuishoort — en wat er alsnog geverifieerd moet worden zodra een verzoek binnenkomt — vormt het verschil tussen een waterdicht Supabase-project en een wagenwijd openstaande applicatie.

## Waar Edge Functions Daadwerkelijk voor Bedoeld Zijn

Edge functions voeren code uit op infrastructuur die jij beheert, dichtbij de eindgebruiker, met toegang tot geheime sleutels die de browser nooit te zien krijgt. Dat levert je drie vaardigheden op die de frontend principieel niet kan bieden:

**Geheimen bewaren.** Een bevoorrechte database-sleutel, het webhook-geheim van je betaalprovider, of een API-sleutel van een AI-model.

**Autorisatiebeslissingen nemen die niet te manipuleren zijn.** Bepalen of een specifieke gebruiker een specifieke actie mag uitvoeren, op een plek waar de gebruiker de logica niet kan aanpassen.

**Bewerkingen uitvoeren namens een gebruiker zonder de details bloot te geven.** Externe systemen aanroepen, data aggregeren over meerdere records heen, of een handeling verrichten waarvoor hogere privileges vereist zijn dan de gebruiker zelf bezit.

Alles daarbuiten — visuele weergave, gebruikersinteractie, optimistische UI-updates en comfortabele invoerchecks — hoort thuis in de frontend. Dat verplaatsen naar een edge function maakt je app uitsluitend trager, zonder een greintje extra veiligheid op te leveren.

## De Veiligheidstoets: Drie Vragen

Stel jezelf bij elk afzonderlijk stukje bedrijfslogica deze drie vragen in vaste volgorde:

**Heeft het een geheim nodig?** Zo ja: server-side. Er bestaat geen scenario waarin een geheime sleutel veilig in een webbrowser kan worden geladen.

**Bepaalt het wat iemand wel of niet mag doen?** Zo ja: server-side. Een autorisatiecheck die de gebruiker in zijn browser kan uitschakelen, is geen controle.

**Kost een fout geld of lekt het gevoelige data?** Zo ja: server-side, zelfs wanneer de frontend dezelfde check ook uitvoert voor een soepele gebruikerservaring.

Drie keer 'nee'? Dan kan de logica prima in de frontend blijven. Voor het leeuwendeel van een applicatie luidt het antwoord driemaal nee, en daarom functioneert de frontend op die punten uitstekend zoals hij is.

## Wat Zich Altijd aan de Vertrouwde Kant Moet Bevinden

**Alles wat een bevoorrechte sleutel gebruikt.** De Supabase `service_role`-sleutel omzeilt elke Row Level Security (RLS) regel die je hebt geschreven en hoort uitsluitend thuis in de omgevingsvariabelen van je edge functions.

**Financiële transacties.** Betalingen aanmaken, transacties verifiëren, restituties uitvoeren en webhooks ontvangen van Stripe of Mollie.

**Aanroepen naar betaalde API's van derden.** LLM-modellen, sms-gateways, geocoding. Niet alleen vanwege de geheime sleutel, maar omdat een edge function de plek is waar je per gebruiker limieten afdwingt vóórdat de kosten gemaakt worden.

**Data-aggregatie over meerdere gebruikers.** Een managementrapport over gegevens die de aanvragende gebruiker individueel niet rechtstreeks mag inzien.

**Beheerdershandelingen.** Het toekennen van rollen, verwijderen van accounts, of acties namens een andere gebruiker.

**Bedrijfsregels met financiële impact.** Kortingen toekennen, orderbedragen doorrekenen en controleren of iemand in aanmerking komt voor een actie.

## De Aanroeper Verifiëren Binnen de Functie

Dit is de stap die door AI gegenereerde functies het vaakst overslaan, en het ontbreken ervan verandert een serverfunctie in een wagenwijd openbaar API-endpoint.

Een edge function die in je Supabase-project is gedeployd kan worden aangeroepen door iedereen die de URL kent. Hij is niet magisch privé omdat hij op jouw cloudomgeving draait. De allereerste regels van elke functie moeten daarom vaststellen wie er belt: lees het sessietoken (JWT) van de aanroeper uit, verifieer de handtekening en leid de gebruikersidentiteit af uit dat cryptografische token.

Twee fouten komen steeds terug: een gebruikers-ID (`user_id`) uitlezen uit de JSON-body van het verzoek in plaats van uit het geverifieerde sessietoken — waardoor de aanroeper simpelweg zelf kan beweren wie hij is. En controleren of er een token aanwezig is, zónder te verifiëren of het token geldig en niet verlopen is.

Zodra de identiteit vaststaat, volgt direct de autorisatievraag: mag *deze* specifieke gebruiker *deze* actie uitvoeren op *dit* specifieke record? Die check hoort thuis in de functie, in de onderliggende RLS-databasepolicies, of bij voorkeur in beide.

## Valideer Hard op de Veiligheidsgrens

Alles wat bij een edge function binnenkomt is onbetrouwbaar, inclusief verzoeken afkomstig van je eigen frontend, omdat iedereen een identiek HTTP-verzoek kan nabouwen met tools als Postman of curl.

Valideer de structuur, datatypes en waardebereiken van elke invoerparameter tegen een schema (zoals Zod). Weiger direct elk verzoek dat onverwachte extra velden bevat in plaats van ze stilzwijgend te negeren; het stilzwijgend accepteren van extra velden is namelijk hoe een frauduleus `is_admin: true` vlaggetje in de database kan belanden. Stel bovendien harde limieten aan de payload-grootte: een functie die oneindig grote bestanden accepteert vormt een direct Denial-of-Service (DoS) en kostenrisico.

Een krachtige gewoonte: deel hetzelfde validatieschema tussen je frontend en je edge function, zodat de browser snelle feedback geeft en de server de keiharde beveiliging afdwingt.

## Geheimenbeheer in Edge Functions

Omgevingsvariabelen binnen functies zijn de aangewezen plek voor API-sleutels. Drie gewoonten houden dit veilig:

**Eén centrale plek per geheim.** Als een sleutel rondslingert in een functie, op een deploymentplatform én in een lokaal testbestand, wordt periodiek roteren iets waar je tegenop ziet.

**Log ze nooit.** Ook niet per ongeluk in foutmeldingen (`console.error(err)`), wat de klassieke manier is waarop geheime tokens belanden in externe logtools waar veel meer mensen toegang toe hebben.

**Hanteer minimale privileges (Least Privilege).** Gebruik waar mogelijk API-sleutels met beperkte rechten in plaats van masterkeys; als een specifieke sleutel lekt, blijft de schade beperkt.

## Cold Starts, Time-outs en Limieten

Praktische eigenschappen die bepalen hoe je functies ontwerpt:

Edge functions die even niet zijn aangeroepen hebben een 'cold start' nodig op het eerste verzoek. Voor een interactieve gebruikersactie kan die vertraging merkbaar zijn; voor een webhook-ontvanger is het irrelevant. Functies kennen bovendien harde time-outlimieten (meestal enkele tientallen seconden). Tijdrovende processen — zoals een omvangrijke data-export of een trage LLM-generatie — horen daarom direct een ontvangstbevestiging te sturen en op de achtergrond verder te draaien, in plaats van de HTTP-verbinding open te houden tot hij crasht.

Ken de limieten van je platform vooraf en ontwerp de gebruikerservaring op het traagste scenario in plaats van op het ideale geval.

## Loggen Zonder Data te Lekken

Edge functions zijn de plek waar je achterhaalt wat er misgaat, maar tegelijkertijd de plek waar persoonsgegevens het makkelijkst lekken naar systemen waar ze niet thuishoren.

Log wat je nodig hebt om incidenten te debuggen: wie de aanroep deed (user_id), wanneer, welke operatie, de tijdsduur, de uitkomst (succes/fout), en een unieke foutcode. Log standaard géén complete request bodies, want daarin staat alles wat jouw gebruikers zojuist hebben ingetypt. Mocht je data nodig hebben om een specifieke fout te reproduceren, log deze dan uitsluitend bij fouten en hanteer een strikte automatische verwijdering na bijvoorbeeld zeven dagen.

Dit is meer dan netjes werken: logbestanden zijn onder de AVG volwaardige verwerkingen van persoonsgegevens, met eigen bewaartermijnen en privacyverplichtingen.

## Je Eigen Functies Controleren

Een half uur inspectie brengt de meeste kwetsbaarheden in een door AI gegenereerd project aan het licht:

Maak een lijst van alle edge functions in je repository. Toets elke functie aan deze vragen: verifieert hij het token van de beller? Leidt hij de identiteit af uit het token en niet uit de payload? Controleert hij of de gebruiker bevoegd is voor dit specifieke record? Valideert hij invoer tegen een schema? Gebruikt hij de `service_role`-sleutel en is dat strikt noodzakelijk? Logt hij privacygevoelige gegevens? En wat gebeurt er als iemand de functie duizend keer in één minuut aanroept?

Voer daarna één praktische test uit: roep een functie rechtstreeks aan via de terminal of een API-tool, buiten je frontend om, met een aangepaste gebruikers-ID. Elke call die slaagt, is een acuut beveiligingslek.

## De Vertrouwde Helft Solide Neerzetten

Voor de meeste met AI gebouwde applicaties is dit een overzichtelijk, afgebakend traject: vaststellen welke operaties aan de verkeerde kant van de grens zijn beland, deze verplaatsen naar edge functions, caller-verificatie en invoervalidatie implementeren, geheimen centraliseren, rate limiting inrichten, en logging AVG-veilig maken.

Dit vormt een vast onderdeel van het [Launch Ready pakket](https://launchstudio.eu/nl/#packages) — uitgevoerd zonder de frontend aan te raken die je in Lovable hebt ontworpen, met een codebase die netjes, conventioneel en AI-leesbaar blijft zodat je daarna zelfstandig door kunt bouwen. De engineers zijn van Manifera: elf jaar ervaring met productiesystemen voor klanten als Vodafone, TNO en CFLW, vanuit Amsterdam en Ho Chi Minhstad.

Heeft je app edge functions maar heb je ze nog nooit rechtstreeks van buitenaf getest? [Praat met een engineer die AI-gegenereerde code begrijpt](https://launchstudio.eu/nl/#contact).

## Wanneer een Functie Juist Níet Nodig Is

De tegenovergestelde fout is minder gevaarlijk maar komt vaker voor dan gedacht: werkelijk alles door edge functions sluizen omdat 'de server veiliger klinkt'.

**Je eigen data uitlezen heeft geen functie nodig.** Als Row Level Security (RLS) een databasetabel correct afschermt naar de eigenaar, kan de frontend deze data rechtstreeks bevragen met de openbare `anon`-sleutel. Dit inpakken in een tussenliggende functie voegt vertraging, cold starts en onderhoud toe, zonder enige meerwaarde — de databasepolicy deed het werk immers al.

**Eenvoudig filteren en sorteren hoort in de database.** PostgreSQL is vele malen sneller in query-optimalisatie dan een JavaScript-functie die data doorgeeft.

**Weergavelogica hoort zeker niet op de server.** Datumnotaties, valuta-opmaak voor de gebruiker en optimistische UI-updates horen thuis waar de gebruiker is: in de browser.

De toets is dezelfde drie vragen in omgekeerde volgorde: als een bewerking geen geheim vereist, geen toegangsrechten toekent en een fout niets kost, hoort de code in de frontend thuis met een RLS-policy die de data aan de onderkant beveiligt.

Een project met veertig edge functions is meestal een project waar iemand starre regels heeft gevolgd in plaats van gezond verstand. Het resulteert in een trage applicatie met een onnodig groot aanvalsoppervlak. Edge functions vormen de beveiligde grens, niet de standaardlocatie voor alle code.

## Echt voorbeeld

### Een Functie Die Iedereen Geloofde Die Zich Meldde

Bram Osinga bouwde Declaratie in Lovable: een tool voor onkostendeclaraties gebruikt door zeven kleine accountantskantoren rond Hilversum, waarbij medewerkers bonnen indienen en maatschapsleden deze goedkeuren.

Het goedkeuren werd afgehandeld door een edge function, wat architectonisch de juiste keuze was — voor het accorderen was immers een bevoorrechte sleutel nodig om een statusveld aan te passen dat werknemers zelf niet mochten wijzigen. De functie was netjes geschreven en deed exact wat er gevraagd werd.

Wat de functie echter niet deed, was verifiëren wie het verzoek verstuurde. De functie las een `user_id` en een `role` rechtstreeks uit de JSON-payload en vertrouwde beide blindelings. Elke medewerker die het 'Netwerk'-tabblad in zijn browser opende, het goedkeuringsverzoek kopieerde en twee waarden aanpaste, kon zijn eigen declaraties voor willekeurige bedragen direct goedkeuren als ware hij de eigenaar van het accountantskantoor.

Niemand had dit nog gedaan; een technische review bracht het lek aan het licht voordat het misging.

Vijf werkdagen werk: caller-verificatie geïmplementeerd over alle zes functies in het project, waarbij de identiteit uitsluitend wordt afgeleid uit het cryptografisch gevalideerde sessietoken; autorisatiechecks toegevoegd per specifieke declaratie en kantoor; invoervalidatie ingeregeld met gedeelde schema's die onverwachte velden hard afwijzen; de bevoorrechte sleutel verwijderd uit twee functies die hem niet nodig hadden; rate limiting geactiveerd op indiening en goedkeuring; en logging teruggebracht tot metadata, waarbij declaratie-inhoud alleen bij fouten tijdelijk wordt vastgelegd.

**Resultaat:** het lek werd gedicht vóórdat er misbruik van werd gemaakt, en de externe accountant van de kantoren — die informeerde naar de scheiding van bevoegdheden — ontving een sluitende technische toelichting waarmee de audit direct werd afgerond.

> *"De functie draaide op mijn eigen server, dus ik ging ervan uit dat het veilig was. Het kwam geen seconde in me op dat iedereen die functie rechtstreeks kon aanroepen en simpelweg kon beweren dat hij de baas was."*
> — **Bram Osinga, Oprichter, Declaratie (Hilversum)**

**Kosten & Doorlooptijd:** € 2.300 (caller-verificatie en autorisatie over zes functies, invoervalidatie, key-scoping, rate limiting, veilige logging) — afgerond in 5 werkdagen.

## Veelgestelde vragen

### Zijn edge functions automatisch privé omdat ze op mijn cloudinfrastructuur draaien?

Nee. Een gedeployde edge function kan worden aangeroepen door iedereen die de openbare URL kent. De functie is 'vertrouwd' in de zin dat hij geheime sleutels kan bewaren zonder dat de browser ze ziet, niet in de zin dat alleen jouw eigen app hem kan bereiken. Daarom moet elke functie zijn aanroeper verifiëren.

### Hoe stelt een edge function betrouwbaar vast wie hem aanroept?

Aan de hand van het sessietoken (JWT) van de gebruiker, waarvan de echtheid en geldigheid binnen de functie cryptografisch worden gecontroleerd. Vertrouw nooit op een `user_id` in de meegestuurde JSON-body, want die kan de aanroeper naar willekeur manipuleren.

### Wat hoort er in een edge function thuis in plaats van in de frontend?

Alles wat geheime sleutels gebruikt, alles wat autorisatiebeslissingen forceert, en elke logica waarbij een foutieve uitkomst geld kost of data lekt. Voor het merendeel van een applicatie geldt dit niet, waardoor die logica prima in de frontend kan blijven.

### Heb ik nog wel Row Level Security nodig als mijn functies autorisatie controleren?

Ja, absoluut. 'Defence in depth' is essentieel: de automatisch gegenereerde Supabase-API blijft altijd bereikbaar met je publieke sleutel, los van je functies. RLS-policies beschermen de database rechtstreeks, terwijl functiechecks de specifieke bedrijfsbewerking beveiligen.

### Welke gegevens mag een edge function veilig loggen?

Standaard uitsluitend metadata: wie riep aan, welke operatie, tijdsduur, resultaat en een foutcode. Vermijd het loggen van complete request-payloads, omdat deze persoonsgegevens bevatten. Log inhoud uitsluitend bij uitzonderingen met een korte automatische bewaartermijn.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Zijn edge functions automatisch privé omdat ze op mijn cloudinfrastructuur draaien?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Nee — iedereen die de URL kent kan ze aanroepen. Ze zijn vertrouwd om geheimen te bewaren, niet afgeschermd van aanroepers; elke functie moet de aanroeper verifiëren."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe stelt een edge function betrouwbaar vast wie hem aanroept?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Via het cryptografisch geverifieerde sessietoken (JWT) binnen de functie, nooit via een user-ID in de request body die door de afzender gemanipuleerd kan worden."
      }
    },
    {
      "@type": "Question",
      "name": "Wat hoort er in een edge function thuis in plaats van in de frontend?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Bewerkingen met geheimen, autorisatiebesluiten, en logica waarbij fouten geld kosten of data lekken. De rest functioneert prima in de frontend."
      }
    },
    {
      "@type": "Question",
      "name": "Heb ik nog wel Row Level Security nodig als mijn functies autorisatie controleren?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ja — de gegenereerde Supabase-API blijft bereikbaar met de publieke anon-key, dus RLS-policies beschermen de database direct terwijl functies de operatie bewaken."
      }
    },
    {
      "@type": "Question",
      "name": "Welke gegevens mag een edge function veilig loggen?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Standaard alleen metadata (user-ID, operatie, duur, status) en inhoud alleen bij fouten met een korte bewaartermijn, aangezien logs persoonsgegevens bevatten."
      }
    }
  ]
}
</script>
