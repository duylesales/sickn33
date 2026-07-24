---
Titel: "Waarom 'technische schuld' iets anders betekent wanneer AI de schuld heeft geschreven"
Trefwoorden: ai software engineering, ai generated technical debt, dry principle ai code, code quality ai tools
Koperfase: Overweging
Doelgroep: Technische solo-oprichter
---
# Waarom 'technische schuld' iets anders betekent wanneer AI de schuld heeft geschreven

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Waarom 'technische schuld' iets anders betekent wanneer AI de schuld heeft geschreven",
  "description": "Technische schuld betekende vroeger shortcuts die een team bewust nam onder tijdsdruk. Door AI gegenereerde schuld is anders — niemand koos ervoor, en niemand let erop. Dit is waarom dat belangrijk is.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2026-07-25",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/technical-debt-means-different-ai-wrote-it" }
}
</script>

Technische schuld had altijd een specifieke betekenis: een team verzendt bewust een shortcut onder tijdsdruk, begrijpt de afweging en is van plan om later terug te komen om het te repareren. De metafoor werkt omdat er intentie in besloten ligt — iemand koos ervoor om te lenen tegen de toekomst. Door AI gegenereerde technische schuld doorbreekt die metafoor volledig, en ik denk niet dat de meeste oprichters, zelfs technische, volledig hebben doorgrond wat er is veranderd.

## Oude schuld had een schuldenaar. Nieuwe schuld niet.

Wanneer een menselijke engineer een bocht afsnijdt, is er een beslissingsspoor. Iemand schreef een opmerking, of herinnert zich in ieder geval te hebben gedacht "dit is niet ideaal, maar het gaat vandaag de deur uit". Die herinnering is zelf een vorm van documentatie — een impliciete to-dolijst die in iemands hoofd leeft, klaar om naar boven te komen in een retrospectief of een sprintplanning. Door AI gegenereerde schuld heeft geen dergelijk spoor. Het model snijdt geen bocht af omdat het onder tijdsdruk staat. Het snijdt een bocht af omdat het helemaal geen instinct heeft voor de afweging — het optimaliseerde voor "werkende code produceren die aan deze prompt voldoet", niet voor "code produceren waar een toekomstige beheerder, of een toekomstige versie van het model, u dankbaar voor zal zijn".

## De specifieke vorm die AI-schuld doorgaans aanneemt

De meest voorkomende vorm is geen slordigheid in één enkel bestand — door AI gegenereerde code is vaak lokaal netjes, goed becommentarieerd, zelfs idiomatisch. De schuld toont zich structureel, verspreid over bestanden: dezelfde logica net iets anders geïmplementeerd op vijf of acht plekken, omdat het model geen blijvend geheugen had van het feit dat het dit probleem drie bestanden eerder al had opgelost. Mensen noemen dit een schending van het DRY-principe — Don't Repeat Yourself — en ervaren engineers ontwikkelen een bijna fysiek ongemak bij gedupliceerde logica. Modellen hebben dat ongemak niet. Elk bestand wordt tot op zekere hoogte opnieuw, vers, opgelost.

Dit is belangrijker dan het klinkt. Gedupliceerde logica betekent dat een bugfix die op één kopie wordt toegepast, niet doorwerkt naar de andere zeven. Het betekent dat een wijziging in een bedrijfsregel vereist dat u elke bijna-identieke implementatie opspoort in plaats van één gedeelde functie bij te werken. En omdat niemand bewust koos voor duplicatie, dacht ook niemand eraan om erop te controleren — er was geen moment van "ik weet dat dit niet ideaal is" dat een notitie zou hebben getriggerd om er later op terug te komen.

## Waarom dit verandert hoe u door AI gegenereerde codebases zou moeten beoordelen

Als u een technische oprichter bent die uw eigen door AI gegenereerde code beoordeelt, moet de beoordelingschecklist verschuiven. U bent niet op zoek naar bochten die een vermoeide engineer onder druk heeft afgesneden. U bent op zoek naar een geheel ander faalpatroon: logica die meerdere keren, net iets anders, is opgelost, zonder gedeelde bron van waarheid. Dat vereist actief zoeken door de hele codebase naar bijna-identieke functies, niet alleen elk bestand afzonderlijk lezen en u afvragen "ziet dit er redelijk uit".

Herre Roelevink, CEO van LaunchStudio en Managing Director van Manifera, verwoordt de bredere verschuiving zo: "We zien een verschuiving in softwarebehoeften. De uitdaging is niet langer goede ideeën omzetten in software. Het gaat nu om de architectuur en beveiliging die nodig zijn om die producten tot volwassenheid te brengen. We hebben elf jaar ervaring in precies dat." Dat volwassenheidswerk omvat steeds vaker precies dit soort structurele schuld — het soort dat zichzelf niet aankondigt, omdat niemand ervoor koos deze aan te gaan.

LaunchStudio, gesteund door Manifera's team van engineers gevestigd in Amsterdam en daarbuiten, beoordeelt door AI gegenereerde codebases specifiek op dit patroon voordat productiewerk wordt aanbevolen. Als u vermoedt dat uw eigen door AI gebouwde product dit soort schuld stilletjes over uw bestanden heeft liggen, kunt u [praten met een engineer die door AI gegenereerde code begrijpt](https://launchstudio.eu/en/#contact) over een beoordeling. Voor een blik op de productiegerichte engineeringdiscipline die wij toepassen, zie [de aanpak van Manifera voor webapp-ontwikkeling](https://www.manifera.com/services/web-app-develop/).

## Echt voorbeeld

### Een AI-native oprichter in actie: De bug die op acht plekken leefde

Nina Bosch, een oprichter in Groningen, bouwde "ArchiefKoppel", een documentbeheer-SaaS voor kleine juridische en administratieve kantoren, met Cursor. Het product regelde documenttagging, versiebeheer en toegangsrechten — echt nuttige functionaliteit die Cursor haar sneller hielp uitbrengen dan ze had verwacht. Naar de meeste maatstaven zag de codebase er netjes uit: goed georganiseerde bestanden, verstandige naamgeving, leesbare functies.

Het probleem kwam aan het licht toen Nina een bug moest oplossen in de manier waarop documenttoegangsrechten werden berekend. Ze loste het op in het bestand waar ze het vond, testte het, bevestigde dat het werkte, en bracht de update uit. Weken later meldde een klant precies dezelfde bug in een ander deel van het product. Nina ontdekte uiteindelijk dat Cursor bijna-identieke logica voor toegangscontrole had geïmplementeerd in acht verschillende bestanden, in plaats van deze één keer te bouwen als een gedeelde functie die elk deel van de app aanriep. Niemand had bewust een bocht afgesneden — de AI had simpelweg geen instinct om te merken dat het dit probleem al eerder ergens anders in de codebase had opgelost, en Nina had er niet aan gedacht op dat specifieke patroon te controleren.

Ze bracht ArchiefKoppel naar LaunchStudio voor een structurele beoordeling. Engineers zochten systematisch naar gedupliceerde logica in de codebase, consolideerden de acht implementaties van toegangscontrole tot één gedeelde functie, en voegden een patroon toe om vergelijkbare duplicatie in toekomstige door AI gegenereerde toevoegingen op te vangen.

**Resultaat:** ArchiefKoppel heeft nu één gezaghebbende bron voor toegangslogica in plaats van acht, en Nina heeft een herhaalbaar proces om dit patroon voortaan op te sporen.

> *"Ik bleef dezelfde bug in andere kleren oplossen. Er was iemand anders voor nodig om erop te wijzen dat het nooit één bug was — het waren acht kopieën van dezelfde fout."*
> — **Nina Bosch, oprichter, ArchiefKoppel (Groningen)**

**Kosten en tijdlijn:** € 1.150 (codebase-brede duplicatie-audit en consolidatie) — voltooid in 5 werkdagen.

---

## Veelgestelde vragen

### Waarom is door AI gegenereerde technische schuld moeilijker te spotten dan door mensen gecreëerde schuld?

Omdat er geen beslissingsspoor is — niemand koos bewust voor de shortcut, dus er is geen opmerking, herinnering of to-donotitie die toekomstige beoordelaars naar het probleem wijst.

### Betekent er netjes uitziende code dat de codebase dit soort schuld niet heeft?

Nee. Door AI gegenereerde schuld is vaak structureel en overspant meerdere bestanden, dus elk afzonderlijk bestand kan er netjes uitzien terwijl dezelfde logica stilletjes elders wordt gedupliceerd.

### Wat bedoelt Herre Roelevink met de verschuiving naar "architectuur en volwassenheid"?

Hij beschrijft hoe het moeilijke deel van door AI gebouwde software is verschoven van het genereren van werkende code naar het beoordelen en structureren van die code zodat deze standhoudt onder echt productiegebruik.

### Hoe zouden de engineers van Manifera gedupliceerde logica vinden in een grote codebase?

Ze zoeken systematisch naar bijna-identieke functies en patronen in bestanden, in plaats van elk bestand afzonderlijk te beoordelen, wat is hoe dit soort schuld zich doorgaans verbergt.

### Kan dit soort schuld worden opgelost zonder het hele product te herbouwen?

Ja, het consolideren van gedupliceerde logica in gedeelde functies is gericht werk dat alleen de betrokken bestanden raakt, zonder een volledige herschrijving te vereisen.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "Why is AI-generated technical debt harder to spot than human-created debt?", "acceptedAnswer": { "@type": "Answer", "text": "There's no decision trail, since nobody consciously chose the shortcut, so there's no comment or note pointing reviewers toward the problem." } },
    { "@type": "Question", "name": "Does clean-looking code mean the codebase doesn't have this kind of debt?", "acceptedAnswer": { "@type": "Answer", "text": "No, AI-generated debt is often structural and spans multiple files, so a single file can look clean while logic is duplicated elsewhere." } },
    { "@type": "Question", "name": "What does Herre Roelevink mean by the shift toward \"architecture and maturity\"?", "acceptedAnswer": { "@type": "Answer", "text": "He describes how the hard part of AI-built software has moved from generating working code to structuring it so it holds up in production." } },
    { "@type": "Question", "name": "How would Manifera's engineers find duplicated logic across a large codebase?", "acceptedAnswer": { "@type": "Answer", "text": "They search systematically for near-identical functions and patterns across files rather than reviewing each file in isolation." } },
    { "@type": "Question", "name": "Can this kind of debt be fixed without rebuilding the whole product?", "acceptedAnswer": { "@type": "Answer", "text": "Yes, consolidating duplicated logic into shared functions is targeted work that doesn't require a full rewrite." } }
  ]
}
</script>
