---
Titel: "De Bus Factor: Wat gebeurt er met uw AI-product als u een maand uitgeschakeld bent"
Trefwoorden: ai native, ai prototype, bus factor startup, solo founder risk, single point of failure saas
Koperfase: Bewustzijn
Doelgroep: AI-Native oprichter
---

# De Bus Factor: Wat gebeurt er met uw AI-product als u een maand uitgeschakeld bent

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "De Bus Factor: Wat gebeurt er met uw AI-product als u een maand uitgeschakeld bent",
  "description": "Als u de enige persoon bent met toegang tot uw productiedatabase, domein en betalingsverwerker.",
  "author": {
    "@type": "Organization",
    "name": "LaunchStudio",
    "url": "https://launchstudio.eu/en/"
  },
  "publisher": {
    "@type": "Organization",
    "name": "Manifera",
    "url": "https://www.manifera.com"
  },
  "datePublished": "2026-07-22",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://launchstudio.eu/en/blog/bus-factor-solo-founder-ai-product-risk"
  }
}
</script>

"Bus factor" is een oude engineeringterm voor een botte vraag: hoeveel mensen zouden door een bus geraakt moeten worden voordat uw project stopt met functioneren? Voor de meeste solo AI-native oprichters is het eerlijke antwoord één. Niet omdat ze nog niemand hebben aangenomen – dat is normaal in deze fase – maar omdat niemand, inclusief een mede-oprichter, een leverancier, of een echtgenoot, zou kunnen inloggen op de database, de domeinregistrar, of de betalingsverwerker als de oprichter simpelweg een paar weken niet kan reageren.

## Dit gaat niet over overlijden, het gaat over een slechte maand

Het gesprek over de bus factor heeft de neiging te worden weggewuifd omdat oprichters zich iets dramatisch en onwaarschijnlijks voorstellen. De realistische versie is aanzienlijk alledaagser: een operatie met een langer herstel dan verwacht, een familie-noodgeval dat vereist dat men offline en onbereikbaar is, of zelfs simpelweg een telefoon die verloren of gestolen is met uw enige authenticator-app erop. Geen van deze situaties zijn uitzonderlijke gevallen in het leven van een mens – het is het soort ding dat bijna iedereen uiteindelijk overkomt. De vraag is alleen of uw product het kan overleven, of dat een storing, een verlopend domein, of een mislukte betalingsronde daar simpelweg onopgelost blijft zitten omdat de ene persoon die het kon herstellen niet bereikbaar is.

Voor een met AI gebouwd product is dit risico vaak erger dan voor een traditioneel gebouwd product, en niet beter. Oprichters die snel bouwen met Lovable, Bolt of Cursor hebben de neiging snel door installatieschermen te bewegen – de database aanmaken, het domein registreren, Stripe verbinden – gebruikmakend van hun eigen persoonlijke accounts en hun eigen e-mailadres voor alles. Op dat moment voelde "voeg een tweede beheerder toe" namelijk als een taak voor later. Later komt zelden uit zichzelf. Het vereist een bewuste stap om terug te gaan en toegang op de juiste manier te delen.

## Wat er daadwerkelijk breekt wanneer de oprichter een tijdje verdwijnt

Drie systemen zijn vrijwel altijd de enkele punten van mislukken (single points of failure): de productiedatabase (als het een handmatige back-up, een schaalwijziging, of noodtoegang nodig heeft, en er slechts één inlog bestaat), de domeinregistrar (een domein dat stilletjes verloopt omdat een verlengingsbetaling is mislukt en geen tweede persoon de melding kreeg), en het account van de betalingsverwerker (geschillen, mislukke afschrijvingen, of een fraudeblokkade die binnen dagen een reactie nodig heeft, en niet weken). Elk van deze systemen dat gedurende zelfs twee of drie weken onbeheerd blijft kan een live product offline halen of betalende klanten uitsluiten. In tegenstelling tot een codebug is er geen manier om het "later te herstellen" zodra een domein daadwerkelijk is verlopen of een account daadwerkelijk is geschorst wegens inactiviteit.

LaunchStudio brengt Manifera's enterprise-grade engineering naar de economie van oprichters. Wat dat praktisch betekent is het behandelen van continuïteit van toegang net zo serieus als de code zelf. Ons team, werkend vanuit Manifera's kantoor in Amsterdam, pakt dit doorgaans op als een gestructureerde toegangs-audit: het vermelden van elk systeem waar een product van afhangt, het bevestigen van wie momenteel toegang heeft, en het instellen van een tweede vertrouwde beheerder – of dat nu een mede-oprichter is, een familielid, of LaunchStudio zelf onder een ondersteuningsregeling – zodat geen enkele beschikbaarheid van een enkel persoon bepaalt of het product live blijft.

## De kloof sluiten zonder iemand aan te nemen

U heeft geen team nodig om een bus factor van één te herstellen. U heeft een gedocumenteerde lijst nodig van elk account waar uw product van afhangt (hosting, database, domein, betalingsverwerker, e-mail, eventuele API-sleutels van derden), een wachtwoordbeheerder-invoer of geheim kluisje gedeeld met ten minste één andere vertrouwde persoon, en – cruciaal – dat die tweede persoon daadwerkelijk wordt toegevoegd als een beheerder of secundair contact op elke dienst, en niet simpelweg te horen krijgt dat het wachtwoord ergens bestaat. Dit is een paar uur aan onglamoureus installatiewerk dat de meeste oprichters blijven uitstellen precies omdat er momenteel niets in brand staat. Het is de moeite waard om te doen voordat dat veranderd.

Als u een tweede set ogen wilt op waar uw product momenteel van afhangt, is onze [contactpagina](https://launchstudio.eu/en/#contact) een snelle manier om dat gesprek te starten. En Manifera's team voor [offshore softwareontwikkeling](https://www.manifera.com/services/offshore-software-development/) is specifiek zo gestructureerd dat de continuïteit van een product nooit afhangt van het bereikbaar zijn van één individu.

## Het toevoegen van een tweede beheerder herstelt MFA niet uit zichzelf

Het toevoegen van een tweede beheerder aan uw database, domeinregistrar en betalingsverwerker sluit de meest duidelijke kloof, maar het kan stilletjes een tweede kloof laten zitten: tweefactorauthenticatie (MFA). De meeste diensten laten u met plezier een tweede beheerdersaccount toevoegen terwijl elke risicovolle actie op dat account – een grote uitbetaling, een domeinoverdracht, een ondersteuningsoproep die bewijst dat u de accounteigenaar bent – zijn verificatiestap nog steeds leidt via een telefoonnummer of authenticator-app die alleen de oprichter bezit. De tweede beheerder kan inloggen. Hij kan nog steeds niet handelen, omdat de controle die er het meest toe doet gekoppeld is aan een apparaat dat hij niet heeft.

Dit is gemakkelijk te missen precies omdat het niet naar boven komt wanneer u simpelweg controleert "kan deze persoon inloggen". Het verschijnt tijdens de exacte noodsituatie die de tweede beheerder verondersteld werd te dekken – een uitbetaling heeft goedkeuring nodig, of een fraudeblokkade moet worden opgeheven, en de verificatiecode gaat naar een telefoon waar niemand behalve de onbereikbare oprichter toegang toe heeft. Het op de juiste manier sluiten hiervan betekent het auditeren van MFA per dienst, en niet alleen beheerderstoegang per dienst.

```
Dienst: Stripe (betalingsverwerker)
Primaire beheerder: Oprichter (persoonlijk e-mailadres)
Secundaire beheerder: Toegevoegd — zakenpartner
MFA-methode: Authenticator-app (alleen telefoon oprichter) — ACTIE NODIG
Back-up/herstelcodes: Nog niet opgeslagen in gedeelde kluis — ACTIE NODIG

Dienst: Domeinregistrar
Primaire beheerder: Oprichter
Secundaire beheerder: Toegevoegd
MFA-methode: SMS naar nummer oprichter — ACTIE NODIG
Back-up/herstelcodes: Opgeslagen in gedeelde wachtwoordbeheerder
```

Een eenvoudige inventarisatie zoals deze, uitgevoerd naast de audit voor beheerderstoegang, is wat "iemand anders heeft een inlog" veranderd in "iemand anders kan daadwerkelijk handelen wanneer het er toe doet."

## Echt voorbeeld

### Een AI-native oprichter in actie: Twee weken offline, niemand anders met de sleutels

Marit Voskuijlen, een oprichter in Drachten, bouwde RittenLog – een SaaS voor rittenregistratie voor kleine wagenparken – met behulp van Lovable. Zoals de meeste solo-oprichters die snel bewegen, had ze de productiedatabase, de domeinregistratie en het Stripe-betalingsaccount volledig ingesteld onder haar eigen persoonlijke inlogs, zonder tweede beheerder op een van die diensten.

Een ongeplande ziekenhuisopname van twee weken veranderde dit van een theoretisch risico in een actief risico. Tijdens dat venster mislukte een routineuze verlengingsbetaling voor het domein stilletjes, en RittenLog's database begon een opslaglimiet te naderen die handmatige aandacht nodig had. Niemand anders had toegang tot een van beide systemen, en Marit was onbereikbaar. Het product kwam binnen dagen van het volledig laten verlopen van het domein, wat het dashboard voor rittenregistratie van elke klant offline zou hebben gehaald zonder duidelijk pad naar herstel.

LaunchStudio werd ingeschakeld zodra Marit weer online was om ervoor te zorgen dat dit niet opnieuw kon gebeuren. Ons team voerde een volledige toegangs-audit uit over RittenLog's stack, voegde een tweede beheerdersaccount toe – een vertrouwd zakelijk contact dat Marit aanwees – aan de database, domeinregistrar en het Stripe-account. We stelden facturatie-waarschuwingen in die naar twee e-mailadressen worden geleid in plaats van één. Een mislukte betaling of een naderende limiet hangt zo nooit meer af van het op tijd zien door één persoon.

**Resultaat:** RittenLog heeft nu twee geverifieerde beheerders op elk kritiek systeem, en een gedocumenteerde toegangslijst die Marit bijwerkt wanneer er een nieuwe dienst wordt toegevoegd.

> *"Ik bouwde RittenLog om andere mensen te helpen hun wagenparken te beheren. Het was nooit bij me opgekomen dat ik het enkele punt van mislukken was voor mijn eigen bedrijf."*
> — **Marit Voskuijlen, Oprichter, RittenLog (Drachten)**

**Kosten en tijdlijn:** € 650 (toegangs-audit en instellen van een tweede beheerder over hosting, database, domein en betalingsverwerker) — voltooid in 4 werkdagen.

---

## Veelgestelde vragen

### Heb ik een mede-oprichter nodig om mijn bus factor te herstellen?

Nee – een vertrouwd zakelijk contact, een familielid, of zelfs een regeling met LaunchStudio voor doorlopende ondersteuning kan dienen als de tweede beheerder. Wat er toe doet is dat iemand anders dan u kan handelen indien nodig.

### Wat is de minimale lijst van systemen die ik eerst zou moeten controleren?

Toegang tot de productiedatabase, domeinregistrar, betalingsverwerker (Stripe of gelijkwaardig), en uw primaire hostingaccount. Deze vier veroorzaken de meeste kans op een onomkeerbaar probleem als ze onbeheerd blijven.

### Is een wachtwoordbeheerder niet voldoende om dit op te lossen?

Een wachtwoordbeheerder lost het probleem op dat "iemand anders zou kunnen inloggen", maar niet het probleem dat "iemand anders daadwerkelijk geautoriseerd is op het account". Betalingsverwerkers en registrars markeren of blokkeren vaak de toegang vanaf een onbekende inlog, zelfs met het correcte wachtwoord. Een correcte tweede beheerder moet dus rechtstreeks worden toegevoegd.

### Als ik een tweede beheerder heb toegevoegd, is mijn bus factor-probleem dan daadwerkelijk opgelost?

Niet volledig – veel diensten leiden risicovolle acties zoals grote uitbetalingen of accountherstel nog steeds via de telefoon of authenticator-app van de oorspronkelijke oprichter, zelfs nadat er een tweede beheerder is toegevoegd. De MFA- en herstelmethode op elke dienst heeft dus zijn eigen controle nodig naast de beheerderstoegang zelf.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Wat is de Bus Factor van een solo AI-founder?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Voor de meeste solo founders is de Bus Factor 1: als de founder uitvalt (ziekte, verlies telefoon), kan niemand bij de database, Stripe of het domein."
      }
    },
    {
      "@type": "Question",
      "name": "Welke 4 accounts zijn het meest kritiek bij een Bus Factor audit?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "1. Productie database toelating 2. Domein-registrar (DNS) 3. Payment provider (Stripe) 4. Primaire Cloud/Hosting provider (Vercel, AWS)."
      }
    },
    {
      "@type": "Question",
      "name": "Is een 1Password/Bitwarden kluis delen genoeg voor continuïteit?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Nee! Stripe en domein-registrars blokkeren inlogs vanaf onbekende IP's/apparaten. Je moet een 2e persoon expliciet toevoegen als geautoriseerde team-admin."
      }
    },
    {
      "@type": "Question",
      "name": "Waarom is MFA (2FA) de verborgen valkuil bij noodtoegang?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Omdat uitbetalingen en domein-transfers een SMS/Authenticator code eisen die alleen op de privé-telefoon van de founder binnenkomt. Sla nood-backupcodes op in de kluis."
      }
    },
    {
      "@type": "Question",
      "name": "Wat kost een Bus Factor & Access audit bij LaunchStudio?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Een volledige toegangs-audit en het inrichten van 2e admin/MFA continuïteit kost gemiddeld €650 en duurt 4 werkdagen."
      }
    }
  ]
}
</script>