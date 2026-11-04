---
Titel: "Kan Ik een SaaS Verkopen die met Lovable Is Gebouwd? Wat Kopers Controleren"
Trefwoorden: saas verkopen gebouwd met lovable, overname ai-gebouwde saas, saas due diligence ai-code, exit ai-startup, LaunchStudio, Manifera
Koperfase: Overweging
Doelgroep: SaaS-Oprichter Scale-Up
---

# Kan Ik een SaaS Verkopen die met Lovable Is Gebouwd? Wat Kopers Controleren

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Kan Ik een SaaS Verkopen die met Lovable Is Gebouwd? Wat Kopers Controleren",
  "description": "Ja, AI-gebouwde SaaS-producten worden gekocht en verkocht. Deze gids legt uit wat overnemende partijen controleren bij de technische due diligence van een Lovable- of Bolt-app, welke rode vlaggen de prijs verlagen en hoe u zich in de maanden vóór een verkoop voorbereidt.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-03-03",
  "inLanguage": "nl-NL",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/can-i-sell-a-saas-built-with-lovable" },
  "citation": [
    { "@type": "CreativeWork", "name": "Veracode 2025 GenAI Code Security Report", "url": "https://www.veracode.com/resources/analyst-reports/2025-genai-code-security-report/" },
    { "@type": "CreativeWork", "name": "GDPR Article 83: Fines", "url": "https://gdpr-info.eu/art-83-gdpr/" },
    { "@type": "CreativeWork", "name": "GDPR Article 28: Processor", "url": "https://gdpr-info.eu/art-28-gdpr/" },
    { "@type": "CreativeWork", "name": "Acquire.com", "url": "https://acquire.com/" },
    { "@type": "CreativeWork", "name": "OWASP Top 10 2021: A01 Broken Access Control", "url": "https://owasp.org/Top10/A01_2021-Broken_Access_Control/" }
  ]
}
</script>

**Kort antwoord:** ja. Kopers vinden omzet, klanten en overdraagbaarheid veel belangrijker dan welke tool de code heeft geschreven. Maar de technische due diligence controleert of de code van u is en kan worden overgedragen, of klantgegevens veilig en conform worden verwerkt, of de app onafhankelijk van persoonlijke accounts draait, en of iemand anders dan u hem kan beheren. AI-gebouwde apps hebben precies daar vaak gaten, en gaten verlagen de prijs of vertragen de deal.

## Belangrijkste Punten

- **AI-gebouwde SaaS-producten worden gekocht en verkocht;** kopers prijzen risico, niet de tool die de code schreef.
- **Technische due diligence richt zich op eigendom, overdraagbaarheid, beveiliging, gegevensbescherming, beheer, codekwaliteit, afhankelijkheden en kosten.**
- **Gebruikelijke rode vlaggen in AI-gebouwde apps:** accounts op persoonlijke e-mailadressen, gelekte sleutels, te ruime toegangspolicies, ongeteste back-ups, deployment alleen via de builder en ontbrekende AVG-documenten.
- **Drie tot zes maanden voorbereiding** lost de meeste problemen op en beschermt de prijs; zelfs acht gerichte weken kunnen de belangrijkste gaten dichten.
- **Een onafhankelijke samenvatting van een audit in de dataroom** maakt van toezeggingen bewijs.

## Waar Overnemende Partijen Werkelijk naar Kijken

| Gebied | Gestelde vragen |
| --- | --- |
| Eigendom | Wie bezit de code, het domein en de accounts? Problemen met licenties van derden? |
| Overdraagbaarheid | Kan elk account zonder problemen aan de koper worden overgedragen? |
| Beveiliging | Bekende kwetsbaarheden, blootgestelde gegevens, geheimen in de code? |
| Gegevensbescherming | AVG-documentatie, verwerkersovereenkomsten, locatie van gegevens, incidenten |
| Beheer | Hosting, back-ups, monitoring, incidentgeschiedenis, uptime |
| Codekwaliteit | Kan een ontwikkelaar het begrijpen en uitbreiden? Tests? Documentatie? |
| Afhankelijkheden | Afhankelijkheid van specifieke platforms, waaronder de AI-builder |
| Kosten | Maandelijkse kosten voor infrastructuur en API's ten opzichte van de omzet |

## Rode Vlaggen die de Prijs Verlagen

- Accounts op het persoonlijke e-mailadres van de oprichter (domein, Supabase, Stripe, GitHub)
- Geheime sleutels in de geschiedenis van de repository of in de frontend
- Ontbrekende of te ruime Row Level Security op klantgegevens
- Geen back-ups, of back-ups die nooit zijn teruggezet
- App alleen gepubliceerd via de AI-builder, zonder onafhankelijke deployment
- Geen verwerkersovereenkomsten of privacydocumentatie
- Logica die alleen werkt omdat niemand de door prompts gegenereerde bestanden heeft gewijzigd
- AI-API-kosten die sneller groeien dan de omzet

Elk van deze punten wordt een onderhandelingspunt, een escrow, een prijsverlaging of een reden om af te haken.

## Voorbereiden in de Maanden Vóór een Verkoop

1. **Breng het eigendom samen.** Zet elk account in een bedrijfsorganisatie met gedeelde toegang.
2. **Laat een beveiligingsaudit uitvoeren** en los kritieke bevindingen op. Onze [pagina over de audit van AI-gegenereerde code](https://launchstudio.eu/nl/blog/ai-generated-code-audit-what-a-vibe-code-audit-covers) legt uit wat die omvat.
3. **Maak de app onafhankelijk** van de AI-builder: GitHub, uw eigen backend en hosting.
4. **Documenteer het beheer:** overzicht van systemen, register van accounts, deployment, back-ups, bekende beperkingen.
5. **Bereid de AVG-documenten voor:** verwerkingsregister, lijst van verwerkers, locaties van gegevens.
6. **Ruim de kosten op:** ken uw kosten voor infrastructuur en AI-API's per klant.
7. **Verzamel cijfers:** uptime, incidenten, supportvolume, churn.

## Hoe Kopers Kleine SaaS-Bedrijven Waarderen

Kleine SaaS-bedrijven worden meestal gewaardeerd als een veelvoud van de terugkerende omzet of winst, aangepast voor groei, churn, concentratie van klanten en risico. Technisch risico werkt direct door in die aanpassing. Een koper die ontdekt dat klantgegevens kunnen uitlekken, dat het bedrijf afhangt van accounts die persoonlijk op naam van de oprichter staan, of dat niemand anders het product kan beheren, verlaagt het veelvoud, houdt een deel van de prijs in escrow of haakt af. Die risico's wegnemen vóór een verkoop is daarom een van de activiteiten met het hoogste rendement die een oprichter kan ondernemen.

## Het Proces van Due Diligence

Een gangbare overname volgt een vast patroon: eerste interesse en cijfers op hoofdlijnen, een intentieverklaring met een indicatieve prijs, daarna due diligence op financieel, juridisch en technisch vlak, gevolgd door de eindonderhandeling en de overdracht. Technische due diligence omvat vaak:

- Toegang tot de repository voor een codereview
- Een doorloop van de architectuur en infrastructuur
- Beoordeling van beveiligingspraktijken, incidenten en eventuele audits
- Beoordeling van privacydocumentatie en verwerkersovereenkomsten
- Vragen over afhankelijkheid van sleutelpersonen en documentatie
- Beoordeling van infrastructuurkosten en schaalbaarheid

Door vooraf een dataroom met dit materiaal klaar te zetten, verkort u het proces en laat u professionaliteit zien.

## Beveiligingsbewijs dat Kopers Vertrouwen

Kopers willen bewijs, geen verklaringen. Nuttige stukken zijn onder meer een samenvatting van een onafhankelijke code- of beveiligingsaudit met datums en de status van herstel, een beschrijving van toegangscontrole en scheiding tussen klanten, verslagen van hersteltests van back-ups, een incidentenlog (ook als dat leeg is), rapporten over kwetsbaarheden in afhankelijkheden en bewijs van MFA op cruciale accounts. Bij AI-gebouwde producten kunnen kopers specifiek vragen hoe gegenereerde code is beoordeeld; een recente audit is het sterkste antwoord. Onderzoek zoals de bevinding van Veracode uit 2025 dat ongeveer 45% van de onderzochte AI-gegenereerde codevoorbeelden beveiligingsfouten bevatte, heeft kopers alerter gemaakt op deze vraag.

## Privacy en de AVG bij een Verkoop

Een koper erft uw verplichtingen en geschiedenis op het gebied van gegevensbescherming. Reken op vragen over de rechtsgrond voor verwerking, privacyverklaringen, verwerkersovereenkomsten met elke subverwerker, locatie van gegevens, bewaartermijnen, de afhandeling van verzoeken van betrokkenen en eventuele datalekken. Onder de AVG kunnen boetes bij ernstige overtredingen oplopen tot €20 miljoen of 4% van de wereldwijde omzet, dus kopers nemen gaten serieus. Een verwerkingsregister, een lijst van subverwerkers en gedocumenteerde maatregelen die klaarliggen, nemen een grote bron van wrijving weg.

## Het Bedrijf Technisch Overdragen

Bij de afronding moet alles netjes naar de koper gaan: GitHub-organisatie, Supabase-organisatie, hosting, domein, betaalprovider, e-mailprovider, analytics, accounts in app stores en eventuele accounts bij AI-providers. Oefen dit vóór de verkoop in gedachten - of beter, op papier: maak een lijst van elk account, de eigenaar, hoe het eigendom overgaat en welke gegevens of contracten toestemming nodig hebben om mee te verhuizen. Vooral accounts bij betaalproviders kunnen een nieuwe verificatie door de koper vereisen; plan daar tijd voor in.

## Afhankelijkheid van Sleutelpersonen

Veel kleine SaaS-producten zijn afhankelijk van de kennis van de oprichter. Kopers verkleinen dat risico met overgangsperiodes, documentatie en soms earn-outs. U kunt het vóór de verkoop verkleinen met een beheersdocument, een README waarmee een nieuwe ontwikkelaar de app kan draaien en deployen, en een korte opgenomen doorloop van de architectuur. Hoe minder het product van uw geheugen afhangt, hoe sterker uw onderhandelingspositie.

## Voorbereiden Zonder een Verkoop te Verraden

U hoeft geen verkoop aan te kondigen om u erop voor te bereiden. Hetzelfde werk - een beveiligingsaudit, het eigendom samenbrengen, documentatie, onafhankelijkheid van de builder - helpt ook bij fondsenwerving, verkoop aan grote klanten en simpelweg het runnen van een gezonder bedrijf. Veel oprichters doen deze voorbereiding als onderdeel van gewone volwassenwording, wat opties openhoudt zonder iets te veranderen aan wat klanten zien.

## Een Tijdlijn voor de Voorbereiding

| Maanden vóór de verkoop | Focus |
| --- | --- |
| 6 | Onafhankelijke beveiligingsaudit; kritieke en hoge bevindingen oplossen |
| 5 | Alle accounts onder het bedrijf brengen; overal MFA inschakelen |
| 4 | De app onafhankelijk maken van de builder; deployen vanuit GitHub |
| 3 | Beheersdocumentatie schrijven; een doorloop van de architectuur opnemen |
| 2 | AVG-documentatie afronden; ontbrekende verwerkersovereenkomsten tekenen |
| 1 | De dataroom voorbereiden; een laatste hersteltest en een bijgewerkte auditsamenvatting |

Dit in acht weken samenpersen is mogelijk met gerichte hulp, maar zes maanden laten oplossingen lang genoeg in productie draaien om te bewijzen dat ze werken.

## Cijfers die het Technische Verhaal Aanvullen

Kopers combineren de technische beoordeling met bedrijfscijfers: maandelijkse terugkerende omzet, groeitempo, churn, concentratie van klanten, brutomarge en supportdruk. Technisch werk beïnvloedt meerdere daarvan. Lagere kosten voor infrastructuur en AI verhogen de marges; minder incidenten verlagen churn en support. Een verbetering in deze cijfers laten zien na technisch werk versterkt uw verhaal.

## Veelgemaakte Fouten bij een Verkoop

- Pas met technisch opruimen beginnen nadat de beoordeling van de koper is gestart
- Beveiliging of compliance in vroege gesprekken mooier voorstellen dan het is
- Niet weten welke accounts op persoonlijke e-mailadressen staan
- De overdracht van app stores, domeinen of betaalproviders vergeten
- Geen documentatie achterlaten voor de ontwikkelaars van de koper

## De Kern

Een SaaS die met Lovable is gebouwd, kan op normale voorwaarden worden verkocht. Wat kopers nodig hebben, is vertrouwen: dat het product in eigendom is, veilig, conform, gedocumenteerd en overdraagbaar. Bouw dat vertrouwen vóór de verkoop op, en de tool waarmee u bouwde wordt een voetnoot in plaats van een onderhandelingspunt.

## Wat Kopers Zeggen over AI-Gebouwde Producten

Kopers hebben in het algemeen geen bezwaar tegen AI-gegenereerde code als zodanig. De teams van veel kopers gebruiken dagelijks zelf AI-tools. Wat hen zorgen baart, is ongecontroleerde code: producten waarin niemand toegangscontrole, geheimen of de omgang met gegevens heeft gecontroleerd, en waarvan de oprichter niet kan uitleggen hoe het systeem werkt. Een oprichter die een audit, gedocumenteerde architectuur en een helder eigendom kan laten zien, verandert het gesprek van "is dit veilig om te kopen?" naar "hoe snel kunnen we het laten groeien?".

## Adviseurs Kiezen

Bij grotere transacties werken oprichters meestal met een advocaat en soms met een M&A-adviseur of makelaar. Haal technische ondersteuning er vroeg bij: iemand die de technische dataroom kan voorbereiden, de vragen van beoordelaars kan beantwoorden en de punten die ze aankaarten snel kan oplossen. Snel reageren tijdens de due diligence houdt de vaart erin, en vaart beschermt de prijs.

## Vragen om te Beantwoorden Vóór Uw Eerste Gesprek met een Koper

Kan ik elk account opsommen dat het bedrijf gebruikt, en wie de eigenaar van elk account is? Heeft een onafhankelijke partij het afgelopen jaar de code beoordeeld? Kan iemand anders dan ik de app deployen en herstellen? Heb ik verwerkersovereenkomsten voor elke dienst die persoonsgegevens verwerkt? Wat zijn mijn kosten voor infrastructuur en AI per klant? Als u alle vijf met vertrouwen kunt beantwoorden, bent u klaar voor serieuze gesprekken.

## Verder Lezen

Onze gidsen over de audit van AI-gegenereerde code, wat er gebeurt als Lovable verandert of stopt, en bewaartermijnen voor Nederlandse SaaS behandelen de drie gebieden die kopers bij AI-gebouwde producten het nauwkeurigst bekijken.

## Samenvatting

Kopers betalen voor vertrouwen. Geef hen accounts in eigendom, een geaudit en gedocumenteerd product, volledige privacydocumentatie en een helder overdrachtsplan.

## De Vraag over AI Zelf

Sommige kopers vragen hoeveel van de code door AI is gegenereerd. Antwoord eerlijk. Wat hen geruststelt, is niet de afwezigheid van AI, maar bewijs dat de code is beoordeeld, beveiligd, getest en gedocumenteerd, en dat een ontwikkelaar ermee kan werken.

## Klaar voor Due Diligence

LaunchStudio bereidt AI-gebouwde SaaS-producten voor op technische due diligence: audits, het samenbrengen van eigendom, onafhankelijkheid van de builder en documentatie, meestal €3.500-€7.500 tegen vaste prijs. Anders dan freelancers wordt LaunchStudio ondersteund door Manifera, vertrouwd door Vodafone, TNO en CFLW, dat klanten al 11+ jaar begeleidt bij technische beoordelingen vanuit Amsterdam, Singapore en Ho Chi Minh-stad; zie [het portfolio van Manifera](https://www.manifera.com/portfolio/). Voor de zakelijke kant van de verkoop van een kleine SaaS publiceren marktplaatsen zoals [Acquire.com](https://acquire.com/) richtlijnen over de verwachtingen van kopers.

## Praktijkvoorbeeld

### Een AI-Native Oprichter in Actie: De Eventplanning-SaaS die Bijna 30% Verloor

Nicole Verbruggen bouwde Feestdraaiboek in Lovable: een planningstool voor zakelijke evenementenbureaus, met tijdlijnen, leverancierslijsten en goedkeuringen door klanten. Na twee jaar had het 85 bureaus als klant, en een groter bedrijf in eventsoftware deed een bod.

Hun technische due diligence leverde een lijst met zorgen op: het Supabase-project en het Stripe-account stonden op het persoonlijke e-mailadres van Nicole, er stond een service role key in de git-geschiedenis, de RLS op de tabel `suppliers` liet elk bureau de leverancierscontacten van alle andere bureaus lezen, er waren geen verwerkersovereenkomsten vastgelegd, en niemand behalve Nicole had de app ooit gedeployd. De koper stelde een prijsverlaging van 30% voor of een escrow van zes maanden.

Nicole vroeg om acht weken. LaunchStudio bracht alle accounts onder het bedrijf, roteerde sleutels en schoonde de geschiedenis op, herstelde de RLS op alle tabellen, liet verwerkersovereenkomsten tekenen en documenteerde ze, richtte deployment vanuit GitHub met staging in, voerde een hersteltest uit en schreef een beheersdocument. Een onafhankelijke samenvatting van de audit werd aan de dataroom toegevoegd.

**Resultaat:** De vervolgbeoordeling van de koper sloot elk punt af. De deal werd afgerond tegen de oorspronkelijke prijs, met een standaardovergangsperiode van twee maanden.

> *"Het kon de koper niet schelen dat AI de code had geschreven. Het ging hen erom dat ik niet kon bewijzen dat iemand het had gecontroleerd."*
> - **Nicole Verbruggen, Oprichter, Feestdraaiboek (Amsterdam)**

**Kosten & Doorlooptijd:** €6.900 (samenbrengen van accounts, roteren van sleutels, RLS-herstel, documentatie van verwerkers, deploymentpipeline, hersteltest, auditsamenvatting en beheersdocument) - afgerond in 18 werkdagen.

## Veelgestelde Vragen

### Betalen kopers minder voor AI-gebouwde SaaS-producten?

Niet vanzelf. Kopers prijzen risico. Een AI-gebouwd product met helder eigendom, goede beveiliging, documentatie en onafhankelijkheid van de builder kan op normale voorwaarden worden verkocht. Gaten op die gebieden leiden tot prijsverlagingen of escrows, ongeacht hoe de code is geschreven.

### Wat is de grootste technische rode vlag bij due diligence?

Blootstelling van klantgegevens, zoals ontbrekende Row Level Security of gelekte geheime sleutels, is meestal het ernstigst. Accounts die aan persoonlijke e-mailadressen zijn gekoppeld en het ontbreken van back-ups volgen op korte afstand, omdat ze de overdraagbaarheid en continuïteit raken.

### Hoe lang moet ik me voorbereiden op een verkoop?

Bij voorkeur drie tot zes maanden, zodat oplossingen klaar zijn en al een tijd draaien. Zelfs acht weken gericht werk kan de meeste technische problemen oplossen als u begint vóór de beoordeling door de koper.

### Hoe helpt Manifera oprichters bij technische due diligence?

Manifera bereidt al 11+ jaar systemen voor op audits en beoordelingen door klanten. LaunchStudio past die ervaring toe: oplossen wat beoordelaars controleren, het documenteren en een onafhankelijke auditsamenvatting leveren voor de dataroom.

### Beïnvloedt een nette technische opzet hoe mijn product online wordt gezien?

Ja. Een product met een stabiel domein, geen incidenten en duidelijke openbare documentatie verdient vertrouwenssignalen die kopers, klanten en AI-assistenten allemaal oppikken. Incidenten en storingen worden daarentegen vaak gevonden en aangehaald.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "inLanguage": "nl-NL",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Betalen kopers minder voor AI-gebouwde SaaS-producten?",
      "acceptedAnswer": { "@type": "Answer", "text": "Niet vanzelf; kopers prijzen risico. Helder eigendom, beveiliging, documentatie en onafhankelijkheid maken normale voorwaarden mogelijk." }
    },
    {
      "@type": "Question",
      "name": "Wat is de grootste technische rode vlag bij due diligence?",
      "acceptedAnswer": { "@type": "Answer", "text": "Blootstelling van klantgegevens zoals ontbrekende RLS of gelekte sleutels, gevolgd door accounts op persoonlijke e-mailadressen en ontbrekende back-ups." }
    },
    {
      "@type": "Question",
      "name": "Hoe lang moet ik me voorbereiden op een verkoop?",
      "acceptedAnswer": { "@type": "Answer", "text": "Bij voorkeur drie tot zes maanden; acht gerichte weken lossen de meeste problemen op als u vóór de beoordeling begint." }
    },
    {
      "@type": "Question",
      "name": "Hoe helpt Manifera oprichters bij technische due diligence?",
      "acceptedAnswer": { "@type": "Answer", "text": "Door op te lossen wat beoordelaars controleren, dat te documenteren en een onafhankelijke auditsamenvatting te leveren, op basis van 11+ jaar klantbeoordelingen." }
    },
    {
      "@type": "Question",
      "name": "Beïnvloedt een nette technische opzet hoe mijn product online wordt gezien?",
      "acceptedAnswer": { "@type": "Answer", "text": "Ja. Stabiliteit en geen incidenten bouwen vertrouwenssignalen op, terwijl incidenten vaak worden gevonden en aangehaald." }
    }
  ]
}
</script>
