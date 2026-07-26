---
Titel: "De drie soorten 'het werkt'-claims — en welke er echt toe doet"
Trefwoorden: ai works, it works claim, ai testing gap, role based testing
Koperfase: Bewustzijn
Doelgroep: AI-Native oprichter (niet-technisch)
---
# De drie soorten 'het werkt'-claims — en welke er echt toe doet

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "De drie soorten 'het werkt'-claims — en welke er echt toe doet",
  "description": "Een uitleg in drie categorieën van wat oprichters daadwerkelijk bedoelen als ze zeggen dat hun door AI gebouwde app 'werkt', en waarom de kloof daartussen stille productiestoringen veroorzaakt.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/en/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2026-07-25",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/en/blog/three-types-of-ai-works-claims" }
}
</script>

Drie oprichters kunnen elk zeggen "mijn app werkt" en drie compleet verschillende dingen bedoelen, en geen van hen zal de kloof beseffen totdat er iets kapotgaat waar de verkeerde persoon bij staat. De uitdrukking "ai works" wordt in oprichterskringen voortdurend gebruikt alsof het één stabiele claim is. Dat is het niet. Het zijn eigenlijk drie afzonderlijke claims die dezelfde paar woorden dragen, en slechts één ervan is veilig genoeg om een bedrijf op te bouwen.

## Type één: "het werkt voor mij"

Dit is de meest voorkomende en de gevaarlijkste versie van de claim, juist omdat die het meest solide aanvoelt voor degene die hem maakt. Een oprichter bouwt een functie, klikt er zelf een paar keer doorheen met zijn eigen account, ziet hem zich correct gedragen, en concludeert dat hij werkt. Wat dit daadwerkelijk bewijst, is smaller dan het klinkt: de functie werkt voor één specifieke persoon, met één specifiek account, via één specifiek pad door de app, op één specifiek moment. Het zegt niets over wat er gebeurt voor een andere gebruiker, een ander accounttype, of een andere volgorde van handelingen. Dit type "het werkt" is een startpunt, geen conclusie.

## Type twee: "het werkt voor de mensen aan wie ik het heb laten zien"

Dit is een betekenisvolle stap vooruit — een handvol andere mensen heeft nu ook door de app geklikt, wat problemen naar boven brengt die de eigen tests van de oprichter nooit zouden hebben blootgelegd. Maar het is nog steeds beperkt tot precies wie die mensen zijn en wat ze toevallig hebben geprobeerd. Als iedereen die de app tot nu toe heeft getest hetzelfde accounttype, dezelfde use case, of hetzelfde algemene gedragspatroon heeft, kan dit type "het werkt" grondig lijken terwijl het toch enorme blinde vlekken heeft. Het voelt meer gevalideerd aan dan type één omdat er meer mensen bij betrokken waren, maar meer mensen die hetzelfde smalle pad testen is niet hetzelfde als een breder scala aan paden testen.

## Type drie: "het werkt onder omstandigheden die ik zelf nog niet heb geprobeerd"

Dit is de enige versie van de claim die daadwerkelijk ertoe doet voor een product dat echte klanten bedient, en het is de moeilijkste om te bereiken omdat het vereist dat u dingen doelbewust test waar niemand van nature een reden toe heeft. Wat gebeurt er voor een gebruikerstype dat u zelf niet hebt? Wat gebeurt er als iemand de stappen in een onverwachte volgorde uitvoert? Wat gebeurt er bij een toestemmingsniveau dat u zichzelf nooit hebt gegeven? Dit type "het werkt" wordt niet opgebouwd door meer terloops te klikken — het wordt opgebouwd door gestructureerd testen dat is ontworpen om de kloof te vinden tussen wat is geprobeerd en wat mogelijk is. Het is ook, niet toevallig, precies de categorie tests die de meeste AI-native oprichters overslaan, omdat het niet noodzakelijk aanvoelt totdat het moment aanbreekt waarop het dat overduidelijk wél was.

## Waarom de kloof tussen type één en type drie onzichtbaar blijft totdat dat niet meer zo is

Het gevaarlijke deel van dit hele raamwerk is dat type één, twee en drie er van buitenaf identiek uitzien. Een oprichter die zelfverzekerd "het werkt" zegt, geeft geen enkel signaal over welke van de drie claims hij daadwerkelijk bedoelt, en vaak beseft de oprichter zelf niet welk type hij maakt. Dit is precies de kloof waar de engineers van LaunchStudio op getraind zijn om te zoeken tijdens een productiegereedheidsbeoordeling — niet "werkt dit," maar "welke versie van werken is daadwerkelijk geverifieerd, en wat is helemaal niet aangeraakt." Het team van meer dan 120 engineers van Manifera, met een vestiging in Singapore die oprichters in de hele regio bedient, benadert elke beoordeling door expliciet te testen voor wat type drie vereist, want dat is de enige versie die overeind blijft zodra echte klanten met echte accounttypes en echte gebruikspatronen arriveren.

Heeft u recent "het werkt" gezegd over een functie en weet u niet zeker welk type u bedoelde, dan is die onzekerheid het waard om op te lossen voordat klanten het voor u oplossen. [Stuur ons de link naar uw prototype voor gratis advies](https://launchstudio.eu/en/#contact) over onder welk type "het werkt" uw app op dit moment daadwerkelijk opereert. Het team van Manifera voor [webapp-ontwikkeling](https://www.manifera.com/services/web-app-develop/) past dezelfde gestructureerde testdiscipline toe op enterprise-producten, waar de kostprijs van een onontdekte type-één-claim in een andere orde van grootte wordt gemeten.

## Echt voorbeeld

### Een AI-native oprichter in actie: de admin-only app van Jesse van Dam

Jesse van Dam, oprichter van MeldPunt, een gemeentelijke meldingsapp in Vlaardingen gebouwd met v0, vertelde vroege stakeholders zelfverzekerd dat de app werkte. Wat hij bedoelde, zonder het zich volledig te realiseren, was type één — hij werkte voor zijn eigen persoonlijke testaccount, dat vanaf het begin van de ontwikkeling adminrechten had. Hij had de app nog nooit als een ander accounttype getest, omdat hij dat nooit nodig had gehad; adminrechten lieten hem alles zien en doen, dus voor hem leek nooit iets kapot.

De kloof kwam aan het licht toen een gemeenteambtenaar de app probeerde te gebruiken met een standaard, niet-admin account. Een rolgebonden bug zorgde ervoor dat het meldingsformulier stilzwijgend niet werd ingediend voor elk ander accounttype dan admin — geen foutmelding, geen zichtbare feedback, gewoon een indiening die leek te lukken en vervolgens verdween. Omdat de eigen tests van Jesse uitsluitend gebruikmaakten van het ene accounttype dat de bug niet activeerde, was deze volledig onzichtbaar gebleven tijdens elke ronde van zijn eigen verificatie.

De engineers van LaunchStudio, ingeschakeld nadat de storing was gemeld, herleidden het probleem tot een toestemmingscontrole die correct was afgebakend voor adminaccounts maar nooit was uitgebreid om standaardrollen te verwerken, waardoor de indienlogica stilzwijgend faalde in plaats van een duidelijke foutmelding te geven. De oplossing bestond uit het corrigeren van de rolgebonden toestemmingslogica en het toevoegen van gestructureerd testen over elk accounttype dat MeldPunt daadwerkelijk moest ondersteunen, niet alleen het type dat Jesse zelf had gebruikt.

**Resultaat:** het meldingsformulier van MeldPunt werd hersteld voor alle accounttypes en opnieuw getest onder elke rol voordat het weer werd geïntroduceerd bij gemeentepersoneel, zonder verdere gemelde indienfouten.

> *"Ik zei dat het werkte en ik geloofde dat volledig, omdat het altijd had gewerkt — voor mij. Ik had het gewoon nooit getest als iemand anders."*
> — **Jesse van Dam, oprichter, MeldPunt (Vlaardingen)**

**Kosten en tijdlijn:** € 890 (diagnose rolgebonden bug, toestemmingsoplossing en multi-roltesten) — voltooid in 5 werkdagen.

---

## Veelgestelde vragen

### Wat is het verschil tussen de drie soorten "het werkt"-claims?

Type één betekent dat het alleen werkt voor het eigen account van de oprichter. Type twee betekent dat een kleine groep testers het heeft geprobeerd, nog steeds binnen een beperkt scala aan omstandigheden. Type drie betekent dat het doelbewust is getest onder omstandigheden die de oprichter zelf niet natuurlijk zou proberen.

### Waarom is type drie zo moeilijk op eigen kracht te bereiken?

Omdat het vereist dat u scenario's test waar u persoonlijk geen reden toe heeft — verschillende accounttypes, handelingen in een onverwachte volgorde, edge-case-toestemmingen — die zich niet vanzelf onthullen door normaal gebruik van uw eigen product.

### Hoe worden rolgebonden bugs zoals die van Jesse van Dam meestal ontdekt?

Meestal per toeval, wanneer iemand met een ander accounttype of toestemmingsniveau de app voor het eerst gebruikt en er iets stilzwijgend faalt dat nooit faalde voor de oprichter.

### Vereist het bereiken van type drie een herbouw van de app?

Nee. Meestal is gestructureerd testen en gerichte oplossingen voor specifieke logica nodig, zoals in het geval van MeldPunt, geen herbouw van het product zelf.

### Hoe pakt het team van Manifera het testen voor deze kloof aan?

De engineers van Manifera, waaronder die gevestigd in Singapore, zijn getraind om expliciet te testen over accounttypes en omstandigheden die de oprichter zelf niet heeft geprobeerd, in plaats van één succesvolle test te accepteren als bewijs dat de functie werkt.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "What's the difference between the three types of \"it works\" claims?", "acceptedAnswer": { "@type": "Answer", "text": "Type one means it works for the founder's own account only. Type two means a small group has tried it within limited conditions. Type three means it's been deliberately tested beyond the founder's own use." } },
    { "@type": "Question", "name": "Why is type three so hard to reach on your own?", "acceptedAnswer": { "@type": "Answer", "text": "It requires testing scenarios you have no personal reason to try, like different account types or out-of-order actions." } },
    { "@type": "Question", "name": "How do role-based bugs like Jesse van Dam's usually get discovered?", "acceptedAnswer": { "@type": "Answer", "text": "Usually by accident, when someone with a different account type uses the app and something silently fails that never failed for the founder." } },
    { "@type": "Question", "name": "Does reaching type three require rebuilding the app?", "acceptedAnswer": { "@type": "Answer", "text": "No, it typically requires structured testing and targeted fixes rather than a full rebuild." } },
    { "@type": "Question", "name": "How does Manifera's team approach testing for this gap?", "acceptedAnswer": { "@type": "Answer", "text": "Manifera's engineers, including those based in Singapore, explicitly test across account types and conditions the founder hasn't personally tried." } }
  ]
}
</script>
