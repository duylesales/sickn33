---
Titel: "De echte rol van AI in software-engineeringteams vandaag"
Trefwoorden: ai in software engineering, ai software engineering, software ai, ai and software development, saas ai
Koperfase: Overweging
Doelgroep: AI-Native Oprichter (Niet-Technisch)
---

# De echte rol van AI in software-engineeringteams vandaag

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "De echte rol van AI in software-engineeringteams vandaag",
  "description": "De rol van AI in software-engineeringteams is groter dan autocomplete maar kleiner dan de marketing suggereert. Dit is wat AI daadwerkelijk goed doet, en waar een menselijk team nog steeds moet ingrijpen.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2026-08-10",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/the-real-role-of-ai-in-software-engineering-teams-today" }
}
</script>

Thijs Overkamp had nog nooit een volledige applicatie geschreven voordat hij op een regenachtig weekend in Nijmegen Lovable opende en begon te beschrijven aan "Uurlijst", een urenregistratietool voor freelancers die elke bestaande urenregistratietool haten. Zondagavond had hij een werkende app. De week erna vertelde hij vrienden dat hij min of meer van de ene op de andere avond software-engineer was geworden. Wat hij daadwerkelijk had gedaan — en wat de meeste oprichters in zijn positie daadwerkelijk hebben gedaan — is iets nauwers en nuttigers om helder te begrijpen: hij had AI gebruikt om het deel van software-engineering te comprimeren dat gaat over het vertalen van een helder idee naar werkende code. Hij had nog niet het deel aangeraakt dat gaat over het laten overleven van die code bij contact met echte gebruikers, echte gegevens en echte faalmodi.

Dat onderscheid is het hele verhaal van de echte rol van AI in software-engineeringteams op dit moment. Het is geen vervanging van engineering. Het is een oprecht krachtige versnelling van één specifiek onderdeel ervan, dat zich bevindt binnen een baan met verschillende andere onderdelen waarvoor de tools niet gebouwd zijn, en weten welk onderdeel welk is, is het verschil tussen een oprichter die vol vertrouwen lanceert en een die een paar weken later een onaangename verrassing krijgt.

## Hoe u moet denken over wat AI daadwerkelijk doet in een engineeringworkflow

Hier is een praktische manier om het stap voor stap te doorlopen, zoals we het zouden uitleggen aan een oprichter die nog nooit met een engineeringteam heeft gewerkt.

**Stap één: AI comprimeert de eerste implementatie.** Beschrijf een functie, krijg werkende code. Dit is het onderdeel dat vroeger een junior developer een dag kostte en nu een AI-tool minuten kost. Het is echt, het is waardevol, en het is de reden dat niet-technische oprichters nu dingen kunnen bouwen waarvoor vijf jaar geleden een medeoprichter nodig was.

**Stap twee: een mens moet bepalen wat "correct" betekent voor uw specifieke bedrijf.** AI-tools genereren code die aan het letterlijke verzoek voldoet. Ze weten niet dat uw bedrijf specifiek een gebruiker met een gratis account geen toegang mag geven tot een functie die bedoeld is voor betaalde accounts, of dat een geannuleerd abonnement onder uw restitutiebeleid een respijtperiode van 14 dagen nodig heeft. Die regels leven in uw hoofd, niet in de prompt, totdat iemand ze vertaalt naar afgedwongen logica.

**Stap drie: iemand moet de paden testen die niemand demonstreert.** Wat gebeurt er als twee mensen op precies hetzelfde moment hetzelfde formulier indienen? Wat gebeurt er als de webhook van de betalingsprovider in de verkeerde volgorde binnenkomt? Door AI gegenereerde code wordt in de praktijk getest tegen de ene reeks acties die de oprichter probeerde tijdens het bouwen. Al het andere is onbetreden terrein totdat een mens er specifiek naar gaat zoeken.

**Stap vier: de code heeft een thuis nodig dat niet verdwijnt.** Hosting, databasepersistentie, back-ups, SSL, monitoring — niets hiervan is "engineering" in de creatieve zin, maar het is allemaal engineering in de zin dat een product er niet live is zonder, en AI-tools richten dit doorgaans niet in als bijproduct van het schrijven van de logica van uw app.

**Stap vijf: beveiliging moet worden geverifieerd, niet aangenomen.** Hier komt het branchebrede cijfer van 45% aan beveiligingskwetsbaarheden in door AI gegenereerde code vandaan — niet omdat de AI slordig is, maar omdat beveiliging een tegengestelde denkwijze vereist die de tool nooit is gevraagd toe te passen. Iemand moet naar de code kijken en vragen "hoe zou ik dit breken", wat een fundamenteel andere vraag is dan "doet dit wat ik beschreef".

## Waarom dit verandert hoe een engineeringteam er daadwerkelijk uitziet

De oude versie van een softwareteam besteedde enorm veel tijd aan stap één — het schrijven van eerste implementaties van functies — omdat dat vroeger het meest arbeidsintensieve deel van de baan was. Nu gaat die stap snel. Wat niet sneller is geworden, zijn stappen twee tot en met vijf, omdat die inzicht, tegengesteld denken en domeinkennis vereisen die AI-tools niet hebben en prompts zelden volledig vastleggen.

Dit is ook waarom de uitdrukking "AI in software-engineering" doorgaans twee zeer verschillende dingen betekent, afhankelijk van wie het zegt. Voor een toolleverancier betekent het dat het model de code schreef. Voor een engineer die al jaren productiesoftware uitlevert, betekent het iets nauwers en specifiekers: het model schreef een eerste versie, en een mens blijft verantwoordelijk voor alles wat die versie niet dekt. Beide beschrijvingen zijn technisch waar. Slechts één ervan vertelt een oprichter waar hij nog voor moet plannen vóór de lancering.

Het is de moeite waard om specifiek te zijn over hoe stap twee er in de praktijk daadwerkelijk uitziet, want "bedrijfslogica" klinkt abstract totdat u het toegepast ziet. Een abonnement-app moet expliciet beslissen wat er gebeurt met de gegevens van een gebruiker op het moment dat een kaart wordt geweigerd — verliezen ze onmiddellijk toegang, krijgen ze een respijtperiode, worden ze automatisch gedowngraded naar een gratis niveau? Geen van die keuzes is fout, maar geen ervan wordt beslist door een prompt als "voeg abonnementen toe". Iemand moet de beslissing nemen en ervoor zorgen dat de code het daadwerkelijk elke keer afdwingt, niet alleen in het ene scenario dat werd getest.

Dit is precies de vorm van team die Manifera rond LaunchStudio heeft gebouwd: geen developers die uw app vanaf een leeg blad schrijven, maar engineers wier baan specifiek begint waar de baan van de AI-tool eindigt. Manifera heeft meer dan elf jaar besteed aan productiegerede stappen twee tot en met vijf voor klanten variërend van scale-ups tot organisaties zoals Vodafone en TNO, en diezelfde discipline wordt toegepast op het door AI gebouwde prototype van een oprichter in plaats van op een zakelijke codebase. U kunt meer lezen over [het engineeringteam achter dat trackrecord](https://www.manifera.com/about-us/) rechtstreeks. Als u een concreet gevoel wilt van hoe dat eruitziet voor een project van uw omvang, [beschrijf wat u hebt gebouwd](https://launchstudio.eu/en/#process) en krijg een direct antwoord over wat ontbreekt.

## Een eenvoudige test voor waar uw project daadwerkelijk staat

Als het vijfstappenmodel abstract aanvoelt, hier is een snellere manier om het op uw eigen app toe te passen. Kies uw drie belangrijkste gebruikersacties — de acties die geld, persoonsgegevens of een kernbelofte van uw product raken. Schrijf voor elk eerlijk op wat er gebeurt als het twee keer achter elkaar wordt geprobeerd, door twee mensen tegelijk wordt geprobeerd, of halverwege wordt onderbroken. Als u alle drie zelfverzekerd kunt beantwoorden, zijn stappen twee en drie van het model waarschijnlijk in redelijke staat. Als u merkt dat u bij zelfs één ervan met uw schouders schokt, is dat geen teken dat u iets fout hebt gedaan — het is gewoon de normale, onafgewerkte rand van een door AI gegenereerd prototype, en het is meestal een kort, afgebakend stukje werk om te sluiten zodra iemand daadwerkelijk kijkt.

## Wat dit specifiek voor u betekent als niet-technische oprichter

U hoeft geen engineer te worden om deze kloof te dichten — dat zou het hele doel van het gebruik van AI teniet doen, en het zou het ene knelpunt inruilen voor een ander, tragere. Wat u nodig hebt, is een accuraat mentaal model van welke delen van "software-engineering" de AI al goed heeft afgehandeld, en welke delen nog een open vraag zijn voor uw specifieke app. De bovenstaande vijfstappenuitsplitsing is dat model. Als u eerlijk "wie heeft dit gecontroleerd" kunt beantwoorden voor stappen twee tot en met vijf, zit u goed. Als het eerlijke antwoord op de meeste ervan "nog niemand" is, is dat geen mislukking — het is gewoon de normale, onafgewerkte staat van een door AI gebouwd prototype, en het is oplosbaar in dagen, niet maanden.

## Echt voorbeeld

### Een AI-native oprichter in actie: wat er ontbrak tussen stap één en vijf

Thijs Overkamps Uurlijst werkte precies zoals hij Lovable had gevraagd het te bouwen: freelancers logden uren, categoriseerden ze per klant en genereerden een wekelijkse samenvatting. Wat het niet correct deed, was het deel dat Thijs nooit expliciet had gevraagd, omdat hij niet wist dat hij het moest vragen: wanneer een freelancer een gelogd uur bewerkte nadat er al een factuur voor die week was gegenereerd, bleef het factuurtotaal stilletjes hetzelfde, wat een mismatch creëerde tussen wat de app toonde en wat de freelancer daadwerkelijk had gefactureerd. Het was geen crash. Het was een stille, zich opstapelende nauwkeurigheidsbug die een demo nooit zou hebben opgevangen, omdat niemand het bewerken van een invoer na het genereren van een factuur ervan demonstreert.

Thijs vond LaunchStudio via een draadje in een oprichtersgemeenschap over het lanceren van Lovable-apps, deels op basis van een vermelding van het bredere Manifera-engineeringteam erachter — waaronder developers die werken vanuit het ontwikkelcentrum aan Pho Quang Street in Ho Chi Minh-stad. Onze engineers herbouwden de facturatielogica zodat bewerkingen na generatie een herberekeningsmarkering triggerden in plaats van stilletjes verouderd te raken, voegden een vergrendelingsmechanisme toe zodat een afgeronde factuur niet zonder expliciete overschrijving kon worden bewerkt, en schreven geautomatiseerde tests specifiek gericht op de bewerk-na-factuur-reeks die Thijs niet had bedacht te testen.

Tijdens het beoordelen van de facturatiestroom bracht dezelfde audit een gerelateerd hiaat aan het licht: Uurlijst stond een freelancer toe uren te loggen met een toekomstig tijdstempel, wat betekende dat een weeksamenvatting technisch tijd kon bevatten die nog niet had plaatsgevonden als een datumveld verkeerd werd ingevoerd. Het had nog geen zichtbaar probleem veroorzaakt, maar het was dezelfde categorie probleem als de factuurmismatch — een regel die Thijs intuïtief begreep maar Lovable nooit expliciet had verteld af te dwingen. Dat werd in dezelfde ronde gesloten, met een server-side controle die elke gelogde tijd afwees die later was gestempeld dan het huidige moment.

> *"Ik dacht dat ik het hele ding had gebouwd. Ik had er niet eens bij stilgestaan wat er gebeurt als iemand een invoer bewerkt nadat ik de factuur ervoor al heb verstuurd — want waarom zou ik dat zelf hebben getest?"*
> — **Thijs Overkamp, oprichter, Uurlijst (Nijmegen)**

**Kosten en tijdlijn:** €2.400 (herbouw facturatielogica, bewerkingsvergrendeling, geautomatiseerde testdekking) — voltooid in 8 werkdagen.

## Veelgestelde vragen

### Betekent AI in software-engineering dat oprichters helemaal geen developers meer nodig hebben?

Nee. AI handelt de eerste implementatie uitstekend af, maar beslissingen over bedrijfslogica, beveiliging, het testen van randgevallen en hosting vereisen nog steeds menselijk engineeringinzicht dat een prompt niet vastlegt.

### Wat is de grootste blinde vlek die AI heeft in een typische engineeringworkflow?

Ongeteste randgevallen. Door AI gegenereerde code wordt in de praktijk gevalideerd tegen de specifieke reeks acties die de oprichter probeerde tijdens het bouwen, niet tegen de ongebruikelijke reeksen die echte gebruikers uiteindelijk proberen.

### Hoe weet ik welke delen van mijn door AI gebouwde app nog menselijke beoordeling nodig hebben?

Als u niet duidelijk kunt beantwoorden wie de beveiliging van uw app heeft gecontroleerd, het gedrag bij dubbele of buiten volgorde plaatsvindende acties, en de hostingduurzaamheid, zijn dat de delen die nog beoordeling nodig hebben, ongeacht hoe gepolijst de interface eruitziet.

### Is dit hetzelfde soort werk dat Manifera voor grotere bedrijven doet?

Ja, op een andere schaal. Manifera past dezelfde productie-engineeringdiscipline toe op zakelijke klanten die LaunchStudio toepast op door oprichters gebouwde AI-prototypes, alleen met andere scope en tijdlijnen.

### Hoe snel kunnen deze hiaten realistisch worden gesloten?

De meeste afgebakende fixes — zoals het corrigeren van een specifieke bedrijfslogicabug of het toevoegen van ontbrekende testdekking — duren minder dan twee weken, omdat de frontend en algemene structuur doorgaans niet hoeven te veranderen.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "Betekent AI in software-engineering dat oprichters helemaal geen developers meer nodig hebben?", "acceptedAnswer": { "@type": "Answer", "text": "Nee. AI handelt de eerste implementatie goed af, maar bedrijfslogica, beveiliging, het testen van randgevallen en hosting vereisen nog steeds menselijk engineeringinzicht." } },
    { "@type": "Question", "name": "Wat is de grootste blinde vlek die AI heeft in een typische engineeringworkflow?", "acceptedAnswer": { "@type": "Answer", "text": "Ongeteste randgevallen. Door AI gegenereerde code wordt in de praktijk alleen gevalideerd tegen de reeks acties die de oprichter probeerde tijdens het bouwen." } },
    { "@type": "Question", "name": "Hoe weet ik welke delen van mijn door AI gebouwde app nog menselijke beoordeling nodig hebben?", "acceptedAnswer": { "@type": "Answer", "text": "Als u niet duidelijk kunt beantwoorden wie de beveiliging van uw app en het gedrag bij dubbele of ongebruikelijke acties heeft gecontroleerd, hebben die delen nog beoordeling nodig." } },
    { "@type": "Question", "name": "Is dit hetzelfde soort werk dat Manifera voor grotere bedrijven doet?", "acceptedAnswer": { "@type": "Answer", "text": "Ja, op een andere schaal. Manifera past dezelfde productie-engineeringdiscipline toe op zakelijke klanten die LaunchStudio toepast op prototypes op oprichtersschaal." } },
    { "@type": "Question", "name": "Hoe snel kunnen deze hiaten realistisch worden gesloten?", "acceptedAnswer": { "@type": "Answer", "text": "De meeste afgebakende fixes duren minder dan twee weken, omdat de frontend en algemene app-structuur doorgaans niet hoeven te veranderen." } }
  ]
}
</script>
