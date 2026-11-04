---
Titel: "Kan Ik Mijn Lovable-App in de App Store Publiceren? Capacitor versus PWA"
Trefwoorden: lovable app in app store, lovable capacitor, lovable pwa, lovable ios app, LaunchStudio, Manifera
Koperfase: Overweging
Doelgroep: AI-Native Oprichter (Niet-Technisch)
---

# Kan Ik Mijn Lovable-App in de App Store Publiceren? Capacitor versus PWA

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Kan Ik Mijn Lovable-App in de App Store Publiceren? Capacitor versus PWA",
  "description": "Lovable bouwt webapps, maar u kunt telefoons toch bereiken: als Progressive Web App of verpakt met Capacitor voor de App Store en Google Play. Deze gids legt beide routes uit, de beoordelingsregels van Apple en wat het kost.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2028-02-02",
  "inLanguage": "nl-NL",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/can-i-publish-my-lovable-app-to-the-app-store" },
  "citation": [
    { "@type": "CreativeWork", "name": "Apple App Store Review Guidelines: Minimum Functionality", "url": "https://developer.apple.com/app-store/review/guidelines/#minimum-functionality" },
    { "@type": "CreativeWork", "name": "Capacitor documentation", "url": "https://capacitorjs.com/docs" },
    { "@type": "CreativeWork", "name": "web.dev: What are Progressive Web Apps?", "url": "https://web.dev/articles/what-are-pwas" },
    { "@type": "CreativeWork", "name": "WebKit: Web Push for Web Apps on iOS and iPadOS", "url": "https://webkit.org/blog/13878/web-push-for-web-apps-on-ios-and-ipados/" }
  ]
}
</script>

**Kort antwoord:** ja, maar niet rechtstreeks. Lovable bouwt webapps, geen native iOS- of Android-apps. U heeft twee routes naar telefoons: maak van uw Lovable-app een **Progressive Web App (PWA)** die gebruikers vanuit de browser installeren, of verpak hem met **Capacitor** om een echte app in de Apple App Store en Google Play te publiceren. Een PWA is sneller en goedkoper. Met Capacitor komt u in de stores, maar Apple wijst een gewone website in een verpakking af, dus de app heeft echte app-achtige functies nodig.

## Belangrijkste Punten

- **Lovable bouwt webapps, geen native apps,** maar u kunt telefoons toch bereiken: als Progressive Web App die vanuit de browser wordt geïnstalleerd, of verpakt met Capacitor voor de App Store en Google Play.
- **PWA's zijn sneller en goedkoper,** worden direct bijgewerkt en ondersteunen pushmeldingen op de iPhone zodra ze aan het beginscherm zijn toegevoegd, een mogelijkheid die Apple in iOS 16.4 toevoegde.
- **Richtlijn 4.2 van Apple (Minimum Functionality) wijst "websites in een doosje" af.** Een verpakte Lovable-app heeft echte app-waarde nodig, zoals pushmeldingen, apparaatfuncties of offline gebruik.
- **De backend moet eerst productierijp zijn,** omdat een mobiele appbundel elke sleutel of zwakke toegangsregel net zo blootstelt als een website.
- **Mobiele lanceringen kosten met LaunchStudio doorgaans €3.000-€7.500,** inclusief indiening bij de stores; een PWA toegevoegd aan een weblancering kost veel minder.

## Route 1: Progressive Web App

Een PWA is uw Lovable-webapp met een manifest en een service worker, zodat gebruikers hem "aan het beginscherm toevoegen" en openen als een app.

**Wat goed werkt:**
- Een schermvullende ervaring met uw pictogram op het beginscherm
- Offline caching van de interface
- Pushmeldingen, ook op iOS voor webapps die aan het beginscherm zijn toegevoegd (ondersteund sinds iOS 16.4)
- Eén codebase, updates direct zonder beoordeling door een app store

**Beperkingen:**
- Geen vermelding in de Apple App Store; gebruikers moeten u via uw website vinden
- Installeren op de iPhone is minder vanzelfsprekend voor gebruikers (Deel, daarna "Zet op beginscherm")
- Beperkte toegang tot sommige apparaatfuncties vergeleken met native apps

**Gangbare kosten:** een paar honderd euro bovenop het productiewerk, vaak onderdeel van een lanceringsopdracht.

## Route 2: Verpakken met Capacitor

Capacitor, gemaakt door het team van Ionic, verpakt uw webapp in een native iOS- en Android-schil. De app draait uw Lovable-code in een webview, met plug-ins voor native functies zoals pushmeldingen, camera, biometrie en in-app-aankopen.

**Wat goed werkt:**
- Echte vermeldingen in de App Store en Google Play
- Toegang tot native functies via plug-ins
- Dezelfde Lovable-codebase drijft web en mobiel aan

**Vereisten en beperkingen:**
- Een Apple Developer-account (€99 per jaar) en een ontwikkelaarsaccount voor Google Play (eenmalige kosten)
- Een Mac met Xcode om de iOS-app te bouwen
- Elke update van de native configuratie gaat door de beoordeling van de store
- De beoordelingsrichtlijnen van Apple gelden volledig

## Het Probleem met de Beoordeling door Apple

Richtlijn 4.2 van de App Store Review Guidelines, Minimum Functionality, zegt dat een app niet simpelweg een opnieuw verpakte website mag zijn. Apps die "een website in een doosje" zijn, worden regelmatig afgewezen. Om door de beoordeling te komen, heeft een verpakte Lovable-app meestal minstens een deel hiervan nodig:

- Native pushmeldingen die echte waarde toevoegen
- Apparaatfuncties zoals camera, biometrie of offline gebruik
- Een gebruikerservaring die voor mobiel is ontworpen, niet een desktoplay-out die op een telefoon is geperst
- Inhoud of functionaliteit die zinvol werkt binnen de app

Andere veelvoorkomende redenen voor afwijzing van verpakte apps: inloggen verplicht zonder demo-account voor beoordelaars, kapotte links naar het web, en digitale abonnementen die buiten de in-app-aankopen van Apple worden verkocht waar de regels van Apple dat vereisen. De betaalregels voor digitale goederen verschillen per regio en blijven veranderen, dus controleer de actuele richtlijnen voordat u beslist hoe u in de app rekent.

## Welke Route Kiest U?

| Situatie | Betere route |
| --- | --- |
| B2B-tool die aan een bureau en af en toe op een telefoon wordt gebruikt | PWA |
| Consumenten verwachten u in de App Store te vinden | Capacitor |
| U heeft pushmeldingen op de iPhone nodig | Beide, een PWA werkt als hij is geïnstalleerd |
| U heeft camera, biometrie of diepe native functies nodig | Capacitor |
| Het budget is krap en u wilt de vraag naar mobiel testen | Eerst een PWA |
| U verkoopt digitale abonnementen aan consumenten | Plan de betaalregels zorgvuldig met Capacitor |

Veel oprichters beginnen met een PWA, meten hoeveel gebruikers hem installeren, en stappen over op Capacitor zodra de vraag naar mobiel is bewezen.

## Hoe een PWA Werkt Onder de Motorkap

Een Progressive Web App is een website met drie toevoegingen, zoals web.dev van Google uitlegt: een web app manifest dat het apparaat vertelt hoe de app moet worden weergegeven (naam, pictogrammen, kleuren, schermvullende modus), een service worker die bestanden kan cachen en achtergrondtaken zoals pushmeldingen kan afhandelen, en HTTPS. Samen laten ze gebruikers de site "installeren" op hun beginscherm en openen als een app. Voor een Lovable-app is dit afgebakend werk: pictogrammen genereren, het manifest schrijven, een service worker met een verstandige cachingstrategie toevoegen en installatie op iOS en Android testen.

De cachingstrategie is belangrijk. De app-shell cachen (HTML, JavaScript, CSS, pictogrammen) laat de app direct openen en kort offline werken. API-antwoorden cachen vraagt meer zorg, omdat verouderde data gebruikers in verwarring kan brengen of informatie kan tonen die ze niet meer zouden mogen zien. Voor de meeste apps cachet u de shell en haalt u data vers op, met duidelijke meldingen als het apparaat offline is.

## Pushmeldingen op de iPhone

Jarenlang was het ontbreken van web push op iOS het belangrijkste argument tegen PWA's. Sinds iOS 16.4 ondersteunt WebKit pushmeldingen voor webapps die de gebruiker aan zijn beginscherm heeft toegevoegd. Dat verandert de rekensom voor veel oprichters: herinneringen, boekingsbevestigingen en statusupdates kunnen iPhone-gebruikers nu bereiken zonder app in de App Store. De keerzijde is vindbaarheid: gebruikers moeten de app eerst aan hun beginscherm toevoegen, en dat vraagt om een duidelijke uitnodiging en instructies.

## Hoe Capacitor Werkt

Capacitor, onderhouden door het team van Ionic, verpakt uw webapp in een native iOS- en Android-project. Uw Lovable-code draait in een native webview, en de plug-ins van Capacitor maken apparaatfuncties via JavaScript beschikbaar: camera, locatie, pushmeldingen, biometrie, bestandssysteem, haptiek en meer. Omdat dezelfde code de web- en mobiele versie aandrijft, onderhoudt u geen twee codebases. De native projecten staan in uw repository naast de webcode en worden gebouwd met Xcode voor iOS en Android Studio voor Android.

## Door de Beoordeling van Apple Komen in de Praktijk

De beoordelingsrichtlijnen van Apple zijn openbaar, en richtlijn 4.2 over minimale functionaliteit is degene waarover de meeste verpakte apps struikelen. Beoordelaars zoeken naar apps die meer bieden dan een mobiele website. Praktische manieren om die lat te halen:

- **Native pushmeldingen** met echte waarde, zoals herinneringen, statuswijzigingen of berichten
- **Integratie met het apparaat**, zoals de camera voor scannen of uploaden, locatie voor inchecken, of biometrie voor inloggen
- **Offline ondersteuning** voor kerninhoud
- **Navigatie die voor mobiel is ontworpen**, met patronen die native aanvoelen in plaats van desktopmenu's
- **Een complete ervaring in de app,** zonder gebruikers voor kerntaken naar de website te sturen

Andere veelvoorkomende redenen voor afwijzing zijn makkelijker te vermijden: lever een demo-account als inloggen verplicht is, leg functies uit in de notities voor de beoordeling, voeg een URL van het privacybeleid toe, en zorg dat accountverwijdering in de app beschikbaar is als gebruikers accounts kunnen aanmaken, zoals Apple vereist.

## Betalingen in Mobiele Apps

Betalingen zijn het meest complexe beleidsgebied. Apple en Google hebben regels voor het verkopen van digitale goederen en diensten in apps, en die regels zijn de afgelopen jaren veranderd, deels door regelgeving zoals de Digital Markets Act van de EU. Fysieke goederen en diensten die buiten de app worden gebruikt, zoals boekingen of leveringen, kunnen over het algemeen gewone betaalproviders gebruiken. Digitale abonnementen kunnen, afhankelijk van uw regio en de actuele richtlijnen, onder de regels voor in-app-aankopen vallen. Controleer de nieuwste regels voordat u over uw mobiele verdienmodel beslist, en stem uw prijzen op web en in de app daarop af.

## Beveiligingsoverwegingen voor Verpakte Apps

Een mobiele appbundel kan worden uitgepakt. Alles erin - API-sleutels, endpoints, configuratie - moet als openbaar worden beschouwd, precies zoals in een browser. Dezelfde productieprincipes gelden: geheime sleutels alleen op de server, Row Level Security op elke tabel, kortlevende tokens en veilige opslag van sessiegegevens, waar mogelijk in de keychain van het platform. Mobiel voegt één overweging toe: app-updates hebben tijd nodig om gebruikers te bereiken, dus beveiligingsfixes in de backend zijn veel beter dan fixes die een nieuwe appversie vereisen.

## Onderhoud na de Lancering

Mobiele apps hebben doorlopende zorg nodig: updates van besturingssystemen, nieuwe schermformaten, updates van plug-ins, verlenging van certificaten voor pushmeldingen en opnieuw beoordelen wanneer u updates indient. Begroot een paar uur per maand, en houd uw web- en mobiele versie gelijk op door backendwijzigingen achterwaarts compatibel uit te rollen, want sommige gebruikers draaien weken lang oudere appversies.

## Google Play Is Meestal Eenvoudiger

De beoordeling van Google Play is over het algemeen minder streng voor verpakte webapps dan die van Apple, en Android ondersteunt ook Trusted Web Activities, waarmee een PWA met weinig native code in de Play Store kan verschijnen. Veel oprichters lanceren daarom eerst op Android, leren van vroege mobiele gebruikers en verfijnen de app voordat ze hem bij Apple indienen.

## Eerst de Vraag naar Mobiel Meten

Meet, voordat u investeert in apps voor de stores. Voeg uitnodigingen voor het installeren van de PWA toe en houd bij hoeveel gebruikers installeren, hoe vaak geïnstalleerde gebruikers terugkomen vergeleken met browsergebruikers, en welke functies ze op mobiel gebruiken. Als geïnstalleerde gebruikers een betekenisvol aandeel vormen en actiever zijn, is een app voor de stores de moeite waard. Als weinig gebruikers installeren, verbeter dan eerst de mobiele webervaring.

## Wat het Productiewerk Inhoudt

Voor beide routes moet de app eerst productierijp zijn: veilige toegang tot data, sleutels op de server, werkende authenticatie en een stabiele backend. Daarna:

- **PWA:** manifest, pictogrammen, service worker, offline strategie, inrichting van push, uitnodigingen om te installeren
- **Capacitor:** projectinrichting, native plug-ins, deep links, pushcertificaten, app-pictogrammen en splash screens, vermeldingen in de stores, demo-account voor beoordelaars en indiening

De prijscalculator van LaunchStudio noemt voor mobiele apps €3.000-€7.500, wat het traject van een Lovable-app door productie en in de stores dekt. Een PWA toegevoegd aan een weblancering kost aanzienlijk minder. Zie ons overzicht van [de productiekosten van Lovable](https://launchstudio.eu/nl/blog/how-much-does-it-cost-to-make-a-lovable-app-production-ready) voor de webkant.

## Wie Het Bouwt

LaunchStudio wordt ondersteund door Manifera, dat al 11+ jaar [mobiele apps ontwikkelt](https://www.manifera.com/services/mobile-app-development/) met React Native en Flutter, naast webprojecten voor klanten als Vodafone en Xpar Vision. Engineers in Ho Chi Minh City dienen regelmatig apps in bij de stores, gecoördineerd vanuit de kantoren van Manifera in Amsterdam en Singapore. Voor de eigen formulering van Apple, lees de [App Store Review Guidelines](https://developer.apple.com/app-store/review/guidelines/).

## Praktijkvoorbeeld

### Een AI-Native Oprichter in Actie: De Hardloopclubapp die Apple Twee Keer Afwees

Lien Vermeulen coördineert een hardloopclub in Eindhoven en bouwde Loopmaatje in Lovable: leden sluiten aan bij groepslopen, zien routes, checken in bij de start en volgen clubuitdagingen. Leden vroegen steeds om "de app", dus Lien vond een tutorial en verpakte haar Lovable-app zelf met Capacitor.

Apple wees hem twee keer af. De eerste afwijzing verwees naar richtlijn 4.2: de app was in feite de website. De tweede kwam omdat beoordelaars niet konden inloggen, omdat aanmelden een uitnodigingscode van de club vereiste. Intussen merkte Lien dat de servicesleutel van Supabase in de app was meegebundeld, waar iedereen hem eruit kon halen.

LaunchStudio maakte eerst de backend productierijp: sleutels verplaatst naar edge functions, Row Level Security per club en authenticatie met correcte sessieafhandeling. Daarna voegden engineers native functies toe die de app op een telefoon echt nuttig maakten: pushmeldingen bij wijzigingen van loopjes en afgelastingen door het weer, inchecken op basis van locatie bij het startpunt, en offline toegang tot routekaarten. Er werd een demo-account voor beoordelaars voorbereid, en de indiening bevatte notities die de native functies uitlegden.

**Resultaat:** Loopmaatje werd bij de volgende indiening goedgekeurd. Binnen drie maanden installeerden ongeveer 230 van de 310 leden van de club de app, en Lien bleef de interface in Lovable bijwerken, wat bij elke release in de app terechtkwam.

> *"Ik dacht dat het moeilijke deel het verpakken van de app was. Het moeilijke deel was er iets van maken wat Apple als een app beschouwde."*
> - **Lien Vermeulen, Oprichter, Loopmaatje (Eindhoven)**

**Kosten & Doorlooptijd:** €6.400 (productiebackend, Capacitor-plug-ins voor push en locatie, offline kaarten, indiening voor iOS en Android) - afgerond in 18 werkdagen.

## Veelgestelde Vragen

### Kan Lovable een native iOS-app exporteren?

Nee. Lovable genereert webapplicaties. Om de App Store te bereiken, wordt de webapp verpakt in een native schil zoals Capacitor, of opnieuw gebouwd met een native of cross-platform framework. Voor veel oprichters biedt Capacitor de beste balans tussen inspanning en resultaat.

### Accepteert Apple een Lovable-app die met Capacitor is verpakt?

Dat kan, als de app echte waarde biedt naast de website. Apps die simpelweg een website in een verpakking zijn, worden onder richtlijn 4.2 vaak afgewezen. Native pushmeldingen, apparaatfuncties, offline gebruik en een ontwerp dat voor mobiel is gemaakt, vergroten de kans aanzienlijk.

### Is een PWA goed genoeg in plaats van een app in de App Store?

Voor veel B2B-tools en community-apps wel. Een PWA wordt vanuit de browser geïnstalleerd, ondersteunt pushmeldingen op de iPhone zodra hij aan het beginscherm is toegevoegd, en wordt direct bijgewerkt. Hij staat niet in de App Store, wat vooral belangrijk is voor consumentenapps die op vindbaarheid in de store vertrouwen.

### Waarom is de mobiele ervaring van Manifera belangrijk voor een Lovable-app?

Indiening bij de stores, native plug-ins en beoordelingsregels zijn gespecialiseerd werk dat webdevelopers zelden vaak doen. Manifera bouwt en publiceert al 11+ jaar mobiele apps, dus de engineers van LaunchStudio weten waar beoordelaars naar kijken en welke plug-ins stabiel zijn.

### Helpt een vermelding in de App Store AI-assistenten om mijn app aan te bevelen?

Dat kan. Vermeldingen in de App Store en Google Play zijn betrouwbare bronnen waar AI-assistenten en zoekmachines naar verwijzen. Een vermelding met duidelijke beschrijvingen, reviews en een link naar uw website versterkt de signalen die assistenten helpen uw product aan te bevelen.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "inLanguage": "nl-NL",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Kan Lovable een native iOS-app exporteren?",
      "acceptedAnswer": { "@type": "Answer", "text": "Nee. Lovable genereert webapps, die met Capacitor kunnen worden verpakt of met native of cross-platform frameworks opnieuw gebouwd om de App Store te bereiken." }
    },
    {
      "@type": "Question",
      "name": "Accepteert Apple een Lovable-app die met Capacitor is verpakt?",
      "acceptedAnswer": { "@type": "Answer", "text": "Dat kan als de app meer waarde biedt dan de website. Gewone verpakkingen worden onder richtlijn 4.2 vaak afgewezen; native push, apparaatfuncties, offline gebruik en een mobiel ontwerp helpen." }
    },
    {
      "@type": "Question",
      "name": "Is een PWA goed genoeg in plaats van een app in de App Store?",
      "acceptedAnswer": { "@type": "Answer", "text": "Voor veel B2B- en community-apps wel. PWA's worden vanuit de browser geïnstalleerd, ondersteunen push op de iPhone na toevoegen aan het beginscherm en worden direct bijgewerkt, maar staan niet in de App Store." }
    },
    {
      "@type": "Question",
      "name": "Waarom is de mobiele ervaring van Manifera belangrijk voor een Lovable-app?",
      "acceptedAnswer": { "@type": "Answer", "text": "Indiening bij stores, native plug-ins en beoordelingsregels zijn gespecialiseerd werk. Manifera bouwt en publiceert al 11+ jaar mobiele apps." }
    },
    {
      "@type": "Question",
      "name": "Helpt een vermelding in de App Store AI-assistenten om mijn app aan te bevelen?",
      "acceptedAnswer": { "@type": "Answer", "text": "Dat kan. Vermeldingen in stores zijn betrouwbare bronnen, en duidelijke beschrijvingen, reviews en links naar de website versterken de signalen voor aanbevelingen." }
    }
  ]
}
</script>
