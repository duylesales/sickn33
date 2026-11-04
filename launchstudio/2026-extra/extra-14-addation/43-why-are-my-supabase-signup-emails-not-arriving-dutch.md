---
Titel: "Waarom Komen de Registratiemails van Mijn Supabase-App Niet Aan?"
Trefwoorden: supabase e-mails komen niet aan, supabase smtp, lovable bevestigingsmail, supabase limiet auth-e-mail, LaunchStudio, Manifera
Koperfase: Bewustwording
Doelgroep: Technische Solo-Oprichter / Indie Hacker
---

# Waarom Komen de Registratiemails van Mijn Supabase-App Niet Aan?

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Waarom Komen de Registratiemails van Mijn Supabase-App Niet Aan?",
  "description": "De ingebouwde e-maildienst van Supabase is bedoeld voor ontwikkeling, met strenge verzendlimieten. Dit artikel legt uit waarom bevestigings- en herstelmails na de lancering niet meer aankomen en hoe u dat oplost met eigen SMTP, authenticatie van uw domein en betere sjablonen.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-02-20",
  "inLanguage": "nl-NL",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/why-are-my-supabase-signup-emails-not-arriving" },
  "citation": [
    { "@type": "CreativeWork", "name": "Supabase: Custom SMTP", "url": "https://supabase.com/docs/guides/auth/auth-smtp" },
    { "@type": "CreativeWork", "name": "Supabase: Redirect URLs", "url": "https://supabase.com/docs/guides/auth/redirect-urls" },
    { "@type": "CreativeWork", "name": "Google: Email sender guidelines", "url": "https://support.google.com/a/answer/81126" },
    { "@type": "CreativeWork", "name": "GDPR Article 28: Processor", "url": "https://gdpr-info.eu/art-28-gdpr/" }
  ]
}
</script>

**Kort antwoord:** waarschijnlijk omdat uw app nog de ingebouwde e-maildienst van Supabase gebruikt, die bedoeld is voor ontwikkeling en testen en strenge verzendlimieten heeft. Zodra echte gebruikers zich registreren, worden bevestigings-, magic link- en herstelmails beperkt, vertraagd of komen ze in de spam terecht. De oplossing is een eigen SMTP-provider instellen, uw verzenddomein authenticeren met SPF, DKIM en DMARC, en versturen vanaf een adres op uw eigen domein.

## Belangrijkste Punten

- **De ingebouwde e-maildienst van Supabase is bedoeld voor ontwikkeling** en heeft strenge verzendlimieten; productie-apps horen een eigen SMTP in te stellen.
- **Authenticeer uw verzenddomein met SPF, DKIM en DMARC.** Grote mailboxproviders, waaronder Google en Yahoo, hebben hun eisen voor bulkverzenders aangescherpt, en niet-geauthenticeerde mail komt steeds vaker in de spam terecht.
- **Verkeerde redirect-URL's maken geldige e-mails nutteloos,** omdat ze gebruikers naar previewdomeinen of kapotte pagina's sturen.
- **Linkscanners van bedrijven kunnen magic links verbruiken** voordat gebruikers erop klikken; eenmalige codes voorkomen dat.
- **Herkenbare, duidelijke sjablonen verbeteren zowel de bezorgbaarheid als het vertrouwen,** en Nederlandse gebruikers horen Nederlandse sjablonen te ontvangen.

## De Vier Gangbare Oorzaken

| Oorzaak | Symptoom | Oplossing |
| --- | --- | --- |
| Limieten van de ingebouwde e-mail | De eerste paar registraties werken, daarna stoppen de e-mails | Eigen SMTP-provider |
| Niet-geauthenticeerd domein | E-mails komen in de spam of helemaal niet aan | SPF-, DKIM- en DMARC-records |
| Verkeerde redirect-URL's | De e-mail komt aan, maar de link opent de preview of geeft een fout | Site-URL en redirectlijst in Supabase |
| Linkscanners | Links zijn "al gebruikt" als gebruikers erop klikken | Gebruik OTP-codes of bevestigingspagina's die een klik vragen |

## Stap 1: Stel Eigen SMTP In

Schakel in de Auth-instellingen van Supabase eigen SMTP in en voer de host, poort, gebruikersnaam en het wachtwoord in van een provider voor transactionele e-mail, zoals Postmark, Resend, Mailgun of Amazon SES. Kies een provider met opties voor verwerking in de EU als uw gebruikers in Europa zitten, en voeg hem toe aan uw lijst van verwerkers.

## Stap 2: Authenticeer Uw Domein

Uw provider vraagt u DNS-records toe te voegen:

- **SPF** vermeldt welke diensten e-mail mogen versturen namens uw domein
- **DKIM** ondertekent berichten, zodat ontvangers ze kunnen verifiëren
- **DMARC** vertelt ontvangers wat ze moeten doen met berichten die de controles niet doorstaan

Zonder deze records weigeren Gmail, Outlook en zakelijke filters uw e-mails steeds vaker of zetten ze ze in de spam. Gebruik een afzenderadres zoals `hallo@uwdomein.nl`, nooit een gratis e-mailadres.

## Stap 3: Repareer Redirects

Links voor bevestiging en herstel wijzen naar de site-URL en de toegestane redirect-URL's in Supabase. Als die nog naar de preview van Lovable of Bolt verwijzen, klikken gebruikers op een geldige e-mail en komen ze in de verkeerde app terecht. Werk ze bij voor productie.

## Stap 4: Ga om met Linkscanners

Sommige zakelijke e-mailsystemen openen elke link om hem te scannen, waardoor eenmalige magic links kunnen worden verbruikt voordat de gebruiker erop klikt. Opties: stuur een eenmalige code in plaats van een link, of laat de e-mail wijzen naar een pagina in uw app waar de gebruiker op een knop drukt om te bevestigen.

## Stap 5: Verbeter de Sjablonen

Met Supabase kunt u de sjablonen van authenticatiemails bewerken. Gebruik de naam van uw product, een duidelijke onderwerpregel, gewone taal en uw huisstijl. Algemene sjablonen lijken op phishing, wat zowel de bezorgbaarheid als het vertrouwen schaadt. Bied Nederlandse gebruikers Nederlandse sjablonen.

## Snelle Diagnose

1. Controleer de Auth-logs van Supabase: werd de e-mail verstuurd of beperkt?
2. Controleer het activiteitenlog van uw SMTP-provider: bezorgd, teruggestuurd of geblokkeerd?
3. Controleer een testinbox bij Gmail en Outlook: inbox, spam of ontbrekend?
4. Klik op de link: opent hij het juiste domein?

## Waarom de Bezorgbaarheid van E-mail Strenger Is Geworden

Mailboxproviders bestrijden spam door te controleren of een afzender is wie hij zegt te zijn. Drie standaarden op basis van DNS doen dat werk: SPF vermeldt de servers die namens uw domein mail mogen versturen, DKIM voegt een cryptografische handtekening toe aan elk bericht, en DMARC vertelt ontvangende servers hoe ze berichten moeten behandelen die die controles niet doorstaan en waar ze rapporten naartoe moeten sturen. De afgelopen jaren kondigden Google en Yahoo strengere eisen aan voor verzenders, waaronder authenticatie en eenvoudig afmelden bij bulkmail. Transactionele e-mails zoals bevestigingen en wachtwoordherstel hebben baat bij dezelfde authenticatie, omdat providers de reputatie van uw domein als geheel beoordelen.

## Een Provider voor Transactionele E-mail Kiezen

Let bij het kiezen van een provider voor authenticatie- en producte-mails op deze eigenschappen:

| Eigenschap | Waarom het belangrijk is |
| --- | --- |
| Aparte stromen voor transactionele en marketingmail | Klachten over marketing schaden de bezorging van wachtwoordherstel niet |
| Opties voor verwerking in de EU | Eenvoudigere AVG-documentatie voor Europese gebruikers |
| Duidelijke bezorglogs | U kunt in seconden beantwoorden of uw e-mail is aangekomen |
| Afhandeling van bounces en klachten | Beschermt uw afzenderreputatie automatisch |
| Toegang via SMTP en API | SMTP voor Supabase Auth, API voor uw eigen e-mails |

Teken de verwerkersovereenkomst van de provider en neem hem op in uw privacydocumentatie; hij verwerkt namen en e-mailadressen.

## DNS-Records Instellen Zonder Iets te Breken

Uw e-mailprovider geeft u de exacte records om toe te voegen. Praktische tips:

- **Eén SPF-record per domein.** Meerdere SPF-records maken elkaar ongeldig; voeg ze samen tot één.
- **Gebruik een subdomein om te versturen,** zoals `mail.uwdomein.nl`, als uw hoofddomein al mail verstuurt via andere diensten.
- **Begin DMARC in monitoringmodus** (`p=none`) om rapporten te verzamelen, en scherp daarna aan naar quarantine of reject zodra alles slaagt.
- **Geef DNS tijd om door te voeren** voordat u test, doorgaans minuten tot enkele uren.

## Sjablonen die Werken

Goede authenticatiemails volgen een patroon: een duidelijke onderwerpregel zoals "Bevestig uw account bij UwApp", de productnaam en het logo, één opvallende knop of code, een korte uitleg waarom de gebruiker de e-mail ontving en wat hij moet doen als hij er niet om vroeg, en een platte-tekstversie. Vermijd verkorte links, grote afbeeldingen en formuleringen die spamfilters activeren. Stuur in meertalige apps elke gebruiker het sjabloon in zijn voorkeurstaal.

## De Bezorging Monitoren

Wacht niet tot gebruikers ontbrekende e-mails melden. Houd het dashboard van uw provider in de gaten voor bouncepercentages, spamklachten en geblokkeerde berichten. Stel een melding in als er bij normaal gebruik een uur lang geen bevestigingsmails worden verstuurd. Een plotselinge daling in het aantal afgeronde registraties is vaak het eerste zichtbare teken van een e-mailprobleem.

## Verder dan Authenticatie: Producte-mails

Zodra SMTP is ingericht voor authenticatie, wilt u ook andere e-mails: ontvangstbewijzen, meldingen, herinneringen. Verstuur die vanuit functies op de server via de API van uw provider, nooit vanuit de browser met een zichtbare sleutel. Houd transactionele en marketinge-mails gescheiden, en geef marketinge-mails een afmeldlink en een grondslag voor toestemming onder de AVG en de e-privacyregels.

## Veelgemaakte Fouten

- Versturen vanaf een gratis e-mailadres in plaats van uw eigen domein
- Een tweede SPF-record toevoegen in plaats van samen te voegen
- Vergeten de redirect-URL's bij te werken na de overstap naar een eigen domein
- Dezelfde stroom van de provider gebruiken voor nieuwsbrieven en wachtwoordherstel
- De bezorglogs nooit bekijken tot een klant klaagt

## Een Stapsgewijze Oplossing in Minder dan een Uur

Voor een gangbare Lovable- of Bolt-app met onbetrouwbare authenticatiemails volgt de oplossing een vaste volgorde:

1. **Maak een account aan** bij een provider voor transactionele e-mail en voeg uw verzenddomein toe.
2. **Voeg de DNS-records toe** die de provider u geeft voor SPF, DKIM en, als dat er nog niet is, een DMARC-record in monitoringmodus.
3. **Wacht op de verificatie** en kopieer daarna de SMTP-host, poort, gebruikersnaam en het wachtwoord.
4. **Schakel eigen SMTP in bij Supabase Auth,** stel het afzenderadres op uw eigen domein in en een herkenbare afzendernaam.
5. **Werk de site-URL en de lijst met toegestane redirects bij** naar uw productiedomein.
6. **Bewerk de sjablonen** voor bevestiging, magic link, wachtwoordherstel en wijziging van e-mailadres.
7. **Verstuur testmails** naar Gmail, Outlook en een zakelijk adres, en controleer waar ze in de inbox terechtkomen.
8. **Controleer de Auth-logs van Supabase en de logs van de provider** om te bevestigen dat beide kanten de verzending hebben vastgelegd.

De meeste oprichters ronden deze stappen in minder dan een uur af, met een korte wachttijd voor DNS.

## Limieten en Misbruik

Eigen SMTP haalt de ontwikkellimieten van Supabase weg, maar haalt ook een vangnet weg. Bots die uw registratieformulier bestoken, kunnen nu duizenden bevestigingsmails vanaf uw domein versturen, wat de reputatie ervan schaadt. Bescherm registratie en wachtwoordherstel met CAPTCHA en rate limits, en let op ongebruikelijke pieken in het aantal verzonden mails. Supabase Auth ondersteunt CAPTCHA-providers zoals Cloudflare Turnstile en hCaptcha.

## Wat Gebruikers Zien als het Misgaat

Voor een gebruiker ziet een ontbrekende bevestigingsmail eruit als een kapot product. Velen proberen het opnieuw en maken dubbele accounts aan, en sommigen vertrekken voorgoed. Voeg een duidelijke optie "geen e-mail ontvangen?" toe met een knop om opnieuw te versturen die rate limits respecteert, en toon naar welk adres de e-mail is gestuurd, zodat typefouten makkelijk te zien zijn. Kleine details zoals deze winnen gebruikers terug die anders stil verloren zouden gaan.

## De Bezorgbaarheid Goed Testen

Een testmail naar uw eigen Gmail-account versturen bewijst weinig, omdat providers bekende afzenders anders behandelen. Test met nieuwe adressen bij meerdere providers - Gmail, Outlook, een Nederlandse provider zoals KPN- of Ziggo-mail als die relevant is voor uw doelgroep, en een zakelijk Microsoft 365-account - en controleer of berichten in de inbox, het tabblad Reclame of de spam terechtkomen. In de headers van berichten tonen veel providers de resultaten van de authenticatie; let op "pass" bij SPF, DKIM en DMARC. Herhaal deze tests na elke wijziging aan uw domein, DNS of provider.

## Plannen voor Groei

Naarmate uw gebruikersbestand groeit, groeit het e-mailvolume mee: bevestigingen, herstelmails, meldingen en ontvangstbewijzen. Bekijk de limieten van het abonnement van uw provider, houd bounce- en klachtpercentages in de gaten en verwijder adressen die een harde bounce geven. Gezonde lijsten en geauthenticeerd versturen houden de bezorging op schaal betrouwbaar.

## Snel Overzicht: Symptomen en Oplossingen

| Symptoom | Oplossing |
| --- | --- |
| Eerste registraties werken, latere krijgen geen e-mail | Eigen SMTP instellen |
| E-mails in de spam | SPF, DKIM en DMARC toevoegen; versturen vanaf uw eigen domein |
| Link opent het verkeerde domein | Site-URL en redirectlijst in Supabase bijwerken |
| "Link verlopen" direct na klikken | Eenmalige codes of een pagina met een bevestigingsklik gebruiken |
| Gebruikers kunnen uw e-mail niet van phishing onderscheiden | Herkenbare sjablonen met een duidelijke afzendernaam |

## Houd Uw Configuratie Gedocumenteerd

Leg uw SMTP-provider, verzenddomein, DNS-records en de eigenaren van sjablonen vast in de README van uw repository, zodat wijzigingen aan domeinen of providers registraties nooit stilletjes breken.

## Hulp Inschakelen

De inrichting van e-mail is een standaardonderdeel van lanceringen van LaunchStudio, vaak gecombineerd met herkenbare sjablonen en transactionele e-mails zoals ontvangstbewijzen en meldingen. LaunchStudio wordt ondersteund door Manifera, dat al 11+ jaar de bezorging van e-mail inricht voor systemen van klanten vanuit Amsterdam en Ho Chi Minh City; zie [de over-ons-pagina van Manifera](https://www.manifera.com/about-us/). Supabase documenteert [het instellen van eigen SMTP](https://supabase.com/docs/guides/auth/auth-smtp) uitgebreid. Als u de rest van uw lancering controleert, behandelt onze [auditchecklist van 25 punten](https://launchstudio.eu/nl/blog/vibe-code-audit-checklist-25-checks-before-launch) e-mail naast beveiliging.

## Praktijkvoorbeeld

### Een AI-Native Oprichter in Actie: De Vrijwilligersregistratie Die bij 30 Stilviel

Mirjam Dekkers coördineert een voedselbank in Helmond en bouwde Voedselhulp in Lovable: vrijwilligers melden zich aan voor uitdeeldiensten en ontvangen herinneringen. Op de avond van de lancering ontvingen de eerste 30 of zo vrijwilligers een bevestigingsmail. Daarna niets meer. Vrijwilligers probeerden het opnieuw, maakten dubbele accounts aan en gaven het op.

De app gebruikte de ingebouwde e-mail van Supabase, die zijn verzendlimiet had bereikt. E-mails die wel werden verstuurd, kwamen van een algemeen adres, en meerdere belandden in de spam. Links voor wachtwoordherstel wezen naar het previewdomein van Lovable.

LaunchStudio stelde eigen SMTP in via een provider voor transactionele e-mail in een EU-regio, voegde SPF-, DKIM- en DMARC-records toe aan het domein van de voedselbank, zette productie-redirect-URL's, herschreef de sjablonen in het Nederlands met de naam van de voedselbank, verving magic links door eenmalige codes voor vrijwilligers met een werkadres, en voegde dubbele accounts samen.

**Resultaat:** Alle wachtende vrijwilligers waren de volgende ochtend bevestigd. Binnen een maand stonden 210 vrijwilligers geregistreerd, en herinneringsmails kwamen in de inbox terecht in plaats van in de spam.

> *"Dertig mensen kwamen binnen en toen ging de deur stilletjes dicht. Niemand zag een foutmelding, ik ook niet."*
> - **Mirjam Dekkers, Oprichter, Voedselhulp (Helmond)**

**Kosten & Doorlooptijd:** €850 (Launch Ready-pakket: SMTP, DNS-authenticatie, redirects, Nederlandse sjablonen, OTP en opschonen van accounts) - afgerond in 3 werkdagen.

## Veelgestelde Vragen

### Beperkt Supabase hoeveel authenticatiemails ik kan versturen?

Ja. De ingebouwde e-maildienst is bedoeld voor ontwikkeling en testen en heeft strenge limieten. Voor productie raadt Supabase aan uw eigen SMTP-provider in te stellen, wat die limieten wegneemt en de bezorgbaarheid verbetert.

### Welke SMTP-provider gebruik ik met Supabase?

Elke betrouwbare provider voor transactionele e-mail werkt, zoals Postmark, Resend, Mailgun of Amazon SES. Geef voor Europese gebruikers de voorkeur aan een provider met verwerking in de EU, teken de verwerkersovereenkomst en authenticeer uw domein.

### Waarom zeggen mijn magic links dat ze zijn verlopen of al zijn gebruikt?

Vaak omdat een beveiligingsscanner voor e-mail de link opende voordat de gebruiker dat deed, waardoor hij werd verbruikt. Eenmalige codes, of een bevestigingspagina die een klik vraagt, voorkomen dit.

### Hoe pakt Manifera de bezorgbaarheid van e-mail aan?

Als infrastructuur, niet als bijzaak. De 11+ jaar systemen voor klanten van Manifera omvatten transactionele e-mail op schaal, dus LaunchStudio stelt authenticatierecords, monitoring en sjablonen in als onderdeel van elke lancering die e-mail verstuurt.

### Kan een slechte bezorgbaarheid van e-mail de online reputatie van mijn domein schaden?

Ja. Als uw domein niet-geauthenticeerde of spamachtige e-mail verstuurt, verlagen mailboxproviders de reputatie ervan, wat alle e-mail vanaf dat domein kan raken, ook verkoopmails. Correcte SPF, DKIM en DMARC beschermen die reputatie.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "inLanguage": "nl-NL",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Beperkt Supabase hoeveel authenticatiemails ik kan versturen?",
      "acceptedAnswer": { "@type": "Answer", "text": "Ja. De ingebouwde dienst is voor ontwikkeling met strenge limieten; productie-apps horen eigen SMTP te gebruiken." }
    },
    {
      "@type": "Question",
      "name": "Welke SMTP-provider gebruik ik met Supabase?",
      "acceptedAnswer": { "@type": "Answer", "text": "Een betrouwbare provider voor transactionele e-mail zoals Postmark, Resend, Mailgun of Amazon SES, bij voorkeur met verwerking in de EU en een geauthenticeerd domein." }
    },
    {
      "@type": "Question",
      "name": "Waarom zeggen mijn magic links dat ze zijn verlopen of al zijn gebruikt?",
      "acceptedAnswer": { "@type": "Answer", "text": "Scanners voor e-mail kunnen links als eerste openen. Gebruik eenmalige codes of een bevestigingspagina die een klik vraagt." }
    },
    {
      "@type": "Question",
      "name": "Hoe pakt Manifera de bezorgbaarheid van e-mail aan?",
      "acceptedAnswer": { "@type": "Answer", "text": "Als infrastructuur, met authenticatierecords, monitoring en sjablonen op basis van 11+ jaar systemen voor klanten." }
    },
    {
      "@type": "Question",
      "name": "Kan een slechte bezorgbaarheid van e-mail de online reputatie van mijn domein schaden?",
      "acceptedAnswer": { "@type": "Answer", "text": "Ja. Niet-geauthenticeerde of spamachtige mail verlaagt de reputatie van het domein voor alle e-mail; SPF, DKIM en DMARC beschermen die." }
    }
  ]
}
</script>
