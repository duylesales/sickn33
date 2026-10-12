---
Titel: "Lovable Custom Domain: Een Actief Domein Veilig Migreren Zonder Downtime"
Trefwoorden: lovable custom domain, dns migratie, ttl instellen, registrar verhuizing, downtime voorkomen, LaunchStudio, Manifera
Koperfase: Beslissing
Doelgroep: SaaS Scale-Up
---

# Lovable Custom Domain: Een Actief Domein Veilig Migreren Zonder Downtime

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Lovable Custom Domain: Een Actief Domein Veilig Migreren Zonder Downtime",
  "description": "Een domeinnaam verhuizen die al door honderden actieve klanten wordt gebruikt is heel iets anders dan een nieuw domein koppelen. TTL-strategie, de exacte stappenvolgorde, e-mail behouden en OAuth callback-URL's die gebruikers buitensluiten.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-09-08",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/98-lovable-custom-domain-migrating-a-live-domain-safely" }
}
</script>

Een gloednieuwe domeinnaam koppelen aan een zojuist gebouwd prototype is een klusje van tien minuten zonder noemenswaardige risico's. Het migreren van een actieve domeinnaam waar dagelijks honderden betalende klanten op inloggen, is een fundamenteel andere discipline. Elke fout is direct realtime zichtbaar voor gebruikers, en sommige misstappen zijn binnen het uur simpelweg niet terug te draaien.

De aanleidingen zijn alledaags: je stapt over naar een professionelere hostingomgeving, je trekt een domein naar je toe dat ooit door een externe freelancer is geregistreerd, je wisselt van registrar na een slechte helpdesk-ervaring, of je migreert je live-applicatie voor het eerst van een generiek preview-webadres naar je officiële bedrijfsdomein.

Geen van deze stappen is technisch hogere wiskunde. Maar het proces is meedogenloos voor wie de verkeerde volgorde aanhoudt.

## Wat er daadwerkelijk mis kan gaan

Het is goed om de potentiële faalmechanismen concreet voor ogen te hebben, want zij bepalen de exacte fasering van je migratie:

**Je website wordt onbereikbaar voor een deel van je bezoekers.** Niet voor iedereen tegelijk, maar willekeurig verspreid over internetproviders, gedurende een periode die je zelf niet meer kunt beïnvloeden doordat DNS-antwoorden op tientallen tussenliggende netwerklagen gecachet worden.

**Al je zakelijke e-mailverkeer valt stil.** Dit is aanzienlijk schadelijker dan een website die tijdelijk down is, en het duurt veel langer voordat je het ontdekt. DNS-servers overzetten zonder de MX- en authenticatierecords exact over te hevelen is veruit de meest desastreuze fout in dit hele traject.

**Geen enkele gebruiker kan meer inloggen.** De OAuth- en authenticatieproviders (zoals Google, GitHub of Supabase Auth) blokkeren alle inlogpogingen omdat de redirects niet overeenkomen met de geconfigureerde Callback URL's.

**Betalingen en abonnementsverlengingen worden niet geregistreerd.** De webhooks van betaalproviders (zoals Stripe of Mollie) wijzen nog naar het oude webadres dat niet langer antwoordt.

**Je Google-posities storten in.** Zoekmachines zien het oude webadres verdwijnen en een nieuw adres verschijnen zónder de juiste permanente HTTP 301-redirects die de overgang formeel duiden.

Vijf afzonderlijke systemen, elk op een andere plek geconfigureerd, en elk perfect tevreden om tot in lengte van dagen naar de oude server te blijven wijzen.

## Verlaag altijd eerst de TTL

Dit is met afstand de meest effectieve voorbereiding, en tevens degene die het vaakst wordt overgeslagen:

Elk afzonderlijk DNS-record bevat een **Time-To-Live (TTL)**: de tijd dat resolvers en internetproviders het antwoord in hun cache mogen vasthouden. Als jouw TTL momenteel op 24 uur (86.400 seconden) staat en je past het IP-adres aan, blijven sommige bezoekers nog een volle dag de oude server benaderen — en daar kun je met geen mogelijkheid iets aan veranderen.

Verlaag daarom enkele dagen vóór de geplande migratie de TTL van alle relevante records naar een minimale waarde — bijvoorbeeld 300 seconden (5 minuten). Wacht vervolgens minimaal 24 uur totdat de oude, lange TTL wereldwijd overal uit de caches is verdwenen. Wanneer je daarna de daadwerkelijke overstap maakt, verspreidt de wijziging zich binnen vijf minuten wereldwijd. En mocht er onverhoopt iets misgaan, dan draai je de wijziging net zo snel weer terug.

Verhoog de TTL pas weer een volle week na een bewezen stabiele migratie.

## De volgorde die downtime uitsluit

Hanteer dit strikte draaiboek:

**1. Inventariseer álles wat aan dit domein gekoppeld is.** De website, e-mail, subdomeinen, authenticatie-callbacks, betaalwebhooks, mobiele app-koppelingen en externe software waarin het domein staat vermeld. Deze inventarisatielijst ís je migratieplan; elk vergeten item wordt een operationeel incident.

**2. Exporteer de complete actieve DNS-zonefile.** Elk afzonderlijk record, letter voor letter zoals het nu live staat. Dit is je referentiepunt en je absolute noodrem.

**3. Bouw de nieuwe hostingomgeving op en test deze op een tijdelijk webadres.** Vóórdat je ook maar één DNS-record aanraakt. De nieuwe server moet je echte applicatie met echte data foutloos serveren vóór de switch.

**4. Richt alle records identiek in bij de nieuwe DNS-provider vóórdat je de naamservers omzet.** Inclusief alle e-mailrecords: MX, SPF, DKIM en DMARC. De configuratie moet kant-en-klaar klaarstaan zodat er geen seconde vacuüm ontstaat.

**5. Werk authenticatie-callbacks en webhooks vooraf bij.** De meeste platforms ondersteunen meerdere geldige callback-adressen tegelijkertijd. Voeg het nieuwe adres toe vóór de overstap; verwijder het oude adres pas een week later. Hiermee schakel je twee van de vijf faalpunten vooraf geruisloos uit.

**6. Schakel om op een rustig moment op een doordeweekse ochtend.** Nooit op vrijdagmiddag of in het weekend. Kies bijvoorbeeld dinsdagochtend om 07:00 uur, zodat je eventuele haperingen direct kunt opvangen tijdens kantooruren.

**7. Valideer direct de complete checklist:** www- en hoofddomein, SSL-certificaat, inloggen, testbetaling en het versturen én ontvangen van e-mail.

**8. Ruim na één week op:** verhoog de TTL weer naar een normale waarde en saneer oude callbacks.

## E-mail verdient een eigen alinea

Omdat hier in de praktijk de zwaarste zakelijke schade ontstaat:

E-mailrecords (MX) staan technisch volledig los van de A- en CNAME-records die naar je website wijzen. Wanneer je de DNS overzet naar een nieuwe provider zonder de MX-, SPF-, DKIM- en DMARC-records vooraf over te nemen, stopt alle inkomende e-mail per direct. Afzenders ontvangen onbestelbaar-meldingen; klanten denken dat je failliet bent of hen negeert.

Neem de mailrecords exact over. Stuur direct na de omzetting testberichten vanaf je eigen zakelijke mailbox en vanuit de applicatie naar meerdere grote e-mailproviders (zoals Google Workspace en Microsoft 365). Controleer of de berichten aankomen en of de SPF- en DKIM-handtekeningen als geldig worden gevalideerd.

## Het verhuizen van de registrar is een aparte operatie

Twee concepten worden voortdurend met elkaar verward: het wijzigen van de **naamservers (DNS)** en het overdragen van de **domeinregistratie (registrar transfer)**.

Het wijzigen van naamservers is een kwestie van minuten en is op elk moment direct omkeerbaar. Het verhuizen van een domein naar een andere registrar (zoals van TransIP naar Cloudflare of AWS) is een formeel administratief proces met verhuiscodes (EPP/auth-code), bevestigingsmails en vaak een verplichte wachttijd van meerdere dagen. Bovendien hanteren veel registrars een overdrachtsblokkade (transfer lock) van 60 dagen na een recente verhuizing.

Doe deze twee stappen nooit tegelijk. Zet eerst rustig de DNS om, valideer dat de website en e-mail een week foutloos draaien, en start pas daarna de formele registrar-transfer wanneer alles in rustig vaarwater is beland. Voor een `.nl`-domein verloopt de overdracht via SIDN doorgaans vlotter dan bij een `.com`, maar de scheiding tussen DNS en registrar blijft essentieel.

## Behoud van zoekmachinerankings

Als niet alleen de hosting verandert, maar ook de feitelijke domeinnaam (bijvoorbeeld van `mijnapp.lovable.app` naar `mijnapp.nl`), moet je je organische vindbaarheid beschermen:

Stel permanente **HTTP 301-redirects** in vanaf elke oude URL naar de exacte equivalente pagina op het nieuwe domein. Behoud deze redirects jarenlang actief. Meld de adreswijziging formeel aan in Google Search Console via de functie 'Adreswijziging'. Werk je canonical tags en XML-sitemaps direct bij. Houd rekening met een lichte tijdelijke schommeling in rankings gedurende de eerste paar weken na de verhuizing.

## De checklist direct na de overstap

Loop deze punten direct na de DNS-omzetting af:
- Zowel de `www`- als de kale domeinversie lossen op, en de ene verwijst netjes met een 301-redirect naar de andere.
- Het SSL-certificaat is geldig op alle varianten, inclusief subdomeinen.
- Een echte gebruiker kan succesvol inloggen via e-mail én via social logins.
- Een testbetaling van € 1 wordt succesvol verwerkt en de webhook activeert de juiste accountstatus.
- Een e-mail gestuurd naar je zakelijke adres komt direct binnen in je inbox.
- Een transactionele mail vanuit de applicatie wordt afgeleverd zonder in de spambox te belanden.
- Geen enkel configuratiebestand in je codebase verwijst nog hardcoded naar het oude webadres.
- De error tracker toont geen onverwachte piek aan 404- of netwerkfouten.

## Mensen informeren, en de links buiten je eigen bereik

Als het webadres zelf wijzigt, zijn er externe plekken die je niet rechtstreeks kunt aanpassen:

**Bladwijzers van klanten en bewaarde wachtwoorden:** Deze volgen permanente redirects automatisch, mits je het oude domein nooit laat verlopen. Het laten verlopen van een oud domein betekent dat kapers het kunnen opkopen en jouw ex-klanten kunnen misleiden.

**Documenten die al verstuurd zijn:** Eerdere offertes, facturen en PDF-contracten bevatten het oude webadres. Goed geconfigureerde redirects zijn het enige wat voorkomt dat die links veranderen in dode 404-pagina's.

**API-koppelingen van zakelijke afnemers:** Klanten van wie de systemen jouw API aanroepen op het oude adres breken zodra je de stekker eruit trekt. Informeer hen persoonlijk met een ruime overgangstermijn en monitor je logs op API-keys die het oude adres nog aanroepen.

**Fysieke uitingen:** Visitekaartjes, belettering op bedrijfswagens en beursmateriaal kun je niet updaten; het behouden van een permanente redirect is hier een vereiste.

## Een domeinmigratie zonder stress

Voor een actief SaaS-product is dit een strikt geregisseerd project: complete inventarisatie van alle gekoppelde diensten, zonefile-export, preventieve verlaging van TTL's, opbouw en validatie van de nieuwe omgeving vóór de switch, simultane registratie van webhooks en callbacks, vlekkeloze omzetting op een rustig ochtendtijdstip, e-mailverificatie en het loskoppelen van de registrar-transfer.

LaunchStudio voert deze migraties uit voor bedrijven met actieve gebruikers, inclusief volledige documentatie van de nieuwe DNS-architectuur. De software engineers zijn van Manifera: elf jaar ervaring met enterprise cloud-migraties voor klanten als Vodafone, TNO en CFLW vanuit Amsterdam Herengracht 420 en Ho Chi Minhstad.

[Vertel ons welk domein je wilt migreren](https://launchstudio.eu/nl/#contact) voor een draaiboek binnen één werkdag, of bekijk onze [pakketten](https://launchstudio.eu/nl/#packages).

## Echt voorbeeld

### De website verhuisde, maar de e-mail bleef achter

Vincent Bogaers bouwde met Lovable het platform Taxatierapport: software voor het opstellen en valideren van vastgoedtaxaties, in gebruik bij negentien makelaarskantoren en vier taxatiebureaus in de regio Bergen op Zoom en Roosendaal. Taxatierapporten worden gegenereerd in de webapp en direct gemaild naar geldverstrekkers en notarissen.

Vincent besloot over te stappen naar een dedicated hostingomgeving en wilde tegelijkertijd het DNS-beheer centraliseren bij dezelfde partij. Hij voerde de webserverrecords in, paste op donderdagmiddag de naamservers aan bij zijn registrar, en zag tot zijn vreugde dat de website binnen twintig minuten actief was op de nieuwe host. Tevreden sloot hij zijn laptop.

De mailserverrecords (MX, SPF, DKIM) waren echter niet overgenomen. Gedurende drie volle dagen werd elke inkomende e-mail naar het domein geruisloos geweigerd door de ontvangende mailservers — inclusief het centrale contactadres dat onder elk taxatierapport stond afgedrukt voor vragen van banken en hypotheekadviseurs.

Op maandagochtend openbaarden zich twee aanvullende crisissituaties: niemand van de negentien makelaars kon meer inloggen, omdat de callback URL van de authenticatiedienst nog naar het oude webadres verwees (de makelaars hadden op vrijdag gedacht dat het systeem een tijdelijke storing had); en de maandelijkse incassowebhook wees nog naar het oude platform, waardoor elf dagen aan abonnementsmutaties niet werden geregistreerd, inclusief twee opzeggingen die daardoor gratis toegang behielden.

In vijf werkdagen werd de situatie hersteld: MX-records, SPF, DKIM en DMARC werden direct hersteld en gevalideerd met leveringstests naar alle grote mailproviders; de geweigerde e-mails van het weekend waren verloren en konden niet worden hersteld, waardoor Vincent persoonlijk contact moest opnemen met alle kantoren en vier hypotheekafdelingen; authenticatie-callbacks werden gecorrigeerd; betaalwebhooks werden opnieuw aangesloten met handtekeningvalidatie en datareconciliatie; TTL's werden verlaagd en een gedocumenteerde zonefile werd opgeleverd; en de geplande registrar-transfer werd met drie weken uitgesteld en vervolgens probleemloos als aparte stap uitgevoerd.

**Resultaat:** De registrar-overstap verliep drie weken later vlekkeloos. Vincent schat dat de drie dagen onbereikbaarheid per e-mail hem bij één taxatiebureau bijna een vol jaar aan opgebouwd vertrouwen heeft gekost.

> *"De website laadde binnen twintig minuten en ik dacht dat ik klaar was. Drie dagen lang werd elke e-mail naar mijn bedrijf geweigerd, inclusief het e-mailadres dat op elk taxatierapport stond dat we ooit hadden verstuurd."*
> — **Vincent Bogaers, Oprichter, Taxatierapport (Bergen op Zoom)**

**Kosten & Doorlooptijd:** € 2.800 (herstel mailrecords en authenticatie, correctie inlogcallbacks, webhook-herstel met datareconciliatie, DNS-zone inventarisatie en draaiboek) — opgeleverd in 5 werkdagen.

## Veelgestelde vragen

### Hoe voorkom ik downtime tijdens het verhuizen van een domeinnaam?

Verlaag de TTL van je DNS-records enkele dagen vooraf naar 300 seconden, richt de nieuwe hostingomgeving vooraf in en test deze op een tijdelijk webadres, neem alle DNS-records (inclusief e-mail) vooraf over, en schakel om op een rustige doordeweekse ochtend.

### Waarom stopt zakelijke e-mail vaak met werken na een DNS-wijziging?

Omdat e-mailrecords (MX, SPF, DKIM, DMARC) technisch losstaan van de records die naar de website wijzen. Wanneer je de naamservers overzet naar een nieuwe provider zonder deze records exact te kopiëren, weigeren ontvangende mailservers direct alle inkomende berichten.

### Waarom kan niemand meer inloggen direct na de overstap?

Omdat de OAuth- en authenticatieproviders (zoals Supabase Auth of Google Login) nog de oude Callback URL hanteren. Registreer het nieuwe adres vóór de overstap naast het oude adres in het dashboard van je authenticatiedienst, en verwijder het oude adres pas na een week.

### Moet ik de registrar-transfer tegelijkertijd met de DNS-omzetting uitvoeren?

Nee, beslist niet. Het aanpassen van naamservers (DNS) is snel en direct omkeerbaar; een registrar-overdracht duurt meerdere dagen en kent vaak verplichte wachttijden. Zet eerst de DNS om, bevestig dat alles stabiel functioneert, en verhuis pas daarna de registratie.

### Wat moet ik direct na de DNS-omzetting controleren?

Controleer de `www`- en hoofddomeinversie, de geldigheid van het SSL-certificaat, een succesvolle inlogpoging, een testbetaling met webhook-registratie, het ontvangen én verzenden van een geauthenticeerde e-mail, en controleer of achtergrondtaken nog foutloos draaien.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Hoe voorkom ik downtime tijdens het verhuizen van een domeinnaam?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Verlaag TTL-waarden dagen vooraf, test de nieuwe omgeving op een tijdelijk adres, neem alle records vooraf over en schakel om op een rustige ochtend."
      }
    },
    {
      "@type": "Question",
      "name": "Waarom stopt zakelijke e-mail vaak met werken na een DNS-wijziging?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Mailrecords (MX, SPF, DKIM) staan los van websiterecords. Zonder deze exact over te zetten worden inkomende e-mails per direct geweigerd."
      }
    },
    {
      "@type": "Question",
      "name": "Waarom kan niemand meer inloggen direct na de overstap?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "De authenticatie-dienst heeft nog de oude Callback URL. Registreer het nieuwe adres vooraf naast het oude adres in het beheerderspaneel."
      }
    },
    {
      "@type": "Question",
      "name": "Moet ik de registrar-transfer tegelijkertijd met de DNS-omzetting uitvoeren?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Nee. DNS-wijzigingen zijn snel en omkeerbaar, terwijl registrar-transfers dagen duren. Voer ze altijd als twee losse fasen uit."
      }
    },
    {
      "@type": "Question",
      "name": "Wat moet ik direct na de DNS-omzetting controleren?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Domeinvarianten, SSL-certificaten, logins, testbetalingen met webhook-events, e-mailverzending en -ontvangst, en geplande achtergrondtaken."
      }
    }
  ]
}
</script>
