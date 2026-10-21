---
Titel: "Subverwerkers: Elke Dienst Opsommen Die Uw App Raakt"
Trefwoorden: subverwerkers, subprocessors, leverancierslijst, datastromen, diensten van derden, LaunchStudio, Manifera
Koperfase: Beslissing
Doelgroep: SaaS Scale-Up
---

# Subverwerkers: Elke Dienst Opsommen Die Uw App Raakt

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Subverwerkers: Elke Dienst Opsommen Die Uw App Raakt",
  "description": "Elke externe dienst waar uw product data naartoe stuurt, is een subverwerker waarover uw klanten recht hebben op informatie. De vergeten exemplaren vinden, de lijst publiceren, en klanten informeren voordat u er een toevoegt.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-12-10",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/subprocessors-listing-every-service-your-app-touches" }
}
</script>

Uw klant tekende een overeenkomst met u. Hun data wordt vervolgens verwerkt door uw hostingplatform, uw databaseprovider, uw e-maildienst, uw error tracker, uw analyticstool en mogelijk een model-API — geen van alle partijen waar uw klant ooit van heeft gehoord.

Dat zijn subverwerkers. Uw klant heeft er recht op te weten wie ze zijn, wat elk ontvangt en waar het naartoe gaat, en vooraf te horen wanneer u er een toevoegt.

De meeste oprichters kunnen er drie of vier noemen. Het werkelijke aantal in een typisch door AI gebouwd product is acht tot twaalf, en in het gat tussen die twee getallen beginnen de ongemakkelijke gesprekken.

## Vind Ze Allemaal

De lijst is geen geheugenoefening. Bouw haar op basis van bewijs.

**De voor de hand liggende vier:** hosting, database, e-mail, betalingen.

**De exemplaren die voor het gemak zijn toegevoegd:** error tracking, analytics, supportchat, sessie-opname, uptimemonitoring, feature flags, een planningswidget.

**De AI-exemplaren:** elke model-API, inclusief die achter een functie die u op een middag uitbracht.

**De infrastructuurexemplaren:** een CDN, DNS, objectopslag, een zoekdienst, een wachtrij.

**De zakelijke exemplaren die klantdata raken:** uw CRM als dat hun contacten bevat, uw facturatietool, een dienst voor digitale ondertekening, een mailinglijst met hun medewerkers.

Controleer het daarna tegen de code in plaats van het geheugen. Zoek naar externe URL's, loop uw omgevingsvariabelen langs — elke sleutel impliceert een dienst — en open het netwerktabblad op uw eigen product om te zien met wie de browser contact maakt. Producten vinden routinematig een lettertypedienst, een ingesloten kaart of een analyticstool waarvan niemand zich herinnert die te hebben toegevoegd.

## Leg Vast Wat Elk Werkelijk Ontvangt

De lijst met namen is de makkelijke helft. Wat ertoe doet voor de beoordeling van een klant, is wat elke dienst krijgt.

Wees specifiek. "Error tracking" is geen antwoord; "error tracking ontvangt stacktraces en, op dit moment, volledige verzoekinhoud inclusief namen van klanten" wel. Dat niveau van specificiteit is ook hoe u ontdekt wat u moet oplossen — de tweede versie van die zin is er een die niemand wil publiceren, en juist daarom leidt het opschrijven ervan tot een wijziging.

Per dienst: welke data, voor welk doel, waar het wordt verwerkt en opgeslagen, en op welke contractuele grondslag als het buiten de EER is.

## Elk Exemplaar Heeft een Overeenkomst Nodig

U bent verplicht met elke subverwerker een verwerkersovereenkomst te hebben die dezelfde verplichtingen oplegt die u van uw klant accepteerde.

Bij grote providers is dit een standaarddocument dat u bij de aanmelding accepteert, vaak als deel van de voorwaarden. Zoek het op, bevestig dat het geldt voor uw accountniveau, en bewaar een kopie of een link.

Twee plekken waar oprichters een gat vinden. Model-API's, waar de verwerkingsvoorwaarden soms expliciete acceptatie of een bepaald plan vereisen, en waar het gedrag rond trainen op ingestuurde data per niveau verschilt. En kleine tools die op een gratis plan zijn toegevoegd, die soms helemaal geen verwerkersovereenkomst bieden — wat ze onbruikbaar maakt voor klantdata, hoe handig ze ook zijn.

## Publiceer de Lijst

Een publieke pagina met uw subverwerkers, wat elk ontvangt en waar, met een datum van laatste wijziging.

Ze verkort de inkoop aanzienlijk, omdat een beoordelaar haar leest in plaats van te vragen. Ze toont een niveau van operationele volwassenheid dat de meeste kleine concurrenten niet bereiken. En ze is het document waarnaar de bijlage van uw verwerkersovereenkomst verwijst, dus er één bijhouden houdt meerdere documenten tegelijk waar.

Bied een manier aan om op wijzigingen te abonneren, ook als dat een e-mailadres is waar mensen kunnen vragen te worden toegevoegd. De meldplicht is makkelijker na te komen als er een mechanisme voor is.

## Er Een Toevoegen Is een Beslissing, Geen Configuratie

De verplichting is klanten te informeren voordat u een subverwerker toevoegt, met de mogelijkheid bezwaar te maken. Dat maakt van "installeer deze tool en kijk of het helpt" een klein proces.

Het proces dat het overnemen waard is: bevestig voordat een nieuwe dienst klantdata ontvangt dat er een verwerkersovereenkomst is, bevestig waar ze verwerkt en opslaat, voeg haar toe aan de lijst, en informeer klanten met een opzegtermijn — 30 dagen is gangbaar.

Dat klinkt zwaar totdat u het alternatief ziet. Een oprichter die terloops een dienst toevoegt en het later noemt, heeft een contractuele toezegging geschonden, en de ontdekking vindt meestal plaats tijdens een beoordeling met een klant die al zorgvuldige vragen stelt.

Het legt ook een nuttige discipline op. Elke nieuwe subverwerker is een blijvende verplichting, nog een regel in het register, nog een afhankelijkheid, nog iets om jaarlijks te beoordelen. Een moment van wrijving vóór het toevoegen ervan is proportioneel.

## Beoordeel Ze Jaarlijks, Want Ze Veranderen

Een lijst van subverwerkers is een momentopname van relaties die onder u bewegen, en drie soorten verandering zijn het opvangen waard.

**De dienst verandert wat ze doet.** Een provider voegt een functie toe die data anders verwerkt, verhuist een regio, of wijzigt zijn voorwaarden — steeds vaker inclusief zijn standpunt over het gebruik van ingestuurde data om modellen te trainen. Providers melden deze wijzigingen per e-mail aan wie het account registreerde, en dat is vaak een adres dat niemand leest.

**De dienst wordt overgenomen.** Nieuwe eigenaar, mogelijk een nieuw rechtsgebied, nieuwe voorwaarden. Dit is de verandering die het meest waarschijnlijk ertoe doet voor een klant en het minst waarschijnlijk door een oprichter wordt opgemerkt.

**U stopt met het gebruik en de data blijft.** Het probleem van de verlaten tool dat elders in deze reeks is beschreven. Een dienst uit uw code verwijderen, verwijdert uw data niet uit de hunne — daarvoor is een verwijderverzoek nodig, dat deel moet uitmaken van het uitfaseren.

Dus een jaarlijkse ronde: bevestig dat elke dienst nog wordt gebruikt, nog een actuele overeenkomst heeft, nog verwerkt waar u zei, en nog alleen bevat wat u verwacht. Vraag voor alles wat u niet meer gebruikt om verwijdering en vraag om bevestiging.

Zet de verlengingsdatums en het e-mailadres van het account in hetzelfde document. Een lijst van subverwerkers die ook vastlegt wie het account heeft en waar de facturen naartoe gaan, is het document dat het mogelijk maakt het product aan iemand anders over te dragen — en dat, meer dan compliance, is meestal de reden dat oprichters blij zijn dat het bestaat.

## De Exemplaren Die zich in de Browser Verstoppen

Diensten die uw server aanroept, zijn in uw code te vinden. Diensten die de browser van de bezoeker aanroept, zijn een aparte categorie, en die missen oprichters volledig, omdat niets in de backend ze noemt.

Elk script, elke stylesheet, elk lettertype, elke afbeelding of insluiting van een derde partij op uw pagina's betekent dat de browser van de bezoeker een verzoek doet aan dat bedrijf — met het IP-adres, de pagina waarop hij is, en vaak een cookie. Dat is een datastroom waarvoor u verantwoordelijk bent, ook al was uw server er nooit bij betrokken.

De gebruikelijke bewoners van deze categorie in een door AI gebouwd product: een lettertypedienst geïmporteerd door een gegenereerde stylesheet, een ingesloten kaart, een videospeler, een supportchatwidget, een insluiting van sociale media, een analyticsscript, en een iconenbibliotheek die van een CDN wordt geladen.

Twee daarvan verdienen bijzondere aandacht in een product met ingelogde gebruikers. Een chatwidget op een geauthenticeerde pagina kan doorgaans de pagina lezen, wat betekent dat hij kan zien welke data van uw klant er op het scherm staat. En elk script op die pagina draait met de origin van uw applicatie, dus het is evengoed een beveiligingsafhankelijkheid als een privacykwestie.

De oplossing is in beide richtingen grotendeels dezelfde: host zelf wat u kunt — lettertypen en iconen zijn triviaal — vervang insluitingen door placeholders die op klik laden, en houd scripts van derden volledig weg van geauthenticeerde pagina's. Wat daarna overblijft, is een korte lijst die u bewust hebt gekozen, en dat is de toestand die u wilt voordat iemand ernaar vraagt.

Een content security policy maakt dit duurzaam in plaats van een eenmalige opruimactie: geef aan van welke bronnen uw pagina's mogen laden, en alles wat later wordt toegevoegd en niet op de lijst staat, laadt gewoon niet. Het is een header, het kost een middag om goed te krijgen, en het verandert "we hebben de derde partijen verwijderd" in "een derde partij kan niet worden toegevoegd zonder bewuste wijziging".

## Dit Inrichten

Voor een bestaand product kost dit doorgaans een halve dag: elke externe dienst geïdentificeerd vanuit code, omgevingsvariabelen en netwerkverkeer in plaats van geheugen, specifiek vastgelegd wat elk ontvangt, locaties van verwerking en opslag bevestigd, voor elk een verwerkersovereenkomst gevonden met gaten gedicht of de dienst vervangen, ongebruikte diensten verwijderd en hun data gewist, een gepubliceerde pagina met subverwerkers met een datum van laatste wijziging en een manier om te abonneren, dezelfde lijst gekoppeld aan de bijlage van uw verwerkersovereenkomst en uw register, en een geschreven proces dat melding vereist voordat een nieuwe dienst klantdata ontvangt.

LaunchStudio maakt dit samen met het register en de verwerkersovereenkomst, omdat het drie weergaven zijn van één inventarisatie. Daarachter staat Manifera — elf jaar, 160+ projecten, klanten als Vodafone, TNO en CFLW, vanaf de Herengracht 420 in Amsterdam.

[Vraag ons uw subverwerkers te vinden vanuit uw code](https://launchstudio.eu/nl/#contact). Het aantal is meestal hoger dan verwacht.

## Echt voorbeeld

### Elf, Geen Vier

Manon Duyvesteyn bouwde Tolkplanner in Lovable: boeking en toewijzing van tolken voor vertaalbureaus en overheidsinstanties, 24 bureaus met zo'n 1.100 tolken.

De privacyfunctionaris van een klant vroeg vóór de verlenging om haar lijst van subverwerkers. Ze schreef er vier op: hosting, database, e-mail en betalingen.

De controle tegen haar code vond er elf. Naast de vier: error tracking die volledige verzoekinhoud ontving, inclusief namen van tolken en details van opdrachten; een supportchatwidget die in de ingelogde applicatie laadde met toegang tot de pagina; een analyticsdienst die URL's met opdrachtidentificaties vastlegde; een model-API die opdrachtbriefings samenvatte, zes maanden eerder toegevoegd, die de volledige briefingtekst verstuurde; een lettertypedienst die bij elke paginalading werd aangesproken, wat betekende dat IP-adressen van bezoekers naar een derde partij gingen; een sms-provider voor meldingen aan tolken, die ze echt was vergeten omdat die één keer was ingesteld; en een dienst voor digitale ondertekening met getekende opdrachtcontracten, inclusief persoonsgegevens van tolken.

Van de elf hadden er vier geen verwerkersovereenkomst: de analyticsdienst, de lettertypedienst, de model-API op het niveau dat ze gebruikte, en de chatwidget.

Vier werkdagen: de volledige inventarisatie gebouwd vanuit code, omgevingsvariabelen en netwerkverkeer; specifiek gedocumenteerd wat elke dienst ontvangt; de lettertypedienst verwijderd en lettertypen zelf gehost; de analyticsdienst vervangen door een cookievrije tool die geen identificaties ontvangt, en URL's aangepast zodat ze geen opdrachtidentificaties meer bevatten; error tracking ingesteld om verzoekinhoud op te schonen; de model-API verplaatst naar een niveau met verwerkingsvoorwaarden en een EU-regio, met de payload teruggebracht tot alleen de briefingtekst in plaats van het volledige opdrachtrecord; de chatwidget verwijderd van geauthenticeerde pagina's en vervangen door een supportlink; verwerkersovereenkomsten gevonden en opgeslagen voor de overige diensten; een gepubliceerde pagina met subverwerkers, locaties en een datum van laatste wijziging; en een geschreven proces dat een overeenkomst, een locatiecontrole, een update van de lijst en 30 dagen melding aan klanten vereist vóór elke nieuwe dienst.

**Resultaat:** de verlenging ging door en de privacyfunctionaris noemde specifiek de gepubliceerde pagina. Manon stuurt de link nu mee met elk voorstel. Twee van de elf diensten bestaan helemaal niet meer in haar product, wat ze het meest bevredigende deel noemt.

> *"Ik had gezworen dat het er vier waren. Wat me het meest dwarszat, was het lettertype — het IP-adres van elke bezoeker ging naar een bedrijf waar ik nooit aan had gedacht, omdat een gegenereerde stylesheet het importeerde."*
> — **Manon Duyvesteyn, Oprichter, Tolkplanner (Den Haag)**

**Kosten & Doorlooptijd:** €2.800 (controle van code en verkeer, documentatie per dienst, zelf gehoste lettertypen, vervanging van analytics, opschonen van foutdata, wijziging van niveau en regio van de model-API met kleinere payload, verwijderen van chatwidget, verzamelen van overeenkomsten, gepubliceerde pagina, meldproces) — afgerond in 4 werkdagen.

## Veelgestelde vragen

### Wat telt als subverwerker?

Elke externe dienst die namens u persoonsgegevens van uw klanten verwerkt — hosting, database, e-mail, error tracking, analytics, model-API's, opslag, sms, digitale ondertekening, en alles wat er verder data van ontvangt.

### Hoe vind ik degene die ik ben vergeten?

Op basis van bewijs in plaats van geheugen: doorzoek de code naar externe URL's, loop elke sleutel in uw omgevingsconfiguratie langs, en open het netwerktabblad op uw eigen product.

### Heeft elke subverwerker een overeenkomst nodig?

Ja, met de verplichtingen die u van uw klant accepteerde. Grote providers nemen er een op in hun voorwaarden; kleine tools op een gratis niveau bieden er soms geen, wat ze onbruikbaar maakt voor klantdata.

### Moet ik de lijst publiceren?

Het is niet strikt verplicht, maar het verkort de inkoop, toont volwassenheid en houdt de bijlage bij uw verwerkersovereenkomst juist. De meeste klanten die erom vragen, lezen liever een pagina dan e-mails uit te wisselen.

### Wat doe ik voordat ik een nieuwe dienst toevoeg?

Bevestig dat er een verwerkersovereenkomst is, controleer waar ze verwerkt en opslaat, voeg haar toe aan de lijst, en informeer klanten met een opzegtermijn — doorgaans 30 dagen — voordat ze data ontvangt.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Wat telt als subverwerker?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Elke externe dienst die namens u persoonsgegevens van uw klanten verwerkt — hosting, database, e-mail, error tracking, analytics, model-API's, opslag en meer."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe vind ik subverwerkers die ik ben vergeten?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Controleer op basis van bewijs — externe URL's in code, elke sleutel in de omgevingsconfiguratie, en het netwerktabblad op uw eigen product."
      }
    },
    {
      "@type": "Question",
      "name": "Heeft elke subverwerker een verwerkersovereenkomst nodig?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ja, met de verplichtingen die u accepteerde. Grote providers nemen er een op in hun voorwaarden; sommige gratis tools bieden er geen en kunnen niet voor klantdata worden gebruikt."
      }
    },
    {
      "@type": "Question",
      "name": "Moet de lijst van subverwerkers worden gepubliceerd?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Het verkort de inkoop, toont volwassenheid en houdt uw verwerkingsbijlage juist — de meeste beoordelaars lezen liever een pagina dan e-mails uit te wisselen."
      }
    },
    {
      "@type": "Question",
      "name": "Wat is het proces vóór het toevoegen van een nieuwe dienst?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Bevestig een verwerkersovereenkomst, controleer de locatie van verwerking en opslag, werk de lijst bij, en informeer klanten met ongeveer 30 dagen opzegtermijn."
      }
    }
  ]
}
</script>
