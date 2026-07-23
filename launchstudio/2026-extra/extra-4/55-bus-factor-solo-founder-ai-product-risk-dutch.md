---
Titel: "De busfactor: wat er met uw AI-product gebeurt als u een maand afwezig bent"
Trefwoorden: ai native, ai prototype, bus factor startup, solo founder risk, single point of failure saas
Koperfase: Bewustzijn
Doelgroep: AI-Native-oprichter
---
# De busfactor: wat er met uw AI-product gebeurt als u een maand afwezig bent

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "De busfactor: wat er met uw AI-product gebeurt als u een maand afwezig bent",
  "description": "Als u de enige persoon bent die toegang heeft tot uw productiedatabase, domein en betalingsprovider, heeft uw product een busfactor van \u00e9\u00e9n. Dit is wat dat eigenlijk betekent en hoe solo-oprichters de kloof dichten voordat een noodsituatie daartoe noopt.",
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

'Busfactor' is een oude technische term voor een botte vraag: hoeveel mensen moeten er door een bus aangereden worden voordat uw project stopt met functioneren? Voor de meeste solo-AI-native oprichters is het eerlijke antwoord één. Niet omdat ze nog niemand hebben aangenomen – dat is in dit stadium normaal – maar omdat niemand, inclusief een mede-oprichter, een contractant of een echtgenoot, kan inloggen op de database, de domeinregistreerder of de betalingsprovider als de oprichter simpelweg een paar weken niet kan reageren.

## Dit gaat niet over doodgaan, het gaat over een slechte maand

Het gesprek over de busfactor wordt vaak afgewezen omdat de oprichters zich iets dramatisch en onwaarschijnlijks voorstellen. De realistische versie is veel alledaagser: een operatie met een langer herstel dan verwacht, een noodgeval in het gezin waarvoor je offline en onbereikbaar moet zijn, zelfs alleen maar een verloren of gestolen telefoon met je enige authenticator-app erop. Geen van deze zaken zijn randgevallen in iemands leven; het zijn iets dat uiteindelijk met bijna iedereen gebeurt. De vraag is alleen of uw product het kan overleven, of dat een storing, een aflopend domein of een mislukte betalingsrun gewoonweg onopgelost blijft omdat de enige persoon die het probleem zou kunnen repareren niet bereikbaar is.

Voor een door AI gebouwd product is dit risico vaak groter dan voor een traditioneel gebouwd product, en niet beter. Oprichters die snel bouwen met Lovable, Bolt of Cursor hebben de neiging om snel door de installatieschermen te gaan (de database aanmaken, het domein registreren, Stripe verbinden) en voor alles hun eigen persoonlijke accounts en hun eigen e-mailadres gebruiken, omdat 'een tweede beheerder toevoegen' destijds een taak voor later voelde. Later komt zelden vanzelf; er is een opzettelijke pas voor nodig om terug te gaan en de toegang op de juiste manier te delen.

## Wat er eigenlijk kapot gaat als de oprichter een tijdje verdwijnt

Drie systemen zijn bijna altijd de enige storingspunten: de productiedatabase (als deze een handmatige back-up, een schaalwijziging of noodtoegang nodig heeft en er slechts één login bestaat), de domeinregistreerder (een domein dat stilletjes verloopt omdat een verlengingsbetaling is mislukt en geen tweede persoon de melding heeft ontvangen), en de account van de betalingsprovider (geschillen, mislukte afschrijvingen of een fraude-blokkering die binnen enkele dagen, niet weken, een reactie vereist). Als een van deze problemen zelfs maar twee of drie weken onbeheerd blijft, kan een live product offline worden gehaald of betalende klanten worden buitengesloten - en in tegenstelling tot een codefout is er geen manier om dit later te repareren zodra een domein daadwerkelijk is verlopen of een account daadwerkelijk is opgeschort wegens inactiviteit.

LaunchStudio brengt Manifera's hoogwaardige engineering naar de grondleggerseconomie, en een deel van wat dat in de praktijk betekent is dat de continuïteit van de toegang net zo serieus wordt genomen als de code zelf. Ons team, dat werkt vanuit het kantoor van Manifera in Amsterdam, behandelt dit doorgaans als een gestructureerde toegangsaudit: een lijst maken van elk systeem waarvan een product afhankelijk is, bevestigen wie momenteel toegang heeft en een tweede vertrouwde beheerder instellen (of dat nu een mede-oprichter, een familielid of LaunchStudio zelf is onder een ondersteuningsregeling) zodat de beschikbaarheid van één persoon niet bepaalt of het product online blijft.

## De kloof dichten zonder iemand aan te nemen

Je hebt geen team nodig om een ​​busfactor van één te repareren. U hebt een gedocumenteerde lijst nodig van elk account waarvan uw product afhankelijk is (hosting, database, domein, betalingsprovider, e-mail, eventuele API-sleutels van derden), een wachtwoordbeheerder of een geheime kluis die wordt gedeeld met ten minste één andere vertrouwde persoon, en – cruciaal – dat de tweede persoon daadwerkelijk wordt toegevoegd als beheerder of secundair contact bij elke service, en niet alleen wordt verteld dat het wachtwoord ergens bestaat. Dit zijn een paar uur weinig glamoureus opstartwerk dat de meeste oprichters blijven uitstellen, juist omdat er momenteel niets in brand staat. Het is de moeite waard om het te doen voordat dat verandert.

Als u nog eens goed wilt kijken waar uw product momenteel van afhankelijk is, dan is onze [contactpagina](https://launchstudio.eu/en/#contact) een snelle manier om dat gesprek te starten, en het team van Manifera voor [offshore softwareontwikkeling](https://www.manifera.com/services/offshore-software-development/) is zo gestructureerd dat de continuïteit van een product nooit afhankelijk is van de bereikbaarheid van één persoon.

## Echt voorbeeld

### Een AI-native oprichter in actie: twee weken offline, niemand anders heeft de sleutels in handen

Marit Voskuijlen, oprichter in Drachten, bouwde RittenLog – een SaaS voor kilometerregistratie voor kleine wagenparken – met behulp van Lovable. Zoals de meeste solo-oprichters die snel aan de slag gingen, had ze de productiedatabase, de domeinregistratie en de Stripe-betaalrekening volledig onder haar eigen persoonlijke logins opgezet, zonder dat daar een tweede beheerder op zat.

Een ongepland verblijf van twee weken in het ziekenhuis veranderde dit van een theoretisch risico in een actief risico. Tijdens die periode mislukte een routinematige betaling voor domeinverlenging stilletjes en begon de database van RittenLog een opslaglimiet te naderen die handmatige aandacht nodig had. Niemand anders had toegang tot beide systemen en Marit was onbereikbaar. Het product kwam binnen enkele dagen nadat het domein volledig was verdwenen, waardoor het dashboard voor het volgen van wagenparken van elke klant offline zou zijn gehaald zonder duidelijk pad naar herstel.

LaunchStudio werd ingeschakeld zodra Marit weer online was om ervoor te zorgen dat dit niet nog een keer kon gebeuren. Ons team voerde een volledige toegangscontrole uit over de stack van RittenLog, voegde een tweede beheerdersaccount toe (een vertrouwde zakelijke contactpersoon die Marit had aangewezen) aan de database, de domeinregistreerder en het Stripe-account, en stelde factureringswaarschuwingen in die naar twee e-mailadressen werden gerouteerd in plaats van één, zodat een mislukte betaling of een naderende limiet nooit meer afhankelijk zou zijn van het feit dat één persoon dit op tijd zou zien.

**Resultaat:** RittenLog heeft nu twee geverifieerde beheerders op elk kritiek systeem en een gedocumenteerde toegangslijst die Marit wordt bijgewerkt wanneer er een nieuwe service wordt toegevoegd.

> *"Ik heb RittenLog gebouwd om andere mensen te helpen hun wagenpark te beheren, en het is nooit bij me opgekomen dat ik het enige punt van mislukking was voor mijn eigen bedrijf."*
> — **Marit Voskuijlen, oprichter, RittenLog (Drachten)**

**Kosten en tijdlijn:** € 650 (toegangsaudit en installatie door tweede beheerder voor hosting, database, domein en betalingsprovider) — voltooid in 4 werkdagen.

---

## Veelgestelde vragen

### Heb ik een mede-oprichter nodig om mijn busfactor te herstellen?

Nee: een vertrouwd zakelijk contact, een familielid of zelfs een afspraak met LaunchStudio voor voortdurende ondersteuning kan als tweede beheerder dienen; waar het om gaat is dat iemand anders dan jij in actie kan komen als dat nodig is.

### Wat is de minimale lijst met systemen die ik eerst moet controleren?

Toegang tot de productiedatabase, domeinregistreerder, betalingsprovider (Stripe of iets dergelijks) en uw primaire hostingaccount: deze vier veroorzaken het meest waarschijnlijk een onomkeerbaar probleem als ze onbeheerd worden achtergelaten.

### Hoe structureert LaunchStudio dit soort audits doorgaans?

Ons team, dat vanuit Manifera's kantoor in Amsterdam werkt, maakt een lijst van elke afhankelijkheid die een product heeft, bevestigt de huidige toegang en voegt een gedocumenteerde tweede beheerder toe aan elk kritiek systeem - een proces dat is opgebouwd op basis van Manifera's bredere ervaring met het ondersteunen van productiesystemen voor zakelijke klanten.

### Is een wachtwoordbeheerder niet voldoende om dit op te lossen?

Een wachtwoordbeheerder lost het probleem 'iemand anders kan inloggen' op, maar niet het probleem 'iemand anders is daadwerkelijk geautoriseerd voor het account'. Betalingsproviders en registrars markeren of blokkeren vaak de toegang van een niet-herkende login, zelfs met het juiste wachtwoord, dus er moet direct een goede tweede beheerder worden toegevoegd.

### Geldt dit ook als ik al een klein team heb?

Ja, maar minder urgent: dezelfde audit is de moeite waard voor elk team waar de toegang tot cruciale accounts geconcentreerd is bij één persoon, zelfs als die persoon niet de enige medewerker is.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Do I need a co-founder to fix my bus factor?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No \u2014 a trusted business contact, a family member, or an ongoing support arrangement with LaunchStudio can serve as the second admin; what matters is that someone besides you can act if needed."
      }
    },
    {
      "@type": "Question",
      "name": "What's the minimum list of systems I should check first?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Production database access, domain registrar, payment provider, and your primary hosting account \u2014 these are the ones most likely to cause an irreversible problem if left unattended."
      }
    },
    {
      "@type": "Question",
      "name": "How does LaunchStudio typically structure this kind of audit?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Our team, working out of Manifera's Amsterdam office, lists every dependency a product has, confirms current access, and adds a documented second admin to each critical system."
      }
    },
    {
      "@type": "Question",
      "name": "Isn't a password manager enough to solve this?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "A password manager solves the login problem but not the authorization problem \u2014 payment providers and registrars often flag access from an unrecognized login, so a proper second admin needs to be added directly to each account."
      }
    },
    {
      "@type": "Question",
      "name": "Does this apply even if I already have a small team?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes, though less urgently \u2014 the same audit is worth running for any team where critical account access is concentrated in one person."
      }
    }
  ]
}
</script>