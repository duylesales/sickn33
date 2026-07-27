---
Titel: "Uw eigen portfolio van 'AI SaaS-producten' auditeren voordat u investeerders pitcht"
Trefwoorden: ai saas products, saas portfolio audit, ai saas due diligence, multi-product saas security
Koperfase: Beslissing
Doelgroep: SaaS-oprichter scale-up
---
# Uw eigen portfolio van 'AI SaaS-producten' auditeren voordat u investeerders pitcht

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Uw eigen portfolio van 'AI SaaS-producten' auditeren voordat u investeerders pitcht",
  "description": "Meerdere AI SaaS-producten onder één bedrijf runnen betekent dat due diligence naar alle producten kijkt, niet alleen naar uw beste. Dit is een raamwerk op oprichtersniveau om uw eigen portfolio eerst te auditeren.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2026-07-27",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/ai-saas-products-portfolio-audit" }
}
</script>

Als u meer dan één AI SaaS-product runt onder één enkel bedrijf, heeft u waarschijnlijk uw best presterende product alle aandacht gegeven: de gepolijste demo, de beveiligingsbeoordeling voordat een grote klant tekende, het monitoringdashboard dat u elke ochtend controleert. Dat is logisch — dat product genereert de omzet. Het probleem is dat due diligence van investeerders uw beste product niet geïsoleerd beoordeelt. Het beoordeelt uw bedrijf, en gedeelde infrastructuur betekent dat een zwakte in uw minst bekeken product als rode vlag naar voren kan komen tegen alle producten, inclusief het product dat u daadwerkelijk pitcht.

Dit is een educatief stuk voor iedere oprichter die een kleine portfolio van door AI gebouwde SaaS-producten runt en die nog niet al zijn producten tegelijk heeft moeten verdedigen tegenover een externe partij. Dit is het raamwerk dat het waard is om te doorlopen voordat de technisch adviseur van een investeerder het voor u doet.

## Waarom een portfolio als systeem wordt beoordeeld, niet als optelsom van onderdelen

Meerdere AI SaaS-producten onder één bedrijf delen vaak standaard infrastructuur, niet door bewust ontwerp — een gemeenschappelijk inlogsysteem, een gedeelde database-instantie, overlappende API-sleutels, of één hostingaccount. Dit delen gebeurt meestal omdat het de weg van de minste weerstand was toen het tweede en derde product snel werden opgezet, hergebruikmakend van wat het eerste product al werkend had. Het is op dat moment een redelijke kortere weg. Het betekent ook dat een beveiligingsgat in de zelden gebruikte inlogflow van Product B, technisch gezien, ook een gat is in de authenticatie van Product A, als ze hetzelfde onderliggende systeem delen.

Due diligence-teams weten dit en zullen er rechtstreeks naar vragen: "delen deze producten infrastructuur, en zo ja, is de gedeelde laag beoordeeld?" Een oprichter die die vraag niet zelfverzekerd kan beantwoorden, signaleert iets ergers dan één enkele bug — het signaleert dat de portfolio niet als systeem is bekeken, wat de vraag oproept wat er verder nog niet is bekeken.

## Het zelfaudit-raamwerk

Voer dit uit voor elk product in uw portfolio, niet alleen het vlaggenschip:

**Inventariseer gedeelde infrastructuur.** Maak een lijst van elk systeem waarvan twee of meer van uw producten gezamenlijk afhankelijk zijn — authenticatie, database, hosting, betalingsverwerking, externe API's. Deze lijst is doorgaans langer dan oprichters verwachten, omdat delen meestal stilletjes gebeurt.

**Controleer wanneer elk product voor het laatst een beveiligingsbeoordeling had.** Niet "is het ooit gebeurd" — wanneer, precies. Een beoordeling van achttien maanden geleden op een codebase die sindsdien aanzienlijk is veranderd, komt neer op bijna geen beoordeling.

**Traceer de impactzone van uw gedeelde systemen.** Vraag voor elk item op uw lijst met gedeelde infrastructuur: als hierin een bekende kwetsbaarheid zou zitten, welke producten zouden dan worden getroffen? Als het antwoord "allemaal" is voor uw inlogsysteem, verdient dat ene systeem prioriteit boven de individuele functies van welk product dan ook.

**Scheid omzetaandacht van risicoaandacht.** Het is logisch om het product dat het meeste geld binnenbrengt het zorgvuldigst te beoordelen. Risico volgt echter geen omzet — een kleiner, minder bekeken product met een gedeeld inlogsysteem kan het toegangspunt zijn dat de hele portfolio compromitteert, ongeacht hoe weinig omzet het zelf genereert.

**Documenteer wat u vindt, ook de gaten.** Investeerders reageren beter op "we hebben dit gat geïdentificeerd en hier is onze remediëringstijdlijn" dan op een gat dat ze zelf vinden tijdens due diligence. Een oprichter die de zwakke punten van de eigen portfolio al kent, komt over als iemand die de zaken onder controle heeft. Een oprichter die verrast wordt door de bevindingen van de eigen technisch adviseur, komt over als het tegenovergestelde.

## Gedeelde-infrastructuurgaten repareren zonder uw funding-ronde te vertragen

Zodra u heeft vastgesteld waar het risico zich daadwerkelijk concentreert, is de oplossing meestal beperkter dan oprichters vrezen — u repareert een gedeeld systeem, niet drie afzonderlijke producten opnieuw bouwen. LaunchStudio brengt Manifera's enterprise-grade engineering, dezelfde standaard gebruikt bij meer dan 160 opgeleverde projecten voor klanten als Vodafone en TNO, naar precies dit soort multi-productbeoordeling. Ons team, werkend vanuit Amsterdam, begint doorgaans met de bovenstaande inventarisatie van gedeelde infrastructuur en prioriteert reparaties op basis van impactzone in plaats van op basis van welk product toevallig het zichtbaarst is. Als u due diligence ingaat en dit wilt laten doen voordat de technisch adviseur van een investeerder het zelfstandig vindt, kunt u [de omvang van een portfoliobrede beoordeling berekenen](https://launchstudio.eu/en/#calculator). De bredere ervaring van Manifera met enterprise-beveiliging en -architectuur staat beschreven in het [portfolio van opgeleverde projecten](https://www.manifera.com/portfolio/).

## Echt voorbeeld

### Een AI-native oprichter in actie: twee producten, één ongepatchte login

Wessel Wassenaar, een oprichter in Wassenaar, runde drie kleine AI SaaS-producten onder één bedrijf. Eén was uitgegroeid tot een oprechte omzetmotor en had een degelijke beveiligingsbeoordeling doorlopen voordat zijn grootste klant tekende. De andere twee waren kleiner, nog steeds winstgevend, maar nooit beoordeeld — en, onbekend bij Wessel tot due diligence begon, deelden ze hun inlogsysteem met elkaar, inclusief een bekende, ongepatchte bug in sessieafhandeling.

Het gat kwam aan het licht tijdens due diligence van een investeerder, toen een technisch adviseur een eenvoudige vraag stelde waar Wessel zich niet op had voorbereid: welke van uw producten delen infrastructuur, en wanneer is de gedeelde laag voor het laatst beoordeeld? Wessel had geen zelfverzekerd antwoord, en de snelle controle van de adviseur vond het sessieafhandelingsprobleem binnen een dag — een bug die, in principe, een sessietoken bedoeld voor het ene product kon laten misbruiken op het andere.

Wessel bracht alle drie de producten onder tijdsdruk naar LaunchStudio, terwijl de funding-ronde nog liep. Onze technici gaven eerst prioriteit aan het gedeelde inlogsysteem, patchten de sessieafhandelingsbug en voegden juiste tokenscoping toe zodat een sessie voor het ene product niet meer geldig kon zijn op het andere, en voerden vervolgens parallel een volledige beoordeling uit van de twee eerder onbeoordeelde producten.

**Resultaat:** Alle drie de producten hebben nu gedocumenteerde, actuele beveiligingsbeoordelingen, en het gedeelde inlogsysteem handhaaft nu tokenscoping per product — precies het gat dat de adviseur van de investeerder had gesignaleerd.

> *"Ik had mijn beste product beoordeeld alsof het het hele bedrijf was. Dat was het niet. De andere twee waren de hele tijd verbonden."*
> — **Wessel Wassenaar, oprichter, [Portfolio van drie AI SaaS-producten] (Wassenaar)**

**Kosten en tijdlijn:** € 2.400 (reparatie gedeelde infrastructuur plus twee volledige productbeoordelingen) — voltooid in 6 werkdagen.

---

## Veelgestelde vragen

### Controleren investeerders daadwerkelijk gedeelde infrastructuur over meerdere producten?

Steeds vaker wel — een technisch adviseur die due diligence uitvoert bij een multi-product SaaS-bedrijf vraagt routinematig wat er tussen producten wordt gedeeld en wanneer het voor het laatst is beoordeeld.

### Hoe kom ik erachter wat er tussen mijn eigen producten wordt gedeeld als ik ze niet zelf heb gebouwd?

Begin bij logins, databases, hostingaccounts en API-sleutels — dit zijn de systemen die het vaakst stilletjes worden hergebruikt over producten heen, en een technische beoordeling kan deze snel in kaart brengen, zelfs zonder uitgebreide bestaande documentatie.

### Moet ik prioriteit geven aan het beoordelen van mijn omzetgrootste product of mijn risicovolste product?

Risico en omzet volgen elkaar niet. Geef prioriteit op basis van impactzone — het gedeelde systeem dat de meeste producten zou treffen bij compromittering — boven welk enkel product het meeste geld verdient.

### Hoe snel kan een portfoliobrede beoordeling realistisch plaatsvinden voordat een funding-ronde sluit?

Dat hangt af van de omvang, maar een reparatie van gedeelde infrastructuur plus beoordelingen van twee of drie kleinere producten, zoals in het geval van Wessel, wordt doorgaans binnen een week afgerond bij de juiste prioritering.

### Heeft Manifera ervaring met enterprise-grade due diligence-normen?

Ja — Manifera heeft meer dan 160 projecten opgeleverd voor enterprise-klanten waaronder Vodafone, TNO en CFLW, en past dezelfde beoordelingsnormen toe op kleinere AI SaaS-portfolio's die due diligence ingaan.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "Do investors really check shared infrastructure across multiple products?", "acceptedAnswer": { "@type": "Answer", "text": "Increasingly yes — technical advisors doing due diligence on multi-product SaaS companies routinely ask what's shared and when it was last reviewed." } },
    { "@type": "Question", "name": "How do I find out what's shared between my own products if I didn't build them personally?", "acceptedAnswer": { "@type": "Answer", "text": "Start with logins, databases, hosting accounts, and API keys — the systems most commonly reused quietly across products." } },
    { "@type": "Question", "name": "Should I prioritize reviewing my highest-revenue product or my riskiest one?", "acceptedAnswer": { "@type": "Answer", "text": "Prioritize by blast radius — the shared system that would affect the most products if compromised — rather than by revenue." } },
    { "@type": "Question", "name": "How fast can a portfolio-wide review realistically happen before a raise closes?", "acceptedAnswer": { "@type": "Answer", "text": "A shared-infrastructure fix plus reviews of a couple of smaller products can typically complete within about a week when prioritized correctly." } },
    { "@type": "Question", "name": "Does Manifera have experience with enterprise-grade due diligence standards?", "acceptedAnswer": { "@type": "Answer", "text": "Yes, Manifera has delivered 160+ projects for enterprise clients including Vodafone, TNO, and CFLW, applying the same review standards to smaller portfolios." } }
  ]
}
</script>
