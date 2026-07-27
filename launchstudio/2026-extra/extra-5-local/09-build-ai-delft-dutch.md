---
Titel: "Hoe Delftse oprichters AI-producten bouwen zonder engineeringteam"
Trefwoorden: build ai, build an ai app, technical founder, ci/cd deployment, Delft
Koperfase: Overweging
Doelgroep: Technische solo-oprichter
---
# Hoe Delftse oprichters AI-producten bouwen zonder engineeringteam

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Hoe Delftse oprichters AI-producten bouwen zonder engineeringteam",
  "description": "Hoe technische solo-oprichters in Delft AI-producten bouwen zonder een engineeringteam aan te nemen, en waar die aanpak vastloopt zodra er echte gebruikers bijkomen.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2026-07-23",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/build-ai-delft" }
}
</script>

Daan Smit studeerde af aan de TU Delft met een graad in werktuigbouwkunde, leerde zichzelf gevaarlijk genoeg te coderen, en gebruikte Cursor om in zes weken een compleet IoT-dashboard te bouwen voor het volgen van sensorvloten, werkend tijdens de avonden na zijn dagbaan. Hij nam niemand aan. Dat is het verhaal van een groeiend aantal oprichters die AI-producten solo proberen te bouwen vanuit Delft — en het is een verhaal dat werkt, tot het moment waarop de deploymentpijplijn zelf het knelpunt wordt.

## Waarom "AI bouwen zonder team" werkt tot op een bepaald punt

Delfts oprichtersbasis ziet er anders uit dan die van de meeste Nederlandse steden vanwege haar zwaartepunt: de TU Delft, een van Europa's toonaangevende technische universiteiten, brengt een gestage stroom voort van technisch ingestelde oprichters die comfortabel genoeg zijn met code om zelf AI-producten te bouwen met tools zoals Cursor, zonder een ontwikkelteam te hoeven aannemen. Dat is een oprecht voordeel — deze oprichters kunnen lezen wat de AI genereert, voor de hand liggende problemen debuggen, en snel itereren zonder een communicatielaag tussen "wat ik wil" en "wat er is gebouwd".

De beperking zit niet in technische vaardigheid. Het is dat een sterke individuele bijdrager zijn en productie-infrastructuur runnen verschillende disciplines zijn, en de meeste technische solo-oprichters in Delft hebben de tweede nog nooit hoeven bezitten — omdat die infrastructuur bij een vorige baan of in de academische wereld doorgaans iemand anders' verantwoordelijkheid was.

## Waar de solo-bouwaanpak vastloopt

Het patroon dat LaunchStudio herhaaldelijk ziet bij technisch bekwame Delftse oprichters:

- Geen CI/CD-pijplijn, wat betekent dat elke deploy een handmatig proces is dat vanaf een laptop wordt uitgevoerd, zonder geautomatiseerde testpoort voordat code de productie bereikt
- Omgevingsvariabelen en databasereferenties die tijdens de vroege ontwikkeling rechtstreeks in de codebase worden hardgecodeerd, en vervolgens nooit worden opgeruimd vóór lancering
- Geen staging-omgeving, waardoor elke wijziging tegen productiegegevens wordt getest, of helemaal niet wordt getest vóór livegang
- Handmatige, ongedocumenteerde deploymentstappen die alleen de oprichter kan uitvoeren, wat een single point of failure creëert

Geen van deze zijn precies kennislacunes — de meeste technisch ingestelde oprichters weten dat deze zaken in theorie belangrijk zijn. Het zijn tijd- en prioriteitslacunes: als u solo bouwt, concurreert deploymentinfrastructuur rechtstreeks met productfuncties om dezelfde uren, en functies winnen doorgaans totdat er iets kapotgaat.

## De kloof dichten zonder aan te nemen

Dit is waar het model van LaunchStudio specifiek goed past bij het profiel van Delftse technische oprichters: in plaats van een volledig engineeringteam aan te nemen, halen oprichters het team van Manifera erbij — meer dan 120 engineers met meer dan 11 jaar productie-ervaring, deels gecoördineerd vanuit onze ontwikkelhub in Ho Chi Minhstad — voor het specifieke infrastructuurwerk dat buiten hun huidige capaciteit valt, zonder eigendom van het product zelf op te geven. De [praktijk voor maatwerksoftwareontwikkeling](https://www.manifera.com/services/custom-software-development/) van Manifera is precies rond dit soort gerichte technische opdrachten gebouwd, in plaats van langetermijnbemanningsverplichtingen.

Voor een Delftse oprichter die probeert uit te zoeken welke delen van zijn met Cursor gebouwde product dit soort verharding nodig hebben, geven de [pakketopties](https://launchstudio.eu/en/#packages) van LaunchStudio inzicht in wat doorgaans is inbegrepen in een productiegereedheidspas, afgestemd op het budget van een solo-oprichter in plaats van een zakelijk traject.

## Echt voorbeeld

### Een AI-native oprichter in actie: het kwetsbare deployproces van SensorForge

Daan Smit bouwde SensorForge, een vlootmonitoringdashboard voor engineeringteams die verspreide IoT-sensornetwerken beheren — een productidee dat rechtstreeks voortkwam uit frustraties die hij had gehad met bestaande tools tijdens zijn tijd rond de robotica-labs van de TU Delft. Volledig gebouwd in Cursor, werkte SensorForge goed voor zijn eerste handvol pilotklanten, allemaal kleine engineeringteams in de Delftse regio.

Het probleem kwam aan het licht tijdens een routinematige update: Daan pushte een wijziging rechtstreeks naar productie zonder eerst een stagingtest, en een databasemigratie liep verkeerd, waardoor het dashboard zes uur offline ging tijdens het actieve monitoringvenster van een pilotklant — het slechtst denkbare moment voor een monitoringtool om uit te vallen. Er was geen rollbackproces, dus Daan moest de vorige databasestatus handmatig reconstrueren uit gedeeltelijke logs.

**Resultaat:** LaunchStudio bouwde een correcte CI/CD-pijplijn met geautomatiseerde tests, een staging-omgeving die productie weerspiegelt, en een one-command rollbackproces, waardoor handmatige productiedeploys volledig werden geëlimineerd.

> *"Ik kon de code schrijven. Ik had geen idee hoe blootgesteld ik elke keer was wanneer ik op deploy klikte, totdat het een klant daadwerkelijk zes uur downtime kostte."*
> — **Daan Smit, oprichter, SensorForge (Delft)**

**Kosten en tijdlijn:** € 2.100 (CI/CD-pijplijn, staging-omgeving, geautomatiseerde rollback) — voltooid in 8 werkdagen.

---

## Veelgestelde vragen

### Ik kan redelijk goed zelf coderen — heb ik LaunchStudio echt nodig?

Veel klanten van LaunchStudio zijn technisch bekwame oprichters zoals Daan. De waarde zit niet in code schrijven die u zelf niet kunt schrijven — het zit in de deployment- en infrastructuurdiscipline, een oprecht andere vaardigheid dan productontwikkeling.

### Werkt LaunchStudio met oprichters die hands-on willen blijven bij hun eigen codebase?

Ja. LaunchStudio bouwt infrastructuur rondom uw bestaande code en draagt doorgaans volledige documentatie en toegang over, in plaats van een doorlopende afhankelijkheid te creëren.

### Is Delfts technische oprichtersscene anders dan andere steden in Zuid-Holland?

Ja, aanzienlijk — de aanwezigheid van de TU Delft betekent dat een groter aandeel van de oprichters hier comfortabel is met zelf code schrijven en lezen, wat bepaalt welke hulp daadwerkelijk nuttig is.

### Wat brengt het technische team van Manifera specifiek mee voor een CI/CD-opzet?

De meer dan 120 engineers van Manifera brengen meer dan 11 jaar productiedeploymentervaring mee, verspreid over meer dan 160 projecten, waaronder infrastructuurwerk voor zakelijke klanten zoals Vodafone, toegepast op een schaal die past bij het product van een solo-oprichter.

### Hoe snel kan een correcte CI/CD-pijplijn daadwerkelijk worden gebouwd?

Voor de meeste opzetten met één product voltooit LaunchStudio dit soort infrastructuurwerk doorgaans binnen één tot twee weken, afhankelijk van de complexiteit van de bestaande codebase.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "I can code reasonably well myself — do I really need LaunchStudio?", "acceptedAnswer": { "@type": "Answer", "text": "The value isn't writing code you can't write yourself — it's deployment and infrastructure discipline, a genuinely different skill set from product development." } },
    { "@type": "Question", "name": "Does LaunchStudio work with founders who want to stay hands-on with their own codebase?", "acceptedAnswer": { "@type": "Answer", "text": "Yes. LaunchStudio builds infrastructure around your existing code and typically hands over full documentation and access rather than creating an ongoing dependency." } },
    { "@type": "Question", "name": "Is Delft's technical founder scene different from other Zuid-Holland cities?", "acceptedAnswer": { "@type": "Answer", "text": "Yes — TU Delft's presence means a higher share of founders here are comfortable writing and reading code themselves." } },
    { "@type": "Question", "name": "What does Manifera's engineering team bring to a CI/CD setup specifically?", "acceptedAnswer": { "@type": "Answer", "text": "Manifera's 120+ engineers bring 11+ years of production deployment experience across 160+ projects, including work for enterprise clients like Vodafone." } },
    { "@type": "Question", "name": "How fast can a proper CI/CD pipeline actually be built?", "acceptedAnswer": { "@type": "Answer", "text": "For most single-product setups, LaunchStudio typically completes this kind of infrastructure work within one to two weeks." } }
  ]
}
</script>
