---
Titel: "Beveiliging van AI-gegenereerde code: Externe scripts, widgets en de gegevens van uw klanten"
Trefwoorden: beveiliging ai-gegenereerde code, externe scripts widgets, content security policy, subresource integrity, chatwidget privacy, LaunchStudio, Manifera
Koperfase: Overweging
Doelgroep: Technische Solo-Oprichter / Indie Hacker
---

# Beveiliging van AI-gegenereerde code: Externe scripts, widgets en de gegevens van uw klanten

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Beveiliging van AI-gegenereerde code: Externe scripts, widgets en de gegevens van uw klanten",
  "description": "Chatwidgets, analysetags, heatmaps en ingesloten tools draaien met volledige toegang tot uw webpagina's. Dit artikel behandelt de risico's voor beveiliging en privacy van externe scripts in door AI gebouwde apps - datalekken, supply chain-aanvallen en toestemming - en hoe u controle houdt via CSP, SRI en een scriptinventaris.",
  "author": { "@type": "Organization", "name": "LaunchStudio", "url": "https://launchstudio.eu/nl/" },
  "publisher": { "@type": "Organization", "name": "Manifera", "url": "https://www.manifera.com" },
  "datePublished": "2027-12-29",
  "inLanguage": "nl-NL",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://launchstudio.eu/nl/blog/ai-generated-code-security-third-party-scripts-widgets-and-your-customers-data" }
}
</script>

"Voeg een chatwidget toe." "Voeg Google Analytics toe." "Voeg een heatmaptool toe zodat ik zie waar mensen klikken." Elk is een prompt van één regel, en AI-codeertools reageren door een scripttag in de lay-out van uw app te plakken - op elke pagina, ook op de pagina's waar klanten hun adres typen, documenten uploaden of betaalgegevens invoeren. Scripts van derden zijn een stille hoek van de beveiliging van AI-gegenereerde code: code die u niet zelf schreef, van bedrijven die u nauwelijks kent, die met dezelfde toegang tot uw pagina's draait als uw eigen code.

## Wat een Script van Derden Kan Doen

Een script dat in uw pagina wordt geladen, kan technisch gezien:

- Alles op de pagina lezen, inclusief formuliervelden terwijl gebruikers typen.
- Cookies en opslag lezen waartoe JavaScript toegang heeft.
- Data naar zijn eigen servers sturen.
- De pagina wijzigen - inhoud invoegen, gebruikers doorsturen, formulieren aanpassen.

Gerenommeerde aanbieders misbruiken dit niet bewust. Maar hun scripts kunnen meer verzamelen dan u bedoelt (tools voor sessie-opname die formulierinvoer vastleggen, bijvoorbeeld), en aanbieders kunnen worden gecompromitteerd: verschillende bekende supply-chainaanvallen injecteerden code om kaartgegevens af te vangen in veelgebruikte scripts, met gevolgen voor elke site die ze laadde.

## De Risico's voor de Beveiliging van AI-Gegenereerde Code, Concreet

**Datalekken.** Tools voor heatmaps en sessie-opname kunnen vastleggen wat gebruikers typen, tenzij ze zijn ingesteld om invoer te maskeren. Analyticstags kunnen persoonsgegevens in URL's of paginatitels oppikken. Chatwidgets ontvangen alles wat gebruikers erin plakken.

**Supply-chaincompromittering.** Wordt een script van een server van derden geladen en wordt die server gecompromitteerd, dan draait de code van de aanvaller op uw pagina's.

**Privacy en toestemming.** Veel trackingscripts vereisen onder EU-regels voorafgaande toestemming. AI-gegenereerde opzetten laden ze meestal direct, vóór welke toestemmingsbanner dan ook.

**Prestaties.** Elk script voegt gewicht en verzoeken toe, wat de laadsnelheid en de Core Web Vitals beïnvloedt.

**Wildgroei.** Na maanden prompten laden apps vaak scripts die niemand zich herinnert te hebben toegevoegd, ook van tools die niet meer worden gebruikt.

## Maatregel 1: Houd een Inventaris Bij

Maak een lijst van elk script van derden, wat het doet, welke pagina's het laden, tot welke data het toegang heeft, of het toestemming vereist en wie het heeft goedgekeurd. Verwijder alles wat niet wordt gebruikt.

## Maatregel 2: Laad Scripts Alleen Waar Nodig

Een chatwidget hoeft niet op de betaalpagina te draaien. Analytics hoeft niet in het beheergedeelte te draaien. Beperk scripts tot de pagina's waar ze een doel dienen, en houd ze weg van pagina's met gevoelige invoer.

## Maatregel 3: Respecteer Toestemming

Laad analytics-, marketing- en sessie-opnamescripts waar vereist pas na toestemming, met een even makkelijke optie om te weigeren. Overweeg privacyvriendelijke analytics die voor basismetingen mogelijk geen toestemming vereisen.

## Maatregel 4: Configureer Tools Privacybewust

Maskeer alle formulierinvoer in tools voor sessie-opname, schakel het opslaan van IP-adressen waar mogelijk uit, stuur geen persoonsgegevens mee in URL's of events, kies dataregio's in de EU en sluit verwerkersovereenkomsten af.

## Maatregel 5: Content Security Policy

Een Content Security Policy-header (CSP) vertelt de browser welke bronnen scripts mogen uitvoeren en waarheen data mag worden gestuurd. Die beperkt de schade van zowel geïnjecteerde scripts als gecompromitteerde derden. Begin in de modus report-only, scherp geleidelijk aan en vermijd brede uitzonderingen zoals `unsafe-inline` waar dat kan.

## Maatregel 6: Subresource Integrity of Zelf Hosten

Voor scripts die in vaste versies van CDN's worden geladen, zorgen Subresource Integrity-hashes (SRI) ervoor dat de browser alleen het exacte bestand uitvoert dat u hebt goedgekeurd. Voor scripts die voortdurend veranderen (veel tags van leveranciers) is SRI niet praktisch; beperk dan waar ze laden en vertrouw op CSP.

## Maatregel 7: Isoleer Gevoelige Flows

Betaalgegevens horen te worden ingevoerd in de gehoste velden of checkoutpagina van de betaalaanbieder, niet in uw eigen formulieren, zodat zelfs een gecompromitteerd script op uw pagina geen kaartnummers kan lezen.

## Een Inventaris van Scripts van Derden Opbouwen

Het beheersen van de risico's van externe scripts voor de beveiliging van AI-gegenereerde code begint met een volledige inventaris:

| Script | Doel | Pagina's | Data waartoe het toegang heeft | Toestemming nodig? | Eigenaar | Houden? |
| --- | --- | --- | --- | --- | --- | --- |
| Analyticstag | Verkeer meten | Alle | Pagina-URL's, interacties | Afhankelijk van tool/configuratie | Marketing | Vervangen door privacyvriendelijke optie |
| Advertentiepixel | Conversies volgen | Alle | Pagina-URL's, events | Ja | Marketing | Alleen op marketingpagina's, na toestemming |
| Chatwidget | Support | Alle | Chatinhoud, paginacontext | Meestal niet voor de supportfunctie | Support | Beperken tot supportpagina's |
| Sessie-opname | UX-onderzoek | Alle | Alles wat wordt getypt en aangeklikt | Ja | Product | Verwijderen uit het portaal |
| Kaartbibliotheek | Locaties tonen | Bestemmingspagina's | Locatiezoekopdrachten | Afhankelijk | Product | Houden, waar mogelijk zelf hosten |

Open om hem op te bouwen de pagina's van uw site met het netwerkpaneel van de browser, maak een lijst van elk extern domein dat scripts laadt, en controleer in uw code en tagmanager wat ze laadt. De kolom "Houden?" wordt uw actielijst.

## Tagmanagers: Handig en Riskant

Met tagmanagers kunnen marketeers scripts toevoegen zonder deployments. Dat gemak betekent ook dat scripts zonder review door engineers op gevoelige pagina's kunnen verschijnen. Gebruikt u er een, beperk dan wie wijzigingen mag publiceren, sluit gevoelige pagina's (checkout, account, formulieren met persoonsgegevens) via regels uit, vereis toestemmingsvoorwaarden voor trackingtags, controleer gepubliceerde wijzigingen maandelijks en neem de tagmanager zelf mee in de planning van uw Content Security Policy.

## Een Content Security Policy voor Echte Sites

Een Content Security Policy wordt als header meegestuurd en vertelt de browser vanaf welke bronnen scripts mogen worden geladen, met welke servers verbinding mag worden gemaakt, welke frames mogen worden getoond, enzovoort. Een startpunt voor veel AI-gebouwde apps:

```
Content-Security-Policy:
  default-src 'self';
  script-src 'self' https://js.stripe.com https://plausible.io;
  connect-src 'self' https://api.stripe.com https://your-project.supabase.co https://plausible.io;
  frame-src https://js.stripe.com;
  img-src 'self' data: https:;
  style-src 'self' 'unsafe-inline';
  frame-ancestors 'none';
  report-uri /csp-report
```

Zet hem eerst live met `Content-Security-Policy-Report-Only`, verzamel een week lang meldingen van overtredingen, pas de toegestane bronnen aan en dwing hem daarna af. Vermijd `unsafe-inline` voor scripts; gebruik nonces of hashes als inline scripts onvermijdelijk zijn.

## Subresource Integrity voor Vaste Bibliotheken

Laadt u een specifieke versie van een bibliotheek van een CDN, voeg dan een attribuut `integrity` toe met de hash van het bestand. De browser weigert het bestand uit te voeren als het is gewijzigd. Dat beschermt tegen gecompromitteerde CDN's voor bestanden met een vaste versie. Voor scripts die voortdurend veranderen - de meeste tags van leveranciers - kan SRI niet worden gebruikt; daar zijn het beperken van pagina's en CSP de belangrijkste verdediging, en is zelf hosten van stabiele bibliotheken vaak de betere keuze.

## Betaalpagina's Verdienen een Speciale Behandeling

Betaalpagina's zijn een geliefd doelwit voor skimmingaanvallen via gecompromitteerde scripts van derden. Houd ze zo schoon mogelijk: geen analytics- of marketingtags, geen chatwidgets, een strikte CSP en het invoeren van kaartgegevens volledig afgehandeld door de gehoste velden of checkoutpagina van de betaalaanbieder. Eisen uit de betaalkaartindustrie richten zich steeds meer op het beheersen van scripts op betaalpagina's; door gehoste betaalcomponenten te gebruiken, blijft het grootste deel van die last bij de aanbieder.

## Toestemmingsbeheer dat Technisch Werkt

Toestemming moet bepalen wat er laadt, niet alleen wat er wordt getoond. Een consentmanager hoort niet-essentiële scripts te blokkeren tot er toestemming is, de keuze vast te leggen met een tijdstempel, gebruikers die later te laten wijzigen, en de toestemmingsstatus door te geven aan scripts die dat ondersteunen. Test door uw site vers te laden, toestemming te weigeren en het netwerkpaneel te controleren: er mogen geen trackingverzoeken verschijnen.

## Due Diligence bij Leveranciers

Vraag u vóór het toevoegen van een script van derden af: welke data ontvangt het, waar wordt die verwerkt, biedt de leverancier een verwerkersovereenkomst, hoe wordt het script geleverd en beveiligd, kan het alleen worden geladen waar het nodig is, en bestaat er een privacyvriendelijker alternatief? Leg de antwoorden vast in de inventaris. Dit kost per leverancier een paar minuten en voorkomt veel toekomstige problemen.

## Zelf Hosten Waar Praktisch

Sommige bronnen van derden kunnen zelf worden gehost in plaats van bij leveranciers te worden geladen: lettertypen, iconensets, stabiele JavaScript-bibliotheken en sommige analyticstools. Zelf hosten haalt een afhankelijkheid van een andere server tijdens het draaien weg, voorkomt dat IP-adressen van bezoekers naar derden worden gestuurd (een punt dat sommige Europese toezichthouders en rechters hebben opgebracht, vooral bij weblettertypen) en vereenvoudigt de Content Security Policy. Houd zelf gehoste bibliotheken bij via uw gewone proces voor afhankelijkheden.

## Prestatievoordelen van Minder Scripts

Elk script van derden voegt netwerkverzoeken toe, JavaScript dat moet worden verwerkt en vaak extra scripts die het zelf laadt. Niet-essentiële scripts verwijderen of uitstellen verbetert Interaction to Next Paint en Largest Contentful Paint vaak merkbaar, vooral op telefoons uit het middensegment. Laad de overgebleven scripts met `async` of `defer`, stel chatwidgets uit tot de gebruiker interactie heeft, en meet het verschil met real-user monitoring. Beveiliging, privacy en prestaties verbeteren samen.

## Monitoren op Onverwachte Scripts

Scripts kunnen verschijnen zonder dat iemand het merkt - via een wijziging in de tagmanager, een gecompromitteerde afhankelijkheid of een leverancier die extra scripts laadt. Monitor met CSP-meldingen van overtredingen (die pogingen tonen om niet-goedgekeurde bronnen te laden), periodieke geautomatiseerde scans van belangrijke pagina's met een lijst van geladen domeinen, en meldingen als er een nieuw domein verschijnt. Behandel op betaal- en accountpagina's elk onverwacht script als een te onderzoeken incident.

## Wat U Gebruikers Vertelt

Uw privacyverklaring hoort de diensten van derden te noemen die data van bezoekers ontvangen, met hun doelen en locaties, en uw informatie over cookies of toestemming hoort overeen te komen met wat er werkelijk laadt. Transparantie is hier zowel een wettelijke eis als een vertrouwenssignaal: gebruikers controleren steeds vaker welke trackers een site gebruikt, en browserextensies maken dat zichtbaar.

## Een Checklist voor Scripts van Derden

Vóór de lancering: inventaris compleet met eigenaren en doelen; ongebruikte scripts verwijderd; scripts beperkt tot de pagina's die ze nodig hebben; niets niet-essentieels op betaal- of accountpagina's; toestemmingsblokkering getest; sessie-opname gemaskeerd of uit gevoelige flows verwijderd; Content Security Policy afgedwongen na een periode in report-only; SRI of zelf hosten voor vaste bibliotheken; toegang tot de tagmanager beperkt; privacyverklaring in overeenstemming met de werkelijkheid. Met deze stappen is de code die u niet zelf schreef niet langer het zwakste deel van uw app.

## Eerste Stap

Open uw checkout- of accountpagina, bekijk het netwerkpaneel en tel de externe domeinen die scripts laden. Elk domein dat u niet kunt verklaren, is een vraag om deze week te beantwoorden.

## Waarom Dit een AI-Specifiek Risico Is

AI-codeertools voegen opmerkelijk gemakkelijk scripts van derden toe: vraag om analytics, een chatwidget of een kaart, en er verschijnt een scripttag in de globale lay-out, geladen op elke pagina, zonder afhandeling van toestemming of beperkingen. Over maanden prompten stapelen ze zich op. Niemand besloot paspoortnummers naar een leverancier van sessie-opname te sturen; het gebeurde omdat een behulpzame tool overal een fragment toevoegde. Daarom verdienen scripts van derden een plek in elke productiereview van AI-gebouwde apps - en daarom zijn een inventaris, beperking per pagina, toestemmingsblokkering en een Content Security Policy het waard om vóór de lancering in te richten in plaats van na een ongemakkelijke vraag van een klant of toezichthouder.

## Onthoud

Elk script dat u laadt, handelt met uw gezag op de pagina's van uw gebruikers. Laad alleen wat u nodig hebt, alleen waar u het nodig hebt, en alleen nadat gebruikers ermee instemmen als toestemming vereist is.

## Waar LaunchStudio Past

LaunchStudio beoordeelt scripts van derden als onderdeel van zijn controles op beveiliging en privacy: inventaris en opschoning, beperking per pagina, laden na toestemming, privacybewuste configuratie, een Content Security Policy afgestemd op uw app en isolatie van betalingen. LaunchStudio wordt aangedreven door Manifera, wiens CEO Herre Roelevink een achtergrond in cybersecurity heeft - inclusief werk aan dark-webmonitoring met TNO - die een zorgvuldige kijk op supply-chainrisico's vormt. De engineers van Manifera werken vanuit Ho Chi Minh-stad, met klantcontact via Amsterdam en Singapore. Zie [de over-ons-pagina van Manifera](https://www.manifera.com/about-us/); [de CSP-gids van MDN](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CSP) is de helderste inleiding.

[Stuur ons de link naar uw site](https://launchstudio.eu/nl/#contact) en we maken een lijst van elk script dat hij laadt.

## Praktijkvoorbeeld

### Een AI-Native Oprichter in Actie: Een Portaal van een Reisbureau met Elf Ongenode Gasten

Yara Ouali, eigenaar van een klein reisbureau in Leidschendam dat gespecialiseerd is in reizen op maat, bouwde Reisdossier in Bolt: een klantportaal waarin reizigers passagiersgegevens invullen, paspoortscans uploaden, reisschema's bekijken, termijnen betalen en chatten met hun reisadviseur. Ongeveer 1.100 reizigers gebruikten het.

Tijdens een privacyreview op verzoek van een partner-touroperator bleek het portaal op elke pagina elf scripts van derden te laden: analytics, twee advertentiepixels, een heatmaptool met sessie-opname, een chatwidget, een reviewwidget, een lettertypedienst, een kaartbibliotheek en drie scripts van tools die Yara niet meer gebruikte. De tool voor sessie-opname legde namen, geboortedata en paspoortnummers van passagiers vast terwijl reizigers ze typten. Alle scripts laadden vóór de cookiebanner. Het termijnformulier verzamelde kaartgegevens in de eigen velden van het portaal voordat het ze doorgaf aan de betaalaanbieder. Er was geen Content Security Policy.

In zes werkdagen verwijderden de engineers van LaunchStudio zes ongebruikte of overbodige scripts, beperkten ze de chatwidget en de reviewwidget tot pagina's zonder persoonlijke formulieren, verplaatsten ze analytics naar een privacyvriendelijke optie met hosting in de EU en laadden ze advertentiepixels alleen na toestemming en nooit op portaalpagina's, haalden ze sessie-opname uit het portaal en lieten ze opgenomen sessies bij de leverancier verwijderen, schakelden ze termijnbetalingen over op de gehoste checkout van Mollie, en zetten ze een Content Security Policy live - eerst in report-only, daarna afgedwongen.

**Resultaat:** De partner-touroperator keurde het portaal goed. De laadtijd van het passagiersformulier halveerde, en Yara keurt nu elk nieuw script goed aan de hand van een inventaris van één pagina.

> *"Ik had elf bedrijven uitgenodigd in de ruimte waar mijn klanten hun paspoortnummers typten. De meeste was ik vergeten."*
> - **Yara Ouali, Oprichter, Reisdossier (Leidschendam)**

**Kosten & Tijdlijn:** € 1.500 (Launch Ready-pakket: inventaris en opschoning van scripts, laden na toestemming, isolatie van betalingen en CSP) - afgerond in 6 werkdagen.

## Veelgestelde Vragen

### Zijn scripts van derden een beveiligingsrisico?

Ze draaien met volledige toegang tot uw pagina's, dus ze kunnen via een verkeerde configuratie data lekken en een aanvalsroute worden als hun aanbieder wordt gecompromitteerd. Een inventaris, beperking en een Content Security Policy verkleinen het risico.

### Kunnen tools voor sessie-opname persoonsgegevens vastleggen?

Ja, inclusief wat gebruikers typen, tenzij invoer wordt gemaskeerd. Houd ze weg van pagina's met gevoelige data en stel maskering overal in.

### Hebben analyticsscripts in de EU toestemming nodig?

Veel wel, vooral scripts die cookies of identificatoren voor tracking gebruiken. Laad ze pas na toestemming, of gebruik privacyvriendelijke analytics die voor basismetingen mogelijk geen toestemming vereisen.

### Hoe beoordeelt Manifera supply-chainrisico's in webapps?

Door elk extern script en elke afhankelijkheid als onderdeel van het aanvalsoppervlak te behandelen - een aanpak gevormd door de cybersecurityachtergrond van Herre Roelevink - en te beperken waartoe elk toegang heeft.

### Helpen minder scripts van derden bij SEO?

Meestal wel. Minder scripts betekenen snellere pagina's en betere Core Web Vitals, wat posities ondersteunt en pagina's makkelijker maakt voor zoekmachines en AI-assistenten om te verwerken.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    { "@type": "Question", "name": "Zijn scripts van derden een beveiligingsrisico?", "acceptedAnswer": { "@type": "Answer", "text": "Ja; ze hebben volledige toegang tot de pagina. Een inventaris, beperking en CSP verkleinen het risico." } },
    { "@type": "Question", "name": "Kunnen tools voor sessie-opname persoonsgegevens vastleggen?", "acceptedAnswer": { "@type": "Answer", "text": "Ja, tenzij invoer wordt gemaskeerd; houd ze weg van gevoelige pagina's." } },
    { "@type": "Question", "name": "Hebben analyticsscripts in de EU toestemming nodig?", "acceptedAnswer": { "@type": "Answer", "text": "Veel wel; laad ze na toestemming of gebruik privacyvriendelijke analytics." } },
    { "@type": "Question", "name": "Hoe beoordeelt Manifera supply-chainrisico's in webapps?", "acceptedAnswer": { "@type": "Answer", "text": "Elk extern script wordt behandeld als aanvalsoppervlak en in toegang beperkt." } },
    { "@type": "Question", "name": "Helpen minder scripts van derden bij SEO?", "acceptedAnswer": { "@type": "Answer", "text": "Meestal wel, via snellere pagina's en betere Core Web Vitals." } }
  ]
}
</script>
